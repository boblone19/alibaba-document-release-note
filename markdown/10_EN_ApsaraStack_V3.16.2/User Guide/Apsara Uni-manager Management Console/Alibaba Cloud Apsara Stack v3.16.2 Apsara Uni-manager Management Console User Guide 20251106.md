---
title: "Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console User Guide"
product_version: "V3.16.2"
doc_version: "20251106"
pdf_pages: 167
source_pdf: "Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console User Guide 20251106.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E7%BB%9F%E4%B8%80%E4%BA%91%E7%AE%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.16.2%20Apsara%20Uni-manager%20Management%20Console%20User%20Guide%2020251106.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console User Guide

t Console?

## What is the Apsara Uni-

**manager Management**

**Console?**

The Apsara Uni-manager Management Console is a service capability platform of the cloud computing industry based on the Alibaba Cloud Apsara Stack platform. It is designed for public service customers and enterprise customers. The platform improves IT management and troubleshooting. The platform also provides large-scale and cost-efficient end-to-end cloud computing and big data services for customers in sectors such as public service, education, healthcare, finance, and enterprise.

**Overview**

The Apsara Uni-manager Management Console simplifies the management and deployment of physical and virtual resources by building an Apsara Stack platform that supports various business types of public service and enterprise customers. The console helps build your business systems in a simple and quick manner, fully improves resource utilization, and reduces O&M costs. This allows you to shift your focus from O&M to business. The console brings the Internet economy model to public service and enterprise customers and builds a new ecosystem chain based on cloud computing. Operations in the Apsara Uni-manager Management Console are classified into the following parts: System initialization: completes basic system configurations, such as creating organizations, resource sets, and users, creating basic resources such as virtual private clouds (VPCs), and creating contacts and contact groups in CloudMonitor. Cloud resource creation: creates resources. Cloud resource management: completes resource management operations, such as starting, using, and releasing resources, and changing resource configurations and resource quotas. nd permissions

## User roles and permissions

This topic describes roles and their permissions.

| Role | Permissions |
|---|---|
| Resource user | Uses the cloud resources created and allocated by the operations administrator. |
| Resource set administrator | Manages the resource set, adds and manages users, activates and manages resources, examines and approves resource applications, and applies for resources or quotas. |
| Organization administrator | Manages the organization, creates and manages subordinate organizations, creates and manages resource sets, adds and manages users, allocates and manages roles, activates and manages resources, assigns administrators and quotas to subordinate organizations and resource sets, applies for resources or quotas, and examines and approves resource or quota applications. |
| Operations administrator | Has read and write permissions on all resources. |
| Security auditor | Audits the security of Apsara Stack. |

nd permissions

| Platform administrator | Initializes the system and creates operations administrators. |
|---|---|
| Resource auditor | Has read-only permission on all resources in Apsara Stack. |
| Organization security administrator | Uses Cloud Security Operation Center (SOC) to manage the security of hosts, applications, and networks for an organization. This role also manages security products related to Elastic Compute Service (ECS). |
| Security system configuration administrator | Configures system security features such as the upgrade center and global configurations. |
| Global organization security administrator | Uses SOC to provide security management for Apsara Stack and all tenants. This role also manages security products related to ECS. |
| Platform security administrator | Uses SOC to manage the security of Apsara Stack. |
| Global organization security auditor | Uses SOC to check the security conditions of all organizations. |
| Platform security auditor | Uses SOC to check the security conditions of Apsara Stack. |
| Platform security configuration administrator | Configures security services in Apsara Stack, such as Server Guard and Web Application Firewall (WAF). |
| Organization resource auditor | Has read-only permissions on all resources in the organization to which it belongs. |

he Apsara Uni-manager Manage ment Console

## Log on to the Apsara Uni-

**manager Management**

**Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable**
**MFA** topic in **Apsara Uni-manager Management Console User Guide** .
ntroduction

## Web page introduction

The web page of the Apsara Uni-manager Management Console consists of the top navigation bar, the information section of the current logon user, and the operation section.

**Web page of the Apsara Uni-manager Management Console**

Table 1. Functional sections of the web page

| Section |   | Description |
|---|---|---|
| 1 | Top naviga tion bar | This section includes the following modules: Home: uses charts to show the usage and monitoring data of existing system resources in each region. Products: manages all types of basic cloud services and resources. Applications: manages cloud applications of enterprises. Enterprise: manages organizations, resource sets, roles, users, logon policies, user groups, ownership, and resource pools. Configurations: manages resource pools, password policies, specifications, menus, and RAM roles. Operations: manages the routine operations of cloud resources, including usage statistics and quotas. Security: provides operation and system logs. |
| 2 | Inform ation sectio n of the curren t logon user | : allows you to switch between English, simplified Chinese, and traditional Chinese. : provides message notifications. User Information: displays the User Information, View Version, and Log Off menu items when you click the icon of the current logon user. If you click User information, you can perform the following operations on the User Information page: View basic information. Modify user information. Change the logon password. View the AccessKey pair of your Apsara Stack tenant account. Switch the current role. Enable or disable alert notification. If you click View Version, you can view the authorization status and build number of the Apsara Uni-manager Management Console. |
| 3 | Operat ion sectio n | Operation section:his section allows you to view information about resources and perform operations on resources. |

guration

## Initial configuration

### Configuration description

Before you use the Apsara Uni-manager Management Console, you must complete a series of basic configuration operations as an administrator, such as creating organizations, resource sets, users, and roles and initializing resources. This is the initial system configuration. The Apsara Uni-manager Management Console manages the organizations, resource sets, users, and roles of cloud data centers in a centralized and service-oriented manner to grant different resource access permissions to different users. Organization After the Apsara Uni-manager Management Console is deployed, a root organization is automatically generated. You can create other organizations under the root organization. Organizations are displayed in a hierarchical structure. You can create subordinate organizations under each organization level. Resource Set A resource set is a container used to store resources. Each resource must belong to a resource set. User A user is a resource manager and user. Role A role is a set of access permissions. You can assign different roles to different users to implement system access control to meet a variety of different requirements. The following table describes the relationships among organizations, resource sets, users, roles, and cloud resources.

| Relationship between two items | Relationsh ip type | Description |
|---|---|---|
| Organization and resource set | One-to- many | An organization can have multiple resource sets, but each resource set can belong to only a single organization. |
| Organization and user | One-to- many | An organization can have multiple users, but each user can belong to only a single organization. |
| Resource set and user | Many-to- many | A user can have multiple resource sets, and a resource set can be assigned to multiple users under the same level-1 organization. |
| User and role | Many-to- many | A user can have multiple roles, and a role can be assigned to multiple users. |
| Resource set and resource | One-to- many | A resource set can have multiple resources, but each cloud resource can belong to only a single resource set. |

### Configuration process

This topic describes the initial configuration process. guration Before you use the Apsara Uni-manager Management Console, you must complete the initial system configurations as an administrator based on the process shown in the following figure.
1. Create an organization
Create an organization to store resource sets and their resources.
2. Create a user
Create a user and assign the user different roles to meet different requirements for system access control.
3. Create a resource set
Create a resource set before you apply for resources.
4. Create cloud resources
Create instances in each service console based on project requirements. For more information about how to create cloud service instances, see the user guide of each cloud service.

## Monitoring

### View the workbench

The Apsara Uni-manager Management Console uses charts to keep you up to date on the current usage and monitoring information of resources.

**Background information**

The resource types displayed may vary with region types. See your dashboard for available resource types.
1. Log on to the Apsara Uni-manager Management Console.
By default, the **workbench** page appears when you log on to the Apsara Uni-manager Management Console. To return to the workbench page from other pages, click **Home** in the top navigation bar.
2. On the **workbench** page, you can view the instance summary information for all regions of
the Apsara Stack environment. You can click **Manage Charts** in the upper-right corner of the page to select all or individual modules to view relevant information. You can also click **Change Layout** in the upper-right corner of the page and drag a specific module to the desired location.

**Quota Overview**

Shows the usage and quotas of Elastic Compute Service (ECS), ApsaraDB RDS, Object Storage Service (OSS), and Server Load Balancer (SLB) resources.

**Instances**

Shows the numbers of ECS instances, ApsaraDB RDS instances, OSS buckets, and SLB instances in each region.

**Instance Trends**

Shows the numbers of recent ECS instances, ApsaraDB RDS instances, OSS buckets, and SLB instances.

**Resource Load**

Shows the top five ECS and ApsaraDB RDS instances in terms of disk usage, CPU utilization, and memory usage.

**Alert Rules**

Shows the number of alerts and details of the alerts.

**My Management**

Shows the numbers of organizations, resource sets, and users.

**Multi-cloud Regions**

Shows the information of all primary and secondary nodes in Apsara Stack. The network connection status and related alerts are displayed for each secondary node.

**Multi-cloud Resources**

Shows the cloud services and the number of instances in each secondary node.

### Configure the workbench

If your homepage is the default homepage, you can customize the dashboards for the homepage.

**Background information**

If Default Homepage is selected on the Menu Permissions tab of your role, no dashboards are displayed in the workbench on the homepage. You can manually configure a URL to be displayed on the homepage.

**Note**

This URL supports only domain names of the oneconsole type. You can view and access a URL only by using the account and the role that are used to specify the URL. For more information, see Create a menu.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click Home.
3. Click **Configure Iframe**.
4. Enter a URL in the field.
5. Click **OK**.

### CloudMonitor

#### Overview

CloudMonitor provides real-time monitoring, alerting, and notification services for resources to protect your business. In the CloudMonitor console, cloud services such as ECS, ApsaraDB for RDS, Server Load Balancer, Object Storage Service, ApsaraDB for Redis, ApsaraDB for MongoDB, AnalyticDB for PostgreSQL, VPN Gateways, Analyticdb for mysql 3.0, Elastic IP Address, API Gateway, Hologres, Tablestore, and Elasticsearch are supported. You can use the metrics of cloud services to configure alert rules and notification policies. This way, you can stay up to date on the status and performance of your instances and scale resources at the earliest opportunity when resources are insufficient.

#### Metrics

This topic describes the metrics available for each service. CloudMonitor checks the availability of services based on their metrics. You can configure alert rules and notification policies for these metrics to stay up to date on the running status and performance of monitored service instances. CloudMonitor can monitor resources of other services, including Elastic Compute Service (ECS), ApsaraDB RDS, ApsaraDB RDS (new link), Server Load Balancer (SLB), Object Storage Service (OSS), KVStore for Redis, ApsaraDB for MongoDB, VPN Gateway, AnalyticDB for MySQL 3.0, Elastic IP Address (EIP), API Gateway, Hologres, Tablestore, and Elasticsearch. The following tables list the metrics for each service.

**ECS**

**Basic metrics**

**Note**

The following metrics are collected from the virtual host layer and are slightly different from metrics collected inside the operating system.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (ECS) CPUUtilization | % | CPUUtilization | userId and instanceId | The CPU usage. |
| (ECS) InternetInRate | bits/s | InternetInRate | userId and instanceId | The rate of inbound traffic to the Internet. |
| (ECS) IntranetInRate | bits/s | IntranetInRate | userId and instanceId | The rate of inbound traffic to the intranet. |
| (ECS) InternetOutRate | bits/s | InternetOutRate | userId and instanceId | The rate of outbound traffic from the Internet. |
| (ECS) IntranetOutRate | bits/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic from the intranet. |
| (ECS)DiskReadBP S | Byte/s | DiskWriteBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS) DiskWriteBPS | Byte/s | DiskWriteBPS | userId and instanceId | The number of bytes written to all disks per second. |
| (ECS) DiskReadIOPS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |

| (ECS) DiskWriteIOPS | Count/s | DiskReadIOPS | userId and instanceId | The number of write IOPS of all disks. |
|---|---|---|---|---|

**Operating system metrics**

**Note**

For ECS instances, you must install a monitoring plug-in to collect metrics at the operating system level. Installation method: In the left-side navigation pane of the Cloud Monitor console, choose Cloud Service Monitoring and click **ECS**. In the **ECS** monitoring list, select the instances that you want to monitor, and click **Batch Install** in the lower part of the page. Metric data is displayed in the monitoring chart in 5 to 10 minutes after the monitoring plug-in is installed.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (Agent) Host.cpu total _ | % | cpu total _ | userId and instanceId | The CPU usage. |
| (Agent) Host.mem.used.u tilization | % | memory usedutil _ ization | userId and instanceId | The memory usage. |
| (Agent) Host.load15 | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
| (Agent) Host.load1 | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
| (Agent) Host.load5 | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| (Agent) Host.disk.utilizati on | % | diskusage utiliza _ tion | userId, instanceId, and device | The disk space usage. |

| (Agent) Host.fs.inode | % | fs inodeutilizatio _ n | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
|---|---|---|---|---|
| (Agent) Host.disk.readbyt es | Byte/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
| (Agent) Host.disk.readiop s | Count/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
| (Agent) Host.disk.writebyt es | Byte/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent) Host.disk.writeiop s | Count/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent) Host.tcpconnecti on | Count | net tcpconnectio _ n | userId, instanceId, and state | The number of Transmission Control Protocol (TCP) connections in each state. |
| (Agent) process.expend _ pid | N/A | process.expend | userId, instanceId, name, and pid | Detailed statistical metrics for the top 5 processes. |
| (Agent) process.count pr _ ocessname | count | process.number | userId, instanceId, and processName | The number of matched processes. |

**ApsaraDB RDS**

By default, an old link is used for ApsaraDB RDS. The period of collected data is 60 to 300 seconds. ApsaraDB RDS supports four engines: MySQL, SQL Server, PolarDB, and PostgreSQL.

**RDS-MySQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage new _ | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage new _ | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage new _ | % | DiskUsage new _ | userId and instanceId | The disk usage. |

| IOPSUtilization n _ ew | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
|---|---|---|---|---|
| MemoryUsage ne _ w | % | MemoryUsage n _ ew | userId and instanceId | The memory usage of the RDS instance. |
| MySQL NetworkI _ nNew new _ | bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL NetworkO _ utNew new _ | bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS new _ _ | Count/s | MySQL QPS new _ _ | userId and instanceId | MySQL QPS _ |
| DockerCpuUsage new _ | % | DockerCpuUsage new _ | userId and instanceId | The CPU usage of the Docker. |

**RDS-SQLServer**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU utilization of the RDS instance. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |
| SQLServer Netwo _ rkInNew | bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |

| SQLServer Netwo _ rkOutNew | bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |
|---|---|---|---|---|

**RDS-PolarDB**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |

**RDS-PostgreSQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS (new link)**

ApsaraDB RDS also supports a new link. The period of collected data is 60 seconds. ApsaraDB RDS (new link) supports three engines: MySQL, PolarDB, and PostgreSQL.

**RDS-Mysql**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage new _ | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |

| CpuUsage | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
|---|---|---|---|---|
| DiskUsage new _ | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPSUsage new _ | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage ne _ w | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| MySQL NetworkI _ nNew new _ | bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL NetworkO _ utNew new _ | bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS new _ _ | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second for the ApsaraDB RDS for MySQL instance. |
| DockerCpuUsage new _ | % | DockerCpuUsage new _ | userId and instanceId | The CPU usage of the Docker. |

**RDS-PolarDB**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage new _ | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage new _ | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage new _ | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPSUsage new _ | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage ne _ w | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |

**RDS-PostgreSQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

| ConnectionUsage new _ | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
|---|---|---|---|---|
| CpuUsage new _ | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage new _ | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPSUsage new _ | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage ne _ w | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |

**SLB**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| MemoryUsage ne _ w | Count | ActiveConnection | userId, instanceId, port, and protocol | Number of active TCP connections per second. |
| InactiveConnecti on | Count | InactiveConnecti on | userId, instanceId, port, and protocol | Number of inactive TCP connections. |
| MaxConnection | Count/s | MaxConnection | userId, instanceId, port, and protocol | The number of concurrent connections per second on the port. |
| NewConnection | Count | NewConnection | userId, instanceId, port, and protocol | The number of new TCP connections. |
| PacketRX | Count/s | PacketRX | userId, instanceId, port, and protocol | The number of outbound packets per second. |
| PacketTX | Count/s | PacketTX | userId, instanceId, port, and protocol | The number of inbound packets per second. |
| TrafficRXNew | bit/s | TrafficRXNew | userId, instanceId, port, and protocol | The inbound bandwidth. |
| TrafficTXNew | bit/s | TrafficTXNew | userId, instanceId, port, and protocol | The outbound bandwidth. |
| UnhealthyServer Count | Count | UnhealthyServer Count | userId, instanceId, port, and vip | The number of unhealthy ECS instances. |

**OSS**

**Overview**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| ValidRequestCou nt | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Byte | InternetSend | userId and BucketName | The outbound traffic from the Internet. |
| InternetRecv | Byte | InternetRecv | userId and BucketName | The inbound traffic to the Internet. |
| IntranetSend | Byte | IntranetSend | userId and BucketName | The outbound traffic from the intranet. |
| IntranetRecv | Byte | IntranetRecv | userId and BucketName | The inbound traffic to the intranet. |
| CdnSend | Byte | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CdnRecv | Byte | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Byte | SyncSend | userId and BucketName | The cross-region replication outbound traffic. |
| SyncRecv | Byte | SyncRecv | userId and BucketName | The cross-region replication inbound traffic. |
| MeteringStorage Utilization | Byte | MeteringStorage Utilization | userId and BucketName | The currently used storage. |

**Request status details**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ServerErrorCount | Count | ServerErrorCount | userId and BucketName | The number of requests with a server error. |

| ServerErrorRate | % | ServerErrorRate | userId and BucketName | The ratio of requests with a server error. |
|---|---|---|---|---|
| NetworkErrorCou nt | Count | NetworkErrorCou nt | userId and BucketName | The number of requests with a network error. |
| NetworkErrorRate | % | NetworkErrorRat e | userId and BucketName | The ratio of requests with a network error. |
| AuthorizationErro rCount | Count | AuthorizationErro rCount | userId and BucketName | The number of requests with an authorization error. |
| ResourceNotFoun dErrorCount | Count | ResourceNotFoun dErrorCount | userId and BucketName | The number of requests with an error that indicates resources cannot be found. |
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |
| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |
| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error that indicates resources cannot be found. |
| ClientTimeoutErr orRate | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | N/A | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The number of successful requests. |

| RedirectCount | Count | RedirectCount | userId and BucketName | The number of redirected requests. |
|---|---|---|---|---|
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |

**Maximum latency**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum E2E latency of GetObject requests. |
| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |
| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPostObjectE2 eLatency |   |   | userId and BucketName | The maximum E2E latency of PostObject requests. |
| MaxPostObjectSe rverLatency |   |   | userId and BucketName | The maximum server latency of PostObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |

| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
|---|---|---|---|---|
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |
| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |
| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |

**Successful requests of different types**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GetObjectCount | Frequency | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |
| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |

| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
|---|---|---|---|---|
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

**ApsaraDB for Redis**

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| FailedCount | Count/S | FailedCount | userId and instanceId | The number of failed operations. |
| IntranetIn | Byte/s | IntranetIn | userId and instanceId | The inbound traffic to the intranet. |
| IntranetInRatio | % | IntranetInRatio | userId and instanceId | The write bandwidth usage. |
| IntranetOut | Byte/s | IntranetOut | userId and instanceId | The outbound traffic from the intranet. |
| IntranetOutRatio | % | IntranetOutRatio | userId and instanceId | The read bandwidth usage. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |
| UsedQPS | Count/S | UsedQPS | userId and instanceId | The number of used queries per second (QPS). |

**ApsaraDB for MongoDB**

**Basic metric**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| CPUUtilization | % | CPUUtilization | userId, instanceId, and role | The CPU usage. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |

| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The ratio of used disk space. |
|---|---|---|---|---|
| IOPSUtilization | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |
| ConnectionAmou nt | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |
| QPS | Count | QPS | userId, instanceId, and role | The number of requests per second. |
| ConnectionAmou nt | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk capacity**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| InstanceDiskAmo unt | Byte | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |
| DataDiskAmount | Byte | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
| LogDiskAmount | Byte | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network requests**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| IntranetIn | Byte | IntranetIn | userId, instanceId, and role | The inbound traffic to the intranet. |
| IntranetOut | Byte | IntranetOut | userId, instanceId, and role | The outbound traffic from the intranet. |
| NumberRequests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |

**Operation count**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| OpCommand | Frequency | OpCommand | userId, instanceId, and role | The number of Command operations. |

| OpDelete | Frequency | OpDelete | userId, instanceId, and role | The number of Delete operations. |
|---|---|---|---|---|
| OpGetmore | Frequency | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpInsert | Frequency | OpInsert | userId, instanceId, and role | The number of Insert operations. |
| OpQuery | Frequency | OpQuery | userId, instanceId, and role | The number of Query operations. |
| OpUpdate | Frequency | OpUpdate | userId, instanceId, and role | The number of Update operations. |

**AnalyticDB for PostgreSQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId, instanceId, and role | The connection usage. |
| CpuUsage | % | CpuUsage | userId, instanceId, and role | The CPU usage. |
| DiskUsage | % | DiskUsage | userId, instanceId, and role | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId, instanceId, and role | The IOPS usage. |
| MemoryUsage | % | MemoryUsage | userId, instanceId, and role | The memory usage. |

**VPN Gateway**

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ipsec.rxPkgs | pps | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate of inbound packets of the connection. |
| ipsec.txPkgs | pps | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate of outbound packets for the connection. |

| ipsec rx.rate _ | bits/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits per second for the connection. |
|---|---|---|---|---|
| ipsec tx.rate _ | bits/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits per second for the connection. |
| ssl client.count _ | count | ssl client.count _ | userId and instanceId | The number of connections. |

**AnalyticDB for MySQL 3.0**

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| connections | count | connections | userId and instanceId | The rate of inbound packets of the connection. |
| worker avg cpu _ _ _ used | % | worker avg cpu _ _ _ used | userId and instanceId | The CPU usage of the worker. |
| executor avg cp _ _ u used _ | % | executor avg cp _ _ u used _ | userId and instanceId | The CPU usage of the executor. |
| worker max nod _ _ e disk used perc _ _ _ ent | % | worker max nod _ _ e disk used perc _ _ _ ent | userId and instanceId | The maximum disk usage of the worker in reserved mode. |
| disk used percen _ _ t | % | disk used percen _ _ t | userId and instanceId | The disk usage in reserved mode. |
| worker max nod _ _ e disk used MB _ _ _ | Mbyte | worker max nod _ _ e disk used MB _ _ _ | userId and instanceId | The maximum used disk space of the worker in elastic mode. |
| ColdDataDiskUsa ge | Mbyte | ColdDataDiskUsa ge | userId and instanceId | The used disk space for cold data in elastic mode. |
| HotDataDiskUsag e | Mbyte | HotDataDiskUsag e | userId and instanceId | The used disk space for hot data in elastic mode. |
| worker avg read _ _ bytes _ | Mbyte | worker avg read _ _ bytes _ | userId and instanceId | The read throughput of the worker. |
| worker avg write _ _ bytes _ | Mbyte | worker avg write _ _ bytes _ | userId and instanceId | The write throughput of the worker. |

| executor avg rea _ _ d bytes MB _ _ | Mbyte | executor avg re _ _ ad bytes MB _ _ | userId and instanceId | The read throughput of the executor. |
|---|---|---|---|---|
| executor avg wri _ _ te bytes MB _ _ | Mbyte | executor avg wri _ _ te bytes MB _ _ | userId and instanceId | The write throughput of the executor. |
| worker avg read _ _ iops _ | count/s | worker avg read _ _ iops _ | userId and instanceId | The read IOPS of the worker. |
| worker avg write _ _ iops _ | count/s | worker avg write _ _ iops _ | userId and instanceId | The write IOPS of the worker. |
| executor avg rea _ _ d iops _ | count/s | executor avg re _ _ ad iops _ | userId and instanceId | The read IOPS of the executor. |
| executor avg wri _ _ te iops _ | count/s | executor avg wri _ _ te iops _ | userId and instanceId | The write IOPS of the executor. |
| worker avg io ut _ _ _ il | % | worker avg io ut _ _ _ il | userId and instanceId | The disk I/O usage. |
| QPS | count/s | qps | userId and instanceId | The number of requests per second. |
| query avg rt _ _ | ms | query avg rt _ _ | userId and instanceId | The average query time. |
| query max rt _ _ | ms | query max rt _ _ | userId and instanceId | The maximum query time. |
| query total wait _ _ _ time | ms | query total wait _ _ _ time | userId and instanceId | The average query waiting time. |
| query max wait _ _ _ time | ms | query max wait _ _ _ time | userId and instanceId | The maximum query waiting time. |
| tps | count/s | tps | userId and instanceId | The number of transactions per second. |
| insert avg rt _ _ | ms | insert avg rt _ _ | userId and instanceId | The average write response time. |
| insert max rt _ _ | ms | insert max rt _ _ | userId and instanceId | The maximum write response time. |
| insert in bytes _ _ | Mbyte | insert in bytes _ _ | userId and instanceId | The write throughput. |

**EIP**

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|

| net rx.rate _ | bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
|---|---|---|---|---|
| net rxPkgs.rate _ | Packets/Second | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Packets/Second | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| out ratelimit dro _ _ p speed _ | Packets/Second | out ratelimit dro _ _ p speed _ | userId and instanceId | The rate at which packets are dropped due to throttling. |

**API Gateway**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Latency | ms | Latency | userId, region, and apiUid | The response time. |
| SumQPS | Count | SumQPS | userId, region, and apiUid | The total number of requests. |
| TrafficRX | KBytes | TrafficRX | userId, region, and apiUid | The inbound traffic. |
| TrafficTX | KBytes | TrafficTX | userId, region, and apiUid | The outbound traffic. |
| code2XX | Count | code2XX | userId, region, and apiUid | The number of times a 2XX HTTP status code is returned. |
| code4XX | Count | code4XX | userId, region, and apiUid | The number of times a 4XX HTTP status code is returned. |
| code5XX | Count | code5XX | userId, region, and apiUid | The number of times a 5XX HTTP status code is returned. |

**Hologres**

**Instance status**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| connection num _ | Count | connection num _ | userId and instanceId | The number of SQL connections. |
| connection usag _ e | % | connection usag _ e | userId and instanceId | The connection usage. |

|   |   |   | Apsara Uni-m t Console U | anager Manageme ser Guide·Monitorin |
|---|---|---|---|---|

| cpu usage _ | % | cpu usage _ | userId and instanceId | The CPU usage. |
|---|---|---|---|---|
| memory usage _ | % | memory usage _ | userId and instanceId | The memory usage. |
| storage usage _ | Bytes | storage usage _ | userId and instanceId | The used storage. |
| io write through _ _ put | Bytes | io write through _ _ put | userId and instanceId | The write I/O throughput per second. |
| io read throughp _ _ ut | Bytes | io read throughp _ _ ut | userId and instanceId | The read I/O throughput per second. |

**Status**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| failed query qps _ _ | count/s | failed query qps _ _ | userId and instanceId | The number of failed queries per second. |
| query latency _ | ms | query latency _ | instanceId, userId, and cmdType | The latency of the query. |
| Query QPS | count/s | query qps _ | instanceId, userId, and cmdType | The QPS. |
| dml rps _ | count/s | dml rps _ | instanceId, userId, and cmdType | The number of write records per second. |

**Tablestore**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| InstanceVCU | count/s | InstanceVCU | userId and instanceName | The VCUs of the instance. |
| InstanceReserved VCU | count/s | InstanceReserve dVCU | userId and instanceName | The reserved VCUs of the instance. |
| InstanceFreeRea dCU NoOp _ | count/s | InstanceFreeRea dCU NoOp _ | userId and instanceName | The internal read CUs. |
| InstanceFreeWrit eCU NoOp _ | count/s | InstanceFreeWrit eCU NoOp _ | userId and instanceName | The internal write CUs. |

| InstanceOverRea dCU NoOp _ | count/s | InstanceOverRea dCU NoOp _ | userId and instanceName | The excess read CUs of the instance. |
|---|---|---|---|---|
| InstanceOverWrit eCU NoOp _ | count/s | InstanceOverWrit eCU NoOp _ | userId and instanceName | The excess write CUs of the instance. |
| InstanceReadCU _ NoOp | count/s | InstanceReadCU _ NoOp | userId and instanceName | The operation read CUs. |
| InstanceWriteCU _ NoOp | count/s | InstanceWriteCU _ NoOp | userId and instanceName | The operation write CUs. |
| InstanceRequest Number NoOp _ | count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| InstanceCount2x xNumber NoOp _ | count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests that return a 2XX HTTP status code. |
| InstanceCount42 9Number NoOp _ | count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests that return HTTP status code 429. |
| InstanceCount4x xNumber NoOp _ | count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests that return a 4XX HTTP status code. |
| InstanceCount5x xNumber NoOp _ | count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests that return a 5XX HTTP status code. |
| InstanceExtranetI n NoOp _ | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic to the Internet. |
| InstanceExtranet Out NoOp _ | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic from the Internet. |
| InstanceFreeExtr anetOut NoOp _ | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The outbound traffic from the Internet that is free of charge. |
| InstanceRowCoun t NoOp _ | count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| InstanceFailRowC ount NoOp _ | count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |

**Elasticsearch**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ClusterStatus | Value | ClusterStatus | userId and instanceId | The status of the cluster. Valid values: 0: green, which indicates normal. 1: yellow, which indicates warning. 2: red, which indicates exception. |
| NodeCPUUtilizati on | % | NodeCPUUtilizati on | userId and instanceId | The CPU usage of the instance node. |
| NodeDiskUtilizati on | % | NodeDiskUtilizati on | userId and instanceId | The disk usage of the instance node. |
| NodeHeapMemor yUtilization | % | NodeHeapMemor yUtilization | userId and instanceId | The HeapMemory usage of the instance node. |

#### View the list of monitored instances

This topic describes how to view the list of monitored instances. You can obtain the status of instances in your organization, resource set, and region in an efficient manner.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the top navigation bar of the **CloudMonitor** console, select an organization, a resource
set, and a region.
4. In the left-side navigation pane of the **CloudMonitor** console, click **Cloud Service**
**Monitoring**.
5. Click a cloud service.
In the instance list that is displayed, view the instance information such as the organization and resource group.

#### View monitoring charts

You can view monitoring charts to obtain up-to-date information about each instance.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > CloudMonitor**.
3. In the left-side navigation pane of the CloudMonitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Monitoring Charts** in the **Actions** column corresponding to an instance.
On the Monitoring Charts page that appears, you can select a date and time to view the monitoring data of each metric.

### Alerts

#### View alert overview

On the **Overview** page in Cloud Monitor, you can view the alert status statistics and alert logs.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > CloudMonitor**.
3. In the left-side navigation pane of the Cloud Monitor page, click **Overview**.
4. On the **Overview** page, view the alert status statistics and alert logs that are generated in
the last 24 hours.

#### Enable or disable alert notification

You can choose whether to enable alert notification by email or DingTalk.

**Prerequisites**

Valid contact information is specified when you create a user. If the contact information has changed, you must modify your personal information. For more information, see Modify personal information.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **Personal information**.
3. In the **Messages** section, select **Email** or **DingTalk** to enable alert notification.
To disable alert notification, clear the corresponding check box.

#### View alert logs

You can view alert information to stay up to date on the running status of Elastic Compute Service (ECS), ApsaraDB RDS, Server Load Balancer (SLB), KVStore for Redis, VPN Gateway, AnalyticDB for PostgreSQL, ApsaraDB for MongoDB, Elastic IP Address (EIP), API Gateway, and Object Storage Service (OSS).

**Background information**

Alert information contains information for all items that do not comply with your configured alert rules.

**Note**

The system can retain up to one million alert items generated within the last three months. This topic describes how to view alert information for ECS. You can view the alert information for other cloud resources in a similar manner.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > Cloud Monitor**.
3. In the left-side navigation pane of the Cloud Monitor page, choose **Alerts > Alert History**.
4. On the **Alert Rule History List** page, filter alert information by rule ID, rule name, service,
and date. The following table describes the fields in the query result. Table 1. Alert information fields

| Parameter | Description |
|---|---|
| Product | The service for which the alert was triggered. |
| Fault Instance | The instance for which the alert was triggered. |
| Occurred At | The time when the alert was triggered. |
| Rule Name | The name of the alert rule. |
| Status | The status of the alert rule. |
| Notification Contact | The recipient of the alert notification. |

#### Alert rules

##### View alert rules

After you create alert rules, you can view your alert rules on the Alert Rules page.

**Background information**

The system provides alert rules for ECS, ApsaraDB RDS, SLB, OSS, KVStore for Redis, VPN Gateway, AnalyticDB for PostgreSQL, ApsaraDB for MongoDB, EIP, and API Gateway.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > CloudMonitor**.
3. In the left-side navigation pane of the CloudMonitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Alert Rules** in the **Actions** column corresponding to an instance.
On the **Alert Rules** page, view the detailed information of alert rules.

##### Create an alert rule

You can create an alert rule to monitor an instance.

**Prerequisites**

For Elastic Compute Service (ECS) instances, you must install a monitoring plug-in to collect metric data at the operating system level. You can use the following method to install a monitoring plug-in:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > Cloud Monitor**.
3. In the left-side navigation pane, choose **Cloud Service Monitoring > ECS**.
4. In the ECS instance list, select the instances that you want to monitor and click **Batch**
**Install**.

**Note**

The monitoring chart displays monitoring data 5 to 10 minutes after the monitoring plugin is installed.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > Cloud Monitor**.
3. In the left-side navigation pane of the Cloud Monitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Alert Rules** in the **Actions** column corresponding to an instance.

**Note**

You can also use the search feature to query specific instances for which you want to create alert rules.
6. On the **Alert Rules** page, click **Create Alert Rule**.
Table 1. Parameters for creating an alert rule

| Parameter | Description |
|---|---|
| Product | The monitored cloud service. |
| Resource Range | The range of resources that is associated with the alert rule. |
| Rule Description | The description of the alert rule. |
| Add Rule Description | Click Add Rule Description to go to the rule configuration panel. For more information, see Parameters for adding rule description. |
| Effective Time | Only a single alert is sent during each mute duration, even if the metric value exceeds the alert rule threshold several times in a row. |
| Effective Period | An alert is sent only when the threshold is crossed during the effective period. |
| HTTP CallBack | The callback URL when the alert conditions are met. |

| Alert Contact Group | The group to which alerts are sent. |
|---|---|

Table 2. Parameters for adding rule description

| Parameter | Description |
|---|---|
| Rule Name | The name of the alert rule. The name must be 1 to 64 characters in length and can contain letters and digits. |
| Metric Name | Different products have different monitoring metrics. For more information, see Metrics. |
| Comparison | The comparison between thresholds and observed values. The comparison operators include >, >=, <, and <=. When the comparison rule is satisfied, an alert rule is triggered. |
| Threshold and Alert Level | Different metrics have different reference thresholds. |

7. Click **OK**.

##### Disable an alert rule

You can disable one or more alert rules.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > CloudMonitor**.
3. In the left-side navigation pane of the Cloud Monitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Alert Rules** in the **Actions** column corresponding to an instance.
6. On the **Alert Rules** page, choose **More > Disable** in the **Actions** column corresponding
to the alert rule to be disabled.
7. In the Disable Alert Rule message, click **Confirm**.

##### Enable an alert rule

You can re-enable alert rules at any time after they have been disabled.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > Cloud Monitor**.
3. In the left-side navigation pane of the CloudMonitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Alert Rules** in the **Actions** column corresponding to an instance.
6. On the **Alert Rules** page, choose **More > Enable** in the **Actions** column corresponding to
the alert rule to be enabled.
7. In the message that appears, click **Confirm**.

##### Delete an alert rule

You can delete alert rules that are no longer needed.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Monitoring and O&M > CloudMonitor**.
3. In the left-side navigation pane of the Cloud Monitor page, click **Cloud Service**
**Monitoring**.
4. Click a cloud service.
5. Click **Alert Rules** in the **Actions** column corresponding to an instance.
6. On the **Alert Rules** page, click **Delete** in the **Actions** column corresponding to the alert
rule to be deleted.
7. In the Delete Alert message, click **Confirm**.
ud on Alibaba Cloud

## VMware Cloud on Alibaba

**Cloud**

### VMware Cloud on Alibaba

**Cloud**

#### Log on to the VMware Cloud on Alibaba

**Cloud console**

This topic describes how to log on to the VMware Cloud on Alibaba Cloud console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. ud on Alibaba Cloud

**Note**

You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button. If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

**Note**

Obtain the username and password from an operations administrator. The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log On**.
4.
5. In the top navigation bar, choose **Products > Elastic Computing > VMware Cloud on**
**Alibaba Cloud**.

#### Bind a VMware Cloud on Alibaba Cloud

**region**

Before you use VMware Cloud on Alibaba Cloud, you must bind a VMware Cloud on Alibaba Cloud region to an organization.

**Prerequisites**

A VMware Cloud on Alibaba Cloud region is managed. For more information, see Add a VMware node.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, click **Resource Pools**.
4. In the organization navigation tree, click an organization. In the **Regions** section, select the
region that you want to bind.
5. Click **Update Association**.

#### Instructions

ud on Alibaba Cloud

##### Limits

Before you use VMware Cloud on Alibaba Cloud virtual machine (VM) templates, you must familiarize yourself with the instance limits.

**General limits**

You must select appropriate operating systems for VMware Cloud on Alibaba Cloud VM templates. The following operating systems are confirmed to be supported and available in the Apsara Uni-manager Management Console: CentOS8.2.2004 CentOS7.2003 CentOS6.10 Ubuntu-20.04.1 Ubuntu-18.04.5 Ubuntu-16.04.7 WindowsServer2016 WindowsServer2019 The Apsara Uni-manager Management Console supports VMware vSphere 6.x. Other versions of VMware vSphere such as 5.x or 7.x can be supported in theory. However, whether or not specific versions are supported depends on the compatibility of the VMware Cloud on Alibaba Cloud API and must be evaluated by the R&D team of the Apsara Unimanager Management Console. The Apsara Uni-manager Management Console does not support the import of existing VMware instances. You must install VMware Tools. For more information, see the VMware documentation. Select Full Installation in the installation process. You must modify network interface controller (NIC) configurations in the operating system of the VM. When you create a VM in the Apsara Uni-manager Management Console, you can specify the IP address of the operating system. This feature is supported by valid NIC configurations. ud on Alibaba Cloud Operating systems of VM templates must be in Dynamic Host Configuration Protocol (DHCP) mode. Information such as the MAC address and universally unique identifier (UUID) in the NIC configurations must be removed. The following information can be retained.

**Note**

Some additional configurations are required for the following operating systems: CentOS 6: You must clear the content in the NIC configuration file named 70persistent-net.rules. The file is stored in the /etc/udev/rules.d/ directory. CentOS 7: The system generates the name for a NIC, such as ifcfg-ens160. You must modify the name to ifcfg-eth0 to make the name take effect. Ubuntu 18.04, 20.04, and later: You must run the `sudo rm /etc/netplan/*.yaml` command to remove the NIC configurations.

##### Suggestions

Before you use VMware Cloud on Alibaba Cloud virtual machine (VM) templates, take note of the following operation suggestions: Select the latest version of VM hardware. Select thin provision for VM disks. Disk replication is required when you create VMs based on templates. Files of disks of the thin provision type are small in size. This helps accelerate the creation of VMs.

**Note**

Large sizes of disk files in VM templates or slow storage write speeds may cause VM creation to time out and fail. The maximum timeout period supported by the Apsara Unimanager Management Console is 10 minutes.

#### Instances

ud on Alibaba Cloud

##### Create a VMware Cloud on Alibaba Cloud

**instance**

A VMware Cloud on Alibaba Cloud instance is a virtual machine (VM) that contains the basic computing components of a server, such as CPU, memory, operating system, network, and disks.

**Prerequisites**

The region where VMware Cloud on Alibaba Cloud is deployed is managed. For more information, see Add a VMware node. The region where VMware Cloud on Alibaba Cloud is deployed is bound to an organization. For more information, see Bind a VMware Cloud on Alibaba Cloud region.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Click **Create Instance** in the upper-right corner.
5. Configure parameters listed in the following table to create an instance.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Basic Settings | Organization | Yes | The organization in which to create the instance. |
|   | Resource Set | Yes | The resource set in which to create the instance. |
| Region | Region | Yes | The region in which to create the instance. |
|   | Zone | Yes | The zone in which to create the instance. |
|   | VPC | Yes | The VPC in which to create the instance. |
|   | vSwitch | Yes | Select the vSwitch to which the instance belongs. The vSwitch corresponds to the port group of a VMware ESXi host or a distributed switch, and maps to the VLAN of a physical switch. |

ud on Alibaba Cloud

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Private IP Address | Yes | The private IPv4 address of the instance. The private IPv4 address must be within the CIDR block of the vSwitch. |
|   | Private Subnet Mask | Yes | The private subnet mask. Example: 255.255.255.0. The specified subnet mask must be within the CIDR block of the selected vSwitch. |
|   | Private IP Address of Gateway | Yes | The private IP address of the gateway. Example: 192.168.100.1. The IP address must be within the CIDR block of the selected vSwitch. |
|   | Private IP Address of DNS Server | No | The private IP address of the DNS server. Example: 114.114.114.114. The IP address must be within the CIDR block of the selected vSwitch. |
| Instance | Instance Family | No | The instance family of the instance. Valid values: Memory Optimized Compute Optimized General Purpose |
|   | Instance Type | Yes | The instance type of the instance. You can specify the vCPUs and memory. |
| Image | Image Type | No | The type of the image. Default value: Public Image. |
|   | Public image | Yes | The public image of the instance. |
|   | > Document Version: 2025110 |   |   |

|   | Apsara Uni-manager Manageme t Console User Guide·VMware Cl ud on Alibaba Clou |   |   |
|---|---|---|---|
| Section | Parameter | Required | Description |
| Storage | System Disk (GB) | No | The system disk to which the operating system is installed. You can configure different storage types for the disk. Valid values: Shared Storage: All: The system selects an available shared storage. We recommend that you select this type. Shared Storage: storageA: The storage named storageA of the VMware Cloud on Alibaba Cloud instance is used. Administrators must make sure the storage is appropriate. If the storage capacity is insufficient, the instance fails to be created. |

ud on Alibaba Cloud

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Data Disk (GB) | No | You can also add data disks after the instance is created. You can configure different storage types for the disk. Valid values: Shared Storage: All: The system selects an available shared storage. We recommend that you select this type. Shared Storage: storageA: The storage named storageA of the VMware Cloud on Alibaba Cloud instance is used. Administrators must make sure the storage is appropriate. If the storage capacity is insufficient, the instance fails to be created. You must also specify the provision type when you create the instance. Valid values: Thin Provision: Storage space increases with the use of the disk. Thick Provision Lazy Zeroed: Storage space is equal to the size of the disk and does not increase. The disk is formatted when data is written. Thick Provision Eager Zeroed: Storage space is equal to the size of the disk and does not increase. The storage of the disk is immediately formatted when the disk is created. |
| Password | Password Setting | No | Select Set after Purchase. |
| Instance Name | Instance Name | Yes | The name of the instance. The name must be 2 to 128 characters in length and can contain letters, periods (.), underscores ( ), hyphens (-), _ and colons (:). It must start with a letter and cannot start with http:// or https://. |

6. Click **Submit**.
ud on Alibaba Cloud

##### View instance information

You can view the list of created instances as well as details of individual instances, such as their basic configurations, disks, and elastic network interfaces (ENIs).
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed. You can view the list of VMware Cloud on Alibaba Cloud instances that are deployed in the current region.
4. Use one of the following methods to go to the details page of an instance:
In the **Instance ID/Name** column, click the instance ID. Click **Manage** in the **Actions** column corresponding to the instance. Choose **More** > **Show Details** in the **Actions** column corresponding to the instance.

##### Modify an instance

You can modify the name and description of a created VMware Cloud on Alibaba Cloud instance.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance that you want to modify and choose **More** > **Modify** in the **Actions**
column.
5. Modify the name and description of the instance.
6. Click **OK**.

##### Remotely connect to an instance

You can remotely connect to and manage added VMware Cloud on Alibaba Cloud instances.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance that you want to manage and click **Remote Connection** in the **Actions**
column.
5. Enter the username and password.
For a Linux instance, enter the username root and the logon password. ud on Alibaba Cloud

**Note**

When you log on to the Linux instance, the password is not displayed as you enter it. Press the Enter key after you enter the password. For a Windows instance, to use a key combination such as Ctrl+Alt+Delete, click the List icon in the upper-right corner of the page and select the corresponding composite key from the drop-down list. Enter the username and password, and click the Log On icon.

##### Stop an instance

You can stop VMware Cloud on Alibaba Cloud instances that are not in use. The stop operation interrupts services that are running on the instances. Exercise caution when you perform this operation.

**Prerequisites**

The instance is in the **Running** state.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Use one of the following methods to stop instances:
To stop a single instance, find the instance and choose **More** > **Instance Status** > **Stop** in the **Actions** column. To stop one or more instances at a time, select the instances and click **Stop** in the lower part of the Instances page.
5. Click **OK**.

**Execution results**

When the instance is being stopped, its state in the **Status** column changes from **Running** to **Stopping**. After the instance is stopped, its state changes to **Stopped**.

##### Start an instance

You can start a stopped instance. ud on Alibaba Cloud

**Prerequisites**

The instance is in the **Stopped** state.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Use one of the following methods to start instances:
To start a single instance, find the instance and choose **More** > **Instance Status** >
**Start** in the **Actions** column.
To start one or more instances at a time, select the instances and click **Start** in the lower part of the Instances page.
5. Click **OK**.

**Execution results**

When the instance is being started, its state in the **Status** column changes from **Stopped** to
**Starting**. After the instance is started, its state changes to **Running**.

##### Restart an instance

After you change the logon password of an instance or install system updates, you must restart the instance. The restart operation stops the instances for a short period of time and interrupts services that are running on the instance. Exercise caution when you perform this operation.

**Prerequisites**

The instance is in the **Running** state.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Use one of the following methods to restart the instance:
To restart a single instance, find the instance and choose **More** > **Instance Status** >
**Restart** in the **Actions** column.
To restart one or more instances at a time, select the instances and click **Restart** in the lower part of the Instances page.
5. In the Restart Instance dialog box, select a restart mode.
**Restart**: restarts the instance normally.
**Force Restart**: forces the instance to restart. This may result in the loss of unsaved
data.
6. Click **OK**.

##### Delete an instance

ud on Alibaba Cloud You can delete instances that are no longer needed to release their resources. Deleted instances cannot be recovered. We recommend that you back up data before you delete an instance. If data disks are released with the instances, the disk data cannot be recovered.

**Prerequisites**

The instance is in the **Stopped** state.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Select the instance and click **Delete** in the lower part of the Instances page.
5. Click **OK**.

##### Change the instance type of an instance

You can change the instance types of instances to suit your business needs. This eliminates the need to create VMware Cloud on Alibaba Cloud instances.

**Prerequisites**

The instance is in the **Stopped** state.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose instance type you want to change and click **Upgrade/Downgrade**
in the **Actions** column.
5. On the page that appears, select a new instance type and click **Submit**.
The page that appears shows the instance types available for selection.
6. Start the instance to make the new instance type take effect.
For more information, see Start an instance.

#### Images

##### Create a custom image

You can perform the following steps to create a custom image.

**Background information**

You can create a custom image from an instance to replicate the data of all disks on the instance. ud on Alibaba Cloud

**Note**

To avoid data security risks, we recommend that you delete sensitive data from an instance before you use the instance to create a custom image.

**Create a custom image from an instance**

1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance from which you want to create a custom image and choose **More** >
**Create Custom Image** in the **Actions** column.
5. Set the name, sharing scope, and description for the custom image, and click **OK**.
The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), hyphens (-), and colons (:). It cannot start with a special character or digit. You can set the sharing scope to the permission scope of the image. The description must be 2 to 256 characters in length and cannot start with http:// or https://.

##### View images

You can view the list of created images.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, choose **Images** > **Images**.
3. In the top navigation bar, move the pointer over **Region** and select the region where the
image is created.
4. Select a filter option, enter the corresponding information in the search box, and then click
**Search**.
You can select multiple filter options to narrow down search results.

| Parameter | Description |
|---|---|
| Image Name | The image name used to search for the image. |
| Image ID | The image ID used to search for the image. |

#### Snapshots

##### Create a snapshot

You can manually create a snapshot for a disk to back up disk data. ud on Alibaba Cloud

**Prerequisites**

The instance to which the disk is attached is in the **Running** or **Stopped** state. The disk is in the **Running** state.

**Background information**

A snapshot of a disk can be used to roll back data of the disk. When you create a snapshot, take note of the following items: For each disk, the first snapshot taken is a full snapshot and subsequent snapshots are incremental snapshots. It takes longer to create the first full snapshot than it does subsequent incremental snapshots. The amount of taken time depends on the amount of data that has been changed since the previous snapshot. The more data that has been changed, the longer it takes to create an incremental snapshot. Avoid creating snapshots during peak hours.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Click the instance from which you want to create a snapshot. On the page that appears,
click the **Snapshots** tab.
5. Click **Create and Bind Snapshot** .
6. Set the name, type, and description for the snapshot, and click **Submit**.

| Parameter | Description |
|---|---|
| Snapshot Name | The name of the snapshot. |
| Snapshot Type | The snapshot type. Valid values: Disk Snapshot: stores information in disks. Memory Snapshot: stores information in memory. |
| Snapshot Description | The description of the snapshot. |

##### Delete a snapshot

You can delete a snapshot that is no longer needed. After the snapshot is deleted, it cannot be recovered.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
ud on Alibaba Cloud
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance whose snapshot is to be deleted and click the **Snapshots** tab.
5. Use one of the following methods to delete the snapshot:
To delete a single snapshot, find the snapshot and click **Delete** in the **Actions** column. To delete one or more snapshots at a time, select the snapshots and click **Delete** in the lower part of the Snapshots tab.
6. Click **OK.**

##### View snapshots

You can view the list of created snapshots.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance in which you want to view snapshots and click the **Snapshots** tab.
5. Select a filter option, enter the corresponding information in the search box, and then click
**Search**.
You can select multiple filter options to narrow down search results.

| Parameter | Description |
|---|---|
| Snapshot Name | The snapshot name used to search for the snapshot. |
| Snapshot ID | The snapshot ID used to search for the snapshot. |

#### Disks

##### Create a disk

To increase the storage space of VMware Cloud on Alibaba Cloud instances, you can create standalone data disks and then attach them to the instances. This topic describes how to create an empty data disk. You cannot create standalone system disks.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance for which you want to create a disk and click the **Disks** tab.
ud on Alibaba Cloud
5. Click **Create and Attach Disk**.
6. Configure parameters listed in the following table to create a disk.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Zone | Yes | The zone in which to create the disk. |
| Basic Settings | Specifications | Yes | The disk category and the disk size. |
|   | Provision Type | Yes | The provision type. Valid values: Thin Provision: Storage space increases with the use of the disk. Thick Provision Lazy Zeroed: Storage space is equal to the size of the disk and does not increase. The disk is formatted when data is written. Thick Provision Eager Zeroed: Storage space is equal to the size of the disk and does not increase. The storage of the disk is immediately formatted when the disk is created. |

7. Click **Submit**.

**Execution results**

The created disk is displayed in the disk list and in the **Running** state.

##### View disks

You can view the list of created disks and the details of individual disks.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed. ud on Alibaba Cloud
4. Click the instance for which you want to view disks. On the page that appears, click the
**Disks** tab.
5. Select a filter option from the drop-down list, enter the relevant information in the search
box, and then click **Search**. You can select multiple filter options to narrow down search results.

| Parameter | Description |
|---|---|
| Disk Name | The disk name used to search for the disk. |
| Disk ID | The disk ID used to search for the disk. |
| Disk Properties | The disk type used to search for disks of that type. Valid values: All System Disk Data Disk |

##### Detach a data disk

You can detach data disks. System disks cannot be detached.

**Warning**

Resources are released after disks are detached. Make sure that the data of a disk is backed up before you detach it.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Click the instance from which you want to detach a data disk. On the page that appears,
click the **Disks** tab.
5. Find the data disk that you want to detach and choose **More** > **Detach** in the **Actions**
column.
6. Click **OK**.

#### ENIs

##### Create an ENI

You can create and bind elastic network interfaces (ENIs) to VMware Cloud on Alibaba Cloud instances.

**Prerequisites**

ud on Alibaba Cloud A virtual private cloud (VPC) and a vSwitch are created. For more information, see Create a VPC and Create a vSwitch in Apsara Stack VPC User Guide.

**Background information**

ENIs are classified into primary and secondary ENIs. A primary ENI is created by default when an instance is created in a VPC. This primary ENI shares the lifecycle of the instance with which it is created and cannot be unbound from the instance. ENIs that are separately created are secondary ENIs. This topic describes how to create a secondary ENI.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Click the instance for which you want to create an ENI. On the page that appears, click the
**ENIs** tab.
5. Click **Create and Bind ENI**.
6. Configure parameters listed in the following table to create an ENI.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization in which to create the ENI. |
|   | Resource Set | Yes | The resource set in which to create the ENI. |
|   | Region | Yes | The region in which to create the ENI. |
|   | Zone | Yes | The zone in which to create the ENI. |
|   | VPC | Yes | The VPC in which to create the ENI. The secondary ENI can be bound only to an instance in the same VPC. Note After an ENI is created, its VPC cannot be changed. |

ud on Alibaba Cloud

| Section Basic Settings | Parameter | Required | Description |
|---|---|---|---|
|   | vSwitch | Yes | The vSwitch in which to create the ENI. The secondary ENI can be bound only to an instance within the same VPC. Select a vSwitch that is deployed within the same zone as the instance to which the ENI is bound. The vSwitch of the ENI can be different from that of the instance. Note After an ENI is created, you cannot change its vSwitch. |

7. Click **Submit**.

**Execution results**

The created ENI is displayed on the ENIs tab and is in the **Bound** state.

##### View ENIs

You can view the list of created elastic network interfaces (ENIs).
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Click the instance for which you want to view ENIs. On the page that appears, click the
**ENIs** tab.
5. Select a filter option, enter the corresponding information in the search box, and then click
**Search**.
You can select multiple filter options to narrow down search results.

| Parameter | Description |
|---|---|
| ENI Name | The ENI name used to search for the ENI. |
| ENI ID | The ENI ID used to search for the ENI. |

| sara Uni-manager Managemen |   |
|---|---|

ud on Alibaba Cloud

| Parameter | Description |
|---|---|
| VSwitch ID | The vSwitch ID used to search for the ENIs that are associated with the vSwitch. |

##### Delete an ENI

You can delete secondary elastic network interfaces (ENIs) that are no longer needed.

**Background information**

Only secondary ENIs can be deleted. Primary ENIs share the same lifecycle as instances and cannot be deleted.
1. Log on to the VMware Cloud on Alibaba Cloud console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, move the pointer over **Region** and select the region where
VMware Cloud on Alibaba Cloud is deployed.
4. Find the instance whose secondary ENI is to be deleted and click the **ENIs** tab.
5. Find the secondary ENI and click **Delete** in the **Actions** column.
6. Click **OK**.

## Enterprise

### Organizations

#### Create an organization

This topic describes how to create an organization. You can create organizations to store resource sets and their resources.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the left-side navigation tree, click a parent organization. On the page that appears, click
**Create Organization**.
5. In the **Add Organization** dialog box, enter an organization name and click **OK**.
6. **Optional:**If the multi-cloud management feature is enabled for the primary node, the
**Synchronously Create Multi-cloud Organization** check box is displayed after you click
**OK**.
Select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

#### Sort organizations

This topic describes how to sort organizations that belong to the same parent organization.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise** .
3. In the left-side navigation pane of the Enterprise page, click **Organizations**.
4. In the left-side organization tree, drag an organization to adjust its position in the tree.

**Note**

You can adjust the position only among organizations of the same level.

#### View organization information

You can view information of an organization on the Organizations page.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. **Optional:**Enter the name of the organization that you want to view in the search box above
the organization navigation tree. Fuzzy search is supported.
5. Click the name of the organization that you want to view.
You can click the **Resource Sets**, **Users**, or **User Groups** tab to query the resource sets, users, and user groups under the organization. Click the **Resource Sets** tab to view the resource set names, resource set IDs, creation time, creators, and user groups. Click the name of a resource set to view its details. Click the **Users** tab to view the usernames, user status, and roles. Click a username to view the user details. Click the **User Groups** tab to view the user group names, corresponding organizations, roles, users, and creation time. Click icons in the upper-right corner of the **Resource Sets**, **Users**, and **User Groups** tabs to perform the following operations on the lists:

| Icon | Description |
|---|---|
|   | Shows the list in full screen mode. You can click the icon in the upper- right corner to exit the full screen mode. |
|   | Selects the size of cells and fonts in the list. Valid values: Default Compact |
|   | Refreshes the list. |
|   | Selects or clears check boxes to determine the items to be displayed in the list. You can also click Reset to restore the list to its original settings. |

#### Change the name of an organization

Users that have operation permissions on an organization can change the name of the organization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. **Optional:**Enter the organization name in the search box for fuzzy search above the
organization tree.
5. Click the organization name that you want to change.
6. In the upper-right corner of the page, click **Editing**.
7. In the Edit Organization dialog box, change the organization name.
8. Click **OK**.

#### Change organization ownership

Users that have operation permissions on an organizations can change the ownership of the organization.

**Prerequisites**

Make sure that each sub-organization under the organization that you want to change the ownership has a unique name. The ownership of an organization cannot be changed across level-1 organizations.

**Background information**

Users can change the ownership of an organization across parent organizations. This way, the ownership of subordinate organizations, users, and resources are also changed in a cascading manner.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, choose **Resources > Changes**.
4. **Optional:**Enter the name of the organization that you want to change in the search box
above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the organization whose ownership you want to change.
6. Click **Change Organization** on the right side of the page.
7. In the **Change Organization To** dialog box, select a new organization and click **OK** to
change the ownership of the original organization along with that of its resources sets and users.

#### Obtain AccessKey pairs of an

**organization**

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption. This helps you verify the identity of a requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain AccessKey pairs of an organization.

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs of an organization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization navigation tree, click the name of the level-1 organization for which you
want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the Management AccessKey dialog box, view the AccessKey pairs of the organization.

#### Create an AccessKey pair for an

**organization**

You can create AccessKey pairs for organizations and delete the original ones to implement the rotation of your AccessKey pairs.

**Prerequisites**

Level-1 organization administrators can create AccessKey pairs for organizations to which they belong. Operations administrators can create AccessKey pairs for all level-1 organizations. A maximum of two AccessKey pairs can be created for each organization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. (Optional) Enter the name of the organization for which you want to create an AccessKey
pair in the search box above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the level-1 organization for which you want to create an AccessKey pair.
6. Click **Management AccessKey** on the right side of the page.
7. In the **Management AccessKey** dialog box, click **Create AccessKey**.

#### Delete an AccessKey pair from an

**organization**

You can delete AccessKey pairs that are no longer needed.

**Prerequisites**

Level-1 organization administrators can delete AccessKeys from organizations to which they belong. Operations administrators can delete AccessKey pairs from all level-1 organizations. At least one AccessKey pair is retained for an organization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. (Optional) Enter the name of the organization from which you want to delete an AccessKey
pair in the search box above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the level-1 organization from which you want to delete an AccessKey pair.
6. Click **Management AccessKey** on the right side of the page.
7. In the **Management AccessKey** dialog box, find the AccessKey pair that you want to
delete and click **Delete** in the **Operation** column.
8. In the message that appears, click **OK**.

#### Disable an AccessKey pair for an

**organization**

You can disable AccessKey pairs that are no longer needed. Newly created AccessKey pairs are in the Enable state by default.

**Prerequisites**

Level-1 organization administrators can disable AccessKey pairs for organizations to which they belong. Operations administrators can disable AccessKey pairs for all level-1 organizations. At least one AccessKey pair is enabled for each level-1 organization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. (Optional) Enter the name of the organization for which you want to disable an AccessKey
pair in the search box above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the level-1 organization for which you want to disable an AccessKey pair.
6. Click **Management AccessKey** on the right side of the page.
7. Find the AccessKey pair that you want to disable and click **Disable** in the **Operation**
column.
8. In the message that appears, click **OK**.

#### Enable an AccessKey pair for an

**organization**

Disabled AccessKey pairs must be enabled before they can be used. Newly created AccessKey pairs are in the Enable state by default.

**Prerequisites**

Level-1 organization administrators can enable AccessKey pairs for organizations to which they belong. Operations administrators can enable AccessKey pairs for all level-1 organizations.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. (Optional) Enter the name of the organization for which you want to enable an AccessKey
pair in the search box above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the level-1 organization for which you want to enable an AccessKey pair.
6. Click **Management AccessKey** on the right side of the page.
7. Find the AccessKey pair that you want to enable and click **Enable** in the **Operation**
column.

#### Delete an organization

Administrators can delete organizations that are no longer needed.

**Prerequisites**

Before you delete an organization, make sure that the organization does not contain users, resource sets, or subordinate organizations. Otherwise, the organization cannot be deleted.

**Warning**

After the organization is deleted, the data of the organization cannot be recovered. Proceed with caution.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. **Optional:**Enter the name of the organization that you want to delete in the search box
above the organization navigation tree. Fuzzy search is supported.
5. Click the name of the organization that you want to delete.
6. Click **Delete** on the right side of the page.
7. In the Confirm message, click **OK**.

### Resource sets

#### Create a resource set

This topic describes how to create a resource set. Before you apply for resources, you must create a resource set.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Resource Sets**.
4. Click **Create Resource Set**.
5. In the **Create Resource Set** dialog box, configure the **Name** and **Organization**
parameters.
6. Click **OK**.

#### View the details of a resource set

When you want to use a cloud resource in your organization, you can view the details of the resource set that contains the resource, including all resource instances and users of the resource set.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Resource Sets**.
4. **Optional:**Select an **organization** from the drop-down list, or enter a **resource set** name
in the search box, and then click **Search**.
5. Click the name of the resource set.
6. On the **Resource Set Details** page, click the **Resources** and **Users** tabs to view all
resource instances and users of the resource set.
7. On the **Resources** tab, click the number next to a resource in a service card. You are
redirected to the instance list page. On the page that appears, view the details of the instance list. The list is automatically filtered and displayed based on the organization and resource set.

#### Change the name of a resource set

You can change the name of a resource set to keep it up-to-date as an administrator.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Resource Sets**.
4. **Optional:**Select an **organization** from the drop-down list, or enter a **resource set** name
in the search box, and then click **Search**.
5. Find the resource set that you want to change and click **Edit Name** in the **Actions** column.
6. In the **Modify Resource Set** dialog box, enter a new name.
7. Click **OK**.

#### Add a member to or delete a member

**from a resource set**

You can add a member to or delete a member from a resource set to manage member access to resources in the resource set. A member can be a user or a user group.

**Prerequisites**

A resource set is created. For more information, see Create a resource set. A user is created. For more information, see Create a user. A user group is created. For more information, see Create a user group.

**Background information**

Members of a resource set have the permissions to use resources in the resource set. If you delete resources from a resource set, members of the resource set are not affected. Similarly, If you delete members from a resource set, resources in the resource set are not affected. You can delete a member that is no longer in use from a resource set. After a member is deleted, the member is no longer able to access the resource set.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Resource Sets**.
4. **Optional:**Select an **organization** from the drop-down list, or enter a **resource set** name
in the search box, and then click **Search**.
5. Find the resource set that you want to manage and click **Member authorization** in the
**Actions** column.
6. **Optional:**In the **Member authorization** dialog box, select the role type of the user or the
user group that you want to add.
7. Add or delete a member.
Add a user or a user group: In the lower-left section, select the user or the user group that you want to add. Delete a user or a user group: In the lower-right section, click **Remove** in the **Operation** column.
8. Click **OK**.

#### Delete a resource set

You can delete resource sets that are no longer needed as an administrator.

**Prerequisites**

The resource set to be deleted does not contain resources, users, or user groups.

**Important**

A resource set cannot be deleted if it contains resources, users, or user groups. The default resource set cannot be deleted.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Resource Sets**.
4. Find the resource set that you want to delete and click **Delete** in the **Actions** column.
5. In the **Confirm** message, click **OK**.

### Roles

#### Create a custom role

You can create custom roles in the Apsara Uni-manager Management Console to more efficiently grant permissions to users so that different personnel can work with different features.

**Background information**

A role is a set of access permissions. Each role has a range of permissions. A user can have multiple roles, which means that the user is granted all the permissions defined for the roles. A role can be used to grant the same set of permissions to a group of users. The total number of custom and default roles cannot exceed 20.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Click **Create Custom Role** in the upper-left corner of the page.
5. In the **Basic configuration** step, set Role name, Description, Sharing Scope, and
Management Permissions. Click **Next**. The following table describes the role parameters. Table 1. Role parameters

| Paramet er | Description |
|---|---|
| Role name | The name of the role. The name can be up to 64 characters in length and can contain only letters and digits. |
| Descripti on | Optional. The description of the role. The description can be up to 500 characters in length and can contain letters, digits, commas (,), semicolons (;), and underscores ( ). _ |
| Sharing Scope | Global: This role is visible and valid for all organizations. |
| Manage ment Permissi ons | All Organizations These permissions apply to all organizations involved. Specified Organization and Subordinate Organizations These permissions apply to the organization to which the user belongs and its subordinate organizations. Resource Sets These permissions apply to the resource sets that are assigned to the user. |

6. In the **Manage permissions** step, select the operation permissions of this role in the
Apsara Uni-manager Operations Console and click **Next**. You can click permission categories on the left side to filter permissions.
7. In the **Application permissions** step, select the operation permissions of this role on
cloud products. Click **Next**. You can click application names on the left side to filter application permissions.
8. In the **Menu permissions** step, select the operation permissions of this role on menus and
homepage dashboard templates corresponding to the role, and click **Next**. You can click the parent menu on the left side to filter permissions on cascading menus.

**Result**

After the role is created, you can click **Authorize now** in the Submission result message to authorize users or user groups. You can also authorize users or user groups on the details page of the role.

#### View the details of a role

If you are uncertain about the specific permissions of a role, you can go to the **Role**
**Authorization** page to view the role permissions.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Click the name of the role that you want to view. On the **Role Authorization** page, view
the information of the role. You can click the **Management Permissions**, **Application Permissions**, **Menu**
**Permissions**, and **Authorized Personnel** tabs to view the role permissions.

#### Modify information about custom roles

This topic describes how to modify information about custom roles. You can modify the name and the permissions of a custom role as an administrator.

**Background information**

You cannot modify information about system roles.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. In the role list, find the custom role whose information you want to modify and click **Modify**
in the **Actions** column.
5. On the **Role authorization** page, modify the name, description, management permission
scope, related permissions, and authorized personnel of the role. Modify the basic information of the role: Click **Modify Basic Information** to modify the name, description, and management permissions of the role. After the modification is complete, click **OK**. Modify permissions: Click the **Management Permissions**, **Application Permissions**, or **Menu Permissions** tab, select or clear related permissions on the corresponding tab, and then click **Update**. Authorize users to assume the role: Click the **Authorized Personnel** tab. In the
**Authorized User** section, click **Authorized**. In the dialog box that appears, select the
users that you want to authorize and click **Confirm authorization**. To cancel authorization from a user, click **Remove** in the **Operation** column. Authorize user groups to assume the role: Click the **Authorized Personnel** tab. In the
**Authorized User Group** section, click **Authorized**. In the dialog box that appears,
select the user groups that you want to authorize and click **Confirm authorization**. To cancel authorization from a user group, click **Remove** in the **Operation** column.

#### Copy a role

You can copy a preset role or a custom role to create a role that has the same permissions.

**Background information**

Operations on the **Role authorization** page are the same as those for creating a custom role. You can add, modify, and remove the role permissions in the copied role. By default, if you do not modify the role permissions, the sharing scope, management permissions, application permissions, menu permissions, and authorized users are all the same as those of the source role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. In the role list, choose
> **Copy** in the **Actions** column corresponding to a role.
5. On the **Create Custom Role** page, set the new role name, sharing scope, and
management permissions.

**Note**

The role name must be unique.
6. Complete the basic configurations of the new role, Click **Next**.
7. In the **Manage permissions** step, select the operation permissions that the new role has
on the Apsara Uni-manager Management Console, Click **Next**.
8. In the **Application permissions** step, select the operation permissions that the new role
has on cloud services, Click **Next**.
9. In the **Menu permissions** step, select the operation permissions that the new role has on
menus, and click **Create Role**. and click **Next**.

**Result**

After the role is created, you can click **Authorize now** in the Submission result message to authorize users or user groups. You can also authorize users or user groups on the details page of the role.

#### Disable a role

When you disable a role, all of its permissions are also disabled.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. In the role list, find the role that you want to disable and click **Disable** in the **Actions**
column.

#### Enable a role

When you enable a disabled role, the permissions of the role are restored.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. In the role list, find the role that you want to enable and click **Enable** in the **Actions**.

#### Delete a custom role

This topic describes how to delete a custom role. You can delete custom roles that you no longer require.

**Prerequisites**

Default or preset roles cannot be deleted. Before you delete a role, you must unbind all user groups from the role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. In the role list, find the role that you want to delete and choose
> **Delete** in the **Actions**
column.
5. In the message that appears, click **OK**.

### Users

#### System users

##### Create a user

You can create a user and assign the user different roles as an administrator to meet different requirements for system access control.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab. Click **Create a user**.
5. In the dialog box that appears, set the following parameters.

| Parameter | Required | Description |
|---|---|---|
| User name | Yes | The Apsara Stack tenant account name of the user. The name must be 1 to 64 characters in length and can contain letters, digits, hyphens (-), underscores ( ), and _ periods (.). |
| Display name | Yes | The display name of the user. The name must be 1 to 128 characters in lengthand can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). _ |
| Role | Yes | The role to be assigned to the user. Note You can enter role names in the field. Fuzzy match is supported. |
| Tissue | Yes | The organization to which the user belongs. |
| Logon policy | Yes | The logon policy that restricts the logon time and IP addresses of the user. The default policy is automatically bound to new users. Note The default policy does not restrict the logon time and IP addresses of the user. To restrict the allowed logon time and IP addresses of the user, you can modify the logon policy of the user or create a logon policy for the user. For more information, see Create an access policy. |
| Phone | Yes | The mobile number of the user. This mobile number is used to notify users of resource application and usage. Make sure that this mobile number is valid. Note If the mobile number of the user changes, update it on the system in a timely manner. |
| Landline | No | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | Yes | The email address of the user. Emails about the resource application and usage are sent to this email address. Make sure that this email address is valid. Note If the email address changes, update it on the system in a timely manner. |

| DingTalk Key | No | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |
|---|---|---|
| Notify User by Email | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
| Notify User by DingTalk | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

6. Click **OK**.

##### Query a user

You can view user information such as the name, organization, mobile number, email address, role, logon time, and initial password.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Enter a **username** in the search box or select an **organization** to view users of the
organization. You can also click **Advanced** on the right side and select a role and MFA status or enter a display name to search for the user that you want to query.
6. Click the username to view the basic information and the resource sets to which it belongs.

##### Modify user information

You can modify user information such as the display name, mobile number, and email address to keep it up to date.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Find the user that you want to modify and click **Edit** in the **Actions** column.
6. In the **Edit User** dialog box, modify the relevant information and click **OK**.

##### Change user roles

You can add, change, and delete roles for a user.

**Change user roles by using user management**

**Cageuse**

**oesbyus**

**guse**

**aage**

**e**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Find the user that you want to modify and choose
> **Authorize** in the **Actions** column.
6. In the **Role** field, add, delete, or change user roles.
You can enter role names in this field. Fuzzy match is supported.
7. Click **OK**.

**Change user roles by changing ownership**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Changes**.
4. Click the
icon to the left of the organization that you want to manage and click **Users**.
5. In the right-side **Users** section, specify a **logon policy**, a **role**, or a **username**. Then, click
**Search** to find the user that you want to change.
6. Find the user and click **Change** in the **Actions** column.
7. In the **Organization to Change** dialog box, select the original or a new organization and
select the role to be added or removed from the **Assigned Roles** drop-down list.

**Note**

If you change only roles without changing the organization, select the original organization.
8. Click **Modify**.

##### Modify the information about a user group

This topic describes how to modify the information about a user group. On the **Users** page, you can view the information of user groups and modify the ownership of users in user groups.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab, select the user that you want to modify and click the
image in the **Actions** column. Select **Add to User Group**. In the dialog box that appears, select a user group and click
**OK** to add the user to the user group.
Select **Remove from User Group**. In the dialog box that appears, select a user group and click **OK** to remove the user from the user group.

##### Modify a user logon policy

This topic describes how to modify a user logon policy. An administrator can modify a user logon policy to restrict the logon time and IP addresses of users.

**Prerequisites**

A logon policy is created. For more information, see Create an access policy.

**Modify a user logon policy**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Modify one or more user logon policies.
If you modify only one user logon policy, perform the following steps: a. Find the user whose logon policy that you want to modify and choose
> **Configure**
**Logon Policy** in the **Actions** column.
b. In the **Assign Logon Policy** dialog box, select a new logon policy and click **OK**. If you modify multiple user logon policies at the same time, perform the following steps: a. Select users whose logon policies that you want to modify. b. In the lower-left corner of the page, click **Configure Logon Policy**. c. In the **Batch Assign Logon Policy** dialog box, select a new logon policy and click **OK**.

##### View the initial password of a user

After a user is created, the system generates an initial password for the user.

**Background information**

Organization administrators can view the initial passwords of all users in the organizations they manage.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Find the user that you want to manage and choose
> **View Initial Password** in the
**Actions** column.

**Note**

After the initial password is changed, the initial password is not displayed.

##### Reset the password of a user

If users forget their logon passwords, the organization administrator can reset the logon passwords for them.

**Prerequisites**

Only organization administrators can reset the password of a user.
1. Log on to the Apsara Uni-manager Management Console as an organization administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the user for which you want to reset the password.
5. In the **User Information** panel, click **Reset password**.
After the password is reset, a message is displayed, which indicates that the password has been reset.

##### Disable or enable a user account

You can disable a user account to prevent the user account from logging on to the Apsara Uni-manager Management Console. User accounts that are disabled must be re-enabled before they can be used to log on to the Apsara Uni-manager Management Console again.

**Background information**

By default, user accounts are enabled when they are created.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Perform the following operations on the current tab:
Find the user whose **Status** is **Enabled** and which you want to disable, click **Disable** in the **Actions** column. In the dialog box prompting you the risks of disabling the user, select the **I have known the risks and confirm this operation** check box and click
**Disable**.
Find the user whose **Status** is **Disabled** and which you want to re-enable, click **Enable** in the **Actions** column. In the dialog box prompting you the risks of enabling the user, click **OK**.

##### Delete a user

You can delete a specific user as an administrator.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **System Users** tab.
5. Find the user that you want to delete and choose
> **Delete** in the **Actions** column.
6. In the dialog box prompting you the risks of deleting, select the **I have known the risks**
**and confirm this delete operation** check box and click **Delete**.

#### Historical users

##### Query deleted users

This topic describes how to query deleted users.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **Historical Users** tab.
5. Search historical users by username. Fuzzy search is supported.

##### Restore historical users

An administrator can restore a deleted user account from the **Historical Users** tab.

**Background information**

The basic information such as the logon password of a restored user is the same as it was before the user was deleted, except for its organization and role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Click the **Historical Users** tab.
5. Find the user that you want to restore and click **Restore** in the **Actions** column.
6. In the **Restore User** dialog box, select an organization and a role.
7. Click **OK**.

### Access control management

#### Create an access policy

To improve the security of the Apsara Uni-manager Management Console, you can create an access policy as an administrator to control logon access based on the logon time and IP addresses of users.

**Background information**

Access policies are used to control the time periods and IP addresses valid for user logon. After a user is bound to an access policy, user logons are limited based on the logon time and IP addresses specified in the policy. The default policy generated by the Apsara Uni-manager Management Console does not have limits on the time and IP addresses valid for user logon. This policy cannot be deleted.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Click **Create an access policy** in the upper-right corner.
5. In the **Create an access policy** dialog box, set Name, Sharing Scope, Policy Property,
Logon Time, and Logon Address. Table 1. Parameters for creating an access policy

| Parameter | Description |
|---|---|
| Name | The name of the access policy. The name must be 2 to 50 characters in length and can contain only letters and digits. The name must be unique in the system. |
| Description | The description of the access policy. |
| Sharing Scope | The scope in which the role is visible. Valid values: Global: The role is globally visible. The default value is Global. Current Organization: The role is visible only in the current organization and is invisible in subordinate organizations. Subordinate Organization: The role is visible in the current organization and all its subordinate organizations. |
| Policy Property | The authentication method of the access policy. Valid values: Whitelist: Logon is allowed if the parameter settings are met. Blacklist: Logon is denied if the parameter settings are met. |

| Logon Time | The permitted logon time period. If this policy is configured, users can log on to the Apsara Uni-manager Management Console only within the configured period. Specify the time period in minutes in a 24-hour clock. Example: 16:32 . Note When the Policy Property parameter is set to Whitelist, you can select No Time Limit. |
|---|---|
| Logon Address | The permitted CIDR block. If the Policy Property parameter is set to Whitelist, IP addresses within this CIDR block are allowed to log on to the Apsara Uni-manager Management Console. If the Policy Property parameter is set to Blacklist, IP addresses within this CIDR block are not allowed to log on to the Apsara Uni-manager Management Console. Note When the Policy Property parameter is set to Whitelist, you can select No CIDR Block Limit. |

6. Click **OK**.

#### Query access policies

This topic describes how to query access policies. You can query the details of an access policy in the Apsara Uni-manager Management Console.

**Background information**

When the Apsara Uni-manager Management Console provides services, the console automatically generates a default policy that does not have limits on the logon time and IP addresses.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Enter the name of the policy that you want to view and click Search.
View the access policy, including the permitted logon time and IP addresses. The following table describes the icons in the upper-right corner that you can click to manage the access policy list.

| Icon | Description |
|---|---|
|   | Shows the list in full screen mode. You can click the icon in the upper- right corner to exit the full screen mode. |
|   | Selects the size of cells and fonts in the list. Valid values: Default Compact |

|   | Refreshes the list. |
|---|---|
|   | Selects or clears check boxes to specify the items that you want to display in the list. You can also click Reset to restore the list to the default settings. |

#### Modify a logon policy

You can modify the policy name, policy properties, permitted logon time period, and IP addresses of a logon policy.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Find the policy that you want to modify and click **Modify** in the **Actions** column.
5. In the **Modify an access policy** dialog box, modify the information of the policy.
6. Click **OK**.

#### Disable an access policy

You can disable access policies that are no longer needed.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Find the access policy that you want to disable and click **Disable** in the **Actions** column.
5. In the message that appears, click **OK**.

#### Enable a logon policy

You can re-enable disabled logon policies.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Find the policy that you want to enable and click **Enable** in the **Actions** column.

#### Delete an access policy

You can delete access policies that are no longer needed.

**Prerequisites**

The access policy to be deleted is not bound to users. If an access policy is bound to a user, the access policy cannot be deleted.

**Background information**

**Note**

The default policy cannot be deleted.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Permission Policies**.
4. Find the policy that you want to delete and click **Delete** in the **Actions** column.
5. In the message that appears, click **OK**.

### User groups

#### Create a user group

You can create a user group in a selected organization and batch authorize users within the group.

**Prerequisites**

An organization is created. For more information, see Create an organization.

**Background information**

Relationships between user groups and users: A user group can contain zero or more users. A user does not need to belong to a user group. You can add a user to multiple user groups. Relationships between user groups and organizations: A user group belongs to only a single organization. You can create multiple user groups within an organization. Relationships between user groups and roles: A role can be assigned to multiple user groups. When a role is assigned to a user group, the permissions that the role has are automatically granted to users within the user group. Relationships between user groups and resource sets: You can add zero or more user groups to a resource set. A user group can be added to multiple resource sets.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Click **Create a user group** in the upper-left corner.
5. In the dialog box that appears, set **User Group Name**, **Tissue**, and **Role authorization**.

| Parameter | Description |
|---|---|
| User Group Name | The name of the user group. The name must be 3 to 255 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods _ (.), and at signs (@). |
| Tissue | The organization to which the user group belongs. |
| Role authorization | The roles that are assigned to the user group. |

6. Click **OK**.

#### Add users to a user group

You can add users to a user group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Find the user group to which you want to add users and click **Add User** in the **Actions**
column.
5. Select users to be added in the left-side section and click the right arrow to move them to
the right-side section.
6. Click **OK**.

#### Remove a user

You can remove users from a user group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Find the user group from which you want to remove a user, click
in the **Actions** column, and choose **Remove User**.
5. Select the user that you want to remove in the **Users under the user group** section and
click the icon to move the user to the **Remove User** section.
6. Click **OK**.

#### Add or remove a role

You can add a role to a user group to grant the role permissions to all users within the group. You can also remove a role from a user group to revoke the role permissions from all users within the group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Find the user group that you want to manage and choose
**Authorized** in the **Actions**
column.
5. In the **Authorized** dialog box, set **Role authorization**.
6. In the drop-down list, you can select or clear a role to grant permissions to or revoke
permissions from the user group.
7. Click **OK**.

#### Modify the name of a user group

You can modify the names of user groups.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Find the user group that you want to modify and click **Editing** in the **Actions** column.
5. In the dialog box that appears, modify **User Group Name**.
6. Click **OK**.

#### Delete a user group

This topic describes how to delete a user groups. You can delete user groups that you no longer require.

**Prerequisites**

Before you delete a user group, you must unbind the user group from all roles. Otherwise, the user group cannot be deleted.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > User Groups**.
4. Find the user group that you want to delete and choose
> **Delete** in the **Actions**
column.
5. In the message that appears, click **OK**.

### Region management

#### Update associations

The Apsara Uni-manager Management Console allows you to manage resources across regions. You can update the associations between organizations and regions.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Regions**.
4. In the left-side organization navigation tree, click the name of the organization that you
want to update.
5. In the right-side **Regions** section, select the names of regions to be associated.
6. Click **Update Association**.

### Change the ownership of an

**instance**

If you want to transfer resource instances to another resource set within the same organization, you can change the resource set ownership of the instances.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Changes**.
4. Click the
icon to the left of the organization that you want to manage and click a resource set.
5. In the right-side **Product Type** section, click the name of the service that contains the
instance you want to manage.
6. Set **Resource Type**, enter the instance ID or name in the search box, and then click
**Search** to search for the instance.
7. Click **Change Ownership** in the **Actions** column corresponding to the instance to change
the ownership of the instance to another resource set.
8. In the **Change Resource Set** dialog box, select the desired resource set and click **OK**.

### Cloud instances

#### Manage Apsara Stack cloud instances

##### Export data of the current cloud

You can export the data of secondary Apsara Stack nodes to a configuration file. This can be used by the primary node to manage nodes in a centralized manner.

**Procedure:**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **Apsara Stack Management** tab.
5. Click **Collect Data of Current Cloud** to collect the deployment information of the current
cloud.
6. Click **Export** to export the information in the JSON format.

##### Add a secondary Apsara Stack node

You can add the configuration information of secondary Apsara Stack nodes to the multi-cloud configuration of the primary Apsara Stack node for centralized management.

**Procedure:**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **Apsara Stack Management** tab.
5. Click **Import**.
6. In the **Create Apsara Stack Secondary Node** dialog box, enter the configuration
information of a secondary node and click **OK**.

| Parameter | Description |
|---|---|
| Cloud Instance Information | The configuration file of the secondary node. For more information, see Export data of the current cloud. |
| Secondary Node Name | The name of the secondary node. |
| Username | The username of the operations administrator that manages the secondary node. |
| Password | The password of the operations administrator that manages the secondary node. |
| Description | The description of the secondary node. |

|   |   | Apsara Uni-manager Manageme t Console User Guide·Enterpris | n e |
|---|---|---|---|

| Parameter | Description |
|---|---|
| AccessKey ID | The AccessKey ID of the operations administrator that manages the secondary node. For more information, see View the AccessKey pair of your Apsara Stack tenant account. |
| AccessKey Secret | The AccessKey secret of the operations administrator that manages the secondary node. For more information, see View the AccessKey pair of your Apsara Stack tenant account. |

**Important**

You must create an operations administrator account in the secondary node. This account is for dedicated use by the primary node and cannot be the default operations administrator account.

##### View managed cloud instances

You can use the multi-cloud management feature to view the details of all managed cloud instances.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **Apsara Stack Management** tab.
You can view the name, description, cloud type, cloud role, and address of all managed cloud instances.
5. Enter a cloud instance name in the search box and click **Search** to search for the cloud
instance.
6. Click **View Details** in the **Actions** column corresponding to the cloud instance.
In the Manage Cloud Instance message, you can view the version, Apsara Stack API (ASAPI) address, and region of the cloud.

##### Modify a cloud instance

If you want to change the information of a cloud instance for more efficient management, you can modify it in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **Apsara Stack Management** tab.
5. Enter the name of the cloud instance that you want to modify in the search box and click
**Search** to search for the cloud instance.
6. Click **Edit** in the **Actions** column corresponding to the cloud instance.
7. In the **Edit Cloud Instance** dialog box, set **Cloud Name**, **Username**, **Password**,
**Description**, **AccessKey ID**, **AccessKey Secret**, **Longitude**, and **Latitude**, and click **OK**.

##### Manage cloud instances

You can manage Apsara Stack cloud instances to check whether they can be connected.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **Apsara Stack Management** tab.
5. Enter a cloud instance name in the search box and click **Search** to search for the cloud
instance.
6. Click **Manage** in the **Actions** column corresponding to the cloud instance.
7. In the **Manage Cloud Instance** dialog box, click **Test Connectivity**.

#### Manage VMware nodes

##### Add a VMware node

You can add the configuration information of VMware nodes to the Apsara Stack VMware management configuration for centralized management.

**Prerequisites**

The configuration file of a VMware node is obtained from the deployment personnel. The VMware node is configured.

**Procedure:**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **VMware Management** tab.
5. Click **Create VMware Node**.
6. In the **Create VMware Node** dialog box, enter the configuration information of a VMware
node and click **OK**.

| Parameter | Description |
|---|---|
| Cloud Instance Information | The configuration file of the VMware node. |
| Cloud Name | The name of the VMware node. |
| Cloud Description | The description of the VMware node. |
| AccessKey ID | The AccessKey ID in the configuration file of the VMware node. |
| AccessKey Secret | The AccessKey secret in the configuration file of the VMware node. |

##### Modify a VMware node

If you want to change the information of a VMware node for more efficient management, you can modify it in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **VMware Management** tab.
5. Enter the name of the VMware node that you want to modify in the search box and click
**Search** to search for the VMware node.
6. Click **Edit** in the **Actions** column corresponding to the VMware node.
7. In the **Edit Cloud Instance** dialog box, set **Cloud Name**, **Cloud Description**, **AccessKey**
**ID**, and **AccessKey Secret**, and click **OK**.

##### Test VMware node connectivity

You can manage VMware nodes to check whether they can be connected.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the Enterprise page, click **Cloud Instances**.
4. Click the **VMware Management** tab.
5. Enter a VMware node name in the search box and click **Search** to search for the VMware
node.
6. Click **Manage** in the **Actions** column corresponding to the VMware node.
7. In the **Manage Cloud Instance** dialog box, click **Test Connectivity**.

### Data permissions

#### Overview

Data permission management allows you to specify which users can access instances of a specific service, grant data access permissions to the users, and view and modify the data permissions in all the RAM policies attached to specified users. Apsara Stack controls users and permissions by managing their visibility and operability in the Apsara Uni-manager Management Console. Many Apsara Stack cloud services are directly used by calling their API operations or SDKs instead of in the console. In this case, data access permissions must be controlled by RAM permission verification provided by the cloud services. RAM policies are configured for such cloud service instances for access control. Automatic judgment is used when personnel are added to or removed from resource sets. However, this judgement method can affect performance and has a high error rate in complex scenarios. To solve this problem, the authorization of cloud services that require data access permissions is separately managed. Organization administrators can configure the data permissions granted to related personnel on the data authorization page.

#### Set the data permissions of resource

#### instances

Organization administrators can set the data permissions of resource instances to allow or deny access to and operations on cloud services in the Apsara Uni-manager Management Console.

**Prerequisites**

The cloud services that support data authorization include Message Queue (MQ), Object Storage Service (OSS), Log Service, DataHub, Container Service for Kubernetes, and Key Management Service (KMS).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Data Permissions**.
4. Click the resource set that you want to manage and click a service type on the right side of
the page.
5. Find the instance that you want to manage and click **Authorize** in the **Actions** column.
6. In the **Data Authorization** dialog box, select the user that you want to manage on the left
side.
7. Turn on or off the data permission switches in the Actions column on the right side.
You can also select or clear Enable All to batch manage permissions.
8. Click **OK**.

#### Edit user permissions

You can use JSON statements to edit user permissions.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Data Permissions**.
4. In the organization navigation tree, click the
icon to the left of the organization that contains the user you want to manage.
5. Click **Users**.
6. Enter the username in the search box and click **Search**.
7. Click **Edit Permissions** in the **Actions** column corresponding to the user.
8. In the Edit Permissions dialog box, select a data permission on the left side and click OK.
If no permissions are available, specify a policy in the text editor. For more information about the syntax and structure of a policy, see Permission policy structure and syntax.

#### View the permissions of a user

You can view the existing permissions of a user.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Data Permissions**.
4. In the organization navigation tree, click the
icon to the left of the organization that contains the user you want to manage.
5. Click **Users**.
6. Enter the username in the search box and click **Search**.
7. Click **View Permissions** in the **Actions** column corresponding to the user.
ons

## Configurations

### Security policies

#### Configure password policies

You can configure password policies for user logons.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Security Policies**.
4. Click the **Password Policy** tab.
5. On the **Password Policy** tab, set the password policy parameters.

| Parameter | Description |
|---|---|
| Password Length | The minimum length of the password. Minimum value: 8. |
| Required Character Types in Password | The character types that must be contained in the password. You can select multiple options. |
| Logon Disabled After Password Expires | Specifies whether to allow logon after the password expires. |
| Password Validity (Days) | The validity period of the password. Unit: days. Maximum value: 1095. A value of 0 indicates that the password never expires. |
| Password Attempts | The maximum number of logon attempts within 1 hour. Maximum value: 32. After the maximum number is reached, the account is locked and cannot be used to log on for a specific period of time. |

ons

| Password History Check | The number of previous passwords that cannot be reused. Maximum value: 24. A value of 0 indicates the password history check is disabled. |
|---|---|

6. Click **Save**.
To restore to the default password policy, click **Reset**.

#### Configure logon control

This topic describes how to configure logon control. You can limit access from multiple clients of users.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Security Policies**.
4. Click the **Logon Control** tab.
5. You can configure the following parameters:
**Session Mode**: Select one of the following values based on your business requirements:
**Single Session**: A user can log on only by using a single client at the same time.
**Multi-session**: A user can log on by using multiple clients at the same time.
**Global MFA**: Enable or disable the Global Multi-factor Authentication (MFA) feature based
on your business requirements. For information about the MFA feature, see Overview.
**Logon Minutes During Which No Actions Occur**: Adjust the slider to select a duration
based on your business requirements. If you do not trigger the relevant feature within the specified duration, you are forced to log off, and you must log on again.
**Logon Hours Before Forced Logoff** : Adjust the slider to select a duration based on
your business requirements. Within the specified duration, the system prompts and forces you to log off, and you must log on again. A value of 0 specifies that this feature is disabled. After the configuration is complete, click **Save**.

### Menus

#### Create a menu

You can create a menu and add its URL to the Apsara Uni-manager Management Console for quick access.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Menu Settings**.
4. On the **Main Menu** page, click **Create** in the upper-right corner.
5. In the **Create** dialog box, configure the menu parameters.
Table 1. Menu parameters

| Parameter | Description |
|---|---|

ons

| Title | The display name of the menu. |
|---|---|
| URL | The URL of the menu. |
| Console Type | Different console types correspond to different domain names. Valid values: oneconsole: You need only to enter the path in the URL field. The domain name is automatically matched. The URL starts with one.console . asconsole: You need only to enter the path in the URL field. The domain name is automatically matched. The URL starts with asc. . asconsole 2.0: You need only to enter the path in the URL field. The domain name is automatically matched. The URL starts with one.console . other: You must enter the domain name in the URL field. |
| Icon | The icon displayed in the left-side navigation pane. The icon cannot be changed. |
| Identifier | The unique identifier of the menu in the system. This identifier can be used to indicate whether the menu is selected in the navigation bar. The identifier cannot be changed. |
| Sort | The display order among the same-level menus. The larger the value, the lower the display order. Leave the Order field empty. |
| Parent Level | The displayed tree structure. |
| Open With | Specifies whether to open the menu in the current window or in a new window. |
| Description | The description of the menu. |

6. Click **OK**.

#### Modify a menu

You can modify an existing menu, including the menu name, URL, icon, and menu order.

**Prerequisites**

Default menus cannot be modified.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Menu Settings**.
4. Find the menu that you want to modify and click **Edit** in the **Actions** column.
5. In the **Edit** dialog box, modify the information of the menu.
For information about the menu parameters, see Create a menu.
6. Click **OK**.

#### Delete a menu

You can delete menus that are no longer needed. ons

**Prerequisites**

Default menus cannot be deleted.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane of the **Configurations** page, click **Menu Settings**.
4. Find the menu that you want to delete and click **Delete** in the **Actions** column.
5. In the message that appears, click **OK**.

#### Show or hide menus

You can perform the following operations to show or hide menus:
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane of the **Configurations** page, click **Menu Settings**.
4. Select or clear the check box in the **Displayed** column corresponding to a menu.

### Specifications

#### Specification parameters

This topic describes the specification parameters of each resource type.

**NAT Gateway**

| Parameter | Description |
|---|---|
| Specifications | The specifications that can be configured for NAT Gateway. |
| Specifications Description | The description of the specifications that can be configured for NAT Gateway. |

**AnalyticDB for PostgreSQL**

| Parameter | Description |
|---|---|
| Specifications | The specifications that can be configured for AnalyticDB for PostgreSQL. |
| Specifications Name | The name of the instance type that can be configured for AnalyticDB for PostgreSQL. |
| CPU | The total number of CPU cores that can be configured for AnalyticDB for PostgreSQL. |
| Memory | The memory size that can be configured for AnalyticDB for PostgreSQL. |

ons

| Storage Space | The total storage size that can be configured for AnalyticDB for PostgreSQL. |
|---|---|
| Version | The version number of AnalyticDB for PostgreSQL. |
| Node | The number of nodes that can be configured for AnalyticDB for PostgreSQL. |

**SLB**

| Parameter | Description |
|---|---|
| Specifications | The instance type that can be configured for Server Load Balancer (SLB). |
| Specifications Name | The name of the instance type that can be configured for SLB. |
| Maximum Connections | The maximum number of connections that can be configured for SLB. |
| New Connections | The number of new connections that can be configured for SLB. |
| QPS | The queries per second (QPS) that can be configured for SLB. |
| Description | The description of the specifications that can be configured for SLB. |

**ApsaraDB RDS**

| Parameter | Description |
|---|---|
| Engine Type | The engine type that can be configured for ApsaraDB RDS. |
| Minimum Storage (GB) | The minimum amount of storage space that can be configured for ApsaraDB RDS. |
| Maximum Storage (GB) | The maximum amount of storage space that can be configured for ApsaraDB RDS. |
| Specifications Name | The name of the instance type that can be configured for ApsaraDB RDS. |
| Version | The version number of ApsaraDB RDS. |
| CPUs | The number of CPU cores that can be configured for ApsaraDB RDS. |
| Maximum Connections | The maximum number of connections that can be configured for ApsaraDB RDS. |
| Memory (GB) | The memory size that can be configured for ApsaraDB RDS. |

ons

| Share Type | The share type that can be configured for ApsaraDB RDS. |
|---|---|

**PolarDB-X**

| Parameter | Description |
|---|---|
| Instance Type | The instance type that can be configured for PolarDB-X. |
| Instance Type Name | The name of the instance type that can be configured for PolarDB-X. |
| Specifications | The specifications that can be configured for PolarDB-X. |
| Specifications Name | The name of the specifications that can be configured for PolarDB-X. |

**ECS**

| Parameter | Description |
|---|---|
| Instance Family | The instance family that is divided into different instance types based on the scenarios for which they are suitable. |
| Specifications Level | The level of the instance type that can be configured for Elastic Compute Service (ECS). |
| vCPUs | The maximum number of vCPUs that can be configured for ECS. |
| Memory (GB) | The memory size that can be configured for ECS. |
| Instance Specifications | The instance type that can be configured for ECS. |
| GPU Type | The GPU type that can be configured for ECS. |
| GPUs | The number of GPUs that can be configured for ECS. |
| Supported ENIs | The number of elastic network interface (ENIs) that can be configured for ECS. |
| Number Of Private IP Addresses | The number of private IP addresses that can be configured for ECS. |

**KVStore for Redis**

| Parameter | Description |
|---|---|
| Specifications Name | The name of the specifications that can be configured for KVStore for Redis. |
| Instance Specifications | The instance type that can be configured for KVStore for Redis. |

ons

| Maximum Connections | The maximum number of connections that can be configured for KVStore for Redis. |
|---|---|
| Maximum Bandwidth | The maximum bandwidth that can be configured for KVStore for Redis. |
| CPUs | The number of CPU cores that can be configured for KVStore for Redis. |
| Version | The version number of KVStore for Redis. |
| Architecture | The architecture of KVStore for Redis. |
| Node Type | The node type of KVStore for Redis. |
| Service Plan | The service plan that can be configured for KVStore for Redis. |

**ApsaraDB for MongoDB**

| Parameter | Description |
|---|---|
| Specifications | The instance type that can be configured for ApsaraDB for MongoDB. |
| Instance Specifications | The name of the specifications that can be configured for ApsaraDB for MongoDB. |
| Engine Type | The engine type that can be configured for ApsaraDB for MongoDB. |
| Version | The version number of ApsaraDB for MongoDB. |
| Serial Number | The serial number of ApsaraDB for MongoDB. |
| Sequence Description | The description of the serial number of ApsaraDB for MongoDB. |
| Maximum Connections | The maximum number of connections that can be configured for ApsaraDB for MongoDB. |
| IOPS | The IOPS of ApsaraDB for MongoDB. |
| Storage Space | The amount of storage space that can be configured for ApsaraDB for MongoDB. |
| Minimum Storage | The minimum amount of storage space that can be configured for ApsaraDB for MongoDB. |
| Maximum Storage | The maximum amount of storage space that can be configured for ApsaraDB for MongoDB. |

#### Create specifications

You can customize specifications for each resource type. ons
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Specifications**.
4. Select the resource type for which you want to create specifications and click the **Resource**
**Specifications** tab.
5. On the **Resource Specifications** tab, click **Create Specifications** in the upper-left
corner.
6. In the dialog box that appears, configure the specifications parameters.
For more information, see Specification parameters.
7. Click **OK**.

#### View specifications

You can view the specifications of each resource type.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane of the **Configurations** page, click **Specifications**.
4. Click the resource type for which you want to view specifications.
5. On the **Resource Specifications** tab, set a **region**, **column**, and **value**. The
corresponding information is displayed in the specifications list.
6. Click the **Existing Specifications** tab and view the existing specifications and their
quantity.

#### Disable specifications

By default, newly created specifications are in the Enabled state.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane of the **Configurations** page, click **Specifications**.
4. Select the resource type for which you want to disable specifications.
5. Click **Disable** in the **Actions** column corresponding to the specifications that you want to
disable.
6. In the message that appears, click **OK**.

#### Export specifications

You can export specifications that you want to view and share.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Specifications**.
4. Select the resource type for which you want to export specifications.
ons
5. Click the **Resource Specifications** tab and click **Export** in the upper-right corner to save
the specifications to your computer as a CSV file.

#### View specifications of each resource

**type in previous versions**

You can view specifications of each resource type in previous versions.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane of the **Configurations** page, click **Specifications**.
4. On the **Specifications** page, click the resource type for which you want to view
specifications.
5. Click the **Specifications History** tab. View the detailed information in the specifications
list.

### Authentication modes

#### Authentication modes

This topic describes the authentication modes. Authentication modes are classified into the token mode and the hybrid mode. You can configure an authentication mode based on your business requirements.

**Token mode**

In token mode, Resource Access Management (RAM) and Security Token Service (STS) are required. Temporary STS tokens are issued to users and cloud services to assist in permission management. In token mode, all cloud services use STS tokens to authenticate users. Cloud services that do not support STS may be affected. For example, only operations administrators and level- 1 organization administrators can log on to the console of a cloud service.

**Note**

On the **Authentication Mode** page, you can view the cloud services that support the token mode. After you enable the token mode, authentication of northbound APIs may be affected. For example, if you use the AccessKey pair of a RAM user to call an API operation to add, delete, modify, or query specified resources in a specified organization and resource set, and the required RAM policies are not attached to the RAM user, an error may be returned.

**Warning**

Before you enable the token mode, we recommend that you contact Alibaba Cloud to evaluate the situation. If an error occurs when you call an API operation, disable the token mode. ons

**Hybrid mode**

In hybrid mode, cloud services that support RAM and STS can still authenticate users based on STS tokens. For cloud services that do not support STS, permissions are managed based on the authentication logic of Apsara Stack tenant accounts and RAM users. In hybrid mode, if you select one or more cloud services, the cloud services use STS tokens to authenticate users. Cloud services that are not selected still authenticate users in hybrid mode.

#### Configure an authentication mode

You can select an appropriate authentication mode for different scenarios.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Authentication Mode**.
4. Select **Token Mode** or **Hybrid** based on the scenario.
If you select **Hybrid**, you can specify a cloud service to use token-based authentication by selecting the checkboxes.

**Important**

After token-based authentication is enabled, the authentication mode of northbound API operations is affected. We recommend that you contact the Alibaba Cloud service team for evaluation before you enable token-based authentication. If an error occurs when an API operation is called, roll back and disable token-based authentication for the service.
5. In the lower part of the page, click **Save**.

### Message center

#### View internal messages

You can view all internal messages, including read and unread messages.

**Background information**

When changes are made to or alerts are generated for an instance in a resource, all users that have read and operation permissions on this resource receive corresponding messages.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, move the pointer over the
icon and click **More**.
3. In the left-side navigation pane of the **Message Center** page, click the target message
scope. Choose **Internal Messages > All Messages** to view all messages, including unread and read messages. Choose **Internal Messages > Unread Messages** to view unread messages. Choose **Internal Messages > Read Messages** to view read messages. ons

#### Mark messages as read

You can mark unread messages as read messages to facilitate message management.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, move the pointer over the
icon and click **More**.
3. In the left-side navigation pane of the **Message Center** page, choose **Internal Messages**
**> Unread Messages**.
In the upper part of the **Unread Messages** page, click different message types to filter messages.
4. On the Unread Messages page, find the message that you want to mark as read and click
**Mark as Read** in the **Actions** column.
You can also select the check boxes to the left of messages and click **Batch Read** in the upper-left corner of the page.
5. In the **Mark as Read** message, click **OK**.

#### Delete a message

You can delete messages that are no longer needed.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, move the pointer over the
icon and click **More**.
3. In the left-side navigation pane of the **Message Center** page, choose **Internal Messages**
**> All Messages**.
4. Find the message that you want to delete on the All Messages tab or other tabs and click
**Delete**.
You can also select the check boxes to the left of messages and click **Batch Delete** in the upper-left corner of the page.

### Configure resource pools

This topic describes how to configure resource pools. You can modify the maximum usage of each resource.

**Prerequisites**

If the physical inventory is unlimited, the logical inventory cannot be less than the used inventory. If the physical inventory is limited, the logical inventory cannot be less than the used inventory and cannot be greater than the physical inventory.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Resource Pool Configuration**.
4. Select the cloud service whose logical inventory that you want to modify and click
. ons You can also enter a name of the cloud service whose logical inventory that you want to modify in the search box and then click the **Search** icon.
5. Click **Save**.

### Custom configurations

#### Configure brands

You can customize the icon, platform name, and logon page of the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Custom Configurations**.
4. In the **Brand Settings** section, click the language tab of the page that you want to modify.
5. Configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Browser ICO Image | You can click Upload Image, select an image file, and then click Open. We recommend that you select an image whose resolution is 160 × 36 pixels in the PNG or JPG format. After the image is uploaded, you can click the icon to preview it. Before you upload a new image, you must click the icon to delete the existing image. |
| Platform Logo | You can click Upload Image, select an image file, and then click Open. We recommend that you select an image whose resolution is 160 × 36 pixels in the PNG or JPG format. After the image is uploaded, you can click the icon to preview it. Before you upload a new image, you must click the icon to delete the existing image. |
| Platform Name | You can customize a platform name. The name can be up to 8 characters in length. |

ons

| Parameter | Description |
|---|---|
| Logon Page | You can click + Add Screen to increase the number of scrolling screens. You can also click the icon to the left of a screen to decrease the number of scrolling screens. One to three scrolling screens can be allowed on the logon page. After you click the tab of a screen, you can perform the following operations: Background Image: Click Upload Image, select a background image file, and then click Open. We recommend that you select an image whose resolution is 1,880 × 1,600 pixels in the PNG or JPG format. After the image is uploaded, you can click the icon to preview it. Before you download a new image, you must click the icon to delete the existing image. Image Copywriting: Customize the image content. The image content can be up to 40 characters in length. |
| Copyright Notice | You can customize the information of the copyright notice. |

## Operations

### Quotas

#### Quota parameters

This topic describes the quota parameters of each service. An organization administrator can set resource quotas and create resources within the allowed quotas for its organization. When the quotas for the organization are used up, the system does not allow the organization administrator to create more resources for the organization. To create more resources, you must first increase the quotas for the organizations. If no quotas are set, you can create an unlimited amount of resources.

**ECS**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for Elastic Compute Service (ECS) and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for ECS. |
| GPU quota (number of cards) | The total number of GPU cores that you can configure for ECS. |
| SSD quota (G) | The total SSD capacity that you can configure for ECS. |
| Efficient cloud disk quota (G) | The total number of disks that you can configure for an ECS instance. |

**VPC**

| Parameter | Description |
|---|---|
| VPC quota (units) | The maximum number of virtual private clouds (VPCs) that you can configure. |

**OSS**

| Parameter | Description |
|---|---|
| OSS quota (G) | The maximum capacity that you can allocate for Object Storage Service (OSS). |

**ApsaraDB RDS for MySQL**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for ApsaraDB RDS for MySQL and the number of used cores. |

| Memory quota (G) | The total memory size that you can configure for ApsaraDB RDS for MySQL. |
|---|---|
| Disk quota (G) | The total storage size that you can configure for ApsaraDB RDS for MySQL. |

**PolarDB**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for PolarDB and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for PolarDB. |
| Disk quota (G) | The total storage size that you can configure for PolarDB. |

**ApsaraDB RDS for SQL Server**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for ApsaraDB RDS for SQL Server and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for ApsaraDB RDS for SQL Server. |
| Disk quota (G) | The total storage size that you can configure for ApsaraDB RDS for SQL Server. |

**ApsaraDB RDS for PostgreSQL**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for ApsaraDB RDS for PostgreSQL and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for ApsaraDB RDS for PostgreSQL. |
| Disk quota (G) | The total storage size that you can configure for ApsaraDB RDS for PostgreSQL. |

**SLB**

| Parameter | Description |
|---|---|
| VIP quota (units) | The maximum number of internal IP addresses that you can configure for Server Load Balancer (SLB). |
| Public network VIP quota (units) | The maximum number of public IP addresses that you can configure for SLB. |

**EIP**

| Parameter | Description |
|---|---|
| EIP quota (units) | The maximum number of elastic IP addresses (EIPs) that you can configure. |

**MaxCompute**

| Parameter | Description |
|---|---|
| CU quota (units) | The total number of capacity units (CUs) that you can configure for MaxCompute. |
| Disk quota (G) | The total storage size that you can configure for MaxCompute. |

**KVStore for Redis**

| Parameter | Description |
|---|---|
| Memory quota (G) | The total memory size that you can configure for KVStore for Redis. |

**PolarDB-X**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPUs that you can configure for PolarDB-X. |

**AnalyticDB for PostgreSQL**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for AnalyticDB for PostgreSQL and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for AnalyticDB for PostgreSQL. |
| Disk quota (G) | The total storage size that you can configure for AnalyticDB for PostgreSQL. |

**ApsaraDB for MongoDB**

| Parameter | Description |
|---|---|
| CPU quota (core) | The total number of CPU cores that you can configure for ApsaraDB for MongoDB and the number of used cores. |
| Memory quota (G) | The total memory size that you can configure for ApsaraDB for MongoDB. |
| Disk quota (G) | The total storage size that you can configure for ApsaraDB for MongoDB. |

**Dedicated hosts**

| Parameter | Description |
|---|---|
| DDH quota (units) | The number of dedicated hosts. |

#### Set quotas for a cloud service

You can set quotas for each organization to allocate and manage resources for each organization in an appropriate manner.

**Prerequisites**

You must set quotas for a parent organization before you can set quotas for its subordinate organizations.

**Background information**

If the parent organization (not including level-1 organizations) has quotas, the available quotas for a subordinate organization are equal to the quotas for the parent organization minus the quotas for other subordinate organizations. This topic describes how to set quotas for Elastic Compute Service (ECS). You can set quotas for other cloud resources in a similar manner.
1. Log on to the Apsara Uni-manager Management Console as an organization administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Quotas**.
4. In the **Organizational Architecture** section, click the name of the organization that you
want to manage.
5. Click **ECS**.
6. In the upper-right corner of the quota section, click the
icon.
7. Set the total quotas and click **Save**.
For information about quota parameters, see Quota parameters.

#### Modify quotas

Administrators can adjust quotas for cloud resources based on their organizational requirements.

**Background information**

This topic describes how to modify quotas for Elastic Compute Service (ECS). You can modify quotas for other cloud resources in a similar manner.
1. Log on to the Apsara Uni-manager Management Console as an organization administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Quotas**.
4. In the **Organizational Architecture** section, click the name of the organization that you
want to manage.
5. Click **ECS**.
6. In the upper-right corner of the quota section, click the
icon.
7. After you modify the quotas, click **Save**.
For more information about specification parameters, see Quota parameters.

#### Reset quotas

Administrators can reset quotas to remove quota limits on cloud resources.

**Prerequisites**

Before you delete a quota for an organization, make sure that no subordinate organizations have quotas.
1. Log on to the Apsara Uni-manager Management Console as an organization administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Quotas**.
4. In the **Organizational Architecture** section, click the name of the organization that you
want to manage.
5. Click the cloud service for which to reset quotas.
6. In the upper-right corner of the quota section, click the
icon.
7. In the message that appears, click **OK**.

#### Quota alert management

##### Create a rule for quota alerts

This topic describes how to create a rule for quota alerts.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. On the **Quota Alerts** page, click **Create Alert**.
5. In the **Create Quota Alert** dialog box, specify the **Organization and Resource Set**,
**Region**, **Cloud Service Category**, **Alert Name**, and **Alert criteria** parameters.
Parameter description

| Parameter | Values | Description |
|---|---|---|
| Alert criteria | Used | An alert is generated when the quota used by the organization and its subordinate organizations exceeds the configured threshold. |
|   | Remaining Available Quota | An alert is generated when the remaining available quota of the organization and its subordinate organizations is lower than the configured threshold. |
| Threshold | Number | Set this parameter according to your business requirements. |
|   | Percentage |   |

6. (Optional) Specify an Internet URL in the Alert Callback box for receiving alerts. Alerts are
sent to the URL by using POST requests over the HTTP protocol.
7. Click **OK**.

##### Modify a quota alert

This topic describes how to modify a quota alert.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. (Optional) On the **Quota Alerts** page, click **Advanced Filter** and enter the name of the
alert that you want to modify. You can also search the alert by **Organization and**
**Resource Set**, **Region**, or **Cloud Service Category**.
5. Find the alert that you want to modify and click **Edit** in the **Actions** column.
6. In the **Edit Quota Alert** dialog box, modify the settings of the **Alert Name**, **Alert criteria**,
**Alert Threshold**, and **Alert Callback** parameters.
7. After the modification is complete, click **OK**.

##### Delete a quota alert

This topic describes how to delete a quota alert. You can delete quota alerts that you no longer require.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. (Optional) On the **Quota Alerts** page, click **Advanced Filter** and enter the name of the
alert that you want to delete. You can also search an alert by **Organization and**
**Resource Set**, **Region**, or **Cloud Service Category**.
5. Find the alert that you want to delete and click **Delete** in the **Actions** column.
6. In the message that appears, click **OK**.

#### View the quota alert history

By viewing alerts, you can understand the usage of resource quotas and obtain exception information in a timely manner.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alert History**.
4. (Optional) On the Quota Alert History page, specify **Alert Triggered At**, **Organization**
**and Resource Set**, **Region**, **Cloud Service Category**, or **Alert Name** to filter the alert
history.
5. Click the alert name to view the alert information.

**Note**

The quota alert history is updated once a day.

### Usage statistics

#### View the usage statistics of cloud

**resources**

The Apsara Uni-manager Management Console shows the number of resource instances that run in the Apsara Stack environment by time, organization, resource set, and region. You can also export statistical reports from the Apsara Uni-manager Management Console.

**Background information**

The following cloud resources support usage statistics: Elastic Compute Service, Container Service for Kubernetes, Container Registry Standard Edition, Virtual Private Cloud, Server Load Balancer, VPN Gateway, Express Connect, NAT Gateway, IPv6 Gateway, Cloud Service Bus, Object Storage Service, ApsaraDB RDS for MySQL, Elastic IP Address, Tablestore, PolarDB-X V1.0, KVStore for Redis, AnalyticDB for PostgreSQL, Apsaradb MongoDB, Graph Database, ApsaraDB RDS for PostgreSQL ,ApsaraDB RDS for SQL Server, Log Service, Elastic Block Store, ECS Snapshot, Auto Scaling, API Gateway, Key Management Service, Realtime Compute, MaxCompute, Data Management, DataHub, Elasticsearch on Kubernetes, Enterprise Distributed Application Service, Dedicated Host, ApsaraDB for OceanBase, Bastionhost (Early Version), Cloud-native Bastionhost, Internet Firewall, VPC Firewall, Threat Detection Service, Database Audit, Web Application Firewall, Anti-DDoS Service, and Network Traffic Monitoring System. The following procedure uses Elastic Compute Service as an example to describe how to view usage statistics. You can view the usage statistics of other cloud resources in a similar manner.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Usage Statistics**.
4. Click **Elastic Compute Service**.
5. Click the
icon to specify a period of time and click **Search**. You can also search for instances by **organization**, **resource set**, **region**, or **instance ID**.
6. **Optional:**Click the
icon to save the displayed information to your computer as an XLS file. The exported file is named <Resource type name>.xls. Find the downloaded file from the download path in the browser setting.

**Note**

In the console, you can view or export up to 500 statistical records to an XLS file. If you want more statistical data, you can call the MeteringQuery operation.

### Statistical analysis

#### View reports of current data

You can use reports to view the most recent resources, quotas, and CloudMonitor data of each service.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Statistical Analysis** > **Reports**.
4. Click the tab that you want to view.
You can click the **Resource Report**, **Quota report**, or **Cloudmonitor report** tab.
5. (Optional) Set **Organization and resource set** and **Geographical** and click **Search**.
6. Click the service that you want to view.
View the most recent data of the service.

#### Export reports

You can export the resources, quotas, or monitoring data that you want to view at the same time based on cloud service types.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Statistical Analysis** > **Reports**.
4. Click the tab that you want to view.
You can click the **Resource Report** or **Quota Report** tab.
5. (Optional) Search for reports by organization and resource set or region.
You can click **Reset** to clear all filter properties.
6. Use one of the following methods to export data:
Export reports by service. a. Click **Create Report Export Task**. b. In the **Create Report Export Task** dialog box, enter a report name and configure other parameters based on your business requirements. Then, click **OK**. Export reports by instance. a. Click the name of a service. b. Select instances and click **Export Selected reports** in the lower-left corner of the page.

#### Download reports of historical data

This topic describes how to download reports of historical data. You can download data reports of cloud services within the specified period of time, resource set, and region by creating download tasks.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane of the **Operations** page, choose **Statistical Analysis** >
**Download Center**.
4. On the **Download Center** page, click **Create Download Task**.
5. Configure the parameters of the download task.

| Parameter | Description |
|---|---|
| Report Name | The name of the report. |
| Report Type | The type of the report. Valid values: Metering Report Resource Monitoring Statistic Report Resource Report Quota Report Detailed Billing Report |
| Product | The cloud service for which you want to download reports. You can select multiple cloud services. |
| Start Time and End Time | The start time and end time of the data. |
| Organization and Resource Sets | The organization to which the data belongs. You can select multiple organizations. |

| sara Uni-manager Managemen onsole User Guide·Operations |   |
|---|---|
| Parameter | Description |

| Region | The region of the data. You can select multiple regions. |
|---|---|

6. Click **OK**.
7. After the **Created** message appears, the **Download Center** page appears. Enter the
information of the created report in the search box and click **Search** to search for the created download task.
8. After **In progress** changes to **Completed** in the **Status** column, click **Download reports**
in the **Action** column.

### Tag management

You can use tags to classify and manage resources from different dimensions.

#### Query tags

Each tag consists of a tag key and a tag value. On the **Tag management** page, you can view all tag keys and values, as well as the information about the resources to which the tags are added.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Tags**.
4. In the left-side navigation pane of the **Tag management** page, click the name of the tag
whose values that you want to view. You can also view the number of cloud services to which the tag is added.
5. (Optional) In the left-side tag key list, click . In the
**Filter Conditions** dialog box,
configure the following filters based on your business requirements: **The organization of**
**the resource**, **Resource set**, **The region of the resource**, and **Keyword**. You must
configure **The organization of the resource** .

#### Create a tag

This topic describes how to create a tag and add the tag to resources.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, click **Tags**.
4. On the **Tag management** page, click **Create tags**.
i. In the **Create tags and bind resources** dialog box, select an existing tag key and tag value or enter a new tag key or tag value. Click **Next**.

**Note**

You can create up to 20 tags and add the tags to resources at a time. A tag key must be unique. ii. In the **Create tags and bind resources** dialog box, select the organization and resource set to which the resource belongs, select the region where the resource resides, select the cloud service to which the resource belongs, and then click **Next**.

**Note**

You can select up to 50 cloud resources at a time. iii. Confirm the information about the tag and resource, and click **OK**.

### Billing management

#### Billing overview

The billing system collects resource usage statistics for each service, organization, or resource set per month. You are charged for the consumed resources based on the billing rules.

**Billing configurations**

Billing configurations involve four terms to meet complex billing requirements. These configurations cover a variety of aspects such as basic prices, time policies, organization policies, and discount policies. The following terms from bottom up are used for different billing logics: Billable item: specifies prices and billing methods. Billing rule: specifies the billing range of services. Billing policy: specifies organization policies and discount capabilities of services. Billing plan: specifies billing time policies and discount capabilities.

**Billing overview**

On the Billing overview page, you can view the numbers of billing plans, policies, and rules that are available and in use. You can also view the effective time of billing plans and policies.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Overview**.
In the upper part of the Billing overview page, you can view the numbers of billing plans, policies, and rules that are available and in use in the **Billing plan**, **Billing Policy**, and
**Billing rules** sections.
4. In the lower part of the page, the effective time of billing plans and policies is displayed in a
Gantt chart. You can select an option from the drop-down list in the upper-right corner to change the time span of the chart.
5. You can slide the Gantt chart left and right to view whether billing plans and policies are
effective within different periods of time. Click **LocateDay** in the upper-right corner of the page to reset the time to the current day.

#### Billable items

##### Create a billable item

Billable items define the billing methods of services. This topic describes how to create a billable item.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Rules**.
4. Click the billing rule to which you want to add a billable item.
5. On the **Billing rule details** page, click **Create a billing item**.
6. In the **Create a billing item** panel, set the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Billing item name | Yes | The name of the custom billable item. The name can be up to 64 characters in length and must be unique. |
| Billing item description | No | The description of the custom billable item. The description can be up to 256 characters in length. |

| Parameter | Required | Description |
|---|---|---|
| Unit price information settings | Yes | The pricing logic of a specific service feature within a unit quantity. Valid values: Fixed pricing: You are charged for each instance on an hourly basis at a fixed rate that does not change with variables within a unit quantity. For example, the storage feature does not have properties such as specifications. You are charged at a fixed rate for each GB of stored data. This pricing logic is fixed pricing. Pricing: Service prices change with properties such as specifications. Prices vary based on types or property values. For example, Elastic Compute Service (ECS) provides a variety of instance types at different prices. Metering fields and values can be found in the metering data. The system obtains the values of specific metering fields from the metering data to determine the unit price of an instance. Additionally, the prices of some services are not entirely determined by specifications. For example, the prices of resources with identical specifications may vary based on their region. In metering pricing mode, prices are determined by a combination of Primary pricing and From pricing, which is similar to MySQL composite indexes. After you set Primary pricing and From pricing, you can click Download pricing file. Then, you can edit the billable items and prices in the file and click Upload pricing file to upload the file again. Note A maximum of two fields can be combined to determine prices. |

| Parameter | Required | Description |
|---|---|---|
| Quantity information settings | Yes | The quantity of resources used in a service within 1 hour. Valid values: Fixed quantity: The number of instances is fixed in each metering data record. For example, you are charged for an ECS instance based on its instance type. Each metering data record represents an instance. Then, the quantity is 1. Metering quantity: The number of instances is defined in each metering data record. A field in the metering data must be used to specify the quantity. During billing, the system obtains the value of this field in the metering data and calculates fees. For example, for Object Storage Service (OSS), the value of the Storage field in the metering data indicates the amount of used storage space. If you are charged for the amount of used storage space, the Storage field must be specified to define the quantity property. Conversion factor: The unit used to measure metering data may not be the same as that used to determine the price. For example, the storage price is calculated based on the amount of GBs consumed in OSS. In the metering data, the unit of the Storage value may be byte. Therefore, a conversion factor must be declared in the definition of each quantity. You can divide a quantity in the metering data by a conversion factor to convert the original unit to the unit in a price. |
| Billing unit | Yes | The unit of the custom billable item. Example: USD/hour. |

7. Click **Determine**.

##### Clone a billable item

You can clone an existing billable item to create the same or a similar billable item.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Rules**.
4. Click the name of the billing rule that you want to manage.
5. In the **Billing item** section, find the billable item that you want to clone and click **Clone** in
the **Operation** column.
6. In the **Create a billing item** panel, modify parameters of the billable item.
For more information about billable item parameters, see Create a billable item.
7. Click **Determine**.

##### Modify a billable item

This topic describes how to modify a billable item.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Rules**.
4. Click the name of the billing rule that you want to manage.
5. In the **Billing item** section, find the billable item that you want to modify and click **Editing**
in the **Operation** column.
6. In the **Modify billing items** panel, modify parameters of the billable item.
7. Click **Determine**.

**Warning**

If you modify billing items that are in use, billing data may change. This change cannot be undone. Proceed with caution.

##### Delete a billable item

You can delete billable items that are incorrect or no longer needed.

**Prerequisites**

At least one billable item is retained in a billing rule.

**Warning**

If you delete billable items, billing data may change. This change cannot be undone. Proceed with caution.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Rules**.
4. Click the name of the billing rule that you want to manage.
5. In the **Billing item** section, find the billable item that you want to delete and click **Delete**
in the **Operation** column.

#### Billing rules

##### Create a billing rule

A billing rule consists of all billable items of a service. Billing rules define which billing dimensions are used for services. This topic describes how to create a billing rule for a cloud service.

**Background information**

Service fees are accumulated from multiple billable items. A billing rule must contain at least one billable item. The number of billable items of a cloud service is unlimited. However, we recommend that you do not configure large numbers of billable items.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings Management** > **Billing Rules**.
4. Click **Create billing rules**.
5. In the **Create billing rules** panel, set the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Rule name | Yes | The name of the custom billing rule. The name can be up to 64 characters in length and must be unique. |
| Rule description | No | The description of the custom billing rule. The description can be up to 256 characters in length. |
| Associated cloud products | Yes | The associated cloud service that you want to manage. |
| Select billing item | Yes | After you select an associated cloud service, you can select billable items. A maximum of three billable items can be selected. If no appropriate billable item is available, you can click Create billing items to create billable items based on actual requirements. For more information, see Create a billable item. |

6. Click **Determine**.

##### View billing rules

This topic describes how to view existing billing rules and their details.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings Management** > **Billing Rules**.
4. (Optional) Use the following methods to filter billing rules:
Select a cloud service associated with billing rules from the service drop-down list and click **Search** to view all billing rules of the cloud service. Select **All statuses**, **Not used**, **In use**, or **Used** from the status drop-down list and click
**Search** to view all billing rules in the corresponding state.
Enter a billing rule name in the search box and click **Search** to search for the billing rule. Fuzzy search is supported.

**Note**

These filter methods can be used individually or in combination to more easily view and classify existing billing rules.
5. On the Billing rules page, view **Rule NAME/Status**, **Associated cloud products**, **Rule**
**description**, **Number of associated policies** , **Included billing items**, and **Fee**.
6. Click the name of the billing rule that you want to view.
On the billing rule details page, you can view **Billing Policy**, **Billing field**, and **Billing**
**item** of the billing rule.
7. Click the
icon to the left of the billable item name. You can view **status**, **Unit Price type**, **Metering field**, **Pricing**, **Bill presentation**,
**Quantity type**, **Quantity value**, and **Conversion factor** of the billable item.

##### Clone a billing rule

You can clone an existing billing rule to create the same or a similar billing policy.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings Management** > **Billing Rules**.
4. Find the billing rule that you want to clone and click **Clone** in the **Operation** column.
5. In the **Create billing rules** panel, modify billing rule parameters based on your
requirements. For more information about billing rule parameters, see Create a billing rule.
6. Click **Determine**.

##### Modify a billing rule

This topic describes how to modify a billing rule.

**Prerequisites**

After a billing rule is created, you cannot delete billable items that are in effect from the billing rule. You can create billable items in the billing rule, but these newly created billable items do not take effect. To modify billable items that are in effect in a billing rule, you must clone the billing rule. For more information, see Clone a billing rule.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings Management** > **Billing Rules**.
4. Click the name of the billing rule that you want to modify.
5. Modify the basic information of the billing rule.
i. In the **Basic information** section, click **Editing**. You can modify **Rule name** and **Rule description**. ii. Click **Save**.
6. Modify the billable items of the billing rule.
i. In the **Billing item** section, find the billable item that you want to modify and click
**Editing** in the **Operation** column.
ii. In the **Modify billing items** panel, modify related parameters and click **Determine**. For more information about billable item parameters, see Create a billable item.

**Warning**

If you modify billing rules that are in use, billing data may change. This change cannot be undone. Proceed with caution.

##### Delete a billing rule

You can delete billing rules that are incorrect or no longer needed.

**Prerequisites**

A billing rule is preconfigured for each service. This rule is used as the default billing rule and cannot be deleted. Default billable items in the default billing rule cannot be deleted. You can create other billable items.

**Warning**

If you delete a billing rule, billing data may change. This change cannot be undone. Proceed with caution.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings Management** > **Billing Rules**.
4. Find the billing rule that you want to delete and click **Delete** in the **Operation** column.
5. In the **Do you want to delete this rule** message, click **Delete**.

#### Billing policies

##### View billing policies

This topic describes how to view existing billing policies.

**Background information**

A billing policy consists of billing rules of multiple cloud services. A billing policy defines billing rules for a group of services, including organizations for which the billing policy is in effect and discounts for all services. A billing policy includes a billing rule for each service, a list of organizations for which the billing policy is in effect, and a discount for each service. The discount for each service can be different.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Policies**.
4. (Optional) Use one of the following methods to filter billing policies:
Select **All statuses**, **Not used**, **In use**, or **Used** from the status drop-down list and click
**Search** to view all billing policies in the corresponding state.
Enter a billing policy name in the search box and click **Search** to search for the billing policy. Fuzzy search is supported.

**Note**

These filtering methods can be used individually or in combination to more easily view and classify existing billing policies.
5. On the Billing Policy page, view **Policy name/Status**, **Include rules**, **Association plan**,
and **Associated organizations**. Move the pointer over the number of rules in the **Include rules** column to view the list of rule names. You can click a rule name to view its details. Move the pointer over the number of plans in the **Association plan** column to view the list of plan names. You can click a plan name to view its details.
6. Click the name of the billing policy that you want to view.
On the **Billing Policy details** page, you can view **Basic Information** and **Billing rules** of the billing policy.
7. In the **Billing rules** section, billing rules included in the billing policy are displayed as a
table. Filter and search for billing rules by **rule status**, **product name**, and **rule name**.
8. Click icons in the upper-right corner of the **Billing rules** section to customize how the
**Billing rules** section is displayed.

| Icon | Description |
|---|---|
|   | Shows the list in full screen mode. You can click the icon in the upper-right corner to exit the full screen mode. |
|   | Selects the size of cells and fonts in the list. Valid values: Default Compact |
|   | Selects or clears check boxes to determine the items to be displayed in the list. You can also click Reset to restore the list to its original settings. |

##### Create a billing policy

This topic describes how to create a billing policy.

**Background information**

The system requires that each billing policy includes all services for which billing is enabled. If a service in a billing policy is provided free of charge, the discount rate can be set to 0. This discount property takes effect only in the billing policy and does not belong to billing rules.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Policies**.
4. Click **Create a billing policy**.
5. In the **Create a billing policy** panel, set the following parameters.

| Parameter | Description |
|---|---|
| Policy name | The name of the custom billing policy. The name can be up to 64 characters in length and must be unique. |
| Note | The description of the custom billing policy. The description can be up to 256 characters in length. |
| Policy effective range | The level-1 organization for which the custom billing policy takes effect. You can select All organizations take effect to assign the billing policy to all level-1 organizations. If a metering data record belongs to an organization or a subordinate organization in the organization list to which a billing policy is assigned, the billing policy is the only one that is applicable to the metering data record. |
| Bind billing rules | You can perform the following operations to select a billing rule: i. Click a service name. ii. Select the billing rule that you want to use on the right. iii. In the Set discount rate column, enter a discount rate. If this service is provided free of charge, set the discount rate to 0. The discount rate cannot exceed 10. The default discount rate is set to 1 for all services, which indicates no discount. After fees of metering data of a service are calculated based on billing rules, the fees are multiplied by the discount rate of the service in the billing policy to calculate the price, discount, and original price. The original price is the sum of the price and the discount. |

6. Click **Determine**.

##### Clone a billing policy

You can clone an existing billing policy to create the same or a similar billing policy.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Policies**.
4. Find the billing policy that you want to clone and click **Clone** in the **Operation** column.
5. In the **Create a billing policy** panel, modify the configurations of the billing policy based
on your requirements. For information about billing policy parameters, see Create a billing policy.
6. Click **Determine**.

##### Modify a billing policy

This topic describes how to modify a billing policy.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Policies**.
4. Click the name of the billing policy that you want to modify.
5. Modify the basic information of the billing policy.
i. In the **Basic information** section, click **Editing**.
**Policy name**, **Associated organizations**, and **Note** can be modified.
ii. Click **Save**.
6. Modify the billing rules and discount rates for each service.
i. In the **Billing rules** section, click **Editing**. ii. Separately modify the billing rules and discount rates. Select the desired billing rule in the **Rule name** column corresponding to the service that you want to manage. Enter the expected discount rate in the **Discount rate** column corresponding to the service that you want to manage. iii. Click **Save**.

**Warning**

If you modify billing rules that are in use, billing data may change. This change cannot be undone. Proceed with caution.

##### Delete a billing policy

You can delete billing policies that are incorrect or no longer needed.

**Prerequisites**

A billing policy is preconfigured in the system. This policy is used as the default billing policy and cannot be deleted.

**Warning**

If you delete a billing policy, billing data may change. This change cannot be undone. Proceed with caution.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Policies**.
4. Find the billing policy that you want to delete and click **Delete** in the **Operation** column.
5. In the **Do you want to delete the policy** message, click **Delete**.

#### Billing plans

##### View billing plans

This topic describes how to view existing billing plans.

**Background information**

A billing plan consists of multiple billing policies that are configured with an effective time and priorities. A billing plan specifies a time range for billing policies. This enables the billing system to use different billing policies at different periods of time.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Plans**.
4. (Optional) Use one of the following methods to filter billing plans:
Select **All statuses**, **Not used**, **In use**, or **Used** from the status drop-down list and click
**Search** to view all billing plans in the corresponding state.
Set **Start Date** and **End Date** from the date picker and click **Search** to view all billing plans that are in effect within the specified period of time.

**Note**

These filtering methods can be used individually or in combination to more easily view and classify existing billing plans.
5. On the Billing plan page, view **Plan NAME/Status**, **Billing Policy**, **Billing rules**, **Priority**,
and **Effective time** of a billing plan. Move the pointer over the number of policies in the **Billing Policy** column to view the list of policy names. You can click a policy name to view its details. Move the pointer over the number of rules in the **Billing rules** column to view the list of rule names. You can click a rule name to view its details. The greater the number in the **Priority** column, the higher the priority of the plan.
6. Click the name of the billing plan that you want to view.
On the **Billing plan details** page, you can view **Basic information** and **Billing Policy**
**list** of the billing plan.
7. In the **Billing Policy list** section, view the billing policies contained in the billing plan.
You can filter and search for billing policies by **status** and **policy name**.
8. Click icons in the upper-right corner of the **Billing Policy list** section to customize how the
**Billing Policy list** section is displayed.

| Icon | Description |
|---|---|
|   | Shows the list in full screen mode. You can click the icon in the upper-right corner to exit the full screen mode. |
|   | Selects the size of cells and fonts in the list. Valid values: Default Compact |
|   | Refreshes the list of billing policies. |
|   | Selects or clears check boxes to determine the items to be displayed in the list. You can also click Reset to restore the list to its original settings. |

##### Create a billing plan

This topic describes how to create a billing plan.

**Prerequisites**

To simplify billing configurations and avoid unexpected charges due to excessive billing plans, a maximum of nine billing pans can be created (not including the default billing plan). To avoid errors caused by empty policies in a billing plan, the default billing policy is included in each billing plan. By default, the default billing policy has the lowest priority. This ensures that at least one billing policy is available after the billing plan is assigned to metering data.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Plans**.
4. Click **Create a billing plan**.
5. In the **Create a billing plan** panel, set the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Plan Name | Yes | The name of the custom billing plan. The name can be up to 64 characters in length and must be unique. |
| Effective time | Yes | The period of time for which the billing plan is in effect. You can select Permanently effective. This way, the billing plan is in effect all the time. |
| Plan priority | Yes | The priority of the billing plan in the billing system. The priority must be an integer greater than or equal to 0. The greater the number, the higher the priority. |
| Plan Remarks | No | The description of the custom billing plan. The description can be up to 256 characters in length. |
| Bind a billing policy | Yes | You can add a billing policy and set the effective time and discount rate for each policy. Perform the following operations: i. Click Add a billing policy. ii. (Optional) Select a state from the All statuses drop- down list and click Search. iii. Select the billing policies that you want to add. iv. Click Determine. v. Set Policy Effective Time and Discount rate for each billing policy. The discount rate must be greater than 0 and less than or equal to 10. |

6. Click **Determine**.

**Note**

Each billing policy in a billing plan has a priority. When metering data is matched to a billing plan, billing policies in the billing plan are selected based on their priorities. When a billing policy is selected, bills are generated only based on this policy.

##### Clone a billing plan

You can clone an existing billing plan to create the same or a similar billing plan.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Plans**.
4. Find the billing plan that you want to clone and click **Clone** in the **Operation** column.
5. In the **Create a billing plan** panel, modify billing plan parameters based on your
requirements. For more information about billing plan parameters, see Create a billing plan.
6. Click **Determine**.

##### Modify a billing plan

This topic describes how to modify a billing plan.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Plans**.
4. Click the name of the billing plan that you want to modify.
5. Modify the basic information of the billing plan.
i. In the **Basic information** section, click **Editing**. You can change **Plan Name**, **Effective range**, **Priority**, and **Remarks**. ii. Click **Save**.
6. Change **Effective time**, **Priority**, and **Discount rate** of the billing policy or delete the
billing policy i. In the **Billing Policy list** section, click **Editing**. ii. Separately change the effective time, priority, and discount rate of a billing policy or delete the billing policy. Select a new effective time from the date picker in the **Effective time** column.

**Note**

The effective time of the default billing policy cannot be changed. Enter a desired discount rate in the **Discount rate** column corresponding to the billing policy. Drag and drop the icon corresponding to the billing policy to prioritize it. The closer to the top of the list, the higher the priority. Click **Delete** in the **Operation** column. In the **Do you want to delete the policy?** message, click Delete.

**Note**

The default billing policy cannot be deleted. iii. Click **Save**.
7. Add a billing policy.
i. Click **Add a billing policy**. ii. (Optional) Select a state from the **All statuses** drop-down list and click **Search**. iii. Select the billing policies that you want to add. iv. Click **Determine**. v. Set **Effective time** and **Discount rate** for each billing policy.

**Warning**

If you modify billing plans that are in use, billing data may change. This change cannot be undone. Proceed with caution.

##### Delete a billing plan

You can delete billing plans that are incorrect or no longer needed.

**Prerequisites**

A billing plan is preconfigured in the system. This policy is used as the default billing policy and cannot be deleted.

**Warning**

If you delete a billing plan, billing data may change. This change cannot be undone. Proceed with caution.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billing Management** > **Billing Plans**.
4. Find the billing plan that you want to delete and click **Delete** in the **Operation** column.
5. In the **Do you want to delete the plan** message, click **Delete**.

#### Bills

##### View cloud service bills

You can view bills by cloud service type.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Billings** > **Cloud Service Bills**.
4. View the bill overview.
i. Click the **Bill overview** tab. ii. Select the year and the month for which you want to view bills from the **Account period** date picker. You can view different data in the following sections:
**Cloud products bill summary**: View the number of cloud services that has billing
enabled, the number of cloud services that incur charges, the total fees generated within the selected month, and the total fees generated within the selected year.
**Consumption trends of cloud products.Last six months** : View the consumption
trend of each cloud service within the last six months. Click **Top 5** or **Top 10** in the upper-right corner to show the top five or top ten cloud services in terms of consumption within each month. Click the or icon to show the consumption trends of cloud services by using a column chart or a line chart.
**Top 10Consumption distribution of cloud products** : View the generated fees and
their proportions of the top ten cloud services within the selected month.
**Consumption details of all cloud products** : View the fees of all cloud services
within the selected month. Select Sort by fee from high to low or Sort by fee from low to high in the upper-right corner to sort cloud services by fees.
5. View bill statistics.
i. Click the **Bill statistics** tab. ii. Select the year and the month for which you want to view bills from the date picker. iii. (Optional) Select the cloud service and the region that you want to view. iv. Click **Search**. You can view the billing information that meets the search conditions. The billing information includes the billing period, cloud service, region, fees, and billing cycle. v. (Optional) Click the icon to modify fees as an operations administrator. vi. (Optional) Click **View details** in the Operation column to view bill details. vii. Save the queried data to your computer. Click **Export all bills** to save all queried data to your computer as an XLS file. Select the bills that you want to export and click **Export Selected bills** to save the selected data to your computer as an XLS file.
6. View bill details.
i. Click the **Bill details** tab. ii. Select the year and the month for which you want to view bills from the **Account period** date picker. iii. (Optional) Set Cloud products, Area, and Instance ID. iv. Click **Search**. You can view the billing information that meets the search conditions. The billing information includes **Account period**, **Cloud products**, **Tissue**, **Resource set**,
**Instance ID**, **Area**, **Billing cycle**, **Free amount**, and **Amount payable**.
v. Save the queried data to your computer. Click **Export all bills** to save all queried data to your computer as an XLS file. Select the bills that you want to export and click **Export Selected bills** to save the selected data to your computer.

##### View bills by organization and resource

**set**

You can view bills by organization and resource set.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Operations**.
3. In the left-side navigation pane, choose **Bills** > **Organization and Resource Set Bills**.
4. View the billing overview.
i. Click the **Billing overview** tab. ii. Select the year and the month for which you want to view bills from the **Account period** date picker. You can view different data in the following sections:
**XX (and all its sub-organizations) billing overview** : View the number of
organizations, the number of organizations that incur costs, the total fees generated within the selected month, and the total fees generated within the selected year.
**Organizational consumption trend. Nearly 6 months** : View the consumption trend
of each organization within the last six months. Click **Top 5** or **Top 10** in the upperright corner to show the top five or top ten organizations in terms of consumption within each month. Click the or icon to show the consumption trends of organizations in a column chart or a line chart.
**Top 10 Resource set consumption distribution**: View the generated fees and their
proportions of the top ten organizations within the selected month.
**Organization consumption details**: View the fees of all organizations within the
selected month. Select Sort by fee from high to low or Sort by fee from low to high in the upper-right corner to sort organizations by fees.
5. View billing statistics.
i. Click the **Billing statistics** tab. ii. Select the year and the month for which you want to view bills from the date picker. iii. (Optional) Select the organization and resource set whose billing statistics you want to view. iv. Click **Search**. You can view the billing information that meets the search conditions. The billing information includes **Account period**, **The name of the organization** , **Resource set**
**name**, **Amount**, and **Billing cycle**.
v. (Optional) Click the icon to modify fees as an operations administrator. vi. (Optional) Click **View details** in the Operation column to view bill details. vii. Save the queried data to your computer. Click **Export all bills** to save all queried data to your computer in an XLS file. Select the bills that you want to export and click **Export Selected bills** to save the selected data to your computer in an XLS file.
6. View billing details.
i. Click the **Billing details** tab. ii. Select the year and the month for which you want to view billing details from the
**Account period** date picker.
iii. (Optional) Specify **Organizations and resource sets** , **Cloud products**, **Region**, and Instance ID. iv. Click **Search**. You can view the billing information that meets the search conditions. The billing information includes **Account period**, **Cloud products**, **Organization**, **Resource set**,
**Instance ID**, **Region**, **Billing cycle**, **Free amount**, and **Amount payable**.
v. Save the queried data to your computer. Click **Export all bills** to save all queried data to your computer in an XLS file. Select the bills that you want to export and click **Export Selected bills** to save the selected data to your computer in an XLS file.

## Security

### View operation logs

You can view operation logs to obtain up-to-date information about all resources and functional modules in the Apsara Uni-manager Management Console. You can also export operation logs to your computer.
1. Log on to the Apsara Uni-manager Management Console as a security administrator.
2. In the top navigation bar, choose**Security** > Global Platform Security > Operation Logs.
3. Select an organization and service, and set the start date and end date to search for logs.
The logs that meet the filter conditions are displayed. Alternatively, you can click **Advanced** in the upper-right corner for more filter conditions, such as **Username**, **Resource ID**, and **Source IP Address**. You can also enter a keyword in the text box. After you specify these parameters, click **Search** to search for specific logs. The following table describes the fields in the query result. Table 1. Fields in the query result

| Field | Description |
|---|---|
| Organizati on | The organization of the object on which operations are performed. |
| Resource Set | The resource set of the object on which operations are performed. |
| Product Type | The resource type of the object on which operations are performed. |
| Resource ID | The ID of the object on which operations are performed. |
| Status | The current status of the operation. |
| Call Source | The name of the operator. |
| Event Type | The operation that was performed. Operations on an Apsara Stack service include create, modify, delete, query, update, bind, unbind, enable, disable, apply for, release, and change the ownership of service instances. |
| Source IP Address | The IP address of the operator. |
| Details | A brief description of the operation. |
| Time | The time when the operation started. |

**Note**

You can click the icon and select the fields that you want to show in the query result from the drop-down list.
4. **Optional:**Click the
icon to save the logs displayed on the current page to your computer as a CSV file.

## RAM

### RAM introduction

Resource Access Management (RAM) is a resource access control service provided by Apsara Stack. You can use RAM to manage users and control which resources are accessible to employees, systems, and applications. RAM provides the following features: RAM role To authorize a cloud service in a level-1 organization to use other resources in the organization, you must create a RAM role. This role specifies the operations that the cloud service can perform on resources. Only system administrators and level-1 organization administrators can create RAM roles. User group You can create multiple users within an organization and grant them different operation permissions on cloud resources. You can create RAM user groups to classify and authorize RAM users within your Apsara Stack tenant account. This simplifies the management of RAM users and their permissions. You can create RAM permission policies to grant different operation permissions to different user groups.

### Permission policy structure

**and syntax**

This topic describes the structure and syntax used to create or update permission policies in Resource Access Management (RAM).

**Policy characters and usage rules**

Characters in a policy The following characters are JSON tokens and are included in policies: `{ } [ ] " , :` . The following characters are special characters in the syntax and are not included in policies: = < > ( ) | . Use of characters If an element can have more than one value, you can perform the following operations: Separate multiple values by using commas (,) as delimiters between each value and use an ellipsis (...) to describe the remaining values. Example: `[ <action_string>,`

```xml
<action_string>, ...] .
```

Include only one value. Examples: `"Action": [<action_string>]` and `"Action":`

```xml
<action_string> .
```

A question mark (?) following an element indicates that the element is optional. Example:

```
 <condition_block? > .
```

A vertical bar ( | ) between elements indicates multiple options. Example: ("Allow" |

```
"Deny") .
```

Elements that must be text strings are enclosed in double quotation marks (""). Example:

```xml
 <version_block> = "Version" : ("1") .
```

**Policy structure**

The policy structure includes the following components: The version number. A list of statements. Each statement contains the following elements: Effect, Action, Resource, and Condition. The Condition element is optional.

**Policy syntax**

```xml
policy = {
     <version_block>,
     <statement_block>
```

`}`

```xml
<version_block> = "Version" : ("1") <statement_block> = "Statement" : [ <statement>, <statement>, ... ] <statement> = {
    <effect_block>,
    <action_block>,
    <resource_block>,
    <condition_block? >
```

`}`

```xml
<effect_block> = "Effect" : ("Allow" | "Deny") <action_block> = ("Action" | "NotAction") :
    ("*" | [<action_string>, <action_string>, ...])
<resource_block> = ("Resource" | "NotResource") :
    ("*" | [<resource_string>, <resource_string>, ...])
<condition_block> = "Condition" : <condition_map> <condition_map> = {
  <condition_type_string> : {
      <condition_key_string> : <condition_value_list>,
      <condition_key_string> : <condition_value_list>,
      ...
```

`},`

```xml
  <condition_type_string> : {
      <condition_key_string> : <condition_value_list>,
      <condition_key_string> : <condition_value_list>,
      ...
  }, ...
```

`}`

```xml
<condition_value_list> = [<condition_value>, <condition_value>, ...] <condition_value> = ("String" | "Number" | "Boolean")
```

Description: The current policy version is 1. The policy can have multiple statements.

| The effect of each statement can be either | Allow | or | Deny | . |
|---|---|---|---|---|
| Note In a statement, both the Action and Resource elements can have multiple values. |   |   |   |   |

Each statement can have its own conditions.

**Note**

A condition block can contain multiple conditions with different operators and logical combinations of these conditions. You can attach multiple policies to a RAM user. If policies that apply to a request include an `Allow` statement and a `Deny` statement, the Deny statement overrides the Allow statement. Element value: If an element value is a number or Boolean value, it must be enclosed in double quotation marks ("") in the same way as strings. If an element value is a string, characters such as the asterisk ( `*` ) and question mark ( ? ) can be used for fuzzy matching.

| The asterisk ( * ) indicate example, ecs:Describe* |   | * | ) indicate |   |
|---|---|---|---|---|
|   | ecs:Describe* |   |   |   |
| The question mark (?) |   |   |   | i |

The asterisk ( `*` ) indicates any number (including zero) of allowed characters. For example, `ecs:Describe*` indicates all ECS API operations that start with `Describe` . The question mark (?) indicates an allowed character.

**Policy format check**

Policies are stored in RAM as JSON documents. When you create or update a policy, RAM first checks whether the JSON format is valid. For more information about JSON syntax standards, see RFC 7159. We recommend that you use tools such as JSON validators and editors to check whether the policies meet JSON syntax standards.

### RAM-based batch

**authorization**

#### View the basic information about a

**RAM-based batch authorization role**

You can view the basic information about a RAM-based batch authorization role, including its user groups and permission policies.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Click the name of a role whose type is **RAM-based Batch Authorization**.
5. On the **Role authorization** page, click the **User Groups** or **Permissions** tab to view the
corresponding information.

#### Create a RAM-based batch

**authorization role**

If you want all RAM users in a user group to have the same permissions on cloud resources, you must use the RAM-based batch authorization feature.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**. In the upper-
left corner of the **Role Permissions** page, click **Create Custom Role**.
4. On the **Create Role** page, click **Advanced Settings**. In the **Advanced Settings** section,
click **Create RAM Authorization**.
5. On the **Create RAM Authorization** page, specify the **Role name**, **Description**, and
**Sharing Scope** parameters. The value of **Sharing Scope** is **Global** by default, which
indicates that the role is visible to and can be used by all organizations.
6. Click **Create and Configure RAM Authorization** .
7. **Optional:**On the **Create RAM Authorization** page, click the **User Groups** tab and the
**Add User Group** button. On the **Add User Group** dialog box, select a user group and
click **OK**.
8. **Optional:**On the **Create RAM Authorization** page, click the **Permissions** tab and the
**Add Policy** button. In the **Add Policy** dialog box, select a policy or create a new policy,
and then click **OK**.

**Note**

You can select a maximum of five policies for a RAM-based batch authorization role.
9. Click **OK**.

#### Create a permission policy

To use a cloud service to access other cloud resources, you must create a policy and attach it to a user group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role that you want to modify and click **Modify** in
the **Actions** column.
5. Click the **Permissions** tab.
6. Click **Policies**. In the **Policies** panel, click **Create Policy**.
7. In the **Create Policy** dialog box, enter the policy information.
For more information about how to enter the policy content, see Permission policy structure and syntax.
8. Click **OK**.

#### Modify the content of a permissions

**policy of a RAM-based batch authorization**

**role**

You can modify the content of a permissions policy of a RAM-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role whose permissions policy want to modify, and
click **Modify** in the **Actions** column.
5. Click the **Permissions** tab and click **Policies**.
6. In the **Policies** panel, click the name of the policy whose content you want to modify.
7. The Policy Details panel is displayed. Click the **Policy Content** tab. Click **Modify Policy**
**content** and modify the content based on your business requirements. Then, click **Save**
**Changes** and **OK**.

**Important**

The modification affects the roles that reference this policy. Proceed with caution. For more information about how to modify the content of a policy, see Permission policy structure and syntax.

#### Modify the name of a permission

**policy attached to a RAM-based batch**

**authorization role**

You can modify the name of a permission policy attached to a RAM-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role whose permission policy want to modify, and
click **Modify** in the **Actions** column.
5. Click the **Permissions** tab and click **Policies**.
6. In the **Policies** panel, find the policy whose name you want to modify, and click **Modify** in
the **Actions** column.
7. In the **Modify Policy** dialog box, modify the name of the policy. Click **OK**.

#### Add a user group to a RAM-based

**batch authorization role**

You can add a user group to a RAM-based batch authorization role based on your business requirements.

**Prerequisites**

A user group is created. For more information, see Create a user group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role to which you want to add a user group, and
click **Modify** in the **Actions** column.
5. Click the **User Groups** tab.
6. Click **Add User Group**. In the **Add User Group** dialog box, select a user group.
7. Click **OK**.

#### Attach a permission policy to a RAM-

**based batch authorization role**

You can attach a permission policy to a RAM-based batch authorization role to grant permissions to all users in a user group.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role to which you want to attach a permission
policy, and click **Modify** in the **Actions** column.
5. Click the **Permissions** tab. Then click **Add Policy**.
6. In the **Add Policy** dialog box, select a policy and click **OK**.
If no policy is available, you must create one. In the **Add Policy** dialog box, click **Create**
**Policy**. For more information about how to enter the policy content, see Permission policy
structure and syntax.

**Note**

You can select a maximum of five policies for a RAM-based batch authorization role.

#### Detach a permission policy from a

**RAM-based batch authorization role**

You can detach a permission policy that is no longer needed from a RAM-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role from which you want to detach a permission
policy, and click **Modify** in the **Actions** column.
5. Click the **Permissions** tab.
6. Find the policy that you want to detach and click **Remove permissions** in the **Actions**
column.
7. In the message that appears, click **OK**.

#### Modify the name of a RAM-based

**batch authorization role**

An administrator can modify the name of a RAM-based batch authorization role.

**Background information**

The names of preset roles cannot be modified.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role whose name you want to modify, and click
**Modify** in the **Actions** column.
5. In the upper-right corner of the Role authorization page, click **Modify Basic Information**.
In the **Modify** dialog box, modify the name of the role.
6. Click **OK**.

#### Delete a RAM-based batch

**authorization role**

You can delete a RAM-based batch authorization role that is no longer needed.

**Prerequisites**

You have unbound all user groups from the RAM-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. Find the RAM-based batch authorization role that you want to delete, and click **Delete** in
the **Actions** column.
5. In the message that appears, click **OK**.

### RAM role-based batch

**authorization**

#### View the basic information about a

**RAM role-based batch authorization role**

You can view the basic information about a RAM role-based batch authorization role, including its permission policies, trust policies, and RAM roles.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Click the name of a role whose type is **RAM Role-based Batch Authorization**.
5. On the **Grant Permissions** page, click the **Custom Policy**, **Trust Policy**, and **RAM Roles**
tabs to view information.

#### Create a RAM role-based batch

**authorization role**

To authorize a cloud service in a level-1 organization to use other resources in the organization, you must create a RAM role-based batch authorization role. This role contains the permissions that are required by the cloud service to perform operations on the resources.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. In the upper-left corner of the **Role Permissions** page, click **Create Custom Role**.
5. On the **Create Custom Role** page, click **Advanced Settings**. In the Advanced Settings
section, click Create RAM Role & Attach Policy.
6. In the **Create RAM Role & Attach Policy** wizard, perform the following steps.
i. Enter a **Role name** and **Description**, and set the **Sharing Scope**. The description is optional. The value of **Sharing Scope** is **Global** by default, which indicates that the role is visible to and can be used by all organizations. Click **Next**. ii. Select one or more policies or create a new policy. Click **Next**.

**Note**

You can select a maximum of five policies for a RAM role-based batch authorization role. iii. Select a **Trust Organization** and **Trust Cloud Service** from the drop-down lists. Click
**Next**.

**Note**

You can select multiple trust organizations and trust cloud services at a time for a RAM role-based batch authorization role. iv. In the Preview Policy step, check the content of the selected permission policies and trust policies, and click **Create**.

#### Modify the content of a permission

**policy or a trust policy for a RAM role-based**

**batch authorization role**

You can modify the content of a custom permission policy and a trust policy for a RAM rolebased batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Find the RAM role-based batch authorization role for which you want to modify a permission
policy or trust policy, and click **Modify** in the **Actions** column.
5. Modify the policy content.
Modify the content of a custom permission policy

**Important**

The modification affects the roles that reference this policy. Proceed with caution. a. Click the **Custom Policy** tab and click **Policies**. In the **Policies** panel, click the name of the policy whose content you want to modify. b. The Policy Details panel is displayed. Click the **Policy Content** tab. Click **Modify**
**Policy content** and modify the content based on your business requirements. Then,
click **Save Changes** and **OK**. For more information about how to modify the policy content, see Permission policy structure and syntax. Modify the content of a trust policy

**Important**

The modification affects the trust entities of the role. Proceed with caution. a. Click the **Trust Policy** tab and click **Modify**. b. (Optional) Select one or more organizations from the **Trust Organization** drop-down list. c. (Optional) Select one or more cloud services from the **Trust Cloud Service** drop-down list. d. In the **Trust Policy** section, modify the content of the policy. Click **Save Changes**. For more information about how to modify the policy content, see Permission policy structure and syntax.

#### Modify the name of a permission

**policy for a RAM role-based batch**

**authorization role**

You can modify the name of a permission policy for a RAM role-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Find the RAM role-based batch authorization role for which you want to modify a permission
policy, and click **Modify** in the **Actions** column.
5. Click the **Custom Policy** tab and click **Policies**. In the **Policies** panel, find the policy
whose name you want to modify, and click **Modify** in the **Actions** column.
6. In the **Modify Policy** dialog box, modify the name of the policy.
7. Click **OK**.

#### Add an organization to a RAM role-

**based batch authorization role**

You can add an organization to a RAM role-based batch authorization role based on your business requirements.

**Prerequisites**

You have created the organization that you want to add. For more information, see Create an organization.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Find the RAM role-based batch authorization role to which you want to add an organization,
and click **Modify** in the **Actions** column.
5. Click the **RAM Role** tab. Click **Create**.
6. In the **Create** dialog box, select an organization. Then click **OK**.

#### Remove a custom permissions policy

**from a RAM role-based batch authorization**

**role**

You can remove permissions that are no longer needed from a RAM role-based batch authorization role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Find the RAM role-based batch authorization role from which you want to remove a custom
permissions policy, and click **Modify** in the **Actions** column.
5. Click the **Custom Policy** tab. Find the policy that you want to remove, and click **Remove**
**permissions** in the **Actions** column.
6. In the message that appears, click **OK**.

#### Delete a RAM role-based batch

**authorization role**

You can delete a RAM role-based batch authorization role that is no longer needed.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Find the RAM role-based batch authorization role that you want to delete, and click **Delete**
in the **Actions** column.
5. In the **Delete** message, click **OK**.

### RAM authorization policies

#### Create a service-linked role

You can create authorization policies and grant them to organizations.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. In the upper-left corner of the page, click **Create Service-linked Role**.
5. On the **Create Service-linked Role** page, set **Organization Name** and **Service Name**.
6. Click **OK**.

#### View the details of a service-linked

**role**

You can view the details of a Resource Access Management (RAM) role, including its role name, creation time, description, and Alibaba Cloud Resource Name (ARN).
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the **Service-linked Roles** page, set **Role Name**, **Service Name**, or **Organization**
**Name**, and click **Search**.
To perform another search, click **Reset**.
5. Find the service-linked role that you want to view and click **View Details** in the **Actions**
column.

#### View RAM policies

You can view the details of a Resource Access Management (RAM) policy, including its policy name, policy type, default version, description, association time, and policy content.

**Prerequisites**

A RAM policy is created. For more information, see Create a service-linked role.
1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the **Service-linked Roles** page, set **Role Name** or **Service Name** and click **Search** in
the upper-right corner. To perform another search, click **Reset**.
5. Find the service-linked role that you want to view and click **View Details** in the **Actions**
column.
6. Click the **Role Policy** tab to view the information of the role policy. Click **View Details** in
the Actions column to view the policy details. ormation management

## Personal information

**management**

### Modify personal information

You can modify your personal information to keep it up to date.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the upper-right corner of the **Basic Information** section, click **Edit**.
4. In the **Modify User Information** dialog box, modify the personal information.
5. Click **OK**.

### Change the logon password

To improve security, you must change your logon password on a regular basis. This topic describes how to change your logon password.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**. ormation management
3. Click **Change Password**.
4. In the **Change Password** dialog box, set **Current Password**, **New Password**, and
**Confirm Password**.
5. Click **OK**.

### Switch the current role

You can switch the scope of your current role.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the user profile picture
and choose **User Information** from the shortcut menu.
3. Click **Switch Role**.
ormation management
4. In the **Switch Role** dialog box that appears, select the role that you want to switch to.
You can also switch back to the default role.

### View the current role policy

You can view the information of your current role policy.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **Personal information**.
3. Click **View Current Role Policy** on the left side of the page.
In the **View Policies of Current Role** dialog box, view your RAM role.
4. Select the organization and the policy that you want to view.
In the **View Policies of Current Role** message, view the policy content.

### View the AccessKey pair of

**your Apsara Stack tenant account**

To ensure the security of cloud resources, the system must verify the identity of visitors and ensure that they have the relevant permissions. You must obtain the AccessKey ID and AccessKey secret of your Apsara Stack tenant to access cloud resources.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, view your AccessKey pair.
ormation management

**Note**

The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### Create an AccessKey pair

You can delete your old AccessKey pairs and create new ones to implement the rotation of your AccessKey pairs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the upper-right corner of the **Apsara Stack AccessKey Pair** section, click **Create**
**AccessKey Pair**.

**Note**

Each user can have up to two AccessKey pairs.

### Delete an AccessKey pair

You can delete AccessKey pairs that are no longer needed.

**Prerequisites**

Each user can delete only its own AccessKey pairs. The administrator cannot delete the AccessKey pairs of users. Each user retains at least one AccessKey pair.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, find the AccessKey pair that you want to
delete and click **Delete** in the **Actions** column.
4. In the message that appears, click **OK**.

### Disable an AccessKey pair

You can disable AccessKey pairs that are no longer needed. Newly created AccessKey pairs are in the Enable state by default.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, find the AccessKey pair that you want to
disable and click **Disable** in the **Actions** column. ormation management Each user can disable only its own AccessKey pairs. The administrator cannot disable the AccessKey pairs of users.
4. In the message that appears, click **OK**.

**Note**

Make sure that at least one AccessKey pair is in the Enable state.

### Enable an AccessKey pair

Disabled AccessKey pairs must be re-enabled before you can continue to use them. Newly created AccessKey pairs are in the Enable state by default.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, find the AccessKey pair that you want to
enable and click **Enable** in the **Actions** column.
4. In the message that appears, click **OK**.

**Note**

Make sure that at least one AccessKey pair is in the Enable state.

### MFA

#### Overview

Multi-factor authentication (MFA) is an identity authentication method in computer systems. It requires users to provide two or more verification factors to gain access to a resource. This topic introduces the principles and use scenarios of MFA.

**Introduction to MFA**

When MFA is enabled, you must enter your username and password (first security factor) and then a variable verification code (second security factor) from an MFA device when you log on to the Apsara Uni-manager Management Console. Two-factor authentication enhances security for your account. MFA devices use the Time-based One-time Password (TOTP) algorithm to generate timedependent 6-digit dynamic verification codes. The Apsara Uni-manager Management Console supports software-based virtual MFA devices. You can install software such as the Alibaba Cloud app that supports MFA on your mobile device such as your mobile phone to act as a virtual MFA device.

**Limits**

The TOTP algorithm requires that the time of the system clock of the Apsara Uni-manager Management Console remain consistent with the standard time on the Internet. Otherwise, discrepancies in time can lead to inconsistent MFA verification codes and leave you unable to log on to the Apsara Uni-manager Management Console. ormation management

#### Bind a virtual MFA device to enable

### MFA

Multi-factor authentication (MFA) is automatically enabled after you bind an MFA device. This topic describes how to bind a virtual MFA device.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the upper-right corner of the **MFA** section, click **Bind Virtual MFA Device**.
4. On the **Bind Virtual MFA Device** page, follow the instructions to bind an MFA device.
The following figure shows the MFA section after the MFA device is bound.

**Results**

After a virtual MFA device is bound, you must enter a 6-digit MFA verification code in addition to your username and password before you can log on to the Apsara Uni-manager Management Console.

#### Unbind a virtual MFA device to

**disable MFA**

To disable multi-factor authentication (MFA), you must disable the MFA device that is bound. This topic describes how to unbind a virtual MFA device to disable MFA.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the upper-right corner of the **MFA** section, click **Disable Virtual MFA Device**.
4. In the dialog box that appears, click **Disable Virtual MFA Device**.
After you disable MFA, you need only to enter your username and password the next time you log on to the Apsara Uni-manager Management Console.

#### Forcibly enable MFA

Administrators, including the platform administrator, operations administrator, and organization administrator, can check whether their users have multi-factor authentication (MFA) enabled. If MFA is disabled for the users, the administrators can forcibly enable MFA for the users.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
ormation management
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose Users > **Users**.
4. Click the **System Users** tab.
5. Find the user for whom you want to enable MFA, click the icon in the
**Actions** column
and choose **MFA Status**. You can select an organization or enter a username to search for a user.
6. In the **MFA Status** message, click **OK**.

**Note**

After MFA is forcibly enabled for a user, the user must go to the Bind Virtual MFA Device page to bind a virtual MFA device before the user can log on to the Apsara Uni-manager Management Console. MFA can be forcibly enabled for users, but cannot be forcibly disabled. Before MFA is enabled, the MFA status of the user is **Not Enabled**. After MFA is enabled, the MFA status of the user is **Enabled but Not Bound**.

#### Reset MFA

If you lose your multi-factor authentication (MFA) key, you must have the administrator reset the key. The MFA key is automatically reset while the password is reset.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users** > **Users**.
4. Click the **System Users** tab.
5. Find the user for whom you want to reset MFA and click the username.
You can search for the user by username, organization, or role.
6. In the user details panel, click **Reset password**.
