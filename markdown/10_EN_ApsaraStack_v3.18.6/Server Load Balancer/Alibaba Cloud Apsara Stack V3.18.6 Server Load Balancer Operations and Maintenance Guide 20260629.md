---
title: "Server Load Balancer Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 41
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Server Load Balancer Operations and Maintenance Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Server%20Load%20Balancer%20Operations%20and%20Maintenance%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Server Load Balancer Operations and Maintenance Guide

ager Operations Console

## Log on to the Apsara Uni-

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the username and password.
ager Operations Console Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

## Network services

### SLB O&M

#### SLB cluster management

After you add tags to Server Load Balancer (SLB) clusters, you can easily find the desired clusters in the tenant console.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **SLB O&M** > **SLB Cluster**
**Management**.
4. On the **SLB Cluster Management** page, select a zone and click **Search** to view
information about the desired cluster.
5. Click **Edit Tag** in the **Actions** column of the desired cluster. In the dialog box that appears,
modify the tag keys and click **OK**. You cannot modify the tags of the default cluster.

#### SLB management

The SLB Management page displays Layer 4 service resources and monitoring and O&M information of Server Load Balancer (SLB) clusters and SLB instances.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**SLB clusters**

The SLB Cluster tab displays the basic information, maximum inbound bits per second (BPS), maximum outbound BPS, maximum inbound packets per second (PPS), maximum outbound PPS, maximum number of active connections, maximum number of inactive connections, and usage data of a single node in an SLB cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **SLB O&M** > **SLB**
**Management**.
4. On the **SLB Management** tab, click the **SLB Cluster** tab, and select the cluster that you
want to view from the **Cluster** drop-down list. You can then view information displayed in the **Node Information** and **Cluster Resource Usage** sections. In the **Node Information** section, you can view node information in the columns, including **Node IP Address**, **Working Status**, **Local IP Address**, **Service Unit**, **Site**
**ID**, and **LVS Group ID**.
**View node details**: Click **Details** in the **Actions** column of the node that you want to
view to go to the **SLB Node Details** page. Then, you can view **Node Information** and
**Usage Data**.
The **Node Information** section displays the following information: **IP**, **Working**
**Status**, **Local CIDR Block**, **ENIs**, **LVS Group ID**, **Proxy Check Type**, **Site ID**,
**Maximum Active Connections**, **Maximum Inactive Connections**, **Inbound BPS**
**Limit**, **Outbound BPS Limit**, **Inbound PPS Limit**, and **Outbound PPS Limit**.
In the **Usage Data** section, specify **Start and End Time** to view the usage data of the node within the specified time range. For more information about the definitions of the metrics, see the Node and instance usage metrics section of this topic. The interval between the start time and end time must not exceed 12 hours. You can click **Last5Minutes**, **Last30Minutes**, **Last1Hour**, or **Last6Hours** to query the usage data within the selected time range. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. In the **Cluster Resource Usage** section, specify a time range to view the usage data of the cluster within the specified time range. You can click the **Core Metrics** or **All**
**indicators** tab to view the corresponding information. For more information about the
definitions of the metrics, see Cluster usage metrics. The interval between the start time and end time must not exceed 12 hours. You can click **Last 1 Hour**, **Last 3 Hours**, **Last 6 Hours**, or **Last 12 Hours** to query the usage data within the specified time range. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time.

**SLB instances**

The SLB Instances tab displays the basic information and usage data of SLB instances, including the inbound and outbound BPS and PPS.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **SLB O&M** > **SLB**
**Management**.
4. On the **SLB Management** page, click the **SLB Instances** tab to view the information
about the SLB instances in the columns, including **IP Address**, **Instance ID**, **Network**
**Type**, **Product**, **Zone**, and **Updated At**.
Click **Advanced Filter** and filter SLB instances by **IP Address Version**, **IP Address**,
**Instance ID**, **Product Name**, **Network Type**, or any combination of them.
5. Click **Details** in the **Actions** column of an SLB instance to go to the **SLB Instance Details**
page. On this page, you can view **Instance Information**, **Server Group Information**, and **Usage Data**. In the **Instance Information** section, view the basic information about the SLB instance, which can be used by O&M engineers to troubleshoot faults and confirm the ownership of the device. You can click **Modify** next to the **Throttling Rule** parameter to modify the throttling rule of the SLB instance. The throttling parameters vary depending on the status of the **SLB**
**instance switch**. For more information, see the **Switch list (switch management)**
section of the **Product console configuration management** topic below **UniConsole** in **Apsara Uni-manager Operations Console User Guide** and view the switch list in the **networkops** console. When the SLB instance switch is **turned on**, you can modify the following throttling parameters. When the SLB instance switch is **turned off**, you can modify only the bandwidth parameter. The maximum values of the throttling parameters are as follows: vip_qps: 50000 QPS. Bandwidth: 15 Gbit/s. The actual value is in bytes and rounded up. vip_cps: 100000 CPS. vip_max_conn_limit: 1000000 CPS. In the **Server Group Information** section, view the server group information of the SLB instance, including **Server Group** and **Listener Name**. To view the weight modification details, click **View Details** in the **Actions** column of the desired server group. Modify weights a. Click **Modify Weight** in the **Actions** column of a server group. In the panel that appears, change the values in the **Weight** column and click **OK**. b. In the message that appears, confirm the information and click **OK**. After maintenance or emergency repair is performed, we recommend that you restore the weight settings. When you perform zone-disaster recovery across two data centers, the system restores the default weight settings. The restored weight settings take effect after your confirmation. If an SLB instance is enabled by a tenant, you can go to the Apsara Unimanager Management Console to modify the weight settings of the SLB instance. In the **Usage Data** section, specify **Start/End Time** and **Node** to view the usage data of the SLB instance within the specified time range. For more information about the definitions of the metrics, see the Node and instance usage metrics section of this topic. The interval between the start time and end time must not exceed 12 hours. You can click **Last5Minutes**, **Last30Minutes**, **Last1Hour**, or **Last6Hours** to query the usage data within the selected time range. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. Click **Details** in the upper-right corner of the resource usage chart to view the details of the resource usage of backend servers.

**Cluster usage metrics**

| Category | Metric | Description | Example |
|---|---|---|---|

| Core Metrics | inBitsPS | The number of inbound bits per second. | 248 |
|---|---|---|---|
|   | outBitsPS | The number of outbound bits per second. | 208 |
|   | connsPS | The number of connections created per second. | 1 |
| All Metrics | sumInBytes | The number of inbound bytes. | 248 |
|   | inPktsPS | The number of inbound packets per second. | 1 |
|   | inDropPktsPS | The number of inbound packets dropped per second. | 0 |
|   | inBitsPS | The number of inbound bits per second. | 248 |
|   | inDropBitsPS | The number of inbound bits dropped per second. | 0 |
|   | aclDropBitsPS | The number of bits dropped by the access control list (ACL) per second. | 0 |
|   | maxConnsPs | The number of concurrent connections per second. | 1 |
|   | outDropPktsPS | The number of outbound packets dropped per second. | 0 |
|   | outPktsPS | The number of outbound packets per second. | 1 |

|   | outBitsPS | The number of outbound bits per second. | 208 |
|---|---|---|---|
|   | outDropBitsPS | The number of outbound bits dropped per second. | 0 |
|   | dropConnsPS | The number of connections dropped per second. | 0 |
|   | actConnsPS | The number of active connections. | 0 |
|   | inActConnPS | The number of inactive connections. | 1 |
|   | sumOutBytes | The number of outbound bytes. | 248 |
|   | connsPS | The number of connections created per second. | 1 |
|   | aclDropPktsPS | The number of packets dropped by access control list (ACL) rules per second. | 0 |
|   | failConnPS | The number of failed connections per second. | 0 |

**Node and instance usage metrics**

| Metric | Description | Example |
|---|---|---|
| sumInBytes | The number of inbound bytes. | 248 |
| inPktsPS | The number of inbound packets per second. | 1 |
| inDropPktsPS | The number of inbound packets dropped per second. | 0 |

| inBitsPS | The number of inbound bits per second. | 248 |
|---|---|---|
| inDropBitsPS | The number of inbound bits dropped per second. | 0 |
| aclDropBitsPS | The number of bits dropped by ACL rules per second. | 0 |
| maxConnsPs | The number of concurrent connections per second. | 1 |
| outDropPktsPS | The number of outbound packets dropped per second. | 0 |
| outPktsPS | The number of outbound packets per second. | 1 |
| outBitsPS | The number of outbound bits per second. | 208 |
| outDropBitsPS | The number of outbound bits dropped per second. | 0 |
| dropConnPS | The number of connections dropped per second. | 0 |
| actConnsPS | The number of active connections. | 0 |
| inActConnPS | The number of inactive connections. | 1 |
| sumOutBytes | The number of outbound bytes. | 248 |
| connsPS | The number of connections created per second. | 1 |
| aclDropPktsPS | The number of packets dropped by ACL rules per second. | 0 |
| failConnPS | The number of failed connections per second. | 0 |

### Proxy O&M

#### Proxy management

The proxy management module displays Layer 7 service resources and monitoring and maintenance information of Server Load Balancer (SLB).

**View information about proxy clusters**

On the Proxy Cluster tab, you can view the node status, usage data, and cluster aggregation metrics of an SLB proxy cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **Proxy O&M** > **SLB Proxy**
**Management**.
4. On the **Proxy Cluster** tab of the **SLB Proxy Management** page, select the cluster that
you want to view from the **Cluster** drop-down list. Then, view the cluster information in the
**Node Information** and **Cluster Aggregation Monitoring** sections.
5. View information in the **Node Information** section.
View node information in the node list, including **Node**, **Cluster**, and **Item**. Find the node whose details you want to view and click **Details** in the **Operation** column. On the **SLB Proxy Node Details** page, specify **Start and End Time** and view the metrics of the node in the **Usage Data** section. The interval between the start time and end time must not exceed 12 hours. You can click **Last5Minutes**, **Last30Minutes**, **Last1Hour**, or **Last6Hours** to query the usage data within the selected time range. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. The following table describes the metrics.

| Category | Metric | Description |
|---|---|---|
| slb proxy cpu _ _ | hirq | The ratio of the time that the system takes to handle hardware interrupts to the total time. |
|   | sirq | The ratio of the time that the system takes to handle software interrupts to the total time. |
|   | sys | The system CPU utilization. |
|   | user | The ratio of the time that the CPU takes to execute user processes to the total time. |
|   | util | The ratio of the CPU usage time to the total time. |
| cument Version: 20260 | 629 1 |   |

|   | wait | The ratio of the time that the CPU waits for I/O operations to the total time. |
|---|---|---|
|   | await | The average amount of time required to send I/O requests to the device that requests the service. Unit: milliseconds. |
| slb proxy diskio _ _ |   |   |
|   | qusize | The average queue length of requests sent to the device. |
|   | rqsize | The average size of requests sent to the device by sector. |
|   | rrqms | The number of sectors read from the device per second. |
|   | rs | The number of read requests sent to the device per second. |
|   | rsecs | The number of sectors read from the device per second. |
|   | svctm | The average amount of time required to serve the device to which I/O requests are sent. Unit: milliseconds. |
|   | util | The ratio of the time that CPU takes to send I/O requests to the device to the total CPU time, which indicates the bandwidth utilization of the device. |
|   | wrqms | The number of merged write requests sent to the device per second. |
|   | ws | The number of write requests sent to the device per second. |
|   | wsecs | The number of sectors written to the device per second. |
|   | load1 | The average system load within 1 minute. Unit: %. |
|   | load5 | The average system load within 5 minutes. Unit: %. |

| r Load Balancer |   |   |
|---|---|---|
| slb proxy load _ _ |   |   |
|   | load15 | The average system load within 15 minutes. Unit: %. |
|   | plit | The number of active tasks in the system during the sampling time, excluding completed tasks. |
|   | runq | The number of tasks in the queue during the sampling time. |
| slb proxy mem _ _ | Dirty | The volume of data pending to be written back to the disk. Unit: KB. |
|   | SReclaimable | The amount of reclaimable slab memory. Unit: KB. |
|   | Shmem | The amount of shared memory that has been allocated. Unit: KB. |
|   | Slab | The cache size of kernel data structure. Unit: KB. |
|   | Writeback | The volume of data being written back. Unit: KB. |
|   | buff | The amount of memory used as a buffer. Unit: KB. |
|   | cach | The amount of memory allocated by the operating system to the file buffer. Unit: KB. |
|   | free | The amount of idle physical memory. Unit: KB. |
|   | total | The total amount of system memory. Unit: KB. |
|   | used | The amount of used memory. Unit: KB. |
|   | util | The memory usage. |
|   | accept | The total number of received TCP connections. |
|   | active | The number of active TCP connections, including connections that are receiving data, sending data, and waiting. |
|   | cps | The average number of TCP connections received per second. |

| slb proxy qps _ _ |   |   |
|---|---|---|
|   | h2qps | The number of HTTP/2 requests processed per second. |
|   | handle | The total number of processed TCP connections. |
|   | handleps | The average number of connections processed per second. |
|   | httpqps | The number of HTTP requests processed per second. |
|   | qps | The number of requests processed per second. |
|   | read | The number of TCP connections that receive request data. |
|   | reqs | The total number of generated requests. |
|   | rt | The average response time. Unit: milliseconds. |
|   | spdyps | The number of SPDY requests processed per second. |
|   | sslf | The number of failed SSL connections. |
|   | sslhst | The average amount of time for an SSL handshake. Unit: milliseconds. |
|   | sslqps | The number of SSL requests processed per second. |
|   | sslv3f | The number of failed SSLv3 connections. |
|   | wait | The number of persistent TCP connections that are waiting. |
|   | write | The number of TCP connections that send response data to users. |
|   | AtmpFa | The number of failed TCP connections per second. |
|   | CurrEs | The current number of TCP connections. |

| r Load Balancer |   |   |
|---|---|---|
| slb proxy tcp _ _ |   |   |
|   | EstRes | The number of times that TCP connections are reset per second. |
|   | active | The number of TCP connections that are proactively initiated per second. |
|   | iseg | The number of inbound TCP segments per second. |
|   | lisove | The number of TCP requests dropped because the listenaccept queue is full. |
|   | outseg | The number of outbound TCP segments per second. |
|   | pasive | The number of passively established TCP connections per second. |
|   | retran | The retransmission rate of segments. The value is calculated based on the re-transmitted segments and the total segments. |

6. In the **Cluster Aggregation Monitoring** section, specify **Start and End Time** and view
the cluster aggregation metrics on the **Core Metrics** and **All Metrics** tabs. The interval between the start time and end time must not exceed 12 hours. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. The following table describes the metrics.

| Tab | Metric | Description |
|---|---|---|
| Core Metrics | qps | The number of requests processed per second. |
|   | accept | The total number of received TCP connections. |
|   | active | The number of active TCP connections, including connections that are receiving data, sending data, and waiting. |
|   | cps | The average number of TCP connections received per second. |

|   | h2qps | The number of HTTP/2 requests processed per second. |
|---|---|---|
| 全部指标 |   |   |
|   | handle | The total number of processed TCP connections. |
|   | handleps | The average number of connections processed per second. |
|   | httpqps | The number of HTTP requests processed per second. |
|   | qps | The number of requests processed per second. |
|   | read | The number of TCP connections that receive request data. |
|   | reqs | The total number of generated requests. |
|   | rt | The average response time. Unit: milliseconds. |
|   | spdyps | The number of SPDY requests processed per second. |
|   | sslf | The number of failed SSL connections. |
|   | sslhst | The average amount of time for an SSL handshake. Unit: milliseconds. |
|   | sslqps | The number of SSL requests processed per second. |
|   | sslv3f | The number of failed SSLv3 connections. |
|   | wait | The number of persistent TCP connections that are waiting. |
|   | write | The number of TCP connections that send response data to users. |

**View information about proxy instances**

You can view the metrics and usage data of SLB proxy instances.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **Proxy O&M** > **SLB Proxy**
**Management**.
4. On the **SLB Proxy Management** page, click the **Proxy Instance** tab.
5. Select a cluster from the **Cluster** drop-down list, enter an instance ID or virtual IP address
(VIP), specify **Listener** and **Start and End Time**, and click **Search**.
6. Click the **Request**, **Connection**, **Traffic**, **Latency**, and **Status Code** tabs to view the
corresponding metrics and usage data. The following table describes the metrics.

|   | Metric | Description |
|---|---|---|
| Request | qps | The average number of requests received per second. |
|   | req concurrent _ | The number of concurrent requests. |
|   | REQ DROP _ | The number of requests that are not forwarded due to rate limiting. |
| Connection | conn concurrent _ | The number of concurrent connections. |
|   | cps | The average number of connections received per second. |
| Traffic | inBitsPS | The inbound traffic rate. Unit: bits/s. |
|   | outBitsPS | The outbound traffic rate. Unit: bits/s. |
| Latency | rt | The average request processing latency. Unit: milliseconds. |
|   | upstream rt _ | The average request processing latency of backend Elastic Compute Service (ECS) instances. Unit: milliseconds. |
|   | status code 2xx _ _ | The number of requests for which a 2xx status code is returned. |

| erations and Mai Network service |   |   |
|---|---|---|
| Status Code |   |   |
|   | status code 3xx _ _ | The number of requests for which a 3xx status code is returned. |
|   | status code 4xx _ _ | The number of requests for which a 4xx status code is returned. |
|   | status code 5xx _ _ | The number of requests for which a 5xx status code is returned. |
|   | status code other _ _ | The number of requests for which a status code other than 2xx, 3xx, 4xx, and 5xx is returned. |
|   | upstream code 4xx _ _ | The number of requests for which a 4xx status code is returned by backend ECS instances. |
|   | upstream code 5xx _ _ | The number of requests for which a 5xx status code is returned by backend ECS instances. |

#### ALB proxy management

The ALB Proxy Management page displays information about Application Load Balancer (ALB) resources and monitoring O&M.

**View information about ALB proxy clusters**

On the ALB Proxy Cluster tab, you can view the node status, usage data, and aggregate metrics of an ALB proxy cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **Proxy O&M** > **ALB Proxy**
**Management**.
4. On the **ALB Proxy Cluster** tab, select the cluster that you want to view from the **Cluster**
drop-down list. Then, view the cluster information in the **Node Information** and **Cluster**
**Aggregation Monitoring** sections.
5. View the cluster information in the **Node Information** section.
View node information in the node list, including the **Node**, **Cluster**, and **Item** columns. Find the node whose details you want to view and click **Details** in the **Actions** column. On the ALB Proxy Node Details page, specify the start time and end time, and view the metrics of the node in the Usage Data section. By default, the data within the last hour is displayed. The interval between the start time and end time cannot exceed 12 hours. After you click the Start and End Time field, you can click **Last5Minutes**,
**Last30Minutes**, **Last1Hour**, or **Last6Hours** to view the usage data within
the selected time range. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. The following table describes the metrics.

| Category | Metric | Description |
|---|---|---|
| alb cpu _ | cpu hirq util _ _ | The percentage of the amount of time that the system takes to handle hardware interrupts to the total amount of time. |
|   | cpu sirq util _ _ | The percentage of the amount of time that the system takes to handle software interrupts to the total amount of time. |
|   | cpu sys util _ _ | The percentage of the amount of time that the system takes to run content to the total amount of time. |
|   | cpu user util _ _ | The percentage of the amount of time that the CPU takes to run user processes to the total amount of time. |
|   | cpu util _ | The percentage of the amount of CPU usage time to the total amount of time. |
|   | cpu wait util _ _ | The percentage of the amount of time that the CPU waits for I/O operations to the total amount of time. |
| alb diskio _ | diskio read req _ _ | The number of read requests sent to the device per second. |
|   | diskio await time _ _ | The average amount of time required to send I/O requests to the device. Unit: milliseconds. |
|   | diskio quese size _ _ | The average queue length of requests sent to the device. |
|   | diskio read req merge _ _ _ d | The number of merged read requests sent to the device per second. |
|   | diskio request size _ _ | The average size of requests sent to the device by sector. |
|   | diskio sector read req _ _ _ | The number of sectors read from the device per second. |

|   | diskio sector write re _ _ _ q | The number of sectors written to the device per second. |
|---|---|---|
|   | diskio service time _ _ | The average amount of time required to serve the device to which I/O requests are sent. Unit: milliseconds. |
|   | diskio util _ | The percentage of the amount of time that the CPU takes to send I/O requests to the device to the total amount of CPU time, which indicates the bandwidth utilization of the device. |
|   | diskio write req _ _ | The number of write requests sent to the device per second. |
|   | diskio write req merg _ _ _ ed | The number of merged write requests sent to the device per second. |
| alb load _ | load1 | The average system load within 1 minute. Unit: %. |
|   | load5 | The average system load within 5 minutes. Unit: %. |
|   | load15 | The average system load within 15 minutes. Unit: %. |
|   | load plist _ | The number of active tasks in the system during the sampling time, excluding tasks that are complete. |
|   | load runq _ | The number of tasks in the queue during the sampling time. |
| alb mem _ | mem buff _ | The amount of memory used as a buffer. Unit: KB. |
|   | mem cach _ | The amount of memory used as a cache. Unit: KB. |
|   | mem dirty _ | The volume of data waiting to be written back to the disk. Unit: KB. |
|   | mem shmem _ | The amount of shared memory that has been allocated. Unit: KB. |

|   | mem slab _ | The cache size of kernel data structure. Unit: KB. |
|---|---|---|
|   | mem sreclaimable _ | The amount of reclaimable slab memory. Unit: KB. |
|   | mem used _ | The amount of used memory. Unit: KB. |
|   | mem util _ | The memory usage. |
|   | mem writeback _ | The volume of data being written back. Unit: KB. |
| alb tcp _ | tcp active conn _ _ | The number of TCP connections that are proactively initiated per second. |
|   | tcp established conn _ _ | The current number of TCP connections. |
|   | tcp fail conn _ _ | The number of failed TCP connections per second. |
|   | tcp pasive conn _ _ | The number of passively established TCP connections per second. |
|   | tcp reset conn _ _ | The number of times that TCP connections are reset per second. |
|   | tcp retransmission _ | The retransmission rate of segments. The value is calculated based on the re-transmitted segments and the total segments. |
|   | tcp stats close wait _ _ _ | The number of TCP connections in the CLOSE WAIT state. _ |
|   | tcp stats closed _ _ | The number of TCP connections in the CLOSED state. |
|   | tcp stats closing _ _ | The number of TCP connections in the CLOSING state. |
|   | tcp stats estab _ _ | The number of TCP connections in the ESTABLISH state. |
|   | tcp stats fin wait 1 _ _ _ _ | The number of TCP connections in the FIN WAIT 1 state. _ _ |

|   | tcp stats fin wait 2 _ _ _ _ | The number of TCP connections in the FIN WAIT 2 state. _ _ |
|---|---|---|
|   | tcp stats last ack _ _ _ | The number of TCP connections in the LAST ACK _ state. |
|   | tcp stats syn recv _ _ _ | The number of TCP connections in the SYN RECV _ state. |
|   | tcp stats syn sent _ _ _ | The number of TCP connections in the SYN SENT _ state. |
|   | tcp stats time wait _ _ _ | The number of TCP connections in the TIME WAIT state. _ |

6. In the **Cluster Aggregation Monitoring** section, specify the start time and end time, and
view the aggregate metrics of the cluster on the **Core Metrics** and **All Metrics** tabs. By default, the data within the last hour is displayed. The interval between the start time and end time cannot exceed 12 hours. You can move the pointer over a point in time in a chart to view the values of all metrics at the point in time. The following table describes the metrics.

| Tab | Metric | Description |
|---|---|---|
| Core Metrics | http qps _ | The number of HTTP requests processed per second. The value equals the result of the average number of requests received per second minus the number of SSL requests processed per second. |
|   | conn accept 1m _ _ | The total number of received TCP connections. |
|   | conn active 1m _ _ | The number of active TCP connections, including connections that are receiving data, sending data, and waiting. |
|   | conn handle 1m _ _ | The total number of processed TCP connections. |
|   | conn read 1m _ _ | The number of TCP connections that receive request data. |

|   | conn wait 1m _ _ | The number of persistent TCP connections that are waiting. |
|---|---|---|
| All Metrics | conn write 1m _ _ | The number of TCP connections that send response data to users. |
|   | http2 qps _ | The number of HTTP/2 requests processed per second. |
|   | http qps _ | The number of HTTP requests processed per second. The value equals the result of the average number of requests received per second minus the number of SSL requests processed per second. |
|   | requests 1m _ | The total number of requests processed. |
|   | rt | The average response time. Unit: milliseconds. |
|   | spdy ps _ | The number of SPDY requests processed per second. |
|   | ssl failed 1m _ _ | The number of failed SSL connections. |
|   | ssl handshake ti _ _ me | The average amount of time required for an SSL handshake. Unit: milliseconds. |
|   | ssl qps _ | The number of SSL requests processed per second. |
|   | sslv3 failed 1m _ _ | The number of failed SSLv3 connections. |
|   | tls failed 1m _ _ | The number of failed TLS connections. |

**View information about ALB proxy instances**

On the ALB Proxy Instance tab, you can view the metrics and usage data of an ALB proxy instance.

**Prerequisites**

The master branch for BaseServiceAll is deployed and at desired state.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **Proxy O&M** > **ALB Proxy**
**Management**.
4. On the **ALB Proxy Instance** tab, select a cluster from the **Cluster** drop-down list, enter an
instance ID or a virtual IP address in the **Instance ID or VIP** field, select a listener from the
**Listener** drop-down list, and then click **Search**.
5. Click the **Request**, **Connection**, **Traffic**, **Latency**, and **Status Code** tabs to view the
usage data charts of the corresponding metrics. The following table describes the metrics.

|   | Metric | Description |
|---|---|---|
| Request | qps | The average number of requests received per second. |
|   | req concurrent _ | The number of concurrent requests. |
| Connection | conn concurrent _ | The number of concurrent connections. |
|   | cps | The average number of connections received per second. |
| Traffic | in bytes 1m _ _ | The inbound traffic rate. Unit: bits/s. |
|   | out bytes 1m _ _ | The outbound traffic rate. Unit: bits/s. |
| Latency | rt | The average request processing latency. Unit: milliseconds. |
|   | upstream rt _ | The average request processing latency of backend Elastic Compute Service (ECS) instances. Unit: milliseconds. |
|   | 100 | The number of requests for which the 100 status code is returned per second. |
|   | 101 | The number of requests for which the 101 status code is returned per second. |
|   | 200 | The number of requests for which the 200 status code is returned per second. |
|   | 206 | The number of requests for which the 206 status code is returned per second. |
|   | 301 | The number of requests for which the 301 status code is returned per second. |

|   | 302 | The number of requests for which the 302 status code is returned per second. |
|---|---|---|
|   | 304 | The number of requests for which the 304 status code is returned per second. |
|   | 400 | The number of requests for which the 400 status code is returned per second. |
|   | 403 | The number of requests for which the 403 status code is returned per second. |
|   | 404 | The number of requests for which the 404 status code is returned per second. |
|   | 416 | The number of requests for which the 416 status code is returned per second. |
|   | 499 | The number of requests for which the 499 status code is returned per second. |
|   | 500 | The number of requests for which the 500 status code is returned per second. |
|   | 502 | The number of requests for which the 502 status code is returned per second. |
|   | 503 | The number of requests for which the 503 status code is returned per second. |
|   | 504 | The number of requests for which the 504 status code is returned per second. |
|   | 508 | The number of requests for which the 508 status code is returned per second. |
|   | status code 2xx _ _ | The number of requests for which a 2xx status code is returned per second. |
|   | status code 3xx _ _ | The number of requests for which a 3xx status code is returned per second. |

| Status Code |   |   |
|---|---|---|
|   | status code 4xx _ _ | The number of requests for which a 4xx status code is returned per second. |
|   | status code 5xx _ _ | The number of requests for which a 5xx status code is returned per second. |
|   | status code other _ _ | The number of requests for which a status code other than 2xx, 3xx, 4xx, and 5xx is returned per second. |
|   | upstream code 4xx _ _ | The number of requests for which a 4xx status code is returned by backend ECS instances per second. |
|   | upstream code 5xx _ _ | The number of requests for which a 5xx status code is returned by backend ECS instances per second. |
|   | upstream 100 _ | The number of requests for which the 100 status code is returned by the upstream per second. |
|   | upstream 101 _ | The number of requests for which the 101 status code is returned by the upstream per second. |
|   | upstream 200 _ | The number of requests for which the 200 status code is returned by the upstream per second. |
|   | upstream 206 _ | The number of requests for which the 206 status code is returned by the upstream per second. |
|   | upstream 301 _ | The number of requests for which the 301 status code is returned by the upstream per second. |
|   | upstream 302 _ | The number of requests for which the 302 status code is returned by the upstream per second. |
|   | upstream 304 _ | The number of requests for which the 304 status code is returned by the upstream per second. |
|   | upstream 400 _ | The number of requests for which the 400 status code is returned by the upstream per second. |
|   | upstream 403 _ | The number of requests for which the 403 status code is returned by the upstream per second. |
| Document Versio |   |   |

|   | upstream 404 _ | The number of requests for which the 404 status code is returned by the upstream per second. |
|---|---|---|
|   | upstream 416 _ | The number of requests for which the 416 status code is returned by the upstream per second. |
|   | upstream 499 _ | The number of requests for which the 499 status code is returned by the upstream per second. |
|   | upstream 500 _ | The number of requests for which the 500 status code is returned by the upstream per second. |
|   | upstream 502 _ | The number of requests for which the 502 status code is returned by the upstream per second. |
|   | upstream 503 _ | The number of requests for which the 503 status code is returned by the upstream per second. |
|   | upstream 504 _ | The number of requests for which the 504 status code is returned by the upstream per second. |
|   | upstream 508 _ | The number of requests for which the 508 status code is returned by the upstream per second. |
|   | upstream other code _ _ | The number of requests for which other status codes are returned by the upstream per second. |

## Network resources

### Cloud instance management

This topic describes how to manage the lifecycle of cloud service instances, including creating, deleting, and querying instance status.

**Create an instance**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Resources** > **Cloud Instance**
**Management**.
4. On the Cloud Instance Management page, choose Create Instance > **Create Instance**.
5. In the **Create VPC** step of the Create Instance wizard, configure the parameters described
in the following table and click **Create**.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in which the instance resides. |
| Cloud Service Instance ID | The ID of the instance. |
| Tunnel Type | SingleTunnel: A virtual IP address (VIP) of the SingleTunnel type allows the Elastic Compute Service (ECS) instances in a single virtual private cloud (VPC) to access external cloud services. AnyTunnel: A VIP of the AnyTunnel type allows the ECS instances in all VPCs to access the specified cloud service. |
| CloudInstance IP | The VIP that you want to assign to the instance. If you do not specify a VIP, the system automatically assigns a VIP. |
| vSwitch ID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The ID of any vSwitch in the VPC to which the ECS instance that needs to access external cloud services belongs. |
| UID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The UID of the user that creates the vSwitch. This parameter is required if the user is not the API caller. |

| BID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The BID of the user that creates the vSwitch. This parameter is required if the user is not the API caller. |
|---|---|
| CIDR Type | This parameter is available only when the Tunnel Type parameter is set to AnyTunnel. Link local (Regular Cloud Services): The AnyTunnel VIP assigned to _ Application Load Balancer (ALB) is allocated from a subnet mask that does not belong to the 100.100.100.0/24 CIDR block. Special Inner (ECS META Server): The AnyTunnel VIP assigned to ALB is allocated from a subnet mask of the 100.100.100.0/24 CIDR block. |

6. In the **Add RS to SLB Instance** step, configure the parameters described in the following
table and click **Create**.

| Parameter | Description |
|---|---|
| VPC ID | The ID of the VPC to which the ECS instance belong. This parameter is required if the ECS instance is deployed in a VPC. |
| RS List | The backend servers that you want to add to the instance. Click Add RS and configure the IP and weight parameters. Valid value of the weight parameter: 0 to 1000. If you do not configure this parameter, the default value 100 is used. Note To delete a real server (RS), click Delete in the Actions column. |

7. In the **Create Listener** step, configure the parameters described in the following table and
click **Create**.

| Parameter | Description |
|---|---|
| Agreement | The listener protocol. Valid values: Tcp Udp |
| Front-end port | The frontend port of the VIP. |
| Backend Port | The service port of the RS. |
| Configuration | Click Configuration to specify configurations such as polling policy and health check. |
| Delete | Click Delete to delete the listener configurations. |

8. Return to the Cloud Instance Management page. If an instance whose tunnel type is
**AnyTunnel** or **SingleTunnel** is displayed, the cloud service instance is created.

**Apply for a Direct AnyTunnel VIP**

1. On the Cloud Instance Management page, choose **Create Instance** > **Create Direct Any**
**Tunnel**.
2. On the Create Direct Any Tunnel VIP page, configure the parameters described in the
following table and click **Create**.

| Parameter | Description |
|---|---|
| RegionID | The ID of the region in which the instance resides. |
| Cloud Service Instance ID | The ID of the instance. |
| Tunnel Type | Direct Any Tunnel: After a Direct Any Tunnel VIP is applied, all ECS instances in the VPC can use the VIP to access the specified cloud service. |
| CloudInstance IP | The VIP that you want to assign to the instance. If you do not specify a VIP, the system automatically assigns a VIP. |
| CIDR Type | Link local (Regular Cloud Services): The Direct Any Tunnel VIP is _ allocated from a subnet mask that does not belong to the 100.100.100.0/24 CIDR block. Special Inner (ECS META Server): The Direct Any Tunnel VIP is allocated from a subnet mask of the 100.100.100.0/24 CIDR block. |

3. Return to the Cloud Instance Management page. If an instance whose tunnel type is
**DirectAnyTunnel** is displayed, the Direct Any Tunnel VIP is applied.

**Import existing resources**

**Prerequisites**

Existing resources have not been imported.

**Procedure**

1. In the upper part of the Cloud Instance Management page, click **Existing Resource**
**Management**.
2. After the page is refreshed, if cloud service instances whose IDs do not start with noe
appear, the existing resources are imported as expected. After all resources are successfully processed, Existing Resource Management is dimmed and you cannot click it to import existing resources. If an instance whose tunnel type is **InvalidResource** appears, the instance is an abnormal resource on the original platform due to reasons such as interrupted creation or invalid resource. After the instance is imported, you can only view or delete the instance but cannot manage the instance. For example, you cannot modify the RS or listener configurations.

**What to do next**

| Operation | Procedure |
|---|---|
| Modify RS configurations | Note You cannot modify RS configurations for instances whose tunnel type is InvalidResource. 1. Find the cloud service instance that you want to manage and clickE dit RS in the Operation column. 2. In the dialog box that appears, modify the RS configurations and clickO K. For more information about the parameters, see Step 6 of this topic. |
| Modify listener configurations | Note You cannot modify listener configurations for instances whose tunnel type is InvalidResource. 1. Find the cloud service instance that you want to manage and clickM odify Listener in the Operation column. 2. In the dialog box that appears, modify the listener configurations and click OK. For more information about the parameters, see Step 7 of this topic. |
| Delete a cloud service instance | 1. Find the cloud service instance that you want to delete and clickD elete in the Operation column. 2. In the message that appears, click OK. |
