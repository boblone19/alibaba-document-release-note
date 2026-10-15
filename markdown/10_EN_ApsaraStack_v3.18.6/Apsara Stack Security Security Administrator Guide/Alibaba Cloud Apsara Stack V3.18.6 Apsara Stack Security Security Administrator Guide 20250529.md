---
title: "Apsara Stack Security Security Administrator Guide 20250529"
product_version: "V3.18.6"
doc_version: "20250529"
pdf_pages: 38
source_pdf: "41ad4128af759968_Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Security Security Administrator Guide 20250529.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE%E5%9F%BA%E7%A1%80%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Security%20Security%20Administrator%20Guide%2020250529.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Apsara Stack Security Security Administrator Guide 20250529

## Table of Contents

- 1 Restrictions
- 2 Log on to Cloud Security Operations Center
- 3 Monitoring and alerting
  - 3.1 View the system monitoring data
  - 3.2 View the business monitoring data
  - 3.3 Configure alert contacts
- 4 O&M management
  - 4.1 Manage middleware
- 5 Cloud service management
  - 5.1 Server Guard
    - 5.1.1 Manage high-risk items and canary release policies
  - 5.2 NDR
    - 5.2.1 View O&M logs
    - 5.2.2 View the node status
    - 5.2.3 Configure features
  - 5.3 KMS
    - 5.3.1 Manage resources
    - 5.3.2 Manage tasks
    - 5.3.3 Manage throttling rules
    - 5.3.4 Manage user quotas
    - 5.3.5 Configure global quotas
    - 5.3.6 Configure global settings
- 6 Updates
  - 6.1 Synchronization overview
  - 6.2 Update feature libraries or the version of Apsara Stack Security
- 7 Log diagnosis
  - 7.1 View end-to-end logs
  - 7.2 Use the quick diagnostics feature
  - 7.3 Use the frontend monitoring feature
- 8 Security Audit
  - 8.1 Overview
  - 8.2 View the summary information about security audit
  - 8.3 Query audit events
  - 8.4 View raw logs
  - 8.5 View the number of logs
  - 8.6 Policy settings
    - 8.6.1 Manage audit rules
    - 8.6.2 Configure alert recipients
    - 8.6.3 Query the archives of audit events and raw logs
    - 8.6.4 Download exported audit events or logs
    - 8.6.5 Modify system settings

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

Cloud Security Operations Center is an operations platform for Apsara Stack Security services. You can use the platform to monitor the statuses and workloads of Apsara Stack Security services and notifies users of alerts. This topic describes how to log on to Apsara Stack Security Center to implement real-time monitoring.

**Prerequisites**

The URL, username, and password that are required to log on to the Apsara Uni-manager Operations Console are obtained from the deployment personnel or administrators. The URL of the Apsara Uni-manager Operations Console is in the format of regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the URL. Then, press the Enter key.

**Note**

You can select a language from the drop-down list in the upper-right corner of the page.
3. Enter your username and password.

**Note**

To obtain the username and password that are used to log on to the Apsara Unimanager Operations Console, contact the deployment personnel or administrators. If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username as prompted. To enhance security, make sure that the password meets the following requirements: The password contains uppercase and lowercase letters. on to Cloud Security Operations Center The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
4. Click **Log On**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Apsara Stack Security**.

**Result**

On the **Cloud Security Operations Center** page, you can view the following information. nitoring and alerting

## 3 Monitoring and alerting

### 3.1 View the system monitoring data

**data**

You can use the system monitoring feature to monitor integrated cloud services and identify exceptions in the cloud services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the system monitoring data.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Monitoring and Alerting** > **System Monitoring**.
3. On the page that appears, view the monitoring overview and monitoring data of cloud
services. On the **Monitoring Overview** tab, view the following information. Overview: You can view the total numbers of monitored services, abnormal services, metrics, and exceptions. Monitoring data of cloud services: You can view the number of metrics, the number of exceptions, and the statuses of all integrated cloud services. On each cloud service tab, view the monitoring data of each cloud service. Tabs of cloud services: Server Guard, Basic Service, Automated Orchestration, Platform for Connecting to Third-party Services, Data Encryption Service, Threat Intelligence, Intelligent Analytics Platform, Updates, Trusted Computing, NDR, Security Operations Center, Key Management Service, Key Management Service (Base Edition), Password service platform, and Container safety. nitoring and alerting Monitoring scope: Click a cloud service tab to view all sub-services of the cloud service in the section marked 2 in the preceding figure. On a cloud service tab, use the search box marked 1 in the preceding figure to search for the required sub-service by service status and name. In a sub-service card marked 3 in the preceding figure, view the information such as the service status, CPU utilization, memory usage, workloads, TCP connections, processes, and the QPS of NGINX. nitoring and alerting Click a sub-service card marked 3 in the preceding figure. On the page that appears, view the monitoring details of the cloud service.

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
services on tabs. nitoring and alerting You can view the following business monitoring data: On the **Basic services** tab, you can view the monitoring details of **YundunConsole** and
**YundunBaseService**.
On the **Server Guard** tab, you can view the monitoring details of Asset exposure, Attack Analysis, Alarm Event, application whitelisting, Virus detection and killing, Asset fingerprint, log, File collection, Binary detection, Webshell detection, Malicious script detection, vulnerability, baseline, tamper resistant, Cloud Anti Virus, Client, and Asset grayscale. On the **NDR** tab, you can view the monitoring details of Network Detection and Response (NDR). On the **Security Auditlog** tab, you can view the monitoring details of **Original Log** and
**Audit events**.
On the **Container Security** tab, you can view the monitoring details of Container assets, Mirror scanning, CICD, Container firewall, Container vulnerability, and Container alarm. On the **Security Operations Center** tab, you can view the monitoring details of SocApp and SiemApp.

### 3.3 Configure alert contacts

This topic describes how to configure and manage alert contacts.

**Background information**

Apsara Stack Security sends alert notifications to alert contacts by text message or email. If the detected information matches an alert rule, Apsara Stack Security sends an alert notification to the alert contacts.
1. Log on to Cloud Security Operations Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Global**
**Platform Security** section, click **Alibaba Cloud Security**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the **Alert Settings** page, click the **Alert Recipient** tab.
5. Click **Add Recipient**.
6. Enter the contact information and click **OK**.
7. Manage alert contacts.
In the contact list, find a contact whose information you want to modify and click **Edit** in the Actions column. M management

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

#### 5.1.1 Manage high-risk items and canary release policies

**release policies**

This topic describes how to manage high-risk items and canary release policies for Server Guard.

**High-risk Items**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > Server Guard O&M > High-**
**risk Items**.
3. Manage high-risk items for Server Guard.
**Physical Server Guard/Vulnerability Management**: This feature is disabled by
default. After you enable the feature, the Server Guard vulnerability management feature is enabled for physical servers. Enabling this feature may expose physical server to vulnerabilities. Proceed with caution.
**Physical Server Guard/Baseline Check**: This feature is disabled by default. After you
enable this feature, the Server Guard baseline inspection feature is enabled for physical servers. Proceed with caution.
**Tenant Server Knight Multi-Level Organization Switch**: This feature is disabled by
default. After you enable this feature, the multi-level organization perspective feature is enabled for Server Guard on the tenant side. It may require a long period of time to enable the feature because a large amount of data needs to be updated. Before you enable the feature, you must apply for an O&M code. The feature cannot be disabled after it is enabled. Proceed with caution.
**ASCM - Apsara Stack Security Data Synchronization**: You can click **Synchronize**
**Data** to manually synchronize data from the Apsara Stack Cloud Management (ASCM)
console to Apsara Stack Security. The data includes information about organizations, resource sets, and assets. It may require a long period of time to synchronize data because a large amount of data needs to be updated. Before the data synchronization, you must apply for an O&M code. Proceed with caution.

**Canary Release Policy Management**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > Server Guard O&M > Canary**
**Release Policy Management**.
3. Manage canary release policies for Server Guard.
On the **Plug-in Publish Management** tab, manage the canary release policy of an extension. Find the required extension and click**View** or **Edit** in the Actions column. In the upper-right corner of the Plug-in Publish Management tab, click the icon to configure the items that you want to view in the extension list. ud service management In the upper-right corner of the Plug-in Publish Management tab, turn on or off **Canary**
**Release Policy Switch**.
On the **Blocking Policy Management** tab, click **Create Blocking Policy**. In the Publish Blocking Policy dialog box, configure the Plug-in Name, Operation Type, Dimension, Source, Unit, Value, and Threshold parameters. Then, click **OK**. After the policy is created, you can modify or delete it. In the upper-right corner of the Blocking Policy Management tab, click the icon to configure the items that you want to view in the extension list. On the **Canary Release Monitoring on Asset** tab, monitor the gray scale of assets. You can find the required asset and push the latest version for the asset, pause the push, and view the push details of the asset. You can also select multiple assets and choose **Batch Operation > Pause** to pause the push of multiple assets at a time.

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
status trend of the node. You can view the status trend of the node from the following dimensions: CPU utilization (%) Memory usage (%) Overall inbound traffic (Mbit/s) Overall outbound traffic (Mbit/s) ud service management Packet loss rate (%) You can view the status trend of the node within a specific time range. The time range can be 30 minutes, 6 hours, 24 hours, 7 days, 30 days, or a custom time range.

#### 5.2.3 Configure features

You can enable or disable features such as malicious IP address filtering and interaction with Anti-DDoS Pro or Anti-DDoS Premium. This topic describes how to configure the features.
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services** > **Network Detection and**
**Response** > **Feature Configuration**.
3. On the **Function configuration** page, turn on or turn off **Malicious IP access filtering**
and **DDoS anti-DDoS** to enable or disable the features. By default, **Malicious IP access filtering** is turned on. If this feature is enabled, the feature takes effect on the platform and tenant sides. The feature helps automatically filter out and block Internet access from malicious IP addresses. The malicious IP addresses are recorded in a threat intelligence library. By default, **DDoS anti-DDoS** is turned off. If this feature is enabled, the interaction between Anti-DDoS Service and anti-DDoS mitigation policies is implemented. In addition, the features related to account management in Apsara Stack Security are enabled.

### 5.3 KMS

#### 5.3.1 Manage resources

This topic describes how to manage resources. You can register and initialize resources.
1. Log on to Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Cloud Services** > **KMS O&M** > **Tenant-side**
**KMS O&M**.
3. On the **Resources** tab, click **Register Resource**. In the **Register Resource** dialog box,
configure the parameters that are described in the following table and click **OK**. KMS-managed HSMs

| Parameter | Description |
|---|---|
| Zone | The zone in which you want to deploy the hardware security module (HSM). |
| Manufacturer | The manufacturer of the HSM. The value of this parameter is automatically provided based on the value of the HSM Model parameter. You do not need to configure this parameter. |

ud service management

| HSM Model | The model of the HSM. Make sure that you select the actual model in use. |
|---|---|
| HSM IP Address | The IP address of the HSM. Enter an IP address that is planned by Deployment Planner. Example: 10.4.XX.XX. If you select a virtual security module (VSM) as HSM Model, enter the IP address of the VSM. |

Cloud Hardware Security Module-managed HSMs

**Important**

If you have already registered Key Management Service (KMS)-managed HSMs, the Cloud Hardware Security Module-managed HSMs tab is dimmed.

| Parameter | Description |
|---|---|
| Zone | The zone in which you want to deploy the HSM. |
| Manufacturer | The manufacturer of the HSM. |
| HSM Model | The model of the HSM. Make sure that you select the actual model in use. |
| HSM | The HSM that you want to register. |

4. Initialize the HSM.
i. In the left-side navigation pane, choose **Cloud Services** > **KMS O&M** > **Tenant-side**
**KMS O&M**.
ii. On the **Resources** tab, click **Initialize HSM**. In the **Initialize HSM** message, click **OK**.

**Note**

If the number of VSMs is smaller than 3, you cannot initialize the HSM. After the initialization request is submitted, the system generates an O&M task. You can choose **Cloud Services** > **KMS O&M** > **Tenant-side KMS**
**O&M** in the left-side navigation pane to go to the Tenant-side KMS O&M page
and view the status of the O&M task on the **Tasks** tab. After the HSM is initialized, health check tasks for the HSM are continuously added to the task list. You can use HSM-related features.
5. Disable the HSM.
i. In the left-side navigation pane, choose **Cloud Services** > **KMS O&M** > **Tenant-side**
**KMS O&M**.
ii. On the **Resources** tab, find the HSM that you want to disable and click **Bring Offline** in the **Actions** column. ud service management iii. Obtain the O&M code for this operation from Apsara Stack technical support as prompted, enter the O&M code in the field, and then click **OK**.

#### 5.3.2 Manage tasks

This topic describes how to view existing tasks on the Tasks tab.
1. Log on to Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > KMS O&M > Tenant-side**
**KMS O&M**.
3. On the Tenant-side KMS O&M page, click the **Tasks** tab. On the Tasks tab, configure the
**Type**, **Status**, or **ID** parameter to search for the task that you want to query.
4. Click the
icon to the left of the task ID to query the execution information about its subtasks.

#### 5.3.3 Manage throttling rules

This topic describes how to create and modify a throttling rule.

**Create a throttling rule**

1. Log on to the KMS O&M platform.
2. In the left-side navigation pane, choose **O&M Management > Throttling**.
3. On the **Throttling** tab, click **Create Rule**.
4. In the **Create Rule** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Resources | The name of the resource. Valid values: s: share d: default |
| Source | The method to combine user and service IDs for your application. Valid values: d: combines all user and service IDs. This is the default value. d d: combines default user and service IDs. _ |
| Threshold | The threshold for throttling. |
| Throttling Policy | Standalone Throttling: Throttling is implemented on a single KMS API operation. Standalone Token Bucket: Throttling is implemented on a single user. |
| Unit | The time unit for throttling. |
| Ticket ID | The ID of the change ticket in your change management system. If no tickets are created, enter 0. |

ud service management

| Ticket Link | The link for the change ticket in your change management system. If no tickets are created, enter ignore. |
|---|---|
| Description | The description for your operation. Both Chinese and English are supported. |

5. Click **OK**.

**Modify a throttling rule**

1. Log on to the KMS O&M platform.
2. In the left-side navigation pane, choose **O&M Management > Throttling**.
3. On the **Throttling** tab, find the throttling rule that you want to modify and click **Modify** in
the **Resources** column.
4. In the **Modify** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Threshold | The threshold for throttling. Note If you want to change the threshold, you must change it for two rules. One rule has Resources set to s and Source to d. The other rule has Resources set to s and Source to d d. _ |
| Throttling Policy | Standalone Throttling: Throttling is implemented on a single KMS API operation. Standalone Token Bucket: Throttling is implemented on a single user. |
| Unit | The time unit for throttling. |
| Ticket ID | The ID of the change ticket in your change management system. If no tickets are created, enter 0. |
| Ticket Link | The link for the change ticket in your change management system. If no tickets are created, enter ignore. |
| Description | The description for your operation. Both Chinese and English are supported. |

5. Click **OK**.

**What to do next**

After a throttling rule is created or modified, the system generates an O&M event. You can view the details about the event by choosing **O&M Management > Event**. You can also view the task status for the event by choosing **O&M Management > Tasks**.

#### 5.3.4 Manage user quotas

This topic describes how to create and modify user quotas.

**Create a user quota**

1. Log on to the KMS O&M platform.
ud service management
2. In the left-side navigation pane, choose **O&M Management > User Quotas**.
3. On the **User Quotas** tab, click **Create Quota**.
4. In the **Create Quota** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| User ID | The ID of the user. |
| Maximum Number of Key Versions | The maximum number of key versions that can be created. |
| Maximum Number of Aliases | The maximum number of aliases that can be created. |
| Ticket ID | The ID of the change ticket in your change management system. If no tickets are created, enter 0. |
| Ticket Link | The link for the change ticket in your change management system. If no tickets are created, enter ignore. |
| Description | The description for your operation. Both Chinese and English are supported. |

5. Click **OK**.

**Modify a user quota**

1. Log on to the KMS O&M platform.
2. In the left-side navigation pane, choose **O&M Management > User Quotas**.
3. On the **User Quotas** tab, find the ID of the user whose quota you want to modify and click
**Modify** in the **Actions** column.
4. In the **Modify** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Maximum Number of Key Versions | The maximum number of key versions that can be created. |
| Maximum Number of Aliases | The maximum number of aliases that can be created. |
| Ticket ID | The ID of the change ticket in your change management system. If no tickets are created, enter 0. |
| Ticket Link | The link for the change ticket in your change management system. If no tickets are created, enter ignore. |
| Description | The description for your operation. Both Chinese and English are supported. |

5. Click **OK**.

**What to do next**

After a user quota is created or modified, the system generates an O&M event. You can view the details about the event by choosing **O&M Management > Event**. You can also view the task status for the event by choosing **O&M Management > Tasks**. ud service management

#### 5.3.5 Configure global quotas

This topic describes how to configure global quotas.
1. Log on to the KMS O&M platform.
2. In the left-side navigation pane, choose **O&M Management > Global Quotas**.
3. On the **Global Quotas** tab, find the required Hardware Security Module (HSM) and click
**Modify** in the Actions column.
4. In the **Modify** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Max count | The maximum number of key versions. |
| Ticket ID | The ID of the change ticket in your change management system. If no tickets are created, enter 0. |
| Ticket Link | The link for the change ticket in your change management system. If no tickets are created, enter ignore. |
| Description | The description for your operation. Both Chinese and English are supported. |

**Note**

After the global quota is modified, the system generates an O&M event. You can view the details about the event by choosing **O&M Management > Event**. You can also view the task status for the event by choosing **O&M Management >**
**Tasks**.

#### 5.3.6 Configure global settings

By default, TASS Crypto Engine hardware security modules (HSMs) do not support ShangMi (SM) algorithms. If your business requires SM algorithms, you need to turn on HSMs (TASSCryptoEngine) Support SM Algorithms on the Global Settings tab. This topic describes how to enable TASS Crypto Engine HSMs to support SM algorithms.

**Warning**

By default, this feature is disabled. After this feature is enabled, TASS Crypto Engine HSMs support the SM2 and SM4 algorithms. Use of this feature outside the Chinese mainland must comply with all applicable local laws and regulations. Enable this feature with caution.
1. Log on to Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > KMS O&M > Tenant-side**
**KMS O&M**.
3. On the Tenant-side KMS O&M page, click the **Global Settings** tab. On the Global Settings
tab, turn on or off **HSMs (TASSCryptoEngine) Support SM Algorithms**. dates

## 6 Updates

### 6.1 Synchronization overview

This function synchronizes specific security information such as rule databases and vulnerabilities from Alibaba Cloud to Apsara Stack. Rule databases are in the initial status before being synchronized from Alibaba Cloud. Only rule databases on Alibaba Cloud can be synchronized to Apsara Stack. The synchronized rules are used in functional modules of Apsara Stack Security to ensure that the security capabilities of Alibaba Cloud are provided in Apsara Stack. The rule database information and rule database synchronization frequency and time can be set by the administrator. The synchronization can also be triggered automatically. If the administrator do not set the synchronization frequency and time, the default settings will apply. Table 1. Synchronization status description

| Status | Description |
|---|---|
| To Be Upgraded | Indicates that a new version of the rule database is available for upgrade. |
| Upgrading | Indicates that the rule database is being downloaded from Alibaba Cloud or is being upgraded. |
| Upgraded | Indicates that the rule database has been upgraded. |
| Upgrade Failed | Indicates that the rule database failed to be upgraded. |

Rule databases can be synchronized from Alibaba Cloud through online upgrade or offline upgrade by importing upgrade package, depending on the deployment mode of Apsara Stack.

### 6.2 Update feature libraries or the version of Apsara Stack Security

**version of Apsara Stack Security**

The upgrade center supports automatic import and manual import of update packages. You can use the update packages to update feature libraries or the version of Apsara Stack Security. This topic describes how to update feature libraries or the version of Apsara Stack Security.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Upgrade Center**.
4. On the **Upgrade configuration** tab, configure Upgrade Package Import.

**Manual import**

dates If your Apsara Stack environment is inaccessible over the Internet, you can manually import update packages to update feature libraries or the version of Apsara Stack Security. a. Set Upgrade Package Import to **Offline Manual Import** and click **Generate Upgrade**
**Identifier**. Then, download update packages. For more information, see Download
update packages. b. Click Import Upgrade Package and drag the downloaded update packages to the dotted box. You can also click the icon to upload the update packages.

**Note**

Before you upload the update packages, click the link in the **Manually Import**
**offline upgrade packages**dialog box and trust the certificate.
After you import the update packages, you can view the update packages on the Feature Library Upgrade page and Version Upgrade page and perform updates.

**Automatic import**

If the Apsara Stack environment can connect to the Internet, you can select the automatic import method to import update packages and update feature libraries or the version of Apsara Stack Security. a. Set Upgrade Package Import to **Online Automatic Import** and configure the parameters.

| Parameter | Description |
|---|---|
| Alibaba Cloud account ID | Enter the ID of your Apsara Stack tenant account. |
| Access Key | Enter the AccessKey ID of the account. |
| Access Secret | Enter an AccessKey secret of the account. |
| Automatic upgrade time period | Select a time period for automatic updates. Valid values: 0-6 when 0-8 when 0-24 when 22-6 when |

b. Click **Connectivity test**. c. If the connectivity test is successful, turn on **Automatic update**. After **Automatic update** is turned on, the system automatically downloads update packages at regular intervals
5. Update feature libraries or the version of Apsara Stack Security.

**Update feature libraries**

Batch update: On the **Feature Library Upgrade** tab, click **One-click upgrade**. dates Update a service in Apsara Stack Security: Find the service that you want to update on the **Feature Library Upgrade** tab and click **Upgrade now** in the **Operation** column. After the update is complete, the status of the service is **Upgrade successful**. If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: On the **Feature Library Upgrade** tab, find the service and click **Version Details** in the **Operation** column to view the versions of the updated rule libraries. You can click **Restart Upgrade** to update a rule library in a feature library. In the **Feature Library Upgrade Records**panel, find the feature library that you want to view and click **Details** in the **Operation** column to view the details of the feature library update package. You can find a rule library and click **Restart**
**Upgrade** in the **Operation** column to update the rule library.
On the **Feature Library Upgrade** tab, find the service and click **Upgrade Records** in the **Operation** column to view the versions of the updated feature libraries.

**Update the version of Apsara Stack Security**

Batch upgrade: On the **Version Upgrade** tab, click **One-click upgrade**. Update a service in Apsara Stack Security: Find the service that you want to update on the **Version Upgrade** tab and click **Upgrade now** in the **Operation** column. After the update is complete, the status of the service is **Upgrade successful**. If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: Click **Upgrade Records** in the **Operation** column to view the versions of the updated feature libraries. You can also click **Restart Upgrade** or **Rollback**. diagnosis

## 7 Log diagnosis

### 7.1 View end-to-end logs

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

### 7.2 Use the quick diagnostics feature

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

### 7.3 Use the frontend monitoring feature

**feature**

This topic describes how to use the frontend monitoring feature to view the monitoring result of an Apsara Stack Security service in a specified period of time. diagnosis
1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Log Diagnostics** > **Frontend Monitoring**.
3. On the **Frontend Monitoring** page, view the frontend diagnostic details.
You can perform the following operations: Search for the frontend monitoring information about an Apsara Stack Security service by service name, period of time, UID of an Apsara Stack tenant account, and network status. View the following information:
**API Errors**: Occurred At, aliUid, Operation Name, Request Method, Error Code, and
Error Message
**GUI Errors**: Occurred At, aliUid, and GUI Detection Node
**Resource Loading Failures**: Occurred At, aliUid, Error Description, Resource URL,
and Resource Tag
**Script Errors**: Occurred At, aliUid, Error Description, Error Reported by promise, and
Error Reported by react
**Page Performance Errors**: Occurred At, aliUid, Network Status, Connection Duration,
Response Duration, Request Duration, SSL Connection Duration, First Packet Time, Page Loading Duration, and Event Loading Duration Click **View Details** in the **Actions** column of an error. In the panel that appears, view the details of the error. urity Audit

## 8 Security Audit

### 8.1 Overview

A security audit refers to the systemic and independent inspection and verification of activities and behavior in the computer network environment. Delegated by property owners and authorized by management authorities, professional auditors give their assessments according to relevant laws and regulations. When the administrator needs to backtrack system operations, the administrator can perform a security audit. Security audits are long-term security management activities throughout the lifecycle of cloud services. The security audit feature of Apsara Stack Security can collect system security data, analyze weaknesses in system operations, report audit events, and classify audit events into important, moderate, and low risk levels. The security administrator views and analyzes audit events to continuously improve the system and ensure the security and reliability of cloud services.

### 8.2 View the summary information about security audit

**information about security audit**

This topic describes how to view the summary information about security audit.

**Background information**

The **Overview** tab provides reports on the raw log trend, audit event trend, audit risk distribution, and security event distribution. The reports are displayed in run charts or pie charts to help security administrators analyze the trend of risks in your cloud services. On the **Overview** tab, security administrators can check the number of logs and the storage usage in a specific time range.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management**, and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Overview** tab.
4. On the **Overview** tab, view the audit summary for the last seven days.
Trends of Raw Log This chart displays the trend of logs that are generated by **Server**, **Network Device**,
**ECS**, **Cloud Products**, **Tenant Database**, or **Platform Database** in the last seven
days. Security administrators can analyze the trend to check whether the number of logs is at a normal level. You can select the modules that you want the system to display above the chart. Audit Events This chart displays the trend of audit events that are generated by **Server**, **Network**
**Device**, **ECS**, **Cloud Products**, **Tenant Database**, or **Platform Database** in the last
seven days. Security administrators can analyze the trend to check whether the number of audit events is at a normal level. Audit Risk Distribution urity Audit This chart displays the percentage distribution of audit events at different risk levels in the last seven days. Risk levels are important, moderate, and low. Security administrators can analyze the trend to check whether the audit events are at acceptable risk levels. Security Issue Distribution This chart displays the percentage distribution of the following types of events in the last seven days: **Process Error**, **Logon Attempt**, **Account**, and **Account Creation**. Security administrators can analyze this chart to check for the most frequent audit events and identify high-risk events to improve security protection. Log Size This chart displays the volume of online logs and offline logs. If the logs consume a large number of storage resources, we recommend that you back up the required audit logs and delete unnecessary logs. Audit Log Size This chart displays the size of logs for each audit type.
5. View the audit summary in a specific time range.
i. Specify **End Time** as the end of the time range to query. ii. In the **Audit Type** section, select the audit types that you want to query. iii. Click **View** to query the audit summary in the last seven days before the specified end time.

### 8.3 Query audit events

This topic describes how to query audit events.

**Background information**

On the **Audit Query** tab, you can view the details of audit events, including the log creation time, audit type, audit object, action type, risk level, and log content. The system matches the logs that are collected by a security audit module against audit rules. If the log content matches an audit rule, an audit event is reported.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Audit Query** tab.
4. On the **Audit Query** tab, configure query conditions to view audit events within the
specified time range. Basic query a. Configure the following parameters: **Audit Type**, **Audit Target**, **Action Type**, **Action**,
**Risk Level**, and **Notify**.
b. Specify a time range to query. c. In the **Full-Text Search** search box, enter a keyword. d. Click **Search**. Advanced query In addition to the basic query conditions, you can configure advanced query conditions. a. Configure basic query conditions. urity Audit b. Click **Advanced Search**. c. In the **Advanced Search** dialog box, configure the **Filter Name**, **User**, **Target**,
**Command**, **Result**, and **Reason** parameters.
d. Click **Save**.

| On | the Audit Query | tab, view information about an audit event in the audit event list. The |   |
|---|---|---|---|
| information includes |   | Audit Time | , |

**Recipient**. You can click the value in the **Audit Rules**column of an audit event. On the
**Audit Rules**tab, you can view the details of the audit rule.
6. Click **Export** to export the audit events.
For more information about how to download the exported audit events to your computer for analysis, see Download exported audit events or logs.

### 8.4 View raw logs

This topic describes how to view raw audit logs.

**Background information**

On the **Raw Log** tab, you can view the raw logs that are generated by a running audit object. Raw logs contain information that is required for debugging. Security administrators can use these raw logs to troubleshoot system failures.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Global**
**Platform Security** section, click **Security Operations Center**.
3. In the left-side navigation pane, choose **Operations > Security Audit**.
4. On the **Security Audit** page, click the **Raw Log** tab.
5. On the **Raw Log** tab, configure query conditions to view the log summary chart and raw
logs within a specific time range. i. Specify **Audit Type** and **Audit Target**. ii. Enter a keyword. iii. Specify a time range to query. iv. Click **Search**.
6. Click **Export** to export the audit events.
Download the exported file for analysis. For more information, see Manage export tasks.

### 8.5 View the number of logs

This topic describes how to view and manage log sources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the Security Audit page, click the **Log Sources** tab to view and manage logs by device
instance. urity Audit You can view the number of logs that are recorded on the current day and the number of logs that are recorded during the previous 30 days for each device instance. If you do not want to display the logs of a device instance, perform the following steps:

**Hide the logs of a single device instance**

i. Find the device instance that you want to manage and click **Hide** in the **Actions** column. ii. In the message that appears, click **OK**.

**Note**

The steps that are performed to display the logs of a device instance are similar to the steps that are performed to hide the logs.

**Hide the logs of multiple device instances at the same time**

i. Select the device instances that you want to manage, click **Batch Manage Display**
**Status**, and then select **Hide** from the drop-down list.
ii. In the message that appears, click **OK**.

**Note**

The steps that are performed to display the logs of multiple device instances are similar to the steps that are performed to hide the logs.

### 8.6 Policy settings

#### 8.6.1 Manage audit rules

This topic describes how to create, modify, or delete an audit rule.

**Background information**

If a log matches an audit rule, an audit event is reported. You can specify regular expressions in an audit rule to match logs. A regular expression defines a matching pattern for character strings and can be used to check whether a string contains a specific substring. The following table provides examples about the pattern.

| Regular expression | Description |
|---|---|
| ^\d{5,12}$ | Matches the consecutive numbers from the fifth number to the twelfth number. |
| load file\( _ | Matches the "load file(" string. _ |

The security audit module defines the default audit rule based on the string that is generated in the log. This applies when an audit event is reported. A security administrator can also customize audit rules based on the string that is generated in the log. This applies when the system encounters an attack. urity Audit
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management**, and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Audit Rules** tab.
5. Create an audit rule.
i. Click **New**. ii. In the **Audit Rules** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the audit rule. |
| Audit Type | Select an audit type. Valid values: Server, Network Device, ECS, Cloud Products, Tenant Database, and Platform Database. |
| Audit Target | Select an audit object based on the audit type that you select. |
| Action Type | Select an action type. Valid values: build, delete, modify, access, enable, disable, login, logout, and other. |
| Action | Select an action. Valid values: Process Error, Logon Attempt, Error, Change, Access, Resource Management, Permission, and Account. |
| Risk Level | Select a risk level for the action that you specify. Valid values: Urgent, Important, Moderate, and Low. |
| Notify | Specify whether to allow the audit rule to generate alerts. Valid values: Enable Alert and Disable Alert. |
| Match Condition | Specify a match condition. |
| Remarks | Enter a description for the audit rule. |

iii. Click **OK**. The system sends an alert email to the specified alert recipient after you create an audit rule. This applies if one string in an audit log of the specified audit type, audit object, or risk level matches the regular expression of the audit rule.
6. Manage audit rules.
You can also perform the following operations: View and edit an audit rule If an audit rule is a custom rule, click **Edit** in the **Actions** column. urity Audit Query audit rules Specify **Audit Type** and **Audit Target**. Enter a keyword in the search box and click
**Search**.
Disable an audit rule Find the audit rule that you want to disable and click **Disable** in the **Actions** column. Enable an audit rule Find the audit rule that has been disabled and click **Enable** in the **Actions** column. Delete an audit rule Find the audit rule that you want to delete and click **Delete** in the **Actions** column.

**Note**

You can delete only custom rules. Import a rule Click **Import Rule** and upload a rule file as prompted. Export a rule You can export multiple custom rules at a time. Select the custom rules that you want to export and click **Export Rule**.

#### 8.6.2 Configure alert recipients

This topic describes how to configure the recipients of alerts on audit events.

**Background information**

After you specify an alert recipient, the system sends a report to the email address of the alert recipient when an audit event occurs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Alert Settings** tab.
5. Create an alert recipient.
i. Click **New**. urity Audit ii. In the **Add Alert Recipient** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| Mailbox | Enter the email address of the alert recipient. |
| Name | Enter the name of the alert recipient. |
| Audit Type | Select an audit type. Valid values: Server, Network Device, ECS, Cloud Products, Tenant Database, and Platform Database. |
| Audit Target | Select an audit object based on the audit type that you specify. |
| Risk Level | Select a risk level for the action. Valid values:G lobal, Urgent, Important, Moderate, and Low. |

iii. Click **OK**.
6. Manage alert recipients.
Search for alert recipients Specify **Audit Type**, **Audit Target**, and **Risk Level**, enter the keyword of the email address, and then click the search icon. Delete alert recipients Find the email address that you want to delete and click **Delete** in the Actions column.

#### 8.6.3 Query the archives of audit events and raw logs

**raw logs**

This topic describes how to query and download the archives of audit events and raw logs.

**Background information**

You can download the archives of events and logs to analyze audit events. This ensures the security of the Apsara Stack environment.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Archiving** tab.
5. Query the archives of events and logs.
By default, the system automatically stores logs of the last 185 days. i. Configure **Audit Type** and **Archiving Type**. urity Audit ii. Specify a time range to query. iii. Click **OK**. Find the file where the archive information is stored and click **Download** in the **Actions** column to save the archive file to your computer.

#### 8.6.4 Download exported audit events or logs

**logs**

This topic describes how to download exported audit events or logs.

**Background information**

You can export audit events or logs on the **Audit Query** or **Raw Log** tab of the Security Audit page. After you export audit events or logs, you can manage the export tasks on the Exporting tab.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Global**
**Platform Security** section, click **Security Operations Center**.
3. In the left-side navigation pane, choose **Operations > Security Audit**.
4. On the **Security Audit** page, click the **Policies** tab.
5. On the **Policies** tab, click the **Exporting** tab.
6. View the created export tasks.
7. Click **Download** to download audit events or logs to your on-premises server.
To delete an export task, click **Delete**.

#### 8.6.5 Modify system settings

This topic describes how to configure system parameters for security audit.

**Background information**

You can configure system parameters to specify the maximum number of system alerts per day and the maximum number of audits per day for raw logs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **System Settings** tab.
5. Find the system parameter that you want to modify and click **Edit** in the **Actions** column.
6. Enter a required value and click **OK**.
urity Audit The value -1 indicates no limit.

**Important**

If the value that you specify for the Total Logs Audited per Day (GB/day), Platform Database Logs Audited per Day (GB/day), or Tenant Database Logs Audited per Day (GB/day) parameter is exceeded, raw logs and audit events are no longer archived or stored. However, raw logs and audit events continue to be audited.
