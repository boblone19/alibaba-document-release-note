---
title: "Alibaba Cloud Apsara Stack V3.18.3 cloud gateway User Guide 20241108"
product_version: "V3.18.3"
doc_version: "20241108"
pdf_pages: 26
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 cloud gateway User Guide 20241108.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20cloud%20gateway%20User%20Guide%2020241108.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 cloud gateway User Guide 20241108

## Table of Contents

- 1 CGW overview
- 2 Log on to the Apsara Uni-manager Management Console
- 3 ONSP
  - 3.1 Overview
  - 3.2 Service cluster deployment
    - 3.2.1 Preparations
    - 3.2.2 Create a custom ECS image
    - 3.2.3 Deploy and activate a service cluster
    - 3.2.4 Application Overview
  - 3.3 Open network service
    - 3.3.1 Perform authorization
    - 3.3.2 Route network traffic to a service cluster
    - 3.3.3 Create a network service instance
    - 3.3.4 View service monitoring data
    - 3.3.5 Configure resource sharing
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

**Procedure**

1. In the address bar of the browser, enter the URL of the Apsara Uni-manager Management
Console and press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

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

Open Network Service Platform (ONSP) can automatically deploy the virtual network devices of partners in a separate virtual private cloud (VPC) in a standard and modulized manner. This solution can help enterprises centrally manage their virtual network devices and reduce deployment costs. ONSP supports standard connection, quick deployment, and efficient O&M for network elements, which improves the user experience of services provided by ecology partners. Centralized deployment: Third-party virtual network elements are deployed as clusters in a separate VPC. This allows you to manage the network elements in the same VPC. Private connections: Service traffic is forwarded to third-party network elements based on elastic network interfaces (ENIs). Fault isolation: Active/active clusters and active/standby clusters are supported. If an error is detected in a cluster, network traffic bypasses the cluster and switches to a running cluster.

**Supported service providers**

To view the services and service providers supported by ONSP, go to the Apsara Stack official website. At the bottom of the page, find the **Partners** section. On the **Apsara Stack**
**Software Compatibility** tab, select **Open Network** as the business scenario.

> **Important:** **Standard service provider**: Hillstone.
> **Non-standard service providers**: Alibaba Cloud does not guarantee the high performance or reliability of services provided by non-standard service providers, and supports the utilization of these services only in scenarios documented in test reports.

**Console operations**

ONSP allows you to deploy service clusters and manage resources in the console: Deploy service clusters: You can make preparations, create custom Elastic Compute Service (ECS) images, and deploy and activate service clusters. After the deployment is complete, you can check whether the clusters encounter errors and quickly troubleshoot errors on the cluster overview pages. Manage ONSP resources: You can grant permissions to accounts, route service traffic, create network service instances, configure service monitoring, and manage resource sharing settings.

### 3.2 Service cluster deployment

This document describes how to deploy a service cluster.

#### 3.2.1 Preparations

Before you deploy a service cluster, you need to plan a network architecture, confirm the status of dependency services, and obtain service metadata. Network architecture: Plan an overall network architecture based on the type of network service to deploy and the method to use the network service. Status of dependency services: Check the status of other services on which Open Network Service Platform (ONSP) relies. Before you start the deployment, check the service version and cluster status in Apsara Infrastructure Management. You can proceed only when the service version is correct and the clusters are at desired state.

| Service | Service type | Product code | Cluster type | Version | Description |
|---|---|---|---|---|---|
| Cloud Gateway (CGW) | An open network service platform | nsp | onpCluster | v3.18.2r | The backend service of ONSP. |
| Hybrid Cloud Application Center |   |   |   | v3.18.2r | The frontend page of ONSP. |
| Apsara Uni- manager Management Console | Network functions virtualizatio n (NFV) service | nfv | nfv controller Cl _ _ uster thirdNet _ | v3.18.2r | Supports elastic network interfaces (ENIs) that can route network traffic. |

Service metadata: Service metadata includes the original image file, configuration file, user guide, and O&M guide. To obtain the original image file, contact Apsara Stack technical support. Then, Apsara Stack technical support logs on to Image Center to search for the image based on the image information that you provide, and applies for the image. After the application is approved, a download URL is generated. You can use the Wget utility to download the image from the URL.

#### 3.2.2 Create a custom ECS image

After you obtain the original image file of the open network service from Apsara Stack technical support, you can call the CreateImage API operation to create a custom image. The image can be used to create service clusters.

**Procedure**

1. Obtain the image from Apsara Stack Image Center.

> **Note:** Apsara Stack Image Center is reserved for internal use. You need to contact technical support to apply for images.

2. Upload the image to the `/home/admin/onp_openapi/images` directory on the machine where
the onp-openapi service is deployed.
3. Call the CreateImage API operation to create an image. For more information, see
CreateImage in ECS Developer Guide.

#### 3.2.3 Deploy and activate a service cluster

This topic describes how to import the configuration file of a network service to Hybrid Cloud Application Center based on your business requirements and network architecture. This topic also describes how to deploy and activate a service cluster to enable the network services provided by the service cluster.

**Import service configurations**

Log on to Hybrid Cloud Application Center and import the configurations of the open network service.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **App Store**.
5. On the **App Store** page, click **Import Application**.

> **Note:** To obtain the configuration file of the open network service, contact Apsara Stack technical support.

6. After the configuration file is imported, click the service card to go to the service details
page.

**Deploy a service cluster**

After you import the configuration file of an open network service, you can deploy a service cluster.
1. On the details page of the open network service, click **Deploy** to create a cluster.

| Parameter | Description |
|---|---|
| Cluster Name | The name of the cluster. |
| Region | The region in which you want to deploy the Elastic Compute Service (ECS) instance. |
| Deployment Type | Specifies the mode in which you want to deploy the cluster. Valid values: Standalone: creates only one ECS instance. Active-Standby: creates two ECS instances. The two instances serve as primary and secondary instances. |
| Zone | The zone in which you want to deploy the ECS instance. The cluster can be deployed only in one zone. |
| cidr | The virtual private cloud (VPC) in which you want to deploy the ECS instance. You can click Add CIDR Block to specify a CIDR block for the VPC. A VPC, a vSwitch, and a security group are automatically created in the specified CIDR block. For more information, see Manage CIDR blocks. Note To ensure that the network service can run as expected, we recommend that you specify a private CIDR block whose subnet mask is less than 26 bits in length for the VPC. |
| Deploy on Dedicated Host | Specifies whether to deploy the cluster on a dedicated physical server. Valid values: No and Yes. If you set this parameter to Yes, you must specify the host group and the host on which to deploy the cluster. In the Host Group drop-down list, select an existing host group. You can also click Add Host Group to add a custom host group. For more information, see Manage dedicated host groups. In the Host drop-down list, select a host for deployment. Note If you set the Deployment Type parameter to Standalone, select only one host. If you set the Deployment Type parameter to Active-Standby, select two hosts. |
| ECS Instance Type | The instance type of the ECS instance. You can select instance types only from the drop-down list because network functions virtualization (NFV) network services require certain instance types of ECS instances. ECS instances with higher specifications provide higher capacities and better performance. |

| ECS Image ID | The image that is used to create the ECS instance. For more information about how to create an image, see Create a custom ECS image. |
|---|---|
| Cluster Description | The description of the cluster. |

2. Click **Deploy**.
3. After the cluster is deployed, click **My Applications** in the left-side navigation pane to view
the created application.

> **Note:** You can click the icon on the right of the application card and select **Change**
> **Application Name** to change the name of the application.

4. Optional. Click the name of the application to go to the application details page.

**Create a secondary cluster**

Click **Create Redundant Cluster** in the upper-right corner of the application details page to create a secondary cluster for disaster recovery. To configure parameters for the secondary cluster, you can refer to the parameter description of the primary cluster in the preceding table.

> **Important:** The secondary cluster must be deployed in a zone different from that of the primary cluster. In this case, if a network error occurs in the primary cluster, network traffic is automatically switched to the secondary cluster.

**View cluster information**

On the left of the cluster details tab, view the basic information, detailed information, and endpoint of the cluster. In the **Basic Information** section, you can view the basic information of the cluster including the cluster ID, cluster name, zone ID, CIDR block, CIDR block name, and description.

> **Note:** You can click the icon on the right of the cluster name to modify the
> cluster name.

In the **Cluster Details** section, you can perform the following operations: delete the cluster, scale out the cluster, log on to instances by using Virtual Network Console (VNC), obtain the VNC password, view the details of instances in the cluster, and delete instances from the cluster.

> **Warning:** Deleting a service cluster may result in service disruptions. Proceed with caution.
> You must delete all routing entries that point to the service cluster before you can delete the cluster.

In the **ONSP Endpoint** section, you can create endpoints, view endpoint details, delete endpoints, and view endpoint logs. On the right of the cluster details tab, you can view the name, basic information, operational logs, and scaling logs of the application.

**View routing policies**

In the **Cluster Basic Information** section of the **Routing Policy** tab, you can view the cluster information including the cluster name, cluster ID, zone ID, bypass status, and task progress.

> **Warning:** After routes are configured for the VPC, if an error occurs in a network element, you can click Bypass to withdraw all routes to the destination cluster, and then directly forward traffic to the destination cluster by using Express Connect circuits. After the network element is recovered, you can click **Restore** to restore all routes that are withdrawn.
> The bypass and restore operations involve high risks. We recommend that you contact Apsara Stack technical support before you perform the operations.

In the **Route Details** section of the **Routing Policy** tab, you can add, modify, or delete routes. On the **Service Monitoring** tab, you can view the instance status and network traffic that flows through the elastic network interfaces (ENIs) associated with the service port. For more information, see View service monitoring data.

**View sharing settings**

On the **Sharing Settings** tab, you can enable the sharing feature to allow specific users to view the application and authorize the users to perform operations. For more information, see Configure sharing settings.

**Activate the cluster**

> **Note:** After a service cluster is deployed, you must activate the cluster before you can use it.

Contact technical support of the service provider and provide information about the deployed network service and the ECS instance that is used. Then, a license file is issued to you. Go to the network service page to activate the service cluster by using the license file.

#### 3.2.4 Application Overview

After you deploy and activate a service cluster, you can view the resource status and cluster monitoring data on the Overview page. If an Elastic Compute Service (ECS) instance encounters an error, and the health check result is not Running, the status of the cluster changes to error. Unhealthy clusters are displayed on the monitoring overview list to notify you of anomalies and help you locate errors.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Applications** > **Hybrid Cloud Application Center**.
3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **Overview**.
5. In the **Resource Overview** section, you can view the information about your applications,
including the **alias** and **creation time**. You can also enter an ECS instance ID to search for an application. Click **Details** in the **Actions** column to view more details about the application.

| Item | Description |
|---|---|
| Details page | On the details page of the application, you can view the basic information about the application and configure clusters and endpoints. For more information, see Deploy and activate a service cluster and Route network traffic to a service cluster. |
| Routing Policy tab | On this tab, you can view the routes and public IP address of the application. For more information, see Route network traffic to a service cluster. |
| Service Monitoring | On this tab, you can view the cluster status and network traffic that flows through the elastic network interfaces (ENIs) associated with the service port. For more information, see View service monitoring data. |

| Sharing Settings | On this tab, you can share your applications to other users. For more information, see Configure resource sharing. |
|---|---|

6. In the **Monitoring Overview - Abnormal Clusters** section, you can view unhealthy
clusters and perform troubleshooting. i. Click **Details** in the **Actions** column. ii. Click the **Service Monitoring** tab, and check the **health check result** of the instance. If the status of the instance is not Running, the instance has an error. iii. Click the application name to go to the details page of the application. In the **Cluster**
**Details** section, copy the **VNC password** of the instance and log on to the instance by
using Virtual Network Computing (**VNC**). iv. After you log on to the instance, you can check the status of the instance, view the error details, and then perform troubleshooting.

### 3.3 Open network service

This document describes how to work with an open network service.

#### 3.3.1 Perform authorization

If you use Open Network Service Platform (ONSP) within a cloud account for the first time, you need to grant the required permissions to the cloud account to allow Cloud Gateway (CGW) to manage elastic network interfaces (ENIs) for virtual private clouds (VPCs).

**Prerequisites**

The cloud account is imported as a resource account, and you use ONSP within the account for the first time.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **My Applications**.
5. In the **Letter of Application** message, click **Authorize**.

#### 3.3.2 Route network traffic to a service cluster

**cluster**

This topic describes how to route network traffic to an open network service cluster for the service to run as expected.

**Process**

**Create a VPC and a vSwitch**

Create a virtual private cloud (VPC) and a vSwitch based on your business plan.
1. Log on to the VPC console to create a VPC. For more information, see the "VPC
management" topic in VPC User Guide.
2. Log on to the VPC console to create a vSwitch in which you want to deploy Elastic Compute
Service (ECS) instances. For more information, see the "vSwitch management" topic in VPC User Guide.
3. Create additional vSwitches based on your business requirements.

> **Note:** If you use a virtual load balancer (VLB) in your network, you need to create an additional virtual IP address (VIP) and an additional vSwitch in the VPC so that an IP address is reserved to provide external load balancing services.

**Create an endpoint**

Network traffic is routed to the service cluster by using an elastic network interface (ENI). Therefore, you need to create an ENI in advance. After the ENI is created, it is automatically associated with the service cluster.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **My Applications**. On the My Applications page, click
the application for which you want to create an endpoint.
5. In the **ONSP Endpoint** section, click **Add Endpoint**.
6. In the **Endpoint** dialog box, configure parameters and click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Cluster ID | The ID of the cluster. |
| Endpoint Name | The name of the endpoint. |
| Level-1 Organization UID | The ID of the level-1 organization to which the ENI belongs. You can view the organization ID on the Organizations page in the Apsara Uni- manager Management Console. |

| Source vSwitch ID | The ID of the vSwitch in which the ENI is deployed. You can view the vSwitch ID on the vSwitch page in the VPC console. Note The CIDR block of the vSwitch cannot overlap with the CIDR block of the service cluster. The vSwitch and the service cluster must be deployed in the same zone. |
|---|---|
| Description | The description of the endpoint. |

7. In the **ONSP Endpoint** section, view the information about the resources used for routing
and record the **endpoint ID**, **endpoint IP address**, and **VLAN ID**.
8. Optional. Delete the endpoint if it is changed or no longer needed.
To delete an endpoint, click **Delete** in the Actions column. Before you delete the endpoint, you must delete the routes that point to the ENI.

> **Warning:** Deleting an endpoint may result in network interruptions. Make sure that no network traffic is received by the endpoint.

**Check the result**

After you create an endpoint, an ENI and a security group are automatically created. To view the ENI and security group, log on to the Apsara Uni-manager Management Console and choose **Products** > **Computing** > **Elastic Compute Service** in the top navigation bar. To view the details of the ENI, choose **Network & Security** > **ENIs** in the left-side navigation pane to go to the ENI page.

> **Important:** The ENI is created by the system. We recommend that you do not modify the ENI.

To view the details of the security group or modify the security group rule, choose **Network**
**& Security** > **Security Groups** in the left-side navigation pane to go to the Security
Groups page. The security group is automatically created for the ENI. By default, all inbound and outbound traffic is allowed.

**Configure a cluster network**

After the ENI is created, you need to log on to the ECS instance on the web page and configure a port and a route that points to the CIDR block of the VPC to receive network traffic from the VPC.
1. In the **Cluster Details** section, find the ECS instance that you want to manage and click
**Details** in the **Actions** column.
2. Click **Create** on the right of the **Classic network access** section to create a classic
network.
3. Click the address in the **web access address** column to log on to the ECS instance.
Configure a port and a route that points to the CIDR block of the VPC by using the recorded
**endpoint ID**, **endpoint IP address**, and **VLAN ID**.

> **Note:** If you have any questions during the configuration, contact technical support of the service provider.

4. Go to the portal of the open network service and probe the gateway IP address to test the
network connectivity.

**Configure routes for the VPC**

You need to configure a route that points to the ENI for the VPC. Then, network traffic can be routed to the open network service cluster.
1. Determine the destination CIDR block.

> **Note:** In VLB scenarios, you need to divide the VIP into two CIDR blocks and use one CIDR block as the destination CIDR block.
> In virtual firewall scenarios, you need to specify a destination CIDR block based on the protection type. For example, you need to specify the CIDR block of the peer VPC for VPC-to-VPC protection. For VPC-to-data center protection, you need to specify the CIDR block of the data center.

2. Query the ID of the next hop ENI.
On the **Application Details** page, find the ID of the endpoint based on the VPC and vSwitch.
3. On the **Routing Policy** tab, click **Add Route**.
To enable zone-disaster recovery, specify the secondary endpoint and the cluster to which the secondary endpoint belongs, and specify the same configurations for the network elements of the secondary cluster.

| Parameter | Description |
|---|---|
| Name | The name of the route. |
| Destination CIDR Block | The destination CIDR block. |
| Route Table ID | The ID of the route table to which you want to add the route. |
| Primary Endpoint Cluster | The cluster to which the primary endpoint belongs. |
| Primary Endpoint | The primary endpoint. By default, network traffic is routed to the primary endpoint. |
| Secondary Endpoint Cluster | The cluster to which the secondary endpoint belongs. |

| Secondary Endpoint | The secondary endpoint. By default, network traffic is automatically switched to the secondary endpoint if an error occurs in the primary endpoint. |
|---|---|

4. Click **Submit**.
5. Optional. After routes are configured for the VPC, if an error occurs in a network element,
you can use the Bypass feature to withdraw all routes to the destination cluster, and then directly forward traffic to the destination cluster by using Express Connect circuits. After the network element is recovered, you can use the **Restore** feature to restore all routes that are withdrawn. To withdraw all routes to the destination cluster, click **Bypass** in the **Cluster Basic**
**Information** section, enter the **authorization code**, and then click **Submit**.
To restore all routes that are withdrawn, click **Restore** in the **Cluster Basic**
**Information** section, enter the **authorization code**, and then click **Submit**.

> **Warning:** The bypass and restore operations involve high risks. We recommend that you contact Apsara Stack technical support before you perform the operations.

#### 3.3.3 Create a network service instance

This topic describes how to create a network service instance, such as a Server Load Balancer (SLB) instance or a firewall security policy. For more information, see LB-F5-BIGIPVE Configuration Guide and FW-Hillstone-CloudEdge Configuration Guide. If you encounter any problems, perform the following operations to contact technical support: Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose
**Products** > **Application** > **Application Management** > **Hybrid Cloud Application**
**Center**. In the left-side navigation pane of the Hybrid Cloud Application Center console,
choose **Plugin Center** > **Quick Access** > **ONSP**. In the left-side navigation pane of the ONSP console, click **App Store**. On the App Store page, select a network service and view the contact information of technical support.

#### 3.3.4 View service monitoring data

This topic describes how to view service monitoring data.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. On the **My Applications** page, select the application that you want to view.
5. Click the **Service monitoring** tab and view the information and status of resources.
6. Click **Details** in the Monitoring details column to view the network traffic that flows through
the elastic network interfaces (ENIs) associated with the service port.

#### 3.3.5 Configure resource sharing

This topic describes how to configure resource sharing so that you can share an application with another user to allow the user to create endpoints and manage traffic routing.

> **Important:** Recipient accounts do not have permissions on cluster network management. Therefore, the recipient accounts need to contact the creator of the open network service after they create endpoints. The creator needs to log on to the ECS instances in the cluster to configure networks for the cluster. Then, the cluster can receive network traffic.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Applications** > **Hybrid Cloud Application Center**.
3. In the left-side navigation pane, click **My Applications**, select the application that you
want to manage, and then open the details page.
4. Click the **Sharing Settings** tab.
5. Click **Add Recipient Account** and enter the account name and organization UID.

| Parameter | Description |
|---|---|

| Name | Enter the name of the recipient account. |
|---|---|
| Aliuid | Enter the UID of the organization to which the recipient account belongs. |

6. Click **Add**. After you add a recipient account, the account is listed in the account list.
To remove a recipient account, click **Delete** in the Actions column.

### 3.4 Manage CIDR blocks

CIDR is a method to allocate IP addresses and route data. You can manage CIDR blocks to allocate and utilize IP addresses in a flexible and efficient manner.

**Background information**

CIDR allows you to segment an IP address into multiple subnets. Each subnet can be assigned a different number of IP addresses based on your business requirements. In a CIDR block, an IP address and a prefix length are separated by using a slash (/). The prefix length indicates the number of network prefix bits in the IP address. For example, if a CIDR block is 192.168.0.0/24, 192.168.0.0 indicates the starting IP address of the CIDR block and /24 indicates that the IP address has 24 network prefix bits.

**Limits**

You cannot delete a CIDR block that is in use.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **CIDR Blocks**.

| Operation | Description |
|---|---|

| Create a CIDR block | i. Click Add CIDR Block in the upper part of the CIDR Blocks page. ii. In the Add CIDR Block dialog box, configure the CIDR Block Name and cidr parameters. Note The CIDR block name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. iii. Click OK. |
|---|---|
| Delete a CIDR block | i. Find the CIDR block that you want to delete in the CIDR block list and clickD elete in the Actions column. ii. Click OK. |

### 3.5 Manage dedicated host groups

**groups**

Open Network Service Platform (ONSP) allows you to create and delete host groups, and add dedicated hosts to host groups. After you create a host group and add a dedicated host to the host group, you can deploy your service cluster on the dedicated host.

**Background information**

Host groups are used to manage and organize dedicated hosts. After you create a dedicated host, you have exclusive access to the host and can create Elastic Compute Service (ECS) instances to deploy different services on the host.

**Limits**

You cannot delete a host group that is in use. Before you delete a host group, remove all hosts from the host group. You cannot delete a dedicated host that is in use.

**Create a host group**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **Dedicated Host Groups**.
5. On the **Dedicated Host Groups** page, click **Create Group**.
6. In the **Create Dedicated Host Cluster** dialog box, specify the name, description, region,
zone, and host specifications for the host group.

> **Note:** You can contact Apsara Stack technical support to confirm the host specifications.

7. Click **Confirm**. The host group is created.

**Manage hosts in a host group**

After a host group is created, you can add hosts to the host group. If a host is no longer needed, you can remove the host from the host group.
1. Go to the host adding page.
On the **Dedicated Host Groups** page, find the host group to which you want to add a host and click **Add Host** in the Actions column. On the **Dedicated Host Groups** page, click the name or ID of the host group to which you want to add a host. On the details page of the host group, click **Create Host**.
2. In the dialog box that appears, specify the name and description of the host.
3. Click **OK**. The host is automatically created.
4. On the details page of the host group, view information about the created host. The
information includes the host name, host ID, host specifications, available vCPUs, total vCPUs, and status.
5. Optional. To delete a host that is no longer needed, click **Delete** in the Actions column.

**View host group details**

On the details page of a host group, you can view the basic information, hosts, and applications of the host group.
1. On the **Dedicated Host Groups** page, click the name or ID of a host group to go to the
details page of the host group. The **Basic Information** section displays the following information about the host group: name, ID, status, zone, instance type, available vCPUs, total vCPUs, available memory, and total memory. The **Hosts** section displays the hosts in the host group. For more information about how to manage the hosts, see the Manage hosts in a host group section of this topic. The **Applications** section displays the applications that use the host group. To view the details of an application, click **Details** in the Actions column to go to the application details page.

**Delete a host group**

You can delete a host group that is no longer needed.
1. On the **Dedicated Host Groups** page, find the host group that you want to delete and
click **Delete** in the Actions column.
2. Click **OK**.

### 3.6 Manage the system

You can migrate resources and update the instance types of Elastic Compute Service (ECS) instances to meet dynamic requirements of your business and system performance.

**Migrate resources**

If the personnel of your enterprise or your business requirements change, you can migrate all applications created by a user and the related resources to another user.

> **Warning:** Resource migration involves high risks. You must contact Apsara Stack technical support before you perform this operation.

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application** > **Application Management**
> **Hybrid Cloud Application Center**.

3. In the left-side navigation pane, choose **Plugin Center** > **Quick Access** > **ONSP**.
4. In the left-side navigation pane, click **System Management**.
5. On the **System Management** page, click **Migrate Resource**.
6. In the **Resource Migration** dialog box, configure the **Destination Account ID (Aliuid)**
and **Authorization Code** parameters and click **Submit**.
**Destination Account ID (Aliuid)**: the ID of the user to which you want to migrate
resources. You can obtain the user ID on the **Users** page in the Apsara Uni-manager Management Console.
**Authorization Code**: the authorization code that is used for the resource migration.
Contact Apsara Stack technical support to obtain the authorization code.

**Update instance types of all ECS instances**

You can update the instance types of all ECS instances in the system. This way, you can select an ECS instance of the latest instance type when you deploy a service cluster.
1. On the **System Management** page, select **Update Instance Type**.
2. In the dialog box that appears, configure the **Authorization Code** parameter and click
**Submit**.

> **Note:** To obtain the authorization code, contact Apsara Stack technical support.
