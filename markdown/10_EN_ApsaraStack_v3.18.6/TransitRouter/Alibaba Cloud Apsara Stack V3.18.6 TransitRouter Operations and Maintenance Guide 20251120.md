---
title: "TransitRouter Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20251120"
pdf_pages: 12
source_pdf: "71545e88ff505c9b_Alibaba Cloud Apsara Stack V3.18.6 TransitRouter Operations and Maintenance Guide 20251120.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%BD%AC%E5%8F%91%E8%B7%AF%E7%94%B1%E5%99%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20TransitRouter%20Operations%20and%20Maintenance%20Guide%2020251120.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# TransitRouter Operations and Maintenance Guide

## Table of Contents

- 1 Log on to the Apsara Uni-manager Operations Console
- 2 CEN O&M
  - 2.1 Manage CEN-TR clusters
  - 2.2 Manage CEN workflows

ager Operations Console

## 1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
ager Operations Console

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

## 2 CEN O&M

> **Note:** By default, the CEN O&M module is not displayed. To use this module, perform the following operations: Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, click **User Authorities**. In the left-side navigation pane, click **Menu** **Management**. On the Menu management page, modify the menu settings to display the CEN O&M module.

### 2.1 Manage CEN-TR clusters

Virtual machines (VMs) that run on physical machines have their own IP addresses, and can access the Internet and host applications.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **CEN O&M** > **CEN-TR**
**Clusters**.
4. On the **CEN-TR Clusters** page, view the **node information** and **aggregate metrics**.
**Node Information**: Select a cluster from the **Cluster** drop-down list. The information
about the selected cluster is displayed, including the **node IP address**, **hostname**, and
**status**.
**Aggregated Metrics**: By default, the metrics within the last hour are displayed. You can
view metrics on the **Core Metrics** and **All Metrics** tab. The following table describes the metrics.

| Metric | Description |
|---|---|

| ations and Maintenance Gui EN O&M | TransitRoute |
|---|---|

| multicast rx bps _ _ | The rate of inbound multicast data that is transmitted to the transit router node. Unit: bit/s. |
|---|---|
| multicast rx pps _ _ | The number of inbound multicast packets that are sent to the transit router node per second. |
| multicast target tx bps _ _ _ | The expected rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
| multicast target tx pps _ _ _ | The expected number of outbound multicast packets that are sent from the transit router node per second. |
| multicast tx bps _ _ | The rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
| multicast tx pps _ _ | The number of outbound multicast packets that are sent from the transit router node per second. |
| rx bps (core metric) _ | The rate of inbound data that is transmitted to the transit router node. Unit: bit/s. |
| rx drop pps _ _ | The number of dropped inbound packets that are sent to the transit router node per second. |
| rx pps _ | The number of inbound packets that are sent to the transit router node per second. |
| tx bps (core metric) _ | The rate of outbound data that is transmitted from the transit router node. Unit: bit/s. |
| tx drop pps _ _ | The number of dropped outbound packets that are sent from the transit router node per second. |
| tx pps _ | The number of outbound packets that are sent from the transit router node per second. |

> **Note:** Configure **Start Time and End Time** to filter and view metrics within the specified time range.
> Click **Last 1 Hour**, **Last 3 Hours**, **Last 6 Hours**, or **Last 12 Hours** to quickly filter metrics.
> The interval between the start and end times cannot be greater than 12 hours.

**What to do next**

**View node monitoring data**

In the **Node Information** list, find the node that you want to view and click **Details** in the
**Operation** column. On the **TR Node** page, view the monitoring data of the node within a
specific period of time, including the **traffic**, **CPU utilization**, and **memory usage**. The following table describes the key monitoring metrics.

| Category | Metric | Description |
|---|---|---|

| Traffic | Flow | multicast rx bps _ _ | The rate of inbound multicast data that is transmitted to the transit router node. Unit: bit/s. |
|---|---|---|---|
|   |   | multicast target tx bps _ _ _ | The expected rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
|   |   | multicast tx bps _ _ | The rate of outbound multicast data that is transmitted from the transit router node. Unit: bit/s. |
|   |   | rx bps _ | The rate of inbound data that is transmitted to the transit router node. Unit: bit/s. |
|   |   | tx bps _ | The rate of outbound data that is transmitted from the transit router node. Unit: bit/s. |
|   | BandWidth | multicast rx pps _ _ | The number of inbound multicast packets that are sent to the transit router node per second. |
|   |   | multicast tx pps _ _ | The number of outbound multicast packets that are sent from the transit router node per second. |
|   |   | multicast target tx pps _ _ _ | The expected number of outbound multicast packets that are sent from the transit router node per second. |
|   |   | rx drop pps _ _ | The number of dropped inbound packets that are sent to the transit router node per second. |
|   |   | tx drop pps _ _ | The number of dropped outbound packets that are sent from the transit router node per second. |
|   |   | tx pps _ | The number of outbound packets that are sent from the transit router node per second. |
| 0 |   | > Document Version: 2025112 |   |

|   |   | rx pps _ | The number of inbound packets that are sent to the transit router node per second. |
|---|---|---|---|
| CPU Utilization |   | cpu util _ | The CPU utilization, in percentage. |
| Memory Usage |   | mem util _ | The memory usage, in percentage. |

> **Note:** Select a time range from the **Query Time** drop-down list to filter metrics within the selected time range.
> Click **Last 1 Hour**, **Last 3 Hours**, **Last 6 Hours**, and **Last 1 Day** to quickly filter metrics.
> Select a CPU model from the drop-down list in the upper-right corner of the **CPU** **Utilization** list to view CPU utilization by CPU model.

### 2.2 Manage CEN workflows

On the CEN workflows page, you can view the workflow event details and relevant information about a Cloud Enterprise Network (CEN) instance. If a workflow is in an abnormal state, you can re-push, skip, and terminate the workflow.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Services** > **CEN O&M** > **CEN**
**Workflows**.
4. On the page that appears, select an option from the **Business Foundation System Type**
drop-down list, enter an event ID in the **Event ID** field, and then click **Search**. You can select **CEN Yaochi** or **BR Yaochi** from the **Business Foundation System Type** drop-down list.
5. View the **basic information** and **procedure details** about the workflow.
**Basic information**: displays the following parameters: **Event ID**, **UID**,
**ContextNameSpace**,**NameSpace**,**Instance ID**,**SourceNameSpace**,**Current**
**status**,**Processing times**, and **Event information details**.
Move the pointer over **View** next to **Event information details** to view the details of the event.
**Procedure details****:** displays the step serial number and the following parameters:

**Event ID,Namespace,State,StepMessage,Data,Creation time, and**

**Modification time.**

Move the pointer over **Details** in the **StepMessage** column to view the details of the step.

**What to do next**

| Operation | Procedure |
|---|---|
| Terminate a workflow | 1. In the Basic information section, click Terminate in the upper-right corner. 2. In the message that appears, click OK. |
| Re-push a workflow | When the event status of a workflow is not in the Succeed state, you can perform a retry on the workflow. 1. In the Basic information section, click Re-push in the upper-right corner. 2. In the message that appears, click OK. |
| Skip a workflow | 1. In the Basic information section, click Jump in the upper-right corner. 2. In the dialog box that appears, configure the Select Jump Method and Steps to Jump parameters. Select Jump Method: Select a skip method. Valid values: Previous Step, Next, and Specify Steps. Steps to Jump: Enter the number of steps to skip. This parameter takes effect and is required if you set the Select Jump Method parameter to Specify Steps. 3. Click OK. |
