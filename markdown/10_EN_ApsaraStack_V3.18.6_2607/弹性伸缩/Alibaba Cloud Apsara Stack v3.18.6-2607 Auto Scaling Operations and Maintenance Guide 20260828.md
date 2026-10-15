---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 8
source_pdf: "6f4d7e319bfd2b88_Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling Operations and Maintenance Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%BC%B9%E6%80%A7%E4%BC%B8%E7%BC%A9/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Auto%20Scaling%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Log in to the Apsara Uni-manager Operations Console
- 2 Check service status
- 3 Manage components

ger Operations Console

## 1 Log in to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log in to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. ger Operations Console

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the correct username and password.

**Note**

Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .

## 2 Check service status

This topic describes how to check the status of services in an ess cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Resource Management**.
By default, the **Product & Cluster O&M** page appears.
3. In the **Product | Cluster** search box, enter **ess**.
The list displays the cluster, status, instance status, inspection alarms, and operations for the ess product.
4. Click a service in the **Instance Status** column to view the services and components of the
ess cluster.

| Service | Component | Description |
|---|---|---|
| ess- coordinator | EssCoordinat or | The OpenAPI layer that exposes the service and handles request persistence and task distribution. |
|   | EssInit | Initializes the database and pushes all elastic scaling API configuration files to the POP configuration center to initialize the OpenAPI. |
|   | EssTrigger | EssTrigger depends on EssInit. Executes tasks such as health checks, maximum and minimum instance checks, and cleanup after a scaling group is deleted. Triggers scheduled tasks and alarm tasks. |
| ess-worker | EssWorker | Executes all elastic scaling tasks, including creating an ECS instance, adding an SLB backend server, updating an RDS whitelist, and synchronizing CloudMonitor groups. Automatically retries failed tasks and includes an effective rollback mechanism. |
|   | ServiceTest | Runs over 60 regression tests to verify the overall application status and feature completeness. |

5. In the **Operations** column for the target cluster, click **Cluster Details** to check if the
service's **Status** is in its final state. If a service has not reached its final state, you can log on to the component machine. Use commands such as `docker ps` and `docker logs` to check the component's container log. Identify the issue based on any exceptions found in the log. After the issue is resolved, restart the component machine.

## 3 Manage components

This topic describes common operations for ESS components, including viewing component monitoring information, logging on to component machines, and restarting those machines.

**View component monitoring**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Resource Management**.
By default, the **Product & Cluster O&M** page appears.
3. In the **Product | Cluster** search box, enter **ess**.
The list displays the cluster, status, instance status, inspection alarms, and operations for the ess product.
4. In the **Actions** column, click **Cluster Details**.
By default, the **Service** tab is selected.
5. In the **Actions** column for the desired service, click **Details**.
6. On the component details page, perform the required operation.
**View component monitoring information**: In the **Actions** column for the desired
instance, click **Component Information > Metrics** to view **Component Metrics**,
**Machine Metrics**, and **System Service Metrics**.
**Log on to a component machine** :
a. In the **Actions** column for the desired instance, click **Terminal**. b. In the left pane, click **vmXXX**, select an **Account Type** and a **Server Account**, and then click **OK**. c. Run commands on the Terminal Service page.
**Restart a component machine**:
a. In the **Actions** column for the desired instance, click **Operation > Restart**. b. In the dialog box, enter **RESTART** and click **OK**.
