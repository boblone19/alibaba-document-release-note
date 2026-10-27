---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager Operations and Maintenance Guide 20241213"
product_version: "V3.18.3"
doc_version: "20241213"
pdf_pages: 11
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager Operations and Maintenance Guide 20241213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%AE%A1%E5%AE%B6/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Big%20Data%20Manager%20Operations%20and%20Maintenance%20Guide%2020241213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager Operations and Maintenance Guide 20241213

## Table of Contents

- 1 Routine maintenance
  - 1.1 Perform routine maintenance
  - 1.2 View the ABM operating status
  - 1.3 Troubleshooting
- 2 Backup and restore

## 1 Routine maintenance

### 1.1 Perform routine maintenance

You can perform routine maintenance on Apsara Big Data Manager (ABM) in the Apsara Infrastructure Management console.

**Inspections in the Apsara Infrastructure Management console**

1. Log on to the ABM console.
2. Click the
icon in the upper-left corner of the ABM console, and click **TIANJI** to log on to the Apsara Infrastructure Management console.
3. Log on to the ABM console. In the upper-right corner, click O&M. On the page that appears,
click the **Clusters** tab to verify that all containers are in their final state.
4. Log on to the ABM console. In the upper-right corner, click Monitor. On the page that
appears, click the **Dashboard** tab to verify that alerts have not been generated.

**Metrics and alert handling**

Monitor hardware components The system retains logs for 30 days and automatically deletes historical logs. If a disk alert is triggered when a large amount of logs exhaust disk space, contact technical support. System exception If a system exception occurs during the inspection, handle the exception in the ABM console. If the exception message is unclear, contact technical support.

### 1.2 View the ABM operating status

**status**

ABM monitors its own health and operating metrics. You need to regularly handle ABM alerts and view ABM operating metrics to evaluate system downtime risks in the future.

**View ABM operating metrics**

In ABM, click **O&M** on the top and click **Clusters**. The **Overview** tab appears. The **Overview** tab displays tendency charts for cluster metrics, including the CPU, memory, disk, load, package, TCP, and disk root directory usage. You need to regularly view and record these metrics to evaluate system downtime risks in the future.

**Handle ABM alerts**

ABM cluster alerts are classified into Critical, Warning, and Exception alerts. You need to handle these alerts in time, especially Critical and Warning alerts.
1. On the **Clusters** page, click the **Health Status** tab.
The **Health Status** tab displays all check items and the alerts that were generated during the check.
2. Click the **Fold** icon for a check item with alerts. All hosts on which the check item was
performed appear.
3. Click a host. In the dialog box that appears, click **Details** for an alert. The alert cause
appears on the right.
4. Click **Details** for a check item with an alert and view the fix method for the alert in the
dialog box that appears.
5. Handle the alert based on the fix method.
You may need to log on to the host when handling the alert. For more information, see Log on to a host.
6. After the alert is handled, click **Refresh** for the host to perform the check again in real
time. In this way, you can check whether the alert is cleared.

**Log on to a host**

You may need to log on to a host to handle alerts or other issues that occurred on the host.
1. On the Health Status tab, click the **Fold** icon for a check item.
2. Click the **Logon** icon for a host. The **TerminalService** page appears.
3. On the **TerminalService** page, select the host on the left to log on to it.

### 1.3 Troubleshooting

**Common failures**

**Logon failure**

If you failed to log on to ABM, clear the cache and cookies in your web browser, and then try again. Based on the logon failure message that appears, check whether the following issues exist: The password that you entered is incorrect. Your account has been locked. Your account has been disabled.

**Other failures**

Contact technical support.

## 2 Backup and restore

**Back up data**

ABM uses a high-availability database. You do not need to manually back up data. To obtain full backup data, contact technical support.

**Restore data**

You do not need to restore data for ABM.
