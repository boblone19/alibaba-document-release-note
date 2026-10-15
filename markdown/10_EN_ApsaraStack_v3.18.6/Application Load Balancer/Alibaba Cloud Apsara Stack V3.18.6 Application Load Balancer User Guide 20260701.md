---
title: "Application Load Balancer User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 136
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Application Load Balancer User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BA%94%E7%94%A8%E5%9E%8B%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1ALB/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Application%20Load%20Balancer%20User%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Application Load Balancer User Guide 20260701

Application Load Balancer User G

## Log in to the ALB console

This topic describes how to navigate to the Application Load Balancer (ALB) console after you log in to the Apsara Uni-manager Management Console by using Google Chrome.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. Application Load Balancer User G

**Note**

You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button. If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

**Note**

Obtain the username and password from an operations administrator. The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**.

**Note**

For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in Apsara Uni-manager Management Console User Guide.
5. In the top menu bar, click **Products > Network > Server Load Balancer (SLB)**.
Application Load Balancer User G

## Quick start

### Overview

This topic describes how to create an Application Load Balancer (ALB) instance to distribute client requests to two backend Elastic Compute Service (ECS) instances.

**Note**

Before you create an ALB instance, you must determine the configurations of the ALB instance, such as the region, type, and specifications. For more information, see Preparations. This topic includes the following operations: Create an ALB instance. An ALB instance is an entity that provides load balancing services. After you create an ALB instance, you must add listeners and backend services to the ALB instance. If you no longer need the ALB instance, you can release it.

### Preparations

Before you create an Application Load Balancer (ALB) instance, you must determine the configurations of the ALB instance, such as the listener type and network type.

**Select a region to deploy an ALB instance**

When you select a region, take note of the following items: To reduce the network latency and accelerate data transmission, we recommend that you select the region that is nearest to your users. To provide more stable and reliable load balancing services, ALB supports primary/secondary zone deployment in most regions. You can select more than one zone to implement zone-disaster recovery. We recommend that you select a region that supports primary/secondary zone deployment. ALB does not support cross-region deployment. Therefore, you must deploy the ALB instance and backend Elastic Compute Service (ECS) instances in the same region.

**Select the network type of the ALB instance (Internet-facing or**

**internal-facing)**

ALB provides Internet-facing and internal-facing load balancing services: If you want to use ALB to distribute requests from the Internet, create an Internet-facing ALB instance. An Internet-facing ALB instance is assigned a public IP address to receive requests from the Internet. If you want to use ALB to distribute requests from the internal network, create an internalfacing ALB instance.

| Specification | Maximum concurrent connections | New connections per second (CPS) | QPS |
|---|---|---|---|
| Small I (slb.s1.small) | 5,000 | 3,000 | 1,000 |
| Medium I (slb.s2.small) | 10,000 | 5,000 | 5,000 |
| Medium II (slb.s2.medium) | 100,000 | 10,000 | 10,000 |
| Large I (slb.s3.small) | 200,000 | 20,000 | 20,000 |
| Large II (slb.s3.medium) | 500,000 | 50,000 | 30,000 |
| Super Large I (slb.s3.large) | 1,000,000 | 100,000 | 50,000 |

Application Load Balancer User G An internal-facing ALB instance is assigned only a private IP address. It is only accessible over the internal network and is not accessible over the Internet.

**Select specifications for your ALB instance**

To ensure service availability, the following instance specifications are available.

**Note**

The available specifications vary based on the actual scenario. The preceding table is for reference only.

**Select a listener protocol**

Before you use ALB, you must create ECS instances that function as backend servers, deploy applications on the ECS instances, and then add the ECS instances to your ALB instance to process client requests. When you create ECS instances, take note of the following items: Region and zones of the ECS instances Make sure that the ECS instances are deployed in the same region as the ALB instance. In this example, an ECS instance named ECS01 and an ECS instance named ECS02 are created in the **China (Hangzhou)** region. Application configurations In this example, two static web pages are hosted on ECS01 and ECS02 by using Apache. Application Load Balancer User G Enter the elastic IP address (EIP) that is associated with ECS01 in the address bar of your browser. Enter the EIP that is associated with ECS02 in the address bar of your browser. No additional configurations are required after you deploy applications on the ECS instances. If you want to use a Layer 4 (TCP or UDP) listener and your ECS instances run Linux, make sure that the following parameters in the net.ipv4.conf file of the /etc/sysctl.conf directory are set to 0:

```
net.ipv4.conf.default.rp_filter = 0 net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.eth0.rp_filter = 0
```

### Create an ALB instance

An Application Load Balancer (ALB) instance is an entity that provides load balancing services.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, click **Create Instance**.
5. On the **Create an ALB instance** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | Select the organization in which you want to create the ALB instance. |
| Resource Set | Select the resource set in which you want to create the ALB instance. |
| Region | Select the region in which you want to create the ALB instance. |
| Instance Name | Enter a name for the ALB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, full-width characters, hyphens (-), colons (:), periods (.), and underscores ( ). It _ must start with a letter. |
| Network Configuration |  |
| Network Type | Select a network type. By default, Intranet is selected. Intranet: The ALB instance has only private IP addresses and can be accessed only by resources in the VPC where the ALB instance is deployed. Internet: The ALB instance has public and private IP addresses. By default, Internet-facing ALB instances use elastic IP addresses (EIPs) to provide services over the Internet. |
| VPC | Select the VPC in which you want to deploy the ALB instance. Note You can click Create a VPC to create a VPC. The VPC is available after you refresh the list. |
| Zone | Select a zone, vSwitch, and cluster. Zone: Select a zone. VSwitch: Select a vSwitch in the selected zone. Cluster: Select a cluster. |
| Specifications | Select the specifications of the ALB instance. The performance metrics vary depending on the instance specifications. For more information, see the ALB instance specifications section of the Instance overview topic. |
| IP Mode | Select an IP mode. By default, Fixed IP is selected. |

Application Load Balancer User G

| Protocol Version | Select an IP version for the ALB instance. By default, IPv4 is selected. IPv4: If you select this option, the ALB instance can be accessed only by IPv4 clients. Dual-stack: If you select this option, the ALB instance can be accessed by IPv4 and IPv6 clients. Note To use the dual-stack feature, you must enable the IPv6 feature for the vSwitches in the zones of the VPC. |
|---|---|

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | The organization to which the server group belongs. |

Application Load Balancer User G
6. Create the ALB instance.
If a service is created on the Service Management page and **Application Load Balancer**
**(ALB)** is displayed in the **Cloud resources** column of the service, confirm the
parameters and click **Confirm Order**. If no service whose **Cloud resources** value is **Application Load Balancer (ALB)** exists on the Service Management page, confirm the parameters and click **Submit**.

### Configure listeners and

**backend services**

This topic describes how to add two Elastic Compute Service (ECS) instances named ECS01 and ECS02 to an Application Load Balancer (ALB) instance. These ECS instances function as backend servers that host static web pages. If you associate a server group with a listener, the listener distributes requests only to backend servers in the server group.

**Prerequisites**

ECS instances are created, and applications are deployed on the ECS instances. The ECS instances are created in the same organization as the ALB instance. In addition, security group rules are configured for the ECS instances to allow HTTP requests from port 80 and HTTPS requests from port 443.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, click **Create Server Group**.
5. On the **Create Server Group** page, configure the following parameters.

| Resource Set | The resource set to which the server group belongs. |
|---|---|
| Region | The region to which the server group belongs. |
| Server Group Type | Select the type of server group that you want to create. Server Type: Backend servers are added by specifying Elastic Compute Service (ECS) instances. IP Address Type: Backend servers are added by specifying IP addresses. |
| Server Group Name | The name of the custom server group. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Network Settings |  |
| VPC | Select a virtual private cloud (VPC) from the VPC drop-down list. Only servers in the VPC can be added to the server group. Note You can click Create VPC to create a VPC. The VPC is available after you refresh the list. |
| Scheduling Algorithm | Select a scheduling algorithm. Weighted Round-robin is selected by default. Weighted Round-robin: Backend servers that have higher weights receive more requests than those that have lower weights. Weighted Least Connections: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, requests are forwarded to the backend server that has fewer connections. Consistent Hashing: Only high-performance ALB instances support consistent hashing. |
| Hash Factor | Select a hash factor. Source IP Address: Specify consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. URL Parameters: Requests for the same URL are forwarded to the same backend server. Note This parameter is required only if you set Scheduling Algorithm to Consistent Hashing. |

Application Load Balancer User G

| Backend Protocol | Select the type of the backend protocol. By default, HTTP is selected. HTTP: If you select this option, you can associate the server group with HTTPS, HTTP, or QUIC listeners. HTTPS: If you select this option, you can associate the server group with HTTPS listeners. gRPC: If you select this option, HTTP/2 is used as the communication protocol. You can associate the server group with HTTPS listeners, and HTTP/2 must be enabled for the HTTPS listeners. |
|---|---|
| Advanced Configurations |  |
| IPv6 | Specify whether to allow the addition of IPv6 backend servers to the server group after IPv6 is enabled for the VPC. This feature is disabled by default. If you do not enable this feature, you can add only IPv4 backend servers to the server group. If you enable this feature, you can add IPv4 and IPv6 backend servers to the server group. Note This parameter is available only if IPv6 is enabled for the selectedV PC. |
| Backend Long Link | Specify whether to enable persistent connection. By default, this feature is enabled. After this feature is enabled, a certain number of persistent connections are kept alive between ALB and backend servers. When ALB receives a new request and an idle persistent TCP connection exists, ALB first uses the persistent TCP connection to forward the request to the backend server. This reduces the number of TCP handshakes and the workload on the backend server. |
| Session Persistence |  |
| Enable Session Persistence | Specify whether to enable the session persistence feature. This feature is disabled by default. If this feature is disabled, ALB distributes each client request to a different backend server. If session persistence is enabled, ALB forwards all requests from a client to the same backend server. To enable session persistence, you must specify the cookie handling method. |

Application Load Balancer User G

| Cookie Handling Method | The cookie processing method. Session persistence is implemented based on cookies. To enable session persistence, you must configure the following parameters: Insert Cookie: If you select this option, you need to only specify the timeout period for the cookie. ALB inserts a session cookie (ServerId) into the first HTTP or HTTPS response that is sent to a client. If subsequent requests to ALB carry this cookie, ALB determines the destination servers of the requests based on the cookie. Cookie Timeout Period: If you set Cookie Handling Method to Insert Cookie, specify a timeout period for session persistence. Valid values: 1 to 86400. Unit: seconds. Default value: 1000. Rewrite Cookie: If you select this option, you can specify the cookie that you want to insert into a response. You must specify the timeout period and the lifetime for the cookie on a backend server. If ALB detects a user-defined cookie, ALB replaces the original cookie with the user-defined cookie. If subsequent requests to ALB carry this user-defined cookie, ALB determines the destination servers of the requests based on the cookie. Cookie Configured on Server: Enter the name for a custom cookie if you set Cookie Handling Method to Rewrite Cookie. |
|---|---|
| Slow Start |  |

Application Load Balancer User G

| Enable Slow Start | Specify whether to enable the slow start mode. This feature is disabled by default. After slow start is enabled, the number of requests that ALB forwards to backend servers gradually increases. When the slow start duration ends, the speed of request forwarding between ALB and backend servers is no longer limited, and the backend servers exit the slow start mode. Note This parameter is required only when you set the Scheduling Algorithm parameter to Weighted Round-robin. After you enable the slow start mode, healthy backend servers do not automatically enter the slow start mode. When you enable the slow start mode for an empty server group: The first backend server added to the server group does not enter the slow start mode. New backend servers can enter the slow start mode only when at least one healthy backend server is not in slow start mode. Backend servers that are removed before the slow start duration ends automatically exit the slow start mode. If you re-add the backend server to a server group, the backend server can enter the slow start mode only when the backend server passes health checks. If a backend server is declared unhealthy before the slow start duration ends, the backend server exits the slow start mode. The backend server re-enters the slow start mode when the backend server passes health checks. After you enable the slow start mode and health checks, only healthy backend servers enter the slow start mode. If you disable health checks, all backend servers immediately enter the slow start mode. |
|---|---|
| Slow Start Duration | The slow start duration. Valid values: 30 to 900. Unit: seconds. Default value: 30. Note To enable slow start, you must specify the duration of slow start. |
| Connection Draining |  |

Application Load Balancer User G

| Enable Connection Draining | Specify whether to enable connection draining. This feature is disabled by default. When you remove a backend server or a backend server is declared unhealthy: If you disable connection draining, existing connections remain open until the clients proactively close the connections or the session persistence duration ends. After you enable connection draining, existing connections remain open for data transmission until the connection draining timeout period ends. Connection draining ensures smooth undeployment of services. |
|---|---|
| Connection Draining Timeout Period | The timeout period of connection draining. Valid values: 0 to 900. Unit: seconds. Default value: 300. Note This parameter is required only if you turn on Enable Connection Draining. |
| Health Check |  |
| Enable Health Check | Specify whether to enable the health check feature. By default, this feature is enabled. To enable health check, you must configure health check parameters. |
| Health Check Mode | After Enable Health Check is turned on, you need to select a health check mode. Custom is selected by default. Custom: You can customize the health check parameters. Select Template: Select the created health check configurations. |
| Health Check Template | After you turn on Enable Health Check and setH ealth Check Mode to Select Template, select a created health check. After you select a template, you can still customize health check parameters. Health check information includes Health Check ID/Name, Protocol, Port, Interval, Response Timeout Period, Health Threshold, and Unhealth Threshold. Click Advanced Filter and specify Health Check ID or Health Check Name to search for health checks. |

Application Load Balancer User G

| Health Check Protocol | The health check protocol. HTTP: HTTP health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. HTTPS: HTTPS health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. TCP: TCP health checks are performed at the network layer. ALB probes the port of a backend server to check whether the server is healthy by sending SYN packets. gRPC: ALB checks whether a backend server is healthy by sending POST or GET requests. |
|---|---|
| Health Check Method | The health check method. GET: If the size of a response exceeds 8 KB, the response is truncated. The results of the health check are not affected. HEAD: HTTP and HTTPS health checks support the HEAD method. Make sure that your backend server supports HEAD requests. If your backend server does not support the HEAD method or the HEAD method is disabled, health checks may fail. In this case, you can use the GET method. POST: Only gRPC health checks support the POST method. Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. HTTP and HTTPS health checks use the HEAD method by default. gRPC health checks use the POST method by default. |
| Health Check Protocol Version | The version for the health check protocol. HTTP1.1 HTTP1.0 Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Check Domain Name | The health check domain name. The internal IP address of your backend server is used as the domain name for the health check by default. You can specify a specific domain name. The name can contain only letters, digits, hyphens (-), and periods (.). Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. |

Application Load Balancer User G

| Health Check Port | The port that ALB uses to perform health checks on backend servers. By default, the backend port specified when you configure the listener is used for the health check. We recommend that you leave this parameter empty unless you want to specify a specific port. Valid values: 1 to 65535. |
|---|---|
| Health Check URL | The URL that is used for health checks. By default, ALB performs HTTP health checks by sending HTTP HEAD requests to the private IP address of a backend Elastic Compute Service (ECS) instance to visit the default homepage configured on the ECS instance. If you do not want to use the default homepage for health checks, you can specify a URL. It must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & =. It must start with a forward _ slash (/). Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| HTTP Health Status Code (HTTP and HTTPS) | The status codes that indicate a healthy backend server. You can select multiple options. Default values: http 2xx and http 3xx. Valid _ _ values: http 2xx _ http 3xx _ http 4xx _ http 5xx _ Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Check Status Code (gRPC) | The status codes that indicate a healthy backend server. Valid values: 0 to 99. You can enter up to 20 value ranges. Separate multiple value ranges with commas (,). Note This parameter is required if you set the Health Check Protocol parameter to gRPC. |
| Response Timeout (Seconds) | The timeout period for a response. The maximum timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. Default value: 5. The timeout period for a health check response. If a backend ECS instance does not return a health check response within the specified timeout period, the instance fails the health check. |

Application Load Balancer User G

| Interval (Seconds) | The interval between two consecutive health checks. The interval between two consecutive health checks. Valid values: 1 to 50. Default value: 2. Unit: seconds. |
|---|---|
| Health Threshold | The number of consecutive successful health checks that must occur before an application is declared healthy. Specify the number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. Valid values: 2 to 10. Default value: 3. |
| Unhealth Threshold | The number of consecutive failed health checks that must occur before an application is declared unhealthy. Specify the number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. Valid values: 2 to 10. Default value: 3. |

Application Load Balancer User G
6. Click **Submit**.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
5. On the **Details** page, click the **Backend Server** tab.
6. Add backend servers based on your business requirements.
a. Click **Add Backend Server** to open the **Add Backend Server** panel. b. In the **Select Server** step, select the ECS instance that you want to add and click **Next**
**Step**.
The server information includes **Instance ID/Name** and **IP Address**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** You can enter a server name for fuzzy search of the destination server.**Server Name** Click an ID in the **Instance ID/Name** column to view the details of the ECS instance. Application Load Balancer User G c. In the **Port and Weight** step, configure ports, weights, and descriptions for all backend servers, and click **OK**.
**Port**: Specify the backend port that the ECS instance uses to receive requests.

**Note**

You can configure multiple backend ports. Valid values: 1 to 65535.
**Weight**: Specify the percentage of requests that the ALB instance distributes to the
backend server. Default value: 100.

**Note**

An ECS instance of a greater weight receives more requests. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive new requests.
**Description**: the description of the backend server.
The value must be 2 to 256 characters in length and can contain letters. It cannot start with http:// or https://. a. Click **Add IP Address** to open the **Add Backend Server** panel. b. In the **Select Server** step, configure an IP address and a remote IP address for the backend server, and then click **Next Step**.
**IP Address**: Enter the IP address of the backend server.
You can click **Add** to add an additional IP address. The format of the IP address, such as 192.168.0.0/16. To delete an IP address, click **Delete** in the **Actions** column.
**Remote IP Address**: An ALB instance can be associated with backend servers that
have IP addresses in different VPCs. If the specified IP address does not belong to the VPC of the current server group, select **Enable Remote IP Address**.

**Note**

You can specify multiple ports and weights for an IP address. If the remote IP address is disabled, the IP address to be added must fall into the CIDR block of the current VPC. If the remote IP address is enabled, you can add private IP addresses that fall into the CIDR block. Application Load Balancer User G c. In the **Port and Weight** step, configure ports, weights, and descriptions for all backend servers, and click **OK**.
**Port**: Specify the backend port that the ECS instance uses to receive requests.

**Note**

You can configure multiple backend ports. Valid values: 1 to 65535.
**Weight**: Specify the percentage of requests that the ALB instance distributes to the
backend server. Default value: 100.

**Note**

An ECS instance of a greater weight receives more requests. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive new requests.
**Description**: the description of the backend server.
The value must be 2 to 256 characters in length and can contain letters. It cannot start with http:// or https://.
7. Optional. On the **Backend Server** tab, you can view the list of backend servers that have
been added. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

**Configure a listener**

Take HTTP as an example.

**Step 1: Open the ALB configuration wizard**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to go to the **ALB Configuration Wizard** page.
On the **Instance Management** page, find the target instance and click **Create Listener** in the **Actions** column. On the Listener tab:

| Parameter | Description |
|---|---|
| Instance ID | The ID of the ALB instance is displayed. |
| Select Listener Protocol | Select a protocol for the listener. In this example, select HTTP. |
| Listener Port | Select the port on which the ALB instance listens. The ALB instance listens on the port and forwards requests to backend servers. Valid values: 1 to 65535. Generally, HTTP uses port 80. Note On the same ALB instance, the ports of listeners that use the same protocol must be unique. HTTP listeners and HTTPS listeners must use different ports. |
| Listener Name | Enter a name for the listener. |
| Idle Connection Timeout Period (s) | The timeout period for idle connections. Valid values: 1 to 60. Unit: seconds. Default value: 15. If no request is received within the specified timeout period, ALB temporarily terminates the connection. When a request is received, ALB creates a new connection. |

Application Load Balancer User G a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. Click **Create Listener**.

**Step 2: Configure a listener**

In the **Configure Listener** step, configure the parameters and click **Next Step**.

| Connection Request Timeout Period (s) | The connection timeout period. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no backend server responds to the connection request within the specified timeout period, ALB returns the HTTP 504 status code to the client. |  |  |
|---|---|---|---|
| Data Compression | Specify whether to enable data compression. By default, this feature is enabled. If you enable this feature, files of specific types are compressed. If you disable this feature, no file is compressed. Currently, Brotli supports all types of files. Gzip supports the following types of files: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, application/xml, and application/json. Note If a client request supports both the Brotli and Gzip compression algorithms, ALB preferentially uses the more efficient Brotli compression algorithm. If a client supports only the Gzip compression algorithm but the file type is not supported by Gzip, ALB does not perform compression. |  |  |
| Retrieve Client IP Address | Specify whether to retrieve the real source IP address of the client. This feature is disabled by default. If this feature is enabled, ALB can retrieve client IP addresses from the X- Forwarded-For header. |  |  |
| Configure Trusted IP Addresses | Configure trusted IP addresses and separate them with semicolons (;). If you set the trusted IP address list to 0.0.0.0/0 , the ALB instance retrieves the leftmost IP address in the X-Forwarded-For header. The IP address is the source client IP address. If you set the trusted IP address list in the format of proxy1 IP;proxy2 IP;... , the ALB instance compares the IP addresses in the X- Forwarded-For header from right to left against the trusted IP address list. The first IP address that is not in the trusted IP address list is considered the source client IP address. Note This parameter is required if you turn on Retrieve Client IP Address. |  |  |
|  |  | proxy1 IP;proxy2 |  |

| re Trusted IP | IP;... |
|---|---|

Application Load Balancer User G

| Use X-Forwarded-For Header to Retrieve Client IP Addresses | Specify whether to use the X-Forwarded-For header to obtain the real IP address of the client. By default, this feature is enabled. If this feature is enabled, ALB adds the X-Forwarded-For header to or removes the X-Forwarded-For header from requests before ALB forwards requests to backend servers. If this feature is disabled, ALB does not make any changes to the X- Forwarded-For header in requests before forwarding requests to backend servers. |
|---|---|
| X-Forwarded-For Header Mode | Select the X-Forwarded-For header mode. By default, Add (ALB adds the IP address of the last hop to the X-Forwarded-For header in the request before ALB forwards the request to a backend server.) is selected. Valid values: Add (ALB adds the IP address of the last hop to the X- Forwarded-For header in the request before ALB forwards the request to a backend server.) Remove (ALB removes the X-Forwarded-For header from the request before ALB forwards the request to a backend server, no matter whether the request contains the X-Forwarded-For header.) |
| Use the SLB-ID header to retrieve ALB instance IDs | Select the HTTP headers that you want to add based on your business requirements. |
| Use the X- Forwarded-Proto header to retrieve the listener protocol of the ALB instance. |  |
| Use the X- Forwarded-Port header to retrieve the listener port of the ALB instance. |  |
| Use the X- Forwarded-Host header to retrieve the domain name of a client. |  |
| Use the X- Forwarded-Client- srcport header to retrieve the port of a client. |  |

Application Load Balancer User G In the **Select Server Group** step, select a **Server Group** and click **Next Step**. Application Load Balancer User G The information about a server group includes **Server Group ID/Name**, **Type**, **Backend**
**Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

**Step 4: Submit the configurations**

In the **Review Configuration** step, confirm the configurations, and then click **Submit**. The configurations of an HTTP listener include **Basic Configurations**, **Add HTTP Header**, and **Server Group**.

**Test the ALB service**

Enter the IP address of the ALB instance in the address bar of a browser to test the load balancing performance of the ALB instance. Figure 1: ECS01 Figure 2: ECS02

### Release an ALB instance

This topic describes how to release an Application Load Balancer (ALB) instance. The backend Elastic Compute Service (ECS) instances are not deleted or affected after you release an ALB instance. Application Load Balancer User G

**Procedure**

**Note**

Before you release an ALB instance, you must disable deletion protection.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the target instance and click **Release** in the
**Actions** column.
5. In the **Release Instance** message, click **OK**.

| Term | Description |
|---|---|
| Instance | ALB provides ultra-high Layer 7 processing capabilities and can increase the service capacity of your applications by distributing network traffic across different backend servers. Each ALB instance supports up to 1 million queries per second (QPS). |
| Listener | A listener is the smallest configurable unit of ALB. Listeners listen for requests over the protocols and ports that you configure. For example, you can configure a listener of ALB to process HTTP requests on port 80. You must add at least one listener to each ALB instance before the ALB instance can distribute network traffic. By default, you can add up to 50 listeners to each ALB instance to distribute network traffic for different workloads. |
| Forwarding rule | ALB distributes requests to backend servers in one or more server groups based on forwarding rules. ALB provides advanced routing features. In addition to the basic routing features, you can specify conditions such as the HTTP header, cookie, and HTTP method in a forwarding rule to route network traffic to different backend servers. |
| Server group | Backend servers can be organized into logical groups (also known as server groups) to which requests are distributed. Each server group contains one or more backend servers that process requests distributed by ALB. Server groups of ALB are independent of ALB. You can associate a server group with different ALB instances. By default, you can specify up to 100 backend servers in each server group. ALB supports multiple types of backend servers, such as Elastic Compute Service (ECS) instances, elastic network interfaces (ENIs), and IP addresses. |
| Health check | ALB checks the availability of backend servers by performing health checks. If a backend server is declared unhealthy, ALB does not forward requests to the backend server. ALB supports flexible health check configurations. For example, you can specify the protocol, port, and thresholds for health checks. ALB provides health check templates that can be applied to different server groups. |

Application Load Balancer User G

## ALB

### Instance management

#### Instance overview

Application Load Balancer (ALB) is developed for Layer 7 load balancing over HTTP, HTTPS, and QUIC and provides advanced routing features.

**ALB components**

image.png

**ALB instance types**

Apsara Stack provides Internet-facing and internal-facing ALB instances. You can configure Internet-facing or internal-facing ALB instances based on your business scenarios.

**Internet-facing ALB instance**

**Internal-facing ALB instance**

| Specification | Maximum concurrent connections | New connections per second (CPS) | QPS |
|---|---|---|---|
| Small I (slb.s1.small) | 5,000 | 3,000 | 1,000 |
| Medium I (slb.s2.small) | 10,000 | 5,000 | 5,000 |
| Medium II (slb.s2.medium) | 100,000 | 10,000 | 10,000 |
| Large I (slb.s3.small) | 200,000 | 20,000 | 20,000 |
| Large II (slb.s3.medium) | 500,000 | 50,000 | 30,000 |
| Super Large I (slb.s3.large) | 1,000,000 | 100,000 | 50,000 |

| Parameter | Description |
|---|---|
| Basic Information |  |

Application Load Balancer User G

**ALB instance specifications**

**Note**

The available specifications vary based on the actual scenario. The preceding table is for reference only.

#### Create an ALB instance

An Application Load Balancer (ALB) instance is an entity that provides load balancing services. ALB provides powerful Layer 7 processing capabilities and can increase the service capacity of your applications by distributing network traffic across different backend servers. This topic describes how to create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, click **Create Instance**.
5. On the **Create an ALB instance** page, configure the following parameters.

| Organization | Select the organization in which you want to create the ALB instance. |
|---|---|
| Resource Set | Select the resource set in which you want to create the ALB instance. |
| Region | Select the region in which you want to create the ALB instance. |
| Instance Name | Enter a name for the ALB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, full-width characters, hyphens (-), colons (:), periods (.), and underscores ( ). It _ must start with a letter. |
| Network Configuration |  |
| Network Type | Select a network type. By default, Intranet is selected. Intranet: The ALB instance has only private IP addresses and can be accessed only by resources in the VPC where the ALB instance is deployed. Internet: The ALB instance has public and private IP addresses. By default, Internet-facing ALB instances use elastic IP addresses (EIPs) to provide services over the Internet. |
| VPC | Select the VPC in which you want to deploy the ALB instance. Note You can click Create a VPC to create a VPC. The VPC is available after you refresh the list. |
| Zone | Select a zone, vSwitch, and cluster. Zone: Select a zone. VSwitch: Select a vSwitch in the selected zone. Cluster: Select a cluster. |
| Specifications | Select the specifications of the ALB instance. The performance metrics vary depending on the instance specifications. For more information, see the ALB instance specifications section of the Instance overview topic. |
| IP Mode | Select an IP mode. By default, Fixed IP is selected. |

Application Load Balancer User G

| Protocol Version | Select an IP version for the ALB instance. By default, IPv4 is selected. IPv4: If you select this option, the ALB instance can be accessed only by IPv4 clients. Dual-stack: If you select this option, the ALB instance can be accessed by IPv4 and IPv6 clients. Note To use the dual-stack feature, you must enable the IPv6 feature for the vSwitches in the zones of the VPC. |
|---|---|

Application Load Balancer User G
6. Create the ALB instance.
If a service is created on the Service Management page and **Application Load Balancer**
**(ALB)** is displayed in the **Cloud resources** column of the service, confirm the
parameters and click **Confirm Order**. If no service whose **Cloud resources** value is **Application Load Balancer (ALB)** exists on the Service Management page, confirm the parameters and click **Submit**.

#### Manage ALB instances

##### Modify the name of an ALB instance

You can modify the name of an Application Load Balancer (ALB) instance. Before you modify the name of an ALB instance, you must disable modification protection for the instance.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. Modification protection is disabled for the ALB instance. For more information, see Configure modification protection.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the edit window.
On the **Instance Management** page, find the instance that you want to manage and click the icon to the right of the instance name in the **Instance ID/Name** column. On the instance details page: a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. In the **Basic Information** section of the **Instance Details** tab on the **Details** page, click the icon next to **Instance Name**.
5. In the **Modify Name** dialog box, modify the **Name** parameter and click **OK**.
Application Load Balancer User G The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

##### Modify deletion protection

After an Application Load Balancer (ALB) instance is created, you can modify deletion protection for the instance. After deletion protection is enabled for an instance, the instance cannot be released.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the edit page.
On the **Instance Management** page, find the instance that you want to manage and turn on or turn off the switch in the **Deletion Protection** column. On the instance details page: a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. In the **Basic Information** section of the **Instance Details** tab on the **Details** page, turn on or turn off the switch below **Deletion Protection**.
5. In the **Modify Deletion Protection** message, click **OK**.

##### Configure modification protection

After an Application Load Balancer (ALB) instance is created, you can configure the modification protection feature for the instance. After the modification protection feature is enabled, you cannot modify the instance name, create listeners, change the configurations, or change the network type.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to configure modification protection:
On the **Instance Management** page, find the instance that you want to manage and turn on or turn off the switch in the **Configuration Read-only Mode** column. On the instance details page: a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
Application Load Balancer User G b. In the **Basic Information** section of the **Instance Details** tab on the **Details** page, turn on or turn off the switch below **Configuration Read-only Mode**.
5. In the **Configuration Read-only Mode** message, click **OK**.

##### Release an instance

You can release Application Load Balancer (ALB) instances based on your business requirements. After an ALB instance is released, the configurations and data of the ALB instance are deleted and cannot be restored.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. Deletion protection is disabled for the ALB instance. For more information, see Modify deletion protection.

**Procedure**

**Note**

Before you release an ALB instance, you must disable deletion protection.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the target instance and click **Release** in the
**Actions** column.
5. In the **Release Instance** message, click **OK**.

#### Modify the configurations of ALB

**instances**

You can upgrade or downgrade Application Load Balancer (ALB) instances based on their performance metrics. This topic describes how to modify the configurations of ALB instances. Before you modify the configurations of an ALB instance, you must disable modification protection for the instance.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. Modification protection is disabled for the ALB instance. For more information, see Configure modification protection.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the configuration modification page.
Application Load Balancer User G On the **Instance Management** page, find the target instance and click **Change**
**Configuration** in the **Actions** column.
On the instance details page: a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. In the **Basic Information** section of the **Instance Details** tab on the **Details** page, click **Change Configuration** to the right of **Specifications**.
5. On the **ALB Change Specification** page, modify the **Specifications** based on the
performance requirements. The performance metrics vary with instance specifications. For more information, see ALB instance specifications. If a service is created on the Service Management page and **Application Load Balancer**
**(ALB)** is displayed in the **Cloud resources** column of the service, confirm the
parameters and click **Confirm Order**. If no service whose **Cloud resources** value is **Application Load Balancer (ALB)** exists on the Service Management page, confirm the parameters and click **Submit**.

#### Change the network type of an ALB

**instance**

Application Load Balancer (ALB) instances support network types of different protocol versions. This topic describes how to change the network type of an ALB instance to meet business requirements. Before you change the network type of an ALB instance, you need to disable the modification protection for the ALB instance.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. Modification protection is disabled for the ALB instance. For more information, see Configure modification protection.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
5. In the **Network Information** section of the **Instance Details** tab on the **Details** page,
change the network type of the ALB instance based on your business requirements.

**ALB instance whose protocol version is IPv4**

a. Click **Change Network Type** next to **IPv4 Address Type**. Application Load Balancer User G b. In the **Change Network Type** or **Change IPv4 Network Type** dialog box, confirm the value of **Destination Network Type** and perform the following operations as needed.
**Change the network type from Internal Network to Internet** : Allocate an elastic
IP Address (EIP) to the zone in the list based on your business requirements. If you select an EIP, perform the following operations: a. In the zone list, click the **Allocate EIP** drop-down list. b. In the **Select EIP** dialog box, select an EIP and click **OK**. The EIP information includes **EIP ID/Name**, **IP Address Status**, **IP Address**, and **Associate Instance**. Click **Advanced Filter**. You can specify **Instance ID**, **Name**, and **IP Address** to search for EIPs. An EIP whose **IP Address Status** is **Associated** cannot be selected. If you do not select an EIP, an EIP is automatically created.
**Change the network type from Internet to Internal Network** : This operation
changes the Internet-facing instance to an internal-facing instance. The system automatically disassociates all EIPs from the instance and assigns a private IP address to the instance. The domain name is resolved to the private IP address. Proceed with caution. c. Click **OK**.

**ALB instance whose protocol version is Dual-stack**

Change the IPv4 network type a. Click **Change Network Type** next to **IPv4 Address Type**. b. In the **Change Network Type** or **Change IPv4 Network Type** dialog box, confirm the value of **Destination Network Type** and perform the following operations as needed.
**Change the network type from Internal Network to Internet** : Allocate an
elastic IP Address (EIP) to the zone in the list based on your business requirements. If you select an EIP, perform the following operations: a. In the zone list, click the **Allocate EIP** drop-down list. b. In the **Select EIP** dialog box, select an EIP and click **OK**. The EIP information includes **EIP ID/Name**, **IP Address Status**, **IP Address**, and **Associate Instance**. Click **Advanced Filter**. You can specify **Instance ID**, **Name**, and **IP Address** to search for EIPs. An EIP whose **IP Address Status** is **Associated** cannot be selected. If you do not select an EIP, an EIP is automatically created.
**Change the network type from Internet to Internal Network** : This operation
changes the Internet-facing instance to an internal-facing instance. The system automatically disassociates all EIPs from the instance and assigns a private IP address to the instance. The domain name is resolved to the private IP address. Proceed with caution. c. Click **OK**. Application Load Balancer User G Change the IPv6 network type a. Click **Change Network Type** next to **IPv6 Address Type**. b. In the **Change IPv6 Network Type** dialog box, confirm the **Destination Network**
**Type** and perform the following operations as needed.
**Change the network type from Internal Network to Internet** : After the network
type changes, Internet bandwidth is enabled for the IPv6 gateway in the VPC.
**IPv6 Gateway**: displays the IPv6 gateway in the VPC where the ALB instance
resides. You can click **Create IPv6 Gateway** to create an IPv6 gateway.
**Change the network type from Internet to Internal Network** : Internet
bandwidth is disabled for the IPv6 gateway. c. Click **OK**.

#### View the list of ALB instances

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, you can view the following information about ALB
instances: **Instance ID/Name**, **Tag**, **Listener**, **Specifications**, **Network Type**, **Network**
**Protocol**, **Status**, **Service Status**, **VPC**, **Deletion Protection**, **Configuration Read-**
**only Mode**, **Organization/Resource Set**, and **Creator**.

**Note**

Up to 100 pages of records can be displayed in the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records. You can filter instances by keyword, **Instance ID**, **Instance Name**, **VPC ID**, **Status**,
**Tag**, and **Creator**.
Click the icon in the upper-right corner to show or hide items in the ALB instance list. You can also drag and drop the items to adjust their order. Click the icon next to the **Status** column to filter ALB instances by status. The available states include **Changing Configurations**, **Running**, **Creating**, **Stopped**, and **Create failed.**. Click the instance ID in the **VPC** column to view the details of the VPC to which the ALB instance belongs. Application Load Balancer User G
5. Optional. On the **Instance Management** page, you can add tags to ALB instances for
easier management. For more information, see Tag management.

#### View the details of an ALB instance

Application Load Balancer (ALB) allows you to view the details of an ALB instance.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
5. On the **Details** page, view the details of the ALB instance.
Click the **Instance Details** tab to view and manage the information in the **Basic**
**Information**, **Network Information**, and **Zone** sections of the ALB instance.
The **Basic Information** section displays the following information about the ALB instance: **Instance ID**, **Instance Name**, **Status**, **Service Status**, **Organization**,
**Resource Set**, **Created By**, **Created At**, **Specifications**, **Deletion Protection**, and
**Configuration Read-only Mode**.
The **Network Information** section displays the following information about the ALB instance: **IPv4 Address Type**, **IPv6 Address Type** (displayed only when **Protocol**
**Version** of the ALB instance is **Dual-stack**), **Protocol Version**, **Address Mode**, **VPC**,
and **Local IP**. Click the ID below **VPC** to view the details of the VPC in which the ALB instance resides. The **Zone** section displays the following information about the ALB instance: **Zone**,
**Instance Status**, **vSwitch**, **Cluster**, **EIP** (displayed only when **IPv4 Address Type** is
**Internet**), and **VIP**.
Click the instance ID in the **vSwitch** column to view the details of the vSwitch to which the ALB instance belongs. Click the IP address in the **EIP** column to view the details of the elastic IP address (EIP) assigned to the ALB instance. Click the **Listener** tab to view and manage the listener protocols and listeners of the ALB instance. For more information, see Listeners. Click the **Monitoring** tab to view the monitoring data of the ALB instance. For more information, see Monitoring. Click the **Operation Logs** tab to view the operation logs of the ALB instance. For more information, see Operation logs.

#### Listeners

##### Listener overview

| Protoc ol | Description | Use scenario |
|---|---|---|
| HTTP | HTTP is an application-layer protocol that is used to package data. HTTP supports cookie-based session persistence. HTTP uses the X-Forward-For header to retrieve client IP addresses. | HTTP is ideal for applications that identify data content, such as web applications and mobile games. |
| HTTPS | HTTPS encrypts data transmission to prevent unauthorized access. Centralized certificate management service is provided. You can upload certificates to ALB. Then, data decryption is offloaded from backend servers to ALB. | HTTPS is applicable to applications that require encrypted data transmission. |
| QUIC | QUIC is a low-latency transport protocol based on UDP. QUIC implements different congestion control algorithms without the need for OS and kernel support. | QUIC can improve network quality, optimize video stuttering, accelerate content delivery for video and audio services, and ensure secure data transmission. |

Application Load Balancer User G After you create an Application Load Balancer (ALB) instance, you must configure listeners for the instance. Listeners listen for connection requests and forward the requests to backend servers based on the forwarding rules specified in scheduling algorithms. Before you configure listeners for an ALB instance, you must disable modification protection for the instance.

**Listener protocols**

ALB provides HTTP, HTTPS, or Quick UDP Internet Connections (QUIC) listeners. You can select listener protocols based on your business scenarios.

##### Add listeners

A listener is the smallest configurable unit of Application Load Balancer (ALB). Listeners listen for requests over the protocols and ports that you configure. For example, you can configure a listener of ALB to process HTTP requests on port 80. You must add at least one listener to each ALB instance before the ALB instance can distribute network traffic. By default, you can add up to 50 listeners to each ALB instance to distribute network traffic for different workloads.

###### Add an HTTP listener

HTTP is ideal for applications that need to identify data content, such as web applications and mobile games. You can add HTTP listeners to forward HTTP requests.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. A server group is created. For more information, see Create a server group.

| Parameter | Description |
|---|---|
| Instance ID | The ID of the ALB instance is displayed. |
| Select Listener Protocol | Select a protocol for the listener. In this example, select HTTP. |
| Listener Port | Select the port on which the ALB instance listens. The ALB instance listens on the port and forwards requests to backend servers. Valid values: 1 to 65535. Generally, HTTP uses port 80. Note On the same ALB instance, the ports of listeners that use the same protocol must be unique. HTTP listeners and HTTPS listeners must use different ports. |
| Listener Name | Enter a name for the listener. |

Application Load Balancer User G

**Step 1: Open the ALB configuration wizard**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to go to the **ALB Configuration Wizard** page.
On the **Instance Management** page, find the target instance and click **Create Listener** in the **Actions** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. Click **Create Listener**.

**Step 2: Configure a listener**

In the **Configure Listener** step, configure the parameters and click **Next Step**.

| Idle Connection Timeout Period (s) | The timeout period for idle connections. Valid values: 1 to 60. Unit: seconds. Default value: 15. If no request is received within the specified timeout period, ALB temporarily terminates the connection. When a request is received, ALB creates a new connection. |  |  |
|---|---|---|---|
| Connection Request Timeout Period (s) | The connection timeout period. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no backend server responds to the connection request within the specified timeout period, ALB returns the HTTP 504 status code to the client. |  |  |
| Data Compression | Specify whether to enable data compression. By default, this feature is enabled. If you enable this feature, files of specific types are compressed. If you disable this feature, no file is compressed. Currently, Brotli supports all types of files. Gzip supports the following types of files: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, application/xml, and application/json. Note If a client request supports both the Brotli and Gzip compression algorithms, ALB preferentially uses the more efficient Brotli compression algorithm. If a client supports only the Gzip compression algorithm but the file type is not supported by Gzip, ALB does not perform compression. |  |  |
| Retrieve Client IP Address | Specify whether to retrieve the real source IP address of the client. This feature is disabled by default. If this feature is enabled, ALB can retrieve client IP addresses from the X- Forwarded-For header. |  |  |
| Configure Trusted IP Addresses | Configure trusted IP addresses and separate them with semicolons (;). If you set the trusted IP address list to 0.0.0.0/0 , the ALB instance retrieves the leftmost IP address in the X-Forwarded-For header. The IP address is the source client IP address. If you set the trusted IP address list in the format of proxy1 IP;proxy2 IP;... , the ALB instance compares the IP addresses in the X- Forwarded-For header from right to left against the trusted IP address list. The first IP address that is not in the trusted IP address list is considered the source client IP address. Note This parameter is required if you turn on Retrieve Client IP Address. |  |  |
|  |  | proxy1 IP;proxy2 |  |

| re Trusted IP | IP;... |
|---|---|

Application Load Balancer User G

| Use X-Forwarded-For Header to Retrieve Client IP Addresses | Specify whether to use the X-Forwarded-For header to obtain the real IP address of the client. By default, this feature is enabled. If this feature is enabled, ALB adds the X-Forwarded-For header to or removes the X-Forwarded-For header from requests before ALB forwards requests to backend servers. If this feature is disabled, ALB does not make any changes to the X- Forwarded-For header in requests before forwarding requests to backend servers. |
|---|---|
| X-Forwarded-For Header Mode | Select the X-Forwarded-For header mode. By default, Add (ALB adds the IP address of the last hop to the X-Forwarded-For header in the request before ALB forwards the request to a backend server.) is selected. Valid values: Add (ALB adds the IP address of the last hop to the X- Forwarded-For header in the request before ALB forwards the request to a backend server.) Remove (ALB removes the X-Forwarded-For header from the request before ALB forwards the request to a backend server, no matter whether the request contains the X-Forwarded-For header.) |
| Use the SLB-ID header to retrieve ALB instance IDs | Select the HTTP headers that you want to add based on your business requirements. |
| Use the X- Forwarded-Proto header to retrieve the listener protocol of the ALB instance. |  |
| Use the X- Forwarded-Port header to retrieve the listener port of the ALB instance. |  |
| Use the X- Forwarded-Host header to retrieve the domain name of a client. |  |
| Use the X- Forwarded-Client- srcport header to retrieve the port of a client. |  |

Application Load Balancer User G Application Load Balancer User G In the **Select Server Group** step, select a **Server Group** and click **Next Step**. The information about a server group includes **Server Group ID/Name**, **Type**, **Backend**
**Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

**Step 4: Submit the configurations**

In the **Review Configuration** step, confirm the configurations, and then click **Submit**. The configurations of an HTTP listener include **Basic Configurations**, **Add HTTP Header**, and **Server Group**.

###### Add an HTTPS listener

This topic describes how to add an HTTPS listener to an Application Load Balancer (ALB) instance. HTTPS is intended for applications that require encrypted data transmission. You can add an HTTPS listener to forward HTTPS requests.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. A server group is created. For more information, see Create a server group. The server certificate is uploaded. For more information, see Manage server certificates.

**Step 1: Open the ALB configuration wizard**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to go to the **ALB Configuration Wizard** page.
On the **Instance Management** page, find the target instance and click **Create Listener** in the **Actions** column. On the Listener tab:

| Parameter | Description |
|---|---|
| Instance ID | The ID of the ALB instance is displayed. |
| Select Listener Protocol | Select a protocol for the listener. HTTPS is selected in this example. |
| Listener Port | Select the port on which the ALB instance listens. The ALB instance listens on the port and forwards requests to backend servers. Valid values: 1 to 65535. Generally, HTTPS uses port 443. |
| Listener Name | Enter a name for the listener. |
| Enable HTTP/2 | Specify whether to enable HTTP/2. By default, HTTP/2 is enabled. You can associate only HTTPS listeners that have HTTP/2 enabled with gRPC server groups. |
| Idle Connection Timeout Period (s) | The timeout period for idle connections. Valid values: 1 to 60. Unit: seconds. Default value: 15. If no request is received within the specified timeout period, ALB temporarily terminates the connection. When a request is received, ALB creates a new connection. |
| Connection Request Timeout Period (s) | The connection timeout period. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no backend server responds to the connection request within the specified timeout period, ALB returns the HTTP 504 status code to the client. |

Application Load Balancer User G a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. Click **Create Listener**.

**Step 2: Configure a listener**

In the **Configure Listener** step, configure the parameters and click **Next Step**.

| Data Compression | Specify whether to enable data compression. By default, this feature is enabled. If you enable this feature, files of specific types are compressed. If you disable this feature, no file is compressed. Currently, Brotli supports all types of files. Gzip supports the following types of files: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, application/xml, and application/json. Note If a client request supports both the Brotli and Gzip compression algorithms, ALB preferentially uses the more efficient Brotli compression algorithm. If a client supports only the Gzip compression algorithm but the file type is not supported by Gzip, ALB does not perform compression. |  |  |
|---|---|---|---|
| Retrieve Client IP Address | Specify whether to retrieve the real source IP address of the client. This feature is disabled by default. If this feature is enabled, ALB can retrieve client IP addresses from the X- Forwarded-For header. |  |  |
| Configure Trusted IP Addresses | Configure trusted IP addresses and separate them with semicolons (;). If you set the trusted IP address list to 0.0.0.0/0 , the ALB instance retrieves the leftmost IP address in the X-Forwarded-For header. The IP address is the source client IP address. If you set the trusted IP address list in the format of proxy1 IP;proxy2 IP;... , the ALB instance compares the IP addresses in the X- Forwarded-For header from right to left against the trusted IP address list. The first IP address that is not in the trusted IP address list is considered the source client IP address. Note This parameter is required if you turn on Retrieve Client IP Address. |  |  |
|  |  | proxy1 IP;proxy2 |  |
| Use X-Forwarded-For Header to Retrieve Client IP Addresses | Specify whether to use the X-Forwarded-For header to obtain the real IP address of the client. By default, this feature is enabled. If this feature is enabled, ALB adds the X-Forwarded-For header to or removes the X-Forwarded-For header from requests before ALB forwards requests to backend servers. If this feature is disabled, ALB does not make any changes to the X- Forwarded-For header in requests before forwarding requests to backend servers. |  |  |

| re Trusted IP | IP;... |
|---|---|

Application Load Balancer User G

| X-Forwarded-For Header Mode | Select the X-Forwarded-For header mode. By default, Add (ALB adds the IP address of the last hop to the X-Forwarded-For header in the request before ALB forwards the request to a backend server.) is selected. Valid values: Add (ALB adds the IP address of the last hop to the X- Forwarded-For header in the request before ALB forwards the request to a backend server.) Remove (ALB removes the X-Forwarded-For header from the request before ALB forwards the request to a backend server, no matter whether the request contains the X-Forwarded-For header.) |
|---|---|
| Use the SLB-ID header to retrieve ALB instance IDs | Select the HTTP headers that you want to add based on your business requirements. |
| Use the X- Forwarded-Proto header to retrieve the listener protocol of the ALB instance. |  |
| Use the X- Forwarded-Port header to retrieve the listener port of the ALB instance. |  |
| Use the X- Forwarded-Host header to retrieve the domain name of a client. |  |
| Use the X- Forwarded-Client- srcport header to retrieve the port of a client. |  |
| Use the X- Forwarded- Clientcert-subjectdn header to retrieve information about the client certificate owner. |  |

Application Load Balancer User G

| Use the X- Forwarded- Clientcert-issuerdn header to retrieve information about the CA that issues the client certificate. |  |
|---|---|
| Use the X- Forwarded- Clientcert-fingerprint header to retrieve the fingerprint of the client certificate. |  |
| Use the X- Forwarded- Clientcert- clientverify header to retrieve the verification result of the client certificate. |  |
| Enable QUIC Upgrade | Specify whether to enable the QUIC upgrade feature. This feature is disabled by default. If you enable this feature, you must select Associated QUIC Listeners. |
| Associated QUIC Listeners | Select a QUIC listener and associate it with the ALB instance. The listener information includes Listener ID/Name, Listener |
|  | Protocol/Port, and Status. Click Advanced Filter. You can enter a listener ID or a listener name to filter listeners.Listener IDListener Name Listener ID: You can enter at most 20 listener IDs. Separate multiple listener IDs with commas (,). Listener Name: You can enter at most 10 listener names. Separate multiple listener names with commas (,). Note This parameter is required if you turn on Enable QUIC Upgrade. |

| Parameter | Description |
|---|---|

Application Load Balancer User G

**Step 3: Configure an SSL certificate**

In the **Configure SSL Certificate** step, configure an SSL certificate to ensure that data transmission is encrypted and the identities of users are verified by a trusted authority. Then, click **Next Step**.

| Server Certificate | Select the desired server certificate. The server certificate information includes Certificate ID/Name, Certificate Type, Algorithm, User, Created At, and Expired At. Click Advanced Filter. You can enter a certificate ID or certificate name to search for certificates.Certificate IDCertificate Name |
|---|---|
| Enable Mutual Authentication | Specify whether to enable mutual authentication. If you turn on the switch, you must specify CA Certificate. |
| CA Certificate | Select the desired CA certificate. The CA certificate information includes Certificate ID/Name, Algorithm, User, Created At, and Expired At. Click Advanced Filter. You can enter a certificate ID or certificate name to search for certificates.Certificate IDCertificate Name Note This parameter is required if you turn on Enable Mutual Authentication. |
| TLS Security Policy Type | The type of the TLS security policy. Valid values: System Policy: a TLS security policy that is preset by the system. Custom Policy: a custom TLS security policy. |
| TLS Security Policy | Select a TLS security policy based on the setting ofT LS Security Policy Type. System policy information includes Security Policy ID, TLS Protocol, and Cipher Suite. For more information about common system policies, see System TLS security policies. Custom policy information includes Security Policy ID/Name, TLS Protocol, and Cipher Suite. Click Advanced Filter. You can specify Security Policy ID or Security Policy Name to search for security policies. |

Application Load Balancer User G In the **Select Server Group** step, select a **Server Group** and click **Next Step**. The information about a server group includes **Server Group ID/Name**, **Type**, **Backend**
**Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. Application Load Balancer User G For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

**Step 5: Submit the configurations**

In the **Review Configuration** step, confirm the configurations, and then click **Submit**. The configurations of the HTTP listener include **Basic Configurations**, **Add HTTP Header**,
**Configure SSL Certificate**, and **Server Group**.

###### Add a QUIC listener

Quick UDP Internet Connection (QUIC) can improve network quality, optimize video stuttering, accelerate content delivery for video and audio services, and ensure secure data transmission. You can add QUIC listeners to forward QUIC requests.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance. A server group is created. For more information, see Create a server group. The server certificate is uploaded. For more information, see Manage server certificates.

**Step 1: Open the ALB configuration wizard**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to go to the **ALB Configuration Wizard** page.
On the **Instance Management** page, find the target instance and click **Create Listener** in the **Actions** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. Click **Create Listener**.

**Step 2: Configure a listener**

In the **Configure Listener** step, configure the parameters and click **Next Step**.

| Parameter | Description |
|---|---|
| Instance ID | The ID of the ALB instance is displayed. |
| Select Listener Protocol | Select a listener protocol. QUIC is selected in this example. |
| Listener Port | Select the port on which the ALB instance listens. The ALB instance listens on the port and forwards requests to backend servers. Valid values: 1 to 65535. |
| Listener Name | Enter a name for the listener. |
| Idle Connection Timeout Period (s) | The timeout period for idle connections. Valid values: 1 to 60. Unit: seconds. Default value: 15. If no request is received within the specified timeout period, ALB temporarily terminates the connection. When a request is received, ALB creates a new connection. |
| Connection Request Timeout Period (s) | The connection timeout period. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no backend server responds to the connection request within the specified timeout period, ALB returns the HTTP 504 status code to the client. |
| Data Compression | Specify whether to enable data compression. By default, this feature is enabled. If you enable this feature, files of specific types are compressed. If you disable this feature, no file is compressed. Currently, Brotli supports all types of files. Gzip supports the following types of files: text/xml, text/plain, text/css, application/javascript, application/x-javascript, application/rss+xml, application/atom+xml, application/xml, and application/json. Note If a client request supports both the Brotli and Gzip compression algorithms, ALB preferentially uses the more efficient Brotli compression algorithm. If a client supports only the Gzip compression algorithm but the file type is not supported by Gzip, ALB does not perform compression. |

Application Load Balancer User G

| Use X-Forwarded-For Header to Retrieve Client IP Addresses | Specify whether to use the X-Forwarded-For header to obtain the real IP address of the client. By default, this feature is enabled. If this feature is enabled, ALB adds the X-Forwarded-For header to or removes the X-Forwarded-For header from requests before ALB forwards requests to backend servers. If this feature is disabled, ALB does not make any changes to the X- Forwarded-For header in requests before forwarding requests to backend servers. |
|---|---|
| X-Forwarded-For Header Mode | Select the X-Forwarded-For header mode. By default, Add (ALB adds the IP address of the last hop to the X-Forwarded-For header in the request before ALB forwards the request to a backend server.) is selected. Valid values: Add (ALB adds the IP address of the last hop to the X- Forwarded-For header in the request before ALB forwards the request to a backend server.) Remove (ALB removes the X-Forwarded-For header from the request before ALB forwards the request to a backend server, no matter whether the request contains the X-Forwarded-For header.) |
| Use the SLB-ID header to retrieve ALB instance IDs | Select the HTTP headers that you want to add based on your business requirements. |
| Use the X- Forwarded-Proto header to retrieve the listener protocol of the ALB instance. |  |
| Use the X- Forwarded-Port header to retrieve the listener port of the ALB instance. |  |
| Use the X- Forwarded-Host header to retrieve the domain name of a client. |  |
| Use the X- Forwarded-Client- srcport header to retrieve the port of a client. |  |

Application Load Balancer User G

**Step 3: Configure an SSL certificate**

| Certificate configuration | Description |
|---|---|
| Server Certificate | Select the desired server certificate. The server certificate information includes Certificate ID/Name, Certificate Type, Algorithm, User, Created At, and Expired At. Click Advanced Filter. You can enter a certificate ID or certificate name to search for certificates.Certificate IDCertificate Name |

Application Load Balancer User G In the **Configure SSL Certificate** step, configure an SSL certificate to ensure that data transmission is encrypted and the identities of users are verified by a trusted authority. Then, click **Next Step**. In the **Select Server Group** step, select a **Server Group** and click **Next Step**. The information about a server group includes **Server Group ID/Name**, **Type**, **Backend**
**Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

**Step 5: Submit the configurations**

In the **Review Configuration** step, confirm the configurations, and then click **Submit**. The configurations of the QUIC listener include **Basic Configurations**, **Add HTTP Header**,
**Configure SSL Certificate**, and **Server Group**.

##### Manage listeners

This topic describes how to modify, enable, disable, and delete a listener, and change the server group associated with a listener.

###### Modify the name of a listener

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

Application Load Balancer User G
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. In the listener list, find the listener that you want to manage and click the
icon to the right of the listener name in the **Listener ID/Name** column.
6. In the **Modify Name** dialog box, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

###### Configure access control

You can configure access control for each listener of an Application Load Balancer (ALB) instance.

###### Enable access control

You can configure whitelists or blacklists for different listeners.

**Prerequisites**

A listener is created. For more information, see Add listeners. Access control is disabled for the listener. For more information, see Disable access control.

**Procedure**

**Note**

Access control may cause some business risks. If a whitelist is configured, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If you configure a whitelist but no IP addresses are added to the whitelist, the listener forwards all requests. If a blacklist is configured for a listener, all requests from the IP addresses that are added to the blacklist are blocked by the listener. If you configure a blacklist but no IP addresses are added to the blacklist, the listener forwards all requests.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.

| Parameter | Description |
|---|---|
| ACL Type | Select an access control mode. Valid values: Whitelist: Only requests from the IP addresses or CIDR blocks in the specified ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. Blacklist: Requests from the IP addresses or CIDR blocks in the specified ACL are blocked. Blacklists apply to scenarios in which you want to block requests from specific IP addresses. |
| ACL | Select an ACL. You can select multiple ACLs. ACL information includes ACL ID/Name, Status, and Created At. Click Advanced Filter. You can specify ACL ID or ACL Name to search for ACLs. |

Application Load Balancer User G On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the configuration window.
In the listener list, find the target listener and click **Enable** in the **Access Control** column. On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. In the **Access Control** section of the **Listener Details** tab on the **Listener** page, click
**Enable** next to **Access Control**.
6. In the **Enable Access Control** dialog box, configure the following parameters and click
**OK**.

###### Modify access control

**Prerequisites**

A listener is created. For more information, see Add listeners. Access control is enabled for the listener. For more information, see Enable access control.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.

| Parameter | Description |
|---|---|
| ACL Type | Select an access control mode. Valid values: Whitelist: Only requests from the IP addresses or CIDR blocks in the specified ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. Blacklist: Requests from the IP addresses or CIDR blocks in the specified ACL are blocked. Blacklists apply to scenarios in which you want to block requests from specific IP addresses. |
| ACL | Select an ACL. You can select multiple ACLs. ACL information includes ACL ID/Name, Status, and Created At. Click Advanced Filter. You can specify ACL ID or ACL Name to search for ACLs. |

Application Load Balancer User G On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the edit window.
In the listener list, find the target listener and click **Modify** in the **Access Control** column. On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. In the **Access Control** section of the **Listener Details** tab on the **Listener** page, click
**Modify** next to **Access Control**.
6. In the **Modify Access Control** dialog box, configure the following parameters and click
**OK**.

###### Disable access control

This topic describes how to disable access control for a listener.

**Prerequisites**

A listener is created. For more information, see Add listeners. Access control is enabled for the listener. For more information, see Enable access control.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
Application Load Balancer User G
4. Use either of the following methods to open the Listener tab.
On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the **Disable Access Control** dialog box, and
then click **OK**. In the listener list, find the target listener and click **Disable** in the **Access Control** column. On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. In the **Access Control** section of the **Listener Details** tab on the **Listener** page, click
**Disable** next to **Access Control**.

###### Start or stop a listener

You can change the running status of a listener by starting or stopping the listener. When a listener is in the Enabling or Disabling state, the listener cannot be modified or removed.

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. In the listener list, find the target listener and click **Enable**/**Disable** in the **Actions** column.
6. In the message that appears, click **OK**.

###### Modify listeners

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

Application Load Balancer User G
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the edit page.
Open the edit page through the ALB instance: a. On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. b. In the upper-right corner of the **Listener** page, click **Modify**. Open the edit page through the listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. Use either of the following methods to open the edit page. Find the target listener in the listener list. In the **Actions** column, click **... > Modify**
**Listener** or **Modify Listener**.
On the listener details page: In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. In the upper-right corner of the **Listener** page, click **Modify**.
5. On the **ALB Configuration Wizard** page, follow the on-screen instructions to modify the
listener. For more information about the parameters, see Add listeners.

**Note**

The protocol and port of a listener cannot be modified. To modify them, create another listener.

###### Change a server group

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
Application Load Balancer User G On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the Change Server Group dialog box.
In the listener list, find the target listener, and in the **Actions** column, click **... > Change**
**Server Group (Default Forwarding Rule)**.
On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. On the **Listener Details** tab of the **Listener** page, click **Change Server Group**
**(Default Forwarding Rule)** in the **Server Group (Default Forwarding Rule)**
section.
6. In the **Change Server Group** dialog box, select a server group and then click **OK**.
The information about a server group includes **Server Group ID/Name**, **Type**, **Backend**
**Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

###### Delete a listener

After you create a listener, you can delete the listener based on your business requirements.

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.

| Parameter | Description |
|---|---|
| TLS Security Policy Type | The type of the TLS security policy. Valid values: System Policy: a TLS security policy that is preset by the system. Custom Policy: a custom TLS security policy. |

Application Load Balancer User G On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. In the listener list, find the target listener, and in the **Actions** column, click **... > Delete**.
6. In the **Delete Listener** message, click **OK**.

##### Modify a TLS security policy

This topic describes how to change the TLS security policies for HTTP listeners.

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the listener details page.
On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column.
5. In the **SSL Certificate** section of the **Listener Details** tab on the **Listener** page, click the
icon next to **TLS Security Policy**.
6. In the **Modify TLS Security Policy** dialog box, configure the following parameters and
click **OK**.

| TLS Security Policy | Select a TLS security policy based on the setting ofT LS Security Policy Type. System policy information includes Security Policy ID, TLS Protocol, and Cipher Suite. For more information about common system policies, see System TLS security policies. Custom policy information includes Security Policy ID/Name, TLS Protocol, and Cipher Suite. Click Advanced Filter. You can specify Security Policy ID or Security Policy Name to search for security policies. |
|---|---|

Application Load Balancer User G

##### View the list of listeners

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. On the **Listener** tab, you can view the following information about created listeners:
**Listener ID/Name**, **Listener Protocol/Port**, **Status**, **Server Group**, **Health Check**
**Status**, and **Access Control**.
You can filter listeners by **Listener ID** and **Listener Protocol**.
**Listener ID**: You can enter at most 20 listener IDs. Separate multiple listener IDs with
commas (,).
**Listener Protocol**: You can select **HTTP**, **HTTPS**, or **QUIC**.
Click an ID in the **Server Group** column to view the details of the server group. Move your pointer over the ID in the **Server Group** column and click the number below
**Servers**. In the **Server Group Instance** dialog box, you can view the backend servers
that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** Application Load Balancer User G For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance. Click the data in the **Health Check Status** column. In the **Server Health Check Status** dialog box, you can view the health check details of the servers under the listener. The health check status is updated with a latency of one to two minutes.

##### View the details of a listener

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the listener details page.
On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column.
5. On the **Listener** page, view the details of the listener.
On the **Listener Details** tab, you can view and manage the information in the following sections: **Basic Information**, **Add HTTP Header**, **Access Control**, **SSL Certificate** (available only for **HTTP** and **QUIC** listeners), and **Server Group (Default Forwarding**
**Rule)**.
**Basic Information**: displays **Listener ID**, **Listener Name**, **Listener Protocol:Port**,
**Status**, **Enable HTTP/2** (available only for **HTTPS** listeners), **Idle Connection**
**Timeout Period**, **Connection Request Timeout Period**, **Data Compression**, and
**QUIC Upgrade** (available only for **HTTPS** listeners).
**Add HTTP Header**: displays **ALB can retrieve client IP addresses by using the X-**
**Forwarded-For header.**, **Use X-Forwarded-For Header to Retrieve Client IP**
**Addresses** , **X-Forwarded-For Header Mode**, and the enabling status of custom
HTTP header fields.
**Access Control**: displays the enabling status of **Access Control**.
Application Load Balancer User G
**SSL Certificate**: displays **Default Server Certificate**, **TLS Security Policy**
(available only for **HTTPS** listeners), and the enabling status of **Mutual**
**Authentication**.
**Server Group (Default Forwarding Rule)**: displays **Server Group ID**, **Server**
**Group Name**, **Type**, **Backend Protocol**, and **Servers**.
Click **View/Modify Backend Server** in the upper-right corner to view or manage the backend servers in the server group for the listener. For more information, see Backend servers. Click the number below **Servers**. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and
**Description**.
You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance. On the **Listener Certificate** tab (available only for **HTTPS** and **QUIC** listeners), you can view and manage the additional certificates of the listener. For more information, see Manage certificates for listeners. On the **Forwarding Rules** tab, you can view and manage the forwarding rules for the listener. For more information, see Manage forwarding rules for a listener.

##### Manage certificates for listeners

###### Add additional certificates

If you want to access multiple domain names or add multiple server certificates, you can add additional certificates to an HTTPS listener after you configure the HTTP listener.

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the listener details page.
On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. On the Listener tab: Application Load Balancer User G a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column.
5. Click the **Listener Certificate** tab.
6. Perform the following operations to add an additional certificate based on your business
requirements. i. Click the **Server Certificate** tab. ii. Click **Add Additional Certificate**. iii. In the **Select Certificate** dialog box, select the server **Certificate** that you want to add and click **OK**. Certificate information includes **Certificate ID/Name**, **Algorithm**, **User**, **Created At**, and **Expired At**. Click **Advanced Filter**. You can specify **Certificate ID** or **Certificate Name** to search for certificates. i. Click the **CA Certificate** tab. ii. Click **Add Additional Certificate**. iii. In the **Select Certificate** dialog box, select the CA **Certificate** that you want to add and click **OK**. Certificate information includes **Certificate ID/Name**, **Algorithm**, **User**, **Created At**, and **Expired At**. Click **Advanced Filter**. You can specify **Certificate ID** or **Certificate Name** to search for certificates.

###### Replace the default certificate of a

**listener**

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

**Note**

We recommend that you renew your certificate before it expires to prevent adverse impacts on your services. Application Load Balancer User G
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the listener details page.
On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column.
5. Click the **Listener Certificate** tab.
6. Perform the following operations to replace the default certificate of the listener based on
your business requirements. i. Click the **Server Certificate** tab. ii. On the Server Certificate tab, find the default server certificate and click **Change** in the
**Actions** column.
iii. In the **Select Certificate** dialog box, select the server **Certificate** that you want to add and click **OK**. Certificate information includes **Certificate ID/Name**, **Algorithm**, **User**, **Created At**, and **Expired At**. Click **Advanced Filter**. You can specify **Certificate ID** or **Certificate Name** to search for certificates. i. Click the **CA Certificate** tab. ii. On the Server Certificate tab, find the default server certificate and click **Change** in the
**Actions** column.
iii. In the **Select Certificate** dialog box, select the CA **Certificate** that you want to add and click **OK**. Certificate information includes **Certificate ID/Name**, **Algorithm**, **User**, **Created At**, and **Expired At**. Click **Advanced Filter**. You can specify **Certificate ID** or **Certificate Name** to search for certificates.

###### Enable or disable mutual authentication

Application Load Balancer User G Mutual authentication improves the security of business-critical services. This topic describes how to configure mutual authentication on an HTTPS listener of an Application Load Balancer (ALB) instance.

**Background information**

One-way authentication: The client must verify the identity of the server. The server does not need to verify the identity of the client. The client downloads the public key certificate from the server for authentication. A connection can be established after the identity of the server is authenticated. Mutual authentication: The client downloads the server certificate (public key certificate) from the server and uploads the client certificate (public key certificate) to the server for authentication. A connection can be established only after both the client and the server are authenticated. Mutual authentication provides higher security.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the listener details page.
On the **Instance Management** page, find the target instance and click the protocol/port of the target listener in the **Listener** column. On the Listener tab: a. Use either of the following methods to open the Listener tab. On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the **Instance ID/Name** column. b. On the **Details** page, click the **Listener** tab. b. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column.
5. Use either of the following methods to open the operation window.
In the **SSL Certificate** section of the **Listener Details** tab on the **Listener** page, click the switch below **Mutual Authentication**. On the Listener Certificate tab: a. Click the **Listener Certificate** tab. b. Click the **CA Certificate** tab. c. Click the switch to the right of **Mutual Authentication**.
6. Perform the following operations based on your business requirements.

**Enable mutual authentication**

In the **Enable Mutual Authentication** dialog box, select the desired CA **Certificate** and click **OK**. Certificate information includes **Certificate ID/Name**, **Algorithm**, **User**, **Created At**, and **Expired At**.

| Direction | Condition | Action |
|---|---|---|
| Inbound forwarding rule | Domain Name, Path, HTTP Header, Query String, HTTP Request Method, Cookie, and Source IP | Forward, Redirect, Return Fixed Responses, Rewrite, Add Header, Remove Header, Throttle Traffic, Mirror Traffic, and CORS |
| Outbound forwarding rule | Inbound conditions (optional): Domain Name, Path, HTTP Header, Query String, HTTP Request Method, Cookie, and Source IP Outbound conditions: Response Status Code and Response Header | Return Fixed Responses, Add Header, and Remove Header |

Application Load Balancer User G Click **Advanced Filter**. You can specify **Certificate ID** or **Certificate Name** to search for certificates. In the message that appears, click **OK**.

##### Manage forwarding rules for a listener

This topic describes how to manage forwarding rules for listeners of an Application Load Balancer (ALB) instance. You can configure forwarding rules for listeners of an ALB instance to forward client requests to backend servers in one or more server groups and forward responses to clients. You can create multiple forwarding rules for each listener of an ALB instance. Forwarding rules are divided into inbound and outbound forwarding rules. ALB instances support inbound and outbound forwarding rules. Each forwarding rule consists of conditions and actions. When a request matches the conditions specified in a forwarding rule, the actions specified in the forwarding rule are performed. You can specify one or more conditions and one or more actions in a forwarding rule. After an ALB instance receives a request, the ALB instance distributes the request to a backend server based on an **inbound forwarding rule**. Then, the response from the backend server is processed based on an **outbound forwarding rule** of the ALB instance and returned to the client. When you create an inbound forwarding rule, you can specify only inbound conditions and actions. When you create an outbound forwarding rule, you can specify both inbound and outbound conditions. However, you can specify only outbound actions in an outbound forwarding rule. Each forwarding rule must contain one **Forward**, **Redirect**, or **Return Fixed Responses** action. This ensures that the ALB instance can forward client requests without interruptions.

**Matching policy**

Application Load Balancer User G
**Matching policy:** Each client request is matched against each forwarding rule in the order of
descending rule priority. A smaller rule number indicates a higher priority. Once a forwarding rule is matched, the traffic is immediately forwarded based on the rule and matching is stopped. Requests that do not match custom inbound forwarding rules are forwarded based on the default forwarding rule. Responses that fail to match custom outbound forwarding rules are directly returned to clients by ALB.

**Note**

If the forwarding path is set to `/*` , requests from all paths are matched. If you want to forward unexpected requests, you can set the path in the forwarding condition to `/*` , set the forwarding action to Return Fixed Responses, and set the status code to 404 or 403. After you configure the forwarding rule, drag and drop the rule to the second-to-last position in the rule list.
**Forwarding rule priority:** Requests are matched against forwarding rules in descending
order of rule priority. A smaller number indicates a higher priority.
**Default forwarding rule:** After you create a listener, the system automatically creates a
default inbound forwarding rule. The forwarding condition is set to - , which indicates that all client requests are matched. The forwarding action is set to **Forward**. In this case, traffic is forwarded to the server group that is configured for the listener.

**Note**

You cannot delete the default forwarding rule. However, you can change the destination server group by configuring the forwarding action. The priority of the default forwarding rule is the lowest and cannot be adjusted.

**Matching rule description**

Exact match: The requested content must be the same as the specified content. Wildcard match: The requested content must match the wildcard pattern of the specified content. Regex matching: The requested content and the specified content are matched based on a regular expression.

###### Create inbound forwarding rules

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
Application Load Balancer User G On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the Forwarding Rules tab.
In the listener list, find the target listener and click **View/Modify Forwarding Rule** in the **Actions** column. On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. Click the **Forwarding Rules** tab.
6. Click **Inbound Forwarding Rules**.
7. Click **Add Rule**.
8. In the **Add Forwarding Rule** section, configure the following parameters and click **OK**.

**Note**

You must add at least one forwarding condition and action. The logical operator among the actions for each condition is OR. If you specify multiple actions for a condition, requests that match one of the actions are forwarded. The logical operator among different conditions is AND. If you specify multiple conditions in a forwarding rule, a request is forwarded when all conditions are met.
**Priority**: Enter the priority of the forwarding rule. Valid values: 1 to 10000. A smaller
value indicates a higher priority.
**Rule Name**: Enter a name for the forwarding rule. If you do not specify this parameter, a
name is automatically assigned.

**Note**

You can specify only one name for a forwarding rule.
**Forwarding Conditions**: Select a condition type and configure the forwarding condition.

**Note**

Click **Add Inbound Forwarding Condition** to add multiple forwarding conditions. A maximum of nine forwarding conditions can be added. Click the or icon on the right of a forwarding condition to adjust the order of forwarding conditions. Click the icon next to a forwarding condition to delete the forwarding condition. Application Load Balancer User G
**Domain Name**: Add a domain name. Example: `*.example.com` .
By default, the exact match mode is used and wildcard characters are supported. You must specify a domain name. The value must be 3 to 128 characters in length and can contain lowercase letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?. The value must contain at least one period (.) and cannot start or end with a period (.). The rightmost domain tag can contain only letters and wildcard characters. It cannot contain digits or hyphens (-). If the value starts with a tilde (~), the regular expression matching mode is used and the value is case-insensitive. You must specify a domain name in regular expression matching mode. In regular expression matching mode, the regular expression cannot start with an asterisk (*).

**Note**

You can click **Add Domain Name** to add multiple domain names. You can click the icon next to a domain name to delete the domain name.
**Path**: Add a path. For example, if the URL is www.example.com/test/test1?x=1&y=2 ,
you can set the parameter to `/test/*` . By default, the exact match mode is used and wildcard characters are supported. If the value starts with a tilde plus an asterisk (~*), the regular expression matching mode is used and the value is case-sensitive. You must specify a path. In non-regular expression matching mode, the value must start with a forward slash (/). In non-regular expression matching mode, the value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * ~ _ + $ & ' @ / ?. If the value starts with a tilde (~), the regular expression matching mode is used and the value is case-insensitive. If the value starts with a tilde plus an asterisk (~*), the regular expression matching mode is used and the value is case-sensitive. You must specify a path in regular expression matching mode. In regular expression matching mode, the value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?.

**Note**

You can click **Add Path** to add multiple paths. You can click the icon next to a path to delete the path. Application Load Balancer User G
**HTTP Header**: Add HTTP headers. For example, you can set the key to `user-agent`
and the value to `*Mozilla/4.0*` .
**Key:** Enter a name for the HTTP header.
You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). You cannot set this parameter to Cookie or Host.
**Value:** Enter a value for the HTTP header.
You must specify a value. The value must be 1 to 128 characters in length and can contain printable characters. It cannot start with a space and end with a space or a backward slash (\). It cannot contain double quotation marks (").

**Note**

You can click **Add Header Value** to add multiple header values. You can click the icon next to a header value to delete the header value.
**Query String**: Add key-value pairs of query strings. For example, if the URL is
www.example.com/test/test1?x=1&y=2 , you can set the parameter to `x:1` or `y:2` .
**Key**: Enter the key of a query string.
You must specify a key. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | & " < >.
**Value**: Enter the value of the query string.
You must specify a value. The value must be 1 to 128 characters in length and can contain lowercase letters and printable characters. It cannot contain spaces and the following special characters: # [ ] { } \ | & " < >.

**Note**

You can click **Add String** to add multiple key-value pairs. You can click the icon next to a key-value pair to delete the key-value pair.
**HTTP Request Method**: Add HTTP request methods.
Valid values: **HEAD**, **GET**, **POST**, **OPTIONS**, **PUT**, **PATCH**, and **DELETE**.

**Note**

You can click **Add Method** to add multiple HTTP request methods. You can click the icon next to a request method to delete the request method. Application Load Balancer User G
**Cookie**: Add cookies. For example, you can set the key to `key` and the value to
`value` .
**Key**: Enter a key.
You must specify a key. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | & " < > .
**Value**: Enter the value.
You must specify a value. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain spaces and the following special characters: # [ ] { } \ | & " < > .

**Note**

You can click **Add Cookie** to add multiple key-value pairs. You can click the icon next to a key-value pair to delete the key-value pair.
**SourceIp**: Add an IP address or a CIDR block. Example: `192.168.1.1/32` .
Standard IP addresses are supported. CIDR blocks of the 0.0.0.0/x type are not supported, where x indicates a digit.

**Note**

You can click **Add Source IP Address** to add multiple source IP addresses. You can click the icon next to a source IP address to delete the source IP address.
**Forwarding Action**: Select an action type and configure **Execute**.

**Note**

A forwarding rule must contain one of the following actions: forward, redirect, and return fixed response. In a forwarding rule, the forward, redirect, or return fixed response action must be placed at the end.

**Note**

You can click **Add Action** to add multiple forwarding actions. You can add up to five forwarding actions. You can click the or icon on the right side of a forwarding action to adjust the order of forwarding actions. You can click the icon next to a forwarding action to delete the forwarding action. Application Load Balancer User G
**Server Group**: Click the Server Group drop-down list. In the **Select Server Group**
dialog box, select the desired server group. The information about a server group includes **Server Group ID/Name**, **Type**,
**Backend Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and
**Description**.
You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.
**Weight**: Enter a weight. Valid values: 0 to 100.
**Session Persistence for Server Groups**: If you want to add multiple server
groups, you must turn on this switch. You can enable or disable session persistence among server groups. After this feature is enabled, session persistence can be implemented among server groups by using cookies. Make sure that session persistence feature is enabled for all added server groups.
**Session Persistence Timeout Period (s)**: the timeout period of session
persistence.

**Note**

You can click **Add Server Group** to add multiple server groups. You can click the icon next to a server group to delete the server group. When you add multiple server groups, you can select server groups that use HTTP or HTTPS. Application Load Balancer User G

**Redirect**

**Protocol**: Select a protocol. Valid values: **HTTP** and **HTTPS**.
**Domain Name**: Enter the destination domain name.
If the default value is used, it cannot be concatenated with other characters. The value must be 3 to 128 characters in length and can contain lowercase letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?. The value must contain at least one period (.) and cannot start or end with a period (.). The rightmost domain tag can contain only letters and wildcard characters. It cannot contain digits or hyphens (-).
**Port**: Enter the destination port.
If the default value is used, it cannot be concatenated with other characters. Port range: 1 to 63335.
**Path**: Enter the destination path.
A value other than the default value must start with a forward slash (/). The value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * ~ _ + $ & ' @ / ?.
**Query**: Enter the destination query string.
The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | " < >.
**Status Code**: Select a status code. Valid values: **301**, **302**, **303**, **307**, and **308**.
Default value: **301**.

**Note**

You must specify at least one parameter for a redirect action. The parameters specify the protocol, domain name, path, and query. Do not set them to the default values. If you specify ${x}, the value returned in the response is used. Otherwise, the default value specified in each request is used.

**Return Fixed Response**

**Response Status Code**: Enter the response status code.
Only 2xx, 4xx, and 5xx strings are supported. x indicates a digit.
**Response Content Type (Optional)**: Select a response content type. Valid values:
**text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
**Response Content (Optional)**: Enter the response content.
The value must be 0 to 1024 characters in length and can contain only ASCII characters. Application Load Balancer User G

**Rewrite**

**Domain Name**: Enter the destination domain name.
If the default value is used, it cannot be concatenated with other characters. The value must be 3 to 128 characters in length and can contain lowercase letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?. The value must contain at least one period (.) and cannot start or end with a period (.). The rightmost domain tag can contain only letters and wildcard characters. It cannot contain digits or hyphens (-).
**Path**: Enter the destination path.
A value other than the default value must start with a forward slash (/). The value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * ~ _ + $ & ' @ / ?.
**Query**: Enter the destination query string.
The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | " < >.

**Note**

You must specify at least one parameter for a rewrite action. The parameters specify the domain name, path, and query. Do not set them to the default values. The rewrite action must work with a forward action.The forward action must be placed at the end. If you specify ${x}, the value returned in the response is used. Otherwise, the default value specified in each request is used. Application Load Balancer User G
**Write Header**: Newly added headers overwrite the existing headers.
**Content Type**: Select a content type. Valid values: **Custom**, **Reference**, and
**System-defined**.
**Key:** Enter a header name.
You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
**Value:** Enter or select the header content.
If you set **Content Type** to **Custom**, enter the header content. If you set **Content Type** to **Reference**, enter the header content. You must specify a value. The value must be 1 to 128 characters in length and can contain printable characters. It cannot start with a space and end with a space or a backward slash (\). It cannot contain double quotation marks ("). If you set **Content Type** to **System-defined**, you can set the Value parameter to
**Client Port**, **Client IP Address**, **Client Request Protocol**, **ALB Instance ID**,
and **ALB Listener Port**.

**Note**

The name is not case-sensitive. You cannot set a header name to one of the following values: slb-id, slb-ip, x-forwarded-for, x-forwarded-proto, x-forwarded-eip, x-forwarded-port, x-forwarded-client-srcport, x-forwarded-host, connection, upgrade, content-length, transfer-encoding, keep-alive, te, host, cookie, remoteip, and authority.
**Delete Header**: Specify the key of the header that you want to remove. Then, the key
and value of the specified header are both removed. The delete action must work with a forward action. You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).

**Note**

The name is not case-sensitive. You cannot set a header name to one of the following values: slb-id, slb-ip, x-forwarded-for, x-forwarded-proto, x-forwarded-eip, x-forwarded-port, x-forwarded-client-srcport, x-forwarded-host, connection, upgrade, content-length, transfer-encoding, keep-alive, te, host, cookie, remoteip, and authority. Application Load Balancer User G

**Traffic Limit**

**QPS (Global)**: Enter the number of requests per second. Default value: 6. Valid
values: 1 to 1000000.
**QPS (Per Client IP Address)** : Enter the queries per second (QPS) limit for an
individual client IP address Valid values: 1 to 1000000.

**Note**

The throttle action must work with a forward action., and The forward action must be placed at the end. If you set both **Throttle and Forward**, requests are forwarded to the specified server group before the QPS reaches the threshold. Otherwise, the HTTP 503 status code is returned to the clients. If you set **Throttle, Redirect, and Forward**, requests are forwarded to the specified server group before the QPS reaches the threshold. If the QPS reaches the threshold, requests are redirected to another address. If you set **Throttle, Return Fixed Response, and Forward** , requests are forwarded to the specified server group before the QPS reaches the threshold. If the QPS reaches the threshold, the response defined by the user is returned to the clients. If you set both **QPS (Global)** and **QPS (Per Client IP Address)** , the value of QPS (Per Client IP Address) must be smaller than that of QPS (Global). If you want to set the match conditions in the forwarding rule to **SourceIp** and **QPS (Per Client IP Address)** , you must turn on **Retrieve Client IP**
**Address** for the listener to allow ALB to retrieve client IP addresses from
the X-Forwarded-For header.

**Mirror Traffic**

**Server Group**: Click the Server Group drop-down list. In the **Select Server Group**
dialog box, select the desired server group. The information about a server group includes **Server Group ID/Name**, **Type**,
**Backend Protocol**, and **Servers**.
Click **Advanced Filter**. You can enter **Server Group ID** or **Server Group Name** to search for server groups. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and
**Description**.
You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance. Application Load Balancer User G
**Cross-origin**: If the response is returned from a URL, and the protocol, domain name,
or port is different from the one requested by the client, cross-origin resource sharing (CORS) is enabled. Cross-origin requests are divided into simple requests and preflight requests.
**Allowed Access Sources**: Specify the URLs that are allowed to access cross-region
resources through a browser. It must start with http:// or https:// and can contain only one asterisk (*), followed by a valid domain name or top-level wildcard domain name. Example: http://*.test.abc.example.com. You can specify a port number in the range of 1 to 65535.

**Note**

You can click **Add Access Source** to add multiple access sources. You can click the icon next to an access source to delete the access source.
**Allowed Methods**: Specify the HTTP methods that the specified URLs can use to
access cross-origin resources. Valid values: **GET**, **POST**, **PUT**, **DELETE**, **HEAD**, **OPTIONS**, and **PATCH**. You can select multiple options.
**Allowed Request Headers**: Specify the headers that can be carried in CORS
requests aside from the built-in headers of browsers. The value must be 1 to 32 characters in length and can contain letters, digits, hyphens (-), and underscores (_). It cannot start and end with a hyphen (-) or an underscore (_).
**Allowed Response Headers**: Specify the response headers that can be parsed
by a browser or JavaScript. The value must be 1 to 32 characters in length and can contain letters, digits, hyphens (-), and underscores (_). It cannot start and end with a hyphen (-) or an underscore (_).

**Note**

You can click **Add Allowed Request Header** to add multiple request headers. You can click the icon next to a request header to delete the request header. You can click **Add Allowed Response Header** to add multiple response headers. You can click the icon next to a response header to delete the response header.
**Allowed Credentials**: Specify whether to allow credentials in CORS requests. Valid
values: **Allow** and **Disallow**.
**Browser Cache Duration**: Specify the maximum period of time for which a preflight
request that uses the OPTIONS method can be cached. Unit: seconds. Valid Values: 1 to 172800. Application Load Balancer User G

**Related operations**

After you add a forwarding rule, you can perform the following operations on the **Inbound**
**Forwarding Rules** tab:

**View the list and details of forwarding rules**

You can enter at most 20 forwarding rule IDs in the **Forwarding Rule ID** field to search for forwarding rules. Separate multiple forwarding rule IDs with commas (,). In a forwarding rule section, you can view the details of a forwarding rule, including the priority, rule name, and configured forwarding conditions and forwarding actions. The last forwarding rule is the default forwarding rule. It has the lowest priority and cannot be modified, edited, or deleted.

**Modify a forwarding rule**

i. Click **Modify** in the upper-right corner of a custom forwarding rule section. ii. In the **Modify Forwarding Rule** section, modify the settings of **Priority**, **Rule Name**, and forwarding conditions and actions, and click **OK**. For more information, see Step 8.

**Delete a forwarding rule**

i. Click **Delete** in the upper-right corner of a custom forwarding rule section. ii. In the **Delete Rule** message, click **OK**.

###### Create outbound forwarding rules

**Prerequisites**

A listener is created. For more information, see Add listeners.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. Use either of the following methods to open the Listener tab.
On the **Instance Management** page, find the target instance and click **View All**
**({TotalCount})** in the **Listener** column.
On the details page of an ALB instance a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Listener** tab.
5. Use either of the following methods to open the Forwarding Rules tab.
In the listener list, find the target listener and click **View/Modify Forwarding Rule** in the **Actions** column. On the listener details page: a. In the listener list, find the target listener and click its ID in the **Listener ID/Name** column, or click **View Details** in the **Actions** column. b. Click the **Forwarding Rules** tab. Application Load Balancer User G
6. Click **Outbound Forwarding Rules**.
7. Click **Add Rule**.
8. In the **Add Forwarding Rule** section, configure the following parameters and click **OK**.

**Note**

You must add at least one forwarding condition and action. The logical operator among the actions for each condition is OR. If you specify multiple actions for a condition, requests that match one of the actions are forwarded. The logical operator among different conditions is AND. If you specify multiple conditions in a forwarding rule, a request is forwarded when all conditions are met.
**Priority**: Enter the priority of the forwarding rule. Valid values: 1 to 10000. A smaller
value indicates a higher priority.
**Rule Name**: Enter a name for the forwarding rule. If you do not specify this parameter, a
name is automatically assigned.

**Note**

You can specify only one name for a forwarding rule.

**Forwarding Conditions**

**Inbound Forwarding Conditions (Optional):** Select a condition type and configure
the inbound forwarding conditions.

**Note**

Click **Add Inbound Forwarding Condition** to add multiple forwarding conditions. A maximum of nine forwarding conditions can be added. Click the or icon on the right of a forwarding condition to adjust the order of forwarding conditions. Click the icon next to a forwarding condition to delete the forwarding condition. Application Load Balancer User G
**Domain Name**: Add a domain name. Example: `*.example.com` .
By default, the exact match mode is used and wildcard characters are supported. You must specify a domain name. The value must be 3 to 128 characters in length and can contain lowercase letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?. The value must contain at least one period (.) and cannot start or end with a period (.). The rightmost domain tag can contain only letters and wildcard characters. It cannot contain digits or hyphens (-). If the value starts with a tilde (~), the regular expression matching mode is used and the value is case-insensitive. You must specify a domain name in regular expression matching mode. In regular expression matching mode, the regular expression cannot start with an asterisk (*).

**Note**

You can click **Add Domain Name** to add multiple domain names. You can click the icon next to a domain name to delete the domain name.
**Path**: Add a path. For example, if the URL is www.example.com/test/test1?x=1&y=2 ,
you can set the parameter to `/test/*` . By default, the exact match mode is used and wildcard characters are supported. If the value starts with a tilde plus an asterisk (~*), the regular expression matching mode is used and the value is case-sensitive. You must specify a path. In non-regular expression matching mode, the value must start with a forward slash (/). In non-regular expression matching mode, the value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * ~ _ + $ & ' @ / ?. If the value starts with a tilde (~), the regular expression matching mode is used and the value is case-insensitive. If the value starts with a tilde plus an asterisk (~*), the regular expression matching mode is used and the value is case-sensitive. You must specify a path in regular expression matching mode. In regular expression matching mode, the value must be 1 to 128 characters in length and can contain letters, digits, and the following special characters: - . * = ~ _ + \ ^ ! $ & | ( ) [ ] ?.

**Note**

You can click **Add Path** to add multiple paths. You can click the icon next to a path to delete the path.

| www.example.com/test/test1?x=1&y=2 |  |
|---|---|
| y:2 | . |

Application Load Balancer User G
**HTTP Header**: Add HTTP headers. For example, you can set the key to `user-agent`
and the value to `*Mozilla/4.0*` .
**Key:** Enter a name for the HTTP header.
You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (- ), and underscores (_). You cannot set this parameter to Cookie or Host.
**Value:** Enter a value for the HTTP header.
You must specify a value. The value must be 1 to 128 characters in length and can contain printable characters. It cannot start with a space and end with a space or a backward slash (\). It cannot contain double quotation marks (").

**Note**

You can click **Add Header Value** to add multiple header values. You can click the icon next to a header value to delete the header value.
**Key**: Enter the key of a query string.
You must specify a key. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | & " < >.
**Value**: Enter the value of the query string.
You must specify a value. The value must be 1 to 128 characters in length and can contain lowercase letters and printable characters. It cannot contain spaces and the following special characters: # [ ] { } \ | & " < >.

**Note**

You can click **Add String** to add multiple key-value pairs. You can click the icon next to a key-value pair to delete the key-value pair.
**HTTP Request Method**: Add HTTP request methods.
Valid values: **HEAD**, **GET**, **POST**, **OPTIONS**, **PUT**, **PATCH**, and **DELETE**.

**Note**

You can click **Add Method** to add multiple HTTP request methods. You can click the icon next to a request method to delete the request method. Application Load Balancer User G
**Cookie**: Add cookies. For example, you can set the key to `key` and the value to
`value` .
**Key**: Enter a key.
You must specify a key. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain uppercase letters, spaces, and the following special characters: # [ ] { } \ | & " < > .
**Value**: Enter the value.
You must specify a value. The value must be 1 to 100 characters in length and can contain printable characters. It cannot contain spaces and the following special characters: # [ ] { } \ | & " < > .

**Note**

You can click **Add Cookie** to add multiple key-value pairs. You can click the icon next to a key-value pair to delete the key-value pair.
**SourceIp**: Add an IP address or a CIDR block. Example: `192.168.1.1/32` .
Standard IP addresses are supported. CIDR blocks of the 0.0.0.0/x type are not supported, where x indicates a digit.

**Note**

You can click **Add Source IP Address** to add multiple source IP addresses. You can click the icon next to a source IP address to delete the source IP address.
**Outbound Forwarding Conditions:** Select a condition type and configure outbound
forwarding conditions.

**Note**

For a forwarding rule, you can add at most one outbound forwarding condition of the **Response Header** type.

**Note**

Click **Add Inbound Forwarding Condition** to add multiple forwarding conditions. A maximum of nine forwarding conditions can be added. Click the or icon on the right of a forwarding condition to adjust the order of forwarding conditions. Click the icon next to a forwarding condition to delete the forwarding condition. Application Load Balancer User G
**Response Status Code**: the status code returned to the client in the response.
You must specify the status code. The response status code must be a number in the range of 100 to 599 and can be a range. Example: 200-233.

**Note**

You can click **Add Status Code** to add an additional status code. You can click the icon to the right of a status code to delete the status code.
**Response Header**: Specify the HTTP headers carried in the response.
**Key:**: Enter a name for the HTTP header.
You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (- ), and underscores (_). You cannot set this parameter to Cookie or Host.
**Value:**: Enter a value for the HTTP header.
You must specify a value. The value must be 1 to 128 characters in length and can contain printable characters. It cannot start with a space and end with a space or a backward slash (\). It cannot contain double quotation marks (").

**Note**

You can click **Add Response Header Value** to add an additional header value. You can click the icon to the right of a header value to delete the header value.
**Forwarding Action**: Select an action type and configure **Execute**.

**Note**

You can add only one forwarding action of the **Return Fixed Response** type for a forwarding rule.

**Note**

You can click **Add Action** to add multiple forwarding actions. You can add up to five forwarding actions. You can click the or icon on the right side of a forwarding action to adjust the order of forwarding actions. You can click the icon next to a forwarding action to delete the forwarding action. Application Load Balancer User G

**Return Fixed Response**

**Response Status Code**: Enter the response status code.
Only 2xx, 4xx, and 5xx strings are supported. x indicates a digit.
**Response Content Type (Optional)**: Select a response content type. Valid values:
**text/plain**, **text/css**, **text/html**, **application/javascript**, and **application/json**.
**Response Content (Optional)**: Enter the response content.
The value must be 0 to 1024 characters in length and can contain only ASCII characters.
**Write Header**: Newly added headers overwrite the existing headers.
**Content Type**: Select a content type. Valid values: **Custom**, **Reference**, and
**System-defined**.
**Key:**: Enter the name of the header that you want to add to the response.
You must specify a key. It must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
**Value:**: Enter or select the value of the header that you want to add to the response.
If you set **Content Type** to **Custom**, enter the header content. If you set **Content Type** to **Reference**, enter the header content. You must specify a value. The value must be 1 to 128 characters in length and can contain printable characters. It cannot start with a space and end with a space or a backward slash (\). It cannot contain double quotation marks ("). If you set **Content Type** to **System-defined**, you can set the Value parameter to
**Client Port**, **Client IP Address**, **Client Request Protocol**, **ALB Instance ID**,
and **ALB Listener Port**.

**Note**

The name is not case-sensitive. You cannot set a header name to one of the following values: connection, upgrade, content-length, and transfer-encoding.
**Delete Header**: Specify the key of the header that you want to delete. Then, the key
and value of the specified header are both deleted.

**Note**

The name is not case-sensitive. You cannot set a header name to one of the following values: connection, upgrade, content-length, and transfer-encoding.

**Related operations**

After you add a forwarding rule, you can perform the following operations on the **Outbound**
**Forwarding Rules** tab:

**View the list and details of forwarding rules**

You can enter at most 20 forwarding rule IDs in the **Forwarding Rule ID** field to search for forwarding rules. Separate multiple forwarding rule IDs with commas (,). In a forwarding rule section, you can view the details of a forwarding rule, including the priority, rule name, and configured forwarding conditions and forwarding actions.

**Modify a forwarding rule**

Application Load Balancer User G i. Click **Modify** in the upper-right corner of a custom forwarding rule section. ii. In the **Modify Forwarding Rule** section, modify the settings of **Priority**, **Rule Name**, and forwarding conditions and actions, and click **OK**. For more information, see Step 8.

**Delete a forwarding rule**

i. Click **Delete** in the upper-right corner of a custom forwarding rule section. ii. In the **Delete Rule** message, click **OK**.

#### Monitoring

You can view the monitoring data of an Application Load Balancer (ALB) instance in Cloud Monitor.

**Prerequisites**

An ALB instance is created. For more information, see Create an ALB instance.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
5. Use one of the following methods to view the monitoring data. By default, the monitoring
data of all metrics of the ALB instance within the last three hours is displayed. For more information about monitoring metrics, see Description of monitoring metrics. View the monitoring data in the ALB instance list: a. On the **Instance Management** page, find the ALB instance that you want to manage and click in the **Monitoring** column. b. In the panel that appears, view the monitoring data that is provided by Cloud Monitor for the ALB instance. View the monitoring data on the details page of the ALB instance: a. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.
b. On the **Details** page, click the **Monitoring** tab to view the monitoring data that is provided by Cloud Monitor for the ALB instance.

| Metric | Unit | Metric name | Dimensions | Description |
|---|---|---|---|---|
| Maximum concurrent connections | short | conn concurrent _ | instanceId | The maximum number of concurrent connections for the load balancer instance. |
| Failed TLS handshakes with backend servers per second | ops | ups tls cps fail _ _ _ | instanceId | The number of failed TLS handshakes per second between the load balancer instance and its backends. |
| New connections per second | ops | cps | instanceId | The number of new connections the load balancer instance establishes per second. |
| Failed connections to backend servers per second | ops | upstream conn error _ _ | instanceId | The number of failed connections per second from the load balancer instance to its backends. |
| Failed TLS handshakes per second | ops | tls cps fail _ _ | instanceId | The number of failed TLS handshakes per second between clients and the load balancer instance. |

Application Load Balancer User G

**Note**

You can specify multiple metrics to view the corresponding monitoring data. You can customize the start and end time to display the monitoring data within a specific time range. You can click **Last Hour**, **Last 3 Hours**, **Last 6 Hours**, **Last 12 Hours**, **Last 1**
**Day**, **Last 3 Days**, and **Last 7 Days** to query the monitoring data within the
selected time range. Click **View more** in the upper-right corner. The **Cloud Monitoring** page appears. On this page, you can perform more monitoring-related operations, including managing alert rules and rule description. For more information, see Manage cloud service monitoring.

| Redirections per second | ops | redirect count _ | instanceId | The number of redirection responses the load balancer instance sends per second. |
|---|---|---|---|---|
| Requests per second | ops | qps | instanceId | The number of requests the load balancer instance processes per second. |
| Backend response time | millisec onds | upstream rt _ | instanceId | The average time in milliseconds from when the load balancer instance sends a request to a backend to when it receives the response. |
| Request latency | millisec onds | rt | instanceId | The average time in milliseconds from when the load balancer instance receives a request to when it sends the response to the client. |
| Outbound bandwidth | bps | bytes out _ | instanceId | The rate of outbound traffic from the load balancer instance, measured in bits per second (bps). |
| Inbound bandwidth | bps | bytes in _ | instanceId | The rate of inbound traffic to the load balancer instance, measured in bits per second (bps). |
| 2xx responses per second | ops | status code 2xx _ _ | instanceId | The number of HTTP 2xx responses the load balancer instance generates per second. |
| 3xx responses per second | ops | status code 3XX _ _ | instanceId | The number of HTTP 3xx responses the load balancer instance generates per second. |

Application Load Balancer User G

| 4xx responses per second | ops | status code 4XX _ _ | instanceId | The number of HTTP 4xx responses the load balancer instance generates per second. |
|---|---|---|---|---|
| 500 responses per second | ops | 500 count _ | instanceId | The number of HTTP 500 responses the load balancer instance generates per second. |
| 502 responses per second | ops | 502 count _ | instanceId | The number of HTTP 502 responses the load balancer instance generates per second. |
| 503 responses per second | ops | 503 count _ | instanceId | The number of HTTP 503 responses the load balancer instance generates per second. |
| 504 responses per second | ops | 504 count _ | instanceId | The number of HTTP 504 responses the load balancer instance generates per second. |
| 5xx responses per second | ops | status code 5xx _ _ | instanceId | The number of HTTP 5xx responses the load balancer instance generates per second. |
| Backend 2xx responses per second | ops | upstream code 2xx _ _ | instanceId | The number of HTTP 2xx responses backends return per second. |
| Backend 3xx responses per second | ops | upstream code 3XX _ _ | instanceId | The number of HTTP 3xx responses backends return per second. |
| Backend 4xx responses per second | ops | upstream code 4XX _ _ | instanceId | The number of HTTP 4xx responses backends return per second. |

Application Load Balancer User G

| Backend 5xx responses per second | ops | upstream code 5XX _ _ | instanceId | The number of HTTP 5xx responses backends return per second. |
|---|---|---|---|---|
| Healthy host count | short | statusup | instanceId | The number of backend hosts that are passing health checks. |
| Unhealthy host count | short | statusdown | instanceId | The number of backend hosts that are failing health checks. |

| Certificat e | Description | Required for one- way authentication | Required for mutual authentication |
|---|---|---|---|
| Server certificate | A server certificate is used to authenticate the identity of a server. A client browser authenticates the identity of a server by checking whether the certificate sent by the server is issued by a trusted CA. | Yes You can purchase or upload a server certificate in the Certificate Management Service console. ALB obtains the certificate from Certificate Management Service and uses the certificate. | Yes You can purchase or upload a server certificate in the Certificate Management Service console. ALB obtains the certificate from Certificate Management Service and uses the certificate. |

Application Load Balancer User G

### Certificate management

#### Certificate overview

To create an HTTPS listener, you must configure an SSL certificate for identity authentication to secure data transmission.

**Certificates supported by Application Load Balancer (ALB)**

| CA certificate | A CA certificate is used by a server to verify the signature of a client certificate. If the signature is invalid, the connection request is denied. Note A client certificate is used to authenticate the identity of the client when the client communicates with the server. You need to install a client certificate only on the client. | No | Yes You can purchase or upload a CA certificate in the Certificate Management Service console. ALB obtains the certificate from Certificate Management Service and uses the certificate. |
|---|---|---|---|

Application Load Balancer User G

**Note**

Since the process of uploading, loading, and verifying a new certificate takes some time, an instance that uses HTTPS also requires a certain amount of time to apply the new certificate. The typical activation time is 1 to 3 minutes. If you want to access multiple domain names or add multiple server certificates, you can add additional certificates to the HTTPS listener. For more information, see Add an additional certificate.

#### Certificate requirements

Application Load Balancer (ALB) supports only NGINX certificates. Before you upload a certificate, make sure that the certificate content, certificate chain, and private key meet the corresponding format requirements.

**Certificates issued by a root CA**

If your certificate is issued by a root certificate authority (CA), the received certificate file contains only one certificate. You do not need other certificates to prove that the matching domain name is trusted. The certificate must meet the following format requirements: The certificate must start with `-----BEGIN CERTIFICATE-----` and end with -----END CERTIFICATE-----. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. The certificate content cannot contain spaces.

**Certificates issued by an intermediate CA**

If your certificate is issued by an intermediate CA, the received certificate file contains multiple certificates. You must upload both the server certificate and the required intermediate certificates to ALB. The format of the certificate chain must meet the following requirements: The server certificate must be put first and the content of the required intermediate certificates must be put underneath without blank lines between the certificates. The certificate content cannot contain spaces. Blank lines are not allowed between the certificates. Each line must contain 64 characters.

|  |  |  | Proc-Type: |
|---|---|---|---|
| 4,ENCRYPTED |  | ), you must run the following command to convert the private key: |  |
|  | openssl rsa -in old server key.pem -out new server key.pem _ _ _ _ |  |  |

| th |  |
|---|---|
| Proc-Type: |  |

Application Load Balancer User G For more information, see RFC1421. Certificates must meet the corresponding format requirements. In most cases, the intermediate CA provides instructions about the certificate format when certificates are issued. The certificates must meet the format requirements. The following section provides a sample certificate chain:

```
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
```

**Public keys of certificates**

ALB supports the following public key algorithms: RSA 1024 RSA 2048 RSA 4096 ECDSA P-256 ECDSA P-384 ECDSA P-521

**Formats of RSA private keys**

When you upload a server certificate, you must upload the private key of the certificate. An RSA private key must meet the following format requirements: The private key must start with `-----BEGIN RSA PRIVATE KEY-----` and end with -----END RSA PRIVATE KEY-----, and these parts must also be uploaded. Blank lines are not allowed in the content. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. For more information, see RFC1421.

**EC private key formats**

**Note**

EC private keys are supported only in the UK (London) region. When you upload a server certificate, you must upload the private key of the certificate. An EC private key must meet the following format requirements: The private key must start with `-----BEGIN EC PARAMETERS-----` and end with -----END EC PARAMETERS-----, and these parts must also be uploaded. Blank lines are not allowed in the content. Each line (except the last line) must contain 64 characters. The last line can contain 64 or fewer characters. For more information, see RFC1421.

| Parameter | Description |
|---|---|
| Regional Information |  |

Application Load Balancer User G `4,ENCRYPTED` . In this case, you must first run the following command to convert the private key:

```
openssl ec -in old_server_key.pem -out new_server_key.pem
```

The following section provides a sample EC private key:

```
-----BEGIN EC PARAMETERS----- Bggq**********Bw== -----END EC PARAMETERS----- -----BEGIN EC PRIVATE KEY----- MHcCAQEEICo9b+vQUhqFUWgWjE0YY4h0b3bE/udcubxVwcVY99MuoAoGCCqGSM49
***************************4xz0SHsuQc/7XBmgmrMpAmE80c0DR
5HcMHFxRPtGLv22T62e5KqN1W3uN9Hplgg== -----END EC PRIVATE KEY-----
```

#### Manage server certificates

This topic describes how to upload and manage server certificates.

**Prerequisites**

A server certificate is purchased. A certificate file obtained from a certificate provider contains the certificate issued by an intermediate CA and your certificate. This is also known as a certificate chain. When you upload a certificate, make sure that the certificate chain is valid. A public key certificate contains a public key and a digital signature. Server Load Balancer (SLB) instances use NGINX certificates issued by a certificate authority. Most of the NGINX certificates are suffixed with .pem, but some may be suffixed with .crt or other extensions. The private key of a certificate. A private key file is suffixed with .key and can be found in the NGINX certificate file issued by the certificate provider.

**Background information**

Up to 100 certificates can be created by each account.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Certificate Management**.
4. On the **Certificate Management** page, click the **Server Certificate** tab.
5. Click **Create Certificate**.
6. In the **Create Certificate** dialog box, configure the following parameters and click
**Submit**.

| Organization | Select the organization to which the certificate belongs. |
|---|---|
| Resource Set | Select the resource set to which the certificate belongs. |
| Certificate Deployment Region | Select the region in which you want to deploy the certificate. |
| Basic Information |  |
| Certificate Name | Enter a name for the certificate. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Certificate Type | Select a certificate type. In this example, Server Certificate is selected. |
| Certificate Standard | Select the certificate standard that you want to upload. By default, International Certificate is selected. |
| Public Key Certificate | Enter the content of the certificate file. Manually specify the content: Open the certificate file, copy the content, and then paste it to this field. Click View Sample to view the valid certificate format. For more information, see Certificate requirements. Upload a certificate file: Click Upload and select a certificate file. The file is parsed to the text box. |
| Private Key | Enter the content of the private key file for the certificate. Manually specify the content: Open the private key file, copy the content, and then paste it to this field. Click View Sample to view the valid certificate format. For more information, see Certificate requirements. Upload a certificate file: Click Upload and select the local private key file. The file is automatically parsed to the text box. |

Application Load Balancer User G

**What to do next**

**View the list of certificates**

On the **Server Certificate** tab of the **Certificate Management** page, you can view the following information about certificates: **Certificate ID/Name**, **Tag**, **Certificate Type**,
**Algorithm**, **User**, **Created At**, **Expired At**, **Organization/Resource Set**, **Sharing Scope**,
and **Creator**. You can filter certificates by keyword, **Certificate ID**, **Certificate Name**, **Tag**, and
**Creator**.
Application Load Balancer User G Click the icon in the upper-right corner to show or hide items in the certificate list. You can also drag and drop the items to adjust their order.

**Manage tags**

On the **Server Certificate** tab of the **Certificate Management** page, you can add tags to certificates for easier management. For more information, see Tag management.

**Modify the name of a certificate**

1. On the **Server Certificate** tab of the **Certificate Management** page, find the server
certificate that you want to manage and click the icon to the right of the name in the
**Certificate ID/Name** column.
2. In the **Modify Certificate Name** dialog box, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

**Delete a certificate**

**Note**

If a certificate is associated with a listener, the certificate cannot be deleted.
1. On the **Server Certificate** tab of the **Certificate Management** page, find the target
certificate and click **Delete** in the **Actions** column.
2. In the message that appears, click **OK**.

#### Manage CA certificates

This topic describes how to upload and manage CA certificates.

**Prerequisites**

A CA certificate and a client certificate are generated. A client CA certificate is used to verify the authority that issues the client certificate. If mutual authentication is enabled, an HTTPS connection can be established only if the client can provide a certificate issued by a given CA.

**Background information**

Up to 100 certificates can be created by each account.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Certificate Management**.
4. On the **Certificate Management** page, click the **Server Certificate** or **CA Certificate**
tab.
5. Click **Create Certificate**.

| Parameter | Description |
|---|---|
| Regional Information |  |
| Organization | The organization to which the certificate belongs. |
| Resource Set | The resource set to which the certificate belongs. |
| Certificate Deployment Region | The region in which you want to deploy the certificate. |
| Basic Information |  |
| Certificate Name | The name of the certificate. |
| Certificate Type | The type of certificate. In this example, CA Certificate is selected. |
| Client CA public key certificate | The CA public key certificate file of the client certificate. |

Application Load Balancer User G
6. On the **Create Certificate** page, configure the following parameters and click **Submit**.

**Related operations**

**View the list of certificates**

On the **CA Certificate** tab of the **Certificate Management** page, you can view the following information about CA certificates: **Certificate ID/Name**, **Tag**, **Algorithm**, **User**, **Created At**,
**Expired At**, **Organization/Resource Set**, **Sharing Scope**, and **Creator**.

**Manage tags**

On the **CA Certificate** tab of the **Certificate Management** page, you can add tags to instances for easier management. For more information, see Tag management.

**Modify the name of a certificate**

1. On the **CA Certificate** tab of the **Certificate Management** page, find the CA certificate
that you want to manage and click the icon to the right of the name in the **Certificate**
**ID/Name** column.
2.

**Remove a certificate**

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | The organization to which the server group belongs. |
| Resource Set | The resource set to which the server group belongs. |
| Region | The region to which the server group belongs. |
| Server Group Type | Select the type of server group that you want to create. Server Type: Backend servers are added by specifying Elastic Compute Service (ECS) instances. IP Address Type: Backend servers are added by specifying IP addresses. |

Application Load Balancer User G

**Note**

If a certificate is associated with a listener, the certificate cannot be removed.
1. On the **CA Certificate** tab of the **Certificate Management** page, find the target
certificate and click **Delete** in the **Actions** column. 2.

### Server group

Backend servers can be organized into logical groups (also known as server groups) to which requests are distributed. Each server group contains one or more backend servers that process requests distributed by Application Load Balancer (ALB). Server groups of ALB are independent of ALB. You can associate a server group with different ALB instances. By default, you can specify up to 100 backend servers in each server group. ALB supports multiple types of backend servers, such as Elastic Compute Service (ECS) instances, elastic network interfaces (ENIs), and IP addresses.

#### Create a server group

If you associate a server group with a listener, the listener distributes requests only to backend servers in the server group. This topic describes how to create a server group.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, click **Create Server Group**.
5. On the **Create Server Group** page, configure the following parameters.

| Server Group Name | The name of the custom server group. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start with a letter. _ |
|---|---|
| Network Settings |  |
| VPC | Select a virtual private cloud (VPC) from the VPC drop-down list. Only servers in the VPC can be added to the server group. Note You can click Create VPC to create a VPC. The VPC is available after you refresh the list. |
| Scheduling Algorithm | Select a scheduling algorithm. Weighted Round-robin is selected by default. Weighted Round-robin: Backend servers that have higher weights receive more requests than those that have lower weights. Weighted Least Connections: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, requests are forwarded to the backend server that has fewer connections. Consistent Hashing: Only high-performance ALB instances support consistent hashing. |
| Hash Factor | Select a hash factor. Source IP Address: Specify consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. URL Parameters: Requests for the same URL are forwarded to the same backend server. Note This parameter is required only if you set Scheduling Algorithm to Consistent Hashing. |
| Backend Protocol | Select the type of the backend protocol. By default, HTTP is selected. HTTP: If you select this option, you can associate the server group with HTTPS, HTTP, or QUIC listeners. HTTPS: If you select this option, you can associate the server group with HTTPS listeners. gRPC: If you select this option, HTTP/2 is used as the communication protocol. You can associate the server group with HTTPS listeners, and HTTP/2 must be enabled for the HTTPS listeners. |
| Advanced Configurations |  |

Application Load Balancer User G

| IPv6 | Specify whether to allow the addition of IPv6 backend servers to the server group after IPv6 is enabled for the VPC. This feature is disabled by default. If you do not enable this feature, you can add only IPv4 backend servers to the server group. If you enable this feature, you can add IPv4 and IPv6 backend servers to the server group. Note This parameter is available only if IPv6 is enabled for the selectedV PC. |
|---|---|
| Backend Long Link | Specify whether to enable persistent connection. By default, this feature is enabled. After this feature is enabled, a certain number of persistent connections are kept alive between ALB and backend servers. When ALB receives a new request and an idle persistent TCP connection exists, ALB first uses the persistent TCP connection to forward the request to the backend server. This reduces the number of TCP handshakes and the workload on the backend server. |
| Session Persistence |  |
| Enable Session Persistence | Specify whether to enable the session persistence feature. This feature is disabled by default. If this feature is disabled, ALB distributes each client request to a different backend server. If session persistence is enabled, ALB forwards all requests from a client to the same backend server. To enable session persistence, you must specify the cookie handling method. |
| Cookie Handling Method | The cookie processing method. Session persistence is implemented based on cookies. To enable session persistence, you must configure the following parameters: Insert Cookie: If you select this option, you need to only specify the timeout period for the cookie. ALB inserts a session cookie (ServerId) into the first HTTP or HTTPS response that is sent to a client. If subsequent requests to ALB carry this cookie, ALB determines the destination servers of the requests based on the cookie. Cookie Timeout Period: If you set Cookie Handling Method to Insert Cookie, specify a timeout period for session persistence. Valid values: 1 to 86400. Unit: seconds. Default value: 1000. Rewrite Cookie: If you select this option, you can specify the cookie that you want to insert into a response. You must specify the timeout period and the lifetime for the cookie on a backend server. If ALB detects a user-defined cookie, ALB replaces the original cookie with the user-defined cookie. If subsequent requests to ALB carry this user-defined cookie, ALB determines the destination servers of the requests based on the cookie. Cookie Configured on Server: Enter the name for a custom cookie if you set Cookie Handling Method to Rewrite Cookie. |

Application Load Balancer User G

| Slow Start |  |
|---|---|
| Enable Slow Start | Specify whether to enable the slow start mode. This feature is disabled by default. After slow start is enabled, the number of requests that ALB forwards to backend servers gradually increases. When the slow start duration ends, the speed of request forwarding between ALB and backend servers is no longer limited, and the backend servers exit the slow start mode. Note This parameter is required only when you set the Scheduling Algorithm parameter to Weighted Round-robin. After you enable the slow start mode, healthy backend servers do not automatically enter the slow start mode. When you enable the slow start mode for an empty server group: The first backend server added to the server group does not enter the slow start mode. New backend servers can enter the slow start mode only when at least one healthy backend server is not in slow start mode. Backend servers that are removed before the slow start duration ends automatically exit the slow start mode. If you re-add the backend server to a server group, the backend server can enter the slow start mode only when the backend server passes health checks. If a backend server is declared unhealthy before the slow start duration ends, the backend server exits the slow start mode. The backend server re-enters the slow start mode when the backend server passes health checks. After you enable the slow start mode and health checks, only healthy backend servers enter the slow start mode. If you disable health checks, all backend servers immediately enter the slow start mode. |
| Slow Start Duration | The slow start duration. Valid values: 30 to 900. Unit: seconds. Default value: 30. Note To enable slow start, you must specify the duration of slow start. |
| Connection Draining |  |

Application Load Balancer User G

| Enable Connection Draining | Specify whether to enable connection draining. This feature is disabled by default. When you remove a backend server or a backend server is declared unhealthy: If you disable connection draining, existing connections remain open until the clients proactively close the connections or the session persistence duration ends. After you enable connection draining, existing connections remain open for data transmission until the connection draining timeout period ends. Connection draining ensures smooth undeployment of services. |
|---|---|
| Connection Draining Timeout Period | The timeout period of connection draining. Valid values: 0 to 900. Unit: seconds. Default value: 300. Note This parameter is required only if you turn on Enable Connection Draining. |
| Health Check |  |
| Enable Health Check | Specify whether to enable the health check feature. By default, this feature is enabled. To enable health check, you must configure health check parameters. |
| Health Check Mode | After Enable Health Check is turned on, you need to select a health check mode. Custom is selected by default. Custom: You can customize the health check parameters. Select Template: Select the created health check configurations. |
| Health Check Template | After you turn on Enable Health Check and setH ealth Check Mode to Select Template, select a created health check. After you select a template, you can still customize health check parameters. Health check information includes Health Check ID/Name, Protocol, Port, Interval, Response Timeout Period, Health Threshold, and Unhealth Threshold. Click Advanced Filter and specify Health Check ID or Health Check Name to search for health checks. |

Application Load Balancer User G

| Health Check Protocol | The health check protocol. HTTP: HTTP health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. HTTPS: HTTPS health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. TCP: TCP health checks are performed at the network layer. ALB probes the port of a backend server to check whether the server is healthy by sending SYN packets. gRPC: ALB checks whether a backend server is healthy by sending POST or GET requests. |
|---|---|
| Health Check Method | The health check method. GET: If the size of a response exceeds 8 KB, the response is truncated. The results of the health check are not affected. HEAD: HTTP and HTTPS health checks support the HEAD method. Make sure that your backend server supports HEAD requests. If your backend server does not support the HEAD method or the HEAD method is disabled, health checks may fail. In this case, you can use the GET method. POST: Only gRPC health checks support the POST method. Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. HTTP and HTTPS health checks use the HEAD method by default. gRPC health checks use the POST method by default. |
| Health Check Protocol Version | The version for the health check protocol. HTTP1.1 HTTP1.0 Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Check Domain Name | The health check domain name. The internal IP address of your backend server is used as the domain name for the health check by default. You can specify a specific domain name. The name can contain only letters, digits, hyphens (-), and periods (.). Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. |

Application Load Balancer User G

| Health Check Port | The port that ALB uses to perform health checks on backend servers. By default, the backend port specified when you configure the listener is used for the health check. We recommend that you leave this parameter empty unless you want to specify a specific port. Valid values: 1 to 65535. |
|---|---|
| Health Check URL | The URL that is used for health checks. By default, ALB performs HTTP health checks by sending HTTP HEAD requests to the private IP address of a backend Elastic Compute Service (ECS) instance to visit the default homepage configured on the ECS instance. If you do not want to use the default homepage for health checks, you can specify a URL. It must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & =. It must start with a forward _ slash (/). Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| HTTP Health Status Code (HTTP and HTTPS) | The status codes that indicate a healthy backend server. You can select multiple options. Default values: http 2xx and http 3xx. Valid _ _ values: http 2xx _ http 3xx _ http 4xx _ http 5xx _ Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Check Status Code (gRPC) | The status codes that indicate a healthy backend server. Valid values: 0 to 99. You can enter up to 20 value ranges. Separate multiple value ranges with commas (,). Note This parameter is required if you set the Health Check Protocol parameter to gRPC. |
| Response Timeout (Seconds) | The timeout period for a response. The maximum timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. Default value: 5. The timeout period for a health check response. If a backend ECS instance does not return a health check response within the specified timeout period, the instance fails the health check. |

Application Load Balancer User G

| Interval (Seconds) | The interval between two consecutive health checks. The interval between two consecutive health checks. Valid values: 1 to 50. Default value: 2. Unit: seconds. |
|---|---|
| Health Threshold | The number of consecutive successful health checks that must occur before an application is declared healthy. Specify the number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. Valid values: 2 to 10. Default value: 3. |
| Unhealth Threshold | The number of consecutive failed health checks that must occur before an application is declared unhealthy. Specify the number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. Valid values: 2 to 10. Default value: 3. |

Application Load Balancer User G
6. Click **Submit**.

#### Manage server groups

##### Modify the name of a server group

**Prerequisites**

A server group is created. For more information, see Create a server group.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the server group that you want to manage and click the
icon to the right of the server group name in the **Server Group ID/Name** column.
5. In the dialog box that appears, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

##### Modify a server group

**Prerequisites**

A server group is created. For more information, see Create a server group.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
Application Load Balancer User G
4. Use either of the following methods to open the edit window.
On the **Server Group** page, find the target server group and click **Modify** in the **Actions** column. On the server group details page: a. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
b. On the **Details** page, click **Modify** in the upper-right corner.
5. On the **Modify Server Group Attributes** page or in the **Modify** dialog box, modify the
configurations of the server group and click **Submit**. For more information about the parameters, see Create a server group.

**Note**

The server group type, VPC, and backend protocol cannot be modified. To modify these parameters, create another server group.

##### Delete a server group

**Prerequisites**

A server group is created. For more information, see Create a server group.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the target server group and click **Delete** in the **Actions**
column.
5. In the **Delete Server Group** message, click **OK**.

#### View the list of server groups

**Prerequisites**

A server group is created. For more information, see Create a server group.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, you can view the list of server groups, including **Server**
**Group ID/Name**, **Tag**, **VPC**, **Type**, **IPv6**, **Backend Protocol**, **Servers**, **Associated**
**Instances**, **Organization/Resource Set**, and **Creator**.
You can filter server groups by keyword, **Server Group ID**, **Server Group Name**, **Tag**, and **Creator**. Application Load Balancer User G Click the icon in the upper-right corner to show or hide items in the server group list. You can also drag and drop the items to adjust their order. Move the pointer over the number in the **Associated Instances** column and click an instance ID to view the details of the ALB instance that is associated with the server group. Click the number in the **Servers** column. In the **Server Group Instance** dialog box, you can view the backend servers that are added to the server group. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.
5. Optional. On the **Server Group** page, you can add tags to server groups for easier
management. For more information, see Tag management.

#### View the details of a server group

**Prerequisites**

A server group is created. For more information, see Create a server group.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
5. On the **Details** page, you can view the details of the server group.
On the **Server Group Details** tab, you can view and manage **Basic Information**,
**Session Persistence**, **Slow Start**, **Connection Draining**, and **Health Check** of the
server group.
**Basic Information**: provides information such as **Server Group ID**, **Server Group**
**Name**, **Status**, **Server Group Type**, **VPC**, **Scheduling Algorithm**, **Backend**
**Protocol Type**, **IPv6**, **Backend Persistent Connection**, and **Created At**.
Click the ID below **VPC** to view the details of the VPC in which the server group resides.
**Session Persistence**: includes the enabling status of **Session Persistence** and the
**Cookie Option** and **Cookie Timeout Period** settings after session persistence is
enabled.
**Slow Start**: includes the enabling status of **Slow Start** and the **Duration** after Slow
Start is enabled. Application Load Balancer User G
**Connection Draining**: includes the enabling status of **Connection Draining** and the
**Timeout Period** after Connection Draining is enabled.
**Health Check**: includes the enabling status of **Health Check** and the **Protocol**,
**Protocol Version**, **Method**, **Domain Name**, **Path**, **Port**, **Normal Status Code**,
**Interval**, **Response Timeout Period**, **Health Threshold**, and **Unhealth Threshold**
after health check is enabled. On the **Backend Server** tab, you can view and manage the backend servers in the server group. For more information, see Backend servers.

#### Backend servers

##### Add backend servers

After you create a server group, you must add one or more backend servers to the server group based on the server group type. This way, the specified backend servers can receive requests distributed by Application Load Balancer (ALB). You can add backend servers of the server type and those of the IP address type.

**Prerequisites**

A server group is created. For more information, see Create a server group. An Elastic Compute Service (ECS) instance is created if you need to add a backend server of the server type.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
5. On the **Details** page, click the **Backend Server** tab.
6. Add backend servers based on your business requirements.
a. Click **Add Backend Server** to open the **Add Backend Server** panel. b. In the **Select Server** step, select the ECS instance that you want to add and click **Next**
**Step**.
The server information includes **Instance ID/Name** and **IP Address**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** You can enter a server name for fuzzy search of the destination server.**Server Name** Click an ID in the **Instance ID/Name** column to view the details of the ECS instance. Application Load Balancer User G c. In the **Port and Weight** step, configure ports, weights, and descriptions for all backend servers, and click **OK**.
**Port**: Specify the backend port that the ECS instance uses to receive requests.

**Note**

You can configure multiple backend ports. Valid values: 1 to 65535.
**Weight**: Specify the percentage of requests that the ALB instance distributes to the
backend server. Default value: 100.

**Note**

An ECS instance of a greater weight receives more requests. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive new requests.
**Description**: the description of the backend server.
The value must be 2 to 256 characters in length and can contain letters. It cannot start with http:// or https://. a. Click **Add IP Address** to open the **Add Backend Server** panel. b. In the **Select Server** step, configure an IP address and a remote IP address for the backend server, and then click **Next Step**.
**IP Address**: Enter the IP address of the backend server.
You can click **Add** to add an additional IP address. The format of the IP address, such as 192.168.0.0/16. To delete an IP address, click **Delete** in the **Actions** column.
**Remote IP Address**: An ALB instance can be associated with backend servers that
have IP addresses in different VPCs. If the specified IP address does not belong to the VPC of the current server group, select **Enable Remote IP Address**.

**Note**

You can specify multiple ports and weights for an IP address. If the remote IP address is disabled, the IP address to be added must fall into the CIDR block of the current VPC. If the remote IP address is enabled, you can add private IP addresses that fall into the CIDR block. Application Load Balancer User G c. In the **Port and Weight** step, configure ports, weights, and descriptions for all backend servers, and click **OK**.
**Port**: Specify the backend port that the ECS instance uses to receive requests.

**Note**

You can configure multiple backend ports. Valid values: 1 to 65535.
**Weight**: Specify the percentage of requests that the ALB instance distributes to the
backend server. Default value: 100.

**Note**

An ECS instance of a greater weight receives more requests. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive new requests.
**Description**: the description of the backend server.
The value must be 2 to 256 characters in length and can contain letters. It cannot start with http:// or https://.
7. Optional. On the **Backend Server** tab, you can view the list of backend servers that have
been added. For backend servers in a server group of the IP address type, you can view the following information: **IP Address**, **Status**, **Port**, **Weight**, and **Description**. You can enter IP addresses to filter backend servers. Separate multiple IP addresses with commas (,). You can enter up to 40 IP addresses.**IP Address** For backend servers in a server group of the server type, you can view the following information: **Instance ID,****IP**, **Zone,****Status**, **Port**, **Weight**, and **Description**. You can enter server IDs to filter servers. Separate multiple server IDs with commas (,). You can enter up to 40 server IDs.**Server ID** Click an ID in the **Instance ID** column to view the details of the ECS instance.

##### Modify the configuration of a backend

**server**

**Prerequisites**

A backend server is added. For more information, see Add backend servers.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
Application Load Balancer User G
4. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
5. On the **Details** page, click the **Backend Server** tab.
6. In the backend server list, modify the ports, weights, and descriptions based on your
business requirements.

**Modify a port**

a. Find the backend server that you want to manage, and click the icon in the **Port** column. b. In the **Change Port** dialog box, modify the value of the **Port** parameter and click **OK**.

**Note**

You can configure multiple backend ports. Valid values: 1 to 65535.

**Modify a weight**

a. Find the backend server that you want to manage, and click the icon in the **Weight** column. b. In the **Modify Weight** dialog box, modify the value of the **Weight** parameter and click
**OK**.

**Note**

An ECS instance of a greater weight receives more requests. Valid values: 0 to 100. If session persistence is enabled, requests may not be evenly distributed to backend servers. If you set the weight of a server to 0, the server does not receive new requests.

**Modify a description**

a. Find the backend server that you want to manage, and click the icon in the
**Description** column.
b. In the **Modify Description** dialog box, modify the value of the **Description** parameter and click **OK**. The value must be 2 to 256 characters in length and can contain letters. It cannot start with http:// or https://.

##### Remove a backend server

You can remove a backend server from a server group based on your business requirements. After the server is removed, the server no longer processes client requests.

**Prerequisites**

A backend server is added. For more information, see Add backend servers.

**Procedure**

Application Load Balancer User G
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Server**
**Groups**.
4. On the **Server Group** page, find the target server group and click its ID in the **Server**
**Group ID/Name** column.
5. On the **Details** page, click the **Backend Server** tab.
6. In the backend server list, find the target backend server and click **Remove** in the **Actions**
column.
7. In the **Remove Server** message, click **OK**.

### Health checks

#### Health check overview

Application Load Balancer (ALB) uses health checks to test the availability of backend servers. The health check feature improves overall service availability and reduces the impacts of backend server failures.

**Background information**

ALB allows you to configure health checks for server groups. By default, health checks are enabled for all server groups. If a backend server is declared unhealthy, ALB does not forward requests to the backend server. ALB supports flexible health check configurations. For example, you can specify the protocol, port, and thresholds for health checks. ALB provides health check templates that can be applied to different server groups. After you enable the health check feature for an ALB instance, the ALB instance periodically checks whether the backend Elastic Compute Service (ECS) instances are healthy. When the ALB instance detects an unhealthy ECS instance, the ALB instance distributes new requests to other healthy ECS instances. When the unhealthy ECS instance recovers, the ALB instance distributes requests to the recovered ECS instance again. If your business is highly sensitive to traffic fluctuations, frequent health checks may affect the availability of your business. To reduce the adverse impacts of health checks on your business, you can reduce the health check frequency, increase the health check interval, or change Layer 7 health checks to Layer 4 health checks. To ensure business continuity, we recommend that you enable the health check feature. ALB instances are deployed in clusters. Nodes in a Linux virtual server (LVS) or Tengine cluster are used to forward data and perform health checks. Nodes in an LVS cluster forward data and perform health checks independently and in parallel based on the configured load balancing policies. If a node in an LVS cluster detects an unhealthy backend ECS instance, the node stops sending client requests to the unhealthy ECS instance. This operation is synchronized across all of the nodes in the LVS cluster. The following figure shows how health checks work. Application Load Balancer User G ALB uses the CIDR block 100.64.0.0/10 for health checks. Make sure that the backend ECS instances do not block this CIDR block. You do not need to configure a security group rule to allow access from the CIDR block 100.64.0.0/10 unless security rules such as iptables are configured. Permitting 100.64.0.0/10 does not increase potential risks because this CIDR block is reserved by Apsara Stack. IP addresses within this CIDR block are not allocated to users.

**Layer 7 health checks on HTTP and HTTPS listeners**

If you add Layer 7 HTTP or HTTPS listeners to your ALB instance, ALB checks the status of backend ECS instances by sending HTTP HEAD requests, as shown in the following figure. For HTTPS listeners, certificates are managed in ALB. To improve system performance, HTTPS is not used to exchange data, including health check data and business data, between the ALB instance and backend ECS instances. How ALB performs Layer 7 health checks:
1. A Tengine node sends an HTTP HEAD request to a backend ECS instance based on the
health check configurations of the Layer 7 listener. The HTTP HEAD request is sent to an address in the following format: ECS instance private IP address + Health check port + Health check path. The HTTP HEAD request also carries the domain name specified in health check configurations.
2. After the backend ECS instance receives the request, the ECS instance checks the status of
the application and returns a relevant HTTP status code.
3. If the Tengine node does not receive a response from the backend ECS instance within the
specified timeout period, the backend server is considered unhealthy.
4. If the Tengine node receives a response from the backend ECS instance within the specified
timeout period, the node matches the returned status code against the status codes specified in health check configurations. If the returned status code matches one of the specified status codes, the backend server is considered healthy. Otherwise, the backend server is considered unhealthy. Application Load Balancer User G

**Health check time windows**

The health check feature improves the availability of your services. However, frequent failovers caused by unhealthy backend servers may affect system availability. Health check time windows are introduced to control failovers. A failover is performed only if a backend server consecutively passes or fails a specific number of health checks within a time window. A health check time window is determined by the following factors: Health check interval: the interval at which health checks are performed. Response timeout period: the amount of time that a backend server takes to respond. Health check threshold: the number of consecutive times that a backend server passes or fails health checks. Health check time windows are calculated by using the following formulas: Time window for health check failures = Response timeout period × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1) Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1)

**Note**

The response time of a successful health check is the duration from the time when a health check request is sent to the time when a response is received. When TCP health checks are configured, the response time is short and almost negligible because the only check item is whether the probed port is alive. When HTTP health checks are configured, the response time varies based on the performance and load of the application server and is typically within a few seconds. Application Load Balancer User G The health check result has the following impacts on request forwarding: If the backend ECS instance fails the health check, new requests are distributed to other backend ECS instances. The client can still access the application as normal. If the backend ECS instance passes the health check, new requests are distributed to the ECS instance. The client can access the application as normal. If an exception occurs on the backend ECS instance and a request arrives during the time window for health check failures, the request is still sent to the unhealthy backend ECS instance. This is because the number of failed health checks has not reached the unhealthy threshold (three times by default). In this case, the client fails to access the application. Application Load Balancer User G

**Examples of the health check response timeout period and the**

**health check interval**

In this example, the following health check configurations are used:

**Response timeout period: 5 seconds**

**Health check interval: 2 seconds**

**Healthy threshold: 3 times**

**Unhealthy threshold: 3 times**

Time window for health check failures = Response timeout period × Unhealthy threshold + Health check interval × (Unhealthy threshold - 1). In this example, the time window is 19 seconds based on the following formula: 5 × 3 + 2 × (3 - 1). If a backend server does not respond within 19 seconds, the backend server is considered unhealthy. The following figure shows the time window from a healthy status to an unhealthy status. Time window for health check successes = Response time of a successful health check × Healthy threshold + Health check interval × (Healthy threshold - 1). In this example, the time window is 7 seconds based on the following formula: (1 × 3) + 2 × (3 - 1). If a backend server responds within 7 seconds, the backend server is considered healthy. Application Load Balancer User G

**Note**

The response time of a successful health check is the duration from the time when a health check request is sent to the time when a response is received. When TCP health checks are configured, the response time is short and almost negligible because the only check item is whether the probed port is alive. When HTTP health checks are configured, the response time varies based on the performance and load of the application server and is typically within a few seconds. The following figure shows the time window from an unhealthy status to a healthy status. In the following figure, the amount of time that is required for the server to respond to a health check request is 1 second. You can specify a domain name for HTTP health checks. This setting is optional. Some application servers must verify the host field in requests before the application servers can accept the requests. In this case, the request header must carry the host field. If a domain name is specified in health check configurations, ALB adds this domain name to the host field when ALB forwards a health check request to an application server. If no domain name is specified, ALB does not include the host field in the request. As a result, the request is rejected by the application server and the health check fails. If your application server verifies the host field in requests, you must specify a domain name in health check configurations to ensure that the health check feature works as expected.

#### Create a health check

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Health**
**Checks**.

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | The organization to which the health check belongs. |
| Resource Set | The resource set to which the health check belongs. |
| Region | The region to which the health check belongs. |
| Health Check Name | The name of the health check. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The _ name must start with a letter. |
| Detailed Configuration |  |
| Health Check Protocol | The protocol that is used to perform the health check. Valid values: HTTP: HTTP health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. HTTPS: HTTPS health checks are performed in a similar way as a browser accesses a web page. ALB checks whether a backend server is healthy by sending HEAD or GET requests. TCP: TCP health checks are performed at the network layer. ALB probes the port of a backend server to check whether the server is healthy by sending SYN packets. gRPC: ALB checks whether a backend server is healthy by sending POST or GET requests. |

Application Load Balancer User G
4. On the **Health Check** page, click **Create Health Check**.
5. In the **Create Health Check** dialog box, configure the following parameters and click
**Submit**.

| Health Check Method | The method that is used for the health check. Valid values: GET: If the size of a response exceeds 8 KB, the response is truncated. The results of the health check are not affected. HEAD: HTTP and HTTPS health checks support the HEAD method. Make sure that your backend server supports HEAD requests. If your backend server does not support the HEAD method or the HEAD method is disabled, health checks may fail. In this case, you can use the GET method. POST: Only gRPC health checks support the POST method. Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. HTTP and HTTPS health checks use the HEAD method by default. gRPC health checks use the POST method by default. |
|---|---|
| Health Check Protocol Version | The version of the health check protocol. Valid values: HTTP1.1 HTTP1.0 Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Check Domain | The domain name that is used for the health check. The internal IP address of your backend server is used as the domain name for the health check by default. You can specify a specific domain name. The name can contain only letters, digits, hyphens (-), and periods (.). Note This parameter is required if you set the Health Check Protocol parameter to HTTP, HTTPS, or gRPC. |
| Health Check Port | The port that ALB uses to perform health checks on backend servers. By default, the backend port specified when you configure the listener is used for the health check. We recommend that you leave this parameter empty unless you want to specify a specific port. Valid values: 1 to 65535. |

Application Load Balancer User G

| Health Check Path | By default, ALB performs HTTP health checks by sending HTTP HEAD requests to the private IP address of a backend Elastic Compute Service (ECS) instance to visit the default homepage configured on the ECS instance. If you do not want to use the default homepage for health checks, you can specify a URL. It must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & =. It must _ start with a forward slash (/). Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
|---|---|
| Health Status Return Code (HTTP, HTTPS) | The status codes that indicate a healthy backend server. You can select multiple options. Default values: http 2xx and http 3xx. _ _ Valid values: http 2xx _ http 3xx _ http 4xx _ http 5xx _ Note This parameter is required if you set the Health Check Protocol parameter to HTTP or HTTPS. |
| Health Status Return Code (gRPC) | The status codes that indicate a healthy backend server. Valid values: 0 to 99. You can enter up to 20 value ranges. Separate multiple value ranges with commas (,). Note This parameter is required if you set the Health Check Protocol parameter to gRPC. |
| Response Timeout (seconds) | The response timeout period. The maximum timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. Default value: 5. The timeout period for a health check response. If a backend ECS instance does not return a health check response within the specified timeout period, the instance fails the health check. |
| Interval (seconds) | The interval between two consecutive health checks. Valid values: 1 to 50. Default value: 2. Unit: seconds. |

Application Load Balancer User G

| Health Threshold | Specify the number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. Valid values: 2 to 10. Default value: 3. |
|---|---|
| Unhealth Threshold | Specify the number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. Valid values: 2 to 10. Default value: 3. |

Application Load Balancer User G
6. Optional. On the **Health Check** page, view the following information about health checks:
**Health Check ID/Name**, **Tag**, **Protocol**, **Protocol Version**, **Method**, **Domain Name**,
**Path**, **Port**, **Normal Status Code**, **Interval**, **Response Timeout Period**, **Health**
**Threshold**, **Unhealth Threshold**, **Organization/Resource Set**, and **Creator**.
You can filter health checks by keyword, **Health Check ID**, **Health Check Name**, **Tag**, and **Created By**. Click the icon in the upper-right corner to show or hide items in the health check list. You can also drag and drop the items to adjust their order.
7. Optional. On the **Health Check** page, you can add tags to health checks for easier
management. For more information, see Tag management.

#### Modify the name of a health check

**Prerequisites**

A health check is created. For more information, see Create a health check.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Health**
**Checks**.
4. On the **Health Check** page, find the health check that you want to manage and click the
icon to the right of the health check name in the **Health Check ID/Name** column.
5. In the **Modify Name** dialog box, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

#### Modify a health check

**Prerequisites**

A health check is created. For more information, see Create a health check.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
Application Load Balancer User G
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Health**
**Checks**.
4. On the **Health Check** page, find the target health check and click **Modify** in the **Actions**
column.
5. In the **Modify** dialog box, modify the parameter settings and click **Submit**.
For more information about the parameters, see Create a health check.

#### Delete a health check

**Prerequisites**

A health check is created. For more information, see Create a health check.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Health**
**Checks**.
4. On the **Health Check** page, find the target health check and click **Delete** in the **Actions**
column.
5. In the **Delete Health Check** message, click **OK**.

### Access control

#### Access control overview

If you want to implement fine-grained access control for Application Load Balancer (ALB), you can enable the access control feature for ALB listeners and configure inbound rules that allow or deny access. This way, you can manage request forwarding and ensure the security and efficiency of network services. You can set whitelists or blacklists for different listeners. Whitelist: Only requests from the IP addresses or CIDR blocks in the whitelist are forwarded. Whitelists apply to scenarios in which you want to allow requests only from specific IP addresses. Risks may arise if the whitelist is improperly configured. After a whitelist is configured, the ALB listener is accessible only from IP addresses that are in the whitelist. If you configure a whitelist but do not add an IP address to the whitelist, the listener forwards all requests. Blacklist: All requests from the IP addresses or CIDR blocks specified in the ACL are denied. Blacklists apply to scenarios in which you want to block access from specific IP addresses. If you configure a blacklist but do not add an IP address to the blacklist, the listener forwards all requests.

**Configuration procedure**

The following figure shows how to configure an ACL for a listener.

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | Select the organization to which the ACL belongs. |
| Resource Set | Select the resource set to which the ACL belongs. |
| ACL Name | The name of the ACL. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start with a letter. _ |

Application Load Balancer User G

#### Create an ACL

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Access**
**Control**.
4. On the **Access Control** page, click **Create ACL**.
5. In the **Create ACL** dialog box, configure the following parameters and click **Submit**.
6. Optional. On the **Access Control** page, view the following information about ACLs: **ACL**
**ID/Name**, **Tag**, **Status**, **Created At**, **Organization/Resource Set**, and **Creator**.
You can filter ACLs by keyword, **ACL ID**, **ACL Name**, **Tag**, and **Creator**. Click the icon in the upper-right corner to show or hide items in the ACL list. You can also drag and drop the items to adjust their order.
7. Optional. On the **Access Control** page, you can add tags to ACLs for easier management.
For more information, see Tag management.

#### Modify the name of an ACL

**Prerequisites**

An access control list (ACL) is created. For more information, see Create an ACL.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Access**
**Control**.
Application Load Balancer User G
4. On the **Access Control** page, find the ACL whose name you want to modify and click the
icon to the right of the ACL name in the **ACL ID/Name** column.
5. In the **Modify Name** dialog box, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

#### Delete an ACL

**Prerequisites**

An access control list (ACL) is created. For more information, see Create an ACL.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Access**
**Control**.
4. On the **Access Control** page, find the target access policy group and click **Delete** in the
**Actions** column.
5. In the **Delete ACL** message, click **OK**.

#### Manage ACLs

After you create an access control list (ACL), you can add entries to the ACL. ACL entries specify the source IP addresses or CIDR blocks from which requests are sent to your ALB instance. You can add multiple IP addresses or CIDR blocks to each ACL.

**Prerequisites**

An access control list (ACL) is created. For more information, see Create an ACL.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Access**
**Control**.
4. On the **Access Control** page, find the target access policy group and click its ID in the **ACL**
**ID/Name** column, or click **Manage** in the **Actions** column.
5. On the page that appears, perform the following operations to manage the ACL.

**Add entries to the ACL**

a. Click **Add Entry**.

| Security policy ID | Supported TLS version | Supported cipher suite |
|---|---|---|

Application Load Balancer User G b. In the **Add Entry** dialog box, configure the following parameters and click **OK**.
**SN**: the serial number of the added entry.
**CIDR Block**: Enter a CIDR block.
The format of a CIDR block, such as 192.168.1.1 or 192.168.1.1/32.
**Remarks**: Enter a description.

**Note**

Click **Add Entry** to add an additional entry. Click the icon in the **Actions** column of an entry to delete the entry.

**Remove an entry from an ACL**

a. In the entry list, find the target entry and click **Delete** in the **Actions** column. b. In the **Delete Entry** message, click **OK**.

### Security policies

This topic describes how to configure a custom TLS security policy for Application Load Balancer (ALB). In most cases, websites or applications deployed on Alibaba Cloud use HTTPS to encrypt data transmission. ALB provides some commonly used TLS security policies to enhance the security of services that use HTTPS. ALB also allows you to configure custom TLS security policies. For example, you can specify the TLS versions that you want to use, or disable certain TLS cipher suites. A TLS security policy consists of TLS versions and cipher suites. A later version supports higher protection but lower compatibility with browsers.

| tls cipher policy 1 0 _ _ _ _ | TLSv1.0 TLSv1.1 TLSv1.2 | ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-RSA-AES128-SHA256 ECDHE-RSA-AES256-SHA384 AES128-GCM-SHA256 AES256-GCM-SHA384 AES128-SHA256 AES256-SHA256 ECDHE-ECDSA-AES128-SHA ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES128-SHA ECDHE-RSA-AES256-SHA AES128-SHA AES256-SHA DES-CBC3-SHA |
|---|---|---|
| tls cipher policy 1 1 _ _ _ _ | TLSv1.1 TLSv1.2 | ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-RSA-AES128-SHA256 ECDHE-RSA-AES256-SHA384 AES128-GCM-SHA256 AES256-GCM-SHA384 AES128-SHA256 AES256-SHA256 ECDHE-ECDSA-AES128-SHA ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES128-SHA ECDHE-RSA-AES256-SHA AES128-SHA AES256-SHA DES-CBC3-SHA |

Application Load Balancer User G

| tls cipher policy 1 2 _ _ _ _ | TLSv1.2 | ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-RSA-AES128-SHA256 ECDHE-RSA-AES256-SHA384 AES128-GCM-SHA256 AES256-GCM-SHA384 AES128-SHA256 AES256-SHA256 ECDHE-ECDSA-AES128-SHA ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES128-SHA ECDHE-RSA-AES256-SHA AES128-SHA AES256-SHA DES-CBC3-SHA |
|---|---|---|
| tls cipher policy 1 2 s _ _ _ _ _ trict | TLSv1.2 | ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-RSA-AES128-SHA256 ECDHE-RSA-AES256-SHA384 ECDHE-ECDSA-AES128-SHA ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES128-SHA ECDHE-RSA-AES256-SHA |

Application Load Balancer User G

| tls cipher policy 1 2 s _ _ _ _ _ trict with 1 3 _ _ _ | TLSv1.2 TLSv1.3 | TLS AES 128 GCM SHA256 _ _ _ _ TLS AES 256 GCM SHA384 _ _ _ _ TLS CHACHA20 POLY1305 SHA256 _ _ _ TLS AES 128 CCM SHA256 _ _ _ _ TLS AES 128 CCM 8 SHA256 _ _ _ _ _ ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-RSA-AES128-SHA256 ECDHE-RSA-AES256-SHA384 ECDHE-ECDSA-AES128-SHA ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES128-SHA ECDHE-RSA-AES256-SHA |
|---|---|---|

| Parameter | Description |
|---|---|
| Basic Information |  |
| Organization | The organization to which the security policy belongs. |

Application Load Balancer User G

#### Creates a custom security policy

ALB provides some commonly used TLS security policies to enhance the security of services that use HTTPS. ALB also allows you to configure custom TLS security policies. For example, you can specify the TLS versions that you want to use, or disable certain TLS cipher suites.

**Limits**

When you specify TLS versions and cipher suites for a custom TLS security policy, make sure that the TLS versions and cipher suites are supported by the clients, such as browsers. Otherwise, the clients may fail to establish connections to the server.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Security**
**Policies**.
4. On the **Security Policy** page, click **Create Security Policy**.
5. On the **Create Security Policy** dialog box, configure the following parameters and click
**Submit**.

|  | Application Load Balancer User G uide·AL |
|---|---|

| Resource Set | The resource set to which the security policy belongs. |
|---|---|
| Region | The region to which the security policy belongs. |
| Name | The name of the custom security policy. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Policy Information |  |
| Minimum Version | Select the versions of the TLS security policy that you want to create.T LSv1.0 is selected by default. Valid values: TLSv1.0 TLSv1.1 TLSv1.2 |
| Enable TLS 1.3 Version | Select whether to enable TLS 1.3. By default, this option is disabled. After you enable TLS 1.3, select at least one cipher suite supported by the version. Otherwise, connection establishments may fail. |

| Encryption Algorithm Suite | Select cipher suites that are supported by the specified TLS version. You can select multiple options. ECDHE-ECDSA-AES128-SHA / International ECDHE-ECDSA-AES256-SHA / International ECDHE-RSA-AES128-SHA / International ECDHE-RSA-AES256-SHA / International AES128-SHA / International AES256-SHA / International DES-CBC3-SHA / International ECDHE-ECDSA-AES128-GCM-SHA256 / International ECDHE-ECDSA-AES256-GCM-SHA384 / International ECDHE-ECDSA-AES128-SHA256 / International ECDHE-ECDSA-AES256-SHA384 / International ECDHE-RSA-AES128-GCM-SHA256 / International ECDHE-RSA-AES256-GCM-SHA384 / International ECDHE-RSA-AES128-SHA256 / International ECDHE-RSA-AES256-SHA384 / International AES128-GCM-SHA256 / International AES256-GCM-SHA384 / International AES128-SHA256 / International AES256-SHA256 / International ECC-SM2-WITH-SM4-SM3 / State Secret |
|---|---|
| Encryption Algorithm TLS1.3 Version Suite | Select cipher suites that are supported by TLS 1.3. You can select multiple options. TLS AES 128 GCM SHA256 _ _ _ _ TLS AES 256 GCM SHA384 _ _ _ _ TLS CHACHA20 POLY1305 SHA256 _ _ _ TLS AES 128 CCM SHA256 _ _ _ _ TLS AES 128 CCM 8 SHA256 _ _ _ _ _ |

Application Load Balancer User G
6. Optional. On the **Security Policy** page, you can view the information about created
security policies, including **Security Policy ID/Name**, **Tag**, **TLS Protocol**, **Cipher Suite**,
**Status**, **Organization/Resource Set**, and **Creator**.
You can filter security policies by keyword, **Security Policy ID**, **Security Policy Name**,
**Tag**, and **Creator**.
Click the icon in the upper-right corner to show or hide items in the security policy list. You can also drag and drop the items to adjust their order.
7. Optional. On the **Security Policy** page, you can add tags to security policies for easier
management. For more information, see Tag management. Application Load Balancer User G

#### Modify the name of a custom security

**policy**

**Prerequisites**

A custom security policy is created. For more information, see Create a custom security policy.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Security**
**Policies**.
4. On the **Security Policy** page, find the security policy whose name you want to modify and
click the icon to the right of the security policy name in the **Security Policy ID/Name** column.
5. In the **Modify Name** dialog box, modify the **Name** parameter and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.

#### Delete a custom security policy

**Prerequisites**

A custom security policy is created. For more information, see Create a custom security policy.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) > Security**
**Policies**.
4. On the **Security Policy** page, find the target security policy and click **Delete** in the
**Actions** column.
5. In the **Delete Security Policy** message, click **OK**.

### Operation logs

Application Load Balancer (ALB) allows you to view the operation logs of an ALB instance, which record the instance status, operation sources, operation time, and API call details. You can analyze and trace historical operations based on the operation logs.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. Use one of the following methods to view the operation logs of an ALB instance:

| Filter condition | Description |
|---|---|
| Resource Type | The resource type. Valid values: ALB Security Policy, ALB CA Certificates, Application Load Balancer, ALB Server Certificate, ALB health check, ALB Server Group, and ALB access control. |
| Event Type | The event type. You can select an event type based on the setting of Resource Type. Valid values: Delete Events, Create Events, Query Events, and Modify Events. |
| Time Range | The time range that you want to query. By default, the current month is selected. |
| Resource ID | The ID of the resource instance. |
| IP Address | The IP address of the operation. |
| Read/Wri te Type | The type of the operation. Valid values: Read Operation and Write Operation. |
| Operatio n Result | The result of the operation. Valid values: Successful and Failed. |
| Keyword | The keyword. You can enter an event ID, resource ID, source IP address, or operation name. |

Application Load Balancer User G View operation logs through the navigation pane. a. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Operation Logs**.
b. On the **Operation Log** page, view the operation event list, including **Operation Time**,
**Operator**, **Resource Type**, **IP Address**, **Operation Name**, **Read/Write Type**,
**Operation Result**, **Call Source**, **Organization**, and **Resource Set**.
Click **Advanced Filter** to filter operation logs by specifying filter conditions. The following table describes the filter conditions. Find the operation that you want to manage and click **View** in the **Details** column. In the **View Operation Details** panel, view information in the **Basic Information** and
**Instance Details** sections.
View operation logs on the Details page. a. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
b. On the **Instance Management** page, find the target instance and click its ID in the
**Instance ID/Name** column.

| Filter condition | Description |
|---|---|
| Operator | The operator that performed the operation. |
| Operation Name | The name of the operation, which is the API operation name. |
| Execution Status | The state of the operation. Valid values: Success and Failed. |
| Operation Source IP Address | The source IP address of the operation. |
| Operation Time | The time range that you want to query. |

Application Load Balancer User G c. On the **Details** page, click the **Operation Logs** tab to view the operation logs of the ALB instance. The operation event list includes the following information: **Operation Name**,
**Operator**, **Execution Status**, **Operation Source**, **Operation Type**, **Operation**
**Source IP Address**, and **Operation Time**.

**Note**

Operation logs are retained for seven days. To adjust the retention period, modify the logging configurations in Configurations > Log Storage Settings as an administrator. If you extend the retention period by modifying the logging configurations, the log data before the modification is not backfilled. Up to 100 pages of records can be displayed in the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records. Click **Advanced Filter** to filter operation logs that you want by specifying filter conditions such as **Operation Name** and **Operator**. Find the operation event that you want to view and click **Operation Details** in the
**Operation** column to view the operation details.

| Parame ter | Description |
|---|---|

Application Load Balancer User G

## Tag management

### Tag overview

Application Load Balancer (ALB) provides the tag management feature. You can use tags to mark and classify ALB resources. This way, you can search for and manage the resources by tag. As the number of instances increases, it becomes more difficult to manage instances. You can use tags to group instances to help you search for and filter instances. Tags are used to mark instances. Each tag consists of a key and a value. Tags have the following limits: ALB instances, certificate management, server groups, health checks, access control, and security policies support tag management. You can modify the key and value of a tag or remove a tag from a resource. If you delete an instance, all tags added to the instance are deleted. This operation does not affect the tags added to other instances. The key of each tag added to the same instance must be unique. If you add a tag that uses the same key as an existing tag, the new tag overwrites the existing tag. You can modify the key and value of a tag or remove a tag from a resource. If you delete an instance, all tags added to the instance are deleted. This operation does not affect the tags added to other instances. You can add up to 20 tags to an instance. This quota cannot be increased. Tags cannot exist as an independent resource. If you create a tag, it must be added to an instance.

### Edit tags

Application Load Balancer (ALB) allows you to edit tags. You can add, modify, and delete tags for an instance. This topic describes how to edit tags for an ALB instance. The operation methods for other ALB-related resource instances are similar to those for ALB instances.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, find the ALB instance that you want to manage,
move the pointer over the icon in the **Tag** column, and then click the icon in the popup box.
5. In the **Edit Tags** dialog box, configure the following parameters and then click **OK**.

| Tag Key | The key of the tag. You can select an existing key or enter a new keyS.elect an existing tag key or enter a new tag key A tag key can be up to 64 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
|---|---|
| Tag Value | The value of the tag. You can select an existing value or enter a new valueS.elect an existing value or enter a new value It can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |

Application Load Balancer User G

**Note**

You can click **Add** to add multiple tags. You must specify the Tag Key and Tag Value parameters.Specify the tag key and the tag value. You can add up to 20 tags. System tags do not count toward the tag quantity limit. You can click the icon next to a tag to delete the tag.
6. In the **Edited** message, confirm the tag information and click **Close**.

### Add tags to multiple ALB

**instances at a time**

Application Load Balancer (ALB) allows you to add tags at a time. This topic describes how to add tags to multiple ALB instances at a time. The operation methods for other ALB-related resource instances are similar to those for ALB instances.

**Procedure**

**Note**

Select at least two items. This configuration applies to all the selected resources. For specific resources, tags may be added or replaced.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, select all instances to which you want to add tags
and click **Batch Add Tags** in the lower-left corner.
5. In the **Batch Add Tags** dialog box, configure the following parameters and click **OK**.

| Parame ter | Description |
|---|---|
| Tag Key | The key of the tag. You can select an existing key or enter a new keyS.elect an existing tag key or enter a new tag key A tag key can be up to 64 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
| Tag Value | The value of the tag. You can select an existing value or enter a new valueS.elect an existing value or enter a new value It can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |

Application Load Balancer User G

**Note**

You can click **Add** to add multiple tags. You must specify the Tag Key and Tag Value parameters.Specify the tag key and the tag value. You can add up to 20 tags. System tags do not count toward the tag quantity limit. You can click the icon next to a tag to delete the tag.
6. In the **Edited** message, confirm the tag information and click **Close**.

### Remove tags from multiple

**ALB instances at a time**

Application Load Balancer (ALB) allows you to remove tags from multiple ALB instances at a time. This topic describes how to remove tags from multiple ALB instances at a time. The operation methods for other ALB-related resource instances are similar to those for ALB instances.

**Procedure**

**Note**

Select at least two items. This configuration applies to all the selected resources. For specific resources, tags may be added or replaced.
1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
Application Load Balancer User G
4. On the **Instance Management** page, select the ALB instances that you want to manage
and click **Batch Remove Tags** below the instance list.
5. In the **Batch Remove Tags** dialog box, select **All** or the tags that you want to remove in
the **Tags to Remove** section and click **OK**.

**Note**

Batch removal is performed based on tag keys. When you select a tag, all tags that have the same tag key are selected.
6. In the **Edited** message, check the tag removal information and click **Close**.

### Search for instances by tag

After you add tags to Application Load Balancer (ALB) resources, you can quickly search for the resources by tag. This topic describes how to search for ALB instances by tag. The operation methods for other ALB-related resource instances are similar to those for ALB instances.

**Procedure**

1. Log on to the Application Load Balancer (ALB) console.
2. In the top menu bar, select the region of the ALB instance.
3. In the navigation pane on the left, choose **Application Load Balancer (ALB) >**
**Instances**.
4. On the **Instance Management** page, select **Tag** from the drop-down list in the upper-left
corner.
5. In the dialog box that appears, select **Tag Key** and **Tag Value**. The system filters the
instances that meet the specified conditions. You can enter a tag key or tag value to search for tags.
**Tag Key**: The AND operation is performed on the keys to obtain the intersection of the
selected keys.
**Tag Value**: The OR operation is performed on the values to obtain the union of the
selected values.
