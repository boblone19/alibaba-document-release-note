---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Operations and Maintenance Guide 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 22
source_pdf: "c536ef598a4fe1e1_Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Operations"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/CDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Defined%20Storage%20Cloud%20Parallel%20File%20Storage%20Operations%20and%20Maintenance%20Guide%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Operations and Maintenance Guide 20260827

## Table of Contents

- 1 Overview
- 2 Log in to the Apsara Uni-manager Operations Console
- 3 Query CPFS O&M metrics
  - 3.1 Query the metrics about the CPFS overall status
  - 3.2 Overall performance metrics of CPFS
  - 3.3 CPFS pdisk metrics
- 4 FAQ about CPFS
  - 4.1 Downtime maintenance process

erview

## 1 Overview

This topic describes the purpose of, requirements on, and usage notes for performing O&M operations on Cloud Parallel File Storage (CPFS). This topic also describes how to contact technical support.

**Purpose**

This guide helps O&M engineers perform preventive maintenance on CPFS to ensure longterm system stability. O&M engineers can follow the instructions in this guide to handle system issues that are identified during maintenance. For system issues that are not covered in this guide, the O&M personnel can contact Apsara Stack CPFS engineers for technical support.

**Requirements**

O&M engineers must possess IT skills, including the knowledge of computer networks, distributed storage operations, and troubleshooting. O&M engineers must pass the pre-job training and learn the knowledge of CPFS. The required knowledge of CPFS includes system principles, networking, features, and the use of maintenance tools.

> **Important:** During the maintenance, O&M engineers must follow operation procedures to ensure personal safety and system security. User data must be kept strictly confidential and must not be copied or disseminated without written consent from users.

**Usage notes**

To ensure a stable system and prevent unexpected events, O&M engineers must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of O&M engineers. This prevents system faults that are caused by unauthorized operations. System security Before O&M engineers perform operations on the system, they must be aware of the impacts of the operations. This ensures that the system is not affected by high-risk operations. O&M engineers must record the details about the issues that are encountered during the operations. This helps O&M engineers troubleshoot the issues. Personal safety and data security O&M engineers must take measures to ensure safety based on device manuals when they use electrical equipment. O&M engineers must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

O&M engineers can contact CPFS technical support for help during the maintenance. in to the Apsara Uni-manager Op erations Console

## 2 Log in to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. in to the Apsara Uni-manager Op erations Console

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .

## 3 Query CPFS O&M metrics

This topic describes the core O&M metrics of Cloud Parallel File Storage (CPFS), including the system status metrics, performance metrics, and pdisk metrics.

### 3.1 Query the metrics about the CPFS overall status

**CPFS overall status**

This topic describes how to query the metrics about the Cloud Parallel File Storage (CPFS) overall status.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management** console,
choose **Resource Management > Machines**.
4. Find the host that you want to manage and click **Terminal** in the Actions column.
5. Select a login username and click **OK** to log in to the operating system of the CPFS storage
host.
6. Run the `mmhealth cluster show` command in the operating system to check the overall
status of the cluster.

> **Note:** If the value 0 is displayed in the Failed and Degraded columns, the status is normal.

7. Run the `mmgetstate -Lsa` command to check the CPFS status.

|   | Note CPFS status description: UNKNOWN: The operating system where CPFS resides is being restarted or is shut down, or the operating system network is abnormal. ACTIVE: The CPFS service is in the normal state. ARBITRATING: CPFS is being started or undergoing fault diagnostics. Check whether an error or warning occurs based on the results of the tail -f /var/mmfs/gen/mmfslog command. If the issue persists, contact Alibaba Cloud technical support. DOWN: CPFS is shut down. |   |   |
|---|---|---|---|
|   |   | tail -f |   |
|   | /var/mmfs/gen/mmfslog |   |   |

### 3.2 Overall performance metrics of CPFS

**of CPFS**

This topic describes how to check the performance status of Cloud Parallel File Storage (CPFS) and check whether long waiters exist.

**Background information**

Waiters is an important metric for analyzing the overall performance of CPFS. Given that CPFS relies on Remote Direct Memory Access (RDMA) for communication, Waiters holds exceptional significance for the end-to-end performance of the entire CPFS Erasure Coding Engine (ECE). You can use the mmdiag --waiters command to monitor the performance of operations performed in the current fileset. You can run the `mmlsnode -N waiters -L` command to view the performance of all CPFS nodes. All values are reported in seconds.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management** console,
choose **Resource Management > Machines**.
4. Find the host that you want to manage and click **Terminal** in the Actions column.
5. Select a login username and click **OK** to log in to the operating system of the CPFS storage
host.
6. Run the `mmlsnode -N waiters -L` command to check the return value.
i. Success code: c25a02005_ext.cloud.a02.amtest38: Waiting 0.0034 sec since 2024-06-26_11:43:09, monitored, thread 329701 ReadmitWorkThread: onThCond 0x7FAD24025A98 (IOBundleNSPDCondvar), reason 'wait for NSPD I/O' c25a02005_ext.cloud.a02.amtest38: Waiting 0.0021 sec since 2024-06-26_11:43:09, monitored, thread 276130 ReadmitWorkThread: onThCond 0x7FAD24027D78 (IOBundleNSPDCondvar), reason 'wait for NSPD I/O' c25a02005_ext.cloud.a02.amtest38: Waiting 0.0019 sec since 2024-06-26_11:43:09, monitored, thread 2275926 ReadmitWorkThread: on ThCond 0x7FAD24026C50 (IOBundleNSPDCondvar), reason 'wait for NSPD I/O' ii. Error codes for moderate-severity latency: Waiting 95.0805 sec since 2024-06-26_11:43:01, monitored, thread 3932937 ReadmitWorkThread: on ThCond 0x557F293C9130 (PdiskAvailabilityCondvar), reason 'Until disk availability stabilizes' Waiting 95.0777 sec since 2024-06-26_11:43:01, monitored, thread 2711607 ReadmitWorkThread: on ThCond 0x7F24041146A8 (VLogIOCondvar), reason 'wait for another thread to do log write' Waiting 95.0777 sec since 2024-06-26_11:43:01, monitored, thread 3782474 ReadmitWorkThread: on ThCond 0x7F2404114628 (VLogIOCondvar), reason 'wait for another thread to do log write'

> **Note:** Under idle conditions, return values of 0.00XX sec are normal. Sporadic latency spikes below 2 seconds constitute low-severity latency. Irregular intervals of sub-2-second latencies can be ignored for I/O-insensitive services. Sustained waiters latencies between 2 seconds and 10 seconds cause file system responsiveness degradation (such as slow ls command execution), while CPFS remains operational under redundancy mechanisms if not persistent. Sustained I/O latencies that exceed 15 seconds trigger persistent system stuttering for CPFS file systems. For general business systems, system stuttering can be solved by restarting CPFS. For key business nodes where disk/node loss tolerance is paramount, real-time dump analysis can be performed to troubleshoot the issue. In deadlock scenarios, CPFS automatically captures diagnostic dumps and traces during exception windows.
> In emergency situations, you can reboot the node where long waiters are located to solve the issue.

### 3.3 CPFS pdisk metrics

This topic describes how to monitor hard disk status.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management** console,
choose **Resource Management > Machines**.
4. Find the host that you want to manage and click **Terminal** in the Actions column.
5. Select a login username and click **OK** to log in to the operating system of the Cloud Parallel
File Storage (CPFS) storage host.
6. Run the `mmvdisk pdisk list --recovery-group all` command to query the pdisk metrics
of CPFS. The following figure shows the return value (State).

| pdisk status | Status description | Solution |
|---|---|---|
| OK | Normal pdisk status | None |
| Readonly | pdisk read-only mode | Replace the pdisk with a new one. |

| slow | Slow pdisk | The pdisk enters a sub-healthy state. We recommend that you replace the pdisk with a new one. |
|---|---|---|
| Missing | pdisk loss | Replace the pdisk with a new one. |
| PTOW | pdisk I/O timeout | Replace the pdisk with a new one. |

## 4 FAQ about CPFS

This topic describes how to handle Cloud Parallel File Storage (CPFS) downtime maintenance issues.

### 4.1 Downtime maintenance process

**process**

This topic describes how to perform Cloud Parallel File Storage (CPFS) downtime maintenance.

> **Important:** The following steps are general and subject to actual scenarios.
> Before downtime maintenance, you must stop the upper-layer business and stop the read and write operations on the shared file storage.
> In the following descriptions, ${fs_id} is the file system ID displayed on the frontend, and the bmcpfs prefix, such as 019bebd3, is removed from the ID.

**Procedure for downtime maintenance of a CPFS cluster**

| S N | Step | Node where the operation is performed | Command to be executed | Expected result |
|---|---|---|---|---|
| Unmount the file system from the client node (BMCP instance) and stop the CPFS client service |   |   |   |   |
| 1 | Unmount the file system on the compute node side | Bare Metal Computing Platform (BMCP) instance (CPFS client) | Run the following command on any BMCP node: mmumount ${fsid} -a _ | df-h \|grep ${fs id} _ |
| 2 | Check whether the file system is unmounted | BMCP instance (CPFS client) | Run the following command on any BMCP node: mmlsmount ${fsid} -L _ | Expected output: File system ${fs id} is _ mounted on 0 nodes |

| 3 | Disable the automatic startup feature of the CPFS client service | BMCP instance (CPFS client) | Run the following command on any client node: mmlsconfig \| grep autoload | If the return value is not no, Run the following command: mmchconfig autoload=no |
|---|---|---|---|---|
| 4 | Disable the CPFS client service | BMCP instance (CPFS client) | Run the following command on any client node: mmshutdown -a | If the return value is down, the CPFS client service is disabled. |
| 5 | Check whether the CPFS client service is disabled | BMCP instance (CPFS client) | Run the following command on any client node: mmgetstate -Lsa | If the CPFS state is down, the CPFS client service is disabled. |
| Unmount the file system from a CPFS storage node and stop the CPFS storage service |   |   |   |   |
| 1 | Unmount the file system on the storage node side | CPFS storage node | Log in to each CPFS storage node in turn to run the following command: mmumount ${fsid} -a _ | df -h \|grep ${fs id} _ |
| 2 | Check whether the file system is unmounted | CPFS storage node | Log in to each CPFS storage node in turn to run the following command: mmlsmount ${fsid} -L _ | Expected output: File system ${fs id} is _ mounted on 0 nodes |
| 3 | Disable the automatic startup feature of the CPFS service | CPFS storage node | Log in to any CPFS storage node to run the following command: mmlsconfig \| grep autoload | If the return value is not no, Run the following command: mmchconfig autoload=no |
| 4 | Disable the CPFS storage service | CPFS storage node | Run the following command on any client node: mmshutdown -a | If the return value is down, the CPFS storage service is disabled. |

| 5 | Check whether the CPFS client service is disabled | CPFS storage node | Run the following command on any client node: mmgetstate -Lsa | If the CPFS state is down, the CPFS client service is disabled. |
|---|---|---|---|---|

**Cluster launch process**

| S N | Step | Node where the operation is performed | Command to be executed | Expected result |
|---|---|---|---|---|
| Start the CPFS service on a CPFS storage node and mount the file system |   |   |   |   |
| 1 | Enable automatic CPFS service startup in system settings | CPFS storage node | Run the following command on any storage node: mmchconfig autoload=yes | The return result of the mmchconfig \| grep autoload command is yes. |
| 1 | Start the CPFS storage service | CPFS storage node | Run the following command on any storage node: mmstartup -a | If the return value is active, the CPFS storage service is started. |
| 2 | Check whether the file system is mounted | CPFS storage node | Run the following command on any storage node: mmlsmount ${fsid} -L _ | Expected output: File system ${fs id} is _ mounted on 6 nodes Note The number of nodes on which the CPFS file system is mounted is subject to the actual number. |
| Start the CPFS storage service on the client node (BMCP instance) and mount the CPFS file system |   |   |   |   |
| 1 | Enable automatic service startup in system settings | BMCP instance (CPFS client) | Run the following command on any client node: mmchconfig autoload=yes | The return result of the mmchconfig \| grep autoload command is yes. |

| 1 | Start the storage service on the CPFS client node | BMCP instance (CPFS client) | Run the following command on any client node: mmstartup -a | If the return value is active, the CPFS storage service is started. |
|---|---|---|---|---|
| 2 | Mount a file system | BMCP instance (CPFS client) | Run the following command on any BMCP instance: mmmount ${fsid} -a _ You need to log in to each BMCP instance in turn to run the following command: mount --bind /cpfs/${fsid}/${clusteri _ _ d}/${srcdir} /${tgtdir} _ _ Note This command is for your reference only. The actual command should prevail. | The mount is successful. |
| 3 | Check whether the file system is mounted | BMCP instance (CPFS client) | Log in to each CPFS client in turn to run the following command: mmlsmount ${fsid} -L _ | Expected output: File system ${fs id} is _ mounted on 9 nodes Note The number of nodes to be mounted is subject to the actual number. |

**Check the health status of the cluster (optional)**

| S N | Step | Node where the operation is performed | Command to be executed | Expected result |
|---|---|---|---|---|
| Start the CPFS service on a CPFS storage node and mount the file system |   |   |   |   |
| 3 | Check the network connectivity | CPFS storage node | Log in to each CPFS storage node in turn to run the following command: sudo mmnetverify all | If the return value is Success, the network connection is normal. |

| 4 | Check the disk status | CPFS storage node | Log in to each CPFS storage node in turn to run the following command: mmvdisk pdisk list --rg all --not-ok | If the return value is All pdisks are ok, the disk status is normal. |
|---|---|---|---|---|
| 5 | Check the latencies | CPFS storage node | Run the following command on any storage node: mmlsnode -N waiters -L | If the return value does not contain any latency that lasts for more than 10s, the latencies are normal. Note This data is for your reference only. The actual data should prevail. |
| 6 | Check basic logs | CPFS storage node | Run the following command on any storage node: tail -f /var/mmfs/gen/mmfslog | If no error is returned, the CPFS service is running properly. |
| 7 | Check node status | CPFS storage node | Run the following command on any storage node: mmhealth cluster show | If the returned values of Failed and Degraded are 0, the node status is normal. |
| Start the CPFS service on the client node (BMCP instance) and mount the file system |   |   |   |   |
| 1 | Check the network connectivity | BMCP instance (CPFS client) | Log in to each CPFS client in turn to run the following command: mmnetverify all | If the return value is Success, the network connection is normal. |
| 2 | Check the file system disk status | BMCP instance (CPFS client) | Run the following command on any client node: mmlsdisk /dev/fsname -m | If the return value of Availability is up, the disk status is normal. |
| 3 | Check the latencies | BMCP instance (CPFS client) | Run the following command on any client node: mmlsnode -N waiters -L | If the return value does not contain any latency that lasts for more than 10s, the latencies are normal. |

| 4 | Check basic logs | BMCP instance (CPFS client) | Run the following command on any client node: tail -f /var/mmfs/gen/mmfslog | If no error is returned, the CPFS service is running properly on the client node. |
|---|---|---|---|---|
| 5 | Check node status | BMCP instance (CPFS client) | Run the following command on any client node: mmhealth cluster show | If the returned values of Failed and Degraded are 0, the node status is normal. |
