---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Security Security Administrator Guide 20241104"
product_version: "V3.18.3"
doc_version: "20241104"
pdf_pages: 18
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Security Security Administrator Guide 20241104.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%BE%E5%9F%BA%E7%A1%80%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Stack%20Security%20Security%20Administrator%20Guide%2020241104.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Security Security Administrator Guide 20241104

## Table of Contents

- 1 Restrictions
- 2 Log on to Cloud Security Operations Center
- 3 Monitoring and alerting
  - 3.1 View the system monitoring data
  - 3.2 View the business monitoring data
- 4 O&M management
  - 4.1 Manage middleware
- 5 Cloud service management
  - 5.1 Server Guard
  - 5.2 NDR
    - 5.2.1 View O&M logs
    - 5.2.2 View the node status
    - 5.2.3 Configure features
- 6 Log diagnosis
  - 6.1 View end-to-end logs
  - 6.2 Use the quick diagnostics feature

trictions

## 1 Restrictions

Before logging on to Apsara Stack Security Center, make sure that your local PC meets the requirements. Table 1. Configuration requirements

| Item | Requirements |
|---|---|
| Browser | Internet Explorer: 11 or later Google Chrome (recommended): 42.0.0 or later Mozilla Firefox: 30 or later Safari: 9.0.2 or later |
| Operating system | Windows XP, Windows 7, or later Mac |

on to Cloud Security Operations Center

## 2 Log on to Cloud Security Operations Center

**Operations Center**

This topic describes how to log on to Cloud Security Operations Center.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

on to Cloud Security Operations Center If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, click **O&M**. In the
left-side navigation pane, choose **Product Management > Products**. On the page that appears, click **Cloud Security Operation Center** in the **Security Services** section.

**Result**

On the **Operations Platform** page, you can view the following information.

## 3 Monitoring and alerting

### 3.1 View the system monitoring data

**data**

You can use the system monitoring feature to monitor integrated cloud services and identify exceptions in the cloud services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the system monitoring data.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Monitoring and Alerting** > **System Monitoring**.
3. On the page that appears, view the monitoring overview and monitoring data of cloud
services. On the **Monitoring Overview** tab, view the following information. Overview: You can view the total numbers of monitored services, abnormal services, metrics, and exceptions. Monitoring data of cloud services: You can view the number of metrics, the number of exceptions, and the statuses of all integrated cloud services. On each cloud service tab, view the monitoring data of each cloud service. Tabs of cloud services: Server Guard, Basic Service, Automated Orchestration, Platform for Connecting to Third-party Services, Data Encryption Service, Threat Intelligence, Intelligent Analytics Platform, Updates, Trusted Computing, NDR, Security Operations Center, Key Management Service, Key Management Service (Base Edition), Password service platform, and Container safety. Monitoring scope: Click a cloud service tab to view all sub-services of the cloud service in the section marked 2 in the preceding figure. On a cloud service tab, use the search box marked 1 in the preceding figure to search for the required sub-service by service status and name. In a sub-service card marked 3 in the preceding figure, view the information such as the service status, CPU utilization, memory usage, workloads, TCP connections, processes, and the QPS of NGINX. Click a sub-service card marked 3 in the preceding figure. On the page that appears, view the monitoring details of the cloud service.

| Catego ry | Description |
|---|---|
| Basic monitor ing | You can specify the monitoring time range and monitoring view to view the details of basic monitoring and middleware monitoring. Valid values for the time range: 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually refresh the monitoring data. You can also turn on Automatic Refresh to automatically refresh the monitoring data. Valid values for the View parameter: Cluster View and Single-server View. You can view the following metrics: CPU usage (%), memory capacity (%), workloads, the number of TCP connections, the number of processes, and the QPS of NGINX. |
| Middle ware | You can specify the monitoring time range and monitoring view to view the details of basic monitoring and middleware monitoring. Valid values for the time range: 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually refresh the monitoring data. You can also turn on Automatic Refresh to automatically refresh the monitoring data. Valid values for the View parameter: Cluster View and Single-server View. You can view the following monitoring data: the QPS of MetaQ, the number of GCs in the JVM, the amount of time consumed to monitor GCs in the JVM, the amount of JVM memory, the number of loaded classes in the JVM, the numbers of JVM threads in different statuses, the number of JVM threads, the QPS of HSF, the response time of HSF (ms), and database usage (%). |
| Health check | Check the health status of all hosts in an application by using TCP or HTTP. |

### 3.2 View the business monitoring data

**data**

You can use the business monitoring feature to monitor the statuses of integrated cloud services. This topic describes how to view the business monitoring data.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Monitoring and Alerting** > **Monitoring**.
3. On the page that appears, view the business monitoring data of Apsara Stack Security
services on tabs. You can view the following business monitoring data: On the **Basic services** tab, you can view the monitoring details of **YundunConsole** and
**YundunBaseService**.
On the **Server Guard** tab, you can view the monitoring details of Asset exposure, Attack Analysis, Alarm Event, application whitelisting, Virus detection and killing, Asset fingerprint, log, File collection, Binary detection, Webshell detection, Malicious script detection, vulnerability, baseline, tamper resistant, Cloud Anti Virus, Client, and Asset grayscale. On the **NDR** tab, you can view the monitoring details of Network Detection and Response (NDR). On the **Security Auditlog** tab, you can view the monitoring details of **Original Log** and
**Audit events**.
On the **Container Security** tab, you can view the monitoring details of Container assets, Mirror scanning, CICD, Container firewall, Container vulnerability, and Container alarm. On the **Security Operations Center** tab, you can view the monitoring details of SocApp and SiemApp. M management

## 4 O&M management

### 4.1 Manage middleware

Cloud Security Operations Center allows you to manage middleware such as Diamond, Tair, ScheduleX, Dubbo, OpenAPI, and MetaQ. This topic describes how to manage Apsara Stack Security middleware.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **O&M management** > **Middleware**
**Management**.
3. On the **Middleware** page, manage middleware.

**Manage Diamond**

Click the **Diamond Management** tab, configure the following parameters, and then click
**Search**. Then, find the required middleware and then click **Save**.

| Parameter | Description |
|---|---|
| Data ID | Enter the data ID of the Diamond middleware. |
| Group ID | Enter the group ID of the Diamond middleware. |
| Application | Enter the application to which the Diamond middleware belongs. |
| Configuration Body | Enter the configuration content of the Diamond middleware. |

**Manage Tair**

Click the **Tair Management** tab, configure the following parameters, and then click
**Submit**.

| Parameter | Description |
|---|---|
| Operation | Select the operation that you want the Tair middleware to perform. Valid values: Query, Edit, and Delete. |
| ns | Enter the name server (NS) record of the Tair middleware. |
| key | Specify the type of the key of the Tair middleware and enter a value for the Key parameter. |

M management

| value | Specify the type of the value of the Tair middleware and enter a value for the Value parameter. |
|---|---|

**Manage ScheduleX**

On the **ScheduleX Management** tab, click **Create Job**, configure the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| API Operation for Processing Job | Enter the full name of the class that is used to process the job. |
| Trigger Method | Select the method that is used to trigger the job. |
| Trigger Execution as Intended | After you select this option, if the job is being executed, the job will be triggered and executed as expected when the next triggering time arrives. |
| Cron Expression | Enter the Quartz time expression. |
| Job Description | Enter a description for the job. |
| Custom Parameter | Enter the string of the custom job. Custom formats are supported. For example, you can enter a JSON string. |

**Manage Dubbo**

Click the **Dubbo Debugging** tab, configure the request parameters, and then click
**Execution**. Then, view the debugging result in the Return Results section.

| Parameter | Description |
|---|---|
| RPC Operation Name | Enter the name of the Remote Procedure Call (RPC) operation for Dubbo debugging. |
| RPC Version | Enter the RPC version for Dubbo debugging. |
| RPC Method | Enter the RPC method that you want to use for Dubbo debugging. |
| RPC Group | Enter the RPC group for Dubbo debugging. |
| RPC Parameter | Enter the parameter type and parameter value for Dubbo debugging. |

M management

**Manage APIs**

Click the **API Debugging** tab, configure the request parameters, and then click **Execute**. Then, view the debugging result in the Return Results section.

| Parameter | Description |
|---|---|
| Request Method | Enter the method for API debugging. |
| Service Name | Enter the name of the service for API debugging. |
| API Version | Enter the version of the operation for API debugging. |
| Operation Name | Enter the name of the operation for API debugging. |
| AccessKeyId | Enter the AccessKey ID for API debugging. |
| AccessKeySecret | Enter the AccessKey secret for API debugging. |
| SecurityToken | Enter the token for API debugging. |
| Domain | Enter the name of the domain for API debugging. |
| POP Parameters | Enter the POP parameters for API debugging. |

**Manage MetaQ**

Click the **Metaq Management** tab, configure the following parameters, and then click
**Send**.

| Parameter | Description |
|---|---|
| Topic | Enetr the topic of the MetaQ middleware. |
| Tag | Enter the tag of the MetaQ middleware. |
| Message Content | Enter the message body of the MetaQ middleware. |

ud service management

## 5 Cloud service management

### 5.1 Server Guard

### 5.2 NDR

#### 5.2.1 View O&M logs

O&M logs include the resource utilization and mirrored traffic logs of Network Detection and Response (NDR). This topic describes how to view the O&M logs of NDR.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services** > **Network Detection and**
**Response** > **O&M Logs**.
3. On the **O & M log** page, view the O&M logs that are generated within the current day, last
day, last 7 days, last 30 days, or a custom time range. The O&M log list displays the log creation time, log type, and log content. You can search O&M logs by event type and keyword.

#### 5.2.2 View the node status

You can view a Network Detection and Response (NDR) node and the status trend of the node. This topic describes how to view the status of an NDR node.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services** > **Network Detection and**
**Response** > **Node Status**.
3. On the page that appears, select the required node and view all physical nodes and the
status trend of the node. You can view the status trend of the node from the following dimensions: CPU utilization (%) Memory usage (%) Overall inbound traffic (Mbit/s) Overall outbound traffic (Mbit/s) Packet loss rate (%) You can view the status trend of the node within a specific time range. The time range can be 30 minutes, 6 hours, 24 hours, 7 days, 30 days, or a custom time range.

#### 5.2.3 Configure features

You can enable or disable features such as malicious IP address filtering and interaction with Anti-DDoS Pro or Anti-DDoS Premium. This topic describes how to configure the features. ud service management
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services** > **Network Detection and**
**Response** > **Feature Configuration**.
3. On the **Function configuration** page, turn on or turn off **Malicious IP access filtering**
and **DDoS anti-DDoS** to enable or disable the features. By default, **Malicious IP access filtering** is turned on. If this feature is enabled, the feature takes effect on the platform and tenant sides. The feature helps automatically filter out and block Internet access from malicious IP addresses. The malicious IP addresses are recorded in a threat intelligence library. By default, **DDoS anti-DDoS** is turned off. If this feature is enabled, the interaction between Anti-DDoS Service and anti-DDoS mitigation policies is implemented. In addition, the features related to account management in Apsara Stack Security are enabled. diagnosis

## 6 Log diagnosis

### 6.1 View end-to-end logs

This topic describes how to use the end-to-end log tracing feature to view end-to-end logs in the Logstore of Apsara Stack Security.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Log Diagnostics** > **End-to-end Log Tracing**.
3. On the **End-to-end Link Log** page, view the end-to-end logs.
You can use the following search conditions to query end-to-end logs.

| Search condition | Description |
|---|---|
| Logstore type | The type of the Logstore that you want to query. Valid values: Platform link logs yundun-luban link log secure-service link log oem link log yundun-soc link log audit-log link log |
| Time range | The start and end time of the query. |
| Keyword | The keyword that you want to use. Fuzzy search and exact search are supported. |

### 6.2 Use the quick diagnostics feature

**feature**

This topic describes how to use the quick diagnostics feature to create a diagnostic task to identify issues on a service.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Log Diagnostics** > **Quick Diagnostics**.
3. On the **One-click diagnosis** page, click **Create diagnostic tasks**. In the panel that
appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|

diagnosis

| Diagnostic products | Select the Apsara Stack Security service for which you want to use the quick diagnostics feature. |
|---|---|
| Diagnose problems | Select the issue that you want to identify for the selected Alibaba Cloud Security service. |
| Parameter configuration | In this section, configure the Inspection configuration parameter. If you set the Inspection configuration parameter to Enabled, you must specify the Inspection cycle field. Valid values of the field: Interval 3 days, 1 week interval, Interval 2 weeks, and The interval is 1 month. |

4. Click **Diagnosis** in the **Operation** column of the created diagnostic task. In the **Tips** dialog
box, click **OK**. In this case, the diagnostic task is in the **Under diagnosis** state. After the diagnostics is complete, the diagnostic task enters the **Diagnosis completed** state. You can view the status of a diagnostic task in the **Current diagnostic task progress** column. You can perform the following operations on the One-click diagnosis page: Configure search conditions to query a diagnostic task. The following table describes the search conditions.

| Search condition | Description |
|---|---|
| Start time and End time | The start time and end time of the query. |
| Product classification | The service type of the diagnostic task that you want to query. |
| Diagnostic progress | The progress of the diagnostic task that you want to query. |
| Diagnosis Results | The diagnostic result of the diagnostic task that you want to query. Valid values: All through and There is a failure item. |

Click **View historical tasks** in the **Operation** column of a diagnostic task to view all historical diagnostic tasks. Click **Edit**, **Delete**, or **Download** in the Operation column of a diagnostic task to edit, delete, or download the diagnostic task.
