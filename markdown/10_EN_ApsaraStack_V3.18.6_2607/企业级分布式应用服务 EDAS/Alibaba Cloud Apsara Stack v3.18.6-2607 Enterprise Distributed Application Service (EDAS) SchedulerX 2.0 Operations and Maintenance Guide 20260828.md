---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 13
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 Operations and Maintenance Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%20EDAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Enterprise%20Distributed%20Application%20Service%20%28EDAS%29%20SchedulerX%202.0%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 Operations and Maintenance Guide 20260828

cture

## Service architecture

### System architecture

SchedulerX consists of a scheduling cluster, a control system, clients, ZooKeeper, MySQL, and a monitoring and alerting system. The following figure shows the system architecture. Figure 1. SchedulerX service architecture SchedulerX-Console Netty

| Sc | Quartz | Quartz |
|---|---|---|
|   | hedulerX-Server |   |

MySQL ZooKeeper Netty SchedulerX-Client

### Components and their

**functions**

SchedulerX includes the central scheduling cluster (SchedulerX-Server), the web console (SchedulerX-Console), MySQL, and ZooKeeper. The following table describes the functions of SchedulerX and its dependencies. Table 1. SchedulerX components and their functions

| Component group | Component | Function description |
|---|---|---|
| Central scheduling cluster | SchedulerX-Server | Schedules all jobs. |
| Management platform | SchedulerX-Console | The management console for job maintenance and other management operations. |
| Common components | MySQL | Stores job configurations and runtime data. |
| > Document Version: 20260828 |   |   |

| chedulerX 2.0 Operations and M intenance Guide·Service archite ture | Enterprise Distributed Applicatio Service (EDAS |   |
|---|---|---|
| Common components |   |   |
|   | ZooKeeper | Provides distributed locking and service discovery. |
|   | DAuth | Authentication center |

enance

## Routine maintenance

After deployment, SchedulerX requires ongoing operations and maintenance (O&M) to ensure its stability and availability. This maintenance includes managing the middleware components that SchedulerX depends on. The main daily O&M checks are as follows.

### Central scheduling cluster

**inspection**

**Process checks**

The SchedulerX runtime is a Java process. You can use the ps command to check if the process is running normally. Check the service port. Run the netstat –ano |grep 52014 command to check if the port is listening.

| Port | Description |
|---|---|
| 52014 | The listener port for SchedulerX-Server. All network traffic passes through this port. |

To check the runtime status, view the logs in the default path: /home/admin/logs/dts-all- 52014/dts.log. To check the process startup method, log on as the admin user, go to the /home/admin/dtsall/bin folder, and run the `appctl.sh start` command.

**Disk space check**

Check if the disk is full of logs. A large log volume can prevent SchedulerX from responding to service registration requests.

```
df -lh df -lh /home/admin/logs
```

SchedulerX uses a log rolling mechanism. However, you should perform this check as a precaution. Delete old logs if necessary.

**Address server check**

Ensure that you can connect to the address server and that the latency is low. On an internal network, the latency must be less than 10 ms.

```
ping jmenv.tbsite.net
```

### Control platform health check

The SchedulerX Console is a web application that runs in an AliTomcat container. The default HTTP port is 7001. To perform a health check on the control platform, follow these steps:
1. Verify that the Tomcat process is running and that port 7001 is open.
2. Check the logs for any obvious errors and clear unnecessary log files. The default path is:
enance /home/admin/logs/dts-console/

| 3. Log on to the target machine and run |   |
|---|---|
| http://127.0.0.1:7001/dts-console/checkpreload.htm |   |

status.
4. As the admin user, go to the /home/admin/dts-console/bin directory and run **./appctl.sh**
**start**.

### Health checks for basic

**components**

This topic describes the health checks for basic components, such as MySQL, ZooKeeper, and Dauth.

#### MySQL health check

SchedulerX depends on the MySQL database service. Run the following command: telnet ${db_domainName} 3306 . In this command, db_domainName is the domain name of the database. A successful connection indicates that the database service is running correctly.

#### ZooKeeper health check

1. Check the disk space.
ZooKeeper writes data to the disk. If the disk is full, data cannot be added or modified.

```
df -lh df -lh /home/admin/
```

| top | to ensure that sys |
|---|---|
| sh zkServer.sh status |   |

2. Run `top` to ensure that system memory and CPU usage are normal.

#### DAuth health check

DAuth is a web system that is deployed on Tomcat. Perform the following checks.
1. Check if the Tomcat process is running and port 8080 is open.
2. Check if the Nginx process is running and port 80 can forward requests to port 8080.
3. /home/admin/dauth/logs/*.log for any obvious abnormalities.
4. /home/admin/dauth/logs directory.
5. url 'localhost:8080'|grep Unsupported command. The service is running normally if the
output contains "Unsupported".
6. /home/admin directory has sufficient disk space.
Because DAuth is also a Diamond client, perform the following checks:
1. /home/admin/logs/diamond-client/diamond-client.log for any obvious abnormalities.
2. Run the command `curl 'http://jmenv.tbsite.net:8080/diamond-server/diamond-unit-`
`spas'` to retrieve a list of servers for the Diamond SPAS unit. Ping each server and ensure enance the latency is below 10 ms.

### Security maintenance

Regularly change account passwords and use strong passwords to ensure account security. This is especially important for SchedulerX administrator accounts. As needed, configure an Intrusion Detection and Prevention System (IDPS) to monitor internal and external network traffic in real time to prevent abnormal activity and attacks.

## Troubleshooting

### Incident response mechanism

A maintenance team should establish an incident response mechanism to promptly resolve failures or security incidents and resume production.

### Troubleshooting methods

If you find a system fault during routine maintenance, use the O&M features of Scheduler and the system logs to obtain detailed information, analyze the cause, and resolve the fault. If you cannot resolve the fault, collect relevant information, such as system info and fault symptoms, and contact an Alibaba Cloud technical support engineer for assistance. After you resolve a fault, review the issue, summarize your findings, and implement improvements.

### Troubleshooting and O&M

#### SchedulerX console

**The console starts but is inaccessible**

You can run the `systemctl status iptables.service` command to check the network channel, firewall rules, and local iptables rules.

**A security prompt appears after you log on to the console**

When you first access the console, the page automatically redirects to the DAuth secure single sign-on (SSO) interface. Your browser might block the page and show a security warning because of an issue with the certificate that DAuth uses. In this case, you can proceed past the warning. You are then redirected to DAuth to confirm your identity. The page then automatically redirects back to the console.

**The console reports a memory overflow**

The Tomcat startup parameters use a standard configuration, so memory issues are uncommon. If a memory overflow or crash occurs, collect detailed information and contact the helpdesk. After you collect the information, you can restart the Tomcat service to restore operations.

**The console log reports a ZooKeeper connection error**

This error likely indicates a problem with the ZooKeeper cluster. You can log on to the ZooKeeper machine and check the status of the ZooKeeper service.
1. Check if the disk on the ZooKeeper machine is full. If it is, clear the logs, check whether
automatic log cleanup is configured, and then restart ZooKeeper. For configuration details, see the official ZooKeeper documentation.
2. Check if the ZooKeeper process is shut down. If it is, restart ZooKeeper.
3. Restart the console.

#### Central scheduling cluster (SchedulerX-

**Server)**

**ZooKeeper connection issues**

This issue is likely caused by a problem with the ZooKeeper cluster. Log on to the ZooKeeper machine and check the status of the ZooKeeper service.
1. Check if the disk on the ZooKeeper machine is full. If the disk is full, clear the logs and
check if the automatic log cleanup parameter is configured. Then, restart ZooKeeper. For more information about this configuration, see the ZooKeeper documentation.
2. Check if the process has shut down. If it has, restart ZooKeeper.
3. Restart the central scheduling cluster.

**Jobs fail to trigger**

If your application is working correctly, this issue is likely caused by a server error. There are two main reasons for this.
1. A ZooKeeper connection issue. For more information, see ZooKeeper connection issues.
2. The server process is not running. If the ZooKeeper connection is normal, check the status
of the server process. If the process is not running, restart the server.

#### Common basic components: ZooKeeper

**cluster**

Insufficient disk space A full disk is often caused by log files. Check the ZooKeeper log file usage and verify that automatic log cleanup is configured as follows: i. autopurge.purgeInterval This parameter specifies the cleanup frequency in hours. The value must be an integer of 1 or greater. The default value is 0, which disables the automatic cleanup feature. Set the value to 24. ii. autopurge.snapRetainCount This parameter is used with the autopurge.purgeInterval parameter. It specifies the number of files to retain. The default value is 3. Set the value to 7. Missing process Restart the process.

### Connect SchedulerX2 to

**Monitoring and Alerts**

SchedulerX2 integrates container monitoring, process monitoring, and JVM monitoring by connecting to the monitoring and alert system.

**View container and process monitoring data**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Monitoring and Alerts > Cloud Platform Monitoring**.
3. In the **Cloud Platform Monitoring** console, click **Business Monitoring > Cloud Service**
**Monitoring** in the navigation pane on the left.
4. On the **Cloud Service Monitoring** page, enter `SchedulerX` in the search box and click
Search. Click the cloud product in the search results.
5. In the service list, click a service component under **schedulerx2**. On the **Infrastructure**
**Monitoring** tab, click **Container Monitoring** and **Process Monitoring** to view the data.

**View JVM monitoring information**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Monitoring and Alerts > Cloud Platform Monitoring**.
3. In the **Cloud Platform Monitoring** console, click **Business Monitoring > Cloud Service**
**Monitoring** in the navigation pane on the left.
4. On the **Cloud Service Monitoring** page, enter `SchedulerX` in the search box and click
Search. Click the cloud product in the search results.
5. In the service list, find **schedulerx2 > schedulerx2ConsoleRole#**. On the
**Infrastructure Monitoring** tab, click **JVM Monitoring**.

**Alert rules**

1. In the **Cloud Platform Monitoring** console, click **Business Monitoring > Alert Rules** in
the navigation pane on the left.
2. On the **Alert Rules** page, enter `SchedulerX2` in the **Rule Name** search box and click
Search. You can then view and edit the rules.
3. In the **Cloud Platform Monitoring** console, click **Business Monitoring > Alert History**
in the navigation pane on the left to view alert information.
4. On the **Alert History** page, enter `schedulerx2` in the Service Catalog search box and
click Search. You can view the alert information in the alert list.
