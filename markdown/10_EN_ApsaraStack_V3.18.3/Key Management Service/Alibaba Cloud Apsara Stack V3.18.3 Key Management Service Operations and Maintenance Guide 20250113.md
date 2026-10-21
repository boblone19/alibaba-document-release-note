---
title: "Alibaba Cloud Apsara Stack V3.18.3 Key Management Service Operations and Maintenance Guide 20250113"
product_version: "V3.18.3"
doc_version: "20250113"
pdf_pages: 14
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Key Management Service Operations and Maintenance Guide 20250113.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Key%20Management%20Service%20Operations%20and%20Maintenance%20Guide%2020250113.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Key Management Service Operations and Maintenance Guide 20250113

## Table of Contents

- 1 Log on to the KMS O&M platform
- 2 Quota management
  - 2.1 Manage a user quota
  - 2.2 Manage a throttling rule
  - 2.3 Configure global quotas
- 3 Log analysis
  - 3.1 Overview
  - 3.2 Query security audit logs
  - 3.3 View logs by using request IDs
  - 3.4 Common KMS errors
    - 3.4.1 Overview
    - 3.4.2 Errors with HTTP status code 4XX
    - 3.4.3 Errors with HTTP status code 500
    - 3.4.4 Errors with HTTP status code 503
    - 3.4.5 Degradation of dependency on a service
- 4 Access control
  - 4.1 Manage read/write permission verification
- 5 O&M of KMS components
  - 5.1 Overview
  - 5.2 Log on to the Apsara Infrastructure Management console
  - 5.3 KMS_HOST
  - 5.4 HSA
  - 5.5 etcd
  - 5.6 Rotator
    - 5.6.1 Primary data center
    - 5.6.2 Secondary data center

rm

## 1 Log on to the KMS O&M platform

This topic describes how to log on to the Key Management Service (KMS) O&M platform.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: ${region}.ops.console.${intranet-domain}. A browser is available. We recommend that you use Google Chrome.

**Operation**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console in the ${region}.ops.console.${intranet-domain}
format. Then, press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter your username and password.
The first time you log on to the Apsara Uni-manager Operations Console, you must change the password of your username. To ensure the security of your account, we recommend that you use a password that meets the minimum complexity requirements. The password must contain letters, digits, and special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
4. Click Log On to log on to the Apsara Uni-manager Operations Console.
5. In the top navigation bar, choose **Products > Security Services > Security > Cloud Services > KMS O&M**.

## 2 Quota management

### 2.1 Manage a user quota

This topic describes how to create and modify a user quota.

**Create a user quota**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, click Cloud Services and choose **Cloud Services > KMS O&M > User Quotas**.
3. Click **Create Quota**.
4. In the **Create Quota** dialog box, configure the following parameters and click Ok.

| Parameter | Description |
|---|---|
| User ID | The ID of the user. |
| Key Quota | The maximum number of keys that are supported. |

**Modify a user quota**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, click Cloud Services and choose **Cloud Services > KMS O&M > User Quotas**.
3. Find the ID of the user whose quota you want to modify and click **Modify** in the **Actions** column.
4. In the **Modify** dialog box, configure the following parameters and click Ok.

| Parameter | Description |
|---|---|
| Key Quota | The maximum number of keys that are supported. |
| Alias Quota | The maximum number of aliases. |

### 2.2 Manage a throttling rule

This topic describes how to create and modify a throttling rule.

**Create a throttling rule**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > KMS O&M > Throttling**.
3. Click **Create Throttling Rule**.
4. In the **Register Resource** dialog box, configure the following parameters and click **Ok**.

| Parameter | Description |
|---|---|
| Resource | The name of the resource. Valid values: s: applies to all API operations. d: applies to the default API operation. |
| Apply To | The method to combine user and service IDs for your application. Valid values: d: combines all user IDs and service IDs. This is the default value. dd: combines the default user ID and service ID. _ |
| Threshold | The threshold for throttling. |
| Throttling Policy | Standalone Throttling: Throttling is implemented on a single Key Management Service (KMS) API operation. Standalone Token Bucket: Throttling is implemented on a single user. |
| Time Unit | The time unit for throttling. |

**Modify a throttling rule**

1. Log on to Cloud Security Operations Center
2. In the left-side navigation pane, choose **Cloud Services > KMS O&M > Throttling**.
3. On the tab that appears, find the required resource, click **Modify** in the **Actions** column of the resource.
4. In the **Modify Rule** dialog box, configure the following parameters and click **Ok**.

| Parameter | Description |
|---|---|
| Threshold | The threshold for throttling. Note If you want to change the value of this parameter, you must change it for two rules. One rule has the Resource parameter set to s and the Apply To parameter set to d. The other rule has the Resource parameter set to s and the Apply To parameter set to dd. _ |
| Throttling Policy | Standalone Throttling: Throttling is implemented on a KMS API operation. Standalone Token Bucket: Throttling is implemented on a single user. |
| Time Unit | The time unit for throttling. |

### 2.3 Configure global quotas

This topic describes how to configure global quotas.

**Procedure**

1. Log on to Cloud Security Operations Center.
2. In the left-side navigation pane, click Cloud Services and choose **KMS O&M > Tenant-side KMS O&M**.
3. On the **Global Quotas** tab, view the information about global quotas. You cannot modify the information on the Global Quotas tab.

## 3 Log analysis

### 3.1 Overview

When the administrator needs to backtrack operations of Key Management Service (KMS), the administrator can perform a security audit. Security audits are long-term security management activities throughout the lifecycle of cloud services. The security audit feature of Apsara Stack Security can collect system security data, analyze weaknesses in system operations, and report audit events to administrators. The administrator can view and analyze the audit events to continuously improve the security and reliability of cloud services.

> **Note:** KMS logs are collected to Log Service by using Logtail. You can analyze the logs in the Log Service console or by calling Log Service API operations. If you cannot analyze the logs in the Log Service console or by calling Log Service API operations, you must log on to the servers on which KMS is deployed and analyze the logs on each server.

### 3.2 Query security audit logs

You can log on to the Security Operations Center (SOC) to query the raw logs and audit events related to O&M operations. This helps you to quickly locate system faults.

**Query raw logs**

1. Log on to the SOC.
For more information, see **Log on to the SOC** section of **Security audit** in **User Guide**.
2. **>**
3. On the **Security Audit** page, click the **Raw Logs** tab.
4. On the **Raw Logs** tab, configure query conditions to view the log summary chart and raw logs within a specific time range for Key
Management Service (KMS). i. Set **Audit Type** to **Cloud Products**. ii. Set **Audit Target** to **KMSPortalAuditLog**. iii. Specify a time range and click **Search**.

> **Note:** If you want to compare data in multiple time ranges, specify a different time range and click **New Query**. KMS generates query tabs for different time ranges. You can click the tabs to compare data between different time ranges.

5. **(Optional)** Click **Export** to create an export task. On the **Exporting** tab, you can download raw logs to your local computer.

**Query audit events**

1. **>**
2. On the **Security Audit** page, click the **Audit Query** tab.
3. On the **Audit Query** tab, configure query conditions to view the audit log summary chart and audit events within a specific time range
for KMS. i. Set **Audit Type** to **Cloud Products**. ii. Set **Audit Target** to **KMSPortalAuditLog**. iii. Configure filter conditions such as Action Type, Risk Level, Notify, and Created At. Then, click **Search**.

> **Note:** You can also click **Advanced Search** and configure the following filter conditions: **Filter Name**, **User**, **Target**, **Action**, **Result**, and **Reason**.

4. **(Optional)** Click **Export** to create an export task. On the **Exporting** tab, you can download audit events to your local computer.

**What to do next**

You can query audit summary information, configure alert recipients, manage log sources, audit rules, event log archiving, export tasks, and modify system configurations based on your business requirements. For more information, see **Security audit** in **User Guide**.

### 3.3 View logs by using request IDs

After you send a request to Key Management Service (KMS), KMS sends you a message that contains a request ID. This topic describes how to view logs by using request IDs. Request IDs can be used in the following scenarios: You can view the KMS audit logs in the /cloud/log/kms/KmsHost#/kms_host/audit.log file. You can view the audit log information of the current access based on the value of request_id. For log entries whose expected_code values are not 200, you can view error information in the debug logs based on the value of request_id. Path to the on-premises logs: /cloud/log/kms/KmsHost#/kms_host/debug.log

> **Note:** The /cloud/log/kms/KmsHost#/kms_host/debug.log and audit.log files are stored on the same machine.

If you need all details of a request, you can view detailed information in the trace logs. Path to the on-premises logs: /cloud/log/kms/KmsHost#/kms_host/debug.log

> **Note:** The /cloud/log/kms/KmsHost#/kms_host/debug.log and audit.log files are stored on the same machine.

You can associate a cryptographic API operation with the trace logs of HSA by using the value of request_id. Path to the on-premises logs: /cloud/log/kms/HSA#/hsa/trace.log

> **Note:** The /cloud/log/kms/KmsHost#/kms_host/trace.log and audit.log files may be stored on different machines.

You can retrieve log information based on other information. You can retrieve the information in the audit logs of KMS by using information other than request_id. If you need to associate the audit logs with other logs, you must use request_id.

### 3.4 Common KMS errors

#### 3.4.1 Overview

KMS has two HTTP status codes in audit.log: expected_code and status_code. Typically, the expected code and status code of an error are the same. ( `expected_code = status_code` ). However, there are exceptions. status_code is the HTTP status code that is actually returned to a user.

#### 3.4.2 Errors with HTTP status code 4XX

Most errors with HTTP status code 4XX are included in the business logic of KMS. For example, HTTP status code 403 indicates a user request authentication failure, and HTTP status code 400 indicates that an input parameter is invalid. You can view the details of an error in the debug log by using the value of request_id.

#### 3.4.3 Errors with HTTP status code 500

This type of error is not included in the business logic of KMS. They are severe errors and must be fixed immediately. In most scenarios, if the status code of an error is **500**, the expected code of this error is also **500**. Such an error may be caused by an unexpected exception in a dependency service. We recommend that you contact the technical support personnel of the dependency service for further assistance. You can view the details of an error in the debug log by using the value of request_id.

#### 3.4.4 Errors with HTTP status code 503

An error with HTTP status code 503 occurs when the user interrupts the connection or a dependency service of Key Management Service (KMS) is abnormal. We recommend that you handle the exception at the earliest opportunity. The status code and expected code of such an error may be different or consistent. The status code is 503 but the expected code is not 503. Possible causes: The client of a user interrupts the connection in advance. The client times out because KMS that functions as the server does not respond within the timeout period. You can check the trace logs by using the value of request_id to determine whether the error is caused by a slow response of the server and identify the specific module. Both the status code and expected code are 503. Such an error is an expected error in a dependency service of KMS. It may occur when the performance of the dependency service is unstable. You can view the details of the error in the debug logs by using the value of request_id. We recommend that you contact the technical support of the dependency service for further assistance.

#### 3.4.5 Degradation of dependency on a service

KMS stores the data of its dependency services in the local cache. If a dependency service is unavailable, KMS uses the obsolete data stored in the cache. In this scenario, the status code in the audit log of KMS is 200, but an additional debug log will be generated. When this situation occurs, users with cached data can access KMS. However, users without cached data encounter a 503 error when they try to access KMS.

## 4 Access control

### 4.1 Manage read/write permission verification

The Apsara Uni-manager Operations Console allows you to verify role permissions in a centralized manner. By default, read/write permission verification is enabled. You can disable read/write permission verification if required.
1. Log on to a server on which Key Management Service (KMS) is deployed. For more information, see KMS_HOST.
2. Access the following path to configure read/write permission verification:

```
 /cloud/app/kms/AdminPortalBackend#/admin_portal_backend/current/conf.global/self/user/local/admin_portal_backend/oam_config.json .
```

3. Set KmsEnableRwPermission to true to enable read/write permission verification.

> **Note:** If you set KmsEnableRwPermission to false, read/write permission verification is disabled.
> You must enable read/write permission verification for all servers.

4. Restart the AdminPortalBackend service to ensure that the configuration changes take effect.
Method 1: Log on to the Apsara Infrastructure Management console and restart the AdminPortalBackend service. For more information, see Log on to the Apsara Infrastructure Management console. Method 2: Log on to the server and stop the admin_portal_backend process. The Apsara Infrastructure Management console automatically starts the process again.

## 5 O&M of KMS components

### 5.1 Overview

You can deploy Key Management Service (KMS) and perform O&M on KMS components in the Apsara Infrastructure Management console. You can log on to a server where KMS is deployed on the **Machines** page in the Apsara Infrastructure Management console.

### 5.2 Log on to the Apsara Infrastructure Management console

**Management console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: ${region}.ops.console.intranet-domain-id.com. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

The first time you log on to the Apsara Uni-manager Operations Console, you must change the password of your username. To ensure the security of your account, we recommend that you use a password that meets the minimum complexity requirements. The password must contain letters, digits, and special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
4. Click Log On to log on to the Apsara Uni-manager Operations Console.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products > Base/Platforms > Apsara**
**Infrastructure Management**.

### 5.3 KMS_HOST

This topic describes how to check the status of the KMS_HOST component.

**Check whether the KMS_HOST component is normal**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products > Base/Platforms > Infrastructure**
**Management**.
2. In the left-side navigation pane, click **Project & Cluster O&M**.
3. Enter kms in the Project | Cluster search box, find the Key Management Service (KMS) cluster that you want to manage, and click
**Cluster Details** in the **Actions** column.
4. On the **Services** tab, enter **kms** in the Service search box and click Details in the Actions column to view the details of the KMS_HOST
component. If the indicator for **KmsHost#** is green, the component is in the desired state.
5. Click **KmsHost#** to view and obtain the IP addresses of all servers on which the KMS_HOST component is deployed.
6. Find a server and click **Terminal** in the Actions column to log on to the server.
7. Run the `curl http://ip:5555/status.html` command and check whether **success** is returned.

> **Note:** The IP address is the IP address of the server in Step 6.
> Use this method to verify all servers on which the KMS_HOST component is deployed.

**Troubleshooting**

1. View logs in the /cloud/log/kms/KmsHost#/kms_host directory.
2. Check whether the KMS_HOST component is normal.
If the KMS_HOST component abnormally exits after it starts, view debug logs in the debug.log file to troubleshoot the specific error. If the KMS_HOST component is running but does not function as expected, view status logs in the status.log file to troubleshoot the specific error.

**Possible errors**

| Error message | Solution |
|---|---|
| xxx selfCheck error Note xxx indicates a component on which the KMSHOST component _ depends. | Check whether the dependency configuration is valid. You can view debug logs in the debug.log file to troubleshoot the specific error. Check whether the xxx component is normal. |
| exit code 1 | View debug logs in the debug.log file to identify the cause of the abnormal exit. |

### 5.4 HSA

This topic describes how to check the status of the HSA component.

**Check whether the HSA component is normal**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products > Base/Platforms > Infrastructure**
**Management**.
2. In the left-side navigation pane, click **Project & Cluster O&M**.
3. Enter kms in the **Project | Cluster** search box and find the Key Management Service (KMS) cluster that you want to manage.
4. Click **Cluster Details** in the **Actions** column.
5. On the **Services** tab, enter **kms** in the Service search box and click Details in the Actions column to view the details of the HSA
component. If the indicator for **HSA#** is green, the component is in the desired state.
6. Click **HSA#** to view and obtain the IP addresses of all servers on which the HSA component is deployed.
7. Find a server and click **Terminal** in the Actions column to log on to the server.
8. Run the `curl http://ip:5555/status.html` command and check whether **success** is returned.

> **Note:** The IP address is the IP address of the server in Step 6.
> Use this method to verify all servers on which the HSA component is deployed.

**Troubleshooting**

1. View logs in the /cloud/log/kms/HSA#/hsa directory.
2. Check whether the HSA component is normal.
If the HSA component abnormally exits after it starts, view debug logs in the debug.log file to troubleshoot the specific error. If the HSA component is running but does not function as expected, view status logs in the status.log file to troubleshoot the specific error.

**Possible errors**

Error: `exit code 1` Troubleshooting: View debug logs in the debug.log file to identify the cause of the abnormal exit. This error can be caused by one of the following reasons: The etcd component does not start as expected. The etcd component starts as expected, but the corresponding data is invalid.

> **Note:** During disaster recovery, synchronization errors in a secondary cluster may cause this error.

### 5.5 etcd

This topic describes how to check the status of the etcd component.

**Check whether the etcd component is normal**

In the Apsara Infrastructure Management console, check whether Etcd and EtcdDecider are in the desired state.
1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products > Base/Platforms > Infrastructure**
**Management**.
2. In the left-side navigation pane, click **Project & Cluster O&M**.
3. Enter kms in the **Project | Cluster** search box and find the Key Management Service (KMS) cluster that you want to manage.
4. Click **Cluster Details** in the **Actions** column.
5. On the **Services** tab, enter **kms** in the Service search box and click Details in the Actions column to view the details of Etcd and
EtcdDecider. If the indicators for **kms.Etcd#** and **kms.EtcdDecider#** are green, they are in the desired state.

**Troubleshooting**

View logs in the /cloud/log/kms/Etcd#/etcd and /cloud/log/kms/EtcdDecider#/decider directories to troubleshoot errors.

**Possible errors**

| Exception | Solution |
|---|---|
| The startup parameters of the etcd component are invalid. | Find the correct settings of the startup parameters in the historical records of the debug.log file. Then, manually start the etcd component. Note Retain the error logs and contact the technical support team to help you identify the cause. |
| Errors in EtcdDecider during service updates cause errors in the etcd component. | In most scenarios, this error occurs when a rolling task exists. You can analyze the error and identify the cause based on the debug.log file of EtcdDecider. |
| The data directory of the etcd component is missing and the etcd component cannot be started. | Use the Apsara Infrastructure Management console to remove the abnormal etcd node, and then add the node again. |

### 5.6 Rotator

#### 5.6.1 Primary data center

This topic describes how to check the status of the rotator of the primary data center. The rotator is a special component. Even if the service role of the rotator is in the desired state, the rotator is not necessarily working as expected. You can view the status of the rotator in the Apsara Infrastructure Management console. Rotator exceptions do not have an impact on the API logic of Key Management Service (KMS). In most scenarios, you need to identify the cause of a rotator exception only when unexpected results are found, such as, when the data in ApsaraDB RDS does not meet expectations.

**Check whether the rotator starts in primary data center mode**

View the value of `current idc master` in the /cloud/log/kms/Rotator#/rotator/debug.log file to check whether the rotator of the primary data center starts in primary data center mode. If the value of `current idc master` is **true**, the rotator starts in primary data center mode. If the value of `current idc master` is **false**, the rotator starts in secondary data center mode.

**Check whether the rotator is in the working state**

The rotator of the primary data center is deployed on all nodes. The nodes work in distributed lock mode to ensure that only one node can work at a time. All other nodes remain in the standby state. View status logs in the /cloud/log/kms/Rotator#/rotator/status.log file and check the status of each node. Check the value of RotatorState in the status logs. Valid values: ExecuteWorker and TryLock. ExecuteWorker: The node is in the working state. TryLock: The node is in the standby state. Figure 1. Working state Figure 2. Standby state

**Possible errors**

Abnormal ApsaraDB RDS database access. Statistics collection and key deletion tasks cannot be executed. Abnormal HSA service. Key rotation tasks cannot be executed. Abnormal Log Service. Metering tasks cannot be executed. Abnormal etcd service. Distributed locks are unavailable and tasks cannot be executed. If one of the tasks on the rotator is abnormal, the rotator may be unable to reach the desired state. In this case, the rotator may be stuck in the desired state, which you can view in the Apsara Infrastructure Management console.

#### 5.6.2 Secondary data center

This topic describes how to check the running status of the rotator of the secondary data center. The rotator of the secondary data center is deployed on all nodes, which are all in the working state. The work scopes of the nodes are idempotent in a certain time range.

**Check whether the rotator starts in secondary data center mode**

Check the value of `current idc master` in /cloud/log/kms/Rotator#/rotator/debug.log, as shown in the following figure. If the value of `current idc master` is **false**, the rotator starts in secondary data center mode. If the value of `current idc master` is
**true**, the rotator starts in primary data center mode.

**Possible errors**

Abnormal network of the primary data center. The etcd of the primary data center is inaccessible. Abnormal etcd of the primary data center. The etcd of the primary data center is inaccessible. Abnormal etcd of the secondary data center. Data cannot be written into etcd. Incorrect etcd information of the primary data center. Data synchronization errors occur.

> **Important:** Rotator exceptions of the secondary data center has a severe impact on KMS in the secondary data center. You must fix the exceptions in a timely manner.
