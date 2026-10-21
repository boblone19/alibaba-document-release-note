---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) Operations and Maintenance Guide 20241213"
product_version: "V3.18.3"
doc_version: "20241213"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) Operations and Maintenance Guide 20241213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Operations%20and%20Maintenance%20Guide%2020241213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) Operations and Maintenance Guide 20241213

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
- 2 Check the service status
  - 2.1 Basic inspection
  - 2.2 Advanced inspection

cture Management console

## 1 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
cture Management console

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Apsara Infrastructure Management Framework**.

## 2 Check the service status

### 2.1 Basic inspection

The basic inspection of Web Application Firewall (WAF) checks whether the service runs as expected.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. In the **Cluster** search box, enter **SemaWafCluster**.
4. Then, click the name of the cluster. The **Cluster Details** page appears.
5. In the **Service** search box on the **Services** tab, enter **yundun-semawaf**. Then, check
whether the service runs as expected.

### 2.2 Advanced inspection

The advanced inspection of Web Application Firewall (WAF) checks the system status and service status.

**Procedure**

1. Log on to the two physical machines of WAF.
i. In the left-side navigation pane, choose **Operations > Cluster Operations**. ii. In the **Cluster** search box, enter **SemaWafCluster**. Then, click the name of the cluster. The **Cluster Details** page appears. iii. In the **Service** search box on the **Services** tab, enter **yundun-semawaf**. Then, click
**Details**. The **Service Details** page appears.
iv. In the **Server Role** search box, enter **YundunSemawafApp#**. v. View the machine information and click **Terminal** in the Actions column to log on to the two physical machines of WAF.
2. Check the system status.
i. View system logs. Run the dmesg -T |tail -30 command to check whether exception logs exist. ii. Check the system loads. Run the `free -h` command to check whether the memory usage is normal. Run the `df -h` command to check whether the disk usage is normal. Run the `uptime` command to check whether the average system load is normal. Run the `top` command to check whether the CPU utilization is normal.
3. Check the service status.

> **Note:** In the WAF installation directory /home/safeline, perform the following operations.

i. Run the `cd /home/safeline` command to open the installation directory. ii. Check the minion service. a. Run the `systemctl status minion` command to check the execution time and the status of the minion service. b. Run the `tail -100 logs/minion/minion.log` command to check whether exception logs exist. iii. Check the mgt-api service. a. Run the `docker logs --tail 50 mgt-api` command to check whether exception logs exist. b. Run the `docker exec -it mgt-api supervisorctl status` command to check whether the service runs as expected and whether **uptime** is normal. c. Run the `tail -50 logs/management/gunicorn.log` command to whether exception logs exist. d. Run the `tail -50 logs/management/daphne.log` command to whether exception logs exist. e. Run the `tail -50 logs/management/scheduler.log` command to check whether exception logs exist. f. Run the `tail -50 logs/management/dramatiq.log` command to check whether exception logs exist. iv. Check the redis service. Run the `docker logs --tail 50 mgt-redis` command to check whether exception logs exist. v. Check the detector service. a. Run the `docker logs --tail 50 detector-srv` command to check whether exception logs exist. b. Run the `tail -50 logs/detector/snserver.log` command to check whether exception logs exist. c. Run the curl 127.0.0.1:8001/stat | grep num command to check whether the service responds and whether the status of the real-time request processing data is normal. For example, check whether the value of the **req_num_total** parameter is normal. The req_num_total parameter indicates the number of requests that are processed within the previous 5 seconds. vi. Check the tengine service. a. Run the `docker logs --tail 50 tengine` command to check whether exception logs exist. b. Run the `tail -50 logs/nginx/error.log` command to check whether exception logs exist. vii. Check the mario service. a. Run the `docker logs --tail 50 mario` command to check whether exception logs exist. b. Run the `tail -50 logs/mario/mario.log` command to check whether exception logs exist. c. Run the `curl 127.0.0.1:3335/api/v1/state` command to check whether the service responds and whether the status of the real-time request processing data is normal. For example, check whether the **num_pending** parameter remains at a high value of nearly 10,000 or whether the value of the **num_processed_last_10s** parameter is normal. The num_processed_last_10s parameter indicates the number of requests that are processed within the previous 10 seconds.
