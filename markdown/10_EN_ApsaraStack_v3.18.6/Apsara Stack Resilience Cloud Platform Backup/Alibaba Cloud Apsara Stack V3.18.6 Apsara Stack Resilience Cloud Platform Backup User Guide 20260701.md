---
title: "Apsara Stack Resilience Cloud Platform Backup User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 13
source_pdf: "196ad3890ce7f961_Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Resilience Cloud Platform Backup User Guide 20260701"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E5%B9%B3%E5%8F%B0%E5%A4%87%E4%BB%BD/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Resilience%20Cloud%20Platform%20Backup%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Apsara Stack Resilience Cloud Platform Backup User Guide 20260701

## Table of Contents

- 1 Go to the platform backup management page
- 2 Platform backup archive storage
  - 2.1 Create a platform backup archive storage
  - 2.2 Manage a platform backup archive storage
- 3 Configure platform backup archiving
  - 3.1 Configure miniRDS backup
  - 3.2 Configure PANGU master backup
  - 3.3 Configure opsDNS backup
  - 3.4 Configure DNS product backup
  - 3.5 Configure in-cloud OSS bucket backup
- 4 View platform backup archiving records

agement page

## 1 Go to the platform backup management page

**management page**

This topic describes how to go to the platform backup management page in the Apsara Unimanager Operations Console. The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. agement page You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, click **System Config**.
6. In the left-side navigation pane, click **Platform Backup Management**.
e

## 2 Platform backup archive storage

**storage**

### 2.1 Create a platform backup archive storage

**archive storage**

This topic describes how to create a storage for cloud platform backups.
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
**Backup Storage**.
3. Click **Create Storage**.
4. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Storage Name | Enter a name for the custom storage. Example: Storage 1. |
| Protocol Type | Select a protocol based on your business requirements. Valid values: OSS: the object storage service provided by Apsara Stack. Amazon S3: the object storage service provided by Amazon Web Services (AWS). |
| Address | If the Protocol Type parameter is set to OSS, enter an OSS endpoint. If the Protocol Type parameter is set to Amazon S3, enter an Amazon S3 endpoint. |
| AccessKey ID/Username | If the Protocol Type parameter is set to OSS, enter an AccessKey ID or a username of OSS. If the Protocol Type parameter is set to Amazon S3, enter an AccessKey ID or a username of Amazon S3. |

e

| AccessKey Secret/Password | If the Protocol Type parameter is set to OSS, enter an AccessKey secret or a password of OSS. If the Protocol Type parameter is set to Amazon S3, enter an AccessKey secret or a password of Amazon S3. |
|---|---|
| Bucket/Storage Path | If the Protocol Type parameter is set to OSS, enter a storage path of OSS. If the Protocol Type parameter is set to Amazon S3, enter a storage path of Amazon S3. |
| Storage Space | Specify the storage capacity. Unit: GB. |
| Alert Threshold | Specify the threshold for reporting alerts. If the percentage of used storage space exceeds the threshold, an alert is reported. |

5. Click **OK**.

### 2.2 Manage a platform backup archive storage

**archive storage**

This topic describes how to view the details of, modify, and delete a platform backup archive storage. A platform backup archive storage is created.
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
**Backup Storage**.
3. On the Archive Storage page, perform operations based on your business requirements.
View the details of a storage: Find the platform backup archive storage that you want to view and click Details in the Actions column. Modify a storage: Find the platform backup archive storage that you want to modify and click **Edit** in the
**Actions** column. You can modify the values of parameters except **Protocol Type**.
Click **OK**. Delete a storage: Find the platform backup archive storage that you want to delete and click **Delete** in the **Actions** column. In the message that appears, click **OK**.

## 3 Configure platform backup archiving

**archiving**

### 3.1 Configure miniRDS backup

This topic describes how to configure a backup policy for miniRDS. A backup archive storage is created. For more information, see . A database instance is created. By default, the dbaas_db, perf_db, dukang_db, bak_db, robot_db, kmsdata, kmsdata_tiangong, idccrypto_data, os_meta, oss_chiji, ummak, account, location, diamond, schedulerx, ram_slave_proxy, subaccount, ram_master, and hsmidcdatabase instances can be backed up.
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
3. Click the **MiniRDS Backup** tab.
4. Configure the backup policy. The following table describes the parameters.
The preset backup policy is used. You need to only specify storage settings.

| Parameter | Description |
|---|---|
| Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
| Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.
6. Click **Add Backup Instance**.
7. Select the database instances that you want to back up, and then click **OK**.

### 3.2 Configure PANGU master backup

**backup**

This topic describes how to configure a backup policy for the PANGU master. A backup archive storage is created. For more information, see . A PANGU cluster is deployed.
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
3. Click the **PANGU Master Backup** tab.
4. Configure the backup policy. The following table describes the parameters.
The preset backup policy is used. You need to only specify storage settings.

| Parameter | Description |
|---|---|
| Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
| Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.

### 3.3 Configure opsDNS backup

This topic describes how to configure a backup policy for opsDNS. A backup archive storage is created. For more information, see .
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
3. Click the **opsDns** tab.
4. Configure the backup policy. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
|   | Archive Storage | Select the backup archive storage created in advance from the drop-down list. |

| sara Stack Resilience | Cloud Platform Backup User Gui e·Configure platform backup ar hivin |   |
|---|---|---|
| Storage Settings |   |   |
|   | Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |
|   | Backup Start At | Select the time when the backup starts. |
| Backup Policy | Cycle Type | Daily Backup: The backup is performed every few days. Hourly Backup: The backup is performed every few hours, such as every hour or every four hours. |
|   | Interval | Specify the interval between two consecutive backups. Enter a positive integer. |

5. Click **Save**.

### 3.4 Configure DNS product backup

This topic describes how to configure a backup policy for the DNS product. A backup archive storage is created. For more information, see .
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
3. Click the **DNS Product Backup** tab.
4. Configure the backup policy. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Storage Settings | Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
|   | Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |
|   | Backup Start At | Select the time when the backup starts. |

| Backup Policy | Cycle Type | Daily Backup: The backup is performed every few days. Hourly Backup: The backup is performed every few hours, such as every hour or every four hours. |
|---|---|---|
|   | Interval | Specify the interval between two consecutive backups. Enter a positive integer. |

5. Click **Save**.

### 3.5 Configure in-cloud OSS bucket backup

**backup**

This topic describes how to configure a backup policy for in-cloud Object Storage Service (OSS) buckets. A backup archive storage is created. For more information, see .
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
3. Click the **In-cloud OSS Bucket Backup** tab.
4. Configure the backup policy. The following table describes the parameters.
The preset backup policy is used. You need to only specify storage settings.

| Parameter | Description |
|---|---|
| Archive Storage | Select the backup archive storage created in advance from the drop-down list. |
| Retention Period (Days) | Specify the number of days to retain the backup archive data. Enter a positive integer. |

5. Click **Save**.
records

## 4 View platform backup archiving records

**archiving records**

This topic describes how to view the archive details after the backup is archived. Platform backup is archived.
1. Go to the platform backup management page. For more information, see .
2. In the left-side navigation pane, choose **Platform Backup Management > Platform**
**Backup Records**.
3. On the Archiving Details page, view the backup archive details.
Archive details are not displayed one week after the backup is deleted.
