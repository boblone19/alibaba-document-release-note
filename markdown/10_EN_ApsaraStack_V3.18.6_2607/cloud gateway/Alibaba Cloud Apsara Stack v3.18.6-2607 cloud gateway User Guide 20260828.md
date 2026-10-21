---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 26
source_pdf: "8d0327434eeac477_Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3CGW/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20cloud%20gateway%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway User Guide 20260828

## Table of Contents

- 1 CGW overview
- 2 Log on to the Apsara Uni-manager Management Console
- 3 ONSP
  - 3.1 Overview
  - 3.2 Service cluster deployment
    - 3.2.1 Preparations
    - 3.2.2 Create a custom ECS image
    - 3.2.3 Deploy and activate a service cluster
    - 3.2.4 Application overview
  - 3.3 Open network service
    - 3.3.1 Perform authorization
    - 3.3.2 Business traffic acquisition
    - 3.3.3 Create a network service instance
    - 3.3.4 View service monitoring data
    - 3.3.5 Configure sharing settings
  - 3.4 Manage CIDR blocks
  - 3.5 Manage dedicated host groups
  - 3.6 Manage the system

## 1 CGW overview

Cloud Gateway (CGW) provides scenario-specific networking services to help enterprises efficiently build hybrid clouds and migrate workloads to clouds.

**Open Network Service Platform (ONSP)**

ONSP is a lifecycle management platform compliant with European Telecommunications Standards Institute (ETSI) standards. ONSP helps you deploy and manage virtual network services that are built based on network functions virtualization (NFV), such as load balancers, firewalls, and network performance management services. ONSP ensures high availability, high scalability, high security, and high O&M efficiency for your networks. ONSP supports the following features: Initialize virtual network service sets Manage virtual network service sets Manage routing policies Check the health status of virtual network elements and isolate faults Uni-manager Management Conso le

## 2 Log on to the Apsara Uni-manager Management Console

**manager Management**

**Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.
1. In the address bar of the browser, enter the URL of the Apsara Uni-manager Management
Console and press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**First-time logon**

The first time you log on to the Apsara Uni-manager Management Console, you must change your username and password. Follow the instructions to change your username and password. The password must be 10 to 32 characters in length, and can contain letters, digits, and special characters, such as exclamation marks (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).

**Forgot password**

If you forgot your password, click Forgot Password and enter your username, email address, and the verification code. Then, a URL is sent to your email box. You can click the URL to reset the password.
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: This is your first time logging on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, follow the instructions to add an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA verification code and click **Authenticate**. MFA is enabled and an MFA device exists: Enter the six-digit MFA verification code and click **Authenticate**.

## 3 ONSP

This document introduces Open Network Service Platform (ONSP) and describes how to deploy a service cluster on ONSP.

### 3.1 Overview

**Background information**

Open Network Service Platform (ONSP) automatically deploys virtual network devices from partners in a separate virtual private cloud (VPC) in a standardized and modular manner. This solution helps enterprises centrally manage their virtual network devices and reduce deployment costs. ONSP supports standard connection, quick deployment, and efficient operation for network elements, which improves the user experience of services provided by ecosystem partners. Centralized deployment: Third-party virtual network elements are deployed as clusters in a separate VPC. This allows you to manage the network elements in the same VPC. Private connections: Service traffic is forwarded to third-party network elements based on elastic network interfaces (ENIs). Fault isolation: Active/active clusters and active/standby clusters are supported. If an error is detected in a cluster, network traffic bypasses the cluster and switches to a running cluster.

**Supported service providers**

To view the services and service providers supported by ONSP, go to the Apsara Stack official website. At the bottom of the page, find **Partners >****System Integration/Compatibility >**
**Network Devices,** device type is **Software** type.

> **Important:** **Standard service provider**: Hillstone.
> **Non-standard service providers**: Alibaba Cloud does not guarantee the high performance or reliability of services provided by non-standard service providers, and supports the utilization of these services only in scenarios documented in test reports.

**Console operations**

The operations of the open network service platform are divided into the following two parts: Deploy service clusters: You can make preparations, create custom Elastic Compute Service (ECS) images, and deploy and activate service clusters. After the deployment is complete, you can check whether the clusters encounter errors and quickly troubleshoot errors on the cluster overview pages. Manage ONSP resources: The steps include the following operations: grant permissions to accounts, route service traffic, create a network service instance, configure service monitoring, and manage resource sharing settings.

### 3.2 Service cluster deployment

This document describes how to deploy a service cluster.

#### 3.2.1 Preparations

Before you deploy a service cluster, you need to plan a network architecture, confirm the status of dependency services, and obtain service metadata. Network architecture: Plan an overall network architecture based on the type of network service to deploy and the method to use the network service. Status of dependency services: Check the status of other services on which Open Network Service Platform (ONSP) relies. Before you start the deployment, check the service version and cluster status in Apsara Infrastructure Management. You can proceed only when the service version is correct and the clusters are at desired state.

| Product name in Chinese | Specificati ons | Product code | Cluster type | Version | Description |
|---|---|---|---|---|---|
| Cloud Gateway (CGW) | An open network service platform | nsp | onpCluster | v3.18.3r | The backend service of ONSP. |
| Hybrid Cloud Application Center |   |   |   | v3.18.3r | The frontend page of ONSP. |
| Apsara Uni- manager Management Console | Network functions virtualizatio n (NFV) service | nfv | nfv controller Cl _ _ uster thirdNet _ | v3.18.3r | Supports elastic network interfaces (ENIs) that can route network traffic. |

Service metadata: Service metadata includes the original image file, configuration file, user guide, and O&M guide. To obtain the original image file, contact Apsara Stack technical support. Then, Apsara Stack technical support logs on to Image Center to search for the image based on the image information that you provide, and applies for the image. After the application is approved, a download URL is generated. You can use the Wget utility to download the image from the URL.

#### 3.2.2 Create a custom ECS image

After you obtain the original image file of the open network service from Apsara Stack technical support, you can call the CreateImage API operation to create a custom image. The image can be used to create service clusters.
1. Obtain the image from Apsara Stack Image Center.

> **Note:** Apsara Stack Image Center is reserved for internal use. You need to contact technical support to apply for images.

2. Upload the image to the `/home/admin/onp_openapi/images` directory on the machine where
the onp-openapi service is deployed.
3. Call the CreateImage API operation to create an image. For more information, see
CreateImage in ECS Developer Guide.

#### 3.2.3 Deploy and activate a service cluster

This topic describes how to import the configuration file of a network service to Hybrid Cloud Application Center based on your business requirements and network architecture. It also explains how to deploy and activate a service cluster to enable the network services provided by the cluster.

**Open the Open Network Service Console**

Log on to Hybrid Cloud Application Center and open the Open Network Service Console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center (AHM)**.

3. In the left-side navigation pane, choose **Plugin Center** > **My Plugins**.
4. Click the **onsp** application card to go to the **Plugin Details** page.
5. In the **Access Entry** section on the right side of the page, click **Open Network Service**
**Console** to go to the Open Network Service Console.

**Import service configurations**

In the Open Network Service Console, import the configurations of the open network service.
1. In the **Open Network Service Console**, click **App Store** in the left-side navigation pane.
2. Click **Import Application**, select the service configuration file, and upload it.

> **Note:** To obtain the configuration file of the open network service, contact Alibaba Cloud technical support.

3. After the configuration file is imported, click the service card to go to the **Application**
**Details** page of the open network service.

**Deploy a service cluster**

After you import the configuration file of an open network service, you can deploy a service cluster.
1. On the **Application Details** page of the open network service, click **Deploy** to create a
cluster.

| Name | Description |
|---|---|
| Cluster Name | The name of the cluster. |
| Region | The region in which you want to deploy the Elastic Compute Service (ECS) instance. |
| Deployment Type | After you select a Region, select the mode in which you want to deploy the cluster. Valid values: Standalone and Active-Standby. Standalone: creates only one ECS instance. Active-Standby: creates two ECS instances. The two instances serve as primary and secondary instances. |
| Zone | The zone in which you want to deploy the ECS instance. The cluster can be deployed only in one zone. |
| cidr | The virtual private cloud (VPC) in which you want to deploy the ECS instance. A VPC, a vSwitch, and a security group are automatically created in the specified CIDR block. You can click Add CIDR Block to specify a CIDR block for the VPC. For more information, see Manage CIDR blocks. Note To ensure that the network service can run as expected, we recommend that you specify a private CIDR block whose subnet mask is smaller than 26 bits for the VPC. |

| Deploy On Dedicated Host | Specifies whether to deploy the cluster on a dedicated physical server. Valid values: No and Yes. If you set this parameter to Yes, you must specify the host group and the host on which to deploy the cluster. In the Host Group drop-down list, select an existing host group. You can also click Add Host Group to add a custom host group. For more information, see Manage dedicated host groups. In the Host drop-down list, select a host for deployment. Note If you set the Deployment Type parameter to Standalone, select only one host. If you set the Deployment Type parameter to Active-Standby, select two hosts. |
|---|---|
| ECS Instance Type | The instance type of the ECS instance. Network functions virtualization (NFV) network services require certain types of ECS instance. You can select ECS instance types from the drop-down list. ECS instances with higher specifications provide higher capacities and better performance. |
| ECS Image ID | The image that is used to create the ECS instance. For more information about how to create an image, see Create a custom ECS image. |
| Cluster Description | The description of the cluster. |

2. Click **Deploy**.
3. After the cluster is deployed, click **My Applications** in the left-side navigation pane to view
the created application.

> **Note:** You can click the icon on the right of the application card and select **Change**
> **Application Name** to change the name of the application.

4. Optional. Click the name of the application to go to the **Application Details** page.

**Create a secondary cluster**

Click **Create Redundant Cluster** in the upper-right corner of the application details page to create a secondary cluster for disaster recovery. To configure parameters for the secondary cluster, you can refer to the parameter description of the primary cluster in the preceding table.

> **Important:** The secondary cluster must be deployed in a zone different from that of the primary cluster. In this case, if a network error occurs in the primary cluster, network traffic is automatically switched to the secondary cluster.

**View cluster information**

In the left area of the cluster tab, you can view the cluster's **Basic Information**,
**Cluster Details**, **ONSP Endpoint**, and more.
In the **Basic Information** section, you can view the basic information of the cluster including the cluster ID, cluster name, zone ID, CIDR block, CIDR block name, and description.

> **Note:** You can click the icon on the right of the cluster name to modify the
> cluster name.

In the **Cluster Details** section, you can perform the following operations: **Delete**
**Cluster**, **Scale Out Cluster**, log on to instances by using Virtual Network Console
(VNC), obtain the VNC password, view the details of instances in the cluster, and delete instances from the cluster.

> **Warning:** Deleting a service cluster may result in service disruptions. Proceed with caution.
> You must delete all routing entries that point to the service cluster before you can delete the cluster.

In the **ONSP Endpoint** section, you can **Create Endpoint**, view endpoint details, delete endpoints, and view endpoint logs. On the right of the cluster details tab, you can view the name, **Basic Information**,
**Operation Logs**, and **Scaling Logs** of the application.

**View routing policies**

In the **Cluster Basic Information** section of the **Routing Policy** tab, you can view the cluster information including the **Cluster Name**, **Cluster ID**, **Zone ID**, **Bypass**
**Status**, and **Progress**.

> **Warning:** After routes are configured for the VPC, if an error occurs in a network element, you can click Bypass to withdraw all routes to the destination cluster, and then directly forward traffic to the destination cluster by using Express Connect circuits. After the network element is recovered, you can click **Restore** to restore all routes that are withdrawn.
> The bypass and restore operations involve high risks. We recommend that you contact Alibaba Cloud technical support before you perform these operations.

In the **Route Details** section of the **Routing Policy** tab, you can add, modify, or delete routes. For more information, see Configure routes for business VPCs. On the **Service Monitoring** tab, you can view the instance status and network traffic that flows through the elastic network interfaces (ENIs) associated with the service port. For more information, see View service monitoring data.

**View sharing settings**

On the **Sharing Settings** tab, you can enable the sharing feature to allow specific users to view the application and authorize them to perform operations. For more information, see Configure sharing settings.

**Activate the cluster**

> **Note:** After a service cluster is deployed, you must activate the cluster before you can use it.

Contact technical support of the service provider and provide information about the deployed network service and the ECS instance that is used. Then, a license file will be issued to you. Go to the network service page to activate the service cluster using the license file.

#### 3.2.4 Application overview

After you deploy and activate a service cluster, you can view the resource status and cluster monitoring data on the Overview page. If an Elastic Compute Service (ECS) instance encounters an error, and the health check result is not Running, the status of the cluster changes to error. Unhealthy clusters are displayed on the monitoring overview list to notify you of anomalies and help you locate errors.
1. Open the Open Network Service Platform console.
2. In the left-side navigation pane, click **Overview**.
3. In the **Resource Overview** section, you can view the information about your applications,
including the **application name** and **creation time**. You can also enter an ECS instance ID to search for an application. Click **Jump** in the **Operation** column to view more details about the application.

| Application details | Description |
|---|---|
| Details tab | On the details tab of the application, you can view the basic information about the application and configure clusters and endpoints. For more information, see Deploy and activate a service cluster and Route network traffic to a service cluster. |
| Routing Policy tab | On this tab, you can view and configure routes. For more information, seeR oute network traffic to a service cluster. |
| Service Monitoring tab | On this tab, you can view the instance status and network traffic that flows through the elastic network interfaces (ENIs) associated with the service port. For more information, see View service monitoring data. |
| Sharing Settings tab | On this tab, you can share your applications with other users. For more information, see Configure sharing settings. |

4. In the **Monitoring overview_abnormal cluster monitoring** section, you can view
abnormal clusters and perform troubleshooting. i. Click **Jump** in the **Operation** column to go to the application details page. ii. Click the **Service Monitoring** tab and check the **health check result** of the instance. If the status of the instance is not Running, the instance has an error. iii. Click the application name to go to the details page of the application. In the **Cluster**
**Details** section, copy the **Virtual Network Computing (VNC) password** of the
instance and log on to the instance by using **VNC**. iv. After you log on to the instance, you can check the status of the instance, view the error details, and then perform troubleshooting.

### 3.3 Open network service

This document describes how to work with an open network service.

#### 3.3.1 Perform authorization

If you use Open Network Service Platform (ONSP) within a cloud account for the first time, you need to grant the required permissions to the cloud account to allow Cloud Gateway (CGW) to manage elastic network interfaces (ENIs) for virtual private clouds (VPCs).

**Prerequisites**

The cloud account is imported as a resource account, and you use ONSP within the account for the first time.
1. Open the ONSP console.
2. In the **Letter of Application** message, click **Authorize**.

#### 3.3.2 Business traffic acquisition

This topic describes how to route network traffic to an open network service cluster for the service to run as expected.

**Process**

**Create a VPC and a vSwitch**

Create a virtual private cloud (VPC) and a vSwitch based on your business plan.
1. Log on to the VPC console to create a VPC. For more information, see "VPC management"
in VPC User Guide.
2. Log on to the VPC console to create a vSwitch in which you want to deploy Elastic Compute
Service (ECS) instances. For more information, see "Manage vSwitches" in VPC User Guide.
3. Create additional vSwitches based on your business requirements.

> **Note:** If you use a virtual load balancer (VLB) in your network, you need to create an additional virtual IP address (VIP) and an additional vSwitch in the VPC to reserve an IP address for external load balancing services.

**Create an endpoint**

Network traffic is routed to the open network service cluster through an elastic network interface (ENI). Therefore, you need to create an ENI in advance. After the ENI is created, it is automatically associated with the open network service cluster.
1. Open the open network service console.
2. In the left-side navigation pane, choose **My Applications** and click the target application.
3. On the **Application Details** page, click the cluster name tab.
4. In the **ONSP Endpoint**section, click **Add Endpoint**.
5. In the **endpoint** dialog box, configure parameters and click **OK**.

| Name | Description |
|---|---|
| Cluster ID | The ID of the cluster. Default value. |
| Endpoint Name | Enter a name for the endpoint. |
| Level-1 Organization UID | The ID of the level-1 organization to which the ENI belongs. You can view the organization ID on the Organizations page in the Apsara Uni- manager Management Console. |
| Source VSwitch ID | The ID of the vSwitch in which the ENI is deployed, which is the business vSwitch ID. You can view the vSwitch ID on the VSwitch page in the VPC console. Note The CIDR block of the vSwitch cannot overlap with the CIDR block of the open network service cluster. The vSwitch and the current cluster must be deployed in the same zone. |
| Description | Detailed description of the drainage operation. |

6. After the endpoint is created, you can view the information about the resources used for
routing in the **ONSP Endpoint** section, and record the **Endpoint ID**, **Endpoint IP**, and
**VLAN ID**.
7. Optional. When the endpoint is changed or no longer needed, click **Delete** in the **Actions**
column to delete the target endpoint.

> **Warning:** Before you delete the endpoint, make sure that the routes that point to the ENI are deleted.
> Removing an endpoint may result in network interruptions. Make sure that no network traffic is forwarded to the endpoint. Proceed with caution.

**Check the result**

After you create an endpoint, an ENI and a security group are automatically created. Log on to the Apsara Uni-manager Management Console and choose **Products** >
**Computing****> Elastic Compute Service** to view the ENI and security group.
To view the details of the ENI, choose **Network & Security** > **ENIs**.

**Important**

> The ENI is created by the system. We recommend that you do not modify the ENI.

To view the details of the security group or modify the security group rule, choose **Network**
**& Security** > **Security Groups**.
A security group is automatically created for the ENI. By default, all inbound and outbound traffic is allowed.

**Configure routes for the VPC**

After the ENI is created, you need to configure a route that points to the ENI for the VPC based on your routing plan. Then, network traffic can be routed to the open network service cluster.
1. Determine the destination CIDR block.

> **Note:** In VLB scenarios, VIPs need to be divided into two CIDR blocks. One of the CIDR blocks is the destination CIDR block.
> In virtual firewall scenarios, you need to specify a destination CIDR block based on your needs. For example, you need to specify the CIDR block of the peer VPC for VPC-to-VPC protection. For VPC-to-data center protection, you need to specify the CIDR block of the data center.

2. Query the ID of the next hop ENI.
On the **Application Details** page, find the ID of the endpoint based on the VPC and vSwitch information.
3. On the **Routing Policy** tab, click **Add Route**.
To enable zone-disaster recovery, specify the secondary endpoint and the cluster to which the secondary endpoint belongs, and configure the same settings for the network elements of the secondary cluster.

| Name | Description |
|---|---|
| Name | Enter a name for the route. |
| Destination CIDR Block | Enter a destination CIDR block. |
| Route Table ID | Enter the ID of the route table to which you want to add the route. |
| Primary Endpoint Cluster | Specify the cluster to which the primary endpoint belongs. |
| Primary Endpoint | By default, network traffic is routed to the primary endpoint. |
| Secondary Endpoint Cluster | Specify the cluster to which the secondary endpoint belongs. |
| Secondary Endpoint | By default, network traffic is automatically switched to the secondary endpoint if the primary endpoint encounters an error. |

4. Click **Submit**.
5. Optional. After routes are configured for the VPC, if an error occurs in a network element,
you can use the Bypass feature to withdraw all routes to the destination cluster, and then directly forward traffic to the destination cluster by using Express Connect circuits. After the error is resolved, you can use the **Restore** feature to restore all routes that are withdrawn.
**Bypass**: Click **Bypass** in the **Cluster Basic Information** section, enter the **Captcha**,
and then click **Submit**.
**Restore**: Click **Restore** in the **Cluster Basic Information** section, enter the **Captcha**,
and then click **Submit**.

> **Warning:** The bypass and restore operations involve high risks. We recommend that you contact Alibaba Cloud technical support before you perform these operations.

**Configure a cluster network**

Log on to the ECS instance on the web page and configure a port and a route that points to the CIDR block of the VPC to receive network traffic from the VPC.
1. In the **Cluster Details** section, find the ECS instance that you want to manage and click
**Details** in the **Actions** column.
2. Click **Create** on the right of the **Classic Network Access** section to create a classic
network access method.
3. After the classic network access method is created, click the address in the **Web Access**
**Address** column to log on to the ECS instance.
Configure a port and a route that points to the CIDR block of the VPC by using the
**Endpoint ID**, **Endpoint IP**, and **VLAN ID** that you recorded in Step 6.

> **Note:** If you have any questions during the configuration, contact technical support of the service provider.

4. Go to the portal of the open network service and probe the gateway IP address to test the
network connectivity.

#### 3.3.3 Create a network service instance

This topic describes how to create a network service instance, such as a Server Load Balancer (SLB) instance or a firewall security policy. For more information, see LB-F5-BIGIPVE Configuration Guide and FW-Hillstone-CloudEdge Configuration Guide. If you encounter any problems, you can select the specific network service, view the contact information, and contact the partner for technical support. To do this:
1. Open the Open Network Service Platform console.
2. Click **App Store** in the left-side navigation pane.
3. On the **App Store** page, select the specific network service, view the contact information,
and contact the partner for technical support.

#### 3.3.4 View service monitoring data

Through service monitoring, you can monitor the status of network element instances and the traffic of business ports.
1. Open the Open Network Service Platform (ONSP) console.
2. In the left-side navigation pane, click **My Applications**.
3. On the **My Applications** page, select the application that you want to view.
4. Click the **Service monitoring** tab and view the information and status of resources.
5. Click **Details** in the Monitoring details column to view the network traffic that flows through
the elastic network interfaces (ENIs) associated with the service port.

#### 3.3.5 Configure sharing settings

Open Network Service Platform (ONSP) allows you to share your application with other users. The authorized users can view information about and perform specific operations on your application.

**Limits**

You can share your application only with users that belong to the same level-1 organization.
1. Open the Open Network Service Platform console.
2. In the left-side navigation pane, click **My Applications**.
3. On the **My Applications** page, click the name of the application that you want to share to
go to the application details page.
4. Click the **Sharing Settings** tab.
5. Click **Add Recipient Account**. In the dialog box that appears, specify the **recipient**
**account name**, **user ID**, and **permissions** to be granted to the user.

| Name | Description |
|---|---|
| Name | The name of the recipient account. |
| Aliuid | The ID of the user. |
| Permissions | The permissions to be granted to the user. Valid values: Management Permission: grants the user all permissions on the application. Access Permission: grants the user only the permissions to view the application, configure cluster endpoints, and configure routing policies. Important Users that are granted the access permission cannot configure the cluster network. Therefore, after a user creates an endpoint, you need to log on to the corresponding Elastic Compute Service (ECS) instance in the cluster to configure the cluster network. This way, the cluster can receive network traffic. |

6. Click **Add**. After you add a recipient account, the recipient account is displayed in the
account list. To remove a recipient account from the account list, click **Delete** in the Actions column.

### 3.4 Manage CIDR blocks

CIDR (Classless Inter-Domain Routing) is a method to allocate IP addresses and route data, which enables more efficient IP address allocation and utilization through flexible IP address space division.

**Background information**

CIDR allows you to segment an IP address into multiple subnets. Each subnet can be assigned a different number of IP addresses based on your requirements. In a CIDR block, an IP address and a prefix length are separated by a slash (/). The prefix length indicates the number of network prefix bits in the IP address. For example, if a CIDR block is 192.168.0.0/24, 192.168.0.0 indicates the starting IP address of the CIDR block and /24 indicates that the IP address has 24 network prefix bits.

**Limits**

You cannot delete a CIDR block that is in use.
1. Open the ONSP console.
2. In the left-side navigation pane, click **CIDR Blocks** to manage CIDR blocks.

| Operation | Description |
|---|---|

| Create a CIDR block | i. Click Add CIDR Block in the upper part of the page. ii. In the Add CIDR Block dialog box, configure the CIDR Block Name and CIDR parameters. Note The CIDR Block Name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a _ letter or Chinese character and cannot start with http:// or https://. iii. Click OK. |
|---|---|
| Delete a CIDR block | i. In the CIDR Block List, click Delete in the Actions column. ii. Click OK. |

### 3.5 Manage dedicated host groups

**groups**

Managing dedicated host groups involves creating and deleting host groups, and adding dedicated hosts to them. After you create host groups and dedicated hosts, you can deploy your service clusters on the dedicated hosts when you activate deployment services.

**Background information**

Dedicated Host Group is used to manage and organize dedicated host resources. After you request a dedicated host, you have exclusive access to the physical server and can create ECS instances on it to meet resource isolation requirements and deployment needs for different services.

**Limits**

You cannot delete a host group that is in use. Before you delete a host group, remove all hosts from the host group. You cannot delete a dedicated host that is in use.

**Create a host group**

1. Open the Open Network Service Platform console.
2. In the left-side navigation pane, click **Dedicated Host Groups**.
3. On the **Dedicated Host Groups** page, click **Create Group**.
4. In the **Create Host Group** dialog box, enter the **Host Group Name** and **Description**, and
select the **Region**, **Zone**, and **Host Instance Type**.

> **Note:** You can contact Alibaba Cloud technical support to confirm the host specifications.

5. Click **Confirm**. The host group is created.

**View host group details**

On the **Dedicated Host Group Details** page, you can view the **Basic Information**, **Host**
**List**, and **Application List** of the host group.
1. On the **Dedicated Host Groups** page, click the host group name/ID to go to the
**Dedicated Host Group Details** page.
**Basic Information**: Displays the **Host Group Name**, **Host Group ID**, **Status**, **Zone**,
**Instance Type**, **Available/total VCPUs**, and **Available/total Memory**.
**Host List**: Displays the dedicated hosts in the host group. For more information about
how to manage hosts, see Manage hosts in a host group.
**Application List**: Displays the applications that use this host group. Click **Details** in the
Actions column of an application to open the application details and view detailed information about the application.

**Manage hosts in a host group**

After a host group is created, you can add hosts to the host group. When a host is no longer needed, you can remove it from the host group.
1. Add dedicated hosts to the host group.
On the **Dedicated Host Groups** page, click **Add Host** in the Actions column of the host group. On the **Dedicated Host Groups** page, click the host group name/ID to go to the
**Dedicated Host Group Details** page, and then click **Host List** and **Create Host**.
2. In the **Create And Add Host** dialog box, enter the **Host Name** and **Description**.
3. Click **Confirm**. After the host is created, you can view and manage the host resources on
the **Dedicated Host Group Details** page. In the **Host List**, view the created host resources, including the **Host Name**, host ID,
**Host Instance Type**, **Available/total VCPUs**, **Available/total Memory**, and **Status**.
When a host resource is no longer needed, click **Delete** in the Actions column of the
**Host List** to delete the host resource.

**Delete a host group**

You can delete a host group that is no longer needed.
1. On the **Dedicated Host Groups** page, click **Delete** in the Actions column of the host
group.
2. Click **OK**.

### 3.6 Manage the system

You can migrate resources and update the instance types of Elastic Compute Service (ECS) instances to meet the dynamic requirements of your business and system performance.

**Migrate resources**

If the personnel of your enterprise or your business requirements change, you can migrate all applications created by a user and the related resources to another user.

> **Warning:** Resource migration involves high risks. You must contact Alibaba Cloud technical support before you perform this operation.

1. Open the Open Network Service Platform console.
2. Click **System Management** in the left-side navigation pane.
3. On the **System Management** page, click **Migrate Resource**.
4. In the **Resource Migration** dialog box, configure the **Destination Account ID (Aliuid)**
and **Authorization Code** parameters and click **Submit**.
**Destination Account ID (Aliuid)**: the ID of the user to which you want to migrate
resources. You can obtain the user ID on the **Users** page in the Apsara Uni-manager Management Console.
**Authorization Code**: Contact Alibaba Cloud technical support to obtain the
authorization code.

**Update instance types of all ECS instances**

You can update the instance types of all ECS instances in the system. This allows you to select an ECS instance of the latest instance type when deploying a service cluster.
1. Open the Open Network Service Platform console.
2. Click **System Management** in the left-side navigation pane.
3. On the **System Management** page, click **Update Instance Type**.
4. In the **Update Instance Type** dialog box, configure the **Authorization Code** parameter
and click **Submit**.

> **Note:** To obtain the authorization code for updating ECS instance types, contact Alibaba Cloud technical support.
