---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 73
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Server%20Load%20Balancer%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Server Load Balancer User Guide 20220928

## Table of Contents

- 1 What is SLB?
- 2 Log on to the SLB console
- 3 Quick start
  - 3.1 Overview
  - 3.2 Before you begin
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
    - 4.4.4 Remove tags
  - 4.5 Release an SLB instance
- 5 Listeners
  - 5.1 Listener overview
  - 5.2 Add a TCP listener
  - 5.3 Add a UDP listener
  - 5.4 Add an HTTP listener
  - 5.5 Add an HTTPS listener
  - 5.6 Enable access control
  - 5.7 Disable access control
- 6 Backend servers
  - 6.1 Backend server overview
  - 6.2 Default server groups
    - 6.2.1 Add ECS instances to the default server group
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
  - 8.3 Upload a certificate
  - 8.4 Generate a CA certificate
  - 8.5 Convert the certificate format
  - 8.6 Replace a certificate

## 1 What is SLB?

This topic provides an overview of Server Load Balancer (SLB). SLB distributes inbound network traffic across multiple Elastic Compute Service (ECS) instances that act as backend servers based on forwarding rules. You can use SLB to improve the responsiveness and availability of your applications. Overview After you add ECS instances that reside in the same region to an SLB instance, SLB uses virtual IP addresses (VIPs) to virtualize these ECS instances into backend servers in a high-performance server pool that ensures high availability. Client requests are distributed to the ECS instances based on forwarding rules. SLB checks the health status of the ECS instances and automatically removes unhealthy ones from the server pool to eliminate single points of failure (SPOFs). This enhances the resilience of your applications. Components SLB consists of three components: An SLB instance is a key load-balancing component in SLB. It receives traffic and distributes traffic to backend servers. To get started with SLB, you must create an SLB instance and add at least one listener and two ECS instances to the SLB instance. A listener checks for connection requests from clients, forwards requests to backend servers, and performs health checks on backend servers. ECS instances are used as backend servers in SLB to receive and process distributed requests. ECS instances can be added to the default server group of an SLB instance. You can also add multiple ECS servers to VServer groups or primary/secondary server groups after the corresponding groups are created. Benefits High availability SLB features full redundancy that avoids SPOFs and supports zone-disaster recovery. You can use SLB with Apsara Stack DNS to achieve geo-disaster recovery with an availability of up to 99.95%. SLB can be scaled based on network traffic to protect your services from outages caused by fluctuating traffic flows. Strong scalability You can increase or decrease the number of backend servers to adjust the load balancing capacity for your applications. Low costs SLB can save 60% of load balancing costs compared with using traditional hardware solutions. Outstanding security You can use SLB with Apsara Stack Security to defend your applications against 5 Gbit/s distributed denial of service (DDoS) attacks. High concurrency An SLB cluster supports hundreds of millions of concurrent connections, and a single SLB instance supports tens of millions of concurrent connections. e

## 2 Log on to the SLB console

This topic provides an example of how to log on to the Server Load Balancer (SLB) console by using Google Chrome. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net working > Server Load Balancer.

## 3 Quick start

### 3.1 Overview

This quick start tutotial describes how to create a public-facing Server Load Balancer (SLB) instance and how to forward requests to two backend servers. Before creating an SLB instance, you must determine the region, type, and billing method of the SLB instance. For more information, see Preparations. This tutotial includes the following content:
1. 创建实例
Create an SLB instance. An SLB instance is a running entity of the SLB service.
2. Add listeners and backend servers.
Configure listening rules and backend servers for the SLB instance. If you no longer need the SLB instance, delete it to avoid extra fees.

### 3.2 Before you begin

This article presents the essential considerations for configuring an SLB instance. Before you create an SLB instance, you must determine the types of listeners and the network traffic you want to balance. Instance region When you select a region, note the following points: To reduce latency and increase the download speed, we recommend that you select a region closest to your end-users. SLB offers stable and reliable load balancing services by providing support for primary/secondary failovers in most regions. This implements disaster recovery across different zones within the same region. We recommend that you select a region that supports the primary/secondary SLB deployment. SLB instances cannot span across regions. Therefore, you must make sure that the SLB instance and its backend Elastic Compute Service (ECS) instances are located in the same region. Network traffic SLB provides load balancing services for both Internet and internal network traffic: If you need to use SLB to distribute requests from the Internet, you can create an Internet-facing SLB instance. An Internet-facing SLB instance comes with a public IP address to receive requests from the Internet. Pay-by-data-transfer: applicable to services with significant traffic fluctuations Pay-by-bandwidth: applicable to services with stable traffic throughput If you need to use SLB to distribute requests from the internal network, you can create an internal SLB instance. Internal SLB instances only have private IP addresses and are only accessible from the internal network and not from the Internet. Listener protocol SLB supports Layer-4 load balancing of Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) traffic, and Layer-7 load balancing of HTTP and HTTPS traffic. A Layer-4 listener directly distributes requests to backend servers without modifying packet headers. After a client request reaches a Layer-4 listener, SLB uses the backend port configured for the listener to establish a TCP connection with an Elastic Compute Service (ECS) instance (backend server). A Layer-7 listener is implemented as a reverse proxy. After a client request reaches a Layer-7 listener, SLB establishes a new TCP connection over HTTP to a backend server, instead of directly forwarding the request to the backend server (ECS instance). Compared with Layer-4 listeners, Layer-7 listeners require an additional step of Tengine processing. Therefore, Layer-4 listeners provide better performance than Layer-7 listeners. In addition, the performance of Layer-7 listeners can also be affected by factors such as insufficient client ports or excessive backend server connections. Therefore, we recommend that you use Layer-4 listeners for high-performance load-balancing services. Backend servers Before you use the SLB service, you must create ECS instances, deploy applications on them, and add the ECS instances to your SLB instance to process client requests. When you create and configure an ECS instance, note the following points: Select a region and zone for the ECS instance Make sure that the ECS instance resides in the same region and Virtual Private Cloud (VPC) as the SLB instance. We recommend that you deploy ECS instances in different zones to improve availability. In this example, two ECS instances named ECS01 and ECS02 are created in the China (Hangzhou) region. The following figure shows their basic configurations. Configure applications In this example, two static web pages are built on ECS01 and ECS02 by using Apache. Enter the Elastic IP address (EIP) associated with ECS01 in the address box of your browser. Enter the EIP associated with ECS02 in the address box. No additional configuration is required after you deploy applications on the ECS instances. However, if you need to use a Layer-4 (TCP or UDP) listener and the ECS instances run on Linux, make sure that the following parameters in the net.ipv4.conf file under /etc/sysctl.conf are set to 0:

```
net.ipv4.conf.default.rp_filter = 0 net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.eth0.rp_filter = 0
```

### 3.3 Create an SLB instance

This topic describes how to create an SLB instance. To get started with SLB, you must create an SLB instance. You can add multiple listeners and backend servers to an SLB instance. Prerequisites You have created ECS instances and deployed applications on them. The ECS instances and the SLB instance belong to the same organization. In addition, the security group rules of the ECS instances permit traffic on HTTP port 80 and HTTPS port 443.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. On the Server Load Balancers page, click Creat e Inst ance.
Organizat ion: Select the organization to which the SLB instance belongs. Make sure that the organization of the SLB instance is the same as the organization of its backend servers. Resource Set : Select the resource set to which the SLB instance belongs. Region: Select a region for the SLB instance. Zone: Select a zone for the SLB instance from the drop-down list. Name: Enter a name for the SLB instance. The name must be 2 to 128 characters in length and can contain letters, digits, full-width characters, underscores (_), hyphens (-), periods (.), and colons (:). Line breaks and spaces are also supported. The name must start with a letter and cannot start with `http://` or `https://` . T ype: Select the instance type of the SLB instance. Possible options are Shared-Performance and Guaranteed-Performance. Shared-performance instances share resources with each other, which means their performance cannot be guaranteed. The performance of a guaranteedperformance SLB instance varies by type. Net work Access: Select the type of network traffic to balance. Possible options are Int ernal Net work and Public Net work. In this example, select Int ernal Net work Net work T ype: Select the network type of the SLB instance. Possible options are Classic Net workand VPC. In this example, select VPC. IP Version: Select an IP version. Service IP: Enter the service IP address of the SLB instance. Make sure that the service IP address is valid. Otherwise, the SLB instance cannot be created. If you do not specify the service IP address, the system automatically allocates an IP address to the SLB instance.
4. Click Submit .
What's next Configure a CLB instance

### 3.4 Configure an SLB instance

This topic describes how to configure an SLB instance. After you create an SLB instance, you must add at least one listener and a group of backend servers to this SLB instance so that it can forward traffic. The following example sets up a TCP listener and adds two ECS instances (ECS01 and ECS02) that host static web pages as backend servers to an SLB instance.
2. On the Server Load Balancers page, find the target SLB instance and click Conf igure List ener in
the Actions column.
3. In the Prot ocol and List ener step, complete the following information and use the default
values for other fields to configure the listening rule. Select List ener Prot ocol: Select a listener protocol. In this example, select T CP. List ening Port : Set a frontend port to receive and forward requests to backend servers. This port is configured for external load balancing. Generally, port 80 is used for HTTP and port 443 is used for HTTPS. In this example, set the port number to 80. Enable Peak Bandwidt h Limit : You can switch on this option and then set a bandwidth limit to control the bandwidth that is used by the applications running on backend servers to provide external services. Scheduling Algorit hm: Select a scheduling algorithm for distributing requests to backend servers. SLB supports the following scheduling algorithms. In this example, select Round-Robin (RR). Weight ed Round-Robin (WRR): Requests are distributed proportionally based on the assigned weights of backend servers. Backend servers with higher weights receive more requests. Weight ed Least Connect ions (WLC): Requests are distributed based on the combination of the weights and active connections of backend servers. If multiple backend servers have the same weight, requests are routed to the backend server with the lowest number of active connections. Round-Robin (RR): Requests are evenly and sequentially distributed to backend servers.
4. Click Next . In the Backend Servers step, select Def ault Server Group and click Add More to
add backend servers. i. In the Select Servers dialog box, select the previously created ECS01 and ECS02 instances and click Next . ii. Configure the weights of the ECS instances. The higher the weight, the more requests a backend server receives. The default weight is 100. We recommend that you use the default value. iii. Click Add. iv. In the Def ault Server Group section, specify backend server ports. A backend server uses this port to receive requests. You can specify the same port for multiple backend servers of an SLB instance. In this example, set the port number to 80.
5. Click Next to configure the health check. The default health check settings are used in this
example. After you enable the health check feature, when a backend server is detected unhealthy, SLB bypasses requests from this backend server to other healthy backend servers. SLB will only send requests to this backend server when it has been restored and is considered healthy.
6. Click Next . In the Submit step, check the configuration and click Submit .
7. Click OK to go back to the Server Load Balancers page, and click
to refresh the page. If the health check state of a backend ECS instance is Act ive, the backend server is working properly and is able to process requests.
8. In the web browser, enter the service IP address of the SLB instance in the address box to test
network load balancing.

### 3.5 Release an SLB instance

This topic describes how to release an SLB instance. You can release an SLB instance when you no longer need it to avoid accumulating unnecessary charges. Releasing an SLB instance will not affect the operation of the backend ECS instances.
2. Find and select the target SLB instance and click Release at the bottom of the list. You can also
choose
> Release in the Actions column.

3. In the Release dialog box, select Release Now.
The system performs release operations at 30-minute and hour marks. However, billing for the SLB instance is stopped at the specified release time.
4. Click Next .
5. Click OK.
Pay-as-you-go SLB instances cannot be restored once deleted. We recommend that you exercise caution when you release SLB instances.

## 4 SLB instances

### 4.1 SLB instance overview

A Server Load Balancer (SLB) instance is a virtual machine in which the SLB service runs. To use the SLB service, you must create an SLB instance first, and then add listeners and backend servers to the SLB instance. Instance network type Alibaba Cloud provides public-facing and internal load balancing services. If you create a public-facing SLB instance, a public IP address is allocated to it. If you create an internal SLB instance, a private IP address is allocated. Public-facing SLB instances A public-facing SLB instance distributes client requests over the Internet to backend servers according to configured forwarding rules. When you create a public-facing SLB instance, the system allocates a public IP address to the instance. You can resolve a domain name to the public IP address to provide public services. Internal SLB instances Internal SLB instances can only be used inside Alibaba Cloud and can only forward requests from clients that can access the internal network of SLB. For an internal SLB instance, you can select the network type: Classic network If you choose classic network for an internal SLB instance, the IP address of the SLB instance is allocated and maintained by Alibaba Cloud. The instance can only be accessed by classic-network ECS instances. VPC network If you choose VPC network for an internal SLB instance, the IP address of the SLB instance is allocated from the CIDR block of the VSwitch that the instance belongs to. An SLB instance of the VPC-type network can only be accessed by ECS instances in the same VPC.

### 4.2 Create an SLB instance

This topic describes how to create an SLB instance. To get started with SLB, you must create an SLB instance. You can add multiple listeners and backend servers to an SLB instance. Prerequisites You have created ECS instances and deployed applications on them. The ECS instances and the SLB instance belong to the same organization. In addition, the security group rules of the ECS instances permit traffic on HTTP port 80 and HTTPS port 443.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. On the Server Load Balancers page, click Creat e Inst ance.
Organizat ion: Select the organization to which the SLB instance belongs. Make sure that the organization of the SLB instance is the same as the organization of its backend servers. Resource Set : Select the resource set to which the SLB instance belongs. Region: Select a region for the SLB instance. Zone: Select a zone for the SLB instance from the drop-down list. Name: Enter a name for the SLB instance. The name must be 2 to 128 characters in length and can contain letters, digits, hyphens (-), colons (:), commas (,), periods (.), and underscores (_). It must start with a letter and cannot start with `http://` or `https://` . T ype: Select the instance type of the SLB instance. Possible options are Shared-Performance and Guaranteed-Performance. Shared-performance instances share resources with each other, which means their performance cannot be guaranteed. The performance of a guaranteedperformance SLB instance varies by type. Maximum concurrent connections: the maximum number of concurrent connections that an SLB instance can support. Connection requests that exceed this limit will be discarded. Connections per second (CPS): the number of new connections per second. Connection requests that exceed this limit will be discarded. QPS: the number of HTTP or HTTPS queries or requests that can be processed per second. This metric is specific to Layer-7 listeners. Connection requests that exceed this limit will be discarded. Net work Access: Select the type of network traffic to balance. Possible options are Internal Network and Public Network. If you select Public Network, you can choose an IP version between IPv6 and IPv4 for the SLB instance and specify a bandwidth for billing. Net work T ype: Select the network type of the SLB instance. Possible options are Classic Network and VPC. IP Version: Select an IP version. Internal SLB instances support only IPv4. Internet-facing SLB instances support IPv6 and IPv4. Service IP: Enter the service IP address of the SLB instance. Make sure that the service IP address is valid. Otherwise, the SLB instance cannot be created. If you do not specify the service IP address, the system automatically allocates an IP address to the SLB instance.
4. Click Submit .
What's next Configure a CLB instance

### 4.3 Start and stop an SLB instance

This topic describes how to start and stop an SLB instance. SLB instances can be started or stopped at any time. A stopped SLB instance does not receive or forward client traffic.
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

This topic describes how to use tags to query SLB instances.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Select a data from the Select a t ag drip-down list to filter instances.
To clear the search condition, move the pointer over the selected tag and click the displayed deletion icon next to it.

#### 4.4.4 Remove tags

This topic describes how to remove tags from an SLB instance. You can only remove tags for one SLB instance at a time.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. In the Act ions column, choose
> Edit T ags.

4. In the Edit T ags dialog box, click the deletion icon next to the tags to be removed, and then click
OK. If a tag is removed from an SLB instance and is not added to any other instances, the tag is deleted from the system.

### 4.5 Release an SLB instance

This topic describes how to release an SLB instance. You can release SLB instances immediately.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Find the target SLB instance and choose
> Release.

4. In the Release dialog box, select Release Now.
5. Click Next .
6. Confirm the displayed information and click OK to release the instance.

## 5 Listeners

### 5.1 Listener overview

This topic provides an overview of listeners. After you create an SLB instance, you must configure one or more listeners for it. A listener checks for connection requests and then distributes the requests to backend servers based on the forwarding rules that are defined by a specified scheduling algorithm. SLB provides listeners for Layer-4 (TCP and UDP) and Layer-7 (HTTP and HTTPS) load balancing. The following table lists the features and use cases of these listeners.

| Protocol | Feature | Use case |
|---|---|---|
| TCP | A connection-oriented protocol that requires a logical connection to be established before any data can be transmitted Source IP address-based session persistence Source IP addresses readable at the network layer Fast data transmission | Services that prioritize high reliability and data accuracy over high-speed data transmission, such as file transmission, email sending or receiving, and remote logon Basic web applications For more information, see Add a TCP listener. |
| UDP | A connectionless protocol that transmits data packets without implementing the three-way handshake and does not provide error recovery or data retransmission Fast data transmission with relatively low reliability | Services that focus on real-time content delivery other than reliability, such as video chats and real-time quotes For more information, see Add a UDP listener. |
| HTTP | An application-layer protocol used to package data Cookie-based session persistence Support for using the X-Forwarded- For (XFF) header to identify original client IP addresses | Applications that need to identify data content, such as web applications and small-sized mobile games For more information, see Add an HTTP listener. |
| HTTPS | Encrypted data transmission that prevents unauthorized access Centralized certificate management that allows certificate uploading and decryption on SLB | Applications that require encrypted transmission For more information, see Add an HTTPS listener. |

### 5.2 Add a TCP listener

This topic describes how to add a TCP listener to an SLB instance. TCP provides reliable and accurate data delivery at relatively low connection speeds and therefore is applicable to services such as file transmission, email sending or receiving, and remote logon. You can add a TCP listener to forward TCP requests. Step 1: Configure the TCP listener Perform the following operations to configure the TCP listener.
1. Log on to the SLB console.
2. In the left-side navigation pane, choose Inst ances > Server Load Balancers.
3. Use one of the following methods to start the listener configuration wizard:
On the Server Load Balancers page, find the target SLB instance and then click Conf igure List ener in the Actions column. On the Server Load Balancers page, click the ID of the target SLB instance. On the List ener tab, click Add List ener.
4. Specify the following information:

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select the protocol of the listener. In this example, select T CP. |
| List ening Port | Set the listening port used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced Set t ings |   |
| Scheduling Algorit hm | SLB supports three scheduling algorithms: round robin (RR), weighted round robin (WRR), and weighted least connections (WLC). Weight ed Round-Robin (WRR): Backend servers with higher weights receive more requests. Round-Robin (RR): Requests are evenly and sequentially distributed to backend servers. Weight ed Least Connect ions (WLC): Requests are distributed based on the combination of the weights and active connections of backend servers. Requests are distributed to the backend server with the least number of active connections. If two backend servers have the same number of active connections, the backend server with a higher weight receives more requests. |

| Parameter | Description |
|---|---|
| Enable Session Persist ence | Specify whether to enable session persistence. Unit: seconds. Valid values: 1 to 3600. After session persistence is enabled, the listener forwards all requests from the same client to a specific backend server for the duration of a session. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
| Enable Peak Bandwidt h Limit | You can switch on this option and then set a bandwidth limit for the listener. If an SLB instance incurs fees based on the bandwidth, you can set different peak bandwidth values for different listeners to limit the amount of traffic that flows in each listener. The sum of the peak bandwidth values of all listeners added to an SLB instance cannot exceed the bandwidth of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |
| Idle T imeout | Specify the idle timeout period of TCP connections. Unit: seconds. Valid values: 10 to 900. |
| Obt ain Client Source IP Address | For Layer-4 listeners, backend servers can directly obtain the actual IP addresses of clients. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to start the listener after the listener is configured. By default, the listener is started after configuration. |

5. Click Next .
Step 3: Add backend servers After you configure the listener, you must add backend servers to process client requests. You can add backend servers to the default server group, or create VServer groups or primary/secondary server groups and then add servers to them. For more information, see Backend server overview. This example adds backend servers to the default server group.
1. Select Def ault Server Group and click Add More.
2. Select ECS instances (backend servers) that you want to add, and then click Next .
3. Configure weights for the added backend servers.
A backend server with a higher weight receives more requests. If the weight of a backend server is set to 0, the backend server does not receive new requests.
4. Click Add. On the Def ault Server Group tab, configure ports for the backend servers.
Set a port for each backend server to receive requests. Valid values: 1 to 65535. You can specify the same port for multiple backend servers of an SLB instance.
5. Click Next .
Step 4: Configure the health check SLB checks the availability of backend servers by performing the health check. The health check feature improves the availability of frontend services by minimizing downtime caused by health issues of backend servers. Click Modif y to configure advanced health check settings. For more information, see Health check overview. Click Next . Step 5: Confirm the settings Complete the following steps to confirm and apply the listener settings:
1. In the Submit step, check the configuration. You can click Modif y to modify configuration
settings.
2. Click Submit .
3. In the Conf igure Successf ul dialog box, click OK.
You can check the created listener on the Listener tab.

### 5.3 Add a UDP listener

This topic describes how to add a UDP listener to an SLB instance. UDP is applicable to services that prioritize real-time content delivery over reliability, such as video chats and real-time quotes. You can add a UDP listener to forward UDP requests. Context Before you configure a UDP listener, note the following limits: Ports 250, 4789, and 4790 of a UDP listener are reserved and therefore are unavailable for your configuration. Fragmented packets are not supported. The UDP listeners of an SLB instance in a classic network do not support the viewing of source IP addresses. The following operations take five minutes to take effect if they are performed for a UDP listener: Remove backend servers Set the weight of a backend server to 0 after it is detected unhealthy Step 1: Configure a TCP listener
1. Log on to the SLB console.
2. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the CLB instance that you want to manage and click Conf igure List ener in the Act ions column. On the Inst ances page, find the CLB instance that you want to manage and click the ID of the instance. On the instance details page, click the List ener tab and then click Add List ener.
3. On the Prot ocol and List ener wizard page, set the following parameters and click Next .

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select T CP. |
| List ening Port | Specify the listening port that is used to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| List ener Name | Enter a name for the listener. |
| Advanced | You can click Modif y to configure the advanced settings. |
| Scheduling Algorit hm | Select a scheduling algorithm. Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are sequentially distributed to backend servers. Consist ent Hash (CH): T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. Not e Only high-performance CLB instances support the CH algorithm. |
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, CLB forwards all requests from a client to the same backend server. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
| Enable Peak Bandwidt h Limit | Specify whether to set the maximum bandwidth of the listener. If the CLB instance is billed based on bandwidth usage, you can set different maximum bandwidth values for different listeners. This limits the amount of traffic that can be forwarded by each listener. The sum of the maximum bandwidth of all listeners that are added to a CLB instance cannot exceed the maximum bandwidth of the CLB instance. By default, this feature is disabled and all listeners share the bandwidth of the CLB instance. |

| Parameter | Description |
|---|---|
| Connect ion T imeout | Specify the timeout period of idle TCP connections. Unit: seconds. Valid values: 10 to 900. |
| Proxy Prot ocol | Use the proxy protocol to pass client IP addresses to backend servers. Not e You cannot enable this feature in scenarios where PrivateLink is used. |
| Obt ain Client Source IP Address | Specify whether to retrieve the real IP addresses of clients. Only Layer 4 listeners support this feature. By default, this feature is enabled. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. |

Step 2: Configure the UDP listener To configure the UDP listener, perform the following operations:
1. In the Prot ocol and List ener step, specify the following information:

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select the protocol of the listener. In this example, select UDP. |
| List ening Port | Set the listening port used to receive requests and forward them to backend servers. Valid values: 1 to 65535. |
| Advanced Set t ings |   |
| Scheduling Algorit hm | SLB supports three scheduling algorithms: RR, WRR, and WLC. Weight ed Round-Robin (WRR): Backend servers with higher weights receive more requests. Round-Robin (RR): Requests are evenly and sequentially distributed to backend servers. Weight ed Least Connect ions (WLC): Requests are distributed based on the combination of the weights and active connections of backend servers. Requests are distributed to the backend server with the least number of active connections. If two backend servers have the same number of active connections, the backend server with a higher weight receives more requests. |

| Parameter | Description |
|---|---|
| Enable Peak Bandwidth Limit | You can switch on this option and then set a bandwidth limit for the listener. If an SLB instance incurs fees based on the bandwidth, you can set different peak bandwidth values for different listeners to limit the amount of traffic that flows in each listener. The sum of the peak bandwidth values of all listeners added to an SLB instance cannot exceed the bandwidth of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |
| Obt ain Client Source IP Address | Backend servers of a UDP listener can directly obtain the actual IP addresses of clients. Not e UDP listeners of an SLB instance in a classic network do not support the viewing of source IP addresses. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to start the listener after the listener is configured. By default, the listener is started after configuration. |

2. Click Next .
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

This topic describes how to add an HTTP listener to an SLB instance. HTTP is applicable to the applications that need to identify data content, such as web applications and small-sized mobile games. You can add an HTTP listener to forward HTTP requests. Step 1: Configure a TCP listener
1. Log on to the SLB console.
2. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the CLB instance that you want to manage and click Conf igure List ener in the Act ions column. On the Inst ances page, find the CLB instance that you want to manage and click the ID of the instance. On the instance details page, click the List ener tab and then click Add List ener.
3. On the Prot ocol and List ener wizard page, set the following parameters and click Next .

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select T CP. |
| List ening Port | Specify the listening port that is used to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| List ener Name | Enter a name for the listener. |
| Advanced | You can click Modif y to configure the advanced settings. |
| Scheduling Algorit hm | Select a scheduling algorithm. Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are sequentially distributed to backend servers. Consist ent Hash (CH): T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. Not e Only high-performance CLB instances support the CH algorithm. |

| Parameter | Description |
|---|---|
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, CLB forwards all requests from a client to the same backend server. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
| Enable Peak Bandwidt h Limit | Specify whether to set the maximum bandwidth of the listener. If the CLB instance is billed based on bandwidth usage, you can set different maximum bandwidth values for different listeners. This limits the amount of traffic that can be forwarded by each listener. The sum of the maximum bandwidth of all listeners that are added to a CLB instance cannot exceed the maximum bandwidth of the CLB instance. By default, this feature is disabled and all listeners share the bandwidth of the CLB instance. |
| Connect ion T imeout | Specify the timeout period of idle TCP connections. Unit: seconds. Valid values: 10 to 900. |
| Proxy Prot ocol | Use the proxy protocol to pass client IP addresses to backend servers. Not e You cannot enable this feature in scenarios where PrivateLink is used. |
| Obt ain Client Source IP Address | Specify whether to retrieve the real IP addresses of clients. Only Layer 4 listeners support this feature. By default, this feature is enabled. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. |

Step 2: Configure the HTTP listener Perform the following operations to configure the HTTP listener.
1. In the Prot ocol and List ener step, specify the following information:

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select the protocol of the listener. In this example, select HT T P. |

| Parameter | Description |
|---|---|
| List ening Port | Set the listening port used to receive requests and forward them to backend servers. Valid values: 1 to 65535. Not e The HTTP listening ports must be unique in an SLB instance. |
| Advanced Set t ings |   |
| Scheduling Algorit hm | SLB supports three scheduling algorithms: RR, WRR, and WLC. Weight ed Round-Robin (WRR): Backend servers with higher weights receive more requests. Round-Robin (RR): Requests are evenly and sequentially distributed to backend servers. Weight ed Least Connect ions (WLC): Requests are distributed based on the combination of the weights and active connections of backend servers. Requests are distributed to the backend server with the least number of active connections. If two backend servers have the same number of active connections, the backend server with a higher weight receives more requests. |
| Redirect ion | Specify whether to redirect traffic from the HTTP listener to an HTTPS listener. Not e Before you enable redirection, make sure that you have created an HTTPS listener. |

| Parameter | Description |
|---|---|
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, the listener forwards all requests from the same client to a specific backend server for the duration of a session. HTTP implements cookie-based session persistence. You can choose from the following approaches to configure session persistence with cookies: Insert cookie: You only need to specify the cookie timeout period. SLB inserts a cookie (SERVERID) to the first HTTP or HTTPS response packet sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. Rewrit e cookie: You can specify the cookie to be inserted into the HTTP or HTTPS response. You must specify the timeout period and lifecycle of this cookie on the backend server. SLB rewrites the original cookie when the new cookie is detected. The next request that contains the new cookie will be distributed to the recorded backend server. |
| Enable Peak Bandwidt h Limit | You can switch on this option and then set a bandwidth limit for the listener. If an SLB instance incurs fees based on the bandwidth, you can set different peak bandwidth values for different listeners to limit the amount of traffic that flows in each listener. The sum of the peak bandwidth values of all listeners added to an SLB instance cannot exceed the bandwidth of this SLB instance. By default, this feature is disabled and all listeners share the bandwidth of the SLB instance. |
| Idle T imeout | Specify the idle timeout period of connections. Unit: seconds. Valid values: 1 to 60. If no request is received during the idle timeout period, SLB closes the connection and will restart the connection when the next request is received. This feature is available in all regions. Not e This feature is unavailable for HTTP/2 requests. |

| Parameter | Description |
|---|---|
| Request T imeout | Specify the request timeout period. Unit: seconds. Valid values: 1 to 180. If no response is received from the backend server during the request timeout period, SLB sends an HTTP 504 error code to the client. This feature is available in all regions. |
| Enable Gzip Compression | Specify whether to enable compression for a specific file type. Gzip supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. |
| Add HT T P Header Fields | Select one or more custom HTTP header fields that you want to add: Use the X-Forwarded-For header field to retrieve the IP addresses of clients. Use the X-Forwarded-Proto header field to retrieve the listener protocol used by the SLB instance. Use the SLB-IP header field to retrieve the public IP address of the SLB instance. Use the SLB-ID header field to retrieve the ID of the SLB instance. |
| Obt ain Client Source IP Address | HTTP listeners use the X-Forwarded-For header field to identify the originating IP addresses of clients. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to start the listener after the listener is configured. By default, the listener is started after configuration. |

2. Click Next .
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

HTTPS is applicable to applications that require encrypted data transmission. You can add an HTTPS listener to forward HTTPS requests. Step 1: Configure a TCP listener
1. Log on to the SLB console.
2. Use one of the following methods to open the listener configuration wizard:
On the Inst ances page, find the CLB instance that you want to manage and click Conf igure List ener in the Act ions column. On the Inst ances page, find the CLB instance that you want to manage and click the ID of the instance. On the instance details page, click the List ener tab and then click Add List ener.
3. On the Prot ocol and List ener wizard page, set the following parameters and click Next .

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select T CP. |
| List ening Port | Specify the listening port that is used to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| List ener Name | Enter a name for the listener. |
| Advanced | You can click Modif y to configure the advanced settings. |
| Scheduling Algorit hm | Select a scheduling algorithm. Weight ed Round-Robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round-Robin (RR): Requests are sequentially distributed to backend servers. Consist ent Hash (CH): T uple: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. Not e Only high-performance CLB instances support the CH algorithm. |

| Parameter | Description |
|---|---|
| Enable Session Persist ence | Specify whether to enable session persistence. After session persistence is enabled, CLB forwards all requests from a client to the same backend server. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
| Enable Peak Bandwidt h Limit | Specify whether to set the maximum bandwidth of the listener. If the CLB instance is billed based on bandwidth usage, you can set different maximum bandwidth values for different listeners. This limits the amount of traffic that can be forwarded by each listener. The sum of the maximum bandwidth of all listeners that are added to a CLB instance cannot exceed the maximum bandwidth of the CLB instance. By default, this feature is disabled and all listeners share the bandwidth of the CLB instance. |
| Connect ion T imeout | Specify the timeout period of idle TCP connections. Unit: seconds. Valid values: 10 to 900. |
| Proxy Prot ocol | Use the proxy protocol to pass client IP addresses to backend servers. Not e You cannot enable this feature in scenarios where PrivateLink is used. |
| Obt ain Client Source IP Address | Specify whether to retrieve the real IP addresses of clients. Only Layer 4 listeners support this feature. By default, this feature is enabled. |
| Aut omat ically Enable List ener Af t er Creat ion | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. |

Step 2 Configure an HTTPS listener To configure an HTTPS listener, perform the following operations:
1. In the Prot ocol and List ener step, configure the listener parameters listed in the following table.

| Parameter | Description |
|---|---|
| Select List ener Prot ocol | Select the protocol type of the listener. In this example, select HT T PS. |

| Parameter | Description |
|---|---|
| List ening Port | The listening port used to receive requests and forward the requests to backend servers. Valid values: 1 to 65535. Not e The listening port numbers must be unique in an SLB instance. |
| Advanced |   |
| Scheduling Algorit hm | SLB supports three scheduling algorithms: round robin, weighted round robin (WRR), and weighted least connections (WLC). Weight ed Round-Robin (WRR): A backend server with a higher weight is more likely to be scheduled and receives more requests. Round-Robin (RR): Requests are evenly and sequentially distributed to backend servers. Weight ed Least Connect ions (WLC): Requests are distributed to the backend server with the least number of connections. If two backend servers have the same number of connections, the backend server with a higher weight will receive more requests. |
| Enable Session Persist ence | Specifies whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from the same client to the same backend server. HTTP session persistence is implemented through cookies. SLB provides two methods to handle cookies: Insert cookie: You only need to specify the cookie timeout period. SLB inserts a cookie (SERVERID) to the first HTTP or HTTPS response packet sent to a client. The next request from the client will contain the cookie, and the listener will distribute the request to the recorded backend server. Rewrit e cookie: You can specify the cookie to be inserted into the HTTP or HTTPS response to meet your specific needs. You must maintain the timeout period and lifecycle of the cookie on the backend server. SLB will overwrite the original cookie if it discovers that a new cookie has been specified. The next request will contain the new cookie, and the listener will distribute the request to the recorded backend server. |

| Parameter | Description |
|---|---|
| Enable Peak Bandwidt h Limit | Specifies whether to configure the bandwidth limit for the listener. If an SLB instance is billed based on bandwidth, you can set different peak bandwidth values for different listeners to limit the amount of traffic passing through each listener. The sum of the peak bandwidth values of all listeners for an SLB instance cannot exceed the bandwidth value of that SLB instance. By default, this feature is disabled, and all listeners share the bandwidth of the SLB instance. |
| Enable Gzip Compression | Specifies whether to enable compression for a specific file type. Gzip supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. |
| Add HT T P Header Fields | Select the custom HTTP header fields that you want to add: Use the X-Forwarded-For header field to retrieve the IP addresses of clients. Use the X-Forwarded-Proto header field to retrieve the listener protocol used by the SLB instance. Use the SLB-IP header field to retrieve the public IP address of the SLB instance. Use the SLB-ID header field to retrieve the ID of the SLB instance. |
| Obt ain Client Source IP Address | HTTP listeners use the X-Forwarded-For header field to obtain the actual IP addresses of clients. |
| Aut omat ically Enable List ener Af t er Creat ion | Specifies whether to start the listener after the listener is configured. By default, the listener is started after configuration. |

2. Click Next .
Step 3 Configure an SSL certificate To add an HTTPS listener, you must upload a server certificate or CA certificate. Not ice SLB supports the following public key algorithms: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521

| Certificate | Description | Required for one-way authentication | Required for mutual authentication |
|---|---|---|---|
| Server certificate | The certificate used to identify the server. The client checks whether the certificate sent by the server is issued by a trusted center. | Yes. You must upload the server certificate to the certificate management system of SLB. | Yes. You must upload the server certificate to the certificate management system of SLB. |
| Client certificate | The certificate that is used to identify the client. The server identifies the client by checking the certificate sent by the client. You can sign a client certificate with a self-signed CA certificate. | No. | Yes. You must install the client certificate on the client. |
| CA certificate | The server uses a CA certificate to verify the signature on the client certificate. If the certificate cannot be verified, the connection request is rejected. | No. | Yes. You must upload the CA certificate to the certificate management system of SLB. |

Before you upload a certificate, take note of the following items: The uploaded certificate must be in the PEM format. After you upload the certificate to SLB, SLB can manage the certificate and you do not need to bind the certificate to backend servers. It may take some time to activate an HTTPS listener because the certificate must be uploaded, loaded, and verified. It can take up to three minutes for an HTTPS listener to be activated. The ECDHE cipher suites used by HTTPS listeners support forward secrecy but do not support the security enhancement parameters required by DHE cipher suites. As a result, strings that contain the `BEGIN DH PARAMETERS` field in a PEM certificate file cannot be uploaded. For more information, see Certificate requirements. HTTPS listeners do not support Server Name Indication (SNI). You can use TCP listeners instead, and then configure SNI on backend servers. The session ticket timeout period of HTTPS listeners is 300 seconds. The actual amount of traffic generated on an HTTPS listener is larger than the billed traffic amount because some traffic is used for handshaking. If a large number of new connections are established, a large amount of traffic will be generated.
1. Select an uploaded server certificate, or click Creat e Server Cert if icat e to upload a server
certificate. For more information, see Overview.
2. To enable HTTPS mutual authentication, click Modif y next to Advanced.
3. Turn on Enable Mut ual Aut hent icat ion, and select an uploaded CA certificate or click Creat e
CA Cert if icat e to upload a CA certificate. You can use a self-signed CA certificate. For more information, see Overview. Step 4 Add backend servers After configuring the listener, you must add backend servers to process client requests. You can use the default server group configured for the SLB instance, or configure a VServer group or a primary/secondary server group. For more information, see Backend server overview. This example uses the default server group. Step 5 Configure health checks CLB checks the availability of backend ECS instances by performing health checks. The health check feature improves service availability and prevents service interruptions caused by single points of failure. Step 6 Submit the configurations Submit the configurations by performing the following operations:
1. On the Conf irm Conf igurat ions wizard page, confirm the configurations. You can click Modif y to
modify the configurations.
2. After you confirm the configurations, click Submit .
3. After the configurations are submitted, click OK.
After you configure the listener, you can view the listener on the Listener tab.

### 5.6 Enable access control

This topic describes how to enable access control for a listener. SLB provides listener-based access control. You can configure different whitelists for different listeners.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. On the page that appears, click the List ener tab.
4. Find the target listener and choose
> Set Access Cont rol in the Actions column.

5. In the Access Cont rol Set t ings dialog box, enable access control and configure the whitelist,
and then click OK. Whit elist : Only the requests from the IP addresses or CIDR blocks in the specified ACL are forwarded. You can use the whitelist feature when you want to allow access from specified IP addresses. Using the whitelist feature may pose risks to your services. The whitelist allows only the traffic from the IP addresses in the specified ACL to access the SLB listener. If the whitelist is used while the corresponding ACL does not contain any IP addresses, the SLB listener forwards all access requests. Separate multiple IP addresses with commas (,). Each IP address must be unique. You can add a maximum of 300 IP addresses. Supported formats: IP addresses (for example, 10.23.12.24) and CIDR blocks (for example, 10.23.12.0/24) 0.0.0.0 and x.x.x.x/0 are not supported. The access control feature works only for new connection requests and does not affect existing connections.

### 5.7 Disable access control

This topic describes how to disable access control for a listener.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. On the page that appears, click the List ener tab.
4. Find the target listener, and choose
> Set Access Cont rol in the Actions column.

5. In the Access Cont rol Set t ings dialog box, disable access control and then click OK.

## 6 Backend servers

### 6.1 Backend server overview

Before the Server Load Balancer (SLB) service can be used, you must add ECS instances as backend servers to an SLB instance to process client requests. Backend server introduction You can set virtual IP addresses for SLB instances. This way, the added ECS instances in the same region can be virtualized into an application service pool that provides high performance and availability. You can manage backend servers by using VServer groups. Each listener of an SLB instance can be associated with a specific VServer group so that different listeners can forward requests to their associated backend servers that use different ports. If you associate a VServer group with a listener, the listener will distribute requests to backend servers in the associated VServer group instead of those in the default server group. Restriction description You can increase or decrease the number of backend ECS instances at any time and switch ECS instances to receive client requests. However, we recommend that you enable the health check feature and make sure that at least one ECS instance is running properly to maintain service stability. When you add ECS instances to an SLB instance, take note of the following items: You can use different operating systems for the backend ECS instances of an SLB instance. However, the applications deployed in the ECS instances must be the same and have consistent data. We recommend that you use the same operating system to facilitate management and maintenance. Up to 50 listeners can be added to a single SLB instance. Each listener corresponds to an application deployed on backend ECS instances. Listening ports of an SLB instance correspond to application service ports opened on backend ECS instances. You can specify a weight for each ECS instance in the application service pool. An ECS instance with a higher weight receives more requests. If session persistence is enabled, requests may not be evenly distributed to backend ECS instances. To solve this problem, we recommend that you disable session persistence and check whether the problem persists. If requests are not distributed evenly, troubleshoot as follows: i. Collect statistics on the access logs of the web service on backend ECS instances for a period of time. ii. Check whether the numbers of access logs of backend ECS instances match SLB configurations. For example, if session persistence is enabled, you must differentiate the access logs for the same IP address. If different weights are configured for backend ECS instances, you must check whether the percentage of access logs is normal based on the percentage of weights. When an ECS instance is undergoing hot migration, persistent connections to SLB may be interrupted. You can solve this problem by reestablishing the connections. Default server groups A default server group contains ECS instances that are used to receive client requests. If a listener is not associated with a VServer group or a primary/secondary server group, the listener will forward requests to ECS instances in the default server group. For more information about how to create a default server group, see Add an ECS instance to the default server group. Primary/secondary server groups A primary/secondary server group only contains two ECS instances. One ECS instance acts as the primary server and the other acts as the secondary server. Health checks are not performed on the secondary server. If the primary server is declared unhealthy, traffic is redirected to the secondary server. If the primary server is declared healthy, services will be restored and traffic will be forwarded to the primary server again. For more information about how to create a primary/secondary server group, see Create and manage a primary/secondary server group. Only TCP and UDP listeners support configuring primary/secondary server groups. VServer groups If you want to distribute different requests to different backend servers or configure domain name- or URL-based forwarding rules, you can use VServer groups. For more information about how to create a VServer group, see Create and manage a vServer group.

### 6.2 Default server groups

#### 6.2.1 Add ECS instances to the default server group

group This topic describes how to add ECS instances as default backend servers to the default server group of an SLB instance. Before you use the SLB service, you must add at least one default backend server to receive client requests forwarded by SLB. Prerequisites Before you add ECS instances to the default server group, make sure that the following conditions are met: An SLB instance is created. For more information, see Create an SLB instance. You have created ECS instances and deployed applications on these ECS instances to process requests.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Def ault Server Group tab.
4. Click Add.
5. In the My Servers dialog box, select ECS instances that you want to add.
6. Click Next .
7. In the Conf igure Port s and Weight s dialog box, specify the weight of each added ECS instance.
An ECS instance with a higher weight receives more requests. You can change the weight of a server and then move the pointer over to change the weights of multiple servers: Click Replicat e t o Below: The weights of all servers below the current server are set to the weight of the current server. Click Replicat e t o Above: The weights of all servers above the current server are set to the weight of the current server. Click Replicat e t o All: The weights of all servers in the default server group are set to the weight of the current server. Click Reset : The weight fields of all servers in the default server group are cleared. Not ice If the weight of a backend server is set to 0, this backend server no longer receives new requests.
8. Click Add.
9. Click OK.

#### 6.2.2 Add IDC servers to the default server group

This topic describes how to add servers in on-premises Internet Data Centers (IDCs) as default backend servers to the default server group of an SLB instance. Before you use the SLB service, you must add at least one default backend server to receive client requests forwarded by SLB. Prerequisites Applications are deployed on the IDC servers, and the IDC servers are ready to receive distributed requests.
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

This topic describes how to remove a backend server that is no longer needed.
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

This topic describes how to create a VServer group and then add IDC servers to the VServer group. You can add ECS instances and IDC servers as backend servers to a VServer group. If you associate a VServer group with a listener, the listener distributes requests only to the backend servers in the VServer group instead of other backend servers. Prerequisites Before you create a VServer group, make sure that applications are deployed on the IDC servers and the IDC servers are ready to receive distributed requests. Context Note the following items before you create a VServer group: An IDC server can be added to multiple VServer groups. A VServer group can be associated with multiple listeners of an SLB instance. The settings of the VServer group include the settings of IDC servers and application ports.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. On the VServer Groups tab, click Creat e VServer Group.
5. On the Creat e VServer Group page, configure the VServer group.
i. In the VServer Group Name field, enter a name for the VServer group. ii. Click Add IDC Server. iii. In the My Servers dialog box, click Add. iv. Select a VPC from the VPC Connected to IDC drop-down list, enter a name for the IDC server, and specify the IP address of the IDC server. The IP address of the IDC server must be accessible to the VPC. v. Click Next . vi. Specify a port and weight for each IDC server, and then click Add. Set the ports and weights based on the following information: Port : The backend port opened on an IDC server to receive requests. Multiple ports can be added to an IDC server. You can set the same port number for multiple backend servers of the same SLB instance. Weight : An IDC server with a higher weight receives more requests. Not ice If the weight of an IDC server is set to 0, the IDC server no longer receives new requests. You can change the weight of a server and then move the pointer over to change the weights of multiple servers: Click Replicat e t o Below: The weights of all servers below the current server are set to the weight of the current server. Click Replicat e t o Above: The weights of all servers above the current server are set to the weight of the current server. Click Replicat e t o All: The weights of all servers in the VServer group are set to the weight of the current server. Click Reset : The weight fields of all servers in the VServer group are cleared. Not ice If the weight of a backend server is set to 0, this backend server no longer receives new requests. vii. Click Add.
6. Click Creat e.

#### 6.3.3 Modify a VServer group

This topic describes how to modify the settings of ECS instances or IDC servers in a VServer group.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. Find the target VServer group and then click Edit in the Actions column.
5. Modify the ports and weights of ECS instances or IDC servers, and then click Save.

#### 6.3.4 Delete a VServer group

This topic describes how to delete a VServer group that is no longer needed for traffic distribution.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the VServer Groups tab.
4. Find the target VServer group, and then click Delet e in the Actions column.
5. In the dialog box that appears, click OK.

### 6.4 Active/standby server groups

#### 6.4.1 Add ECS instances to a primary/secondary server group

server group This topic describes how to create a primary/secondary server group and then add ECS instances to the primary/secondary server group. You can use a primary/secondary server group to implement failover between a primary server and a secondary server. By default, the primary server handles all distributed requests. When the primary server fails, traffic is redirected to the secondary server. Prerequisites Before you create a primary/secondary server group, make sure that the following conditions are met: An SLB instance is created. For more information, see Create an SLB instance. You have created ECS instances and deployed applications on these ECS instances to process requests.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. On the Primary/Secondary Server Groups tab, click Creat e Primary/Secondary Server Group.
5. On the Creat e Primary/Secondary Server Group page, configure the primary/secondary server
group. i. In the Primary/Secondary Server Group Name field, enter a name for the primary/secondary server group. ii. Click Add. In the My Servers dialog box, select ECS instances that you want to add in the Select Servers step. You can add up to two ECS instances to a primary/secondary server group. iii. Click Next . iv. Configure the backend ports opened on ECS instances to receive requests, and then click Add. You can set multiple ports for an ECS instance. v. Set an ECS instance as the primary server. vi. Click Creat e.

#### 6.4.2 Add IDC servers to a primary/secondary server group

server group This topic describes how to create a primary/secondary server group and then add IDC servers to the primary/secondary server group. You can use a primary/secondary server group to implement failover between a primary server and a secondary server. By default, the primary server handles all distributed requests. When the primary server fails, traffic is redirected to the secondary server. Prerequisites The IDC servers are created, configured to deploy applications, and ready to receive distributed requests.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. On the Primary/Secondary Server Groups tab, click Creat e Primary/Secondary Server Group.
5. On the Creat e Primary/Secondary Server Group page, configure the primary/secondary server
group. i. In the Primary/Secondary Server Group Name field, enter a name for the primary/secondary server group, and then click Add IDC Server. ii. In the My Servers dialog box, click Add. iii. Select a VPC from the VPC Connected to IDC drop-down list, enter a name for the IDC server, and specify the IP address of the IDC server. The IP address of the IDC server must be accessible to the VPC. iv. Click Next . v. Configure the backend ports opened on ECS instances to receive requests, and then click Add. You can set multiple ports for an IDC server. vi. Set a backend server as the primary server. vii. Click Creat e.

#### 6.4.3 Delete a primary/secondary server group

If a primary/secondary server group is no longer needed to forward traffic, you can delete the primary/secondary server group.
1. Log on to the SLB console.
2. Find the target SLB instance and click its instance ID.
3. Click the Primary/Secondary Server Groups tab.
4. Find the target primary/secondary server group and click Delet e in the Actions column.
5. In the dialog box that appears, click OK.

## 7 Health check

### 7.1 Health check overview

Server Load Balancer (SLB) checks the availability of backend servers (ECS instances) by performing health checks. The health check feature improves the overall availability of your frontend business and mitigates the impact of exceptions occurring on backend ECS instances. After the health check feature has been enabled, SLB stops distributing requests to ECS instances that are declared unhealthy and distributes new requests to healthy ECS instances. When the unhealthy ECS instances have recovered, SLB begins forwarding requests to the ECS instances again. If your business is highly sensitive to traffic loads, frequent health checks may impact the availability of normal business. To reduce the impacts of health checks on your business, you can reduce the health check frequency, increase the health check interval, or change Layer 7 health checks to Layer 4 health checks to match business conditions. We recommend that you do not disable the health check feature to ensure business continuity. Health check process SLB is deployed in clusters. Node servers in the LVS or Tengine cluster forward data and perform health checks. The node servers in the LVS cluster forward data and perform health checks independently and in parallel based on configured load balancing policies. If an LVS node server detects that a backend ECS instance is unhealthy, the node server no longer sends new client requests to the ECS instance. SLB uses the CIDR block of 100.64.0.0/10 for health checks. Make sure that backend ECS instances do not block this CIDR block. You do not need to configure a security group rule to allow access from this CIDR block. However, if you have configured security rules such as iptables, you must allow access from this CIDR block. 100.64.0.0/10 is reserved by Alibaba Cloud. Other users cannot use IP addresses within this CIDR block, and therefore there are no security risks associated with it. Health checks of HTTP or HTTPS listeners For Layer 7 (HTTP or HTTPS) listeners, SLB checks the status of backend ECS instances by sending HTTP HEAD requests. For HTTPS listeners, certificates are managed in SLB. To improve system performance, HTTPS is not used for data exchange (including health check data and business interaction data) between SLB and backend ECS instances. The health check process of a Layer 7 listener is as follows:
1. A Tengine node server sends an HTTP HEAD request containing the configured domain name to the
internal IP address, health check port, and health check path of a backend ECS instance based on health check settings.
2. After receiving the request, the backend ECS instance returns an HTTP status code based on the
running status.
3. If the Tengine node server does not receive a response from the backend ECS instance within the
specified response timeout period, the node server determines that the service is unresponsive and the health check fails.
4. If the Tengine node server receives a response from the backend ECS instance within the specified
response timeout period, the node server compares the response information with the configured status code. If the status code in the response is the same as the configured one, the backend ECS instance is declared healthy. Otherwise, the backend ECS instance is declared unhealthy. Health checks of TCP listeners For TCP listeners, SLB checks the status of backend ECS instances by establishing TCP connections to improve health check efficiency. The health check process of a TCP listener is as follows:
1. An LVS node server sends a TCP SYN packet to the internal IP address and health check port of a
backend ECS instance.
2. After receiving the request, the backend ECS instance returns an SYN+ACK packet if listening on the
corresponding port is normal.
3. If the LVS node server does not receive a packet from the backend ECS instance within the
specified response timeout period, the node server determines that the service is unresponsive and the health check fails. Then, the node server sends an RST packet to the backend ECS instance to terminate the TCP connection.
4. If the LVS node server receives a packet from the backend ECS instance within the specified
response timeout period, the node server determines that the service runs properly and the health check succeeds. Then, the node server sends an RST packet to the backend ECS instance to terminate the TCP connection. Typically, a TCP three-way handshake is conducted to establish a TCP connection. After the LVS node server receives the SYN+ACK packet from the backend ECS instance, the node server sends an ACK packet, and then immediately sends an RST packet to terminate the TCP connection. This process may cause the ECS instance to regard that an error such as an abnormal exit occurred in the TCP connection, and then report a corresponding error such as `Connection reset by peer` , for example, in Java connection pool logs. Solution: You can implement HTTP health checks. If you have enabled the feature of obtaining actual client IP addresses on backend ECS instances, you can ignore connection errors caused by the access of the SLB CIDR block. Health checks of UDP listeners For UDP listeners, SLB checks the status of backend ECS instances by sending UDP packets. The health check process of a UDP listener is as follows:
1. An LVS node server sends a UDP packet to the internal IP address and health check port of an ECS
instance based on health check configurations.
2. If the listening on the corresponding port of the ECS instance is abnormal, the ECS instance returns
an ICMP error message such as `port XX unreachable` . Otherwise, no message is returned.
3. If the LVS node server receives the ICMP error message within the response timeout period, the
node server determines that the service is abnormal and the health check fails.
4. If the LVS node server does not receive any message within the response timeout period, the node
server determines that the service is normal and the health check succeeds. For UDP health checks, the health check result may not reflect the real status of a backend ECS instance in the following situation: If the backend ECS instance uses a Linux operating system, the speed at which ICMP messages in high concurrency scenarios are sent is limited due to the ICMP attack prevention feature of Linux. In this case, even if a service exception occurs, SLB may declare the backend ECS instance healthy because the error message `port XX unreachable` is not returned. Consequently, the health check result deviates from the actual service status. Solution: You can specify a request and a response for UDP health checks. The ECS instance is considered healthy only when the specified response is returned. However, the client must be configured accordingly for returning responses. Health check time window The health check feature effectively improves the availability of your services. However, to avoid impacts on system availability caused by frequent switching after failed health checks, the health check status only switches when health checks successively succeed or fail for a specified number of times within a certain time window. The health check time window is determined by the following three factors: Health check interval: how often health checks are performed Response timeout: the time to wait for a response Health check threshold: the number of times health checks succeed or fail successively The health check time window is calculated as follows: Time window for health check failures = Response timeout × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1) Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1) The response time of a successful health check is the duration from the time when the health check request is sent to the time when the response is received. When TCP health checks are used, the response time is almost negligible because only whether the specific port is alive is checked. For HTTP health checks, the response time depends on the performance and load of the application server and is typically within a few seconds. The health check result has the following impact on request forwarding: If the health check of the target ECS instance fails, new requests are distributed to other ECS instances. This does not affect client access. If the health check of the target ECS instance succeeds, new requests are distributed to the instance and client access is normal. If an exception occurs on the target ECS instance and a request arrives during a time window for health check failures, the request is still sent to the ECS instance because the number of failed health checks has not reached the unhealthy threshold (3 by default). In the case, client access fails. Examples of health check response timeout and health check interval The examples use the following health check settings: Response t imeout : 5s Healt h check int erval: 2s Healt hy t hreshold: 3 Unhealt hy t hreshold: 3 Time window for health check failures = Response timeout × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1). That is, 5 × 3 + 2 × (3-1) = 19s. The following figure shows the process of a status change from healthy to unhealthy. Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1). That is, (1 × 3) + 2 × (3-1) = 7s (assuming that the response time of a successful health check is 1s). The response time of a successful health check is the duration from the time when the health check request is sent to the time when the response is received. When TCP health checks are used, the response time is almost negligible because only whether the specific port is alive is checked. For HTTP health checks, the response time depends on the performance and load of the application server and is typically within a few seconds. The following figure shows the process of a status change from unhealthy to healthy. Domain name setting in HTTP health checks When HTTP health checks are used, you can set a domain name for health checks. The setting is optional. Some application servers verify the host field in requests. In this case, the request header must contain the host field. If a domain name is configured in the health check feature, SLB adds the domain name to the host field when forwarding a request to an application server. If no domain name is configured, the health check request will be denied by the application server because it does not contain a host field and the health check may fail. If your application server verifies the host field in requests, you must configure a domain name to make sure that the health check feature works.

### 7.2 Disable the health check feature

This topic describes how to disable the health check feature. If you disable the health check feature, requests may be distributed to unhealthy ECS instances and cause impacts on your business. We recommend that you enable the health check feature. Context You can only disable the health check feature for HTTP and HTTPS listeners. The health check feature for UDP and TCP listeners cannot be disabled.
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

Server Load Balancer (SLB) only supports certificates in the PEM format. Before you upload a certificate, make sure that the certificate content, certificate chain, and private key conform to the corresponding format requirements. Certificates issued by a root CA If the certificate was issued by a root CA, the received certificate is the only one that needs to be uploaded to SLB. In this case, the website configured with the certificate is regarded as a trusted website, and does not require additional certificates. The certificate must meet the following format requirements: The certificate must start with `-----BEGIN CERTIFICATE-----` and end with -----END CERTIFICATE- ----, and these parts must also be uploaded. Each line except the last line must contain 64 characters. The last line can contain 64 or fewer characters. The certificate content cannot contain any spaces. The following figure shows a sample certificate in PEM format issued by a root CA. Certificates issued by an intermediate CA If the certificate was issued by an intermediate CA, the received certificate file will contain multiple certificates. You must upload both the server certificate and the required intermediate certificates to SLB. The format of the certificate chain must meet the following requirements: The server certificate must be put first and the content of the one or more required intermediate certificates must be put underneath without any blank lines between the certificates. The certificate content cannot contain any spaces. Blank lines are not allowed between the certificates. Each line must contain 64 characters. For more information, see RFC 1421. The certificate must conform to the corresponding format requirements. Generally, the intermediate CA provides instructions about the certificate format when issuing the certificate. The certificate must conform to the format requirements. A sample certificate chain is shown as follows.

```
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
```

Public keys of certificates SLB supports the following public key algorithms: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521 RSA private keys When you upload a server certificate, you must upload the private key of the certificate. An RSA private key must meet the following format requirements: The private key must start with `-----BEGIN RSA PRIVATE KEY-----` and end with -----END RSA PRIVATE KEY-----, and these parts must also be uploaded. Blank lines are not allowed in the certificate content. Each line except the last line must contain 64 characters. The last line can contain 64 or fewer characters. For more information, see RFC 1421. You may use an encrypted private key. For example, the private key starts with `BEGIN PRIVATE KEY----`
  - `-` and ends with -----END PRIVATE KEY----- or starts with `-----BEGIN ENCRYPTED PRIVATE KEY-----`
and ends with -----END ENCRYPTED PRIVATE KEY-----. The private key may also contain `Proc-Type:` `4,ENCRYPTED` . In this case, you must first run the following command to convert the private key:

```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```

The following figure shows a sample RSA private key.

### 8.3 Upload a certificate

This topic describes how to create and upload a certificate. Before you create an HTTPS listener, you must upload the required server certificate and CA certificate to SLB. You do not need to configure certificates on backend servers after uploading the certificates to SLB. Prerequisites A server certificate is purchased. A CA certificate and a client certificate are generated. Context Note that you can create up to 100 certificates per account.
1. In the left-side navigation pane, click Cert if icat es.
2. Click Creat e Cert if icat e.
3. In the Creat e Cert if icat e dialog box, set certificate parameters and then click Creat e.

| Parameter | Description |
|---|---|
| Cert if icat e Name | Enter a name for the certificate. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), underscores ( ), and _ asterisks (*). |
| Organizat ion | Select the organization to which the certificate belongs. |
| Resource Group | Select the resource group to which the certificate belongs. |
| Cert if icat e T ype | Select Server Cert if icat e. For HTTPS one-way authentication, only the server certificate and the private key are required. |
| Public Key Cert if icat e | Copy and paste the contents of the server certificate into the field. Click Example to view the valid certificate format. For more information, see Certificate requirements. |
| Privat e Key | Copy and paste the private key of the server certificate into the field. Click Example to view the valid certificate format. For more information, see Certificate requirements. Not ice A private key is required only when you upload a server certificate. |
| Region | Select one or more regions where the certificate will be deployed. |

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

Common Name is the domain name of the SLB instance.
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

Enter a pass phrase when creating the Key. It is the password to protect the private Key from unauthorized access. Enter the same password twice.
3. Run the following command to create a csr file for the client Key.

```python
sudo openssl req -new -key /root/ca/users/client.key -out /root/ca/users/client.csr
```

Enter the pass phrase set in the previous step and other required information when prompted. A challenge password is the password of the client certificate. Note that it is not the password of the client Key.
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
