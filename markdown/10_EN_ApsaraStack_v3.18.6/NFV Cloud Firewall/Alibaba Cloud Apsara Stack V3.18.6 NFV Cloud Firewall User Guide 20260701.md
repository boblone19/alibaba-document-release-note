---
title: "NFV Cloud Firewall User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 205
source_pdf: "9bb787c89a516a43_Alibaba Cloud Apsara Stack V3.18.6 NFV Cloud Firewall User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-NFV%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20NFV%20Cloud%20Firewall%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# NFV Cloud Firewall User Guide 20260701

## Table of Contents

- 1 Usage notes
- 2 Getting started
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 NFV Cloud Firewall
  - 3.1 Firewalls
    - 3.1.1 Create a vFW cluster
    - 3.1.2 Create a disaster recovery vFW cluster
    - 3.1.3 View and log in to an ECS instance
    - 3.1.4 Create an endpoint for a vFW cluster
    - 3.1.5 Add a vFW route
    - 3.1.6 Quick bypass
    - 3.1.7 View details of a vFW cluster
  - 3.2 CIDR block management
    - 3.2.1 Create a CIDR block
    - 3.2.2 Manage CIDR blocks
  - 3.3 Route configuration
    - 3.3.1 Create a route
    - 3.3.2 Advertise and withdraw a route
    - 3.3.3 Manage routes
  - 3.4 Dedicated hosts
    - 3.4.1 Create a dedicated host group
    - 3.4.2 Manage dedicated host groups
  - 3.5 System settings
    - 3.5.1 Cross-organization resource authorization
    - 3.5.2 Workflows
  - 3.6 Best practices
    - 3.6.1 VPC-VPC protection within an organization by NFV Cloud Firewall in a single data center
    - 3.6.2 VPC-VPC protection across organizations by NFV Cloud Firewall in a single data center
    - 3.6.3 vSwitch-vSwitch protection within an organization by NFV Cloud Firewall in a single data center
    - 3.6.4 Configure the bypass and restoration features of NFV Cloud Firewall
    - 3.6.5 VPC-data center protection by NFV Cloud Firewall in a single data center

sage notes

## 1 Usage notes

This topic describes the usage notes for the Security Orchestration, Automation, and Response (SOAR) User Guide and the configuration requirements for the on-premises computer used to log on to Apsara Stack Security Center.

**User guide usage notes**

To integrate Apsara Stack security operations and response, the features of SOAR are integrated into Security Operations Center (SOC). The SOAR User Guide describes only the unique features of SOAR. For more information about the features of SOC, see the SOC User Guide.

**On-premises computer configuration requirements**

You can log on to Apsara Stack Security Center only when your on-premises computer meets the configuration requirements in Table 1. Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

etting started

## 2 Getting started

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. The roles available in Apsara Stack Security are all default roles. You cannot create custom roles. Before you log in to Apsara Stack Security, make sure that your account is assigned the required role. For more information, see the Default roles in Apsara Stack Security section of this topic. Table 1: Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| Organization security administrator | This role has the permissions to use Security Operations Center (SOC) to manage the security of hosts, applications, and networks for an organization. This role also has the permissions to manage security services related to Elastic Compute Service (ECS). |
| Global organization security administrator | This role has the permissions to use SOC to perform security management for Apsara Stack and all tenants and manage security services related to ECS. |
| Security auditor | This role has the permissions to audit the security of Apsara Stack. |
| Global organization security auditor | This role has the permissions to use SOC to check the security status of all organizations. |

If you do not have an account or a role, contact the administrator to create a user and assign a role to the user. For more information, see **Create a user** in **Apsara Uni-manager**
**Management Console User Guide**.

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. To configure the Cloud Security system, you must log on with a global organization security administrator account. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
etting started Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
> **Forgot password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

## 3 NFV Cloud Firewall

### 3.1 Firewalls

**Quotas on NFV Cloud Firewall**

In the upper-right corner of the **Firewalls** page, you can view the firewall capacity, which indicates the throughput of the firewall purchased for the site. You can configure quotas in Quota Management in the Apsara Uni-manager Management Console.

#### 3.1.1 Create a vFW cluster

This topic describes how to create a virtual firewall (vFW) cluster.

**Prerequisites**

A CIDR block is created. For more information, see Create a CIDR block. If your business needs to use dedicated hosts, you must create a dedicated host group. For more information, see Create a dedicated host group.

**Create a vFW cluster**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Click **Create Cluster**, configure all parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the application to which the custom cluster belongs. The name must be 1 to 128 characters in length. |
| VFW Cluster Name | Enter a name for the vFW cluster. The name must be 1 to 128 characters in length. |
| Organization | Select the organization to which the cluster belongs. |
| Resource Set | Select the resource set to which the cluster belongs. |

| Area | Select the region in which the cluster belongs. |
|---|---|
| Zone | Select a zone in which you want to create the cluster. |
| CIDR | Select the CIDR block that you created. |
| Deployment Type | Select a deployment mode for the cluster. Active-Standby: Two Elastic Compute Service (ECS) instances are created. Standalone: One ECS instance is created. |
| Dedicated Host | Select whether to deploy the cluster on a dedicated host. No: The cluster is deployed in shared cloud resources. You do not need to specify a dedicated host group or a dedicated host. This option is suitable for general-purpose business scenarios that do not require special compliance or performance isolation. Yes: The cluster is deployed on a dedicated host. You must select a dedicated host group and a dedicated host. This option is suitable for scenarios that require exclusive physical resources, high security compliance, or performance isolation. If you select Yes, make sure that a dedicated host is created. For more information, see Create a dedicated host and Create a dedicated host in a host group. |
| Network Type | Valid value: 25 G. |
| CPU Type | Valid values: Intel/X86 and HG/X86. |
| VFW Specifications | If CPU Type is set to Intel/X86, you can select 1Gbps, 2Gbps, 6Gbps, 12Gbps, or 24Gbps. If CPU Type is set to HG/X86, you can select 1Gbps, 2Gbps, 6Gbps, 12Gbps, or 16Gbps. |
| ECS Specification | Select an ECS instance type. |
| ECS Image ID | Select an ECS image ID. |
| Description | Enter a description for the cluster. The description can be 1 to 255 characters in length. |

#### 3.1.2 Create a disaster recovery vFW cluster

A disaster recovery (DR) cluster is a redundancy mechanism that prevents network failure and security risks caused by single points of failure (SPOF). This topic describes how to create a DR vFW cluster.

**Prerequisites**

A virtual firewall (vFW) cluster is created. For more information, see Create a vFW cluster.

**Create a DR vFW cluster**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the vFW cluster that you want to manage and click its name to go to the details page.
5. In the upper-right corner of the details page, click **Create Slave Cluster**, configure the
parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| VFW Cluster Name | Enter a name for the vFW cluster. The name can be 1 to 128 characters in length. |
| Zone | Select a zone in which you want to create the cluster. The DR cluster cannot be deployed in the same zone as the primary cluster. |
| Deployment Type | Select a deployment mode for the cluster. Active-Standby: Two Elastic Compute Service (ECS) instances are created. Standalone: Only one ECS instance is created. |
| Dedicated Host | Select whether to deploy the cluster on a dedicated host. No: The cluster is deployed in shared cloud resources. You do not need to specify a dedicated host group or a dedicated host. This option is suitable for general-purpose business scenarios that do not require special compliance or performance isolation. Yes: The cluster is deployed on a dedicated host. You must select a dedicated host group and a dedicated host. This option is suitable for scenarios that require exclusive physical resources, high security compliance, or performance isolation. If you select Yes, make sure that a dedicated host is created. For more information, see Create a dedicated host and Create a dedicated host in a host group. |
| Network Type | Valid value: 25 G. |
| CPU Type | Valid values: Intel/X86 and HG/X86. |
| ECS Specification | Select an ECS instance type. |

| ECS Image ID | Select an ECS image ID. |
|---|---|
| Description | Enter a description for the cluster. The description can be 1 to 255 characters in length. |

#### 3.1.3 View and log in to an ECS instance

This topic describes how to view and log in to an Elastic Compute Service (ECS) instance in a virtual firewall (vFW) cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the vFW cluster that you want to manage and click its name to go to the details page.
5. In the **ECS Info** section, view the details of the ECS instances.
6. Find the ECS instance that you want to view and click **Details** in the **Operation** column.
Then, you can view the method to log in to the ECS instance.
**VNC**: You can click **Click to get** to obtain the VNC password.
**Classic Network**: You can click **Create** to create a login method over the classic
network. You can create only one login method over the classic network.
**VPC Network**: You can click **Create** and select a vSwitch ID to create a login method
over a virtual private cloud (VPC). You can create only one login method over a VPC.

#### 3.1.4 Create an endpoint for a vFW cluster

An endpoint defines a security control node for inbound and outbound traffic. The node directs traffic to the virtual firewall (vFW) cluster for security detection and policy execution. This topic describes how to create an endpoint for a vFW cluster.

**Note**

The number of endpoints supported by a vFW cluster varies. The quota in the console prevails.

**Create an endpoint for a vFW cluster**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the vFW cluster that you want to manage and click its name to go to the details page.
5. In the **Endpoint** section, click **Create Endpoint**, configure the parameters, and then click
**OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the endpoint. The name can be 1 to 128 characters in length. The name is the unique identifier. |
| Organization | Select the organization to which the endpoint belongs. |
| Resource Set | Select the resource set to which the endpoint belongs. |
| Area | The current region is selected by default and cannot be changed. |
| Zone | The current zone is selected by default and cannot be changed. |
| IP Stack | Select an IP stack for the endpoint. IPv4: The system allocates an IPv4 endpoint from the selected virtual private cloud (VPC) and vSwitch. This is the default value. Dual-stack: The system automatically allocates IPv4 and IPv6 endpoint IP addresses from the selected VPC and vSwitch. Dual-stack is available only when IPv6 is enabled for the vFW cluster. |
| Source VPC | Select the VPC of the endpoint. |
| Source Vswitch | A vSwitch is a subnet within the selected VPC. Select the vSwitch that is associated with the endpoint. |
| Description | Enter a description for the endpoint. The description can be 0 to 256 characters in length. |

After you create the endpoint, return to the Details page. You can find that the endpoint is in the **Running** state, and the endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

#### 3.1.5 Add a vFW route

A virtual firewall (vFW) route controls the traffic path and ensures the execution of security policies. This topic describes how to create a vFW route.

**Prerequisites**

A vFW cluster and an endpoint of the vFW are created. For more information, see Create a vFW cluster and Create an endpoint for a vFW cluster.

**Create a vFW cluster route**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the vFW cluster that you want to manage and click its name to go to the details page.
5. In the **VFW Router** section, click **Create VFW Route**, configure the parameters, and then
click **OK**. Click the **IPv4 Route** or **IPv6 Route** tab based on your business requirements.

| Parameter | Description |
|---|---|
| VPC | Select the virtual private cloud (VPC) to which the vFW route belongs. |
| VLAN ID | After you select a VPC, you can select the VLAN ID. |
| Interface Name | After you select a VPC, an interface is automatically selected by the system. |
| Next Hop | After you select a VPC, a next hop is automatically selected by the system. |
| Destination CIDR Block | Enter the destination CIDR block to which the vFW route applies. The CIDR block defines the scope of traffic to be regulated by the vFW route. |
| Description | Enter a description. The description can be 1 to 255 characters in length. |

#### 3.1.6 Quick bypass

The quick bypass feature is designed for emergency scenarios. It temporarily bypasses the security detection and filtering features of firewalls without affecting business continuity. This feature works with Virtual Private Cloud (VPC) and Express Connect to implement failover. This topic describes how to enable and disable the quick bypass feature.

**Enable and disable quick bypass**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the virtual firewall (vFW) cluster that you want to manage and click its name to go to
the **Details** page.
5. In the **Bypass** section, click **One-click bypass**, enter the **verification code**, and then
click **OK**. The **verification code** is the UID of the level 1 organization. To resume route advertisement, click **One-click Revert**.

> **Warning:** If you click **One-click Bypass**, all VPC routes from the vFW cluster are automatically withdrawn. If you click **One-click Revert**, advertisement of VPC routes to the vFW cluster is resumed.

#### 3.1.7 View details of a vFW cluster

This topic describes how to view the details about a virtual firewall (vFW) cluster.

**View vFW cluster information**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Firewalls**.
4. Find the vFW cluster that you want to manage and click its name to go to the **Details** page.
You can view information in the following sections: **Cluster Information**, **Bypass**, **ECS**
**Info**, **Endpoint**, **VFW Interface**, and **VFW Route**.

### 3.2 CIDR block management

#### 3.2.1 Create a CIDR block

CIDR blocks provide a flexible way to represent IP address ranges. NFV Cloud Firewall uses these CIDR blocks to simplify the configuration of security policies and ensure fine-grained control of network traffic. Before you can create a virtual firewall (vFW) cluster, you need to create a CIDR block. This topic describes how to create a CIDR block.

**Create a CIDR block**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **CIDR Management**.
4. Click **Create CIDR**, configure the parameters, and then click **OK**.

| Parameter | Description |
|---|---|

| Name | Enter a name for the custom CIDR block. The name can be 1 to 128 characters in length. |   |   |
|---|---|---|---|
| Organization | Select the organization to which the CIDR block belongs. |   |   |
| Resource Set | Select the resource set to which the CIDR block belongs. |   |   |
| Area | Select the region in which you want to create the CIDR block. |   |   |
| IPv4 CIDR | Enter an IPv4 CIDR block in the format of <IP address>/<prefix length> . To ensure that network elements can be created, we recommend that you use a private CIDR block whose subnet mask is smaller than 26 bits. |   |   |
|   |   | <IP address>/<prefix |   |
| IPv6 CIDR | Select whether to allocate an IPv6 CIDR. No Allocation: The system does not assign an IPv6 CIDR block to the VPC. This is the default value. Auto Allocation: Select an address pool from the Address Pool drop- down list. Then, the system automatically allocates an IPv6 CIDR block from the address pool. Manual Assignment: Select an address pool from the Address Pool drop-down list, specify an IPv6 IP address, and then click Validate. This validates the specified IPv6 CIDR block. |   |   |

| IPv4 CIDR | length> |
|---|---|

#### 3.2.2 Manage CIDR blocks

This topic describes how to view and delete CIDR blocks.

**View CIDR blocks**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **CIDR Management**.
4. View the CIDR block list.
You can view the CIDR block name, organization, resource set, CIDR, and status.

**Delete CIDR blocks**

> **Warning:** Before you delete a CIDR block, make sure that the CIDR block is no longer used in your NFV Cloud Firewall configurations.

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **CIDR Management**.
4. Find the CIDR block that you want to delete and click **Delete** in the **Operation** column.
5. In the **Tips** message, check the information and click **OK**.

### 3.3 Route configuration

#### 3.3.1 Create a route

This topic describes how to create a route to redirect traffic.

**Prerequisites**

A virtual firewall (vFW) is created. For more information, see Create a vFW cluster.

**Create a route**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
4. In the upper-right corner of the page, click **Create Traffic Diversion Route**, configure the
parameters, and then click **OK**. You can configure **virtual private cloud (VPC)-to-VPC**, **vSwitch-to-vSwitch**, and **VPC-**
**to-data center** IPv4 and IPv6 routes. In this example, a VPC-to-VPC IPv4 route is
configured.

| Parameter | Description |
|---|---|
| Organization | Select an organization for the route. |
| Resource Set | Select a resource set for the route. |
| Area | Select the region in which you want to create the route. |

| Name |   | Enter a name for the route. |
|---|---|---|
| Bilateral Route |   | If you enable bilateral routing, the vFW cluster checks traffic in both directions based on configured policies. In a VPC-to-VPC communication scenario, if you disable bilateral routing, only one-way traffic checks are performed between the VPCs, such as traffic from VPC1 to VPC2. If you enable bilateral routing, traffic checks are performed in both directions between the VPCs. If you disable bilateral routing, you only need to configure the local network scope and port. If you enable bilateral routing, you need to configure both local and peer network scopes and ports. Note If you disable bilateral routing, you can configure two routes (local- to-peer and peer-to-local) to check traffic. The effect is equivalent to enabling bilateral routing. |
| Local Inform ation | Route Name | After you enter a name in the Route Name field, a route name is automatically generated. |
|   | VPC | Select a VPC. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically selected. |
|   | Routing Table | When you create a VPC, the system automatically creates a default route table. You can add system routes to the route table to manage VPC traffic. You can create multiple route tables for a VPC based on your business requirements. When you create a route for traffic redirection, the vFW cluster automatically reads the information about the VPC route table. |
|   | Target CIDR Block | Enter a destination CIDR block. |
|   | Applicatio n | Select an application. |
|   | Master VFW Cluster | Select the primary vFW cluster. |
|   | Master Endpoint Informati on | Select the endpoint of the primary vFW cluster. You can configure an endpoint for the cluster on the Firewalls page. |

|   | Slave VFW Cluster | Select a secondary vFW cluster. |
|---|---|---|
|   | Slave Endpoint Informati on | Select the endpoint of the secondary vFW cluster. You can configure an endpoint for the cluster on the Firewalls page. |
|   | Route Name | After you enter a name in the Route Name field, a route name is automatically generated. |
|   | VPC | Select a VPC. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically selected. |
|   | Routing Table | When you create a VPC, the system automatically creates a default route table. You can add system routes to the route table to manage VPC traffic. You can create multiple route tables for a VPC based on your business requirements. When you create a route for traffic redirection, the vFW cluster automatically reads the information about the VPC route table. |
| Peer Inform ation |   |   |
|   | Target CIDR Block | Enter a destination CIDR block. |
|   | Applicatio n | Select an application. |
|   | Master VFW Cluster | Select the primary vFW cluster. |
|   | Master Endpoint Informati on | Select the endpoint of the primary vFW cluster. You can configure an endpoint for the cluster on the Firewalls page. |
|   | Slave VFW Cluster | Select a secondary vFW cluster. |
|   | Slave Endpoint Informati on | Select the endpoint of the secondary vFW cluster. You can configure an endpoint for the cluster on the Firewalls page. |

After the route is created, the route is in the **Unpublish** status by default. You need to manually advertise the route before the route can be displayed in the VPC route table.

#### 3.3.2 Advertise and withdraw a route

After you create a route, you need to advertise the route. After the route is advertised, it is displayed in the route table of the virtual private cloud (VPC). This topic describes how to advertise and withdraw a route.

**Usage notes**

After a route is advertised, the route cannot be modified or deleted. To modify or delete the route, you must withdraw the route first.

**Advertise routes**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
Advertise a single route a. Find the route that you want to advertise and click **Publish** in the **Operation** column. b. In the **Tips** message, confirm the settings and click **OK**. Advertise multiple routes at the same time a. Select the routes that you want to advertise and click **Publish** below the route list. b. In the **Tips** message, confirm the settings and click **OK**. After a route is advertised, the status in the **Status** column changes to **Published**.

**Withdraw routes**

> **Warning:** We recommend that you withdraw routes during off-peak hours. To prevent service unavailability, make sure that your service no longer uses Cloud Firewall before you withdraw a route.

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
Withdraw a single route a. Find the route that you want to withdraw and click **Undo** in the **Operation** column. b. In the **Tips** message, confirm the settings and click **OK**. Withdraw multiple routes at the same time a. Select the routes that you want to withdraw and click **Undo** below the route list. b. In the **Tips** message, confirm the settings and click **OK**.

#### 3.3.3 Manage routes

This topic describes how to view, modify, and delete routes.

**View route configurations**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
4. View the list of routes.

**Modify route configurations**

You can modify only routes that are not advertised.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
4. Find the route that you want to modify, click **Edit** in the **Operation** column, modify the
configurations, and then click **OK**. You can modify the following parameters: **Target CIDR Block**, **Application**, **Master VFW**
**Cluster**, **Master Endpoint Information**, **Slave VFW Cluster**, and **Slave Endpoint**
**Information**.

**Delete routes**

You can delete only routes that are not advertised.

> **Warning:** Before you delete a route, make sure that the route is not in use.

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Route Configuration**.
4. Find the route that you want to delete and click **Delete** in the **Operation** column.
5. In the **Tips** message, check the information and click **OK**.

### 3.4 Dedicated hosts

#### 3.4.1 Create a dedicated host group

Dedicated hosts define a deployment mode in which physical servers are for exclusive use. In this mode, the entire physical server (host) can be exclusive only to you to ensure that the NFV Cloud Firewall instance is physically isolated from the instances of other tenants. This enhances security and helps you meet compliance requirements.

**Create a dedicated host group**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Dedicated Host**.
4. In the upper-right corner of the page, click **Create Dedicated Host Group**, configure the
parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the host group. The name can be 1 to 64 characters in length. |
| Organization | Select an organization for the host group. |
| Resource Set | Select a resource set for the host group. |
| Area | Select the region in which you want to create the host group. |
| Zone | Select the zone in which you want to create the host group. |
| Instance Specification | Select an instance type for the host group. |
| Description | Enter a description. The description can be 0 to 64 characters in length. |

5. Find the host group, click **Create Dedicated Host**, enter a name and a description, and
then click **OK**.

#### 3.4.2 Manage dedicated host groups

This topic describes how to manage host groups.

**View host groups**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Dedicated Host** and view the list of dedicated host
groups.
4. Click the host group name to view the host group details.
You can view the cluster information, host list, and application list.

**Create a dedicated host in a host group**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Dedicated Host** and view the list of dedicated host
groups.
4. Find the host group that you want to manage, click **Create Dedicated Host** in the
**Operation** column, enter a name and a description, and then click **OK**.
You can also click the name of the host group, and then click **Create Dedicated Host** on the details page.

**Delete a host group**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Dedicated Host**.
4. Find the host group that you want to delete and click **Delete** in the **Operation** column.
5. In the **Tips** message, check the information and click **OK**.

### 3.5 System settings

#### 3.5.1 Cross-organization resource authorization

**authorization**

This topic describes how to grant permission on the NFV Cloud Firewall instance purchased by Account A0 in Organization A to Account B0 in Organization B.

**Step 1: Use Account B0 to authorize Account A0 to access VPCs**

**within Account B0**

Log in to the console with **Account B0**.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Configuration > Cross Organizational**
**Resource Authorization**.
4. On the **Outgoing Authorization** tab, click the **Resource** tab.
5. In the upper-right corner of the tab, click **Create Cross Organizational Resource**
**Authorization**. In the dialog box that appears, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination Primary Organization UID | Enter the UID of Account A0. |
| Destination Organization Name | Enter Organization A. |
| Organization | Select Organization B. |
| Resource Set | Select the resource set to which the virtual private cloud (VPC) belongs. |
| Selected VPC Resource | The authorized VPCs are displayed. |
| VPC Resource | The VPCs that you want to authorize. You can select one or more VPCs. |
| Description | Enter a description. The description can be 0 to 64 characters in length. |

6. Return to the resource list to check the VPCs that are authorized to Account A0.
You can filter VPCs by **Destination Primary Organization UID** or **Description**.

**Step 2: Account A0 specifies the vFW clusters accessible to**

**Account B0**

Log in to the console with **Account A0**.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Configuration > Cross Organizational**
**Resource Authorization**.
4. On the **Incoming Authorization** tab, you can view the VPCs that are authorized to
Account A0 in Step 1.
5. On the **Outgoing Authorization** tab, click the **Cluster** tab.
6. In the upper-right corner of the tab, click **Create Cross Organizational Cluster**
**Authorization**. In the dialog box that appears, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|

| Destination Primary Organization UID | Enter the UID of Account B0. |
|---|---|
| Destination Organization Name | Select Organization B. |
| Organization | Enter Organization A. |
| Resource Set | Select the resource set to which the application belongs. |
| Application | Select the application. |

**What to do next: Use Account A0 to configure the vFW cluster**

Log in to the console with **Account A0**. In the cluster authorized in Step 2, configure traffic redirection routes and virtual firewall (vFW) routes to protect network traffic between the VPCs of account B0.

#### 3.5.2 Workflows

This topic describes how to view the workflow details of a virtual firewall (vFW) cluster or an endpoint task.

**View workflows of a vFW cluster**

You can view the details about workflows of vFW cluster creation and deletion tasks, including the resource name and creation time.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Configuration > Workflow**.
4. On the **VFW Cluster** tab, view the cluster creation and deletion workflows.
You can filter workflows by task ID, task name, resource ID, resource name, or task status.
5. Click the
icon to the left of the task ID to view the task details.
6. Click the
icon in each step to view the details of each subtask.

**View workflows of endpoint tasks**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Cloud Firewall**. On the **NFV Cloud Firewall** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Configuration > Workflow**.
4. On the **Endpoint** tab, view the endpoint creation and deletion workflows.
You can filter workflows by task ID, task name, resource ID, resource name, or task status.
5. Click the
icon to the left of the task ID to view the task details.
6. Click the
icon in each step to view the details of each subtask.

### 3.6 Best practices

> **Note:** The following best practices are created based on Apsara Stack V3.18.6. As the service continues to iterate, some console pages, parameter names, or options may have changed. For example, the **CIDR** parameter is changed to **IPv4 CIDR** and the **IPv6 CIDR** parameter is added. The **IP Stack** parameter is added when you create a virtual firewall (vFW) endpoint. When you perform operations, the console shall prevail. The core operation logic and process remain unchanged.

#### 3.6.1 VPC-VPC protection within an organization by NFV Cloud Firewall in a single data center

**organization by NFV Cloud Firewall in a single**

**data center**

In a data center, virtual private clouds (VPCs) that belong to the same organization need to communicate. To ensure the security of inter-VPC communication, you can use NFV Cloud Firewall to enforce access control on the east-west traffic between the VPCs.

**Topology**

An organization has deployed two VPCs in a data center: VPC1 and VPC2. The CIDR block of

| PC1 is 10.1.0.0/16 . It contains v IDR block of VPC2 is 10.2.0.0/16 10.2.1.1 ). ECS1 and ECS2 need t | 10.1.0.0/16 |   | . It contains v |
|---|---|---|---|
| 10.2.1.1 |   |   |   |

| 10.1.1.0/24 |   | ) and ECS1 ( | 10.1.1.1 |   |
|---|---|---|---|---|
| ins vSwitch2 ( |   |   |   | ) and ECS |

VPC1 is `10.1.0.0/16` . It contains vSwitch1 ( `10.1.1.0/24` ) and ECS1 ( `10.1.1.1` ). The CIDR block of VPC2 is `10.2.0.0/16` . It contains vSwitch2 ( `10.2.1.0/24` ) and ECS2 ( `10.2.1.1` ). ECS1 and ECS2 need to communicate with each other. However, potential security risks exist if the organization directly connects the two VPCs. The east-west traffic between the VPCs must be inspected and controlled. To meet this goal, the organization uses an account that assumes the organization security admin role to create an NFV Cloud Firewall cluster, create endpoints in VPC1 and VPC2, and publish traffic redirection routes. In the preceding solution, VPC1 and VPC2 are securely connected, and ECS1 and ECS2 can communicate as expected. In addition, all east-west traffic is redirected to NVF Cloud Firewall and matched against access control policies. This efficiently enhances the security of inter-VPC communication.

|   | V 10.2.0 |
|---|---|
| 10. vSwitch2 10.2.1.0/24 ECS2 ep2 | 10. |

**VPC1**

10.1.0.0/16

|   | Swit .2.1.0 |
|---|---|
| 10.2. ECS2 ep2 | .2. |

**vSwitch1**

10.1.1.0/24 ECS1 ep1 VFW(M) VFW(S)

**vFW Network Service Cluster**

**NE VPC**

(19216810/24)

**Create resources**

Use an account that belongs to the current organization to log in to the Apsara Uni-manager Management Console, switch to the organization admin role, and create resources such as VPCs, vSwitches, and Elastic Compute Service (ECS) instances. Create VPC1 and VPC2: Create vSwitch1 and vSwitch2: Create ECS instances and a security group:

> **Important:** In this example, the security group permits traffic from all sources to simplify the configuration. In actual business scenarios, you need to configure the security group to permit traffic based on the business needs of the ECS instances. Do not permit traffic from all sources.

**Configure NFV Cloud Firewall**

**Step 1: Create a RAM role (required only for new organizations)**

1. Use an account that can assume the organization security admin role by default to log in to
the Apsara Uni-manager Management Console and choose **Security > Network Security**
**> NFV Cloud Firewall**.
If this is the first time the level-1 organization of the account uses NFV Cloud Firewall, the
**ram role does not exist** message is displayed after you are logged in. In this case, you
need to create a Resource Access Management (RAM) role first.
2. Switch to the role that has permissions on the organization, such as the organization admin
or organization security admin role. You can also use the admin account of the Apsara Unimanager Management Console. Choose **Configurations > Service-linked Roles**, click
**Create Service-linked Role**, configure the following parameters, and click **OK**.
**Service Name:** Select **Cloud Firewall**.
**Authorized Organization Name:** Select the organization on which the role is granted
permissions. In this example, NFV_POC1 is selected.

**Step 2: Check the vFW capacity**

On the **Firewalls** page of the **NFV Cloud Firewall** console, **VFW Capacity: xGbps/nGbps** is displayed in the upper-right corner.
**x Gbps** before the forward slash (**/**): the current capacity used by the organization. If this is
the first time an organization uses NFV Cloud Firewall, **0Gbps** is displayed.
**n Gbps** after the forward slash (**/**): the maximum capacity that the organization can use. If
a number is displayed, the number indicates the maximum capacity, such as **10Gbps** in the following figure. If **-Gbps** is displayed: Scenario 1: No capacity quota for this organization is assigned to the admin account of the Apsara Uni-manager Management Console. The maximum capacity equals the
**logical inventory** allocated to the super account of the Apsara Uni-manager
Management Console. If no **logical inventory** is allocated to the super account, the maximum capacity equals the value of the **Issued** field of NFV Cloud Firewall-ALY00 in

**System Config > Authorization information > Authorized Specifications Details**

of the Apsara Uni-manager Operations Console. Scenario 2: The capacity quota of the admin account for this organization is set to 0. This means that the account is not allowed to create NFV Cloud Firewall clusters. You can create NFV Cloud Firewall clusters only when `Capacity required for creating an` NFV Cloud Firewall cluster + Current capacity used ≤ Total capacity . If not, you need to use the admin account to adjust the NFV Cloud Firewall quota for this organization.

**Step 3: Create a CIDR block (required only during the first time**

**you create an NFV Cloud Firewall cluster)**

If this is the first time you create an NFV Cloud Firewall cluster in a level-1 organization, you need to first create a CIDR block. You can select one or more CIDR blocks that you created when you create the network element (NE) VPC. In most cases, one CIDR block is sufficient within each organization.

**Important**

> We recommend that you use a subnet belonging to `192.168.0.0/16` or
> `172.16.0.0/16` . Do not use a CIDR block that overlaps with that of the production VPC in the organization, in case address conflicts occur.

1. On the **CIDR Management** page of the **NFV Cloud Firewall** console, click **Create CIDR**
and configure the following parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the NE VPC. In this example, entern fv poc1. _ |
| Organization | Select the organization to which the current account belongs. In this example, level-1 organization NFV POC1 is selected. _ |
| Resource Set | Select a resource set. In this example, the default resource set is selected. |
| Area | Select a region. |
| CIDR | Enter a CIDR block. The mask length must be smaller than 26. In this example, enter 192.168.1.0/24. |

2. After you confirm the configuration, click **OK**. After the status of the CIDR block changes
from **processing** to **success**, the CIDR block is created.

**Step 4: Create an NFV Cloud Firewall application**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click **Create Cluster** and
configure the following parameters in the panel that appears to create an NFV Cloud Firewall application. When you create an application, a vFW cluster is simultaneously created.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the NFV Cloud Firewall application. We recommend that you enter an informative name that contains the business information. Example: nfv poc. _ |
| VFW Cluster Name | Enter the name of the vFW cluster. In a single data center, the application name can be the same as the vFW cluster name. In a disaster recovery environment, we recommend that you include the data center information in the vFW cluster name to simplify O&M. Example: nfv poc az1. _ _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | Select a region from the drop-down list. |
| Zone | Select a zone from the drop-down list. Create a vFW cluster on the ECS cluster in the data center. |
| CIDR | Select a CIDR block from the drop-down list, which indicates the NE VPC in which the vFW cluster is created. If no CIDR block is created, the list is empty. |
| Deployment Type | Select a cluster deployment mode to meet your business requirements: Active-Standby: In this high-availability mode, two vFW ECS instances are used for disaster recovery. This mode consumes twice the vFW capacity consumed by the standalone mode. Standalone: In this mode, only one vFW ECS instance is used. This mode does not provide high availability and consumes the vFW capacity. |
| Dedicated Host | Specify whether to deploy the cluster on a dedicated host. No: The cluster is randomly deployed on ECS instances. Yes: You need to specify a dedicated host group and a dedicated host. |
| Network Type | Default value: 25 G. |
| CPU Type | You can choose Intel/X86 orHG /X86. This parameter allows you to choose the ECS cluster that uses the specified CPU type. |

| VFW Specification | Select a vFW specification that meets the preceding network and CPU type conditions from the drop-down list. This parameter indicates the maximum throughput of the vFW cluster for large packets, which consumes the equivalent firewall capacity quota. |
|---|---|
| ECS Specification | Select an ECS specification that meets the preceding network and CPU type conditions from the drop-down list. |
| ECS Image ID | Select the image used by the vFW cluster from the drop-down list. |
| Description | Enter the description of the cluster. We recommend that you include the business, department, and organization information in the description so that the administrator can easily identify the businesses protected by the vFW cluster. |

> **Note:** The values of the CPU Type, VFW Specification, ECS Specification, and ECS Image ID parameters vary depending on the environment and Apsara Stack version. Specify these parameters based on the actual business requirements.

2. After you confirm the configuration, click **OK**. Then, the system automatically verifies the
capacity and quota. If the capacity is sufficient, the operation succeeds and a new NFV Cloud Firewall application is displayed in the list. The status of the vFW cluster changes to
**Creating**.
3. Click the task ID in the **Task ID** column of the application to go to the Workflow page. On
this page, you can view the progress of the cluster creation task. When the subtasks
**ecs_start** and **eni_attach** enter the **Successful** state, the cluster is created.
4. Return to the **Firewalls** page. The NFV Cloud Firewall application is displayed. When the
status of the vFW cluster changes to **Running**, click the application name to go to the application details page. You can view the health status of the vFW ECS instance in the
**Health Status** column. If **Healthy** is displayed, the cluster service functions as expected.
You can then proceed to the next step. If not, the cluster service is not ready. Wait patiently. Common prompts:
**Quota check not passed**: The capacity usage exceeds the specified quota. In this case,
use the admin account to log in to the Apsara Uni-manager Management Console and adjust the NFV Cloud Firewall capacity quota for the current organization.
**cluster capacity reach license limit**: The capacity usage exceeds the total capacity. In
this case, increase the NFV Cloud Firewall capacity by placing a purchase order.

**Step 5: Create endpoints**

An endpoint is equivalent to an interface used by NFV Cloud Firewall to connect to a VPC. It occupies an IP address from the VPC and serves as the next hop for inter-VPC communication. All match traffic is automatically redirected to NFV Cloud Firewall, and then inspected and matched against access control policies. Two processes are involved to create an endpoint:
**Process on the cloud platform side**: An elastic network interface (ENI) is created. You
can view the ENI information by checking the ENI whose description is **Interface for**
**fastpath ft-int-onp use by nfv forbid to operate** on the **ENIs** page of the **ECS** console
in the Apsara Uni-manager Management Console. This process logically associates the endpoint with the VPC.
**Process on the NFV Cloud Firewall side** : A vFW interface is automatically created. You
can use the vFW account to access the NFV Cloud Firewall console or CLI and then view the configuration of the vFW interface. This process logically associates the endpoint with the vFW cluster.

> **Note:** The number of endpoints supported by NFV Cloud Firewall depends on the ECS specification you selected when you create the vFW cluster. The upper limit and current usage displayed in the console prevail. When the upper limit is reached, new endpoints can no longer be created.

**Create an endpoint in VPC1**

1. Go to the NFV Cloud Firewall application details page. In the **Endpoint** section, click
**Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1. |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

**Create an endpoint in VPC2**

1. In the **Endpoint** section, click **Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC2.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC2. |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the region of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC2 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc2. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.
After you complete the configuration, the endpoints and vFW interfaces enter the following states.

**Step 6: Create vFW routers**

By default, a vFW interface is configured with a direct route that points to the CIDR block of the vSwitch. However, you still need to add static routes to the vFW to route traffic to the CIDR blocks of VPC1 and VPC2.

**Add a route that routes traffic from the vFW to VPC1**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC1.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC1 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC1. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.

**Add a route that routes traffic from the vFW to VPC2**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC2.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC2 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |

| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
|---|---|
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC2. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc2. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.
After the configuration is completed, the vFW routers enter the following states.

**Step 7: Create a vFW web portal and log in to the vFW**

**(required only for the first time)**

A web portal is used to access the web interface of NFV Cloud Firewall over HTTPS. In a highavailability cluster, each vFW ECS instance requires a web portal. By default, you need only to access the primary node of the cluster to complete the operation. When an HA switchover is triggered, you need to access the secondary node of the cluster. You can use one of the following types of web portals to access NFV Cloud Firewall. You can create only one web portal of each type.
**Classic network**: After the web portal is created, a classic network IP address is displayed.
The web portal is connected to the web port and SSH port of the vFW ECS instance through a Server Load Balancer (SLB) instance deployed in the classic network. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.
**VPC**: After the web portal is created, a vSwitch IP address in the VPC is displayed. The web
portal is connected to the web port and SSH port of the vFW ECS instance through an SLB instance deployed in the VPC. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.

**Create a vFW web portal**

**Classic network web portal**

1. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the first ECS instance.
2. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.
3. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the second ECS instance.
4. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.

**VPC web portal**

If your O&M network has access to a VPC, you can also create a VPC web portal in the VPC to access the vFW ECS instance.

> **Important:** Do not create a VPC web portal in the production VPC that is connected to NFV Cloud Firewall in case route conflicts occur.

Refer to the classic network web portal procedure, go to the access mode details pages of the two ECS instances, and complete the following steps to create a VPC web portal for each ECS instance.
1. In the **VPC** section, click **Create**.
2. In the **Create VPC Network Access Method** dialog box, set **Vswitch ID** to the ID of a
vSwitch in the VPC. Make sure that the vSwitch has idle IP addresses.

**Log in to the vFW**

Use a browser to access the web URL of the vFW. Then, the login page of the vFW is displayed. In the upper-right corner of the page shows whether the current device is the primary device or the secondary device. You must log in to the primary device first. Enter the default username and password, which are both admin. After you are logged in, you are required to change the default password. After the change, the new password is synchronized to the secondary device. After you log in to the vFW again, check the hardware platform information and license. Make sure that the authorization is valid and proceed.

**Step 8: Create vFW access control policies**

By default, NFV Cloud Firewall blocks traffic from all sources. To enable intercommunication, you need to configure access control policies to permit access from specific sources. In this scenario, configure a policy to permit ECS1 to access ECS2 and enable logging to generate access records. In a production environment, we recommend that you do not enable logging for all access control policies.
1. In the Apsara Uni-manager Management Console, choose **Policy > Security Policy >**
**Policy** and then choose **New > Policy**.
2. Configure the following parameters to create a policy to permit ECS1 to access ECS2, and
click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy to describe its purpose. |

| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
|---|---|
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC2 is selected. |
| Destination Address | Create an address object named ECS2, which contains the IP address of ECS2 ( 10.2.1.1 ). |
| Service | Select Any. |
| Action | Select Permit. |
| Options | Click Options, and select Session start and Session end for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

3. **Enable session logging for the vFW** : In the Apsara Uni-manager Management Console,
choose **Monitor > Log > Session Log** and click **Configure**. In the right-side **Session** panel, turn on **Enable**. If you want to view logs in the console, select **Local Database**. If you want to view logs at the CLI, select **Cache**.

> **Important:** When session logging is disabled for the vFW, even if you have enabled logging in the access control policy, you cannot find any records on the log query page. You can view only the number of policy hits.

**Step 9: Create traffic redirection routes**

Types of traffic redirection routes:
**VPC-VPC**: In VPC-VPC protection scenarios (scenario in this topic), create traffic redirection
routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
**VS-VS**: In vSwitch-vSwitch protection scenarios, create traffic redirection routes on NFV
Cloud Firewall and publish the routes to the specified VPC route table.
**VPC-IDC**: In VPC-data center protection scenarios (scenario in this topic), create traffic
redirection routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
1. After you confirm that the configuration in the preceding steps is correct, log in to the **NFV**
**Cloud Firewall** console of the Apsara Uni-manager Management Console and go to the
**Route Configuration** page. Then, choose **Create Traffic Diversion Route > VPC-VPC**.

> **Warning:** **If you perform this operation in a production environment, make sure that** **the specifications of the vFW meet the expectation. If the volume of business** **traffic to redirect exceeds the maximum throughput of the vFW, the network** **latency increases and packet loss occurs.**

2. Configure the following parameters to configure a route to redirect VPC-VPC traffic and
click **OK**.

| Parameter |   | Description |
|---|---|---|
| Organization |   | Select an organization from the drop-down list. |
| Resource Set |   | Select a resource set from the drop-down list. |
| Area |   | Select a region from the drop-down list. |
| Name |   | Enter a name for the custom route. |
| Bilateral Route |   | By default, traffic redirection is configured for only one VPC. You can also turn on Bilateral Route to configure traffic redirection for two interconnected VPCs. In this example, Bilateral Routing is turned on and traffic redirection is configured for VPC1 and VPC2 at a time. |
|   | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to vpc2 in this example. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC1 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |

|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC2, which is 10.2.0.0/16 . |
|---|---|---|
| Local Inform ation |   |   |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |
| Peer Inform ation | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to vpc1 in this example. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC2 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC1, which is 10.1.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |

|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|---|---|---|
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |

After you complete the configuration, the **Route Status** column of the routes displays
**Unpublish**. In this case, the O&M engineer needs to complete adding and checking all
routes and then publish the routes one after one or in batches. This feature allows you to perform route configuration and traffic redirection within two time windows in case you do not have sufficient time to complete the two tasks within the same time window.
3. Click **Publish** in the **Operation** column of the desired traffic redirection route and click **OK**.
Wait until the status of the route changes from **Publishing** to **Published**. This means that the route is in effect. This way, the outbound traffic of VPC1 and VPC2 is redirected to NFV Cloud Firewall. After the traffic redirection route is published, log in to the **VPC** console, go to the **Route**
**Tables** page, and view the status of the routes in the route tables of VPC1 and VPC2.
You can find that the two routes whose mask length is N+1 are published from NFV Cloud Firewall. Their next hops are set to the ENI of the endpoint. The **route names** you entered are displayed in the route descriptions to simplify O&M. Route table of VPC1: Route table of VPC2:

**Step 10: Verify the business**

1. Log in to ECS1 and initiate a business test:
i. Run the `ping <ECS2 IP>` command on ECS1 to test the connectivity to ECS2. The ping succeeds. ii. Run the `ssh root@<ECS2 IP>` command on ECS1 to log in to ECS2 over SSH. The operation succeeds.
2. Log in to the Apsara Uni-manager Management Console to view logs.
Choose **Policy > Security Policy > Policy**, find the desired policy, and check whether the **number of hits** increases. Choose **Monitor > Log > Session Log**, set **Time** to **Real-time**, and check whether ping (corresponding to ICMP) and SSH (corresponding to TCP) logs are generated. In addition, check whether session logs containing source and destination IP addresses related to the test are generated.

**Other scenarios**

**Scenario 1: When a VPC contains multiple vSwitches, do I need**

**to create an endpoint for each vSwitch on NFV Cloud Firewall?**

**Solution**: No. vSwitches in a VPC can communicate with each other. Typically, an NFV Cloud
Firewall cluster needs only one endpoint in each VPC. You do not need to create an endpoint for each vSwitch. In the following example, vSwitch1-2 in VPC1 and vSwitch2-2 in VPC2 do not have endpoints. However, they can communicate with each other through NFV Cloud Firewall.

**VPC1**

**VPC2**

10.1.0.0/16 10.2.0.0/16

**vSwitch2-2**

**vSwitch1-2**

**vSwitch1**

**vSwitch2**

10.1.2.0/24 10.1.1.0/24 10.2.1.0/24 10.2.2.0/24 ECS1 ECS2-2 ECS2 ECS1-2 ep1 ep2 VFW(M) VFW(S)

**vFW Network**

Service Cluster NE VPC (192.168.1.0/24)

**Scenario 2: How do I connect multiple VPCs? How many VPCs**

**can be connected to NFV Cloud Firewall?**

**Solution**: A VPC is connected to NFV Cloud Firewall through an endpoint. Therefore, you only
need to add routes to the VPC route table to redirect traffic to NFV Cloud Firewall. The Endpoint page shows the maximum number of VPCs supported depending on the instance type selected for NFV Cloud Firewall.

|   | VPC2 1 |
|---|---|
| Destination Ne to VPC1 N to VPCN N vSwitch2 10.2.1.0/24 ECS2 ep2 |   |

VPC1 10.1.0.0/16

**DestinationNext Hop**

to VPC2 NFV to VPC3 NFV

|   |   | witch2 |
|---|---|---|
| ECS2 ep2 |   |   |

vSwitch1 10.1.1.0/24 ECS1 ep1 VFW(M) VFW(S) vFW Network Service Cluster NE VPC (192.168.1.0/24)

|   | VPCN 1 |   |
|---|---|---|
| Destination Ne to VPCN N to VPC3 N vSwitchN 10.N.1.0/24 ECSN epN |   |   |
|   |   | xt FV FV |

VPC3 10.3.0.0/16

**DestinationNext Hop**

to VPC1 NFV to VPCN NFV

|   |   | witch |
|---|---|---|
| ECSN epN |   |   |

vSwitch3 10.3.1.0/24 ECS3 ep3

#### 3.6.2 VPC-VPC protection across organizations by NFV Cloud Firewall in a single data center

**organizations by NFV Cloud Firewall in a**

**single data center**

In a data center, virtual private clouds (VPCs) that belong to different organizations need to communicate with each other. In this scenario, you can use NFV Cloud Firewall to protect intercommunication between VPCs that belong to different organizations.

**Topology**

In a data center, Organization 1 and Organization 2 each have created a VPC. Resources are deployed as follows: Organization 1: The CIDR block of VPC1 is `10.1.0.0/16` . It contains vSwitch1 ( `10.1.1.0/24` ) and ECS1 ( `10.1.1.1` ). Organization 2: The CIDR block of VPC3 is `10.3.0.0/16` . It contains vSwitch3 ( `10.3.1.0/24` ) and ECS3 ( `10.3.1.1` ). Due to business needs, ECS1 needs to communicate with ECS3. However, the VPCs belong to different organizations and VPCs are isolated from each other by default. To meet security compliance requirements, the Elastic Compute Service (ECS) instances must directly communicate. To balance connectivity and security, you can use the centralized traffic redirection architecture of NFV Cloud Firewall:
1. Cross-organization resource access authorization: Organization 2 can authorize
Organization 1 to access key metadata of VPC3, such as the VPC ID, VPC name, VPC CIDR block, vSwitch ID, vSwitch name, and route table ID.
2. Create an NFV Cloud Firewall cluster and publish traffic redirection routes: Use an account
within Organization 1 to create an NFV Cloud Firewall cluster, create endpoints in VPC1 and VPC3, and publish traffic redirection routes.
3. Access control: All east-west traffic is redirected to the virtual firewall (vFW) cluster for
access control and logging. After the configuration is completed, the Elastic Compute Service (ECS) instances in the VPCs can communicate across organizations. The bidirectional communication is centrally regulated and protected by NFV Cloud Firewall. Organization 2 authorizes Organ Organization 1 authorizes the vFW clust

| FW cl |   |   |
|---|---|---|
|   | F | W |

Organization 1 Organization 2

|   | V 10.3.0. |
|---|---|
| 10.3 vSwitch3 10.3.1.0/24 ECS3 ep3 | 10.3 |

**VPC1**

**VPC3**

10.1.0.0/16

|   |   | Switc .3.1.0 |
|---|---|---|
| 10.3. ECS3 ep3 |   | .3. |

**vSwitch1**

10.1.1.0/24 ECS1 ep1

|   | VFW(M) VFW(S) vFW Network Servic NE VPC |
|---|---|

**Create resources**

Use accounts that belong to Organization 1 and Organization 2 to log in to the Apsara Unimanager Management Console, switch to the organization admin role, and create resources such as VPCs, vSwitches, and ECS instances.

**Create resources in Organization 1**

Create VPC1: Create vSwitch1: Create ECS1 and a security group:

**Create resources in Organization 2**

Create VPC3: Create vSwitch3: Create ECS3 and a security group:

> **Important:** In this example, the security group permits traffic from all sources to simplify the configuration. In actual business scenarios, you need to configure the security group to permit traffic based on the business needs of the ECS instances. Do not permit traffic from all sources.

**Configure NFV Cloud Firewall**

**Step 1: Create a RAM role (required only for new organizations)**

Repeat the steps to create a Resource Access Management (RAM) role for Organization 1 and Organization 2 with the accounts that belong to the two organizations.
1. Use an account that can assume the organization security admin role by default to log in to
the Apsara Uni-manager Management Console and choose **Security > Network Security**
**> NFV Cloud Firewall**.
If this is the first time the level-1 organization of the account uses NFV Cloud Firewall, the
**ram role does not exist** message is displayed after you are logged in. In this case, you
need to create a RAM role first.
2. Switch to the role that has permissions on the organization, such as the organization admin
or organization security admin role. You can also use the admin account of the Apsara Unimanager Management Console. Choose **Configurations > Service-linked Roles** and click **Create Service-linked Role**.
3. Configure the following parameters, and click **OK**.

**Create a RAM role for Organization 1:**

**Service Name**: Select **Cloud Firewall**.
**Authorized Organization Name**: Select the organization on which the role is granted
permissions. In this example, NFV_POC1 is selected.

**Create a RAM role for Organization 2:**

**Service Name**: Select **Cloud Firewall**.
**Authorized Organization Name**: Select the organization on which the role is granted
permissions. In this example, NFV_POC2 is used.

**Step 2: Authorize Organization 1 to access VPC resources**

**across organizations**

In this scenario, the NFV Cloud Firewall clusters are created and managed by Organization 1. However, access to the VPC of Organization 2, such as VPC3, is required for crossorganization communication. Therefore, Organization 2 must authorize Organization 1 to access its VPC resources so that Organization 1 can create endpoints, configure firewall routes, create access control policies, and publish traffic redirection routes.
1. Obtain the level-1 organization UID and name of Organization 1: Log in to the Apsara Uni-
manager Management Console by using the account that belongs to Organization 1. Click the user icon in the upper-right corner. On the **User Information** page, record the values of the **Organization** and **Tenant Account Alias** (level-1 organization UID) fields.
2. Authorize Organization 1 to access the VPC resources of Organization 2:
i. Log in to the **NFV Cloud Firewall** console in Apsara Uni-manager Management Console by using the account that belongs to Organization 2. In the left-side navigation pane, choose **System Configuration > Cross Organization Resource Authorization**. On the page that appears, choose **Outgoing Authorization > Resource** and click **Create**
**Cross Organization Resource Authorization**.
ii. In the **Create Cross Organization Resource Authorization** panel, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination Primary Organization UID | Enter the UID of Organization 1. Do not enter the account UID. The organization UID usually starts with 1XX. In most cases, enter the value of the Tenant Account Alias field on the User Information page. |
| Destination Organization Name | Enter the name of Organization 1. In most cases, enter the value of the Organization field on the User Information page. |
| Organization | Select an organization from the drop-down list, that is, the organization to which the VPC to be authorized belongs. It may be a level-2 or level-3 organization below Organization 2. |
| Resource Set | Select the resource set to which the VPC to be authorized belongs from the drop-down list. |
| VPC Resource | Select the VPC to be authorized from the drop-down list. Fuzzy match is supported. The selected VPC is displayed in the Selected VPC Resource field. You can modify Organization and Resource Set and select another VPC. The selected VPC will be retained in this case. In this example, only VPC3 is selected. |
| Description | Enter a description. We recommend that you enter the description in the format of Organization name + VPC name to simplify O&M. This description will be displayed on the peer organization page. |

After you complete the configuration, you can find the authorization setting on the page, as shown in the following figure.

**Step 3: Check the firewall capacity of Organization 1**

On the **Firewalls** page of the **NFV Cloud Firewall** console, **VFW Capacity: xGbps/nGbps** is displayed in the upper-right corner.
**x Gbps** before the forward slash (**/**): the current capacity used by the organization. If this is
the first time an organization uses NFV Cloud Firewall, **0Gbps** is displayed.
**n Gbps** after the forward slash (**/**): the maximum capacity that the organization can use. If
a number is displayed, the number indicates the maximum capacity, such as **10Gbps** in the following figure. If **-Gbps** is displayed: Scenario 1: No capacity quota for this organization is assigned to the admin account of the Apsara Uni-manager Management Console. The maximum capacity equals the
**logical inventory** allocated to the super account of the Apsara Uni-manager
Management Console. If no **logical inventory** is allocated to the super account, the maximum capacity equals the value of the **Issued** field of NFV Cloud Firewall-ALY00 in

**System Config > Authorization information > Authorized Specifications Details**

of the Apsara Uni-manager Operations Console. Scenario 2: The capacity quota of the admin account for this organization is set to 0. This means that the account is not allowed to create NFV Cloud Firewall clusters. You can create NFV Cloud Firewall clusters only when `Capacity required for creating an` NFV Cloud Firewall cluster + Current capacity used ≤ Total capacity . If not, you need to use the admin account to adjust the NFV Cloud Firewall quota for this organization.

**Step 4: Create a CIDR block for Organization 1 (required only**

**during the first time you create a cluster)**

If this is the first time you create an NFV Cloud Firewall cluster in a level-1 organization, you need to first create a CIDR block. You can select one or more CIDR blocks that you created when you create the network element (NE) VPC. In most cases, one CIDR block is sufficient within each organization.

> **Important:** We recommend that you use a subnet belonging to 192.168.0.0/16 or 172.16.0.0/16. Do not use a CIDR block that overlaps with that of the production VPC in the organization, in case address conflicts occur.

1. On the **CIDR Management** page of the **NFV Cloud Firewall** console, click **Create CIDR**
and configure the following parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the NE VPC. In this example, entern fv poc1. _ |
| Organization | Select the organization to which the current account belongs. In this example, level-1 organization NFV POC1 is selected. _ |
| Resource Set | Select a resource set. In this example, the default resource set is selected. |
| Area | Select a region. |
| CIDR | Enter a CIDR block. The mask length must be smaller than 26. In this example, enter 192.168.1.0/24. |

2. After you confirm the configuration, click **OK**. After the status of the CIDR block changes
from **processing** to **success**, the CIDR block is created.

**Step 5: Create an NFV Cloud Firewall application for**

**Organization 1**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click **Create Cluster** and
configure the following parameters in the panel that appears to create an NFV Cloud Firewall application. When you create an application, a vFW cluster is simultaneously created.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the NFV Cloud Firewall application. We recommend that you enter an informative name that contains the business information. Example: nfv poc. _ |
| VFW Cluster Name | Enter the name of the vFW cluster. In a single data center, the application name can be the same as the vFW cluster name. In a disaster recovery environment, we recommend that you include the data center information in the vFW cluster name to simplify O&M. Example: nfv poc az1. _ _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | Select a region from the drop-down list. |
| Zone | Select a zone from the drop-down list. Create a vFW cluster on the ECS cluster in the data center. |
| CIDR | Select a CIDR block from the drop-down list, which indicates the NE VPC in which the vFW cluster is created. If no CIDR block is created, the list is empty. |
| Deployment Type | Select a cluster deployment mode to meet your business requirements: Active-Standby: In this high-availability mode, two vFW ECS instances are used for disaster recovery. This mode consumes twice the vFW capacity consumed by the standalone mode. Standalone: In this mode, only one vFW ECS instance is used. This mode does not provide high availability and consumes the vFW capacity. |

| Dedicated Host | Specify whether to deploy the cluster on a dedicated host. No: The cluster is randomly deployed on ECS instances. Yes: You need to specify a dedicated host group and a dedicated host. |
|---|---|
| Network Type | Default value: 25 G. |
| CPU Type | You can choose Intel/X86 orHG /X86. This parameter allows you to choose the ECS cluster that uses the specified CPU type. |
| VFW Specification | Select a vFW specification that meets the preceding network and CPU type conditions from the drop-down list. This parameter indicates the maximum throughput of the vFW cluster for large packets, which consumes the equivalent firewall capacity quota. |
| ECS Specification | Select an ECS specification that meets the preceding network and CPU type conditions from the drop-down list. |
| ECS Image ID | Select the image used by the vFW cluster from the drop-down list. |
| Description | Enter the description of the cluster. We recommend that you include the business, department, and organization information in the description so that the administrator can easily identify the businesses protected by the vFW cluster. |

> **Note:** The values of the CPU Type, VFW Specification, ECS Specification, and ECS Image ID parameters vary depending on the environment and Apsara Stack version. Specify these parameters based on the actual business requirements.

2. After you confirm the configuration, click **OK**. Then, the system automatically verifies the
capacity and quota. If the capacity is sufficient, the operation succeeds and a new NFV Cloud Firewall application is displayed in the list. The status of the vFW cluster changes to
**Creating**.
3. Click the task ID in the **Task ID** column of the application to go to the Workflow page. On
this page, you can view the progress of the cluster creation task. When the subtasks
**ecs_start** and **eni_attach** enter the **Successful** state, the cluster is created.
4. Return to the **Firewalls** page. The NFV Cloud Firewall application is displayed. When the
status of the vFW cluster changes to **Running**, click the application name to go to the application details page. You can view the health status of the vFW ECS instance in the
**Health Status** column. If **Healthy** is displayed, the cluster service functions as expected.
You can then proceed to the next step. If not, the cluster service is not ready. Wait patiently. Common prompts:
**Quota check not passed**: The capacity usage exceeds the specified quota. In this case,
use the admin account to log in to the Apsara Uni-manager Management Console and adjust the NFV Cloud Firewall capacity quota for the current organization.
**cluster capacity reach license limit**: The capacity usage exceeds the total capacity. In
this case, increase the NFV Cloud Firewall capacity by placing a purchase order.

**Step 6: Authorize Organization 2 to access vFWs across**

**organizations**

1. Go to the **System Configuration > Cross Organization Resource Authorization** page,
click the **Incoming Authorization** tab, check the VPC authorization information of Organization 2, and record **Source Primary Organization UID** for further configuration. If the page shows a large number of organizations and VPCs, you can also filter by organization UID, VPC ID, and VPC description in fuzzy match mode.
2. Go to the **System Configuration > Cross Organization Resource Authorization** page,
choose **Outgoing Authorization > Cluster**, and click **Create Cross Organizational**
**Cluster Authorization**.
3. In the **Create Cross Organizational Cluster Authorization** panel, configure the
following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination Primary Organization UID | Enter the UID of Organization 2, which is the value ofS ource Primary Organization UID recorded in the preceding step. |
| Destination Primary Organization Name | Enter the name of Organization 2. |
| Organization | Select an organization from the drop-down list, that is, the organization to which the vFW to be authorized belongs. It may be a level-2 or level-3 organization below Organization 1. |
| Resource Set | Select the resource set to which the vFW to be authorized belongs from the drop-down list. |
| Application | Select the NFV Cloud Firewall application from the drop-down list. Only the selected NFV Cloud Firewall application can access the VPC authorized by Organization 2. |

After you complete the configuration, you can find the authorization setting on the page, as shown in the following figure.

**Step 7: Create an endpoint for Organization 1**

An endpoint is equivalent to an interface used by NFV Cloud Firewall to connect to a VPC. It occupies an IP address from the VPC and serves as the next hop for inter-VPC communication. All match traffic is automatically redirected to NFV Cloud Firewall, and then inspected and matched against access control policies. Two processes are involved to create an endpoint:
**Process on the cloud platform side**: An elastic network interface (ENI) is created. You
can view the ENI information by checking the ENI whose description is **Interface for**
**fastpath ft-int-onp use by nfv forbid to operate** on the **ENIs** page of the **ECS** console
in the Apsara Uni-manager Management Console. This process logically associates the endpoint with the VPC.
**Process on the NFV Cloud Firewall side** : A vFW interface is automatically created. You
can use the vFW account to access the NFV Cloud Firewall console or CLI and then view the configuration of the vFW interface. This process logically associates the endpoint with the vFW cluster.

> **Note:** The number of endpoints supported by NFV Cloud Firewall depends on the ECS specification you selected when you create the vFW cluster. The upper limit and current usage displayed in the console prevail. When the upper limit is reached, new endpoints can no longer be created.

**Create an endpoint in VPC1**

1. Go to the NFV Cloud Firewall application details page. In the **Endpoint** section, click
**Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1. |
| Organization | Select an organization from the drop-down list. In this example, NFV POC1 is selected. _ |

| Resource Set | Select a resource set from the drop-down list. |
|---|---|
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

**Create an endpoint in VPC3**

1. In the **Endpoint** section, click **Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC3.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC3. |
| Organization | Select an organization from the drop-down list. In this example, NFV POC1 is selected. _ |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC3 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc3. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.
After you complete the configuration, the endpoints and vFW interfaces enter the following states.

**Step 8: Create vFW routers for Organization 1**

By default, a vFW interface is configured with a direct route that points to the CIDR block of the vSwitch. However, you still need to add static routes to the vFW to route traffic to the CIDR blocks of VPC1 and VPC3.

**Add a route that routes traffic from the vFW to VPC1**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC1.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC1 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC1. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.

**Add a route that routes traffic from the vFW to VPC3**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC3.

| Parameter | Description |
|---|---|

| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC3 is selected. |
|---|---|
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC3. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc3. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.
After the configuration is completed, the vFW routers enter the following states.

**Step 9: Create a vFW web portal for Organization 1 and log in**

**to the vFW (required only for the first time)**

A web portal is used to access the web interface of NFV Cloud Firewall over HTTPS. In a highavailability cluster, each vFW ECS instance requires a web portal. By default, you need only to access the primary node of the cluster to complete the operation. When an HA switchover is triggered, you need to access the secondary node of the cluster. You can use one of the following types of web portals to access NFV Cloud Firewall. You can create only one web portal of each type.
**Classic network**: After the web portal is created, a classic network IP address is displayed.
The web portal is connected to the web port and SSH port of the vFW ECS instance through a Server Load Balancer (SLB) instance deployed in the classic network. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.
**VPC**: After the web portal is created, a vSwitch IP address in the VPC is displayed. The web
portal is connected to the web port and SSH port of the vFW ECS instance through an SLB instance deployed in the VPC. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.

**Create a vFW web portal**

**Classic network web portal**

1. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the first ECS instance.
2. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.
3. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the second ECS instance.
4. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.

**VPC web portal**

If your O&M network has access to a VPC, you can also create a VPC web portal in the VPC to access the vFW ECS instance.

> **Important:** Do not create a VPC web portal in the production VPC that is connected to NFV Cloud Firewall in case route conflicts occur.

Refer to the classic network web portal procedure, go to the access mode details pages of the two ECS instances, and complete the following steps to create a VPC web portal for each ECS instance.
1. In the **VPC** section, click **Create**.
2. In the **Create VPC Network Access Method** dialog box, set **Vswitch ID** to the ID of a
vSwitch in the VPC. Make sure that the vSwitch has idle IP addresses.

**Log in to the vFW**

Use a browser to access the web URL of the vFW. Then, the login page of the vFW is displayed. In the upper-right corner of the page shows whether the current device is the primary device or the secondary device. You must log in to the primary device first. Enter the default username and password, which are both admin. After you are logged in, you are required to change the default password. After the change, the new password is synchronized to the secondary device. After you log in to the vFW again, check the hardware platform information and license. Make sure that the authorization is valid and proceed.

**Step 10: Create vFW access control policies for Organization 1**

By default, NFV Cloud Firewall blocks traffic from all sources. To enable intercommunication, you need to configure access control policies to permit access from specific sources. In this scenario, configure a policy to permit ECS1 to access ECS3 and enable logging to generate access records. In a production environment, we recommend that you do not enable logging for all access control policies.
1. In the Apsara Uni-manager Management Console, choose **Policy > Security Policy >**
**Policy** and then choose **New > Policy**.
2. Configure the following parameters to create a policy to permit ECS1 to access ECS3, and
click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy to describe its purpose. |
| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC3 is selected. |
| Destination Address | Create an address object named ECS3, which contains the IP address of ECS3 ( 10.3.1.1 ). |
| Service | Select Any. |

| Action | Select Permit. |
|---|---|
| Options | Click Options, and select Session start and Session end for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

3. **Enable session logging for the vFW** : In the Apsara Uni-manager Management Console,
choose **Monitor > Log > Session Log** and click **Configure**. In the right-side **Session** panel, turn on **Enable**. If you want to view logs in the console, select **Local Database**. If you want to view logs at the CLI, select **Cache**.

> **Important:** When session logging is disabled for the vFW, even if you have enabled logging in the access control policy, you cannot find any records on the log query page. You can view only the number of policy hits.

**Step 11: Create traffic redirection routes for Organization 1**

Types of traffic redirection routes:
**VPC-VPC**: In VPC-VPC protection scenarios (scenario in this topic), create traffic redirection
routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
**VS-VS**: In vSwitch-vSwitch protection scenarios, create traffic redirection routes on NFV
Cloud Firewall and publish the routes to the specified VPC route table.
**VPC-IDC**: In VPC-data center protection scenarios (scenario in this topic), create traffic
redirection routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
1. After you confirm that the configuration in the preceding steps is correct, log in to the **NFV**
**Cloud Firewall** console of the Apsara Uni-manager Management Console and go to the
**Route Configuration** page. Then, choose **Create Traffic Diversion Route > VPC-VPC**.

> **Warning:** **If you perform this operation in a production environment, make sure that** **the specifications of the vFW meet the expectation. If the volume of business** **traffic to redirect exceeds the maximum throughput of the vFW, the network** **latency increases and packet loss occurs.**

2. Configure the following parameters to configure a route to redirect VPC-VPC traffic and
click **OK**.

| Parameter | Description |
|---|---|

| Organization |   | Select an organization from the drop-down list. |
|---|---|---|
| Resource Set |   | Select a resource set from the drop-down list. |
| Area |   | Select a region from the drop-down list. |
| Name |   | Enter a name for the custom route. |
| Bilateral Route |   | By default, traffic redirection is configured for only one VPC. You can also turn on Bilateral Route to configure traffic redirection for two interconnected VPCs. In this example, Bilateral Routing is turned on and traffic redirection is configured for VPC1 and VPC3 at a time. |
| Local Inform ation | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. In this example, enter route to vpc3. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC1 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC3, which is 10.3.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |

|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|---|---|---|
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |
|   | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. In this example, enter route to vpc1. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC3 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
| Peer Inform ation |   |   |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC1, which is 10.1.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |

After you complete the configuration, the **Route Status** column of the routes displays
**Unpublish**. In this case, the O&M engineer needs to complete adding and checking all
routes and then publish the routes one after one or in batches. This feature allows you to perform route configuration and traffic redirection within two time windows in case you do not have sufficient time to complete the two tasks within the same time window.
3. Click **Publish** in the **Operation** column of the desired traffic redirection route and click **OK**.
Wait until the status of the route changes from **Publishing** to **Published**. This means that the route is in effect. This way, the outbound traffic of VPC1 and VPC3 is redirected to NFV Cloud Firewall. After the traffic redirection route is published, log in to the **VPC** console with the accounts of Organization 1 and Organization 2, go to the **Route Tables** page, and view the status of the routes in the route tables of VPC1 and VPC3. You can find that the two routes whose mask length is N+1 are published from NFV Cloud Firewall. Their next hops are set to the ENI of the endpoint. The **route names** you entered are displayed in the route descriptions to simplify O&M. Route table of VPC1 within Organization 1: Route table of VPC3 within Organization 2:

**Step 12: Verify the business**

1. Log in to ECS1 and initiate a business test:
i. Run the `ping <ECS3 IP>` command on ECS1 to test the connectivity to ECS3. The ping succeeds. ii. Run the `ssh root@<ECS3 IP>` command on ECS1 to log in to ECS3 over SSH. The operation succeeds.
2. Log in to the Apsara Uni-manager Management Console to view logs.
Choose **Policy > Security Policy > Policy**, find the desired policy, and check whether the **number of hits** increases. Choose **Monitor > Log > Session Log**, set **Time** to **Real-time**, and check whether ping (corresponding to ICMP) and SSH (corresponding to TCP) logs are generated. In addition, check whether session logs containing source and destination IP addresses related to the test are generated.

#### 3.6.3 vSwitch-vSwitch protection within an organization by NFV Cloud Firewall in a single data center

**organization by NFV Cloud Firewall in a single**

**data center**

If you want to protect communication between vSwitches that belong to the same organization, virtual private cloud (VPC), and data center, you can use NFV Cloud Firewall to enforce fine-grained access control on the east-west traffic.

**Limits**

Only when the VPC has subnet routing 2.0 enabled, you can redirect traffic between vSwitches (**vSwitch-vSwitch**) that belong to the same organization and data center to NFV Cloud Firewall.

**Note**

In Apsara Stack V3.18.0 and later, subnet routing 2.0 is enabled for newly created VPCs by default. Existing VPCs still use the default subnet routing 1.0. For more information about the support for subnet routing 2.0, refer to the VPC documentation. Before you begin, the VPC, make sure that subnet routing 2.0 is enabled for the VPC.

**Topology**

VPC1 ( `10.1.0.0/16` ) consists of two business subnets that belong to the same organization and data center: vSwitch1 ( `10.1.1.0/24` ), which uses the system route table. ECS1 ( `10.1.1.1` ) is attached to vSwitch1. vSwitch1-2 ( `10.1.2.0/24` ), which uses a custom route table. ECS1-2 ( `10.1.2.1` ) is attached to vSwitch1-2. Due to business requirements, ECS1 and ECS1-2 need to communicate with each other. To meet security compliance and business isolation requirements, the Elastic Compute Service (ECS) instances must not directly communicate over the VPC. Communication between the subnets must be regulated, audited, and managed based on access control policies. To ensure the security of intercommunication, the organization uses an account that assumes the organization security admin role to create an NFV Cloud Firewall cluster, create endpoints in vSwitch1 and vSwitch1-2, and publish traffic redirection routes. In the preceding solution, traffic between vSwitch1 and vSwitch1-2 is forcefully redirected to the NFV Cloud Firewall cluster, matches against access control policies, and then forwarded to the destination. This way, communication between vSwitches in the same VPC can be bidirectionally protected, controlled, and audited.

|   |   | System Route Table vSwitch1 10.1.1.0/24 Destination Next Hop to vSwitch1-2 NFVECS1 ep1 |
|---|---|---|

|   |   | xt Ho |
|---|---|---|

|   |   | witch 0.1.2. |
|---|---|---|
| 10.1 ECS1- ep2 |   | 0.1 |

Organization 1 VFW(M) VFW(S)

**vFW Network**

Service Cluster

**NE VPC**

(192.168.1.0/24)

**Create resources**

Use an account that belongs to the current organization to log in to the Apsara Uni-manager Management Console, switch to the organization admin role, and create resources such as VPCs, custom route tables, vSwitches, and ECS instances. Create VPC1: Create a custom route table: Create vSwitch1 and associate it with the system route table, and create vSwitch1-2 and associate it with the custom route table: Create ECS instances and a security group:

> **Important:** In this example, the security group permits traffic from all sources to simplify the configuration. In actual business scenarios, you need to configure the security group to permit traffic based on the business needs of the ECS instances. Do not permit traffic from all sources.

**Configure NFV Cloud Firewall**

**Step 1: Create a RAM role (required only for new organizations)**

1. Use an account that can assume the organization security admin role by default to log in to
the Apsara Uni-manager Management Console and choose **Security > Network Security**
**> NFV Cloud Firewall**.
If this is the first time the level-1 organization of the account uses NFV Cloud Firewall, the
**ram role does not exist** message is displayed after you are logged in. In this case, you
need to create a Resource Access Management (RAM) role first.
2. Switch to the role that has permissions on the organization, such as the organization admin
or organization security admin role. You can also use the admin account of the Apsara Unimanager Management Console. Choose **Configurations > Service-linked Roles**, click
**Create Service-linked Role**, configure the following parameters, and click **OK**.
**Service Name:** Select **Cloud Firewall**.
**Authorized Organization Name:** Select the organization on which the role is granted
permissions. In this example, NFV_POC1 is selected.

**Step 2: Check the vFW capacity**

On the **Firewalls** page of the **NFV Cloud Firewall** console, **VFW Capacity: xGbps/nGbps** is displayed in the upper-right corner.
**x Gbps** before the forward slash (**/**): the current capacity used by the organization. If this is
the first time an organization uses NFV Cloud Firewall, **0Gbps** is displayed.
**n Gbps** after the forward slash (**/**): the maximum capacity that the organization can use. If
a number is displayed, the number indicates the maximum capacity, such as **10Gbps** in the following figure. If **-Gbps** is displayed: Scenario 1: No capacity quota for this organization is assigned to the admin account of the Apsara Uni-manager Management Console. The maximum capacity equals the
**logical inventory** allocated to the super account of the Apsara Uni-manager
Management Console. If no **logical inventory** is allocated to the super account, the maximum capacity equals the value of the **Issued** field of NFV Cloud Firewall-ALY00 in

**System Config > Authorization information > Authorized Specifications Details**

of the Apsara Uni-manager Operations Console. Scenario 2: The capacity quota of the admin account for this organization is set to 0. This means that the account is not allowed to create NFV Cloud Firewall clusters. You can create NFV Cloud Firewall clusters only when `Capacity required for creating an` NFV Cloud Firewall cluster + Current capacity used ≤ Total capacity . If not, you need to use the admin account to adjust the NFV Cloud Firewall quota for this organization.

**Step 3: Create a CIDR block (required only during the first time**

**you create an NFV Cloud Firewall cluster)**

If this is the first time you create an NFV Cloud Firewall cluster in a level-1 organization, you need to first create a CIDR block. You can select one or more CIDR blocks that you created when you create the network element (NE) VPC. In most cases, one CIDR block is sufficient within each organization.

**Important**

> We recommend that you use a subnet belonging to `192.168.0.0/16` or
> `172.16.0.0/16` . Do not use a CIDR block that overlaps with that of the production VPC in the organization, in case address conflicts occur.

1. On the **CIDR Management** page of the **NFV Cloud Firewall** console, click **Create CIDR**
and configure the following parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the NE VPC. In this example, entern fv poc1. _ |
| Organization | Select the organization to which the current account belongs. In this example, level-1 organization NFV POC1 is selected. _ |
| Resource Set | Select a resource set. In this example, the default resource set is selected. |
| Area | Select a region. |
| CIDR | Enter a CIDR block. The mask length must be smaller than 26. In this example, enter 192.168.1.0/24. |

2. After you confirm the configuration, click **OK**. After the status of the CIDR block changes
from **processing** to **success**, the CIDR block is created.

**Step 4: Create an NFV Cloud Firewall application**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click **Create Cluster** and
configure the following parameters in the panel that appears to create an NFV Cloud Firewall application. When you create an application, a vFW cluster is simultaneously created.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the NFV Cloud Firewall application. We recommend that you enter an informative name that contains the business information. Example: nfv poc. _ |
| VFW Cluster Name | Enter the name of the vFW cluster. In a single data center, the application name can be the same as the vFW cluster name. In a disaster recovery environment, we recommend that you include the data center information in the vFW cluster name to simplify O&M. Example: nfv poc az1. _ _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | Select a region from the drop-down list. |
| Zone | Select a zone from the drop-down list. Create a vFW cluster on the ECS cluster in the data center. |
| CIDR | Select a CIDR block from the drop-down list, which indicates the NE VPC in which the vFW cluster is created. If no CIDR block is created, the list is empty. |
| Deployment Type | Select a cluster deployment mode to meet your business requirements: Active-Standby: In this high-availability mode, two vFW ECS instances are used for disaster recovery. This mode consumes twice the vFW capacity consumed by the standalone mode. Standalone: In this mode, only one vFW ECS instance is used. This mode does not provide high availability and consumes the vFW capacity. |
| Dedicated Host | Specify whether to deploy the cluster on a dedicated host. No: The cluster is randomly deployed on ECS instances. Yes: You need to specify a dedicated host group and a dedicated host. |
| Network Type | Default value: 25 G. |
| CPU Type | You can choose Intel/X86 orHG /X86. This parameter allows you to choose the ECS cluster that uses the specified CPU type. |

| VFW Specification | Select a vFW specification that meets the preceding network and CPU type conditions from the drop-down list. This parameter indicates the maximum throughput of the vFW cluster for large packets, which consumes the equivalent firewall capacity quota. |
|---|---|
| ECS Specification | Select an ECS specification that meets the preceding network and CPU type conditions from the drop-down list. |
| ECS Image ID | Select the image used by the vFW cluster from the drop-down list. |
| Description | Enter the description of the cluster. We recommend that you include the business, department, and organization information in the description so that the administrator can easily identify the businesses protected by the vFW cluster. |

> **Note:** The values of the CPU Type, VFW Specification, ECS Specification, and ECS Image ID parameters vary depending on the environment and Apsara Stack version. Specify these parameters based on the actual business requirements.

2. After you confirm the configuration, click **OK**. Then, the system automatically verifies the
capacity and quota. If the capacity is sufficient, the operation succeeds and a new NFV Cloud Firewall application is displayed in the list. The status of the vFW cluster changes to
**Creating**.
3. Click the task ID in the **Task ID** column of the application to go to the Workflow page. On
this page, you can view the progress of the cluster creation task. When the subtasks
**ecs_start** and **eni_attach** enter the **Successful** state, the cluster is created.
4. Return to the **Firewalls** page. The NFV Cloud Firewall application is displayed. When the
status of the vFW cluster changes to **Running**, click the application name to go to the application details page. You can view the health status of the vFW ECS instance in the
**Health Status** column. If **Healthy** is displayed, the cluster service functions as expected.
You can then proceed to the next step. If not, the cluster service is not ready. Wait patiently. Common prompts:
**Quota check not passed**: The capacity usage exceeds the specified quota. In this case,
use the admin account to log in to the Apsara Uni-manager Management Console and adjust the NFV Cloud Firewall capacity quota for the current organization.
**cluster capacity reach license limit**: The capacity usage exceeds the total capacity. In
this case, increase the NFV Cloud Firewall capacity by placing a purchase order.

**Step 5: Create endpoints**

An endpoint is equivalent to an interface used by NFV Cloud Firewall to connect to a VPC. It occupies an IP address from the VPC and serves as the next hop for inter-VPC communication. All match traffic is automatically redirected to NFV Cloud Firewall, and then inspected and matched against access control policies. Two processes are involved to create an endpoint:
**Process on the cloud platform side**: An elastic network interface (ENI) is created. You
can view the ENI information by checking the ENI whose description is **Interface for**
**fastpath ft-int-onp use by nfv forbid to operate** on the **ENIs** page of the **ECS** console
in the Apsara Uni-manager Management Console. This process logically associates the endpoint with the VPC.
**Process on the NFV Cloud Firewall side** : A vFW interface is automatically created. You
can use the vFW account to access the NFV Cloud Firewall console or CLI and then view the configuration of the vFW interface. This process logically associates the endpoint with the vFW cluster.

> **Note:** The number of endpoints supported by NFV Cloud Firewall depends on the ECS specification you selected when you create the vFW cluster. The upper limit and current usage displayed in the console prevail. When the upper limit is reached, new endpoints can no longer be created.

**Create an endpoint for vSwitch1 in VPC1**

1. Go to the NFV Cloud Firewall application details page. In the **Endpoint** section, click
**Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint
for vSwitch1 in VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1 vsw1. _ |
| Organization | Select an organization from the drop-down list. In this example, NFV POC1 is selected. _ |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the virtual firewall (vFW) cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. In this example, vSwitch1 is selected. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1 vsw1. _ _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

**Create an endpoint for vSwitch1-2 in VPC1**

1. In the **Endpoint** section, click **Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint
for vSwitch1-2 in VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1 vsw1-2. _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. In this example, vSwitch1-2 is selected. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1 vsw1-2. _ _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.
After the configuration is completed, the endpoint and vFW interface enter the following states.

**Step 6: Create vFW routers (check only)**

In vSwitch-vSwitch protection scenarios, the vFW interface is configured with routes that directly point to the CIDR blocks of the vSwitches. Therefore, you do not need to add static routes.

**Step 7: Create a vFW web portal and log in to the vFW**

**(required only for the first time)**

A web portal is used to access the web interface of NFV Cloud Firewall over HTTPS. In a highavailability cluster, each vFW ECS instance requires a web portal. By default, you need only to access the primary node of the cluster to complete the operation. When an HA switchover is triggered, you need to access the secondary node of the cluster. You can use one of the following types of web portals to access NFV Cloud Firewall. You can create only one web portal of each type.
**Classic network**: After the web portal is created, a classic network IP address is displayed.
The web portal is connected to the web port and SSH port of the vFW ECS instance through a Server Load Balancer (SLB) instance deployed in the classic network. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.
**VPC**: After the web portal is created, a vSwitch IP address in the VPC is displayed. The web
portal is connected to the web port and SSH port of the vFW ECS instance through an SLB instance deployed in the VPC. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.

**Create a vFW web portal**

**Classic network web portal**

1. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the first ECS instance.
2. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.
3. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the second ECS instance.
4. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.

**VPC web portal**

If your O&M network has access to a VPC, you can also create a VPC web portal in the VPC to access the vFW ECS instance.

> **Important:** Do not create a VPC web portal in the production VPC that is connected to NFV Cloud Firewall in case route conflicts occur.

Refer to the classic network web portal procedure, go to the access mode details pages of the two ECS instances, and complete the following steps to create a VPC web portal for each ECS instance.
1. In the **VPC** section, click **Create**.
2. In the **Create VPC Network Access Method** dialog box, set **Vswitch ID** to the ID of a
vSwitch in the VPC. Make sure that the vSwitch has idle IP addresses.

**Log in to the vFW**

Use a browser to access the web URL of the vFW. Then, the login page of the vFW is displayed. In the upper-right corner of the page shows whether the current device is the primary device or the secondary device. You must log in to the primary device first. Enter the default username and password, which are both admin. After you are logged in, you are required to change the default password. After the change, the new password is synchronized to the secondary device. After you log in to the vFW again, check the hardware platform information and license. Make sure that the authorization is valid and proceed.

**Step 8: Configure vFW access control policies**

By default, NFV Cloud Firewall blocks traffic from all sources. To enable intercommunication, you need to configure access control policies to permit access from specific sources. In this scenario, configure a policy to permit ECS1 to access ECS1-2 and enable logging to generate access records. In a production environment, we recommend that you do not enable logging for all access control policies.
1. In the Apsara Uni-manager Management Console, choose **Policy > Security Policy >**
**Policy** and then choose **New > Policy**.
2. Configure the following parameters to create a policy to permit ECS1 to access ECS1-2, and
click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy. |
| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Destination Address | Create an address object named ECS1-2, which contains the IP address of ECS1-2 ( 10.1.2.1 ). |
| Service | Select Any. |

| Action | Select Permit. |
|---|---|
| Options | Click Options, and select Session start and Session end for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

3. **Enable session logging for the vFW** : In the Apsara Uni-manager Management Console,
choose **Monitor > Log > Session Log** and click **Configure**. In the right-side **Session** panel, turn on **Enable**. If you want to view logs in the console, select **Local Database**. If you want to view logs at the CLI, select **Cache**.

**Important**

> When session logging is disabled for the vFW, even if you have enabled logging in the access control policy, you cannot find any records on the log query page. You can view only the number of policy hits.

**Step 9: Create traffic redirection routes**

Types of traffic redirection routes:
**VPC-VPC**: In VPC-VPC protection scenarios, create traffic redirection routes on NFV Cloud
Firewall and publish the routes to the specified VPC route table.
**VS-VS**: In vSwitch-vSwitch protection scenarios (scenario in this topic), create traffic
redirection routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
**VPC-IDC**: In VPC-data center protection scenarios, create traffic redirection routes on NFV
Cloud Firewall and publish the routes to the specified VPC route table.
1. After you confirm that the configuration in the preceding steps is correct, log in to the **NFV**
**Cloud Firewall** console of the Apsara Uni-manager Management Console and go to the
**Route Configuration** page. Then, choose **Create Traffic Diversion Route > VS-VS**.

> **Warning:** **If you perform this operation in a production environment, make sure that** **the specifications of the vFW meet the expectation. If the volume of business** **traffic to redirect exceeds the maximum throughput of the vFW, the network** **latency increases and packet loss occurs.**

2. Configure the following parameters to configure a route to redirect vSwitch-vSwitch traffic
and click **OK**.

| Parameter | Description |
|---|---|
| Organization | Select an organization from the drop-down list. |

| Resource Set |   | Select a resource set from the drop-down list. |
|---|---|---|
| Area |   | Select a region from the drop-down list. |
| Name |   | Enter a name for the custom route. |
| VPC |   | Select a VPC from the drop-down list. In this example, VPC1 is selected. |
| VPC CIDR Block |   | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
| Bilateral Route |   | By default, traffic redirection is configured for only one VPC. You can also turn on Bilateral Route to add traffic redirection routes to the route tables of the two vSwitches. In this example, Bilateral Routing is turned on and traffic redirection is configured for vSwitch1 and vSwitch1-2 at a time. |
| Local Inform ation | Route Name | We recommend that you enter a name to indicate the destination vSwitch in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. In this example, enter route to vsw1-2. _ _ |
|   | vSwitch | Select a vSwitch from the drop-down list. In this example, vSwitch1 is selected. |
|   | Routing Table | After you select a vSwitch, the route table associated with the vSwitch is automatically displayed. You cannot modify this parameter. |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of vSwitch1-2, which is 10.1.2.0/24 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |

|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|---|---|---|
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |
|   | Route Name | We recommend that you enter a name to indicate the destination vSwitch in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. In this example, enter route to vsw1. _ _ |
|   | vSwitch | Select a vSwitch from the drop-down list. In this example, vSwitch1-2 is selected. |
|   | Routing Table | After you select a vSwitch, the route table associated with the vSwitch is automatically displayed. You cannot modify this parameter. |
| Peer Inform ation |   |   |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of vSwitch1, which is 10.1.1.0/24 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |

After you complete the configuration, the **Route Status** column of the routes displays
**Unpublish**. In this case, the O&M engineer needs to complete adding and checking all
routes and then publish the routes one after one or in batches. This feature allows you to perform route configuration and traffic redirection within two time windows in case you do not have sufficient time to complete the two tasks within the same time window.
3. Click **Publish** in the **Operation** column of the desired traffic redirection route and click **OK**.
Wait until the status of the route changes from **Publishing** to **Published**. This means that the route is in effect. This way, the traffic between vSwitch1 and vSwitch1-2 is redirected to NFV Cloud Firewall. After the traffic redirection route is published, log in to the **VPC** console, go to the **Route**
**Tables** page, and view the status of the routes in the route tables of vSwitch1 and vSwitch1-
2. You can find that the two routes whose mask length is N+1 are published from NFV Cloud Firewall. Their next hops are set to the elastic network interface (ENI) of the endpoint. The
**route names** you entered are displayed in the route descriptions to simplify O&M.
System route table of vSwitch1: Custom route table of vSwitch1-2:

**Step 10: Verify the business**

1. Log in to ECS1 and initiate a business test:
i. Run the `ping <ECS1-2 IP>` command on ECS1 to test the connectivity to ECS1-2. The ping succeeds. ii. Run the `ssh root@<ECS1-2 IP>` command on ECS1 to access ECS1-2 over SSH. The operation succeeds.
2. Log in to the Apsara Uni-manager Management Console to view logs.
Choose **Policy > Security Policy > Policy**, find the desired policy, and check whether the **number of hits** increases. Choose **Monitor > Log > Session Log**, set **Time** to **Real-time**, and check whether ping (corresponding to ICMP) and SSH (corresponding to TCP) logs are generated. In addition, check whether session logs containing source and destination IP addresses related to the test are generated.

**Other scenarios**

**Scenario: When a VPC contains multiple vSwitches, do I need**

**to create an endpoint for each vSwitch on NFV Cloud Firewall?**

**Solution**: Yes. In vSwitch-vSwitch protection scenarios, a vSwitch is equivalent to a VPC.
Therefore, you need to create an endpoint for each vSwitch and associate a separate route table with each vSwitch on NFV Cloud Firewall.

#### 3.6.4 Configure the bypass and restoration features of NFV Cloud Firewall

**features of NFV Cloud Firewall**

When an NFV Cloud Firewall cluster is faulty or requires emergency debugging, you may need the business traffic to bypass security devices (Express Connect is required) in order to ensure network connectivity and immediately restore access control after the issue is fixed. To meet this goal, you can use the **bypass** and **restoration** features of NFV Cloud Firewall to batch withdraw and republish traffic redirection routes. This way, business traffic is switched between traffic redirection routes and backup routes to implement failover and restoration.

**Background information**

NFV Cloud Firewall can connect virtual private clouds (VPCs) without the need for Express Connect. In extreme scenarios, such as when the entire NFV Cloud Firewall cluster is unavailable, communication will be interrupted and cannot be quickly restored if no backup routes are configured. To address this issue, NFV Cloud Firewall provides the **bypass** and **restoration** features, which can be used in combination with Express Connect to implement secure and efficient failover and restoration. You can also use other backup tunneling service or configure backup routes to achieve this goal.
**Bypass**: automatically withdraws all cross-VPC traffic redirection routes published by the
NFV Cloud Firewall cluster, including VPCs that belong to the current organization and VPCs that you are authorized to manage in other organizations. This feature fails traffic over to backup routes, such as Express Connect circuits, to quickly restore business communication.
**Restoration**: republishes all traffic redirection routes to redirect east-west traffic to the
NFV Cloud Firewall cluster for access control.

> **Warning:** Do not set NVF Cloud Firewall to the bypass mode when no backup routes are configured because this will result in network interruptions.

**Status of the bypass and restoration features**

When the status of the bypass feature is **Normal**, traffic is redirected to NFV Cloud Firewall as expected. When the status of the bypass feature is **Bypass**, NFV Cloud Firewall runs in bypass mode and traffic is not redirected to NFV Cloud Firewall.

**Implementations and limits**

**Bypass**: The `deleteRouteEntry` API operation of VPC is called to delete traffic redirection
routes concurrently. The deletion task is run by VPC. Due to factors such as the network size, resource usage of cloud services, and actual number of routes, no SLA is guaranteed for route withdrawal on the NFV Cloud Firewall side.
**Restoration**: Traffic redirection routes for different VPCs are republished concurrently.
However, traffic redirection routes for a single VPC are republished one after another.

**Topology**

Organization 1 created VPC1 and VPC2. The CIDR block of VPC1 is `10.1.0.0/16` and it

|   | 10.1.1.1 |
|---|---|
| 10.2.1.0/24 |   |

VPC2 are connected over Express Connect by default. ECS1 can ping and access ECS2 over SSH. To meet security compliance requirements, the organization uses an account that assumes the organization security admin role to create an NFV Cloud Firewall cluster, create endpoints in VPC1 and VPC2, and publish traffic redirection routes. VPC1 and VPC2 are connected through NFV Cloud Firewall and communication between the VPCs is regulated by access control policies. For example, ECS1 can ping ECS2 but ECS1 cannot access ECS2 over SSH. When the NFV Cloud Firewall cluster fails and then recovers from the failure, you can use the bypass and restoration features to switch between different routes to ensure business continuity: When the bypass feature is used, ECS1 and ECS2 can communicate over Express Connect. ECS1 can ping ECS2 and access ECS2 over SSH. When the restoration feature is used, ECS1 and ECS2 can communicate through NFV Cloud Firewall. ECS1 can ping ECS2 but cannot access ECS2 over SSH.

| 10.1.0.0/16 vSwitch1 10.1.1.0/24 Destination Next Hop to VPC2/17 NFV to VPC2/16 Express ConnEeCctS1 ep1 |   |
|---|---|

|   | V | PC2 |
|---|---|---|
| 10.2.0.0/16 vSwitch2 ct 10.2.1.0/24 VRouter Destination to VPC1/17 ECS2 to VPC1/16 Expr ep2 | 10.2.0 |   |

Backup Route for Failover

| v 1 |   |   |
|---|---|---|
|   | v 1 |   |
|   |   | t Hop |
|   |   | V |

|   | vSw 10.2.1 |
|---|---|

Express Connect VRouter Organization 1 VFW(M) VFW(S) vFW Network Service Cluster NE VPC (19216810/24)

**Create resources**

Use an account that belongs to the current organization to log in to the Apsara Uni-manager Management Console, switch to the organization admin role, and create VPCs, vSwitches, and Elastic Compute Service (ECS) instances. Create VPC1 and VPC2: Create vSwitch1 and vSwitch2: Create ECS instances and a security group:

> **Important:** In this example, the security group permits traffic from all sources to simplify the configuration. In actual business scenarios, you need to configure the security group to permit traffic based on the business needs of the ECS instances. Do not permit traffic from all sources.

Configure Express Connect: Configure VPC routes (the mask length of the Express Connect route is set to the mask length of the VPC):

**Configure NFV Cloud Firewall**

**Step 1: Create a RAM role (required only for new organizations)**

1. Use an account that can assume the organization security admin role by default to log in to
the Apsara Uni-manager Management Console and choose **Security > Network Security**
**> NFV Cloud Firewall**.
If this is the first time the level-1 organization of the account uses NFV Cloud Firewall, the
**ram role does not exist** message is displayed after you are logged in. In this case, you
need to create a Resource Access Management (RAM) role first.
2. Switch to the role that has permissions on the organization, such as the organization admin
or organization security admin role. You can also use the admin account of the Apsara Unimanager Management Console. Choose **Configurations > Service-linked Roles**, click
**Create Service-linked Role**, configure the following parameters, and click **OK**.
**Service Name:** Select **Cloud Firewall**.
**Authorized Organization Name:** Select the organization on which the role is granted
permissions. In this example, NFV_POC1 is selected.

**Step 2: Check the vFW capacity**

On the **Firewalls** page of the **NFV Cloud Firewall** console, **VFW Capacity: xGbps/nGbps** is displayed in the upper-right corner.
**x Gbps** before the forward slash (**/**): the current capacity used by the organization. If this is
the first time an organization uses NFV Cloud Firewall, **0Gbps** is displayed.
**n Gbps** after the forward slash (**/**): the maximum capacity that the organization can use. If
a number is displayed, the number indicates the maximum capacity, such as **10Gbps** in the following figure. If **-Gbps** is displayed: Scenario 1: No capacity quota for this organization is assigned to the admin account of the Apsara Uni-manager Management Console. The maximum capacity equals the
**logical inventory** allocated to the super account of the Apsara Uni-manager
Management Console. If no **logical inventory** is allocated to the super account, the maximum capacity equals the value of the **Issued** field of NFV Cloud Firewall-ALY00 in

**System Config > Authorization information > Authorized Specifications Details**

of the Apsara Uni-manager Operations Console. Scenario 2: The capacity quota of the admin account for this organization is set to 0. This means that the account is not allowed to create NFV Cloud Firewall clusters. You can create NFV Cloud Firewall clusters only when `Capacity required for creating an` NFV Cloud Firewall cluster + Current capacity used ≤ Total capacity . If not, you need to use the admin account to adjust the NFV Cloud Firewall quota for this organization.

**Step 3: Create a CIDR block (required only during the first time**

**you create an NFV Cloud Firewall cluster)**

If this is the first time you create an NFV Cloud Firewall cluster in a level-1 organization, you need to first create a CIDR block. You can select one or more CIDR blocks that you created when you create the network element (NE) VPC. In most cases, one CIDR block is sufficient within each organization.

> **Important:** We recommend that you use a subnet belonging to `192.168.0.0/16` or
> `172.16.0.0/16` . Do not use a CIDR block that overlaps with that of the production VPC in the organization, in case address conflicts occur.

1. On the **CIDR Management** page of the **NFV Cloud Firewall** console, click **Create CIDR**
and configure the following parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the NE VPC. In this example, entern fv poc1. _ |
| Organization | Select the organization to which the current account belongs. In this example, level-1 organization NFV POC1 is selected. _ |
| Resource Set | Select a resource set. In this example, the default resource set is selected. |
| Area | Select a region. |
| CIDR | Enter a CIDR block. The mask length must be smaller than 26. In this example, enter 192.168.1.0/24. |

2. After you confirm the configuration, click **OK**. After the status of the CIDR block changes
from **processing** to **success**, the CIDR block is created.

**Step 4: Create an NFV Cloud Firewall application**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click **Create Cluster** and
configure the following parameters in the panel that appears to create an NFV Cloud Firewall application. When you create an application, a vFW cluster is simultaneously created.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the NFV Cloud Firewall application. We recommend that you enter an informative name that contains the business information. Example: nfv poc. _ |
| VFW Cluster Name | Enter the name of the vFW cluster. In a single data center, the application name can be the same as the vFW cluster name. In a disaster recovery environment, we recommend that you include the data center information in the vFW cluster name to simplify O&M. Example: nfv poc az1. _ _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | Select a region from the drop-down list. |

| Zone | Select a zone from the drop-down list. Create a vFW cluster on the ECS cluster in the data center. |
|---|---|
| CIDR | Select a CIDR block from the drop-down list, which indicates the NE VPC in which the vFW cluster is created. If no CIDR block is created, the list is empty. |
| Deployment Type | Select a cluster deployment mode to meet your business requirements: Active-Standby: In this high-availability mode, two vFW ECS instances are used for disaster recovery. This mode consumes twice the vFW capacity consumed by the standalone mode. Standalone: In this mode, only one vFW ECS instance is used. This mode does not provide high availability and consumes the vFW capacity. |
| Dedicated Host | Specify whether to deploy the cluster on a dedicated host. No: The cluster is randomly deployed on ECS instances. Yes: You need to specify a dedicated host group and a dedicated host. |
| Network Type | Default value: 25 G. |
| CPU Type | You can choose Intel/X86 orHG /X86. This parameter allows you to choose the ECS cluster that uses the specified CPU type. |
| VFW Specification | Select a vFW specification that meets the preceding network and CPU type conditions from the drop-down list. This parameter indicates the maximum throughput of the vFW cluster for large packets, which consumes the equivalent firewall capacity quota. |
| ECS Specification | Select an ECS specification that meets the preceding network and CPU type conditions from the drop-down list. |
| ECS Image ID | Select the image used by the vFW cluster from the drop-down list. |
| Description | Enter the description of the cluster. We recommend that you include the business, department, and organization information in the description so that the administrator can easily identify the businesses protected by the vFW cluster. |

> **Note:** The values of the CPU Type, VFW Specification, ECS Specification, and ECS Image ID parameters vary depending on the environment and Apsara Stack version. Specify these parameters based on the actual business requirements.

2. After you confirm the configuration, click **OK**. Then, the system automatically verifies the
capacity and quota. If the capacity is sufficient, the operation succeeds and a new NFV Cloud Firewall application is displayed in the list. The status of the vFW cluster changes to
**Creating**.
3. Click the task ID in the **Task ID** column of the application to go to the Workflow page. On
this page, you can view the progress of the cluster creation task. When the subtasks
**ecs_start** and **eni_attach** enter the **Successful** state, the cluster is created.
4. Return to the **Firewalls** page. The NFV Cloud Firewall application is displayed. When the
status of the vFW cluster changes to **Running**, click the application name to go to the application details page. You can view the health status of the vFW ECS instance in the
**Health Status** column. If **Healthy** is displayed, the cluster service functions as expected.
You can then proceed to the next step. If not, the cluster service is not ready. Wait patiently. Common prompts:
**Quota check not passed**: The capacity usage exceeds the specified quota. In this case,
use the admin account to log in to the Apsara Uni-manager Management Console and adjust the NFV Cloud Firewall capacity quota for the current organization.
**cluster capacity reach license limit**: The capacity usage exceeds the total capacity. In
this case, increase the NFV Cloud Firewall capacity by placing a purchase order.

**Step 5: Create endpoints**

An endpoint is equivalent to an interface used by NFV Cloud Firewall to connect to a VPC. It occupies an IP address from the VPC and serves as the next hop for inter-VPC communication. All match traffic is automatically redirected to NFV Cloud Firewall, and then inspected and matched against access control policies. Two processes are involved to create an endpoint:
**Process on the cloud platform side**: An elastic network interface (ENI) is created. You
can view the ENI information by checking the ENI whose description is **Interface for**
**fastpath ft-int-onp use by nfv forbid to operate** on the **ENIs** page of the **ECS** console
in the Apsara Uni-manager Management Console. This process logically associates the endpoint with the VPC.
**Process on the NFV Cloud Firewall side** : A vFW interface is automatically created. You
can use the vFW account to access the NFV Cloud Firewall console or CLI and then view the configuration of the vFW interface. This process logically associates the endpoint with the vFW cluster.

> **Note:** The number of endpoints supported by NFV Cloud Firewall depends on the ECS specification you selected when you create the vFW cluster. The upper limit and current usage displayed in the console prevail. When the upper limit is reached, new endpoints can no longer be created.

**Create an endpoint in VPC1**

1. Go to the NFV Cloud Firewall application details page. In the **Endpoint** section, click
**Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1. |
| Organization | Select an organization from the drop-down list. |

| Resource Set | Select a resource set from the drop-down list. |
|---|---|
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

**Create an endpoint in VPC2**

1. In the **Endpoint** section, click **Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC2.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC2. |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the region of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC2 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc2. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.
After you complete the configuration, the endpoints and vFW interfaces enter the following states.

**Step 6: Create vFW routers**

By default, a vFW interface is configured with a direct route that points to the CIDR block of the vSwitch. However, you still need to add static routes to the vFW to route traffic to the CIDR blocks of VPC1 and VPC2.

**Add a route that routes traffic from the vFW to VPC1**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC1.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC1 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC1. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.

**Add a route that routes traffic from the vFW to VPC2**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC2.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC2 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |

| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
|---|---|
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC2. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc2. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.
After the configuration is completed, the vFW routers enter the following states.

**Step 7: Create a vFW web portal and log in to the vFW**

**(required only for the first time)**

A web portal is used to access the web interface of NFV Cloud Firewall over HTTPS. In a highavailability cluster, each vFW ECS instance requires a web portal. By default, you need only to access the primary node of the cluster to complete the operation. When an HA switchover is triggered, you need to access the secondary node of the cluster. You can use one of the following types of web portals to access NFV Cloud Firewall. You can create only one web portal of each type.
**Classic network**: After the web portal is created, a classic network IP address is displayed.
The web portal is connected to the web port and SSH port of the vFW ECS instance through a Server Load Balancer (SLB) instance deployed in the classic network. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.
**VPC**: After the web portal is created, a vSwitch IP address in the VPC is displayed. The web
portal is connected to the web port and SSH port of the vFW ECS instance through an SLB instance deployed in the VPC. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.

**Create a vFW web portal**

**Classic network web portal**

1. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the first ECS instance.
2. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.
3. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the second ECS instance.
4. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.

**VPC web portal**

If your O&M network has access to a VPC, you can also create a VPC web portal in the VPC to access the vFW ECS instance.

> **Important:** Do not create a VPC web portal in the production VPC that is connected to NFV Cloud Firewall in case route conflicts occur.

Refer to the classic network web portal procedure, go to the access mode details pages of the two ECS instances, and complete the following steps to create a VPC web portal for each ECS instance.
1. In the **VPC** section, click **Create**.
2. In the **Create VPC Network Access Method** dialog box, set **Vswitch ID** to the ID of a
vSwitch in the VPC. Make sure that the vSwitch has idle IP addresses.

**Log in to the vFW**

Use a browser to access the web URL of the vFW. Then, the login page of the vFW is displayed. In the upper-right corner of the page shows whether the current device is the primary device or the secondary device. You must log in to the primary device first. Enter the default username and password, which are both admin. After you are logged in, you are required to change the default password. After the change, the new password is synchronized to the secondary device. After you log in to the vFW again, check the hardware platform information and license. Make sure that the authorization is valid and proceed.

**Step 8: Configure vFW access control policies**

By default, NFV Cloud Firewall blocks traffic from all sources. To enable intercommunication, you need to configure access control policies to permit access from specific sources. In this scenario: Configure a policy to permit ping packets from ECS 1 to ECS 2 and enable logging to generate access records. Configure a policy to deny access from ECS1 to ECS2 over SSH and enable logging to generate access records.

> **Note:** In a production environment, we recommend that you do not enable logging for all access control policies.

1. In the Apsara Uni-manager Management Console, choose **Policy > Security Policy >**
**Policy** and then choose **New > Policy**.
2. Configure the following parameters to create a policy to permit ping packets from ECS1 to
ECS2, and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy. |
| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC2 is selected. |
| Destination Address | Create an address object named ECS2, which contains the IP address of ECS2 ( 10.2.1.1 ). |
| Service | Select ICMP. |
| Action | Select Permit. |
| Options | Click Options, and select Session start and Session end for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

3. Choose **New > Policy** again, configure the following parameters to block access from
ECS1 to ECS2 over SSH, and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy. |
| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC2 is selected. |

| Destination Address | Create an address object named ECS2, which contains the IP address of ECS2 ( 10.2.1.1 ). |
|---|---|
| Service | Select SSH. |
| Action | Select Deny. |
| Options | Click Options, and select Deny for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

4. **Enable session logging for the vFW** : In the Apsara Uni-manager Management Console,
choose **Monitor > Log > Session Log** and click **Configure**. In the right-side **Session** panel, turn on **Enable**. If you want to view logs in the console, select **Local Database**. If you want to view logs at the CLI, select **Cache**.

> **Important:** When session logging is disabled for the vFW, even if you have enabled logging in the access control policy, you cannot find any records on the log query page. You can view only the number of policy hits.

**Step 9: Create traffic redirection routes**

**VPC-VPC**: In VPC-VPC protection scenarios (scenario in this topic), create traffic redirection
routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
**VS-VS**: In vSwitch-vSwitch protection scenarios, create traffic redirection routes on NFV
Cloud Firewall and publish the routes to the specified VPC route table.
**VPC-IDC**: In VPC-data center protection scenarios (scenario in this topic), create traffic
redirection routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
1. After you confirm that the configuration in the preceding steps is correct, log in to the **NFV**
**Cloud Firewall** console of the Apsara Uni-manager Management Console and go to the
**Route Configuration** page. Then, choose **Create Traffic Diversion Route > VPC-VPC**.

> **Warning:** **If you perform this operation in a production environment, make sure that** **the specifications of the vFW meet the expectation. If the volume of business** **traffic to redirect exceeds the maximum throughput of the vFW, the network** **latency increases and packet loss occurs.**

2. Configure the following parameters to configure a route to redirect VPC-VPC traffic and
click **OK**.

| Parameter |   | Description |
|---|---|---|
| Organization |   | Select an organization from the drop-down list. |
| Resource Set |   | Select a resource set from the drop-down list. |
| Area |   | Select a region from the drop-down list. |
| Name |   | Enter a name for the custom route. |
| Bilateral Route |   | By default, traffic redirection is configured for only one VPC. You can also turn on Bilateral Route to configure traffic redirection for two interconnected VPCs. In this example, Bilateral Routing is turned on and traffic redirection is configured for VPC1 and VPC2 at a time. |
| Local Inform ation | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to vpc2 in this example. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC1 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC2, which is 10.2.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |

|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|---|---|---|
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |
|   | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to vpc1 in this example. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC2 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
| Peer Inform ation | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block | Enter the destination CIDR block. In this example, enter the CIDR block of VPC1, which is 10.1.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |

After you complete the configuration, the **Route Status** column of the routes displays
**Unpublish**. In this case, the O&M engineer needs to complete adding and checking all
routes and then publish the routes one after one or in batches. This feature allows you to perform route configuration and traffic redirection within two time windows in case you do not have sufficient time to complete the two tasks within the same time window.
3. Click **Publish** in the **Operation** column of the desired traffic redirection route and click **OK**.
Wait until the status of the route changes from **Publishing** to **Published**. This means that the route is in effect. This way, the outbound traffic of VPC1 and VPC2 is redirected to NFV Cloud Firewall. After the traffic redirection route is published, log in to the **VPC** console, go to the **Route**
**Tables** page, and view the status of the routes in the route tables of VPC1 and VPC2.
You can find that the two routes whose mask length is N+1 are published from NFV Cloud Firewall. Their next hops are set to the elastic network interface (ENI) of the endpoint. The
**route names** you entered are displayed in the route descriptions to simplify O&M.
Route table of VPC1: Route table of VPC2:

**Step 10: Verify the business**

1. Log in to ECS1 and initiate a business test:
i. Run the `ping <ECS2 IP>` command on ECS1 to test the connectivity to ECS2. The ping succeeds. ii. Run the `ssh <ECS2 IP>` command on ECS1 to log in to ECS2 over SSH. The operation failed.
2. Log in to the Apsara Uni-manager Management Console to view logs.
Choose **Policy > Security Policy > Policy**, find the desired policy, and check whether the **number of hits** increases. Choose **Monitor > Log > Session Log**, set **Time** to **Real-time**, and check whether ping (corresponding to ICMP) and SSH (corresponding to TCP) logs are generated. In addition, check whether session logs containing source and destination IP addresses related to the test are generated.

**Perform the bypass and restoration operations**

**Obtain the organization UID (alias of the Apsara Stack tenant**

**account)**

The bypass or restoration operation requires you to enter a verification code, which is the organization UID. You need to enter the UID of the organization to which the current account belongs, which is also known as the alias of the Apsara Stack tenant account. In the upper-right corner, click the user icon. On the **User Information** page, record the value of the **Tenant Account Alias** field.

**Perform the bypass operation**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click the name of the desired
application to go to the application details page. In the **Bypass** section, click **One-click**
**Bypass**.
2. In the right-side panel, enter the organization UID **alias of the Apsara Stack tenant**
**account** into the **Captcha** field and click **OK**.
After **Bypass Status** changes from **Normal** to **Bypassing** and then to **Bypassed**, the bypass operation is completed.
3. Check whether the bypass operation is successful.
i. View the route tables of the VPCs. The result shows that all traffic redirection routes published by NFV Cloud Firewall are automatically withdrawn. As shown in the following figure, only /16 Express Connect routes exist in the route table. Traffic is preferably routed over Express Connect. Route table of VPC1: Route table of VPC2: ii. Log in to ECS1 and initiate a business test: Ping ECS2 from ECS1. The ping succeeds. Access ECS2 from ECS1 over SSH. ECS1 can access ECS2. iii. Log in to the NFV Cloud Firewall console. No log is generated.

**Perform the restoration operation**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click the name of the desired
application to go to the application details page. In the **Bypass** section, click **One-click**
**Revert**.
2. In the right-side panel, enter the organization UID **alias of the Apsara Stack tenant**
**account** into the **Captcha** field and click **OK**.
After **Bypass Status** changes from **Bypassed** to **Recovering** and then to **Normal**, the restoration operation is completed.
3. Check whether the restoration operation is successful.
i. View the route tables of the VPCs. The result shows that all traffic redirection routes are republished by NFV Cloud Firewall. As shown in the figure, in the routing table, the /17 routes published by NFV Cloud Firewall have the highest priority. Traffic is redirected to NFV Cloud Firewall. Route table of VPC1: Route table of VPC2: ii. Log in to ECS1 and initiate a business test: Ping ECS2 from ECS1. The ping succeeds. Access ECS2 from ECS1 over SSH. ECS1 failed to access ECS2. iii. Log in to the NFV Cloud Firewall console. Logs are generated.

**Summary**

Before you configure NFV Cloud Firewall for VPC-VPC protection, you can add an Express Connect circuit between the VPCs as a backup route for failover when the NFV Cloud Firewall cluster fails. The Express Connect circuit can be used together with the bypass and restoration features to quickly respond to emergencies and restore businesses. You can deploy an Express Connect circuit as a backup route before you enable NFV Cloud Firewall or dynamically add one based on the VPC communication information when the NFV Cloud Firewall cluster fails. The solution must take into consideration the number of VPCs, the number of routes, and the requirements on business continuity or fault tolerance.

**In zone-disaster recovery scenarios, pay close attention to the traffic redirection**

**configuration of NFV Cloud Firewall. The primary cluster publishes two N+1**

**routes and the secondary cluster publishes one N route. In addition, pay**

**attention to the priorities of the traffic redirection routes and backup routes,**

**which are determined by their mask lengths. Make sure that the routes do not**

**conflict with each other. You can also divide the destination CIDR block on NFV**

**Cloud Firewall before you add routes to ensure that the business traffic precisely**

**matches the routes.**

The reliability of NFV Cloud Firewall modes in descending order is as follows: single-data center standalone mode (1 x 1) < single-data center dual-node HA mode (1 x 2) < disaster recovery cluster + standalone mode (2 x 1) < disaster recovery cluster + dual-node HA mode (2 x 2).

#### 3.6.5 VPC-data center protection by NFV Cloud Firewall in a single data center

**Cloud Firewall in a single data center**

In this best practice, a production virtual private cloud (VPC) needs to securely communicate with a data center and data transmission in the east-west direction must be regulated by firewall policies. In this case, you need to use NFV Cloud Firewall together with the HUB_VPC architecture to centrally protect communication between the production VPC and data center.

**Introduction to VPC-data center protection**

To use the VPC-IDC protection architecture of NFV Cloud Firewall, you need to create a HUB_VPC that serves as a hub between NFV Cloud Firewall and the data center. All outbound traffic of the production VPC is routed to and inspected by NFV Cloud Firewall and then transmitted to the data center by the HUB_VPC. This architecture divides the network into two components: Integration of the HUB_VPC with the data center network: The HUB_VPC is connected to the network of the data center by using a standard VPC-data center network integration solution. In a scenario where there is only one data center, the active/active or active/standby mode is usually used on the data center side. When you connect the HUB_VPC and data center, you still need to add a static route that points to the CIDR block of the HUB_VPC to the route table of the virtual border router (VBR). This ensures that core switches (CSWs) can complete packet encapsulation and both sides can communicate with each other. Traffic redirection by NFV Cloud Firewall: The production VPC, NFV Cloud Firewall, and HUB_VPC are connected in a way similar to VPC-VPC protection. You need to create endpoints to establish connections and configure traffic redirection routes. After the specific routes are published to the route tables of the production VPC and HUB_VPC, outbound traffic of the production VPC and data center are redirected to NFV Cloud Firewall. The solution that uses a VPC as the hub requires you to integrate the HUB_VPC and the network of the data center only once. Then, traffic from other VPCs is automatically redirected to the HUB_VPC and then routed to the data center. This saves you the need to repeatedly perform VPC-data center network integration. You only need to add routes pointing to the CIDR blocks of the new VPCs to the route table on the data center side, the route tables of the CSWs, and the route table of the HUB_VPC.

> **Important:** Data is exchanged through the HUB_VPC between the production VPC and data center, which means that the network link between two ends (the production VPC and the data center) becomes invisible. This affects traffic detection performed by Apsara Stack Security and traffic detection and analysis on the CSW side.

**Network Integration That Connects**

**Traffic Redirection by**

**HUB_VPC and Data Center**

Destination Next Hop to_IDC 172.16.0.0/16 IDC Production VPC HUB_VPC to_VPC 10.1.0.0/16 VRouter 10.1.0.0/16 192.168.33.0/16 to_hubvpc 192.168.33.0/24 VRouter Destination CSW

| n A D | ne cces evic |
|---|---|

to_VPC 10.1.0.0/1 Destination Next Hop Destination Next Hop to_IDC 172.16.0.0/16 CSW to_IDC 172.16.0.0/17 NFV to_IDC 172.16.128.0/17 NFV to_VPC 10.1.0.0/17 NFV to_VPC 10.1.128.0/17 NFV

| .0/1 | 7 |
|---|---|

|   | 10.1.1.0/24 ECS1 ep1 |
|---|---|

hub_vSwitch VBR Data Center VRouter 192.168.33.0/24 172.16.0.0/16 ep2 VFW(M) VFW(S) vFW Network Service Cluster NE VPC (192.168.1.0/24)

**Topology**

In this scenario, a single Network Function Virtualization (NFV) cluster and a single HUB_VPC are used. An enterprise has the following resources deployed in the cloud and data center:

| 10.1.0.0/16 | , |
|---|---|
| 1 is |   |

In the cloud: The CIDR block of the production VPC is `10.1.0.0/16` , the CIDR block of the vSwitch1 is `10.1.1.0/24` , and the IP address of ECS1 is `10.1.1.1` . In the data center: The CIDR block of the data center is `172.16.0.0/16` and the server IP address is `172.16.1.1` . The enterprise needs to connect the production VPC to the network of the data center for intercommunication and protect the data exchanged between them. To ensure connectivity and security, NFV Cloud Firewall is used in combination with the HUB_VPC architecture. Prepare the HUB_VPC `192.168.33.0/24` . Follow the standard procedure defined by Apsara Stack to integrate the HUB_VPC with the network of the data center. Use CSW1, CSW2, two VBRs, and two Express Connect circuits to ensure the high availability of intercommunication. Use an account that assumes the organization security admin role to create an NFV Cloud Firewall cluster. Create endpoints in VPC1 and HUB_VPC, and publish traffic redirection routes. This way, VPC1 and the data center can securely communicate through NFV Cloud Firewall, and ECS1 and the server in the data center can communicate.

**Network Integration That Connects HUB_VPC and Data Center**

**Traffic Redirection by NFV Cloud Firewall**

| NE VPC 192.168.1.0/24 V 10P .C 11 .0.0/16 Dest t tin o o_a _I Vt Di Po C Cn 11 7 1 2 0 . .1 1 6 . 0. 0 . 0. 0 / 1/ 1 6 6 H U B _V VN P Destination Next Hop tt oo __II DD CC 11 77 22 .. 11 66 .. 10 2.0 8/ .1 07 NN FF VV /1 7 VFW(M) vSwitch1 10.1.1.0/24 ECS1 vFW Network Service Clust ep-vpc1 VFW(S) | CSW1 Destination Next Hop ttt ooo ___ hVID uPC bC 11 7 1 c2 0 1. .1 1 96 . 20. .0 . 10. 60 / 81/1 .6 36 V R o u I t tD e eC r v p 3 . 0 / 2 4 V R o u r P Ce Cx 1t Hop 192.168H .U 33B ._0V /P 1C VBR 6 Data Center 172.16.0.0 Destination Next Hop Express t t to o o_ _ _I V VD P PC C C 1 11 7 1 12 0 0. . .1 1 16 . .0 1.0 . 20. 80 / .1/ 01 7 /6 1 7 C N NS F FW V V Dest ti on _a Vti Po Cn 1 1 0 . 1 . 0 . Connect 192h .1u 6b 8_.v 3S 3w .0it /c 2h 4 VRouter AA ctc it viv ee /S/A taADc ncetci dvveibecs yes Connect Cir c1 t uiit u c 2riC Server Express 172.16.1.1/16 er ep-idc VBR Destination Next Hop ttt ooo ___ hVID uPC bC 11 7 1 c2 0 1. .1 1 96 . 20. .0 . 10. 60 / 81/1 .6 36 V R o u I t tD e eC r v p 3 . 0 / 2 4 V R o u r CSW2 |
|---|---|

|   | Destination t to o_ _I VD PC C 11 7 12 0. .1 16 .0.0 .0.0 /1/1 66 VFW(M) vFW Network Service VFW(S) |   |   |
|---|---|---|---|
|   |   | VFW(M) |   |
|   |   |   | vFW Network |
|   |   | VFW(S) |   |

**Create resources**

Use an account that belongs to the current organization to log in to the Apsara Uni-manager Management Console, switch to the organization admin role, and create resources such as VPCs, vSwitches, and Elastic Compute Service (ECS) instances. Create VPC1 and HUB_VPC: Create vSwitch1 and hub_vSwitch: Create an ECS instance and a security group. Assets other than resources in the cloud, such as servers in the data center, are not displayed.

> **Important:** In this example, the security group permits traffic from all sources to simplify the configuration. In actual business scenarios, you need to configure the security group to permit traffic based on the business needs of the ECS instances. Do not permit traffic from all sources.

**Standard VPC-data center network integration**

Perform standard VPC-data center network integration to connect the HUB_VPC to the data center: Configuration in the cloud: typically completed by the on-site delivery time or with the assistance of the technical account manager (TAM). Device configuration in the data center: completed by the networking team on the tenant side. The configuration includes network connections and routes that point to VPC1. Details are not described in this topic. VBR routes on CSWs: routes that point to the data center and VPC1, and routes that point to the HUB_VPC. If you do not add these routes, communication issues occur. The following configuration is used in this example: Example of VBR routes on CSWs (Add routes pointing to VPC1 and HUB_VPC after completing network integration): Example of routes added to the route table of the HUB_VPC (Add routes pointing to the data center after completing network integration):

**Configure NFV Cloud Firewall**

**Step 1: Create a RAM role (required only for new organizations)**

1. Use an account that can assume the organization security admin role by default to log in to
the Apsara Uni-manager Management Console and choose **Security > Network Security**
**> NFV Cloud Firewall**.
If this is the first time the level-1 organization of the account uses NFV Cloud Firewall, the
**ram role does not exist** message is displayed after you are logged in. In this case, you
need to create a Resource Access Management (RAM) role first.
2. Switch to the role that has permissions on the organization, such as the organization admin
or organization security admin role. You can also use the admin account of the Apsara Unimanager Management Console. Choose **Configurations > Service-linked Roles**, click
**Create Service-linked Role**, configure the following parameters, and click **OK**.
**Service Name:** Select **Cloud Firewall**.
**Authorized Organization Name:** Select the organization on which the role is granted
permissions. In this example, NFV_POC1 is selected.

**Step 2: Check the vFW capacity**

On the **Firewalls** page of the **NFV Cloud Firewall** console, **VFW Capacity: xGbps/nGbps** is displayed in the upper-right corner.
**x Gbps** before the forward slash (**/**): the current capacity used by the organization. If this is
the first time an organization uses NFV Cloud Firewall, **0Gbps** is displayed.
**n Gbps** after the forward slash (**/**): the maximum capacity that the organization can use. If
a number is displayed, the number indicates the maximum capacity, such as **10Gbps** in the following figure. If **-Gbps** is displayed: Scenario 1: No capacity quota for this organization is assigned to the admin account of the Apsara Uni-manager Management Console. The maximum capacity equals the
**logical inventory** allocated to the super account of the Apsara Uni-manager
Management Console. If no **logical inventory** is allocated to the super account, the maximum capacity equals the value of the **Issued** field of NFV Cloud Firewall-ALY00 in

**System Config > Authorization information > Authorized Specifications Details**

of the Apsara Uni-manager Operations Console. Scenario 2: The capacity quota of the admin account for this organization is set to 0. This means that the account is not allowed to create NFV Cloud Firewall clusters. You can create NFV Cloud Firewall clusters only when `Capacity required for creating an` NFV Cloud Firewall cluster + Current capacity used ≤ Total capacity . If not, you need to use the admin account to adjust the NFV Cloud Firewall quota for this organization.

**Step 3: Create a CIDR block (required only during the first time**

**you create an NFV Cloud Firewall cluster)**

If this is the first time you create an NFV Cloud Firewall cluster in a level-1 organization, you need to first create a CIDR block. You can select one or more CIDR blocks that you created when you create the network element (NE) VPC. In most cases, one CIDR block is sufficient within each organization.

**Important**

> We recommend that you use a subnet belonging to `192.168.0.0/16` or
> `172.16.0.0/16` . Do not use a CIDR block that overlaps with that of the production VPC in the organization, in case address conflicts occur.

1. On the **CIDR Management** page of the **NFV Cloud Firewall** console, click **Create CIDR**
and configure the following parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the NE VPC. In this example, entern fv poc1. _ |
| Organization | Select the organization to which the current account belongs. In this example, level-1 organization NFV POC1 is selected. _ |
| Resource Set | Select a resource set. In this example, the default resource set is selected. |
| Area | Select a region. |
| CIDR | Enter a CIDR block. The mask length must be smaller than 26. In this example, enter 192.168.1.0/24. |

2. After you confirm the configuration, click **OK**. After the status of the CIDR block changes
from **processing** to **success**, the CIDR block is created.

**Step 4: Create an NFV Cloud Firewall application**

1. On the **Firewalls** page of the **NFV Cloud Firewall** console, click **Create Cluster** and
configure the following parameters in the panel that appears to create an NFV Cloud Firewall application. When you create an application, a vFW cluster is simultaneously created.

| Parameter | Description |
|---|---|
| Application Name | Enter the name of the NFV Cloud Firewall application. We recommend that you enter an informative name that contains the business information. Example: nfv poc. _ |
| VFW Cluster Name | Enter the name of the vFW cluster. In a single data center, the application name can be the same as the vFW cluster name. In a disaster recovery environment, we recommend that you include the data center information in the vFW cluster name to simplify O&M. Example: nfv poc az1. _ _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | Select a region from the drop-down list. |
| Zone | Select a zone from the drop-down list. Create a vFW cluster on the ECS cluster in the data center. |
| CIDR | Select a CIDR block from the drop-down list, which indicates the NE VPC in which the vFW cluster is created. If no CIDR block is created, the list is empty. |
| Deployment Type | Select a cluster deployment mode to meet your business requirements: Active-Standby: In this high-availability mode, two vFW ECS instances are used for disaster recovery. This mode consumes twice the vFW capacity consumed by the standalone mode. Standalone: In this mode, only one vFW ECS instance is used. This mode does not provide high availability and consumes the vFW capacity. |
| Dedicated Host | Specify whether to deploy the cluster on a dedicated host. No: The cluster is randomly deployed on ECS instances. Yes: You need to specify a dedicated host group and a dedicated host. |
| Network Type | Default value: 25 G. |
| CPU Type | You can choose Intel/X86 orHG /X86. This parameter allows you to choose the ECS cluster that uses the specified CPU type. |

| VFW Specification | Select a vFW specification that meets the preceding network and CPU type conditions from the drop-down list. This parameter indicates the maximum throughput of the vFW cluster for large packets, which consumes the equivalent firewall capacity quota. |
|---|---|
| ECS Specification | Select an ECS specification that meets the preceding network and CPU type conditions from the drop-down list. |
| ECS Image ID | Select the image used by the vFW cluster from the drop-down list. |
| Description | Enter the description of the cluster. We recommend that you include the business, department, and organization information in the description so that the administrator can easily identify the businesses protected by the vFW cluster. |

> **Note:** The values of the CPU Type, VFW Specification, ECS Specification, and ECS Image ID parameters vary depending on the environment and Apsara Stack version. Specify these parameters based on the actual business requirements.

2. After you confirm the configuration, click **OK**. Then, the system automatically verifies the
capacity and quota. If the capacity is sufficient, the operation succeeds and a new NFV Cloud Firewall application is displayed in the list. The status of the vFW cluster changes to
**Creating**.
3. Click the task ID in the **Task ID** column of the application to go to the Workflow page. On
this page, you can view the progress of the cluster creation task. When the subtasks
**ecs_start** and **eni_attach** enter the **Successful** state, the cluster is created.
4. Return to the **Firewalls** page. The NFV Cloud Firewall application is displayed. When the
status of the vFW cluster changes to **Running**, click the application name to go to the application details page. You can view the health status of the vFW ECS instance in the
**Health Status** column. If **Healthy** is displayed, the cluster service functions as expected.
You can then proceed to the next step. If not, the cluster service is not ready. Wait patiently. Common prompts:
**Quota check not passed**: The capacity usage exceeds the specified quota. In this case,
use the admin account to log in to the Apsara Uni-manager Management Console and adjust the NFV Cloud Firewall capacity quota for the current organization.
**cluster capacity reach license limit**: The capacity usage exceeds the total capacity. In
this case, increase the NFV Cloud Firewall capacity by placing a purchase order.

**Step 5: Create endpoints**

An endpoint is equivalent to an interface used by NFV Cloud Firewall to connect to a VPC. It occupies an IP address from the VPC and serves as the next hop for inter-VPC communication. All match traffic is automatically redirected to NFV Cloud Firewall, and then inspected and matched against access control policies. Two processes are involved to create an endpoint:
**Process on the cloud platform side**: An elastic network interface (ENI) is created. You
can view the ENI information by checking the ENI whose description is **Interface for**
**fastpath ft-int-onp use by nfv forbid to operate** on the **ENIs** page of the **ECS** console
in the Apsara Uni-manager Management Console. This process logically associates the endpoint with the VPC.
**Process on the NFV Cloud Firewall side** : A vFW interface is automatically created. You
can use the vFW account to access the NFV Cloud Firewall console or CLI and then view the configuration of the vFW interface. This process logically associates the endpoint with the vFW cluster.

> **Note:** The number of endpoints supported by NFV Cloud Firewall depends on the ECS specification you selected when you create the vFW cluster. The upper limit and current usage displayed in the console prevail. When the upper limit is reached, new endpoints can no longer be created.

**Create an endpoint in VPC1**

1. Go to the NFV Cloud Firewall application details page. In the **Endpoint** section, click
**Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
VPC1.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as VPC1. |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the vFW cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, VPC1 is selected. |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.

**Create an endpoint in the HUB_VPC**

1. In the **Endpoint** section, click **Create Endpoint** on the right side.
2. In the **Create Endpoint** panel, configure the following parameters to create an endpoint in
the HUB_VPC.

| Parameter | Description |
|---|---|
| Name | Enter an endpoint name. We recommend that you include the VPC information, such as HUB VPC. _ |
| Organization | Select an organization from the drop-down list. |
| Resource Set | Select a resource set from the drop-down list. |
| Area | By default, the region of the virtual firewall (vFW) cluster is selected and cannot be changed. |
| Zone | By default, the zone of the vFW cluster is selected and cannot be changed. |
| Source VPC | Select the source VPC that you want to connect from the drop- down list. In this example, the HUB VPC is selected. _ |
| Source Vswitch | Select the source vSwitch from the drop-down list to assign an IP address to the endpoint. |
| Description | Enter an informative description. We recommend that you enter a description related to the VPC, vSwitch, and business. Example: link to hub vpc. _ _ _ |

3. After you confirm the configuration, click **OK** to create the endpoint. Then, a new endpoint
in the **Creating** state is displayed on the page.
4. Click the task ID in the Task ID column of the endpoint to go to the Workflow page. On this
page, you can view the progress of the endpoint creation task. When the task enters the
**Successful** state, the endpoint is created.
5. Return to the Details page. You can find that the endpoint is in the **Running** state, and the
endpoint ID and IP address are displayed. In the **VFW Interface** section, a vFW interface is automatically added based on the endpoint information. If the Configuration Details column of the vFW interface displays
**Published**, the endpoint workflow is completed.
After the configuration is completed, the endpoint and vFW interface enter the following states.

**Step 6: Create vFW routers**

By default, a vFW interface is configured with a direct route that points to the CIDR block of the vSwitch. However, you still need to add static routes to the vFW to route traffic to the CIDR blocks of VPC1 and the data center. Traffic destined for the data center must traverse the HUB_VPC. Therefore, when you add a static route that points to the data center to the vFW, set the next hop to the endpoint of the HUB_VPC.

**Add a route that routes traffic from the vFW to VPC1**

1. In the **VFW Router** section of the Details page, click **Create VFW Router** on the right
side.
2. Configure the following parameters to add a route that routes traffic from the vFW to VPC1.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, VPC1 is selected. |
| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of VPC1. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination VPC name, _ _ such as route to vpc1. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.

**Add a route that routes traffic from the vFW to the data center**

1. In the **VFW Router** section of the Details page, click **Create VFW Router**.
2. Configure the following parameters to add a route that routes traffic from the vFW to the
data center.

| Parameter | Description |
|---|---|
| VPC | Select the VPC that is connected to the vFW from the drop- down list. In this example, the HUB VPC is selected. _ |

| VLAN ID | After you select the VPC, select the VLAN ID used by the vFW interface from the drop-down list. The VLAN ID indicates the vFW interface from which the static route sends traffic. |
|---|---|
| Interface Name | The vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Next Hop | The gateway IP address of the vFW interface is automatically selected based on the specified VLAN ID. You cannot change this parameter. |
| Destination CIDR Block | Enter the destination CIDR block of the static route in the format of subnet address/mask length . In this example, enter the CIDR block of the data center. |
| Description | Enter the description of the static route. We recommend that you specify it in the format of route to destination name, such _ _ as route to idc. _ _ |

3. After you confirm the configuration, click **OK** to create a vFW router. Then, a new vFW
router is displayed in the list. If the Configuration Details column of the vFW router displays
**Published**, the vFW router is created.
After the configuration is completed, the vFW routers enter the following states.

**Step 7: Create a vFW web portal and log in to the vFW**

**(required only for the first time)**

A web portal is used to access the web interface of NFV Cloud Firewall over HTTPS. In a highavailability cluster, each vFW ECS instance requires a web portal. By default, you need only to access the primary node of the cluster to complete the operation. When an HA switchover is triggered, you need to access the secondary node of the cluster. You can use one of the following types of web portals to access NFV Cloud Firewall. You can create only one web portal of each type.
**Classic network**: After the web portal is created, a classic network IP address is displayed.
The web portal is connected to the web port and SSH port of the vFW ECS instance through a Server Load Balancer (SLB) instance deployed in the classic network. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.
**VPC**: After the web portal is created, a vSwitch IP address in the VPC is displayed. The web
portal is connected to the web port and SSH port of the vFW ECS instance through an SLB instance deployed in the VPC. After network integration, you can use this IP address to log in to the web interface of NFV Cloud Firewall over the O&M network.

**Create a vFW web portal**

**Classic network web portal**

1. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the first ECS instance.
2. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.
3. In the **ECS Info** section of the NFV Cloud Firewall application details page, click **Detail** in
the Operation column of the second ECS instance.
4. In the **Classic Network** section, click **Create**. Read the on-screen instructions and click
**OK** to create a classic network web portal.
After you click OK, the web portal enters the **processing** state. When it enters the **success** state, the web portal is created. Then, you can view the web URL and SSH URL on the page.

**VPC web portal**

If your O&M network has access to a VPC, you can also create a VPC web portal in the VPC to access the vFW ECS instance.

> **Important:** Do not create a VPC web portal in the production VPC that is connected to NFV Cloud Firewall in case route conflicts occur.

Refer to the classic network web portal procedure, go to the access mode details pages of the two ECS instances, and complete the following steps to create a VPC web portal for each ECS instance.
1. In the **VPC** section, click **Create**.
2. In the **Create VPC Network Access Method** dialog box, set **Vswitch ID** to the ID of a
vSwitch in the VPC. Make sure that the vSwitch has idle IP addresses.

**Log in to the vFW**

Use a browser to access the web URL of the vFW. Then, the login page of the vFW is displayed. In the upper-right corner of the page shows whether the current device is the primary device or the secondary device. You must log in to the primary device first. Enter the default username and password, which are both admin. After you are logged in, you are required to change the default password. After the change, the new password is synchronized to the secondary device. After you log in to the vFW again, check the hardware platform information and license. Make sure that the authorization is valid and proceed.

**Step 8: Create vFW access control policies**

By default, NFV Cloud Firewall blocks traffic from all sources. To enable intercommunication, you need to configure access control policies to permit access from specific sources. In this scenario, configure a policy to permit ECS1 to access the server in the data center and enable logging to generate access records.

> **Note:** In a production environment, we recommend that you do not enable logging for all access control policies.

1. In the Apsara Uni-manager Management Console, choose **Policy > Security Policy >**
**Policy** and then choose **New > Policy**.
2. Configure the following parameters to create a policy to permit ECS1 to access the server
in the data center, and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter the name of the policy. |
| Source Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of VPC1 is selected. |
| Source Address | Create an address object named ECS1, which contains the IP address of ECS1 ( 10.1.1.1 ). |
| Destination Zone | We recommend that you specify a security zone. When the platform automatically creates a vFW interface, a security zone corresponding to the VPC ID is created. In this example, the ID of the HUB VPC is selected. _ |

| Destination Address | Create an address object named IDC Server, which contains the IP address of the server in the data center ( 172.16.1.1 ). |
|---|---|
| Service | Select Any. |
| Action | Select Permit. |
| Options | Click Options, and select Session start and Session end for Log. Important This step only sets the policy to request the system to generate logs. However, whether logs can be successfully generated and queried depends on whether the vFW logging feature is enabled. |

3. **Enable session logging for the vFW** : In the Apsara Uni-manager Management Console,
choose **Monitor > Log > Session Log** and click **Configure**. In the right-side **Session** panel, turn on **Enable**. If you want to view logs in the console, select **Local Database**. If you want to view logs at the CLI, select **Cache**.

> **Important:** When session logging is disabled for the vFW, even if you have enabled logging in the access control policy, you cannot find any records on the log query page. You can view only the number of policy hits.

**Step 9: Create traffic redirection routes**

**VPC-VPC**: In VPC-VPC protection scenarios, create traffic redirection routes on NFV Cloud
Firewall and publish the routes to the specified VPC route table.
**VS-VS**: In vSwitch-vSwitch protection scenarios, create traffic redirection routes on NFV
Cloud Firewall and publish the routes to the specified VPC route table.
**VPC-IDC**: In VPC-data center protection scenarios (scenario in this topic), create traffic
redirection routes on NFV Cloud Firewall and publish the routes to the specified VPC route table.
1. After you confirm that the configuration in the preceding steps is correct, log in to the **NFV**
**Cloud Firewall** console of the Apsara Uni-manager Management Console and go to the
**Route Configuration** page. Then, choose **Create Traffic Diversion Route > VPC-IDC**.

> **Warning:** **If you perform this operation in a production environment, make sure that** **the specifications of the vFW meet the expectation. If the volume of business** **traffic to redirect exceeds the maximum throughput of the vFW, the network** **latency increases and packet loss occurs.**

2. Configure the following parameters to configure a route to redirect VPC-IDC traffic and click
**OK**.

| Parameter |   | Description |
|---|---|---|
| Organization |   | Select an organization from the drop-down list. |
| Resource Set |   | Select a resource set from the drop-down list. |
| Area |   | Select a region from the drop-down list. |
| Name |   | Enter a name for the custom route. |
| Bilateral Route |   | By default, traffic redirection is configured for only one VPC. You can also turn on Bilateral Route to configure traffic redirection for two interconnected VPCs. In this example, Bilateral Routing is turned on and traffic redirection is configured for VPC1 and the data center at a time. |
| Local Inform ation | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to idc in this example. _ _ |
|   | VPC | Select a VPC from the drop-down list. In this example, VPC1 is selected. |
|   | VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block (IDC CIDR Block) | Enter the destination CIDR block. In this example, enter the CIDR block of the data center, which is 172.16.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |

|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |
|---|---|---|
|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |
|   | Route Name | We recommend that you enter a name to indicate the destination VPC in order to simplify O&M. The information will be displayed on the Route Tables page in the VPC console of the Apsara Uni-manager Management Console. Enter route to vpc1 in this example. _ _ |
|   | HUB VPC | Select a VPC from the drop-down list. In this example, the HUB VPC is _ selected. |
| Peer Inform ation |   |   |
|   | HUB VPC CIDR Block | After you select a VPC, the CIDR block of the VPC is automatically displayed for reference. You cannot modify this parameter. |
|   | Routing Table | After you select a VPC, select the route table of the VPC from the drop- down list. |
|   | Target CIDR Block (VPC CIDR Block) | Enter the destination CIDR block. In this example, enter the CIDR block of VPC1, which is 10.1.0.0/16 . |
|   | Applicatio n | Select the NFV Cloud Firewall application from the drop-down list. Select the same application in the local and peer information. |
|   | Master VFW Cluster | Select the primary vFW cluster from the drop-down list. Two traffic redirection routes whose mask length is N+1 are published. |
|   | Master Endpoint Informati on | An endpoint is automatically selected as the next hop of the route. To select more endpoints, manually select them from the drop-down list. |

|   | Slave VFW Cluster | You can skip this parameter when there is only one data center. |
|---|---|---|
|   | Slave Endpoint Informati on | You can skip this parameter when there is only one data center. |

After you complete the configuration, the **Route Status** column of the routes displays
**Unpublish**. In this case, the O&M engineer needs to complete adding and checking all
routes and then publish the routes one after one or in batches. This feature allows you to perform route configuration and traffic redirection within two time windows in case you do not have sufficient time to complete the two tasks within the same time window.
3. Click **Publish** in the **Operation** column of the desired traffic redirection route and click **OK**.
Wait until the status of the route changes from **Publishing** to **Published**. This means that the route is in effect. This way, the outbound traffic of VPC1 and the data center is redirected to NFV Cloud Firewall. After the traffic redirection route is published, log in to the **VPC** console, go to the **Route**
**Tables** page, and view the status of the routes in the route tables of VPC1 and HUB_VPC.
You can find that the two routes whose mask length is N+1 are published from NFV Cloud Firewall. Their next hops are set to the elastic network interface (ENI) of the endpoint. The
**route names** you entered are displayed in the route descriptions to simplify O&M.
Route table of VPC1: Route table of HUB_VPC:

**Step 10: Verify the business**

1. Log in to ECS1 and initiate a business test:
i. Run the `ping <IDC Server IP>` command on ECS1 to test the connectivity to the server in the data center. The ping succeeds. ii. Run the `ssh root@<IDC Server IP>` command on ECS1 to log in to the server in the data center over SSH. The operation succeeds.
2. Log in to the Apsara Uni-manager Management Console to view logs.
Choose **Policy > Security Policy > Policy**, find the desired policy, and check whether the **number of hits** increases. Choose **Monitor > Log > Session Log**, set **Time** to **Real-time**, and check whether ping (corresponding to ICMP) and SSH (corresponding to TCP) logs are generated. In addition, check whether session logs containing source and destination IP addresses related to the test are generated.

**Other scenarios**

**Scenario 1: What network architecture do I use when multiple**

**VPCs need to communicate with a data center and connections**

**to the data center use the active/active mode?**

Solution: After you connect the VPCs and data center to NFV Cloud Firewall, use a HUB_VPC to access the data center. When two Express Connect circuits are established in active/active mode on the data center side, traffic is balanced through CSW1 and CSW2.

**Network Integration That Connects HUB_VPC and Data Center**

**Traffic Redirection by NFV Cloud Firewall**

CSW1

**VPC1**

> **Destination Next Hop**

10.1.0.0/16

|   | op Destination t t to o o_ _ _I V VD P PC C C 1 21 7 1 12 0 0. . .1 1 26 . .0 0.0 . .0 0.0 / /1 1/1 6 66 VFW(M) vFW Network Service Clu |
|---|---|

> to_IDC 172.16.0.0/16 IDC to_VPC1 10.1.0.0/16 VRouter to_VPC2 10.2.0.0/16 VRouter to_hubvpc 192.168.33.0/24 VRouter
> **Destination Next Hop**
> to_IDC 172.16.0.0/16 NFV

VBR

**HUB_VPC**

192.168.33.0/16

**vSwitch1**

Data Center 172.16.0.0/ 10.1.1.0/24 Express Connect Circuit 1

> **Destination Next Hop**
> **Destination**
> to_IDC 172.16.0.0/16 CSW to_VPC1 10.1.0.0/16 NFV to_VPC2 10.2.0.0/16 NFV
> to_VPC1 10.1.0 to_VPC2 10.2.0

ECS1

|   |   | vFW Network Se |
|---|---|---|

ep-vpc1

> Active/Active

Access Express Connect Circuit 2 Device

**Server**

**hub_vSwitch**

172.16.1.1/16 VRouter 192.168.33.0/24 ep-idc VBR

**VPC2**

VFW(S) 10.2.0.0/16

**vSwitch2**

10.2.1.0/24

> **Destination Next Hop**
> to_IDC 172.16.0.0/16 IDC to_VPC1 10.1.0.0/16 VRouter to_VPC2 10.2.0.0/16 VRouter to_hubvpc 192.168.33.0/24 VRouter

ep-vpc2 ECS2 CSW2

> **Destination Next Hop**
> to_IDC 172.16.0.0/16 NFV

**Scenario 2: Can I use different vFWs for protection?**

Solution: Yes.

**Network Integration That Connects**

**Traffic Redirection by**

**HUB_VPC and Data Center**

| VPC1 10.1.0.0/16 Destination Next Hop to_IDC 172.16.0.0/16 NFV A vSwitch1 10.1.1.0/24 ECS1 ep-vpc1 VPC2 10.2.0.0/16 Destination Next Hop to_IDC 172.16.0.0/16 NFV B vSwitch2 10.2.1.0/24 ep-vpc2 ECS2 |   | NE VPC 192.168.1.0/24 NFV A Destination N t to o_ _I VD PC C 11 7 12 0. .1 16 .0.0 .0.0 /1/1 66 H U B _VV P VFW(M) vFW Network Service Cluster A VFW(S) VFW(M) vFW Network Service Cluster B VFW(S) Destination t to o_ _I VD PC C 21 7 12 0. .1 26 .0.0 .0.0 /1/1 66 H U B _V NFV B | CSW1 Destination Next Hop P Ce Cx 1t Hop tt tt oo oo __ __ hV VID uP PC bC C 1 21 7 1 1 c2 0 0 1. . .1 1 2 96 . . 20 0. .0 . . 10 0. 60 / / 81 1/1 .6 6 36 V V R R o o u u I t t tD e e eC r r v p 3 . 0 / 2 4 V R o u r 192.168H .U 3B 3._0V /P 1C VBR 6 Data Center 172.16.0.0/1 Des t t tt o o oin _ _ _a I V VDt P Pi Co C Cn 1 21 7 1 1 2 0 0 . . . 1 1 2 6 . . 0 0 . 0 . . 0 0 . 0 / / 1 1/ 1 6 6 6 N N N C F FV Ve Sx W A Bt Hop Dest t ti o on _ _a V Vti P Po C Cn 1 2 1 1 0 0 . . 1 2 . . 0 0 1ct ite un cn iro C C Express AAcctitvivee/S/AtacnA Dtidvc ebec vye ics es 192h .1u 6b 8_v .3S 3w .0it /c 2h 4 VRouter 172S .1e 6r .v 1e .r 1/16 2Connect ep-idcA E Cx ir pr ce ui s ts VBR ep-idcB Destination Next Hop CSWtt tt 2oo oo __ __ hV VID uP PC bC C 1 21 7 1 1 c2 0 0 1. . .1 1 2 96 . . 20 0. .0 . . 10 0. 60 / / 81 1/1 .6 6 36 V V R R o o u u I t t tD e e eC r r v p 3 . 0 / 2 4 V R o u r Next Hop VPC PC2 |
|---|---|---|---|
|   |   | NE VPC 192.168.1.0/24 NFV A Destination t to o_ _I VD PC C 11 7 12 0. .1 16 .0.0 .0.0 /1/1 66 VFW(M) vFW Network Service Cluster A VFW(S) VFW(M) vFW Network Service Cluster B VFW(S) Destination t to o_ _I VD PC C 21 7 12 0. .1 26 .0.0 .0.0 /1/1 66 NFV B |   |

**Scenario 3: Can I use multiple vFWs and multiple HUB_VPCs at**

**the same time?**

Solution: Yes.

**Network Integration That Connects HUB_VPC and Data Center**

**Traffic Redirection by NFV Cloud Firewall**

CSW1

|   | NE VPC 192.168.1.0/24 NFV A Destination N Fe Vx At Hop t to o_ _I VD PC C 11 7 12 0. .1 16 .0.0 .0.0 /1/1 66 N VFW(M) vFW Network Service Clus VFW(S) N N Fe Vx Bt Hop VFW(M) vFW Network Service Cluste VFW(S) Destination t to o_ _I VD PC C 1 27 12 0.1 .26 .. 00 .. 00 // 11 6 NFV B |
|---|---|

VBR A

> **Destination** **Next Hop** to_IDC 172.16.0.0/16 IDC to_VPC1 10.1.0.0/16 VRouterA to_hubvpcA 192.168.33.0/24 VRouterA

| NFV A Destination x At Hop t to o_ _I VD PC C 11 7 12 0. .1 16 .0.0 .0.0 / VFW(M) vFW Network Service |   |   |
|---|---|---|
|   |   | vFW Network |

|   | Destination t to o_ _I VD PC C 1 17 12 0.1 .16 .. 00 .. 00 // 11 192h .1u 6b 8_v .3S 3w .0it /c 2h 4 ep-idcA |
|---|---|

VPC1 10.1.0.0/16

> **Destination****Next Hop**
> to_IDC 172.16.0.0/16 NFV A

VBR B

> **Destination** **Next Hop** to_IDC 172.16.0.0/16 IDC to_VPC2 10.2.0.0/16 VRouterB to_hubvpcB 192.168.34.0/24 VRouterB

vSwitch1 10.1.1.0/24 VRouterA Data Center 172.16.0.0/16 ECS1 ep-vpc1 Express Connect Circuit B1

> **Destination**
> to_VPC1 10.1.0.0 to_VPC2 10.2.0.0

Access Active/Active Device Active/Standby Server Express Connect Circuit B2 172.16.1.1/16 HUB_VPCB 192.168.34.0/16 VPC2 10.2.0.0/16 VBR A

> **Destination****Next Hop**
> **Destination****Next Hop**
> to_IDC 172.16.0.0/16 VBR B to_VPC2 10.2.0.0/16 NFV B
> to_IDC 172.16.0.0/16 NFV B
> **Destination** **Next Hop** to_IDC 172.16.0.0/16 IDC to_VPC1 10.1.0.0/16 VRouterA to_hubvpcA 192.168.33.0/24 VRouterA

vSwitch2 10.2.1.0/24 hub_vSwitch 192.168.34.0/24 VRouterB ep-vpc2 ECS2 ep-idcB VBR B

> **Destination** **Next Hop** to_IDC 172.16.0.0/16 IDC to_VPC2 10.2.0.0/16 VRouterB to_hubvpcB 192.168.34.0/24 VRouterB

CSW2
