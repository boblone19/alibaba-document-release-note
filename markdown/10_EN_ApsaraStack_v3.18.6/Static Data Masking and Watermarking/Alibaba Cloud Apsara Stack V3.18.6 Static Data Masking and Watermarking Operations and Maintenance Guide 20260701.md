---
title: "Static Data Masking and Watermarking Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260701"
pdf_pages: 22
source_pdf: "dfe2babde18a78f3_Alibaba Cloud Apsara Stack V3.18.6 Static Data Masking and Watermarking Operations and Maintenance G"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-%E6%95%B0%E6%8D%AE%E9%9D%99%E6%80%81%E8%84%B1%E6%95%8F%E4%B8%8E%E6%B0%B4%E5%8D%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Static%20Data%20Masking%20and%20Watermarking%20Operations%20and%20Maintenance%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Static Data Masking and Watermarking Operations and Maintenance Guide

## Table of Contents

- 1 O&M overview
- 2 Routine Inspections
  - 2.1 Log on to the Apsara Uni-manager Management Console
  - 2.2 View the status of an instance
  - 2.3 View profile
  - 2.4 View tasks
- 3 Metric details
- 4 Core alert handling
- 5 Apsara Stack Security ECS logon (products deployed under yundun_vpc)
- 6 FAQ
  - 6.1 Failed to create or upgrade the Apsara Stack Security console
  - 6.2 faq-about-data-sources
    - 6.2.1 Failed to test the connection to the data source.
    - 6.2.2 File source creation failed
    - 6.2.3 Remote file source test connection failed
    - 6.2.4 Case: Test connection error socket read timeout
  - 6.3 Discover Task Issues
    - 6.3.1 Failed to find that the task has tables.
    - 6.3.2 Inaccurate results found
    - 6.3.3 Found task stuck
    - 6.3.4 Case: When you create a discovery task, fewer tables are seen in the schema than in the source database.
  - 6.4 Desensitization task issues
    - 6.4.1 Field desensitization exception
    - 6.4.2 Data warehousing exceptions
    - 6.4.3 Extremely slow desensitization performance
    - 6.4.4 The desensitization task fails to include tables.
    - 6.4.5 Table initialization failed
    - 6.4.6 Object migration failed
    - 6.4.7 The desensitization task is stuck.
    - 6.4.8 Case: an error is reported when a field that is not desensitized is stored. The field length is too long.

## 1 O&M overview

**Purpose**

This manual guides O&M personnel to perform preventive maintenance on the Apsara Unimanager O&M console to ensure the stable operation of the database static de-sensitivity and watermark system. O&M personnel can handle system problems found during maintenance according to the instructions in this manual. If the problem cannot be solved according to this manual, contact Alibaba Cloud technical engineers to handle it.

**O&M requirements**

O&M personnel must have IT industry skills, including computer network knowledge, computer operation knowledge, and problem analysis and troubleshooting capabilities. O&M personnel must undergo pre-job training to acquire the necessary knowledge of the Alibaba Cloud system, including but not limited to system principles, networking, feature usage, and maintenance tools.

> **Important:** During maintenance operations, O&M personnel must abide by operation regulations to ensure personal safety and system safety. User data must be kept strictly confidential and must not be copied or disseminated without written consent from users.

## 2 Routine Inspections

### 2.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Operations Console User Guide** .

### 2.2 View the status of an instance

**Procedure**

1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Security > Data Security > Static Data**
**Desensitization and Watermarks**.
3. You can view the **Status** and **High Availability Status** information.
**Status**: the status of the instance.
**High Availability**: whether the high availability mode is enabled.

**Exception handling principles**

If the following two types of situations are found in the status view, you must immediately start the troubleshooting process to avoid the problem from expanding: The status is marked as **Exception**. The status is displayed as **Updating** for a long time. If the upgrade is not completed for more than two hours, the status is abnormal.

### 2.3 View profile

**Overview**

The full operation of the de-identified and watermark modules is controlled at the macro level. The key data is displayed by time dimension (day, week, month, or custom period), including the number of data sources, sensitive types, number of sensitive tables, number of sensitive files, number of de-identified tasks running, amount of de-identified data, and top ranking of de-identified tasks. You can also export the statistical results to documents, documents, and other formats for subsequent reporting and archiving. We recommend that you focus on **data source analysis**, which focuses on the fluctuation of the number of data sources and the distribution of sensitive data types, tables, and files. You can also focus on **data desensitization task analysis**, which focuses on the task running frequency, the amount of data desensitized, and the running status. You can use these two dimensions to accurately grasp the running status of modules and quickly locate global exceptions.

**Procedure**

1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Security > Data Security > Static Data**
**Desensitization and Watermarks**.
3. Find the instance that you want to view and click **Details** in the **Actions** column.
4. View the **overview** of the instance.

### 2.4 View tasks

**Overview**

To view the task status and results, you must cover the following six types of tasks: discovery task, desensitization task, watermark task, traceability task, anonymization task, and column encryption task. You must check the three core dimensions to ensure that the task progresses normally. The first is the running status. Check whether there are problems such as abnormal errors and stuck. The second is the task progress, check whether there is stagnation, progress stuck. The third is the duration, which determines whether there is an exception that the duration is too long (exceeds the normal threshold of similar tasks) or too short (suspected incomplete execution). If any of the preceding issues is found, you must immediately view the task details and further analyze and confirm the cause based on the log to provide an accurate basis for subsequent troubleshooting and resolution.

**Procedure**

1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Security > Data Security > Static Data**
**Desensitization and Watermarks**.
3. Find the instance that you want to view and click **Details** in the **Actions** column.
4. On the **Data Discovery**, **Data Desensitization**, **Data Provenance**, **Anonymous**
**Privacy Protection**, and **Column Encryption** tabs, you can view the running status of the
task.

## 3 Metric details

**View the monitoring dashboard of a CMS**

Static data desensitization and watermark products have been connected to the CMS platform. Log on to the product-CloudMonitor to check the running status of the product.
1. Log on to the Apsara Uni-manager Operations console.
2. In the top navigation bar, choose **Products > Migration and Operations >**
**CloudMonitor**.
3. In the left-side navigation pane, choose **Cloud Resource Monitoring > Cloud Product**
**Monitoring** to search for static data desensitization and watermark products.
4. Click the target instance to view the monitoring data of the product.
Operations and maintenance personnel can directly view the following core information through the CMS platform to achieve comprehensive control of the product running status. Instance Usage: includes the number of enabled instances, the distribution of workloads on each instance, and the usage frequency. You can accurately grasp the instance running saturation. Instance status: synchronously displays information such as whether each instance is running normally and whether there are abnormal alerts. This information is complementary to the status check on the white screen page. Resource usage: monitors the CPU, memory, and disk space usage of the instance in real time to warn of potential risks such as insufficient resources.

## 4 Core alert handling

The core alerts for static database de-information and watermarking systems include alerts for CPU, memory, and disk usage overruns. If this type of alert occurs, you should log on to the corresponding instance quickly to view the trigger factors. If necessary, contact Alibaba Cloud technical support. CS logon (products deployed und er yundun_vpc)

## 5 Apsara Stack Security ECS logon (products deployed under yundun_vpc)

**logon (products deployed**

**under yundun_vpc)**

**Query the logon information of a springboard machine**

1. Confirm the deployment form: on Tianji and on PaaS.

**3182 Version: Apsara Infrastructure Management Framework deployment.**

Enter the **OPS1** machine to obtain the oem database connection through the following command and enter the oem database.

```bash
curl -s http://127.0.0.1:7070/api/v3/column/service.res.result|awk -F '": "' '/db_p assword/{print $2}'|awk -F'"' '/yundunoem/{s="mysql -h"$44" -u"$36" -p"$4" -D"$40" -P"$12;gsub("\\\\","",s);print s}'
```

**3182 or later: PAAS deployment.**

Enter the **OPS1** machine. Run the following command to connect to the oem database and enter the oem database.

```
db_data=$(kubectl get secret yundunoem-minirds-secret -n yundun-basic -oyaml | grep db_ | grep -v f:db_); OLD_IFS="$IFS"; IFS=' '; db=(${db_data}); IFS="$OLD_IFS"; db_ host=$(echo ${db[1]}| base64 -d); db_name=$(echo ${db[3]}| base64 -d); db_password= $(echo ${db[5]}| base64 -d); db_port=$(echo ${db[7]}| base64 -d); db_user=$(echo ${ db[9]}| base64 -d); echo "mysql -u${db_user} -P${db_port} -h${db_host} -D${db_name} -p${db_password}"
```

2. Obtain the login information of the springboard machine: VIP and reverse proxy.
i. Execute the following SQL statement to obtain the VIP. Yundun3.16.2SP023 and later support VIP logon.

```
select name,instance_info from o_cluster_resource where cluster_id = (select id fro m o_cluster where name = 'yundun_vpc' and status in ('UPGRADE_SUCCESS','PRODUCE_SUCCESS')) and type in ('ALB','PASSWORD')\G
```

CS logon (products deployed und er yundun_vpc) ii. Execute the following SQL statement to obtain the reverse proxy:

```
select name,instance_info from o_cluster_resource where cluster_id = (select id fro m o_cluster where name = 'yundun_vpc' and status in ('UPGRADE_SUCCESS','PRODUCE_SUCCESS')) and type in ('REVERSE_VIP','PASSWORD')\G
```

3. Log on to the springboard machine.

**on tianji**

Enter the oem container. Go to OPS1 and run the following command to go to the yundunoem container:

```bash
hostname=$(curl -s localhost:7070/api/v3/column/c.id?c.project=yundun-advance | gre p Basic | awk -F '"' '{print $4}' | head -n 1) machine=$(curl -s "localhost:7070/api/v5/ListMachineSR?cluster=${hostname}" | /home /tops/bin/python -m json.tool | grep '"hostname":' | sort | uniq | grep -v vm | awk -F '"' '{print $4}' | head -n 1) ssh $machine containerId=$(docker ps --format "{{.ID}} {{.Names}}" | grep 'oem' | awk '{print $1 }') docker exec -it ${containerId} bash
```

Enter the springboard machine.

```
ssh -p ${mappingPort} root@${mappingIp}
```

**on paas**

On OPS1, run the following command to enter the yundunoem container:

```bash
kubectl exec -it yundun-oem-0 bash -n yundun-basic
```

Enter the springboard machine.

```
ssh -p ${mappingPort} root@${mappingIp}
```

**Query information about ECS instances that are used to**

**desensitize databases**

in the oem database, use the following sql statement to query data. the cluster_type value needs to be obtained from relevant personnel when a new product is connected. the instance_id value is generally displayed on the page. If you want to query all products, you only need to remove the instance_id query condition. CS logon (products deployed und er yundun_vpc)

```
SELECT name, instance_info AS info, TYPE FROM o_cluster_resource WHERE TYPE IN ('ECS', 'PASSWORD') AND NAME LIKE '%ecs%' AND cluster_id IN ( SELECT cluster_id FROM o_commodity_cluster WHERE instance_id = 'discoverymask-CU9KdFfwv2eaflsfYs') \G
```

the following figure shows the query result. the privateIpAddress value is the ip address of the ecs instance, and the password value is the password of the ecs instance.

**ecs password decryption**

The 3181 version of ECS adds password encryption and requires decryption. to decrypt the ecs password, go to the `/home/admin/yundun-csm-private/` directory of the oem container and run the following command.

```bash
# Replace '${xxxx}' with the actual password.
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') decryptPassword '{"password":"${xxxx}"}'
```

# Example

```
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') decryptPassword '{"password":"xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxx"}'
```

# In V3.18.3 and later, use the following method to decrypt data:

```
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') Password/decryptPassword '{"password":"xxxxxx"}'
```

## 6 FAQ

**This topic describes how to troubleshoot common issues.**

### 6.1 Failed to create or upgrade the Apsara Stack Security console

**the Apsara Stack Security console**

The following logic is used to perform hierarchical troubleshooting to accurately locate the root cause of the fault.
1. Check the deployment /upgrade status of the product image first to determine whether the
product image has been completely deployed or upgraded. If the product image has not been completed, this step is used as the core of troubleshooting. The focus is on checking the image pull, deployment progress, and whether there are resource conflicts.
2. If the image deployment /upgrade has been completed, go to the next step to check.
3. Check the startup status of the core process. Check whether the Java process and the DC
process are successfully started. The failure of the process is a frequent cause of the failure. If the image is successfully deployed, the system self-check is performed. If the 200 is successful, the system self-check is performed.

```bash
curl -k 'https://127.0.0.1:443/user/getSystemStatus.action'
```

4. If the process is not started, you must use logs to troubleshoot the cause of the startup
failure (such as configuration errors, missing dependencies, and insufficient permissions).

> **Warning:** To view log details, you must log on to the ECS instance corresponding to the cloud- native product in advance. Before you perform this operation, make sure that you have the logon permission on the corresponding instance and record the operation to avoid affecting other business operations.

### 6.2 faq-about-data-sources

#### 6.2.1 Failed to test the connection to the data source.

**data source.**

Check whether the database connection information configured by the static equipment is correct, and find the customer to confirm whether the database connection information provided by the customer is correct. Check whether the network from the static detachment device to the database server is unblocked. For example, go to the background of the desensitization system and run the ping and nc commands. Check whether the database version is supported, whether the database itself is normal, and whether there are logon restrictions. You can use other devices to configure the IP address of the static product, and then use a third-party client tool to try to connect to the database through jdbc.

#### 6.2.2 File source creation failed

Check whether the `/dbfw_dc` has enough remaining disk space. Check `/` if there is enough remaining disk space.

#### 6.2.3 Remote file source test connection failed

**failed**

check whether the ftp connection information, especially the path information, is correct. check whether the network from the static detachment device to the ftp server is smooth. for example, go to the background of the desensitization system and run the ping and nc commands to verify. check whether the ftp device service is normal. you can use another device to log on to the ftp service through a third-party tool.

#### 6.2.4 Case: Test connection error socket read timeout

**read timeout**

**Problem description**

An error socket read timeout when connecting to Oracle.

**Cause**

The connected database is Oracle's rac, and the connection IP provided by the customer does not provide Oracle services.

**Solution**

The connection is successful after the customer re-provides the IP address.

### 6.3 Discover Task Issues

#### 6.3.1 Failed to find that the task has tables.

View the error message in the discovery task log

```
 /dbfw_bkup/tasklog/DISCOVER_TASK_*.log .
```

Check whether the database user permissions are sufficient. Check whether the database service is normal. You can directly connect to the database to perform the select operation for verification.

#### 6.3.2 Inaccurate results found

View the discovery rule hit ratio in the discovery task log `/dbfw_bkup/tasklog/DISCOVER_TASK_*.log` , and then check the confirmation ratio setting of the discovery rule on the foreground page. Front page to view data samples. Use the database client tool to directly view the source database data.

#### 6.3.3 Found task stuck

Review the discovery task log `/dbfw_bkup/tasklog/DISCOVER_TASK_*.log` to determine which stage or table the card is in. If you find that the task is stuck in a table, connect to the source database to check whether the table status is normal, whether the table is locked, and whether the query can be normal. obtain the jstack information of the java process, obtain the jstack information again in a few minutes, and send the jstack information twice to alibaba cloud technical support students.

#### 6.3.4 Case: When you create a discovery task, fewer tables are seen in the schema than in the source database.

**task, fewer tables are seen in the schema**

**than in the source database.**

**Problem description**

A customer reported that Oracle's source database has 590 tables, but only 578 tables can be seen when creating a discovery task.

**Cause**

After checking, the other 12 tables are temporary tables. Temporary tables are not desensitized. Therefore, temporary tables are filtered out when you create a discovery task.

**Solution**

The product mechanism can be explained directly to the customer. You can use the `select temporary,count(*) from user_tables group by temporary` statement to query whether a table is a temporary table in the source database, as shown in the following figure. A temporary table with the value of Y is a temporary table, and a temporary table with the value of N is not a temporary table. When you create a discovery task, you can only view tables with the temporary attribute of N.

### 6.4 Desensitization task issues

#### 6.4.1 Field desensitization exception

View the error message in the log `/dbfw_bkup/tasklog/MASK_TASK_*.log` of the desensitization task. Obtain the error data in the log and perform desensitization verification on the Desensitization Algorithm page. Directly connect to the source database to see if there is a dirty data. Check whether the desensitization algorithm and parameter configurations are correct.

#### 6.4.2 Data warehousing exceptions

View the error message in the log `/dbfw_bkup/tasklog/MASK_TASK_*.log` of the desensitization task. Check whether the source and destination databases have the same table structure. Check whether there is an overlength or violation of the primary and foreign key constraints and unique constraints. Check whether the space of the destination database is full. Check whether the database service of the destination database is normal.

#### 6.4.3 Extremely slow desensitization performance

**performance**

Check whether a large number of desensitization exceptions are detected. Check the resource usage of the static system for high pressure. Check whether the resource usage of the source and destination databases is under high pressure.

#### 6.4.4 The desensitization task fails to include tables.

**tables.**

View the error message in the log `/dbfw_bkup/tasklog/MASK_TASK_*.log` of the desensitization task. Check whether the services of the source and destination databases are normal, and whether errors are reported at the time when the de-sensitive task fails. Check whether the failed tables are normal in the source database and whether the corresponding schema exists in the destination database.

#### 6.4.5 Table initialization failed

View the error message in the log `/dbfw_bkup/tasklog/MASK_TASK_*.log` of the desensitization task. Check whether the destination database has a table name occupied by an object with the same name. Check whether the desensitized table is associated with a primary foreign key and the associated table is not in the desensitization task. check whether the ddl table in the background database privicy_table_info is correct. check whether the ddl table can be executed normally in the target database.

#### 6.4.6 Object migration failed

View the error message in the log `/dbfw_bkup/tasklog/MASK_TASK_*.log` of the desensitization task. check whether the ddl of the object in the background library table_object is correct. you can use the ddl in the target library to verify whether the object can be executed properly.

#### 6.4.7 The desensitization task is stuck.

View the de-identification task log `/dbfw_bkup/tasklog/MASK_TASK_*.log` to determine which stage or table the card is stuck in. If you find that the desensitization task is stuck in a table, connect the source and destination databases to check whether the table status is normal, whether the table is locked, and whether the query can be normal. obtain the jstack information of the java process, obtain the jstack information again in a few minutes, and send the jstack information twice to alibaba cloud technical support students.

#### 6.4.8 Case: an error is reported when a field that is not desensitized is stored. The field length is too long.

**that is not desensitized is stored. The field**

**length is too long.**

**Problem description**

When you run an Oracle database-to-database desensitization task, a column that is not desensitized is of the char(5) type. However, the column is overlong when it is returned to the database.

**Cause**

Checking the character set shows that the character set of the source oracle library is gbk, the character set of the target oracle library is utf-8, and the data in this column is a Chinese character followed by 3 spaces. Chinese characters are stored in gbk character set with a length of 2 and become 3 in utf8, resulting in an extremely long length (for example, male characters are stored as C4D0 in gbk and E794B7 in utf8).

**Solution**

The destination database is changed to a database with the GBK character set.
