---
title: "Alibaba Cloud Apsara Stack V3.18.3 MaxCompute Operations and Maintenance Guide 20250126"
product_version: "V3.18.3"
doc_version: "20250126"
pdf_pages: 158
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 MaxCompute Operations and Maintenance Guide 20250126.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AE%A1%E7%AE%97%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20MaxCompute%20Operations%20and%20Maintenance%20Guide%2020250126.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 MaxCompute Operations and Maintenance Guide 20250126

## Table of Contents

- 1 Concepts and architecture
- 2 O&M commands and tools
  - 2.1 Before you start
  - 2.2 odpscmd commands
  - 2.3 Tunnel commands
  - 2.4 LogView tool
    - 2.4.1 Usage notes
    - 2.4.2 Overview
    - 2.4.3 Preliminary knowledge of LogView
    - 2.4.4 Use LogView
  - 2.5 Apsara Big Data Manager
- 3 Routine O&M
  - 3.1 Manage service configurations
  - 3.2 Perform routine inspections
  - 3.3 Shut down a chunk server for maintenance and clone the chunk server
  - 3.4 Shut down a chunk server for maintenance without compromising the system
  - 3.5 Adjust the virtual resources of Apsara Distributed Operating System in MaxCompute
  - 3.6 Restart MaxCompute services
- 4 Common issues and solutions
  - 4.1 Query and allocate resources in a MaxCompute cluster
  - 4.2 Common issues and data skew troubleshooting
- 5 MaxCompute O&M
  - 5.1 Log on to the ABM console
  - 5.2 Business O&M
    - 5.2.1 O&M overview and entry
    - 5.2.2 Project management
      - 5.2.2.1 Manage projects
      - 5.2.2.2 View project details
      - 5.2.2.3 Encrypt data
      - 5.2.2.4 Grant access permissions on the metadata warehouse
      - 5.2.2.5 Perform disaster recovery
      - 5.2.2.6 Migrate projects
    - 5.2.3 Manage quota groups
    - 5.2.4 Job management
      - 5.2.4.1 Manage job snapshots
    - 5.2.5 Business optimization
      - 5.2.5.1 Merge small files
      - 5.2.5.2 Compress idle files
      - 5.2.5.3 Analyze resources
  - 5.3 Service O&M
    - 5.3.1 Control service O&M
      - 5.3.1.1 O&M features and page
      - 5.3.1.2 Overview
      - 5.3.1.3 Control server roles
      - 5.3.1.4 Control service configuration
      - 5.3.1.5 Metadata warehouse for the control service
      - 5.3.1.6 Stop or start a service role
      - 5.3.1.7 Start AdminConsole
      - 5.3.1.8 Collect service logs
    - 5.3.2 Job Scheduler O&M
      - 5.3.2.1 O&M features and page
      - 5.3.2.2 Overview
      - 5.3.2.3 Manage service roles
      - 5.3.2.4 Job Scheduler compute nodes
      - 5.3.2.5 Enable and disable SQL acceleration
      - 5.3.2.6 Restart a master node of Job Scheduler
    - 5.3.3 Apsara Distribute File System O&M
      - 5.3.3.1 O&M features and page
      - 5.3.3.2 Overview
      - 5.3.3.3 Manage service roles
      - 5.3.3.4 Apsara Distributed File System storage
      - 5.3.3.5 Change the primary master node of Apsara Distributed File System
      - 5.3.3.6 Clear the recycle bin of Apsara Distributed File System
      - 5.3.3.7 Enable or disable data rebalancing for Apsara Distributed File System
      - 5.3.3.8 Run a checkpoint on a master node of Apsara Distributed File System
    - 5.3.4 Tunnel service
      - 5.3.4.1 O&M features and page
      - 5.3.4.2 Overview
      - 5.3.4.3 Manage service roles
      - 5.3.4.4 Traffic analysis
      - 5.3.4.5 Manage configurations
      - 5.3.4.6 Restart tunnel servers
  - 5.4 Cluster O&M
    - 5.4.1 O&M features and entry
    - 5.4.2 Manage cluster health checks
    - 5.4.3 Overview
    - 5.4.4 Servers
    - 5.4.5 Scale in and scale out a MaxCompute cluster
    - 5.4.6 Restore environment settings
  - 5.5 Host O&M
    - 5.5.1 O&M features and page
    - 5.5.2 Overview
    - 5.5.3 Manage host services
  - 5.6 Deep inspection
    - 5.6.1 Overview
    - 5.6.2 Inspect clusters
    - 5.6.3 MaxCompute risk inspection
    - 5.6.4 Log on to MaxCompute AG

## 1 Concepts and architecture

The following figure shows the architecture of MaxCompute. The architecture and descriptions are for reference only. The actual service that is released and the features that are updated prevail. Figure 1: MaxCompute architecture indicates the basic features of MaxCompute. indicates the enhanced features of MaxCompute. indicates the features that are provided by external systems.

| Category | Description |
|---|---|

| Peripheral platforms | MaxCompute supports the following peripheral platforms: Apsara Uni-manager Management Console: a unified and intelligent O&M platform. For more information, see Apsara Uni- manager Management Console User Guide. DataWorks: a visualization tool. You can use DataWorks to perform common operations, such as synchronizing data, scheduling jobs, and generating reports. For more information, see DataWorks Technical White Paper. Apsara Big Data Manager (ABM): provides an easy method for field engineers to manage MaxCompute. For more information, see Apsara Big Data Manager Technical White Paper. Platform for AI (PAI): a machine learning algorithm platform based on MaxCompute. For more information, see Platform for AI Technical White Paper. Second-party applications: other Alibaba Cloud services supported by MaxCompute, such as DataV. Three-party applications: other services that are compatible with MaxCompute. |
|---|---|
| Tools | MaxCompute supports the following tools: Tunnel: a tunnel service. MaxCompute allows you to import heterogeneous data into or export the data from MaxCompute by using Tunnel. For more information, see the Tunnel section in Technical White Paper. MaxCompute Migration Assist (MMA): the data migration tool of MaxCompute. If you use MMA, Meta Carrier is used to access your Hive metastore service and capture Hive metadata. Then, MMA uses the Hive metadata to generate data definition language (DDL) statements and SQL statements of Hive user- defined table-valued functions (UDTFs). The DDL statements are used to create MaxCompute tables and their partitions. The SQL statements of Hive UDTFs are used to migrate data. Hybrid backup recovery (HBR): integrates data backup and migration capabilities of Apsara Stack. odpscmd: the MaxCompute client. For more information, see the "Client" section in MaxCompute User Guide. MaxCompute Studio: the big data integrated development environment tool that is provided by MaxCompute. MaxCompute Studio is installed on a developer client. It is a development plug-in that Alibaba Cloud provides for the popular integrated development environment (IDE) IntelliJ IDEA. DataWorks DataStudio: a visualized development platform provided by DataWorks. For more information, see DataWorks User Guide. |

| User interfaces | MaxCompute supports the following interfaces: Interactive languages: CLI, SQL, Python, Java, and Scala. SDKs and APIs: SDK for Java, SDK for Python, and Java Database Connectivity (JDBC). For more information, see MaxCompute Developer Guide. |
|---|---|
| SQL computing capabilities | MaxCompute supports the following SQL computing capabilities: Enhanced capabilities: support LOAD, parameterized view, lifecycle management, and CLONE TABLE. User-defined functions (UDFs): include SQL UDFs, Java UDFs, and Python UDFs. Query: the query operations, such as SELECT and EXPLAIN statements and built-in functions. Data manipulation language (DML) statements: include INSERT, UPDATE, and DELETE. DDL statements: allow you to create internal tables, external tables, clustered tables, and partitioned tables. Basic capabilities: support multiple data types and data formats and allow you to upload resource files. For more information, see the "MaxCompute SQL" section in MaxCompute User Guide. |
| Computing models | MaxCompute supports the following computing models: Mars: a tensor-based unified distributed computing framework. Mars allows you to use parallel and distributed computing technologies to accelerate data processing for Python data science stacks. For more information, see the "Mars" section in MaxCompute User Guide. Spark on MaxCompute: a solution developed by Alibaba Cloud to enable the seamless use of Spark on the MaxCompute platform. It supplements a wide range of features to MaxCompute. For more information, see the "Spark on MaxCompute" section in MaxCompute User Guide. MapReduce on MaxCompute: allows you to run MapReduce jobs on MaxCompute. For more information, see MaxCompute MapReduce in MaxCompute User Guide. VVP on MaxCompute: encapsulates the features of Realtime Compute for Apache Flink that is developed on the Ververica Platform (VVP) based on MaxCompute resources. You can use the Cupid joint computing platform to complete the operations related to real-time computing by using the underlying storage and computing resources of MaxCompute on the VVP UI. For more information, see the "VVP On MaxCompute" section in MaxCompute User Guide. Graph: a processing framework designed for iterative graph computing. For more information, see the "MaxCompute Graph" section in MaxCompute User Guide. |

| Management | MaxCompute can be managed from the following aspects: Cost: measures resource usage. Job: provides mechanisms to manage jobs. For example, you can use these mechanisms to schedule jobs, use LogView to view job information, and set job priorities. Engine resource: supports high-performance MaxCompute Query Acceleration (MCQA). Large scale: allows you to deploy MaxCompute clusters across regions. Lakehouse: a data management platform that combines data lakes and data warehouses. It integrates the flexibility and broad ecosystem support of data lakes with the enterprise-class deployment of data warehouses. For more information, see MaxCompute Operations and Maintenance Guide. |
|---|---|
| Compliance governance | MaxCompute allows you to use the following methods for compliance governance: Security management: allows you to control the permissions of users and roles, and supports multiple access control methods, such as ACL-based access control, policy-based access control, and column-level access control. Unified intelligent metadata service: stores metadata in a unified manner. Log audit: audits different log data of different users. Backup and restoration: allows you to back up and restore data from a storage system. Dynamic data masking: allows you to query data masking rules in DataWorks. Data quality: DataWorks provides an end-to-end platform that supports quality check, notification, and management services for various heterogeneous data sources. Content moderation audit: uses the content moderation engine to identify and audit security-sensitive content. For more information about security, see MaxCompute Security White Paper. |
| Data storage | MaxCompute stores data as tables or volumes. |

The following figure shows how a MaxCompute job is run. Figure 2: Run a MaxCompute job The following concepts are involved in the procedure for running a MaxCompute job:
1. MaxCompute instance: the instance of a MaxCompute job. A job is anonymous if it is not
defined. A MaxCompute job can contain multiple MaxCompute tasks. In a MaxCompute instance, you can submit multiple SQL or MapReduce tasks, and specify whether to run the tasks in parallel or in sequence. This is rarely implemented because MaxCompute jobs are not commonly used. In most cases, an instance contains only one task.
2. MaxCompute task: a specific task in MaxCompute. Almost 20 task types, such as SQL,
MapReduce, Admin, Lot, and Xlib, are supported. The logic of tasks varies based on the task type. Different tasks in an instance are differentiated by task name. MaxCompute tasks are run on control clusters. Simple tasks, such as metadata modification, can be run in control clusters for their entire lifecycles. To run computing tasks, you must submit Fuxi jobs to compute clusters.
3. Fuxi job: a computing model provided by the Job Scheduler module. A Fuxi job indicates a
task that can be complete. A Fuxi service indicates a resident process. The directed acyclic graph (DAG) scheduling approach can be used to schedule Fuxi jobs. Each job has a job master that schedules its job resources. For the SQL task type, Fuxi jobs are divided into offline and online jobs. Online jobs evolve from the jobs in service mode. An online job is also called a quasi-real-time task. An online job is a resident process that can be run when tasks are available. This reduces the amount of time required to start or stop a job. You can submit a MaxCompute task to multiple compute clusters. The primary key name of a Fuxi job is the combination of the cluster name and job name. The JSON plan for Job Scheduler to submit a job and the status of a finished job are stored in Apsara Distributed File System.
4. Fuxi task: a task in a Fuxi job. Different Fuxi tasks represent different logics. Fuxi tasks can
be linked together as pipes to implement complex logic.
5. Fuxi instance: the instance of a Fuxi task. A Fuxi instance is the smallest unit that can be
scheduled by Job Scheduler. A task that is being run is divided into many logical units to improve the processing speed. Different instances of a task are run based on the same logic but process different input data and generate different output data.
6. Fuxi worker: an underlying concept of Job Scheduler. A worker represents an operating
system process. A worker can be reused by multiple Fuxi instances, but a worker can process only one instance at a time.

> **Note:** Instance ID: the unique identifier of a MaxCompute job. It is commonly used for troubleshooting. You can construct the LogView component for the current instance based on the project name and instance ID.
> Service master or job master: a master node of the service or job type. A service master or job master is responsible for requesting and scheduling resources, creating work plans for workers, and monitoring workers across their entire lifecycles.

The storage and computing layer of MaxCompute is a core component of the cloud computing platform developed by Alibaba Cloud. As the kernel of Apsara Distributed Operating System, this component runs on compute clusters that are independent of control clusters. In the preceding architecture, major modules in the kernel of Apsara Distributed Operating System are displayed.

## 2 O&M commands and tools

### 2.1 Before you start

Before using MaxCompute O&M commands and tools, you must be aware of the following information: During the MaxCompute O&M process, the default account is admin. You must run all commands as an admin user. You must use your admin account and sudo to run commands that require sudo privileges.

### 2.2 odpscmd commands

You can use the CLI to perform O&M operations. Before you run commands on the CLI, you must log on to the CLI by performing the following steps:
1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter **odps-service-computer** in the search box and click the name of the service that is displayed.
3. On the details page of the **odps-service-computer** service, click **ComputerInit#** in the
Components pane. On the Instances tab, find the instance that you want to manage and click **Terminal** in the **Actions** column. On the page that appears, run commands to perform O&M operations.

**Console command directories and configurations**

The MaxCompute client is stored in the clt folder in the /apsara/odps_tools directory of MaxCompute AG. The client configuration file is stored in the conf directory in the clt folder. By default, the access_id, access_key, end_point, log_view, and tunnel_point parameters are configured. You can run the `./clt/bin/odpscmd` command to view information such as the version number in interactive mode. For example, you can run the `HTTP GET` /projects/admin_task_project/system; command to check the version information of MaxCompute.

**Client command parameters**

The following figure shows the client command parameters. Figure 4: Client command parameters
**-e**: The client does not execute SQL statements in interactive mode.
**--project, -u, and -p** : The client preferentially uses the specified user, pass, and project
parameters instead of the values of the parameters that are configured in the conf file. For parameters that are not specified, the values of the parameters that are configured in the conf file are used.
**-k and -f** : The client directly executes local SQL files.
**--instance-priority**: the priority for the task. Valid values: 0 to 9. A smaller value specifies
a higher priority. Default value: 9.
**-r**: the number of times that a failed command can be retried. This parameter is commonly
used in script jobs.

**Commonly used SQL commands for O&M**

The following table describes the commonly used commands. Table 1: Commonly used commands

| Command | Description |
|---|---|
| whoami | Queries your Apsara Stack tenant account and endpoint information. |
| show p | Queries the information about all instances that have been run. |
| wait <instanceid> | Displays the LogView and Fuxi job information of a task again. To run this command, you must have the owner permissions, and the LogView and Fuxi job information must be stored in the same project. |
| kill <instanceid> | Terminates an instance. |
| tunnel upload/download | Tests whether the tunnel is available. This parameter is used for troubleshooting. |
| desc project <projectname> -extended | Queries the information about a project. desc extended table: queries the information about tables. desc table name partition(pt spec): queries the _ _ information about partitions. desc resource $resource name: queries the _ information about project resources. desc project $project name -extended: queries the _ information about clusters. |
| export <project name>< local file path> _ _ | Exports the DDL statements of all tables in a project. |
| create table <tablename> (...) | Creates a table. |

| select count(*) from <tablename> | Queries a table. |
|---|---|
| Explain | Creates plans without the need to submit Fuxi jobs. You can use this command to view resources required for tasks. |
| list | Queries the information about tables, resources, and roles. |
| show | Queries the information about tables and partitions. |
| purge | Removes all data from the recycle bin of MaxCompute to the recycle bin of Apsara Distributed File System. purge table <tablename>: removes data from a single table. purge all: removes data from all tables in the current project. |

### 2.3 Tunnel commands

You can use Tunnel commands provided by the MaxCompute client to implement the original features of the Dship tool. Tunnel commands are mainly used to upload or download data. Table 1 Tunnel commands

| Parameter | Description |
|---|---|
| Tunnel Upload | Allows you to upload data to a MaxCompute table. You can upload files or level-1 directories. You can upload data to only one table or only one partition in a table each time. For a partitioned table, you must specify the partition to which you want to upload data. For a multi-level partitioned table, you must specify the lowest-level partition. |
| Tunnel Download | Allows you to download data from a MaxCompute table. You can only download data to a single file. You can download data from only one table or partition to a single local file each time. For a partitioned table, you must specify the partition from which you want to download data. For a multi-level partitioned table, you must specify the lowest-level partition. |
| Tunnel Resume | Allows you to resume data uploads. If an error occurs due to network interruption or Tunnel service faults, you can resume file or directory transmission after the interruption. You can use this command to resume only data uploads. Each data upload or download operation is called a session. To resume a session, you must specify the session ID in the Resume command. |
| Tunnel Show | Displays historical records. |
| Tunnel Purge | Clears the session directory. Logs from the last three days are cleared by default. |

Tunnel commands allow you to obtain help information by using the Help subcommand on the client. This section describes how to use the subcommand for each command.

**Upload**

Upload data in the local data file to a MaxCompute table. Sample commands:

```
odps@ project_name>tunnel help upload; usage: tunnel upload [options] <path> <[project.]table[/partition]>
              upload data from local file
 -acp,-auto-create-partition <ARG>   auto create target partition if not
                                     exists, default false
 -bs,-block-size <ARG>               block size in MiB, default 100
 -c,-charset <ARG>                   specify file charset, default ignore.
                                     set ignore to download raw data
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
 -rd,-record-delimiter <ARG>         specify record delimiter, support
                                     unicode, eg \u0001. default "\r\n"
 -s,-scan <ARG>                      specify scan file
                                     action(true|false|only), default true
 -sd,-session-dir <ARG>              set session dir, default
                                     D:\software\odpscmd_public\plugins\ds
                                     hip
 -ss,-strict-schema <ARG>            specify strict schema mode. If false,
                                     extra data will be abandoned and
                                     insufficient field will be filled
                                     with null. Default true
 -te,-tunnel_endpoint <ARG>          tunnel endpoint
    -threads <ARG>                   number of threads, default 1
 -tz,-time-zone <ARG>                time zone, default local timezone:
                                     Asia/Shanghai
Example:
    tunnel upload log.txt test_project.test_table/p1="b1",p2="b2"
```

**Parameters**:
-acp: the partition to which you want to upload data. If the specified partition does not exist, a partition is automatically created. By default, partitions are not created. -bs: the size of the data block uploaded by Tunnel each time. Default value: 100 MiB (1 MiB = 1024 × 1024 bytes). -c: the encoding format of the data file. Default value: UTF-8. By default, if this parameter is not configured, raw data is downloaded. -cp: specifies whether to compress the local data file before you upload the data to MaxCompute to reduce network traffic. By default, the local data file is compressed. -dbr: specifies whether to ignore dirty data, such as additional columns, missing columns, or unmatched types of column data. If you set this parameter to true, all data that does not match the definition of the table is ignored. If you set this parameter to false, an error is returned after dirty data is detected. This ensures that raw data in the table to which you want to upload data is not contaminated. -dfp: the format of DATETIME data. Default value: yyyy-MM-dd HH:mm:ss. -fd: the column delimiter used in the local data file. By default, commas (,) are used as column delimiters. -h: specifies whether the data file that you want to upload has a table header. If this parameter is set to true, the data file can contain a table header. In this case, Dship skips the table header and uploads data from the second row. -mbr: specifies the maximum number of allowed dirty data records. If the number of dirty data records exceeds 1,000, the upload stops. Default value: 1000. -ni: the NULL data identifier. Default value: an empty string (""). -rd: the row delimiter used in the local data file. Default value: \r\n. -s: specifies whether to scan the local data file. Default value: false. true: The system scans the data and starts to import the data only if the data is in the correct format. false: The system does not scan the data before the system imports the data. only: The system only scans the data but does not import the data. -sd: the session directory. -te: the Tunnel endpoint. -threads: the number of threads. Default value: 1. -tz: the time zone. Default value: local time zone, such as, Asia/Shanghai.

**Show**

Displays historical records. Sample commands:

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

Resumes the execution of historical operations. Only data uploads can be resumed. Sample commands:

```
odps@ project_name>tunnel help resume; usage: tunnel resume [session_id] [-force]
              resume an upload session
 -f,-force   force resume
Example:
    tunnel resume
```

**Download**

Downloads data from a MaxCompute table. Sample commands:

```
odps@ project_name>tunnel help download; usage: tunnel download [options] <[project.]table[/partition]> <path>
              download data to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
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
                                   unicode, eg \u0001. default "\r\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   D:\software\odpscmd_public\plugins\dshi
```

`p`

```
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
    -threads <ARG>                 number of threads, default 1
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Shanghai
usage: tunnel download [options] instance://<[project/]instance_id> <path>
              download instance result to local file
 -c,-charset <ARG>                 specify file charset, default ignore.
                                   set ignore to download raw data
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
```

```
                                   default false
    -limit <ARG>                   specify the number of records to
                                   download
 -ni,-null-indicator <ARG>         specify null indicator string, default
                                   ""(empty string)
 -rd,-record-delimiter <ARG>       specify record delimiter, support
                                   unicode, eg \u0001. default "\r\n"
 -sd,-session-dir <ARG>            set session dir, default
                                   D:\software\odpscmd_public\plugins\dshi
```

`p`

```
 -te,-tunnel_endpoint <ARG>        tunnel endpoint
    -threads <ARG>                 number of threads, default 1
 -tz,-time-zone <ARG>              time zone, default local timezone:
                                   Asia/Shanghai
Example:
    tunnel download test_project.test_table/p1="b1",p2="b2" log.txt
    tunnel download instance://test_project/test_instance log.txt
```

**Parameters**:
-c: the encoding format of the data file. Default value: UTF-8. -ci: the indexes of the columns whose data you want to download. The column indexes start from 0. Separate column indexes with commas (,). -cn: the names of the columns whose data you want to download. Separate column names with commas (,). -cp and -compress: specifies whether to compress the local file before you download the file to reduce network traffic. By default, the local file is compressed. -dfp: the format of DATETIME data. Default value: yyyy-MM-dd HH:mm:ss. -e: specifies whether to represent data of the DOUBLE type that you want to download by using an exponential function. If the data is not represented by an exponential function, retain a maximum of 20 digits. -fd: the column delimiter used in the local data file. By default, commas (,) are used as column delimiters. -h: specifies whether the data file has a table header. If you set this parameter to true, the data file has a table header. In this case, Dship skips the table header and uploads data from the second row.

> **Note:** `-h=true` and `threads>1` cannot be used together.

-limit: the number of rows that you want to download. -ni: the NULL data identifier. Default value: an empty string (""). -rd: the row delimiter used in the local data file. Default value: \r\n. -sd: the session directory. -te: the Tunnel endpoint. -threads: the number of threads. Default value: 1. -tz: the time zone. Default value: local time zone, such as, Asia/Shanghai.

**Purge**

Clears the session directory. Sessions within the last three days are cleared by default. Sample commands:

```
odps@ project_name>tunnel help purge; usage: tunnel purge [n]
              force session history to be purged.([n] days before, default
              3 days)
Example:
    tunnel purge 5
```

### 2.4 LogView tool

#### 2.4.1 Usage notes

Before you use LogView, you must check the status of the LogView process. If the process is closed, start the process. To query the status of the LogView process and start the process, perform the following steps:
1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter **odps-service-console** in the search box and click the name of the service that is displayed.
3. On the details page of the **odps-service-console** service, click **LogView#** in the
Components pane. On the Instances tab, find the instance that you want to manage and click **Terminal** in the **Actions** column.
4. On the page that appears, run the following command to find the Docker container in which
LogView resides:

```bash
docker ps|grep logview;
```

5. Run the following commands to query the status of the LogView process:

```
ps -aux|grep logview; netstat -ntulp|grep 9000;
```

6. If the process is closed, run the following command to start the process:

```
/opt/aliyun/app/logview/bin/control start;
```

#### 2.4.2 Overview

You can use LogView to check and debug tasks for a MaxCompute job that is submitted. LogView allows you to check the details of a job.

**Features**

LogView allows you to check the status, details, and results of a job, and the progress of each phase.

**Log on to LogView**

After you submit an SQL task on a client, a long string that starts with `http://logview.odps.aliyun.com/logview` is returned. In this example, a client named odpscmd is used. Figure 1: Returned long string Remove all line feeds and enter the string in the address bar of a browser.

#### 2.4.3 Preliminary knowledge of LogView

For complex SQL queries, you must have an in-depth knowledge of the relationships between MaxCompute tasks and Fuxi instances before you can understand LogView. In short, a MaxCompute task consists of one or more Fuxi jobs. Each Fuxi job consists of one or more Fuxi tasks. Each Fuxi task consists of one or more Fuxi instances. Figure 1. Relationships between MaxCompute tasks and Fuxi instances The following figures show the relevant information in LogView.

**MaxCompute Instance**

Figure 2. MaxCompute Instance

**MaxCompute Task**

Figure 3. MaxCompute Task

**Task Detail - Fuxi Job**

Figure 4. Task Detail - Fuxi Job(1) Figure 5. Task Detail - Fuxi Job(2)

**Task Detail - Summary**

Figure 6. Task Detail - Summary

**Task Detail - JSONSummary**

Figure 7. Task Detail - JSONSummary

#### 2.4.4 Use LogView

This topic describes how to use LogView.

**Background information**

LogView allows you to view each point in time in the lifecycle of a job, the amount of time consumed by Job Scheduler to schedule a task, user-defined function (UDF) and MapReduce debugging information, and task status, query the polling interval, and check for data skews. For more information about how to log on to LogView, see Usage notes.

**View each point in time in the lifecycle of a job**

Figure 1: View each point in time in the lifecycle of a job

**View the amount of time consumed by Job Scheduler to**

**schedule a task**

Figure 2: View the amount of time consumed by Job Scheduler to schedule a task

**Query the polling interval**

Run the following command to query the polling interval:

```
select * from skew a join small b on a.key=b.key;
```

Figure 3: Query the polling interval After a MaxCompute job is submitted, odpscmd polls the status of the job at an interval of approximately 5 seconds.

**Check for data skews**

Figure 4: Check for data skews

**View the UDF and MapReduce debugging information**

Figure 5: View the UDF and MapReduce debugging information

**View task status**

Figure 6: View task status

**Identify the LogView component based on the job ID**

After a job is submitted, you can press Ctrl+C to return to odpscmd and perform other operations. For example, you can run the wait <instanceid>; command to identify the LogView component and obtain the task status. Figure 7: Identify the LogView component based on the job ID

**Query the tasks that are running**

After you exit the control window, you can run the show p; command to query the tasks that are running and the historical tasks. Figure 8: Query the tasks that are running

### 2.5 Apsara Big Data Manager

Apsara Big Data Manager (ABM) supports O&M on big data services from the perspectives of business, services, clusters, and hosts. You can also update big data services, customize alert configurations, and view the O&M history in the ABM console. For more information about how to log on to the ABM console and how to manage MaxCompute, see MaxCompute O&M.

## 3 Routine O&M

### 3.1 Manage service configurations

MaxCompute configurations are stored in the /apsara/odps_service/deploy/env.cfg directory in odpsag. The configuration file contains the following content:

```
odps_worker_num=3 executor_worker_num=3 hiveserver_worker_num=3 replication_server_num=3 messager_partition_num=3
```

You can modify the values of these parameters based on your business requirements and start the corresponding MaxCompute services based on the configured values. For more information, see Restart MaxCompute services. If you add `xstream_max_worker_num=3` at the end of the configuration file, three workers are running when you start XStream.

### 3.2 Perform routine inspections

1. Check whether all machines are at desired state in the Apsara Infrastructure Management
console. i. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane, choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps in the **Product | Cluster** search box to search for MaxCompute clusters. Figure 1: Search for clusters ii. Check whether all machines are at desired state based on the information in the **Status** and **Instance Status** columns. The following figure provides an example on machines that are not at desired state. Figure 2: Check whether all machines are at desired state iii. Find the cluster that you want to manage and click **Service** and **Component** in the
**Instance Status** column to view the details such as exceptions. You can also click
**Cluster Details** in the **Actions** column to view the details of the cluster.
2. Go to the /home/admin/odps/odps_tools/clt/bin/odpscmd -e directory and run the following
command:

```
select count(*) from datahub_smoke_test;
```

The following figure provides an example on a **Fuxi job** that is running as expected.
3. Run the following commands to check whether the following workers exist and whether the
workers have been recently restarted:

```
i. r swl Odps/MessagerServicex; ii. r swl Odps/OdpsServicex; iii. r swl Odps/HiveServerx; iv. r swl Odps/QuotaServicex;
```

```
v. r swl Odps/ReplicationServicex;
```

4. Run the following command to check whether an error exists:

```
puadmin lscs |grep -vi NORMAL|grep -vi DISK_OK;
```

5. Run the following commands to check whether data is complete:

```
i. puadmin fs -abnchunk -t none; ii. puadmin fs -abnchunk -t onecopy; iii. puadmin fs -abnchunk -t lessmin;
```

6. Log on to the machine on which Apsara Name Service and Distributed Lock Synchronization
System resides.

```
echo srvr | nc localhost 10240 | grep Mode;
```

Example:

```
tj_show -r nuwa.NuwaZK#>/tmp/nuwa;pssh -h /tmp/nuwa -i "echo srvr | nc localhost 1024 0 | grep Mode";
```

7. Run the following commands to check whether Apsara Distributed File System runs as
expected:

```
puadmin gems; puadmin gss;
```

8. Perform daily inspections in the Apsara Big Data Manager (ABM) console to check disk
usage.

### 3.3 Shut down a chunk server for maintenance and clone the chunk server

**maintenance and clone the chunk**

**server**

This topic describes how to shut down a chunk server for maintenance and clone the chunk server if a hardware failure occurs.

**Background information**

If you shut down a chunk server for maintenance and clone the chunk server, the resources of the chunk server in the cluster become unavailable during the maintenance period. However, MaxCompute services are not affected.

**Prerequisites**

All MaxCompute services are at desired state and run as expected. All services on the OPS1 server are at desired state and run as expected. Disk space is sufficient. Data migration is triggered when a node is unpublished. The machine that you want to shut down is checked. Services that exist on the machine must be switched from the primary node to the secondary node.

**Procedure**

1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose Resource Management > Product & Cluster O&M. On the Product & Cluster O&M page, enter odps in the Product | Cluster search box to search for MaxCompute clusters. Find the cluster that you want to manage and click Cluster Details in the Actions column. On the Services tab of the details page, enter **odps-service-computer** in the search box and click the service that is displayed. On the details page of the service, click
**ComputerInit#** in the Components pane. On the Instances tab, find the instance that you
want to manage and click Terminal in the Actions column. On the page that appears, run the following three commands to check the data integrity of Apsara Distributed File System:

```
puadmin abnchunk fs -t none; -- Check whether files are lost. If no output is generated, files are complete. puadmin abnchunk fs -t onecopy; -- Check whether each file has only one copy. If no output is generated, each file ha s only one copy. puadmin abnchunk fs -t lessmin; -- Check whether the number of files is smaller than the minimum number of backups. I f no output is generated, the number of files is smaller than the minimum number of b ackups.
```

2. Add the machine that you want to shut down to the blacklist of Job Scheduler.
i. Run the following command to enable the blacklist feature of Job Scheduler. Skip this step if this feature is enabled.

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

3. Shut down the machine for maintenance. After the maintenance is complete, restart the
machine.

> **Note:** Do not compromise the system during the maintenance.

4. Run the following commands to remove the machine from the blacklist of Job Scheduler:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster remove $hostname; /apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

5. Set the state of the rma action to pending for the faulty machine.
i. Log on to the OPS1 server and run the following command. Set the action_name parameter to rma and the action_status parameter to pending. Then, set the hostname parameter to the name of the faulty machine. In this example, the hostname parameter is set to m1.

**curl "http://127.0.0.1:7070/api/v5/SetMachineAction?hostname=m1" -d**

**'{"action_name":"rma", "action_status":"pending"}';**

The following results are returned: `{`

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

**curl "http://127.0.0.1:7070/api/v5/AddAuditLog?**

**object=/m/m1&category=action" -d '{"category":"action",**

**"from":"tianji.HealingService#", "object":"/m/m1", "content": "{\n \"action\" :**

**\"/action/rma\",\n \"description\" : \"/monitor/rma=error, mtime:**

**1513488046851649\",\n \"status\" : \"pending\"\n}\n" }';**

In this example, the mtime parameter is set to 1513488046851649 to specify the maintenance time of the faulty machine. Set the mtime parameter to the current system time when you configure audit logs. Run the following command to query the current system time:

**curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?**

**hostname=m1&attr=action_name,action_status,action_description@mtime";**

The following results are returned: `{`

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
i. Wait until the state of the rma action becomes approved or doing on the machine. Run the following command to check the action status of the machine:

**curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=m1";**

A large amount of information is returned. Search for the action_status parameter in the returned results. ii. Check the approval status of the request on the machine. A value of pending indicates that the request is being processed. A value of approved, doing, or done indicates that the request is approved. If no value is returned, the request is not approved. Run the following command to query the approval status:

**curl http://127.0.0.1:7070/api/v5/GetMachineInfoPackage?**

**hostname=m1&attr=sr.id,sr.action_name,sr.action_status;**

A large amount of information is returned. Search for the items in the doing state.
7. Shut down the machine when the state of the rma action becomes approved or doing. After
the maintenance is complete, start the machine.

> **Note:** If you want to clone the machine after the maintenance is complete, proceed with the next step. Otherwise, skip the next step.

8. Clone the machine.
i. After the maintenance is complete, run the following command to clone the machine on the OPS1 server:

**curl "http://127.0.0.1:7070/api/v5/SetMachineAction?**

**hostname=m1&action_name=rma&action_status=doing" -d**

**'{"action_name":"clone", "action_status":"approved", "action_description":"",**

**"force":true}';**

The following results are returned: `{`

```json
"err_code": 0, "err_msg": "", "data": [
```

`{`

```json
"hostname": "m1"
```

`}` `]` `}` ii. Access the clone container. Check the clone status and confirm whether the clone operation takes effect. a. Query the clone container. Run the following command to query the clone container:

**docker ps|grep clone;**

The following results are returned:

```
18c1339340ab reg.docker.god7.cn/tianji/ops_service:1f147fec4883e082646715cb79c3710f7b2ae9c6e6851 9a9452b92b4b3366a ops.OpsClone__.clone.1514969139
```

b. Log on to the container. Run the following command to log on to the container:

**docker ps|grep clone;**

c. Query the clone task. Run the following command to query the clone task:

**/home/tops/bin/python /root/opsbuild/bin/opsbuild.py acli list --status=ALL -n**

**10000 | vim -**

9. Run the following command to restore the status of the machine:

**curl "http://127.0.0.1:7070/api/v5/SetMachineAction?**

**hostname=m1&action_name=rma" -d**

**'{"action_name":"rma","action_status":"done", "force":true}';**

0. Check the status of the machine by using a command or in the Apsara Infrastructure
Management console. If the machine is in the GOOD state, the maintenance is complete. Run the following command to check the status of the machine:

**curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?**

**hostname=m1&attr=state,hostname";**

1. Check whether the cluster is at desired state. Make sure that all services on the machine
that you publish are at desired state.

### 3.4 Shut down a chunk server for maintenance without compromising the system

**maintenance without**

**compromising the system**

**Prerequisites**

All MaxCompute services are at desired state and run as expected.

**Procedure**

1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose Resource Management > Product & Cluster O&M. On the Product & Cluster O&M page, enter odps in the Product | Cluster search box to search for MaxCompute clusters. Find the cluster that you want to manage and click Cluster Details in the Actions column. On the Services tab of the details page, enter **odps-service-computer** in the search box and click the service that is displayed. On the details page of the service, click
**ComputerInit#** in the Components pane. On the Instances tab, find the instance that you
want to manage and click Terminal in the Actions column. On the page that appears, run the following three commands to check the data integrity of Apsara Distributed File System:

```
puadmin abnchunk fs -t none; -- Check whether files are lost. If no output is generated, files are complete. puadmin abnchunk fs -t onecopy; -- Check whether each file has only one copy. If no output is generated, each file ha s only one copy. puadmin abnchunk fs -t lessmin; -- Check whether the number of files is smaller than the minimum number of backups. I f no output is generated, the number of files is smaller than the minimum number of b ackups.
```

2. Add the machine that you want to shut down to the blacklist of Job Scheduler.
i. Run the following command to enable the blacklist feature of Job Scheduler. Skip this step if this feature is enabled.

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

3. Shut down the machine for maintenance. After the maintenance is complete, restart the
machine.

> **Note:** Do not compromise the system during the maintenance.

4. Run the following commands to remove the machine from the blacklist of Job Scheduler:

```
/apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster remove $hostname; /apsara/deploy/rpc_wrapper/rpc.sh blacklist cluster get;
```

**Expected results**

During the shutdown of the chunk server, Apsara Distributed File System continuously tries to read data, and SQL tasks remain in the running state. The tasks are complete after the task runs for 7 to 8 minutes, or after the machine resumes.

### 3.5 Adjust the virtual resources of Apsara Distributed Operating System in MaxCompute

**Apsara Distributed Operating**

**System in MaxCompute**

**Prerequisites**

All MaxCompute services are at desired state and run as expected.

**Procedure**

1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the details page of the cluster, click the **Desired State Configuration** tab. On the Desired State Configuration tab, click the role.conf file in the services/fuxi directory.
3. On the right side of the role.conf file, modify the machine tags and click **Preview and**
**Submit**.
4. In the **Confirm and Submit** dialog box, enter the change description and click **Submit**.
5. The cluster starts rolling, and the changes start to take effect.

> **Note:** You can check the task status in operation logs. If the task status is rolling succeeded, the changes take effect.

6. After the changes are made, run the `r ttrl` command on the TerminalService page to
confirm the changes.

### 3.6 Restart MaxCompute services

**Procedure**

1. Log on to the Apsara Infrastructure Management console. In the left-side navigation pane,
choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, enter odps in the **Product | Cluster** search box to search for MaxCompute clusters.
2. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the **Services** tab of the details page, enter **odps-service-computer** in the search box and click the name of the service that is displayed.
3. On the details page of the **odps-service-computer** service, click **ComputerInit#** in the
Components pane. On the Instances tab, find the instance that you want to manage and click **Terminal** in the **Actions** column to go to the TerminalService page. All subsequent CLI operations are performed on this page. Figure 1: Go to the TerminalService page
4. Run the following command to query the number of machines:

```
tj_show -r fuxi.Tubo#;
```

5. Divide the number of machines by 3 to obtain the number of workers.

> **Note:** The number of workers ranges from 1 to 3.

6. Modify the number of workers in the env.cfg file in the vim /apsara/odps_service/deploy
directory.

```
odps_worker_num = 2 executor_worker_num = 2 hiveserver_worker_num = 2 replication_server_num = 2 messager_partition_num = 2 -- In this example, the values are for reference only.
```

7. Restart MaxCompute and Hive.

```
/apsara/odps_service/deploy/install_odps.sh restart_hiveservice; -- Restart Hive. /apsara/odps_service/deploy/install_odps.sh restart_odpsservice; -- Restart MaxCompute.
```

```
r swl Odps/OdpsServicex; r swl Odps/HiveServerx; -- Check the update status and update time of the services after you restart the serv ices.
```

8. Restart the message service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeploymessagerservice; -- Restart the message service. r swl Odps/MessagerServicex; -- Check the update status and update time of the service after you restart the servi ce.
```

9. Restart the quota service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeployquotaservice; -- Restart the quota service. r swl Odps/QuotaServicex; -- Check the update status and update time of the service after you restart the servi ce.
```

0. Restart the replication service.

```
cd /apsara/odps_service/deploy/; sh install_odps.sh pedeployreplicationservice; -- Restart the replication service. r swl Odps/ReplicationServicex; -- Check the update status and update time of the service after you restart the servi ce.
```

1. Restart the service mode.

```
r plan Odps/CGServiceControllerx >/home/admin/servicemode.json; r sstop Odps/CGServiceControllerx; r start /home/admin/servicemode.json; -- Restart the service mode. r swl Odps/CGServiceControllerx; -- Check the update status and update time of the service after you restart the servi ce.
```

## 4 Common issues and solutions

**solutions**

### 4.1 Query and allocate resources in a MaxCompute cluster

**in a MaxCompute cluster**

This topic describes how to query and allocate the storage and computing resources in a MaxCompute cluster. This topic also introduces quota groups, the relationship between quota groups and MaxCompute projects, and the division principles of quota groups.

**How do I query the resources that can be allocated to projects**

**in a MaxCompute cluster?**

Storage resources: The available storage resources in a MaxCompute cluster are limited and can be calculated based on the number of compute nodes in the entire cluster. The storage capacity in a MaxCompute cluster is managed by using Apsara Distributed File System. You can run the commands of Apsara Distributed File System to query the information about the storage capacity, such as the storage usage. The following metrics are used to measure the storage resources of a cluster: Storage Capacity: the total size of files that can be stored in a cluster. You can calculate the storage capacity of a cluster based on the following formula: Storage capacity = Number of machines × [Size of a single disk × (Number of disks on a single machine - 1)] × System security threshold × System compression ratio/Number of distributed replicas.

> **Note:** Based on the compression ratio of standard TPC-H test datasets, the ratio of the original data size to the compressed data size is 3 to 1. The ratio varies based on the characteristics of business data.
> Typically, three replicas are stored in a distributed manner.
> Security threshold: **The default value is 0.85 in the MaxCompute system.** You can specify a custom security threshold based on your business requirements. A value of 0.85 indicates that if more than 85% of the total storage capacity is used, the security level is low. You must scale out the system based on your business requirements or delete unnecessary data.

Query the storage capacity of a MaxCompute cluster Run the `puadmin lscs` command on the cluster AG. The total storage capacity, available storage capacity, and used storage capacity are displayed at the end of the output. Figure 1: Storage capacity of a cluster

> **Note:** Parameters:
> Total Disk Size: the total size of physical space. Each file is stored in three replicas. The size of logical space is one third of the size of physical space.
> Total Free Disk Size: the total size of available storage space, excluding the storage space of recycle bins on chunk servers.
> Total File Size: the total size of physical space that is used by the files of Apsara Distributed File System, including the files that are stored in the /deleted/ directory.

Run the following command on the cluster AG to query the storage capacity used by all projects:

```
pu ls -l pangu://localcluster/product/aliyun/odps/
```

Example:

```
pu ls -l pangu://localcluster/product/aliyun/odps/|grep adsmr -A 4 -- Query the storage capacity that is used by a single project. In this example, the storage capacity of the adsmr project is queried.
```

Figure 2: Storage capacity of a project

> **Note:** Parameters:
> Length: the logical length that is used by the project. The physical length required is three times the logical length.
> FileNumber: the number of files that are stored.
> DirNumber: the number of directories that are created.

File Size: the total number of files that can be stored in a cluster. This number is limited based on the memory capacity of PanguMaster. A large number of small files or an improper number of files in a cluster also affect the stability of the cluster and its services. The index files of Apsara Distributed File System, including the information about Apsara Distributed File System files and directories, are stored in the memory of PanguMaster. Each file in the memory of PanguMaster corresponds to a file node. The memory of PanguMaster is occupied by file nodes, directories of all levels, and chunks. A large file is split into multiple chunks in Apsara Distributed File System. Therefore, the factors that affect the memory usage of PanguMaster include the number of files, directory hierarchy, and number of chunks. If the size of the original files in Apsara Distributed File System is large, the memory usage of PanguMaster is relatively low. If a large number of small files exist, the memory usage of PanguMaster is relatively high. We recommend that you perform the following operations to reduce the memory usage of PanguMaster: Delete empty directories and reduce the number of directory levels. Do not create directories. A directory is automatically created when a file is created. Store multiple files in a directory. You can store up to 100,000 files in a directory. Decrease the length of file names and directory names to reduce the memory usage and network traffic in PanguMaster. Reduce the number of small tables and files. We recommend that you use the tunnel service to upload and commit MaxCompute tables only when the table data size reaches 64 MB. The following figure shows the numbers of files that can be stored in Apsara Distributed File System based on the memory capacity of PanguMaster. Figure 3: Numbers of files that can be stored in Apsara Distributed File System based on the memory capacity of PanguMaster Query the number of files stored in a MaxCompute cluster Run the `pu quota` command on the cluster AG to query the total number of files that are stored in a MaxCompute cluster. Figure 4: Total number of files that are stored in a MaxCompute cluster Run the following command on the cluster AG to query the total number of files that are stored in a project of a MaxCompute cluster. In this example, the adsmr project is queried.

```
pu ls -l pangu://localcluster/product/aliyun/odps/|grep adsmr -A 4
```

Figure 5: Total number of files that are stored in a project of a MaxCompute cluster

> **Note:** Parameters:
> FileNumber: the number of files that are stored.
> DirNumber: the number of directories that are created.
> The total number of files that are stored in the adsmr project is the sum of the numbers of files and directories.

Computing resources: The computing resources of a MaxCompute cluster include the CPU and memory resources. The total amount of computing resources is calculated based on the following formula: Total amount of computing resources = (Number of CPU cores of a single machine + Memory size of a single machine) × Number of machines. One CPU core on each machine is used by the system. Therefore, if a machine contains 56 CPU cores, 55 CPU cores of the machine are managed by the distributed scheduling system and are scheduled for use by MaxCompute. The remaining memory is allocated by Job Scheduler. Typically, each CPU core is allocated 4 GB of memory in a MaxCompute task. This ratio varies based on MaxCompute tasks. Query computing resources Run the `r ttrl` command on the cluster AG to query all computing resources of a cluster. Figure 6: All computing resources of a cluster

> **Note:** The domain names of Tubo machines are displayed in the first column. The CPU cores of Tubo machines are displayed in the second column, and the unit is u, where one CPU core equals 100 u. The memory size of Tubo machines is displayed in the third column, and the unit is MB. The tags that are added to Tubo machines in Job Scheduler are displayed in the fourth column.

Run the `r tfrl` command on the cluster AG to query the remaining computing resources of a cluster. Figure 7: Remaining computing resources of a cluster

> **Note:** The domain names of Tubo machines are displayed in the first column. The CPU cores of Tubo machines are displayed in the second column, and the unit is u, where one CPU core equals 100 u. The memory size of Tubo machines is displayed in the third column, and the unit is MB. The tags that are added to Tubo machines in Job Scheduler are displayed in the fourth column.

Run the r cru command on the cluster AG to query the resources used by the tasks that are running in MaxCompute. Figure 8: Resources used by the tasks that are running

> **Note:** The task names are displayed in the first column. The CPU cores that are used by tasks are displayed in the second column. The memory size that is used by tasks is displayed in the third column. The number of Fuxi instances that are started by the corresponding role for tasks in Job Scheduler is displayed in the fourth column.

**How do I allocate resources to projects in a MaxCompute**

**cluster?**

Storage resource allocation: The storage capacity and the maximum number of files are configured when you create a project based on the characteristics of the project. You can modify the configurations in MaxCompute AdminConsole. Figure 9: Configurations of the storage capacity and the maximum number of files If the following error messages are returned, the occupied storage space or the number of files exceeds the limit. In this case, you must organize the data in the project by deleting unnecessary table data or increasing the storage capacity. Figure 10: Error messages

> **Important:** The sum of the storage capacity of all projects cannot exceed the total storage capacity of a cluster. Similarly, the total number of files of all projects cannot exceed the total number of files of a cluster. Therefore, you must properly allocate the storage capacity and the maximum number of files for different projects and make timely adjustments based on your business requirements.

Computing resource allocation: Computing resources are allocated based on quota groups. What is a quota group? MaxCompute allows you to divide the computing resources of a cluster into different quota groups, and schedule these quota groups based on your business requirements. A quota group represents a specific amount of CPU and memory resources. You can specify the MinQuota and MaxQuota parameters to configure the CPU and memory resources of a quota group. The MinQuota parameter specifies the minimum amount of resources allocated to the quota group, and the MaxQuota parameter specifies the maximum amount of resources allocated to the quota group. For example, if you set the MinCPU parameter to 500, at least five CPU cores are allocated to the quota group. If you set the MaxCPU parameter to 2000, up to 20 CPU cores are allocated to the quota group. By default, MaxCompute uses a fairness-aware integrated resource (FAIR) scheduling policy and a first-in-first-out (FIFO) scheduling policy. The difference between the FAIR and FIFO scheduling policies lies in the keys that are used to sort tasks in waiting queues. If each schedule unit has its own priority, both the FAIR and FIFO scheduling policies allocate resources to high-priority schedule units first. If all schedule units share the same priority, the FIFO scheduling policy sorts the schedule units based on the time when they are submitted. The schedule units that are submitted earlier have a higher priority. The FAIR scheduling policy sorts the schedule units based on the value of the slotNum parameter. A smaller value of the slotNum parameter specifies a higher priority. This way, the same resources are allocated to schedule units of the same priority. You can run the `r` `quota` command on the cluster AG to query quota group settings. Figure 11: Query quota group settings Run the following command on the cluster AG to create and modify a quota group based on your business requirements:

```
sh /apsara/deploy/rpc_wrapper/rpc.sh setquota -i $QUOTAID -a $QUOTANAME -t fair -s $max_cpu_quota $max_mem_quota -m $min_cpu_quota $min_mem_quota
```

> **Note:** If the **$QUOTAID** parameter is specified, the specified quota group is modified. If the $QUOTAID parameter is not specified, a quota group is created.

Figure 12: Create a quota group Figure 13: Modify a quota group Divide quota groups To correctly divide quota groups, you must first understand the relationship between a MaxCompute project and a quota group. When you create a project, you must specify the quota group to which the project belongs. You can change the quota group after the project is created. Figure 14: Select a quota group Resources in a quota group can be used by all tasks of the projects that belong to this quota group. Therefore, the tasks of projects in the same quota group may affect each other during peak hours. Large tasks may occupy all resources in the quota group, whereas other computing tasks can only wait for resources. The following figures provide an example. In the scenario of the first figure, a great number of tasks are waiting for resources, whereas the remaining resources of the cluster are sufficient. In this case, you can check the quota usage. In the scenario of the second figure, the 9243 quota group is allocated 50 CPU cores and all allocated CPU cores are used. The tasks of projects that belong to the 9243 quota group must wait until the quota is available. In this case, the remaining resources of the cluster cannot be used by these tasks. Figure 15: Tasks waiting for resources Figure 16: Quota that is used up You must divide quota groups based on the following general principles: Make sure that quota groups do not affect each other in a large resource pool, and prevent overly fine-grained division of quota groups. For example, some large tasks cannot be scheduled due to quota group limits, or a quota group may be occupied for an extended period of time, which affects other tasks in the group. Consider the specified MinQuota and MaxQuota parameters when you divide quota groups. You can oversell the resources in your cluster. That is, the sum of the maximum quotas of all quota groups can be greater than the total amount of cluster resources. However, the oversell ratio cannot be too high. Otherwise, a project may perpetually occupy a large amount of resources. Take the following factors into consideration when you divide quota groups: the priorities of tasks, task duration, amount of task data, and characteristics of computing types. Properly configure quota groups for peak hours. We recommend that you configure a separate quota group for tasks that are important and time-consuming. Divide quota groups and select quota groups for projects based on a resource preallocation policy, and adjust your configurations in a timely manner based on actual requirements.

### 4.2 Common issues and data skew troubleshooting

**troubleshooting**

**Scenario 1: how to determine whether a job has stopped**

**running due to insufficient resources**

Symptom: The job does not progress as expected. Figure 1. Symptom Cause: The issue is typically caused by insufficient resources. You can use LogView to determine the status of job resources (task instance status). Ready: indicates that instances are waiting for Job Scheduler to allocate resources. Instances can resume operation after they obtain the necessary resources. Wait: indicates that instances are waiting for dependent tasks to complete. The task instances in the Ready state shown in the following figure indicate that there are insufficient resources to run these tasks. After an instance obtains the necessary resources, its status changes to **Running**. Solution: If there are insufficient resources during peak hours, you can reschedule the tasks to run during off-peak hours. If the computing quotas are insufficient, check whether the quota group of the project has sufficient computing resources. If computing resources in the cluster are occupied for long periods of time, you can develop a computing quota allocation policy to scale the quota as necessary. We recommend that you do not run abnormally large jobs to prevent the jobs from occupying resources for extended periods of time. You can enable SQL acceleration, so that you can run small jobs without requesting resources from Job Scheduler. You can use the First-In First-Out (FIFO) scheduling policy.

**Scenario 2: how to find the root cause of a job that has been**

**running for an extended period of time**

Symptom: The MaxCompute job execution progress has remained at 99% for a long period of time. Cause: The running time of some Fuxi instances in the MaxCompute job is significantly longer than that of other Fuxi instances. Figure 2. Cause analysis Further analysis: Analyze the job summary in LogView, and calculate the difference between the max and avg values of input and output records of a slow task. If the max and avg values differ by several orders of magnitude, it can be initially determined that the job data is skewed. Figure 3. Further analysis Solution: If there are slow Fuxi instances on a particular machine, check whether a hardware failure has occurred on the machine.

**Scenario 3: How to improve the concurrency of MaxCompute**

**jobs**

Fault locating: The concurrency of Map tasks depends on the following factors: Split size and merge limit. Map takes a series of data files as inputs. Larger files are split into partitions based on the odps.sql.mapper.split.size value, which is 256 MB by default. An instance is started for each partition. However, starting an instance requires resources and time. Small files can be merged into a single partition based on the odps.sql.mapper.merge.limit.size value and be processed by a single instance to improve instance utilization. The default value of odps.sql.mapper.merge.limit.size is 64 MB. The total size of small files merged cannot exceed this value. Instances cannot process data across multiple partitions. A partition is mapped to a folder in Apsara Distributed File System. You must run at least one instance to process data in a partition. Instances cannot process data across multiple partitions. In a partition, you must run instances based on the preceding rule. Typically, the number of instances for Reduce tasks is 1/4 of that for Map tasks. The number of instances for Join tasks is the same as that for Map tasks, but cannot exceed 1,111. You can use the following methods to increase the number of concurrent instances for Reduce and Join tasks:

```
 set odps.sql.reducer.instances = xxx
 set odps.sql.joiner.instances = xxx
```

Scenarios that require higher concurrency: A single record only contains a small amount of data. Because a single record contains a small amount of data, there are many records in a file of the same size. If you split data into 256 MB chunks, a single Map instance needs to process a large number of records, reducing concurrency. Dump operations occur in the Map, Reduce, and Join stages. Based on the preceding job summary analysis, the displayed dump information indicates that the instance does not have sufficient memory to sort data in the Shuffle stage. Improving concurrency can reduce the amount of data processed by a single instance to the amount of data that can be handled by the memory, eliminate disk I/O time consumption, and improve the processing speed. Time-consuming UDFs are used. The execution of UDFs is time-consuming. If you execute UDFs concurrently, you can reduce the UDF execution time of an instance. Solution: You can decrease the following parameter values to improve the concurrency of Map tasks:

```
odps.sql.mapper.split.size = xxx odps.sql.mapper.merge.limit.size = xxx
```

You can increase the following parameter values to improve the concurrency of Reduce and Join tasks:

```
odps.sql.reducer.instances = xxx odps.sql.joiner.instances = xxx
```

> **Note:** Improving concurrency will result in a greater amount of resources being consumed. We recommend that you take cost into account when improving concurrency. An instance takes an average of 10 minutes to complete after optimization, improving overall resource utilization. We recommend that you optimize jobs in critical paths so that they consume less time.


**Scenario 4: how to resolve data skew issues**

Different types of data skew issues in SQL are resolved in different ways. GROUP BY data skew The uneven distribution of GROUP BY keys results in data skew on reducers. You can set the anti-skew parameter before executing SQL tasks.

```
set odps.sql.groupby.skewindata=true
```

After this parameter is set to true, the system automatically adds a random number to each key when running the Shuffle hash algorithm and prevents data skew by introducing a new task. DISTRIBUTE BY data skew Using constants to execute the DISTRIBUTE BY clause for full sorting of the entire table will result in data skew on reducers. We recommend that you do not perform this operation. Data skew in the Join stage Data is skewed in the Join stage when the Join keys are unevenly distributed. For example, a key exists in multiple joined tables, resulting in a Cartesian explosion of data in the Join instance. You can use one of the following solutions to resolve data skew in the Join stage: When a large table and a small table are joined, use MapJoin instead of Join to optimize query performance. Use a separate logic to handle a skewed key. For example, when a large number of null values exist in the key, you can filter out the null values or execute a CASE WHEN statement to replace them with random values before the Join operation. If you do not want to modify SQL statements, configure the following parameters to allow MaxCompute to perform automatic optimization:

```
set odps.sql.skewinfo=tab1:(col1,col2)[(v1,v2),(v3,v4),...] set odps.sql.skewjoin=true;
```

Data skew caused by multi-distinct Multi-distinct syntax aggravates GROUP BY data skew. You can use the GROUP BY clause with the COUNT function instead of multi-distinct to alleviate the data skew issue. UDF OOM Some jobs report an OOM error during runtime. The error message is as follows: `FAILED:`

```
ODPS-0123144: Fuxi job failed - WorkerRestart errCode:9,errMsg:SigKill(OOM), usually
```

`caused by OOM(out of memory)` . You can fix the error by configuring the UDF runtime parameters. Example:

```
odps.sql.mapper.memory=3072; set odps.sql.udf.jvm.memory=2048; set odps.sql.udf.python.memory=1536;
```

The related data skew settings are as follows:

```
set odps.sql.groupby.skewindata=true/false
```

Description: allows you to enable GROUP BY optimization.

```
set odps.sql.skewjoin=true/false
```

Description: allows you to enable Join optimization. It is effective only when odps.sql.skewinfo is set.

```
set odps.sql.skewinfo
```

Description: allows you to set detailed information for Join optimization. The command syntax is as follows:

```
set odps.sql.skewinfo=skewed_src:(skewed_key)[("skewed_value")] src a join src_skewjoin1 b on a.key = b.key;
```

Example:

```
set odps.sql.skewinfo=src_skewjoin1:(key)[("0")] -- The output result for a single skewed value of a single field is as follows: explain select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src_skewjoin1 b on a. key = b.key; set odps.sql.skewinfo=src_skewjoin1:(key)[("0")("1")] -- The output result for multiple skewed values of a single field is as follows: explai n select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src_skewjoin1 b on a.key = b.key;
```

**Scenario 5: how to configure common SQL parameters**

**Map settings**

```
set odps.sql.mapper.cpu=100
```

Description: allows you to set the number of CPUs used by each instance in a Map task. Default value: 100. Valid values: 50 to 800.

```
set odps.sql.mapper.memory=1024
```

Description: allows you to set the memory size of each instance in a Map task. Unit: MB. Default value: 1024. Valid values: 256 to 12288.

```
set odps.sql.mapper.merge.limit.size=64
```

Description: allows you to set the maximum size of control files to be merged. Unit: MB. Default value: 64. You can set this variable to control the inputs of mappers. Valid values: 0 to Integer.MAX_VALUE.

```
set odps.sql.mapper.split.size=256
```

Description: allows you to set the maximum data input volume for a Map task. Unit: MB. Default value: 256. You can set this variable to control the inputs of mappers. Valid values: 1 to Integer.MAX_VALUE.

**Join settings**

```
set odps.sql.joiner.instances=-1
```

Description: allows you to set the number of instances in a Join task. Default value: -1. Valid values: 0 to 2000.

```
set odps.sql.joiner.cpu=100
```

Description: allows you to set the number of CPUs used by each instance in a Join task. Default value: 100. Valid values: 50 to 800.

```
set odps.sql.joiner.memory=1024
```

Description: allows you to set the memory size of each instance in a Join task. Unit: MB. Default value: 1024. Valid values: 256 to 12288.

**Reduce settings**

```
set odps.sql.reducer.instances=-1
```

Description: allows you to set the number of instances in a Reduce task. Default value: -1. Valid values: 0 to 2000.

```
set odps.sql.reducer.cpu=100
```

Description: allows you to set the number of CPUs used by each instance in a Reduce task. Default value: 100. Valid values: 50 to 800.

```
set odps.sql.reducer.memory=1024
```

Description: allows you to set the memory size of each instance in a Reduce task. Unit: MB. Default value: 1024. Valid values: 256 to 12288.

**UDF settings**

```
set odps.sql.udf.jvm.memory=1024
```

Description: allows you to set the maximum memory size used by the UDF JVM heap. Unit: MB. Default value: 1024. Valid values: 256 to 12288.

```
set odps.sql.udf.timeout=600
```

Description: allows you to set the timeout period of a UDF. Unit: seconds. Default value: 600. Valid values: 0 to 3600.

```
set odps.sql.udf.python.memory=256
```

Description: allows you to set the maximum memory size used by the UDF Python API. Unit: MB. Default value: 256. Valid values: 64 to 3072.

```
set odps.sql.udf.optimize.reuse=true/false
```

Description: When this parameter is set to true, each UDF function expression can only be calculated once, improving performance. Default value: true.

```
set odps.sql.udf.strict.mode=false/true
```

Description: allows you to control whether functions return NULL or an error if dirty data is found. If the parameter is set to true, an error is returned. Otherwise, NULL is returned.

**MapJoin settings**

```
set odps.sql.mapjoin.memory.max=512
```

Description: allows you to set the maximum memory size for a small table when running MapJoin. Unit: MB. Default value: 512. Valid values: 128 to 2048.

```
set odps.sql.reshuffle.dynamicpt=true/false
```

Description: Dynamic partitioning scenarios are time-consuming. Disabling dynamic partitioning can accelerate SQL. If there are few dynamic partitions, disabling dynamic partitioning can prevent data skew.

**Scenario 6: how to check the storage usage of a single project**

Launch the MaxCompute console as a project owner and run the `desc project` <project_name>-extended; command to view the following information. Figure 4. Storage information The preceding figure shows the capacity-related storage information of the project. The relationship between the physical and logical values of the related metrics is: Physical value of a metric = Logical value of the metric * Number of replicas.

## 5 MaxCompute O&M

### 5.1 Log on to the ABM console

This topic describes how to log on to the Apsara Big Data Manager (ABM) console.

**Prerequisites**

**Procedure**

### 5.2 Business O&M

#### 5.2.1 O&M overview and entry

This topic describes the business O&M features and how to go to the business O&M page.

**Business O&M features**

Projects: Project List: shows all projects and project details in a MaxCompute cluster. You can search for and filter projects. You can also change the quota group of a project. If zonedisaster recovery is enabled, you can specify resource replication parameters and determine whether to enable resource replication for a project. Authorize Package for Metadata Repository: allows you to authorize members of a project to access the metadata warehouse. Encryption at Rest: allows you to encrypt the data stored in MaxCompute projects. Disaster Recovery: allows you to view the cluster status when zone-disaster recovery is enabled for MaxCompute. You can enable the switchover between the primary and secondary clusters. You can also determine whether to run scheduled tasks to synchronize resources between the primary and secondary clusters. Quota Groups: shows the quota groups of all projects in a MaxCompute cluster. It allows you to create and modify quota groups. You can also view details about quota groups and enable period management for quota groups. Jobs: shows information about jobs in a MaxCompute cluster. You can search for and filter jobs. You can also view the operational logs, terminate running jobs, and collect job logs. Business Optimization: File Merging: allows you to create file merge tasks for clusters and projects. You can also filter merge tasks and view the records of the tasks. File Archiving: allows you to create file archive tasks for clusters and projects. You can also filter archive tasks and view the records of the tasks. Resource Analysis: allows you to view the resource usage of the cluster from different dimensions.

**Go to the business O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and then **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Business**
tab. In the left-side navigation pane, choose **Projects > Project List**.

#### 5.2.2 Project management

##### 5.2.2.1 Manage projects

The Project List page displays all projects and project details of MaxCompute clusters. You can filter, query, and sort projects. You can also change the quota group of a project. If zonedisaster recovery is enabled, you can configure resource replication parameters and specify whether to enable resource replication for a project.

**Go to the Project List page**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the **Business** tab. On the Business tab, choose
**Projects > Project List** in the left-side navigation pane.
The **Project List** page displays the information about all projects in a MaxCompute cluster, including the name, cluster, used storage, storage quota, storage usage, number of files, owner, and creation time of each project.

**View project details**

On the **Project List** page, click the name of the project that you want to manage to go to the details page. On the details page of the project, view information on the Overview, Jobs, Storage, Computing, Configuration, Tunnel, Resource Analysis, Encryption at Rest, and Cluster Replication tabs. For more information, see View project details.

**Change a quota group**

You can change the default quota group of a project.
1. On the **Project List** page, find the project that you want to manage, move the pointer over
**Actions**, and then select **Change Default Quota Group**. In the **Change Default Quota**
**Group** panel, configure the parameters.
Parameters:
**Project:** the project for which you want to change the quota group.
**Region**: the region in which the project resides.
**Cluster**: the default cluster to which the project belongs. If the project belongs to
multiple clusters, you can select the default cluster from the drop-down list.
**Quota Group**: the quota group to which the project belongs. If you want to change the
quota group, select a quota group from the drop-down list.
2. Click **Run**.

**Modify the storage quota**

You can modify the storage quota of a project.
1. On the **Project List** page, find the project that you want to manage, move the pointer over
**Actions**, and then select **Modify Storage Quota**. In the **Change Storage Quota** panel,
configure the parameters. Parameters:
**Region**: the region in which the project resides.
**Project**: the name of the project for which you want to modify the storage quota.
**Cluster**: the default cluster to which the project belongs.
**Target Storage Quota**: the destination storage quota. Unit: TB.
**Reason**: the reason for the modification.
2. Click **Run**.

**Configure resource replication**

The resource replication feature can be configured only in zone-disaster recovery scenarios. In other scenarios, you can only view the settings. In zone-disaster recovery scenarios, you can specify whether to enable the resource replication feature for a project in the primary cluster. If the resource replication feature is enabled for a project, you can configure data synchronization rules for the project to regularly synchronize data such as table data to a secondary cluster.
1. On the **Project List** page, find the project that you want to manage, move the pointer over
**Actions**, and then select **Resource Replication**. In the **Copy Resource** panel, configure
the parameters. Parameters:
**Enable**: specifies whether to enable the resource replication feature. Valid values: **true**
and **false**. Default value: **false**.
**Configure**: the data synchronization rules for the project. In most cases, the default
settings are used. If you want to modify the settings, contact O&M engineers.
2. After you modify the code in the **Configure** field, click **Compare Versions** to view the
highlighted differences.
3. Click **Run**.

**Switch the tunnel configurations**

1. On the **Project List** page, specify filter conditions to search for projects for which you want
to switch the tunnel configurations.
2. Select the projects for which you want to switch the tunnel configurations and click **Switch**
**Tunnel Configurations**.

> **Note:** Select one or more projects.
> If you want to switch the tunnel configurations of a project, you can also perform the following operations: On the **Project List** page, click the name of the project that you want to manage. On the details page of the project, click the **Tunnel** tab. On the Tunnel tab, click **Switch Tunnel Configurations** in the Actions column. In the **Switch** **Tunnel Configurations** panel, select a value from the **Destination Configurations** drop-down list.

3. In the **Switch Tunnel Configurations** dialog box, select a value from the **Destination**
**Configurations** drop-down list.
4. Click **Run**. The tunnel configurations are switched.

##### 5.2.2.2 View project details

The Apsara Big Data Manager (ABM) console allows you to view the details of your MaxCompute projects, including the project overview, jobs, storage, configurations, quota groups, tunnel, and information about resource analysis, storage encryption, and crosscluster replication.

**Go to the details page of a project**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Business**
tab. On the Business tab, choose **Projects** > **Project List** in the left-side navigation pane. On the page that appears, click the name of a project to view its details.

**Overview**

On the **Overview** tab, you can view the following information about the project: Basic information, such as the default quota group, creator, creation time, service, and region. Trend charts that show the trends of used CPU and memory resources, guaranteed CPU and memory resources, and the upper limits of CPU and memory resources by minute in different colors. Trend chart that shows the trends of CPU utilization and memory usage by day in different colors.

**Jobs**

On the **Jobs** tab, you can view job snapshots by day in the previous week. The detailed information about a job snapshot includes the job ID, project, quota group, submitter, duration, minimum CPU utilization, maximum CPU utilization, minimum memory usage, maximum memory usage, DataWorks node ID, cluster, status, start time, priority, and type. You can also view the run logs of a job to identify errors. You can perform the following operations on the Jobs tab: Customize columns or sort job snapshots by column. View the run logs of jobs during a specific period of time or terminate jobs.

**Storage**

On the **Storage** tab, you can view the storage usage, used storage space, storage quota, and available storage space. You can also view a trend chart that shows the trends of storage usage, including the number of files in Apsara Distributed File System, storage size, the number of tables, the number of partitions, and redundant storage space by day in different colors.

> **Note:** The Storage tab displays only the information about storage resources. To view the information about computing resources, go to the Quota Groups tab.

**Configuration**

On the **Configuration** tab, you can configure the general, sandbox, SQL, MapReduce, access control, and resource recycling properties of the project. You can configure package-based authorization to allow access to the metadata warehouse. On the **Properties** tab, modify configuration items based on your business requirements and click **Submit**. To restore all configuration items to the default settings, click **Reset**. On the **Authorize Package for Metadata Repository** tab, you can install the package and perform package-based authorization.

**Quota Groups**

On the **Quota Groups** tab, you can view the quota groups of a project and the details of each quota group. To view the details of a quota group, click the quota group name in the **Quota** column. For more information about quota groups, see Manage quota groups.

> **Note:** The Quota Groups tab displays only the information about computing resources. To view the information about storage resources, go to the Storage tab.

**Tunnel**

On the **Tunnel** tab, you can view the tunnel throughput of the project in units of bytes per minute. The Tunnel Throughput (Bytes/Min) chart shows the trend lines of inbound and outbound traffic in different colors.

**Resource Analysis**

On the **Resource Analysis** tab, you can view the resource usage of the project from different dimensions, including tables, tasks, duration, start time, and engines.

**Encryption at Rest**

On the **Encryption at Rest** tab, you can configure encryption algorithms to encrypt data. The following encryption algorithms are supported: AES-CTR, AES-256, RC4, and SM4.

**Cross-cluster Replication**

On the **Cross-cluster Replication** tab, you can view the projects for which the cross-cluster replication feature is enabled and the details and status of cross-cluster replication. When you deploy multiple clusters to use MaxCompute, MaxCompute projects may be mutually dependent, and data is directly read between projects. MaxCompute regularly scans tables or partitions that are directly read by other tables or partitions. If the duration of direct data reading reaches the specified threshold, MaxCompute adds the tables or partitions to the cross-cluster replication list. For example, Project 1 in Cluster A depends on Table 1 of Project 2 in Custer B. In this case, Project 1 directly reads data from Table 1. If the duration of direct data reading reaches the specified threshold, MaxCompute adds Table 1 to the cross-cluster replication list. The **Cross-cluster Replication** tab consists of the **Replication Details** and **Replication**
**Configuration** tabs.
On the Replication Details tab, the information about the tables that support cross-cluster replication is displayed. You can view the project name, cluster name, table name, partition, storage space, number of files, and cluster to which the data is synchronized. On the Replication Configuration tab, the configurations of the tables that support crosscluster replication are displayed. You can view the table name, priority, cluster to which the data is synchronized, and lifecycle. You can also view the progress of cross-cluster replication for a table.

##### 5.2.2.3 Encrypt data

You can specify whether to encrypt the data stored in MaxCompute projects.

**Prerequisites**

MaxCompute V3.8.0 or later is deployed. In this case, storage encryption is supported by default. If you deploy MaxCompute of an earlier version and update the version to V3.8.0 or later, storage encryption is not supported by default. To enable storage encryption, complete relevant configurations for your MaxCompute cluster. For more information, contact an O&M administrator.

**Background information**

After storage encryption is enabled for a project, this feature cannot be disabled, and only the data that is newly written to the project is automatically encrypted. To encrypt historical data, you can create rules and configure tasks. Before you encrypt historical data for a project, make sure that you understand the concepts of rules and tasks in Apsara Big Data Manager (ABM). A rule is used to specify the time period of historical data that you want to encrypt in a specific project. After you create a rule, the system obtains the data in the specified time period every day after the data is exported from the metadata warehouse. Only one rule can be retained every day. If multiple rules are created on a single day, only the latest rule takes effect. Each rule takes effect only once. You can create a key rotate task to encrypt the selected historical data.

**Procedure**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Business**
tab. The **Project List > page appears**.
4. On the **Project List** page, click the name of a project to go to the details page.
5. On the details page of the project, click the **Encryption at Rest** tab. The **Encrypt** tab
appears.
6. Enable storage encryption.
After storage encryption is enabled, all data that is newly written to the project is automatically encrypted. i. On the **Encrypt** tab, click **Modify** in the Actions column. In the **Configure Encrypted**
**Storage** panel, configure the **Encryption Algorithm**, **region**, and **project** parameters.

> **Note:** The AES-CTR, AES-256, RC4, and SM4 encryption algorithms are supported.

ii. Click **Run**. After storage encryption is enabled, the switch in the **Encrypted Storage** column is
**turned on**.
7. If you want to encrypt historical data or encrypted data, perform the following steps:
i. Configure a rule. On the **Create Rule** tab, find a time period in the **Create Rule** section and click **OK** in the Actions column. In the Create Rule message, click **Run**. A rule is created and appears in the rule list. The available time periods include **Last Three Months**, **Last Six Months**, **Three**
**Months Ago**, **Six Months Ago**, and **All**.
ii. Create a key rotate task. On the **Configure Task** tab, click **Add a key rotate task** . In the **Edit Key Rotate Task** panel, configure the parameters that are described in the following table and click **Run**.

| Parameter | Description |
|---|---|
| Region | The region in which the project whose data you want to encrypt resides. Select a region from the drop-down list. |
| Project Name | The name of the project whose data you want to encrypt. |
| Start Timestamp | The start time of the task. |
| Ended At | The end time of the task. |
| Priority | The priority of the task. A smaller value specifies a higher priority. |
| Enabled | Specifies whether to enable the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of merge tasks for the project. Valid values: Yes: limits the concurrency. Merge tasks cannot be concurrently run. No: does not limit the concurrency. Merge tasks can be concurrently run. |
| Maximum Concurrent Tasks | The maximum number of merge tasks that can be concurrently run for the cluster in which the selected project resides. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |
| Maximum Number of Running Jobs | The maximum number of jobs that can be concurrently run for the cluster in which the selected project resides. This parameter is a global parameter. The jobs refer to all types of jobs in the cluster in which the selected project resides. |

| Merge Parameters | { "odps.merge.cross.paths": "true", "odps.idata.useragent": "odps encrypt key rotate via force mergeTask", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.failure.handling": "any", "odps.merge.maintain.order.flag": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.quickmerge.flag": "true", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.force.rewrite": "true", "odps.merge.restructure.action": "hardlink" } |
|---|---|

8. **Optional.** View the history of data encryption in the project.
On the **Historical Queries** tab, select a date from the **Date** drop-down list. Then, you can view the information about storage encryption on the specified date.

##### 5.2.2.4 Grant access permissions on the metadata warehouse

**warehouse**

You can grant access permissions on the metadata warehouse to projects and project members.

**Prerequisites**

If MaxCompute V3.8.1 or later is deployed, the package of the metadata warehouse is installed by default. In this case, you can directly use Apsara Big Data Manager (ABM) to grant access permissions on the metadata warehouse. If MaxCompute is upgraded to V3.8.1 or later, the package of the metadata warehouse is not installed by default. Before you grant access permissions on the metadata warehouse, you must manually install the package of the metadata warehouse. A project is created in DataWorks. For more information about how to create a workspace, see **Create a workspace** in **DataWorks User Guide**.

**Background information**

To allow a project to access the metadata warehouse, grant the required permissions to the project and install the package to the project in the ABM console. When you install the package, ABM retrieves authentication information, such as the AccessKey pair, of the project from DataWorks. If the project is created in MaxCompute, an error message is returned.

**Procedure**

1. Log on to the Apsara Big Data Manager console.
2. In the upper-left corner, click the
icon and then **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Business**
tab. Choose **Projects > Project List**.
4. Click the name of a project to go to the project details page.
5. On the project details page, click the **Configuration** tab. Then, click the **Authorize**
**Package for Metadata Repository** tab.
6. Click **Authorize** in the Actions column. In the **Authorize Package** message, click **Run**. A
message appears, indicating that the permissions are granted.
7. Click **Install** in the Actions column. In the **Install Package** message, click **Run**. A message
appears, indicating that the package is installed. After the package is installed, the switch in the **Authorized** column is turned on.

##### 5.2.2.5 Perform disaster recovery

When a primary MaxCompute cluster fails, you can perform a primary/secondary switchover in the Apsara Big Data Manager (ABM) console to restore services. This topic describes the prerequisites and procedure of disaster recovery. In this topic, disaster recovery indicates zone-disaster recovery.

**Prerequisites**

The resource replication feature is disabled in the ABM console. To disable the feature, perform the following steps: i. Log on to the ABM console. ii. In the upper-left corner, click the icon and then **MaxCompute**. iii. In the left-side navigation pane of the **Business** tab, choose **Projects > Disaster**
**Recovery**.
iv. On the page that appears, turn off **Resource Synchronization Status**. The domain name of ABM is pointed to the IP address of the secondary ABM cluster. To point the domain name to the IP address, perform the following steps: i. Log on to the ABM console. ii. In the upper-left corner, click the icon and then **MaxCompute**. iii. On the MaxCompute page, click **Management** in the top navigation bar. In the left-side navigation pane of the page that appears, click **Jobs**. The **Jobs** tab appears by default. iv. Find the **Change Bcc Dns-Vip Relation For Disaster Recovery** job and click **Run** in the Actions column. The **Job Properties** section appears. v. Click the icon next to Group Name to configure the IP address of the Docker container.

> **Note:** NewBccAGIp indicates the IP address of the Docker container under AG# for the bcc-saas service of the secondary ABM cluster. You must configure an IP address at the #Docker# level.

In the dialog box that appears, click the **Servers** tab. Enter the IP address of a server in the field and click **Add Server**. Then, click **OK**. The IP address is configured. vi. In the upper-right corner, click **Run**. In the message that appears, click **Confirm**. vii. On the page that appears, click **Start** in the upper-right corner. The switchover starts.

> **Note:** If a step fails, click **Retry**. After all the steps are complete, the domain name of ABM is pointed to the IP address of the secondary ABM cluster.

The secondary ABM cluster page is accessible. If this page is inaccessible, go to the /usr/loca/bigdatak/controllers/bcc/tool/disaster_recovery directory of the Docker container in bcc-saa.AG# of the secondary ABM cluster. Then, run the `/home/tops/bin/python`

|   | script in the directory. If job success _ |
|---|---|

Then, run the `/home/tops/bin/python disaster_init.py` script in the current directory. If job_success appears, the execution succeeds. After the scripts are successfully run, you can go to the secondary cluster page.

> **Note:** If an exception occurs when you run the scripts, click **Retry**.

The Business Continuity Management Center (BCMC) switchover of MaxCompute is complete. The services on which MaxCompute depends are running normally. The services include AAS, Tablestore, and MiniRDS. By default, the data synchronization feature is disabled for MaxCompute projects because the computing and storage resources of the primary and secondary data centers are limited. To enable the data synchronization feature, submit a ticket.

**Background information**

Pay attention to the following points for a disaster recovery switchover: By default, the logon to Apsara Big Data Manager depends on the Apsara Uni-manager Operations Console. If the Apsara Uni-manager Operations Console has not reached the desired state, single sign-on is not supported. In this case, go to the /usr/loca/bigdatak/controllers/bcc/tool/disaster_recovery directory of the Docker container in bcc-saa.AG#. Then, run `change_login_by_bcc.sh` to switch the logon mode to the mode that is independent of the Apsara Uni-manager Operations Console. After the Apsara Unimanager Operations Console has reached the desired state, run `change_login_by_aso.sh` to switch the logon mode back to the mode that depends on the Apsara Uni-manager Operations Console. An exception may occur in each step of the switchover process. If an exception occurs, click **Retry**. If the retry succeeds, proceed to the next step. If the exception persists after multiple retries, contact O&M engineers to perform troubleshooting. Then, click **Retry** to complete the step. For each switchover, the Apsara distributed operating system of the original primary MaxCompute cluster must be restarted. Otherwise, the admintask service may be faulty after the switchover is complete. In the Collect Unsynchronized Data step, an exception shown in the following figure may occur. If this occurs, click **Recollect Unsynchronized Data**.

**Procedure**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and then **MaxCompute**.
3. In the left-side navigation pane of the **Business** tab, choose **Projects > Disaster**
**Recovery**.
4. In the upper-right corner, click **Switchover Process** to start the disaster recovery process.
5. Wait for resource replication to automatically stop.
Wait for resource replication to automatically stop. After **Next** becomes blue, click **Next**.

> **Note:** If an error occurs, click **Retry**. If the retry is invalid, contact O&M engineers to perform troubleshooting and try again.

6. Switch control clusters.
i. Wait for the primary/secondary switchover to complete for control clusters.

> **Note:** After the original primary cluster becomes the secondary cluster, the switchover is complete.

ii. Click **Restart Standby Cluster**.

> **Note:** The MaxCompute clusters become abnormal.

iii. After the MaxCompute clusters become normal, click **Restart Frontend Server** and wait until the restart result is returned. iv. After the restart succeeds, click **Test adminTask**.

> **Note:** If an exception occurs, click **Retry** and then **Test adminTask**. Alternatively, repeat from Step 6.b.

v. After **Next** becomes blue, click **Next**.

> **Note:** The **Switching** message remains displayed until the test succeeds.

7. Switch computing clusters.
The computing cluster switchover automatically starts for the projects that have two computing clusters. The switchover cannot be performed for the projects that have only one computing cluster. After the switchovers are complete for all the projects, click **Next**.

> **Note:** If the computing clusters of a project fail to be switched, contact O&M engineers to identify the cause of the exception. If the exception can be fixed, fix it and click **Retry** to continue the switchover. If the project is damaged or does not need a cluster switchover, click **Next** after you confirm that computing clusters of other projects are switched.

8. Switch the replication service to the secondary clusters.
The script is automatically run at the background. When a success message appears, click
**Next**.
9. Collect unsynchronized data.
i. Wait for the system to collect statistics on projects that contain unsynchronized data.

> **Note:** This step requires a long time to complete. The specific time depends on the data volume.

ii. After the collection is complete, click **Download Unsynchronized Data of Selected**
**Projects** to download the unsynchronized data to your computer.

> **Note:** The unsynchronized data that is obtained from this step is required for the **Manually Fill in Missing Data** step. The projects that are obtained from this step must be the same as those for the **Repair Metadata** and **Manually Fill in** **Missing Data** steps.

iii. After the unsynchronized data is downloaded, verify the data and click **Next**. If all data is synchronized, click **Next**.

> **Note:** If the unsynchronized data is abnormal, you can click **Recollect** **Unsynchronized Data**.

0. Repair metadata.
Select all projects, click **Repair Metadata of Selected Projects** , and then wait for results. If the metadata of some projects fails to be repaired, click **Download Last**
**Execution Log** and send the logs to O&M engineers. The logs can be used to identify and
analyze the cause of the exception. After the exception is fixed, repair the metadata of the projects again. If you do not need to repair the metadata of all projects, click **Next** after the metadata of required projects is repaired.
1. Manually supplement missing data.
Use DataWorks or the odpscmd client to manually supplement the missing data based on the unsynchronized data that you downloaded. After you supplement the missing data, select all projects and click **Confirm Data Repair Complete**. Then, click **Next**.
2. Repair unsynchronized resources.
i. Wait for the system to collect statistics on projects that contain unsynchronized resources.

> **Note:** This step requires a long time to complete. The specific time depends on the data volume.

ii. Use DataWorks or the odpscmd client to manually supplement the missing resources based on the unsynchronized resources that you collected. If an exception occurs, send exception information to O&M engineers to perform troubleshooting. After all the project resources are repaired, click **Complete and Next**.
3. Wait for resource replication to automatically start.
Wait for resource replication to automatically start. After **Next** becomes blue, click **Next**.
4. Exit the configuration wizard.
After the switchover is complete, click **Back** to exit the wizard.

##### 5.2.2.6 Migrate projects

Apsara Big Data Manager (ABM) allows you to migrate MaxCompute projects across regions from one cluster to another. This allows you to balance the computing and storage resources of each cluster.

> **Note:** The project migration feature is supported only when the clusters are deployed in multi-region mode.

**Create a project migration task**

1. In the left-side navigation pane of the **Business** tab, choose **Projects > Project**
**Migration**.
2. In the upper part of the **Migration Mission** page, select the region where the project
resides.
3. In the upper-right corner of the Migration Mission page, click **Create Mission**. On the
Create Migration Mission page, configure the parameters in the **General**, **Source**, **Target**
**Selection**, and **Cluster for Mission Execution** sections as prompted.
The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Source | Source Cluster | The name of the source cluster. Select a cluster from the drop-down list. |
|   | Quota Group | The quota group of the source cluster. Select a quota group from the drop-down list. |
|   | projectList | The projects that you want to migrate. After you configure the Quota Group parameter, all projects in the quota group are automatically loaded. You can migrate the projects at a time. If specific projects in the quota group do not need to be migrated, you can remove the projects based on your business requirements. |
| Target Selection | Copy Source Quota Group | Specifies whether the destination cluster uses the same quota group as the source cluster. If you enable this feature, you cannot configure the Target Quota Group parameter. |
|   | Change Tunnel Routing Address | Specifies whether to use a new Tunnel route. Tunnel provides highly concurrent upload and download services for offline data. Each project has a default Tunnel route. If you want to use a new Tunnel route after a project is migrated to a new cluster, enable Change Tunnel Routing Address and specify the new Tunnel route. |
| Document Version: | 20250126 7 |   |

|   | PanguVolume Target Server | Specifies whether the destination Apsara Distributed File System volume can be specified. Cross-volume project migration is not supported. Set this parameter to No. |
|---|---|---|
| Cluster for Mission Execution | Cluster | Source Cluster: the source cluster pushes the project to the destination cluster. Target Cluster: the destination cluster pulls the project from the source cluster. |

4. Click **Preview** to preview project migration details.
5. After you confirm the configuration, click **Start Planning** in the upper-left corner. Then, a
project migration task is generated and the migration details appear. The task may require a long period of time to be generated. In most cases, a standard project migration task includes five steps: i. **Add Target Cluster**: Add the destination cluster to the cluster list of the project that you want to migrate. ii. **Start to Replicate**: Replicate the project from the source cluster to the destination cluster. iii. **Switch Default Cluster**: Change the default cluster of the project to the destination cluster. After the default cluster is changed, generated data is written to the destination cluster. iv. **Clear Replication**: Clear the data replication list. During project migration, the migrated project in the source cluster and the corresponding project in the destination cluster synchronize data based on the data replication list. This ensures data consistency between the two projects. Data is continuously synchronized until the data replication list is cleared. v. **Remove Source Cluster**: Delete the migrated project from the source cluster. For more information about how to modify a task after the task is generated, see Modify a project migration task.

**Run the project migration task**

After the project migration task is created, you can run the task on the **Migration Details** page.
1. Click the task name in the task list to go to the **Migration Details** page.
2. On the **Migration Details** page, click **Submit for Execution**.
After the project migration task starts to run, the system automatically runs the **Add**
**Target Cluster** and **Start to Replicate** steps in sequence.
If you migrate multiple projects at a time, the process requires many steps to complete. Therefore, we recommend that you sort the steps by **project** to view the migration steps for each project. If the **status** of a step is **Success**, the step is complete. If the status of a step is **Failed**, the step fails. In the migration process, specific steps can be run only after you click **OK**. If you do not need to perform a step, click **Skip**. If you want to **confirm** or **skip** multiple steps at a time, select the steps and click **OK** or **Skip** in the upper-left corner of the Migration Details page. You can also click the **status** of a migration step for a project. In the dialog box that appears, click **Yes** to skip the remaining steps.
3. After the **Start to Replicate** step is complete, check the difference in data volumes
between the migrated project in the source cluster and the corresponding project in the destination cluster.

> **Important:** We recommend that you run the next step only when the difference in data volumes does not exceed 5%.

To check the data volume of a project, log on to the admingateway host in the cluster in which the project resides and run the **pu dirmeta**
**/product/aliyun/odps/${project_name}/** command.
4. If the difference in data volumes does not exceed 5%, perform one of the following
operations: Change the default cluster: Click **OK** in the Actions column of the **Switch Default**
**Cluster** step. After you perform this operation, the destination cluster becomes the
default cluster of the migrated project. In this example, the default cluster is changed. Do not change the default cluster: Click **Skip** in the Actions column of the **Switch**
**Default Cluster** step. After you perform this operation, the source cluster is still used as
the default cluster of the project. After the default cluster is changed, generated data is written to the destination cluster.

> **Warning:** During project migration, the migrated project in the source cluster and the corresponding project in the destination cluster synchronize data based on the data replication list to ensure data consistency. A long period of time is required to complete data synchronization. Therefore, after the default cluster is changed, we recommend that you wait for about one week before you proceed to the next step.

5. Wait for about one week and check whether the data volume of the migrated project in the
source cluster is the same as that of the corresponding project in the destination cluster. To check the data volume of a project, log on to the admingateway host in the cluster in which the project resides and run the **pu dirmeta**
**/product/aliyun/odps/${project_name}/** command.

> **Warning:** Before you proceed to the next step, make sure that the data volume of the migrated project in the source cluster is the same as that of the corresponding project in the destination cluster. Otherwise, data may be lost.

6. To retain the migrated project in the source cluster, click **Skip** in the Actions column of the
**Remove Source Cluster** step before you perform the **Clear Replication** step.
7. After the data volume of the migrated project in the source cluster becomes the same as
that of the project in the destination cluster, click **OK** in the Actions column of the **Clear**
**Replication** step to clear the data replication list.
After the data replication list is cleared, data is no longer synchronized between the migrated project in the source cluster and the corresponding project in the destination cluster. The system automatically runs the **Remove Source Cluster** step to delete all migrated projects from the source cluster. This releases storage and computing resources.

**View migration details**

You can view the details of a project migration task, including the steps, results, and debugging information.
1. If multiple migration tasks exist, search for a task or filter tasks on the **Migration Mission**
page. Filter tasks: Select a task state from the **Filter out Mission By** drop-down list. All tasks in this state are automatically filtered from the migration task list. Search for a task: Enter the name of a migration task in the search box in the upper-right corner and click the search icon to **search for the task**.
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

#### 5.2.3 Manage quota groups

Apsara Big Data Manager (ABM) shows the quota groups of all projects in a MaxCompute cluster. You can create and modify quota groups. You can also view details about quota groups and enable period management for quota groups.

**Go to the Quota Groups page**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and then select **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Business**
tab. In the left-side navigation pane of the tab that appears, click **Quota Groups**. Then, click **Quota Groups** or **Periods** based on your business requirements.

**Add a quota group**

In the upper-right corner of the **Quota Groups** page, click **Create Quota Group**. In the panel that appears, configure the parameters and click **Run**.

| Parameter | Description |
|---|---|
| Cluster | The cluster of the quota group that you want to create. |
| Quota Group | The name of the quota group that you want to create. |
| Preemption Policy | The preemption policy of the quota group. Valid values: No Preemption and Preemption. Default value: No Preemption. |
| Scheduling Type | The type of resource scheduling. Valid values: First In, First Out and Average. Default value: First In, First Out. |
| Minimum CUs | The minimum number of compute units (CUs) that are provided by the quota group. |
| Maximum CUs | The maximum number of CUs that are provided by the quota group. |
| CPU-to-Memory Ratio | The ratio of CPUs to memory of hosts in the quota group. |

**Modify a quota group**

On the **Quota Groups** page, find the quota group that you want to modify and click **Modify** in the Actions column. In the panel that appears, modify the settings and click **Run**.

> **Note:** If period management has been enabled for the quota group that you want to modify, first modify the period management configuration.

**View details about a quota group**

On the **Quota Groups** page, find the quota group whose details you want to view and click
**Details** in the Actions column. Then, you can view information about the resource usage,
resource analysis, and time-specific configuration management of the quota group.

**Enable time-specific configuration management for a quota**

**group**

1. On the **Periods** page, find the quota group for which you want to enable time-specific
configuration management and click **Period Management** in the Actions column.
2. On the **Period Management** tab, click **Set Periods**. In the dialog box that appears,
specify Period and click **Use TimeSet**.

> **Note:** You can click **Add** to specify more than one period or **Delete** to delete a period.
> For a quota group for which time-specific configuration management is enabled, you can click **Edit** in the Actions column. In the **Modify Period Configuration** panel, modify the parameters of the quota group within the specified period.

3. To disable time-specific configuration management for a quota group, click **Set Periods**
again. In the dialog box that appears, click **Close TimeSet**.

#### 5.2.4 Job management

##### 5.2.4.1 Manage job snapshots

The job snapshot feature allows you to manage the tasks that are created in MaxCompute and the merge tasks that are created in Apsara Big Data Manager (ABM). You can also view the LogView information of jobs, terminate jobs, and collect job logs.

**View job snapshots**

You can view job snapshots by day in the previous week. The information about a job snapshot includes the job ID, project, quota group, submitter, duration, minimum and maximum CPU utilization, minimum and maximum memory usage, DataWorks node, status, start time, priority, and type. You can also view the run logs of a job to identify errors.
1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the **Business** tab. In the left-side navigation pane, choose **Jobs > Job Snapshots** to go to the **Job Snapshots** page.
2. In the upper-right corner of the Job Snapshots page, specify the date and time when the job
snapshots that you want to view are generated.
3. Click the **All**, **Running**, **Waiting for Resources**, or **Initializing** tab to view job snapshots
in the corresponding state.
4. Find the job snapshot whose information you want to view and click **Logview** in the Actions
column. In the Generate Logview dialog box, click **Run** to view the LogView information of the job.

**Terminate jobs**

1. In the left-side navigation pane of the **Business** tab, choose **Jobs > Job Snapshots** to go
to the **Job Snapshots** page.
2. Select one or more jobs and click **Terminate Job** above the snapshot list. In the Terminate
Job panel, the information about the jobs that you want to terminate is displayed.
3. After you confirm the information, click **Run**. After you click Run, a message that indicates
the results appears.

**Collect job logs**

If an exception occurs during the running of a job, you can collect job logs to identify and analyze the exception.
1. In the left-side navigation pane of the **Business** tab, choose **Jobs > Job Snapshots** to go
to the **Job Snapshots** page.
2. In the upper-right corner of the **Job Snapshots** page, move the pointer over **Actions** and
select **Collect Job Logs**.
3. In the **Collect Job Logs** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Service Role | The services from which you want to collect job logs. You can select one or more services. |
| instanceid | Optional. The job ID. |
| requestid | Optional. The request ID returned when the job fails. If the value that you specify is not a request ID, job logs that contain the specified value are collected. |
| Time Period | The time range to collect job logs. |
| Time Interval | Optional. The time interval to collect job logs. Unit: hours. |

4. Click **Run** to start the collection of job logs.
5. View the status and progress of job log collection.
In the upper-right corner of the **Job Snapshots** page, move the pointer over **Actions** and select **Execution History** next to **Collect Job Logs**. In the **Execution History** panel, view the status and history of job log collection.
**RUNNING** indicates that job logs are being collected. **SUCCESS** indicates that job logs are
collected. **FAILED** indicates that job logs fail to be collected. If a record of job log collection is in the **RUNNING** state, you can click **Details** in the Details column to view the progress of job log collection.
6. View the path to store job logs.
In the **Execution History** panel, find a record of job log collection in the SUCCESS state and click **Details** in the Details column. In the Collect Job Logs section, find the odps_worker_collect module and click View Details to view the path in which the collected job logs are stored.

#### 5.2.5 Business optimization

##### 5.2.5.1 Merge small files

Excessive small files in a MaxCompute cluster occupy a lot of memory resources. Apsara Big Data Manager (ABM) allows you to merge multiple small files in MaxCompute clusters and projects to free up the memory occupied by these files.

**Create a merge task for a cluster**

If excessive small files exist in most projects of a MaxCompute cluster, you can create a merge task to merge these files in the cluster in a centralized manner.
1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the Business tab. On the **Business** tab, choose **Business Optimization > File**
**Merging** in the left-side navigation pane. The **Merge Tasks** tab appears.
2. In the **Merge Tasks for Clusters** section, click **Create Merge Task**. In the Modify Merge
Task for Cluster panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Cluster | The cluster for which you want to run the merge task. Select a cluster from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of merge tasks for the cluster. Valid values: Yes: limits the concurrency. Merge tasks cannot be concurrently run. No: does not limit the concurrency. Merge tasks can be concurrently run. |
| Maximum Concurrent Tasks | The maximum number of merge tasks that can be concurrently run for the selected cluster. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |
| Enabled | Specifies whether to enable the task. |

| Merge Parameters | The configurations for the merge task. You can use the following default configurations: { "odps.idata.useragent": "SRE Merge", "odps.merge.cpu.quota": "75", "odps.merge.quickmerge.flag": "true", "odps.merge.cross.paths": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.maintain.order.flag": "true", "odps.merge.failure.handling": "any" } |
|---|---|
| Maximum Running Jobs | The maximum number of jobs that can be concurrently run for the selected cluster. This parameter is a global parameter. The jobs refer to all types of jobs in the selected cluster. |

3. Click **Compare Versions** below the **Merge Parameters** parameter to view the differences
between the original and modified values.
4. Click **Run**.
The merge task that you create appears in the Merge Tasks for Clusters section.

**Create a merge task for a project**

If excessive small files exist in only a few projects of a MaxCompute cluster, you can create a merge task to merge the small files in a specific project.
1. On the **Business** tab, choose **Business Optimization > File Merging** in the left-side
navigation pane. The **Merge Tasks** tab appears.
2. In the **Merge Tasks for Projects** section, click **Create Merge Task**. In the Modify Merge
Task for Project panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region | The region in which the selected project resides. Select a region from the drop- down list. |
| Project Name | The name of the project for which you want to run the merge task. Select a project from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Priority | The priority of the task. A smaller value specifies a higher priority. |
| Enabled | Specifies whether to enable the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of merge tasks for the project. Valid values: Yes: limits the concurrency. Merge tasks cannot be concurrently run. No: does not limit the concurrency. Merge tasks can be concurrently run. |
| Maximum Concurrent Tasks | The maximum number of merge tasks that can be concurrently run for the selected project. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |

| Maximum Running Jobs | The maximum number of jobs that can be concurrently run for the selected project. This parameter is a global parameter. The jobs refer to all types of jobs in the selected project. |
|---|---|

3. Click **Run**.
The merge task that you create appears in the Merge Tasks for Projects section.

**View merge task statistics**

On the **Business** tab, choose **Business Optimization > File Merging** in the left-side navigation pane. Then, click the **Historical Statistics** tab to view the historical statistics of merge tasks for clusters and projects.

**Merge Tasks**

In the Merge Tasks section, the statistics on all merge tasks for each day in the previous month are displayed in a trend chart. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that time out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes.

**Merge Tasks for Clusters and Merge Tasks for Projects**

In the Merge Tasks for Clusters and Merge Tasks for Projects sections, the statistics on merge tasks for clusters and projects on a specific day in the previous month are displayed in tables. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that time out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes.

**Manage merge types**

On the **Business** tab, choose **Business Optimization > File Merging** in the left-side navigation pane. Then, click the **Merge Types** tab to view the existing merge types and merge parameters.

**Create a merge type**

1. In the **Merge Tasks** section, click **Create Merge Type**. In the Modify Merge Type panel,
configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Merge Type | The name of the merge type. |
| Merge Parameters | The merge parameters of the merge type. |

2. Click **Compare Versions** below the **Merge Parameters** parameter to view the differences
between the original and modified values.
3. Click **Run**.
The merge type that you create appears in the Merge Tasks section.

##### 5.2.5.2 Compress idle files

Apsara Big Data Manager (ABM) allows you to create archive tasks to compress idle files in MaxCompute clusters and projects. This saves storage space for the clusters.

**Definition**

In a cluster, ABM sorts the tables or partitions created for more than 90 days by storage space and compresses the first 100,000 tables or partitions.

**Create an archive task for a cluster**

If excessive idle files exist in most projects of a MaxCompute cluster, you can create an archive task to compress these idle files in the cluster in a centralized manner.
1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the Business tab. On the **Business** tab, choose **Business Optimization > File**
**Archiving** in the left-side navigation pane. The **Archive Tasks** tab appears.
2. In the **Archive Tasks for Clusters** section, click **Create Archive Task**. In the Modify
Archive Task for Cluster panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Cluster | The cluster for which you want to run the archive task. Select a cluster from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of archive tasks for the cluster. Valid values: Yes: limits the concurrency. Archive tasks cannot be concurrently run. No: does not limit the concurrency. Archive tasks can be concurrently run. |

| Maximum Concurrent Jobs | The maximum number of archive tasks that can be concurrently run for the selected cluster. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |
|---|---|
| Enable | Specifies whether to enable the task. |
| Maximum Running Jobs | The maximum number of jobs that can be concurrently run for the selected cluster. This parameter is a global parameter. The jobs refer to all types of jobs in the selected cluster. |
| Archive Parameters | The configurations for the archive task. You can use the following default configurations: { "odps.idata.useragent": "SRE Archive", "odps.oversold.resources.ratio": "100", "odps.merge.quickmerge.flag": "true", "odps.merge.cross.paths": "true", "odps.merge.smallfile.filesize.threshold": "4096", "odps.merge.maxmerged.filesize.threshold": "4096", "odps.merge.max.filenumber.per.instance": "10000", "odps.merge.max.filenumber.per.job": "10000000", "odps.merge.maintain.order.flag": "true", "odps.sql.hive.compatible": "true", "odps.merge.compression.strategy": "normal", "odps.compression.strategy.normal.compressor": "zstd", "odps.merge.failure.handling": "any", "odps.merge.archive.flag": "true" } |

3. Click **Compare Versions** below the Archive Parameters parameter to view the differences
between the original and modified values.
4. Click **Run**.
The archive task that you create appears in the Archive Tasks for Clusters section.

**Create an archive task for a project**

If excessive idle files exist in only a few projects of a MaxCompute cluster, you can create an archive task to compress the idle files in a specific project.

> **Note:** If the tables or partitions of a project are not the first 100,000 idle files in the cluster in which the project resides, an archive task cannot compress the idle files in the project.

1. On the **Business** tab, choose **Business Optimization > File Archiving** in the left-side
navigation pane. The **Archive Tasks** tab appears.
2. In the **Archive Tasks for Projects** section, click **Create Archive Task**. In the Modify
Archive Task for Project panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region | The region in which the selected project resides. Select a region from the drop- down list. |
| Project Name | The name of the project for which you want to run the archive task. Select a project from the drop-down list. |
| Start Time | The start time of the task. |
| End Time | The end time of the task. |
| Priority | The priority of the task. A smaller value specifies a higher priority. |
| Enable | Specifies whether to enable the task. |
| Bandwidth Limit | Specifies whether to limit the concurrency of archive tasks for the project. Valid values: Yes: limits the concurrency. Archive tasks cannot be concurrently run. No: does not limit the concurrency. Archive tasks can be concurrently run. |

| Maximum Concurrent Jobs | The maximum number of archive tasks that can be concurrently run for the selected project. This parameter takes effect only when the Bandwidth Limit parameter is set to No. |
|---|---|
| Maximum Running Jobs | The maximum number of jobs that can be concurrently run for the selected project. This parameter is a global parameter. The jobs refer to all types of jobs in the selected project. |

3. Click **Run**.
The archive task that you create appears in the Archive Tasks for Projects section.

**View archive task statistics**

On the **Business** tab, choose **Business Optimization > File Archiving** in the left-side navigation pane. Then, click the **Historical Statistics** tab to view the historical statistics of archive tasks for clusters and projects.

**Archive Tasks**

In the Archive Tasks section, the statistics on all archive tasks for each day in the previous month are displayed in a trend chart. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that time out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes.

**Statistics by Cluster and Statistics by Project**

In the Statistics by Cluster and Statistics by Project sections, the statistics on archive tasks for clusters and projects on a specific day in the previous month are displayed in tables. You can view the numbers of running tasks, finished tasks, waiting tasks, tasks that time out, failed tasks, invalid tasks, merged partitions, and reduced files, and saved storage space in bytes.

**Manage archive types**

On the **Business** tab, choose **Business Optimization > File Archiving** in the left-side navigation pane. Then, click the **Archive Types** tab to view the existing archive types and archive parameters.

**Create an archive type**

1. In the **Archive Tasks** section, click **Create Archive Type**. In the Modify Archive Type
panel, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Archive Type | The name of the archive type. |
| Archive Parameters | The archive parameters of the archive type. |

2. Click **Compare Versions** below the **Archive Parameters** parameter to view the
differences between the original and modified values.
3. Click **Run**.
The archive type that you create appears in the Archive Tasks section.

##### 5.2.5.3 Analyze resources

Apsara Big Data Manager (ABM) allows you to analyze the resources of MaxCompute clusters from multiple dimensions to help you better understand the data stored in MaxCompute. You can view the analysis results of data storage on the Tables, Projects, Tasks, Execution Time, Start Time, and Engines tabs.

**Tables**

On the Tables tab, you can view the detailed information about all tables in each project, including the number of partitions, physical storage usage, and number of Apsara Distributed File System files of each table, and the rankings based on the number of partitions, physical storage usage, and number of Apsara Distributed File System files. You can also sort tables by number of partitions, physical storage usage, and number of Apsara Distributed File System files. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then, click the Business tab. On the **Business** tab, choose **Business Optimization > Resource**
**Analysis** in the left-side navigation pane. The **Tables** tab appears.

**Projects**

On the Projects tab, you can view the detailed information about the data stored in each project, including the number of Apsara Distributed File System files, physical storage usage, capacity unit (CU) usage, total memory usage, number of tasks, number of tables, and idle storage space of each project. You can also view the daily and weekly percentage by which the value of each metric is increased. In the left-side navigation pane of the **Business** tab, choose **Business Optimization >**
**Resource Analysis**. On the page that appears, click the **Projects** tab.

**Tasks**

On the Tasks tab, you can view the detailed information about all tasks in each project, including the instance ID, status, CU usage, start time, end time, duration, ranking of CU usage, and SQL statements of each task. In the left-side navigation pane of the **Business** tab, choose **Business Optimization >**
**Resource Analysis**. On the page that appears, click the **Tasks** tab.

**Execution Time**

On the Execution Time tab, you can view the numbers of tasks that consume less than 5 minutes, less than 15 minutes, less than 30 minutes, less than 60 minutes, and more than 60 minutes. In the Execution Time chart, the numbers of tasks of each day in the specified time period are displayed in different colors to show the trends of tasks of different durations. In the left-side navigation pane of the **Business** tab, choose **Business Optimization >**
**Resource Analysis**. On the page that appears, click the **Execution Time** tab.

**Start Time**

On the Start Time tab, you can view the numbers of tasks that start in different time periods for each project. The time interval is 30 minutes. In the Tasks chart, the numbers of tasks that start in different time periods of each day in the specified time period are displayed. In the left-side navigation pane of the **Business** tab, choose **Business Optimization >**
**Resource Analysis**. On the page that appears, click the **Start Time** tab.

**Engines**

On the Engines tab, you can view the trends of performance metrics of tasks in each project in the Task Performance Analysis chart. The performance metrics include cost_cpu, cost_mem, cost_time, input_bytes, input_bytes_per_cu, input_records, input_records_per_cu, odps_job_num, output_bytes, output_bytes_per_cu, output_records, and output_records_per_cu. In the left-side navigation pane of the **Business** tab, choose **Business Optimization >**
**Resource Analysis**. On the page that appears, click the **Engines** tab.

### 5.3 Service O&M

#### 5.3.1 Control service O&M

##### 5.3.1.1 O&M features and page

This topic describes the O&M features for the control service and how to go to the O&M page.

**O&M features**

On the Overview tab, the overall information about the control service is displayed. You can view the summary of services, service role status, job statistics, statistics on the executor thread pool, and the trend chart of job latency. On the Service Roles tab, the information about the service roles of the control service is displayed. You can view the host, status, requested CPU resources, and requested memory of each service role. On the Configuration Management tab, you can modify the configurations of global computing, cluster-level computing, computing scheduling, and cluster endpoints. On the Metadata Repository tab, the information about the metadata repository of MaxCompute is displayed. You can view the generation time and status of the metadata repository and the trend chart of generation during a specific period of time. In the upper-right corner of the Control page, you can move the pointer over Actions and select Start Service Role or Stop Service Role to enable or disable a service role of MaxCompute, or select Execution History to view the operation history. If you fail to start or stop a service role, you can identify the cause of the failure. In the upper-right corner of the Control page, you can move the pointer over Actions and select Start Admin Console to start AdminConsole. In the upper-right corner of the Control page, you can move the pointer over Actions and select Collect Service Logs to collect service logs and identify the cause of service failures.

**Go to the O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute**.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Control**. The **Overview** tab for
the control service appears.

##### 5.3.1.2 Overview

On the Overview tab, the overall information about the control service is displayed. You can view the summary of services, service role status, job statistics, statistics on the executor thread pool, and the trend chart of job latency.

**Go to the Overview tab**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Control** in the left-side navigation pane. The **Overview** tab for the control service appears.

**Services**

In the Services section, the numbers of available services and unavailable services are displayed.

**Service Status**

In the Service Status section, all control service roles are displayed. You can also view the numbers of available services and unavailable services for each service role.

**Traffic - Jobs**

In the Traffic - Jobs section, the statistics on jobs in the selected cluster are displayed. You can view the total number of jobs in the cluster, number of jobs that are running, number of jobs that are waiting for resources, and number of jobs that are waiting for scheduling.

**Saturability - Executor Pool Size**

In the Saturability - Executor Pool Size section, the information about the thread pool is displayed. You can view the resource usage, number of jobs being processed, queue length, and maximum concurrency.

**Latency - Waiting Jobs**

In the Latency - Waiting Jobs section, the trend chart of jobs is displayed. The chart displays the trend lines of the numbers of jobs that are running, jobs that are waiting for resources, and jobs that are waiting for scheduling in different colors. You can click the icon in the upper-right corner of the chart to zoom in on the trend chart and specify the time range during which you want to view the trends.

##### 5.3.1.3 Control server roles

The Server Roles tab on the Control page shows information about the roles of the control service. You can view the host, status, requested CPU resources, and requested memory of each role.

**Go to the Server Roles tab**

In the left-side navigation pane of the **Services** page, click **Control**. Then, click the **Server**
**Roles** tab.

##### 5.3.1.4 Control service configuration

The Configuration page under Control is the access to configuring global computing, clusterlevel computing, computing scheduling, and cluster endpoints. If you want to modify the configurations of the control service, submit a ticket to apply for technical support, and then modify the configurations carefully under the guidance of technical support engineers. In the left-side navigation pane of the **Services** tab, click **Control**. Then, click the
**Configuration** tab.
The **Configuration** page consists of the following tabs: Computing: provides the Global Computing, Cluster Computing, and Compute Scheduling tabs. Tunnel Routing Address: provides the Cluster Endpoints tab.

##### 5.3.1.5 Metadata warehouse for the control service

**service**

This topic describes how to view the completion time and status of the output tasks of the metadata warehouse and the trend chart of the consumed time for running tasks in MaxCompute. The metadata warehouse in MaxCompute regularly runs output tasks every day. Apsara Big Data Manager (ABM) obtains the status of output tasks every 30 minutes. If an output task of the metadata warehouse is not complete within 24 hours, the output task is regarded as a failure. In the left-side navigation pane of the **Services** tab, click **Control**. On the page that appears, click the **Metadata Repository** tab. The **Metadata Repository** tab displays the completion time of the output tasks of the metadata warehouse and the trend chart of the consumed time for running tasks. The time displayed in the **Completed At** column indicates the time when an output task is complete. The time displayed in the **Collected At** column indicates the last time at which ABM obtains the status of output tasks.

##### 5.3.1.6 Stop or start a service role

Apsara Big Data Manager (ABM) allows you to start or stop the service roles of the MaxCompute control service and view the operation history. If you fail to start or stop a service role, you can identify the cause of the failure.

**Stop a service role**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Control**. On the Overview tab,
move the pointer over **Actions** in the upper-right corner and select **Stop Service Role**.
5. In the Stop Service Role panel, select the service role that you want to stop and click **Run**.
6. Move the pointer over **Actions** in the upper-right corner and select **Execution History**
next to **Stop Service Role**. In the Execution History panel, check whether the operation is successful. In the Execution History panel, you can view the status, submission time, start time, end time, operator, type, and parameters of each operation.
7. In the Execution History panel, you can find an operation record and click **Details** in the
Details column to view the details. In the details panel, you can view the job name, status, steps, script, and parameter settings. You can also download the details to your on-premises computer.

**Start a service role**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Control**. On the Overview tab,
move the pointer over **Actions** in the upper-right corner and select **Start Service Role**.
5. In the Start Service Role panel, select the service role that you want to start and click **Run**.
6. Move the pointer over **Actions** in the upper-right corner and select **Execution History**
next to **Start Service Role**. In the Execution History panel, check whether the operation is successful. In the Execution History panel, you can view the status, submission time, start time, end time, operator, type, and parameters of each operation.
7. In the Execution History panel, you can find an operation record and click **Details** in the
Details column to view the details. In the details panel, you can view the job name, status, steps, script, and parameter settings. You can also download the details to your on-premises computer.

**Identify the cause of a failure**

This section describes how to identify the cause of the failure to start a service role.
1. On the Overview tab, move the pointer over Actions in the upper-right corner and select
Execution History next to Start Service Role. In the Execution History panel, find a failed operation record and click **Details** in the Details column to view the details.
2. In the Start Service Role panel, find a failed step and click **View Details** to identify the
cause of the failure. You can view the parameter settings, outputs, error messages, script, and runtime parameters to identify the cause of the failure.

##### 5.3.1.7 Start AdminConsole

AdminConsole is a management platform of MaxCompute and is disabled by default. Apsara Big Data Manager (ABM) allows you to quickly start AdminConsole to manage MaxCompute clusters in an efficient manner.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Step 1: Start AdminConsole**

2. In the upper-left corner, click the
icon and click **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Control**.
5. In the upper-right corner of the page that appears, choose **Actions > Start Admin**
**Console**.
6. In the **Start Admin Console** panel, click **Run**.

**Step 2: View the execution status or progress**

1. On any tab of the **CONTROL** page, click **Actions** and select **Execution History** next to
**Start Admin Console** in the upper-right corner to view the execution history.
**RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the
execution succeeds. **FAILED** indicates that the execution fails.
2. In the Execution History panel, click **Details** in the Details column to view the execution
progress if the status is **RUNNING**.

**Step 3: (Optional) Identify the cause of a failure**

If the status is **FAILED**, you can view the execution logs to identify the cause of the failure.
1. On any tab of the **CONTROL** page, click **Actions** and select **Execution History** next to
**Start Admin Console** in the upper-right corner to view the execution history.
2. In the Execution History panel, click **Details** in the Details column of the task to view the
details.
3. On the **Servers** tab of the failed step, click **View Details** in the Actions column of a failed
server. The **Execution Output** tab appears in the Execution Details section. You can view the output to identify the cause of the failure.

##### 5.3.1.8 Collect service logs

Apsara Big Data Manager (ABM) allows you to collect service logs that are generated during a specific period of time to identify the cause of a failure.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Step 1: Collect service logs**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Control**.
5. On the Control page, move the pointer over **Actions** in the upper-right corner and select
**Collect Service Logs**.
6. In the **Collect Service Logs** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Target Service | The service from which you want to collect service logs. You can select one or more services from the drop-down list. |
| Time Period | The time period during which the logs that you want to collect are generated. |

| Hostname | The name of the host. Separate multiple hostnames with commas (,). |
|---|---|

7. Click **Run**.

**Step 2: View the status or progress**

1. On the **Control** page, move the pointer over **Actions** in the upper-right corner and select
**Execution History** next to **Collect Service Logs** to view the history of service log
collection.
**RUNNING** indicates that service logs are being collected. **SUCCESS** indicates that service
logs are collected. **FAILED** indicates that service logs fail to be collected.
2. If a record of service log collection is in the **RUNNING** state, click **Details** in the Details
column to view the progress of service log collection.

**Step 3: (Optional) Identify the cause of a failure**

If a record of service log collection is in the **FAILED** state, you can view the logs to identify the cause of the failure.
1. On the **Control** page, move the pointer over **Actions** in the upper-right corner and select
**Execution History** next to **Collect Service Logs** to view the history of service log
collection.
2. In the Execution History panel, find a failed record and click **Details** in the Details column
to view the details.
3. On the **Servers** tab of the failed step, click **View Details** in the Actions column. The
**Execution Output** tab appears in the Execution Details section. You can view the output
to identify the cause of the failure.

#### 5.3.2 Job Scheduler O&M

##### 5.3.2.1 O&M features and page

This topic describes the O&M features for Job Scheduler and how to go to the O&M page.

**O&M features**

On the Overview tab, the key information about the operations of Job Scheduler is displayed. You can view the summary of services, service role status, statistics on resource allocation, statistics on compute nodes, and the trend charts of CPU utilization and memory usage. On the Service Roles tab, the information about the master nodes and service roles of Job Scheduler is displayed. You can restart the master nodes of Job Scheduler on this tab. On the Compute Nodes tab, the information about the compute nodes of Job Scheduler is displayed. You can manage the blacklist of compute nodes and the read-only permissions on this tab. In the upper-right corner of the Fuxi page, you can move the pointer over Actions and select Enable SQL Acceleration or Disable SQL Acceleration to enable or disable the SQL acceleration mode for Job Scheduler. You can also restart the primary and secondary master nodes.

**Go to the O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute**.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Fuxi**. The **Overview** tab for Job
Scheduler appears.

##### 5.3.2.2 Overview

On the Overview tab, the key information about the operations of Job Scheduler is displayed. You can view the summary of services, service role status, statistics on resource allocation, statistics on compute nodes, and the trend charts of CPU utilization and memory usage.

**Go to the Overview tab**

1. Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top
navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Fuxi** in the left-side navigation pane.
2. On the Fuxi page, select a cluster and click the **Overview** tab. The **Overview** tab for Job
Scheduler of the selected cluster appears.

**Services**

In the Services section, the numbers of available services, unavailable services, and services that are being updated are displayed.

**Service Status**

In the Service Status section, all service roles of Job Scheduler and their status are displayed. You can also view the number of physical servers on which each service role is deployed and the number of physical servers at desired state for each service role. Click the name of a service role to go to the Apsara Infrastructure Management console and view the details of the service role.

**Trend for Resource Usage**

In the Trend for Resource Usage section, the trend charts of CPU utilization and memory usage for Job Scheduler are displayed. Each trend chart provides information about the used quota, minimum quota, maximum cluster quota, requested quota, and maximum quota in different colors. The trend charts are periodically refreshed. You can also manually refresh the trend charts. You can also view the trend charts of CPU utilization and memory usage within a specific period of time.

**Saturability - Resource Usage**

In the Saturability - Resource Usage section, the statistics on the allocation of CPU and memory resources are displayed. In the CPU (Core) section, you can view the CPU utilization, the total number of CPU cores, the number of available CPU cores, and the number of CPU cores for SQL acceleration. In the Memory (Bytes) section, you can view the memory usage, the total memory size, the available memory size, and the memory size for SQL acceleration.

**Compute Nodes**

In the Compute Nodes section, the information about compute nodes is displayed. You can view the percentage of online compute nodes, the total number of compute nodes, the number of online compute nodes, and the number of compute nodes that are added to the blacklist.

##### 5.3.2.3 Manage service roles

This topic describes how to view the master nodes and service roles of Job Scheduler, manage service roles, and restart master nodes.

**Go to the Service Roles tab**

1. Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top
navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Fuxi** in the left-side navigation pane.
2. On the Fuxi page, select a cluster and click the **Service Roles** tab. The **Service Roles** tab
for Job Scheduler of the selected cluster appears. On the **Service Roles** tab, the information about the master nodes and service roles of Job Scheduler is displayed. The information about a master node includes the IP address, hostname, service role, and start time. The information about a service role includes the role name, hostname, IP address, role status, and host status.

**Server roles**

| Service role | Description | Quantity | Form | High availability |
|---|---|---|---|---|
| FuxiMaster# | The master role of Job Scheduler. | Deployed on at least two physical servers. | Process | Yes |

| FuxiApiServer# | The API service role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
|---|---|---|---|---|
| PackageManager# | The package management role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
| Tubo# | The compute node role of Job Scheduler. | Deployed on at least three physical servers. | Process | Yes |
| DeployAgent# | The package delivery agent of Job Scheduler. | Deployed on at least three physical servers. | Process | Yes |
| FuxiDecider# | The approval role of Job Scheduler. | Deployed together with the master role on at least two physical servers. | Process | Yes |
| FuxiMonitor# | The monitoring role of Job Scheduler. | Deployed on each physical server. | Process | N/A |

**FuxiMaster#**

Service role description This service role does not depend on other service roles. This role is the master role of Job Scheduler. In most cases, the FuxiMaster# role is deployed on three physical servers. You must deploy the FuxiMaster# role on at least two physical servers. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiMaster#/fuxi_master` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**FuxiApiServer#**

Service role description This service role depends on the FuxiMaster# role. This role is the API service role of Job Scheduler. In most cases, the FuxiApiServer# role is deployed on three physical servers. You must deploy the FuxiApiServer# role on at least two physical servers. You can deploy the FuxiApiServer# role together with the FuxiMaster# role. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory:

```
 /cloud/app/fuxi/FuxiApiServer#/fuxi_apiserver .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**PackageManager#**

Service role description This service role does not depend on other service roles. This role is used to manage the computing software packages of Job Scheduler. In most cases, the PackageManager# role is deployed on three physical servers. You must deploy the PackageManager# role on at least two physical servers. You can deploy the PackageManager# role together with the FuxiMaster# role. Make sure that at least one physical server on which this role is deployed works properly. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory:

```
 /cloud/app/fuxi/Packagemanager#/packagemanager .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**Tubo#**

Service role description This service role depends on the FuxiMaster# role. Physical servers on which this role is deployed serve as the compute nodes of Job Scheduler. You must deploy the Tubo# role on at least three physical servers. Computing tasks are scheduled to physical servers on which the Tubo# role is deployed. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/Tubo#/tubo` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**DeployAgent#**

Service role description This service role depends on the PackageManager# role. Physical servers on which this role is deployed serve as agents for deploying the computing software packages of Job Scheduler. You must deploy the DeployAgent# role on at least three physical servers. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/DeployAgent#/deploy_agent` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**FuxiDecider#**

Service role description This service role does not depend on other service roles. Physical servers on which this role is deployed are used to approve the requests for starting or shutting down the compute nodes of Job Scheduler. This role is required if you want to shut down a compute node. In most cases, the FuxiDecider# role is deployed on three physical servers. You must deploy the FuxiDecider# role on at least two physical servers. You can deploy the FuxiDecider# role together with the FuxiMaster# role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiDecider#/fuxi_decider` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**FuxiMonitor#**

Service role description This service role does not depend on other service roles. In most cases, the FuxiMonitor# role is deployed on each physical server of a cluster and is used to monitor all service roles of Job Scheduler that are deployed on each physical server. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/fuxi/FuxiMonitor#/fuxi_monitor` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**Supported operations**

You can restart the master nodes of Job Scheduler. For more information, see Restart a master node of Job Scheduler.

##### 5.3.2.4 Job Scheduler compute nodes

You can view the details of compute nodes on the Compute Nodes page for Job Scheduler, including the total CPU, idle CPU, total memory, and idle memory of each compute node. You can also check whether a node is added to the blacklist and whether it is active. You can also add compute nodes to or remove compute nodes from the blacklist or read-only list on the Compute Nodes page.

**Go to the Compute Nodes tab**

1. In the left-side navigation pane of the **Services** tab, click **Fuxi**.
2. Select a cluster, and click the **Compute Nodes** tab. The **Compute Nodes** tab for Job
Scheduler appears. On this tab, you can view the details of compute nodes, including the total CPU, idle CPU, total memory, and idle memory of each compute node. You can also check whether a node is added to the blacklist and whether the node is active.

**Blacklist and read-only setting**

You can add compute nodes to or remove compute nodes from the blacklist or read-only list. To add compute nodes to the blacklist, perform the following steps:
1. On the **Compute Nodes** tab, find the desired compute node and click **Add to Blacklist** in
the **Actions** column.
2. In the Add Compute Node to Blacklist panel, click **Run**. A message appears, indicating that
the action is submitted. The value of the **Hostname** parameter is automatically filled. You do not need to specify a value for this parameter. You can check whether a compute node is added to the **blacklist** in the compute node list after the configuration is complete.

##### 5.3.2.5 Enable and disable SQL acceleration

You can enable or disable SQL acceleration for Job Scheduler in the Apsara Big Data Manager (ABM) console. The execution speed of SQL statements in Job Scheduler is greatly increased with SQL acceleration enabled, but more computing resources are consumed.

**Enable SQL acceleration**

1. In the left-side navigation pane of the **Services** tab, click **Fuxi**. Then, select a cluster.
2. In the upper-right corner of the tab that appears, choose **Actions** > **Enable SQL**
**Acceleration**.
3. In the Enable SQL Acceleration panel, set the **WorkerSpans** parameter.
**WorkerSpans**: the default resource quota of the cluster and the resource quota for a
specific period. Default value: **default:2,12-23:2**.

> **Note:** The default value indicates that the default resource quota is 2 and the resource quota for the period from 12:00 to 23:00 is also 2. You can set the resource quota as needed. For example, you can set this parameter to default:2,12-23:4 to increase the resource quota in peak hours.

4. Click **Run**.

**Disable SQL acceleration**

1. In the left-side navigation pane of the **Services** tab, click **Fuxi**. Then, select a cluster.
2. In the upper-right corner of the tab that appears, choose **Actions** > **Disable SQL**
**Acceleration**.
3. In the Disable SQL Acceleration panel, click **Run**.

**View the execution history of enabling or disabling SQL**

**acceleration**

After you submit the action of enabling or disabling SQL acceleration, you can view the execution history to check whether the action is complete. The system executes the action as a job. It provides execution records and logs for each execution so that you can identify faults encountered during its execution. This section describes how to view the execution history of enabling SQL acceleration.
1. In the left-side navigation pane of the **Services** tab, click **Fuxi**. Then, select a cluster.
2. In the upper-right corner of the tab that appears, click **Actions** and select **Execution**
**History** next to **Enable SQL Acceleration**.
3. In the Execution History panel, view the execution history of enabling SQL acceleration.
The execution history shows the current status, submission time, start time, end time, and operator of each execution.
4. If the execution fails, click **Details** in the Details column to identify the cause of the failure.

##### 5.3.2.6 Restart a master node of Job Scheduler

Job Scheduler is the resource management and task scheduling system of the Apsara distributed operating system. Apsara Big Data Manager (ABM) allows you to quickly restart the primary and secondary master nodes of Job Scheduler. Cluster services are not affected during the restart process.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Step 1: Restart a master node of Job Scheduler**

2. In the upper-left corner, click the
icon and select **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tag, click **Fuxi**. On the page that appears,
click the **Server Roles** tab.
5. On the **Server Roles** tab, find a primary or secondary master node and click **Restart Fuxi**
in the **Actions** column.
6. In the **Restart Fuxi Master Node** panel, click **Run**. A message appears, indicating that
the job is submitted. The **Restart Fuxi Master Node** panel appears.

**Step 2: View the execution status or progress**

1. In the **Restart Fuxi Master Node** panel, check the execution history of restarting master
nodes of Job Scheduler. The **Restart Fuxi Master Node** panel displays the restart history. **RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the execution succeeds. **FAILED** indicates that the execution fails.
2. If the status is **RUNNING**, click **Details** in the Details column to view the execution
progress.

**Step 3: (Optional) Identify the cause of a failure**

If the status is **FAILED**, you can view the execution logs to identify the cause of the failure.
1. In the **Restart Fuxi Master Node** panel, check the execution history of restarting master
nodes of Job Scheduler.
2. Click **Details** in the Details column of the task to view the details.
3. On the **Servers** tab of the failed step, find a failed node and click **View Details** in the
Actions column. The **Execution Output** tab appears in the Execution Details section. You can view the output to identify the cause of the failure.

#### 5.3.3 Apsara Distribute File System O&M

##### 5.3.3.1 O&M features and page

This topic describes the O&M features for Apsara Distributed File System and how to go to the O&M page.

**O&M features**

On the Overview tab, the key information about the operations of Apsara Distributed File System is displayed. You can view the summary of services, service role status, statistics on storage usage, statistics on storage nodes, and the trend charts of storage usage and the number of files. On the Service Roles tab, the information about the master nodes and service roles of Apsara Distributed File System is displayed. You can change the primary master node or run a checkpoint on a master node of Apsara Distributed File System. On the Storage Management page, the information about the storage nodes of Apsara Distributed File System is displayed. You can set the status of a storage node to Disabled or Normal, or set the status of a disk on a storage node to Normal or Error. In the Master Status section of the Service Roles tab, you can find a master node and choose Actions > Change Primary Master Node in the Actions column to change the primary master node of Apsara Distributed File System in the selected cluster. In the Master Status section of the Service Roles tab, you can find a master node and choose Actions > Run Checkpoint on Master Node in the Actions column to run a checkpoint on the master node to write memory data to disks. In the upper-right corner of the Pangu page, you can move the pointer over Actions and select Empty Recycle Bin to clear the recycle bin of Apsara Distributed File System. In the upper-right corner of the Pangu page, you can move the pointer over Actions and select Enable Data Rebalancing or Disable Data Rebalancing to enable or disable the data rebalancing feature of Apsara Distributed File System.

**Go to the O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Pangu**. On the Pangu page,
select a cluster. The **Overview** tab for Apsara Distributed File System of the selected cluster appears.

##### 5.3.3.2 Overview

On the Overview tab, the key information about the operations of Apsara Distributed File System is displayed. You can view the summary of services, service role status, statistics on storage usage, statistics on storage nodes, and the trend charts of storage usage and the number of files.

**Go to the Overview tab**

1. Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top
navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Pangu** in the left-side navigation pane.
2. On the **Pangu** page, select a cluster. The **Overview** tab for Apsara Distributed File System
of the selected cluster appears.

**Services**

In the Services section, the status of Apsara Distributed File System and the number of service roles are displayed.

**Service Status**

In the Service Status section, all service roles of Apsara Distributed File System and their status are displayed. You can also view the number of physical servers on which each service role is deployed and the number of physical servers at desired state for each service role.

**Saturability - Storage Usage**

In the Saturability - Storage Usage section, the statistics on storage usage and the number of files are displayed. In the Storage Usage section, you can view the storage usage, total storage space, available storage space, and the size of the recycle bin. In the File Count section, you can view the storage usage of files, maximum number of files, number of existing files, and number of files in the recycle bin.

**Storage Trend and File Count Trend**

In the Storage Trend and File Count Trend sections, the trend charts of storage usage and the number of files are displayed. The Storage Trend chart shows the trend lines of the total storage space, used storage space, and storage usage in different colors. The File Count Trend chart shows the trend line of the number of files. In the upper-right corner of a chart, you can click the icon to zoom in on the chart. The following figure shows an enlarged chart of storage usage. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the storage usage of the cluster in the specified period.

**Storage Nodes**

In the Storage Nodes section, the information about the storage nodes of Apsara Distributed File System is displayed. You can view the numbers of data nodes, normal nodes, disks, and normal disks. You can also view the percentages of faulty nodes and faulty disks.

##### 5.3.3.3 Manage service roles

This topic describes how to view the master nodes and service roles of Apsara Distributed File System and manage service roles. This topic also describes how to change the primary master node or run a checkpoint on a master node of Apsara Distributed File System.

**Go to the Service Roles tab**

1. Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top
navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Pangu** in the left-side navigation pane.
2. On the Pangu page, select a cluster and click the **Service Roles** tab. The **Service Roles**
tab for Apsara Distributed File System of the selected cluster appears. On the **Service Roles** tab, the information about the master nodes and service roles of Apsara Distributed File System are displayed. The information about a master node includes the IP address, hostname, service role, and log ID. The information about a service role includes the role name, hostname, role status, and host status.

**Service roles**

| Service role | Description | Quantity | Form | High reliability |
|---|---|---|---|---|
| PanguMaster# | The master role of Apsara Distributed File System. | Deployed on at least three physical servers. | Process | Yes |
| PanguChunkserver# | The data node role of Apsara Distributed File System. | Deployed on at least three physical servers. | Process | Yes |
| PanguSupervisor# | The role that is used to control the service roles of Apsara Distributed File System. | Deployed together with the master role on at least three physical servers. | Process | Yes |

| PanguMonitor# | The monitoring role of Apsara Distributed File System. | Deployed on each physical server. | Process | N/A |
|---|---|---|---|---|
| PanguTools# | The toolkit of Apsara Distributed File System. | Deployed on at least one physical server. | N/A | N/A |

**PanguMaster#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least one volume for a cluster. A volume contains multiple master nodes. Each volume contains one primary master node and multiple secondary master nodes. A cluster for which three physical servers are deployed can work properly if a single physical server becomes faulty. A cluster for which five physical servers are deployed can work properly if one or two physical servers become faulty. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/pangu/PanguMaster#/pangu_master` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**PanguChunkserver#**

Service role description This service role depends on the PanguMaster# role. You must deploy this role on at least three physical servers for a cluster. This is because three replicas are written when you write data to a cluster. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned.

> **Note:** You must make sure that a request for shutting down data nodes is approved. In this case, data migration is complete.

Logs Logs are stored in the following directory:

```
 /cloud/app/pangu/PanguChunkserver#/pangu_chunkserver .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**PanguSupervisor#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least three physical servers for a cluster. The primary instance is elected to provide services. This role is used to approve the requests for starting or shutting down the master nodes or data nodes of a cluster. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory:

```
 /cloud/app/pangu/PanguSupervisor#/pangu_supervisor .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**PanguMonitor#**

Service role description This service role does not depend on other service roles. In most cases, the PanguMonitor# role is deployed on each physical server of a cluster and is used to monitor all service roles of Apsara Distributed File System that are deployed on each physical server. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs Logs are stored in the following directory: `/cloud/app/pangu/PanguMonitor#/pangu_monitor` . Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**PanguTools#**

Service role description This service role does not depend on other service roles. A physical server on which this role is deployed provides the CLI toolkit for Apsara Distributed File System. You can deploy this role on one or more physical servers. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs N/A Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**Supported operations**

You can change the primary master node or run a checkpoint on a master node of Apsara Distributed File System. For more information, see Change the primary master node of Apsara Distributed File System or Run a checkpoint on a master node of Apsara Distributed File System.

##### 5.3.3.4 Apsara Distributed File System storage

This topic describes how to view the storage overview and storage node information of Apsara Distributed File System, and how to set the status of storage nodes and data disks.

**Entry to the Storage Overview page**

1. On the **Services** page, click **Pangu** in the left-side navigation pane.
2. Select a cluster from the drop-down list, and then click the **Storage** tab. The **Storage**
**Overview** page for Apsara Distributed File System appears.
The **Storage Overview** page displays whether data rebalancing is enabled, key metrics and their values, suggestions to handle exceptions, and rack specifications of Apsara Distributed File System.

**Entry to the Storage Nodes page**

1. On the **Services** page, click **Pangu** in the left-side navigation pane.
2. Select a cluster from the drop-down list, and then click the **Storage** tab. The **Storage**
**Overview** page for Apsara Distributed File System appears.
3. Click the **Storage Nodes** tab. The **Storage Nodes** page appears.
The **Storage Nodes** page displays the information about all storage nodes of Apsara Distributed File System, including the total storage size, available storage size, status, TTL, and send buffer size.

**Set the storage node status**

You can set the storage node status to Disabled or Normal. This section describes how to set the status of a storage node to Disabled.
1. On the **Storage Nodes** page, find the target storage node and choose **Actions** > **Set**
**Node Status to Disabled** in the Actions column.
2. In the **Set Node Status to Shutdown** panel, click **Run**. A message appears, indicating
that the action has been submitted. The values of the **Volume** and **Hostname** parameters are automatically filled based on the selected storage node. You do not need to specify values for the parameters. You can check whether the status of storage node is changed in the storage node list.

**Set the data disk status**

You can set the data disk status to Error or Normal. This section describes how to set the status of a data disk to Error.
1. On the **Storage Nodes** page, find the target storage node and choose **Actions** > **Set Disk**
**Status to Error** in the Actions column.
2. In the **Set Disk Status to Error** panel, set the **Diskid** parameter.
The values of the **Volume** and **Hostname** parameters are automatically filled based on the selected storage node. You do not need to specify values for the parameters.
3. Click **Run**. A message appears, indicating that the action has been submitted.

##### 5.3.3.5 Change the primary master node of Apsara Distributed File System

**Distributed File System**

Apsara Big Data Manager (ABM) allows you to perform a primary/secondary switchover on the master nodes of Apsara Distributed File System. After the primary/secondary switchover is complete, an original secondary master node becomes the primary master node, and the original primary master node becomes a secondary master node.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on MaxCompute.

**Background information**

A volume in Apsara Distributed File System is similar to a namespace. The default volume is PanguDefaultVolume. If a cluster contains a large number of nodes, multiple volumes may exist. A volume has three master nodes. One of the nodes serves as the primary master node, and the other two nodes serve as secondary master nodes.

**Procedure**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and then select **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Pangu**. Then, select a cluster and
click the **Server Roles** tab.
5. In the **Master Status** section of the **Server Roles** tab, find the required master node and
choose **Actions** > **Change Primary Master Node** in the Actions column. In the Change Primary Master Node panel, specify the required parameters. The following table describes the parameters.
**Volume**: the volume whose primary master node needs to be changed. Default value:
**PanguDefaultVolume**. If a cluster contains multiple volumes, set this parameter to the
name of the actual volume whose primary master node needs to be changed.
**Hostname**: the hostname of the secondary master node that is to be the new primary
master node.
**Log Gap**: the maximum log number gap between the original primary and secondary
master nodes you want to switch. During the switchover, the system checks the log number gap. If the gap is less than the specified value, the switchover is allowed. Otherwise, you cannot change the primary master node. Default value: **100000**.
6. Click **Run**. A message appears, indicating that the job is submitted. The **Change Primary**
**Master Node** panel appears.
The **Change Primary Master Node** panel shows the switchover history. **RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the execution succeeds. **FAILED** indicates that the execution fails.
7. If the status is FAILED, click **Details** in the Details column to identify the cause of the
failure. You can also view information about **parameter settings**, **node details**, **script**, and
**execution parameters** to identify the cause of the failure.

##### 5.3.3.6 Clear the recycle bin of Apsara Distributed File System

**File System**

Apsara Big Data Manager (ABM) allows you to clear the recycle bin of Apsara Distributed File System to release storage space.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Procedure**

1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the Services tab. On the **Services** tab, click **Pangu** in the left-side navigation pane. On the Pangu page, select a cluster.
2. On the **Overview** tab, move the pointer over **Actions** in the upper-right corner and select
**Empty Recycle Bin**.
3. In the Empty Recycle Bin panel, configure the **Volume** parameter. By default, this
parameter is set to **${volume.volume}**.
4. Click **Run**. The Success message appears to inform you that the request is submitted.
5. View the status.
On the **Overview** tab, move the pointer over **Actions** in the upper-right corner and select
**Execution History** next to **Empty Recycle Bin** to view the operation history.
**RUNNING** indicates that the recycle bin is being cleared. **SUCCESS** indicates that the
recycle bin is cleared. **FAILED** indicates that the recycle bin fails to be cleared.
6. If an operation record is in the FAILED state, click **Details** in the Details column to identify
the cause of the failure. You can also view the parameter settings, server details, script, and runtime parameters to identify the cause of the failure.

##### 5.3.3.7 Enable or disable data rebalancing for Apsara Distributed File System

**Apsara Distributed File System**

Apsara Big Data Manager (ABM) allows you to enable or disable data rebalancing for Apsara Distributed File System.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Disable data rebalancing**

1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the Services tab. On the **Services** tab, click **Pangu** in the left-side navigation pane.
2. On the **Pangu** page, select the cluster that you want to manage.
3. Move the pointer over **Actions** in the upper-right corner and select **Disable Data**
**Rebalancing**.
4. In the Disable Data Rebalancing panel, configure the **Volume** parameter. By default, this
parameter is set to **${volume.volume}**.
5. Click **Run**. The Success message appears to inform you that the request is submitted.
6. View the status.
Move the pointer over **Actions** in the upper-right corner and select **Execution History** next to **Disable Data Rebalancing** to view the operation history.
**RUNNING** indicates that the request is being processed. **SUCCESS** indicates that the
request is successful. **FAILED** indicates that the request fails.
7. If an operation record is in the FAILED state, click **Details** in the Details column to identify
the cause of the failure. For more information, see the Identify the cause of a failure section of this topic.

**Enable data rebalancing**

1. On the **Services** tab, click **Pangu** in the left-side navigation pane.
2. On the **Pangu** page, select the cluster that you want to manage.
3. Move the pointer over **Actions** in the upper-right corner and select **Enable Data**
**Rebalancing**.
4. In the Enable Data Rebalancing panel, configure the **Volume** parameter. By default, this
parameter is set to **${volume.volume}**.
5. Click **Run**. The Success message appears to inform you that the request is submitted.
6. View the status.
Move the pointer over **Actions** in the upper-right corner and select **Execution History** next to **Enable Data Rebalancing** to view the operation history.
**RUNNING** indicates that the request is being processed. **SUCCESS** indicates that the
request is successful. **FAILED** indicates that the request fails.
7. If an operation record is in the FAILED state, click **Details** in the Details column to identify
the cause of the failure. For more information, see the Identify the cause of a failure section of this topic.

**Identify the cause of a failure**

This section describes how to identify the cause of a failure.
1. In the Execution History panel, find a failed operation record and click **Details** in the
Details column.
2. In the panel that appears, find a failed step and click **View Details** to identify the cause of
the failure. You can also view the parameter settings, server details, script, and runtime parameters to identify the cause of the failure.

##### 5.3.3.8 Run a checkpoint on a master node of Apsara Distributed File System

**Apsara Distributed File System**

Apsara Big Data Manager (ABM) allows you to run checkpoints on the master nodes of Apsara Distributed File System. This way, memory data is written to disks. If Apsara Distributed File System is faulty, you can use checkpoints to restore data to the state before the failure. This ensures data consistency.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Procedure**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Pangu**. On the Pangu page,
select a cluster and click the **Service Roles** tab.
5. In the **Master Status** section of the **Service Roles** tab, find the master node that you
want to manage, move the pointer over Actions in the **Actions** column, and then select
**Run Checkpoint on Master Node**. In the Run Checkpoint on Master Node panel,
configure the **Volume** parameter.

> **Note:** By default, the **Volume** parameter is set to **${volume.volume}**.

6. Click **Run**. The Success message appears to inform you that the request is submitted. The
**Run Checkpoint on Master Node** panel appears.
In the **Run Checkpoint on Master Node** panel, the history of checkpoints on the master node is displayed. **RUNNING** indicates that the request is being processed. **SUCCESS** indicates that the request is successful. **FAILED** indicates that the request fails.
7. If an operation record is in the FAILED state, click **Details** in the Details column to identify
the cause of the failure. You can also view the parameter settings, server details, script, and runtime parameters to identify the cause of the failure.

#### 5.3.4 Tunnel service

##### 5.3.4.1 O&M features and page

This topic describes the O&M features for the tunnel service and how to go to the O&M page.

**Definition**

The tunnel service serves as a data tunnel of MaxCompute. You can use this service to upload data to or download data from MaxCompute.

**O&M features**

On the Overview tab, the overall information about the tunnel service is displayed. You can view the summary of services, service role status, and the trend chart of throughput. On the Service Roles tab, the information about the service roles of the tunnel service is displayed. On the Traffic Analysis tab, the traffic curves of specific projects in a specific period of time are displayed. The curves indicate the traffic types and the peak throughout in the specified period. This helps you make informed decisions. On the Configuration Management tab, you can manage endpoints. You can also view all the projects that are configured in the current cluster and switch the tunnel configurations for projects. In the upper-right corner of the Service Roles tab, you can click Restart Tunnel Service to restart tunnel servers.

**Go to the O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute**.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Tunnel**. The **Overview** tab for
the tunnel service appears.

##### 5.3.4.2 Overview

On the Overview tab, the overall information about the tunnel service is displayed. You can view the summary of services, service role status, and the trend chart of throughput.

**Go to the Overview tab**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Tunnel** in the left-side navigation pane. The **Overview** tab for the tunnel service appears. On the **Overview** tab, the key operating information about the tunnel service is displayed, such as the summary of services, service role status, and the trend chart of throughput.

**Services**

In the Services section, the numbers of available services, unavailable services, and services that are being updated are displayed.

**Service Status**

In the Service Status section, all service roles of the tunnel service and their status are displayed. You can also view the number of physical servers on which each service role is deployed and the number of physical servers at desired state for each service role.

**Tunnel Throughput (Bytes per Minute)**

In the Tunnel Throughput (Bytes per Minute) section, a chart is displayed. The trend lines of different colors indicate the inbound and outbound traffic. This trend chart can be automatically or manually refreshed. You can also view the trend chart of the tunnel throughput in a specific period of time.

##### 5.3.4.3 Manage service roles

On the Service Roles tab, the information about the service roles of the tunnel service is displayed. You can view the role name, hostname, IP address, role status, and host status of each service role.

**Go to the Service Roles tab**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Tunnel** in the left-side navigation pane. On the Tunnel page, click the **Service Roles** tab. The **Service**
**Roles** tab for the tunnel service appears.
On the **Service Roles** tab, the information about all service roles of the tunnel service is displayed. You can view the role name, hostname, IP address, role status, and host status of each service role. A service role may be in the **good**, **error**, or **upgrading** state.

**Service roles**

| Service role | Descript ion | Quantity | Form | High availability |
|---|---|---|---|---|
| FrontendServer# | The frontend service role. | Deployed on at least two physical servers. | Process | Yes |
| TunnelFrontendServer# | The tunnel service role. | Deployed on at least two physical servers. | Process | Yes |
| ServiceTest# | The detection service role. | Deployed on at least one physical server. | Process | N/A |

**FrontendServer#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least two instances of a cluster. The two instances are associated with one virtual IP address (VIP) for load balancing. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/odps-service-`

```
frontend/FrontendServer#/frontend_server/current/log .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**TunnelFrontendServer#**

Service role description This service role does not depend on other service roles. You must deploy this role on at least two instances of a cluster. The two instances are associated with one VIP for load balancing. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical servers on which the service role is deployed can be recloned. You must reclone the physical servers in batches. Logs Logs are stored in the following directory: `/cloud/app/odps-service-`

```
frontend/TunnelFrontendServer#/tunnel_frontend_server/current/log .
```

Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

**ServiceTest#**

Service role description This service role does not depend on other service roles. This role provides the frontend service detection capability. You can deploy this role on one or more physical servers. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. Reclone The physical servers on which the service role is deployed can be recloned. Logs N/A. Monitoring You can check whether the physical servers on which the service role is deployed are at desired state. For more information, see the Go to the Service Roles tab section of this topic.

##### 5.3.4.4 Traffic analysis

The Traffic Analysis tab displays the traffic curves of specific projects in a specific period. The curves show traffic types and the peak throughout in the specified period, which helps you make informed decisions.

**Go to the Traffic Analysis tab**

In the left-side navigation pane of the **Services** tab, click **Tunnel Service**. Then, click the
**Traffic Analysis** tab. The **Traffic Analysis** tab for the Tunnel service appears.
After you specify a period and the project for traffic analysis, click the icon. Then, you can view the upstream and downstream throughput curves of Tunnel traffic for traffic analysis.

> **Note:** The traffic data comes from Monitoring System. Make sure that this system is normal.
> By default, the top five projects that have the most traffic are selected. You can also filter projects based on your business requirements.
> By default, the beginning of the period is two days before the current time, and the end of the period is one day before the current time. You can also specify the period based on your business requirements.

##### 5.3.4.5 Manage configurations

On the Configuration Management tab, you can manage endpoints, view all the projects that are configured in the current cluster, and switch the tunnel configurations for projects.

**Go to the Configuration Management tab**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the Services tab. On the **Services** tab, click **Tunnel** in the left-side navigation pane. Then, click the **Configuration Management** tab. The
**Configuration Management** tab for the tunnel service appears.
On the **Configuration Management** tab, you can add, modify, and remove endpoints. You can also view all the projects that are configured in the current cluster and switch the tunnel configurations for projects.

**Add an endpoint**

1. On the **Configuration Management** tab, select a region and a cluster from the drop-down
lists and click the icon.
2. Click the **Endpoint Configurations** tab.
3. On the Endpoint Configurations tab, click **Add** in the upper-right corner. In the **Add**
**Endpoint** panel, configure the **New Cluster** and **New Host** parameters.
4. Click **Run**. The endpoint is added.

> **Note:** On the **Endpoint Configurations** tab, select the endpoints that you want to remove and click **Delete** in the upper-right corner to remove multiple endpoints at a time.
> On the **Endpoint Configurations** tab, find the endpoint that you want to modify and click **Modify** in the **Actions** column to modify the endpoint.

**Switch the tunnel configurations**

1. On the **Configuration Management** tab, select a region and a cluster from the drop-down
lists and click the icon.
2. Click the **Projects** tab.
3. On the Projects tab, select one or more projects for which you want to switch the tunnel
configurations and click **Switch Tunnel Configurations**.
4. In the **Switch Project Tunnel** panel, configure the **Destination Cluster** parameter and
click **Run**.

##### 5.3.4.6 Restart tunnel servers

Apsara Big Data Manager (ABM) allows you to restart tunnel servers for specific service roles of the tunnel service.

**Prerequisites**

The management permissions on MaxCompute are granted to your ABM account.

**Background information**

You can restart one or more tunnel servers at a time on the **Service Roles** tab.

**Step 1: Restart tunnel servers**

1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Services**
tab.
4. In the left-side navigation pane of the **Services** tab, click **Tunnel**. On the Tunnel page,
select a cluster and click the **Service Roles** tab.
5. On the Service Roles tab, select one or more service roles for which you want to restart
tunnel servers and click **Restart Tunnel Service** in the upper-right corner.
6. In the **Restart Tunnel Server** panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Forcibly Restart | Specifies whether to forcibly restart tunnel servers for the selected service roles. Valid values: no force: does not forcibly restart tunnel servers. If a service role is _ running, the tunnel server is not restarted. force: forcibly restarts tunnel servers. In this case, the status of a service role does not affect the restart of the tunnel server. |
| Hostname | The hostnames of the selected service roles. The value is automatically provided. You do not need to specify a value for this parameter. |

7. Click **Run**.

**Step 2: View the status or progress**

1. On the **Overview** or **Service Roles** tab of the **Tunnel** page, click **Execution History** in
the upper-right corner to view the operation history.
**RUNNING** indicates that tunnel servers are being restarted. **SUCCESS** indicates that
tunnel servers are restarted. **FAILED** indicates that tunnel servers fail to be restarted.
2. If an operation record is in the **RUNNING** state, click **Details** in the Details column to view
the progress.

**Step 3: (Optional) Identify the cause of a failure**

If an operation record is in the **FAILED** state, you can view the run logs to identify the cause of the failure.
1. On the **Overview** or **Service Roles** tab of the **Tunnel** page, click **Execution History** in
the upper-right corner to view the operation history.
2. In the Execution History panel, find a failed operation record and click **Details** in the
Details column.
3. On the **Servers** tab of the failed step, click **View Details** in the Actions column. The
**Execution Output** tab appears in the Execution Details section. You can view the output
to identify the cause of the failure.

### 5.4 Cluster O&M

#### 5.4.1 O&M features and entry

This topic describes the O&M features of MaxCompute clusters. It also provides more information about how to go to the MaxCompute cluster O&M page.

**Cluster O&M features**

O&M features of MaxCompute clusters: Overview: shows the overall running information about a cluster. You can view the host status, service status, health check result, and health check history. You can also view the trend charts of CPU utilization, disk usage, memory usage, load, and packet transmission for the cluster. In the Log on section, you can click the name of the host whose role is pangu master, fuxi master, or odps ag to log on to the host. Health Status: shows all checkers for a cluster. You can query checker details, check results for hosts in the cluster, and schemes to clear alerts (if any exists). You can also log on to a host and perform manual checks on the host. Servers: shows information about hosts in a cluster. The information includes the hostname, IP address, role, type, CPU utilization, memory usage, root disk usage, packet loss rate, and packet error rate. Scale out Cluster or Scale in Cluster: allows you to add or remove physical hosts to scale out or scale in a MaxCompute cluster. Enable Auto Repair: allows you to enable auto repair for MaxCompute clusters. Restore Environment Settings: allows you to restore environment settings for multiple hosts in a MaxCompute cluster at a time.

**Go to the Clusters tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and then **MaxCompute**.
3. On the MaxCompute page, click **O&M** in the top navigation bar. Then, click the **Clusters**
tab.
4. In the left-side navigation pane of the **Clusters** tab, click a cluster. The **Overview** tab for
the selected cluster appears.

#### 5.4.2 Manage cluster health checks

On the Health Status tab, all check items and check results of a cluster are displayed. You can view the details of check items and view the check results for hosts to handle alerts. You can also log on to a host and perform manual checks on the host.

**Go to the Health Status tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Clusters**
tab.
4. On the **Clusters** tab, select a cluster. Then, click the **Health Status** tab. The **Health**
**Status** tab for the selected cluster appears.
On the **Health Status** tab, you can view all check items for the cluster and the check results for the hosts in the cluster. The following alerts may be reported on a host: **Critical**,
**Warning**, and **Exception**. The alerts are represented in different colors. You must handle
the alerts at the earliest opportunity, especially the **Critical** and **Warning** alerts. The following table describes the check results.

| Check result | Description |
|---|---|
| Critical | A critical alert. |
| Warning | A threshold-based alert. |
| Exception | An exception in a script call. |

**View the details of a check item**

1. On the Health Status tab, find the check item whose details you want to view and click
**Details** in the Actions column. In the Details message, view the details of the check item.
The following information about the check item is displayed: **Name**, **Source**, **Alias**,
**Application**, **Type**, **Scheduling**, **Data Collection**, **Default Execution Interval**, and
**Description**. The schemes to clear alerts are provided in the description.
2. Click **Show More** to view more information about the check item.
You can view more information in the **Script**, **Target (TianJi)**, **Default Threshold**, and
**Mount Point** sections.

**View the hosts for which alerts are reported and causes for the**

**alerts**

You can view the check history and check results of a check item on a host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click a hostname. In the panel that appears, find the alert that you want to manage and
click **Details** in the Actions column to view the cause of the alert.

**Log on to a host**

You may need to log on to a host to handle alerts or other issues that occur on the host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click the **Login in** icon next to a hostname. The **TerminalService** page appears.
3. On the **TerminalService** page, click the hostname in the left-side navigation pane to log
on to the host.

**Run a check item again**

After you handle an alert for a host, click **Refresh** in the Actions column of the host to run the check item again for the host. This way, you can check whether the alert is cleared.

#### 5.4.3 Overview

This topic describes how to go to the Overview tab for the O&M of a MaxCompute cluster. This topic also describes the cluster overview and the operations that you can perform on the Overview tab.

**Go to the Overview tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose Big Data Computing > **MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click **O&M** in the top navigation bar. Then, click the **Clusters**
tab.
4. On the **Clusters** tab, select a cluster. The **Overview** tab for the O&M of the selected
cluster appears. On the **Overview** tab, you can quickly log on to the hosts that are commonly used to manage the MaxCompute cluster. You can view the host status, service status, health check results, and health check history. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, and packet transmission for the cluster.

**Quick Logon**

In the Quick Logon section, you can quickly log on to the hosts that assume the pangu master, fuxi master, and odps ag roles and are commonly used to manage a MaxCompute cluster.
1. In the **Quick Logon** section of the **Overview** tab, click a hostname in the **Hostname**
column. The **Hosts** tab appears.
2. In the left-side host list, find the host to which you want to log on and click the **Login in**
icon next to the hostname. The **TerminalService** page appears.
3. In the left-side navigation pane, click the hostname to log on to the host.

**Servers**

In the Servers section, the number of hosts in the **good** or **error** state is displayed.

**Services**

In the Services section, all services deployed in the cluster are displayed. You can view the number of services in the **good** or **bad** state.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the cluster in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the cluster in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the cluster over time in different colors. These trend lines reflect the data transmission status of the cluster. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the cluster in the specified period.

**Health Check**

In the Health Check section, the number of check items for the cluster and the numbers of CRITICAL, WARNING, and EXCEPTION alerts are displayed. Click **View Details** to go to the Health Status tab. On the Health Status tab, you can view the details of health checks. For more information, see Manage cluster health checks.

**Health Check History**

In the Health Check History section, the records of health checks performed on the cluster are displayed. You can view the numbers of CRITICAL, WARNING, and EXCEPTION alerts. Click **View Details** to go to the Health Status tab. On the Health Status tab, you can view the details of health checks. For more information, see Manage cluster health checks. You can click the event content of a check to view the exception items of the check.

#### 5.4.4 Servers

The Servers tab shows information about hosts. The information includes the hostname, IP address, role, type, CPU utilization, total memory size, available memory size, load, root disk usage, packet loss rate, and packet error rate. In the left-side navigation pane of the **Clusters** tab, click a cluster. Then, click the **Servers** tab. The **Servers** tab for the selected cluster appears. To view more information about a host, click the name of the host. The Hosts tab appears.

#### 5.4.5 Scale in and scale out a MaxCompute cluster

**cluster**

Apsara Big Data Manager (ABM) supports the scaling of MaxCompute cluster. If you want to scale out a MaxCompute cluster, you can add physical hosts in the default cluster of Apsara Infrastructure Management to the MaxCompute cluster. If you want to scale in a MaxCompute cluster, you can remove physical hosts in the default cluster of Apsara Infrastructure Management from the MaxCompute cluster.

**Description**

In Apsara Stack, the scale-out operation on a cluster is complex. You must configure a new physical host on Deployment Planner. This way, the host can be added to the default cluster of Apsara Infrastructure Management. The default cluster of Apsara Infrastructure Management is considered an idle resource pool in which resources are available. The default cluster can provide resources for scaling out business clusters. To scale out a cluster, you can add physical hosts in the default cluster of Apsara Infrastructure Management to the cluster. To scale in a cluster, you can move physical hosts from the cluster to the default cluster of Apsara Infrastructure Management. You can use this method to scale out or scale in a MaxCompute cluster in the ABM console.

**Prerequisites**

Scale-out: The physical host that you want to add is an **SInstance** host in the default cluster of Apsara Infrastructure Management. Scale-out: The template host is an **SInstance** host. You can log on to the admingateway host in a MaxCompute cluster to view SInstance hosts. Scale-in: The physical host that you want to remove is an **SInstance** host. You can log on to the admingateway host in a MaxCompute cluster to view SInstance hosts.

**Scale out a MaxCompute cluster**

You can add multiple hosts to a MaxCompute cluster at the same time to scale out the cluster. To achieve this, you must specify an existing host as the template host. When you scale out the MaxCompute cluster, the hosts copy configurations from the template host. This way, the hosts can be added to the cluster at the same time.
1. Log on to the admingateway host in the MaxCompute cluster. Run the `r ttrl` command
to query and record **SInstance** hosts. For more information about how to log on to a host, see Log on to a host.
2. In the left-side navigation pane of the **Clusters** tab, click a cluster. Then, click the **Servers**
tab. On the Servers tab, select an **SInstance** host and use it as the template host.
3. In the upper-right corner of the Servers tab, choose **Actions > Scale out Cluster**. In the
**Scale out Cluster** panel, configure the parameters.
Parameters:
**Region**: the region of the host that you want to add.
**Refer Hostname**: the name of the template host. By default, the name of the selected
host is used.
**hostname**: the name of the host that you want to add. The drop-down list displays all
available hosts in the default cluster for scale-out operations. You can select one or more hosts from the drop-down list.
4. In the Scale out Cluster panel, click **Run**.
5. View the scale-out status.
In the upper-right corner of the Servers tab, click **Actions** and select **Execution History** next to **Scale out Cluster** to view the scale-out history. The cluster may require a long period of time to be scaled out. In the Current Status column, **RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the execution is successful. **FAILED** indicates that the execution fails.
6. In the Execution History panel, click **Details** in the Details column to view the steps and
progress of the execution if the status is RUNNING.
7. In the Execution History panel, click **Details** in the Details column to identify the cause of
the failure if the status is **FAILED**.

**Scale in a MaxCompute cluster**

You can remove multiple hosts from a MaxCompute cluster at the same time to scale in the cluster.
1. Log on to the admingateway host in the MaxCompute cluster. Run the `r ttrl` command
to query and record **SInstance** hosts. For more information about how to log on to a host, see Log on to a host.
2. In the left-side navigation pane of the **Clusters** tab, click a cluster. Then, click the **Servers**
tab. On the Servers tab, select one or more **SInstance** hosts that you want to remove.
3. In the upper-right corner of the Servers tab, choose **Actions > Scale in Cluster**. In the
**Scale in Cluster** panel, configure the parameters.
Parameters:
**Region**: the region of the host that you want to remove.
**Hostname**: the name of the host that you want to remove. By default, the name of the
selected host is used.
4. In the Scale in Cluster, click **Run**.
5. View the scale-in status.
In the upper-right corner of the Servers tab, click **Actions** and select **Execution History** next to **Scale in Cluster** to view the scale-in history. The cluster may require a long period of time to be scaled in. In the Current Status column,
**RUNNING** indicates that the execution is in progress. **SUCCESS** indicates that the
execution is successful. **FAILED** indicates that the execution fails.
6. In the Execution History panel, click **Details** in the Details column to view the steps and the
progress of the execution if the status is RUNNING.
7. In the Execution History panel, click **Details** in the Details column to identify the cause of
the failure if the status is **FAILED**.

**Identify the cause of a scale-in or scale-out failure**

In this example, cluster scale-in is used to describe how to identify the cause of a failure.
1. In the upper-right corner of the **Clusters** tab, click **Actions** and select **Execution History**
next to **Scale in Cluster** to view the scale-in history.
2. In the Execution History panel, click **Details** in the Details column of a failed operation to
identify the cause of the failure. You can locate the failure cause based on the following information: parameter settings, host details, scripts, and execution parameters.

#### 5.4.6 Restore environment settings

Apsara Big Data Manager (ABM) allows you to restore the environment settings for multiple hosts in a MaxCompute cluster at a time.

**Procedure**

You can restore the environment settings for multiple hosts in a MaxCompute cluster at a time.
1. Log on to the MaxCompute console from ABM. In the top navigation bar, click O&M. Then,
click the Clusters tab. On the **Clusters** tab, move the pointer over **Actions** in the upperright corner and select **Restore Environment Settings**. In the **Restore Environment**
**Settings** panel, specify the hosts whose environment settings you want to restore.

> **Note:** Separate multiple hostnames with commas (,).

2. Click **Run**. The Success message appears to inform you that the request is submitted.
3. View the restoration status.
Move the pointer over **Actions** and select **Execution History** next to **Restore**
**Environment Settings** to view the operation history.
It requires some time for the restoration to complete. In the Current Status column,
**RUNNING** indicates that environment settings are being restored. **SUCCESS** indicates that
environment settings are restored. **FAILED** indicates that environment settings fail to be restored.
4. If an operation record is in the RUNNING state, click **Details** in the Details column to view
the steps and progress of the operation.
5. If an operation record is in the **FAILED** state, click **Details** in the Details column to identify
the cause of the failure.

### 5.5 Host O&M

#### 5.5.1 O&M features and page

This topic describes the O&M features for the host service and how to go to the O&M page.

**O&M features**

On the Overview tab, the brief information about hosts in a MaxCompute cluster is displayed. You can view the server information and service role status of a host. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, and packet loss rate for the host. You can zoom in on the trend charts to view the enlarged trend charts of CPU utilization, memory usage, disk usage, loads, and packet loss rate for a host. These trend charts are the same as those displayed on the Overview tab for the host. On the Service Roles tab, the cluster to which a host belongs, the services that are running on the host, and the service roles that are deployed on the host are displayed.

**Go to the O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose **Big Data Computing** >
**MaxCompute** to go to the MaxCompute console.
3. In the MaxCompute console, click O&M in the top navigation bar. Then, click the **Hosts** tab.
4. In the left-side host list of the **Hosts** tab, select a host. The **Overview** tab for the selected
host appears.

#### 5.5.2 Overview

On the Overview tab, the brief information about hosts in a MaxCompute cluster is displayed. You can view the server information and service role status of a host. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, and packet loss rate for the host.

**Go to the Overview tab**

Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the **Hosts** tab. On the **Hosts** tab, select a host from the left-side host list. The **Overview** tab for the selected host appears. On the **Overview** tab, you can view the server information and service role status of the selected host. You can also view the trend charts of CPU utilization, disk usage, memory usage, loads, and packet transmission for the host.

**Server Information**

In the Server Information section, the information about the host is displayed. You can view the region, cluster, name, IP address, status, data center, and server room of the host.

**Service Role Status**

In the Service Role Status section, the information about the services that are deployed on the host is displayed. You can view the roles, status, and number of services.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the host in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the host in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the host in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the host in the specified period.

#### 5.5.3 Manage host services

On the Service Roles tab, the services and service roles that are deployed on a host are displayed. Log on to the MaxCompute console from Apsara Big Data Manager (ABM). In the top navigation bar, click O&M. Then, click the **Hosts** tab. In the left-side host list, select a host. Then, click the **Service Roles** tab. The **Service Roles** tab for the selected host appears. On the **Service Roles** tab, you can view the cluster to which the host belongs, the services that are running on the host, and the service roles that are deployed on the host.

### 5.6 Deep inspection

#### 5.6.1 Overview

The deep inspection feature helps you check the monitoring alerts, resource usage, and key metrics of MaxCompute. You can use this feature to check the health status of the platform to avoid unexpected risks. This helps ensure the stability of MaxCompute clusters. The deep inspection feature can check information about the following aspects: Health status of MaxCompute clusters. For more information, see MaxCompute cluster inspection. Risks that affect the health of MaxCompute clusters. For more information, see MaxCompute risk inspection.

> **Note:** Apsara Big Data Manager (ABM) does not recycle inspection reports, but collects all risks and related thresholds that are contained in the inspection reports.

#### 5.6.2 Inspect clusters

This topic describes how to check the health status of MaxCompute clusters and quickly identify faulty clusters.

**Background information**

You can perform the following operations to check the health status of a MaxCompute cluster: Inspect the status of a cluster Inspect cluster alerts Inspect the control service Inspect Job Scheduler Inspect Apsara Distributed File System Inspect the tunnel service Inspect Apsara Name Service and Distributed Lock Synchronization System Inspect a metadata warehouse

**Inspect the status of a cluster**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Site Navigation** > **TIANJI** to go to the Apsara Infrastructure Management console.
4. In the **Apsara Infrastructure Management** console, choose **Resource Management >**
**Product & Cluster O&M** in the left-side navigation pane.
5. On the **Product & Cluster O&M** page, enter odps in the **Product | Cluster** search box to
search for MaxCompute clusters.
6. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
On the details page, view the status of the cluster in the **Basic Information** section and the status of the services in the cluster on the **Services** tab to check whether the services are at desired state. If the services of the cluster are in the **Not Ready** state, submit a ticket for technical support.

**Inspect cluster alerts**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Big Data Computing** > **MaxCompute** to go to the MaxCompute console.
4. In the **MaxCompute** console, click O&M in the top navigation bar. Then, click the **Clusters**
tab. On the Clusters tab, select a cluster. Then, click the **Health Status** tab. The value in the **Critical** column indicates the number of critical alerts. The value in the **Warning** column indicates the number of threshold-based alerts. The value in the **Exception** column indicates the number of exceptions in script calls. In most cases, the values in the **Critical**, **Warning**, and **Exception** columns are all 0, or no result is displayed on this tab. If the number of alerts or exceptions is displayed for a check item, you can find the check item and click **Details** in the Actions column to troubleshoot the issues. If you have other questions, submit a ticket for technical support.

**Inspect the control service**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Big Data Computing** > **MaxCompute** to go to the MaxCompute console.
4. In the **MaxCompute** console, click O&M in the top navigation bar. Click the **Services** tab.
Then, click **Control** in the left-side navigation pane.
5. On the **Overview** tab of the **Control** page, view the role information in the **Service Status**
section. If a service role of the cluster is unavailable, submit a ticket for technical support.

**Inspect Job Scheduler**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Big Data Computing** > **MaxCompute** to go to the MaxCompute console.
4. In the **MaxCompute** console, click O&M in the top navigation bar. Click the **Services** tab.
Then, click **Fuxi** in the left-side navigation pane.
5. On the **Overview** tab of the **Fuxi** page, view information in the **Service Status** and **Trend**
**for Resource Usage** sections.
Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: If the CPU utilization or memory usage reaches the upper limit for an extended period of time, we recommend that you submit tasks during off-peak hours. If the CPU utilization or memory usage still reaches the upper limit, submit a ticket for technical support.

**Inspect Apsara Distributed File System**

**View the status of a node, storage usage, and the number of**

**files for a cluster**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Big Data Computing** > **MaxCompute** to go to the MaxCompute console.
4. In the **MaxCompute** console, click O&M in the top navigation bar. Click the **Services** tab.
Then, click **Pangu** in the left-side navigation pane.
5. On the **Overview** tab of the **Pangu** page, view the status of service roles in the **Service**
**Status** Section and the information about the selected cluster in the **Saturability -**
**Storage Usage** section.
Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: If the storage usage or the number of files exceeds 80%, submit a ticket for technical support.

**Check the disk status of Apsara Distributed File System**

1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
2. Run the following command to check the disk status of Apsara Distributed File System:

```
puadmin lscs|grep -vi NORMAL|grep -vi DISK_OK
```

If an error occurs, submit a ticket for technical support.

**Check the data integrity of Apsara Distributed File System**

1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
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

The following command provides an example on the normal output. If data is returned, data loss occurs. In this case, submit a ticket for technical support.

```
Master Address: nuwa://localcluster/sys/pangu/master ChunkId Type FoundTime
```

**Inspect the tunnel service**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. In the upper-left corner, click the
icon.
3. Choose **Big Data Computing** > **MaxCompute** to go to the MaxCompute console.
4. In the **MaxCompute** console, click O&M in the top navigation bar. Click the **Services** tab.
Then, click **Tunnel** in the left-side navigation pane.
5. On the **Overview** tab of the **Tunnel** page, view the status of service roles in the **Service**
**Status** section and the throughput of the tunnel service in the **Tunnel Throughput**
**(Bytes per Minute)** section.
Inspection result 1: If a service role is in the **good** state, and the number of physical servers on which the service role is deployed is equal to the number of physical servers at desired state for the service role, the service role works properly. Otherwise, submit a ticket for technical support. Inspection result 2: The traffic status of the selected cluster is displayed in the **Tunnel**
**Throughput (Bytes per Minute)** section.

**Inspect Apsara Name Service and Distributed Lock**

**Synchronization System**

1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
2. Run the following command to check the health status of Apsara Name Service and
Distributed Lock Synchronization System:

```
tj_show -r nuwa.NuwaZK#>/tmp/nuwa;pssh -h /tmp/nuwa -i "echo srvr| nc localhost 10240
| grep Mode"
```

The following command provides an example on the normal output. One leader and two followers are available. If no **leader** or **follower** is returned or an error message is returned, submit a ticket for technical support.

```
[1] 11:21:43 [SUCCESS] vm010230012204 Mode: leader [2] 11:21:43 [SUCCESS] vm010230009054 Mode: follower [3] 11:21:43 [SUCCESS] vm010230017122 Mode: follower
```

**Inspect a metadata warehouse**

1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
2. Run the following command to switch to the administrator role:

```
su admin
```

3. Check the logs of a metadata warehouse.
Syntax

```
cat /apsara/meta/logs/<datetime>/meta.log
```

**datetime**: the directory that stores the logs that are generated on the specified date.
Example Run the following command to query the logs of a metadata warehouse that are generated on April 24, 2022:

```
cat /apsara/meta/logs/20220424/meta.log
```

Check whether the returned results are consistent with the information that is marked in the following figure. If the returned results are inconsistent with the information in the following figure, run the `sh /apsara/meta/daliyrun.sh` command as the administrator to restart MaxCompute AG and check the logs again. If the issue persists, submit a ticket for technical support.

#### 5.6.3 MaxCompute risk inspection

If the number of chunks or the number of files in the volumes directory exceeds the upper limit, the cluster becomes unstable or even fails. This topic describes how to check risks that exist in MaxCompute clusters and how to handle the risks.

**Background information**

You can check risks that exist in a MaxCompute cluster from the following aspects: Check the number of chunks Check the number of files in the volumes directory

**Check the number of chunks**

If the number of chunks exceeds the upper limit, the chunkserver service becomes unstable and data queries are slow. To check the number of chunks, perform the following steps:
1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
2. Run the following command to check the number of chunks:

```
puadmin lscs|grep tcp
```

If the number of chunks exceeds 2 million, small files must be merged.

**Check the number of files in the volumes directory**

If the number of files in the volumes directory exceeds the upper limit, the files in the volumes directory may be damaged. To check the number of files in the volumes directory, perform the following steps:
1. Log on to MaxCompute AG.
For more information, see Log on to MaxCompute AG.
2. Run the following command to check the number of files in the volumes directory:

```
pu ls -l /product/aliyun/odps/adsmr|grep -A4 volume
```

If the number of files in the volumes directory exceeds 5 million, a risk exists. If the number of files in the volumes directory exceeds 8 million, a high risk exists. In this case, you must submit a ticket and contact Alibaba Cloud engineers for technical support.

#### 5.6.4 Log on to MaxCompute AG

This topic describes how to log on to MaxCompute AG.

**Procedure**

1. Log on to the Apsara Big Data Manager (ABM) console.
For more information, see Log on to the ABM console.
2. Choose **Site Navigation** > **TIANJI** to go to the Apsara Infrastructure Management console.
3. In the **Apsara Infrastructure Management console** , choose Resource Management >
**Machines** in the left-side navigation pane. On the Machines page, click Advanced Filter.
Enter odps in the Product field and click Search. Find a host and click Terminal in the Actions column.
