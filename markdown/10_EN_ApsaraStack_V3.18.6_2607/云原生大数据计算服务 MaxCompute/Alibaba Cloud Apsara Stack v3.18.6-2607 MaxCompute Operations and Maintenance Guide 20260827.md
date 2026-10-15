---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Operations and Maintenance Guide 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 160
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Operations and Maintenance Guide 20260827.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AE%A1%E7%AE%97%E6%9C%8D%E5%8A%A1%20MaxCompute/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20MaxCompute%20Operations%20and%20Maintenance%20Guide%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Operations and Maintenance Guide 20260827

## MaxCompute job workflow

This article describes the job execution architecture of the MaxCompute distributed computing system. It explains the end-to-end concepts, from user task submission to underlying resource scheduling, to help you understand system operations and troubleshooting logic.

**MaxCompute job workflow diagram**

| user center 6. Persist, queue, & schedule job 2. User auth Scheduler 1. Submit 12. End request HTTPServer/ Frontend 7. Submit task execution 5.1 Return 5. Send request machine X success async 3. Forward e rx ee qc uu eti so tn Executor request 12. End 8. Find service odpsWorker subprocess by type Periodically & version query results 4. P &a r As Pe r ae uq tu hest SQL p_v roe crs ei so snXX I 9. Compile & optimize SQL |   | Fuxi job 11. Execute SQL runtime 10. Submit Fuxi job |
|---|---|---|

it

**Concepts**

The following concepts are involved in MaxCompute jobs.
1. MaxCompute instance: A running instance of a MaxCompute job. If no job is explicitly
defined, it is considered an anonymous job. A single MaxCompute job can contain multiple tasks, allowing one instance to submit several SQL or MapReduce (MR) tasks for parallel or serial execution. However, since organizing multiple tasks under a single job is uncommon, a MaxCompute instance typically contains just one task.
2. MaxCompute task: A specific unit of work. There are nearly 20 task types, such as SQL, MR,
admin, LOT, and XLib, each with significantly different execution logic. Within the same instance, different tasks are identified by their task_name. A MaxCompute task runs on the control cluster. Simple operations, like metadata modifications, can complete their entire lifecycle on the control cluster. However, for computational workloads, the task must submit a Fuxi job to a compute cluster.
3. Fuxi job: A computational model in the task scheduling system. It is a task that runs to
completion, as opposed to a Fuxi service, which is a long-running process. A Fuxi job supports Directed Acyclic Graph (DAG) scheduling. Each job has a corresponding job master that handles resource scheduling within that job. For SQL queries, Fuxi jobs are divided into offline jobs and online jobs (which evolved from Service Mode). An online job, also known as a near-real-time task, uses long-running processes that remain active in the system. These processes execute tasks on demand, reducing startup and shutdown overhead and improving processing speed. A MaxCompute task can submit jobs to multiple compute clusters. A Fuxi job is uniquely identified by its cluster name and job name. The task scheduling system stores the job's JSON plan and final status in the Apsara Distributed File System.
4. Fuxi task: A concept within a Fuxi job, similar to a MaxCompute task. Different Fuxi tasks
represent different execution logic. Fuxi tasks can be linked together through pipes to perform complex operations.
5. Fuxi instance: An instance of a Fuxi task and the smallest unit of work scheduled by the
task scheduling system. During execution, a single task breaks down into many logical units that are processed in parallel to increase speed. All instances of a task share the same execution logic but operate on different input and output data.
6. Fuxi worker: A low-level concept in the task scheduling system. A worker is an operating
system process. Multiple Fuxi instances can share and reuse a single worker, but a worker can process only one instance at a time. InstanceID: The unique identifier for a MaxCompute job. It is essential for troubleshooting. You can construct the logview for an instance by using its project name and InstanceID. service master/job master: Master nodes for service and job tasks, respectively. They request and schedule resources, creating work plans for workers, and monitoring the worker lifecycle.

## O&M commands and tools

### Usage notes

Before you use MaxCompute O&M commands and tools, take note of the following information.

**Instructions for account usage**

During MaxCompute O&M, the default account is admin, and all commands must be executed by using the admin user. If a command requires superuser privileges, you must run the command by using the admin account with sudo.

**Account usage management**

To mitigate security risks associated with high-privilege accounts, MaxCompute has integrated an access control list (ACL) management mechanism to restrict the usage scope of accounts and ensure that MaxCompute can be called only within the platform-side network, such as the specified virtual private cloud (VPC), to prevent privilege abuse.
**This ACL management mechanism has the following features** :
**Traceability of interception records**:
When a platform AccessKey pair is blocked by ACL due to being used outside its authorized scope, the system automatically generates an interception log, which can be viewed in the ACL account management interface. For more information, see **Apsara Uni-manager**

**Operations Console User Guide > Security management > Account security >**

**Account management for cloud services > Account ACL control**.
**PPv2 enablement required for VPC scenarios**:
To obtain full capability support within a VPC, you must enable the `odpsPPV2Enable` feature and set `odpsPPV2Enable` to `true` when you plan data in Deployment Planner. After this feature is enabled, the system can identify and verify the VPC information during an authentication process, and record the corresponding VPC ID in ACL blocking logs to facilitate security audit and troubleshooting. To check whether the `odpsPPV2Enable` feature is enabled, perform the following steps: i. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane, choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter `odps` in the **Product | Cluster** search box to search for MaxCompute clusters. ii. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column to go to the cluster details page. iii. On the **Desired State Configuration** tab, find the `kv.conf` and `tag.conf` files. iv. Click **Show Content** on the right side to check whether the values of the `odpsPPV2Enable` parameters in the two files are `true` . If the `odpsPPV2Enable` parameters are not specified in the configuration or the corresponding values of the parameters are `false` , contact MaxCompute O&M engineers to adjust the configuration.

### odpscmd commands

**Log in to the CLI**

You can use the CLI to perform O&M operations. Before you run commands at the CLI, you must log in to the CLI by performing the following steps:
1. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps into the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter `odps-service-computer` into the **Service** search box.
3. Click the name of the service in the **Service** column to go to the **Service odps-service-**
**computer** page.
4. Select **ComputerInit#**.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of the instance to open the
TerminalService page. All subsequent commands are executed on this page.

**Console command directories and configurations**

The MaxCompute client is stored in the clt folder in the /apsara/odps_tools directory of MaxCompute AG. The client configuration file is stored in the conf directory in the clt folder. By default, the access_id, access_key, end_point, log_view, and tunnel_point parameters are

| _ _ d. After you run the | _ _ cd /apsara/odps tools/ _ |   |
|---|---|---|
| ./clt/bin/odpscmd |   |   |
|   |   | command to enter the in |

you can view the MaxCompute version. For example, you can run the `HTTP GET` /projects/admin_task_project/system; command to view the version of MaxCompute.

**Client command parameters**

The following figure shows the client command parameters.
**-e**: The client does not execute SQL statements in interactive mode.
**--project, -u, and -p** : The client preferentially uses the specified user, pass, and project
settings instead of those in the conf file. For parameters that are not specified, the corresponding settings in the conf file are used.
**-k and -f** : The client directly executes local SQL files.
**--instance-priority**: Specify the priority of the task. Valid values: 0 to 9. A smaller value
indicates a higher priority. Default value: 9.
**-r**: Specify the maximum number of times that a failed command can be retried. This
parameter is commonly used in script jobs.

**Commonly used SQL commands for O&M**

The following table describes the commonly used commands. Table 1: Commonly used commands

| Command | Description |
|---|---|
| whoami | Queries your Apsara Stack tenant account and endpoint information. |
| show p | Queries the information about all instances that have been run. |
| wait <instanceid> | Displays the LogView and Fuxi job information of a task. To run this command, you must acquire permissions from the owner, and the LogView and Fuxi job information must be stored in the same project. |
| kill <instanceid> | Terminates an instance. |
| tunnel upload/download | Tests whether the tunnel is available. This parameter is used for troubleshooting. |
| desc project <projectname> - extended | Queries the information about a project. desc extended table: queries the information about tables. desc table name partition(pt spec): queries the information about _ _ partitions. desc resource $resource name: queries the information about project _ resources. desc project $project name -extended: queries the information _ about clusters. |
| export <project name> < local file path> _ _ | Exports the DDL statements of all tables in a project. |
| create table <tablename> (...) | Creates a table. |
| select count(*) from <tablename> | Queries a table. |
| Explain | Creates plans without submitting Fuxi jobs. You can run this command to view resources requested by tasks. |
| list | Queries the information about tables, resources, and roles. |

| show | Queries the information about tables and partitions. |
|---|---|
| purge | Migrates all data from the recycle bin of MaxCompute to the recycle bin of Apsara Distributed File System. purge table <tablename>: clears data in a table. purge all: clears data in all tables of the current project. |

### Tunnel commands

You can use Tunnel commands provided by the MaxCompute client to implement the original features of the Dship tool. Tunnel commands are typically used to upload or download data. Table 1 Tunnel commands

| Command | Description |
|---|---|
| tunnel upload | Allows you to upload data to a MaxCompute table. You can upload files or level-1 directories. You can upload data to only one table or only one partition in a table each time. For a partitioned table, you must specify the partition to which you want to upload data. For a multi-level partitioned table, you must specify the lowest-level partition. |
| tunnel download | Allows you to download data from a MaxCompute table. You can download data only to a single file. You can download data from only one table or partition to a single local file each time. For a partitioned table, you must specify the partition from which you want to download data. For a multi-level partitioned table, you must specify the lowest- level partition. |
| tunnel resume | Allows you to resume uploads. If an error occurs due to network interruptions or Tunnel service faults, you can resume file or directory transmission. You can use this command to resume only uploads. Each upload or download operation is considered a session. To resume a session, you must specify the session ID in the Resume command. |
| tunnel show | Displays historical records. |
| tunnel purge | Clears the session directory. Sessions within the last three days are cleared by default. |

You can run the Help subcommand of Tunnel on the client to obtain the help information. This section describes how to use the subcommand for each command.

**Upload**

Uploads data of a local file to a MaxCompute table. The following example shows how to use the sub-commands:

```
odps@ project_name>tunnel help upload; usage: tunnel upload [options] <path> <[project.]table[/partition]>
              upload data from local file
 -acp,-auto-create-partition <ARG>   auto create target partition if not
                                     exists, default false
 -bs,-block-size <ARG>               block size in MiB, default 100
 -c,-charset <ARG>                   specify file charset, default ignore.
                                     set ignore to download raw data
 -cf,-csv-format <ARG>               use csv format (true|false), default
                                     false. When uploading in csv format,
                                     file splitting not supported.
 -cp,-compress <ARG>                 compress, default true
 -dbr,-discard-bad-records <ARG>     specify discard bad records
                                     action(true|false), default false
 -dfp,-date-format-pattern <ARG>     specify date format pattern, default
                                     yyyy-MM-dd HH:mm:ss
 -fd,-field-delimiter <ARG>          specify field delimiter, support
                                     unicode, eg \u0001. default ","
 -h,-header <ARG>                    if local file should have table
                                     header, default false
 -mbr,-max-bad-records <ARG>         max bad records, default 1000
 -ni,-null-indicator <ARG>           specify null indicator string,
                                     default ""(empty string)
 -ow,-overwrite <true | false>       overwrite specified table or
                                     partition, default: false
 -rd,-record-delimiter <ARG>         specify record delimiter, support
                                     unicode, eg \u0001. default "\n"
 -s,-scan <ARG>                      specify scan file
                                     action(true|false|only), default true
 -sd,-session-dir <ARG>              set session dir, default
                                     /apsara/odps/odps/odps_tools/clt/plug
                                     ins/dship
 -ss,-strict-schema <ARG>            specify strict schema mode. If false,
                                     extra data will be abandoned and
                                     insufficient field will be filled
                                     with null. Default true
 -t,-threads <ARG>                   number of threads, default 1
 -te,-tunnel_endpoint <ARG>          tunnel endpoint
 -time,-time <ARG>                   keep track of upload/download elapsed
                                     time or not. Default false
 -tz,-time-zone <ARG>                time zone, default local timezone:
                                     Asia/Shanghai
Example:
    tunnel upload log.txt test_project.test_table/p1="b1",p2="b2"
```

**Parameters**:
-acp: the partition to which you want to upload data. If the specified partition does not exist, a partition is automatically created. By default, partitions are not created. -bs: the size of the data block uploaded by Tunnel each time. Default value: 100 MiB (1 MiB = 1,024 × 1,024 bytes). -c: the encoding format of the data file. Default value: UTF-8. By default, if this parameter is not configured, raw data is downloaded. -cf: specifies whether the file is a CSV file. Default value: False. -cp: specifies whether to compress the local data file before you upload the file to MaxCompute. This helps reduce data usage. By default, the local data file is compressed. -dbr: specifies whether to ignore dirty data, such as additional columns, missing columns, or unmatched types of column data. If you set this parameter to true, all data that fails to match the definition of the table is ignored. If you set this parameter to false, an error is returned after dirty data is detected. This ensures that raw data in the table to which you want to upload data is not contaminated. -dfp: the format of DATETIME data. Default value: yyyy-MM-dd HH:mm:ss. -fd: the column delimiter used in the local data file. By default, commas (,) are used as the column delimiter. -h: specifies whether the data file that you want to upload has a table header. If this parameter is set to true, the data file can contain a table header. In this case, Dship skips the table header and uploads data from the second row. -mbr: specifies the maximum number of dirty data records allowed. If the number of dirty data records exceeds 1,000, the upload stops. Default value: 1000. -ni: the NULL data identifier. Default value: an empty string (""). -ow: specifies whether the uploaded data overwrites the table or partition. Default value: False. This value indicates that data is uploaded in append mode. -rd: the row delimiter used in the local data file. Default value: \r\n. -s: specifies whether to scan the local data file. Default value: false. true: The system scans the data and starts to upload the data only if the data is in the valid format. false: The system does not scan the data before the system uploads the data. only: The system only scans the data but does not upload the data. -sd: the session directory. -ss: specifies the strict schema mode. Default value: True. If you set this parameter to False, extra data is discarded, and the fields that are not specified are filled with NULL. -t: specifies the number of threads. Default value: 1. -te: the Tunnel endpoint. -time: specifies whether the upload time is tracked. Default value: False. -threads: the number of threads. Default value: 1. -tz: the time zone. Default value: local time zone, such as Asia/Shanghai.

**Show**

Displays historical records. The following example shows how to use the sub-commands:

```
odps@ project_name>tunnel help show; usage: tunnel show history [options]
              show session information
 -n,-number <ARG>   lines
Example:
    tunnel show history -n 5
    tunnel show log
```

**Parameters**:
-n: the number of rows that you want to display.

**Resume**

Resumes historical operations. Only uploads can be resumed. The following example shows how to use the sub-commands:

```
odps@ project_name>tunnel help resume; usage: tunnel resume [session_id] [-force]
              resume an upload session
 -f,-force   force resume
Example:
    tunnel resume
```

**Parameters**:
-f: specifies whether to forcefully resume historical operations. This parameter is omitted by default.

**Download**

The following example shows how to use the sub-commands:

```
odps@ project_name>tunnel help download; usage: tunnel download [options] <[project.]table[/partition]> <path>
              download data to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
 -cf,-csv-format <ARG>             use csv format (true|false), default
                                   false. When uploading in csv format,
                                   file splitting not supported.
 -ci,-columns-index <ARG>          specify the columns index(starts from
                                   0) to download, use comma to split each
                                   index
 -cn,-columns-name <ARG>           specify the columns name to download,
                                   use comma to split each name
 -cp,-compress <ARG>               compress, default true
 -dfp,-date-format-pattern <ARG>   specify date format pattern, default
                                   yyyy-MM-dd HH:mm:ss
 -e,-exponential <ARG>             When download double values, use
                                   exponential express if necessary.
                                   Otherwise at most 20 digits will be
                                   reserved. Default false
 -fd,-field-delimiter <ARG>        specify field delimiter, support
                                   unicode, eg \u0001. default ","
```

```
 -h,-header <ARG>                  if local file should have table header,
                                   default false
    -limit <ARG>                   specify the number of records to
                                   download
 -ni,-null-indicator <ARG>         specify null indicator string, default
                                   ""(empty string)
 -rd,-record-delimiter <ARG>       specify record delimiter, support
                                   unicode, eg \u0001. default "\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   /apsara/odps/odps/odps_tools/clt/plugin
                                   s/dship
 -t,-threads <ARG>                 number of threads, default 1
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
 -time,-time <ARG>                 keep track of upload/download elapsed
                                   time or not. Default false
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Chongqing
usage: tunnel download [options] instance://<[project/]instance_id> <path>
              download instance result to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
 -cf,-csv-format <ARG>             use csv format (true|false), default
                                   false. When uploading in csv format,
                                   file splitting not supported.
 -ci,-columns-index <ARG>          specify the columns index(starts from
                                   0) to download, use comma to split each
                                   index
 -cn,-columns-name <ARG>           specify the columns name to download,
                                   use comma to split each name
 -cp,-compress <ARG>               compress, default true
 -dfp,-date-format-pattern <ARG>   specify date format pattern, default
                                   yyyy-MM-dd HH:mm:ss
 -e,-exponential <ARG>             When download double values, use
                                   exponential express if necessary.
                                   Otherwise at most 20 digits will be
                                   reserved. Default false
 -fd,-field-delimiter <ARG>        specify field delimiter, support
                                   unicode, eg \u0001. default ","
 -h,-header <ARG>                  if local file should have table header,
                                   default false
    -limit <ARG>                   specify the number of records to
                                   download
 -ni,-null-indicator <ARG>         specify null indicator string, default
                                   ""(empty string)
 -rd,-record-delimiter <ARG>       specify record delimiter, support
                                   unicode, eg \u0001. default "\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   /apsara/odps/odps/odps_tools/clt/plugin
                                   s/dship
 -t,-threads <ARG>                 number of threads, default 1
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
 -time,-time <ARG>                 keep track of upload/download elapsed
                                   time or not. Default false
```

```
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Shanghai
Example:
    tunnel download test_project.test_table/p1="b1",p2="b2" log.txt
    tunnel download instance://test_project/test_instance log.txt
```

**Parameters**:
-c: the encoding format of the data file. Default value: UTF-8. -cf: specifies whether the file is a CSV file. Default value: False. Only TXT and CSV files can be downloaded. TXT files are downloaded by default. -ci: the indexes of the columns from which you want to download data. The column indexes start from 0. Separate column indexes with commas (,). -cn: the names of the columns from which you want to download data. Separate column names with commas (,). -cp and -compress: specifies whether to compress the local file before you download the file. This helps reduce data usage. By default, the local file is compressed. -dfp: the format of DATETIME data. Default value: yyyy-MM-dd HH:mm:ss. -e: specifies whether to represent data of the DOUBLE type that you want to download by using an exponential function. If the data is not represented by an exponential function, retain a maximum of 20 digits. -fd: the column delimiter used in the local data file. By default, commas (,) are used as the column delimiter. -h: specifies whether the data file has a table header. If you set this parameter to true, the data file has a table header. In this case, Dship skips the table header and uploads data from the second row. `-h=true` and `threads>1` cannot be used together. -limit: the number of rows that you want to download. -ni: specifies the NULL data identifier. Default value: `""` (empty string). -rd: the row delimiter used in the local data file. Default value: \r\n. -sd: the session directory. -t: specifies the number of threads. Default value: 1. -te: the Tunnel endpoint. -time: specifies whether the download time is tracked. Default value: False. -threads: the number of threads. Default value: 1. -tz: the time zone. Default value: local time zone, such as Asia/Shanghai.

**Purge**

Clears the session directory. Sessions within the last three days are cleared by default. The following example shows how to use the sub-commands:

```
odps@ project_name>tunnel help purge; usage: tunnel purge [n]
              force session history to be purged.([n] days before, default
              3 days)
Example:
    tunnel purge 5
```

### LogView tool

#### Prerequisites

Before using the LogView tool, check the LogView process status. If the process is shut down, start the process.

**Open the command execution window**

1. Log on to the Apsara Infrastructure Management platform. Go to **Resource Management**
**> Product and Cluster O&M**. In the **Product | Cluster** search box, enter odps to find the
relevant clusters.
2. Click **Cluster Details** in the **Actions** column of the target cluster. On the **Service List** tab,
use the **Service** search box to find the `odps-service-console` service.
3. Click the **Service** name to open the **Service: odps-service-console** page.
4. Click **LogView#**.
5. On the **Instance List** tab, click **Terminal** in the **Actions** column for the target machine to
open the TerminalService window. All subsequent command line operations are performed in this window.

**Example process management commands**

Use the following commands to check the process status and start the process.
1. Run the following command to find the LogView Docker container.

```bash
docker ps|grep logview;
```

2. Run the following commands to check the LogView process status.

```
ps -aux|grep logview; netstat -ntulp|grep 9000;
```

3. If the process is shut down, run the following command to start the process.

```
/opt/aliyun/app/logview/bin/control start;
```

#### Overview

LogView allows you to check and debug the tasks of a MaxCompute job after the job is submitted. You can use LogView to check the details of a job.

**Features**

LogView allows you to check the status, details, and results of a job, and the progress of each phase.

**Log in to LogView**

After you submit an SQL task on a client, a long string that starts with `http://logview.odps.aliyun.com/logview` is returned. In this example, a client named odpscmd is used. Figure 1: Returned long string After you remove the carriage return and line feed characters in the long string, you can view the monitoring data of LogView through a web browser.

#### What is LogView?

For complex SQL queries, you must have an in-depth knowledge of the relationships between MaxCompute tasks and Fuxi instances before you can understand LogView. In short, a MaxCompute task consists of one or more Fuxi jobs. Each Fuxi job consists of one or more Fuxi tasks. Each Fuxi task consists of one or more Fuxi instances. Figure 1: Relationships between MaxCompute tasks and Fuxi instances

**MaxCompute Task**

**Fuxi Task**

**Fuxi Task**

**Fuxi Task**

**...**

**Fuxi Instance**

**Fuxi Instance**

**Fuxi Instance**

**...**

The following figures show the relevant information in LogView.

**MaxCompute Instance**

Figure 2: MaxCompute instance

**MaxCompute Task**

Figure 3. MaxCompute task

**Task Detail-Fuxi Job**

Figure 4. Task Detail - Fuxi job (1) Figure 5. Task Detail - Fuxi job (2)

**Task Detail-Summary**

Figure 6. Task Detail - Summary

**Task Detail-JSONSummary**

Figure 7. Task Detail - JSON summary

#### Work with LogView

This topic describes how to work with LogView.

**Background information**

LogView allows you to view each point in time throughout the lifecycle of a job, time consumed by Job Scheduler to schedule an instance, polling interval, UDF and MR debugging information, and task status (Terminated). You can also check for data skews. For more information about how to log in to LogView, see Before you start.

**View each point in time throughout the lifecycle of a job**

Figure 1: View each point in time throughout the lifecycle of a job In Fuxi Jobs, the **Start Time** field indicates the start time of a Fuxi task. In the Fuxi Instance of Fuxi Task, the **Start Time** field indicates the start time of the Fuxi instance.

**View the time consumed by Job Scheduler to schedule an**

**instance**

Figure 2: View the amount of time consumed by Job Scheduler to schedule a task The following formula is used to calculate the amount of time consumed by Job Scheduler to schedule a task: Fuxi instance start time - Fuxi task start time = Amount of time consumed to schedule the task. In this example, it takes about 2 seconds to schedule a Fuxi instance in the M1 task.

**View the polling interval**

Sample commands:

```
SELECT * FROM skew a JOIN small b ON a.key=b.key;
```

After a MaxCompute job is submitted, odpscmd polls the status of the job at an interval of approximately 5 seconds. You can obtain the ID and LogView of the instance.

**Check for data skews**

In a Fuxi task, the durations of different instances are similar. You can click the icon in the StdOut column of a Fuxi instance to view the volume of data processed on the instance. If the volume significant differs from that on other instances, data skews exist.

**View UDF and MR debugging information**

You can click the icons in the StdOut and StdErr columns of a Fuxi instance to view UDF and MR debugging information.

**View task status (Terminated)**

If an error occurs during task execution, you can view the error message on the **Result** tab of LogView. You can also locate the cause of the error on the Job Details tab.

**Locate LogView based on the instance ID**

After a job is submitted, you can press Ctrl+C to return to odpscmd and perform other operations. For example, you can run the wait <instanceid>; command to locate LogView and obtain the job status.

**Locate running tasks**

After you close the control window, you can run the show p; command to locate the tasks that are running and the historical tasks.

### Apsara Big Data Manager

Apsara Big Data Manager (ABM) allows you to manage and maintain big data services in terms of businesses, services, clusters, and hosts. You can also update big data services, customize alert configurations, and view the O&M history in the ABM console. For more information about how to log in to the ABM console and perform MaxComputerelated O&M operations, see Log in to the ABM console and O&M using Apsara Bigdata Manager.

## Routine O&M

### Manage service configurations

MaxCompute configurations are stored in the /apsara/odps_service/deploy/env.cfg directory in MaxCompute AG. The configuration file contains the following content:

```
odps_worker_num=3 executor_worker_num=3 hiveserver_worker_num=3 replication_server_num=3 messager_partition_num=3
```

You can modify the values of these parameters based on your business requirements and start the corresponding MaxCompute services based on the configured values. For more information, see Restart MaxCompute services. If you add `xstream_max_worker_num=3` at the end of the configuration file, three workers are launched when you start XStream.

### Routine inspections

1. Check whether all machines are in desired state in the Apsara Infrastructure Management
console. i. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane, choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps into the **Product | Cluster** search box to search for MaxCompute clusters. ii. Confirm whether all machines have reached the desired state by checking the information in the **Status** and **Instance Status** columns. iii. Find the cluster that you want to manage and click **Service** and **Component** in the
**Instance Status** column to view the detailed information about exceptions. You can also
click **Cluster Details** in the **Actions** column to view the details of the cluster.
2. Go to the TerminalService page
i. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. On the **Services** tab of the details page, enter `odps-service-computer` into the
**Service** search box.
ii. Click the name of the service in the **Service** column to go to the **Service odps-service-**
**computer** page.
iii. Select **ComputerInit#**. iv. On the **Instances** tab, click **Terminal** in the **Actions** column of the instance to open the TerminalService page. All subsequent commands are executed on this page.
3. Go to the /home/admin/odps/odps_tools/clt/bin/odpscmd -e directory and run the following
command:

```
select count(*) from datahub_smoke_test;
```

The `Fuxi job` runs as expected.
4. Run the following commands to check whether the following workers exist and whether the
workers have been recently restarted:

```
i. r swl Odps/MessagerServicex; ii. r swl Odps/OdpsServicex; iii. r swl Odps/HiveServerx; iv. r swl Odps/QuotaServicex; v. r swl Odps/ReplicationServicex;
```

5. Run the following command to check whether an error exists:

```
puadmin lscs |grep -vi NORMAL|grep -vi DISK_OK;
```

6. Run the following commands to check data integrity:

```
i. puadmin fs -abnchunk -t none; ii. puadmin fs -abnchunk -t onecopy; iii. puadmin fs -abnchunk -t lessmin;
```

7. Log in to the machine on which Apsara Name Service and Distributed Lock Synchronization
System resides.

```
echo srvr | nc localhost 10240 | grep Mode;
```

**Example**:

```
tj_show -r nuwa.NuwaZK#>/tmp/nuwa;pssh -h /tmp/nuwa -i "echo srvr | nc localhost 1024 0 | grep Mode";
```

8. Run the following commands to check whether Apsara Distributed File System runs as
expected:

```
puadmin gems; puadmin gss;
```

9. Perform routine inspections in the Apsara Big Data Manager (ABM) console to check disk
usage.

### Shut down a chunk server for

**maintenance and clone the chunk**

**server**

This topic describes how to shut down a chunk server for maintenance and clone the chunk server if a hardware fault occurs.

**Background information**

If you shut down a chunk server for maintenance and clone the chunk server, the resources of the chunk server in the cluster become unavailable within the maintenance period. However, MaxCompute services are not affected.

**Prerequisites**

All MaxCompute services are in desired state and run as expected. All services on the OPS1 server are in desired state and run as expected. Disk space is sufficient. Data migration is triggered when a node is undeployed. If the primary node resides on the machine that you want to undeploy, make sure that services are switched from the primary node to the secondary node.

**Go to the CLI page**

1. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product and Cluster O&M**. On the Product & Cluster O&M page, enter `odps` in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter odps-service-computer into the **Service** search box and click the name of the service that is displayed.
3. Click the name of the service in the **Service** column to go to the **Service odps-service-**
**computer** page.
4. Select **ComputerInit#**.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of the instance to open the
TerminalService page. All subsequent commands are executed on this page.

**Run commands**

1. Run the following commands to check the data integrity of Apsara Distributed File System:

```
puadmin abnchunk fs -t none; -- Check whether files are lost. If no output is generated, files are complete. puadmin abnchunk fs -t onecopy; -- Check whether each file has only one copy. If no output is generated, each file ha s only one copy. puadmin abnchunk fs -t lessmin; -- Check whether the number of files is smaller than the minimum number of backups. I f no output is generated, the number of files is smaller than the minimum number of b ackups.
```

2. Add the machine that you want to shut down to the blacklist of Job Scheduler.
i. Run the following command to enable the blacklist feature of Job Scheduler. Skip this step if this feature is already enabled.

```
/apsara/deploy/rpc_caller --Server=nuwa://localcluster/sys/fuxi/master/ForClient -- Method=/fuxi/SetGlobalFlag --Parameter={\"fuxi_Enable_BadNodeManager\":false};
```

ii. Run the following command to check the existing hostnames in the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

iii. Run the following command to add the machine that you want to shut down to the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster add $hostname;
```

iv. Run the following command to check whether the machine that you want to shut down is added to the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

3. Shut down the machine for maintenance. After the maintenance is completed, restart the
machine. Do not compromise the system during the maintenance.
4. Run the following commands to remove the machine from the blacklist of Job Scheduler:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster remove $hostname; /apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

5. Set rma=pending for the faulty machine.
i. Log in to the OPS1 server and run the following command. Set the action_name parameter to `rma` and the action_status parameter to `pending` . Then, set the hostname parameter to the name of the faulty machine. In this example, the hostname parameter is set to m1.

**Run the following command:**

```bash
curl "http://127.0.0.1:7070/api/v5/SetMachineAction?hostname=m1" -d '{"action_nam e":"rma", "action_status":"pending"}';
```

**Return results**:
`{`

```json
    "err_code": 0,
    "err_msg": "",
    "data": [
```

`{`

```json
            "hostname": "m1"
```

`}` `]` `}` ii. Configure audit logs. Sample command:

```bash
curl "http://127.0.0.1:7070/api/v5/AddAuditLog?object=/m/m1&category=action" -d '{" category":"action", "from":"tianji.HealingService#", "object":"/m/m1", "content": " {\n \"action\" : \"/action/rma\",\n \"description\" : \"/monitor/rma=error, mtime: 1513488046851649\",\n \"status\" : \"pending\"\n}\n" }';
```

In this example, the `mtime` parameter is set to `1513488046851649` to specify the maintenance time window of the faulty machine. Set the mtime parameter to the current system time when you configure audit logs. Run the following command to query the current system time:

**Run the following command:**

```bash
curl "http://127.0.0.1:7070/api/v5/GetMachineInfo? hostname=m1&attr=action_name,action_status,action_description@mtime";
```

**Return results**:
`{`

```json
    "err_code": 0,
    "err_msg": "",
    "data": {
        "action_description": "",
        "action_description@mtime": 1516168642565661,
        "action_name": "rma",
        "action_name@mtime": 1516777552688111,
        "action_status": "pending",
        "action_status@mtime": 1516777552688111,
        "hostname": "m1",
        "hostname@mtime": 1516120875605211
```

`}` `}`
6. Wait for approval.
i. Wait until the status of the rma action becomes approved or doing on the machine. a. **Run the following command:**

```bash
curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=m1";
```

b. **Return results**: A large amount of information is returned. Search for the `action_status` parameter in the returned results.

| machine. A value of | pending |
|---|---|
| approved, doing, or done |   |

ii. Check the approval status of the request on the machine. A value of `pending` indicates that the request is being processed. A value of `approved, doing, or done` indicates that the request is approved. If no value is returned, the request is not approved.

**Run the following command:**

```bash
curl http://127.0.0.1:7070/api/v5/GetMachineInfoPackage? hostname=m1&attr=sr.id,sr.action_name,sr.action_status;
```

**Return results**:
A large amount of information is returned. Search for the items in the `doing` state.
7. Shut down the machine when the status of the rma action becomes `approved or doing` .
After the maintenance is complete, restart the machine. If you want to clone the machine after the maintenance is complete, proceed to the next step. Otherwise, skip the next step.
8. Clone the machine.
i. After the maintenance is complete, run the following command to clone the machine on the OPS1 server:

**Run the following command:**

```bash
curl "http://127.0.0.1:7070/api/v5/SetMachineAction? hostname=m1&action_name=rma&action_status=doing" -d '{"action_name":"clone", "actio n_status":"approved", "action_description":"", "force":true}';
```

**Return results**:
`{`

```json
"err_code": 0, "err_msg": "", "data": [
```

`{`

```json
"hostname": "m1"
```

`}` `]` `}` ii. Access the clone container. Check the clone status and confirm whether the clone task is in progress. a. Query the clone container.

**Run the following command:**

```bash
docker ps|grep clone;
```

**Return results**:

```
18c1339340ab reg.docker.god7.cn/tianji/ops_service:1f147fec4883e082646715cb79c3710f7b2ae9c6e68 fa9a9452b92b4b3366a ops.OpsClone__.clone.1514969139
```

b. Log in to the container.

**Run the following command:**

```bash
docker ps|grep clone;
```

c. Query the clone task.

**Run the following command:**

```
/home/tops/bin/python /root/opsbuild/bin/opsbuild.py acli list --status=ALL -n 10 000 | vim -
```

9. Run the following command to restore the status of the machine:

**Run the following command:**

```json
curl "http://127.0.0.1:7070/api/v5/SetMachineAction?hostname=m1&action_name=rma" -d ' {"action_name":"rma","action_status":"done", "force":true}';
```

0. Check the status of the machine by running the corresponding command or using the
Apsara Infrastructure Management console. If the machine is in the GOOD state, the maintenance is complete.

**Run the following command:**

```bash
curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=m1&attr=state,hostname";
```

1. Check whether the cluster is in desired state. Make sure that all services on the machine
that you deploy are in desired state.

### Shut down a chunk server for

**maintenance without**

**compromising the system**

**Prerequisites**

All MaxCompute services are in desired state and run as expected.

**Go to the TerminalService page**

1. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product and Cluster O&M**. On the Product & Cluster O&M page, enter `odps` in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter odps-service-computer into the **Service** search box and click the name of the service that is displayed.
3. Click the name of the service in the **Service** column to go to the **Service odps-service-**
**computer** page.
4. Select **ComputerInit#** in the Components list.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of the desired instance to
open the TerminalService page. All subsequent commands are executed on this page.

**Run commands**

1. Run the following commands to check the data integrity of Apsara Distributed File System:

```
puadmin abnchunk fs -t none; -- Check whether files are lost. If no output is generated, the files are complete. puadmin abnchunk fs -t onecopy; -- Check whether each file has only one copy. If no output is generated, each file ha s only one copy. puadmin abnchunk fs -t lessmin; -- Check whether the number of files is smaller than the minimum number of backups. I f no output is generated, the number of files is smaller than the minimum number of b ackups.
```

2. Add the machine that you want to shut down to the blacklist of Job Scheduler.
i. Run the following command to enable the blacklist feature of Job Scheduler. Skip this step if this feature is already enabled.

```
/apsara/deploy/rpc_caller --Server=nuwa://localcluster/sys/fuxi/master/ForClient -- Method=/fuxi/SetGlobalFlag --Parameter={\"fuxi_Enable_BadNodeManager\":false};
```

ii. Run the following command to check the existing hostnames in the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

iii. Run the following command to add the machine that you want to shut down to the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster add $hostname;
```

iv. Run the following command to check whether the machine that you want to shut down is added to the blacklist:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

3. Shut down the machine for maintenance. After the maintenance is completed, restart the
machine. Do not compromise the system during the maintenance.
4. Run the following commands to remove the machine from the blacklist of Job Scheduler:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster remove $hostname; /apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

**Expected result**

During the shutdown of the chunk server, Apsara Distributed File System attempts to read data consistently, and `SQL` tasks remain in the `running` state. The tasks are completed after 7 to 8 minutes or after the machine recovers.

### Adjust the virtual resources of

**Apsara Distributed Operating**

**System in MaxCompute**

**Prerequisites**

All MaxCompute services are in the desired state and run as expected.

**Procedure**

1. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter `odps` in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Desired State Configuration** tab, enter `role.conf` into the search box to search for the **role.conf** file in the **fuxi** directory.
3. In the right-side editor, modify the machine tags and click **Preview and Submit**.
4. In the **Confirm and Submit** dialog box, enter the change description and click **Submit**.
5. The cluster starts rolling, and the changes start to take effect.
On the **Action History** tab, you can check the task status. If the task status is
**Succeeded**, the changes are in effect.
6. After the changes are applied, run the r ttrl; command on the TerminalService page to
confirm the changes.

### Restart MaxCompute services

**Go to the TerminalService page**

1. Log in to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter `odps` in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter odps-service-computer into the **Service** search box and click the name of the service that is displayed.
3. Click the name of the service in the **Service** column to go to the **Service odps-service-**
**computer** page.
4. Select **ComputerInit#**.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of the instance to open the
TerminalService page. All subsequent commands are executed on this page.

**Run commands**

1. Run the following command to query the number of machines:

```
tj_show -r fuxi.Tubo#;
```

2. Divide the number of machines by 3 to obtain the number of workers.
The number of workers ranges from 1 to 3.
3. Modify the number of workers in the env.cfg file in the `vim /apsara/odps_service/deploy`
directory.

```
odps_worker_num = 2 executor_worker_num = 2 hiveserver_worker_num = 2 replication_server_num = 2 messager_partition_num = 2 -- In this example, the values are for reference only.
```

4. Restart MaxCompute and Hive.

```
/apsara/odps_service/deploy/install_odps.sh restart_hiveservice; -- Restart Hive. /apsara/odps_service/deploy/install_odps.sh restart_odpsservice; -- Restart MaxCompute. r swl Odps/OdpsServicex; r swl Odps/HiveServerx; -- Check the status and update time of the service after you restart the service.
```

5. Restart the message service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeploymessagerservice; -- Restart the message service. r swl Odps/MessagerServicex; -- Check the status and update time of the service after you restart the service.
```

6. Restart the quota service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeployquotaservice; -- Restart the quota service. r swl Odps/QuotaServicex; -- Check the status and update time of the service after you restart the service.
```

7. Restart the replication service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeployreplicationservice; -- Restart the replication service. r swl Odps/ReplicationServicex; -- Check the status and update time of the service after you restart the service.
```

8. Restart the service mode.

```
r plan Odps/CGServiceControllerx >/home/admin/servicemode.json; r sstop Odps/CGServiceControllerx; r start /home/admin/servicemode.json; -- Restart the service mode. r swl Odps/CGServiceControllerx; -- Check the status and update time of the service after you restart the service.
```

## O&M using Apsara Bigdata

**Manager**

### Log in to the ABM console

This topic describes how to log in to the Apsara Big Data Manager (ABM) console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter the username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. After you have read and selected the privacy policy, click **Agree to Privacy Policy and**
**Log In**.
5. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, click
**Product Operation**.
6. Choose **Big Data > Bigdata Manager** to go to the **Instrument cluster** tab of the ABM
console.

### Monitoring

#### Dashboard

The Apsara Bigdata Manager (ABM) dashboard displays key metrics of MaxCompute. It also provides detailed information about alerts MaxCompute. This helps you understand the overall status of MaxCompute. In addition, the dashboard supports automatic data refresh and full-screen mode.

**Go to the dashboard**

1. Log in to the ABM console. By default, the **Instrument cluster** tab appears.
To return to the **Instrument cluster** tab from other pages, click the icon in the upper-left corner and select **ABM**.
2. On the **Instrument cluster** tab, select a region from the **Area** drop-down list in the upper-
left corner to view the key metrics of MaxCompute in the selected region.

**View the key metrics for MaxCompute**

The **Instrument cluster** tab displays the key metrics of **MaxCompute**. To view these metrics, navigate to the **MaxCompute** section on the Instrument cluster tab. The **MaxCompute** section displays the overview of jobs, real-time capacity of the control system, data import traffic, computing resource usage, physical storage usage, and trends of the logical and physical CPU utilization of a MaxCompute cluster.

**Specify a time range to view metrics**

By default, the Instrument cluster tab displays cluster metrics collected within the previous two days. You can specify a time range to view the metrics. In the **Select Time** section of the **Instrument cluster** tab, specify the start time and end time by year, month, and day, and then click **Ok** to view the metrics collected within the specified time range.

**Full-screen mode**

The dashboard supports the full-screen mode. This mode allows you to view the status of big data services. In the upper part of the **Instrument cluster** tab, click the icon to display the **Instrument**
**cluster** tab in full-screen mode.

#### Resource library

The resource library displays the resource usage of MaxCompute. This topic describes how to access the Resource Library tab and view the resource library of MaxCompute.

**Go to the Resource Library tab**

1. Log in to the Apsara Bigdata Manager (ABM) console. By default, the **Instrument cluster**
tab appears. To return to the **Instrument cluster** tab from other pages, click the icon in the upper-left corner and select **ABM**.
2. On the **Instrument cluster** tab, click the **Resource Library** tab.

**View the resource library of MaxCompute**

In the left-side navigation pane of the **Resource Library** tab, click **MaxCompute**. On the page that appears, you can view the resource usage of MaxCompute. The resource library of MaxCompute displays the trends of compute unit (CU) usage and storage usage, records of CU and storage usage, and proportions of idle CUs and storage.

**Supported operations**

You can filter or sort records of CU usage and storage usage based on a column. For more information, see Common operations.

#### Health

In the Apsara Big Data Manager (ABM) console, the Degree of health tab allows you to view the monitoring checkers of each big data service and the alerts of different severity levels. You can view the details of alerts and perform a post-check to confirm whether the alerts are cleared.

**Procedure**

1. Log in to the ABM console.
After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
2. In the top navigation bar, click **Monitoring**.
3. Click the **Degree of health** tab to view the health check information.
The Degree of health tab displays the monitoring checkers, monitoring sources, severity level, and monitoring details. You can filter data based on your business requirements. You can click the icon to the left of a monitoring checker to view information such as the host status and the report time.

#### Reports

In the Apsara Big Data Manager (ABM) console, the Report tab allows you to view the inspection results of each big data service.

**Procedure**

1. Log in to the ABM console.
After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
2. In the top navigation bar, click **Monitoring**.
3. Click the **Report** tab to view the reports.
The Report tab displays the following information about each report: ID, Report Name, Product, Template Name, Instance Type, Created By, and Created At. You can also view the details about each report.

### O&M

#### Business O&M

##### Business O&M features and entry point

This topic describes the business O&M features and how to navigate to the business O&M page.

**Business O&M features**

| Feature | Description |
|---|---|

| Project manageme nt | Project List: displays all projects in a MaxCompute cluster and the project details. You can filter, query, or sort projects. You can also change the default quota group and storage quota of a project. In zone-disaster recovery scenarios, you can configure resource replication parameters and specify whether to enable resource replication for a project. Yuancangpackageauthorization: allows you to authorize members of a project to access the metadata repository of MaxCompute. StorageEncryption: allows you to specify whether to encrypt the data stored in MaxCompute projects. Project disaster recovery: allows you to view the cluster status when zone-disaster recovery is enabled for MaxCompute. You can switch between the primary and secondary clusters. You can also specify whether to run scheduled tasks to synchronize resources between the primary and secondary clusters. |
|---|---|
| Quota group manageme nt | Displays the quota groups of all projects in a MaxCompute cluster. You can create and modify quota groups. You can also view details about quota groups and enable time- sharing management for quota groups. |
| Job manageme nt | Displays all jobs in a MaxCompute cluster. You can filter and query jobs. You can also view the operational logs of a job, terminate ongoing jobs, and collect job logs. |
| Business governanc e | Small File Merge: allows you to create merge tasks for clusters and projects. You can also filter merge tasks and view the historical statistics on merge tasks. Cold File Compression: allows you to create cold file archive tasks for clusters and projects. You can also filter archive tasks and view the historical statistics on archive tasks. Resource Analysis: allows you to analyze cluster resources in terms of tables, projects, tasks, and duration. |

**Go to the business O&M page**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar
and then click the **Business operation and maintenance** tab to perform business O&M operations.

##### Project management

###### Manage projects

The Project List page displays all projects and project details of MaxCompute clusters. You can filter, query, and sort projects. You can also change the quota group of a project. If zonedisaster recovery is enabled, you can configure resource replication parameters and specify whether to enable resource replication for a project.

**Go to the Project List page**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Project Management > Project List**. On the **Project List** page, you can view the
projects in a cluster. The **Project List** page displays the key information about each project, including the project name, cluster, used storage, storage quota, storage usage, number of files, owner, and creation time of each project.

**View project details**

On the **Project List** page, click the name of the project whose details you want to view. On the details page of the project, view information on the **Overview**, **Operation**, **Storage**,
**Calculation**, **Configuration**, **Channel**, **ResourceAnalysis**, **StorageEncryption**, and
**ClusterReplication** tabs.

**Change a quota group**

You can change the default quota group of a project.
1. On the **Project List** page, find the project that you want to manage and click **Actions >**
**Modify a default quota group** in the Actions column to open the **Modify a project**
**default quota group** panel.
2. In this panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Project | The project for which you want to change the quota group. |
| Geography | The region in which the project resides. |
| Cluster | The default cluster to which the project belongs. If the project belongs to multiple clusters, you can select the default cluster from the drop-down list. |
| Quota Group | The quota group to which the project belongs. If you want to change the quota group, select the quota group from the drop-down list. |

3. Click **Run**.

**Change a storage quota**

You can change the storage quota of a project.
1. On the **Project List** page, find the project that you want to manage and click **Actions >**
**Modify storage quotas** in the Actions column to open the **Storage Quota Adjustment**
panel.
2. In this panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Area | The region in which the project resides. |
| Project | The name of the project for which you want to change the storage quota. |
| Cluster | The default cluster to which the project belongs. |
| Target Storage Quota (TB) | The new storage quota. Unit: TB. |
| Reason | The reason for the change. |

3. Click **Run**.

**Configure resource replication**

The resource replication feature can be configured only in zone-disaster recovery scenarios. In other scenarios, you can only view the settings. In zone-disaster recovery scenarios, you can specify whether to enable the resource replication feature for a project in the primary cluster. If the resource replication feature is enabled for a project, you can configure data synchronization rules for the project to regularly synchronize data such as table data to a secondary cluster.
1. On the **Project List** page, find the project that you want to manage and click **Actions >**
**Update replication status** to go to the **View Multi-Cluster Replication configuration**
panel.
2. In this panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Open | Specifies whether to enable the resource replication feature. Valid values: true and false. Default value: false. |
| Configurati on | The data synchronization rules for the project. In most cases, the default settings are used. If you want to modify the settings, contact O&M engineers. |

3. After you modify the code in the **Configuration** editor, click **Compare Versions** to view
the differences between the **earlier version** and the **current version**.
4. Click **Run**.

**Switch the tunnel configuration**

1. On the **Project List** page, select a region and a cluster name from the drop-down lists next
to **Cluster** to filter projects.
2. Select a method for switching the channel configuration.
**Switch the channel configuration for multiple projects at a time** : On the **Project**
**List** page, select multiple projects for which you want to switch the channel configuration
and click **Switch Channel Configuration** below the list. The **Toggle Project Channel**
**Configuration** dialog box appears.
Select one or more projects.
**Switch the channel configuration for a single project** : On the **Project List** page,
click the name of the project that you want to manage. On the page that appears, click
**Channel > Channel Configuration > Switch Channel Configuration**. The **Switch**
**project Channel cluster** panel appears.
3. In this panel, select the desired channel from the **Target Configuration** drop-down list.
4. Click **Run**. The tunnel configuration is switched.

###### View project details

Apsara Big Data Manager (ABM) allows you to view the details of your MaxCompute projects, including the project overview, jobs, storage, computing, configurations, tunnel, and information about resource analysis, storage encryption, and cluster replication.

**Go to the details page of a project**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Project Management > Project List**.
3. On the page that appears, click the name of a project to view its details.

**Overview**

On the **Overview** tab, you can view the following information about the project: Basic information, such as the default compute cluster quota group, creator, creation time, service, and region. Charts that display the trends of CPU and memory usage, guaranteed CPU and memory resources, and maximum CPU and memory resources on a per-minute basis. The trend curves are shown in different colors. Chart that displays the trends of CPU utilization and memory usage on a daily basis. The trend curves are shown in different colors.

**Operation**

On the **Operation** tab, you can view daily job snapshots within the previous week. The details of a job snapshot include the instance, project, quota group, submitter, duration, minimum CPU utilization, maximum CPU utilization, minimum memory usage, maximum memory usage, DataWorks node ID, cluster, status, start time, priority, and type. You can also view the operational logs of a job to troubleshoot errors. You can perform the following operations on the Operation tab: Customize columns or sort job snapshots by column. View the operational logs of jobs within a specific period of time or terminate jobs.

**Storage**

On the **Storage** tab, you can view the following information: **Storage space water level**,
**Physical Storage Used**, **Physical storage quota**, and **Physical Storage Remaining**. You
can also view the chart that displays the trend of storage usage, including the number of files in Apsara Distributed File System, storage size, number of tables, number of partitions, and redundant storage space on a daily basis. The trend curves are shown in different colors. The Storage tab displays only the information about storage resources. To view the information about computing resources, click the **Calculation** tab.

**Calculation**

On the **Calculation** tab, you can view the quota groups of the project and the details of each quota group. To view the details of a quota group, click the quota group name in the **Quota Name** column. For more information about quota groups, see Quota group management. The Calculation tab displays only the information about computing resources. To view the information about storage resources, click the **Storage** tab.

**Configuration**

On the **Configuration** tab, you can configure the Common, Sandbox, SQL, MR, restrictions, and Recycle properties of the project. You can also configure access to the metadata repository. On the **AttributeItem** tab, if you want to modify a configuration item, click the icon to the left of the configuration item category, modify the configuration item, and then click **Submit**. To restore all configuration items to the default settings, click **Reset**. On the **Yuancangpackageauthorization** tab, you can install a package and perform package-based authorization.

**Channel**

On the **Channel** tab, you can view the tunnel configuration and throughput of the project. The Channel Service Throughput (B/min) chart displays the trends of inbound and outbound traffic. The trend curves are shown in different colors.

**ResourceAnalysis**

On the **ResourceAnalysis** tab, you can view the resource usage of the project from different dimensions, including TableDimensions, TaskDimension, Time-consumingdimension, StartupDimension, and EngineDimension.

**StorageEncryption**

On the **Encryption at Rest** tab, you can encrypt data by using the following encryption algorithms: AES-CTR, AES256, RC4, and SM4. For more information, see MaxCompute storage encryption.

**ClusterReplication**

On the **ClusterReplication** tab, you can view the projects for which the cluster replication feature is enabled and the details and status of cluster replication. When you deploy multiple clusters to use MaxCompute, MaxCompute projects may mutually depend on each other, and data is directly exchanged between projects. MaxCompute periodically scans tables or partitions that are directly read by other tables or partitions. If the duration of data reads reaches the specified threshold, MaxCompute adds the tables or partitions to the cluster replication list. For example, Project 1 in Cluster A depends on Table 1 of Project 2 in Cluster B. In this case, Project 1 directly reads data from Table 1. If the duration of data reads reaches the specified threshold, MaxCompute adds Table 1 to the cluster replication list. The **ClusterReplication** tab consists of the **CopyConfiguration** and **CopyDetails** tabs. On the **CopyConfiguration** tab, the configurations of the tables that support cluster replication are displayed. You can view the table name, priority, cluster to which the data is synchronized, and lifecycle. You can also view the progress of cluster replication for a table. On the **CopyDetails** tab, the information about the tables that support cluster replication is displayed. You can view the project name, cluster name, table name, partition, storage size, number of files, and cluster to which the data is synchronized.

###### Encrypt data

You can specify whether to encrypt the data stored in MaxCompute projects.

**Prerequisites**

MaxCompute V3.8.0 or later is deployed. In this case, storage encryption is supported by default. If you deploy MaxCompute of an earlier version and update the version to V3.8.0 or later, storage encryption is not supported by default. To enable storage encryption, complete relevant configurations for your MaxCompute cluster. For more information, consult an O&M administrator.

**Background information**

After storage encryption is enabled for a project, this feature cannot be disabled, and only the data that is newly written to the project is automatically encrypted. To encrypt historical data, you can create rules and configure tasks. Before you encrypt historical data for a project, make sure that you understand the concepts of rules and tasks in Apsara Big Data Manager (ABM). A rule is used to specify the time period of historical data that you want to encrypt in a specific project. After you create a rule, the system obtains the data in the specified time period every day after the data is exported from the metadata warehouse. Only one rule can be retained every day. If multiple rules are created on a single day, only the latest rule takes effect. Each rule takes effect only once. You can create a key rotate task to encrypt the selected historical data.

**Entry for storage encryption**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Project Management > Project List**.
3. Click the name of a project to go to the project details page.
4. On the project details page, click the **StorageEncryption** tab. The **Encryption** tab
appears by default.

**Enable storage encryption**

After storage encryption is enabled, all data that is newly written to the project is automatically encrypted.
1. On the **Encryption** tab, click **Modify** in the Actions column. In the **Configure Encrypted**
**Storage** panel, configure the **Encryption Algorithm**, **region**, and **project** parameters.
The AES-CTR, AES-256, RC4, and SM4 encryption algorithms are supported.
2. Click **Run**.

**Important**

After storage encryption is enabled, the value in the **Whether the storage is**
**encrypted** column is **encrypted**. After storage encryption is enabled for a project, this
feature cannot be disabled.

**Encrypt historical data**

To encrypt historical data or encrypted data, perform the following steps:
1. Configure a rule.
On the **Create Rule** tab, find a time period in the **Create Rule** section and click **OK** in the Actions column. In the Create Rule message, click **Run**. A rule is created and appears in the rule list. The available time periods include **Last Three Months**, **Last Six Months**, **Three Months**
**Ago**, **Six Months Ago**, and **All**.
2. Create a key rotate task.
On the **Configure Task** tab, click **Add a key rotate task** . In the **Edit Key Rotate Task** panel, configure the parameters that are described in the following table and click **Run**.

| Parameter | Description |
|---|---|
| Region | The region in which the project whose data you want to encrypt resides. Select a region from the drop-down list. |
| Project Name | The name of the project whose data you want to encrypt. |
| Start Timestamp | The start time of the task. |
| Ended At | The end time of the task. |

| xCompute | de·O&M using Apsara Bigdata M nage |
|---|---|

| Priority | The priority of the task. A smaller value specifies a higher priority. |
|---|---|
| Enabled | Specifies whether to enable the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of merge tasks for the project. Valid values: Yes: limits the concurrency. Merge tasks cannot be concurrently run. No: does not limit the concurrency. Merge tasks can be concurrently run. |
| Maximum Concurrent Tasks | The maximum number of merge tasks that can be concurrently run for the cluster in which the selected project resides. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |
| Maximum Number of Running Jobs | The maximum number of jobs that can be concurrently run for the cluster in which the selected project resides. This parameter is a global parameter. The jobs refer to all types of jobs in the cluster in which the selected project resides. |
| Merge Parameters | { "odps.merge.cross.paths": "true", "odps.idata.useragent": "odps encrypt key rotate via force mergeTask", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.failure.handling": "any", "odps.merge.maintain.order.flag": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.quickmerge.flag": "true", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.force.rewrite": "true", "odps.merge.restructure.action": "hardlink" } |

3. Optional. View the history of data encryption in the project.
On the **Historical Queries** tab, select a date from the **Date** drop-down list. Then, you can view the information about storage encryption on the specified date.

###### Grant access permissions on the

**metadata warehouse**

You can grant access permissions on the metadata warehouse to projects and project members.

**Prerequisites**

If MaxCompute V3.8.1 or later is deployed, the package of the metadata warehouse is installed by default. In this case, you can directly use Apsara Big Data Manager (ABM) to grant access permissions on the metadata warehouse. If MaxCompute is upgraded to V3.8.1 or later, the package of the metadata warehouse is not installed by default. Before you grant access permissions on the metadata warehouse, you must manually install the package of the metadata warehouse. A project is created in DataWorks. For more information about how to create a workspace, see **Create a workspace** in **DataWorks User Guide**.

**Background information**

To allow a project to access the metadata warehouse, grant the required permissions to the project and install the package to the project in the ABM console. When you install the package, ABM retrieves authentication information, such as the AccessKey pair, of the project from DataWorks. If the project is created in MaxCompute, an error message is returned.

**Go to the authorization page for the metadata warehouse**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Project Management > Project List**.
3. Click the name of a project to go to the project details page.
4. On the project details page, click the **Configuration > Yuancangpackageauthorization**
tab.

**Perform authorization and installation**

1. Click **Authorization** in the Actions column. In the **package authorization** message, click
**Run**. A message appears, indicating that the permissions are granted.
2. Click **Installation** in the Actions column. In the **package installation** message, click **Run**.
A message appears, indicating that the package is installed.
3. After the package is installed, the status of **Authorization** changes to **authorised**.

###### Migrate MaxCompute projects

Apsara Big Data Manager (ABM) allows you to migrate MaxCompute projects across regions from one cluster to another. This helps balance the computing and storage resources of each cluster. The project migration feature is supported only when the clusters are deployed in multiregion mode.

**Create a project migration task**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Project Management > Project Migration**.
3. In the upper part of the **Project Migration** page, select the region where the project
resides.
4. In the upper-right corner of the Migration Mission page, click **Create Mission**. On the
Create Migration Mission page, configure the parameters in the **General**, **Source**, **Target**
**Selection**, and **Cluster for Mission Execution** sections as prompted.
The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Source | Source Cluster | The name of the source cluster. Select a cluster from the drop-down list. |
|   | Quota Group | The quota group of the source cluster. Select a quota group from the drop-down list. |
|   | projectList | The projects that you want to migrate. After you configure the Quota Group parameter, all projects in the quota group are automatically loaded. You can migrate the projects at a time. If specific projects in the quota group do not need to be migrated, you can remove the projects. |
|   | Copy Source Quota Group | Specifies whether the destination cluster uses the same quota group as the source cluster. If you enable this feature, you cannot configure the Target Quota Group parameter. |

| Target Selection |   |   |
|---|---|---|
|   | Change Tunnel Routing Address | Specifies whether to use a new Tunnel route. Tunnel provides highly concurrent upload and download services for offline data. Each project has a default Tunnel route. If you want to use a new Tunnel route after a project is migrated to a new cluster, enable Change Tunnel Routing Address and specify the new Tunnel route. |
|   | PanguVolume Target Server | Specifies whether the destination Apsara Distributed File System volume can be specified. Currently, cross-volume project migration is not supported. Therefore, set this parameter to No. |
| Cluster for Mission Execution | Cluster | Source Cluster: the source cluster pushes the project to the destination cluster. Target Cluster: the destination cluster pulls the project from the source cluster. |

5. Click **Preview** to preview project migration details.
6. After you confirm the configuration, click **Start Planning** in the upper-left corner. Then, a
project migration task is generated and the migration details appear. The task may require a long period of time to be generated. In most cases, a standard project migration task includes five steps: i. **Add Target Cluster**: Add the destination cluster to the cluster list of the project that you want to migrate. ii. **Start to Replicate**: Replicate the project from the source cluster to the destination cluster. iii. **Switch Default Cluster**: Change the default cluster of the project to the destination cluster. After the default cluster is changed, data is written to the destination cluster. iv. **Clear Replication**: Clear the data replication list. During project migration, the migrated project in the source cluster and the corresponding project in the destination cluster synchronize data based on the data replication list. This ensures data consistency between the two projects. Data is continuously synchronized until the data replication list is cleared. v. **Remove Source Cluster**: Delete the migrated project from the source cluster. For more information about how to modify a task after the task is generated, see Modify a project migration task.

**Run the project migration task**

After the project migration task is created, you can run the task on the **Migration Details** page.
1. Click the task name in the task list to go to the **Migration Details** page.
2. On the **Migration Details** page, click **Submit for Execution** to run the task.
After the project migration task starts to run, the system automatically runs the **Add**
**Target Cluster** and **Start to Replicate** steps in sequence.
If you migrate multiple projects at a time, the process requires many steps to complete. Therefore, we recommend that you sort the steps by **project** to view the migration steps for each project. If the **status** of a step is **Success**, the step is completed. If the status of a step is **Failed**, the step fails. During the migration process, specific steps can be run only after you click **OK**. If you do not need to perform a step, click **Skip**. If you want to **confirm** or **skip** multiple steps at a time, select the steps and click **OK** or **Skip** in the upper-left corner of the Migration Details page. You can also click the **status** of a migration step for a project. In the message that appears, click **Yes** to skip the remaining steps.
3. After the **Start to Replicate** step is completed, check the difference in data volumes
between the migrated project in the source cluster and the corresponding project in the destination cluster.

**Important**

We recommend that you run the next step only when the difference in data volumes does not exceed 5%. To check the data volume of a project, log in to the admingateway host in the cluster in which the project resides and run the **pu dirmeta**
**/product/aliyun/odps/${project_name}/** command.
4. If the difference in data volumes does not exceed 5%, perform one of the following
operations: Change the default cluster: Click **OK** in the Actions column of the **Switch Default**
**Cluster** step. After you perform this operation, the destination cluster becomes the
default cluster of the migrated project. In this example, the default cluster is changed. Do not change the default cluster: Click **Skip** in the Actions column of the **Switch**
**Default Cluster** step. After you perform this operation, the source cluster is still used as
the default cluster of the project. After the default cluster is changed, data is written to the destination cluster.

**Warning**

During project migration, the migrated project in the source cluster and the corresponding project in the destination cluster synchronize data based on the data replication list to ensure data consistency. A long period of time is required to complete data synchronization. Therefore, after the default cluster is changed, we recommend that you wait for about one week before you proceed to the next step.
5. Wait for about one week and check whether the data volume of the migrated project in the
source cluster is the same as that of the corresponding project in the destination cluster. To check the data volume of a project, log in to the admingateway host in the cluster in which the project resides and run the **pu dirmeta**
**/product/aliyun/odps/${project_name}/** command.

**Warning**

Before you proceed to the next step, make sure that the data volume of the migrated project in the source cluster is the same as that of the corresponding project in the destination cluster. Otherwise, data may be lost.
6. To retain the migrated project in the source cluster, click **Skip** in the Actions column of the
**Remove Source Cluster** step before you perform the **Clear Replication** step.
7. After the data volume of the migrated project in the source cluster becomes the same as
that of the project in the destination cluster, click **OK** in the Actions column of the **Clear**
**Replication** step to clear the data replication list.
After the data replication list is cleared, data is no longer synchronized between the migrated project in the source cluster and the corresponding project in the destination cluster. The system automatically runs the **Remove Source Cluster** step to delete all migrated projects from the source cluster. This releases storage and computing resources.

**View migration details**

You can view the details of a project migration task, including the steps, results, and debugging information.
1. If multiple migration tasks exist, search for a task or filter tasks on the **Migration Mission**
page. Filter tasks: Select a task state from the **Filter out Mission By** drop-down list. All tasks in this state are automatically filtered out. Search for a task: Enter the name of a migration task in the search box in the upper-right corner and click the search icon to **search for the task**.
2. On the Migration Mission page, click the name of the desired migration task. On the
**Migration Details** page, view the details of the migration task.
3. If a step fails, click the **Details** or **Debugging** icon in the Actions column to view the
details or debugging information of the step. This allows you to identify the cause of the failure.
4. Perform other required operations.
In the upper-right corner of the Migration Mission page, click **Menu**. You can export the step list, change the column width to automatically fit the content, or specify whether to show or hide a column. Right-click a cell in the step list and copy the cell content.

**View step details and debugging information**

If a step fails, you can view the step details and debugging information to identify the cause of the failure. To identify the cause of the failure, perform the following steps:
1. Click **Details** in the Actions column to view the details of the step.
2. Click **Debugging** in the Actions column to view the debugging information of the step.

**Modify a project migration task**

After a project migration task is created, you can modify the task if the task does not meet your requirements. To modify the task, find the required task, and click **Modify Mission** in the Actions column. You can also click **Replan** on the **Migration Details** page.

##### Quota group management

Apsara Big Data Manager (ABM) displays the quota groups of all projects in a MaxCompute cluster. You can create and modify quota groups. You can also view the details about quota groups and enable time-sharing management for quota groups.

**Go to the quota group list**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. After you navigate to the **Business operation and maintenance** tab, choose **Quota**
**Group Management > Quota Group List** in the left-side navigation pane to go to the
**Quota Group List** page.

**Create a quota group**

1. On the **Quota Group List** page, click **Add Quota Group** in the upper-right corner. In the
**Add Quota Group** panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Cluster | The cluster to which the quota group belongs. |
| Quota Group | The name of the quota group. |
| CU guarantee | The minimum number of compute units (CUs) provided by the quota group. |
| CU upper limit | The maximum number of CUs provided by the quota group. |
| cpu memory ratio | The ratio of CPU cores to memory of the machines in the cluster to which the quota group belongs. |
| Scheduling Type | The resource scheduling type. Valid values: First In First Out (default) and Equally Divided. |
| Preemption strategy | The preemption policy of the quota group. Valid values: No preemption (default) and Preemption. |

2. Click **Run** to create the quota group.

**Modify a quota group**

1. On the **Quota Group List** page, click **Modification** in the **Actions** column of a quota
group. In the **Modifying a Quota Group** panel, modify the parameters. If time-sharing management is already enabled for the quota group that you want to modify, you need to adjust the time-sharing management configuration first.
2. Click **Run** to apply the modifications.

**View the details about a quota group**

On the **Quota Group List** page, click **Details** in the **Actions** column of a quota group to view its details, including resource consumption, resource analysis, and time-sharing management.

**Enable time-sharing management for a quota group**

**Configure time-sharing management**

1. In the left-side navigation pane, choose **Quota Group Management > Quota**
**component time** to go to the **Quota component time** page.
2. Click **time sharing management** in the **Actions** column of a quota group to go to the
**Time-Sharingmanagement** tab.
3. Click **Set timesharing**. In the **Set timesharing** panel, specify **Time period** and click **OK**
to add a time period, and then click **Use TimeSet**. You can click **New** to add a time period and click **Delete** to delete a time period. For a quota group that has time-sharing management enabled, you can click
**Edit** in the **Actions** column to modify the time-sharing management settings. In
the **Modify Timesharing Configuration** panel, modify the time-sharing management parameters.
4. To disable time-sharing management for a quota group, click **Set timesharing** again. In
the panel that appears, click **Close TimeSet**.

**View time-sharing management details**

1. In the left-side navigation pane, choose **Quota Group Management > Quota**
**component time** to go to the **Quota component time** page.
2. Click **Details** in the **Actions** column of the desired quota group to view the following
information: resource consumption, resource analysis, and time-sharing management.

##### Job management

###### Manage job snapshots

The job snapshot feature allows you to manage the tasks that are created in MaxCompute and the merge tasks that are created in Apsara Big Data Manager (ABM). You can also view the LogView information of jobs, terminate jobs, and collect job logs.

**Manage job snapshots**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Job Management > Job Snapshot** to go to the **Job Snapshot** page.

**View job snapshots**

You can perform the following operations: View the details of a job snapshot generated at a specific point in time of a day. The details include the instance, project, quota group, submitter, duration, minimum CPU utilization, maximum CPU utilization, minimum memory usage, maximum memory usage, DataWorks node ID, status, start time, priority, and type. View the details of job snapshots generated within a specific time period. The details include the instance, project, quota group, average CPU utilization, peak CPU utilization, average memory usage, peak memory usage, number of collections, earliest collection time, latest collection time, start time, priority, and type. You can also view the operational logs of a job to identify errors.
1. Search for job snapshots.
On the **JobSnapshot** tab, click the date and time in the upper-right corner to filter job snapshots by day. Click the **All**, **Running**, **Waiting for Resources**, or **Initializing** tab to view job snapshots in the corresponding state. On the **JobSnapshot(TimeRange)** tab, click the date and time in the upper-right corner to query job snapshots within the specified time period.
2. Find the desired snapshot and click **Logview** in the **Operation** column. In the **Generate**
**Logview** dialog box, click **Run** to view the LogView information of the job.

**Terminate jobs**

1. On the **JobSnapshot** tab, select one or more jobs that you want to terminate and click
**Terminate Job** above the list. In the **Kill Operation** panel, view the jobs to be terminated.
2. After you confirm the information, click **Run**. Then, a message that indicates the results
appears.

**Collect job logs**

If an exception occurs during the running of a job, you can collect job logs to identify and analyze the exception.

**Collect logs**

1. On the **JobSnapshot** tab, choose **Actions > Job Log Collection** in the upper-right corner.
2. In the **Job Log Collection** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Service Role | The service roles that you want to use to collect job logs from the cluster. You can select one or more service roles. |
| intanceid | Optional. The ID of the job instance. |
| requestid | Optional. The request ID returned when the job fails. If the value that you specify is not a request ID, job logs that contain the specified value are collected. |
| Time Range | The time range within which job logs are collected. |
| Time interval | Optional. The interval of log collection. Unit: hours. |

3. After you complete the configuration, click **Run** to start job log collection.

**View execution history**

1. Yo can view the status and progress of job log collection.
i. On the **JobSnapshot** tab, choose **Actions > Execution History**. ii. In the **Execution History** panel, you can view the status of the current log collection task and historical log collection tasks. `RUNNING` indicates that the task is collecting logs. `SUCCESS` indicates that the task is completed. `FAILED` indicates that the task failed. If the task is in the `RUNNING` state, you can click **Details** in the **Details** column of the task to view the progress.
2. View the path where job logs are stored.
After the log collection task is completed, click **Details** in the **Details** column of the task in the **Execution History** panel. Then, view the path where the collected job logs are stored in the **Job Log Collection** step.

##### Business optimization

###### Merge small files

Excessive small files in a MaxCompute cluster occupy a lot of memory resources. Apsara Big Data Manager (ABM) allows you to merge multiple small files in MaxCompute clusters and projects to free up the memory occupied by these files.

**Go to the small file merging page**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Business Governance > Small File Merge**. The **TaskConfiguration** tab is displayed by
default.

**Create a merge task for a cluster**

If excessive small files exist in most projects of a MaxCompute cluster, you can create a merge task to merge these files in the cluster in a centralized manner.
1. In the **Cluster merge task** section of the **TaskConfiguration** page, click **add merge**
**task**. In the **Edit cluster merge configuration** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Cluster | The cluster for which you want to run the merge task. Select a cluster from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |

| Whether current limiting | Specifies whether to limit the concurrency of merge tasks for the cluster. Valid values: Yes: limits the concurrency. Merge tasks cannot run concurrently. No: does not limit the concurrency. Merge tasks can run concurrently. |
|---|---|
| Maximum concurrency | The maximum number of merge tasks that can run concurrently for the selected cluster. This parameter takes effect only when the Whether current limiting parameter is set to No. |
| Open | Specifies whether to enable the task. |
| merge parameter | The configurations for the merge task. You can use the following default configurations: { "odps.idata.useragent": "SRE Merge", "odps.merge.cpu.quota": "75", "odps.merge.quickmerge.flag": "true", "odps.merge.cross.paths": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.maintain.order.flag": "true", "odps.merge.failure.handling": "any" } |
| Maximum number of running jobs | The maximum number of jobs that can run concurrently for the selected cluster. This parameter is a global parameter. The jobs refer to all types of jobs in the selected cluster. |

2. Click **Compare Versions** below merge parameter to view the differences between the
original and modified values.
3. Click **Run**.
The merge task that you created appears in the **Cluster merge task** section.

**Create a merge task for a project**

If excessive small files exist in only a few projects of a MaxCompute cluster, you can create a merge task to merge the small files in a specific project.
1. In the **project merge task** section of the **TaskConfiguration** page, click **add merge**
**task**. In the **Edit a project merge task** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|

| Geography | The region in which the selected project resides. Select a region from the drop- down list. |
|---|---|
| Project Name | The name of the project for which you want to run the merge task. Select a project from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Priority | The priority of the task. A smaller value indicates a higher priority. |
| Whether to start | Specifies whether to enable the task. |
| Whether current limiting | Specifies whether to limit the concurrency of merge tasks for the project. Valid values: Yes: limits the concurrency. Merge tasks cannot run concurrently. No: does not limit the concurrency. Merge tasks can run concurrently. |
| Maximum concurrency | The maximum number of merge tasks that can run concurrently for the selected project. This parameter takes effect only when the Whether current limiting parameter is set to No. |
| Maximum number of running jobs | The maximum number of jobs that can run concurrently for the selected project. This parameter is a global parameter. The jobs refer to all types of jobs in the selected project. |

2. Click **Run**.
The merge task that you created appears in the **project merge task** section.

**View merge task statistics**

On the **HistoricalStatistics** tab, you can view the historical statistics of merge tasks for clusters and projects.

| Statistical type | Statistics details |
|---|---|

| Merge statistics | In the merge statistics section, the statistics on all merge tasks for each day in the previous month are displayed in a line chart. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that timed out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes. |
|---|---|
| Cluster statistics | In the Cluster Statistics section, the statistics on merge tasks for clusters on a specific day in the previous month are displayed in tables. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that timed out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes. |
| Project statistics | In the Project Statistics section, the statistics on merge tasks for projects on a specific day in the previous month are displayed in tables. You can view the maximum concurrency, priority, whether to limit the concurrency of merge tasks, and saved storage space in bytes. You can also view the numbers of running tasks, finished tasks, waiting tasks, tasks that timed out, failed tasks, invalid tasks, merged partitions, and reduced files. |

**Manage merge types**

On the **mergetypemanagement** tab, you can view the existing merge types and merge parameters.
1. Create a merge type.
In the **merge statistics** section, click **New merge type**. In the **Edit merge type** panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| merge type | The name of the merge type. |
| merge parameter | The merge parameters of the merge type. |

2. Click **Compare Versions** below **merge parameter** to view the differences between the
original and modified values.
3. Click **Run**.
The merge type that you created appears in the **merge statistics** section. To modify the merge type, click **Modify** in the **Operation** column.

###### Compress idle files

Apsara Big Data Manager (ABM) allows you to create archive tasks to compress idle files in MaxCompute clusters and projects. This saves storage space.

**Introduction**

In a cluster, ABM sorts the tables or partitions retained for more than 90 days by storage space. Then, ABM compresses the first 100,000 tables or partitions.

**Go to the Cold File Compression tab**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Business Governance > Cold File Compression**. By default, the **TaskConfiguration**
tab appears.

**Create an archive task for a cluster**

If excessive idle files exist in most projects of a MaxCompute cluster, you can create an archive task to compress these idle files in the cluster.
1. In the **Cluster archive task** section of the **TaskConfiguration** tab, click **New archive**
**task**. In the **Edit the cluster archive configuration** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Cluster | The cluster for which you want to run the archive task. Select a cluster from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Whether current limiting | Specifies whether to limit the concurrency of archive tasks for the cluster. Valid values: Yes: limits the concurrency. Archive tasks cannot be concurrently run. No: does not limit the concurrency. Archive tasks can be concurrently run. |
| Maximum concurrenc y | The maximum number of archive tasks that can be concurrently run for the selected cluster. This parameter takes effect only when the Whether current limiting parameter is set to No. |
| Open | Specifies whether to enable the task. |
| Maximum number of running jobs | The maximum number of jobs that can be concurrently run for the selected cluster. This parameter is a global parameter. The jobs refer to all types of jobs in the selected cluster. |

| Archive parameter | The configurations of the archive task. You can use the following default configurations: { "odps.idata.useragent": "SRE Archive", "odps.oversold.resources.ratio": "100", "odps.merge.quickmerge.flag": "true", "odps.merge.cross.paths": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.maintain.order.flag": "true", "odps.sql.hive.compatible": "true", "odps.merge.compression.strategy": "normal", "odps.compression.strategy.normal.compressor": "zstd", "odps.merge.failure.handling": "any", "odps.merge.archive.flag": "true" } |
|---|---|

2. You can click **Compare Versions** below the Archive parameter parameter to view the
differences between the original and modified values.
3. After you complete the configuration, click **Run**.
The archive task that you create appears in the **Cluster archive task** list.

**Create an archive task for a project**

If excessive idle files exist in only a few projects of a MaxCompute cluster, you can create an archive task to compress the idle files in a specific project. If the tables or partitions of a project are not ranked among the top 100,000 in the cluster, the archive task cannot compress the idle files in the project.
1. In the **project archive task** section of the **TaskConfiguration** tab, click **New archive**
**task**. In the **Edit a project archive task** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Geography | The region in which the selected project resides. Select a region from the drop- down list. |
| Project Name | The name of the project for which you want to run the archive task. Select a project from the drop-down list. |

| Start Time | The start time of the task. |
|---|---|
| End Time | The end time of the task. |
| Priority | The priority of the task. A small value indicates a high priority. |
| Whether to start | Specifies whether to enable the task. |
| Whether current limiting | Specifies whether to limit the concurrency of archive tasks for the project. Valid values: Yes: limits the concurrency. Archive tasks cannot be concurrently run. No: does not limit the concurrency. Archive tasks can be concurrently run. |
| Maximum concurrenc y | The maximum number of archive tasks that can be concurrently run for the selected project. This parameter is valid only when Bandwidth Limit is set to No. |
| Maximum number of running jobs | The maximum number of jobs that can be concurrently run for the selected project. This parameter is a global parameter. The jobs refer to all types of jobs in the selected project. |

2. After you complete the configuration, click **Run**.
The newly created archive task appears in the list of archive tasks for projects.

**View archive task statistics**

Click the **HistoricalStatistics** tab. On this tab, you can view the statistics of archive tasks, cluster archive tasks, and project archive tasks.

| Section | Statistics |
|---|---|
| archive statistics | The chart shows statistics on the execution of all archive tasks by day within the last month. It shows the numbers of running tasks, finished tasks, waiting tasks, timeout tasks, failed tasks, invalid tasks, merged partitions, and reduced files. It also shows the reduced physical storage usage in bytes. |
| Cluster Statistics | This section shows statistics on the execution of archive tasks for clusters by day within the last month. The table shows the numbers of running tasks, finished tasks, waiting tasks, timeout tasks, failed tasks, invalid tasks, merged partitions, and reduced files. The table also shows the reduced physical storage usage in bytes. |

| Project Statistics | This section shows statistics on the execution of archive tasks for projects by day within the last month. The table shows the numbers of running tasks, finished tasks, waiting tasks, timeout tasks, failed tasks, invalid tasks, merged partitions, and reduced files. The table also shows the reduced physical storage usage in bytes. |
|---|---|

**Manage archive types**

On the **Archivetypemanagement** tab, you can view the existing archive types and archive parameters.
1. Add an archive type
In the **archive statistics** section, click **New archive type**. In the **Edit archive type** panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| archive type | The name of the archive type. |
| archive parameter | The archive parameters of the archive type. |

2. After you complete the configuration, click **Compare Versions** below the **archive**
**parameter** parameter to view the differences between the original and modified values.
3. Then, click **Run**.
The archive type that you add appears in the **archive statistics** list. To modify an archive type, click **Modify** in the **Operation** column of the archive type.

###### Analyze MaxCompute resources

Apsara Big Data Manager (ABM) allows you to analyze the resources of MaxCompute clusters from multiple dimensions to help you better understand the data stored in MaxCompute. You can view the analysis results of data storage from the table, project, task, execution time, start time, and engine dimensions.

**Go to the resource analysis page**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Business Governance > Resource Analysis**. The **TableDimensions** tab appears by
default.

**Table dimension**

On the **TableDimensions** tab, you can view the detailed information about all tables in each project, including the number of partitions, physical storage usage, and number of Apsara Distributed File System files of each table, and the rankings based on the number of partitions, physical storage usage, and number of Apsara Distributed File System files. You can also sort tables by number of partitions, physical storage usage, and number of Apsara Distributed File System files.

**Project dimension**

On the **ProjectDimensions** tab, you can view the detailed information about the data stored in each project, including the number of Apsara Distributed File System files, physical storage usage, capacity unit (CU) usage, total memory usage, number of tasks, number of tables, and idle storage space of each project. You can also view the daily and weekly percentage by which the value of each metric is increased.

**Task dimension**

On the **TaskDimension** tab, you can view the execution status of tasks from three dimensions: task analysis, acceleration mode analysis, and abnormal reading/writing analysis.

**Task analysis**

On the **TaskDimension > TaskAnalysis** tab, you can view the detailed information about all tasks and rankings in each project, including the instance ID, running status, total consumption of CU, start time, end time, duration, ranking of CU usage, and SQL statements of each task.

**Acceleration mode analysis**

On the **TaskDimension > AccelerationModeAnalysis** tab, you can view the status of tasks in SQL acceleration mode in a cluster, which helps you optimize tasks. The metrics include the total number of accelerated tasks, the status of accelerated tasks, small tasks, and SQL tasks.

**Abnormal reading and writing analysis**

On the **TaskDimension > Abnormalreadingandwritinganalysis** tab, you can view the tasks in which exceptions occur on read/write operations. You can find the task based on the task information, and analyze and optimize the task.

**Time-consuming dimension**

On the **Time-consumingdimension** tab, you can view the numbers of tasks that consume less than 5 minutes, less than 15 minutes, less than 30 minutes, less than 60 minutes, and more than 60 minutes. In the Time-consuming operation chart, the numbers of tasks of each day in the specified time period are displayed in different colors to show the trends of tasks of different durations.

**Startup dimension**

On the **StartupDimension** tab, you can view the numbers of tasks that are started in different time periods for each project. The time interval is 30 minutes. In the Number of time period tasks chart, the numbers of tasks that are started in different time periods of each day in the specified time period are displayed.

**Engine dimension**

On the **EngineDimension** tab, you can view the trends of performance metrics of tasks in each project in the task Performance analysis chart. The performance metrics include cost_cpu, cost_mem, cost_time, input_bytes, input_bytes_per_cu, input_records, input_records_per_cu, odps_job_num, output_bytes, output_bytes_per_cu, output_records, and output_records_per_cu.

**Measurement dimension**

On the **MeasurementDimensions** tab, you can view the storage data of each project from the storage quota dimension. The storage data includes the upper limit of logical storage, maximum number of logical files, quota group ID, quota group name, upper limit CU of quota group, guaranteed CU of quota group, yesterday's CPU consumption, yesterday's memory consumption, yesterday's task volume, yesterday's logical storage, specification configuration, region, cluster, and collection date.

##### MaxCompute zone-disaster recovery

When a primary MaxCompute cluster fails, you can perform a primary/secondary switchover in the Apsara Big Data Manager (ABM) console to restore services. This topic describes the zone-disaster recovery feature of MaxCompute.

**Go to the zone-disaster recovery page**

1. Go to the Business operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Business operation and maintenance** tab, choose
**Zone-Disaster Recovery > Overview** to go to the **Overview** page.

**View the synchronization speed**

On the **Overview** page, the **Primary and Secondary Data Center Synchronization**
**Bandwidth** section displays a graph of the synchronization rate in MB/s for a specified time
period. in-avg: The average inbound network traffic. out-avg: The average outbound network traffic. To manually refresh the page, click the icon. To automatically refresh the page, click the icon and set the **Refresh Interval** and **Time Range** parameters.

**View the operation history**

Click **Operation History** in the upper-right corner of the **Overview** page to view the history of operations performed on this page, such as **Start Synchronization**, **Trigger**
**Unsynchronized Resource Query**, **Trigger Unsynchronized Data Query**, and **Switch**
**Default Compute Cluster**.

**Download the latest lists of unsynchronized data and resources**

The **Current RPO** section shows the Recovery Point Objective (RPO), which is the maximum acceptable data loss during synchronization. RPO 1 hour: A maximum of 1 hour of data loss is acceptable. RPO 0: Real-time synchronization with no data loss. Click **Download Latest Unsynchronized Data List** or **Download Latest Unsynchronized**
**Resource List** to download the information to your computer. Before you download a list,
check its retrieval time. If the list is not recent, click **Re-trigger Retrieval** to obtain the latest list of unsynchronized data or resources.

**Project overview**

The **Project Overview** section shows detailed disaster recovery information for each project, including whether the disaster recovery feature is enabled.

**Disaster recovery configuration**

If the **Disaster Recovery Cluster** column for a project contains a value, the disaster recovery feature is supported, and you can perform disaster recovery operations. If the column is empty, the feature is not supported for that project. For projects that support disaster recovery, configure the feature before starting synchronization:
1. Click **Configure** in the **Actions** column for the target project. In the disaster recovery
configuration panel that appears, configure the following parameters:

| Parameter | Description |
|---|---|

| Project Name | The name of the target project. This parameter cannot be modified. |
|---|---|
| Number Of Concurrent Processes | Configure this parameter based on the current network bandwidth. Note A single instance uses about 10 MB of bandwidth. |
| Synchronization Interval | An interval greater than 4 hours (14,400 seconds) is recommended. Note A short interval can cause network congestion and fill up the queue. |

2. Click **Execute** to complete the configuration.

**Start synchronization**

In the **Project Overview** section, click **Start Synchronization** in the **Actions** column for the target project. Then, click **Execute** in the **Start Synchronization** dialog box. The value in the **Synchronization Enabled** column for the target project changes from **Disabled** to
**Enabled**.

**Switch the default compute cluster**

In the **Project Overview** section, click **Switch Default Compute Cluster** in the **Actions** column for the target project. In the dialog box that appears, click **Execute**. A direct switch of the default compute cluster can cause data loss. Before you switch, ensure that data synchronization is complete and stop all data writes.

**View the switch history**

In the **Project Overview** section, click **View Switch History** in the **Actions** column for the target project to view the history of switches from the source cluster to the target cluster.

#### Service O&M

##### Control service O&M

###### Control service O&M features and entry

**point**

This topic describes the O&M features for control services and how to go to the O&M page.

**O&M features**

**Overview**: displays the information about control services. You can view the aggregated
information about services, service role status, job statistics, executor thread pool statistics, and job latency trend.
**ServiceRole**: displays the service roles of control services. You can view the host, service
status, requested CPU resources, and requested memory of each service role.
**ConfigurationManagement**: allows you to manage the configurations of global
computing, cluster-level computing, computing scheduling, and cluster endpoints.
**YuancangMonitoring**: displays the information about the metadata repository of
MaxCompute. You can view the completion time and status of the output tasks of the metadata repository and the time consumption trend of output tasks within a specific period of time.
**Service Role Startup/Stopped**: allows you to start or stop a service role of MaxCompute
or view the execution history of a service role. When you fail to start or stop a service role, you can quickly locate the cause of failure.
**Start Admin Console**: allows you to start Admin Console.
**Service log collection**: allows you to collect MaxCompute service logs to locate the cause
of service failures.
**Control Quantity Modification**: allows you to change the number of control nodes for
each service, such as HiveServer and ExecutorWorker.

**Go to the O&M page**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Monitoring** page appears by default. You can
click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar
and then click the **Service operation and maintenance** tab to perform service O&M operations.

###### Overview of control services

On the Overview tab, you can view the information about control services, including the aggregated information about services, service role status, job statistics, executor thread pool statistics, and job latency trend.

**Go to the Overview tab**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**. By default, the **Overview** tab appears.

**Service Summary**

In this section, the numbers of available services and unavailable services are displayed.

**Service Status**

In this section, all control service roles are displayed. You can also view the numbers of available services and unavailable services for each service role.

**Traffic-Job Run**

In this section, the statistics on jobs in the selected cluster are displayed. You can view the total number of jobs in the cluster, number of jobs that are running, number of jobs that are waiting for resources, and number of jobs that are waiting for scheduling. and the numbers of running jobs, jobs waiting for resources, and jobs waiting for scheduling respectively.

**Saturation-Executors thread pool**

In this section, the information about the thread pool is displayed. You can view the resource usage, number of jobs being processed, queue length, and maximum concurrency.

**Delay-waiting for job trend**

In this section, the chart displays changes in the numbers of jobs that are running, jobs that are waiting for resources, and jobs that are waiting for scheduling by using trend curves in different colors. You can click the icon in the upper-right corner of the chart to zoom in and specify a time range to view the trend within the specified time range.

###### Control service roles

The ServiceRole tab on the Control Services page displays information about the service roles of control services. You can view the host, status, requested CPU resources, and requested memory of each service role.

**View service role information**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**. Then, click the **ServiceRole** tab.
3. View the information about service roles, including **Host**, **Service Status**, **CPU**
**application**, and **Memory Request**.

###### Control service configuration

On the ConfigurationManagement tab, you can manage the configurations of global computing, cluster-level computing, computing scheduling, and cluster endpoints. If you want to modify the configurations of control services, submit a ticket to apply for technical support. Then, modify the configurations under the guidance of technical engineers.

**Go to the ConfigurationManagement tab**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**. Then, click the **ConfigurationManagement** tab.

**What to do next**

The **ConfigurationManagement** tab consists of the following tabs:
**Computescheduling**: You can manage configurations on the
**GlobalComputeConfiguration**, **Cluster-levelcomputingconfiguration**, and
**Computeschedulingconfiguration** tabs.
**DataChannelrouting**: You can manage configurations on the **Clusteraccessaddress** tab.

###### Metadata repository for control services

This topic describes how to view the completion time and status of the output tasks of the metadata repository and the time consumption trend of output tasks within a specific period of time in MaxCompute.

**Usage notes**

Output tasks of the metadata repository in MaxCompute are executed at a scheduled time every day. Apsara Big Data Manager (ABM) retrieves the status of output tasks every 30 minutes. If an output task is not completed within 24 hours, the task is considered failed.

**What to do next**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**. Then, click the **YuancangMonitoring** tab.
3. View information about the metadata repository.
The **YuancangMonitoring** tab displays the completion time of the output tasks of the metadata repository and the time consumption trend of output tasks within a specific period of time.
**Yuan warehouse output time**: displays information about the output tasks of the
metadata repository, including **Data Date**, **Completion time**, **Acquisition time**,
**Consumption**, and **Error Message**.
The **Completion time** column displays the time when an output task was completed. The **Acquisition time** column displays the latest status of an output task retrieved by ABM.
**Running time**: displays the time consumption trend of output tasks within the specified
period of time.

###### Stop or start a service role

Apsara Big Data Manager (ABM) allows you to start or stop the service roles of the MaxCompute control service and view the execution history. If you fail to start or stop the service roles, you can identify the cause of the failure.

**Go to the Control Services page**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**.

**Stop a service role**

1. On the **Control Services** page, choose **Actions > Service Role Stopped** in the upper-
right corner.
2. In the **Service Role Stopped** panel, select the service role that you want to stop and click
**Run**.
3. On the **Control Services** page, click **Execution History** in the upper-right corner. In the
**Execution History** panel, check whether the operation is successful.
In the **Execution History** panel, you can view the status, submission time, start time, end time, operator, type, and parameters of each operation.
4. Click **Details** in the Details column to view the execution details.
In the details panel, you can view the job name, status, steps, script, and parameter settings. You can also click **Download Execution Details** to download the details to your on-premises computer.

**Start a service role**

1. On the **Control Services** page, choose **Actions > Service Role Startup** in the upper-
right corner.
2. In the **Service Role Startup** panel, select the service role that you want to start and click
**Run**.
3. On the **Control Services** page, click **Execution History** in the upper-right corner. In the
**Execution History** panel, check whether the operation is successful.
In the **Execution History** panel, you can view the status, submission time, start time, end time, operator, type, and parameters of each operation.
4. Click **Details** in the Details column to view the execution details.
In the details panel, you can view the job name, status, steps, script, and parameter settings. You can also click **Download Execution Details** to download the details to your on-premises computer.

**Identify the cause of a failure**

This section describes how to identify the cause of the failure to start a service role.
1. On the **Control Services** page, click **Actions** in the upper-right corner, and then click
**Execution History** next to **Service Role Startup**.
2. On the **Execution History** page, find the job that you want to view and click **Details**.
3. In the **Service Role Startup** panel, choose **Service Role Startup > Servers > View**
**Details** to locate the failure cause.
You can analyze the cause of the failure by combining **Parameter Configuration**,
**Execution Output**, and **Execution Parameters**.

###### Start Admin Console

Admin Console is a management platform of MaxCompute and is disabled by default. Apsara Big Data Manager (ABM) allows you to quickly start AdminConsole to manage MaxCompute clusters in an efficient manner.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Start Admin Console**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**.
3. In the upper-right corner, choose **Actions > Start AdminConsole**.
4. In the **Start AdminConsole** panel, click **Run**. Then, the system displays the operation
submitted.

**View task status or progress**

1. On the **Control Services** page, click **Execution History** in the upper-right corner. In the
**Execution History** panel, you can view the history of the Start AdminConsole operation.
**RUNNING** indicates that the "Start AdminConsole" task is in progress. **SUCCESS**
indicates that the task has succeeded. **FAILED** indicates that the task has failed.
2. If the status of the task is **RUNNING**, click **Details** in the Details column to view the
execution progress.

**(Optional) Locate the cause of failure**

If the status of a "Start AdminConsole" task is **FAILED**, you can view the execution logs to locate the cause of failure.
1. On the **Control Services** page, click **Actions** in the upper-right corner, and then click
**Execution History** next to **Start AdminConsole**.
2. In the **Execution History** panel, find the task that you want to view and click **Details**.
3. In the **Start AdminConsole** panel, choose **Start AdminConsole > Machine Details >**
**View Details** corresponding to the failed step to locate the cause of failure.
You can analyze the cause of failure by clicking **Parameter Configuration** and
**Execution Parameters**.

###### Collect service logs

Apsara Big Data Manager (ABM) allows you to collect service logs generated within the specified time period. This helps you identify the cause of failure.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Collect service logs**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**.
3. On the Control Services page, choose **Actions > Service log collection** in the upper-right
corner.
4. In the **Service log collection** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Module Name | The service from which you want to collect service logs. You can select one or more services from the drop-down list. |

| Time Range | The time period during which the logs that you want to collect are generated. |
|---|---|
| Host Name | Separate multiple hostnames with commas (,). |

5. After you complete the configuration, click **Run**.

**View task status or progress**

1. On the **Control Services** page, click **Execution History** in the upper-right corner. In the
**Execution History** panel, you can view the history of the service log collection operation.
**RUNNING** indicates that service logs are being collected. **SUCCESS** indicates that
service logs are collected. **FAILED** indicates that service logs fail to be collected.
2. If a service log collection task is in the **RUNNING** state, click **Details** in the Details column
to view the progress of the task.

**(Optional) Locate the cause of failure**

If the status is **FAILED**, you can view the execution logs to identify the cause of failure.
1. On the **Control Services** page, click **Actions** in the upper-right corner, and then click
**Execution History** next to **Service log collection**.
2. In the **Execution History** panel, find the task that you want to view and click **Details**.
3. In the **Service log collection** panel, choose **Service log collection > Servers > View**
**Details** to locate the cause of failure.
You can analyze the cause of failure by clicking **Parameter Configuration** and
**Execution Parameters**.

###### Change the number of control nodes

MaxCompute allows you to change the number of control nodes for each service, such as HiveServer and ExecutorWorker.

**Change the number of control nodes**

1. Go to the Service operation and maintenance tab of MaxCompute.
2. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Control Services**.
3. In the upper-right corner of the page, click **Actions** > **Control Quantity Modification**.
4. In the **Control Quantity Modification** panel, modify the related control information,
including HiveServer, ExecutorWorker, AuthServer, RecycleWorker, CatalogServer, OdpsWorker, and MessageServer.
5. After the configuration is complete, click **Run**. A message appears, indicating that the
operation has been submitted.

**View the execution status or progress**

1. On the **Control Services** page, click **Execution History** in the upper-right corner. In the
**Execution History** panel, view the operation history of control information modification.
For control information modification tasks, **RUNNING** indicates that the execution is in progress, **SUCCESS** indicates that the execution succeeds, and **FAILED** indicates that the execution fails.
2. Find a task in the **RUNNING** state, and click **Details** in the Details column to view the
execution progress.

**Locate the cause of a failure to modify control information**

The following example describes how to locate the cause of a failure to modify the number of control nodes.
1. On the **Control Services** page, click **Actions** in the upper-right corner, and then click
**Execution History** next to **Control Quantity Modification**.
2. On the **Execution History** page, find the task that you want to manage and click **Details**
in the Details page.
3. In the **Control Quantity Modification** panel, choose **Control Quantity Modification >**
**Servers > View Details** to locate the failure cause.
You can analyze the cause of the failure by combining **Parameter Configuration** and
**Execution Parameters**.

##### Job Scheduler O&M

###### O&M features and entry point

This topic describes the O&M features for Job Scheduler and how to go to the O&M page.

**O&M features**

**Overview**: displays the key information about the operations of Job Scheduler. You can
view the summary of services, service role status, statistics on resource allocation, statistics on compute nodes, and the trends of CPU utilization and memory usage.
**ServiceRole**: displays the information about the master nodes and service roles of Job
Scheduler. You can restart the master nodes of Job Scheduler on this tab.
**ComputeNodes**: displays the information about the compute nodes of Job Scheduler. You
can manage the blacklist of compute nodes and the read-only permissions on this tab.
**Enable/Disable SQL acceleration**: allows you to enable or disable SQL acceleration for
Job Scheduler.
**Fuxi master Restart**: allows you to restart the primary and secondary master nodes.

**Go to the O&M page**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar
and then click the **Service operation and maintenance** tab.
4. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Fuxi service**. The Overview tab of the Job Scheduler appears by default.

###### Overview

On the Overview tab, the key information about the operations of Job Scheduler is displayed. You can view the summary of services, service role status, statistics on resource allocation, statistics on compute nodes, and the trends of CPU utilization and memory usage.

**Go to the Overview tab**

1. Go to the service O&M page for Job Scheduler.
2. On the **Overview** tab, you can view the key metrics of Job Scheduler. The metrics include
**Service Summary**, **Service Status**, **Resource Usage Trends**, **Saturation-Resource**
**Allocation**, and **Overview of compute node resources**.

**Service Summary**

This section displays the numbers of available services, unavailable services, and services that are being upgraded.

**Service Status**

This section displays all service roles of Job Scheduler and their status. You can also view the number of physical servers on which each service role is deployed and the number of physical servers in desired state for each service role. Click the name of a service role in the **Role** to go to the **Apsara Infrastructure**
**Management console** and view the details of the service role.

**Resource Usage Trends**

This section displays the trends of CPU utilization and memory usage for Job Scheduler. Each chart provides information about the used quota, minimum quota, maximum cluster quota, requested quota, and maximum quota in different colors. The statistics in the charts are periodically updated. You can also manually update the statistics. You can also view the trends of CPU utilization and memory usage within a specific period of time.

**Saturation-Resource Allocation**

This section displays the statistics on the allocation of CPU and memory resources.
**CPU allocation**: You can view the CPU utilization, the total number of CPU cores, the
number of available CPU cores, and the number of CPU cores for SQL acceleration.
**Memory allocation**: You can view the memory usage, the total memory size, the available
memory size, and the memory size for SQL acceleration.

**Overview of compute node resources**

This section displays the information about compute nodes. You can view the percentage of online compute nodes, the total number of compute nodes, the number of online compute nodes, and the number of compute nodes that are added to the blacklist.

###### Manage service roles

This topic describes how to view the master nodes and service roles of Job Scheduler, manage service roles, and restart master nodes.

**Go to the ServiceRole tab**

1. Go to the Service operation and maintenance tab for Job Scheduler.
2. Click the **ServiceRole** tab. This tab displays the information about Job Scheduler service
roles, including the service role name, host, IP address, service role status, and host status.

**Service roles**

| Service role | Description | Quantity | Form | High availability |
|---|---|---|---|---|
| FuxiMaster# | The master role of Job Scheduler. | Deployed on at least two physical servers. | Process | Yes |
| FuxiApiServer# | The API service role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
| PackageManager# | The package management role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
| Tubo# | The compute node role of Job Scheduler. | Deployed on at least three physical servers. | Process | Yes |
| DeployAgent# | The package delivery agent of Job Scheduler. | Deployed on at least three physical servers. | Process | Yes |
| FuxiDecider# | The approval role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
| FuxiMonitor# | The monitoring role of Job Scheduler. | Deployed on each physical server | Process | N/A |

**FuxiMaster#**

Service role description This service role does not depend on other service roles. This role is the master role of Job Scheduler. In most cases, the FuxiMaster# role is deployed on three physical servers. You must deploy the FuxiMaster# role on at least two physical servers. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiMaster#/fuxi_master` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**FuxiApiServer#**

Service role description This service role depends on the FuxiMaster# role. This role is the API service role of Job Scheduler. In most cases, the FuxiApiServer# role is deployed on three physical servers. You must deploy the FuxiApiServer# role on at least two physical servers. You can deploy the FuxiApiServer# role together with the FuxiMaster# role. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory:

```
 /cloud/app/fuxi/FuxiApiServer#/fuxi_apiserver .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**PackageManager#**

Service role description This service role does not depend on other service roles. This role is used to manage the computing software packages of Job Scheduler. In most cases, the PackageManager# role is deployed on three physical servers. You must deploy the PackageManager# role on at least two physical servers. You can deploy the PackageManager# role together with the FuxiMaster# role. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory:

```
 /cloud/app/fuxi/Packagemanager#/packagemanager .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**Tubo#**

Service role description This service role depends on the FuxiMaster# role. Physical servers on which this role is deployed serve as the compute nodes of Job Scheduler. You must deploy the Tubo# role on at least three physical servers. Computing tasks are scheduled to physical servers on which the Tubo# role is deployed. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/Tubo#/tubo` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**DeployAgent#**

Service role description This service role depends on the PackageManager# role. Physical servers on which this role is deployed serve as agents for deploying the computing software packages of Job Scheduler. You must deploy the DeployAgent# role on at least three physical servers. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/DeployAgent#/deploy_agent` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**FuxiDecider#**

Service role description This service role does not depend on other service roles. Physical servers on which this role is deployed are used to approve the requests for starting or shutting down the compute nodes of Job Scheduler. This role is required if you want to shut down a compute node. In most cases, the FuxiDecider# role is deployed on three physical servers. You must deploy the FuxiDecider# role on at least two physical servers. You can deploy the FuxiDecider# role together with the FuxiMaster# role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiDecider#/fuxi_decider` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**FuxiMonitor#**

Service role description This service role does not depend on other service roles. In most cases, the FuxiMonitor# role is deployed on each physical server of a cluster and is used to monitor all service roles of Job Scheduler that are deployed on each physical server. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiMonitor#/fuxi_monitor` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**Supported operations**

You can restart the master nodes of Job Scheduler. For more information, see Restart a master node of Job Scheduler.

###### Job Scheduler compute nodes

You can view the details of compute nodes on the ComputeNodes tab for Job Scheduler, including the total CPU, idle CPU, total memory, and idle memory of each compute node. You can also check whether a node is added to the blacklist and whether it is active. You can also add compute nodes to or remove compute nodes from the blacklist or read-only list on the ComputeNodes tab.

**Go to the ComputeNodes tab**

1. Go to the service O&M tab for Job Scheduler.
2. Click the **ComputeNodes** tab. On this tab, you can view the details of compute nodes,
including the total CPU, idle CPU, total memory, and idle memory of each compute node. You can also check whether a node is added to the blacklist and whether the node is active.

**Blacklist and read-only settings**

You can add compute nodes to or remove compute nodes from the blacklist or read-only list. To add compute nodes to the blacklist, perform the following steps:
1. On the **ComputeNodes** tab, find the desired compute node and click **Actions > Add**
**blacklist** in the Actions column.
2. In the panel that appears, click **Run**. A message appears, indicating that the action is
submitted. The value of the **Hostname** parameter is automatically filled. You do not need to specify a value for this parameter. You can check whether a compute node is added to the **blacklist** in the **compute node** list after the configuration is complete.

###### Enable and disable SQL acceleration

You can enable or disable SQL acceleration for Job Scheduler in the Apsara Big Data Manager (ABM) console. The execution speed of SQL statements in Job Scheduler is greatly increased with SQL acceleration enabled, but more computing resources are consumed.

**Enable SQL acceleration**

1. Go to the service O&M page for Job Scheduler.
2. In the upper-right corner of the page, click **Actions > Enable SQL acceleration**.
3. In the **Enable SQL acceleration** panel, configure the **WorkerSpans** parameter.
**WorkerSpans**: the default resource quota of the cluster and the resource quota for a
specific period. Default value: **default:2,12-23:2**. The default value indicates that the default resource quota is 2 and the resource quota for the period from 12:00 to 23:00 is also 2. You can set the resource quota based on your business requirements. For example, you can set this parameter to default:2,12- 23:4 to increase the resource quota in peak hours.
4. Click **Run**.

**Disable SQL acceleration**

1. Go to the service O&M page for Job Scheduler.
2. In the upper-right corner of the page, click **Actions > Disable SQL acceleration**.
3. In the panel that appears, click **Run**.

**View the execution history of enabling or disabling SQL**

**acceleration**

After you submit the action of enabling or disabling SQL acceleration, you can view the execution history to check whether the action is complete. The system executes the action as a job. It provides execution records and logs for each execution so that you can identify faults encountered during its execution. This section describes how to view the execution history of enabling SQL acceleration.
1. In the upper-right corner of the page, click **Actions** and select **Execution History** next to
**Enable SQL acceleration**.
2. In the **Execution History** panel, view the execution history of enabling SQL acceleration.
The execution history displays the current status, submission time, start time, end time, and operator of each execution.
3. Find the job that you want to view and click **Details** in the Details column. In the **Enable**
**SQL acceleration** panel, choose **Enable SQL acceleration > Servers > View Details**
to locate the cause of the failure. You can analyze the cause of the failure by combining **Parameter Configuration**,
**Servers**, **Commands**, and **Execution Parameters**.

###### Restart a master node of Job Scheduler

Job Scheduler is the resource management and task scheduling system of the Apsara distributed operating system. Apsara Big Data Manager (ABM) allows you to quickly restart the primary and secondary master nodes of Job Scheduler. Cluster services are not affected during the restart process.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Restart a master node of Job Scheduler**

1. Go to the service O&M page for Job Scheduler.
2. On the **ServiceRole** tab, find the primary or secondary master node that you want to
manage and click **Fuxi master Restart** in the **Actions** column.
3. In the **Fuxi master Restart** panel, click **Run**. A message appears, indicating that the job is
submitted. The **Fuxi master Restart** panel appears.

**View the execution status or progress**

1. In the **Fuxi master Restart** panel, check the execution history of restarting master nodes
of Job Scheduler. The **Fuxi master Restart** panel displays the restart history. **RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the execution succeeds. **FAILED** indicates that the execution fails.
2. If the status is **RUNNING**, click **Details** in the Details column to view the execution
progress.

**(Optional) Identify the cause of a failure**

If the status is **FAILED**, you can view the execution logs to identify the cause of the failure.
1. In the **Fuxi master Restart** panel, check the execution history of restarting master nodes
of Job Scheduler.
2. Click **Details** in the Details column of the job to view the details.
3. On the **Servers** tab of the failed step, click **View Details** in the Actions column of a failed
server. The **Execution Output** tab appears in the Execution Details section. You can view the output to identify the cause of the failure.

##### Apsara Distribute File System O&M

###### O&M features and page

This topic describes the O&M features for Apsara Distributed File System and how to go to the O&M page.

**O&M features**

The **Overview** tab displays the key operation metrics of Apsara Distributed File System. You can view the summary of services, service role status, statistics on storage usage, statistics on storage nodes, and the trend charts of storage usage and the number of files. The **ServiceRole** tab displays the information about the master nodes and service roles of Apsara Distributed File System. You can change the primary master node or run a checkpoint on a master node of Apsara Distributed File System. The **StorageManagement** tab displays the information about the storage nodes of Apsara Distributed File System. You can set the status of a storage node to Disabled or Normal, or set the status of a disk on a storage node to Normal or Error. In the master status section of the ServiceRole tab, you can find a master node and choose Actions > **Master performs switching** in the Actions column to change the primary master node of Apsara Distributed File System in the selected cluster. In the master status section of the ServiceRole tab, you can find a master node and choose Actions > **The Master executes the Checkpoint** in the Actions column to run a checkpoint on the master node to write memory data to disks. In the upper-right corner of the Pangu Service page, you can move the pointer over Actions and select **Clean up the system Recycle bin** to clear the recycle bin of Apsara Distributed File System. In the upper-right corner of the Pangu Service page, you can move the pointer over Actions and select **Enable automatic data equalization** or Turn off automatic data equalization to enable or disable the data rebalancing feature of Apsara Distributed File System.

**Go to the O&M page of Apsara Distributed File System**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar.
Then, click the **Service operation and maintenance** tab.
4. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Pangu Service**. The Overview tab of the default cluster for Apsara Distributed File System
appears.

###### Overview

On the Overview tab, the key information about the operations of Apsara Distributed File System is displayed. You can view the summary of services, service role status, statistics on storage usage, statistics on storage nodes, and the trends of storage usage and the number of files.

**Go to the Overview tab**

1. Go to the service O&M page for Apsara Distributed File System.
2. On the **Overview** tab, you can view the key metrics of Apsara Distributed File System,
including **Service Summary**, **Service Status**, **Saturation-storage level**, **Physical**
**storage capacity**, **Document change trend**, and **Storage Node Overview**.

**Service Summary**

This section displays the status of Apsara Distributed File System and the number of service roles.

**Service Status**

This section displays all service roles of Apsara Distributed File System and their status. You can also view the number of physical servers on which each service role is deployed and the number of physical servers in desired state for each service role.

**Saturation-storage level**

This section displays the statistics on storage usage and the number of files.
**Storage water level**: You can view the storage usage, total storage space, available
storage space, and the size of the recycle bin.
**Number of files Water level**: You can view the storage usage of files, maximum number
of files, number of existing files, and number of files in the recycle bin.

**Physical storage capacity and Document change trend**

In the Physical storage capacity and Document change trend sections, the trend charts of storage usage and the number of files are displayed. The Physical storage capacity chart shows the trend lines of the total storage space, used storage space, and storage usage in different colors. The Document change trend chart shows the trend line of the number of files. In the upper-right corner of a chart, you can click the icon to zoom in on the chart. The following figure shows an enlarged chart of storage usage. You can specify the start date and end date in the upper-left corner of the enlarged chart to view the storage usage of the cluster in the specified period.

**Storage Node Overview**

This section displays the information about the storage nodes of Apsara Distributed File System. You can view the numbers of data nodes, normal nodes, disks, and normal disks. You can also view the percentages of faulty nodes and faulty disks.

###### Manage service roles

This topic describes how to view the master nodes and service roles of Apsara Distributed File System and manage service roles. This topic also describes how to change the primary master node or run a checkpoint on a master node of Apsara Distributed File System.

**Go to the ServiceRole tab**

1. Go to the Service operation and maintenance page for Apsara Distributed File System.
2. On the **ServiceRole** tab, view the information about the master nodes and service roles of
Apsara Distributed File System. The information about a master node includes the IP address, hostname, service role, and log ID. The information about a service role includes the service role name, hostname, IP address, service role status, and host status.

**Service roles**

| Service role | Description | Quantity | Form | High reliability |
|---|---|---|---|---|
| PanguMaster# | The master role of Apsara Distributed File System. | Deployed on at least three physical servers. | Process | Yes |

| PanguChunkserver# | The data node role of Apsara Distributed File System. | Deployed on at least three physical servers. | Process | Yes |
|---|---|---|---|---|
| PanguSupervisor# | The role that is used to control the service roles of Apsara Distributed File System. | Deployed together with the master role on at least three physical servers. | Process | Yes |
| PanguMonitor# | The monitoring role of Apsara Distributed File System. | Deployed on each physical server. | Process | N/A |
| PanguTools# | The toolkit of Apsara Distributed File System. | Deployed on at least one physical server. | N/A | N/A |

**PanguMaster#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least one volume for a cluster. A volume contains multiple master nodes. Each volume contains one primary master node and multiple secondary master nodes. A cluster for which three physical servers are deployed can work properly if a single physical server becomes faulty. A cluster for which five physical servers are deployed can work properly if one or two physical servers become faulty. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/pangu/PanguMaster#/pangu_master` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see Go to the ServiceRole tab.

**PanguChunkserver#**

Service role description This service role depends on the PanguMaster# role. You must deploy this role on at least three physical servers for a cluster and in multiple racks. This is because three replicas are written when you write data to a cluster. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. You must make sure that a request for shutting down data nodes is approved. In this case, data migration is complete. Logs Logs are stored in the following directory:

```
 /cloud/app/pangu/PanguChunkserver#/pangu_chunkserver .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see Go to the ServiceRole tab.

**PanguSupervisor#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least three physical servers for a cluster. The primary instance is elected to provide services. This role is used to approve the requests for starting or shutting down the master nodes or data nodes of a cluster. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory:

```
 /cloud/app/pangu/PanguSupervisor#/pangu_supervisor .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see Go to the ServiceRole tab.

**PanguMonitor#**

Service role description This service role does not depend on other service roles. In most cases, the PanguMonitor# role is deployed on each physical server of a cluster and is used to monitor all service roles of Apsara Distributed File System that are deployed on each physical server. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/pangu/PanguMonitor#/pangu_monitor` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see Go to the ServiceRole tab.

**PanguTools#**

Service role description This service role does not depend on other service roles. A physical server on which this role is deployed provides the CLI toolkit for Apsara Distributed File System. You can deploy this role on one or more physical servers. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs N/A Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see Go to the ServiceRole tab.

**Supported operations**

You can change the primary master node or run a checkpoint on a master node of Apsara Distributed File System. For more information, see Change the primary master node of Apsara Distributed File System or Run a checkpoint on a master node of Apsara Distributed File System.

###### Apsara Distributed File System storage

This topic describes how to view the storage overview and storage node information of Apsara Distributed File System, and how to set the status of storage nodes and data disks.

**Go to the storage overview page**

1. Go to the service O&M page for Apsara Distributed File System.
2. Click the **StorageManagement** tab. By default, the **StorageOverview** tab appears.
The **StorageOverview** tab displays the following information about Apsara Distributed File System: **rebalance Status**, **Total Nodes**, **Number of normal nodes**, **Total**
**number of disks**, **Number of normal disks**, **Total storage size**, and **Remaining**
**storage size**.

**Go to the storage node page**

1. Go to the service O&M page for Apsara Distributed File System.
2. Click the **StorageManagement > StorageNode** tab.
The **StorageNode** tab displays information about all storage nodes of Apsara Distributed File System, including **Number of chunks**, **Total Space**, **Remaining**
**space**, **Status**, **TTL**, and **sendBuffer**.

**Set the status of a storage node**

You can set the status of a storage node to **Disabled** or **Normal**. This example shows how to set the status of a storage node to Disabled. You can follow the same steps to set the status of a storage node to Normal.
1. On the **StorageNode** tab, find the desired node and choose **Actions > Set Storage**
**Node to Down State**.
2. In the **Set Storage Node to Down State** dialog box, click **Run**.
The **Volume** and **Hostname** parameters are automatically specified based on the storage node you selected. After you complete the preceding steps, you can check whether the status of storage node is changed in the storage node list.

**Set the status of a data disk**

You can set the status of a data disk to **Error** or **Normal**. This example shows how to set the status of a data disk to Error. You can follow the same steps to set the status of a data disk to Normal.
1. On the **StorageNode** tab, find the desired node and choose **Actions > Set data disk to**
**error state**.
2. In the **Set data disk to error state** panel, specify **DiskId**.
The **Volume** and **Hostname** parameters are automatically specified based on the storage node you selected.
3. After you complete the configuration, click **Run**.

###### Change the primary master node of

**Apsara Distributed File System**

Apsara Big Data Manager (ABM) allows you to perform a primary/secondary switchover on the master nodes of Apsara Distributed File System. After the primary/secondary switchover is complete, an original secondary master node becomes the primary master node, and the original primary master node becomes a secondary master node.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Background information**

A volume in Apsara Distributed File System is similar to a namespace. The default volume is PanguDefaultVolume. If a cluster contains a large number of nodes, multiple volumes may exist. Each volume has three master nodes. One of the nodes serves as the primary master node, and the other two nodes serve as secondary master nodes.

**Procedure**

1. Go to the service O&M page for Apsara Distributed File System.
2. Click the **ServiceRole** tab.
3. In the **master status** section of the **ServiceRole** tab, find the master node that you want
to manage and choose **Actions > Master perform switching**. In the Master performs switching panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Volume | The default value is PanguDefaultVolume. If a cluster contains multiple volumes, set this parameter to the name of the actual volume whose primary master node needs to be changed. |
| Hostname | The hostname of the secondary master node that will become the new primary master node. |
| Log gap _ | The maximum log gap between the original primary and secondary master nodes. During the switchover, the system checks the log gap between the original primary and secondary master nodes. If the gap is less than the specified value, the switchover is allowed. Otherwise, you cannot change the primary master node. Default value: 100000. |

4. After you complete the configuration, click Click **Run**. A message appears, indicating that
the request is submitted. The **Master performs switching** panel appears. The **Master performs switching** panel shows the switchover history. **RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the execution succeeds. **FAILED** indicates that the execution fails.
5. If an execution is in the FAILED state, click **Details** in the Details column to identify the
cause of the failure. You can analyze the cause of failure by clicking **Parameter Configuration**, **Servers**, and **Execution Parameters**.

###### Run a checkpoint on a master node of

**Apsara Distributed File System**

Apsara Big Data Manager (ABM) allows you to run checkpoints on the master nodes of Apsara Distributed File System. This way, memory data is written to disks. If Apsara Distributed File System is faulty, you can use checkpoints to restore data to the state before the failure. This ensures data consistency.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Procedure**

1. Go to the Service operation and maintenance page for Apsara Distributed File System.
2. Click the **ServiceRole** tab.
3. In the **master status** section of the **ServiceRole** tab, find the master node that you want
to manage, move the pointer over **Actions** in the Actions column, and then select **The**
**Master executes the Checkpoint**. In the The Master executes the Checkpoint panel,
configure the **Volume** parameter. By default, the **Volume** parameter is set to **$(volume.volume)**.
4. Click **Run**. The Success message appears to inform you that the request is submitted. The
**The Master executes the Checkpoint** panel appears.
In the **The Master executes the Checkpoint** panel, the history of checkpoints on the master node is displayed. **RUNNING** indicates that the request is being processed.
**SUCCESS** indicates that the request is successful. **FAILED** indicates that the request
fails.
5. If an operation record is in the FAILED state, click **Details** in the Details column to identify
the cause of the failure. You can analyze the cause of the failure by combining **Parameter Configuration**,
**Servers**, and **Execution Parameters**.

###### Clear the recycle bin of Apsara

**Distributed File System**

Apsara Big Data Manager (ABM) allows you to clear the recycle bin of Apsara Distributed File System to release storage space.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Clear the system recycle bin**

1. Go to the Service operation and maintenance page for Apsara Distributed File System.
2. On the **Overview** tab, move the pointer over **Actions** in the upper-right corner and select
**Clean up the system Recycle bin** .
3. In the panel that appears, configure the **Volume** parameter. By default, this parameter is
set to **${volume.volume}**.
4. Click **Run**. The Success message appears to inform you that the request is submitted.

**View the operation history of system recycle bin cleanup**

After you execute a system recycle bin cleanup, you can view the execution history to check whether the cleanup operation is complete. The system executes the operation as a job. It provides execution records and logs for each execution so that you can identify faults encountered during its execution. The following example describes how to view the execution history of clearing the system recycle bin.
1. Click **Actions** in the upper-right corner and select **Execution History** next to **Clean up**
**the system Recycle bin**.
2. In the **Execution History** panel, view the execution history of clearing the system recycle
bin. The execution history displays the current status, submission time, start time, end time, and operator of each execution.
3. Find the job that you want to view and click **Details** in the Details column. In the **Clean up**
**the system Recycle bin** panel, choose **Clean up the system Recycle bin > Servers >**
**View Details** to locate the cause of the failure.
You can analyze the cause of the failure by combining **Parameter Configuration**,
**Servers**, and **Execution Parameters**.

###### Enable or disable data rebalancing for

**Apsara Distributed File System**

Apsara Big Data Manager (ABM) allows you to enable or disable data rebalancing for Apsara Distributed File System.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Disable data rebalancing**

1. Go to the service O&M page for Apsara Distributed File System.
2. On the **Overview** tab, choose **Actions > Turn off automatic data equalization** in the
upper-right corner.
3. In the panel that appears, specify **Volume**. The default value is PanguDefaultVolume.
4. After you complete the configuration, click **Run**.

**Enable data rebalancing**

1. Go to the service O&M page for Apsara Distributed File System.
2. On the **Overview** tab, choose **Actions > Enable automatic data equalization** in the
upper-right corner.
3. In the panel that appears, specify **Volume**. The default value is PanguDefaultVolume.
4. After you complete the configuration, click **Run**.

**Identify the cause of failure to enable or disable data**

**rebalancing**

After you enable or disable data rebalancing, you can check whether the operation is successful in the execution history. The system executes the operation by running a job. It provides execution records and logs for each execution so that you can identify faults occurred during the execution. This section describes how to view the execution history of operations for enabling data rebalancing.
1. Move the pointer over **Actions** in the upper-right corner of the page and click **Execution**
**History** next to **Enable automatic data equalization**.
2. In the **Execution History** panel, view the execution history of operations for enabling data
rebalancing. The execution history displays the current status, submission time, start time, end time, and operator of each operation.
**RUNNING** indicates that the operation is in progress. **SUCCESS** indicates that the
operation is completed. **FAILED** indicates that the operation failed.
3. Find the operation that you want to view and click **Details** in the Details column. In the
**Enable automatic data equalization** panel, choose **Enable automatic data**
**equalization > Servers > View Details** in the failed step to locate the cause of failure.
You can analyze the cause of failure by clicking **Parameter Configuration**, **Servers**, and **Execution Parameters**.

##### Tunnel service

###### O&M features and entry point

This topic describes the O&M features for the tunnel service and how to go to the O&M page for the tunnel service.

**What is the tunnel service?**

The tunnel service serves as a data tunnel of MaxCompute. You can use this service to upload data to or download data from MaxCompute.

**O&M features**

**Overview**: displays the overall information about the tunnel service. You can view the
summary of services, service role status, and the throughput trend chart.
**ServiceRole**: displays the information about the roles of the tunnel service.
**Flowanalysis**: displays the traffic curves of specific projects within a specific period of
time. The curves indicate the traffic types and the peak throughout within the specified period. This helps you make informed decisions.
**ConfigurationManagement**: allows you to manage endpoints. You can also view all the
projects that are configured in the current cluster and switch the tunnel configurations for projects.
**Restart the tunnel service**: allows you to restart the tunnel service.

**Go to the O&M page**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar
and then click the **Service operation and maintenance** tab.
4. In the left-side navigation pane of the **Service operation and maintenance** tab, click
**Channel Services**. The Overview tab of the tunnel service appears by default.

###### Overview

On the Overview tab, the overall information about the tunnel service is displayed. You can view the summary of services, service role status, and the trend chart of throughput.

**Go to the Overview tab**

1. Go to the Channel Services page of MaxCompute.
2. On the **Overview** tab, you can view key metrics of the tunnel service, including **Service**
**Summary**, **Service Status**, and **Channel Service Throughput**.

**Service Summary**

In this section, the numbers of available service roles, unavailable service roles, and service roles that are being updated are displayed.

**Service Status**

In this section, all service roles of the tunnel service and their status are displayed. You can also view the number of physical servers on which each service role is deployed and the number of physical servers at desired state for each service role.

**Channel Service Throughput**

In this section, the throughput trend of the tunnel service is displayed on a per-minute basis. You can manually update the statistics or set the system to automatically update the statistics. You can also view the trend of the throughput within a specific period of time.

###### Manage tunnel service roles

On the ServiceRole tab, the information about the roles of the tunnel service is displayed. You can view the role name, hostname, IP address, role status, and host status of each service role. You can also restart the roles of the channel service if necessary.

**Go to the ServiceRole tab**

1. Go to the tunnel service O&M page of MaxCompute.
2. On the **ServiceRole** tab, the information about all roles of the tunnel service is displayed.
You can view the role name, hostname, IP address, role status, and host status of each role. A service role may be in the `good` , `error` , or `upgrading` state.

**Service roles**

| Service role | Descript ion | Quantity | Form | High availability |
|---|---|---|---|---|
| FrontendServer# | The frontend service role. | Deployed on at least two physical servers. | Process | Yes |
| TunnelFrontendServer# | The tunnel service role. | Deployed on at least two physical servers. | Process | Yes |
| ServiceTest# | The probing service role. | Deployed on at least one physical server. | Process | None |

**FrontendServer#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least two instances of a cluster. The two instances are associated with a virtual IP address (VIP) for load balancing. RMA and server restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) and can be restarted. You need to restart the physical servers in batches. Server reclone The physical servers on which the service role is deployed can be recloned. You need to reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/odps-service-`

```
frontend/FrontendServer#/frontend_server/current/log .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**TunnelFrontendServer#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least two instances of a cluster. The two instances are associated with a VIP for load balancing. RMA and server restart The physical servers on which the service role is deployed support the RMA and can be restarted. You need to restart the physical servers in batches. Server reclone The physical servers on which the service role is deployed can be recloned. You need to reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/odps-service-`

```
frontend/TunnelFrontendServer#/tunnel_frontend_server/current/log .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**ServiceTest#**

Service role description This service role does not depend on other service roles. This role provides the frontend service detection capability. You can deploy this role on one or more physical servers. RMA and server restart The physical server on which the server role is deployed supports the RMA or restart operation. Server reclone The physical servers on which the service role is deployed can be recloned. Logs N/A. Monitoring You can check whether the physical servers on which the service role is deployed are in desired state. For more information, see the Go to the ServiceRole tab section of this topic.

**Restart the tunnel service**

You can restart multiple roles of the tunnel service at a time.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Procedure**

1. On the **ServiceRole** tab, select the service role that you want to restart in the **Service**
**Overview** list and click **Restart the tunnel service** in the upper-right corner.
2. In the **Restart the Tunnel Server** panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Forced restart | Specifies whether to forcefully restart tunnel servers for the selected service roles. Valid values: no force: does not forcefully restart tunnel servers. If a service role is _ running, the tunnel server is not restarted. force: forcefully restarts tunnel servers. In this case, the status of a service role does not affect the restart of the tunnel server. |
| Hostname | The hostnames of the selected service roles. The value is automatically provided. |

3. After you complete the configuration, click **Run**.

**View the execution status or progress**

On the **ServiceRole** tab, click **Execution History** in the upper-right corner to view the history of operations for restarting service roles.
**RUNNING** indicates that the operation is in progress. **SUCCESS** indicates that the
operation succeeds. **FAILED** indicates that the operation fails. If the status is **RUNNING**, click **Details** in the Details column to view the execution progress.

**(Optional) Identify the cause of failure**

If the status is **FAILED**, you can view the execution logs to identify the cause of failure.
1. On the **ServiceRole** tab, click **Execution History** in the upper-right corner to view the
history of operations for restarting service roles.
2. In the Execution History panel, click **Details** in the Details column of the operation to view
the details.
3. In the **Restart the Tunnel Server** panel, choose **Restart the Tunnel Server > Servers**
**> View Details** in the failed step to locate the cause of failure.

###### Traffic analysis

The Flowanalysis tab displays the traffic curves of specific projects within a specific period of time. The curves show traffic types and the peak throughout within the specified time period, which helps you make informed decisions.

**Go to the Flowanalysis tab**

1. Go to the Channel Services page of MaxCompute.
2. Click the **Flowanalysis** tab. After you specify a time period and a project for traffic
analysis, click the icon. Then, you can view the uplink throughput and downlink throughput in the **Tunnel traffic uplink throughput** and **Downlink throughput of**
**Tunnel traffic** charts.
**Time selection**: Select a time range.
**Project Name**: Select one or more projects from the drop-down list.
The traffic data comes from `tianjimon` . Make sure that this system functions as expected.

###### Configuration management

On the ConfigurationManagement tab, you can manage endpoints, view all the projects that are configured in the current cluster, and switch the tunnel configurations for projects.

**Go to the ConfigurationManagement tab**

1. Go to the Channel Services page of MaxCompute.
2. Click the **ConfigurationManagement** tab.
On the **ConfigurationManagement** tab, you can add, modify, and remove endpoints. You can also view all the projects that are configured in the current cluster and switch the tunnel configurations for projects.

**Add an endpoint**

1. On the **ConfigurationManagement** tab, select a region and a cluster from the drop-down
lists next to **Regional Cluster** and click the icon.
2. Click the **Endpointconfiguration** tab.
3. On the Endpointconfiguration tab, click **New** in the upper-right corner. In the **Added**
**endpoint** panel, configure the **New Cluster** and **The new host** parameters.
4. Click **Run**. The endpoint is added.
On the **Endpointconfiguration** tab, select the endpoints that you want to remove and click **Delete** in the upper-right corner to remove multiple endpoints at a time. On the **Endpointconfiguration** tab, find the endpoint that you want to modify and click **Modification** in the **Actions** column to modify the endpoint.

**Switch the tunnel configurations**

1. On the **ConfigurationManagement** tab, select a region and a cluster from the drop-down
lists next to **Regional Cluster** and click the icon.
2. Click the **Channelclusterprojectlist** tab.
3. Select one or more projects for which you want to switch the tunnel configurations and click
**Switch Channel Configuration**.
4. In the **Switch project tunnel** panel, configure the **Target Cluster** parameter and click
**Run**.

##### Replication service

The replication service allows you to configure base_config, infoBetweenClusters, taskParams, virtualResource, and bandwidthTopology in a region.

**Go to the O&M page of the replication service**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar.
Then, click the **Service operation and maintenance** tab.
4. In the left-side navigation pane of the **Service operation and maintenance** page, click
**Replication Service**. The **ConfigurationManagement** tab appears.

**Manage configuration items**

On the **ConfigurationManagement** tab, select a region from the **Geography** drop-down list. Then, you can manage the following configuration items.

| Configurati on item | Configuration method |
|---|---|
| base config _ | In the base config section, click Modify Basic Configuration. Modify _ Configuration Content based on your business requirements, click Compare Versions, confirm that the modifications are correct, and then clickR un. |
| infoBetween Clusters | In the infoBetweenClusters section, click Modify infoBetweenClusters. Modify Configuration Content based on your business requirements, click Compare Versions, confirm that the modifications are correct, and then clickR un. |
| taskParams | In the taskParams section, click Modify taskParams. Modify Configuration Content based on your business requirements, click Compare Versions, confirm that the modifications are correct, and then click Run. |
| virtualResou rce | In the virtualResource section, click Modify virtualResource. Modify Configuration Content based on your business requirements, click Compare Versions, confirm that the modifications are correct, and then clickR un. |

| bandwidthT opology | In the bandwidthTopology section, click Modify bandwidthTopology. Modify Configuration Content based on your business requirements, click Compare Versions, confirm that the modifications are correct, and then clickR un. |
|---|---|

In the **base_config**, **infoBetweenClusters**, and **taskParams** sections, you can sort entries by column information in ascending or descending order. Keyword search is supported. In the **virtualResource** and **bandwidthTopology** sections, you can filter data based on existing columns. In addition, you can use the drop-down **menu** to export data to a **CSV** or **XLS** file, **adjust column widths to fit content automatically**, and **configure which columns are displayed** .

#### Cluster O&M

##### Cluster O&M features and entry point

This topic describes the O&M features of MaxCompute clusters. It also provides information about how to go to the MaxCompute cluster O&M page.

**Cluster O&M features**

O&M features of MaxCompute clusters:
**Overview**: You can view the overall information about a cluster, including the host status,
service status, and health check history. You can also view the trend charts of the CPU utilization, disk usage, load, memory usage, packet loss rate, and packet error rate of the cluster. In the Quick Login section, you can click the name of the host whose role is pangu master, fuxi master, or odps ag to log in to the host.
**Health**: Displays all metrics of a cluster. You can view the details of metrics, solutions to
the alerts triggered by the metrics, and status of each metric. You can also log in to a host and manually perform checks on the host.
**Machine List**: Displays information about the hosts in a cluster. The information includes
the hostname, IP address, role, and type.
**Node expansion/Node shrinkage**: You can add or remove physical hosts to scale out or
scale in a MaxCompute cluster.

**Go to the cluster O&M tab**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar.
Then, click the **Cluster O & M** tab.

##### Overview of MaxCompute clusters

This topic describes how to go to the Overview tab for managing and maintaining a MaxCompute cluster. This topic also introduces the Overview tab and the operations that you can perform on this tab.

**Go to the Overview tab**

1. Go to the cluster O&M tab of Maxcompute.
2. By default, the **Overview** tab appears.
The **Overview** tab displays O&M modules commonly used to manage the selected cluster, including **Quick Login**, **Machine Status**, **Service Status**, and **Running Health**. This tab also consists of the following resource usage trend charts: **CPU**, **DISK**, **MEMORY**, **LOAD**, and **PACKAGE**.

**Quick Login**

In the Quick Login section, you can quickly log in to the hosts of `pangu master` , `fuxi` `master` , and `odps ag` , which are commonly used to manage and maintain MaxCompute clusters.
1. In the **Quick Login** list of the **Overview** tab, click the name of a host in the **Host** column
to go to the **Host O & M** tab.
2. In the left-side host list, find the host to which you want to log in and click the
icon next to the hostname to go to the **TerminalService** page.
3. In the left-side navigation pane, click the hostname to log in to the host.

**Machine Status**

In the Machine Status section, the number of hosts in the **good** or **error** state is displayed.

**Service Status**

In the Service Status section, all services deployed in the cluster are displayed. You can view the number of services in the **good** or **bad** state.

**CPU**

This chart shows the trend lines of the total CPU utilization (cpu), CPU utilization for executing code in kernel space (sys), and CPU utilization for executing code in user space (user). The trend lines are displayed in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster within the specified time period.

**DISK**

The DISK chart shows the trend line of the storage usage of the cluster over time. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the cluster within the specified time period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes over time. The trend lines are displayed in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes within the specified time period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory capacity, used memory, memory used by buffers, memory used by the page cache, and available memory over time. The trend lines are displayed in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the cluster within the specified time period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets over time. The trend lines are displayed in different colors. These trend lines reflect the data transmission status of the cluster. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the cluster within the specified time period.

**Running Health**

In the Running Health section, the number of check items for the cluster and the numbers of CRITICAL, WARNING, and EXCEPTION alerts are displayed. Click **View Details** to go to the Health tab. On the Health tab, you can view the details of health checks. For more information, see Manage cluster health checks.

##### Manage cluster health checks

On the Health tab, all check items and check results of a cluster are displayed. You can view the details of check items and view the check results for hosts to handle alerts. You can also log in to a host and perform manual checks on the host.

**Go to the Health tab**

1. Go to the cluster O&M tab of MaxCompute.
2. Click the **Health** tab. On this tab, you can view all check items for the cluster and the check
results of the hosts in the cluster. The following alerts may be reported on a host: **Critical**,
**Warning**, and **Exception**. The alerts are shown in different colors. You must handle the
alerts at the earliest opportunity, especially the **Critical** and **Warning** alerts. The following table describes the check results.

| Check result | Description |
|---|---|
| Critical | A critical alert. |
| Warning | A threshold-based alert. |
| Exception | An exception in a script call. |

**View the details of a check item**

1. On the **Health** tab, find the check item that you want to view and click **Details** in the
**Actions** column. In the message that appears, view the details of the check item.
The following information about the check item is displayed: **Name**, **Source**, **Alias**,
**Application**, **Type**, **Scheduling**, **Default Parameters**, **Custom Parameters**, and
**Description**. The methods to clear alerts are provided in the description.
2. Click **Show More** to view more information about the check item.
You can view more information in the **Script**, **Target (TianJi)**, **Default Threshold**, and
**Custom Threshold** sections.

**View the hosts for which alerts are reported and the causes for**

**the alerts**

You can view the check history and check results of a check item on a host.
1. On the **Health** tab, click the
icon to the left of a check item to show all alerts that are triggered by the check item. You can view all hosts on which the check item is run.
2. Click a hostname in the **Host** column. In the panel that appears, click **Details** in the
Actions column of a check result to view the cause.

**Handle alerts**

On the **Health** tab, find the check item for which alerts are triggered and click **Details** in the Actions column. In the **Details** message, view the methods to clear alerts.

**Run a check item again**

After you clear an alert for a host, choose **Actions > Refresh** for the host on the **Health** tab to run the check item on the host again. This allows you to confirm whether the alert will be triggered again.

##### View hosts in a MaxCompute cluster

The Machine List tab displays information about all hosts in the current MaxCompute cluster.

**View host information**

1. Go to the cluster O&M tab of MaxCompute.
2. Click the **Machine List** tab. On this tab, you can view information about all hosts in the
current cluster, including the hostname, IP address, role, and host type. To view detailed information about a host, click the name of the host in the **Hostname** column. Then, the Host O & M tab appears.

##### Scale a MaxCompute cluster

Apsara Big Data Manager (ABM) allows you to scale MaxCompute clusters. To scale out a cluster, you can add physical hosts from the default cluster of Apsara Infrastructure Management to the cluster. To scale in a cluster, you can move physical hosts from the cluster to the default cluster of Apsara Infrastructure Management.

**Usage notes**

In Apsara Stack, cluster scale-out is complex. You must configure a new physical host on Deployment Planner. This way, the host can be added to the default cluster of Apsara Infrastructure Management. Regarded as an idle resource pool, the default cluster can provide resources for scaling out production clusters. To scale out a cluster, you can add physical hosts from the default cluster of Apsara Infrastructure Management to the cluster. To scale in a cluster, you can move physical hosts from the cluster to the default cluster of Apsara Infrastructure Management. You can use this method to scale out or scale in MaxCompute clusters in the ABM console.

**Prerequisites**

**Scale-out conditions**:
The physical host that you want to add is an **SInstance** host in the default cluster of Apsara Infrastructure Management. The template host is an **SInstance** host. You can log in to the admingateway host in a MaxCompute cluster to view SInstance hosts.
**Scale-in conditions**: The physical host that you want to remove is an **SInstance** host.
You can log in to the admingateway host in a MaxCompute cluster to view SInstance hosts.

**View host types**

1. Log in to the admingateway host in the MaxCompute cluster.
2. Run the `r ttrl` command to query and record `SInstance` hosts.

**Scale out a MaxCompute cluster**

You can add multiple hosts to a MaxCompute cluster at a time to scale out the cluster. To do this, you must specify an existing host as the template host. When you scale out the MaxCompute cluster, the hosts clone configurations from the template host. This way, the hosts can be added to the cluster at a time.
1. Go to the cluster O&M tab of MaxCompute.
2. Click the **Machine List** tab. On the **Machine List** tab, select a host of the `SInstance`
type as the template host.
3. Then, choose **Actions > Node expansion**. In the **Node expansion** panel, configure the
parameters. Parameters:
**Region**: the region of the host that you want to add.
**Refer Hostname**: the name of the template host. By default, the name of the selected
host is used.
**hostname**: the name of the host that you want to add. The drop-down list displays all
available hosts in the default cluster for scale-out. You can select one or more hosts from the drop-down list.
4. After you complete the configuration, click **Run**.

**Scale in a MaxCompute cluster**

You can remove multiple hosts from a MaxCompute cluster at a time to scale in the cluster.
1. Go to the cluster O&M tab of MaxCompute.
2. Click the **Machine List** tab. On the **Machine List** tab, select one or more hosts of the
**SInstance** type to remove.
3. Then, choose **Actions > Node shrinkage**. In the **Node shrinkage** panel, configure the
parameters. Parameters:
**Region**: the region of the host that you want to remove.
**Hostname**: the name of the host that you want to remove. By default, the name of the
selected host is used.
4. After you complete the configuration, click **Run**.

**Identify the cause of a scale-out or scale-in failure**

After you scale out or scale in a cluster, you can view the execution history to check whether the operation is successful. The system executes the operation by running a job. It provides execution records and logs for each execution so that you can identify faults occurred during the execution. This section describes how to identify the cause of a scale-in failure. You can follow the same procedure to identify the cause of a scale-out failure.
1. Click **Execution History** in the upper-right corner of the page. In the **Execution History**
panel, view the execution history of scale-in operations. The execution history displays the name, current status, submission time, start time, end time, and operator of each operation. Scale-out and scale-in operations are time-consuming. **RUNNING** indicates that the operation is in progress. **SUCCESS** indicates that the operation is completed. **FAILED** indicates that the operation failed.
2. Find the operation that you want to view and click **Details** in the Details column. In the
**Node shrinkage** panel, choose **Node shrinkage > Servers > View Details** in the failed
step to locate the cause of failure. You can analyze the cause of failure by clicking **Parameter Configuration**, **Servers**, and **Execution Parameters**.

#### Host O&M

##### O&M features and page

This topic describes the O&M features for the host service and how to go to the O&M page.

**O&M features**

On the **Overview** tab, the brief information about hosts in a MaxCompute cluster is displayed. You can view the server information and service role status of a server. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, packet loss rate, and packet error rate for the server. On the **Service Role** tab, the cluster to which a host belongs, the service instances that are running on the host, and the service roles that are deployed on the host are displayed.

**Go to the O&M page**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar.
Then, click the **Host O & M** tab.

##### Host overview

On the Overview tab, the brief information about hosts in a MaxCompute cluster is displayed. You can view the server information and service role status of a host. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, and packet loss rate for the host.

**Go to the Overview tab**

1. Go to the host O&M tab of MaxCompute.
2. By default, the **Overview** tab appears.
On the **Overview** tab, you can view the key metrics of the selected host, including host information, service roles and status, and the CPU, DISK, MEMORY, LOAD, and PACKAGE charts that show the usage trends.

**Machine Information**

In the Machine Information section, the detailed information about the host is displayed. You can view the region, cluster, name, IP address, status, data center, and server room of the host.

**Machine Service Role Status**

In the Machine Service Role Status section, the information about the services that are deployed on the host is displayed. You can view the roles, status, and number of services.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the host in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the/ directory for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the host in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the host in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the host in the specified period.

##### Manage service roles

On the Service Role tab, the service instances and service roles that are deployed on a host are displayed.

**View the service role of a host**

1. Go to the host O&M tab of MaxCompute.
2. Click the **Service Role** tab. On this tab, you can view information about the O&M service
roles of the host, including the cluster where the host resides, service instances running on the host, and the roles of the service instances.

### Management

#### Overview

The Management tab of MaxCompute consists of the following modules: Job Services, Recycling Management, Health Management, and Operational Audit.
**Job Services**: allows you to run jobs to perform O&M operations on MaxCompute.
**Recycling Management**: allows you to configure recycling settings to recycle chart data
in MaxCompute.
**Health Management**: allows you to create health check items and apply them to service
hosts.
**Operational Audit**: allows you to view the job execution records and O&M records in
MaxCompute.

#### Job services

##### Overview

This topic describes job-related concepts and the Job Execution page in MaxCompute. MaxCompute allows you to run jobs to perform O&M operations on services. Jobs, also known as service O&M tasks, are O&M operations performed on physical devices in a cluster. Jobrelated operations are performed on the **Job Execution** page.

**Concepts**

Ordinary job: A job that can only be manually run. No timer is set. Cron job: A job that is automatically run based on timer settings.

**Job Execution page**

The **Job Execution** page contains the following tabs: Jobs You can view, run, copy, export, and delete ordinary jobs, and view their execution history. You can search for a specific ordinary job. Cron Jobs You can enable, disable, view, run, copy, export, and delete cron jobs, and view their execution history. You can search for a specific cron job. Execution History You can view the execution history of ordinary and cron jobs. You can specify multiple filter conditions to search for a specific job and view the execution history of the specific job.

##### Enable or disable a cron job

When a cron job is generated, the job is disabled by default. You must manually enable it. If you do not need the cron job to run during a specified time period, you can manually disable it.

**Prerequisites**

An Apsara Big Data Manager (ABM) administrator account is obtained.

**Procedure**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Management** in the top navigation bar. In the left-side
navigation pane, click **Job Services**. The **Job Execution** page appears.
4. On the **Job Execution** page, click the **Cron Jobs** tab.
5. On the **Cron Jobs** tab, you can enable or disable a cron job.
To enable a cron job in the inactive state, click **Enable** in the Actions column of the cron job. After a cron job is enabled, its **status** changes to **Active**. The **Enable** button is replaced by **Disable**. To disable a cron job in the active state, click **Disable** in the Actions column of the cron job. After a cron job is disabled, its **status** changes to **Inactive**. The **Disable** button is replaced by **Enable**.

##### Manually run a job

After you create a regular job, you must manually run the job to perform O&M operations. You can also manually run a cron job.

**Prerequisites**

An Apsara Big Data Manager (ABM) administrator account is obtained.

**Procedure**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Management** in the top navigation bar. In the left-side
navigation pane, click **Job Services**. The **Job Execution** page appears.
4. On the **Job Execution** page, click the **Jobs** tab.
To manually run a cron job, click the **Cron Jobs** tab. The procedure for manually running a cron job is the same as that for manually running a regular job. In this example, a regular job is run.
5. On the **Jobs** tab, find a job and choose **Actions > Run**.
6. In the dialog box that appears, configure the parameters in the **Configure target group**
**and parameters** step, and then click **Next Step**.
7. Follow the on-screen instructions in the **Confirm Risk** step, and then click **Confirm**.
A record is automatically generated on the **Execution History** tab. For more information, see View job execution history.
8. On the job execution page, click **Start** in the upper part to run the job.
If you leave the job execution page without performing any operations, you can find the execution record on the **Execution History** tab. You can choose **Actions > Details** to go to the job execution page again.

##### View job execution history

MaxCompute allows you to view the execution history of a specific job or all jobs.

**Prerequisites**

An Apsara Big Data Manager (ABM) administrator account is obtained.

**Background information**

After you confirm to run a job, MaxCompute generates logs to help you learn about the execution details of the job. The **Execution History** tab provides the following features: Information such as the trigger mode, status, start time, and end time of each job. Job execution details and parameter settings. You can also download the execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the **Pending** state or rerun a job that is in the **Exception** state. This topic describes how to view the execution history of a regular job. You can follow the same procedure to view the execution history of a cron job.

**View the execution history of a job**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Management** in the top navigation bar. In the left-side
navigation pane, click **Job Services**. The **Job Execution** page appears.
4. On the **Job Execution** page, click the **Jobs** tab.
5. On the **Jobs** tab, click **History** in the Actions column of a regular job. The **Execution**
**History** tab appears.
You can view the execution history of this job on the **Execution History** tab. For more information, see View execution history.

**View execution history**

1. If the number of historical records is large on the **Execution History** tab, you can specify
the instance name, time range, and execution status, and then click **Search** to query historical records that meet the conditions.
2. You can also find a record and choose **Actions > Details** to view the job execution details.
The following table lists the operations that you can perform on records in different states.

| Execution status | Supported operation | Procedure |
|---|---|---|
|   | View parameter settings | Click Parameter Configuration in the upper-right corner of the job details page, and select Context Parameters or Global Parameters to view the context parameters or global parameters of the job. |

| ger |   |   |
|---|---|---|
| All states |   |   |
|   | Download execution details | Click Download Execution Details in the upper-right corner of the job details page to download the job execution details to your on-premises machine. Save the job execution details into a TXT file. The execution details record the JSON and raw data of job execution. |
|   | View the execution details of steps | On the Servers tab of a step, click View Details in the Actions column of a server. The execution details of the step performed on the server, including the execution output, are displayed in the Execution Details section. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|   | Refresh the page | If the job is in the running state, you can clickR efresh in the upper-right corner of the job details page to view the latest execution status. |
| Pending | Start the job | Click Start in the upper-right corner of the job details page to start the job. |
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |
| Unconfirmed | Complete the manual operation | In the manual step to be performed, follow the instructions and click OK to go to the next step. |
|   | Roll back to the final status of the previous step | In the manual step to be performed, clickR ollback to roll back to the final status of the previous step. |
|   | Cancel the job | Click Cancel to cancel the job. |
|   | Retry the step that encountered exceptions | In the step that encountered exceptions, click Retry to retry the step. |

| xCompute |   |   |
|---|---|---|
| Exception |   |   |
|   | Skip the step that encountered exceptions | In the step that encountered exceptions, click Skip to skip this step and perform the subsequent steps. |
|   | Roll back to the final status of the previous step | In the step that encountered exceptions, click Rollback to roll back to the final status of the previous step. |
|   | Reset the step that encountered exceptions to the Pending state | In the step that encountered exceptions, click Reset to reset the step to the Pending state. When the step that encountered exceptions is reset to the Pending state, the execution status changes to Paused. You can click Continue in the upper-right corner of the job details page to perform the step again. |
|   | View the execution details of steps that encountered exceptions | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step performed on the server, including the execution output and error message, are displayed in the Execution Details section. After you view the details of the server that encountered exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to perform the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|   | Retry the failed step | In the failed step, click Retry to retry the step. |
|   | Skip the failed step | In the failed step, click Skip to skip this step and perform the subsequent steps. |
|   | Roll back to the final status of the previous step | In the failed step, click Rollback to roll back to the final status of the previous step. |

| Failure |   |   |
|---|---|---|
|   | Reset the failed step to the Pending state | In the failed step, click Reset to reset the step to the Pending state. When the failed step is reset to the Pending state, the execution status changes to Paused. You can click Continue in the upper-right corner of the job details page to perform the step again. |
|   | View the execution details of failed steps | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step performed on the server, including the execution output and error message, are displayed in the Execution Details section. After you view the details of the server that encountered exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to perform the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |

#### Recycling management

You can configure recycling settings for custom chart data or default chart data.

**Prerequisites**

Your Apsara Big Data Manager (ABM) account is granted the required permissions on services on which you want to perform O&M operations.

**Procedure**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. In the top navigation bar of the MaxCompute console, click **Management**. In the left-side
navigation pane of the **Management** page, click **Recycling Management**. The **Chart**
**data recovery** page appears.

**Custom**

a. In the upper-right corner of the Chart data recovery page, click **Add**. In the **Add** panel, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Products | Specify a service. By default, MaxCompute is specified. |
| Chart Location | The position of the chart to be recycled on the O&M page. Example: Project List-Overview. |
| Library name. Table name | The names of the database and table from which the chart data will be recycled. The value is in the Database name.Table name format. |
| Retrieve Field | The target field in the table from which the chart data will be recycled. |
| Retention period (days) | The retention period of the chart data to be recycled. |

b. After you complete the configuration, click **Submission**. Then, you can view the recycling item in the **Custom** section. You can also modify the recycling item by clicking **Modification** in the Actions column.

**System**

This section displays the default recycling items, including the chart data on the
**Business operation and maintenance** and **Service operation and maintenance**
tabs. This section consists of the following parameters: **Chart Location**, **Retention**
**period (days)**, **Modification time**, and **Actions**. You can click **Modification** in the
**Actions** column of a recycling item to modify the retention period. After you modify the
parameter, click **Submission**.

#### Health management

##### Monitoring settings

Apsara Big Data Manager (ABM) provides a wide variety of built-in scheduling and monitoring checkers for each big data service. These checkers are used to identify service faults and trigger alerts. This helps you detect and fix faults at the earliest opportunity.

**Prerequisites**

Your Apsara Big Data Manager (ABM) account is granted the required permissions on services that you want to manage and maintain. The alert sources and check items corresponding to the monitoring checkers are obtained.

**Background information**

Different services have different scheduling and monitoring checkers, but you can configure and manage them in the same manner.
**Scheduling checkers**: These checkers run scheduling scripts on the servers of specific
Apsara Infrastructure Management roles and generate raw alert data. Raw alert data provides information about the checker, server, alert severity, and alert content. Raw alert data is stored in the ABM database.
**Monitoring checkers**: Monitoring checkers will collect raw alert data generated by
scheduling checkers to the corresponding service pages of ABM. You can configure filter policies to display alerts collected by preferred checkers on specific service pages. Both scheduling and monitoring checkers are built-in checkers. You cannot add scheduling or monitoring checkers. However, you can modify certain parameters of these checkers, such as whether to enable a checker, operation settings, and description. In addition, you can add or delete mount points for monitoring checkers.

**Go to the Management page**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. In the top navigation bar, click **Management** to go to the Management page.

**View details and mount points of scheduling checkers**

The mount points of scheduling checkers are built-in, and you cannot add, modify, or delete mount points. The mount points of scheduling checkers correspond to all hosts of the Apsara Infrastructure Management role that runs the scheduling script.
1. In the left-side navigation pane, click **Health Management**. By default, the **Monitoring**
**Configuration > Scheduling** tab appears.
The **Scheduling** tab displays all scheduling checkers of the service.
2. On the **Scheduling** tab, find the scheduling checker that you want to view and click **View**
in the Actions column to view its details. The details of the scheduling checker include the name, alias, description, and steps of the checker.
3. On the Scheduling tab, find the scheduling checker that you want to view and click the
icon on the left to view the mount points of the scheduling checker.

**Modify a scheduling checker**

You can configure the scheduling interval and operation settings of a scheduling checker, and specify whether to enable the scheduling checker.
1. In the left-side navigation pane, click **Health Management**. By default, the **Monitoring**
**Configuration > Scheduling** tab appears.
2. On the **Scheduling** tab, find the scheduling checker that you want to manage and click
**Edit** in the Actions column. In the Modify Checker dialog box, configure the parameters.
**Type**: If you set this parameter to **System Default**, other parameters, such as
**Execution Interval** and **Parameters**, are set to the default values. If you set
this parameter to **Custom**, you can configure other parameters as needed. Configure the **Execution Interval** parameter based on the **crontab** command.
3. After you complete the configuration, click **OK**.

**View faulty hosts**

You can view all faulty hosts in the current cluster.
1. In the left-side navigation pane, click **Health Management**. By default, the **Monitoring**
**Configuration > Scheduling** tab appears.
2. Click **Faulty Servers** in the upper-right corner to view the faulty hosts in the cluster.
The list shows all faulty hosts in the current cluster and the role of each host in Apsara Infrastructure Management.

**Modify a monitoring checker**

You can modify the name and description of a monitoring checker and configure whether to enable the monitoring checker. The alert sources and check items of monitoring checkers are built-in. We recommend that you do not modify them.
1. In the left-side navigation pane, click **Health Management**. By default, the **Monitoring**
**Configuration > Scheduling** tab appears.
2. Click the **Monitoring** tab.
The **Monitoring** tab displays all monitoring checkers of the service.
3. On the Monitoring tab, find the monitoring checker that you want to manage and click
**Modify** in the Actions column to modify the configurations of the monitoring checker,
including the alert source, check items, name, and description of the monitoring checker.
4. After you complete the configuration, click **OK**.

**Add a mount point for a monitoring checker**

You can add mount points for monitoring checkers in order to collect raw alert data to the O&M page of each service in the ABM console.
1. In the left-side navigation pane, click **Health Management**. By default, the **Monitoring**
**Configuration > Scheduling** tab appears.
2. Click the **Monitoring** tab.
3. On the Monitoring tab, find the monitoring checker that you want to manage and click the
icon on the left to view the mount points of the monitoring checker.
4. Click **Add Mount Point** below the mount point list. In the dialog box that appears,
configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|

| O&M using Apsara Bigda ger | ta Ma MaxComput |
|---|---|

| Mount Point | The mount point to which the monitoring checker collects inspection results. For example, a value of odps/host specifies that the result is collected to the host O&M page of MaxCompute. |
|---|---|
| Filter Policy | The filter policy. Valid values: None: All alerts generated by the monitoring checker are displayed. Custom: The alerts generated by the monitoring checker are filtered by the filter configured for the service tree node. Node Name: The alerts whose node name is the same as the name of the current node are displayed. |
| Enabled | Specifies whether to enable the mount point. |

5. After you complete the configuration, click **OK**.

**Delete a mount point for a monitoring checker**

1. Go to the Management page. In the left-side navigation pane, click **Health Management**.
By default, the **Monitoring Configuration > Scheduling** tab appears.
2. Click the **Monitoring** tab.
3. On the Monitoring tab, find the monitoring item that you want to manage and click the
icon on the left to view the mount points of the monitoring checker.
4. Find the mount point that you want to delete and click **Delete** in the Mount Point column. In
the message that appears, click **OK**.

**Delete a monitoring checker**

1. Go to the Management page. In the left-side navigation pane, click **Health Management**.
By default, the **Monitoring Configuration > Scheduling** tab appears.
2. Click the **Monitoring** tab.
3. Find the monitoring checker that you want to delete and click **Delete** in the Actions
column. In the message that appears, click **OK**.

##### Inspection management

The inspection management feature of Apsara Big Data Manager (ABM) allows you to configure inspection scenarios, inspection items, and scenario combinations based on your business requirements.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M.

**Go to the Inspection Management page**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. In the top navigation bar of the **MaxCompute** console, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Management**. The **Scheduling** tab is displayed by default.
4. Click the **Patrol Configuration** tab. The **Scenes** tab is displayed by default.

**Create a scenario**

1. In the upper-right corner of the **Scenes** tab, click **Create Scene**. In the Create Scene
panel, configure the parameters, including Name, Description, Trigger Mode, Sharing, Status, and Tag.
2. Click **Submit**.
After the scenario is created, you can perform operations on the scenario, such as **Edit**,
**Start Patrol**, and **Manage Patrol Items**. You can also click **Execution History** to view
the execution history.

**Create an inspection item**

1. Click the **Patrol Items** tab and then click **Create Patrol Item** in the upper-right corner.
2. In the **Create Patrol Item** panel, configure the parameters.
3. Click **Submit**.
After the inspection item is created, you can perform operations on the inspection item, such as **Edit** and **Delete**.

**Create a scenario combination**

1. Click the **Scenario Combination** tab. Then, click **Create Scene** in the upper-right corner.
2. In the **Create Scene** panel, configure the parameters.
3. Click **Submit**.
After the scenario combination is created, you can perform operations on the scenario combination, such as **Edit** and **Manage Patrol Items**. You can also click **Execution**
**History** to view the execution history.

#### Audit O&M operations

This feature allows you to view the O&M operations of MaxCompute. The details of each operation are provided for tracing and troubleshooting.

**Prerequisites**

Your Apsara Big Data Manager (ABM) account is granted the required permissions on services on which you want to perform O&M.

**Procedure**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Management** in the top navigation bar. In the left-side
navigation pane of the **Management** page, click **Operational Audit**. The **Operational Audit** page displays the historical O&M operations of MaxCompute. The information about MaxCompute O&M operations includes the operation name, operation ID, risk, current status, submission time, start time, end time, operator, type, parameters, and details. The Operational Audit page displays only the historical O&M operations of a big data service. Take note that the O&M operations of job services are not displayed.
4. Click **Details** for an operation to view the O&M operation details.
If an O&M operation fails, view the cause of failure.
5. When an O&M task is in the Not Started, Pending, Exception, or Failure state, you can
perform the operations listed in the following table.

| State | Supported operation |
|---|---|
| Not Started | Click Start to start the task. Click Parameter Configuration to view the parameters of the task. Click Cancel to cancel the task. |
| Pending | Follow the instructions and click OK to go to the next step. Click Rollback to roll back to the final status of the previous step. Click Parameter Configuration to view the parameters of the task. Click Cancel to cancel the task. |
| Exception | Click Retry to retry the step. Click Skip to skip the step and perform the subsequent steps. Click Rollback to roll back to the final status of the previous step. Click Parameter Configuration to view the parameters of the task. Click Cancel to cancel the task. |
| Failure | Click Retry to retry the step. Click Skip to skip this step and perform the subsequent steps. Click Rollback to roll back to the final status of the previous step. Click Parameter Configuration to view the parameters of the task. Click Cancel to cancel the task. |

6. To download the O&M operation execution logs, click **Download Execution Details** in the
upper part of the panel.

## Deep inspection

### Overview

The deep inspection feature helps you check the monitoring alerts, resource usage, and key metrics of MaxCompute. You can use this feature to check the health status of the platform to avoid unexpected risks. This helps ensure the stability of MaxCompute clusters. The deep inspection feature can check information about the following aspects: MaxCompute cluster inspection: checks the health status of MaxCompute clusters. MaxCompute risk inspection: checks for risks that affect the health of MaxCompute clusters. Apsara Big Data Manager (ABM) does not recycle inspection reports, but collects all risks and related thresholds that are contained in the inspection reports.

### Inspect clusters

This topic describes how to check the health status of MaxCompute clusters and quickly identify faulty clusters.

**Background information**

You can perform the following operations to check the health status of a MaxCompute cluster: Inspect the status of a cluster Inspect cluster alerts Inspect the control service Inspect Job Scheduler Inspect Apsara Distributed File System Inspect the tunnel service Inspect Apsara Name Service and Distributed Lock Synchronization System Inspect a metadata warehouse

**Inspect the status of a cluster**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon.
3. In the **Site Navigation** section, click **TIANJI**.
4. In the **Apsara Infrastructure Management** console, choose **Resource Management >**
**Product & Cluster O&M** in the left-side navigation pane.
5. On the **Product & Cluster O&M** page, enter `odps` in the **Product | Cluster** search box
to search for MaxCompute clusters.
6. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the details page, view the status of the cluster in the **Basic Information** section and the status of the services in the cluster on the **Services** tab to check whether the services are at desired state. If the services of the cluster are in the **Not Ready** state, submit a ticket for technical support.

**Inspect cluster alerts**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the **MaxCompute** page, click Operation and maintenance in the top navigation bar.
Then, click the **Cluster O & M** tab. On the Cluster O & M tab, click the **Health** tab. The value in the **Critical** column indicates the number of critical alerts. The value in the **Warning** column indicates the number of threshold-based alerts. The value in the **Exception** column indicates the number of exceptions in script calls. In most cases, the values in the **Critical**, **Warning**, and **Exception** columns are all 0, or no result is displayed on this tab. If the number of alerts or exceptions is displayed for a check item, you can find the check item and click **Details** in the Actions column to troubleshoot the issues. If you have other questions, submit a ticket for technical support.

**Inspect the control service**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the **MaxCompute** page, click Operation and maintenance in the top navigation bar.
Click the **Service operation and maintenance** tab. Then, click **Control Services** in the left-side navigation pane.
4. On the **Overview** tab of the **Control Services** page, view the role information in the
**Service Status** section.
If a service role of the cluster is unavailable, submit a ticket for technical support.

**Inspect Job Scheduler**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the **MaxCompute** page, click Operation and maintenance in the top navigation bar.
Click the **Service operation and maintenance** tab. Then, click **Fuxi service** in the leftside navigation pane.
4. On the **Overview** tab of the **Fuxi service** page, view information in the **Service Status**
and **Resource Usage Trends** sections. Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: If the CPU utilization or memory usage reaches the upper limit for an extended period of time, we recommend that you submit tasks during off-peak hours. If the CPU utilization or memory usage still reaches the upper limit, submit a ticket for technical support.

**Inspect Apsara Distributed File System**

**View the status of a node, storage usage, and the number of**

**files for a cluster**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the **MaxCompute** page, click Operation and maintenance in the top navigation bar.
Click the **Service operation and maintenance** tab. Then, click **Pangu Service** in the left-side navigation pane.
4. On the **Overview** tab of the **Pangu Service** page, view the status of service roles in the
**Service Status** Section and the information about the selected cluster in the **Saturation-**
**storage level** section.
Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: If the storage usage or the number of files exceeds 80%, submit a ticket for technical support.

**Check the disk status of Apsara Distributed File System**

1. Log in to MaxCompute AG.
2. Run the following command to check the disk status of Apsara Distributed File System:

```
puadmin lscs|grep -vi NORMAL|grep -vi DISK_OK
```

If an error occurs, submit a ticket for technical support.

**Check the data integrity of Apsara Distributed File System**

1. Log in to MaxCompute AG.
2. Run the following commands to check the data integrity of Apsara Distributed File System:
Check whether files are lost.

```
puadmin fs -abnchunk -t none
```

Check whether data is being backed up.

```
puadmin fs -abnchunk -t onecopy
```

Check whether the number of replicas is less than the normal number.

```
puadmin fs -abnchunk -t lessmin
```

The following code shows a normal output. If data is returned, data loss occurs. In this case, submit a ticket for technical support.

```
Master Address: nuwa://localcluster/sys/pangu/master ChunkId Type FoundTime
```

**Inspect the tunnel service**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the **MaxCompute** page, click Operation and maintenance in the top navigation bar.
Click the **Service operation and maintenance** tab. Then, click **Channel Services** in the left-side navigation pane.
4. On the **Overview** tab of the **Channel Services** page, view the status of service roles in the
**Service Status** section and the throughput of the tunnel service in the **Channel Service**
**Throughput (B/min)** section.
Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: The traffic status of the selected cluster is displayed in the **Channel**
**Service Throughput (B/min)** section.

**Inspect Apsara Name Service and Distributed Lock**

**Synchronization System**

1. Log in to MaxCompute AG.
2. Run the following command to check the health status of Apsara Name Service and
Distributed Lock Synchronization System:

```
tj_show -r nuwa.NuwaZK#>/tmp/nuwa;pssh -h /tmp/nuwa -i "echo srvr| nc localhost 10240
| grep Mode"
```

The following code provides an example on a normal output. One leader and two followers are available. If no **leader** or **follower** is returned or an error message is returned, submit a ticket for technical support.

```
[1] 11:21:43 [SUCCESS] vm010230012204 Mode: leader [2] 11:21:43 [SUCCESS] vm010230009054 Mode: follower [3] 11:21:43 [SUCCESS] vm010230017122 Mode: follower
```

**Inspect a metadata warehouse**

1. Log in to MaxCompute AG.
2. Run the following command to switch to the admin user:

```
su admin
```

3. Check the logs of a metadata warehouse.

**Command format**

```
cat /apsara/meta/logs/<datetime>/meta.log
```

**datetime**: the directory that stores the logs that are generated on the specified date.

**Example**

Run the following command to query the logs of a metadata warehouse that are generated on April 24, 2022:

```
cat /apsara/meta/logs/20220424/meta.log
```

Check whether the returned results are consistent with the information that is marked in the following figure. If the returned results are inconsistent with the information in the following figure, run the `sh /apsara/meta/daliyrun.sh` command as the admin user to restart MaxCompute AG and check the logs again. If the issue persists, submit a ticket for technical support.

### MaxCompute risk inspection

If the number of chunks or the number of files in the volumes directory exceeds the upper limit, the cluster becomes unstable or even fails. This topic describes how to check risks that exist in MaxCompute clusters and how to handle the risks.

**Background information**

You can check risks that exist in a MaxCompute cluster from the following dimensions: Check the number of chunks Check the number of files in the volumes directory

**Check the number of chunks**

If the number of chunks exceeds the upper limit, the chunkserver service becomes unstable and data queries are slowed down. To check the number of chunks, perform the following steps:
1. Log in to MaxCompute AG.
2. Run the following command to check the number of chunks:

```
puadmin lscs|grep tcp
```

If the number of chunks exceeds 2 million, small files must be merged.

**Check the number of files in the volumes directory**

If the number of files in the volumes directory exceeds the upper limit, the files in the volumes directory may be damaged. To check the number of files in the volumes directory, perform the following steps:
1. Log in to MaxCompute AG.
2. Run the following command to check the number of files in the volumes directory:

```
pu ls -l /product/aliyun/odps/adsmr|grep -A4 volume
```

If the number of files in the volumes directory exceeds 5 million, a risk exists. If the number of files in the volumes directory exceeds 8 million, a high risk exists. In this case, you must submit a ticket and contact Apsara Stack engineers for technical support.

### Log in to MaxCompute AG

This topic describes how to log in to MaxCompute AG.

**Procedure**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. In the **Site Navigation** section, click **TIANJI**.
3. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**. In the left-side navigation pane, choose **Resource Management** >
**Machines**. Then, complete the steps in the following figure.

## Common issues and

**solutions**

### Query and allocate resources

**in a MaxCompute cluster**

This topic describes how to query and allocate the storage and computing resources in a MaxCompute cluster. This topic also introduces quota groups, the relationship between quota groups and MaxCompute projects, and how to create quota groups properly.

**Query the resources that can be allocated to projects in a**

**MaxCompute cluster**

**Storage resources**

The available storage resources in a MaxCompute cluster are limited and can be calculated based on the number of compute nodes in the cluster. The storage capacity of a MaxCompute cluster is managed by using Apsara Distributed File System. You can run the commands of Apsara Distributed File System to query the storage information, such as the storage usage. The following metrics are used to measure the storage resources of a cluster:
**Storage capacity**: the total size of files that can be stored in a cluster. You can calculate
the storage capacity of a cluster based on the following formula: Storage capacity = Number of machines × [Size of a single disk × (Number of disks on a single machine - 1)] × System security threshold × System compression ratio/Number of distributed replicas.
**System compression ratio**: Based on the compression ratio of standard TPC-H
test datasets, the ratio of data size before compression to data size after compression is 3 to 1. The ratio varies based on the actual data.
**Number of distributed replicas**: In most cases, the number of distributed
replicas is 3.
**System security threshold**: **The default value is 0.85 in the MaxCompute**
**system.** You can specify a custom security threshold based on your business
requirements. A value of 0.85 indicates that if more than 85% of the total storage capacity is used, the security level is low. You must scale out the system based on your business requirements or delete unnecessary data. View the storage capacity of a MaxCompute cluster Run the `puadmin lscs` command on Cluster AG. The total disk space, total free space, and total file size are displayed at the end of the command output. Figure 1: Storage capacity of a cluster Parameters:
**Total Disk Size**: the total physical storage space. Each file is stored
in three replicas. The logical space is one third of the physical space.
**Total Free Disk Size**: the available storage space, excluding the
storage space of recycle bins on chunk servers.
**Total File Size**: the physical space occupied by the files of Apsara
Distributed File System, including the files that are stored in the /deleted/ directory. Run the following command on Cluster AG to query the storage space used by all projects:

```
pu ls -l pangu://localcluster/product/aliyun/odps/
```

Example:

```
pu ls -l pangu://localcluster/product/aliyun/odps/|grep adsmr -A 4 -- Query the storage space that is used by a single project. In this example, the s torage usage of the adsmr project is queried.
```

Figure 2: Storage usage of a project Parameters:
**Length**: the logical length used by the project. The physical length
required is three times the logical length.
**FileNumber**: the number of files that are stored.
**DirNumber**: the number of directories that are created.
**File size**: the total number of files that can be stored in a cluster. This number depends on
the memory capacity of PanguMaster. A large number of small files or an improper number of files in a cluster will affect the stability of the cluster and its services. The index files of Apsara Distributed File System, including the information about Apsara Distributed File System files and directories, are stored in the memory of PanguMaster. Each file in the memory of PanguMaster corresponds to a file node. The memory of PanguMaster is occupied by file nodes, directories of all levels, and chunks. A large file is split into multiple chunks in Apsara Distributed File System. Therefore, the factors that affect the memory usage of PanguMaster include the number of files, directory hierarchy, and number of chunks. If the size of the original files in Apsara Distributed File System is large, the memory usage of PanguMaster is relatively low. In scenarios where a large number of small files are stored, Pangu Master occupies a large amount of memory. We recommend that you perform the following operations to optimize the memory usage of PanguMaster: Delete empty directories and reduce the number of directory levels. Do not manually create directories. A directory is automatically created when a file is created. Store multiple files in one directory. You can store up to 100,000 files in a directory. Decrease the length of file names and directory names to reduce the memory usage and network traffic in PanguMaster. Reduce the number of small tables and files. We recommend that you use the tunnel service to upload and commit MaxCompute tables only when the table size reaches `64` `MB` . The following table shows the maximum number of files supported by PanguMaster with different memory specifications.

| Memory | Maximum number of files supported |
|---|---|
| 48G | 87.5 million |
| 96G | 175 million |
| 128G | 233 million |

Query the number of files stored in a MaxCompute cluster Run the `pu quota` command on Cluster AG to query the total number of files that are stored in a MaxCompute cluster. Figure 3: Total number of files stored in a MaxCompute cluster Run the following command on Cluster AG to query the total number of files that are stored in a project of a MaxCompute cluster. In this example, the adsmr project is queried.

```
pu ls -l pangu://localcluster/product/aliyun/odps/|grep adsmr -A 4
```

Figure 4: Total number of files that are stored in a project of a MaxCompute cluster Parameters:
**FileNumber**: the number of files that are stored.
**DirNumber**: the number of directories that are created.
**FileNumber** + **DirNumber** = Total number of files stored in the
adsmr project.

**Computing resources**

Computing resources in a MaxCompute cluster typically refer to CPU and memory resources. Total computing resources = Number of CPU cores and memory size of a single compute node × Number of machines. The system on each machine occupies one CPU core. Therefore, if a machine has 56 CPU cores, 55 CPU cores are managed by the distributed scheduler and are scheduled to the services of MaxCompute. The remaining memory is allocated by Job Scheduler. Typically, for every CPU core, 4 GB of memory is allocated to a MaxCompute task. This ratio varies based on MaxCompute tasks. Query computing resources Run the `r ttrl` command on Cluster AG to query all computing resources of a cluster. Figure 5: Computing resources of a cluster The domain names of Tubo machines are displayed in the first column. The CPU cores of Tubo machines are displayed in the second column, and the unit is u. One CPU core equals 100 u. The memory size of Tubo machines is displayed in the third column, and the unit is MB. The tags that are added to Tubo machines in Job Scheduler are displayed in the fourth column. Run the `r tfrl` command on Cluster AG to query the remaining computing resources of a cluster. Figure 6: Remaining computing resources of a cluster The domain names of Tubo machines are displayed in the first column. The CPU cores of Tubo machines are displayed in the second column, and the unit is u. One CPU core equals 100 u. The memory size of Tubo machines is displayed in the third column, and the unit is MB. The tags that are added to Tubo machines in Job Scheduler are displayed in the fourth column. Run the `r cru` command on Cluster AG to query the resources used by the tasks running in MaxCompute. Figure 7: Resources used by running tasks The task names are displayed in the first column. The CPU cores that are used by tasks are displayed in the second column. The memory that is used by tasks is displayed in the third column. The number of Fuxi instances that are started by the corresponding role for tasks in Job Scheduler is displayed in the fourth column.

**Allocate resources to projects in a MaxCompute cluster**

**Allocate storage resources**

The storage capacity and the maximum number of files are configured when you create a project. You can modify the configurations in MaxCompute Admin Console. If the following error messages are returned, the occupied storage space or the number of files has exceeded the limit. In this case, you must organize the data in the project by deleting unnecessary tables or expanding the storage capacity. Figure 8: Error messages

**Important**

The sum of the storage usage of all projects cannot exceed the total storage capacity of a cluster. Similarly, the total number of files in all projects cannot exceed the total number of files supported by a cluster. Therefore, you must properly plan storage space and the maximum number of files for each project and make timely adjustments based on your business requirements.

**Allocate computing resources**

Computing resource allocation means planning quota groups. What is a quota group? MaxCompute clusters can be divided into different resource groups (quota groups). A quota group represents a certain amount of allocated CPU and memory resources and the scheduling policy of the quota group. You can specify the MinQuota and MaxQuota parameters to configure the CPU and memory resources of a quota group. MinQuota specifies the minimum amount of resources allocated to the quota group, and MaxQuota specifies the maximum amount of resources allocated to the quota group. For example, MinCPU=500 indicates that the quota group can allocate at least 5 (500/100) cores. MaxCPU=2000 indicates that the quota group can allocate at most 20 (2000/100) cores. By default, MaxCompute uses the fairness-aware integrated resource (FAIR) scheduling policy and the first-in-first-out (FIFO) scheduling policy. The difference between the FIFO and FAIR scheduling policies is the sort key of WaitingQueue. If each schedule unit has its own priority, both the FAIR and FIFO scheduling policies allocate resources to high-priority schedule units first. If all schedule units share the same priority, the FIFO scheduling policy sorts the schedule units based on the time when they are submitted. The schedule units that are submitted earlier have a higher priority. The FAIR scheduling policy sorts the schedule units based on the value of the slotNum parameter. A smaller value of the slotNum parameter specifies a higher priority. This way, the same resources are allocated to schedule units of the same priority. You can run the `r quota` command on Cluster AG to query the quota group settings. Run the following command on Cluster AG to create and modify a quota group based on your business requirements:

```
sh /apsara/deploy/rpc_wrapper/rpc.sh setquota -i $QUOTAID -a $QUOTANAME -t fair -s $m ax_cpu_quota $max_mem_quota -m $min_cpu_quota $min_mem_quota
```

If the **$QUOTAID** parameter is specified, the specified quota group is modified. If the $QUOTAID parameter is not specified, a quota group is created. Plan quota groups To plan quota groups properly, you must first understand the relationship between MaxCompute projects and quota groups. When you create a project, you must specify the quota group to which the project belongs. You can change the quota group after the project is created. The resources in a quota group can be used by the tasks of all projects belong to the quota group. Therefore, tasks sharing the same quota group may compete for resources during peak hours. For example, one or more large tasks ma occupy all resources in the quota group while other computing tasks have to wait. In the following figure, a great number of tasks are waiting for resources, whereas the remaining resources of the cluster remain idle. Figure 9: Tasks waiting for resources In this case, you can check the quota usage. The quota group is allocated 50 CPU cores and all allocated CPU cores are used. The tasks of projects that belong to the quota group must wait until the quota is available. The remaining resources of the cluster cannot be used by these tasks. Therefore, you must plan quota groups based on the following principles: Plan quota groups based on business scenarios to avoid resource contention in an oversized resource pool. You also need to avoid creating an excessive number of small-sized resource pools. Otherwise, the scheduling of large tasks may be restricted or a large task may occupy the entire quota group for a long period of time. Consider the MinQuota and MaxQuota parameters when you plan quota groups. You can overcommit the resources in your cluster. That is, the sum of the maximum quotas of all quota groups can be greater than the total amount of cluster resources. However, the overcommitment ratio cannot be too large. Take the following factors into consideration when you plan quota groups: the priorities of tasks, task duration, amount of task data, and characteristics of computing tasks. Configure quota groups properly for peak hours. We recommend that you configure a separate quota group for tasks that are important and time-consuming. Planning quota groups and selecting quota groups for projects is a resource pre-allocation strategy. You also need to adjust your resource allocation in a timely manner based on the actual resource demands.

### Work with IPv4/IPv6 dual

**stack**

This topic describes how to work with the IPv4/IPv6 dual stack feature of MaxCompute.

**Usage notes**

MaxCompute supports IPv4 by default. To use the IPv4/IPv6 dual stack feature, contact
**Apsara Stack technical support** to perform the following operations:
1. Complete transformation to support IPv6 on the platform side.
2. Enable IPv6 for MaxCompute. For more information, see **Network changes > Feature**
**orchestration > IPv6 dashboard** in **VPC O&M Guide**.
We recommend that you also enable PPv2 when enabling IPv6 in case the blacklist and whitelist do not take effect. For more information, see the Account usage management section of the Usage notes topic.

### Troubleshoot common issues

**and data skew issues**

**Scenario 1: how to determine whether a job has stopped**

**running due to insufficient resources**

**Symptom**

The job does not progress as expected.

**Cause**

Typically, the job runs out of resources. You can use LogView to determine the status of job resources (task instance status).
**Ready**: indicates that instances are waiting for Job Scheduler to allocate resources.
Instances can resume after the required resources are allocated.
**Wait**: indicates that instances are waiting for dependent tasks to complete.
The task instances in the Ready state shown in the following figure indicate that there are insufficient resources to run these tasks. After an instance obtains the required resources, its status changes to **Running**.

**Solution**

If the task instances run out of resources during peak hours, you can run the tasks during off-peak hours. If the computing quotas are insufficient, check whether the quota group of the project has sufficient computing resources. If computing resources in the cluster are occupied for a long period of time, you can formulate a computing quota allocation strategy to increase the quota limit. We recommend that you do not run excessively large jobs to prevent the jobs from occupying resources for an extended period of time. You can enable SQL acceleration. This allows you to run small jobs without requesting resources from Job Scheduler. You can also use the First-In First-Out (FIFO) scheduling policy.

**Scenario 2: how to find the root cause of a job that has been**

**running for an extended period of time**

**Symptom**

Symptom: The MaxCompute job execution progress has remained at 99% for a long period of time.

**Cause**

1. **Preliminary analysis.**
Cause: The uptime of some Fuxi instances in the MaxCompute job is significantly longer than that of other Fuxi instances.
2. **Further analysis.**
Analyze the job summary in LogView, and calculate the difference between the max and avg values of input and output records of a slow task. If the max and avg values differ by several orders of magnitude, it can be determined that the job data is skewed.

**Solution**

If there are slow Fuxi instances on a particular machine, check whether a hardware fault has occurred on the machine.

**Scenario 3: how to improve the concurrency of MaxCompute**

**jobs**

**Fault locating**

The concurrency of Map tasks depends on the following factors: Split size and merge limit. Map takes a series of data files as input. Larger files are divided into chunks based on the odps.sql.mapper.split.size value, which is 256 MB by default. An instance is started for each chunk. However, starting an instance requires resources and time. Small files can be merged into a single chunk based on the odps.sql.mapper.merge.limit.size value and processed by a single instance to improve instance utilization. The default value of odps.sql.mapper.merge.limit.size is 64 MB. The total size of small files merged cannot exceed this value. Instances cannot process data across chunks. A chunk is mapped to a folder in Apsara Distributed File System. You must run at least one instance to process data in a chunk. Instances cannot process data across chunks. In a chunk, you must run instances by following the preceding rule. Typically, the number of instances for Reduce tasks is 1/4 of that for Map tasks. The number of instances for Join tasks is the same as that for Map tasks, but cannot exceed 1,111. You can use the following methods to increase the number of concurrent instances for Reduce and Join tasks:

```
set odps.sql.reducer.instances = xxx set odps.sql.joiner.instances = xxx
```

**Scenarios that require higher concurrency**

A single record contains only a small amount of data. When a single record contains a small amount of data, the number of records in a file of the same size increases. If you divide data into 256-MB chunks, a single Map instance needs to process a large number of records, which compromises the concurrency. Dump operations occur in the Map, Reduce, and Join stages. Based on the preceding job summary analysis, the displayed dump information indicates that the instance does not have sufficient memory to sort data in the Shuffle stage. Improving concurrency can reduce the amount of data processed by a single instance to the amount of data that can be handled by the memory, eliminate disk I/O time consumption, and improve the processing efficiency. Time-consuming UDFs are used. The execution of UDFs is time-consuming. If you execute UDFs concurrently, you can reduce the UDF execution time of an instance.

**Solution**

You can decrease the following parameter values to improve the concurrency of Map tasks:

```
odps.sql.mapper.split.size = xxx odps.sql.mapper.merge.limit.size = xxx
```

You can increase the following parameter values to improve the concurrency of Reduce and Join tasks:

```
odps.sql.reducer.instances = xxx odps.sql.joiner.instances = xxx
```

Take note that improving concurrency will increase resource consumption. We recommend that you take the cost into consideration when improving concurrency. An instance takes an average of 10 minutes to complete after optimization, which improves the overall resource utilization. We recommend that you optimize jobs in key pipelines so that they will require less time.

**Scenario 4: how to resolve data skew issues**

Different types of data skew issues in SQL are resolved by using different methods.

| Data skew type | Cause and solution |
|---|---|
| GROUP BY | The uneven distribution of GROUP BY keys results in data skew on reducers. You can set the anti-skew parameter before executing SQL tasks. set odps.sql.groupby.skewindata=true After this parameter is set to true, the system automatically adds a random number to each key when running the Shuffle hash algorithm and prevents data skew by introducing a new task. |
| DISTRIBU TE BY | Using constants to execute the DISTRIBUTE BY clause for full table sorting will result in data skew on reducers. We recommend that you do not perform this operation. |

| JOIN | Data is skewed in the Join stage when the Join keys are unevenly distributed. For example, a key exists in multiple joined tables, resulting in a Cartesian explosion of data in the Join instance. You can use one of the following solutions to resolve data skew issues in the Join stage: When a large table and a small table are joined, use MapJoin instead of Join to optimize query performance. Use a separate logic to handle a skewed key. For example, when a large number of null values exist in the key, you can filter out the null values or execute a CASE WHEN statement to replace them with random values before the Join operation. If you do not want to modify SQL statements, configure the following parameters to allow MaxCompute to perform automatic optimization: set odps.sql.skewinfo=tab1:(col1,col2)[(v1,v2),(v3,v4),...] set odps.sql.skewjoin=true; |   |
|---|---|---|
| MULTI- DISTINCT | The multi-distinct syntax aggravates GROUP BY data skew. You can use the GROUP BY clause with the COUNT function instead of multi-distinct to alleviate the data skew issue. |   |
|   | Some jobs report an OOM error during runtime. The error message is as follows: FAILED: ODPS-0123144: Fuxi job failed - WorkerRestart errCode:9,errMsg:SigKill(OOM), usually caused by OOM(out of memory) . You can fix the error by configuring the UDF runtime parameters. Example: odps.sql.mapper.memory=3072; set odps.sql.udf.jvm.memory=2048; set odps.sql.udf.python.memory=1536; |   |
|   |   | FAILED: ODPS-0123144: Fuxi job failed - WorkerRestart |
|   | errCode:9,errMsg:SigKill(OOM), usually caused by OOM(out of memory) |   |
| UDF OOM |   |   |

**Examples**

The following table describes the related data skew settings.

| Statement | Description |
|---|---|
| set odps.sql.groupby.skewindata=true/fals e | Enable GROUP BY optimization. |
| set odps.sql.skewjoin=true/false | Allows you to enable Join optimization. It is effective only when odps.sql.skewinfo is set. |

| set odps.sql.skewinfo | Allows you to set detailed information for Join optimization. The syntax is as follows: set odps.sql.skewinfo=skewed src: _ (skewed key)[("skewed value")] _ _ src a join src skewjoin1 b on a.key = _ b.key; Example: set odps.sql.skewinfo=src skewjoin1:(key) _ [("0")] -- The output result for a single skewed value of a single field is as follows: explain select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src skewjoin1 b on a.key = b.key; _ set odps.sql.skewinfo=src skewjoin1:(key) _ [("0")("1")] -- The output result for multiple skewed values of a single field is as follows: explain select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src skewjoin1 b on a.key = b.key; _ |
|---|---|

**Scenario 5: how to configure common SQL parameters**

| Type | Statement | Description |
|---|---|---|
| Map settin gs | set odps.sql.mapper.cpu=100 | Specifies the number of CPUs used by each instance in a Map task. Default value: 100. Valid values: 50 to 800. |
|   | set odps.sql.mapper.memory=10 24 | Specifies the memory size of each instance in a Map task. Unit: MB. Default value: 1024. Valid values: 256 to 12288. |
|   | set odps.sql.mapper.merge.lim it.size=64 | Specifies the maximum size of control files to be merged. Unit: MB. Default value: 64. You can set this variable to control the input of mappers. Valid values: 0 to Integer.MAX VALUE. _ |
| 57 | > Document Version: 2026082 |   |

|   | set odps.sql.mapper.split.siz e=256 | Specifies the maximum input volume for a Map task. Unit: MB. Default value: 256. You can set this variable to control the input of mappers. Valid values: 1 to Integer.MAX VALUE. _ |
|---|---|---|
| Join settin gs | set odps.sql.joiner.instances =-1 | Specifies the number of instances in a Join task. Default value: -1. Valid values: 0 to 2000. |
|   | set odps.sql.joiner.cpu=100 | Specifies the number of CPUs used by each instance in a Join task. Default value: 100. Valid values: 50 to 800. |
|   | set odps.sql.joiner.memory=10 24 | Specifies the memory size of each instance in a Join task. Unit: MB. Default value: 1024. Valid values: 256 to 12288. |
| Reduc e settin gs | set odps.sql.reducer.instance s=-1 | Specifies the number of instances in a Reduce task. Default value: -1. Valid values: 0 to 2000. |
|   | set odps.sql.reducer.cpu=100 | Specifies the number of CPUs used by each instance in a Reduce task. Default value: 100. Valid values: 50 to 800. |
|   | set odps.sql.reducer.memory=1 024 | Specifies the memory size of each instance in a Reduce task. Unit: MB. Default value: 1024. Valid values: 256 to 12288. |
|   | set odps.sql.udf.jvm.memory=1 024 | Specifies the maximum memory size that can be used for the JVM heap of a UDF. Default value: 1024. Unit: MB. Valid values: 256 to 12288. |
|   | set odps.sql.udf.timeout=600 | Specifies the timeout period of a UDF. Unit: seconds. Default value: 600. Valid values: 0 to 3600. |

|   | set odps.sql.udf.python.memor y=256 | Specifies the maximum memory size used by the UDF Python API. Unit: MB. Default value: 256. Valid values: 64 to 3072. |
|---|---|---|
| UDF Settin gs |   |   |
|   | set odps.sql.udf.optimize.reu se=true/false | When this parameter is set to true, each UDF expression can only be calculated once. This improves the performance. Default value: true. |
|   | set odps.sql.udf.strict.mode= false/true | Specifies whether functions return NULL or an error if dirty data is found. If the parameter is set to true, an error is returned. If the parameter is set to false, NULL is returned. |
| MapJo in settin gs | set odps.sql.mapjoin.memory.m ax=512 | Specifies the maximum memory size for a small table in a MapJoin task. Unit: MB. Default value: 512. Valid values: 128 to 2048. |
|   | set odps.sql.reshuffle.dynami cpt=true/false | Dynamic partitioning is time-consuming in some scenarios. Disabling dynamic partitioning can accelerate SQL execution. If the number of dynamic partitions is small, disabling dynamic partitioning can prevent data skew. |

**Scenario 6: how to check the storage usage of a single project**

Launch the MaxCompute console as a project owner and run the `desc project` <project_name>-extended; command to view the following information. The preceding figure shows the capacity-related storage information of the project. The relationship between the physical and logical values of the related metrics is: Physical value of a metric = Logical value of the metric x Number of replicas.
