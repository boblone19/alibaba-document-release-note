---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 130
source_pdf: "5269826c1e6a94a5_Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Server%20Load%20Balancer%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer User Guide 20260828

## Table of Contents

- 1 What is SLB?
- 2 Log on to the SLB console
- 3 Quick start
  - 3.1 Overview
  - 3.2 Preparations
  - 3.3 Create an SLB instance
  - 3.4 Configure an SLB instance
  - 3.5 Release an SLB instance
  - 3.6 Enable Proxy Protocol to obtain client IP addresses
  - 3.7 Add backend servers and their ENIs
- 4 SLB instances
  - 4.1 Overview
  - 4.2 Instance management
    - 4.2.1 Instance overview
    - 4.2.2 Create and manage CLB instances
    - 4.2.3 Listeners
      - 4.2.3.1 Listener overview
      - 4.2.3.2 Configure and manage listeners
        - 4.2.3.2.1 Add a TCP listener
        - 4.2.3.2.2 Add a UDP listener
        - 4.2.3.2.3 Add an HTTP listener
        - 4.2.3.2.4 Add an HTTPS listener
        - 4.2.3.2.5 Configure forwarding rules
        - 4.2.3.2.6 Domain name extensions
          - 4.2.3.2.6.1 SLB additional domain names
          - 4.2.3.2.6.2 Add and manage additional domain names
    - 4.2.4 Backend servers
      - 4.2.4.1 Backend server overview
      - 4.2.4.2 vServer groups
        - 4.2.4.2.1 Create a vServer group
        - 4.2.4.2.2 Modify a vServer group
        - 4.2.4.2.3 Delete a vServer group
      - 4.2.4.3 Default server groups
        - 4.2.4.3.1 Add a backend server
        - 4.2.4.3.2 Change the weights of backend servers in the default server group
        - 4.2.4.3.3 Remove backend servers
      - 4.2.4.4 Primary/secondary server groups
        - 4.2.4.4.1 Create a primary/secondary server group
        - 4.2.4.4.2 Delete a primary/secondary server group
    - 4.2.5 Primary/secondary vServer groups
    - 4.2.6 Health checks
      - 4.2.6.1 Health check overview
      - 4.2.6.2 Configure health checks
      - 4.2.6.3 Disable the health check feature
    - 4.2.7 Associate an EIP with an internal-facing SLB instance and manage the EIP
    - 4.2.8 View monitoring data in the console
    - 4.2.9 View fine-grained monitoring data in the console
    - 4.2.10 View the details of an SLB instance
  - 4.3 Certificate management
    - 4.3.1 Certificate overview
    - 4.3.2 Certificate requirements
    - 4.3.3 Add and manage certificates
    - 4.3.4 Generate a CA certificate
    - 4.3.5 Convert certificate formats
  - 4.4 Manage access logs
  - 4.5 Access control
    - 4.5.1 Access control overview
    - 4.5.2 Create and manage ACLs
    - 4.5.3 Adjust the quota on ACLs
  - 4.6 Operation logs
  - 4.7 Tag management
    - 4.7.1 Overview
    - 4.7.2 Add tags
    - 4.7.3 Remove tags
    - 4.7.4 Search for resources by tag
- 5 Quick links

## 1 What is SLB?

This topic provides an overview of Server Load Balancer (SLB). SLB distributes network traffic across backend Elastic Compute Service (ECS) instances based on forwarding rules. SLB extends the service capability of applications and enhances their availability.

**Overview**

After you add ECS instances that are deployed in the same region to an SLB instance, SLB uses virtual IP addresses (VIPs) to virtualize the ECS instances into backend servers in a highperformance server pool that ensures high availability. Client requests are distributed to the ECS instances based on forwarding rules. SLB checks the health status of the ECS instances and automatically removes unhealthy ECS instances from the pool to eliminate single points of failure. This improves the availability of your applications.

**Components**

SLB consists of the following components: An SLB instance is a running entity of the SLB service that receives and distributes traffic to backend servers. To get started with SLB, you must create an SLB instance and add at least one listener and two ECS instances to the SLB instance. A listener checks client requests and forwards them to backend servers. A listener also performs health checks on backend servers. ECS instances are used as backend servers in SLB to receive and process client requests. You can add ECS instances to the default server group of an SLB instance. You can also add multiple ECS servers to vServer groups or primary/secondary server groups after the corresponding groups are created.

**Benefits**

High availability SLB is designed with full redundancy to eliminate single points of failure and support zonedisaster recovery. You can use SLB with services such as Apsara Stack DNS to implement geo-disaster recovery with 99.95% service uptime. SLB can be scaled based on application loads to ensure business continuity during traffic fluctuations. Scalability You can add or remove backend servers based on your business requirements to improve the availability of your service. Cost-effectiveness SLB can reduce 60% of load balancing costs compared with traditional hardware-based solutions. Security You can integrate SLB with Apsara Stack Security to defend your applications against DDoS attacks of up to 5 Gbit/s. High concurrency An SLB cluster supports hundreds of millions of concurrent connections and a single SLB instance supports tens of millions of concurrent connections. sole

## 2 Log on to the SLB console

This topic describes how to navigate to the Server Load Balancer (SLB) console after you log on to the Apsara Uni-manager Management Console by using Google Chrome.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. sole

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

**Forgot password**

If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**. For information about how to bind and enable MFA, see the **Security Center** >
**Multi-factor Authentication** > **Manage Multi-factor Authentication** section in
the Apsara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose **Products > Networking > Server Load Balancer**.

## 3 Quick start

### 3.1 Overview

This topic describes how to create an Internet-facing Server Load Balancer (SLB) instance to distribute client requests to two backend Elastic Compute Service (ECS) instances. Before you create an SLB instance, you must determine the configurations of the SLB instance, such as the region, type, and specification. For more information, see Preparations. This topic includes the following operations: Create an SLB instance. An SLB instance is an entity that provides load balancing services. After you create an SLB instance, you must add listeners and backend servers to the SLB instance. If you no longer need the SLB instance, you can release it.

### 3.2 Preparations

Before you create a Server Load Balancer (SLB) instance, you must determine the configurations of the SLB instance, such as the listener type and network type.

**Select a region**

When you select a region, take note of the following items: SLB does not support cross-region deployment. Therefore, you must deploy the SLB instance and backend Elastic Compute Service (ECS) instances in the same region. To reduce the network latency and accelerate data transmission, we recommend that you select the region that is nearest to your users. To provide more stable and reliable load balancing services, SLB supports primary/secondary zone deployment in most regions. You can select more than one zone to implement zone-disaster recovery. We recommend that you select a region that supports primary/secondary zone deployment.

**Select a network type (Internet-facing or internal-facing)**

SLB provides Internet-facing and internal-facing load balancing services: If you want to use SLB to distribute requests from the Internet, create an Internet-facing SLB instance. An Internet-facing SLB instance is assigned a public IP address to receive requests from the Internet. If you want to use SLB to distribute requests from the internal network, create an internalfacing SLB instance. An internal SLB instance is assigned only a private IP address. It is accessible only over the internal network and is not accessible over the Internet.

**Select an instance specification**

Apsara Stack provides high-performance SLB instances that use exclusive resources to ensure high service availability. The following table describes the supported specifications.

| Specification | Maximum connections | New connections per second | Queries per second |
|---|---|---|---|
| Small I (slb.s1.small) | 5,000 | 3,000 | 1,000 |
| Medium I (slb.s2.small) | 50,000 | 5,000 | 5,000 |
| Medium II (slb.s2.medium) | 100,000 | 10,000 | 10,000 |
| Large I (slb.s3.small) | 200,000 | 20,000 | 20,000 |
| Large II (slb.s3.medium) | 500,000 | 50,000 | 30,000 |
| Super Large I (slb.s3.large) | 1,000,000 | 100,000 | 50,000 |

The available specifications vary based on the actual scenario. The preceding table is for reference only.

**Select a listener protocol**

SLB supports TCP and UDP load balancing at Layer 4, and HTTP and HTTPS load balancing at Layer 7. A Layer 4 listener distributes requests to backend servers without modifying packet headers. After a client request reaches a Layer 4 listener, SLB establishes a TCP connection to the ECS instance port specified in the listener configuration. A Layer 7 listener functions as a reverse proxy. After a client request reaches a Layer 7 listener, SLB establishes a new TCP connection to a backend server over HTTP, instead of directly forwarding the request to the backend ECS instance. Compared with Layer 4 listeners, Layer 7 listeners require an additional step of Tengine processing. Therefore, Layer 4 listeners outperform Layer 7 listeners. In addition, the performance of Layer 7 listeners may be degraded due to factors such as insufficient client ports or excessive backend server connections. If you require high performance, we recommend that you use Layer 4 listeners.

**Create backend servers**

Before you use SLB, you must create ECS instances that function as backend servers, deploy applications on the ECS instances, and then add the ECS instances to your SLB instance to process client requests. When you create ECS instances, take note of the following items: Region and zones of the ECS instances Make sure that the ECS instances are deployed in the same region as the SLB instance. In this example, an ECS instance named ECS01 and an ECS instance named ECS02 are created in a specified region. Application configurations In this example, two static web pages are hosted on ECS01 and ECS02 by using Apache. Enter the elastic IP address (EIP) that is associated with ECS01 in the address bar of your browser. Enter the EIP that is associated with ECS02 in the address bar of your browser. No additional configurations are required after you deploy applications on the ECS instances. If you want to use a Layer 4 (TCP or UDP) listener and your ECS instances run Linux, make sure that the following parameters in the net.ipv4.conf file of the /etc/sysctl.conf directory are set to 0:

```
net.ipv4.conf.default.rp_filter = 0 net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.eth0.rp_filter = 0
```

### 3.3 Create an SLB instance

A Server Load Balancer (SLB) instance is an entity that provides load balancing services. You can add multiple listeners and backend servers to an SLB instance.

**Prerequisites**

Elastic Compute Service (ECS) instances are created, and applications are deployed on the ECS instances. The ECS instances are created in the same organization as the SLB instance to be created. In addition, security group rules are configured for the ECS instances to allow HTTP requests from port 80 and HTTPS requests from port 443.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, click **Create CLB**.
5. On the **Create SLB Instance** page, configure the SLB instance as follows.

| Parameter | Description |
|---|---|
| Area |   |
| Organization/ Resource group | Select the organization and resource group for the CLB instance from the drop- down lists. |
| Region/Availa bility zone | Select the region and availability zone for the CLB instance from the drop-down lists. |
| Cluster | Select the cluster for the CLB instance from the drop-down list. |
| Basic configurations |   |
| Number of instances | Enter the number of CLB instances to create. |
| CLB instance name | Enter a name for the instance. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It can contain digits, full-width characters, hyphens (-), colons (:), periods (.), and underscores ( ). The name supports line breaks and spaces but _ cannot start with http:// or https:// . |
| Specification type | Select the specification type for the CLB instance. Guaranteed-Performance is selected by default. |

| Instance specification | Select the instance specification for the CLB instance. Performance metrics vary for different specifications of Guaranteed-Performance instances. For more information, see Instance specifications. You can also click AI-powered Specification Recommendation to get a recommendation. The AI assistant suggests a suitable instance specification based on your business needs. When you click Select Now, the recommended specification is automatically selected in the list. |
|---|---|
| Network and instance type |   |
| Instance type | Select the instance type. The options are Internal and Public. Internal is selected by default. |
| Network type | Select the network type. The options are Virtual Private Cloud and Classic Network. Note You can select Virtual Private Cloud only when Instance Type is set to Internal. |
| IP version | Select the IP version for the instance. You can select multiple versions. The options are IPv4 and IPv6. Note You can select IPv6 only when Network Type is set to Classic Network. If you select multiple IP versions, one instance is created for each selected version. |
| VPC | Select a VPC. Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. You can click Create VPC to create a VPC. After creation, you may need to refresh the page to select the new VPC. |

| VSwitch | Select a VSwitch. Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. You can click Create VSwitch to create a VSwitch. After creation, you may need to refresh the page to select the new VSwitch. |
|---|---|
| Line type | Select the line type based on the instance plan. The line types for Internal instances differ from those for Public instances. Public instances support line types such as BGP SLB and CMCC AZ1. _ _ Internal instances support line types such as slbprivatevipv6. Note This parameter is required only when Network Type is set to Classic Network and IP Version includes IPv6. |
| Service IP | Enter a service IP address. If you leave this field blank, the system automatically assigns an IP address. Note Ensure that the service IP address is valid. Otherwise, the CLB instance cannot be created. If you specify a private IP address, it must be within the CIDR block of the selected VSwitch. |
| Bandwidth limit | Select a bandwidth limit. The options are Unlimited and Limited. Unlimited is selected by default. Note You can select Limited only when Instance Type is set to Public. |
| Bandwidth (Mbps) | Enter the bandwidth. The value must be between 1 and 5,120. Note This parameter is required only when Instance Type is set to Public and Bandwidth Limit is set to Limited. |
| VPC + EIP for public access |   |

| Enable EIP association | Specifies whether to associate an Elastic IP Address (EIP). Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. |
|---|---|
| Elastic IP Address (EIP) | Select an Elastic IP Address (EIP). Note This parameter is required only when Instance Type is set to Internal, Network Type is set to Virtual Private Cloud, and the Enable EIP Association switch is turned on. You can click Create EIP to create an EIP. After creation, you may need to refresh the page to select the new EIP. |

Before creating the instance, use the **Configuration Overview** panel on the right to review your settings. Click a field value to navigate to the corresponding parameter and modify it as needed. Click **Quota Management** (if the organization or resource group has no quota) or **Manage** in the **Quota** area (if the organization or resource group has a quota) to manage quotas for cloud products. For more information about quota management, see the **Quota Management** chapter in the **Apsara Uni-manager Operation Console User Guide** .
6. Create the CLB instance.
For a service created in Service Management with the **Cloud Resource** set to **Server**
**Load Balancer (SLB)**, confirm the related configuration parameters and click **Confirm**
**Order**.
For a service that is not created in Service Management where the **Cloud Resource** is
**Server Load Balancer (SLB)**: Confirm the relevant configuration parameters, and click
**Submit**.
For more information about service management, see the **Service Management** chapter in the **Apsara Uni-manager Operation Console User Guide** .
7. **(Optional)** After creating the instance, you can download its details. On the **Instance**
**Management** page, click the
icon in the upper-right corner. Select the columns to include, such as Instance ID, Organization, and Resource Group, and then click **OK**.

**What to do next**

### 3.4 Configure an SLB instance

This topic describes how to configure a Server Load Balancer (SLB) instance. To enable an SLB instance to forward traffic, you must add at least one listener and one group of backend servers to the SLB instance. In this example, a TCP listener and two Elastic Compute Service (ECS) instances named ECS01 and ECS02 are added to an SLB instance. These ECS instances function as backend servers that host static web pages.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the SLB instance that you want to manage and
click **Configure Listener** in the **Actions** column.
5. In the **Protocol & Listener** step, configure a listener based on the following information
and use the default values for other parameters. Then, click **Next**.
**Listener Protocol**: the listener protocol. In this example, **TCP** is selected.
**Listening Port**: the frontend port that is used to receive requests and distribute
requests to backend servers. The SLB instance uses this port to provide external services. In most cases, port 80 is used for HTTP listeners and port 443 is used for HTTPS listeners. In this example, port **80** is used. Click **Modify** next to Advanced Settings to modify the configurations in the **Advanced**
**Settings** section.
**Scheduling Algorithm**: the scheduling algorithm. In this example, **Round Robin** is
selected. Valid values:
**Weighted Round-robin (WRR)**: Backend servers with higher weights receive more
requests than backend servers with lower weights.
**Round Robin**: Requests are distributed to backend servers in sequence.
**Consistent Hashing**: Only TCP and UDP listeners support consistent hashing.
**Hash Factor**: You can set this parameter to **Source IP Address** or **Four-**
**element**.
**Source IP Address**: specifies consistent hashing that is based on source IP
addresses. Requests from the same source IP address are distributed to the same backend server.
**Four-element**: specifies consistent hashing that is based on the following
factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Only high-performance SLB instances support consistent hashing.
**Bandwidth Throttling**: specifies whether to enable bandwidth throttling. Applications
that run on backend ECS instances provide external services. You can set bandwidth caps to limit the service capabilities of applications. In this example, Bandwidth Throttling is turned on.
**Maximum Bandwidth**: the maximum bandwidth. Valid values: 0 to 1000. Unit:
Mbit/s.
6. In the **Backend Servers** step, perform the following steps to add backend servers. Then,
click **Next**. i. Set the Server Group Type parameter to **Default Server Group**. Then, click **Add More**. ii. In the **Servers** panel, select the ECS instances named ECS01 and ECS02 and click **Next**. iii. In the **Configure Weight** step, configure weights for backend servers. A backend server with a higher weight receives more requests. The default value is **100**. We recommend that you use the default value. Click **Add**. iv. On the **Default Server Group** tab, specify the backend ports that are used by backend ECS instances to receive requests. You can specify the same port for multiple backend servers that are added to the same SLB instance. In this example, port **80** is used.
7. In the **Health Check** step, configure health checks. We recommend that you use the
default settings. Then, click **Next**. After you enable the health check feature for the SLB instance, the SLB instance periodically checks whether the backend ECS instances are healthy. When the SLB instance detects an unhealthy ECS instance, the SLB instance distributes requests to other healthy ECS instances. When the unhealthy ECS instance recovers, the SLB instance distributes requests to the recovered ECS instance again.
8. In the **Confirm Configurations** step, click **Submit**.
9. In the **SLB Configuration Wizard** message, wait until the configurations are complete and
click **OK**.
0. Return to the **Instance Management** page. Then, click the
icon to refresh the page. If the health check status of the backend ECS instances is **Running**, the backend ECS instances can process requests distributed from the SLB instance.
1. Enter the IP address of the SLB instance in the address bar of a browser to test the load
balancing performance of the SLB instance. Figure 1: ECS01 Figure 2: ECS02

### 3.5 Release an SLB instance

This topic describes how to release a Server Load Balancer (SLB) instance. After you release an SLB instance, the backend Elastic Compute Service (ECS) instances of the SLB instance are not released or affected.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, release one or more CLB instances:
To release a single instance: Find the target instance and in the **Actions** column, click
**Release**.
To release multiple instances: Select the checkboxes of the instances, and then click
**Release** below the instance list.
5. In the **Release** panel, click **Release**.
6. In the **Release Resource** dialog box, click **Confirm Release**.

### 3.6 Enable Proxy Protocol to obtain client IP addresses

**obtain client IP addresses**

You can enable Proxy Protocol for a Layer 4 listener of Server Load Balancer (SLB) to obtain client IP addresses.

**Background information**

In most cases, the source IP addresses that are obtained by the backend servers of Layer 4 SLB are client IP addresses. However, if the client IP address of a request is translated into another IP address before SLB forwards the request to a backend server, the backend server cannot obtain the client IP address. Proxy Protocol can be used by Layer 4 SLB listeners to pass client IP addresses to backend servers. After Proxy Protocol is enabled, SLB adds a TCP header to a request without modifying the existing headers. The TCP header carries information such as the source IP address, destination IP address, source port, and destination port. SLB supports only Proxy Protocol V2.

**Usage notes**

Before you enable Proxy Protocol, make sure that your backend servers support Proxy Protocol V2. Otherwise, new connections fail. NGINX Plus R16 and later and open source NGINX 1.13.11 and later support Proxy Protocol V2. If multiple listeners are associated with the same backend server group, you must enable Proxy Protocol for all listeners.

**Step 1: Add a TCP or UDP listener**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the instance that you want to manage and click
**Configure Listener** in the **Actions** column.
5. Follow the configuration wizard to configure a listener.
**Listener Protocol**: Select **TCP** or **UDP**.
Enable Proxy Protocol: Click **Modify** next to **Advanced Settings**. Then, turn on **Use**
**Proxy Protocol to Pass Client IP Addresses to Backend Servers** and click **Next**.
For more information, see Add a TCP listener or Add a UDP listener.

**Step 2: Enable Proxy Protocol for a backend server**

After you enable Proxy Protocol for a listener, you must also enable Proxy Protocol for backend servers. Otherwise, request forwarding failures or health check failures occur. Log in to a backend server and run the following command to enable Proxy Protocol to obtain client IP addresses:

```
http {
    #...
    server {
        listen 80   proxy_protocol;
        listen 443  ssl proxy_protocol;
        #...
```

`}` `}`

```
stream {
    #...
    server {
        listen 12345 proxy_protocol;
        #...
```

`}` `}`

**Step 3: Obtain client IP addresses**

The following example shows how an IPv4 client IP address is carried in the Proxy Protocol V2 header in the binary format. The following example shows how an IPv6 client IP address is carried in the Proxy Protocol V2 header in the binary format.

### 3.7 Add backend servers and their ENIs

**ENIs**

An elastic network interface (ENI) is a network interface that can be associated with an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). ENIs can improve the availability of clusters, offer cost savings in service failovers, and enable fine-grained network management. You can add a backend server and its associated primary and secondary ENIs to a Server Load Balancer (SLB) instance.

**Background information**

If multiple ENIs are associated with the ECS instance that you want to add to an SLB instance, you can add both the primary and secondary ENIs of the ECS instance. You can add the primary and secondary ENIs of ECS instances only for highperformance SLB instances. You can add only secondary ENIs in the console. To add primary ENIs, make an API request.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance management details page, click the **vServer Groups**, **Default Server**
**Group**, or **Primary/Secondary Server Groups** tab.
You can add ECS instances and their associated primary and secondary ENIs to the default server group, a vServer group, or a primary/secondary server group. A vServer group is used in this example.
6. On the **vServer Groups** tab, click **Create vServer Group**.
7. On the Create vServer Group page, configure the **vServer Group Name** parameter.
8. Click **Add** to open the **Servers** panel.
9. In the **Select Servers** step, turn on **Advanced Settings**.
0. Select the ECS instances that you want to add and click **Next**.
1. In the **Configure Weight** step, configure the **Port** and **Weight** parameters and click **Add**.
Specify the Port and Weight parameters based on the following information:
**Port**: The backend port opened on an ECS instance to receive requests.
You can specify the same port on multiple backend servers for the same SLB instance. In addition, you can click **Add Port** to specify multiple ports on a backend server.
**Weight**: An ECS instance with a higher weight receives more requests.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests. After you add backend servers to the server group of the listener, you can view the server group that contains the primary and secondary ENIs on the **Instances** page. : indicates an ECS instance. : indicates the primary and secondary ENIs.
2. Select the ECS instances that you want to add and click **Create**. In the **Confirm** message,
click **OK**.

## 4 SLB instances

### 4.1 Overview

This topic describes how to view the total number of instances and quotas on public IP addresses and internal IP addresses in the Server Load Balancer (SLB) console.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. In the left-side navigation pane, click **Overview**.
4. On the **Overview** page, you can view the following information:
In the **Instance Overview** section, view the total number of SLB instances, the number of SLB instances in the Running state, the number of certificates, and the number of expired certificates. In the **Public IP Address Quota**, **Internal IP Quota - VPC**, or **Internal IP Quota -**
**Classic Network** section, view the quotas, assignment rate, and usage of public IP
addresses and private IP addresses. In the **Top 10 in Quota Use** section, click the **VPC Intranet Quota Utilization**, **Classic**
**Network Quota Utilization**, or **Internet Quota Utilization** tab to view the quota
usage rankings of the organization and the quota usage of each network type in the previous 7, 15, or 30 days. In the **Monitoring Sorting** section, you can view the monitoring data. In the **Alarm Statistics** section, you can view alerts.

### 4.2 Instance management

#### 4.2.1 Instance overview

Server Load Balancer (SLB) balances loads by distributing requests from clients across backend servers. To use SLB, you must create an SLB instance and add listeners and backend servers to the SLB instance.

**Instance types**

Apsara Stack provides Internet-facing and internal-facing SLB instances.

**Internet-facing SLB instances**

When you create an Internet-facing SLB instance, the system automatically assigns a public IP address to the SLB instance. You can associate your domain name with the public IP address. SLB instances receive requests from clients over the Internet and distribute the requests to backend servers based on the forwarding rules that you configure on listeners. Features of an Internet-facing SLB instance when it serves Internet-facing applications: An Internet-facing SLB instance is assigned a public IP address to provide services over the Internet. You cannot disassociate the public IP address from the SLB instance. An Internet-facing SLB instance uses the default metering method or the pay-by-bandwidth metering method.

**Internal-facing SLB instances**

An internal-facing SLB instance is assigned a private IP address to distribute requests from the internal network of Apsara Stack to backend servers based on the forwarding rules that you configure on listeners. If you want an internal-facing SLB instance to process requests from the Internet, you can associate an elastic IP address (EIP) with the SLB instance. Features of an internal-facing SLB instance when it serves Internet-facing applications: An internal-facing SLB instance can use the associated EIP to provide services over the Internet. You can disassociate the EIP from the SLB instance if you no longer need the EIP. You can associate an EIP with an Internet Shared Bandwidth instance. An EIP that is associated with an Internet Shared Bandwidth instance supports the subscription, pay-asyou-go, and pay-by-95th-percentile-bandwidth billing methods. The network types supported by an internal-facing SLB instance vary based on the billing method of the internal-facing SLB instance. Subscription internal-facing SLB instances support the following network types: classic network and virtual private cloud (VPC). VPC If an internal-facing SLB instance is deployed in a VPC, the private IP address of the SLB instance is allocated from the CIDR block of the specified vSwitch in the VPC. The internal-facing SLB instance can be accessed only by Elastic Compute Service (ECS) instances in the VPC. Classic network If an internal-facing SLB instance is deployed on the classic network, the private IP address of the SLB instance is allocated and managed by Apsara Stack. The internalfacing SLB instance can be accessed only by ECS instances on the classic network.

**Important**

Internal-facing SLB instances of the classic network type are no longer available for purchase. Pay-as-you-go internal-facing SLB instances support only the VPC network type.

**Instance specifications**

High-performance SLB instances have the following key metrics: Maximum number of connections The maximum number of concurrent connections that an SLB instance supports. If the number of existing concurrent connections reaches the upper limit, new connection requests are dropped. Connections per second (CPS) The number of new connections that can be established per second. If CPS reaches the upper limit, new connection requests are dropped. Queries per second (QPS) The number of HTTP or HTTPS queries (requests) that can be processed per second. This metric is specific to Layer 7 listeners. If QPS reaches the upper limit, new connection requests are dropped. Table 1: Specifications of high-performance SLB instances

| Specification | Maximum number of connections | CPS | QPS |
|---|---|---|---|
| Small I (slb.s1.small) | 5,000 | 3,000 | 1,000 |
| Medium I (slb.s2.small) | 50,000 | 5,000 | 5,000 |
| Medium II (slb.s2.medium) | 100,000 | 10,000 | 10,000 |
| Large I (slb.s3.small) | 200,000 | 20,000 | 20,000 |
| Large II (slb.s3.medium) | 500,000 | 50,000 | 30,000 |
| Super Large I (slb.s3.large) | 1,000,000 | 100,000 | 50,000 |

The available specifications vary based on the actual scenario. The preceding table is for reference only.

#### 4.2.2 Create and manage CLB instances

A Classic Load Balancer (CLB) instance is a running instance of the load balancing service. You can add multiple listeners and backend servers to a CLB instance.

**Prerequisites**

Create an ECS instance and deploy your application services. Ensure that the ECS instance and the CLB instance are in the same organization and that the security group of the ECS instance allows access on ports 80 (HTTP) and 443 (HTTPS).

**Create a CLB instance**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, click **Create CLB**.
5. On the **Create SLB Instance** page, configure the SLB instance as follows.

| Parameter | Description |
|---|---|
| Area |   |
| Organization/ Resource group | Select the organization and resource group for the CLB instance from the drop- down lists. |
| Region/Availa bility zone | Select the region and availability zone for the CLB instance from the drop-down lists. |
| Cluster | Select the cluster for the CLB instance from the drop-down list. |
| Basic configurations |   |
| Number of instances | Enter the number of CLB instances to create. |
| CLB instance name | Enter a name for the instance. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It can contain digits, full-width characters, hyphens (-), colons (:), periods (.), and underscores ( ). The name supports line breaks and spaces but _ cannot start with http:// or https:// . |
| Specification type | Select the specification type for the CLB instance. Guaranteed-Performance is selected by default. |
| Instance specification | Select the instance specification for the CLB instance. Performance metrics vary for different specifications of Guaranteed-Performance instances. For more information, see Instance specifications. You can also click AI-powered Specification Recommendation to get a recommendation. The AI assistant suggests a suitable instance specification based on your business needs. When you click Select Now, the recommended specification is automatically selected in the list. |
| Network and instance type |   |

| Instance type | Select the instance type. The options are Internal and Public. Internal is selected by default. |
|---|---|
| Network type | Select the network type. The options are Virtual Private Cloud and Classic Network. Note You can select Virtual Private Cloud only when Instance Type is set to Internal. |
| IP version | Select the IP version for the instance. You can select multiple versions. The options are IPv4 and IPv6. Note You can select IPv6 only when Network Type is set to Classic Network. If you select multiple IP versions, one instance is created for each selected version. |
| VPC | Select a VPC. Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. You can click Create VPC to create a VPC. After creation, you may need to refresh the page to select the new VPC. |
| VSwitch | Select a VSwitch. Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. You can click Create VSwitch to create a VSwitch. After creation, you may need to refresh the page to select the new VSwitch. |

| Line type | Select the line type based on the instance plan. The line types for Internal instances differ from those for Public instances. Public instances support line types such as BGP SLB and CMCC AZ1. _ _ Internal instances support line types such as slbprivatevipv6. Note This parameter is required only when Network Type is set to Classic Network and IP Version includes IPv6. |
|---|---|
| Service IP | Enter a service IP address. If you leave this field blank, the system automatically assigns an IP address. Note Ensure that the service IP address is valid. Otherwise, the CLB instance cannot be created. If you specify a private IP address, it must be within the CIDR block of the selected VSwitch. |
| Bandwidth limit | Select a bandwidth limit. The options are Unlimited and Limited. Unlimited is selected by default. Note You can select Limited only when Instance Type is set to Public. |
| Bandwidth (Mbps) | Enter the bandwidth. The value must be between 1 and 5,120. Note This parameter is required only when Instance Type is set to Public and Bandwidth Limit is set to Limited. |
| VPC + EIP for public access |   |
| Enable EIP association | Specifies whether to associate an Elastic IP Address (EIP). Note This parameter is required only when Instance Type is set to Internal and Network Type is set to Virtual Private Cloud. |

| Elastic IP Address (EIP) | Select an Elastic IP Address (EIP). Note This parameter is required only when Instance Type is set to Internal, Network Type is set to Virtual Private Cloud, and the Enable EIP Association switch is turned on. You can click Create EIP to create an EIP. After creation, you may need to refresh the page to select the new EIP. |
|---|---|

Before creating the instance, use the **Configuration Overview** panel on the right to review your settings. Click a field value to navigate to the corresponding parameter and modify it as needed. Click **Quota Management** (if the organization or resource group has no quota) or **Manage** in the **Quota** area (if the organization or resource group has a quota) to manage quotas for cloud products. For more information about quota management, see the **Quota Management** chapter in the **Apsara Uni-manager Operation Console User Guide** .
6. Create the CLB instance.
For a service created in Service Management with the **Cloud Resource** set to **Server**
**Load Balancer (SLB)**, confirm the related configuration parameters and click **Confirm**
**Order**.
For a service that is not created in Service Management where the **Cloud Resource** is
**Server Load Balancer (SLB)**: Confirm the relevant configuration parameters, and click
**Submit**.
For more information about service management, see the **Service Management** chapter in the **Apsara Uni-manager Operation Console User Guide** .
7. **(Optional)** After creating the instance, you can download its details. On the **Instance**
**Management** page, click the
icon in the upper-right corner. Select the columns to include, such as Instance ID, Organization, and Resource Group, and then click **OK**.

**More operations**

**CLB instance list**

The **Instance Management** page lists your created CLB instances. The list can display up to 10,000 records across 100 pages. If the number of records exceeds 10,000, use filters to display the data you need. You can search for a target instance by entering keywords or by using advanced filters with specific criteria. Click the icon in the upper-right corner of the list to customize which columns to show or hide, and to drag and drop to reorder columns. Click the icon next to a specific column name for extended sorting options. Click the icon to the right of the **Status** column to filter instances by status. Click the icon to the right of the **Service address** column to filter instances by service address type. Click the icon in the **Monitoring** column to view instance, port, and high-precision second-level monitoring information for the target CLB instance. Click the icon to the right of the **Instance ID/name** column to modify the name of the target CLB instance. In the **Service address** column, click the VPC, VSwitch, or Service IP to view details of the corresponding VPC, VSwitch, or Elastic IP Address (EIP) that the CLB instance belongs to or is bound to. In the **Port/Health check/Backend server** column, click a port number to view the listener information for the target CLB instance. In the **Port/Health check/Backend server** column, click the backend server information to view the server group information for the target CLB instance. Expand a server group and click an instance name to view the details of a specific instance added to the server group. Click the toggle switch in the **Instance protection** column to enable or disable instance protection.

**Manage tags**

On the **Instance Management** page, you can use tags to mark and group instances. For more information, see Manage tags.

**Instance protection**

After creating a CLB instance, you can enable release protection for it to prevent accidental deletion.
1. On the **Instance Management** page, find the target instance, and in the **Instance**
**Protection** column, click the **Release Protection** switch.
2. In the dialog box that appears, click **OK**.

**Start or stop an instance**

You can start or stop a CLB instance at any time. A stopped instance no longer accepts or forwards client traffic.
1. On the **Instance Management** page, start or stop one or more instances:
To start or stop a single instance: Find the target instance and in the **Actions** column, click **Start** or **Stop**. To start or stop multiple instances: Select the checkboxes of the instances, and then click
**Start** or **Stop** below the instance list.
2. In the dialog box that appears, click **OK**.

**Release an instance**

You can release instances that are no longer needed. Before releasing an instance, you must disable its release protection.
1. On the **Instance Management** page, release one or more CLB instances:
To release a single instance: Find the target instance and in the **Actions** column, click
**Release**.
To release multiple instances: Select the checkboxes of the instances, and then click
**Release** below the instance list.
2. In the **Release** panel, click **Release**.
3. In the **Release Resource** dialog box, click **Confirm Release**.

**Modify instance specification**

You can change the instance specification of a Guaranteed-Performance CLB instance to meet your performance requirements.
1. On the **Instance Management** page, find the target instance, and in the **Actions** column,
click
**> Modify Specification**.
2. On the **Modify SLB Specification** page**,** modify the **Instance Specification** and
**Bandwidth Limit** settings based on your performance requirements, and then click
**Submit**.
**Instance Specification**: You can also click **AI-powered Specification**
**Recommendation** to get a recommendation. The AI assistant suggests a suitable instance
specification based on your business needs. When you click **Select Now**, the recommended specification is automatically selected in the list.

**Modify an IP address**

You can modify the service address.

**Warning**

Modifying the service IP address (VIP) interrupts traffic forwarding for about five minutes. Proceed with caution. Before modifying the IP address, you must disable release protection for the instance and ensure that the new IP address is not already allocated.
1. On the **Instance Management** page, find the target instance, and in the **Actions** column,
click
**> Modify IP Address**.
2. In the **Modify IP Address** panel, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Current IP | Displays the current private service address of the SLB instance in the VPC. |

| Current subnet | Displays the current subnet IP address of the SLB instance. This parameter is displayed only for internal-facing SLB instances in a VPC. |
|---|---|
| Subnet | Select a new subnet. This parameter is required only for internal-facing SLB instances in a VPC. |
| Automatically assign IPv4 address | Specify whether to automatically assign an IPv4 address. |
| IPv4 address | Enter a custom IPv4 address. This parameter is required if you do not select Automatically Assign IPv4 Address. |

**Manage a CLB instance**

1. On the **Instance Management** page, find the target instance, and click the instance ID in
the **Instance ID/Instance Name** column, information in the **Port/Health**
**Check/Backend Server** column, or **Listener Configuration Wizard**, **Add Backend**
**Server**, or **Manage** in the **Actions** column.
2. On the **Instance Details** page, you can manage the target CLB instance.
The key information card for the instance displays important information, including the instance ID, status, region, network type, number of listeners, and monitoring data. Click the instance ID next to **Affiliated Network** to view the details of the VPC to which the CLB instance belongs. Click the number next to **Number of Listeners** to view and manage the protocols and listeners for the CLB instance. Click the data under any monitoring metric to view the CloudMonitor data for the CLB instance. Click the **Instance Details** tab to view or manage basic information, specification information, and EIP information for the CLB instance. In the **Basic information** section, click the icon next to **Instance Name** to modify the name of the CLB instance. In the **Basic information** section, click the toggle switch next to **Release Protection** to configure instance protection. In the **Specification information** section, click the instance ID next to **Affiliated**
**Network** to view the details of the VPC and VSwitch to which the CLB instance belongs.
For an internal-facing instance in a VPC, click **Modify Specification** in the upper-right corner of the **Specification information** section to change the instance specification. For an internal-facing instance in a VPC, click **Bind** or **Unbind** in the upper-right corner of the **EIP information** section to associate and manage an EIP. For more information, see Associate and manage an EIP for an internal-facing SLB instance. If an EIP is associated, click its ID next to **EIP** to view its details. Click the **Listeners** tab to manage the listeners for the instance. For more information, see Configure and manage listeners. Click the **Virtual server groups** tab to manage the virtual server groups for the instance. For more information, see Virtual server groups. Click the **Default server group** tab to manage the default server group for the instance. For more information, see Default server group. Click the **Primary/secondary server group** tab to manage the primary/secondary server groups for the instance. For more information, see Primary/secondary server groups. Click the **Monitoring** tab to view the CloudMonitor data for the instance. For more information, see View monitoring data in the console. Click the **High-precision second-level monitoring** tab to view second-level CloudMonitor data for Layer 4 load balancing. For more information, see View highprecision second-level monitoring data in the console. Click the **Action log** tab to view the operation logs for the instance. For more information, see Action logs. In the upper-right corner, click **Start** or **Stop** to start or stop the CLB instance. In the upper-right corner, click **Modify Specification** to change the instance specification.

#### 4.2.3 Listeners

##### 4.2.3.1 Listener overview

This topic provides an overview of listeners. After you create a Server Load Balancer (SLB) instance, you must configure one or more listeners for the SLB instance. A listener checks for connection requests and then distributes the requests to backend servers based on the forwarding rules that are defined by a specified scheduling algorithm. SLB provides TCP and UDP listeners for Layer 4 load balancing, and HTTP and HTTPS listeners for Layer 7 load balancing. The following table describes the features and use scenarios of these listeners.

| Protocol | Description | Use scenario |
|---|---|---|
| TCP | A connection-oriented protocol that requires a logical connection to be established before data can be transmitted. Session persistence is based on source IP addresses. Source IP addresses are visible at the network layer. Data is transmitted at a fast rate. | Applicable to scenarios that require high reliability and data accuracy but can withstand a low transmission speed. These scenarios include file transmission, email sending and receiving, and remote logons. Web applications that do not have custom requirements. |

| UDP | A connectionless protocol. UDP transmits data packets directly instead of making a three-way handshake with the other party before UDP sends data. UDP does not provide error recovery or data re-transmission. Fast data transmission but relatively low reliability. | Applicable to scenarios where real- time transmission outweighs reliability, such as video conferencing and real-time quote services. |
|---|---|---|
| HTTP | An application-layer protocol that is used to package data. Cookie-based session persistence. Retrieve client IP addresses by using the X-Forward-For header. | Intended for applications that identify data content, such as web applications and mobile games. |
| HTTPS | Encrypted data transmission that prevents unauthorized access. Centralized certificate management service. You can upload certificates to SLB. Then, data decryption is offloaded from backend servers to SLB. | Intended for applications that require encrypted data transmission. |

##### 4.2.3.2 Configure and manage listeners

###### 4.2.3.2.1 Add a TCP listener

TCP provides reliable and accurate content delivery at relatively low connection speeds. Therefore, TCP is ideal for file transfer, email services, and remote logins. You can add a TCP listener to forward TCP requests.

**Step 1: Open the listener configuration wizard**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **SLB Configuration Wizard** page:
On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure Listener** in the **Actions** column. On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure** in the **Port/Health Check/Backend Server** column. On the **Instance Management** page, find the SLB instance that you want to manage and click the instance ID in the **Instance ID/Name** column or **Manage** in the **Actions** column. On the instance management details page, click the **Listeners** tab. On the Listeners tab, click **Add Listener**.

**Step 2: Configure a listener**

In the **Protocol & Listener** step, configure the parameters that are described in the following table and click **Next**.

| Parameter | Description |
|---|---|
| Listener Protocol | The listener protocol. In this example, TCP is selected. |
| Listening Port | The listener port that is used to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| Advanced Settings |   |
| Scheduling Algorithm | The scheduling algorithm. Valid values: Weighted Round-robin (WRR): Backend servers with higher weights receive more requests than backend servers with lower weights. Round Robin: Requests are distributed to backend servers in sequence. Consistent Hashing: Only TCP and UDP listeners support consistent hashing. Hash Factor: You can set this parameter to Source IP Address or Four-element. Source IP Address: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. Four-element: specifies consistent hashing that is based on the following factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Note Only high-performance SLB instances support consistent hashing. |

| Session Persistence | Specifies whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from the same client to the same backend server. For TCP listeners, session persistence is implemented based on IP addresses. Requests from the same IP address are forwarded to the same backend server. |
|---|---|
| Session Persistence Timeout | The timeout period of session persistence. Valid values: 1 to 36000. Unit: seconds. Note This parameter is required only if you turn on Session Persistence. |
| Enable Connection Draining | Specifies whether to enable connection draining. By default, connection draining is disabled. After connection draining is enabled, connections to backend servers remain open within the specified period of time even if the backend servers are removed or fail health checks. |
| Connection Draining Timeout Period | The timeout period of connection draining. Value values: 10 to 900. Unit: seconds. Note This parameter is required only if you turn on Enable Connection Draining. |
| Bandwidth Throttling | Specifies whether to set the maximum bandwidth for the listener. By default, bandwidth throttling is disabled. For a pay-by-bandwidth SLB instance, you can set different maximum bandwidth values for different listeners. This limits the amount of traffic that can be forwarded by each listener. The sum of the maximum bandwidth of all listeners that are added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. All listeners share the bandwidth of the SLB instance. |
| Maximum Bandwidth | The maximum bandwidth. Valid values: 0 to 1000. Unit: Mbit/s. Note This parameter is required only if you turn on Bandwidth Throttling. |
| Connection Timeout | The timeout period of a TCP connection. Value values: 10 to 900. Unit: seconds. |

| Client IP Address Preservation | Specifies whether to obtain client IP addresses. By default, this feature is enabled. Backend servers associated with Layer 4 listeners can obtain client IP addresses without additional configurations. |
|---|---|
| Use Proxy Protocol to Pass Client IP Addresses to Backend Servers | Specifies whether to use Proxy Protocol to pass source client IP addresses to backend servers. By default, this feature is disabled. |
| Automatically Enable Listener | Specifies whether to immediately enable the listener after it is added. By default, listeners are enabled after they are added. |

**Step 3: Add backend servers**

In the **Backend Servers** step, add backend servers to process requests received by the SLB instance and click **Next**. The primary/secondary vServer group feature is provided for Layer 4 SLB listeners and disabled by default. If you need to use the primary/secondary vServer group feature, contact Apsara Stack technical support to enable this feature.
**Enable Primary/Secondary Failover**: specifies whether to enable the primary/secondary
failover feature. If the primary/secondary vServer group feature is enabled, you must turn on this switch. If you turn on Enable Primary/Secondary Failover, configure a primary/secondary vServer group for the listener. For more information, see Primary/secondary vServer groups. If the primary/secondary vServer group feature is disabled or is enabled but Enable Primary/Secondary Failover is turned off, perform the following operations to configure backend servers for the listener. For more information, see Backend server overview. Configure the **Server Group Type** parameter to process requests forwarded by SLB.
**vServer Groups**: If you set the Server Group Type parameter to vServer Groups, select
an existing vServer group from the **Server Group** drop-down list. You can also select **Create vServer Group** from the Server Group drop-down list to create a vServer group and select backend servers. For more information, see Create a vServer group.
**Default Server Group**: If you set the Server Group Type parameter to Default Server
Group, use the default server group configured for the SLB instance. If servers are added to the default server group, you must configure the server ports and weights that are used to receive requests in the **Port** and **Weight** columns. You can also add servers to the default server group and configure the server ports and weights. For more information, see Add a backend server. Valid values of the Port parameter are 1 to 65535. You can specify the same port for different backend servers that are added to the same SLB instance.
**Primary/Secondary Server Groups**: If you set the Server Group Type parameter to
Primary/Secondary Server Groups, select an existing primary/secondary server group from the **Server Group** drop-down list. You can also select **Create Primary/Secondary Server Group** from the Server Group drop-down list to create a primary/secondary server group and select backend servers. For more information, see Create a primary/secondary server group.

**Step 4: Configure health checks**

The health check feature cannot be disabled for a listener that is associated with a primary/secondary server group. In the **Health Check** step, configure health checks and click **Next**.
1. Turn on **Health Check**. By default, Health Check is turned on. This switch cannot be turned
off.
2. Optional. Click **Modify** next to **Advanced Settings** to modify the advanced configurations
of the health check feature. For more information, see Configure health checks.

**Step 5: Submit the configurations**

Perform the following steps to submit the configurations:
1. In the **Confirm Configurations** step, check the configurations in the Listeners, Health
Check, and Backend Servers sections. You can click **Modify** in the **Listeners**, Health Check, and Backend Servers sections or click **Previous** to modify the configurations.
2. Confirm the configurations and click **Submit**.
3. In the **SLB Configuration Wizard** message, wait until the configurations are complete and
click **OK**.

**What to do next**

After listeners are configured, you can view the information about the listeners on the Listeners tab and perform the following operations:

**View the details of a listener**

1. On the Listeners tab, find the listener that you want to view and click the listener name in
the **Listener Name** column.
2. In the Listener Details dialog box, view the details of the listener and manage the listener.
i. In the **Basic Information** section, you can modify the basic information of the listener and configure access control. ii. iii. In the **Server Group** section, you can modify the configurations of the backend server group and backend servers. iv. In the **Health Check** section, you can modify the health check configurations.

**View abnormal backend servers**

1. On the Listeners tab, find the listener that you want to manage and click **Abnormal** in the
**Health Status** column. In the **Unhealthy Backend Servers** message, view the list of
abnormal backend servers.
2. In the **Unhealthy Backend Servers** message, click an instance name to view the
information about the instance that is added as a backend server.

**Modify the configurations of a backend server group**

On the Listeners tab, find the listener that you want to manage and click the name of the backend server group in the **Server Group** column to modify the configurations of the backend server group. The configurations of default server group cannot be modified.

**Modify the configurations of a listener**

When a listener is in the Enabling or Disabling state, the listener cannot be modified or removed. If a listener is already associated with a server group, you cannot associate the listener with the default server group.
1. On the Listeners tab, find the listener that you want to manage and click **Modify Listener**
in the **Actions** column.
2. On the **Configure Listener** page, refer to the preceding configuration steps to check and
modify the configurations and click **Next** until you submit the modified configurations.

**Change the states of listeners**

**Warning**

After a listener is disabled, the listener stops forwarding requests. This may cause service interruptions. Proceed with caution.
1. Change the state of a single listener: On the Listeners tab, find the listener that you want to
manage and click **Enable** or **Disable** in the **Actions** column. Change the states of multiple listeners at a time: On the Listeners tab, select the listeners that you want to manage and click **Enable** or **Disable** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Remove listeners**

1. Remove a single listener: On the Listeners tab, find the listener that you want to remove,
move the pointer over the icon in the **Actions** column, and then select **Delete**. Remove multiple listeners at a time: On the Listeners tab, select the listeners that you want to remove and click **Delete** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Configure access control**

You can configure access control for each listener of an SLB instance. Enabling access control may bring business risks. If a whitelist is configured for a listener, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If a blacklist is configured for a listener, all requests from the IP addresses that are added to the blacklist are blocked by the listener. If you enable a whitelist or blacklist but do not add an IP address to the whitelist or blacklist, all requests are forwarded.
1. On the Listeners tab, find the listener that you want to manage, move the pointer over the
icon in the **Actions** column, and then select **Configure Access Control**. You can also click **Configure** in the **Access Control** column.
2. In the **Configure Access Control** panel, configure the parameters that are described in
the following table and click **OK**.

| Parameter | Description |
|---|---|
| Access Control | Specifies whether to enable access control. If you do not need to configure access control, turn off Access Control. |
| Access Control Mode | The access control method. This parameter is required only if you turn on Access Control. Valid values: Whitelist: Allows Access from Specified IP Addresses: Only requests from the IP addresses or CIDR blocks specified in the access control list (ACL) are forwarded. You can use a whitelist in scenarios where you want to allow access only from specific IP addresses to an application. Blacklist: Block specific IP addresses from accessing the IP address of the SLB instance.: Requests from the IP addresses or CIDR blocks specified in the ACL are denied. You can use a blacklist in scenarios where you want to deny access only from specific IP addresses to an application. |
| Select ACL | The ACL to use. This parameter is required only if you turn on Access Control. |

###### 4.2.3.2.2 Add a UDP listener

UDP is ideal for services that prioritize real-time content delivery over reliability, such as video conferencing and real-time quote services. You can add a UDP listener to forward UDP requests.

**Background information**

Before you configure a UDP listener, take note of the following limits: You cannot specify ports 250, 4789, or 4790 for UDP listeners. They are system reserved ports. Fragmentation is not supported. If you add a UDP listener to a Server Load Balancer (SLB) instance deployed in a classic network, the UDP listener cannot pass client IP addresses to backend servers. The following operations take effect 5 minutes after they are performed on a UDP listener: Remove backend servers. Set the weight of a backend server to 0 after it is declared unhealthy.

**Step 1: Open the listener configuration wizard**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **SLB Configuration Wizard** page:
On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure Listener** in the **Actions** column. On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure** in the **Port/Health Check/Backend Server** column. On the **Instance Management** page, find the SLB instance that you want to manage and click the instance ID in the **Instance ID/Name** column or **Manage** in the **Actions** column. On the instance management details page, click the **Listeners** tab. On the Listeners tab, click **Add Listener**.

**Step 2: Configure a listener**

On the **Protocol & Listener** wizard page, configure parameters as described in the following table. Click **Next**.

| Parameter | Description |
|---|---|
| Select Listener Protocol | Select a listener protocol. In this example, UDP is selected. |
| Listener Port | Specify the listener port to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| Advanced Settings |   |

| Scheduling Algorithm | SLB supports the following scheduling algorithms: Weighted Round-robin (WRR): Backend servers with higher weights receive more requests than backend servers with lower weights. Round Robin (RR): Requests are distributed to backend servers in sequence. Consistent Hashing (CH): Only TCP and UDP listeners support consistent hashing. Hash Factor: You can select Source IP or Four-element. Source IP: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. Four-element: specifies consistent hashing that is based on four factors: the source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server. Note Only high-performance SLB instances support the consistent hashing algorithm. |
|---|---|
| Session Persistence | Specify whether to enable session persistence. SLB maintains the persistence of UDP sessions by using consistent hashing that is based on source IP addresses. You can enable session persistence only when you set Scheduling Algorithm to Consistent Hashing (CH) and set Hash Factor to Source IP. |
| Connection Draining | Specify whether to enable connection draining. By default, connection draining is disabled. After connection draining is enabled, connections to backend servers remain open during the specified timeout period even if the backend servers are removed or fail health checks. |
| Connection Draining Timeout Period | The timeout period for connection draining. Value values: 10 to 900. Unit: seconds. Note To enable connection draining, you must specify a timeout period. |
| Bandwidth Throttling for Listeners | Specify whether to specify a maximum bandwidth for the listener. By default, no maximum bandwidth is specified for a listener. If a pay-by-bandwidth SLB instance is used, you can set a maximum bandwidth for each listener to limit the amount of network traffic forwarded by listeners. The sum of the maximum bandwidth of all listeners that are added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. By default, all listeners share the bandwidth of the SLB instance. |

| Maximum Bandwidth | Specify the maximum bandwidth. Valid values: 0 to 1000. Unit: Mbit/s. Note You must specify the maximum bandwidth if you enable bandwidth throttling for the listener. |
|---|---|
| Connection Timeout Period | Specify a timeout period for a TCP connection. Value values: 10 to 900. Unit: seconds. |
| Obtain Client Source IP Address | By default, this feature is enabled. Backend servers associated with UDP listeners can preserve client IP addresses without additional configurations. Note If you add a UDP listener to an SLB instance deployed in a classic network, the UDP listener cannot pass client IP addresses to backend servers. |
| Use the Proxy protocol to pass client IP addresses to backend servers | Specify whether to use the Proxy protocol to pass source client IP addresses to backend servers. By default, this feature is disabled. |
| Automatically Enable Listener | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. |

**Step 3: Add backend servers**

In the **Backend Servers** step, add backend servers to process requests received by the SLB instance and click **Next**. The primary/secondary vServer group feature is provided for Layer 4 SLB listeners and disabled by default. If you need to use the primary/secondary vServer group feature, contact Apsara Stack technical support to enable this feature.
**Enable Primary/Secondary Failover**: specifies whether to enable the primary/secondary
failover feature. If the primary/secondary vServer group feature is enabled, you must turn on this switch. If you turn on Enable Primary/Secondary Failover, configure a primary/secondary vServer group for the listener. For more information, see Primary/secondary vServer groups. If the primary/secondary vServer group feature is disabled or is enabled but Enable Primary/Secondary Failover is turned off, perform the following operations to configure backend servers for the listener. For more information, see Backend server overview. Configure the **Server Group Type** parameter to process requests forwarded by SLB.
**vServer Groups**: If you set the Server Group Type parameter to vServer Groups, select
an existing vServer group from the **Server Group** drop-down list. You can also select **Create vServer Group** from the Server Group drop-down list to create a vServer group and select backend servers. For more information, see Create a vServer group.
**Default Server Group**: If you set the Server Group Type parameter to Default Server
Group, use the default server group configured for the SLB instance. If servers are added to the default server group, you must configure the server ports and weights that are used to receive requests in the **Port** and **Weight** columns. You can also add servers to the default server group and configure the server ports and weights. For more information, see Add a backend server. Valid values of the Port parameter are 1 to 65535. You can specify the same port for different backend servers that are added to the same SLB instance.
**Primary/Secondary Server Groups**: If you set the Server Group Type parameter to
Primary/Secondary Server Groups, select an existing primary/secondary server group from the **Server Group** drop-down list. You can also select **Create Primary/Secondary Server Group** from the Server Group drop-down list to create a primary/secondary server group and select backend servers. For more information, see Create a primary/secondary server group.

**Step 4: Configure health checks**

The health check feature cannot be disabled for a listener that is associated with a primary/secondary server group. In the **Health Check** step, configure health checks and click **Next**.
1. Turn on **Health Check**. By default, Health Check is turned on. This switch cannot be turned
off.
2. Optional. Click **Modify** next to **Advanced Settings** to modify the advanced configurations
of the health check feature. For more information, see Configure health checks.

**Step 5: Submit the configurations**

Perform the following steps to submit the configurations:
1. In the **Confirm Configurations** step, check the configurations in the Listeners, Health
Check, and Backend Servers sections. You can click **Modify** in the **Listeners**, Health Check, and Backend Servers sections or click **Previous** to modify the configurations.
2. Confirm the configurations and click **Submit**.
3. In the **SLB Configuration Wizard** message, wait until the configurations are complete and
click **OK**.

**What to do next**

After listeners are configured, you can view the information about the listeners on the Listeners tab and perform the following operations:

**View the details of a listener**

1. On the Listeners tab, find the listener that you want to view and click the listener name in
the **Listener Name** column.
2. In the Listener Details dialog box, view the details of the listener and manage the listener.
i. In the **Basic Information** section, you can modify the basic information of the listener and configure access control. ii. iii. In the **Server Group** section, you can modify the configurations of the backend server group and backend servers. iv. In the **Health Check** section, you can modify the health check configurations.

**View abnormal backend servers**

1. On the Listeners tab, find the listener that you want to manage and click **Abnormal** in the
**Health Status** column. In the **Unhealthy Backend Servers** message, view the list of
abnormal backend servers.
2. In the **Unhealthy Backend Servers** message, click an instance name to view the
information about the instance that is added as a backend server.

**Modify the configurations of a backend server group**

On the Listeners tab, find the listener that you want to manage and click the name of the backend server group in the **Server Group** column to modify the configurations of the backend server group. The configurations of default server group cannot be modified.

**Modify the configurations of a listener**

When a listener is in the Enabling or Disabling state, the listener cannot be modified or removed. If a listener is already associated with a server group, you cannot associate the listener with the default server group.
1. On the Listeners tab, find the listener that you want to manage and click **Modify Listener**
in the **Actions** column.
2. On the **Configure Listener** page, refer to the preceding configuration steps to check and
modify the configurations and click **Next** until you submit the modified configurations.

**Change the states of listeners**

**Warning**

After a listener is disabled, the listener stops forwarding requests. This may cause service interruptions. Proceed with caution.
1. Change the state of a single listener: On the Listeners tab, find the listener that you want to
manage and click **Enable** or **Disable** in the **Actions** column. Change the states of multiple listeners at a time: On the Listeners tab, select the listeners that you want to manage and click **Enable** or **Disable** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Remove listeners**

1. Remove a single listener: On the Listeners tab, find the listener that you want to remove,
move the pointer over the icon in the **Actions** column, and then select **Delete**. Remove multiple listeners at a time: On the Listeners tab, select the listeners that you want to remove and click **Delete** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Configure access control**

You can configure access control for each listener of an SLB instance. Enabling access control may bring business risks. If a whitelist is configured for a listener, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If a blacklist is configured for a listener, all requests from the IP addresses that are added to the blacklist are blocked by the listener. If you enable a whitelist or blacklist but do not add an IP address to the whitelist or blacklist, all requests are forwarded.
1. On the Listeners tab, find the listener that you want to manage, move the pointer over the
icon in the **Actions** column, and then select **Configure Access Control**. You can also click **Configure** in the **Access Control** column.
2. In the **Configure Access Control** panel, configure the parameters that are described in
the following table and click **OK**.

| Parameter | Description |
|---|---|
| Access Control | Specifies whether to enable access control. If you do not need to configure access control, turn off Access Control. |
| Access Control Mode | The access control method. This parameter is required only if you turn on Access Control. Valid values: Whitelist: Allows Access from Specified IP Addresses: Only requests from the IP addresses or CIDR blocks specified in the access control list (ACL) are forwarded. You can use a whitelist in scenarios where you want to allow access only from specific IP addresses to an application. Blacklist: Block specific IP addresses from accessing the IP address of the SLB instance.: Requests from the IP addresses or CIDR blocks specified in the ACL are denied. You can use a blacklist in scenarios where you want to deny access only from specific IP addresses to an application. |
| Select ACL | The ACL to use. This parameter is required only if you turn on Access Control. |

###### 4.2.3.2.3 Add an HTTP listener

HTTP is ideal for applications that need to identify data content, such as web applications and mobile games. You can add HTTP listeners to forward HTTP requests.

**Step 1: Open the listener configuration wizard**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **SLB Configuration Wizard** page:
On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure Listener** in the **Actions** column. On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure** in the **Port/Health Check/Backend Server** column. On the **Instance Management** page, find the SLB instance that you want to manage and click the instance ID in the **Instance ID/Name** column or **Manage** in the **Actions** column. On the instance management details page, click the **Listeners** tab. On the Listeners tab, click **Add Listener**.

**Step 2: Configure a listener**

On the **Protocol & Listener** wizard page, configure parameters as described in the following table. Click **Next**.

| Parameter | Description |
|---|---|
| Select Listener Protocol | Select a listener protocol. In this example, HTTP is selected. |
| Listener Port | Specify the listener port to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| Advanced Settings |   |
| Scheduling Algorithm | SLB supports the following scheduling algorithms: Weighted Round-robin (WRR): Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round Robin (RR): Requests are distributed to backend servers in sequence. |
| Redirection by Listener | Specifies whether to redirect traffic from the HTTP listener to an HTTPS listener. After you enable this feature, HTTP requests received on port 80 are redirected to port 443 that uses HTTPS. |

| Listener | Select the HTTPS listener to receive redirected HTTP requests. Note If you want Redirection by Listener to take effect, you must set Listener. |
|---|---|
| Session Persistence | Specify whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from a client to the same backend server. Note If you disable Redirection by Listener, you must enable this feature. |
| Cookie Option | SLB persists HTTP sessions based on cookies. SLB allows you to use the following methods to process cookies: Insert Cookie: If you select this option, you only need to specify the timeout period for the cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. Rewrite Cookie: If you select this option, you can specify the cookie that you want to insert into an HTTP or HTTPS response. You must specify the timeout period and the lifetime for a cookie on a backend server. After you specify a cookie, SLB overwrites the original cookie with the specified cookie. The next time SLB receives a client request that carries the specified cookie, the listener distributes the request to the recorded backend server. Note To enable session persistence, you must specify Cookie Option. |
| Session Persistence Timeout Period | Set the session persistence timeout period. Valid values: 1 to 86400. Unit: seconds. Note To enable session persistence, you must specify the session persistence timeout period. |

| Bandwidth Throttling for Listener | Specify whether to set a maximum bandwidth for the listener. By default, this feature is disabled. If a pay-by-bandwidth SLB instance is used, you can set the maximum bandwidth of each listener to limit the amount of network traffic that can be forwarded by listeners. The sum of the maximum bandwidth of all listeners that are added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. All listeners share the bandwidth of the SLB instance. Note If you disable Redirection by Listener, you must enable this feature. |
|---|---|
| Maximum Bandwidth | Set a maximum bandwidth. Valid values: 0 to 1000. Unit: Mbit/s. Note You must specify a maximum bandwidth to enable Bandwidth Throttling for Listener. |
| Idle Connection Timeout Period | Specify the timeout period for idle connections. Unit: seconds. Valid values: 1 to 60. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. Note If you disable Redirection by Listener, you must enable this feature. |
| Connection Request Timeout | Specify a timeout period for connection requests. Unit: seconds. Valid values: 1 to 900. If no response is received from a backend server within the specified timeout period, SLB returns the HTTP 504 status code to the client. Important If you enable this feature and set the connection request timeout period to 900 seconds, pay attention to alerts. Valid values: 1 to 180. If you set the connection request timeout period to 900 seconds, the number of monitoring connections of SLB cannot exceed 100,000. You must connect to the monitoring system of Apsara Infrastructure Management or Network Operations Console in the Apsara Uni-manager Operations Console. Note If you disable Redirection by Listener, you must enable this feature. |

| Gzip Compression | Specify whether to enable GZIP compression to compress specific types of files. GZIP supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. Note If you disable Redirection by Listener, you must enable this feature. |
|---|---|
| Custom HTTP Header | You can select the following options: Insert X-Forwarded-For to retrieve client IP addresses Insert SLB-ID to retrieve SLB instance IDs Insert SLB-IP to retrieve SLB instance IP addresses Insert X-Forwarded-Proto to retrieve the SLB listener protocol Note If you disable Redirection by Listener, you must enable this feature. |
| Obtain Client Source IP Address | By default, this feature is enabled. Preserve the real IP address of the client that sends the request. Note If you disable Redirection by Listener, you must enable this feature. |
| Automatically Enable Listener | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. Note If you disable Redirection by Listener, you must enable this feature. |

**Step 3: Add backend servers**

On the **Backend Servers** wizard page, add backend servers to process requests forwarded by SLB and click **Next**.

**Important**

HTTP listeners do not support primary/secondary server groups. Set **Server Group Type** to process requests forwarded by SLB, and configure parameters as described in the following table.
**vServer Groups**: If you set the Server Group Type parameter to vServer Groups, select an
existing vServer group from the **Server Group** drop-down list. You can also select **Create vServer Group** from the Server Group drop-down list to create a vServer group and select backend servers. For more information, see Create a vServer group.
**Default Server Group**: If you set the Server Group Type parameter to Default Server
Group, use the default server group configured for the SLB instance. If servers are added to the default server group, you must configure the server ports and weights that are used to receive requests in the **Port** and **Weight** columns. You can also add servers to the default server group and configure the server ports and weights. For more information, see Add a backend server. Valid values of the Port parameter are 1 to 65535. You can specify the same port for different backend servers that are added to the same SLB instance.

**Step 4: Configure health checks**

On the **Health Check** wizard page, configure health checks and click **Next**.
1. **Health Check**: By default, health checks are enabled. You can disable this feature.
2. Optional. If health checks are enabled, click **Modify** next to **Advanced Settings** to modify
the advanced configuration of the health checks. For more information, see Configure health checks.

**Step 5: Submit the configurations**

Perform the following steps to submit the configurations:
1. In the **Confirm Configurations** step, check the configurations in the Listeners, Health
Check, and Backend Servers sections. You can click **Modify** in the **Listeners**, Health Check, and Backend Servers sections or click **Previous** to modify the configurations.
2. Confirm the configurations and click **Submit**.
3. In the **SLB Configuration Wizard** message, wait until the configurations are complete and
click **OK**.

**What to do next**

After listeners are configured, you can view the information about the listeners on the Listeners tab and perform the following operations:

**View the details of a listener**

1. On the Listeners tab, find the listener that you want to view and click the listener name in
the **Listener Name** column.
2. In the Listener Details dialog box, view the details of the listener and manage the listener.
i. In the upper-right corner, you can click **Manage Forwarding Rules** to configure forwarding rules. ii. In the **Basic Information** section, you can modify the basic information of the listener and configure access control. iii. In the **Server Group** section, you can modify the configurations of the backend server group and backend servers. iv. In the **Health Check** section, you can modify the health check configurations.

**View abnormal backend servers**

1. On the Listeners tab, find the listener that you want to manage and click **Abnormal** in the
**Health Status** column. In the **Unhealthy Backend Servers** message, view the list of
abnormal backend servers.
2. In the **Unhealthy Backend Servers** message, click an instance name to view the
information about the instance that is added as a backend server.

**Modify the configurations of a backend server group**

On the Listeners tab, find the listener that you want to manage and click the name of the backend server group in the **Server Group** column to modify the configurations of the backend server group. The configurations of default server group cannot be modified.

**Modify the configurations of a listener**

When a listener is in the Enabling or Disabling state, the listener cannot be modified or removed. If a listener is already associated with a server group, you cannot associate the listener with the default server group.
1. On the Listeners tab, find the listener that you want to manage and click **Modify Listener**
in the **Actions** column.
2. On the **Configure Listener** page, refer to the preceding configuration steps to check and
modify the configurations and click **Next** until you submit the modified configurations.

**Change the states of listeners**

**Warning**

After a listener is disabled, the listener stops forwarding requests. This may cause service interruptions. Proceed with caution.
1. Change the state of a single listener: On the Listeners tab, find the listener that you want to
manage and click **Enable** or **Disable** in the **Actions** column. Change the states of multiple listeners at a time: On the Listeners tab, select the listeners that you want to manage and click **Enable** or **Disable** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Remove listeners**

1. Remove a single listener: On the Listeners tab, find the listener that you want to remove,
move the pointer over the icon in the **Actions** column, and then select **Delete**. Remove multiple listeners at a time: On the Listeners tab, select the listeners that you want to remove and click **Delete** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Configure access control**

You can configure access control for each listener of an SLB instance. Enabling access control may bring business risks. If a whitelist is configured for a listener, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If a blacklist is configured for a listener, all requests from the IP addresses that are added to the blacklist are blocked by the listener. If you enable a whitelist or blacklist but do not add an IP address to the whitelist or blacklist, all requests are forwarded.
1. On the Listeners tab, find the listener that you want to manage, move the pointer over the
icon in the **Actions** column, and then select **Configure Access Control**. You can also click **Configure** in the **Access Control** column.
2. In the **Configure Access Control** panel, configure the parameters that are described in
the following table and click **OK**.

| Parameter | Description |
|---|---|
| Access Control | Specifies whether to enable access control. If you do not need to configure access control, turn off Access Control. |
| Access Control Mode | The access control method. This parameter is required only if you turn on Access Control. Valid values: Whitelist: Allows Access from Specified IP Addresses: Only requests from the IP addresses or CIDR blocks specified in the access control list (ACL) are forwarded. You can use a whitelist in scenarios where you want to allow access only from specific IP addresses to an application. Blacklist: Block specific IP addresses from accessing the IP address of the SLB instance.: Requests from the IP addresses or CIDR blocks specified in the ACL are denied. You can use a blacklist in scenarios where you want to deny access only from specific IP addresses to an application. |
| Select ACL | The ACL to use. This parameter is required only if you turn on Access Control. |

###### 4.2.3.2.4 Add an HTTPS listener

This topic describes how to add an HTTPS listener to a Server Load Balancer (SLB) instance. HTTPS is intended for applications that require encrypted data transmission. You can add an HTTPS listener to forward HTTPS requests.

**Step 1: Open the listener configuration wizard**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **SLB Configuration Wizard** page:
On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure Listener** in the **Actions** column. On the **Instance Management** page, find the SLB instance that you want to manage and click **Configure** in the **Port/Health Check/Backend Server** column. On the **Instance Management** page, find the SLB instance that you want to manage and click the instance ID in the **Instance ID/Name** column or **Manage** in the **Actions** column. On the instance management details page, click the **Listeners** tab. On the Listeners tab, click **Add Listener**.

**Step 2: Configure a listener**

On the **Protocol & Listener** wizard page, configure parameters as described in the following table. Click **Next**.

| Parameter | Description |
|---|---|
| Listener Protocol | Select a listener protocol. In this example, HTTPS is selected. |
| Listening Port | Specify the listener port to receive and forward requests to backend servers. Valid values: 1 to 65535. |
| Advanced Settings |   |
| Scheduling Algorithm | SLB supports the following scheduling algorithms: Weighted Round Robin: Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round Robin: Requests are distributed to backend servers in sequence. |
| Session Persistence | Specify whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from the same client to the same backend server. |

| Cookie Persistence | SLB persists HTTP sessions based on cookies. SLB allows you to use the following methods to process cookies: Insert Cookie: If you select this option, you only need to specify the timeout period for the cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. Rewrite Cookie: If you select this option, you can specify the cookie that you want to insert into an HTTP or HTTPS response. You must specify the timeout period and the lifetime for a cookie on a backend server. After you specify a cookie, SLB overwrites the original cookie with the specified cookie. The next time SLB receives a client request that contains the specified cookie, the listener distributes the request to the recorded backend server. Note To enable session persistence, you must specify Cookie Persistence. |
|---|---|
| Session Persistence Timeout | Set the timeout period for session persistence. Valid values: 1 to 86400. Unit: seconds. Note To enable session persistence, you must specify the session persistence timeout period. |
| HTTP/2 | Specify whether to enable HTTP/2.0 for the frontend protocol of the SLB instance. |
| Bandwidth Throttling for Listeners | Specify whether to specify a maximum bandwidth for the listener. By default, this feature is disabled. If a pay-by-bandwidth SLB instance is used, you can set the maximum bandwidth of each listener to limit the amount of network traffic forwarded by listeners. The sum of the maximum bandwidth of all listeners that are added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. All listeners share the bandwidth of the SLB instance. |
| Maximum Bandwidth | Specify the maximum bandwidth for the SLB instance. Valid values: 0 to 1000. Unit: Mbit/s. Note To enable bandwidth throttling for the listener, you must specify a maximum bandwidth. |

| Idle Connection Timeout | Specify a timeout period for idle connections. Valid values: 1 to 60. Unit: seconds. If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB establishes a new connection. |
|---|---|
| Connection Request Timeout | Specify a timeout period for connection requests. Unit: seconds. Valid values: 1 to 900. If no response is received from the backend server within the request timeout period, SLB returns the HTTP 504 error code to the client. Important If you enable this feature and set the connection request timeout period to 900 seconds, pay attention to alerts. Valid values: 1 to 180. Unit: seconds. If you set the connection request timeout period to 900 seconds, the number of monitoring connections of SLB cannot exceed 100,000. You must connect to the monitoring system of Apsara Infrastructure Management or Network Operations Console in the Apsara Uni- manager Operations Console. |
| Gzip Compression | Specify whether to enable GZIP compression to compress specific types of files. GZIP supports the following file types: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, and application/xml. |
| Custom HTTP Headers | You can select the following options: Use the X-Forwarded-For header to retrieve client IP addresses. Use the SLB-ID header to retrieve the ID of the SLB instance. Use the SLB-IP header to retrieve the public IP address of the SLB instance. Use the X-Forwarded-Proto header to retrieve the listener protocol. |
| Client IP Address Preservation | By default, this feature is enabled. Obtain the real IP address of the client that sends the request. |
| Automatically Enable Listener | Specify whether to immediately enable the listener after it is created. By default, listeners are enabled after they are created. |

**Step 3: Configure an SSL certificate**

On the **SSL Certificates** wizard page, configure an SSL certificate to ensure that data transmission is encrypted and the identities of users are verified by a trusted authority. Click
**Next**.
1. Select the **Server Certificate**.
You can also select **Create Server Certificate** or click **Create Server Certificate** to create and select a server certificate. For detailed operations, see Uploaded certificates.
2. (Optional) To enable HTTPS mutual authentication or configure a TLS security policy, click
**Modify** on the right side of **Advanced Settings**.
**Mutual Authentication**: You must select a **CA Certificate** if you enable mutual
authentication. You can also select **Create CA Certificate** or click **Create CA Certificate** to create and select a CA certificate.
**TLS Security Policy**: A TLS security policy contains TLS protocol versions and cipher
suites that are available for HTTPS. The following security policies are supported:

**tls_cipher_policy_1_0**

**tls_cipher_policy_1_1**

**tls_cipher_policy_1_2**

**tls_cipher_policy_1_2_strict**

**tls_cipher_policy_1_2_without_sha1**

**tls_cipher_policy_1_2_strict_with_1_3**

Before you upload a certificate, take note of the following items: SLB supports the following public key algorithms: RSA 1024, RSA 2048, RSA 4096, ECDSA P-256, ECDSA P-384, and ECDSA P-521. The format of the certificate must be NGINX. After you upload a certificate to SLB, SLB can manage the certificate. You do not need to associate the certificate with backend servers. It may take a few minutes to upload, load, and verify the certificate. Therefore, an HTTPS listener is not available immediately after it is created. It requires about 1 to 3 minutes to enable an HTTPS listener. The Elliptic-curve Diffie–Hellman (ECDH) cipher suite used by HTTPS listeners supports perfect forward secrecy (PFS). You cannot upload security hardening parameters required by ECDH as a file. In other words, you cannot specify the petameters as a string in `BEGIN DH PARAMETERS` . HTTPS listeners do not support Server Name Indication (SNI). You can choose TCP listeners and configure SNI on backend servers. By default, the timeout period of session tickets for HTTPS listeners is 300 seconds. The actual amount of data transfer on an HTTPS listener is greater than the billed amount because a portion of data is used for handshaking. Therefore, the amount of data transfer greatly increases when a large number of connections are established.

**Step 4: Add backend servers**

On the **Backend Servers** wizard page, add backend servers to process requests received by the SLB instance and click **Next**. Set **Server Group Type** to process requests forwarded by SLB, and configure parameters as described in the following table.
**vServer Groups**: If you set the Server Group Type parameter to vServer Groups, select an
existing vServer group from the **Server Group** drop-down list. You can also select **Create vServer Group** from the Server Group drop-down list to create a vServer group and select backend servers. For more information, see Create a vServer group.
**Default Server Group**: If you set the Server Group Type parameter to Default Server
Group, use the default server group configured for the SLB instance. If servers are added to the default server group, you must configure the server ports and weights that are used to receive requests in the **Port** and **Weight** columns. You can also add servers to the default server group and configure the server ports and weights. For more information, see Add a backend server. Valid values of the Port parameter are 1 to 65535. You can specify the same port for different backend servers that are added to the same SLB instance.

**Step 5: Configure health checks**

On the **Health Check** wizard page, configure health checks and click **Next**.
1. **Health Check**: By default, health checks are enabled. You can disable this feature.
2. Optional. If health checks are enabled, click **Modify** next to **Advanced Settings** to modify
the advanced configuration of the health checks. For more information, see Configure health checks.

**Step 6: Confirm the configurations**

Perform the following steps to submit the configurations:
1. In the **Confirm Configurations** step, check the configurations in the Listeners, Health
Check, and Backend Servers sections. You can click **Modify** in the **Listeners**, Health Check, and Backend Servers sections or click **Previous** to modify the configurations.
2. Confirm the configurations and click **Submit**.
3. In the **SLB Configuration Wizard** message, wait until the configurations are complete and
click **OK**.

**What to do next**

After listeners are configured, you can view the information about the listeners on the Listeners tab and perform the following operations:

**View the details of a listener**

1. On the Listeners tab, find the listener that you want to view and click the listener name in
the **Listener Name** column.
2. In the Listener Details dialog box, view the details of the listener and manage the listener.
i. In the **Basic Information** section, you can modify the basic information of the listener and configure access control. ii. iii. In the **Server Group** section, you can modify the configurations of the backend server group and backend servers. iv. In the **Health Check** section, you can modify the health check configurations.

**View abnormal backend servers**

1. On the Listeners tab, find the listener that you want to manage and click **Abnormal** in the
**Health Status** column. In the **Unhealthy Backend Servers** message, view the list of
abnormal backend servers.
2. In the **Unhealthy Backend Servers** message, click an instance name to view the
information about the instance that is added as a backend server.

**Modify the configurations of a backend server group**

On the Listeners tab, find the listener that you want to manage and click the name of the backend server group in the **Server Group** column to modify the configurations of the backend server group. The configurations of default server group cannot be modified.

**Modify the configurations of a listener**

When a listener is in the Enabling or Disabling state, the listener cannot be modified or removed. If a listener is already associated with a server group, you cannot associate the listener with the default server group.
1. On the Listeners tab, find the listener that you want to manage and click **Modify Listener**
in the **Actions** column.
2. On the **Configure Listener** page, refer to the preceding configuration steps to check and
modify the configurations and click **Next** until you submit the modified configurations.

**Change the states of listeners**

**Warning**

After a listener is disabled, the listener stops forwarding requests. This may cause service interruptions. Proceed with caution.
1. Change the state of a single listener: On the Listeners tab, find the listener that you want to
manage and click **Enable** or **Disable** in the **Actions** column. Change the states of multiple listeners at a time: On the Listeners tab, select the listeners that you want to manage and click **Enable** or **Disable** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Remove listeners**

1. Remove a single listener: On the Listeners tab, find the listener that you want to remove,
move the pointer over the icon in the **Actions** column, and then select **Delete**. Remove multiple listeners at a time: On the Listeners tab, select the listeners that you want to remove and click **Delete** in the lower-left corner.
2. In the **Confirm** message, click **OK**.

**Configure access control**

You can configure access control for each listener of an SLB instance. Enabling access control may bring business risks. If a whitelist is configured for a listener, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If a blacklist is configured for a listener, all requests from the IP addresses that are added to the blacklist are blocked by the listener. If you enable a whitelist or blacklist but do not add an IP address to the whitelist or blacklist, all requests are forwarded.
1. On the Listeners tab, find the listener that you want to manage, move the pointer over the
icon in the **Actions** column, and then select **Configure Access Control**. You can also click **Configure** in the **Access Control** column.
2. In the **Configure Access Control** panel, configure the parameters that are described in
the following table and click **OK**.

| Parameter | Description |
|---|---|
| Access Control | Specifies whether to enable access control. If you do not need to configure access control, turn off Access Control. |
| Access Control Mode | The access control method. This parameter is required only if you turn on Access Control. Valid values: Whitelist: Allows Access from Specified IP Addresses: Only requests from the IP addresses or CIDR blocks specified in the access control list (ACL) are forwarded. You can use a whitelist in scenarios where you want to allow access only from specific IP addresses to an application. Blacklist: Block specific IP addresses from accessing the IP address of the SLB instance.: Requests from the IP addresses or CIDR blocks specified in the ACL are denied. You can use a blacklist in scenarios where you want to deny access only from specific IP addresses to an application. |
| Select ACL | The ACL to use. This parameter is required only if you turn on Access Control. |

###### 4.2.3.2.5 Configure forwarding rules

This topic describes how to configure forwarding rules for a Server Load Balancer (SLB) instance. You can configure domain name-based or URL-based forwarding rules for an SLB instance that uses Layer 7 listeners. Layer 7 listeners distribute requests destined for different domain names or URLs to different Elastic Compute Service (ECS) instances.

**Background information**

You can add multiple forwarding rules to a listener. Each forwarding rule is associated with a unique server group. Each server group contains one or more ECS instances. For example, you can configure a listener to forward read requests to one server group and write requests to another server group. This allows you to balance the loads of the backend servers. SLB forwards requests based on the following rules: If a request matches a domain name-based or URL-based forwarding rule of a listener, the listener forwards the request to the server group specified in the matching forwarding rule. If a request does not match a domain name-based or URL-based forwarding rule but the listener is associated with a server group, the listener forwards the request to the associated server group. If none of the preceding conditions are met, requests are forwarded to the ECS instances in the default server group of the SLB instance.

**Configure domain name-based or URL-based forwarding rules**

You can configure domain name-based or URL-based forwarding rules only for HTTP and HTTPS listeners.
1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the SLB instance that you want to manage and
click **Manage** in the **Actions** column or the instance ID in the **Instance ID/Name** column.
5. On the instance management details page, click the **Listeners** tab. On the **Listeners** tab,
find the listener that you want to manage and click **Configure Forwarding Rule** in the
**Actions** column.
6. In the **Forwarding Rule** panel, configure the following parameters in the **Add**
**Forwarding Rule** section:
**Domain Name**: the requested domain name.
**URL**: the requested URL.
**vServer Groups**: the vServer group that you want to associate with the forwarding rule.
**Description**: the description.
Naming conventions of domain names: Example of a wildcard domain name: *.test.com. A domain name must start with an asterisk (*) in the *. or *aaa. format, and cannot end with an asterisk (*). Example of a standard domain name: www.test.com. Naming conventions of URLs: A URL must be 2 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & The URL must start with a forward slash (/) and cannot be a forward slash (/). If the URL of a request contains special characters, you must use URL escape codes to convert the special characters. For example, if the URL of a request contains a number sign (#), the number sign must be converted into the escape code (%23). This way, the system can match the URL of the request against URL-based forwarding rules. You must specify at least one of the domain name and URL for each forwarding rule. You can click **Add Domain Name** to add a domain name-based forwarding rule, or click
**Add Rule** to add a URL-based forwarding rule.
Configure a domain name-based forwarding rule When you configure a domain name-based forwarding rule, leave the URL field empty. You do not need to enter a forward slash (/) in this field. The domain name can contain only letters, digits, hyphens (-), and periods (.). If a request matches multiple domain name-based forwarding rules, exact match prevails over wildcard match, as described in the following table. Table 1: Domain name-based forwarding rules

| Match mode | Requested URL | Domain name-based forwarding rule (√ indicates that the domain name is a match, whereas x indicates that the domain name is not a match.) |   |   |
|---|---|---|---|---|
|   |   | www.aliyun.c om | *.aliyun.c om | *.market.aliyun.c om |
| Exact match | www.aliyun.com | ✓ | x | x |
| Wildcard match | market.aliyun.com | x | ✓ | x |
|   | info.market.aliyun.co m | x | x | ✓ |

Configure a URL-based forwarding rule When you configure a URL-based forwarding rule, leave the Domain Name field empty. URL-based forwarding rules support string matching and adopt sequential matching. Examples: `/admin` , `/bbs_` , and `/ino_test` . Configure both domain name-based and URL-based forwarding rules You can configure both domain name-based and URL-based forwarding rules to forward traffic destined for different URLs of the same domain name. We recommend that you configure a default forwarding rule with the URL field left empty in case errors are triggered when the URLs of requests are not matched.

| e whose domain name is | www.example.com |   |
|---|---|---|
| www.example.com/index.html |   |   |
|   |   | to Server Gro |

requests to Server Group 2. To meet the preceding requirements, you must configure two forwarding rules. Otherwise, the HTTP 404 status code is returned if a request destined for the `www.example.com` domain name does not match a forwarding rule. To delete a forwarding rule, find the rule and click **Delete** in the **Actions** column.
7. Click **Add Forwarding Rule**.
If the forwarding rules that you want to configure lack the root path, the **Confirm** message appears. You can click **Cancel** to ignore the message. You can also click **OK** to close the message. After you add the root path, click **Add**
**Forwarding Rule** again.

**Modify forwarding rules**

1. On the instance management details page, click the **Listeners** tab. On the **Listeners** tab,
find the listener that you want to manage and click **Configure Forwarding Rule** in the
**Actions** column.
2. In the **Forwarding Rule** panel, find the forwarding rule that you want to modify in the
**Forwarding Rules** section and click **Modify** in the **Actions** column.
3. In the **Modify Forwarding Rule** panel, modify the description or change the vServer
group. You can click **Show Server Groups** to view the list of available virtual servers.
4. Optional. Turn on or off **Advanced Setting** based on your business requirements. If you
turn on this switch, you can configure the parameters that are described in the following table. If Advanced Setting is turned on, you can configure a scheduling algorithm, session persistence, and health checks for the forwarding rule. If Advanced Setting is turned off, the configurations of the listener are used.

| Parameter | Description |
|---|---|
| Scheduling Algorithm | The scheduling algorithm. Valid values: Weighted Round Robin: Backend servers that have higher weights receive more requests than backend servers that have lower weights. Round Robin: Requests are distributed to backend servers in sequence. |

| Session Persistence | Specifies whether to enable session persistence. After session persistence is enabled, SLB forwards all requests from the same client to the same backend server. SLB persists HTTP sessions based on cookies. To enable session persistence, you must configure the following parameters: Cookie Persistence Insert Cookie: If you select this option, you need to only specify the timeout period of a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. Session Persistence Timeout: If you select Insert Cookie as Cookie Persistence, you must specify the timeout period of session persistence. Default value: 1000. Valid values: 1 to 86400. Unit: seconds. Rewrite Cookie: If you select this option, you can specify the cookie that you want to insert into an HTTP or HTTPS response. In this case, you must specify the timeout period and lifetime of the cookie on a backend server. After you specify a cookie, SLB overwrites the original cookie with the specified cookie. The next time SLB receives a client request that carries the specified cookie, the listener distributes the request to the recorded backend server. Cookie: If you select Rewrite Cookie as Cookie Persistence, you must specify a name for the cookie. The name can contain only letters, digits, underscores ( ), _ and hyphens (-). |
|---|---|

| Health Check | Specifies whether to enable the health check feature. If you turn on this switch, you must configure the following parameters: Health Check Method: The default value HEAD is used. Health Check Port: the port that is used to perform health checks on backend servers. Valid values: 1 to 65535. By default, the backend port specified when you configure the listener is used for health checks. We recommend that you leave this parameter empty unless you want to specify a specific port. Health Check URL: the uniform resource identifier (URI) of the page that is used for health checks. We recommend that you perform health checks on static web pages. By default, the requested URL specified for the forwarding rule is displayed. The URI must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & = It must start with a forward _ slash (/). Health Check Domain Name (Optional): the domain name that is used for health checks. The domain name can contain only letters, digits, hyphens (-), and periods (.). By default, no HOST field is specified. Normal Status Codes: the HTTP status codes that indicate a successful health check. You can select one or more HTTP status codes. By default, http 2x and _ http 3x are selected. Valid values: _ http 2x _ http 3x _ http 4x _ http 5x _ Health Check Response Timeout: the maximum timeout period of a health check response. Valid values: 1 to 300. Default value: 5. Unit: seconds. After you specify the timeout period of a health check response, if a backend ECS instance does not return a health check response within the specified timeout period, the instance fails the health check. Health Check Interval: the interval at which health checks are performed. Default value: 2. Unit: seconds. Valid values: 1 to 50. Default value for UDP health checks: 5. Healthy Threshold: the number of consecutive health checks that an ECS instance must pass before the ECS instance is declared healthy. Valid values: 2 to 10. Default value: 3. Unhealthy Threshold: the number of consecutive health checks that an ECS instance must fail before the ECS instance is declared unhealthy. Valid values: 2 to 10. Default value: 3. |
|---|---|

5. Click **OK**.

**Delete a forwarding rule**

1. On the instance management details page, click the **Listeners** tab. On the **Listeners** tab,
find the listener that you want to manage and click **Configure Forwarding Rule** in the
**Actions** column.
2. In the **Forwarding Rule** panel, find the forwarding rule that you want to delete in the
**Forwarding Rules** section and click **Delete** in the **Actions** column.
3. In the message that appears, click **OK**.
4. In the message that appears, confirm the high-risk operation and click **Delete**.

###### 4.2.3.2.6 Domain name extensions

###### 4.2.3.2.6.1 SLB additional domain names

To allow a listener to distribute HTTPS requests that are destined for different domain names to different backend server groups, you can add multiple SSL certificates to the listener.

**Terms**

Server Name Indication (SNI) is an extension to SSL and TLS. SNI allows a server to install multiple SSL certificates on the same IP address. When a client accesses Server Load Balancer (SLB), the certificate configured for the requested domain name is used by default. If the request does not match the certificate configured for the domain name, the certificate configured for the HTTPS listener is used.

**Limits**

SNI is supported only by high-performance SLB instances. SLB supports the following algorithms for public keys: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521

###### 4.2.3.2.6.2 Add and manage additional domain names

**names**

To configure an HTTPS listener to distribute HTTPS requests that are destined for different domain names to different backend server groups, you can add multiple SSL certificates to the listener by using the additional domain name feature of Server Load Balancer (SLB).

**Prerequisites**

An SLB instance is created, and an HTTPS listener is configured for the SLB instance. For more information, see Add an HTTPS listener. You are familiar with the usage notes of additional domain names. For more information, see SLB additional domain names.

**Add an additional domain name**

You can add additional domain names only for HTTPS listeners.
1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance management details page, click the **Listeners** tab. On the **Listeners** tab,
find the HTTPS listener that you want to manage, move the pointer over the

**> Actions**

**> Manage Additional Certificate**

6. In the **Manage Additional Certificate** panel, click **Add Additional Certificate** and
configure the following parameters: i. **Additional Domain**: the additional domain name. Domain name-based forwarding rules support exact match and wildcard match. a. You can specify a specific domain name such as www.aliyun.com in a forwarding rule. b. You can also specify a wildcard domain name such as *.aliyun.com or *.market.aliyun.com in a forwarding rule. If a request matches multiple domain name-based forwarding rules, exact match prevails over wildcard match. If a request matches multiple wildcard domain names, a higher-level wildcard domain name prevails over a lower-level wildcard domain name. In the following table, "✓" indicates that the domain name of the request matches the domain name specified in the forwarding rule. "×" indicates that the domain name of the request does not match the domain name specified in the forwarding rule.

| Match mode | Requested URL | Domain name-based forwarding rule |   |   |
|---|---|---|---|---|
|   |   | www.aliyun.c om | *.aliyun.com | *.market.aliyun. com |
| Exact match | www.aliyun.com | √ | × | × |
| Wildcard match | market.aliyun.com | × | √ | × |
| Wildcard match | info.market.aliyun.co m | × | × | √ |

ii. **Server Certificate**: the server certificate that you want to associate with the domain name. The domain name of the certificate must be the same as the additional domain name that you add. If you add multiple wildcard-domain certificates, requests match only the first wildcard-domain certificate.
7. Click **OK**.
8. **Optional.** Perform the following steps to configure a forwarding rule. You must configure a
forwarding rule based on the additional domain name for the additional domain name to take effect. i. On the **Note** page, click **Configure Rule**. You can also click the ID of the SLB instance on the **Instance Management** page and click the **Listeners** tab. Find the HTTPS listener that you want to manage and click **Configure Forwarding Rule** in the **Actions** column. ii. In the **Forwarding Rule** panel, enter a domain name and a URL to configure a forwarding rule, and click **Add Forwarding Rule**. Make sure that the domain name configured in the forwarding rule is the same as the additional domain name that you added.

**What to do next**

**Modify an additional domain name**

You can replace the certificate that is associated with an additional domain name. For the default domain name, manage its associated certificate on the Listeners tab.
1. In the **Manage Additional Certificate** panel, find the additional domain name that you
want to modify in the **Additional Certificates** section and click **Modify** in the **Actions** column.
2. Select another certificate from the **Server Certificate** drop-down list and click **OK**.

**Remove an additional domain name**

You can remove additional domain names that you no longer use. The default domain name cannot be removed.
1. In the **Manage Additional Certificate** panel, find the additional domain name that you
want to remove in the **Additional Certificates** section and click **Delete** in the **Actions** column.
2. In the message that appears, click **Delete**.

#### 4.2.4 Backend servers

##### 4.2.4.1 Backend server overview

Before you use a Server Load Balancer (SLB) instance, you must add Elastic Compute Service (ECS) instances as the backend servers of the SLB instance to receive requests forwarded by the listeners of the SLB instance.

**Introduction**

After you add ECS instances that are deployed in the same region to an SLB instance, SLB uses virtual IP addresses to combine the ECS instances into a high-performance, highavailability backend server pool. You can also use vServer groups to manage backend servers. You can associate listeners with different server groups. This way, SLB can distribute requests to backend servers that use different ports in different server groups. If you associate a listener with a vServer group, the listener distributes requests to the ECS instances in the vServer group instead of the ECS instances in the default server group.

**Limits**

You can add ECS instances to or remove ECS instances from an SLB instance anytime. SLB distributes network traffic across groups of ECS instances. Before you use SLB, make sure that the health check feature is enabled and at least one ECS instance works as expected to ensure service stability. When you add backend servers, take note of the following items: You can add two ECS instances that run different operating systems to an SLB instance. However, the applications deployed on the ECS instances must be the same and have consistent data. To facilitate management and maintenance, we recommend that you add ECS instances that run the same operating system to an SLB instance. You must configure a listener for each application deployed on a backend ECS instance. Each SLB instance supports up to 50 listeners. SLB uses listener ports to receive client requests and forward the requests to backend ports that are used by the applications on ECS instances. You can specify a weight for each ECS instance in a server group. An ECS instance with a higher weight receives more requests. If session persistence is enabled, requests may be unevenly distributed to backend servers. We recommend that you disable session persistence and check whether the issue persists. If requests are unevenly distributed, troubleshoot the issue by performing the following steps: i. Count the numbers of access log entries generated on different ECS instances within a period of time. ii. Check whether the numbers of access log entries generated on different ECS instances have deviations based on the SLB configurations. If session persistence is enabled, you must exclude access log entries that contain the same IP address. If the ECS instances have different weights, check whether the numbers of access log entries are weighted. When an ECS instance performs hot migration, persistent connections to SLB may be closed. Make sure that the automatic reconnection mechanism is configured for your applications.

**Default server group**

You can add ECS instances to the default server group of an SLB instance to receive requests. If a listener is not associated with a vServer group or a primary/secondary server group, the listener forwards all requests to the ECS instances in the default server group by default. Each SLB instance has a default server group, which is shared by all listeners added to the SLB instance. You can add backend servers to the default server group based on your business requirements. Before an SLB instance can process requests, you must add at least one backend server to the default server group to receive requests. For more information, see Add ECS instances to the default server group.

**vServer groups**

Each SLB instance can have multiple vServer groups. You can associate listeners with a vServer group and specify vServer groups in forwarding rules to control where network traffic is distributed. You can create vServer groups for SLB to distribute different requests to different backend servers. To allow SLB to distribute requests based on domain names or URLs, you can specify vServer groups in domain name-based forwarding rules or URL-based forwarding rules. For more information, see Add ECS instances to a vServer group.

**Primary/secondary server groups**

You cannot associate a Layer 7 listener with a primary/secondary server group. You can associate only TCP and UDP listeners with primary/secondary server groups. A primary/secondary server group contains only two ECS instances. One ECS instance serves as the primary server, and the other ECS instance serves as the secondary server. SLB does not perform health checks on the secondary server in a primary/secondary server group. If the primary server is down, network traffic is automatically distributed to the secondary server. When the primary server recovers, network traffic is switched back to the primary server. For more information, see Add ECS instances to a primary/secondary server group.

##### 4.2.4.2 vServer groups

###### 4.2.4.2.1 Create a vServer group

This topic describes how to create a vServer group and add on-premises servers or Elastic Compute Service (ECS) instances to the vServer group. A vServer group is a group of ECS instances or on-premises servers. If you associate a vServer group with a listener, the listener distributes requests only to backend servers in the vServer group.

**Prerequisites**

Before you add ECS instances to a vServer group, make sure that the following requirements are met: A Server Load Balancer (SLB) instance is created. For more information, see Create an SLB instance. ECS instances are created and applications are deployed on the ECS instances to receive requests. Before you add on-premises servers to a vServer group, make sure that the following requirements are met: Applications are deployed on the on-premises servers, and the servers are ready to receive requests.

**Background information**

Before you create a vServer group, take note of the following items: An ECS instance or an on-premises server can be added to multiple vServer groups. A vServer group can be associated with one or more listeners of an SLB instance. A vServer group consists of ECS instances or on-premises servers and application ports.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **vServer Groups** tab and click **Create**
**vServer Group**.
On the **Instance Management** page, find the SLB instance, click **Add Backend Server** in the **Actions** column, and then click the **vServer Groups** tab. On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column of the SLB instance. On the instance details page, click the **vServer Groups** tab. On the **Instance Management** page, find the SLB instance, and click **vServer Groups** in the **Port/Health Check/Backend Server** column, or click **Not Configured** in the column and click the **vServer Groups** tab.
5. On the **Create vServer Group** page, enter a name in the **vServer Group Name** field and
use one of the following methods to add a backend server to the vServer group.

**Add ECS instances to a vServer group**

i. Click **Add** to go to the **Servers** panel. ii. On the **Select Servers** wizard page, select the ECS instances that you want to add and click **Next**. You can select multiple ECS instances at a time. iii. On the **Configure Weight** wizard page, specify **Port** and **Weight** for each ECS instance and click **Add**. Specify the Port and Weight parameters based on the following information:
**Port**: The backend port opened on an ECS instance to receive requests.
You can specify the same port on multiple backend servers for the same SLB instance. In addition, you can click **Add Port** to specify multiple ports on a backend server.
**Weight**: An ECS instance with a higher weight receives more requests.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests. Click **Remove** to remove the selected backend servers.

**Add on-premises servers to a vServer group**

i. Click **Add On-premises Server** to open the **Servers** panel. ii. On the **Select Servers** wizard page, click **Add**, set the **VPC Connected to Data**
**Center**, **On-premises Server Name**, and **On-premises Server IP Address**
parameters, and then click **Next**. You can add multiple on-premises servers. Make sure that the on-premises servers specified in **On-premises Server IP**
**Address** can communicate with virtual private clouds (VPCs).
iii. On the **Configure Weight** wizard page, specify **Port** and **Weight** for each on-premises server and click **Add**. Specify the Port and Weight parameters based on the following information:
**Port**: The backend port opened on an on-premises server to receive requests. Multiple
ports can be opened on an on-premises server. You can specify the same port on multiple backend servers for the same SLB instance. In addition, you can click **Add Port** to specify multiple ports on a backend server.
**Weight**: An on-premises server with a higher weight receives more requests.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests.
6. Confirm the **Port** and **Weight** settings for the selected servers and click **Add**.
7. In the **Confirm** message, click **OK**.

**What to do next**

**Set the same weight for multiple servers in batch**

1. In the **Added Servers** section on the **Create vServer Group** page, select the servers you
want and click **Set Same Weight** below the list.
2. In the dialog box that appears, specify **Weight** and click **OK**.

**Remove a server**

In the **Added Servers** section on the **Create vServer Group** page, find the server you want to remove and click **Delete** in the **Actions** column. In the **Added Servers** section on the **Create vServer Group** page, select the backend servers that you want to remove and click **Delete** below the list.

###### 4.2.4.2.2 Modify a vServer group

This topic describes how to modify the configurations of Elastic Compute Service (ECS) instances or on-premises servers in a vServer group.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **vServer Groups** tab:
On the **Instance Management** page, find the SLB instance, click **Add Backend Server** in the **Actions** column, and then click the **vServer Groups** tab. On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column of the SLB instance. On the instance details page, click the **vServer Groups** tab. On the **Instance Management** page, find the SLB instance, and click **vServer Groups** in the **Port/Health Check/Backend Server** column, or click **Not Configured** in the column and click the **vServer Groups** tab.
5. On the vServer Groups tab, find the vServer group that you want to modify and click
**Modify** in the **Actions** column.
6. On the **Modify vServer Group** page, change the ports and weights of the ECS instances or
on-premises servers, and click **Save**.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests.
7. In the message that appears, click **OK**.

###### 4.2.4.2.3 Delete a vServer group

If you no longer use a vServer group to receive requests, you can delete the vServer group.

**Procedure**

Before you delete a vServer group, make sure that no listener is associated with the vServer group. If a listener is associated with the vServer group, disassociate the listener first.
1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **vServer Groups** tab:
On the **Instance Management** page, find the SLB instance, click **Add Backend Server** in the **Actions** column, and then click the **vServer Groups** tab. On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column of the SLB instance. On the instance details page, click the **vServer Groups** tab. On the **Instance Management** page, find the SLB instance, and click **vServer Groups** in the **Port/Health Check/Backend Server** column, or click **Not Configured** in the column and click the **vServer Groups** tab.
5. On the vServer Groups tab, find the vServer group that you want to delete and click **Delete**
in the **Actions** column.
6. In the **Confirm** message, click **OK**.
7. In the message that appears, confirm the high-risk operation and click **Delete**.

##### 4.2.4.3 Default server groups

###### 4.2.4.3.1 Add a backend server

Each Server Load Balancer (SLB) instance is associated with a default server group, which is shared by all listeners added to the SLB instance. You can add backend servers to the default server group as needed. Before an SLB instance can process requests, you must add at least one backend server to the default server group to receive requests.

**Prerequisites**

Before you add Elastic Compute Service (ECS) instances to the default server group, make sure that the following requirements are met: An SLB instance is created. For more information, see Create an SLB instance. ECS instances are created, and applications are deployed on the ECS instances to receive requests. Before you add on-premises servers to the default server group, make sure that the following requirements are met: Applications are deployed on the on-premises servers, and the servers are ready to receive requests.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **Default Server Group** tab.
On the **Instance Management** page, find the SLB instance you want and click **Add**
**Backend Server** in the **Actions** column.
On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column. On the instance details page, click the **Default Server Group** tab. On the **Instance Management** page, find the SLB instance and click **Default Server**
**Group** or **Not Configured** in the **Port/Health Check/Backend Server** column.
5. Use one of the following methods to add a backend server to the default server group:

**Add ECS instances to the default server group**

i. Click **Add** to open the **Servers** panel. ii. On the **Select Servers** wizard page, select the ECS instances that you need and click
**Next**.
iii. On the **Configure Weight** wizard page, specify the weight of each ECS instance and click **Add**.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests.

**Add on-premises servers to the default server group**

i. Click **Add On-premises Server** to open the **Servers** panel. ii. On the **Select Servers** wizard page, click **Add**, specify the **VPC Connected to Data**
**Center**, **On-premises Server Name**, and **On-premises Server IP Address**
parameters, then click **Next**. iii. On the **Configure Ports and Weights** wizard page, specify the weight of each onpremises server and click **Add**.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests.
6. In the **Servers to Add** panel, select the servers that you want and click **OK**.
7. In the message that appears, click **OK**.

###### 4.2.4.3.2 Change the weights of backend servers in the default server group

**in the default server group**

This topic describes how to change the weights of backend servers in the default server group to adjust the proportion of requests distributed to the backend servers.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **Default Server Group** tab:
On the **Instance Management** page, find the SLB instance you want and click **Add**
**Backend Server** in the **Actions** column.
On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column. On the instance details page, click the **Default Server Group** tab. On the **Instance Management** page, find the SLB instance and click **Default Server**
**Group** or **Not Configured** in the **Port/Health Check/Backend Server** column.
5. Change the weights of backend servers in the default server group.
Change the weight of a backend server i. On the Default Server Group tab, find the backend server that you want to manage and click the weight value in the **Weight** column. ii. In the **Modify Weight** dialog box, change the value of the **Weight** parameter and click
**OK**.
Change the weights of multiple backend servers at a time i. On the Default Server Group tab, select the backend servers that you want to manage and click **Modify Weight** in the lower-left corner. ii. In the **Modify Weight** panel, set the weights based on one of the following conditions and click **OK**: a. If you select **Set Same Weight**, set the same weight for the selected backend servers. b. If you select **Set Different Weights**, separately set the weights in the **Weight** column for the selected backend servers. iii. In the **Confirm** message, click **OK**. An Elastic Compute Service (ECS) instance or an on-premises server with a higher weight receives more requests.

**Important**

A larger weight indicates that the backend server can receive more requests. The default weight is 100. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive requests.

###### 4.2.4.3.3 Remove backend servers

This topic describes how to remove backend servers that are no longer needed.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **Default Server Group** tab:
On the **Instance Management** page, find the SLB instance you want and click **Add**
**Backend Server** in the **Actions** column.
On the **Instance Management** page, click the ID or name of the SLB instance. Alternatively, click **Manage** in the **Actions** column. On the instance details page, click the **Default Server Group** tab. On the **Instance Management** page, find the SLB instance and click **Default Server**
**Group** or **Not Configured** in the **Port/Health Check/Backend Server** column.
5. Remove backend servers.
Remove a single backend server i. On the Default Server Group tab, find the backend server that you want to remove and click **Remove** in the **Actions** column. ii. In the **Confirm** message, click **OK**. Remove multiple backend servers at a time i. On the Default Server Group tab, select the backend servers that you want to remove and click **Batch Delete** in the lower-left corner. ii. In the **Confirm** message, click **OK**.

##### 4.2.4.4 Primary/secondary server groups

###### 4.2.4.4.1 Create a primary/secondary server group

In traditional scenarios, the backend server group consists of a primary server and a secondary server. If the primary server fails, requests are distributed to the secondary server.

**Prerequisites**

Before you create a primary/secondary server group, make sure that the following requirements are met: A Server Load Balancer (SLB) instance is created. For more information, see Create an SLB instance. Elastic Compute Service (ECS) instances are created and applications are deployed on the ECS instances to receive requests distributed by the SLB instance. Applications are deployed on the on-premises servers, and the servers are ready to receive requests.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **Primary/Secondary Server Groups** tab
and click **Create Primary/Secondary Server Group**. On the **Instance Management** page, find the SLB instance and, in the **Actions** column, click **Add Backend Server**. Click the **Primary/Secondary Server Groups** tab. On the **Instance Management** page, click the ID of the SLB instance. On the **Instance**
**Management** page, click the **Primary/Secondary Server Groups** tab.
On the **Instance Management** page, find the SLB instance, click **Primary/Secondary**
**Server Groups** in the **Port/Health Check/Backend Server** column, or click **Not**
**Configured** in the column and click the **Primary/Secondary Server Groups** tab.
5. On the **Create vServer Group** page, enter a name in the **Primary/Secondary Server**
**Group Name** field and use one of the following methods to add a backend server to the
primary/secondary server group:

**Add ECS instances to a primary/secondary server group**

i. In the **Primary/Secondary Server Group Name** field, enter a name for the primary/secondary server group. ii. Click **Add** to go to the **Servers** panel. iii. On the **Select Servers** wizard page, select the ECS instances that you want to add and click **Next**. You can add only two ECS instances to a primary/secondary server group. iv. On the **Configure Weight** wizard page, set **Port** for each ECS instance and click **Add**. Configure the ports based on the following information:
**Port**: The backend port opened on an ECS instance to receive requests.
You can set the same port for multiple backend servers for the same SLB instance. In addition, you can click **Add Port** to specify multiple ports for a backend server. v. Select **Host** in the **Type** column and select a server as the primary server.

**Add on-premises servers to a primary/secondary server group**

i. In the **Primary/Secondary Server Group Name** field, enter a name for the primary/secondary server group. ii. Click **Add On-premises Server** to go to the **Servers** panel. panel. iii. On the **Select Servers** wizard page, click **Add**, set the **VPC Connected to Data**
**Center**, **On-premises Server Name**, and **On-premises Server IP Address**
parameters, then click **Next**. You can add a maximum of two on-premises servers to one primary/secondary server group.

**Make sure that the on-premises server can use the specified IP address to**

**communicate with the VPC.**

iv. On the **Configure Weight** wizard page, set Port for each on-premises server and click
**Add**.
Configure the ports based on the following information:
**Port**: The backend port opened on an on-premises server to receive requests. Multiple
ports can be opened on an on-premises server. You can set the same port for multiple backend servers for the same SLB instance. In addition, you can click **Add Port** to specify multiple ports for a backend server. v. Select **Host** in the **Type** column and select a server as the primary server.
6. Click **Create**. In the message that appears, click **OK**.

###### 4.2.4.4.2 Delete a primary/secondary server group

If you no longer use a primary/secondary server group to receive requests, you can delete the primary/secondary server group.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Use one of the following methods to go to the **Primary/Secondary Server Groups** tab.
On the **Instance Management** page, find the SLB instance that you want to manage and click **Add Backend Server** in the **Actions** column. On the instance management details page, click the **Primary/Secondary Server Groups** tab. On the **Instance Management** page, find the SLB instance that you want to manage and click the instance ID in the Instance ID/Name column. On the instance management details page, click the **Primary/Secondary Server Groups** tab. On the **Instance Management** page, find the SLB instance that you want to manage and click a port or **Not Configured** in the **Port/Health Check/Backend Server** column. On the instance management details page, click the **Primary/Secondary Server**
**Groups** tab.
5. On the Primary/Secondary Server Groups tab, find the primary/secondary server group that
you want to delete and click **Delete** in the **Actions** column.
6. In the message that appears, click **OK**.

#### 4.2.5 Primary/secondary vServer groups

This topic describes the primary/secondary vServer group feature. A Server Load Balancer (SLB) primary/secondary vServer group supports two groups of virtual servers. When a fault occurs, load balancing services are switched from the primary vServer group to the secondary vServer group.

**Architecture**

The primary/secondary vServer group feature is provided for Layer 4 SLB listeners and disabled by default. Primary/secondary vServer groups can be associated only with TCP and UDP listeners. After you enable the primary/secondary vServer group feature, the feature takes effect only for new listeners. The existing listeners that are previously associated with backend servers in primary/secondary vServer groups are not affected. After you enable the primary/secondary vServer group feature, applications that use persistent connections cannot be switched to use the new feature immediately due to business requirements. In automatic switchover scenarios, the policies of Linux virtual server (LVS) nodes are inconsistent when the number of real server nodes changes. If the status of real servers is constantly changing, which makes the real server failure rate of the primary vServer group oscillate about the failover threshold, the system may frequently switch between the primary and secondary clusters. A real server cannot be added to both the primary vServer group and the secondary vServer group. To enable the primary/secondary vServer group feature, you must enable the health check feature. The number of virtual servers that can be added to a primary/secondary vServer group is not limited. However, we recommend that you add no more than 200 Layer 4 backend servers for a single SLB instance.

**Prerequisites**

The primary/secondary vServer group feature is enabled. Two or more vServer groups are created, and one or more Elastic Compute Service (ECS) instances are added to each vServer group. For more information, see Create a vServer group.

**Create a primary/secondary vServer group**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the SLB instance that you want to manage and
click **Configure Listener** in the Actions column.
5. On the **SLB Configuration Wizard** page, set the Listener Protocol parameter to **TCP** or
**UDP**, and configure other parameters in the **Protocol & Listener** step. In the **Backend**
**Servers** step, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Enable Primary/Second ary Failover | Specifies whether to enable the primary/secondary vServer group feature. |

| Primary Server Group | The primary vServer group. You can also click Create vServer Group to create a vServer group, refresh the page, and then select the new vServer group. |
|---|---|
| Secondary Server Group | The secondary vServer group. You can also click Create vServer Group to create a vServer group, refresh the page, and then select the new vServer group. |
| Failover Policy | Primary Server First: When a fault occurs in the primary vServer group, the system automatically switches services to the secondary vServer group. When the availability of the primary vServer group exceeds the failover threshold, the system automatically switches services back to the primary vServer group. In the Cloud Monitor console, you can view the alerts about this switchover. Manual Failover: By default, the primary vServer group provides services. You decide when to switch between the primary and secondary vServer groups. |
| Failover Threshold | The percentage of servers that failed a health check out of the total number of servers in the primary vServer group, which is the failover threshold. Valid values: 1 to 100. The threshold applies to both the primary and secondary vServer groups. This parameter is required if you set the Failover Policy parameter to Primary Server First. |

**Switch between the primary and secondary vServer groups**

After you configure a listener, if you set the Failover Policy parameter to Manual Failover, you must manually switch between the primary and secondary vServer groups when needed. The switchover operation does not change the role of a vServer group. It changes only the vServer group that is providing services. The interval between two switchover operations cannot be shorter than 1 minute. Conditions for switching services from the primary vServer group to the secondary vServer group: The real server failure rate of the primary vServer group exceeds the failover threshold. The time elapsed since the last switchover operation is greater than or equal to the minimum interval between switchover operations. The secondary vServer group has available real servers. In the following scenario, you can switch services from the primary vServer group to the secondary vServer group without any considerations: The primary vServer group has no available real servers, whereas the secondary vServer group has available real servers. Conditions for switching services from the secondary vServer group to the primary vServer group: The real server failure rate of the primary vServer group drops below the failover threshold. The time elapsed since the last switchover operation is greater than or equal to the minimum interval between switchover operations. The secondary vServer group has no available real servers. In the following scenario, you can switch services from the secondary vServer group back to the primary vServer group without any considerations: The secondary vServer group has no available real servers. A vServer group with no available real servers: The vServer group contains real servers, but all have failed health checks and are declared unhealthy. Alternatively, the vServer group has real servers, but their weights are all set to 0. Or, you may not have added any real servers to the vServer group.
1. On the Listeners tab, find the listener that you want to manage and click **Switch Primary**
**and Secondary Server Groups** under the primary/secondary vServer group name in the
**Server Group** column.
2. Wait until the **Switched** message appears, which indicates that a switchover is complete.

**View unhealthy backend servers**

After a listener is configured, you can view the health check status information.
1. In the listener list, find the listener that you want to check and click **Unhealthy** in the
**Health Check Status** column. In the **Unhealthy Backend Servers** dialog box that
appears, you can view the list of unhealthy backend servers.
2. In the **Unhealthy Backend Servers** message, click an instance name to view the
information about the instance that is added as a backend server.

**What to do next**

For more information about how to perform other operations on listeners, see the What to do next section of the "Add a TCP listener" topic.

#### 4.2.6 Health checks

##### 4.2.6.1 Health check overview

Server Load Balancer (SLB) performs health checks to check the availability of backend Elastic Compute Service (ECS) instances. The health check feature improves overall service availability and reduces the impact of backend server failures. After you enable the health check feature for an SLB instance, the SLB instance periodically checks whether the backend ECS instances are healthy. When the SLB instance detects an unhealthy ECS instance, the SLB instance distributes new requests to other healthy ECS instances. When the unhealthy ECS instance recovers, the SLB instance distributes requests to the recovered ECS instance again. If your business is highly sensitive to traffic fluctuations, frequent health checks may affect the availability of your business. To reduce the adverse impacts of health checks on your business, you can reduce the health check frequency, increase the health check interval, or change Layer 7 health checks to Layer 4 health checks. To ensure business continuity, we recommend that you enable the health check feature.

**How health checks work**

SLB instances are deployed in clusters. Nodes in a Linux virtual server (LVS) or Tengine cluster are used to forward data and perform health checks. Nodes in an LVS cluster forward data and perform health checks independently and in parallel based on the configured load balancing policies. If a node in an LVS cluster detects an unhealthy backend ECS instance, the node stops sending client requests to the unhealthy ECS instance. This operation is synchronized across all of the nodes in the LVS cluster. The following figure shows how health checks work. SLB uses the CIDR block 100.64.0.0/10 for health checks. Make sure that the backend ECS instances do not block this CIDR block. You do not need to configure a security group rule to allow access from the CIDR block 100.64.0.0/10 unless security rules such as iptables are configured. Permitting 100.64.0.0/10 does not increase potential risks because this CIDR block is reserved by Apsara Stack. IP addresses within this CIDR block are not allocated to users.

**Layer 7 health checks on HTTP and HTTPS listeners**

If you add Layer 7 HTTP or HTTPS listeners to your SLB instance, SLB checks the status of backend ECS instances by sending HTTP HEAD requests, as shown in the following figure. For HTTPS listeners, certificates are managed in SLB. To improve system performance, HTTPS is not used to exchange data, including health check data and business data, between the SLB instance and backend ECS instances. How SLB performs Layer 7 health checks:
1. A Tengine node sends an HTTP HEAD request to a backend ECS instance based on the
health check configurations of the Layer 7 listener. The HTTP HEAD request is sent to an address in the following format: ECS instance private IP address + Health check port + Health check path. The HTTP HEAD request also carries the domain name specified in health check configurations.
2. After the backend ECS instance receives the request, the ECS instance checks the status of
the application and returns a relevant HTTP status code.
3. If the Tengine node does not receive a response from the backend ECS instance within the
specified timeout period, the backend server is considered unhealthy.
4. If the Tengine node receives a response from the backend ECS instance within the specified
timeout period, the node matches the returned status code against the status codes specified in health check configurations. If the returned status code matches one of the specified status codes, the backend server is considered healthy. Otherwise, the backend server is considered unhealthy.

**Layer 4 health checks on TCP listeners**

If you add TCP listeners to your SLB instance, SLB performs Layer 4 health checks by establishing TCP sessions, as shown in the following figure. This improves the health check efficiency. How SLB performs TCP health checks:
1. An LVS node sends a TCP SYN packet to a backend ECS instance based on the health check
configurations of the TCP listener. The TCP SYN packet is sent to an address in the following format: ECS instance private IP address + Health check port.
2. After the backend ECS instance receives the request, the ECS instance returns an SYN-ACK
packet if the ECS port on which SLB listens is normal.
3. If the LVS node does not receive a response from the backend ECS instance within the
specified timeout period, the backend ECS instance is considered unhealthy. Then, the node sends an RST packet to the backend ECS instance to terminate the TCP session.
4. If the LVS node receives a response from the backend ECS instance within the specified
timeout period, the node considers the ECS instance healthy and then sends an RST packet to the backend ECS instance to terminate the TCP session. A TCP three-way handshake is performed to establish TCP sessions. After the LVS node receives the SYN-ACK packet from the backend ECS instance, the node sends an ACK packet, and then immediately sends an RST packet to terminate the TCP session. Due to the three-way handshake mechanism, the backend ECS instances may take TCP session terminations as connectivity errors. Then, the ECS instances may record an error, such as `Connection reset by peer` , in application logs, such as Java connection pool logs. Solutions: Configure HTTP health checks for TCP listeners. Enable Proxy Protocol to pass client IP addresses to backend ECS instances. This enables the ECS instances to ignore connectivity errors that are caused by access from the CIDR block of SLB.

**Layer 4 health checks on UDP listeners**

If you add UDP listeners to your SLB instance, SLB checks the status of backend ECS instances by sending UDP packets, as shown in the following figure. How SLB performs UDP health checks:
1. An LVS node sends a UDP packet to a backend ECS instance based on the health check
configurations of the UDP listener. The UDP packet is sent to an address in the following format: ECS instance private IP address + Health check port.
2. If the ECS port on which SLB listens is abnormal, an Internet Control Message Protocol
(ICMP) error message, such as `port XX unreachable` , is returned. If the ECS port is normal, no message is returned.
3. If the LVS node receives an ICMP error message within the specified timeout period, the
backend ECS instance is considered unhealthy.
4. If the LVS node does not receive ICMP error messages from the backend ECS instance
within the specified timeout period, the ECS instance is considered healthy.

|   | Note UDP health check results may not reflect the actual status of the application on a backend ECS instance in the following situation: If a backend ECS instance runs the Linux operating system, the rate at which ICMP messages are sent in high concurrency scenarios is limited due to the ICMP attack prevention mechanism of Linux. In this case, even if an application error occurs, SLB may consider the backend ECS instance healthy because SLB has not received the port XX unreachable error message. As a result, the health check result is different from the actual application status. Solutions: You can set SLB to send a specific string to a backend server. The backend server is considered healthy only if it returns a specific response to SLB. However, the application on the backend server must be configured accordingly to return responses. |   |   |
|---|---|---|---|
|   |   | port XX |   |
|   | unreachable |   |   |

**Health check time windows**

The health check feature improves the availability of your services. However, frequent failovers caused by unhealthy backend servers may affect system availability. Health check time windows are introduced to control failovers. A failover is performed only if a backend server consecutively passes or fails a specific number of health checks within a time window. A health check time window is determined by the following factors: Health check interval: the interval at which health checks are performed. Response timeout period: the amount of time that a backend server takes to respond. Health check threshold: the number of consecutive times that a backend server passes or fails health checks. Health check time windows are calculated based on the following formulas: Time window for health check failures = Response timeout period × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1) Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1) The response time of a successful health check is the duration from the time when a health check request is sent to the time when a response is received. When TCP health checks are configured, the response time is short and almost negligible because the only check item is whether the probed port is alive. When HTTP health checks are configured, the response time varies based on the performance and load of the application server and is typically within a few seconds. The health check result has the following impacts on request forwarding: If the backend ECS instance fails the health check, new requests are distributed to other backend ECS instances. The client can still access the application as normal. If the backend ECS instance passes the health check, new requests are distributed to the ECS instance. The client can access the application as normal. If an exception occurs on the backend ECS instance and a request arrives during the time window for health check failures, the request is still sent to the unhealthy backend ECS instance. This is because the number of failed health checks has not reached the unhealthy threshold (three times by default). In this case, the client fails to access the application.

**Examples of the health check response timeout period and the**

**health check interval**

In this example, the following health check configurations are used:

**Response timeout period: 5 seconds**

**Health check interval: 2 seconds**

**Healthy threshold: 3 times**

**Unhealthy threshold: 3 times**

Time window for health check failures = Response timeout period × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1). In this example, the time window is 19 seconds based on the following formula: 5 × 3 + 2 × (3 - 1). If a backend server does not respond within 19 seconds, the backend server is considered unhealthy. The following figure shows the time window from a healthy status to an unhealthy status. Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1). In this example, the time window is 7 seconds based on the following formula: (1 × 3) + 2 × (3 - 1). If a backend server responds within 7 seconds, the backend server is considered healthy. The response time of a successful health check is the duration from the time when a health check request is sent to the time when a response is received. When TCP health checks are configured, the response time is short and almost negligible because the only check item is whether the probed port is alive. When HTTP health checks are configured, the response time varies based on the performance and load of the application server and is typically within a few seconds. The following figure shows the time window from an unhealthy status to a healthy status. In the following figure, the amount of time that is required for the server to respond to a health check request is 1 second.

**Domain names for HTTP health checks**

You can specify a domain name for HTTP health checks. This setting is optional. Some application servers must verify the host field in requests before the application servers can accept the requests. In this case, the request header must carry the host field. If a domain name is specified in health check configurations, SLB adds this domain name to the host field when SLB forwards a health check request to an application server. If no domain name is specified, SLB does not include the host field in the request. As a result, the request is rejected by the application server and the health check fails. If your application server verifies the host field in requests, you must specify a domain name in health check configurations to ensure that the health check feature works as expected.

##### 4.2.6.2 Configure health checks

Server Load Balancer (SLB) performs health checks to check the availability of backend Elastic Compute Service (ECS) instances. The health check feature improves service availability and prevents service errors caused by unhealthy backend ECS instances. When you add or modify a listener, you can enable health checks and use the default health check configuration. Alternatively, you can click Advanced Settings and customize the health check configuration. Configure the following parameters in **Advanced Settings** to customize the health check configuration. Table 1. **Advanced Settings** for health checks

| Advanced Settings for health checks | Description |
|---|---|
| Health Check Protocol | Select a protocol for health checks. TCP: TCP health checks are performed at the network layer. SLB probes the port of a backend server to check whether the server is healthy by sending SYN packets. UDP: UDP health checks are performed at the network layer. SLB probes the port of a backend server to check whether the server is healthy by sending UDP packets. HTTP: HTTP health checks are performed in a similar way as a browser accesses a web page. SLB checks whether a backend server is healthy by sending HEAD or GET requests. Note The UDP option is available only when the Listener Protocol parameter is set to UDP. |
| HTTP Version (available only when Listener Protocol is set to HTTP) | Select an HTTP version. http1.0 http1.1 Note By default, the HTTP Version feature is disabled. To enable the feature, contact Apsara Stack technical support. |
| Health Check Method (only for HTTP health checks) | HTTP and HTTPS listeners support the GET and HEAD methods. If the GET method is used and the response size exceeds 8 KB, the response is truncated. However, you can still obtain the health check result based on the response. By default, HTTP listeners send HEAD requests to probe the availability of backend servers. Make sure that the backend servers support HEAD requests. |

| Content-based Deep Health Check | When this feature is enabled, listeners not only check HTTP status codes, but also check whether the responses returned by backend servers meet the requirements. Listeners can determine whether the application layer functions as normal by checking the returned content. When this feature is disabled, listeners determine the health status of backend servers only by checking HTTP status codes. Note This parameter is available only when the Listener Protocol parameter is set to TCP and the Health Check Protocol parameter is set to HTTP. The Content-based Deep Health Check feature is disabled by default. To enable the feature, contact Apsara Stack technical support. |
|---|---|
| Health Check Port | Specify the backend port to be probed. Enter a port or leave it empty to probe the port used by the backend server (recommended). Valid values: 1 to 65535. Note If a vServer group or a primary/secondary server group is associated with the listener, and the ECS instances in the server group use different ports, leave this parameter empty. SLB automatically probes the port of each ECS instance. |
| Health Check URI and Health Check Domain Name (Optional) (available only when Health Check Protocol is set to HTTP or UDP) | If you do not want to use the default homepage for health checks, you can manually specify a URI. Some application servers must verify the host field in requests before the application servers can accept the requests. In this case, the request header must carry the host field. If a domain name is configured in health check settings, SLB adds this domain name to the host field when SLB forwards a health check request to one of the preceding application servers. If no domain name is configured, SLB does not include the host field in the request. As a result, the request is rejected by the application server and the health check fails. If your application server needs to verify the host field in requests, you must configure a domain name in health check settings to ensure that the health check feature functions as normal. |

| Return | The expected response content returned by backend servers. When the response content contains the specified string, the health check is passed. Note This parameter is available only when the Listener Protocol parameter is set to TCP, the Health Check Protocol parameter is set to HTTP, and the Content-based Deep Health Check feature is enabled. |
|---|---|
| Normal Status Codes (only for HTTP health checks) | Select the HTTP status codes that indicate healthy backend servers. By default, http 2xx and http 3xx are selected. _ _ http 2xx _ http 3xx _ http 4xx _ http 5xx _ |
| Health Check Response Timeout | Specify the timeout period for a health check response. If a backend ECS instance does not return a response within the specified timeout period, the server fails the health check. Valid values: 1 to 300. Unit: seconds. Default value for UDP listeners: 10. Default value for HTTP, HTTPS, and TCP listeners: 5. |
| Health Check Interval | Specify the interval between two consecutive health checks. All nodes in the Linux Virtual Server (LVS) cluster perform health checks independently and in parallel on backend ECS instances at the specified interval. However, the frequency at which a single ECS instance is probed does not conform to the health check interval because the nodes probe the ECS instance at different time points. Valid values: 1 to 50. Unit: seconds. Default value for UDP listeners: 5. Default value for HTTP, HTTPS, and TCP listeners: 2. |
| Healthy Threshold | The number of consecutive successful health checks that must occur on a backend ECS instance before this ECS instance is declared healthy. Valid values: 2 to 10. Default value: 3. |
| Unhealthy Threshold | The number of health checks that a healthy backend ECS instance must consecutively fail before the ECS instance is considered unhealthy. Valid values: 2 to 10. Default value: 3. |
| Health Check Requests | Specify the health check request. The value must be 1 to 500 characters in length and can contain only letters and digits. Note This parameter is available only when the Listener Protocol parameter is set to UDP. |

| Health Check Result | Specify the health check response. The value must be 1 to 500 characters in length and can contain only letters and digits. Note This parameter is available only when the Listener Protocol parameter is set to UDP. |
|---|---|
| FIN Termination | Specify whether to enable FIN termination. TCP segments with the FIN flag are used to terminate the connection after the health check is complete. However, in certain scenarios, the frequent establishment and termination of connections during health checks may increase CPU overheads. Note This parameter is available only when the Listener Protocol parameter is set to TCP and the Health Check Protocol parameter is set to TCP. |

##### 4.2.6.3 Disable the health check feature

This topic describes how to disable the health check feature for a Server Load Balancer (SLB) instance. If you disable the health check feature, requests may be distributed to unhealthy backend Elastic Compute Service (ECS) instances. This causes service interruptions. We recommend that you enable the health check feature.

**Background information**

You can disable the health check feature only for HTTP and HTTPS listeners. The health check feature for UDP and TCP listeners cannot be disabled.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance management details page, click the **Listeners** tab.
6. On the Listeners tab, find the listener that you want to manage and click **Modify Listener**
in the **Actions** column.
7. On the **Configure Listener** page, click **Next** until you go to the **Health Check** step.
8. Turn off Health Check and click **Next**.
9. Click **Submit**. In the message that appears, click **OK**.

#### 4.2.7 Associate an EIP with an internal-facing SLB instance and manage the EIP

**SLB instance and manage the EIP**

If you create an internal-facing Server Load Balancer (SLB) instance in a virtual private cloud (VPC) and want to use it to access the Internet, you can associate an elastic IP address (EIP) with the SLB instance. This way, the SLB instance can forward requests from the Internet and provide Internet-facing services.

**Prerequisites**

An internal-facing SLB instance is created in a VPC. For more information, see Create an SLB instance. An EIP is created. For more information, see the **Create and manage an EIP** topic in
**Apsara Stack VPC User Guide**.

**Limits**

The internal-facing SLB instance and the EIP must be deployed in the same region. Each SLB instance can be associated with only one EIP.

**Associate the EIP with the SLB instance**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance details page, click the **Instance Details** tab.
6. If the SLB instance is not associated with an EIP, click **Bind** to the right of **EIP** in the **EIP**
**Information** section.
7. In the **Bind EIP** dialog box, specify **Elastic IP Address (EIP)** and click **OK**.
8. Optional. After the EIP is associated, click the ID of the EIP to the right of **EIP** in the **EIP**
**Information** section to view the details of the EIP.

**Disassociate the EIP from the SLB instance**

After you disassociate the EIP from the SLB instance, the SLB instance can no longer forward requests from the Internet. If the data is not updated after you perform this operation, refresh the page.
1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance details page, click the **Instance Details** tab.
6. In the **EIP Information** section, click **Unbind** in the upper-right corner.
7. In the message that appears, confirm the information and click **OK**.

#### 4.2.8 View monitoring data in the console

You can view the monitoring data of a Server Load Balancer (SLB) instance in Cloud Monitor, such as the number of connections, number of packets, and data transfer.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the SLB instance that you want to manage and
click the icon in the Monitoring column.
5. In the Monitoring panel, view the monitoring data of the SLB instance.
The following table describes the SLB metrics.

**Server Load Balancer (SLB)**

Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceActiveCo nnection | Count | InstanceActiveConne ction | userId, instanceId, and protocol | The number of active TCP connections. |
| InstanceInactive Connection | Count | InstanceInactiveConn ection | userId, instanceId, and protocol | The number of inactive connections on the port. |
| InstanceDropCon nection | Count/s | InstanceDropConnect ion | userId, instanceId, and protocol | The number of connections dropped from the listener per second. |

| InstancecDropTr afficRX | Bit/s | InstanceDropTrafficR X | userId, instanceId, and protocol | The number of inbound bits dropped from the listener per second. |
|---|---|---|---|---|
| InstanceDropTraf ficTX | Bit/s | InstanceDropTrafficT X | userId, instanceId, and protocol | The number of outbound bits dropped from the listener per second. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketR X | userId, instanceId, and protocol | The number of inbound packets dropped per second on an instance. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketT X | userId, instanceId, and protocol | The number of outbound packets dropped per second on an instance. |
| InstanceMaxCon nection | Count/s | InstanceMaxConnecti on | userId, instanceId, and protocol | The number of concurrent connections per second on the port. |
| InstanceNewCon nection | Count | InstanceNewConnecti on | userId, instanceId, and protocol | The number of new TCP connections. |
| InstancePacketR X | Count/s | InstancePacketRX | userId, instanceId, and protocol | The number of inbound packets per second. |
| InstancePacketT X | Count/s | InstancePacketTX | userId, instanceId, and protocol | The number of outbound packets per second. |
| InternetInRate | Bit/s | InstanceTrafficRXNe w | userId, instanceId, and protocol | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId, instanceId, and protocol | The outbound bandwidth. |

| HealthyServerCo unt | Count | InstanceHeathyServe rCount | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
|---|---|---|---|---|
| UnhealthyServer Count | Count | InstanceUnhealthySe rverCount | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Sum of inflow bandwidth | Bit/s | InstanceTrafficRXNe w SUM _ | userId, instanceId, and protocol | The total inbound bandwidth. |
| Sum of outflow bandwidth | Bit/s | InstanceTrafficTXNew SUM _ | userId, instanceId, and protocol | The total outbound bandwidth. |
| Seven-layer instance Qps | Request s/s | InstanceSevenFloorQ ps | userId and instanceId | The QPS at Layer 7. |
| InstanceFailConn ection | Count | InstanceFailConnecti on | userId and instanceId | The number of failed connections to the instance per second. |
| Instance Layer -7 Back-end Health Check Failure Rate | % | InstanceSeventhFloor UnhealthyServerRate | userId, instanceId, and rip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |
| QPS usage of seven-tier instances | % | InstanceSevenFloorQ psRate | userId and instanceId | The QPS usage of the instance at Layer 7. |
| Maximum instance connections usage | % | InstanceMaxConnecti onRate | userId and instanceId | The maximum connection utilization of the instance. |

**Port-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| TCPActiveConne ction | Count | ActiveConnectio n | userId, instanceId, port, and protocol | The number of active TCP connections per second. |
| TCPInactiveConn ection | Count | InactiveConnecti on | userId, instanceId, port, and protocol | The number of inactive TCP connections. |
| DropConnection | Count/s | DropConnection | userId, instanceId, port, and protocol | The number of connections dropped from the listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, port, and protocol | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, port, and protocol | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, port, and protocol | The number of inbound packets that are dropped per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, port, and protocol | The number of outbound packets that are lost per second. |
| MaxConnection | Count/s | MaxConnection | userId, instanceId, port, and protocol | The number of concurrent connections to the TCP port per second. |
| TCPNewConnecti on | Count | NewConnection | userId, instanceId, port, and protocol | The number of new TCP connections. |

| PacketInPerSeco nd | Count/s | PacketRX | userId, instanceId, port, and protocol | The number of inbound packets per second. |
|---|---|---|---|---|
| PacketOutPerSec ond | Count/s | PacketTX | userId, instanceId, port, and protocol | The number of outbound packets per second. |
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, port, and protocol | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, port, and protocol | The outbound bandwidth. |
| HealthyServerCo unt | Count | HeathyServerCo unt | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
| UnhealthyServer Count | Count | UnhealthyServer Count | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Port inflow bandwidth sum | Bit/s | TrafficRXNew SU _ M | userId, instanceId, port, and protocol | The total inbound bandwidth. |
| Port outflow bandwidth sum | Bit/s | TrafficTXNew SU _ M | userId, instanceId, port, and protocol | The total outbound bandwidth. |
| Seven layers Qps | Requests/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |
| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |

| Failure rate of seven-tier back- end health check | % | SeventhFloorUnh ealthyServerRat e | userId, instanceId, port, and vip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |
|---|---|---|---|---|

#### 4.2.9 View fine-grained monitoring data in the console

**the console**

You can view the near-real-time monitoring data of a Layer 4 Server Load Balancer (SLB) instance in Cloud Monitor, such as the number of connections, number of packets, and data transfer.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instance Management** page, find the SLB instance that you want to manage and
click **Manage** in the **Actions** column to go to the instance management details page.
5. On the instance management details page, click the **Fine-grained Monitoring** tab.
6. On the **Fine-grained Monitoring** tab, click **Enable Fine-grained Monitoring**. In the
dialog box that appears, select an existing project or create a project, select a Logstore, select **I understand the above information** , and then click **OK**.
7. On the Fine-grained Monitoring tab, view the monitoring data of the SLB instance.
The following table describes the metrics of Layer 4 SLB.

| Metric | Description |
|---|---|
| Flow | Incoming traffic: the amount of network traffic to the SLB instance. Transmission Traffic: the amount of network traffic from the SLB instance. |
| Data Packet | Received Packets: the number of packets received by the SLB instance per second. Send Packets: the number of packets sent by the SLB instance per second. |

| Connections | Valid Connections: the number of TCP connections that are in the ESTABLISHED state. If persistent connections are used, a connection can transfer multiple file requests at the same time. Invalid Connections: the number of TCP connections that are not in the ESTABLISHED state. You can run the netstat -an command to view the connections for both Windows and Linux instances. Maximum Connections: the total number of TCP connections. |
|---|---|
| New Connections | The average number of new TCP connections established between clients and the SLB instance within a statistical period. |
| Dropped Flow | Incoming Traffic: the amount of inbound traffic dropped per second. Transmission Traffic: the amount of outbound traffic dropped per second. |
| Dropped Packets | Received Packets: the number of inbound packets dropped per second. Send Packets: the number of outbound packets dropped per second. |
| Exception | Disconnected Connections: the number of connections closed between the SLB instance and clients within a statistical period. Failed Connections: the number of connections failed between the SLB instance and clients within a statistical period. |
| ACL Dropped Packets | The number of packets dropped due to ACL rules. |
| ACL Dropped Flow | The amount of traffic dropped due to ACL rules. |

#### 4.2.10 View the details of an SLB instance

This topic describes how to view the details of a Server Load Balancer (SLB) instance.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. On the **Instances** page, find the target instance, then click its instance ID in the **Instance**
**ID/Instance Name** column, or click **Manage** in the **Actions** column.
5. On the instance management details page, view the details of the SLB instance.
In the **Basic Information** section of the Instance Details tab, find the **Instance Name** parameter, move the pointer over the parameter value, and then click the icon. You can modify the name of the SLB instance. In the **Configuration Information** section, click the virtual private cloud (VPC) ID or vSwitch ID below **Network**. You can view the details of the VPC or vSwitch.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Instance Name | The name of the instance. |
| ID | The ID of the instance. |
| Zone ID | The ID of the zone in which the instance resides. |
| Status | The state of the instance. |
| Network Type | The network type of the instance. You can deploy SLB instances in the classic network or a VPC. |
| Instance Type | The type of the instance. Internet-facing SLB instances and internal-facing SLB instances are supported. |
| IP Version | The IP address type of the instance. IPv4 and IPv6 IP addresses are supported. |
| Configuration Information |   |
| Instance Specification | The specification of the instance. The performance of high-performance SLB instances varies based on the instance specification. For more information, see the Instance specifications section of the "SLB instance overview" topic. |
| Service Address | The service IP address of the instance. |
| Created At | The time when the instance was created. |
| Maximum Bandwidth | The maximum bandwidth of the instance. Valid values: 1 to 5120. Unit: Mbit/s. Note This parameter is displayed only if you set the Instance Type parameter to Internet and the Bandwidth limit parameter to Restriction. |

### 4.3 Certificate management

#### 4.3.1 Certificate overview

This topic provides an overview of certificates. To create an HTTPS listener, you must first upload the required third-party server certificate and certificate issued by a certificate authority (CA) to Server Load Balancer (SLB). You do not need to install certificates on backend servers after you upload the certificates to SLB.

| Certificat e | Description | Required for one-way authentication | Required for mutual authentication |
|---|---|---|---|
| Server certificat e | A server certificate is used to authenticate the identity of a server. A browser authenticates the identity of a server by checking whether the certificate sent by the server is issued by a trusted CA. | Yes You must upload the server certificate to the certificate management system of SLB. | Yes You must upload the server certificate to the certificate management system of SLB. |
| Client certificat e | A client certificate is used to authenticate the identity of a client. A server authenticates the identity of a client by verifying the certificate sent by the client. You can sign the client certificate with a self- signed CA certificate. | No | Yes You must install the client certificate on the client. |
| CA certificat e | A CA certificate is used by a server to verify the signature of a client certificate. If the signature is invalid, the connection request is denied. | No | Yes You must upload the CA certificate to the certificate management system of SLB. |

SLB supports third-party certificates. To upload a third-party certificate, you must have the files that contain the public key and private key of the certificate. HTTPS server certificates and client CA certificates are supported. You can add up to 600 certificates with each account.

#### 4.3.2 Certificate requirements

Server Load Balancer (SLB) supports only certificates in the PEM format. Before you upload a certificate, make sure that the certificate content, certificate chain, and private key meet the corresponding format requirements.

**Certificates issued by a Root CA**

If your certificate is issued by a Root certification authority (CA), the received certificate file contains only one certificate. You do not need other certificates to prove that the matching domain name is trusted. The certificate must meet the following format requirements: The certificate must start with `-----BEGIN CERTIFICATE-----` and end with -----END CERTIFICATE-----. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. The certificate content cannot contain spaces.

**Certificates issued by an Intermediate CA**

If your certificate is issued by an Intermediate CA, the received certificate file contains multiple certificates. You must upload both the server certificate and the required intermediate certificates to SLB. The format of the certificate chain must meet the following requirements: The server certificate must be put first and the content of the required intermediate certificates must be put underneath without blank lines between the certificates. The certificate content cannot contain spaces. Blank lines are not allowed between the certificates. Each line must contain 64 characters. For more information, see RFC1421. Certificates must meet the corresponding format requirements. In most cases, the Intermediate CA provides instructions about the certificate format when certificates are issued. The certificates must meet the format requirements. The following section provides a sample certificate chain:

```
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
```

**Public keys of certificates**

SLB supports the following public key algorithms: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521

**RSA private key formats**

When you upload a server certificate, you must upload the private key of the certificate. An RSA private key must meet the following format requirements: The private key must start with `-----BEGIN RSA PRIVATE KEY-----` and end with -----END RSA PRIVATE KEY-----, and these parts must also be uploaded. Blank lines are not allowed in the content. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. For more information, see RFC1421. You may use an encrypted private key. For example, the private key starts with `----BEGIN` `PRIVATE KEY-----` and ends with -----END PRIVATE KEY-----, or starts with `-----BEGIN` `ENCRYPTED PRIVATE KEY-----` and ends with -----END ENCRYPTED PRIVATE KEY-----. The private key may also contain `Proc-Type: 4,ENCRYPTED` . In this case, you must first run the following command to convert the private key:

```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```

#### 4.3.3 Add and manage certificates

When you configure an HTTPS listener, you can directly use a certificate from Certificate Management Service or upload a third-party server certificate and a certificate authority (CA) certificate to Server Load Balancer (SLB). After you upload the certificates to SLB, you do not need to configure certificates on backend servers.

**Prerequisites**

A server certificate is purchased. A CA certificate and a client certificate are generated.

**Background information**

You can add up to 600 certificates with each account.

**Upload a certificate**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) >**
**Certificates**.
4. On the **Certificate Management** page, click **Add Certificate**.
5. On the **Create Certificate** page, configure the parameters that are described in the
following table and click **Submit**.

| Parameter | Description |
|---|---|
| Regional information |   |
| Organization | The organization to which the certificate belongs. |
| Resource Set | The resource set to which the certificate belongs. |
| Certificate deployment region | The region in which you want to deploy the certificate. |

| Sharing Scope | The sharing scope of the certificate. Valid values: Current Resource Set: Only the administrators of the current resource set can use shared certificates. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can use shared certificates. Current Organization: Only the administrators of the current organization can use shared certificates. |
|---|---|
| Basic information |   |
| Certificate Name | The name of the certificate. The name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), underscores ( ), and asterisks (*). _ |
| Certificate Type | The type of the certificate. Valid values: International Certificate and State Secret Certificate. Note x86 architectures, including Intel and Hygon, support ShangMi (SM) certificates. |
| Public Key Certificate | The public key certificate. Set the value to Server Certificate. |
| Public Key Certificate | The content of the server certificate. Paste the content into the editor. Click View Sample to view valid certificate formats. For more information, see Certificate requirements. |
| Private Key | The private key of the server certificate. Paste the private key into the editor. Click View Sample to view valid certificate formats. For more information, see Certificate requirements. Important A private key is required only if you upload a server certificate. |

**Add a CA certificate**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) >**
**Certificates**.
4. On the **Certificate Management** page, click **Create CA Certificate**.
5. On the **Create Certificate** page, configure the parameters that are described in the
following table and click **Submit**.

| Parameter | Description |
|---|---|
| Regional information |   |
| Organization | The organization to which the certificate belongs. |
| Resource Set | The resource set to which the certificate belongs. |
| Certificate deployment region | The region in which you want to deploy the certificate. |
| Sharing Scope | The sharing scope of the certificate. Valid values: Current Resource Set: Only the administrators of the current resource set can use shared certificates. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can use shared certificates. Current Organization: Only the administrators of the current organization can use shared certificates. |
| Basic information |   |
| Certificate Name | The name of the certificate. The name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), underscores ( ), and _ asterisks (*). |
| Client CA public key certificate | The public key certificate of the CA that issued the client certificate. Click View Sample to view valid certificate formats. For more information, see Certificate requirements. |

**What to do next**

**View certificates**

On the **Certificate Management** page, you can view information about certificates in the certificate list. The list is limited to 100 pages and can display a maximum of 10,000 entries. If you have more than 10,000 entries, use filters to find the data that you need. Enter a keyword or click **Advanced Filter** and enter a search condition to search for certificates. Click the icon in the upper-right corner of the list to select the columns that you want to show or hide. You can also drag the columns to adjust the order. Click the icon next to the **Certificate Status** column and select **Normal** or **Expired** to filter certificates. Click the icon next to the **Certificate Type** column and select a certificate type to filter certificates. Click the icon next to the **Sharing Scope** column and select an item to filter certificates. Find a certificate and click the icon next to the name in the **Certificate ID/Name** column to modify its name. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.

**Configure the sharing settings**

You can modify the sharing scope of a certificate.
1. On the **Certificate Management** page, find the certificate that you want to manage and
click **Sharing Settings** in the **Actions** column.
2. In the **Sharing Settings** dialog box, configure the **Sharing Scope** parameter and click
**OK**.

**View associated SLB instances**

You can view SLB instances that are associated with a certificate.
1. On the **Certificate Management** page, find the certificate that you want to manage and
click **Associated Instance** in the **Actions** column.
2. In the **Associated Instance** dialog box, view the ID and port number of each associated
SLB instance.
3. Click the ID in the **Instance ID** column to view the listeners of the SLB instance.

**Remove certificates**

If a certificate is associated with a listener, the certificate cannot be removed.
1. Method 1: On the **Certificate Management** page, find the certificate that you want to
remove and click **Delete** in the **Actions** column. Method 2: On the **Certificate Management** page, select the certificates that you want to remove and click **Batch Delete** in the lower-left corner.
2. In the message that appears, click **OK**.
3. In the **Release Resource** message, click **OK**.
4. In the message that appears, click **OK**.

**Remove all expired certificates**

We recommend that you replace certificates before they expire to avoid impacts on your service.
1. On the **Certificate Management** page, click **Delete All Expired Certificates**.
2. In the message that appears, click **OK**. All expired certificates are removed.
If a certificate is associated with a listener, the certificate cannot be removed.

#### 4.3.4 Generate a CA certificate

When you configure an HTTPS listener, you can use a self-signed certificate authority (CA) certificate. You can also use the CA certificate to sign a client certificate.

**Generate a CA certificate by using OpenSSL**

1. Upload a certificate to a Linux server. Run the following commands to create a ca folder in
the /root directory, and then create four subfolders in the ca folder:

```python
 sudo mkdir ca
 cd ca
 sudo mkdir newcerts private conf server
```

newcerts is used to store the digital certificate signed by the CA certificate. private is used to store the private key of the CA certificate. conf is used to store the configuration files used for simplifying parameters. server is used to store the server certificate.
2. Create an openssl.conf file that contains the following information in the conf folder:

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

3. Run the following commands to generate a private key:

```python
cd /root/ca sudo openssl genrsa -out private/ca.key
```

The following figure shows the command output.
4. Run the following command, enter the required information as prompted, and then press
the Enter key to generate a .csr file.

```python
sudo openssl req -new -key private/ca.key -out private/ca.csr
```

Common Name: the domain name of the Server Load Balancer (SLB) instance.
5. Run the following command to generate a .crt file:

```python
sudo openssl x509 -req -days 365 -in private/ca.csr -signkey private/ca.key -out priv ate/ca.crt
```

6. Run the following command to set the initial sequence number of the CA key. The key can
be any four characters.

```python
sudo echo FACE > serial
```

7. Run the following command to create a CA key library:

```python
sudo touch index.txt
```

8. Run the following command to create a certificate revocation list for removing the client
certificate:

```python
sudo openssl ca -gencrl -out /root/ca/private/ca.crl -crldays 7 -config "/root/ca/conf/openssl.conf"
```

Output:

```
Using configuration from /root/ca/conf/openssl.conf
```

**Sign a client certificate**

1. Upload a certificate to a Linux server. Run the following command to create a users folder
in the ca folder:

```python
sudo mkdir users
```

2. Run the following command to create a client key:

```python
sudo openssl genrsa -des3 -out /root/ca/users/client.key 1024
```

When you create the key, enter a passphrase as the key password to prevent unauthorized use if the key leaks. Enter the same password twice.
3. Run the following command to create a .csr file for the client key:

```python
sudo openssl req -new -key /root/ca/users/client.key -out /root/ca/users/client.csr
```

Enter the passphrase used in the previous step and other required information as prompted. A challenge password is the password of the client certificate. Take note that the challenge password is not the password of the client key.
4. Run the following command to use the CA key to sign the client key:

```python
sudo openssl ca -in /root/ca/users/client.csr -cert /root/ca/private/ca.crt -keyfile /root/ca/private/ca.key -out /root/ca/users/client.crt -config "/root/ca/conf/openssl.conf"
```

Enter y when you are prompted to confirm the operations.
5. Run the following command to convert the certificate to a PKCS12 file:

```python
sudo openssl pkcs12 -export -clcerts -in /root/ca/users/client.crt -inkey /root/ca/us ers/client.key -out /root/ca/users/client.p12
```

Enter the passphrase of the client key as prompted and press the Enter key. Then, enter the password used to export the client certificate. This password is used to protect the client certificate and is required when you install the client certificate.
6. Run the following commands to view the generated client certificate:

```
 cd users
```

`ls`

#### 4.3.5 Convert certificate formats

Server Load Balancer (SLB) supports only certificates in the PEM format. Certificates in other formats must be converted to the PEM format before they can be uploaded to SLB. We recommend that you use OpenSSL to convert certificate formats.

**Convert a certificate from DER to PEM**

DER: This format is usually used on the Java platform. In most cases, the certificate file suffix is .der, .cer, or .crt. Run the following command to convert the certificate format:

```
openssl x509 -inform der -in certificate.cer -out certificate.pem
```

Run the following command to convert the private key:

```
openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem
```

**Convert a certificate from P7B to PEM**

P7B: This format is usually used in Windows Server and Tomcat. Run the following command to convert the certificate format:

```
openssl pkcs7 -print_certs -in incertificate.p7b -out outcertificate.cer
```

**Convert a certificate from PFX to PEM**

PFX: This format is usually used in Windows Server. Run the following command to extract the certificate:

```
openssl pkcs12 -in certname.pfx -nokeys -out cert.pem
```

Run the following command to extract the private key:

```
openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes
```

### 4.4 Manage access logs

Server Load Balancer (SLB) allows you to view access logs. After you enable the access log feature, you can store access logs in a Logstore. This way, you can analyze the access logs in Simple Log Service (SLS).

**Limits**

Only Layer 7 SLB listeners, including HTTP and HTTPS listeners, support access logs.

**Prerequisites**

An SLB instance is created. For more information, see Create and manage SLB instances. A vServer group is created. For more information, see Create a vServer group. Backend servers are added to the vServer group, and applications are deployed on the backend servers. An HTTP or HTTPS listener is configured for the SLB instance. For more information, see Add an HTTP listener or Add an HTTPS listener. SLS is activated. For more information, see SLS documentation.

**Configure access logs**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Access**
**Logs**.
4. Method 1: On the **Access Log** page, find the SLB instance that you want to manage and
click **Settings** in the **Actions** column. Method 2: On the **Access Log** page, select the SLB instances that you want to manage and click **Batch Configure** in the lower-left corner.
5. In the **Log Settings** panel, configure the **Project** and **Logstore** parameters and click **OK**.
**Project**: the resource management unit that is used to isolate and manage resources in
SLS.
**Select Project**: If you set the Project parameter to Select Project, select an existing
project from the drop-down list.
**Create Project**: If you set the **Project** parameter to Create Project, enter the project
name and configure the **Organization** and **Resource Set** parameters to create a project.
**Logstore**: the unit that is used to collect, store, and query log data in SLS.
Make sure that the name of the project is unique and the region of the project is the same as that of the SLB instance.

**What to do next**

After the access log feature is enabled, you can query access log data and disable the access log feature.

**Query access log data**

1. On the **Access Log** page, find the SLB instance that you want to manage and click the
project name in the **Simple Log Service** column or **View Logs** in the **Actions** column.
2. On the page that appears, query and retrieve log data.
Enter an SQL statement to query log data.

| Field | Description |
|---|---|
| body bytes sent _ _ | The size of the HTTP response body. Unit: bytes. |
| client ip _ | The IP address of the client that sends the request. |
| client port _ | The port number of the client that sends the request. |
| host | By default, the value is obtained from request parameters. If no value is obtained from request parameters, the value is obtained from the Host header. If no value is obtained from request parameters or the Host header, the IP address of the backend server that processes the request is used as the value. |
| http host _ | The Host header of the HTTP request. |
| http referer _ | The Referer header of the HTTP request. |
| http user agent _ _ | The Http User Agent header of the HTTP request. _ _ |
| http x forwarded for _ _ _ | The X-Forwarded-For header of the HTTP request. |
| http x real ip _ _ _ | The real client IP address. |
| read request time _ _ | The amount of time that SLB takes to process the request. Unit: milliseconds. |

| request length _ | The length of the request, including the start line, request headers, and the request body. |
|---|---|
| request method _ | The request method. |
| request time _ | The duration between the time when SLB receives the first request and the time when SLB returns the response. Unit: seconds. |
| request uri _ | The uniform resource identifier (URI) of the request. |
| scheme | The scheme of the request. Valid values: HTTP and HTTPS. |
| server protocol _ | The version of the HTTP protocol that is received by the SLB instance. Examples: HTTP/1.0 and HTTP/1.1. |
| slb vport _ | The listener port of the SLB instance. |
| slbid | The ID of the SLB instance. |
| ssl cipher _ | The cipher suite that is used to establish the SSL-VPN connection. Example: ECDHE-RSA-AES128-GCM-SHA256. |
| ssl protocol _ | The protocol that is used to establish the SSL-VPN connection. Example: TLS 1.2. |
| status | The status of the response that is returned by the SLB instance. |
| tcpinfo rtt _ | The amount of time that is taken to establish a TCP connection. Unit: microseconds. |
| time | The time when the log entry was generated. |
| upstream addr _ | The IP address and port of the backend server. |
| upstream response ti _ _ me | The amount of time from when a connection is established between the SLB instance and the backend server to when the connection is closed. Unit: seconds. |
| upstream status _ | The HTTP status code sent from the backend server to the SLB instance. |
| vip addr _ | The virtual IP address. |

| write response time _ _ | The amount of time that is required to respond to the write request. Unit: milliseconds. |
|---|---|

For example, you can enter the following SQL statement to query the top 20 most active clients. You can analyze the request sources and make informed business decisions.

```
* | select http_user_agent, count(*) as pv group by http_user_agent order by pv desc
limit 20
```

**Disable the access log feature**

If you no longer need to collect the access logs of your SLB instance, you can disable the access log feature.
1. On the **Access Log** page, find the SLB instance that you want to manage and click **Delete**
in the **Actions** column.
2. In the message that appears, click **OK**.
Disabling the access log feature does not delete the corresponding SLS project or Logstore.

### 4.5 Access control

#### 4.5.1 Access control overview

This topic describes how to enable access control for a listener. You can enable access control for each listener of a Server Load Balancer (SLB) instance. After you create a listener, you can enable or disable access control, configure an access control list (ACL), or modify access control configurations for the listener.

**ACL overview**

You can set whitelists or blacklists for different listeners. Whitelist: Only requests from the IP addresses or CIDR blocks on the whitelist are forwarded. Whitelists apply to scenarios in which you want to allow requests only from specific IP addresses. Risks may arise if the whitelist is improperly configured. After a whitelist is configured, the SLB listener is accessible only from IP addresses that are on the whitelist. If you configure a whitelist but do not add an IP address to the whitelist, the listener forwards all requests. Blacklist: All requests from the IP addresses or CIDR blocks on the blacklist are denied. Blacklists apply to scenarios in which you want to block access from specific IP addresses. If you configure a blacklist but do not add an IP address to the blacklist, the listener forwards all requests.

**Limits**

Apsara Stack allows you to adjust ACL quotas. For more information, see Adjust ACL quotas.

| Item | Default value | Quota name |
|---|---|---|
| Maximum number of ACLs that can be configured by each Apsara Stack tenant account | 50 | max acl number per region _ _ _ _ |

| Maximum number of ACLs that can be associated with each listener | 3 | maxaclsizekey |
|---|---|---|
| Maximum number of ACL entries that can be associated with each listener | 900 | maxaclentrykey |
| Maximum number of entries that can be added to each ACL | 300 | acl entry quota _ _ |
| Maximum number of times that each ACL can be associated with different listeners | 50 | acl max vip quota _ _ |
| Maximum number of entries that can be added to an ACL in each call | 20 | acl max entry per request |

**Procedure**

The following figure shows how to configure an ACL for a listener.

#### 4.5.2 Create and manage ACLs

Server Load Balancer (SLB) supports access control lists (ACLs) for listeners, which can be used to control access from specific IP addresses and CIDR blocks.

**Create an ACL**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Access**
**Control**.
4. On the **Access Control** page, click **Create ACL**.
5. In the **Create ACL** dialog box, configure the parameters and click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Organization | The organization to which the ACL belongs. |
| Resource Set | The resource set to which the ACL belongs. |
| ACL Name | The name of the ACL. |

| IP Version | The IP version of the ACL. Valid values: IPv4 IPv6 |
|---|---|
| Add Multiple Addresses/CIDR Blocks and Descriptions | Enter ACL entries. Note Enter one entry per line. Press the Enter key to start a new line. In each entry, separate the IP address or CIDR block and its description with a vertical bar (\|). Example: 192.168.1.0/24\|Description. You can add at most 20 entries at a time. ACL entries cannot contain space characters or carriage returns. |

**What to do next**

**View existing ACLs**

On the **Access Control** page, you can view the existing ACLs. Enter a keyword or click **Advanced Filter** to search for ACLs that meet the specified conditions. Click the icon in the upper-right corner to specify the columns that you want to show or hide and adjust the order of the columns by dragging them. Click the ID in the **Associated Listener** column to view the details of the SLB instances associated with the ACL.

**Modify the name of an ACL**

1. On the **Access Control** page, find the ACL whose name you want to modify, move the
pointer over the ACL name in the **ACL Name/ID** column, and then click the icon.
2. In the dialog box that appears, modify the **ACL Name** parameter and click **OK**.
The name must be 1 to 80 characters in length, and can contain letters, digits, forward slashes (/), periods (.), underscores (_), and hyphens (-). It must start with a letter.

**Add IP entries to an ACL**

1. On the **Access Control** page, find the ACL that you want to manage and click its ID in the
**ACL ID/Name** column. Alternatively, click **Actions** in the **Manage** column.
2. On the page that appears, add IP entries to the ACL.
If you add an entry for an IP address or a CIDR block that already exists, the entry is ignored. Click **Add Entry**. In the **Add ACL Entry** dialog box, configure the **IP Address/CIDR**
**Block** and **Description** parameters and click **OK**.
You can add a single IP address, such as 192.168.1.1 or 192.168.1.1/32. You can add a single CIDR block, such as 192.168.1.0/24. Click **Add ACL Entries**. In the **Add Multiple Entries** dialog box, configure the **Add**
**Multiple Addresses/CIDR Blocks and Descriptions** parameter and click **OK**.
Enter one entry per line. Press the Enter key to start a new line. In each entry, separate the IP address or CIDR block and its description with a vertical bar (**|**). Example: **192.168.1.0/24|Description**. You can add at most 20 entries at a time. ACL entries cannot contain space characters or carriage returns. Click **Import**. In the **Import** dialog box, click **Download Template**, specify the template information, and then click **Next**. You can add at most 20 entries at a time. ACL entries cannot contain space characters or carriage returns.

**Export IP entries from an ACL**

1. On the **Access Control** page, find the ACL that you want to manage and click the ACL ID in
the **ACL ID/Name** column or **Actions** in the **Manage** column.
2. On the page that appears, click **Export** to export IP entries.

**Remove IP entries from an ACL**

1. On the **Access Control** page, find the ACL that you want to manage and click the ACL ID in
the **ACL ID/Name** column or **Actions** in the **Manage** column.
2. On the page that appears, find the IP entry that you want to remove and click **Delete** in the
**Actions** column. Alternatively, select the IP entries that you want to remove and click
**Delete** in the lower-left corner.
3. In the message that appears, click **Delete**.

**Delete an ACL**

1. On the **Access Control** page, find the ACL that you want to delete and click **Actions** in the
**Actions** column.
2. In the **Delete** message, click **OK**.
3. In the message that appears, confirm the high-risk operation and click **Delete**.

**Manage tags**

On the Access Control page, you can add tags to ACLs for management. For more information, see Manage tags.

#### 4.5.3 Adjust the quota on ACLs

Server Load Balancer (SLB) allows you to increase the quota on access control lists (ACLs) to thousands of entries. This topic describes how to increase the quota on ACLs.

**Step 1: Confirm the name of the cluster to which the instance**

**belongs**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, click **Service Management**.
4. Select **webapp-rule** from the **Service** drop-down list.
5. On the **Service Instances** tab, view the name of the **StandardCloudCluster** cluster **to**
**which the instance belongs**.

**Step 2: Obtain the openapi.endpoint**

1. In the left-side navigation pane, choose **Resources** > **Product & Cluster O&M**.
2. In the **Product | Cluster** search box, enter the name of the cluster that you want to search
for, click **Show Cluster** in the Actions column, and then click **Cluster Details**.
3. On the **Cluster Details** page, click the **Resource Details** tab.
4. In the **Resource Name** search box, enter **rule** to search for resources whose name is **rule**
and type is **dns**.
5. In the **Resource Application Result** column, click the
icon.
6. Click the information in the column. In the **Resource Application Result** message, view
the value of the **dns** parameter, which is the **openapi.endpoint**.

**Step 3: Adjust the quota**

1. In the address bar of your browser, enter the **openapi.endpoint**, append the suffix
**/ruleConfig**, and then press the Enter key to go to the **rule configuration center**.
2. To quickly find the quota parameter that you want to modify, enter the quota parameter in
the **action** search box and click **Search**. The default quota parameters are not displayed. If you cannot find the quota parameter that you want to modify, you must add the quota first. After you add the quota, you can modify the parameters. For more information, see Step 4: Add a quota.
3. Find the **action** and click **Modify** in the **Actions** column.
4. On the Modify Configurations page, modify the **configuration** parameters and click
**Modify**. For more information about the **configuration** parameters, see Limits.

**(Optional) Step 4: Add a quota**

1. In the address bar of your browser, enter the **openapi.endpoint**, append the suffix
**/ruleConfigInsert**, and then press the Enter key**.**
2. On the page that appears, configure the parameters to add a quota. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Configuration Type | Valid values: expr class config *expr pro _ |
| Service code | Enter the service name. |
| action | Enter the action that you want to perform. |
| User Type | Select a user type. Valid values: default usr id _ bid tag Note You can select a user type to modify the configurations for a user that has a specific UID, BID, or tag. The default value is default, which specifies that the configurations are applied globally. |
| Specification | Enter a quota. |
| Variable Type | Specify a data type for the variables in the specification. This parameter is optional. |
| Variables Requiring Thread Count | Enter the variables that need to calculate the number of threads. This parameter is optional. |
| Error Code | Enter an error code. This parameter is optional. |

| Description | Enter a description. This parameter is optional. |
|---|---|
| Simultaneous Cache Update | Specify whether to simultaneously update the cache when you add the quota. By default, this feature is enabled. |

3. Click **Add**.

### 4.6 Operation logs

Server Load Balancer (SLB) allows you to view the operation log of an SLB instance, which records the instance status, operation source, operation time, and API call details. You can analyze and trace historical operations based on the operation data.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. Use the following method to view the operation logs of an SLB instance.
In the left-side navigation pane, choose **Classic Load Balancer (CLB) > Operation**
**Log**.
View the operation logs of a single SLB instance on the instance management details page. a. From the navigation pane on the left, choose **Classic Load Balancer (CLB) >**
**Instances**.
b. On the **Instances** page, find the target instance, then click its instance ID in the
**Instance ID/Instance Name** column, or click **Manage** in the **Actions** column.
c. On the instance management details page, click the **Operation Logs** tab. Operation logs are retained for seven days. To adjust the retention period, modify the logging configurations in Configurations > Log Storage Settings as an administrator. If you extend the retention period by modifying the logging configurations, the log data before the modification is not backfilled. The list can display up to 10,000 records across 100 pages. If the number of records exceeds 10,000, use filters to display the data you need.
4. **Optional.** You can filter operation records by filter conditions such as **Operation Name**
and **Operator**. The following table describes the filter conditions.

| Filter condition | Description |
|---|---|
| Operator | Enter the operator that performed the operation. |
| Operation Name | Enter the name of the operation, which is the API operation name. |

| Execution Status | Select Success or Failed. |
|---|---|
| Operation Source IP Address | Enter the source IP address of the operation. |
| Operation Time | Select a time range to query. |

5. **Optional.** Find the operation that you want to view and click **Operation Details** in the
**Operation** column to view the operation details.

### 4.7 Tag management

#### 4.7.1 Overview

Server Load Balancer (SLB) provides the tag management feature. You can use tags to mark and classify SLB resources. This way, you can search for and manage the resources by tag.

**Tag overview**

Tags are used to mark resources. Each tag consists of a key and a value. Before you use tags, take note of the following limits: SLB instances and access control lists (ACLs) support tag management. You can modify the key and value of a tag or remove a tag from a resource. If you delete a resource, all tags added to the resource are removed. This operation does not affect the tags added to other resources. The key of each tag added to the same resource must be unique. If you add a tag that uses the same key as an existing tag, the new tag overwrites the existing tag. At most 10 tags can be added to a resource. You can add or remove a maximum of five tags at a time. Tags cannot exist as an independent resource. If you create a tag, it must be added to a resource.

#### 4.7.2 Add tags

Server Load Balancer (SLB) allows you to add tags. You can add tags to a single resource or add tags to multiple resources at a time. This topic describes how to add tags to SLB instances. The method of adding tags to access control lists (ACLs) is similar to that of adding tags to SLB instances.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Perform the following operations to add tags to SLB instances:
Add tags to a single SLB instance a. On the **Instance Management** page, find the SLB instance that you want to manage, move the pointer over the **Tag** column, and then click the icon. b. In the **Edit Tags** dialog box, configure the parameters that are described in the following table and click **OK**. You can click **Add** to add more tags.

| Param eter | Description |
|---|---|
| Tag Key | The key of the tag. You can select or enter a tag key. The tag key can be up to 64 characters in length and cannot start with aliyun or acs: . The tag key cannot contain http:// or https:// . |
| Tag Value | The value of the tag. You can select or enter a tag value. The tag value can be up to 128 characters in length and cannot start with aliyun or acs: . The tag value cannot contain http:// or https:// . |

c. In the **Edited** message, confirm the tag information and click **Close**. Add tags to multiple SLB instances at a time a. On the **Instance Management** page, select the SLB instances that you want to manage, move the pointer over More in the lower-left corner, and then select **Batch**
**Add Tags**.
b. In the **Batch Add Tags** dialog box, configure the **Tag Key** and **Tag Value** parameters and click **OK**. c. In the **Edited** message, confirm the tag information and click **Close**.

#### 4.7.3 Remove tags

Server Load Balancer (SLB) allows you to remove tags. You can remove tags from a single resource or remove tags from multiple resources at a time. This topic describes how to remove tags from SLB instances. The method of removing tags from access control lists (ACLs) is similar to that of removing tags from SLB instances.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Instances**.
4. Perform the following operations to remove tags from SLB instances:
Remove tags from a single SLB instance a. On the **Instance Management** page, find the SLB instance that you want to manage, move the pointer over the **Tag** column, and then click the icon. b. In the **Edit Tags** dialog box, click the icon next to the tag that you want to remove and click **OK**. c. In the **Edited** message, confirm the tag information and click **Close**. Remove tags from multiple SLB instances at a time a. On the **Instance Management** page, select the SLB instances that you want to manage, move the pointer over More in the lower-left corner, and then select **Batch**
**Remove Tags**.
b. In the **Batch Remove Tags** dialog box, select the tags that you want to remove in the
**Tags to Remove** section and click **OK**.
c. In the **Edited** message, confirm the tag information and click **Close**.

#### 4.7.4 Search for resources by tag

After you add tags to Server Load Balancer (SLB) instances or access control lists (ACLs), you can quickly search for the resources by tag. This topic describes how to search for resources by tag.

**Procedure**

1. Log on to the SLB console.
2. In the top navigation bar, select the region where the Classic Load Balancer (CLB) instance
is located.
3. Search for resources by tag based on your business requirements.
Search for SLB instances by tag a. From the navigation pane on the left, choose **Classic Load Balancer (CLB) >**
**Instances**.
b. On the **Instance Management** page, select **Tag** from the drop-down list and select tag keys and tag values in the dialog box that appears. Search for ACLs by tag a. From the navigation pane on the left, choose **Classic Load Balancer (CLB) > Access**
**Control**.
b. On the **Access Control** page, click **Advanced Filter** and then click the **Tag** dropdown list.
4. In the dialog box that appears, select tag keys and tag values in the **Tag Key** and **Tag**
**Value** sections. Then, click **Search**.
The resources with the specified tag keys and tag values are displayed.

## 5 Quick links

Quick links let you quickly open the consoles of related products and manage them. SLB provides quick links to the following products: VPC EIP Express Connect CEN Alibaba Cloud DNS cross-cloud DNS ECS Auto Scaling
