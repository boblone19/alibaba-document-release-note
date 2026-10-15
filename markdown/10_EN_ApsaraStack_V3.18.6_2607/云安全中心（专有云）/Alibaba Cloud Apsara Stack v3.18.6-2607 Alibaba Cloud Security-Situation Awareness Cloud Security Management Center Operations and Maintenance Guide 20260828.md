---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 13
source_pdf: "7781c39f8542828b_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Ma"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Log in to the Apsara Infrastructure Management console
- 2 SOC
  - 2.1 Check the service status
    - 2.1.1 Perform the basic inspection
    - 2.1.2 Perform the advanced inspection
      - 2.1.2.1 Perform the advanced inspection on SocApp
      - 2.1.2.2 Perform the advanced inspection on SiemAPP
    - 2.1.3 Perform the business inspection
  - 2.2 Restart SocApp
  - 2.3 Restart SiemApp

ucture Management console

## 1 Log in to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log in to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. ucture Management console

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Apsara Infrastructure Management**.

## 2 SOC

### 2.1 Check the service status

#### 2.1.1 Perform the basic inspection

The basic inspection of Security Operations Center (SOC) checks whether a service runs as expected. This topic describes how to perform the basic inspection.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose Platform Operation > Apsara Infrastructure Management
> Resource Management to log in to the Apsara Infrastructure Management console.
3. In the left-side navigation pane, choose Resource Management > **Product & Cluster**
**O&M**.
4. On the Product & Cluster O&M page, enter sas-securityoperationscentercluster in the
**Product | Cluster** search box. Then, click **Cluster Details** in the Actions column.
5. On the **Services** tab of the Cluster Details page, click the name of the service.
6. In the left-side pane of the **Component Details** page, click **yundun-soc** to check whether
the value of the Status Details parameter is Ready.

#### 2.1.2 Perform the advanced inspection

The advanced inspection of Threat Detection Service (TDS) checks whether the service runs as expected and check the service features.

##### 2.1.2.1 Perform the advanced inspection on SocApp

**SocApp**

This topic describes how to perform the advanced inspection on SocApp.

**Procedure**

1. Log in to the terminal server.
2. Access the SocApp containers based on different pod names. Each pod corresponds to one
SocApp container. i. Run the kubectl get pod -n sas | grep soc command to determine the SocApp pod names. In the return result, a string in the [yundun-soc-Digit] format is the name of a SocApp pod, such as yundun-soc-0 and yundun-soc-1 marked in the following yellow box. ii. Run the `kubectl exec -it [Pod name] -n sas -- bash` command to access the corresponding SocApp container.
3. Check the status of the Java process.
Run the following command: ps aux | grep java | grep soc . If a record is returned, the Java process is normal.
4. Check the health of the component.
Run the following command: `sudo -u admin /home/admin/yundunsoc/bin/preload.sh` . If ok is returned, the component is healthy.
5. View the following log files:
/home/admin/yundunsoc/logs/isoc.log: stores the info logs that are generated during the running of SocApp, including the operations center, risk analysis, and log management. /home/admin/yundunsoc/logs/common-default.log: stores the info logs that are generated during the running of SocApp, including asset management and alert rule settings. /home/admin/yundunsoc/logs/common-error.log: stores the logs that are generated when SocApp fails.

##### 2.1.2.2 Perform the advanced inspection on SiemAPP

**SiemAPP**

1. Log in to the terminal server.
2. Access the SiemAPP containers based on different pod names.
i. Run the kubectl get pod -n sas | grep siem command to determine the SiemAPP pod names. In the return result, a string in the [yundun-siem-Digit] format is the name of a SiemAPP pod, such as yundun-siem-0 and yundun-siem-1. ii. Run the `kubectl exec -it [Pod name] -n sas -- bash` command to access the corresponding SiemAPP container.
3. Check the status of the Java process.
Run the ps aux | grep java | grep yundunsiem command. If a record is returned, the Java process is normal.
4. Check the health of the component.
Run the `sudo -u admin /home/admin/yundunsiem/bin/preload.sh` command. If ok is returned, the component is healthy.
5. View the following log files:
/home/admin/yundunsiem/logs/importer_all.log: stores the info logs that are generated during the running of SiemApp. /home/admin/yundunsiem/logs/common-error.log: stores the logs that are generated when SiemApp fails. /home/admin/yundunsiem/logs/common-default.log: stores the middleware-related logs that are generated during the running of SiemApp.

#### 2.1.3 Perform the business inspection

The business inspection of Security Operations Center (SOC) checks whether the businesslevel services run as expected.
1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
Product Operation > Security O&M > Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Monitoring and Alerting** > **Business**
**Monitoring**. On the Business Monitoring page, click the Security Operations Center tab.
3. Click SocApp to view the system monitoring details.

| Metric | Description | Exception and handling suggestion |
|---|---|---|

| ES Connect status | Specifies whether Elasticsearch can be connected. Valid values: 1 and 0. 1: Elasticsearch can be connected. 0: Elasticsearch cannot be connected. | If the value 0 is displayed, check whether an Elasticsearch cluster is deployed in Apsara Stack Security. If no Elasticsearch cluster is deployed, ignore the issue. If an Elasticsearch cluster is deployed, contact the product R&D team to resolve the issue. |
|---|---|---|
| Timed task execution status with lease | The execution status of the scheduled task. The value N indicates that the scheduled task has been executed for N times. The value 0 indicates that the scheduled task is not executed. | The value 0 does not indicate an exception. If the value 0 is returned, you must re-analyze the scheduled task based on the execution cycle and business logic of the task. |
| Timed task execution status without lease | The execution status of the scheduled task. The value N indicates that the scheduled task has been executed for N times. The value 0 indicates that the scheduled task is not executed. | The value 0 does not indicate an exception. If the value 0 is returned, you must re-analyze the scheduled task based on the execution cycle and business logic of the task. |
| Data volume TOP 10 | The data volumes of the top 10 tables with the largest amount of data in the yundunsoc database. | In most cases, the data volume of a table is less than 10 million entries. If a table has a data volume of more than 100 million entries, find the table in the yundunsoc database and check whether the data volume is reasonable within the current cloud platform. You can also contact the product R&D team to resolve the issue. |
| Error Log Count | The number of error logs in SOC. | Error logs exist when your service is running as expected. If the number of error logs sharply increases, you must check whether the SOC features are available, check the error messages in error logs, and then contact the product R&D team to resolve the issue. |

| Exception Log Count | The number of exception logs in SOC. | Exception logs exist when your service is running as expected. If the number of exception logs sharply increases, you must check whether the SOC features are available, check the error messages in exception logs, and then contact the product R&D team to resolve the issue. |
|---|---|---|
| Disk Usage | The usage details of the disk. The disk usage is displayed from the following dimensions: the size of total partitions (total disk space), size of used partitions (used disk space), size used by the container (total size of the container root directory), and size used by logs (total size of the log directory). | If the size of used partitions is close to the size of total partitions, check whether the disk space of the physical machine is sufficient. You can determine whether to release the disk space that is used by the container and logs. |

4. Click SiemApp to view the system monitoring details.

| Metric | Description | Exception and handling suggestion |
|---|---|---|
| Pipeline State Distribution | All pipelines of the service, including built-in pipelines and custom pipelines. The number of successful pipelines and the number of failed pipelines are calculated. | If the number of failed pipelines is greater than 0, some pipelines fail. In this case, check whether the custom pipeline settings are correct and resolve the issue based on the logs of the security information and event management (SIEM) container. You can also contact the product R&D team to resolve the issue. |
| Pipeline Startup Status | The startup status of the built- in pipeline. The value 1 indicates that the pipeline is started. The value 0 indicates that the pipeline is not started. | If the value 0 is displayed, you can view the logs of the pipeline related to the SIEM container and resolve the issue. You can also contact the product R&D team to resolve the issue. |

| Disk Usage | The usage details of the disk. The disk usage is displayed from the following dimensions: the size of total partitions (total disk space), size of used partitions (used disk space), size used by the container (total size of the container root directory), and size used by logs (total size of the log directory). | If the size of used partitions is close to the size of total partitions, check whether the disk space of the physical machine is sufficient. You can determine whether to release the disk space that is used by the container and logs. |
|---|---|---|
| Error Log Count | The number of error logs in SIEM. | Error logs exist when your service is running as expected. If the number of error logs sharply increases, you must check whether the SIEM features are available, check the error messages in error logs, and then contact the product R&D team to resolve the issue. |

5. Click the UEBA tab to view the detailed system monitoring information.
6. Click the ASM tab to view the detailed system monitoring information.
7. Click the Report tab to view the detailed system monitoring information.

### 2.2 Restart SocApp

If SocApp of Security Operations Center (SOC) fails, perform the following steps to restart SocApp:
1. Log in to the terminal server.
2. Run the following command to determine the name of a SocApp pod:

```bash
kubectl get pod -n sas | grep soc
```

**Important**

In the return result, a string in the [yundun-soc-Digit] format is the name of a SocApp pod, such as yundun-soc-0 or yundun-soc-1. If the suffix of a string is not a digit, the string is not the name of a SocApp pod.
3. Run the following command to access the SocApp container:

```bash
kubectl exec -it [Pod name] -n sas -- bash
```

4. Run the following command to find the Java process:

```
  ps aux |grep soc
```

5. Run the following command to stop the current process:

```
kill -9 Process ID
```

6. Run the following command to restart the process:

```python
  sudo -u admin /home/admin/yundunsoc/bin/appctl.sh restart
```

7. Run the following command to check whether the process is restarted:

```bash
  curl http://127.0.0.1:10070/checkpreload.htm
```

### 2.3 Restart SiemApp

If SiemApp of Security Operations Center (SOC) fails, perform the following steps to restart SiemApp:
1. Log in to the terminal server.
2. Run the following command to determine the name of a SiemApp pod:

```bash
kubectl get pod -n sas | grep siem
```

**Important**

In the return result, a string in the [yundun-siem-Digit] format is the name of a SiemApp pod, such as yundun-siem-0 or yundun-siem-1. If the suffix of a string is not a digit, the string is not the name of a SiemApp pod.
3. Run the following command to access the SiemApp container:

```bash
kubectl exec -it [Pod name] -n sas -- bash
```

4. Run the following command to find the Java process:

```
  ps aux |grep siem
```

5. Run the following command to stop the current process:

```
kill -9 Process ID
```

6. Run the following command to restart the process:

```python
  sudo -u admin /home/admin/yundunsiem/bin/appctl.sh restart
```

7. Run the following command to check whether the process is restarted:

```bash
  curl http://127.0.0.1:10070/checkpreload.htm
```
