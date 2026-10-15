---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Operations and Maintenance Guide 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 14
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Operations and Maintenance Guide 20260827.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20NAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20File%20Storage%20NAS%20Operations%20and%20Maintenance%20Guide%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Operations and Maintenance Guide 20260827

## Service architecture

File Storage NAS (NAS) is a cloud service that provides file storage for compute nodes such as Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. NAS supports standard file access protocols. NAS file systems are based on Apsara Distributed File System. NAS maintains three copies for each data file across multiple storage nodes. Frontend nodes receive and cache connection requests from Network File System (NFS) clients. Frontend nodes are highly available because they are stateless and distributed. In a cluster of six nodes, less than 30 minutes is required to restore one TB of data. The larger the cluster size, the faster the restoration speed. For more information, see **NAS Technical Whitepaper**.

## Routine maintenance

### View the status of a KV

**service**

This topic describes how to check whether the KV service of a File Storage NAS (NAS) cluster is normal.
1. Find the RecycleJob role in the nas-recycle service of the cluster and log on to the target
machine.
2. Use the kuadmin tool to view the NAS app service added to the KV service.

```
/apsara/deploy/kuadmin listapp
```

If an error occurs in the output of the listapp command, the kvmaster service is abnormal.
3. Use the ku tool to check whether the KV service is normal.

```
/apsara/deploy/ku checkready nas checkready ocm
```

If no output is returned for the checkready command or the status is NO, the KV service is abnormal.
4. Use the mcu tool to view the status and information of the kvmaster service.
i. Query the kvmaster service, which is typically 3master.

```
/apsara/deploy/mcu gas
```

ii. Query kvmaster config.

```
/apsara/deploy/mcu gac
```

### Query the information about

**file systems and users**

1. Find the RecycleJob role in the nas-recycle service of your cluster and log on to the target
machine.
2. Use the ocm_cmd and ku tools to query the file system ID (fsid) and the corresponding
partition. i. Query the volume and fsid by specifying the username.

```
/apsara/deploy/ocm_cmd list_volume -u <user>
```

ii. Query the partition corresponding to the file system by specifying the fsid parameter.

```
/apsara/deploy/ku querypart nas <fsid>
```

3. In the RecycleJob role, use the ocm_cmd tool to query the information about the NAS cluster
and permission group. Query the volume and fsid by specifying the username.

```
/apsara/deploy/ocm_cmd list_volume -u <user>
```

4. Query the information about deleted volumes.

```
/apsara/deploy/ocm_cmd list_deleted_volume
```

5. Query the mount information by user and volume.

```
/apsara/deploy/ocm_cmd get_volume_mount_info -u <user> -v <volume>
```

6. Query the protocol type of the file system by user and volume.

```
/apsara/deploy/ocm_cmd get_volume_protocoltype -u <user> -v <volume>
```

1 indicates the Network File System (NFS) protocol. 2 indicates the Server Message Block (SMB) protocol. 3 indicates the combination of NFS and SMB.
7. Query the permission group by user.

```
/apsara/deploy/ocm_cmd list_access_group -u <user>
```

8. Query the permission policy by user and permission group.

```
/apsara/deploy/ocm_cmd list_access_rule -u <user> -g <group>
```

9. Modify the protocol type of the file system by user and volume.

```
/apsara/deploy/ocm_cmd update_volume_protocoltype -u <user> -v <volume> --protocolTyp e <1/2/3>
```

0. Query the partition and distance information.
i. Query the kvserver information of the cluster.

```
/apsara/deploy/ku --interactive=false --command=getallserver --appname=nas |grep 10280|grep tcp|awk '{print $2}'
```

ii. Query the partition and distance information based on the kvserver information.

```
/apsara/deploy/ofsu --interactive=false --command=getpartdist --param1=<kvserver> --param2=nas | grep -v PID
```

1. Query the detailed information of the file system.
i. Query all partitions.

```
/apsara/deploy/ku --interactive=false --command=getallpart --param1=nas | grep tc p | awk '{print $3}'
```

ii. Query the file system by specifying the partition.

```
/apsara/deploy/ofsu --interactive=false --command=getfilesystem --appname=nas --p aram1=<partition>
```

iii. Query file system details by user and volume.

```
/apsara/deploy/ofsu --interactive=false --command=getfsinfo --appname=nas --param 1=<user> --param2=<volume>
```

2. Query the azone and location information of the NAS cluster.
i. Obtain the ocm tool. The access_id and access_key is required.

```
vim /cloud/app/nasnfs/NFSSupervisor#/nfs_supervisor/current/conf.merge/ocm_cmd.json
```

ii. Record the ocm_host, access_id, and access_key information and use the ocm tool to query the location information.

```
/apsara/deploy/ocm_tool lli --ocm_host=<ocm_host> --access_id=<access_id> --acces s_key=<access_key>
```

### Query the information about a

**cluster recycle job**

1. Find the RecycleJob role in the nas-recycle service of the cluster and use the nas_ju tool to
query the current recycle job of the cluster.

```
/apsara/deploy/nas_ju list
```

2. Query the details of the recycle job by specifying the job name.

```
/apsara/deploy/nas_ju info <job_name>
```

Example

```
/apsara/deploy/nas_ju info volume_recycle_20171024105007
```

### View the module service logs

**of a NAS cluster**

1. Find the RecycleJob role in the nas-recycle service of the cluster and view the logs of the KV
service. After you use the ku and kuadmin tools to determine whether the KV service is abnormal, you can view the corresponding ku.LOG and kuadmin.LOG in the /apsara/deploy/log directory to obtain the error message.
2. Log on to the OcmServer machine to view the ocm logs.
Generally, three ocm machines are deployed for load balancing. To find specific request logs, you may need to check the three machines.

```
vim /cloud/log/nas-ocm/OcmServer#/ocm_server/ocm_server.LOG
```

3. Log on to the Tengine machine under the nas-ocm service to view the NGINX logs.

```
cd/cloud/log/nasocm/Tengine#/tengine
```

```
cd /cloud/log/nas-ocm/Tengine#/tengine
```

The tengine_starter.log file stores the startup logs. The latest access_log file stores the success logs and the error_log file stores the error logs.
4. Log on to the NFSServer machine to view the ganesha logs.

```
vim /cloud/log/nas-kvengine/KVServer#/kv_server/ganesha.LOG
```

### Set the disk usage limit

By setting the disk usage limit, you can control the total amount of data written to disks. When the data write volume reaches the limit, the system denies data writing. When the data write volume drops below the limit, the system resumes data writing. To set the disk usage limit, perform the following steps:
1. Log in to the Apsara Uni-manager Operations Console
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane, click **Product & Cluster O&M**. Enter **nas** in the **Product |**
**Cluster** search box.
4. Find your cluster and click **Cluster Details** in the Actions column.
5. On the **Desired State Configuration** tab, choose **services > nas-nfs > user >**
**nfs_supervisor** in the file list, and configure the nfs_supervisor.json file.
`{`

```json
    "nas_disk_usage_limit":90
```

`}` The value of the **nas_disk_usage_limit** parameter is a percentage. Data writing stops when the data write volume reaches the specified value. We recommend that you set the value to **90**. If the nfs_supervisor.json file is not created for your cluster, perform the following operations: i. On the right side of the **services > nas-nfs > user** folder, choose
**> Create File**.
Create a folder named nfs_supervisor. ii. In the **Create File** dialog box, set **Creation Type** to **Folder** and **File/Folder Name** to nfs_supervisor.json, and then click **OK**. iii. On the right side of the nfs_supervisor folder, choose
**> Create File**. Create a file
named nfs_supervisor.json. iv. In the **Create File** dialog box, set **Creation Type** to **File** and **File/Folder Name** to nfs_supervisor.json. v. Configure the nfs_supervisor.json file. `{`

```json
    "nas_disk_usage_limit":90
```

`}` The value of the **nas_disk_usage_limit** parameter is a percentage. Data writing stops when the data write volume reaches the specified value. We recommend that you set the value to **90**.
6. After the configuration is changed, the cluster is rolled again and the configuration takes
effect.

**Note**

After data writing is disabled, you can use one of the following methods to resume data writing: Delete the file system or file content and perform write operations seven days later. The system recycles deleted data within seven days. Change the value of the nas_disk_usage_limit parameter.

**Verify the configuration**

To verify the configuration, perform the following steps:
1. Create a file system and mount it.
2. Write data to the file system and make sure that the data volume reaches the limit. Verify
that data writing is disabled. The use of other commands, such as ACL commands, is not affected.
3. View logs.
