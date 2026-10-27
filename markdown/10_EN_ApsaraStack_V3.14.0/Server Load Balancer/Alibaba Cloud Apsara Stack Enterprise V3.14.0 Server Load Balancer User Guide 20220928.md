---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 72
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Server%20Load%20Balancer%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer User Guide 20220928

## Table of Contents

- 1 What is SLB?
- 2 Log on to the SLB console
- 3 Quick start
  - 3.1 Overview
  - 3.2 Make preparations
  - 3.3 Create an SLB instance
  - 3.4 Configure an SLB instance
  - 3.5 Release an SLB instance
- 4 SLB instances
  - 4.1 SLB instance overview
  - 4.2 Create an SLB instance
  - 4.3 Start and stop an SLB instance
  - 4.4 Tags
    - 4.4.1 Tag overview
    - 4.4.2 Add tags
    - 4.4.3 Query SLB instances by tag
    - 4.4.4 Remove a tag
  - 4.5 Release an SLB instance
- 5 Listeners
  - 5.1 Listener overview
  - 5.2 Add a TCP listener
  - 5.3 Add a UDP listener
  - 5.4 Add an HTTP listener
  - 5.5 Add an HTTPS listener
  - 5.6 Configure forwarding rules
  - 5.7 Enable access control
  - 5.8 Disable access control
- 6 Backend servers
  - 6.1 Backend server overview
  - 6.2 Default server groups
    - 6.2.1 Add and manage a default backend server
    - 6.2.2 Add IDC servers to the default server group
    - 6.2.3 Change the weight of a backend server
    - 6.2.4 Remove a backend server
  - 6.3 VServer groups
    - 6.3.1 Add ECS instances to a VServer group
    - 6.3.2 Add IDC servers to a VServer group
    - 6.3.3 Modify a VServer group
    - 6.3.4 Delete a VServer group
  - 6.4 Active/standby server groups
    - 6.4.1 Add ECS instances to a primary/secondary server group
    - 6.4.2 Add IDC servers to a primary/secondary server group
    - 6.4.3 Delete a primary/secondary server group
- 7 Health check
  - 7.1 Health check overview
  - 7.2 Disable the health check feature
- 8 Certificate management
  - 8.1 Certificate overview
  - 8.2 Certificate requirements
  - 8.3 Upload certificates
  - 8.4 Generate a CA certificate
  - 8.5 Convert the certificate format
  - 8.6 Replace a certificate

## 1 What is SLB?

This topic provides an overview of Server Load Balancer (SLB). SLB distributes inbound network traffic across multiple Elastic Compute Service (ECS) instances that act as backend servers based on forwarding rules. You can use SLB to improve the responsiveness and availability of your applications. Overview After you add ECS instances that are deployed in the same region to a SLB instance, SLB uses virtual IP addresses (VIPs) to virtualize these ECS instances into backend servers in a high-performance server pool that ensures high availability. Client requests are distributed to the ECS instances based on forwarding rules. SLB checks the health status of the ECS instances and automatically removes unhealthy ones from the server pool to eliminate single points of failure (SPOFs). This enhances the resilience of your applications. Components SLB consists of three components: A SLB instance is a running SLB service entity that receives traffic and distributes traffic to backend servers. To get started with SLB, you must create a SLB instance and add at least one listener and two ECS instances to the SLB instance. A listener checks client requests and forwards them to backend servers. It also performs health checks on backend servers. ECS instances are used as backend servers to receive distributed requests. You can separately add ECS instances to the server pool, or use vServer groups or primary/secondary server groups to add and manage ECS instances in batches. Benefits High availability SLB is designed with full redundancy that avoids SPOFs and supports zone-disaster recovery. SLB can be scaled based on application loads and can provide continuous service during traffic fluctuations. High scalability You can increase or decrease the number of backend servers to adjust the load balancing capability of your applications. Cost-effectiveness SLB can save 60% of load balancing costs compared with using traditional hardware solutions. Security You can use SLB with Apsara Stack Security to defend your applications against up to 5 Gbit/s DDoS attacks. High concurrency A SLB cluster supports hundreds of millions of concurrent connections and a single SLB instance supports tens of millions of concurrent connections. e

## 2 Log on to the SLB console

This topic describes how to go to the Server Load Balancer (SLB) console after you log on to the Apsara Uni-manager Management Console by using the Chrome browser. Prerequisites The domain name of the Apsara Uni-manager Management Console is obtained from the engineer that deploys the service before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose Product s > Net working > Server Load Balancer.

## 3 Quick start

### 3.1 Overview

This topic describes how to create an Internet SLB instance and forward client requests to two ECS instances that act as backend servers. Not e Before you create an SLB instance, you must plan its configurations such as the instance type, region, and billing method. Perform the following operations:
1. 创建实例
Create an SLB instance. An SLB instance is an entity running the SLB service.
2. Add listeners and backend servers
After you create an SLB instance, you must add listeners and backend servers. If an SLB instance is no longer needed, delete the instance to avoid extra fees.

### 3.2 Make preparations

This topic describes the considerations for configuring a Server Load Balancer (SLB) instance. Before you create an SLB instance, you must determine the listener type and network type of the SLB instance. Select the region of the SLB instance When you select a region, take note of the following issues: To reduce latency and increase the download speed, we recommend that you select a region that is closest to your customers. To provide more stable and reliable load balancing services, SLB supports primary/secondary zone deployment in most regions. This implements disaster recovery across data centers in the same region. We recommend that you select a region that supports primary/secondary zone deployment. SLB does not support cross-region deployment. Therefore, you must deploy the SLB instance and backend Elastic Compute Service (ECS) instances in the same region. Select the network type of the SLB instance (Internet-facing or internal-facing) SLB provides load balancing services for the public network and internal network: If you want to use SLB to distribute requests from the Internet, create an Internet-facing SLB instance. An Internet-facing SLB instance is assigned a public IP address to receive requests from the Internet. 按流量计费：适用于波峰波谷效应明显的业务。 按带宽计费：适用于带宽较为平稳的业务。 If you want to use SLB to distribute requests from the internal network, create an internal-facing SLB instance. An internal-facing SLB instance is assigned a private IP address and is only accessible from the internal network. Select an instance type Apsara Stack released guaranteed-performance SLB instances on April 1, 2018. When you create an SLB instance, you can choose a guaranteed-performance instance that provides exclusive resources and higher service availability. SLB provides six types of instances: For a pay-as-you-go instance, we recommend that you select the instance type that provides the highest specifications. This guarantees flexible load balancing services at no extra costs. However, if the capacity of Super I (slb.s3.large), the highest-performance instance type, far exceeds the demand of your business, you can select a more appropriate type such as Higher II (slb.s3.medium). Select a listener protocol SLB supports Layer 4 (TCP and UDP) and Layer 7 (HTTP and HTTPS) load balancing: A Layer 4 listener directly distributes requests to backend servers without modifying packet headers. After a client request reaches a Layer 4 listener, SLB uses the backend port that is configured for the listener to establish a TCP connection with a backend ECS instance. A Layer 7 listener functions as a reverse proxy. After a client request reaches a Layer 7 listener, SLB establishes a new TCP connection over HTTP with a backend server, instead of directly forwarding the request to the backend server (ECS instance). Compared with Layer 4 listeners, Layer 7 listeners require an additional step of Tengine processing. Therefore, Layer 4 listeners provide better performance than Layer 7 listeners. In addition, the performance of Layer 7 listeners may be affected by factors such as insufficient client ports or excessive backend server connections. We recommend that you use Layer 4 listeners for high performance purposes. Create backend servers Before you use the SLB service, you must create ECS instances, deploy applications on the ECS instances, and then add the ECS instances to your SLB instance to process client requests. When you create and configure an ECS instance, take note of the following issues: Region and zones of the ECS instance Make sure that the ECS instance is deployed in the same region as the SLB instance. We recommend that you deploy ECS instances in different zones to improve availability. In this example, two ECS instances named ECS01 and ECS02 are created in the China (Hangzhou) region. The following figure shows their basic configurations. Configurations In this example, two static web pages are hosted on ECS01 and ECS02 by using Apache. Enter the elastic IP address (EIP) that is associated with ECS01 in the address bar of your browser. Enter the EIP that is associated with ECS02 in the address bar of your browser. No additional configurations are required after you deploy applications on the ECS instances. However, if you want to use a Layer 4 (TCP or UDP) listener and the ECS instances run Linux, make sure that the following parameters in the net.ipv4.conf file under /etc/sysctl.conf are set to 0:

```
net.ipv4.conf.default.rp_filter = 0 net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.eth0.rp_filter = 0
```

### 3.3 Create an SLB instance

This topic describes how to create a Server Load Balancer (SLB) instance. An SLB instance is a running entity of the SLB service. You can add multiple listeners and backend servers to an SLB instance. Prerequisites Elastic Compute Service (ECS) instances are created and applications are deployed on the ECS instances. The ECS instances and the SLB instance belong to the same organization. In addition, the security group rules configured for the ECS instances allow access from port 80 (HTTP) and port 443 (HTTPS).
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Inst ances.
3. On the Inst ances page, click Creat e Inst ance.
4. Configure the SLB instance and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the SLB instance belongs. Not e Make sure that the SLB instance and its backend servers belong to the same organization. |
| Resource Set | Select the resource group to which the SLB instance belongs. |
| Region | Select the region where you want to deploy the SLB instance. |
| Zone | Select the zone where you want to deploy the SLB instance. |
| Quant it y | Select the number of SLB instances that you want to purchase. |
| Inst ance Name | Enter a name for the SLB instance. If you set Quantity to a value greater than 1, the system automatically assigns names to the SLB instances. |
| Inst ance Edit ion | Select one of the following options: Shared-resource: Shared-resource SLB instances share resources with each other. The performance of shared-resource SLB instances is not guaranteed. High-perf ormance: High-performance SLB instances use exclusive resources. The performance of high-performance SLB instances varies by specification. |
| Inst ance T ype | Select the type of network traffic that you want to distribute. Valid values: Internal Network and Internet. Internal Network is selected in this example. |
| Net work T ype | Select the network type of the SLB instance. Valid values: Classic Network and VPC. VPC is selected in this example. |
| IP Version | Select an IP version. |
| VPC | Select a virtual private cloud (VPC). |
| vSwit ch | Select a vSwitch. |
| Billing Met hod | Set the billing method. |

What's next

### 3.4 Configure an SLB instance

This topic describes how to configure a Server Load Balancer (SLB) instance. Before an SLB instance can forward traffic, you must add at least one listener and one group of backend servers to the SLB instance. The following example shows how to add a TCP listener and Elastic Compute Service (ECS) instances to an SLB instance. The ECS instances are ECS 01 and ECS 02. These ECS instances function as backend servers that host static web pages. Procedure
1. Log on to the SLB console.
2. On the Inst ances page, find the SLB instance that you want to manage and click Conf igure
List ener in the Actions column.
3. On the Prot ocol and List ener wizard page, set the following parameters to configure the
listener. Use the default settings for other parameters. Click Next . Select List ener Prot ocol: Select a listener protocol. T CP is selected in this example. List ening Port : Specify a frontend port to receive and distribute requests to backend servers. In this example, the port is set to 80. The SLB instance uses this port to provide external services. In most cases, port 80 is set for HTTP listeners and port 443 is set for HTTPS listeners. Advanced: Enable Peak Bandwidt h Limit : Applications that run on backend ECS instances provide external services. You can set bandwidth caps to limit service capabilities of applications. Scheduling Algorit hm: SLB supports the following scheduling algorithms. Round-Robin (RR) is selected in this example. Weight ed Round-Robin (WRR): Requests are distributed to backend servers in sequence. Backend servers that have higher weights receive more requests. Round-Robin (RR): Requests are distributed to backend servers in sequence. Consist ent Hash (CH): Only high-performance SLB instances support the CH algorithm. Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port number, and destination port number. Requests that contain the same information based on the four factors are distributed to the same backend server. Round robin
4. On the Backend Servers wizard page, select Def ault Server Group and click Add More to add
backend servers. i. In the Available Servers panel, select ECS 01 and ECS 02 and click Next . ii. A backend server that has a higher weight receives more requests. The default value is 100. We recommend that you use the default value. iii. Click Add. iv. On the Def ault Server Group tab, specify backend ports that are available to receive requests. The ports are used by backend ECS instances to receive requests. You can specify the same port for multiple backend servers that are added to the same SLB instance. The port is set to 80 in this example.
5. Click Next to configure the health check feature. The default health check settings are used in this
example. After you enable health checks for the SLB instance, the SLB instance periodically checks whether the backend ECS instances are healthy. When the SLB instance detects an unhealthy ECS instance, the SLB instance distributes the requests to other healthy ECS instances. When the unhealthy ECS instance recovers, the SLB instance starts to distribute requests to the ECS instance again.
6. Click Next . On the Conf irm wizard page, check the configurations and click Submit .
7. Click OK to go back to the Inst ances page and click
to refresh the page. If the health check state of a backend ECS instance is Act ive, this indicates that the backend server works as expected and can process requests. Instances-2
8. Enter the IP address of the SLB instance into the address bar of the browser to test load balancing
services of the instance. ECS01 ECS02

### 3.5 Release an SLB instance

If an SLB instance is no longer needed, you can release the instance to save costs. The backend ECS instances will not be deleted or affected after you delete an SLB instance. Procedure
1. Log on to the SLB console.
2. On the Inst ances page, find the instance and click
> Release in the Actions column, or select

the instance and click Release at the lower part of the page.
3. In the Release dialog box, select Release Now.
Not e The system performs release operations at 30-minute and hour marks. However, billing for the SLB instance is stopped at the specified release time.
4. Click Next .
5. Click OK to release the SLB instance.
Not e Pay-as-you-go SLB instances cannot be restored once deleted. We recommend that you exercise caution when you release SLB instances.

## 4 SLB instances

### 4.1 SLB instance overview

A Server Load Balancer (SLB) instance is a running entity of the SLB service. To use the SLB service, you must create an SLB instance and add listeners and backend servers to the instance. Instance network types Apsara Stack provides Internet-facing and internal-facing SLB instances. You can create Internet-facing SLB instances or internal-facing SLB instances based on your business requirements. If you create an Internet-facing SLB instance, a public IP address is allocated. If you create an internal-facing SLB instance, a private IP address is allocated. Internet-facing SLB instances An Internet-facing SLB instance distributes client requests over the Internet to backend servers based on configured forwarding rules. An internal-facing SLB instance in a virtual private cloud (VPC) can process requests sent over the Internet only when the instance is associated with an elastic IP address (EIP). The following table provides more detailed information.

| Type | Feature |
|---|---|
| Internet-facing SLB instances After you create an Internet-facing SLB instance, the system allocates a public IP address to the instance. You can bind a domain name to the public IP address to provide external services. | The public IP address is allocated to the SLB instance and cannot be unbound from the instance. Internet-facing SLB instances support only pay- by-data-transfer and pay-by-bandwidth billing methods. |

| Type | Feature |
|---|---|
| Internal-facing SLB instances that are associated with EIPs An internal-facing SLB instance that is associated with an EIP can process requests sent over the Internet. | A public IP address is allocated to the EIP. You can associate the EIP with the SLB instance and disassociate the EIP from the SLB instance based on your requirements. An EIP that is associated with an EIP bandwidth plan supports the 95th percentile bandwidth billing method. |

Internal-facing SLB instances Internal-facing SLB instances can be used only inside Apsara Stack and can forward only requests from clients that can access SLB instances over the internal network. You can select one of the following network types for an internal-facing SLB instance: Classic network If you choose classic network for an internal-facing SLB instance, the IP address of the SLB instance is allocated and maintained by Apsara Stack. This instance can be accessed only by Elastic Compute Service (ECS) instances in the classic network. VPC If you choose VPC for an internal-facing SLB instance, the IP address of the SLB instance is allocated from the CIDR block of the vSwitch that is attached to the VPC. This SLB instance can be accessed only by ECS instances in the VPC. Instance types and specifications Alibaba Cloud provides shared-performance SLB instances and guaranteed-performance SLB instances. Guaranteed-performance SLB instances provide reliable performance metrics. Shared-performance SLB instances All shared-performance SLB instances share SLB resources. This indicates that the instance performance cannot be guaranteed. Guaranteed-performance SLB instances The following content describes three key metrics of guaranteed-performance SLB instances: Maximum number of connections The maximum number of concurrent connections that a CLB instance supports. When the number of existing concurrent connections reaches the upper limit, new connection requests are dropped. Connections per second (CPS) The number of new connections that are established per second. When the CPS value reaches the upper limit, new connection requests are dropped. Queries per second (QPS) The number of HTTP or HTTPS queries (requests) that can be processed per second. This metric is specific to Layer 7 listeners. When the QPS value reaches the upper limit, new connection requests are dropped. Apsara Stack provides four types of guaranteed-performance SLB instances.

| Type | Specification | Max connection | CPS | QPS | Purchase method |
|---|---|---|---|---|---|
| Type 1 | Small I (slb.s1.small) | 5,000 | 3,000 | 1,000 | Available for purchase from the official website of Apsara Stack. |
| Type 2 | Standard I (slb.s2.small) | 50,000 | 5,000 | 5,000 | Available for purchase from the official website of Apsara Stack. |
| Type 3 | Standard II (slb.s2.mediu m) | 100,000 | 10,000 | 10,000 | Available for purchase from the official website of Apsara Stack. |
| Type 4 | Higher I (slb.s3.small) | 200,000 | 20,000 | 20,000 | Available for purchase from the official website of Apsara Stack. |

The following table describes the differences between shared-performance SLB instances and guaranteed-performance SLB instances.

| Feature | Shared-performance SLB instance | Guaranteed-performance SLB instance |
|---|---|---|
| Resource allocation | Shared resources | Exclusive resources |
| Service level agreement for guaranteed availability | Not supported | 99.95% |
| IPv6 | × | √ |
| Server Name Indication (SNI) certificates | × | √ |
| Support for blacklists and whitelists | × | √ |
| Elastic network interface (ENI) mounting | × | √ |
| Assignment of secondary IP addresses to ENIs that are bound to ECS instances | × | √ |
| HTTP-to-HTTPS redirection | × | √ |

| User Guide·SLB instances |   | Server Load Balance |
|---|---|---|

| Feature | Shared-performance SLB instance | Guaranteed-performance SLB instance |
|---|---|---|
| Consistent hashing | × | √ |
| TLS security policies | × | √ |
| HTTP2 | × | √ |
| Websocket(S) | × | √ |

### 4.2 Create an SLB instance

This topic describes how to create a Server Load Balancer (SLB) instance. An SLB instance is a running entity of the SLB service. You can add multiple listeners and backend servers to an SLB instance. Prerequisites Elastic Compute Service (ECS) instances are created and applications are deployed on the ECS instances. The ECS instances and the SLB instance belong to the same organization. In addition, the security group rules of the ECS instances allow access from port 80 (HTTP) and port 443 (HTTPS). Procedure
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Inst ances.
3. On the Inst ances page, click Creat e Inst ance.
Organizat ion: Select an organization for the SLB instance from the drop-down list. Not e Make sure that the organization of the SLB instance is the same as the organization of its backend servers. Resource Set : Select a resource set for the SLB instance from the drop-down list. Region: Select the region where you want to deploy the SLB instance. Zone: Select a zone for the SLB instance from the drop-down list. Inst ance Name: Enter a name for the SLB instance in the Instance Name field. The name must be 2 to 128 characters in length, and can contain letters, digits, full-width characters, hyphens (-), colons (:), periods (.), and underscores (_). Line breaks and spaces are supported. It must start with a letter and cannot start with `http://` or `https://` . Inst ance Edit ion: Select one of the following options: shared-performance and guaranteedperformance. Shared-performance SLB instances share resources with each other. The performance of shared-performance SLB instances is not guaranteed. The performance of guaranteed-performance SLB instances varies by type. Inst ance T ype: Select the type of network traffic that you want to distribute. Valid values: Internal Network and Internet. Net work T ype: Select the network type of the SLB instance. Valid values: Classic Network and VPC. IP Version: Select an IP version. IP Address: Enter a service IP address for the SLB instance. Make sure that the service IP address is valid. Otherwise, the SLB instance cannot be created. If you do not set this parameter, the system automatically allocates an IP address to the SLB instance. Not e The private IP address that you specify must belong to the destination CIDR block of the vSwitch.
4. Click Submit .
What's next Configure a CLB instance

### 4.3 Start and stop an SLB instance

This topic describes how to start and stop an SLB instance. SLB instances can be started or stopped at any time. A stopped SLB instance does not receive or forward client traffic. Procedure
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Find the target SLB instance. In the Act ions column, choose
> St art or

> St op.

4. To start or stop multiple instances at a time, select the instances and click St art or St op at the
bottom of the page.

### 4.4 Tags

#### 4.4.1 Tag overview

This topic provides an overview of tags in SLB. SLB provides the tag management feature that allows you to classify SLB instances by using tags. Each tag consists of a key and a value. Before you use tags, note the following limits: Tags must be added to SLB instances. Each SLB instance can have a maximum of ten tags. You can add or remove a maximum of 5 tags at a time. The key of each tag added to an SLB instance must be unique. If a tag with the same key already exists, the tag is overwritten with the new value.

#### 4.4.2 Add tags

This topic describes how to add tags to an SLB instance.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. In the Act ions column, choose
> Edit T ags.

4. Edit tags in the Edit T ags dialog box.
To add a tag, perform the following operations: To add an existing tag, click Saved T ags and then select a tag. To create and add a new tag, click New T ag in the Edit T ags dialog box, enter the key and value of the new tag, and then click OK next to the value.
5. Click OK.

#### 4.4.3 Query SLB instances by tag

This topic describes how to use tags to query SLB instances. Procedure
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Select a data from the Select a t ag drip-down list to filter instances.
Not e To clear the search condition, move the pointer over the selected tag and click the displayed deletion icon next to it.

#### 4.4.4 Remove a tag

This topic describes how to remove tags from a CLB instance. You can only remove tags for one CLB instance at a time. Procedure
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. In the Act ions column, choose
> Edit T ags.

4. In the Edit T ags dialog box, click the deletion icon next to the tags to be removed, and then click
OK. Not e If a tag is removed from a CLB instance and is not added to other instances, the tag is deleted from the system.

### 4.5 Release an SLB instance

This topic describes how to release an SLB instance. You can release SLB instances immediately. Procedure
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Find the target SLB instance and choose
> Release.

4. In the Release dialog box, select Release Now.
5. Click Next .
6. Confirm the displayed information and click OK to release the instance.

## 5 Listeners

### 5.1 Listener overview

This topic provides an overview of listeners. After you create a Server Load Balancer (SLB) instance, you must configure one or more listeners for it. A listener checks for connection requests and then distributes the requests to backend servers based on the forwarding rules that are defined by a specified scheduling algorithm. SLB provides Layer 4 (TCP and UDP) and Layer 7 (HTTP and HTTPS) listeners. The following table lists the features and use cases of these listeners.

| Protocol | Feature | Use case |
|---|---|---|
| TCP | A connection-oriented protocol. A logical connection must be established before data can be sent and received. Source IP address-based session persistence. Source IP addresses readable at the network layer. Fast data transmission | Applicable to scenarios that require high reliability and data accuracy but can tolerate low speeds, such as file transmission, sending or receiving emails, and remote logons. Web applications that do not have special requirements. For more information, see Add a TCP listener. |
| UDP | A connectionless protocol. UDP transmits data packets directly instead of making a three-way handshake with the other party before UDP sends data. UDP does not provide error recovery or data re-transmission. Fast data transmission but relatively low reliability. | Applicable to scenarios where real-time transmission is more important than reliability, such as video chats and real- time financial market pushes. For more information, see Add a UDP listener. |
| HTTP | An application-layer protocol that is used to package data. Cookie-based session persistence. Use X-Forward-For to obtain source IP addresses. | Applicable to scenarios that require data content to be identified, such as web applications and small mobile games. For more information, see Add an HTTP listener. |
| HTTPS | Encrypted data transmission that prevents unauthorized access. Centralized certificate management service. You can upload certificates to SLB. The decryption operations are directly completed on SLB. | Applicable to scenarios that require encrypted transmission. For more information, see Add an HTTPS listener. |

### 5.2 Add a TCP listener

This topic describes how to add a Transmission Control Protocol (TCP) listener to a Server Load Balancer (SLB) instance. TCP provides reliable and accurate data delivery at relatively low connection speeds. Therefore, TCP applies to file transmission, email sending or receiving, and remote logons. You can add a TCP listener to forward TCP requests. Step 1: Open the listener configuration wizard To open the listener configuration wizard, perform the following operations:
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Inst ances.
3. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the SLB instance and click Conf igure List ener in the Act ions column. On the Inst ances page, click the ID of the SLB instance. On the List ener tab, click Add List ener. Step 2: Configure the TCP listener To configure the TCP listener, perform the following operations:
1. Set the following parameters and click Next .

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select the protocol of the listener. In this example, T CP is selected. |
| List ening Port | Specify the listening port that is used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced |   |

| Parameter | Description |
|---|---|
| Scheduling Algorit hm | SLB supports the following scheduling algorithms: Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are distributed to backend servers in sequence. Consist ent Hash (CH): Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Not e Only high-performance SLB instances support the CH algorithm. |
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from a client to the same backend server. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
| Enable Peak Bandwidt h Limit | Specify whether to set a bandwidth limit for the listener. If an SLB instance is billed based on bandwidth usage, you can set different bandwidth limit values for different listeners. This limits the amount of network traffic that flows through each listener. The sum of the bandwidth limit values of all listeners that are added to an SLB instance cannot exceed the bandwidth limit of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |
| Idle T imeout | Specify the timeout of idle TCP connections. Unit: seconds. Valid values: 10 to 900. |
| Obt ain Client Source IP Address | Backend servers associated with Layer 4 listeners can obtain client IP addresses without additional configurations. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, this feature is enabled. |

Step 3: Add backend servers After you configure the listener, you must add backend servers to process client requests. You can use the default server group that is configured for the SLB instance, or create a vServer group or a primary/secondary server group. For more information, see Backend server overview. Backend servers are added to the default server group in this example.
1. On the Backend Servers wizard page, select Def ault Server Group and click Add More.
2. In the My Servers panel, select the ECS instances that you want to add as backend servers and
click Next .
3. On the Conf igure Port s and Weight s wizard page, specify the weights of the backend servers
that you want to add. A backend server with a higher weight receives more requests. Not e If the weight of a backend server is set to 0, no request is distributed to the backend server.
4. Click Add. On the Default Server Group tab, specify the ports that you want to open on the
backend servers to receive requests. The backend servers are the ECS instances that you selected. Valid values: 1 to 65535. You can specify the same port on different backend servers that are added to an SLB instance.
5. Click Next .
Step 4: Configure health checks SLB performs health checks to check the availability of the ECS instances that serve as backend servers. The health check feature improves overall service availability and reduces the impact of backend server failures. Click Modif y to configure advanced health check settings and click Next. For more information, see Health check overview. Step 5: Submit the configurations To submit the configurations, perform the following operations:
1. On the Conf irm wizard page, check the configurations. You can click Modif y to modify the
configurations.
2. After you confirm the configurations, click Submit .
3. In the Conf igurat ion Successf ul message, click OK.
After you configure the listener, you can view the listener on the Listener tab.

### 5.3 Add a UDP listener

This topic describes how to add a User Datagram Protocol (UDP) listener to a Server Load Balancer (SLB) instance. UDP applies to services that prioritize real-time content delivery over reliability, such as video conferencing and real-time quote services. You can add a UDP listener to forward UDP packets. Context Before you configure a UDP listener, take note of the following items: You are not allowed to specify ports 250, 4789, or 4790 for UDP listeners. They are system reserved ports. Fragmentation is not supported. You cannot view source IP addresses by using the UDP listeners of an SLB instance in the classic network. The following operations take effect 5 minutes after they are performed on a UDP listener: Remove backend servers. Set the weight of a backend server to 0 after it is detected unhealthy. Step 2: Configure the UDP listener To configure the listener, perform the following operations:
1. On the Prot ocol and List ener wizard page, set the following parameters and click Next .

| Parameter | Description |
|---|---|
| List ener Prot ocol | Select a protocol for the listener. In this example, UDP is selected. |
| List ening Port | Set the listening port that is used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced |   |
| Scheduling Algorit hm | SLB supports the following scheduling algorithms: Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are distributed to backend servers in sequence. Consist ent Hash (CH): Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. QUIC ID: specifies consistent hashing that is based on Quick UDP Internet Connections (QUIC) IDs. Requests that contain the same QUIC ID are distributed to the same backend server. Not ice QUIC is implemented based on draft-ietf- quic-transport-10 and is rapidly evolving. Therefore, compatibility is not guaranteed for all QUIC versions. We recommend that you perform tests before you apply the protocol to a production environment. |

| Parameter | Description |
|---|---|
| Enable Session Persist ence | Specify whether to enable session persistence. SLB maintains the persistence of UDP sessions by using consistent hashing that is based on source IP addresses. |
| Enable Peak Bandwidt h Limit | Specify whether to set a bandwidth limit for the listener. If an SLB instance is billed based on bandwidth usage, you can specify different bandwidth limit values for different listeners. This limits the amount of network traffic that flows through each listener. The sum of the bandwidth limit values of all listeners that are added to an SLB instance cannot exceed the bandwidth limit of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |
| Obt ain Client Source IP Address | Backend servers associated with UDP listeners can obtain client IP addresses without additional configurations. Not e You cannot view source IP addresses by using the UDP listeners of an SLB instance in the classic network. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, this feature is enabled. |

Step 3: Add backend servers After you configure the listener, you must add backend servers to process client requests. You can use the default server group that is configured for the SLB instance, or create a vServer group or a primary/secondary server group. For more information, see Backend server overview. Backend servers are added to the default server group in this example.
1. On the Backend Servers wizard page, select Def ault Server Group. Then, click Add More.
2. In the Available Servers panel, select the Elastic Compute Service (ECS) instances that you want
to add as backend servers and click Next .
3. Set weights for the backend servers that you add.
An ECS instance with a higher weight receives more requests. Not e If the weight of a backend server is set to 0, no request is distributed to the backend server.
4. Click Add. On the Default Server Group tab, specify the ports that you want to open on the
backend servers to receive requests. The backend servers are the ECS instances that you selected. Valid values: 1 to 65535. You can specify the same port on different backend servers that are added to an SLB instance.
5. Click Next .
Step 3: Configure health checks CLB checks the availability of backend ECS instances by performing health checks. The health check feature improves service availability and prevents service interruptions caused by single points of failure.
1. (Optional)On the Healt h Check wizard page, click Modif y to modify the health check
configurations. For more information, see 配置和管理健康检查.
2. Click Next .
Step 4: Submit the configurations
1. On the Conf irm Conf igurat ions wizard page, confirm the configurations. You can click Modif y to
modify the configurations.
2. After you confirm the configurations, click Submit .
3. After the configurations are submitted, click OK.
After you configure the listener, you can view the listener on the Listener tab.

### 5.4 Add an HTTP listener

This topic describes how to add an HTTP listener to a Server Load Balancer (SLB) instance. HTTP is applicable to applications that must identify data from different users, such as web applications and mobile games. You can add HTTP listeners to forward HTTP requests. Step 1: Configure an HTTP listener
1. Log on to the SLB console.
2. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the SLB instance that you want to manage and click Conf igure List ener in the Act ions column. On the Inst ances page, click the ID of the SLB instance that you want to manage. On the List ener tab, click Add List ener.
3. Set the following parameters to configure the listener.

| Parameter | Description |
|---|---|
| List ener Prot ocol | Select a protocol for the listener. In this example, HT T P is selected. |
| List ening Port | Specify the listening port that is used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced | Click Modif y to configure advanced settings. |

| Parameter | Description |
|---|---|
| Scheduling Algorit hm | Select a scheduling algorithm. Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are distributed to backend servers in sequence. |
| Redirect ion | Specify whether to redirect traffic from the HTTP listener to an HTTPS listener. Not e Before you enable redirection, make sure that an HTTPS listener is created. |
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from a client to the same backend server. HTTP session persistence is implemented through cookies. You can use one of the following methods to handle cookies: Insert cookie: If you select this option, you need only to specify the timeout period of the cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client contains the cookie. Then, the listener distributes the request to the recorded backend server. Rewrit e cookie: If you select this option, you can specify the cookie that you want to insert into an HTTP or HTTPS response. You must specify the timeout period and the lifetime of a cookie on a backend server. When SLB detects a user-defined cookie, SLB rewrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie. Then, the listener forwards the request to the recorded backend server. |
| Enable Peak Bandwidt h Limit | Specify whether to set a bandwidth limit for the listener. Unit: Mbit/s. Valid values: 0 to 5120. If an SLB instance is billed based on bandwidth usage, you can set different bandwidth limit values for different listeners. This limits the amount of network traffic that flows through each listener. The sum of the bandwidth limit values of all listeners that are added to an SLB instance cannot exceed the bandwidth limit of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |

| Parameter | Description |
|---|---|
| Idle T imeout | Specify the timeout period of idle connections. Unit: seconds. Valid values: 1 to 60. If no request is received within the specified timeout period, SLB closes the connection. SLB recreates the connection when a new connection request is received. |
| Request T imeout | Specify the request timeout period. Unit: seconds. Valid values: 1 to 180. If no response is received from the backend server within the request timeout period, SLB returns an HTTP 504 error to the client. |
| Enable Gzip Compression | Specify whether to enable Gzip compression to compress specific types of files. Gzip supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. |
| Add HT T P Header Fields | You can add the following HTTP headers: Use the X-Forwarded-For header to retrieve the real IP addresses of clients. Use the SLB-ID header to retrieve the ID of the SLB instance. Use the SLB-IP header to retrieve the public IP address of the SLB instance. Use the X-Forwarded-Proto header to retrieve the listener protocol used by the SLB instance. |
| Obt ain Client Source IP Address | Specify whether to retrieve the real IP address of the client. By default, this feature is enabled. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, this feature is enabled. |

4. Click Next .
Step 2: Add backend servers After you configure the listener, you must add backend servers to process client requests. You can use the default server group that is configured for the SLB instance. You can also create a vServer group or a primary/secondary server group. For more information, see Backend server overview. The default server group is selected in this example.
1. On the Backend Servers wizard page, select Def ault Server Group. Then, click Add More.
2. In the My Servers panel, select the Elastic Compute Service (ECS) instances that you want to add
as backend servers and click Next .
3. On the Conf igure Port s and Weight s wizard page, specify the weights of the backend servers
that you want to add. A backend server with a higher weight receives more requests. If the weight of a backend server is set to 0, no request is distributed to the backend server.
4. Click Add. On the Default Server Group tab, specify the ports that you want to open on the
backend servers to receive requests. The backend servers are the ECS instances that you selected. Valid values: 1 to 65535. You can specify the same port on different backend servers that are added to an SLB instance.
5. Click Next .
Step 3: Configure health checks CLB checks the availability of backend ECS instances by performing health checks. The health check feature improves service availability and prevents service interruptions caused by single points of failure.
1. (Optional)On the Healt h Check wizard page, click Modif y to modify the health check
configurations. For more information, see 配置和管理健康检查.
2. Click Next .
Step 4: Submit the configurations
1. On the Conf irm Conf igurat ions wizard page, confirm the configurations. You can click Modif y to
modify the configurations.
2. After you confirm the configurations, click Submit .
3. After the configurations are submitted, click OK.
After you configure the listener, you can view the listener on the Listener tab.

### 5.5 Add an HTTPS listener

This topic describes how to add an HTTPS listener to a Server Load Balancer (SLB) instance. HTTPS is intended for applications that require encrypted data transmission. You can add an HTTPS listener to forward HTTPS requests. Step 1: Configure an HTTPS listener
2. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the SLB instance that you want to manage and click Conf igure List ener in the Actions column. On the Inst ances page, click the ID of the SLB instance that you want to manage. On the List ener tab, click Add List ener.
3. Set the following parameters and click Next .

| Parameter | Description |
|---|---|
| List ener Prot ocol | Select the protocol type of the listener. In this example, HT T PS is selected. |

| r Load Balancer | User Guide·Listener |
|---|---|

| Parameter | Description |
|---|---|
| List ening Port | Specify the listening port that is used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced | Click Modif y to configure advanced settings. |
| Scheduling Algorit hm | Select a scheduling algorithm. Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are distributed to backend servers in sequence. |
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from a client to the same backend server. SLB maintains the persistence of HTTP sessions based on cookies. SLB allows you to use the following methods to process cookies: Insert cookie: If you select this option, you need only to specify the timeout period of the cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client contains the cookie. Then, the listener distributes the request to the recorded backend server. Rewrit e cookie: If you select this option, you can specify the cookie that you want to insert into an HTTP or HTTPS response. You must specify the timeout period and the lifetime of a cookie on a backend server. After you specify a cookie, SLB overwrites the original cookie with the specified cookie. The next time SLB receives a client request that carries the specified cookie, the listener distributes the request to the recorded backend server. |
| Enable HT T P/2 | Select whether to enable HTTP/2.0 for the frontend protocol of the SLB instance. |
| Enable Peak Bandwidt h Limit | Specify whether to set a bandwidth limit for the listener. If an SLB instance is billed based on bandwidth usage, you can set different bandwidth limit values for different listeners. This limits the amount of traffic that flows through each listener. The sum of the bandwidth limit values of all listeners that are added to an SLB instance cannot exceed the bandwidth limit of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |

| Parameter | Description |
|---|---|
| Idle T imeout | Specify the timeout period of idle connections. Unit: seconds. Valid values: 1 to 60. If no request is received within the specified timeout period, SLB closes the connection. SLB recreates the connection when a new connection request is received. |
| Request T imeout | Specify the request timeout period. Unit: seconds. Valid values: 1 to 180. If no response is received from the backend server within the request timeout period, SLB returns an HTTP 504 error to the client. |
| Enable Gzip Compression | Specify whether to enable Gzip compression to compress specific types of files. Gzip supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. |
| Add HT T P Header Fields | You can add the following HTTP headers: Use the X-Forwarded-For header to retrieve the real IP addresses of clients. Use the SLB-ID header to retrieve the ID of the SLB instance. Use the SLB-IP header to retrieve the public IP address of the SLB instance. Use the X-Forwarded-Proto header to retrieve the listener protocol used by the SLB instance. |
| Obt ain Client Source IP Address | Specify whether to retrieve the real IP address of the client. By default, this feature is enabled. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, this feature is enabled. |

Step 2: Configure an SSL certificate When you add an HTTPS listener, you must upload a server certificate or certification authority (CA) certificate , as shown in the following table.

| Item | Description | Required for one-way authentication | Required for mutual authentication |
|---|---|---|---|
| Server cert if ica t e | The certificate that is used to identify the server. Your browser uses the server certificate to verify whether the certificate sent by the server is signed and issued by a trusted CA. | Yes You must upload the server certificate to the certificate management system of SLB. | Yes You must upload the server certificate to the certificate management system of SLB. |

| Item | Description | Required for one-way authentication | Required for mutual authentication |
|---|---|---|---|
| Client cert if ica t e | The certificate that is used to identify the client. The server identifies the client by checking the certificate sent by the client. You can sign a client certificate with a self-signed CA certificate. | No | Yes You must install the client certificate on the client. |
| CA cert if ica t e | The server uses a CA certificate to verify the signature on the client certificate. If the signature is invalid, the connection request is denied. | No | Yes You must upload the CA certificate to the certificate management system of SLB. |

Before you upload a certificate, take note of the following items: SLB supports the following public key algorithms: RSA 1024, RSA 2048, RSA 4096, ECDSA P-256, ECDSA P-384, and ECDSA P-521. The certificate that you want to upload must be in the PEM format. After you upload a certificate to SLB, SLB can manage the certificate. You do not need to bind the certificate to backend servers. It may take a few minutes to upload, load, and verify the certificate. Therefore, an HTTPS listener is not enabled immediately after it is created. It requires about 1 to 3 minutes to enable an HTTPS listener. The ECDHE cipher suite used by HTTPS listeners supports forward secrecy. It does not support the security enhancement parameters that are required by the DHE cipher suite. Therefore, you cannot upload certificates (PEM files) that contain the `BEGIN DH PARAMETERS` field. For more information, see Certificate requirements. HTTPS listeners do not support Server Name Indication (SNI). You can choose TCP listeners and configure SNI on backend servers. By default, the timeout period of session tickets for HTTPS listeners is 300 seconds. The actual amount of data transfer on an HTTPS listener is larger than the billed amount because a portion of data is used for handshaking. If a large number of connections are established, a large amount of data is used for handshaking.
1. On the SSL Cert if icat es wizard page, select the server certificate that you uploaded. You can also
click Creat e Server Cert if icat e to upload a server certificate.
2. To enable mutual authentication or configure a TLS security policy, click Modif y next to
Advanced.
3. Enable mutual authentication, and select an uploaded CA certificate. You can also upload a CA
certificate. Step 3: Add backend servers After you configure the listener, you must add backend servers to process client requests. You can use the default server group that is configured for the SLB instance. You can also create a vServer group or a primary/secondary server group. For more information, see Backend server overview. The default server group is selected in this example.
1. On the Backend Servers wizard page, select Def ault Server Group. Then, click Add More.
2. In the My Servers panel, select the Elastic Compute Service (ECS) instances that you want to add
as backend servers and click Next .
3. Set weights for the selected ECS instances in the Weight column.
Not e An ECS instance with a higher weight receives more requests. The default weight is 100. You can click Reset to set Weight to the default value. If you set the weight of a server to 0, the server does not receive requests.
4. Click Add. Specify the ports for backend servers to receive requests. Valid values: 1 to 65535. Click
Next . You can specify the same port for backend servers that are added to a CLB instance. Step 4: Configure health checks CLB checks the availability of backend ECS instances by performing health checks. The health check feature improves service availability and prevents service interruptions caused by single points of failure. Step 5: Submit the configurations
1. On the Conf irm Conf igurat ions wizard page, confirm the configurations. You can click Modif y to
modify the configurations.
2. After you confirm the configurations, click Submit .
3. After the configurations are submitted, click OK.
After you configure the listener, you can view the listener on the Listener tab.

### 5.6 Configure forwarding rules

This topic describes how to configure forwarding rules for a Server Load Balancer (SLB) instance. You can configure domain name-based or URL-based forwarding rules for an SLB instance that uses Layer 7 listeners. Layer 7 listeners distribute requests destined for different domain names or URLs to different Elastic Compute Service (ECS) instances. Context You can add multiple forwarding rules to a listener. Each forwarding rule is associated with a unique server group. Each server group contains one or more ECS instances. For example, you can configure a listener to forward read requests to one server group and write requests to another server group. This allows you to optimize load balancing among your server resources. SLB forwards requests based on the following rules: If a request matches a domain name-based or URL-based forwarding rule of a listener, the request is forwarded to the corresponding server group based on the forwarding rule. If a request does not match the domain name-based or URL-based forwarding rules of a listener but the listener is associated with a server group, the request is forwarded to the server group. If none of the preceding conditions are met, requests are forwarded to the ECS instances in the default server group of the SLB instance.
1. Log on to the SLB console.
2. Click the ID of the SLB instance that you want to manage. On the List ener tab, find the listener
that you want to manage. You can configure domain name-based or URL-based forwarding rules only for HTTP and HTTPS listeners.
3. Click Conf igure Forwarding Rule in the Act ions column.
4. Configure forwarding rules based on the following information:
Configure a domain name-based forwarding rule When you configure a domain name-based forwarding rule, leave the URL field empty. You do not need to enter a forward slash (/) in this field. The domain name can contain only letters, digits, hyphens (-), and periods (.). Domain-based forwarding rules support both exact matching and wildcard matching. For example, www.aliyun.com is an exact domain name, whereas *.aliyun.com and *.market.aliyun.com are wildcard domain names. When a request matches multiple domain name-based forwarding rules, an exact match prevails over wildcard matches, as described in the following table. Domain name matching rule

| Type | Request URL | Domain name matching rule (√ indicates that the domain name is matched whereas x indicates that the domain name is not matched.) |   |   |
|---|---|---|---|---|
|   |   | www.aliyun.co m | *.aliyun.com | *.market.aliyun.co m |
| Exact match | www.aliyun.com | √ | x | x |
| Wildcard match | market.aliyun.com | x | x | x |
|   | info.market.aliyun.co m | x | x | √ |

Configure a URL-based forwarding rule When you configure a URL-based forwarding rule, leave the Domain Name field empty. The URL can contain only letters, digits, and hyphens (-)./%?#& The URL must start with a forward slash (/). Not e If you enter only a forward slash (/) in the URL field, the URL-based forwarding rule is invalid. URL-based forwarding rules support string matching and adopt sequential matching. Examples: `/admin` , `/bbs_` , and `/ino_test` . Configure both domain name-based and URL-based forwarding rules You can configure both domain name-based and URL-based forwarding rules to forward traffic destined for different URLs of the same domain name. We recommend that you configure a default forwarding rule with the URL field left empty in case errors are returned when the URLs of requests are not matched. For example, the domain name of a website is `www.aaa.com` . You are required to forward requests destined for `www.aaa.com/index.html` to Server Group 1 and forward requests destined for other URLs of the domain name to Server Group 2. To meet the preceding requirements, you must configure two forwarding rules, as shown in the following figure. Otherwise, a 404 error code is returned when a request destined for the `www.aaa.com` domain name does not match all forwarding rules.
5. Click Save.

### 5.7 Enable access control

This topic describes how to enable access control for a listener. You can enable access control for each listener of a Classic Load Balancer (CLB). You can set whitelists for different listeners to regulate network access control. Procedure
1. Log on to the SLB console.
2. Click the ID of the CLB instance.
3. Click the List ener tab, find the listener that you want to manage, and then choose
> Set

Access Cont rol in the Act ions column.
4. Set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Enable Access Cont rol | Enable access control. |
| Access Cont rol Met hod | Whit elist : After you set a whitelist for a listener, the listener forwards only requests from IP addresses or CIDR blocks that are added to the whitelist. However, your business may be adversely affected if the whitelist is not set properly. After you set a whitelist for a CLB listener, only requests from IP addresses or CIDR blocks that are added to the whitelist are distributed by the listener. After you enable the whitelist, if no IP address is added to the whitelist, the listener does not forward requests. |

| Parameter | Description |
|---|---|
| Access Cont rol List | Select a network ACL. IPv6 instances can be associated only with IPv6 network ACLs, and IPv4 instances can be associated only with IPv4 network ACLs. Not e Separate multiple IP entries with commas (,). You can add up to 300 IP entries to each network ACL. IP entries must be unique within each network ACL. |

### 5.8 Disable access control

This topic describes how to disable access control for a listener. Procedure
1. Log on to the SLB console.
2. Find an SLB instance and click its instance ID.
3. Click the List ener tab next to the Inst ance Det ails tab.
4. Find the listener for which you want to disable access control, and choose
> Set Access

Cont rol in the Actions column.
5. In the Access Cont rol Set t ings panel, disable access control and then click OK.

## 6 Backend servers

### 6.1 Backend server overview

Before you use the Server Load Balancer (SLB) service, you must add Elastic Compute Service (ECS) instances as backend servers to an SLB instance to process client requests. Backend server overview You can set virtual IP addresses for an SLB instance. This way, the added ECS instances in the same region can be virtualized into an application service pool that provides high performance and availability. You can manage backend servers by using vServer groups. A listener of an SLB instance can be associated with a specific vServer group so that different listeners can forward requests to their associated backend servers that use different ports. Not e If you associate a vServer group with a listener, the listener distributes requests to backend servers in the associated vServer group instead of those in the default server group. Limits You can increase or decrease the number of backend ECS instances at any time and switch ECS instances to receive client requests. When you perform the operations, make sure that the health check feature is enabled and at least one ECS instance is running as expected to maintain service stability. When you add backend ECS instances, take note of the following items: You can add ECS instances of different operating systems to an SLB instance. However, the applications deployed on the ECS instances must be the same and have consistent data. We recommend that you use ECS instances of the same operating system to facilitate management and maintenance. Up to 50 listeners can be added to a single SLB instance. Each listener corresponds to an application deployed on backend ECS instances. Listening ports of an SLB instance correspond to application service ports that are opened on backend ECS instances. You can specify a weight for each ECS instance in the application service pool. An ECS instance with a higher weight receives more requests. If session persistence is enabled, requests may not be evenly distributed to backend ECS instances. To solve this problem, we recommend that you disable session persistence and check whether the problem persists. If requests are not evenly distributed, troubleshoot the issue in the following way: i. Collect statistics on the access logs of the web service on backend ECS instances for a specified period. ii. Check whether the numbers of access logs of backend ECS instances match SLB configurations. If session persistence is enabled, you must differentiate the access logs for the same IP address. If different weights are configured for backend ECS instances, you must check whether the percentage of access logs is normal based on the percentage of weights. When an ECS instance is undergoing hot migration, persistent connections to SLB may be interrupted. You can solve this problem by reestablishing the connections. Default server groups A default server group contains ECS instances that are used to receive requests. If a listener is not associated with a vServer group or a primary/secondary server group, the listener forwards requests to ECS instances in the default server group. Before you use the SLB service, you must add at least one default backend server to receive client requests forwarded by SLB. For more information, see Add an ECS instance to the default server group. vServer groups You can use a vServer group if you want to distribute different requests to different backend servers or configure forwarding rules based on domain names and URLs. For more information, see Create and manage a vServer group. Primary/secondary server groups A primary/secondary server group contains only two ECS instances. One ECS instance acts as the primary server and the other acts as the secondary server. Health checks are not performed on the secondary server. If the primary server is detected unhealthy, traffic is redirected to the secondary server. After the primary server recovers and is considered healthy, traffic is switched back to the primary server. For more information, see Create and manage a primary/secondary server group. Not e You can add primary/secondary server groups only for TCP and UDP listeners. Related information Add an ECS instance to the default server group Create and manage a vServer group Create and manage a primary/secondary server group

### 6.2 Default server groups

#### 6.2.1 Add and manage a default backend server

This topic describes how to add a default backend server. Before you use the Classic Load Balancer (CLB) service, you must add at least one default backend server to receive client requests. Prerequisites Before you add an Elastic Compute Service (ECS) instance to the default server group, make sure that the following requirements are met: A CLB instance is created. For more information, see Create an SLB instance. ECS instances are created and applications are deployed on the ECS instances to receive requests. Add a default backend server
1. Log on to the SLB console.
2. Find the CLB instance that you want to manage and click its ID.
3. Click the Def ault Server Group tab.
4. Click Add.
5. In the My Servers panel, for Select Servers, select one or more ECS instances that you want to
add to the default server group.
6. Click Next .
7. For Conf igure Port s and Weight s, specify the weight of each ECS instance.
An ECS instance that has a higher weight receives more requests. You can change the weight of a server and then move the pointer over to change the weights of other servers: If you click Replicat e t o Below, the weights of all servers below the current server are set to the weight of the current server. If you click Replicat e t o Above, the weights of all servers above the current server are set to the weight of the current server. If you click Replicat e t o All, the weights of all servers in the default server group are set to the weight of the current server. If you click Reset , when you clear the weight of the current server, the weights of all servers in the default server group are cleared. Not ice Valid values of weights: 0 to 100. If you set the weight of a server to 0, the server does not receive requests. If two servers have the same weight, only one server receives requests.
8. Click Add.
9. Click OK.
Change the weight of a backend server
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Move the pointer over the weight value of the target backend server and click the
icon.
5. Change the weight and then click OK.
A backend server (ECS instance or IDC server) with a higher weight receives more requests. Not ice The weight value ranges from 0 to 100. If the weight of a backend server is set to 0, no requests are sent to the backend server. Remove a backend server
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Find the target backend server and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

#### 6.2.2 Add IDC servers to the default server group

This topic describes how to add servers in on-premises Internet Data Centers (IDCs) as default backend servers to the default server group of an SLB instance. Before you use the SLB service, you must add at least one default backend server to receive client requests forwarded by SLB. Prerequisites Applications are deployed on the IDC servers, and the IDC servers are ready to receive distributed requests. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Click Add IDC Server.
5. In the My Servers dialog box, click Add.
6. Select a VPC from the VPC Connected to IDC drop-down list, enter a name for the IDC server, and
specify the IP address of the IDC server.
7. Click Next .
8. In the Conf igure Port s and Weight s step, specify the weight of each added IDC server.
An IDC server with a higher weight receives more requests. You can change the weight of a server and then move the pointer over to change the weights of multiple servers: Click Replicat e t o Below: The weights of all servers below the current server are set to the weight of the current server. Click Replicat e t o Above: The weights of all servers above the current server are set to the weight of the current server. Click Replicat e t o All: The weights of all servers in the default server group are set to the weight of the current server. Click Reset : The weight fields of all servers in the default server group are cleared. Not ice If the weight of a backend server is set to 0, this backend server no longer receives new requests.
9. Click Add.
10. Click OK.

#### 6.2.3 Change the weight of a backend server

This topic describes how to change the weight of a backend server to adjust the proportion of requests sent to the backend server.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Move the pointer over the weight value of the target backend server and click the
icon.
5. Change the weight and then click OK.
A backend server (ECS instance or IDC server) with a higher weight receives more requests. Not ice The weight value ranges from 0 to 100. If the weight of a backend server is set to 0, no requests are sent to the backend server.

#### 6.2.4 Remove a backend server

This topic describes how to remove a backend server that is no longer needed. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Find the target backend server and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

### 6.3 VServer groups

#### 6.3.1 Add ECS instances to a VServer group

This topic describes how to create a VServer group and then add ECS instances as backend servers to the VServer group. If you associate a VServer group with a listener, the listener distributes requests only to the backend servers in the VServer group instead of other backend servers. Prerequisites Before you create a VServer group, make sure that the following conditions are met: An SLB instance is created. For more information, see Create an SLB instance. You have created ECS instances and deployed applications on these ECS instances to process requests. Context Note the following items before you create a VServer group: An ECS instance can be added to multiple VServer groups. A VServer group can be associated with multiple listeners of an SLB instance. The settings of the VServer group include the settings of ECS instances and application ports.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. On the VServer Groups tab, click Creat e VServer Group.
5. On the Creat e VServer Group page, configure the VServer group.
i. In the VServer Group Name field, enter a name for the VServer group. ii. Click Add. In the My Servers dialog box, select ECS instances that you want to add. iii. Click Next . iv. Specify a port and a weight for each ECS instance and then click Add. Set the ports and weights based on the following information: Port : The backend port opened on an ECS instance to receive requests. You can set the same port number for multiple backend servers of the same SLB instance. In addition, you can click Add Port to add multiple ports for a backend server. Weight : An ECS instance with a higher weight receives more requests. Not ice If the weight of an ECS instance is set to 0, the ECS instance no longer receives new requests. You can change the weight of a server and then move the pointer over to change the weights of multiple servers: Click Replicat e t o Below: The weights of all servers below the current server are set to the weight of the current server. Click Replicat e t o Above: The weights of all servers above the current server are set to the weight of the current server. Click Replicat e t o All: The weights of all servers in the VServer group are set to the weight of the current server. Click Reset : The weight fields of all servers in the VServer group are cleared. Not ice If the weight of a backend server is set to 0, this backend server no longer receives new requests. v. Click Add.
6. Click Creat e.

#### 6.3.2 Add IDC servers to a VServer group

This topic describes how to create a VServer group and then add IDC servers to the VServer group. You can add ECS instances and IDC servers as backend servers to a VServer group. If you associate a VServer group with a listener, the listener distributes requests only to the backend servers in the VServer group instead of other backend servers. Prerequisites Before you create a VServer group, make sure that applications are deployed on the IDC servers and the IDC servers are ready to receive distributed requests. Context Note the following items before you create a VServer group: An IDC server can be added to multiple VServer groups. A VServer group can be associated with multiple listeners of an SLB instance. The settings of the VServer group include the settings of IDC servers and application ports. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. On the VServer Groups tab, click Creat e VServer Group.
5. On the Creat e VServer Group page, configure the VServer group.
i. In the VServer Group Name field, enter a name for the VServer group. ii. Click Add IDC Server. iii. In the My Servers dialog box, click Add. iv. Select a VPC from the VPC Connected to IDC drop-down list, enter a name for the IDC server, and specify the IP address of the IDC server. The IP address of the IDC server must be accessible to the VPC. v. Click Next . vi. Specify a port and weight for each IDC server, and then click Add. Set the ports and weights based on the following information: Port : The backend port opened on an IDC server to receive requests. Multiple ports can be added to an IDC server. You can set the same port number for multiple backend servers of the same SLB instance. Weight : An IDC server with a higher weight receives more requests. Not ice If the weight of an IDC server is set to 0, the IDC server no longer receives new requests. You can change the weight of a server and then move the pointer over to change the weights of multiple servers: Click Replicat e t o Below: The weights of all servers below the current server are set to the weight of the current server. Click Replicat e t o Above: The weights of all servers above the current server are set to the weight of the current server. Click Replicat e t o All: The weights of all servers in the VServer group are set to the weight of the current server. Click Reset : The weight fields of all servers in the VServer group are cleared. Not ice If the weight of a backend server is set to 0, this backend server no longer receives new requests. vii. Click Add.
6. Click Creat e.

#### 6.3.3 Modify a VServer group

This topic describes how to modify the settings of ECS instances or IDC servers in a VServer group. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. Find the target VServer group and then click Edit in the Actions column.
5. Modify the ports and weights of ECS instances or IDC servers, and then click Save.

#### 6.3.4 Delete a VServer group

This topic describes how to delete a VServer group that is no longer needed for traffic distribution. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. Find the target VServer group, and then click Delet e in the Actions column.
5. In the dialog box that appears, click OK.

### 6.4 Active/standby server groups

#### 6.4.1 Add ECS instances to a primary/secondary server group

server group This topic describes how to create a primary/secondary server group and then add ECS instances to the primary/secondary server group. You can use a primary/secondary server group to implement failover between a primary server and a secondary server. By default, the primary server handles all distributed requests. When the primary server fails, traffic is redirected to the secondary server. Prerequisites Before you create a primary/secondary server group, make sure that the following conditions are met: An SLB instance is created. For more information, see Create an SLB instance. You have created ECS instances and deployed applications on these ECS instances to process requests. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. On the Primary/Secondary Server Groups tab, click Creat e Primary/Secondary Server Group.
5. On the Creat e Primary/Secondary Server Group page, configure the primary/secondary server
group. i. In the Primary/Secondary Server Group Name field, enter a name for the primary/secondary server group. ii. Click Add. In the My Servers dialog box, select ECS instances that you want to add in the Select Servers step. You can add up to two ECS instances to a primary/secondary server group. iii. Click Next . iv. Configure the backend ports opened on ECS instances to receive requests, and then click Add. You can set multiple ports for an ECS instance. v. Set an ECS instance as the primary server. vi. Click Creat e.

#### 6.4.2 Add IDC servers to a primary/secondary server group

server group This topic describes how to create a primary/secondary server group and then add IDC servers to the primary/secondary server group. You can use a primary/secondary server group to implement failover between a primary server and a secondary server. By default, the primary server handles all distributed requests. When the primary server fails, traffic is redirected to the secondary server. Prerequisites The IDC servers are created, configured to deploy applications, and ready to receive distributed requests. Procedure
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. On the Primary/Secondary Server Groups tab, click Creat e Primary/Secondary Server Group.
5. On the Creat e Primary/Secondary Server Group page, configure the primary/secondary server
group. i. In the Primary/Secondary Server Group Name field, enter a name for the primary/secondary server group, and then click Add IDC Server. ii. In the My Servers dialog box, click Add. iii. Select a VPC from the VPC Connected to IDC drop-down list, enter a name for the IDC server, and specify the IP address of the IDC server. The IP address of the IDC server must be accessible to the VPC. iv. Click Next . v. Configure the backend ports opened on ECS instances to receive requests, and then click Add. You can set multiple ports for an IDC server. vi. Set a backend server as the primary server. vii. Click Creat e.

#### 6.4.3 Delete a primary/secondary server group

This topic describes how to delete a primary/secondary server group of a Server Load Balancer (SLB) instance. If a primary/secondary server group is no longer needed to forward traffic, you can delete the primary/secondary server group. Procedure
1. Log on to the SLB console.
2. Find the SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. On the Primary/Secondary Server Groups tab, find the primary/secondary server group that you
want to delete and click Delet e in the Act ions column.
5. In the message that appears, click OK.

## 7 Health check

### 7.1 Health check overview

This topic describes the health check feature of Server Load Balancer (SLB). SLB checks the availability of Elastic Compute Service (ECS) instances that act as backend servers by performing health checks. The health check feature improves the overall availability of your frontend business and mitigates the impacts of exceptions that occur on backend ECS instances. After you enable the health check feature, SLB stops distributing requests to ECS instances that are declared unhealthy and distributes new requests to healthy ECS instances. When the unhealthy ECS instances have recovered, SLB starts forwarding requests to these ECS instances again. If your business is highly sensitive to traffic loads, frequent health checks may impact the availability of normal business. To reduce the impacts of health checks on your business, you can reduce the health check frequency, increase the health check interval, or change Layer 7 health checks to Layer 4 health checks. We recommend that you do not disable the health check feature to ensure business continuity. Health check process SLB is deployed in clusters. Node servers in the LVS or Tengine cluster forward data and perform health checks. The node servers in the LVS cluster forward data and perform health checks independently and in parallel based on configured load balancing policies. If an LVS node server detects that a backend ECS instance is unhealthy, this node server no longer sends new client requests to this ECS instance. This operation is synchronized among all node servers in the LVS cluster. SLB uses the CIDR block of 100.64.0.0/10 for health checks. Make sure that backend ECS instances do not block this CIDR block. You do not need to configure a security group rule to allow access from this CIDR block. However, if you have configured security rules such as iptables, you must allow access from this CIDR block. 100.64.0.0/10 is reserved by Alibaba Cloud. Other users cannot use any IP addresses within this CIDR block, and therefore no relevant security risks exist. Health checks of HTTP or HTTPS listeners For Layer 7 (HTTP or HTTPS) listeners, SLB checks the status of backend ECS instances by sending HTTP HEAD requests. The following figure shows the process. For HTTPS listeners, certificates are managed in SLB. To improve system performance, HTTPS is not used for data exchange (including health check data and business interaction data) between SLB and backend ECS instances. The following section describes the health check process of a Layer 7 listener:
1. A Tengine node server sends an HTTP HEAD request that contains the configured domain name to
the internal IP address, health check port, and health check path of a backend ECS instance based on health check settings.
2. After the backend ECS instance receives the request, the ECS instance returns an HTTP status code
based on the running status.
3. If the Tengine node server does not receive a response from the backend ECS instance within the
specified response timeout period, the backend server is declared unhealthy.
4. If the Tengine node server receives a response from the backend ECS instance within the specified
response timeout period, the node server compares the response with the configured status code. If the response contains the status code that indicates a healthy server, the backend server is declared healthy. Otherwise, the backend server is declared unhealthy. Health checks of TCP listeners For TCP listeners, SLB checks the status of backend servers by establishing TCP connections to improve health check efficiency. The following figure shows the process. The following section describes the health check process of a TCP listener:
1. An LVS node server sends a TCP SYN packet to the internal IP address and health check port of a
backend ECS instance.
2. After the backend ECS instance receives the request, the ECS instance returns an SYN-ACK packet if
the corresponding port is listening normally.
3. If the LVS node server does not receive a packet from the backend ECS instance within the
specified response timeout period, the backend ECS instance is declared unhealthy. Then, the node server sends an RST packet to the backend ECS instance to terminate the TCP connection.
4. If the LVS node server receives a packet from the backend ECS instance within the specified
response timeout period, the node server determines that the service runs properly and the health check succeeds. Then, the node server sends an RST packet to the backend ECS instance to terminate the TCP connection. Not e A TCP three-way handshake is conducted to establish a TCP connection. After the LVS node server receives the SYN+ACK packet from the backend ECS instance, the node server sends an ACK packet, and then immediately sends an RST packet to terminate the TCP connection. This process may cause backend ECS instances to think that an error such as an abnormal exit occurred in the TCP connection. Then, these instances may report a corresponding error message, such as `Connection reset by peer` , in logs such as Java connection pool logs. Solution: You can implement HTTP health checks. If you have enabled the feature of obtaining actual client IP addresses on backend ECS instances, you can ignore connection errors caused by the access of the SLB CIDR block. Health checks of UDP listeners For UDP listeners, SLB checks the status of backend ECS instances by sending UDP packets. The following figure shows the process. The following section describes the health check process of a UDP listener:
1. An LVS node server sends a UDP packet to the internal IP address and health check port of an ECS
instance based on health check configurations.
2. If the corresponding port of the ECS instance is not listening normally, the system returns an ICMP
error message, such as `port XX unreachable` . Otherwise, no message is returned.
3. If the LVS node server receives the ICMP error message within the response timeout period, the
backend ECS instance is declared unhealthy.
4. If the LVS node server does not receive any messages from the backend ECS instance within the
response timeout period, the ECS instance is declared healthy. Not e For UDP health checks, the health check result may not reflect the real status of a backend ECS instance in the following situation: If the backend ECS instance uses a Linux operating system, the speed at which ICMP messages in high concurrency scenarios are sent is limited due to the ICMP attack prevention feature of Linux. In this case, even if a service exception occurs, SLB may declare the backend ECS instance healthy because the error message `port XX unreachable` is not returned. Consequently, the health check result deviates from the actual service status. Solution: You can specify a request and a response for UDP health checks. The ECS instance is considered healthy only when the specified response is returned. However, the client must be configured accordingly to return responses. Health check time window The health check feature effectively improves the availability of your services. However, to avoid impacts on system availability caused by frequent switching after failed health checks, the health check status switches only when health checks successively succeed or fail for a specified number of times within a certain time window. The health check time window is determined by the following factors: Health check interval: how often health checks are performed Response timeout: the length of time to wait for a response Health check threshold: the number of consecutive successes or failures of health checks The health check time window is calculated based on the following formula: Time window for health check failures = Response timeout × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1) Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1) Not e The response time of a successful health check is the duration from the time when the health check request is sent to the time when the response is received. When TCP health checks are used, the response time is short and almost negligible because only whether the specific port is alive is checked. For HTTP health checks, the response time depends on the performance and load of the application server and is typically within a few seconds. The health check result has the following impacts on request forwarding: If the health check of the backend ECS instance fails, new requests are distributed to other backend ECS instances. This does not affect client access. If the health check of the backend ECS instance succeeds, new requests are distributed to this instance. The client access is normal. If an exception occurs on the backend ECS instance and a request arrives during a time window for health check failures, the request is still sent to the backend ECS instance. This is because the number of failed health checks has not reached the unhealthy threshold (3 times by default). In this case, the client access fails. Examples of health check response timeout and health check interval The following health check settings are used in these examples: Response T imeout Period: 5 Seconds Healt h Check Int erval: 2 Seconds Healt hy T hreshold: 3 T imes Unhealt hy T hreshold: 3 T imes Time window for health check failures = Response timeout × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1). That is, 5 × 3 + 2 × (3 - 1) = 19 seconds. If the response time of a health check exceeds 19 seconds, the health check fails. The following figure shows the time window from a healthy status to an unhealthy status. Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1). That is, (1 × 3) + 2 × (3 - 1) = 7 seconds. If the response time of a successful health check is less than seven seconds, the health check succeeds. Not e The response time of a successful health check is the duration from the time when the health check request is sent to the time when the response is received. When TCP health checks are used, the response time is short and almost negligible because only whether the specific port is alive is checked. For HTTP health checks, the response time depends on the performance and load of the application server and is typically within a few seconds. The following figure shows the time window from an unhealthy status to a healthy status (assume that it takes 1 second for the server to respond to a health check request). Domain name setting in HTTP health checks When HTTP health checks are used, you can set a domain name for health checks. The setting is optional. Some application servers verify the host field in requests. In this case, the request header must contain the host field. If a domain name is configured in health check setting, SLB adds the domain name to the host field when SLB forwards a request to an application server. If no domain name is configured, the health check request is denied by the application server because it does not contain a host field and the health check may fail. If your application server verifies the host field in requests, you must configure a domain name to make sure that the health check feature works.

### 7.2 Disable the health check feature

This topic describes how to disable the health check feature. If you disable the health check feature, requests may be distributed to unhealthy ECS instances and cause impacts on your business. We recommend that you enable the health check feature. Context Not e You can only disable the health check feature for HTTP and HTTPS listeners. The health check feature for UDP and TCP listeners cannot be disabled. Procedure
1. Log on to the SLB console.
2. On the Server Load Balancer page, find the target SLB instance and click its instance ID.
3. On the List eners tab, find the target listener and click Conf igure in the Act ions column.
4. On the Conf igure List ener page, click Next until the Healt h Check step appears.
5. Turn off Enable Healt h Check.
6. Click Next .
7. Click Submit , and then click OK.

## 8 Certificate management

### 8.1 Certificate overview

This topic provides an overview of the certificates that can be deployed on SLB instances. To use an HTTPS listener, you must upload the required third-party server certificate and digital identification issued by a certificate authority (CA) to SLB. You do not need to configure certificates on backend servers after uploading the certificates to SLB. To upload a third-party certificate, you must have the files that contain the public key and private key of the certificate. HTTPS server certificates and client CA certificates are supported. You can create a maximum of 100 certificates per account.

### 8.2 Certificate requirements

Server Load Balancer (SLB) supports only certificates in the PEM format. Before you upload a certificate, make sure that the certificate content, certificate chain, and private key meet the corresponding format requirements. Certificates issued by a root CA If the certificate was issued by a root certification authority (CA), the received certificate is the only one that needs to be uploaded to SLB. In this case, the website that is configured with this certificate is regarded as a trusted website and does not require additional certificates. The certificate must meet the following format requirements: The certificate must start with `-----BEGIN CERTIFICATE-----` and end with -----END CERTIFICATE- ----. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. The certificate content cannot contain spaces. Certificates issued by an intermediate CA If the certificate was issued by an intermediate CA, the received certificate file contains multiple certificates. You must upload both the server certificate and the required intermediate certificates to SLB. The format of the certificate chain must meet the following requirements: The server certificate must be put first and the content of the one or more required intermediate certificates must be put underneath without blank lines between the certificates. The certificate content cannot contain spaces. Blank lines are not allowed between the certificates. Each line must contain 64 characters. For more information, see RFC1421. Certificates must meet the corresponding format requirements. In most cases, the intermediate CA provides instructions about the certificate format when certificates are issued. The certificates must meet the format requirements. The following section provides a sample certificate chain:

```
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
```

Public keys of certificates SLB supports the following public key algorithms: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521 RSA private keys When you upload a server certificate, you must upload the private key of the certificate. An RSA private key must meet the following format requirements: The private key must start with `-----BEGIN RSA PRIVATE KEY-----` and end with -----END RSA PRIVATE KEY-----, and these parts must also be uploaded. Blank lines are not allowed in the content. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. For more information, see RFC1421. You may use an encrypted private key. For example, the private key starts with `----BEGIN PRIVATE` `KEY-----` and ends with -----END PRIVATE KEY-----, or starts with `-----BEGIN ENCRYPTED PRIVATE` `KEY-----` and ends with -----END ENCRYPTED PRIVATE KEY-----. The private key may also contain `Proc-Type: 4,ENCRYPTED` . In this case, you must first run the following command to convert the private key:

```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```

### 8.3 Upload certificates

This topic describes how to create and upload certificates to Server Load Balancer (SLB). Before you create an HTTPS listener, you must upload the required server certificate and CA certificate to SLB. You do not need to configure certificates on backend servers after you upload the certificates to SLB. Prerequisites A server certificate is purchased. A CA certificate and a client certificate are generated. Context Note that you can create up to 100 certificates with each account.
1. In the left-side navigation pane, click Cert if icat es.
2. On the Certificates page, click Creat e Cert if icat e.
3. In the Creat e Cert if icat e panel, set the required parameters and click Creat e.

| Parameter | Description |
|---|---|
| Cert if icat e Name | Enter a name for the certificate. The name must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), underscores ( ), and _ asterisks (*). |
| Organizat ion | The organization to which the certificate belongs. |
| Resource Group | The resource set to which the certificate belongs. |
| Cert if icat e St andard | Select the type of certificate. You can select Int ernat ional St andard Cert if icat e or Nat ional St andard Cert if icat e. |
| Public Key Cert if icat e | The content of the server certificate. Paste the content into the editor. Click Example to view the valid certificate formats. For more information, see Certificate requirements. |
| Privat e Key | The private key of the server certificate. Paste the private key into the editor. Click Example to view the valid certificate formats. For more information, see Certificate requirements. Not ice A private key is required only when you upload a server certificate. |
| Region | The region where you want to deploy the certificate. |

4. Click Creat e.

### 8.4 Generate a CA certificate

When you configure an HTTPS listener, you can use a self-signed CA certificate. This topic describes how to generate a CA certificate and use the CA certificate to sign a client certificate. Generate a CA certificate by using Open SSL
1. Run the following commands to create a ca folder in the /root directory and then create four
subfolders under the ca folder.

```python
sudo mkdir ca cd ca sudo mkdir newcerts private conf server
```

newcerts is used to store the digital certificate signed by the CA certificate. private is used to store the private Key of the CA certificate. conf is used to store the configuration files used for simplifying parameters. server is used to store the server certificate.
2. Create an openssl.conf file that contains the following information in the conf directory.

```
 [ ca ]
 default_ca = foo
 [ foo ]
 dir = /root/ca
 database = /root/ca/index.txt
 new_certs_dir = /root/ca/newcerts
 certificate = /root/ca/private/ca.crt
 serial = /root/ca/serial
 private_key = /root/ca/private/ca.key
 RANDFILE = /root/ca/private/.rand
 default_days = 365
 default_crl_days= 30
 default_md = md5
 unique_subject = no
 policy = policy_any
 [ policy_any ]
 countryName = match
 stateOrProvinceName = match
 organizationName = match
 organizationalUnitName = match
 localityName = optional
 commonName      = supplied
 emailAddress    = optional
```

3. Run the following command to generate a private Key.

```python
cd /root/ca sudo openssl genrsa -out private/ca.key
```

The following figure is an example of the key generation.
4. Run the following command and input the required information according to the prompts. Press
Enter to generate a csr file.

```python
sudo openssl req -new -key private/ca.key -out private/ca.csr
```

Not e Common Name is the domain name of the SLB instance.
5. Run the following command to generate a crt file:

```python
sudo openssl x509 -req -days 365 -in private/ca.csr -signkey private/ca.key -out privat e/ca.crt
```

6. Run the following command to set the start sequence number for the private Key, which can be
any four characters.

```python
sudo echo FACE > serial
```

7. Run the following command to create a CA Key library:

```python
sudo touch index.txt
```

8. Run the following command to create a certificate revocation list for removing the client
certificate:

```python
sudo openssl ca -gencrl -out /root/ca/private/ca.crl -crldays 7 -config "/root/ca/conf/ openssl.conf"
```

The output is:

```
Using configuration from /root/ca/conf/openssl.conf
```

Sign the client certificate
1. Run the following command to generate a users folder under the ca directory to store the client
Key.

```python
sudo mkdir users
```

2. Run the following command to create a Key for the client certificate:

```python
sudo openssl genrsa -des3 -out /root/ca/users/client.key 1024
```

Not e Enter a pass phrase when creating the Key. It is the password to protect the private Key from unauthorized access. Enter the same password twice.
3. Run the following command to create a csr file for the client Key.

```python
sudo openssl req -new -key /root/ca/users/client.key -out /root/ca/users/client.csr
```

Enter the pass phrase set in the previous step and other required information when prompted. Not e A challenge password is the password of the client certificate. Note that it is not the password of the client Key.
4. Run the following command to sign the client Key.

```python
sudo openssl ca -in /root/ca/users/client.csr -cert /root/ca/private/ca.crt -keyfile /r oot/ca/private/ca.key -out /root/ca/users/client.crt -config "/root/ca/conf/openssl.con
```

`f"` Enter y twice when prompted to confirm the operation.
5. Run the following command to convert the certificate to a PKCS12 file.

```python
sudo openssl pkcs12 -export -clcerts -in /root/ca/users/client.crt -inkey /root/ca/user s/client.key -out /root/ca/users/client.p12
```

Follow the prompts to enter the pass phrase of client Key. Then enter the password used for exporting the client certificate. This password is used to protect the client certificate, which is required when you install the client certificate.
6. Run the following commands to view the generated client certificate:

```
 cd users
```

`ls`

### 8.5 Convert the certificate format

Server Load Balancer (SLB) supports PEM certificates only. Certificates in other formats must be converted to the PEM format before they can be uploaded to SLB. We recommend that you use Open SSL for conversion. Convert DER to PEM DER: This format is usually used on a Java platform. The certificate file suffix is generally . der, . cer, or . crt. Run the following command to convert the certificate format:

```
openssl x509 -inform der -in certificate.cer -out certificate.pem
```

Run the following command to convert the private key:

```
openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem
```

Convert P7B to PEM P7B: This format is usually used in a Windows server and Tomcat. Run the following command to convert the certificate format:

```
openssl pkcs7 -print_certs -in incertificate.p7b -out outcertificate.cer
```

Convert PFX to PEM PFX: This format is usually used in a Windows server. Run the following command to extract the certificate:

```
openssl pkcs12 -in certname.pfx -nokeys -out cert.pem
```

Run the following command to extract the private key:

```
openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes
```

### 8.6 Replace a certificate

This topic describes how to replace a certificate with a new certificate. We recommend that you replace certificates before they expire to avoid impacts on your service.
1. Create and upload a new certificate.
For more information, see Overview.
2. Configure the certificate for the target HTTPS listener.
For more information, see Add an HTTPS listener.
3. On the Cert if icat es page, find the certificate to be replaced and click Delet e in the Actions
column.
4. In the dialog box that appears, click OK.
