---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Operations and Maintenance Guide 20250612"
product_version: "V3.18.3"
doc_version: "20250612"
pdf_pages: 14
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Operations and Maintenance Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20Operations%20and%20Maintenance%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Operations and Maintenance Guide 20250612

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
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

## 1 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
ucture Management console

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose**Products**
**> Base/Platforms > Infrastructure Management**.

## 2 SOC

### 2.1 Check the service status

#### 2.1.1 Perform the basic inspection

The basic inspection of Threat Detection Service (TDS) checks whether the service runs as expected. This topic describes how to perform the basic inspection.

**Procedure**

## 1 Log on to the Apsara Infrastructure Management console.

2. In the left-side navigation pane, click **Project & Cluster O&M**.
3. On the page that appears, enter **BasicThinCluster** in the **Product | Cluster** search box.
4. Find the cluster whose name is in the format of BasicThinCluster-A-xx and click **Cluster**
**Details** in the **Actions** column.
5. On the page that appears, click the **Services** tab.
6. In the **Service** search box, enter **yundun-soc**. In the list that appears, click Details in the
Actions column of the required service to view the details of each component.

#### 2.1.2 Perform the advanced inspection

The advanced inspection of Threat Detection Service (TDS) checks whether the service runs as expected and check the service features.

##### 2.1.2.1 Perform the advanced inspection on SocApp

**SocApp**

This topic describes how to perform the advanced inspection on SocApp.

**Procedure**

2. Log on to the physical server of Security Operations Center (SOC).
i. In the left-side navigation pane, click **Project & Cluster O&M**. ii. On the page that appears, enter **BasicThinCluster** in the **Product | Cluster** search box. iii. Find the cluster whose name is in the format of BasicThinCluster-A-xx and click **Cluster**
**Details** in the **Actions** column.
iv. On the page that appears, click the **Services** tab. v. In the **Service** search box, enter **yundun-soc**. In the list that appears, click **Details** in the **Actions** column of the required service. vi. In the **Components** section of the page that appears, click **SocApp#** to view the detailed information. vii. On the **Instances** tab, find the required instance and click **Terminal** in the **Actions** column.
3. Run the following command to log on to the docker container of SOC:

```python
sudo docker exec -it $(sudo docker ps | grep SocApp | awk '{print $1}') bash
```

4. Run the following command to check the status of the Java process:

```
ps aux | grep soc
```

If a record is returned, the Java process is normal.
5. Run the following command to check the component is healthy:

```python
sudo -u admin /home/admin/yundunsoc/bin/preload.sh
```

If `ok` is returned, the component is healthy.
6. View the following log files:
`/home/admin/yundunsiem/logs/isoc.log` : stores the info logs that are generated during the running of the SOC services such as operations center, situation monitoring, risk analysis, log management, log analysis, and storage management. `/home/admin/yundunsiem/logs/common-default.log` : stores the info logs that are generated during the running of the SOC services such as asset management and alert rule setting. `/home/admin/yundunsiem/logs/common-error.log` : stores the logs that are generated when SOC fails.

##### 2.1.2.2 Perform the advanced inspection on SiemAPP

**SiemAPP**

This topic describes how to Perform the advanced inspection on SiemAPP.

**Procedure**

2. Log on to the physical server of Security Operations Center (SOC).
i. In the left-side navigation pane, click **Project & Cluster O&M**. ii. On the page that appears, enter **BasicThinCluster** in the **Product | Cluster** search box. iii. Find the cluster whose name is in the format of BasicThinCluster-A-xx and click **Cluster**
**Details** in the **Actions** column.
iv. On the page that appears, click the **Services** tab. v. In the **Service** search box, enter **yundun-soc**. In the list that appears, click **Details** in the **Actions** column of the required service. vi. In the **Components** section of the page that appears, click **SiemApp#** to view the detailed information. vii. On the **Instances** tab, find the required instance and click **Terminal** in the **Actions** column.
3. Run the following command to log on to the two docker containers of SOC:

```python
sudo docker exec -it $(sudo docker ps | grep SiemApp | awk '{print $1}') bash
```

4. Run the following command to check the status of the Java process:

```
ps aux |grep siem
```

5. If a record is returned, the Java process is normal.
6. Run the following command to check the component is healthy:

```python
sudo -u admin /home/admin/yundunsiem/bin/preload.sh
```

If `ok` is returned, the component is healthy.
7. View the following log files:
`/home/admin/yundunsiem/logs/importer_all.log` : stores the info logs that are generated during the running of SiemApp. `/home/admin/yundunsiem/logs/common-error.log` : stores the logs that are generated when SiemApp fails. `/home/admin/yundunsiem/logs/common-default.log` : stores the middleware-related logs that are generated during the running of SiemApp.

#### 2.1.3 Perform the business inspection

The business inspection of Threat Detection Service (TDS) checks whether the business-level services run as expected.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Step 1: Log on to Cloud Security Operations Center**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
> **Security**.

**Step 2: Perform the business inspection**

1. In the left-side navigation pane, choose **Monitoring and Alerting** > **Monitoring**.
2. On the **Business Monitoring** page, click the **Security Operations Center** tab.
The **Security Operations Center** tab displays the SocApp and SiemApp cards. Click **SocApp** to view the monitoring details.

| Metric | Description | Exception and handling suggestion |
|---|---|---|
| ES Connect status | Indicates whether Elasticsearch can be connected. Valid values: 1: Elasticsearch can be connected. 0: Elasticsearch cannot be connected. | If the value 0 is displayed, check whether an Elasticsearch cluster is deployed in Apsara Stack Security. If no Elasticsearch clusters are deployed, you can ignore the issue. If an Elasticsearch cluster is deployed, contact the R&D team to resolve the issue. |
| Timed task execution status with lease | The execution status of the scheduled task. The value N indicates that the scheduled task has been executed for N times, and the value 0 indicates that the scheduled task is not executed. | The value 0 does not indicate an exception. If the value 0 is returned, you must re- analyze the scheduled task based on the execution cycle and business logic of the task. |
| Timed task execution status without lease | The execution status of the scheduled task. The value N indicates that the scheduled task has been executed for N times, and the value 0 indicates that the scheduled task is not executed. | The value 0 does not indicate an exception. If the value 0 is returned, you must re- analyze the scheduled task based on the execution cycle and business logic of the task. |
| Data volume TOP 10 | The data volumes of the top 10 tables with the largest amount of data in the yundunsoc database. | In most cases, the data volume of a table is less than 10 million entries. If a table has a data volume of over 100 million entries, find the table in the yundunsoc database and check whether the data volume is reasonable within the current cloud platform. You can also contact R&D team to resolve the issue. |
| Error Log Count | The number of error logs in SOC. | Error logs exist when your service is running as expected. If the number of error logs sharply increases, you must check whether the SOC features are available, check the error messages in error logs, and then contact the R&D team to resolve the issue. |

| Exception Log Count | The number of exception logs in SOC. | Exception logs exist when your service is running as expected. If the number of exception logs sharply increases, you must check whether the SOC features are available, check the error messages in exception logs, and then contact the R&D team to resolve the issue. |
|---|---|---|
| Disk Usage | The usage details of the disk. The disk usage is displayed from the following dimensions: the size of total partitions (total disk space), the size of used partitions (used disk space), the size used by the container (total size of the container root directory), and the size used by logs (total size of the log directory). | If the size of used partitions is close to the size of total partitions, check whether the disk space of the physical machine is sufficient. You can determine whether to release the disk space that is used by the container and logs. |

Click **SiemApp** to view the system monitoring details.

| Metric | Description | Exception and handling suggestion |
|---|---|---|
| Pipeline State Distribution | All pipelines of the service, including built-in pipelines and custom pipelines. The number of successful pipelines and the number of failed pipelines are calculated. | If the number of failed pipelines is greater than 0, some pipelines fail. In this case, check whether the custom pipeline settings are correct and resolve the issue based on the logs of the security information and event management (SIEM) container. You can also contact the R&D team to resolve the issue. |
| Pipeline Startup Status | The startup status of the built- in pipeline. The value 1 indicates that the pipeline is started, and the value 0 indicates that the pipeline is not started. | If the value 0 is displayed, you can view the logs of the pipeline related to the SIEM container and resolve the issue. You can also contact the R&D team to resolve the issue. |

| Disk Usage | The usage details of the disk. The disk usage is displayed from the following dimensions: the size of total partitions (total disk space), the size of used partitions (used disk space), the size used by the container (total size of the container root directory), and the size used by logs (total size of the log directory). | If the size of used partitions is close to the size of total partitions, check whether the disk space of the physical machine is sufficient. You can determine whether to release the disk space that is used by the container and logs. |
|---|---|---|

### 2.2 Restart SocApp

If Threat Detection Service (TDS) fails, you can perform the following steps to restart SocApp:
1. Run the following command to log on to the host on which TDS is deployed:

```
  ssh Host IP address
```

2. Run the following command to find the image ID of TDS:

```python
  sudo docker ps -a | grep SocApp
```

3. Run the following command to enter the docker container:

```bash
  docker exec -it [imageId] /bin/bash
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
  curl http://127.0.XX.XX:10070/checkpreload.htm
```

### 2.3 Restart SiemApp

If Threat Detection Service (TDS) fails, you can perform the following steps to restart SiemApp:
1. Run the following command to log on to the host on which TDS is deployed:

```
  ssh Host IP address
```

2. Run the following command to find the image ID of TDS:

```python
  sudo docker ps -a | grep SiemApp
```

3. Run the following command to enter the docker container:

```bash
  docker exec -it [imageId] /bin/bash
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
  curl http://127.0.XX.XX:10070/checkpreload.htm
```
