---
title: "Security Orchestration Automation and Response (SOAR) Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260701"
pdf_pages: 10
source_pdf: "8168b14b6eb1b792_Alibaba Cloud Apsara Stack V3.18.6 Security Orchestration Automation and Response (SOAR) Operations "
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%87%AA%E5%8A%A8%E7%BC%96%E6%8E%92%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Security%20Orchestration%20Automation%20and%20Response%20%28SOAR%29%20Operations%20and%20Maintenance%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Security Orchestration Automation and Response (SOAR) Operations and Maintenance Guide

## Table of Contents

- 1 Log in to the Apsara Infrastructure Management console
- 2 View alert notifications
- 3 View a dashboard
- 4 View an inspection task

to the Apsara Infrastructure Man agement console

## 1 Log in to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log in to the Apsara Infrastructure Management console.

**Prerequisites**

The URL, username, and password that are required to log on to the Apsara Uni-manager Operations Console are obtained from the deployment personnel or administrators. The URL of the Apsara Uni-manager Operations Console is in the format of regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
to the Apsara Infrastructure Man agement console

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Apsara Infrastructure Management**.
alert notifications

## 2 View alert notifications

## 1 Log in to the Apsara Infrastructure Management console.

2. In the top navigation bar of the Apsara Uni-manager Operations Console, choose
**Monitor&Alert > Alert Management** > **Alert Overview**.
3. Use the modules in the left-side navigation pane to view service alert information and
configure related alert notifications. a dashboard

## 3 View a dashboard

2. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Product**
**Operation > Security O&M > Cloud Shield Operations Center**.
3. In the left-side navigation pane, choose **Monitoring and Alerting** > **System Monitoring**.
4. On the **System Monitoring** page, click the **Automated Orchestration** tab. On the
Automated Orchestration tab, view the CPU utilization, load, and status of Security Orchestration Automation and Response (SOAR).
4. In the left-side navigation pane, choose **Monitoring and Alerting > Business**
**Monitoring**.
5. On the **Business Monitoring** page, click the **Automated Orchestration** tab.
a dashboard
6. On the Automated Orchestration tab, click the **sophon-bluespace** card to view the
numbers of successful and failed executions of the SOAR playbook. an inspection task

## 4 View an inspection task

2. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Product**
**Operation > Security O&M > Cloud Shield Operations Center**.
3. In the left-side navigation pane, choose **Inspection and Diagnostics** > **Inspection**
**Configuration**.
4. On the Inspection configuration page, click the Inspection Template tab. On the **Inspection**
**Template** tab, select yundun-soar from the service type drop-down list. Find the inspection
template that you want to manage and click **Inspect Now** in the Operation column. In the Perform Diagnostics panel, click Diagnose Now.

> **Note:** Sandbox diagnostics is used to check whether the network configurations of the Python sandbox on the current tenant side meet your expectations.
> Global diagnostics is used to inspect the system resource usage of the sophon-web and sophon-bluespace services.

5. Switch to the Inspection Records tab. On the Inspection Records tab, find the completed
inspection record and click View in the Operation column. In the panel that appears, view the inspection details.
