---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 cloud gateway User Guide 20230714"
product_version: "V3.16.2"
doc_version: "20230714"
pdf_pages: 21
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 cloud gateway User Guide 20230714.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230718/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20cloud%20gateway%20User%20Guide%2020230714.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 cloud gateway User Guide 20230714

## What is CGW?

Cloud Gateway (CGW) provides scenario-specific network access services to help enterprises efficiently build hybrid clouds and migrate workloads to clouds. -manager Management Console

## Log on to the Apsara Uni-

manager Management Console This topic describes how to log on to the Apsara Uni-manager Management Console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations in
the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click Aut hent icat e. For more information, see the Bind a virt ual MFA device t o enable MFA topic in Apsara Uni-manager Operat ions Console User Guide. stance to a VPC

## Connect a bare metal

instance to a VPC After you create a vSwitch that is exclusive for bare metal instances in a virtual private cloud (VPC), you can submit an application to request Apsara Stack to connect the bare metal instance to the VPC. After your application is approved, the bare metal instance can access the VPC.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
3. In the left-side navigation pane, click VSwit ches.
4. Click Creat e a swit ch to create a vSwitch that is exclusive for bare metal instances.
Basic Information: Set the Origination and Resource Set parameters. Region: Select a region and a zone for the vSwitch. Detailed Settings: Set the Sharing Scope, VPC, Dedicated for Bare Metal Instances, IPv4 CIDR Block, IPv6 CIDR Block, and Description parameters. Import ant Turn on Dedicated for Bare Metal Instances because the vSwitch needs to be exclusive for the bare metal instance.
5. Use Bare Metal Management Service to connect the bare metal instance to the VPC.
i. In the top-navigation bar, choose Product s > Ot hers > Int elligent Operat ions Syst em. ii. In the left-side navigation pane, choose Bare Met al Management Service > Applicat ion Groups. T hen, set Group T ype to Instance. If the Instance group type does not exist, create one first. iii. Select the bare metal instance that you want to add to the application group, and click View Det ails in the Actions column. iv. On the Group Det ails page, click Apply f or Bare Met al Inst ance in t he Machines sect ion. Set the network type to VPC, and specify the organization, resource set, VPC, and VPC subnet. After your application is approved, the bare metal instance can access the VPC. Import ant To avoid potential risks, Bare Metal Management Service does not support bare metal instances that use classic networks.

## ONSP

This document introduces Open Network Service Platform (ONSP) and describes how to deploy a service cluster on ONSP.

### Overview

Open Network Service Platform (ONSP) can automatically deploy virtual network devices in a dedicated virtual private cloud (VPC) in a standard and modelized manner. This solution can centrally manage virtual network appliances and reduce deployment costs. ONSP supports standard access, quick deployment, and efficient O&M for network elements, which improve the user experience of ecological network services for enterprises. Centralized deployment: Third-party virtual network elements are deployed in an exclusive VPC as clusters. The network elements can be managed in the same VPC. Private connections: Service traffic is forwarded to third-party network elements through elastic network interfaces (ENIs). Fault isolation: Active/active clusters and active/standby clusters are supported. If an error is detected in a cluster, network traffic bypasses the cluster and switches to a functioning cluster. Data center disaster recovery: Disaster recovery across data centers is supported for virtual network service clusters. If an error arises in the data center or a virtual network service cluster, network traffic is automatically switched to the secondary cluster. To find a list of services and service providers supported by ONSP, navigate to the Apsara St ack Part ners > Syst em Int egrat ion/Compat ibilit y > Net work Devices tab at the bottom of Alibaba Cloud Apsara Stack and check the devices whose device type is Sof t ware. Console operations are classified into cluster deployment and network management: Service cluster deployment: Deploy clusters on ONSP. The steps include: make preparations, create and configure resource accounts, create custom Elastic Compute Service (ECS) images, and deploy and activate a cluster. Manage ONSP resources: The steps include: grant permissions to accounts, route service traffic, create a network service instance, configure service monitoring, and manage resource sharing settings.

### Service cluster deployment

This document describes how to deploy a service cluster.

#### Preparations

Before you deploy a service cluster, you need to plan a network architecture, confirm the status of dependency services, and obtain service metadata. Network architecture: plan an overall network architecture based on the type of network service to deploy and the method to use the network service. Status of dependency services: Check the status of other services on which Open Network Service Platform (ONSP) relies. Before you start the deployment, check the service edition and cluster status in Apsara Infrastructure Management. You can proceed only when the service edition is correct and the clusters are in the ready state.

| Project name | Specif icat i on | Product name | Clust er t ype | Edit ion | Feat ure |
|---|---|---|---|---|---|
| Cloud Gateway (CGW) | An open network service platform | nsp | onpCluster | v3.16.2r | The backend service of ONSP. |
| Hybrid Cloud Application Center |   |   |   | v3.16.2r | The frontend page of ONSP. |
| Apsara Uni- manager | Virtualized network services | nfv | nfv controller _ _ Cluster thirdN _ et | v3.16.2r | Support elastic network interfaces (ENIs) that can route network traffic. |

Service metadata: Service metadata includes the original image file, configuration file, user guide, and O&M guide. To obtain the original image file, contact Apsara Stack technical support. Then, Apsara Stack technical support logs on to Image Center to search for the image based on the image information that you provide, and applies for the image. After the application is approved, a download URL is generated. You can use the Wget utility to download the image from the URL.

#### Create and manage resource accounts

All service clusters on Open Network Service Platform (ONSP) must belong to the same resource account. Therefore, you must first create and configure a resource account. The service account owns the service clusters and relevant resources. Therefore, we recommend that you assign the resource account to the organization of the IT department.
1. Log on to the Apsara Uni-manager Management Console, and create and manage an organization,
resource sets, and resource users. This organization is exclusive to ONSP. We recommend that you do not deploy service resources in this organization. For more information, see Enterprise Center in Apsara Uni-manager User Guide.
2. In the Apsara Uni-manager Management Console, choose Applicat ions > Hybrid Cloud
Applicat ion Cent er.
3. In the left-side navigation pane, choose Syst em Management > Account Management .
Before you create and manage an open network service in Hybrid Cloud Application Center, you must import the organization as a cloud account.
4. Click Import Account and set the parameters. The following table describes the parameters.

| Paramet er | Descript ion |
|---|---|
| Cloud Service Provider | Apsara Stack |
| Alias | Enter an alias for the resource account. |
| Account | Enter the AccessKey ID of the resource account. |
| Account Key | Enter the AccessKey secret of the resource account. |
| regionId | Enter the ID of the region to which the resource account belongs. |
| Organizatio n | Enter the name of the organization to which the resource account belongs. |
| Resource Set | Enter the ID of the resource set to which the resource account belongs. |
| primaryKey | Enter the primary key of the resource account. The primary key is also the UID of the organization. |

5. Click Import .

#### Create a custom ECS image

After you obtain the original image file of the open network service from Apsara Stack technical support, you can call the CreateImage API operation to create a custom image. The image can be used to create service clusters.
1. Obtain the image from Apsara Stack Image Center.
Apsara Stack Image Center is reserved for internal use. You need to contact technical support to apply for images.
2. Upload the image to the `/home/admin/onp_openapi/images` directory on the machine where the
onp-openapi service is deployed.
3. Call the CreateImage API operation to create an image. For more information, see CreateImage in ECS
Developer Guide.

#### Deploy and activate a service cluster

This topic describes how to import the configuration file of a network service to Hybrid Cloud Application Center based on business requirements and network architectures. You also need to deploy and activate a service cluster to enable it to provide network services. Import service configurations Log on to Hybrid Cloud Application Center and import the configurations of the open network service.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Applicat ions > Hybrid Cloud Applicat ion Cent er.
3. In the left-side navigation pane, click App St ore.
4. On the App St ore page, click Import Applicat ion.
To obtain the configuration file of the open network service, contact Apsara Stack technical support.
5. After you import the configuration file, click the Open Net work Services category to view the
details about the service. Deploy a service cluster After you import the configuration file, you can deploy a service cluster.
1. Navigate to the Hybrid Cloud Applicat ion Cent er > App St ore page, select the Open Network
Services category, and then click the card of the service that you want to deploy to go to the details page.
2. You can click Deploy to deploy a service cluster, or click Free T rial to deploy a trial run cluster.

| Paramet er | Descript ion |
|---|---|
| Cluster Name | Enter a name for the cluster. |
| Account Name | Select the resource account. |
| Region | Select the region in which the Elastic Compute Service (ECS) instance is deployed. |
| Deployment Type | Select whether to deploy the cluster in standalone or active-standby mode. Standalone specifies that only one ECS instance will be created. Active-Standby specifies that two ECS instances will be created. The ECS instances work as primary and secondary instances. |
| Zone | Select the zone in which the ECS instance is deployed. The cluster can be deployed only in one zone. |

| CIDR Block | The virtual private cloud (VPC) in which the ECS instance is deployed. You can add Add CIDR Block to specify a CIDR block for the VPC. A VPC, a vSwitch, and a security group are automatically created in the specified CIDR block. Not e To ensure that the network service can run as expected, we recommend that you specify a private CIDR block whose subnet mask is smaller than 26 bits for the VPC. |
|---|---|
| ECS Instance Type | Select an ECS instance type. Network functions virtualization (NFV) network services require certain types of ECS instance. You can select ECS instance types from the drop-down list. ECS instances with higher specifications provide higher capacities and better performance. |
| ECS Image ID | Select the image that is used to create the ECS instance. The image is the custom image created in Create a custom ECS image. |
| Cluster Description | Enter a description for the cluster. |

3. Click Deploy to start the deployment. You can click View Det ails to go to the details page of the
cluster. You can also view the cluster on the My Applicat ions page. What to do next To delete a service cluster, click Delet e Clust er on the right side of the Details section. Warning Deleting a service cluster may result in service disruptions. Proceed with caution. You must delete all routing entries that point to the service cluster before you can delete the cluster. To scale out a service cluster, click Scale out Clust er on the right side of the Details section. To create a redundant cluster, click Creat e Redundant Clust er in the upper-right corner of the application details page. Import ant The redundant cluster must be deployed in a different zone than the primary cluster. If an error arises in the primary cluster, network traffic is automatically switched to the redundant cluster. Activate the cluster After you deploy a service cluster, you must activate the cluster before you can use it. Contact technical support and provide the network service that you want to deploy and the information about the ECS instance that you want to use. Then, a license file is issued to you. Go to the network service page to activate the service cluster.

### Open network service

This document describes how to work with an open network service.

#### Grant permissions to an account

The first time a cloud account uses an open network service, you need to grant the required permissions to the cloud account to allow Cloud Gateway (CGW) to manage elastic network interfaces (ENIs) for virtual private clouds (VPCs). Prerequisites The cloud account is imported as a resource account, and it is the first time the cloud account uses the open network service.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Applicat ions > Hybrid Cloud Applicat ion Cent er.
3. In the left-side navigation pane, click My Applicat ions.
4. In the Let t er of Applicat ion message, click Aut horize.

#### Route network traffic to a service cluster

This topic describes how to route network traffic to an open network service cluster. Create a virtual private cloud (VPC) and a vSwitch Create a VPC and a vSwitch based on your business plan.
1. Log on to the VPC console to create a VPC. For more information, see Manage VPCs in VPC User Guide.
2. Log on to the VPC console to create a vSwitch in which you want to deploy Elastic Compute Service
(ECS) instances. For more information, see Manage vSwitches in VPC User Guide.
3. Create a vSwitch based on your business requirements.
If you use a virtual load balancer (VLB) in your network, you need to create an additional virtual IP address (VIP) and an additional vSwitch in the VPC so that an IP address is reserved to provide external services. Add an Open Network Service Platform (ONSP) endpoint Network traffic is routed to the open network service cluster through an elastic network interface (ENI). Therefore, you need to add an ENI in advance. The ENI is automatically associated with the open network service cluster.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Applicat ions > Hybrid Cloud Applicat ion Cent er.
3. In the left-side navigation pane, click My Applicat ions and click the cluster that you want to
manage.
4. In theONSP Endpoint section, click Add Endpoint .
5. In the Endpoint dialog box, set the parameters and click OK.

| Paramet er | Descript ion |
|---|---|
| Endpoint Name | Enter a name for the endpoint. |
| Organization UID | Enter the UID of the organization to which the ENI belongs. |
| Source vSwitch ID | Enter the ID of the vSwitch in which the ENI is deployed. Not e The CIDR block of the vSwitch must not overlap with that of the open network service cluster. The vSwitch and the open network service cluster must be deployed in the same zone. |
| Description | Enter a description for the endpoint. |

6. In the ONSP Endpoint section, view the information about the resources used for routing. Record
the endpoint ID, endpoint IP address, and VLAN ID. Result After you add an endpoint, an ENI and a security group are automatically created. You can view the security group in the ECS console. To view the details about the ENI, navigate to the Net work & Securit y > ENIs page. Import ant The ENI is created by the systemWe recommend thatyou do notmodify the ENI The ENI is created by the system. We recommend that you do not modify the ENI. To view or modify the security group rule, navigate to the Net work & Securit y > Securit y Groups page. A security group is automatically created for the ENI. By default, all inbound and outbound traffic is allowed. Related operations Remove an ONSP endpoint : To remove an endpoint, click Delet e in the Actions column. Before you remove an endpoint, make sure that all route entries that point to the ENI and the elastic IP addresses (EIPs) associated with the ENI are deleted. Warning Removing an endpoint may result in network interruptions. Make sure that no network traffic is forwarded to the endpoint. Proceed with caution. Configure a cluster network After you create an ENI, you need to log on to the ECS instance and configure a port and a CIDR block for receiving network traffic from the VPC.
1. In the cluster details section, find the ECS instance that you want to manage and click Det ails in the
Act ions column.
2. Click Creat e on the right side of the Classic Network section.
3. Log on to the ECS instance through the classic network created in Step 2. Then, configure a port and
a route entry that points to the CIDR block of the VPC by specifying the endpoint ID, endpoint IP address, and VLAN ID. If a problem persists, contact technical support.
4. Go to the page of the open network service and probe the gateway IP address to test the network
connectivity. Configure VPC routes Configure a route that points to the ENI for the VPC. Then, network traffic can be routed to the open network service cluster.
1. Determine the destination CIDR block.
In VLB scenarios, VIPs need to be divided into two CIDR blocks. One of the CIDR blocks is the destination CIDR block. In virtual firewall scenarios, you need to specify a destination CIDR block. For example, you need to specify the CIDR block of the peer VPC for VPC-to-VPC communication. For VPCto-data center communication, you need to specify the CIDR block of the data center.
2. Query the ID of the next hop ENI.
On the Applicat ion Det ails page, find the ID of the endpoint based on the VPC and vSwitch.
3. On the Rout ing Policy tab, click Add Rout e.
Zone-disast er recovery: To enable zone-disaster recovery, specify the secondary endpoint and the cluster to which the secondary endpoint belongs, and specify the same configurations for the network elements of the secondary cluster.

| Paramet er | Descript ion |
|---|---|
| Name | Enter a name for the route. |

| Destination CIDR Block | Enter a destination CIDR block. |
|---|---|
| Route Table ID | Enter the ID of the route table to which you want to add the route. |
| Primary Endpoint Cluster | Specify the cluster to which the primary endpoint belongs. |
| Primary Endpoint | By default, network traffic is routed to the primary endpoint. |
| Secondary Endpoint Cluster | Specify the cluster to which the secondary endpoint belongs. |
| Secondary Endpoint | By default, network traffic is automatically switched to the secondary endpoint if the primary endpoint encounters an error. |

4. Click Submit .
Enable Internet access You need to configure a public IP address to route Internet traffic to the open network service cluster. This allows requests from the Internet to access the service cluster.
1. On the Rout ing Policy tab, click Add Public IP.
To enable zone-disaster recovery, assign a public IP address to each of the primary and secondary data centers, and mount both the public IP addresses to the Global Server Load Balancing (GSLB) instance.

| Paramet er | Descript ion |
|---|---|
| Name | Enter a name for the public IP address. |
| Bandwidth | Enter a maximum bandwidth value for the public IP address. |
| Primary Endpoint Cluster | Specify the cluster to which the primary endpoint belongs. |
| Primary Endpoint | By default, network traffic is routed to the primary endpoint. |

| Secondary Endpoint Cluster | This parameter is not in use. Skip this parameter. |
|---|---|
| Secondary Endpoint | This parameter is not in use. Skip this parameter. |

2. Click Submit . After you submit the configurations, the details about the public IP address are
displayed in the public IP address list.

#### Create a network service instance

This topic describes how to create a network service instance, such as a Server Load Balancer (SLB) instance or a firewall security policy. For more information, see LB-F5-BIGIPVE Configuration Guide and FW-Hillstone-CloudEdge Configuration Guide. If an issue persists, navigate to the Applicat ions > Hybrid Cloud Applicat ion Cent er > App St ore > Open Net work Services page, find the network service, view the contact information about technical support, and then request technical support.

#### View service monitoring data

This topic describes how to view service monitoring data.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Applicat ions > Hybrid Cloud Applicat ion Cent er.
3. On the My Applicat ions page, select the application that you want to view.
4. Click the Service Monit oring tab, and view the information and status of the resources.
5. Click Det ails to view the monitoring data of network traffic that flows through the ENIs associated
with the service port.

#### Configure resource sharing

This topic describes how to configure resource sharing so that you can share an application with another user to allow the user to create endpoints and manage traffic routing. Import ant Recipient accounts do not have permissions on cluster network management. Therefore, the recipient accounts need to contact the creator of the open network service after they create endpoints. The creator needs to log on to the ECS instances in the cluster to configure networks for the cluster. Then, the cluster can receive network traffic.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Applicat ions > Hybrid Cloud Applicat ion Cent er.
3. In the left-side navigation pane, click My Applicat ions, select the application that you want to
manage, and then open the details page.
4. Click the Sharing Set t ings tab.
5. Click Add Recipient Account and enter the account name and organization UID.

| Paramet er | Descript ion |
|---|---|
| Name | Enter the name of the recipient account. |
| Aliuid | Enter the UID of the organization to which the recipient account belongs. |

6. Click Add. After you add a recipient account, the account is listed in the account list.
To remove a recipient account, click Delet e in the Actions column.
