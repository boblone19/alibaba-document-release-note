---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 446
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Log%20Service%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Log Service User Guide 20220928

## Table of Contents

- 1 What is Log Service?
- 2 Quick start
  - 2.1 Procedure
  - 2.2 Log on to the Log Service console
  - 2.3 Obtain an AccessKey pair
  - 2.4 Manage projects
  - 2.5 Manage Logstores
  - 2.6 Manage shards
- 3 Data collection
  - 3.1 Collection by Logtail
    - 3.1.1 Overview
      - 3.1.1.1 Logtail overview
      - 3.1.1.2 Log collection process of Logtail
      - 3.1.1.3 Logtail configuration files and record files
    - 3.1.2 Installation
      - 3.1.2.1 Install Logtail in Linux
      - 3.1.2.2 Install Logtail in Windows
      - 3.1.2.3 Set Logtail startup parameters
    - 3.1.3 Logtail machine group
      - 3.1.3.1 Overview
      - 3.1.3.2 Create a machine group based on a server IP address
      - 3.1.3.3 Create a machine group based on a custom ID
      - 3.1.3.4 View server groups
      - 3.1.3.5 Modify a server group
      - 3.1.3.6 View the status of a server group
      - 3.1.3.7 Delete a server group
      - 3.1.3.8 Manage server group configurations
      - 3.1.3.9 Manage a Logtail configuration
      - 3.1.3.10 Configure an account ID on a server
    - 3.1.4 Text logs
      - 3.1.4.1 Configure text log collection
      - 3.1.4.2 Collect logs by line
      - 3.1.4.3 Use regular expressions to collect logs
      - 3.1.4.4 Collect DSV formatted logs
      - 3.1.4.5 Collect JSON logs
      - 3.1.4.6 Collect NGINX logs
      - 3.1.4.7 Collect IIS logs
      - 3.1.4.8 Collect Apache logs
      - 3.1.4.9 Configure parsing scripts
      - 3.1.4.10 Configure the time format
      - 3.1.4.11 Import historical logs
      - 3.1.4.12 Generate a topic
    - 3.1.5 Custom plug-ins
      - 3.1.5.1 Collect MySQL binary logs
      - 3.1.5.2 Collect MySQL query results
      - 3.1.5.3 Collect syslogs
      - 3.1.5.4 Configure data processing methods
    - 3.1.6 Collect container logs
      - 3.1.6.1 Collect standard Docker logs
      - 3.1.6.2 Collect Kubernetes logs
      - 3.1.6.3 Collect container text logs
      - 3.1.6.4 Collect stdout and stderr logs from containers
    - 3.1.7 Limits
  - 3.2 Other collection methods
    - 3.2.1 WebTracking
    - 3.2.2 Use SDKs to collect logs
      - 3.2.2.1 Producer Library
      - 3.2.2.2 Log4j Appender
      - 3.2.2.3 Logback Appender
      - 3.2.2.4 Golang Producer Library
      - 3.2.2.5 Python logging
    - 3.2.3 Common log formats
      - 3.2.3.1 Log4j logs
      - 3.2.3.2 Python logs
      - 3.2.3.3 Node.js logs
      - 3.2.3.4 WordPress logs
      - 3.2.3.5 Unity3D logs
- 4 Query and analysis
  - 4.1 Overview
  - 4.2 Real-time analysis
  - 4.3 Enable the indexing feature and configure indexes for a Logstore
  - 4.4 Query logs
  - 4.5 Export logs
  - 4.6 Index data type
    - 4.6.1 Overview
    - 4.6.2 Query text data
    - 4.6.3 Numeric type
    - 4.6.4 JSON indexes
  - 4.7 Query syntax and functions
    - 4.7.1 Search syntax
    - 4.7.2 LiveTail
    - 4.7.3 LogReduce
    - 4.7.4 Contextual query
    - 4.7.5 Saved search
    - 4.7.6 Quick analysis
  - 4.8 Analysis grammar
    - 4.8.1 General aggregate functions
    - 4.8.2 Security check functions
    - 4.8.3 Map functions
    - 4.8.4 Approximate functions
    - 4.8.5 Mathematical statistics functions
    - 4.8.6 Mathematical calculation functions
    - 4.8.7 String functions
    - 4.8.8 Date and time functions
    - 4.8.9 URL functions
    - 4.8.10 Regular expression functions
    - 4.8.11 JSON functions
    - 4.8.12 Type conversion functions
    - 4.8.13 IP functions
    - 4.8.14 GROUP BY syntax
    - 4.8.15 Window functions
    - 4.8.16 HAVING syntax
    - 4.8.17 ORDER BY syntax
    - 4.8.18 LIMIT syntax
    - 4.8.19 Syntax for CASE statements and if() functions
    - 4.8.20 Nested subqueries
    - 4.8.21 Array functions
    - 4.8.22 Binary string functions
    - 4.8.23 Bitwise operations
    - 4.8.24 Interval-valued comparison and periodicity-valued comparison functions
    - 4.8.25 Comparison functions and operators
    - 4.8.26 Lambda functions
    - 4.8.27 Logical functions
    - 4.8.28 Field aliases
    - 4.8.29 JOIN operations between Logstores and Relational Database Service (RDS) tables
    - 4.8.30 Geospatial functions
    - 4.8.31 Geography functions
    - 4.8.32 JOIN syntax
    - 4.8.33 UNNEST function
  - 4.9 Machine learning syntax and functions
    - 4.9.1 Overview
    - 4.9.2 Smooth functions
    - 4.9.3 Multi-period estimation functions
    - 4.9.4 Change point detection functions
    - 4.9.5 Maximum value detection function
    - 4.9.6 Prediction and anomaly detection functions
    - 4.9.7 Time series decomposition function
    - 4.9.8 Time series clustering functions
    - 4.9.9 Frequent pattern statistics function
    - 4.9.10 Differential pattern statistics function
    - 4.9.11 Root cause analysis function
    - 4.9.12 Correlation analysis functions
    - 4.9.13 Kernel density estimation function
  - 4.10 Advanced analysis
    - 4.10.1 Optimize queries
    - 4.10.2 Use cases
    - 4.10.3 Time field conversion examples
  - 4.11 Visual analysis
    - 4.11.1 Analysis graph
      - 4.11.1.1 Overview
      - 4.11.1.2 Display query results in a table
      - 4.11.1.3 Display query results on a line chart
      - 4.11.1.4 Display query results on a column chart
      - 4.11.1.5 Display query results on a bar chart
      - 4.11.1.6 Display query results on a pie chart
      - 4.11.1.7 Display query results on an area chart
      - 4.11.1.8 Display query results on a single value chart
      - 4.11.1.9 Display query results on a progress bar
      - 4.11.1.10 Display query results on a map
      - 4.11.1.11 Display query results on a flow chart
      - 4.11.1.12 Display query results in a Sankey diagram
      - 4.11.1.13 Display query results on a word cloud
      - 4.11.1.14 Display query results on a treemap chart
    - 4.11.2 Dashboard
      - 4.11.2.1 Overview
      - 4.11.2.2 Create and delete a dashboard
      - 4.11.2.3 Configure the display mode of a dashboard
      - 4.11.2.4 Edit mode
      - 4.11.2.5 Drill-down analysis
      - 4.11.2.6 Configure and use a filter on a dashboard of a Logstore
      - 4.11.2.7 Markdown chart
- 5 Alerts
  - 5.1 Overview
  - 5.2 Configure an alarm
    - 5.2.1 Configure alerts
    - 5.2.2 Grant permissions on alerts to a RAM user
    - 5.2.3 Configure alert notification methods
  - 5.3 Modify and view an alarm
    - 5.3.1 Modify an alert
    - 5.3.2 View history alerts
    - 5.3.3 Manage an alert
  - 5.4 Relevant syntax and fields for reference
    - 5.4.1 Conditional expression syntax of an alert
    - 5.4.2 Fields in alert log entries
- 6 Real-time consumption
  - 6.1 Overview
  - 6.2 Consume log data
  - 6.3 Consumption by consumer groups
    - 6.3.1 Use consumer groups to consume log data
    - 6.3.2 View the status of a consumer group
  - 6.4 Use LogHub Storm to consume log data
  - 6.5 Use Flume to consume log data
  - 6.6 Use open source Flink to consume log data
  - 6.7 Use Logstash to consume log data
  - 6.8 Use Spark Streaming to consume log data
  - 6.9 Use Realtime Compute to consume log data
- 7 Data shipping
  - 7.1 Ship logs to OSS
    - 7.1.1 Overview
    - 7.1.2 Ship log data from Log Service to OSS
    - 7.1.3 Obtain the ARN of a RAM role
    - 7.1.4 Storage Formats
    - 7.1.5 Decompress Snappy compressed files
- 8 RAM
  - 8.1 Overview
  - 8.2 Create a RAM role
  - 8.3 Create a user
  - 8.4 Create a RAM user group
  - 8.5 Add a RAM user to a RAM user group
  - 8.6 Create a permission policy
  - 8.7 Grant a RAM user the permissions to manage a project
  - 8.8 Grant permissions to a RAM role
  - 8.9 Use custom policies to grant RAM user the required permissions
- 9 FAQ
  - 9.1 Log collection
    - 9.1.1 How do I troubleshoot Logtail collection errors?
    - 9.1.2 What can I do if Log Service does not receive heartbeats from a Logtail client?
    - 9.1.3 How do I query the local log collection statuses?
    - 9.1.4 How do I test a regular expression?
    - 9.1.5 How do I optimize regular expressions?
    - 9.1.6 How do I use the full regex mode to collect log entries in multiple formats?
    - 9.1.7 How do I set the time format for logs?
    - 9.1.8 How do I configure non-printable characters in a sample log?
    - 9.1.9 How do I troubleshoot errors during container log collection?
  - 9.2 Log search and analysis
    - 9.2.1 FAQ about log query
    - 9.2.2 What can I do if no log data is retrieved?
    - 9.2.3 What are the differences between log consumption and log search and analytics?
    - 9.2.4 How do I resolve common errors returned in log data queries?
    - 9.2.5 Why data queries are inaccurate?
  - 9.3 Alarm
    - 9.3.1 FAQ about alerts

## 1 What is Log Service?

Log Service (SLS) is a one-stop logging service developed by Alibaba Cloud that is widely used by Alibaba Group in big data scenarios. You can use Log Service to collect, query, and consume log data. Without the need to invest in in-house data collection and processing systems. This enables you to focus on your business, improving business efficiency and helping your business to expand. Log Service provides the following features: Log collection: Log Service allows you to collect events, binary logs, and text logs in real time by using multiple methods, such as Logtail and JavaScript. Query and analysis: Log Service allows you to query and analyze the collected log data and view analysis results on charts and dashboards. Status alert: Log Service can automatically run query statements at regular intervals after you create an alert task. If the query results meet the conditions of the alert task, Log Service sends an alert to the specified recipients in real time. Real-time consumption: Log Service provides real-time consumption interfaces through which log consumers can consume log data.

## 2 Quick start

### 2.1 Procedure

This topic provides the basic procedure to use Log Service. You can use this procedure to create projects, create Logstores, and collect log data. The following figure shows the Procedure.
1. Optional. Obtain an AccessKey pair.
Before you can use Log Service through APIs or SDKs, you must have an AccessKey pair.
2. Create a project.
Create a project in a specified region and add a description.
3. Create a Logstore.
Create a Logstore for the project and specify the number of shards.
4. Collect text logs
Select a method to collect log data based on your business requirements. Text log collection is used as an example.
5. Enable the index feature and configure indexes for a Logstore, and query and analyze logs.
Log Service supports real-time log query andanalysis. After you enable the indexing feature, you can query and analyze logs and configure Overview and dashboards.
6. Configure an alert rule.
Log Service allows you to configure alerts based on log query results. Then, Log Service sends alerts by using multiple methods, such as a custom webhook.
7. Consume logs in real time.
Log Service allows you to consume logs by using multiple methods, such as a Spark Streaming client, Storm spout, and Flink connector.

### 2.2 Log on to the Log Service console

This topic describes how to log on to the Log Service console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. In the top navigation bar, choose Product s > Log Service.
5. On the page that appears, select the organization and region, and then click SLS. The home page of the Log
Service console is displayed.

### 2.3 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only the operation administrators or level-1 organization administrators can obtain the AccessKey pair of an organization. Context To call Apsara Uni-manager and cloud service APIs, we recommend that you use the AccessKey pair of a personal account. If you use the AccessKey pair of a personal account, you must configure header parameters as described in the following table for access control.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

> **Warning:** The AccessKey pairs of personal accounts are under control of the Apsara Uni-manager permission system. AccessKey pairs of organization accounts have higher permissions. For security purposes, organization operations must be approved by administrators.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click Personal
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view your AccessKey pair.

> Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account. You must keep your AccessKey pair confidential.

Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the organization navigation tree, click an organization name.
5. In the Current Organization section, click Management Accesskey.
6. In the Management AccessKey, view the AccessKey pair of the organization.

> Not e An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization.

### 2.4 Manage projects

This topic describes how to create, modify, and delete projects in the Log Service console. Context A project in Log Service is a resource management unit. The resources in each project are isolated from resources in other projects. We recommend that you store the log data of different applications in dedicated projects. You can manage Logstores, Logtail configurations, log sources, log data, and machine groups in a project. Each project provides an endpoint for you to access the resources. A project provides the following features: Allows you to store log data from different sources in different Logstores of a project. You can use Log Service to collect log data from multiple sources such as business projects, products, and environments. You can then store the log data of each source in a separate Logstore. This simplifies the downstream processes such as the consuming, exporting, and indexing of log data. In addition, you can manage access permissions at the project level. Provides an endpoint for you to access the resources in the project. Log Service allocates an exclusive endpoint to each project. You can use the endpoint to read, write, and manage the log data in the project. Create a project

> Not e
> You can create a project only by using the Log Service console.
> You can create up to 50 projects under each Apsara Stack tenant account.

1. Log on to the Log Service console.
2. In the Project s section, click Creat e Project .
3. Set the parameters based on your requirements. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Project Name | The name of the project. The project name must be unique across all regions. Use the following naming conventions: The name can contain lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit. The name must be 3 to 63 characters in length. Not e After a project is created, its name cannot be modified. |
| Description | The description of the project. After the project is created, the description is displayed in the Project s section. If you need to modify the description after the project is created, find the project in the Project s section, and click Edit in the Act ions column. The description must be 0 to 64 characters in length and cannot contain the following characters: < > ' \ " \\ . |
| Region | The region to which the project belongs. We recommend that you select a region that is closer to the log source. After a project is created, its region cannot be modified. This means that projects cannot be migrated across regions. |

4. Click OK.
Modify the description of a project To modify the description of a project, perform the following steps:
1. In the Project s section, find the project.
2. In the Act ions column, click Edit .
3. In the Modif y Project dialog box, modify the description of the project.

> Not e You cannot modify the project name or region.

4. Click OK.
View the information of a project To view the information of a project, click the project name in the Project s section. On the Overview page, you can view the project information such as the endpoint and region. Delete a project To delete a project, perform the following steps:

> **Warning:** After you delete a project, all logs and configurations in the project are deleted and cannot be restored.

1. In the Project s section, find the project.
2. In the Act ions column, click Delet e.
3. In the dialog box that appears, select a reason for deletion.
If you select Ot her issues, enter the reason in the text box.
4. Click OK.

### 2.5 Manage Logstores

This topic describes how to create, modify, and delete a Logstore in the Log Service console. A Logstore is a collection of resources inside a project. The log data in a Logstore is collected from the same source. Context You can create multiple Logstores in a project. We recommend that you create a Logstore for each type of application log. Logstores provide the following features: Real-time log collection Log storage and real-time log consumption Log indexing and real-time log query Create a Logstore

> Not e You can create a maximum of 100 Logstores in each project.

1. Log on to the Log Service console.
2. In the Project s section, click the name of a project.
3. On the page that appears, click
next to the search box.
4. In the Creat e Logst ore pane, set the parameters and click OK.

| Parameter | Description |
|---|---|
| Logstore Name | The name of the Logstore. The Logstore name must be unique in the project to which the Logstore belongs. The name can contain lowercase letters, digits, hyphens (-), and underscores ( ). _ The name must start and end with a lowercase letter or digit. The name must be 3 to 63 characters in length. Not e After a Logstore is created, its name cannot be modified. |
| WebTracking | Specifies whether to enable the WebTracking feature for the Logstore. You can use WebTracking to collect the log data of HTML websites, HTML5 websites, iOS apps, or Android apps and forward the data to Log Service. This feature is not enabled by default. |
| Permanent Storage | Specifies whether to permanently store the log data in the Logstore. If you disable this feature, you must specify a retention period for log data. |
| Data Retention Period | The duration for which log data is stored in the Logstore after the log data is collected. Unit: days. Valid values: 1 to 3000. When this period expires, the log data is deleted. |
| Shards | The number of shards in the Logstore. You can divide a Logstore into 1 to 10 shards. |
| Automatic Sharding | Specifies whether to enable the automatic sharding feature. This feature is not enabled by default. If you enable this feature, Log Service automatically splits shards in the Logstore when the data transfer exceeds the capacity of the existing shards. |
| Maximum Shards | The maximum number of shards. This parameter is required if you enable the automatic sharding feature. Maximum value: 64. |

| Parameter | Description |
|---|---|
| Log Public IP | Specifies whether to add the following information to the Tag field of each collected log entry: client ip : the public IP address of the log source. __ _ __ receive time : the time when Log Service receives the log entry. The __ _ __ value is a UNIX timestamp. |

Modify the configurations of a Logstore To modify the configurations of a Logstore, perform the following steps:
1. In the Project s section, click the name of the project to which the Logstore belongs.
2. On the page that appears, click the
icon next to the Logstore, and select Modif y from the shortcut menu.
3. In the upper-right corner of the Logst ore At t ribut es page, click Modif y.
You can modify the Dat a Ret ent ion Period, WebT racking, Aut omat ic Sharding, Maximum Shards, and Log Public IP parameters. You can also split or merge the existing shards.
4. Click Save.
Delete a Logstore To delete a Logstore, perform the following steps:

> Not e

After you delete a Logstore, the log data in the Logstore is deleted and cannot be restored. Before you can delete a Logstore, you must delete the Logtail configurations that are associated with the Logstore.
1. In the Project s section, click the name of the project to which the Logstore belongs.
2. On the page that appears, click the
icon next to the Logstore, and select Delet e from the shortcut menu.
3. In the message that appears, click OK.

### 2.6 Manage shards

This topic describes how to split, merge, and delete shards in the Log Service console. Logs are stored on shards in a Logstore. Each Logstore can have multiple shards. When you create a Logstore, you must specify the number of shards in the Logstore. After a Logstore is created, you can split or merge the shards. Hash key Log Service uses 128-bit MD5 hashes as the hash key of a Logstore. The entire MD5 hash range is [00000000000000000000000000000000,ffffffffffffffffffffffffffffffff). The hash key range of a Logstore falls within the entire MD5 hash range. When you create a Logstore, you must specify the number (N) of shards in the Logstore. The hash key range of the Logstore is evenly divided into N parts. Each part is assigned to a shard. The hash key range of a shard is a left-closed and right-open interval that is specified by the following parameters: BeginKey: the start of the hash key range. The value of this parameter is included in the range. EndKey: the end of the hash key range. The value of this parameter is excluded from the range. If you split a shard, the hash key range of the shard is evenly split. If you merge two shards, the hash key ranges of the shards are also merged. A hash key range determines the scope of a shard. When you push log data to a Logstore, you can specify a hash key for the log data. Log Service then writes the log data to the shard whose hash key range includes the specified hash key. This is called the hash key mode. If you do not specify a hash key for log data, the load balancing mode is used and Log Service writes the log data to a random available shard. However, when you pull log data from a Logstore, you must specify the shard where the log data is stored. For example, a Logstore is divided into four shards and the hash key range of the Logstore is [00,FF). lists the hash key range of each shard. Example shards

| Shard | Hash key range |
|---|---|
| Shard0 | [00,40) |
| Shard1 | [40,80) |
| Shard2 | [80,C0) |
| Shard3 | [C0,FF) |

If you set the hash key of log data to 5F, Log Service writes the log data to shard 1 because the hash key range of shard 1 includes 5F. If you set the hash key to 8C, the log data is written to shard 2 because the hash key range of shard 2 includes 8C. Read/write capacity Each shard provides an identical read/write capacity. Therefore, the read/write capacity of a Logstore depends on the number of shards in the Logstore. We recommend that you adjust the capacity of a Logstore based on the data traffic. For a Logstore, if the data traffic exceeds the read/write capacity, you can split shards to increase the Logstore capacity. If the data traffic is much less than the read/write capacity, you can merge shards to reduce the Logstore capacity and save costs. For example, a Logstore consists of two read/write shards and the shards provide a maximum write capacity of 10 MB/s. If log data is written to the Logstore at a rate of 14 MB/s, we recommend that you split one of the shards into two shards. However, if log data is written at a rate of 3 MB/s, you can merge the two shards because the capacity of one shard already meets the read/write requirements.

> Not e

If an API operation that writes data to a Logstore constantly returns 403 or 500 errors, you can check the data traffic metrics that are provided by Log Service and determine whether to split shards. If the data traffic of a Logstore exceeds the read/write capacity of the Logstore, Log Service provides the best possible service but does not guarantee the service quality. Shard status A shard can be in one of the following states: Read/write Read-only After a shard is created, the default status of the shard is read/write. If you split or merge shards, the status of the original shards changes to read-only and the new shards are in the read/write state. You can write data to and read data from a read/write shard. However, you can only read data from a read-only shard and cannot write data to the shard. If you need to split a shard in a Logstore, you must specify the ID of the shard and an MD5 hash. The shard must be in the read/write state. The MD5 hash must be greater than the value of the BeginKey parameter of the shard and less than the value of the EndKey parameter of the shard. After the shard is split, the Logstore has two more shards. The status of the original shard changes from read/write to read-only. You can consume the log data in the original shard but cannot write log data to the shard. The new shards are in the read/write state and are listed below the original shard. The hash key ranges of the new shards cover that of the original shard. If you need to merge shards in a Logstore, you must specify a read/write shard. The shard cannot be the last read/write shard in the shard list. Log Service finds the shard whose hash key range follows the hash key range of the specified shard, and merges the two shards into a new shard. The status of the original shards changes from read/write to read-only. You can consume the log data in the original shards but cannot write log data to the shards. The new shard is in the read/write state. The hash key range of the new shard covers those of the original shards. You can perform the following operations on shards in the Log Service console: Split a shard. Merge shards. Split a shard Each shard provides a write capacity of 5 MB/s and a read capacity of 10 MB/s. For a Logstore, if the data traffic exceeds the total read/write capacity of existing shards, we recommend that you split shards to increase the capacity.
1. Log on to the Log Service console.
2. In the Projects section, click the project that you want to manage.
3. On the Log St orage > Logst ores tab, find the Logstore whose configurations you want to modify, click the
icon, and then select Modif y.
4. In the upper-right corner of the Logst ore At t ribut es page, click Modif y.
5. In the Shard Management section, find the shard that you want to split, and click Split in the Act ions
column.
6. In the drop-down list, click the number of new shards.
7. In the Act ions column, click OK.
8. In the upper-right corner of the Logst ore At t ribut es page, click Save.
Enable the automatic sharding feature Log Service provides the automatic sharding feature. If you enable the automatic sharding feature for a Logstore, shards are automatically split if the following conditions are met: The data traffic of the Logstore exceeds the total capacity of the shards in the Logstore for more than five minutes. The number of read/write shards does not exceed the maximum number of shards that is allowed in the Logstore after an automatic shard split.

> Not e After a shard is split into multiple shards, the new shards will not be automatically split within 15 minutes.

When you create or modify a Logstore, you can enable the automatic sharding feature. If this feature is enabled, you must specify the maximum number of shards that is allowed in the Logstore after an automatic shard split. For more information, see Manage Logstores. Automatic Sharding Specifies whether to enable the automatic sharding feature. If you turn on this switch, the shards are automatically split when the preceding conditions are met. Maximum Shards The maximum number of shards that is allowed in the Logstore after an automatic shard split. The maximum value is 64. Merge shards You can merge shards in a Logstore to reduce the capacity of the Logstore.
1. In the upper-right corner of the Logst ore At t ribut es page, click Modif y.
2. In the Shard Management section, find the shard that you want to merge with another shard, and click
Merge in the Act ions column.
3. In the upper-right corner of the Logst ore At t ribut es page, click Save.
Delete a shard Automatic deletion When you create a Logstore, you can set a retention period for log data. When the retention period expires, the shards in the Logstore and the log data in the shards are automatically deleted. Manual deletion If you turn on the Permanent St orage switch when you create a Logstore, the shards in the Logstore and the log data in the shards are not automatically deleted. If you need to delete the shards and the log data in the shards, you can delete the Logstore. For more information, see Delete a Logstore.

## 3 Data collection

### 3.1 Collection by Logtail

#### 3.1.1 Overview

##### 3.1.1.1 Logtail overview

Logtail is a log collection agent provided by Log Service. You can use Logtail in Log Service console to collect logs in real time from multiple sources. These sources include Alibaba Cloud Elastic Compute Service (ECS) instances, servers deployed in on-premises data centers, and servers provided by other cloud service providers. Logtail-based log collection Benefits Provides non-intrusive log collection based on log files. You do not need to modify the application code. Log collection does not affect the operation logic of your applications. Supports the collection of multiple logs, such as text logs, binlogs, HTTP logs, and container stdout logs. Collects data from standard containers and various container clusters, such as swarm clusters and Kubernetes clusters. Handles various exceptions that occur in the log collection process. If a network or server exception occurs, Logtail retries log collection and locally caches logs to ensure data security. Provides centralized management based on Log Service. After you install Logtail on the servers from which you want to collect logs, you can configure these servers and the collection method in the Log Service console. You do not need to log on to the servers. Provides a comprehensive self-protection mechanism. To minimize the impact of Logtail on the performance of the related servers, Logtail limits the usage of CPU, memory, and network resources. Processing capabilities and limits For more information, see Limits. Configuration process Configuration process To collect logs from servers by using Logtail, follow these steps:
1. Install Logtail. For more information about how to install Logtail on a server from which you want to collect
logs, see Install Logtail in Linux and Install Logtail in Windows.
2. Log Service use server groups to manage all servers from which you want to collect logs by using Logtail. Log
Service allows you to define server groups by using IP addresses or custom identifiers. You can create a server group as prompted when you apply Logtail configurations to server groups.
3. Create a Logtail configuration and apply it to the server group. For more information about how to create a
Logtail configuration, see Configure text log collection. After the preceding process is complete, logs on the server are automatically collected and sent to the selected Logstore. However, historical logs are not collected. You can use the Log Service console, SDKs, or APIs to query these logs. Log Service allows you to view the status of log collection and check whether errors occur. For more information, see Collect logs by using Logtail. Containers For information about Alibaba Cloud Container Service for Kubernetes or user-created Kubernetes clusters, see Collect Kubernetes logs. For information about other user-created Docker clusters, see Collect standard Docker logs. Terms Server group: A server group contains one or more servers from which logs of a specific type are collected. You can apply Logtail configurations to a server group. This enables Log Service to collect logs from all servers in the server group. You can use the Log Service console to manage a sever group. For example, you can create, delete, add, or remove a server. Each server group can contain different versions of Windows servers or Linux servers. Logtail: Logtail is the agent that collects logs from the servers on which Logtail runs. For more information, see Install Logtail in Linux and Install Logtail in Windows. After you install Logtail on a server, you must create a Logtail configuration and apply it to the server group to which the server belongs. In Linux, Logtail is installed in the `/usr/local/ilogtail` directory. Logtail initiates two separate processes whose names start with ilogtail. One is a collection process and the other is a daemon process. The program

| running log is /usr/local/ilogtail/ilogtail.LOG . In Windows, Logtail is installed in the C:\Program Files\Alibaba\Logtail m Files (x86)\Alibaba\Logtail (for 64-bit systems) directory. You can ch | /usr/local/ilogtail/ilogtail.LOG |   | . |
|---|---|---|---|
|   |   | C:\Program Files\Alibaba\Logtail |   |
| m Files (x86)\Alibaba\Logtail |   |   |   |

Services to view the two Windows services generated from Logtail. One is LogtailWorker (log collection process) and the other is LogtailDaemon. The program running log is `logtail_*.log` in the installation directory. Logtail configuration: A Logtail configuration is a set of policies that are used by Logtail to collect logs. You can specify Logtail parameters such as the data source and collection mode. This allows you to customize log collection policies for all servers in a server group. A Logtail configuration determines how to collect a type of logs from a server, parse the logs, and send them to a specified Logstore. You can create a Logtail configuration for a Logstore in the Log Service console. This enables the Logstore to receive logs that are collected by using this Logtail configuration. Features Logtail provides the following features:

| Feature | Description |
|---|---|
| Real-time log collection | Logtail dynamically monitors log files and reads and parses incremental logs in real time. In most cases, logs are sent to Log Service within 3 seconds after they are generated. Not e Logtail does not collect historical data. If Logtail reads a log later than 12 hours after the log was generated, Logtail drops the log. |
| Automatic log rotation | Some applications rotate log files based on the file size or date. In the rotation process, the original log files are renamed and empty log files are created. For example, files such as app.LOG.1 and app.LOG.2 are generated for the app.LOG file after log rotation. You can specify the file (for example, app.LOG) to which collected logs are written. Logtail monitors the log rotation process to ensure that no logs are lost. |
| Multiple data sources | Logtail can collect text logs, syslogs, HTTP logs, and MySQL binlogs. |
| Automatic exception handling | If data transmission fails due to exceptions such as Log Service errors, network errors, or quota exhaustion, Logtail retries log collection based on the specific scenario. If the retry fails, Logtail writes the data to the local cache and resends the data after the exception no longer exists. |
| Flexible collection policy configuration | You can create a Logtail configuration to specify how logs are collected from an ECS instance. You can select log directories and files by using exact match or wildcard match based on actual scenarios. You can also customize the extraction method of collected logs and the names of extracted fields. Log Service allows you to extract logs by using regular expressions. The log data models of Log Service require that each log has a precise timestamp. Logtail provides custom log time formats. This allows you to extract the required timestamps from log data of different formats. |
| Automatic synchronization of Logtail configurations | After you create or update a Logtail configuration in the Log Service console, Logtail receives and validates the configuration within 3 minutes. No data loss occurs during the configuration update process. |

| og Service | User Guide·Data collectio |
|---|---|

| Feature | Description |
|---|---|
| Automatic upgrade | After you install Logtail on a server, Log Service manages the automatic upgrade of Logtail without manual intervention. No data loss occurs during the Logtail upgrade process. |
| Status monitoring | Logtail monitors its consumption of CPU and memory in real time. This prevents Logtail from excessively consuming your resources. If the resource consumption exceeds the limit, Logtail restarts to avoid affecting other services on the server. Logtail limits network traffic to avoid excessive bandwidth consumption. |
| Data transmission with a signature | Logtail obtains your Alibaba Cloud AccessKey pair and uses it to sign all log data packets before they are sent. This prevents data tampering during transmission. Not e Logtail obtains your Alibaba Cloud AccessKey pair over HTTPS to ensure the security of your AccessKey pair. |

Data collection reliability During data collection, Logtail stores the collected checkpoints to the local directory on a regular basis. If an exception (for example, an unexpected server shutdown or a process crash) occurs, Logtail restarts and then collects data from the last recorded checkpoint to prevent data loss. Logtail runs based on the resource limits specified in the configuration file. If the usage of a resource exceeds the limit for more than 5 minutes, Logtail restarts. After the restart, duplicate data may be generated. Logtail uses multiple internal mechanisms to improve log collection reliability. However, logs may be lost in the following conditions: Logtail is not running but logs are rotated multiple times. The log rotation rate is high, for example, one rotation per second. The log collection rate is lower than the log generation rate for a long period of time.

##### 3.1.1.2 Log collection process of Logtail

This topic describes the process that Logtail uses to collect server logs. The process consists of the following steps: monitor files, read files, process logs, filter logs, aggregate logs, and send logs.

> Not e After the Logtail configuration is applied to a machine group, unmodified logs on the servers in the machine group are considered as historical logs. Logtail does not collect historical logs in normal running mode. If you want to collect historical logs, see Import historical logs.

Monitor files After you install Logtail on a server and create a Logtail configuration based on a data source, the Logtail configuration is delivered from Log Service to Logtail in real time. Then, Logtail starts to monitor files based on the Logtail configuration.
1. Logtail scans log directories and files that comply with the specified file naming rules based on the specified
log path and maximum monitoring directory depth. Logtail registers event monitoring and periodical polling for the directory from which Logtail collect logs. In Linux, Inotify is used. In Windows, ReadDirectoryChangesW is used. This method ensures the timeliness and stability of log collection.
2. If the compliant log files in the specified directory are not modified after the configuration is applied, Logtail
does not collect these files. If modification events are generated for log files, Logtail triggers the collection process and reads these files. Read files After Logtail detects that a log file has been updated, Logtail reads the log file. If Logtail reads the log file for the first time, it checks the file size. If the file size is less than 1 MB, Logtail reads the file from the beginning. If the file size is greater than 1 MB, Logtail reads the file from the last 1 MB of data. If Logtail has read the file before, Logtail reads the file from the last checkpoint. Logtail can read up to 512 KB of data at a time. Therefore, you must limit the log size to 512 KB.

> Not ice If you have changed the system time on your server, you must manually restart Logtail. Otherwise, the log time is incorrect and logs are dropped.

Process logs When Logtail reads a log, it divides the log into multiple lines, parses the log, and sets the time field of the log. Divide each log into multiple lines If you specifies Regex t o Mat ch First Line Only in the Logtail configuration, the log data read by Logtail at one time is divided into multiple lines based on the specified beginning of the line. If the beginning of the line is not specified, each data block is processed as a log. Parse each log Logtail parses each log based on the Logtail configuration, such as regular expressions, delimiters, and JSON.

> Not ice A complicated regular expression may lead to high CPU usage. Therefore, we recommend that you use an efficient regular expression.

Handle parsing failures Logtail determines how to handle parsing failures based on whether the Drop Failed to Parse Logs switch is turned on in the Logtail configuration. If the Drop Failed t o Parse Logs is turned on, Logtail drops the logs that fail to be parsed and reports an error. If the f eat ure switch is turned off, Logtail uploads the logs that fail to be parsed. In these logs, the key is set to raw_log and the value is set to the log content. Set the time field of a log If the time field of the log is not specified, the log time is the current parsing time. If the time field of the log is specified, the following operations are performed: The log time is extracted from the parsed log fields if the difference between the log time and the current time is less than 12 hours. The log is dropped and an error is reported if the difference between the log time and the current time is greater than 12 hours. Filter logs After Logtail process logs, it filters the logs based on the filter configuration. If the Filt er Conf igurat ion is not specified, Logtail does not filter logs and proceed with the next step. If the Filt er Conf igurat ion is specified, Logtail traverses and verifies all the fields of each log. Logtail collects a log if the log matches the filter configuration. Logtail does not collect a log if the log does not match the filter configuration. Aggregate logs Logtail sends the logs that match the filter configuration to Log Service. To reduce the number of network requests, Logtail caches the processed and filtered logs for a period of time. Then, Logtail aggregates and packages these logs before sending them to Log Service. If one of the following conditions is met during caching, logs are immediately packaged and sent to Log Service. The log aggregation period exceeds three seconds. The number of aggregated logs exceeds 4,096. The total size of aggregated logs exceeds 512 KB. Send logs Logtail sends the aggregated logs to Log Service. You can set the `max_bytes_per_sec` and `send_request_concurrency` parameters in Set Logtail startup parameters to adjust the log data sending rate and the maximum concurrent requests. In this case, Logtail ensures that the sending rate and the concurrent requests do not exceed the limits. If the log data fails to be sent, Logtail retries or stops the operation based on the error message.

| Error | Description | Handling method |
|---|---|---|
| 401 | Logtail is not authorized to collect data. | Logtail drops the log packets. |
| 404 | The specified project or Logstore does not exist in the Logtail configuration. | Logtail drops the log packets. |
| 403 | The shard quota is exhausted. | Logtail waits for three seconds and retries. |
| 500 | A Log Service exception has occurred. | Logtail waits for three seconds and retries. |
| Network timeout | A network connection error has occurred. | Logtail waits for three seconds and retries. |

##### 3.1.1.3 Logtail configuration files and record files

This topic describes the basic configuration files and record files of Logtail. When Logtail is active, it uses a series of configuration files and generates record files. The basic configuration files are as follows: Startup configuration file (ilogtail_config.json) Account ID configuration file User-defined identifier file (user_defined_id) Logtail configuration file (user_log_config.json) The basic record files are as follows: AppInfo record file (app_info.json) Logtail operational log file (ilogtail.LOG) Logtail plug-in log file (logtail_plugin.LOG) Container path mapping file (docker_path_config.json) Startup configuration file (ilogtail_config.json) This file is used to query or set Logtail runtime parameters. The file is in the JSON format. After you install Logtail, you can use the startup configuration file to perform the following operations: Change the values of the Logtail runtime parameters. You can change the CPU usage threshold, usage threshold of terminate and stay resident (TSR) programs, and other settings. Check whether the installation commands are correct. The settings of `config_server_address` and `data_server_list` in this file depend on the parameters and installation commands selected when you installed Logtail. If the region specified in config_server_address is unreachable or is different from the region where Log Service resides, the selected parameters or commands are incorrect. In this case, Logtail cannot collect logs and must be reinstalled.

> **Warning:** The file must be a valid JSON file. Otherwise, Logtail cannot be started.
> If you modify the file, you must restart Logtail to validate your modifications.

The following table describes the default parameters in the startup configuration file. You can also add other parameters. For more information, see Set Logtail startup parameters. Default parameters

| Parameter | Description |
|---|---|
| config server address _ _ | The address that Logtail uses to receive the configuration file from Log Service. This address depends on the parameters and installation commands that you selected when you installed Logtail. Ensure that the address is reachable and is in the same region as Log Service. |
| data server list _ _ | The data server address. This address depends on the parameters and installation commands that you selected when you installed Logtail. Ensure that the address is reachable and is in the same region as Log Service. |
| cluster | The name of the region where a server resides. |
| endpoint | The endpoint of Log Service. For more information, see View the information of a project. |
| cpu usage limit _ _ | The CPU usage threshold, which is calculated by core. |
| mem usage limit _ _ | The TSR usage threshold. |
| max bytes per sec _ _ _ | The traffic limit on the raw data that is sent by Logtail. If the value of this parameter is greater than 20 Mbit/s, traffic limiting does not take effect. |
| process thread count _ _ | The number of threads that Logtail uses to write data to log files. |
| send request concurrency _ _ | The number of concurrent requests for sending data packets asynchronously. Logtail sends data packets asynchronously by default. If the write transactions per second (TPS) is high, you can set a greater value for this parameter. |

File path Linux: The file is stored in /usr/local/ilogtail/ilogtail_config.json. Container Service: The file is stored in a Logtail container. The file path is specified in the environment variable

| ALIYUN LOGTAIL CONFIG _ _ | of the Logtail contai |
|---|---|

`ALIYUN_LOGTAIL_CONFIG` of the Logtail container. You can run the command docker inspect ${logtail_co ntainer_name} | grep ALIYUN_LOGTAIL_CONFIG to query the file path. For example, the file path is /etc/ilogt ail/conf/cn-hangzhou/ilogtail_config.json. Windows: 64-bit: The file is stored in C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json. 32-bit: The file is stored in C:\Program Files\Alibaba\Logtail\ilogtail_config.json. Sample file

```
$cat /usr/local/ilogtail/ilogtail_config.json
```

`{`

```json
    "config_server_address" : "http://logtail.cn-hangzhou-intranet.log.aliyuncs.com",
    "data_server_list" :
```

`[` `{`

```json
            "cluster" : "ap-southeast-2",
            "endpoint" : "cn-hangzhou-intranet.log.aliyuncs.com"
```

`}` `],`

```json
    "cpu_usage_limit" : 0.4,
    "mem_usage_limit" : 100,
    "max_bytes_per_sec" : 2097152,
    "process_thread_count" : 1,
    "send_request_concurrency" : 4,
    "streamlog_open" : false
```

`}` Account ID configuration file This file contains the ID of your Apsara Stack tenant account. The file indicates that the account can collect logs from the server where Logtail is installed. If you want to collect logs from ECS instances that do not belong to your account or from on-premises data centers, you must create an account ID configuration file.

> Not e
> The file is used only when you collect logs from ECS instances that do not belong to your account and or from on-premises data centers.
> The file can contain only the ID of your Apsara Stack tenant account. It cannot contain the IDs of RAM users under your Apsara Stack tenant account.
> The file name cannot contain a suffix.
> Each Logtail can have multiple account ID configuration files. Each Logtail container can have only one account ID configuration file.

File path Linux: The file is stored in `/etc/ilogtail/users/` . Container Service: The file is stored in a Logtail container. The file path is specified in the environment variable `ALIYUN_LOGTAIL_USER_ID` of the Logtail container. You can run the command docker inspect ${logtail_c ontainer_name} | grep ALIYUN_LOGTAIL_USER_ID to query the file path. Windows: The file is stored in C:\LogtailData\users\ . Sample file

```
$ls /etc/ilogtail/users/
**************** *****************
```

User-defined identifier file (user_defined_id) This file is used to configure machine groups with user-defined identifiers. For more information, see Create a machine group based on a custom ID.

> Not e
> This file is used only when you configure a machine group with user-defined identifiers.
> If you configure multiple user-defined identifiers for a machine group, separate them with line breaks.

File path Linux: The file is stored in /etc/ilogtail/user_defined_id. Container Service: The file is stored in a Logtail container. The file path is specified in the environment variable `ALIYUN_LOGTAIL_USER_DEFINED_ID` of the Logtail container. You can run the command docker inspect ${logt ail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID to query the file path. Windows: The file is stored in C:\LogtailData\user_defined_id. Sample file

```
$cat /etc/ilogtail/user_defined_id aliyun-ecs-rs1e16355
```

Logtail configuration file (user_log_config.json) This file contains the Logtail configuration that Logtail receives from Log Service. The file is in the JSON format and is updated along with configuration updates. You can use this file to check whether the Logtail configuration is delivered to the server where Logtail is installed. If the Logtail configuration file exists and all contents in the file are up to date, the Logtail configuration is delivered.

> Not ice
> We recommend that you do not modify the Logtail configuration file unless you need to specify sensitive information, such as the AccessKey pair and database password.
> You must upload this file when you submit a ticket.

File path Linux: The file is stored in /usr/local/ilogtail/user_log_config.json. Container Service: The file is stored in /usr/local/ilogtail/user_log_config.json. Windows 64-bit: The file is stored in C:\Program Files (x86)\Alibaba\Logtail\user_log_config.json. 32-bit: The file is stored in C:\Program Files\Alibaba\Logtail\user_log_config.json. Sample file

```
$cat /usr/local/ilogtail/user_log_config.json
```

`{`

```json
   "metrics" : {
      "##1.0##k8s-log-c12ba2028*****939f0b$app-java" : {
         "aliuid" : "16542189*****50",
         "category" : "app-java",
         "create_time" : 1534739165,
         "defaultEndpoint" : "cn-hangzhou-intranet.log.aliyuncs.com",
         "delay_alarm_bytes" : 0,
         "enable" : true,
         "enable_tag" : true,
         "filter_keys" : [],
         "filter_regs" : [],
         "group_topic" : "",
         "local_storage" : true,
         "log_type" : "plugin",
         "log_tz" : "",
         "max_send_rate" : -1,
         "merge_type" : "topic",
         "plugin" : {
            "inputs" : [
```

`{`

```json
                  "detail" : {
                     "IncludeEnv" : {
                        "aliyun_logs_app-java" : "stdout"
```

`},`

```json
                     "IncludeLable" : {
                        "io.kubernetes.container.name" : "java-log-demo-2",
                        "io.kubernetes.pod.namespace" : "default"
```

`},`

```json
                     "Stderr" : true,
                     "Stdout" : true
```

`},`

```json
                  "type" : "service_docker_stdout"
```

`}` `]` `},`

```json
         "priority" : 0,
         "project_name" : "k8s-log-c12ba2028c*****ac1286939f0b",
         "raw_log" : false,
         "region" : "cn-hangzhou",
         "send_rate_expire" : 0,
         "sensitive_keys" : [],
         "tz_adjust" : false,
         "version" : 1
```

`}` `}` `}` AppInfo record file (app_info.json) This file contains the startup time of Logtail. It also contains the IP address and hostname that Logtail obtains. You must check the IP address obtained by Logtail when you configure an IP address-based machine group. In most cases, Logtail obtains server IP addresses based on the following rules: If the IP address of a server is associated with its hostname in the /etc/hosts server file, Logtail obtains the IP address. If the IP address of a server is not associated with its hostname, Logtail obtains the IP address of the first network interface card (NIC) on the server.

> Not e
> The AppInfo record file contains only the basic Logtail information, which cannot be manually modified.
> If you modify the hostname or other network settings of the server, you must restart Logtail to obtain a new IP address.

Parameters

| Parameter | Description |
|---|---|
| UUID | The serial number of the server. |
| hostname | The hostname. |
| instance id _ | The unique identifier of Logtail. This identifier is randomly generated. |
| ip | The IP address that is obtained by Logtail. If this parameter is not specified, Logtail has not obtained the IP address of a server. In this case, Logtail cannot function properly. You must set an IP address for your server and restart Logtail. Not e If the machine group is an IP address-based machine group, ensure that the IP address specified for the machine group is the same as the value of this parameter. If the two IP address are different, modify the IP address that you specified for the machine group in the Log Service console. Check the IP addresses again after 1 minute. |
| logtail version _ | The version of Logtail. |
| os | The version of the operating system. |
| update time _ | The last startup time of Logtail. |

File path Linux: The file is stored in /usr/local/ilogtail/app_info.json. Container Service: The file is stored in /usr/local/ilogtail/app_info.json. Windows 64-bit: The file is stored in C:\Program Files (x86)\Alibaba\Logtail\app_info.json. 32-bit: The file is stored in C:\Program Files\Alibaba\Logtail\app_info.json. Sample file

```
$cat /usr/local/ilogtail/app_info.json
```

`{`

```json
   "UUID" : "",
   "hostname" : "logtail-ds-slpn8",
   "instance_id" : "E5F93BC6-B024-11E8-8831-0A58AC14039E_1**. ***. ***.***_1536053315",
   "ip" : "1**. ***. ***.***",
   "logtail_version" : "0.16.13",
   "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64",
   "update_time" : "2018-09-04 09:28:36"
```

`}` Logtail operational log file (ilogtail.LOG) This file contains operational information about Logtail. Log severity levels are ranked as follows in ascending order: `INFO` , `WARN` , `ERROR` . Logs of the `INFO` level can be ignored. File path For Linux: The file is stored in /usr/local/ilogtail/ilogtail.LOG. Container Service: The file is stored in /usr/local/ilogtail/ilogtail.LOG. Windows 64-bit: The file is stored in C:\Program Files (x86)\Alibaba\Logtail\logtail_*.log. 32-bit: The file is stored in C:\Program Files\Alibaba\Logtail\logtail_*.log. Sample file

```json
$tail /usr/local/ilogtail/ilogtail.LOG [2018-09-13 01:13:59.024679] [INFO] [3155] [build/release64/sls/ilogtail/elogtail.cpp:123] change working dir:/usr/local/ilogtail/ [2018-09-13 01:13:59.025443] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:175 ] load logtail config file, path:/etc/ilogtail/conf/ap-southeast-2/ilogtail_config.json [2018-09-13 01:13:59.025460] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:176 ] load logtail config file, detail:{
   "config_server_address" : "http://logtail.ap-southeast-2-intranet.log.aliyuncs.com",
   "data_server_list" : [
```

`{`

```json
         "cluster" : "ap-southeast-2",
         "endpoint" : "ap-southeast-2-intranet.log.aliyuncs.com"
```

`}` `]` Logtail plug-in log file (logtail_plugin.LOG) This file contains operational information about plug-ins, such as stdout, binlog, and HTTP plug-ins. Log severity levels are ranked as follows in ascending order: `INFO` , `WARN` , `ERROR` . Logs of the `INFO` level can be ignored. File path Linux: The file is stored in /usr/local/ilogtail/logtail_plugin.LOG Container Service: The file is stored in /usr/local/ilogtail/logtail_plugin.LOG. Windows: The file is not supported. Sample file

```
$tail /usr/local/ilogtail/logtail_plugin.LOG 2018-09-13 02:55:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 02:55:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop 2018-09-13 03:00:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 03:00:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop 2018-09-13 03:03:26 [INF] [log_file_reader.go:221] [ReadOpen] [##1.0##sls-zc-test-hz-pub$docker-std out-config,k8s-stdout] open file for read, file:/logtail_host/var/lib/docker/containers/7f46afec 6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f114 8b2e2f31bd3410f5b2d624-json.log offset:40379573 status:794354-64769-40379963 2018-09-13 03:03:26 [INF] [log_file_reader.go:221] [ReadOpen] [##1.0##k8s-log-c12ba2028cfb444238cd9 ac1286939f0b$docker-stdout-config,k8s-stdout] open file for read, file:/logtail_host/var/lib/doc ker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59 ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379573 status:794354-64769-40 379963 2018-09-13 03:04:26 [INF] [log_file_reader.go:308] [CloseFile] [##1.0##sls-zc-test-hz-pub$docker-st dout-config,k8s-stdout] close file, reason:no read timeout file:/logtail_host/var/lib/docker/ containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9c dfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379963 status:794354-64769-403799 2018-09-13 03:04:27 [INF] [log_file_reader.go:308] [CloseFile] [##1.0##k8s-log-c12ba2028cfb444238cd 9ac1286939f0b$docker-stdout-config,k8s-stdout] close file, reason:no read timeout file:/logta il_host/var/lib/docker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/ 7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379963 sta tus:794354-64769-40379963 2018-09-13 03:05:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 03:05:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop
```

Container path mapping file (docker_path_config.json) This file is automatically created only when container files are collected. It records path mappings between container files and actual files. The file is in the JSON format.

> Not e This file is only an information record file. Modifications to this file do not take effect. If you delete this file, another one is automatically created without service interruptions.

File path The file is stored in /usr/local/ilogtail/docker_path_config.json. Sample file

```
$cat /usr/local/ilogtail/docker_path_config.json
```

`{`

```json
   "detail" : [
```

`{`

```json
         "config_name" : "##1.0##k8s-log-c12ba2028cfb444238cd9ac1286939f0b$nginx",
         "container_id" : "df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330d10",
         "params" : "{\n   \"ID\" : \"df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330
d10\",\n \"Path\" : \"/logtail_host/var/lib/docker/overlay2/947db346695a1f65e63e582ecfd10ae1f5701 9a1b99260b6c83d00fcd1892874/diff/var/log\",\n \"Tags\" : [\n \"nginx-type\",\n \"access -log\",\n \"_image_name_\",\n \"registry.cn-hangzhou.aliyuncs.com/log-service/docker-logtest:latest\",\n \"_container_name_\",\n \"nginx-log-demo\",\n \"_pod_name_\",\n \"nginx-log-demo-h2lzc\",\n \"_namespace_\",\n \"default\",\n \"_pod_uid_\",\n \"87e56ac3-b65b-11e8-b172-00163f008685\",\n \"_container_ip_\",\n \"172.20.4.224\",\n \"purpose\",\n \"test\"\n ]\n}\n"
```

`}` `],`

```json
   "version" : "0.1.0"
```

`}`

#### 3.1.2 Installation

##### 3.1.2.1 Install Logtail in Linux

This topic describes how to install Logtail on a Linux server. Supported systems Logtail supports the following x86-64 (64-bit) Linux operating systems: Aliyun Linux Ubuntu Debian CentOS openSUSE Red Hat

> Not e If you have installed Logtail, the installer will uninstall the existing version of Logtail, delete the
> `/usr/local/ilogtail` directory, and then reinstall Logtail. By default, Logtail runs after the installation and
> at startup.

1. Run the following command to download the Logtail installer:

```
wget http://${service:sls-backend-server:sls_data.endpoint}/logtail.sh -O logtail.sh; chmod 755 lo gtail.sh
```

> Not e You must replace ${service:sls-backend-server:sls_data.endpoint} in the command with the actual endpoint. For more information about endpoints, see View the information of a project.

2. Run the installation command.
Start Linux PowerShell and run the following command as an administrator to install Logtail:

```
./logtail.sh install
```

3. Configure an account ID for a server.
View the version of Logtail To view the version of Logtail, open the file in the `/usr/local/ilogtail/app_info.json` directory. The `logtail_version` field shows the version of Logtail.

```
$cat /usr/local/ilogtail/app_info.json
```

`{`

```json
   "UUID" : "0DF18E97-0F2D-486F-B77F-*********",
   "hostname" : "david*******",
   "instance_id" : "F4FAFADA-F1D7-11E7-846C-00163E30349E_*********_1515129548",
   "ip" : "**********",
   "logtail_version" : "0.16.0",
   "os" : "Linux; 2.6.32-220.23.2.ali1113.el5.x86_64; #1 SMP Thu Jul 4 20:09:15 CST 2013; x86_64",
   "update_time" : "2018-01-05 13:19:08"
```

`}` Upgrade Logtail You can use the Logtail installer (logtail.sh) to upgrade Logtail. The installer selects an upgrade method based on the configurations of the existing Logtail.

> Not e During the upgrade, Logtail is temporarily stopped. Only related files are overwritten. The configuration file, checkpoint file, and logs are retained.

Run the following commands to upgrade Logtail:

```python
# Download the Logtail installer.
wget http://${service:sls-backend-server:sls_data.endpoint}/logtail.sh -O logtail.sh; chmod 755 logtai l.sh
# Upgrade Logtail.
sudo ./logtail.sh upgrade
```

Response:

```bash
# The upgrade is successful.
Stop logtail successfully. ilogtail is running Upgrade logtail success
```

`{`

```json
   "UUID" : "***",
   "hostname" : "***",
   "instance_id" : "***",
   "ip" : "***",
   "logtail_version" : "0.16.11",
   "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64",
   "update_time" : "2018-08-29 15:01:36"
```

`}`

```bash
# The upgrade fails because the current version is the latest version.
[Error]: Already up to date.
```

Start and stop Logtail Start Logtail Run the following command as an administrator:

```
/etc/init.d/ilogtaild start
```

Stop Logtail Run the following command as an administrator:

```
/etc/init.d/ilogtaild stop
```

Uninstall Logtail Run Linux PowerShell as an administrator to uninstall Logtail:

```
wget http://${service:sls-backend-server:sls_data.endpoint}/logtail.sh -O logtail.sh chmod 755 logtail.sh ./logtail.sh uninstall
```

##### 3.1.2.2 Install Logtail in Windows

This topic describes how to install Logtail on a Windows server. Supported systems Logtail supports the following Windows operating systems: Windows 7 (Client) 32-bit Windows 7 (Client) 64-bit Windows Server 2008 32-bit Windows Server 2008 64-bit Windows Server 2012 64-bit Windows Server 2016 64-bit
1. Download the installation package.
Run the following command to download the installation package:

```
wget http://${service:sls-backend-server:sls_data.endpoint}/windows/logtail_installer.zip
```

> Not e You must replace ${service:sls-backend-server:sls_data.endpoint} in the command with the actual endpoint. For more information about endpoints, see View the information of a project.

2. Decompress the `logtail_installer.zip` package to the current directory.
3. Run the installation command.
Run Windows PowerShell or Command Prompt as an administrator. Enter the `logtail_installer` directory, and then run the installation command based on the network type.

```
.\logtail_installer.exe install me-east-1
```

> Not e You must replace ${region} in the command with the actual endpoint. For more information about endpoints, see View the information of a project.

4. Configure an account ID for a server.
Installation directory After you run the installation command, Logtail is installed in the specified directory. The directory cannot be changed. In the directory, you can View the version of Logtail in the app_info.json file or Uninstall Logtail. The installation directory is as follows: 32-bit Windows: C:\Program Files\Alibaba\Logtail 64-bit Windows: C:\Program Files (x86)\Alibaba\Logtail

> Not e You can run 32-bit or 64-bit applications in a 64-bit Windows operating system. However, the operating system stores 32-bit applications in separate x86 folders to ensure compatibility.
> Logtail for Windows is a 32-bit application. Therefore, it is installed in the Program Files (x86) folder in 64-bit Windows. If Logtail for 64-bit Windows becomes available in the future, it will be installed in the Program Files folder.

View the version of Logtail To view the version of Logtail, go to the default installation directory, and then use the notepad or another text editor to open the app_info.json file. The `logtail_version` field shows the version of Logtail. In the following example, the version of Logtail is 1.0.0.0: `{`

```json
    "logtail_version" : "1.0.0.0"
```

`}` Upgrade Logtail Automatic upgrade Logtail later than 1.0.0.0 is automatically upgraded in Windows. Manual upgrade Logtail earlier than 1.0.0.0 must be manually upgraded. The manual upgrade procedure is the same as the installation procedure.

> Not e During a manual upgrade, the files in the original installation directory are deleted. We recommend that you back up the files before you perform a manual upgrade.

Start and stop Logtail Open the Cont rol Panel, choose System and Security > Administ rat ive T ools, and then double-click Services. Find the service based on your Logtail version. Logtail 0.x.x.x: LogtailWorker. Logtail 1.0.0.0 and later: LogtailDaemon. Perform the following operations as required: Start Logtail Right-click the service and select St art from the shortcut menu. Stop Logtail Right-click the service and select St op from the shortcut menu. Restart Logtail Right-click the service and select Rest art from the shortcut menu. Uninstall Logtail Run Windows PowerShell or Command Prompt as an administrator. Enter the `logtail_installer` directory, and then run the following command:

```
.\logtail_installer.exe uninstall
```

After Logtail is uninstalled, the installation directory is deleted. However, some residual configuration data is still maintained in the C:\LogtailData directory. You can manually delete the data. The residual configuration data includes the following information: checkpoint: checkpoints of all plug-ins, for example, the Windows event log plug-in. logtail_check_point: checkpoints of Logtail. users: IDs of Apsara Stack tenant accounts.

##### 3.1.2.3 Set Logtail startup parameters

This topic describes how to set Logtail startup parameters. Context You may need to set Logtail startup parameters in the following scenarios: You need to collect a large number of log files that consume much memory. You want to maintain the metadata (such as the file signature, collection location, and file name) of each file in the memory. The CPU usage is high due to heavy log data traffic. The traffic sent to Log Service is heavy due to a large amount of log data. You want to collect syslogs or TCP data streams. Startup configurations File path

```
/usr/local/ilogtail/ilogtail_config.json
```

File format JSON Sample file (only partial configurations are provided) `{`

```json
    ...
    "cpu_usage_limit" : 0.4,
    "mem_usage_limit" : 100,
    "max_bytes_per_sec" : 2097152,
    "process_thread_count" : 1,
    "send_request_concurrency" : 4,
    "streamlog_open" : false,
    "streamlog_pool_size_in_mb" : 50,
    "streamlog_rcv_size_each_call" : 1024,
    "streamlog_formats":[],
    "streamlog_tcp_port" : 11111,
    "buffer_file_num" : 25,
    "buffer_file_size" : 20971520,
    "buffer_file_path" : "",
    ...
```

`}` Startup parameters

| Parameter | Description | Example |
|---|---|---|
| cpu usage limit _ _ | The CPU usage threshold for a single core. Data type: double. | For example, the value 0.4 indicates that the CPU usage of Logtail is limited to 40% processing capacity of a single core. In most cases, the processing capacity of a single core is about 24 MB/s in the simple mode and 12 MB/s in the full regex mode. |
| mem usage limit _ _ | The usage threshold of the resident memory. Data type: integer. Unit: MB. | For example, the value 100 indicates that the memory usage of Logtail is limited to 100 MB. If the threshold is exceeded, Logtail restarts. If you want to collect more than 1,000 log files, you can increase the threshold value. |
| max bytes per sec _ _ _ | The traffic limit on the raw data that is sent by Logtail. Data type: integer. Unit: bytes/s. | For example, the value 2097152 indicates that the data transfer rate of Logtail is limited to 2 MB/s. |

| Parameter | Description | Example |
|---|---|---|
| process thread count _ _ | The number of threads that Logtail uses to process data. | Default value: 1. Each thread provides a write speed of 24 MB/s in the simple mode and 12 MB/s in the full regex mode. We recommend that you do not modify the default value. |
| send request concurrency _ _ | Logtail sends data packets asynchronously by default. If the write transactions per second (TPS) is high, you can set this parameter to a greater value. | Twenty asynchronous concurrencies are provided by default. Each concurrency can provide 0.5 MB/s to 1 MB/s network throughput. The number of concurrencies varies with the network delay. |
| streamlog open _ | Specifies whether to receive syslogs. Data type: Boolean. | The value false indicates that syslogs are not received. The value true indicates that syslogs are received. |
| streamlog pool size in m _ _ _ _ b | The size of memory pool that the syslog server uses to cache syslogs. Unit: MB. | Logtail requests memory when it starts. Set the memory pool size based on the server memory size and your business requirements. |
| streamlog rcv size each c _ _ _ _ all | The size of the buffer that Logtail uses when the linux socket rcv API is called. Unit: bytes. Valid values: 1024 to 8192. | You can set a greater value if the syslog traffic is high. |
| streamlog formats _ | The method that is used to parse received syslogs. | N/A |
| streamlog tcp addr _ _ | The associated address that Logtail uses to receive syslogs. Default value: 0.0.0.0. | N/A |
| streamlog tcp port _ _ | The TCP port that Logtail uses to receive syslogs. | Default value: 11111. |
| buffer file num _ _ | The maximum number of cached files. If a network exception occurs or the writing quota is exceeded, Logtail writes parsed logs to local files in the installation directory. After the network recovers or a new writing quota is available, Logtail retries to send the logs to Log Service. | Default value: 25. |
| buffer file size _ _ | The maximum number of bytes that can be contained in each cache file. The maximum disk space available for cache files is the value of buffer file num _ _ multiplied by the value of buffer file size. _ _ | Default value: 20971520 bytes (20 MB). |

| Parameter | Description | Example |
|---|---|---|
| buffer file path _ _ | The directory in which cached files are stored. If you modify this parameter, you must move the files (for example, logtail\buffer\file *) in the old _ _ _ cache directory to the new directory. Then, Logtail can read, send, and delete the cache files. | The default value is null, which indicates that the cached files are stored in the Logtail installation directory /usr/local/ilogtail. |
| bind interface _ | The name of the NIC associated with the local machine, for example, eth1. This parameter is valid only for Logtail that runs in Linux. | By default, the available NICs are automatically associated with the local machine. If you specify this parameter, Logtail will use the specified NIC to upload logs. |
| check point filename _ _ | The full path in which the checkpoint file is stored. This parameter is used to customize the path to store the checkpoint file of Logtail. | Default value: /tmp/logtailcheckpoint. We _ _ recommend that Docker users modify this path and mount the directory where the checkpoint file resides to the host. Otherwise, duplicate collection occurs due to checkpoint data loss when the container is released. For example, you can set check point filename to _ _ /data/logtail/check point.dat in Docker and _ add -v /data/docker1/logtail:/data/logtail to the Docker startup command. Then, the /data/docker1/logtail directory of the host is mounted to the /data/logtail directory of Docker. |

|   | /data/docker1/logtail:/data/logtail |
|---|---|

> Not e
> The preceding table lists only the common startup parameters. If the ilogtail_config.json file contains parameters that are not listed in the table, the default settings are used for these parameters.
> We recommend that you do not add unnecessary parameters to the ilogtail_config.json file.

Modify configurations
1. Configure the ilogtail_config.json file as needed.
Ensure that the modified configurations are in the valid JSON format.
2. Restart Logtail to apply the modified configurations.

```
/etc/init.d/ilogtaild stop /etc/init.d/ilogtaild start /etc/init.d/ilogtaild status
```

#### 3.1.3 Logtail machine group

##### 3.1.3.1 Overview

Log Service uses machine groups to manage the servers from which you want to collect logs by using Logtail. A machine group is a virtual group that contains multiple servers. If you want to use a Logtail configuration file to collect logs from multiple servers, you can add the servers to a machine group. Then, you can apply the Logtail configuration file to the machine group. To define a machine group, you can use one of the following methods: IP address: Add the IP addresses of all servers to a machine group. Each server can be identified by using its unique IP address. Custom ID: Use a custom ID to identify the machine group and use the same ID for servers in the machine group.

> Not e Windows and Linux servers cannot be added to the same machine group.

IP address-based machine groups You can add multiple servers to a machine group by adding their IP addresses to the machine group. Then, you can create a Logtail configuration file for all the servers at the same time. If you use ECS instances and have not associated them with hostnames or changed their network types, you can add their private IP addresses to the machine group. In other cases, you must add the server IP addresses obtained by Logtail to a machine group. The IP address of each server is recorded in the IP address field of the app_info.json file on the server.

> Not e The app_info.json file records the internal information of Logtail. This file includes the server IP addresses obtained by Logtail. If you modify the IP address field of the file, the IP addresses obtained by Logtail remain unchanged.

Logtail obtains a server IP address by using the following methods: If the IP address of a server is associated with the hostname in the /etc/hosts file of the server, Logtail obtains this IP address. If the IP address of a server is not associated with the hostname, Logtail obtains the IP address of the first network interface controller (NIC) on the server. For more information, see Create an IP address-based server group. Custom ID-based machine groups You can use custom IDs to dynamically define machine groups. An application system consists of multiple modules. You can scale out each module by adding multiple servers to the module. If you want to collect logs by module, you can create a machine group for each module. Therefore, you must specify a custom ID for each server in each module. For example, a website consists of an HTTP request processing module, a caching module, a logic processing module, and a storage module. The custom IDs of these modules can be http_module, cache_module, logic_module, and store_module. For more information, see Create a machine group based on a custom ID.

##### 3.1.3.2 Create a machine group based on a server IP address

This topic describes how to create a machine group based on a server IP address. You can create a machine group based on a server IP address that is obtained by using a Logtail configuration file. You can then use the same Logtail configuration file to collect logs from the machine group. Prerequisites A project is created. A Logstore is created in the project. One or more servers are available. The IP addresses of the servers are obtained. Logtail is installed on the servers. For more information, see Install Logtail in Linux or Install Logtail in Windows. The ID of your Apsara Stack tenant account is configured on the server. For more information, see Configure an account ID for a server.
1. Log on to the Log Service console.
2. In the Project s section, click the name of a project.
3. In the left-side navigation pane, click the Machine Groups icon.
4. In the pane that appears, click the
icon next to Machine Group and select Creat e Machine Group from the shortcut menu. You can also create a machine group in the Logtail configuration wizard.
5. Create a machine group.
i. Enter a machine group name in the name field. The machine group name must be 3 to 128 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores (_). It must start and end with a lowercase letter or digit.

> Not ice After the machine group is created, its name cannot be modified.

ii. Select IP Addresses from the Ident if ier drop-down list. iii. Enter a topic name in the T opic field. For more information about topics, see Generate a topic. iv. Enter the IP addresses of the servers in the IP Addresses text box.

> Not ice
> Separate each IP address with a line break.
> Do not add Windows servers and Linux servers to the same machine group.

6. Click OK.
Result You can view the created machine group in the Machine Groups pane.

##### 3.1.3.3 Create a machine group based on a custom ID

This topic describes how to create a machine group based on a custom ID. Context You can use a custom ID to identify a machine group in the following scenarios: Servers reside in multiple custom network environments such as virtual private clouds (VPCs). IP addresses of different servers may be the same. In this scenario, Log Service cannot distinguish between servers based on IP addresses. You want to implement automatic server discovery. To do this, you only need to set a custom ID of a new server to the custom ID of an existing machine group. Log Service automatically identifies the server and adds it to the machine group.
1. Set a custom ID on a server.
Linux Logt ail Set a custom ID in the `/etc/ilogtail/user_defined_id` file. For example, if you need to set a custom ID of a server to `userdefined` , run the following command to open the file:

```bash
# vim /etc/ilogtail/user_defined_id
```

In the file, enter `userdefined` . Windows Logt ail Set a custom ID in the C:\LogtailData\user_defined_id file. For example, if you need to set a custom ID of a server, run the following command:

```
C:\LogtailData>more user_defined_id userdefined_windows
```

> Not ice
> A machine group cannot include both Linux and Windows servers. Therefore, do not set a custom ID of a Linux server and a custom ID of a Windows server to the same value.
> You can set multiple custom IDs for a single server. Separate each custom ID with a line break.
> If the /etc/ilogtail/ or C:\LogtailData directory or the /etc/ilogtail/user_defined_id or C:\LogtailDa ta\user_defined_id file does not exist, create the directory or the file.

2. Create a machine group.
i. Log on to the Log Service console. ii. In the Project s section, click a project. iii. In the left-side navigation pane, click the Machine Groups icon. iv. Click the icon next to Machine Groups, and select Creat e Machine Group from the shortcut menu. v. Set the parameters of the machine group. name: Enter a machine group name. The machine group name must be 3 to 128 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores (_). It must start and end with a lowercase letter or digit.

> Not e After the machine group is created, its name cannot be modified.

Ident if ier: Select Cust om ID. T opic: Enter a topic name for the machine group. For more information, see Generate a topic. Cust om Ident if ier: Enter the custom ID that you set in Step 1. vi. Click OK.

> Not e If you need to add a server to the machine group, set a custom ID of the server to the custom ID of the machine group. The server is then listed in the Machine Group St at us section.

3. View the status of the machine group.
In the Machine Groups pane, click the name of the machine group. On the Machine Group Set t ings page, view the status of the machine group. You can view the IP address list of the servers in the machine group and their heartbeat status.

> Not e
> The Machine Group St at us section lists the IP addresses of the servers whose custom ID is the same as the custom ID that you set for the machine group.
> For example, the custom ID of a machine group is userdefined and the IP addresses in the Machine Group St at us section are 10.10.10.10, 10.10.10.11, and 10.10.10.12. This means that the custom ID userdefined is set for the three servers. If you need to add the server whose IP address is 10.10.10.13 to the machine group, set the custom ID userdefined for the server. Then, the IP address of the server is displayed in the Machine Group St at us section. Log Service collects logs from the server based on the Logtail configuration file of the machine group.

The heartbeat status indicates whether the connection between a server and Log Service is normal. For information about how to troubleshoot heartbeat errors, see What can I do if no heartbeat packet is received from a Logtail client? Delete the custom IDs of a server If you need to change the ID of a server from a custom ID to the server IP address, delete the user_defined_id file. The change takes effect within 1 minute. In Linux, run the following command to delete the file:

```
rm -f /etc/ilogtail/user_defined_id
```

In Windows, run the following command to delete the file:

```
del C:\LogtailData\user_defined_id
```

Time required for a change to take effect After you create, edit, or delete a user_defined_id file, the change takes effect within 1 minute. If you need the change to take immediate effect, restart Logtail. In Linux, run the following commands to restart Logtail:

```
/etc/init.d/ilogtaild stop /etc/init.d/ilogtaild start
```

In Windows, perform the following steps to restart Logtail: Open the Control Panel. In the window that appears, choose Cont rol Panel > Administ rat ive T ools > Services. Right-click Logt ailWorker, and select Rest art from the shortcut menu. Example An application consists of multiple modules. Each module runs on multiple servers. For example, a website consists of an HTTP request processor, a cache, a logic processor, and a storage. You may scale out each module by adding multiple servers. You need to collect logs from both the existing and new servers.
1. Set a custom ID for each server.
Install Logtail on the servers and set a custom ID for each server. In this example, you can use four custom IDs: http_module, cache_module, logic_module, and store_module. Each custom ID corresponds to a module.
2. Create a machine group for each module.
When you create a machine group for a module, enter the custom ID of the module in the Cust om Ident if ier field.
3. View the status of the machine group.
On the Machine Group Set t ings page of the machine group, you can view the status of the machine group in the Machine Group St at us section. You can view the list of servers in the machine group and their heartbeat status.
4. If you need to add a server whose IP address is 10.1.1.3 to the machine group whose custom ID is http_module,
set the custom ID http_module for the server. Then, you can view the server in the Machine Group St at us section.

##### 3.1.3.4 View server groups

This topic describes how to view the server groups of a project on the Server Groups page in the Log Service console.
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane of the page that appears, click the Server Groups icon to display the list of
server groups. You can view all server groups of the project.

##### 3.1.3.5 Modify a server group

This topic describes how to modify a server group in the Log Service console. After you create a server group, you can modify the parameters of the server group.
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane of the page that appears, click the Server Groups icon to display the list of
server groups.
4. Click the name of the server group to be modified. On the Server Group Set t ings page, click Modif y.

> Not e The name of the server group cannot be modified.

5. Modify the parameters of the server group, and then click Save.

##### 3.1.3.6 View the status of a server group

This topic describes how to view the status of a server group in the Log Service console. You can view the heartbeat information of Logtail to check whether Logtail is installed on the servers in a server group.
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane of the page that appears, click the Server Groups icon to display the list of
server groups.
4. Click the name of the server group. On the Server Group Set t ings page, check the server group status.
If the heartbeat is OK, Logtail is installed on the servers in the server group and Logtail is connected to Log Service. If the heartbeat status is FAIL, Logtail fails to connect to Log Service. If the FAIL state persists, perform troubleshooting based on the instructions provided in What can I do if no heartbeat packet is received from a Logtail client?

##### 3.1.3.7 Delete a server group

This topic describes how to delete a server group in the Log Service console. You can delete a server group if you no longer need to collect logs from the server group.
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane of the page that appears, click the Server Groups icon to display the list of
server groups.
4. Find the server group that you want to delete, click the
icon next to the server group, and then select Delet e.
5. In the dialog box that appears, click OK.

##### 3.1.3.8 Manage server group configurations

This topic describes how to manage server group configurations in the Log Service console. Log Service uses server groups to manage the servers from which you collect logs by using Logtail. In the Log Service console, you can create, view, modify, and delete server groups. You can also view the status of server groups, manage server group configurations, and apply server group identifiers. Context Log Service allows you to manage the Logtail configurations that you create for Logtail installed on the servers in a server group. You can apply Logtail configurations to a server group. The Logtail configurations determine what logs are collected on each server, how the logs are parsed, and which Logstore the logs are written to.
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane of the page that appears, click the Server Groups icon to display the list of
server groups.
4. Click the name of the server group whose configurations you want to modify. On the Server Group Set t ings
page, click Modif y.
5. In the Conf igurat ions section, modify the Logtail configuration that you want to apply to the server group
and click Save. After a Logtail configuration is added, it is delivered to Logtail on each server in the server group. After a Logtail configuration is removed, it is removed from Logtail.

##### 3.1.3.9 Manage a Logtail configuration

This topic describes how to manage a Logtail configuration in the Log Service console. Before you can collect logs from a server, you must install Logtail on the server. After you install Logtail, you must create a Logtail configuration in the Log Service console and apply the Logtail configuration to the server. You can create and modify Logtail configurations in Logstores. Create a Logtail configuration For information about how to create a Logtail configuration in the Log Service console, see Configure text log collection. View Logtail configurations
1. Log on to the Log Service console.
2. Find the target project in the project list and click the project name.
3. In the left-side navigation pane, click the closing angle bracket (>) next to the target Logstore and choose
Dat a Import > Logt ail Conf igurat ions. Each item under Logt ail Conf igurat ions indicates a Logtail configuration. Modify a Logtail configuration Under Logt ail Conf igurat ions, click the name of the Logtail configuration. On the Logt ail Conf ig page, click Modif y. You can also change the log collection mode of the Logtail configuration, and then apply the Logtail configuration to the server group again. The process of modifying a Logtail configuration is the same as the process of creating a Logtail configuration. Delete a Logtail configuration Click the icon next to the Logtail configuration, and then select Delet e. After the Logtail configuration is deleted, it is disassociated from the server group. Logtail no longer collects logs specified by the Logtail configuration.

##### 3.1.3.10 Configure an account ID on a server

This topic describes how to configure the ID of an Apsara Stack tenant account on a server. Prerequisites Logtail is installed on the server. For more information, see Install Logtail in Linux or Install Logtail in Windows. Context You must configure the ID if the server is an on-premises server or an ECS instance that belong to another Apsara Stack tenant account. You must also configure the ID if the server is a cloud server that is provided by a third-party vendor. Then, the Apsara Stack tenant account can use Logtail to collect logs from the server. If you do not configure the account ID on the server, Log Service cannot receive the heartbeat of the server and Logtail cannot collect logs from the server.
1. View the ID of your Apsara Stack tenant account.
i. Log on to the Apsara Uni-manager Management Console. For more information, see Log on to the Log Service console. ii. In the top navigation bar, click Ent erprise. iii. In the left-side navigation pane, click Organizat ions. iv. Select the destination account and click Obt ain an accesskey v. In the AccessKey dialog box, view the account ID.
2. Log on to the server and configure the account ID on the server.
Linux server: In the /etc/ilogtail/users directory, create a file. Set the name of the file to the account ID. If the directory does not exist, create the directory first. You can configure multiple account IDs for a server. Examples:

```
touch /etc/ilogtail/users/1************** touch /etc/ilogtail/users/1**************
```

If you no longer need to collect logs from the server to a Log Service project, run the following command to delete the account ID:

```
rm /etc/ilogtail/users/1**************
```

Windows server: In the C:\LogtailData\users directory, create a file. Set the name of the file to the account ID. To delete the account ID, delete the file. For example, you can delete the file of an account ID from the C:\LogtailData\users\1************** directory.

> Not e
> After you configure the ID of an Apsara Stack tenant account on a server, the account is authorized to use Logtail to collect logs from the server. If an account is no longer used to collect logs from the server, delete the account ID file from the server at the earliest opportunity.
> After you configure or delete an account ID, the change takes effect within 1 minute.

#### 3.1.4 Text logs

##### 3.1.4.1 Configure text log collection

This topic describes how to configure Logtail in the Log Service console to collect text logs from specified servers. Prerequisites Logtail is installed. Logtail can be installed on a Windows or Linux operating system. For more information, see Install Logtail in Linux and Install Logtail in Windows. Each log file can be collected by using only one Logtail configuration. If you want to collect a log file by using more than one Logtail configuration, we recommend that you use symbolic links. For example, to collect a log file by using two Logtail configurations in the `/home/log/nginx/log` directory, you can use the original log path for one Logtail configuration. Then, run the `ln -s /home/log/nginx/log /home/log/nginx/link_log` command to create a symbolic link for this directory and use the symbolic link as the log path for the other Logtail configuration. Logtail supports only Windows or Linux operating systems. For more information, see Logtail overview. Logtail configuration procedure You can specify Logtail configurations in the Log Service console. Logtail supports various collection modes, such as simple mode, NGINX configuration mode, Apache configuration mode, IIS configuration mode, delimiter mode, JSON mode, and full regex mode. Configuration procedure Collection modes Logtail supports various collection modes, such as simple mode, NGINX configuration mode, Apache configuration mode, IIS configuration mode, delimiter mode, JSON mode, and full regex mode. Simple mode Logtail can be used to collect logs in the simple mode. For more information, see Collect logs by line. Full regex mode Logtail can be used to collect logs in the full regex mode. For more information, see Use regular expressions to collect logs. Delimiter mode Logtail can be used to collect logs in the delimiter mode. For more information, see Collect DSV formatted logs. JSON mode Logtail can be used to collect logs in the JSON mode. For more information, see Collect JSON logs. NGINX configuration mode Logtail can be used to collect logs in the NGINX configuration mode. For more information, see Collect NGINX logs. IIS configuration mode Logtail can be used to collect logs in the IIS configuration mode. For more information, see Collect IIS logs. Apache configuration mode Logtail can be used to collect logs in the Apache configuration mode. For more information, see Collect logs in Apache mode.
1. Log on to the Log Service console.
2. Select a data source.
You can use one of the following three methods to select a data source: On the homepage of the Log Service console, select a data source in the Import Dat a section. In the Project s section, click a project name. On the Overview page, click Import Dat a. On the Logstores tab in the left-side navigation pane, find a Logstore and click the closing angle bracket (>) in front of the Logstore name. Then, click the plus sign (+) next to Dat a Import . Select a data source based on your business requirements. Log Service supports the following log sources of text logs: RegEx-T ext Log, Single Row-T ext Log, Mult i-Row-T ext Log, Delimit er Mode-T ext Log, JSON-T ext Log, Nginx-T ext Log, IIS-T ext Log, and Apache-T ext Log.
3. Select a Logstore, and then click Next.
Select an existing project and Logstore. You can also click Creat e Now to create a project and Logstore. For more information, see Manage a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a server group.
Before you create a server group, ensure that Logtail is installed. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a server group. For more information, see Overview. If you have created a server group, click Use Exist ing Server Groups to select the server group.
5. Configure the server group, and then click Next.
Select a server group and move the group from Source Server Groups to Applied Server Groups.
6. Specify Logtail parameters.
Logtail parameters vary based on collection modes. For more information, see the relevant parameters for specific collection modes.
7. (Optional)Specify Advanced Opt ions and click Next .
Specify Advanced Opt ions based on your business requirements. We recommend that you do not modify the default settings unless otherwise required.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. |
| Upload Raw Log | Specifies whether to upload raw logs. If you turn on this switch, raw logs are written to the raw field and uploaded with the parsed logs. __ __ |
| Topic Generation Mode | Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic is set to an empty string and you can query logs without the need to enter a topic. Server Group T opic At t ribut es: This mode is used to differentiate log data that is generated by different frontend servers. File Pat h RegEx: If you select this mode, you must enter a value in the Cust om RegEx field to extract part of the path as the topic. This mode is used to differentiate log data that is generated by users or instances. |

| Parameter | Description |
|---|---|
| Custom RegEx | Specifies a custom regular expression. If you select File Pat h RegEx for T opic Generat ion Mode, you must enter a custom regular expression. |
| Log File Encoding | utf8: indicates UTF-8 encoding. gbk: indicates GBK encoding. |
| Timezone | Specifies the time zone where logs are collected. System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: Select a time zone. |
| Timeout | If a log file is not updated within a specific period of time, Logtail considers the file to be timed out. Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet a condition: Set the condition to Key:level Regex:WARNI NG\|ERROR . It indicates that only logs with the severity level of WARNING or ERROR are collected. Filter logs that do not meet a condition: Set the condition to Key:level Regex:^(?!. *(INFO\|DEBUG)). * . It indicates that logs with the severity level of INFO or DEBUG are not collected. Set the condition to Key:url Regex:. *^(?!.*(healthcheck)). * . It indicates that logs whose URL contains the keyword healthcheck are not collected. For example, logs in which the key is url and the value is /inner/hea lthcheck/jiankong.html are not collected. |

| Key:level Regex:WARNI |   |
|---|---|

|   | NG\|ERROR |
|---|---|

|   | lthcheck/jiankong.html |
|---|---|

8. Configure an index.
Configure an index based on your business requirements. For more information, see Enable the index feature and configure indexes for a Logstore. After you complete the settings, you can start to collect logs.

##### 3.1.4.2 Collect logs by line

This topic describes how to collect logs by line and configure indexes. You can specify the required settings in the Log Service console. Context To collect logs by line, you must select the simple mode. The simple mode can be divided into two types: Singleline mode In this mode, each line of log data is considered as a log. Two logs in a log file are separated by a line break. Logtail does not extract log fields in this mode. The default regular expression is `(. *)` . Logtail records the system time of the current server as the timestamp of a log. You can modify or manage advanced Logtail settings after you have completed the configuration procedure. For more information, see Manage a Logtail configuration. Multi-line mode In the multi-line mode, a regular expression is used to match the first line of a log. The settings in the multi-line mode are similar to the settings in the full regex mode. For more information, see Use regular expressions to collect logs.
1. Log on to the Log Service console.
2. Select a data source.
Select Single Row-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |   |   |
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. |   |   |
| Mode | If you have specified Single Row-T ext Log for the data source, the default mode is Simple Mode. You can change the mode. |   |   |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory that is specified in the log path is monitored. |   |   |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |

| Parameter | Description |
|---|---|
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect logs by line.

##### 3.1.4.3 Use regular expressions to collect logs

This topic describes how to collect logs by using regular expressions and configure indexes. You can specify the required settings in the Log Service console. Context If you need to collect multi-line logs and extract fields from logs, we recommend that you use regular expressions. Log Service can generate a regular expression based on a sample log that you enter in the Import Dat a wizard. However, you must modify the expression to match fields in the sample log as expected. For more information, see How do I test a regular expression?.
1. Log on to the Log Service console.
2. Select a data source.
Select RegEx-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |
|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |

| Parameter | Description |   |   |
|---|---|---|---|
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. |   |   |
| Mode | If you have specified RegEx-T ext Log for the data source, the default mode is Full Regex Mode. You can change the mode. |   |   |
| Singleline | The singleline mode is enabled by default. In this mode, logs are separated by line. To collect multi-line logs, such as Java program logs, you must disable the Singleline mode and configure Regex t o Mat ch First Line. |   |   |
| Log Sample | Enter a sample log that is retrieved from the data source. Then, Log Service generates a regular expression. |   |   |
| Regex to Match First Line | You can click Aut o Generat e or Manual. After you enter a sample log entry and click Aut o Generat e, the system generates a regular expression. If no regular expression is generated, you can switch to the manual mode and enter a regular expression for verification. |   |   |
| Extract Field | To analyze and process specific fields in logs, you can turn on the Ext ract Field switch. Then, the specified fields are converted to key-value pairs and sent to Log Service. You must specify a regular expression to parse the log content. |   |   |

| Parameter | Description |
|---|---|
| RegEx | If you turn on the Extract Field switch, you must specify this setting. Automatically generate a regular expression You can select the fields to be extracted from the sample log and then click Generate Regular Expression. The system generates a regular expression. Enter a regular expression You can also enter a regular expression. Click Manually to switch to the manual mode. After you enter a regular expression, click Validat e to check whether the regular expression can parse the log content. For more information, see How do I test a regular expression?. |
| Extracted Content | If you turn on the Ext ract Field switch, you must specify this setting. After a regular expression is automatically generated or manually specified, you must specify the key name for each extracted field. |
| Use System Time | If you turn on the Ext ract Field switch, you must specify this setting. If you turn off the Use Syst em T ime switch, you must specify a field as the time field and name this field time . After you specify the time field, click Aut o Generat e in the T ime Conversion Format field to automatically parse the time. For more information, see Configure the time format. |
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory specified in the log path is monitored. |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |

| Guide·Data collection | Log Servic |
|---|---|

| Parameter | Description |
|---|---|
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to use regular expressions to collect logs.

##### 3.1.4.4 Collect DSV formatted logs

This topic describes how to collect delimiter-separated values (DSV) formatted logs and configure indexes. You can specify the required settings in the Log Service console. Context DSV formatted logs use line feeds as boundaries. Each line is a log entry. The fields of each log entry are separated with a fixed delimiter. The characters that can be used as delimiters include the tab (\t), space, vertical bar (|), comma (,), and semicolon (;). A field that contains a delimiter must be enclosed in double quotation marks (""), which are used as quotes. Log formats Common DSV formatted logs include comma-separated values (CSV) and tab-separated values (TSV) formatted logs. A delimiter can contain a single charact er or mult iple charact ers. Single-character delimiter You can specify a single-character delimiter and a quote in the console. Delimit er: The fields of each log entry are separated with a single-character delimiter, such as the tab ( \t ), vertical bar ( | ), space, comma ( `,` ), and semicolon ( ; ). You can also specify a non-printable character as the delimiter.

> Not e A double quotation mark ( `"` ) cannot be used as a delimiter.

If a double quotation mark (") is included in a log entry but not used as a quote, it must be escaped and processed as double quotation marks ( `""` ). When Log Service parse logs, it restores double quotation marks ( `""` ) into a double quotation mark ( `"` ). You can use a double quotation mark ( `"` ) on each boundary of a field as a quote. You can also use a double quotation mark (escaped as `""` ) in the content of a field. If the use of a double quotation mark (") does not comply with the defined format, you can use the simple mode or full regex mode to parse fields. For example, assume that you use commas (,) as delimiters and include double quotation marks (“”) and

| the field with quotes and escape the double quotation marks into |   |   |   |   | "" | . |
|---|---|---|---|---|---|---|
| 1999,Chevy,"Venture ""Extended Edition, Very Large""","",5000.00 |   |   |   |   |   |   |
| s: | 1999 , | Chevy | , | Venture "Extended Edition, Very Large" | , empt |   |

```
 5000.00 .
```

Quot e: If a log field contains delimiters, you must specify a quote to enclose the field. Otherwise, the field cannot be parsed as expected. Log Service parses the content enclosed in quotes as one field. Only delimiters can exist between fields. You can use one of the following characters as the quote: tab ( \t ), vertical bar ( | ), space, comma ( `,` ), semicolon ( ; ), and non-printable characters. For example, a log is `1997,Ford,E350,"ac, abs, moon",3000.00` . In this example, the comma ( `,` ) is used as the delimiter and the double quotation mark (") is used as the quote. The log entry can be parsed into five fields: `1997` , `Ford` , `E350` , `ac, abs, moon` , and `3000.00` . Among the five fields, `ac, abs, moon` enclosed in quotes is regarded as one field.

> Not e Log Service allows you to use a non-printable character as a delimiter or quote. Non-printable characters are characters whose decimal ASCII codes are within the range of 1 to 31 and 127. If you use a non- printable character as a delimiter or quote, you must find the hexadecimal ASCII code of this character and enter the character in the following format: `0x`the hexadecimal ASCII code of the non-printable character. For example, to use the non-printable character whose decimal ASCII code is 1 and hexadecimal ASCII code is 01, you must enter `0x01` .

Multi-character delimiter Each mult i-charact er delimit er can contain two or three characters, such as || , `&&&` , and ^_^ . If you specify a multi-character delimiter, Log Service parses logs only based on the delimiter. You do not need to use quotes to enclose log fields.

> Not e You must ensure that log fields do not contain the delimiter. Otherwise, Log Service cannot parse these fields as expected.

| to | && | , the lo |
|---|---|---|
| ac&abs&moon |   |   |

| 1997&&Ford&&E350&&ac&abs&moon&&3000.00 |   |   |
|---|---|---|
| nd | 3000.00 | . |

fields: `1997` , `Ford` , `E350` , `ac&abs&moon` , and `3000.00` . Sample logs Single-charact er delimit er

```
05/May/2016:13:30:28,10.10. *. *,"POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=***********
*****&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=**********************
********** HTTP/1.1",200,18204,aliyun-sdk-java
05/May/2016:13:31:23,10.10. *. *,"POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=***********
*****&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=**********************
********** HTTP/1.1",401,23472,aliyun-sdk-java
```

Mult i-charact er delimit er

```
05/May/2016:13:30:28&&10.200. **. **&&POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=*******
*********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd
6x7hAgQ7b1c%3D HTTP/1.1&&200&&18204&&aliyun-sdk-java 05/May/2016:13:31:23&&10.200. **. **&&POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=*******
*********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************
************** HTTP/1.1&&401&&23472&&aliyun-sdk-java
```

1. Log on to the Log Service console.
2. Select a data source.
Select Delimit er-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration file.
The following table lists the Logtail parameters.

| Parameter | Description |
|---|---|
| Config Name | The name must be 3 to 128 characters in length, and can contain only lowercase letters, digits, hyphens (-), and underscores ( ). The name must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |

| Parameter | Description |
|---|---|
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration file. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |
| Docker File | If you collect logs from Docker containers, you can configure the paths and tags of the containers. Logtail monitors the containers when they are created and destroyed, filters the logs of the containers by tag, and collects the filtered logs. |
| Mode | If you have specified Delimit er-T ext Log for the data source, the default mode is Delimit er Mode. You can change the mode. |
| Log Sample | Enter a sample log entry that is retrieved from a log source in an actual scenario. Then, Log Service extracts a regular expression from the log entry. |
| Delimiter | Select a delimiter. Select a delimiter based on the log format. Otherwise, logs may fail to be parsed. Not e If you use a non-printable character as a delimiter, you must find the hexadecimal ASCII code of this character and enter the character in the following format: 0xthe hexadecimal ASCII code of th e non-printable character . For example, to use the non-printable character whose decimal ASCII code is 1 and hexadecimal ASCII code is 01, you must enter 0x01 . |

| ap |   |
|---|---|

| 0xthe hexadecimal ASCII code of th |   |
|---|---|

| Parameter | Description |
|---|---|
| Quote | Select a quote. Select a quote based on the log format. Otherwise, logs may fail to be parsed. Not e If you use a non-printable character as a quote, you must find the hexadecimal ASCII code of this character and enter the character in the following format: 0xthe hexadecimal ASCII code of th e non-printable character . For example, to use the non-printable character whose decimal ASCII code is 1 and hexadecimal ASCII code is 01, you must enter 0x01 . |
| Extracted Content | After you enter a sample log and select a delimiter, Log Service extracts log fields based on the delimiter and defines the fields as values. You must specify a key for each value. |
| Incomplete Entry Upload | This feature specifies whether to upload a log entry whose number of parsed fields is less than the number of the specified keys. If you turn on this switch, the log entry is uploaded. Otherwise, the log entry is dropped. For example, if you set the delimiter to the vertical bar ( \| ), the log entry 11\|22\|33\|44\|55 can be parsed into the following fields: 11 , 22 , 33 , 44 , and 55 . You can set the keys to A , B , C , D , and E . If you turn on the Incomplet e Ent ry Upload switch, the 55 field is uploaded as the value of the D key when Log Service collects the log entry 11\|22\|33\|55 . If you turn off the Incomplet e Ent ry Upload switch, Log Service drops the log entry because the fields and keys do not match. |
| Use System Time | If you turn on the Extract Field switch, you must specify this setting. If you turn off the Use System Time switch, you must specify a field as the time field and name this field time . After you specify the time field, click Aut o Generat e in the T ime Conversion Format field to automatically parse the time. For more information, see Configure the time format. |
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory that is specified in the log path is monitored. |

| 0xthe hexadecimal ASCII code of th |   |
|---|---|

| 11\|22\|33\|44\|55 |   |   |
|---|---|---|
| 33 | , | 44 |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |

| Parameter | Description |
|---|---|
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect DSV formatted logs.

##### 3.1.4.5 Collect JSON logs

This topic describes how to use Logtail to collect JSON logs and configure indexes. You can specify the required settings in the Log Service console. Context Logtail can parse JSON objects from logs. It extracts the keys and values from the first layer of an object as the names and values of log fields. The valid data types of field values include object, array, and primitive data types such as string or number. JSON logs can be written in the following two types of structures: Object: a collection of key-value pairs. Array: an ordered list of values. Lines of JSON logs are separated with \n . Each line is extracted as a single log. Logtail can parse only JSON logs of the object type. If you want to parse JSON logs of other types, such as JSON arrays, you must use regular expressions to extract the fields or specify the simple mode to collect logs by line. Sample log A sample JSON log is as follows:

```json
{"url": "POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun% 202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10. 200.98.220", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "18204"}, "time" : "05/May/2016:13:30:28"} {"url": "POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun% 202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10. 200.98.210", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "10204"}, "time" : "05/May/2016:13:30:29"}
```

1. Log on to the Log Service console.
2. Select a data source.
Select JSON-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |   |   |
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. |   |   |
| Mode | If you have specified JSON-T ext Log for the data source, the default mode is JSON Mode. You can change the mode. |   |   |
| Use System Time | If you turn on the Extract Field switch, you must specify this parameter. If you turn off the Use System Time switch, you must specify a field as the time field and name this field time . After you specify the time field, click Aut o Generat e in the T ime Conversion Format field to automatically parse the time. For more information, see Configure the time format. |   |   |

| Parameter | Description |
|---|---|
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory specified in the log path is monitored. |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |

| Parameter | Description |
|---|---|
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect JSON logs.

##### 3.1.4.6 Collect NGINX logs

This topic describes how to collect NGINX logs and configure indexes. You can connect Log Service to NGINX and specify the required settings in the Log Service console. Context The NGINX log format and path are specified in the /etc/nginx/nginx.conf configuration file. NGINX log format In the configuration file, the format of NGINX logs is defined as follows:

```
log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                 '$request_time $request_length '
                 '$status $body_bytes_sent "$http_referer" '
                 '"$http_user_agent"';
```

The path of the log file is declared as follows. The "main" portion that follows the path indicates that logs are written in the preceding format.

```
access_log /var/logs/nginx/access.log main
```

Sample log A sample NGINX log is as follows:

```
192.168.1.2 - - [10/Jul/2015:15:51:09 +0800] "GET /ubuntu.iso HTTP/1.0" 0.000 129 404 168 "-" "Wget/1. 11.4 Red Hat modified"
```

NGINX log fields

| Field | Description |
|---|---|
| remote addr _ | The IP address of the client. |
| remote user _ | The username of the client. |
| request | The URL and HTTP protocol of the request. |
| status | The status of the request. |
| body bytes sent _ _ | The number of bytes in the response that is returned to the client, excluding the size of the response header. |
| connection | The serial number of a connection. |
| connection requests _ | The number of requests that are received from a connection. |
| msec | The time when the log is written. The time is measured in seconds, accurate to milliseconds. |
| pipe | Indicates whether the request is pipelined. If the request is pipelined, the field value is p . Otherwise, the field value is . . |
| http referer _ | The URL of the web page linked to the resource that is being requested. |
| “http user agent” _ _ | The browser information of the client. The information must be enclosed by double quotation marks (""). |
| request length _ | The length of the request. The length includes the request line, request header, and request body. |
| request time _ | The time period for which the request is processed. The time period is measured in seconds, accurate to milliseconds. The time period starts when the first byte is read from the client and ends when the log is written after the last byte is sent to the client. |
| [$time local] _ | The local time in the Common Log Format. The time must be enclosed by brackets []. |

1. Log on to the Log Service console.
2. Select a data source.
Select Nginx-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |
|---|---|

| Parameter | Description |   |   |
|---|---|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |   |   |
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is adopted in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. |   |   |
| Mode | If you have specified Nginx-T ext Log for the data source, the default mode is NGINX Conf igurat ion Mode. You can change the mode. |   |   |
| NGINX Log Configuration | Enter the log configuration section that is specified in a standard NGINX configuration file. The section starts with log format . _ |   |   |
| NGINX Key | Log Service reads the keys of NGINX logs. |   |   |
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |   |   |

| Parameter | Description |
|---|---|
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory specified in the log path is monitored. |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |

| Parameter | Description |
|---|---|
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect NGINX logs.

##### 3.1.4.7 Collect IIS logs

This topic describes how to collect Internet Information Services (IIS) logs and configure indexes. You can specify the required settings in the Log Service console. Context To meet log analysis requirements, we recommend that you use the W3C Extended Log File Format. To use this format, click Select Fields in the IIS Manager, and then select sc-bytes and cs-bytes in the Standard Fields list. Log format The W3C Extended Log File Format is as follows:

```
logExtFileFlags="Date, Time, ClientIP, UserName, SiteName, ComputerName, ServerIP, Method, UriStem, Ur iQuery, HttpStatus, Win32Status, BytesSent, BytesRecv, TimeTaken, ServerPort, UserAgent, Cookie, Refer er, ProtocolVersion, Host, HttpSubStatus"
```

Field prefixes

| Prefix | Description |
|---|---|
| s- | The server action. |
| c- | The client action. |
| cs- | The client-to-server action. |
| sc- | The server-to-client action. |

Fields

| Field | Description |
|---|---|
| date | The date on which the client sends the request. |
| time | The time when the client sends the request. |
| s-sitename | The Internet service name and instance number of the site visited by the client. |
| s-computername | The name of the server on which the log is generated. |
| s-ip | The IP address of the server on which the log is generated. |
| cs-method | The HTTP request method that is used by the client, for example, GET or POST. |
| cs-uri-stem | The URI resource requested by the client. |
| cs-uri-query | The query string that follows the question mark (?) in the HTTP request. |
| s-port | The port number of the server to which the client is connected. |
| cs-username | The username used by the client to access the server. Authenticated users are referenced as domain\username . Anonymous users are indicated by a hyphen (-). |
| c-ip | The IP address of the client that sends the request. |
| cs-version | The protocol version that is used by the client, for example, HTTP 1.0 or HTTP 1.1. |
| user-agent | The browser that is used by the client. |
| Cookie | The content of the sent or received cookie. A hyphen (-) is used if no cookie is sent or received. |
| referer | The site that the client last visited. This site provides a link to the current site. |
| cs-host | The header name of the host. |
| sc-status | The HTTP or FTP status code that is returned by the server. |
| sc-substatus | The HTTP substatus code that is returned by the server. |
| sc-win32-status | The Windows status code that is returned by the server. |

| er Guide·Data collection | Log Servic |
|---|---|

| Field | Description |
|---|---|
| sc-bytes | The number of bytes that are sent by the server. |
| cs-bytes | The number of bytes that are received by the server. |
| time-taken | The processing time of the request. Unit: milliseconds. |

1. Log on to the Log Service console.
2. Select a data source.
Select IIS-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |   |   |
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. For more information, see Collect container text logs. |   |   |
| Mode | If you have specified IIS-T ext Log for the data source, the default mode is IIS Conf igurat ion Mode. You can change the mode. |   |   |
| Log Format | Select the log format of your IIS server logs. Valid values: IIS: Microsoft IIS log file format NCSA: NCSA Common log file format W3C: W3C Extended Log File Format |   |   |

| Parameter | Description |
|---|---|
| IIS Configuration | Enter the log configuration section that is specified in an IIS configuration file. If you select IIS or NCSA, the fields of the IIS log format are preconfigured. If you select W3C, enter the content that is specified for the logFile logExtFileFlags in the configuration file. For more information, see Specify the IIS Configuration field. |
| IIS Key Name | Log Service reads the keys of IIS logs. |
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory that is specified in the log path is monitored. |

7. Specify the IIS Configuration field.
i. Open the IIS configuration file. Default path of the IIS5 configuration file: C:\WINNT\system32\inetsrv\MetaBase.bin Default path of the IIS6 configuration file: C:\WINDOWS\system32\inetsrv\MetaBase.xml Default path of the IIS7 configuration file: C:\Windows\System32\inetsrv\config\applicationHost.confi g ii. Find the `logFile logExtFileFlags` field and copy the text in the quotation marks that follow the field name. iii. Paste the text into the quotation marks ("") in the IIS Conf igurat ion field.
8. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |

| ervice | User Guide·Data collectio |
|---|---|

| Parameter | Description |
|---|---|
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

9. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect IIS logs.

##### 3.1.4.8 Collect Apache logs

This topic describes how to collect Apache logs and configure indexes. You can specify the required settings in the Log Service console. Log formats The Apache configuration file defines two log formats: combined log format and common log format. You can also customize a log format. Syntax of the combined log format:

```
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
```

Syntax of the common log format:

```
LogFormat "%h %l %u %t \"%r\" %>s %b"
```

Syntax of a custom log format:

```
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %D %f %k %p %q %R %T %I %O" customized
```

You must specify the log format, log file directory, and log file name in the Apache configuration file. For example, the following declaration in the configuration file indicates that the combined log format is used. The log file directory is /var/log/apache2/access_log and the log file name is access_log.

```
CustomLog "/var/log/apache2/access_log" combined
```

Apache log fields

| Format string | Key name | Description |
|---|---|---|
| %a | client addr _ | The IP address of the client in the request. |
| %A | local addr _ | The local private IP address. |
| %b | response size bytes _ _ | The size of the response. Unit: bytes. If no bytes are sent, the value is “-”. |
| %B | response bytes _ | The size of the response. Unit: bytes. If no bytes are sent, the value is 0. |
| %D | request time msec _ _ | The time period for which the request is processed. Unit: milliseconds. |
| %h | remote addr _ | The name of the remote host. |
| %H | request protocol supple _ _ | The request protocol. |

| L | og Service |   | User Guide·Data collectio | n |
|---|---|---|---|---|

| Format string | Key name | Description |
|---|---|---|
| %l | remote ident _ | The identity information that is provided by a remote computer. |
| %m | request method supple _ _ | The request method. |
| %p | remote port _ | The port number of the server. |
| %P | child process _ | The ID of the child process. |
| %q | request query _ | The query string. If it does not exist, the value is an empty string. |
| “%r” | request | The request, which includes the method name, address, and HTTP protocol. |
| %s | status | The HTTP status code for the response. |
| %>s | status | The HTTP status code for the final response. |
| %f | filename | The name of the requested file. |
| %k | keep alive _ | The number of keep-alive requests. |
| %R | response handler _ | The type of the handler that generates the response on the server. |
| %t | time local _ | The local time when the server receives the request. |
| %T | request time sec _ _ | The time period for which the request is processed. Unit: seconds. |
| %u | remote user _ | The username that you used to log on to the client. |
| %U | request uri supple _ _ | The requested URL, excluding query strings. |
| %v | server name _ | The name of the server. |
| %V | server name canonical _ _ | The server name based on the UseCanonicalName setting. |
| %I | bytes received _ | The number of bytes that are received by the server. To use this field, you must enable the mod logio module. _ |
| %O | bytes sent _ | The number of bytes that are sent by the server. To use this field, you must enable the mod logio _ module. |
| “%{User-Agent}i” | http user agent _ _ | The information about the client. |
| “%{Rererer}i” | http referer _ | The URL of the web page linked to the resource that is being requested. |

Sample log

```
192.168.1.2 - - [02/Feb/2016:17:44:13 +0800] "GET /favicon.ico HTTP/1.1" 404 209 "http://localhost/x1. html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/4 8.0.2564.97 Safari/537.36"
```

1. Log on to the Log Service console.
2. Select a data source.
Select Apache-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
The following table lists the Logtail parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| Config Name | The configuration name must be 3 to 128 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. Not e The configuration name cannot be modified after it is created. |   |   |
| Log Path | The directory and name of the log file. The specified log file name can be a complete file name or a file name that contains wildcards. Recursive directory matching is used in the log file search. If this matching method is applied, all files that match the specified file name in the specified directory and its sub-directories are monitored. Example 1: /apsara/nuwa/ … /*.log indicates the files whose extension is .log in the /apsara/nuwa directory and its sub- directories are monitored. Example 2: /var/logs/app * … /*.log* indicates the files whose _ file name contains .log in the following directories are monitored: the sub-directories of the /var/logs directory that match the ap p * format and the sub-directories of these matching sub- _ directories. Not e Each log file can be collected by using only one Logtail configuration. Only the asterisk ( * ) and question mark ( ? ) can be used as wildcards in the log path. |   |   |
|   |   | ap |   |
| Docker File | If the log file to be collected is in a Docker container, you can configure the internal path and container tag. Logtail monitors the creation and destruction of the container, filters logs of the container based on the tag, and collects the filtered logs. For more information, see Collect container text logs. |   |   |
| Mode | If you have specified Apache-T ext Log for the data source, the default mode is Apache Conf igurat ion Mode. You can change the mode. |   |   |
| Log Format | Select a log format based on the format declared in your Apache log configuration file. To facilitate the query and analysis of log data, we recommend that you use a custom Apache log format. |   |   |

| Parameter | Description |
|---|---|
| APACHE Logformat Configuration | Enter the log configuration section that is specified in the Apache configuration file. The section starts with LogFormat. Not e If the specified Log Format is Common or Combined, the system enters a commonly used syntax of the log format. Check whether the log format is the same as that defined in the Apache configuration file. |
| APACHE Key Name | Log Service reads the keys of Apache logs. Confirm the key names on the Logtail configuration page. |
| Drop Failed to Parse Logs | Specifies whether to upload logs to Log Service if the logs fail to be parsed. If you turn on this switch, logs that fail to be parsed are not uploaded to Log Service. If you turn off this switch, raw logs are uploaded to Log Service when logs fail to be parsed. |
| Maximum Directory Monitoring Depth | The maximum number of directory layers that can be recursively monitored when logs are collected from the data source. Valid values: 0 to 1000. The value 0 indicates that only the directory specified in the log path is monitored. |

7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |

| Parameter | Description |
|---|---|
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After you complete the settings, you can start to collect Apache logs.

##### 3.1.4.9 Configure parsing scripts

This topic describes how to configure log contents for log collection. Specify a method to separate log lines A complete access log such as an NGINX access log occupies a line. Separate multiple log entries with line breaks. For example, the following shows two access logs:

```
10.1.1.1 - - [13/Mar/2016:10:00:10 +0800] "GET / HTTP/1.1" 0.011 180 404 570 "-" "Mozilla/4.0 (compati ble; MSIE 6.0; Windows NT 5.1; 360se)" 10.1.1.1 - - [13/Mar/2016:10:00:11 +0800] "GET / HTTP/1.1" 0.011 180 404 570 "-" "Mozilla/4.0 (compati ble; MSIE 6.0; Windows NT 5.1; 360se)"
```

For Java applications, a log entry usually spans several lines. Therefore, log entries are separated based on the identifier at the beginning of each log entry. The following example shows a Java application log.

```
[2016-03-18T14:16:16,000] [INFO] [SessionTracker] [SessionTrackerImpl.java:148] Expiring sessions 0x152436b9a12aecf, 50000 0x152436b9a12aed2, 50000 0x152436b9a12aed1, 50000 0x152436b9a12aed0, 50000
```

The preceding Java application log entries each start with a time field. The regular expression that matches these time fields is [\d+-\d+-\w+:\d+:\d+,\d+]\s. .* . You can enter information in the Log Service console as shown in the following figure. Full regular expression mode Extract log fields To conform to the data models of Log Service, a log contains one or more key-value pairs. If you want to extract specific fields for analysis, you must set a regular expression. If you do not want to process the contents of a log, you can treat the log as a key-value pair. You can determine whether to extract fields from the preceding NGINX access log. Extract fields

| (\S+)\s-\s-\s\[(\S+)\s[^]]+]\s"(\w+). * |   |   |
|---|---|---|
|   | GET | . |

`13/Mar/2016:10:00` , and `GET` . Extract all

| (. *) | . The extracted field is |
|---|---|

```
HTTP/1.1" 0.011 180 404 570 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; 360se)" .
```

Specify a log time To conform to the data models of Log Service, a log must have a time field in the Unix timestamp format. You can use the system time when Logtail collects a log or the time in the log contents as the log time. For the preceding NGINX access log: If you extract the time field from the log contents as the log time, the time is `13/Mar/2016:10:00:10` and the time expression is %d/%b/%Y:%H:%M:%S . If you use the system time when the log was collected as the log time, the log time is converted into a timestamp.

##### 3.1.4.10 Configure the time format

Each log in Log Service must have a timestamp that records the log generation time. When you collect logs from log files, Logtail must extract the timestamp string of each log and parse it into a timestamp. Therefore, you need to specify a timestamp format to facilitate parsing. In Linux, Logtail supports all time formats provided by the strftime() function. If a timestamp string can match one of the time formats that are provided by the strftime() function, Logtail can parse and use the timestamp string.

> Not e

The log timestamp is accurate to seconds. Therefore, you need to specify seconds in a time format, without the need for other information such as milliseconds or microseconds. In addition, you need to configure the time field rather than other information. Common log time formats supported by Logtail The timestamp strings of logs have diverse formats. To make configuration easier, the following table lists the common log time formats supported by Logtail:

| Format | Description | Example |
|---|---|---|
| %a | The abbreviation of a day in a week. | Fri |
| %A | The day in a week. | Friday |
| %b | The abbreviation of a month. | Jan |
| %B | The month name. | January |
| %d | The numerical day in a month. Valid values: 01 to 31. | 07 and 31 |
| %h | The abbreviation of a month. The format is equivalent to %b . | Jan |
| %H | The hour in the 24-hour format. | 22 |
| %I | The hour in the 12-hour format. | 11 |
| %m | The numerical month. | 08 |
| %M | The numerical minute. Valid values: 00 to 59. | 59 |

|   | User Guide·Data collection |   | Log Servic | e |
|---|---|---|---|---|

| Format | Description | Example |
|---|---|---|
| %n | A line break. | Line break |
| %p | The local time in the a.m. or p.m. format. | AM and PM |
| %r | The time in the 12-hour format. The format is equivalent to %I:%M:%S %p . | 11:59:59 AM |
| %R | The time includes hours and minutes. The format %R is equivalent to %H:%M . | 23:59 |
| %S | The numerical second. Valid values: 00 to 59. | 59 |
| %t | A tab. | Tab |
| %y | The two-digit numerical year. Valid values: 00 to 99. | 04 and 98 |
| %Y | The four-digit numerical year. | 2004 and 1998 |
| %C | The numerical century. Valid values: 00 to 99. | 16 |
| %e | The numerical day in a month. Valid values: 1 to 31. A single digit is preceded by a space. | 7 and 31 |
| %j | The numerical day in a year. Valid values: 001 to 366. | 365 |
| %u | The numerical day in a week. Valid values: 1 to 7, in which 1 represents Monday. | 2 |
| %U | The numerical week in a year. Sunday is the first day of a week. Valid values: 00 to 53. | 23 |
| %V | The numerical week in a year. Monday is the first day of a week. If a week has four or more days that start from January 1, the week is treated as the first week. Otherwise, the next week is treated as the first week. Valid values: 01 to 53. | 24 |
| %w | The numerical day in a week. Valid values: 0 to 6, in which 0 represents Sunday. | 5 |
| %W | The numerical week in a year. Monday is the first day of a week. Valid values: 00 to 53. | 23 |

|   | %p |
|---|---|

| Format | Description | Example |
|---|---|---|
| %c | The standard date and time. | To specify more information such as the long date and short date, you can use the preceding formats to provide exact expression. |
| %x | The standard date. | To specify more information such as the long date and short date, you can use the preceding formats to provide exact time expressions. |
| %X | The standard time. | To specify more information such as the long date and short date, you can use the preceding formats to provide exact expression. |
| %s | The Unix timestamp. | 1476187251 |

Example The following table lists the common log time formats, examples, and corresponding time expressions.

| Log time format | Example | Time expression |
|---|---|---|
| Custom | 2017-12-11 15:05:07 | %Y-%m-%d %H:%M:%S |
| Custom | [2017-12-11 15:05:07.012] | [%Y-%m-%d %H:%M:%S] |
| RFC822 | 02 Jan 06 15:04 MST | %d %b %y %H:%M |
| RFC822Z | 02 Jan 06 15:04 -0700 | %d %b %y %H:%M |
| RFC850 | Monday, 02-Jan-06 15:04:05 MST | %A, %d-%b-%y %H:%M:%S |
| RFC1123 | Mon, 02 Jan 2006 15:04:05 MST | %A, %d-%b-%y %H:%M:%S |
| RFC3339 | 2006-01-02T15:04:05Z07:00 | %Y-%m-%dT%H:%M:%S |
| RFC3339Nano | 2006-01-02T15:04:05.999999999Z07:00 | %Y-%m-%dT%H:%M:%S |

##### 3.1.4.11 Import historical logs

Logtail collects incremental logs by default. If you want to import historical logs, use the historical log importing feature of Logtail. Prerequisites To collect logs from Linux servers, use Logtail 0.16.15 or later. To collect logs from Windows servers, use Logtail 1.0.0.1 or later. To ensure successful log collection, update Logtail to the latest version. Context Logtail collects log files based on events. The system captures events by detecting or polling files for changes at intervals. Additionally, Logtail can load events from local files to trigger log collection. Logtail implements historical log collection based on these local events. You can import historical log files from the Logtail installation directory. The location of the directory varies based on the operating system. Linux: /usr/local/ilogtail Windows: 32-bit: C:\Program Files\Alibaba\Logtail 64-bit: C:\Program Files (x86)\Alibaba\Logtail

> Not e
> The maximum interval between the time a local event is generated and the time the local event is imported is one minute.
> Loading local configurations is a special action. Therefore, Logtail sends the `LOAD_LOCAL_EVENT_ALARM` alert to your server to notify you of this action.
> If you want to import a large number of log files, we recommend that you modify the Logtail startup configuration to increase the upper limit of CPU to 2.0 GHz or more and the upper limit of the memory size to 512 MB or more. For more information, see Set Logtail startup parameters.

1. Configure log collection.
If a collection configuration is only used to import historical log files, you can specify a collection directory that does not exist. For more information, see Configure text log collection.
2. Obtain a unique identifier for a collection configuration.
Obtain the unique identifier in the user_log_config.json file stored in the installation directory of Logtail. In Linux, use the grep command in the directory to query the unique identifier. In Windows, use tools such as Notepad to query the unique identifier. To query a unique identifier in a Linux operating system, run the following command:

```
grep "##" /usr/local/ilogtail/user_log_config.json | awk '{print $1}'
                    "##1.0##log-config-test$multi"
                    "##1.0##log-config-test$ecs-test"
                    "##1.0##log-config-test$metric_system_test"
                    "##1.0##log-config-test$redis-status"
```

3. Add local events.
Local events are stored in the local_event.json file that resides in the installation directory of Logtail. The file is in the JSON format. The syntax is: `[` `{`

```json
    "config" : "${your_config_unique_id}",
    "dir" : "${your_log_dir}",
    "name" : "${your_log_file_name}"
```

`},` `{`

```
   ...
```

`}`

```
   ...
```

`]` Parameters

| Parameter | Description | Example |
|---|---|---|
| config | The unique identifier that is obtained in Step 2. | ##1.0##log-config-test$ecs-test |

| Log Se | rvice |   | User Guide·Data collectio | n |
|---|---|---|---|---|

| Parameter | Description | Example |   |   |
|---|---|---|---|---|
| dir | The directory where logs are stored. Not e The directory cannot end with a slash ( / ). | /data/logs |   |   |
| name | The name of a log file. Wildcards are supported. | For example, access.log.2018- 08-08 and access.log* |   |   |
|   |   |   | access.log.2018- |   |
|   |   |   | access.log* |   |

|   | 08-08 |
|---|---|

> Not e To prevent Logtail from loading invalid JSON files, save local event configurations to a temporary file, edit the configurations in the temporary file, and copy the contents to the local_event.js on file.

Configuration examples In a Windows system, you can use tools such as Notepad to add local events to the local_event.json file. In a Linux system, add local events as follows:

```bash
$ cat /usr/local/ilogtail/local_event.json
```

`[` `{`

```json
    "config": "##1.0##log-config-test$ecs-test",
    "dir": "/data/log/",
    "name": "access.log.
```

`},` `{`

```json
    "config": "##1.0##log-config-test$ecs-test",
    "dir": "/tmp",
    "name": "access.log.2017-08-09"
```

`}` `]` What's next Check whether Logtail has loaded configurations

| local event.json _ |   | file, Logtail loads t |
|---|---|---|
| he contents of the | local event.json _ |   |

To check whether Logtail has read local events, use the following methods: If the contents of the `local_event.json` file are cleared, it indicates that Logtail has read the local events. Check whether the ilogtail.LOG file in the Logtail installation directory contains the `process local event` keywords. If the contents of the `local_event.json` are cleared and these keywords cannot be found, the local configuration file may be screened due to invalid contents. Check whether the configuration is loaded but no data is collected Possible causes are as follows: The configuration is invalid. The local `config` file does not exist. The log file does not exist in the path specified in the collection configuration. The log file has been collected by Logtail.

##### 3.1.4.12 Generate a topic

This topic describes how to generate a topic in the Log Service console. After you generate a topic, you can use the topic to group logs. You can specify topics for logs when these logs are written. You can use a topic as a filter when you query logs. Topic generation modes You can set a topic when you use Logtail to collect logs or when you use API operations or SDKs to upload logs. The following topic generation modes are available in the Log Service console: Null - Do not generat e t opic, Server Group T opic At t ribut es, and File Pat h RegEx. Null - Do not generat e t opic When you configure Logtail in the Log Service console to collect text logs, the default topic generation mode is Null - Do not generat e t opic. In this mode, no topic is generated and query logs without specifying a topic. Server Group T opic At t ribut es You can use this mode to identify logs that are generated from multiple servers. Logs from multiple servers can be stored in the same file or directory. To identify these logs based on topics during log collection, you can create server groups and add the servers into different groups. When you create server groups, you must specify a unique t opic at t ribut e for each server group and set T opic Generat ion Mode to Server Group T opic At t ribut es. After you complete the configuration, apply the Logtail settings to the server groups. If the Server Group T opic At t ribut es mode is selected, Logtail uploads the topic attribute of each server group as topics to Log Service. When you query logs, you must specify the topic of the target server group as a filter. File Pat h RegEx You can use this mode to differentiate between logs that are generated by multiple users or instances. If Log Service stores logs in different directories for different users or instances, duplicate sub-directory names or log file names may exist in these directories. As a result, Log Service cannot identify the source of logs. You can select File Pat h RegEx in the T opic Generat ion Mode field. Enter a regular expression that matches an absolute file path, and set an instance name as a topic. If you select File Pat h RegEx, Logtail uses an instance name as the topic of the logs that Logtail uploads to Log Service. The topic generated varies based on your directory structure and configuration. You must specify an instance name as a topic when you query logs. For example, the following directory structure includes directories that each store logs generated by different users or instances:

```
/logs
  | - /userA/serviceA
    | - service.log
  | - /userB/serviceA
    | - service.log
  | - /userC/serviceA
    | - service.log
```

If you want to extract multiple separate fields from a file path, use a multi-layer extraction method of ?P<k

| ey> |   | . The value of the key can contain lowercase letters and digits. For example: |
|---|---|---|
|   | /home/admin/serviceA/userB/access.log \/home\/admin\/(? P<service>[^\/]+)/(? P<user>[^/]+)/. * |   |

The following custom tags are created for logs:

```
"__tag__ : service : serviceA" "__tag__ : user : userB"
```

> Not e Logtail 0.16.19 and later are supported.

If you specify the /logs file path and the service.log file name in a regular expression, Logtail collects logs from the preceding directories that contain the service.log file and uploads the logs to Log Service. However, Log Service cannot identify the log source based on log contents. You can select File Pat h RegEx in the T opic Generat ion Mode field, and enter the \/(.*)\/serviceA\/.* regular expression to extract instance names. After the configuration is complete, the following topics are generated for logs in different directories: userA, userB, and userC. You can specify a topic as a filter to query logs.

> Not e You must escape the forward slashes ( `/` ) in the file path that the regular expression contains.

St at ic t opic generat ion You can select File Pat h RegEx in the T opic Generat ion Mode field, and enter cust omized:// + cust om t opic in the `Custom RegEx` field.

> Not e Logtail 0.16.21 and later are supported.

Set a log topic
1. Configure Logtail in the Log Service console. For more information, see Configure text log collection.
To set the topic generation mode to Server Group T opic At t ribut es, go to the T opic section on the server group creation or modification page.
2. In the Logtail Configuration for Data Import step, click Advanced Opt ions and select a t opic generat ion
mode.

#### 3.1.5 Custom plug-ins

Context Log Service allows you to collect text logs and system logs through Logtail. Logtail supports connections with multiple data sources, such as HTTP or MySQL query results and MySQL binary logs. You can collect HTTP request data and upload the processing results to Log Service in real time to check service availability check and continuous availability monitoring. You can configure MySQL query results as the data source, and then synchronize incremental data based on custom IDs or time. You can also configure an SQL data source to synchronize MySQL binary logs, subscribe to database changes, and query or analyze logs in real time.

> Not e This feature is only supported on Linux and must be used together with Logtail. 0.16.0 or later versions. For more information, see Install Logtail in Linux.

Configuration process
1. Configure a method that is used to collect logs from the data source.
Different Logtail configurations for different data sources. Select a Logtail configuration according to your data source.
2. Configure a processing method.
Logtail provides multiple processing methods for binary logs, MySQL query results, NGINX monitoring data, and HTTP input sources. You can configure multiple processing methods for a single input source. Each input source supports all processing methods. Logtail runs the configured processing methods in sequence. For more information, see Configure data processing methods.
3. Apply the configurations to the machine group.
After you configure the collection and processing methods, apply them to the specified machine group. Then, Logtail automatically applies the configurations and starts data collection.

##### 3.1.5.1 Collect MySQL binary logs

Logtail is used as a MySQL slave. It is used to collect binary logs from a MySQL master. Logtail collects binary logs by using a similar method to Alibaba Canal. This improves the efficiency of log collection. Features Allows you to collect incremental data of databases in the form of binary logs to improve performance. Supports MySQL databases such as ApsaraDB RDS for MySQL. Supports multiple database filters, such as regular expressions. Allows you to set binary log file positions. Allows you to record synchronization statuses by using the checkpoint mechanism. MySQL binary logs are available only for Logtail 0.16.0 or later versions that you install on Linux. For more information about how to update Logtail and view Logtail versions, see Install Logtail in Linux. Binary logs in the ROW format must be enabled for MySQL databases. By default, binary logs in the ROW format are enabled for RDS instances.

```bash
# Check whether binary logs are enabled.
mysql> show variables like "log_bin"; +---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+ 1 row in set (0.02 sec)
# View the format of binary logs.
mysql> show variables like "binlog_format"; +---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+ 1 row in set (0.03 sec)
```

Each server ID must be unique. Make sure that the ID of each slave to be synchronized is unique. Limits for RDS databases: Logtail cannot be installed on an RDS instance. You must install Logtail on an ECS instance that can communicate with the destination RDS instance. Secondary RDS databases cannot be used to collect binary logs. You must configure a primary RDS database to collect binary logs. Implementation Logtail enables communication between master and slave MySQL servers. The process of how master and slave MySQL servers communicate is provided in the following information:
1. Logtail is used as a MySQL slave. It can also be used to send dump requests to the MySQL master.
2. After the dump requests are received, the MySQL master delivers its binary logs to Logtail in real time.
3. Logtail parses and filters binary logs, and then uploads the results to Log Service.
Scenarios The MySQL binary logging feature applies to scenarios in which you need to synchronize large amounts of data and meet high performance requirements. Query the incremental data of databases in real time. Audit operations that are performed on databases. Use Log Service to query data, visualize query results, transform data for stream processing, export data to MaxCompute for offline computing, and export log to Object Storage Service (OSS) for long-term storage. Data reliability We recommend that you enable the global transaction identifier (GTID) feature of the MySQL server and upgrade Logtail to version 0.16.15 or later. This prevents repeated data collection during a primary/secondary server switchover and ensures data reliability. Incomplete data collection: If the network between Logtail and the MySQL server is disconnected for a long period of time, some data may not be collected. A MySQL binary log plug-in is used as a MySQL slave to collect binary logs from the master server. Logtail establishes a connection with the master server to obtain data from the server. If the network between Logtail and the master node is disconnected, the master node still generates new binary logs and deletes expired binary logs. After the connection is reestablished and Logtail is reconnected to the master server, Logtail uses the last checkpoint to request binary log data from the master server. However, if the network is disconnected for a long period of time, the data generated after the checkpoint may be deleted. In this case, the recovery mechanism specifies the new point at which Logtail resumes collecting binary logs. The new point is the most recent binary log file position. If the network is disconnected for a long period of time, some data generated between the checkpoint and the new data collection point may not be collected. Repeated data collection: If the ordinal numbers of binary logs on the master and slave servers are different and a master/slave switchover occurs, repeated data collection may occur. If the MySQL master-slave synchronization is configured, the master server synchronizes the generated binary log data to the slave server. Then, the slave server stores the received binary log data to the local binary log file. If the ordinal numbers of binary logs on the master and slave servers are different, a master/slave switchover occurs. In this case, the mechanism that uses a binary log file name and an offset as the checkpoint causes repeated data collection. For example, assume that a data entry ranges from `(binlog.100, 4)` to `(binlog.105, 4)` on the master server, and ranges from `(binlog.1000, 4)` to `(binlog.1005, 4)` on the slave. Logtail has obtained the data from the master server and updated the checkpoint to `(binlog.105, 4)` . In this case, if a master/slave switchover occurs without exception, Logtail continues to obtain binary logs from the new master server based on the local checkpoint `(binlog.105, 4)` . The new master server returns the data entries that range from `(b` `inlog.1000, 4)` to `(binlog.1005, 4)` to Logtail. This is because the ordinal numbers of these data entries on the new master server are greater than the ordinal numbers of data entries requested by Logtail. As a result, log data is repeatedly collected. Parameter The type of input sources is `service_canal` .

| Parameter | Type | Required | Description |
|---|---|---|---|
| Host | string | No | The IP address of the host where the database resides. Default value: 127.0.0.1. |
| Port | int | No | The port number that you can use to connect with the database. Default value: 3306. |
| User | string | No | The database username. Default value: root. The configured user must have the read permissions on the source database and the MySQL REPLICATION permission. Example: CREATE USER canal IDENTIFIED BY 'canal'; GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *. * TO 'canal'@'%'; -- GRANT ALL PRIVILEGES ON *. * TO 'canal'@'%' ; FLUSH PRIVILEGES; |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Password | string | No | The database password. By default, this parameter is unspecified. If you require a high level of data security, we recommend that you set both the username and the password to xxx. After your configurations are synchronized to the on-premises server, find the Password parameter in the /usr/local/ilogtail/userlogconfig.json _ _ file and modify the value. Not e After you modify the password, use the sudo /et c/init .d/ilogt aild st op; sudo /et c/init .d/ilogt aild st art command to restart Logtail. If you modify the value of the Password parameter on the web and synchronize your configurations to the on-premises server, the configurations on the on-premises server are overwritten. You can change the configurations on the on-premises server later. |
| ServerID | int | No | The ID of a MySQL slave whose role is assumed by Logtail. Default value: 125. Not e In a MySQL database, each ID must be unique. Otherwise, synchronization fails. |
| IncludeTables | String array | Yes | The names of matched tables. Each value contains a database name and a table name, for example, test db.test table . _ _ You must specify a regular expression for the parameter. Logtail does not collect incremental data from tables whose names do not match the regular expression. To collect incremental data from all tables of a database, set the value of the IncludeTables parameter to . *\\.. * . Not e If an exact match is required, make sure that the regular expression is prefixed by ^ . In this case, you must also make sure that the regular expression is suffixed by $ . Example: ^test db\\.test table$ . _ _ |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ExcludeTable s | String array | No | The names of excluded tables expressed as a regular expression. The name of a table must include the name of the database to which the table belongs, for example, test db.test table . If _ _ a table meets one of the conditions specified in the parameter, the table is not collected. If you do not specify this parameter, incremental data from all tables is collected. Not e If an exact match is required, make sure that the regular expression is prefixed by ^ . In this case, you must also make sure that the regular expression is suffixed by $ . Example: ^test db\\.test table$ . _ _ |
| StartBinName | string | No | The name of the first binary log file that is collected by Logtail. If you do not specify this parameter, Logtail starts to collect binary log files that are generated from the current time. To collect data from a specific location, view the name of the current binary log file and the file offset. Then, set StartBinName and StartBinLogPos to actual values. Example: # Set StartBinName to mysql-bin.000063 and StartBinLogPos to 0. mysql> show binary logs; +------------------+-----------+ \| Log name \| File size \| _ _ +------------------+-----------+ \| mysql-bin.000063 \| 241 \| \| mysql-bin.000064 \| 241 \| \| mysql-bin.000065 \| 241 \| \| mysql-bin.000066 \| 10778 \| +------------------+-----------+ 4 rows in set (0.02 sec) Not e If you set the StartBinName parameter, a large amount of traffic is generated during the first collection. |
| StartBinLogP os | int | No | The offset of the first binary log file that is collected. Default value: 0. |
| EnableGTID | bool | No | Specifies whether to add GTID. Default value: true. If the value is false, no GTID is added to uploaded data. |
| EnableInsert | bool | No | Specifies whether to collect log events triggered by INSERT operations. Default value: true. If the value is false, INSERT events are not collected. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| EnableUpdate | bool | No | Specifies whether to collect UPDATE events. Default value: true. If the value is false, UPDATE events are not collected. |
| EnableDelete | bool | No | Specifies whether to collect DELETE events. Default value: true. If the value is false, DELETE events are not collected. |
| EnableDDL | bool | No | Specifies whether to collect data definition language (DDL) events. Default value: false. If the value is false, DDL events are not collected. Not e This parameter does not support the IncludeTables or ExcludeTables filtering methods. |
| Charset | string | No | The encoding method. Default value: utf-8 . |
| TextToString | bool | No | Specifies whether to convert data of the text type into a string. Default value: false. |
| PackValues | bool | No | Specifies whether to encapsulate event data into the JSON format. Default value: false. If the value is false, event data is not encapsulated. If this feature is enabled, Logtail encapsulates event data into the data and old data fields in the JSON format. The _ old data field is available only for ROW UPDATE events. _ _ For example, assume that a table has three fields named c1, c2, and c3. If this feature is disabled, the ROW INSERT event data _ contains three fields c1, c2, and c3. If this feature is enabled, c1, c2, and c3 are encapsulated into one data field and the value is {"c1":"...", "c2": "...", "c3": "..."} . Not e This parameter is available only for Logtail V0.16.19 and later. |
| EnableEventM eta | bool | No | Specifies whether to collect event metadata. Default value: false. If the value is false, event metadata is not collected. The metadata of binary log events includes event time , _ event log position , event size , and _ _ _ event server id . _ _ Not e This parameter is available only for Logtail V0.16.21 and later. |

Synchronize data from tables whose names do not end with `_inner` in the `user_info` RDS database.
1. Log on to the Log Service console.
2. Select a data source.
Click Import Dat a. On the Import Dat a page, select MYSQL BinLog.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Configure the data source.
Set the Config Name and Plug-in Config fields. In the Plug-in Conf ig field, modify the parameter settings in the default configuration template based on your business requirements. `{`

```json
 "inputs": [
```

`{`

```json
         "type": "service_canal",
         "detail": {
             "Host": "************.mysql.rds.aliyuncs.com",
             "Port": 3306,
             "User" : "root",
             "ServerID" : 56321,
             "Password": "*******",
             "IncludeTables": [
                 "user_info\\.. *"
```

`],`

```json
             "ExcludeTables": [
                 ". *\\. \\S+_inner"
```

`],`

```json
             "TextToString" : true,
             "EnableDDL" : true
```

`}` `}` `]` `}` inputs: specifies the collection configurations. This parameter is required. You must configure statements to collect data based on your data source. processors: specifies the processing method. This parameter is optional. For more information about how to set a processing method, see Configure data processing methods.
7. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

8. (Optional)Modify the configurations on the server.
If you do not enter the actual URL, username, or password in Plug-in Conf ig, you must replace them with actual values after the configurations are synchronized to the server.

> Not e If you have entered the actual information, skip this step.

i. Log on to the server where Logtail is installed, find the `service_canal` keyword in the `/usr/local/ilo` `gtail/user_log_config.json` file, and then set related fields. These fields include `Host` , `User` , and

| gtail/user log config.json _ _ |   |   |
|---|---|---|
|   | Password | . |

ii. Run the following command to restart Logtail:

```python
sudo /etc/init.d/ilogtaild stop; sudo /etc/init.d/ilogtaild start
```

The configurations that are used to collect binary logs are completed. If changes are made to your database, Logtail immediately collects the updated data and uploads the data to Log Service.

> Not e Logtail collects incremental binary logs. If no data is collected, check whether changes are made to the table in your database after the configurations are updated.

Metadata fields When you collect binary logs, some metadata is also uploaded. The following table lists the fields of uploaded metadata.

| Parameter | Description |   | Example |   |   |
|---|---|---|---|---|---|
| host _ _ | The name of the host where the database resides. |   | *********.mysql.rds.aliy uncs.com |   |   |
| db _ _ | The name of the RDS database. |   | my-database |   |   |
| table _ _ | The name of the table. |   | my-table |   |   |
| event _ _ | The type of the event. Valid values: |   | row update , _ row insert , and _ row delete _ |   |   |
| id _ _ | The ID of the current collection. The value starts from 0 and increments by 1 each time a binary log event is collected. |   | 1 |   |   |
| gtid _ _ | The GTID. |   | 7d2ea78d-b631-11e7-8afb- 00163e0eef52:536 |   |   |
|   |   |   |   | 7d2ea78d-b631-11e7-8afb- |   |
|   |   |   | 00163e0eef52:536 |   |   |
| filename _ _ | The name of the binary log file. |   | binlog.001 |   |   |
| offset _ _ | The offset of the binary log file. The value is updated after each COMMIT operation. |   | 12876 |   |   |

|   |   | *********.mysql.rds.aliy |   |
|---|---|---|---|
|   | uncs.com |   |   |

Example After you completed the preceding steps to set a processing method, perform `INSERT` , `UPDATE` , and `DELETE` operations on the `SpecialAlarm` table in the `user_info` database. The following information shows the schema, database operations, and sample logs that are collected by Logtail. Schema

```
CREATE TABLE `SpecialAlarm` ( `id` int(11) unsigned NOT NULL AUTO_INCREMENT, `time` datetime NOT NULL, `alarmtype` varchar(64) NOT NULL, `ip` varchar(16) NOT NULL, `count` int(11) unsigned NOT NULL, PRIMARY KEY (`id`), KEY `time` (`time`) USING BTREE, KEY `alarmtype` (`alarmtype`) USING BTREE ) ENGINE=MyISAM AUTO_INCREMENT=1;
```

Database operations Perform the INSERT, DELETE, and UPDATE operations on the database.

```
insert into specialalarm (`time`, `alarmType`, `ip`, `count`) values(now(), "NO_ALARM", "10.10. **.
***", 55);
delete from specialalarm where id = 4829235 ; update specialalarm set ip = "10.11. ***.**" where id = "4829234";
```

Create an index for `zc.specialalarm` .

```
ALTER TABLE `zc`.`specialalarm` ADD INDEX `time_index` (`time` ASC);
```

Sample logs On the data preview or Search & Analysis page, you can view a sample log that corresponds to each operation. INSERT statement

```
__source__: 10.30. **.** __tag__:__hostname__: iZbp145dd9fccu***** __topic__: _db_: zc _event_: row_insert _gtid_: 7d2ea78d-b631-11e7-8afb-00163e0eef52:536 _host_: *********.mysql.rds.aliyuncs.com _id_: 113 _table_: specialalarm alarmtype: NO_ALARM count: 55 id: 4829235 ip: 10.10. ***.*** time: 2017-11-01 12:31:41
```

DELETE statement

```
__source__: 10.30. **.** __tag__:__hostname__: iZbp145dd9fccu**** __topic__: _db_: zc _event_: row_delete _gtid_: 7d2ea78d-b631-11e7-8afb-00163e0eef52:537 _host_: *********.mysql.rds.aliyuncs.com _id_: 114 _table_: specialalarm alarmtype: NO_ALARM count: 55 id: 4829235 ip: 10.10. **.*** time: 2017-11-01 12:31:41
```

UPDATE statement

```
__source__: 10.30. **.** __tag__:__hostname__: iZbp145dd9fccu**** __topic__: _db_: zc _event_: row_update _gtid_: 7d2ea78d-b631-11e7-8afb-00163e0eef52:538 _host_: *********.mysql.rds.aliyuncs.com _id_: 115 _old_alarmtype: NO_ALARM _old_count: 55 _old_id: 4829234 _old_ip: 10.10.22.133 _old_time: 2017-10-31 12:04:54 _table_: specialalarm alarmtype: NO_ALARM count: 55 id: 4829234 ip: 10.11. ***.*** time: 2017-10-31 12:04:54
```

DDL statement

```
__source__: 10.30. **.** __tag__:__hostname__: iZbp145dd9fccu**** __topic__: _db_: zc _event_: row_update _gtid_: 7d2ea78d-b631-11e7-8afb-00163e0eef52:539 _host_: *********.mysql.rds.aliyuncs.com ErrorCode: 0 ExecutionTime: 0 Query: ALTER TABLE `zc`.`specialalarm` ADD INDEX `time_index` (`time` ASC) StatusVars:
```

Usage notes We recommend that you increase resource limits on Logtail to process traffic surges and prevent data security risks. If the limits are exceeded, Logtail may be forcibly restarted. You can modify the resource limits in the /usr/local/ilogtail/ilogtail_config.json file. Then, you can run the sudo /et c/init .d/ilogt aild st op;sudo /et c/init .d/ilogt aild st art command to restart Logtail. The following example shows how to set the CPU limit to two and memory limit to 2,048 MB: `{`

```json
    ...
    "cpu_usage_limit":2,
    "mem_usage_limit":2048,
    ...
```

`}`

##### 3.1.5.2 Collect MySQL query results

This topic describes how to configure Logtail in the Log Service console to collect MySQL query results. Context If you want to collect data from a MySQL database, you can install Logtail on a server and connect the server with the database. Then, you can create a Logtail configuration file by executing a custom SQL statement in the Log Service console and deliver the configuration file to Logtail. Logtail can use the custom SQL statement to collect data from the database at regular intervals.

> Not e This feature applies only to Logtail 0.16.0 and later versions that run on Linux. For more information, see Install Logtail in Linux.

Benefits Supports MySQL databases such as ApsaraDB RDS for MySQL. When you collect data, you can perform the following operations: Paginate query results. Set time zones. Set timeout periods. Store checkpoints. Transmit data over the SSL protocol. Set the maximum size of data that can be collected at a time. Implementation Logtail executes the specified SELECT statement at a regular interval based on the Logtail configurations, and then uploads the query results to Log Service. When Logtail obtains a query result, Logtail saves the value of the CheckPoint field in the on-premises server. The next time Logtail executes the SELECT statement, Logtail adds the saved value of the CheckPoint field to the SELECT statement. This way, Logtail collects the incremental data of MySQL databases. Scenarios Collect incremental data based on specific marks such as an auto-increment ID or a point in time. Customize data synchronization based on specified filtering conditions. Parameters The following table describes Logtail parameters. The type of the data source is `service_mysql` .

| Parameter | Type | Required | Description |
|---|---|---|---|
| Address | string | No | The address of the MySQL database. Default value: 127.0.0.1:3306. |
| User | string | No | The username of the MySQL database. Default value: root. |

| User Guide·Data collection |   |   | Log Servic |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Password | string | No | The password of the MySQL database. By default, this parameter is unspecified. |
| DialTimeOutMs | int | No | The timeout period for the database connection. Unit: milliseconds. Default value: 5000. |
| ReadTimeOutMs | int | No | The timeout period for data reading. Unit: milliseconds. Default value: 5000. |
| StateMent | string | Yes | The SQL statement. |
| Limit | bool | No | Specifies whether to paginate query results by using the LIMIT clause. Default value: false. |
| PageSize | int | No | The number of log entries to return on each page. You must specify this parameter if you set the Limit parameter to true. |
| MaxSyncSize | int | No | The maximum number of log entries that are synchronized at a time. Default value: 0. This value indicates that no limit is set for the size of data that can be synchronized at a time. |
| CheckPoint | bool | No | Specifies whether to use checkpoints during data collection. Default value: false. |
| CheckPointColumn | string | No | The name of the checkpoint column. You must specify this parameter if you set the CheckPoint parameter to true. |
| CheckPointColumnType | string | No | The type of the checkpoint column. Valid values: int and time . |
| CheckPointStart | string | No | The initial value of the checkpoint. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| CheckPointSavePerPage | bool | No | If this parameter is set to true, a checkpoint is saved each time query results are paginated. If this parameter is set to false, a checkpoint is saved after each synchronization. |
| IntervalMs | int | Yes | The synchronization interval. Unit: milliseconds. |

We recommend that you paginate query results by specifying the `Limit` parameter. If you set the `Limit` parameter to true, the LIMIT clause is automatically appended to the SQL statement specified by the `StateMent` parameter when you run a query. If you set the `CheckPoint` parameter to true, the data that is selected based on the `StateMent` parameter must contain the checkpoint column. In addition, the WHERE clause must contain the checkpoint field. The value of the checkpoint field is a question mark ( ? ). For example, assume that the checkpoint is "id" and the value of the `StateMent` parameter is `SELECT * from`

```
... where id > ? .
```

| he | CheckPoint |
|---|---|
| CheckPointStart |   |
| of | CheckPointColumnType |

If you set the `CheckPoint` parameter to true, you must specify the `CheckPointColumn` , `CheckPointColumnT`

| int | or | time |   |
|---|---|---|---|
| set to | time |   | , My |

The value of `CheckPointColumnType` can only be set to `int` or `time` . If the value is set to `int` , the int64 data type is used for internal storage. If the value is set to `time` , MySQL DATE, DATETIME, and TIME are supported. The following procedure describes how to synchronize incremental data from a MySQL database to Log Service. In this procedure, the logtail.VersionOs field is synchronized every 10 seconds. The value of the count parameter in this field is greater than 0. The value of the initial checkpoint is 2017-09-25 11:00:00. Log entries are paginated and each page contains 100 log entries. The checkpoint of each page is saved.
1. Log on to the Log Service console.
2. Select a data source.
Click Import Dat a. On the Import Dat a page, select MYSQL Query Result -Plug-in.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Configure the data source.
In the Plug-in Conf ig field, modify the parameter settings in the default configuration template based on your business requirements. `inputs` : specifies the collection configurations. This parameter is required. `processors` : specifies the processing method. This parameter is optional. You must configure statements to collect data based on your data source. You can specify one or more processing methods. For more information, see Configure data processing methods.

> Not e If you require a high level of data security, we recommend that you set both the username and the password to xxx. After your configurations are synchronized to the on-premises server, find the Password parameter in the /usr/local/ilogtail/user_log_config.json file and modify the value.

The following example shows the configurations: `{`

```json
 "inputs": [
```

`{`

```json
         "type": "service_mysql",
         "detail": {
             "Address": "********:3306",
             "User": "logtail",
             "Password": "*******",
             "DataBase": "logtail",
             "Limit": true,
             "PageSize": 100,
             "StateMent": "SELECT * from logtail.VersionOs where time > ?",
             "CheckPoint": true,
             "CheckPointColumn": "time",
             "CheckPointStart": "2017-09-25 11:00:00",
             "CheckPointSavePerPage": true,
             "CheckPointColumnType": "time",
             "IntervalMs": 10000
```

`}` `}` `]` `}`
7. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

8. (Optional)Modify the configurations on the server.
If you do not enter the actual URL, username, or password in the Specif y Dat a Source page, you must replace them with actual values after the configurations are synchronized to the server.

> Not e If you have entered the actual information, skip this step.

i. Log on to the server where Logtail is installed, find the `service_mysql` keyword in the `/usr/local/ilo` `gtail/user_log_config.json` file, and then set related fields. These fields include: `Address` , `User` ,

| gtail/user log config.json _ _ |   |   |
|---|---|---|
| and | Password | . |

ii. Run the following command to restart Logtail:

```python
sudo /etc/init.d/ilogtaild stop; sudo /etc/init.d/ilogtaild start
```

Example After you configure the processing method, you can view the processed data in the Log Service console. The following information shows the schema and sample logs that are collected by Logtail. Schema

```
CREATE TABLE `VersionOs` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `time` datetime NOT NULL,
  `version` varchar(10) NOT NULL DEFAULT '',
  `os` varchar(10) NOT NULL,
  `count` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `timeindex` (`time`)
```

`)` Sample output

```json
"count": "4" "id: "721097" "os: "Windows" "time: "2017-08-25 13:00:00" "version": "1.3.0"
```

##### 3.1.5.3 Collect syslogs

This topic describes how to use the syslog plug-in of Logtail to collect syslogs from a server. Prerequisites Logtail 0.16.13 or a later version is installed on the server. On a Linux server, local syslogs can be forwarded to the IP address and port of a specified server by using syslog agents such as rsyslog. After you create a Logtail configuration for the specified server, the syslog plug-in of Logtail receives the syslogs over TCP or UDP. In addition, the syslog plug-in parses the received syslogs and extract log fields such as facility, tag (program), severity, and content based on the specified syslog protocol. The syslog protocol can be RFC 3164 or RFC 5424.

> Not e

Logtail installed on a Windows server does not support the syslog plug-in. You can configure multiple syslog plug-ins for Logtail. For example, you can use both TCP and UDP to listen on 127.0.0.1:9999. Implementation After the syslog plug-ins start to listen on a specified IP address and port, Logtail can act as a syslog server to collect syslogs from various data sources. These syslogs include system logs collected by rsyslog, access or error logs forwarded by NGINX, and logs forwarded by syslog clients in languages such as Java. Logtail parameters The following table describes Logtail parameters. The type of the input is `service_syslog` .

| Parameter | Type | Required | Description |   |   |
|---|---|---|---|---|---|
| Address | String | No | The protocol, address, and port on which the syslog plug- in listens. The syslog plug-in obtains logs based on the value of this parameter. Format: [tcp/udp]://[ip]: [port] . Default value: tcp://127.0.0.1:9999 . Not e The specified protocol, address, and port must be the same as those specified for the forwarding rule in the rsyslog configuration file. If the server on which Logtail is installed has multiple IP addresses, you can set the IP address to 0.0.0.0. It means that the syslog plug-in listens on all IP addresses of the server. |   |   |
|   |   |   |   | [tcp/udp]://[ip]: |   |
| ParseProtocol | String | No | The protocol that is used to parse logs. This parameter is not specified by default, indicating that logs are not parsed. Valid values: rfc3164: The RFC 3164 protocol is used to parse logs. rfc5424: The RFC 5424 protocol is used to parse logs. auto: The syslog plug-in selects a protocol based on the log content. |   |   |

|   | [port] |
|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| IgnoreParseFailur e | Boolean | No | Specifies whether to ignore a parsing failure. Default value: true. Valid values: true: Logs that fail to be parsed are included in the returned content field. false: Logs that fail to be parsed are dropped. |

Default fields

| Field | Type | Description |
|---|---|---|
| hostname _ _ | String | The hostname. If a hostname is not provided in the log, the hostname of the current host is obtained. |
| program _ _ | String | The tag field in the protocol. |
| priority _ _ | String | The priority field in the protocol. |
| facility _ _ | String | The facility field in the protocol. |
| severity _ _ | String | The severity field in the protocol. |
| unixtimestamp _ _ | String | The timestamp of the log. |
| content _ _ | String | The log content. If the log fails to be parsed, this field contains the complete content of the log. |
| ip _ _ | String | The IP address of the current host. |

Configure the plug-in of Logtail to collect syslogs
1. Add a forwarding rule for rsyslog.
Modify the /etc/rsyslog.conf rsyslog configuration file on the server from which syslogs are collected. Add a forwarding rule at the end of the configuration file. Then, rsyslog forwards syslogs to the specified IP address and port. If you want to collect syslogs of the server by using Logtail on this server, set the forwarding address to 127.0.0.1 and the port to an idle port. If you want to collect syslogs of the server by using Logtail on a second server (Server B), set the forwarding address to the public IP address of the second server and port to an idle port. For example, the following forwarding rule indicates that logs are forwarded to 127.0.0.1:9000 over TCP.

```
*. * @@127.0.0.1:9000
```

2. Run the following command to restart rsyslog and validate the log forwarding rule:

```python
sudo service rsyslog restart
```

3. Log on to the Log Service console.
4. Select the data source Cust om Dat a Plug-in.
You can use one of the following three methods to select a data source: On the homepage of the Log Service console, select a data source in the Import Dat a section. In the Project s section, click a project name. On the Overview page, click Import Dat a, and then select a data source. On the Logstores tab in the left-side navigation pane, find a Logstore and click the closing angle bracket (>) in front of the Logstore name. Click the plus sign (+) next to Dat a Import , and then select a data source.
5. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
6. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
7. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

8. Configure the data source.
Set Conf ig Name and Plug-in Conf ig. The `inputs` section is required. It specifies the collection configuration. The `processors` section is optional. It specifies the processing configuration. You must specify a collection statement for the collection configuration based on the data source. You can specify one or more processing methods for the processing configuration. For more information, see Configure data processing methods. The following sample code shows how to use UDP and TCP to listen on 127.0.0.1:9000: `{`

```json
     "inputs": [
```

`{`

```json
             "type": "service_syslog",
             "detail": {
                 "Address": "tcp://127.0.0.1:9000",
                 "ParseProtocol": "rfc3164"
```

`}` `},` `{`

```json
             "type": "service_syslog",
             "detail": {
                 "Address": "udp://127.0.0.1:9001",
                 "ParseProtocol": "rfc3164"
```

`}` `}` `]` `}`
9. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

Configure the plug-in of Logtail to collect NGINX logs NGINX access logs can be forwarded to specified addresses and ports over the syslog protocol. To deliver NGINX access logs as syslogs from a server to Log Service, you can create a Logtail configuration and apply it to the server group to which the server belongs.
1. Add a forwarding rule to the nginx.conf configuration file on the NGINX server.
For example, add the following content to the configuration file.

```bash
http {
    ...
    # Add this line.
    access_log syslog:server=127.0.0.1:9000,facility=local7,tag=nginx,severity=info combined;
    ...
```

`}`
2. Run the following command to restart the NGINX service and validate the configuration.

```python
sudo service nginx restart
```

3. Create a Logtail configuration and apply it to the server group to which the server belongs.
For more information, see Configure the plug-in of Logtail to collect syslogs.
4. Check whether the Logtail configuration takes effect.
Run the `curl http://127.0.0.1/test.html` command in shell to generate an access log. If the Logtail configuration takes effect, you can view the log information on the query page of the Log Service console.

##### 3.1.5.4 Configure data processing methods

Logtail allows you to configure plug-ins for data processing. Each plug-in defines a processing method. You can configure one or more processing methods for a data source. Then, Logtail executes the processing methods in sequence. This topic describes the available data processing methods and describes how to configure the methods. Implementation The following figure shows how collected data is processed. Implementation Plug-in elements When you configure the data processing methods, you must set the key parameter to `processors` and the value parameter to an array of JSON objects. Each object contains the details of a processing method. Each object contains the `type` and `detail` fields. The `type` field specifies the type of a processing method. The `detail` field contains configuration details.

```json
"processors" : [
```

`{`

```json
            "type" : "processor_anchor",
            "detail" : {
                ...
```

`}` `},` `{`

```json
            "type" : "processor_regex",
            "detail" : {
                ...
```

`}` `}` `]` Processing methods The following processing methods are supported: Extract log fields by using a regular expression Extract log fields by using start and stop keywords Extract log fields by using a single-character delimiter Extract log fields by using a multi-character delimiter Convert an IP address into a geographical location Filter log fields by using a regular expression Add log fields Remove log fileds Extract log time (Go) Expand log fields (JSON) Combine log fields (JSON) Rename fields Extract log time (Strptime) You can also create a custom method that includes several of the preceding methods. For more information, see Custom methods. Extract log fields by using a regular expression This method extracts the fields that match a specified regular expression. The type of the plug-in is `processor_regex` . Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field to extract by using the regular expression. |
| Regex | string | Yes | The regular expression. Enclose the value of fields to extract with parentheses () . |
| Keys | String array | Yes | The array of fields to extract, for example, ["key1", "key2" …]. |
| NoKeyError | bool | No | Specifies whether to report an error if no field matches the regular expression. Default value: false. |
| NoMatchError | bool | No | Specifies whether to report an error if the specified regular expression does not match logs. Default value: false. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: false. This value specifies that the SourceKey parameter is not returned. |
| FullMatch | bool | Yes | Specifies whether to extract fields that exactly match the Regex parameter. Default value: true. This value specifies that fields that partially match the Regex parameter are extracted. |

The following example shows how to extract fields from an access log. Input data

```json
"content" : "10.200. **. ** - - [10/Aug/2017:14:57:51 +0800] \"POST /PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A 30%20GMT&Topic=raw&Signature=<yourSignature> HTTP/1.1\" 0.024 18204 200 37 \"-\" \"aliyun-sdk-java"
```

Configurations `{`

```json
    "type" : "processor_regex",
    "detail" : {"SourceKey" : "content",
         "Regex" : "([\\d\\.] +) \\S+ \\S+ \\[(\\S+) \\S+\\] \"(\\w+) ([^\\\"]*)\" ([\\d\\.]+) (\\d
+) (\\d+) (\\d+|-) \"([^\\\"]*)\" \"([^\\\"]*)\" (\\d+)",
         "Keys"   : ["ip", "time", "method", "url", "request_time", "request_length", "status", "le
ngth", "ref_url", "browser"],
         "NoKeyError" : true,
         "NoMatchError" : true,
         "KeepSource" : false
```

`}` `}` Output data

```json
"ip" : "10.200. **.**" "time" : "10/Aug/2017:14:57:51" "method" : "POST" "url" : "/PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun% 202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=<yourSignature>" "request_time" : "0.024" "request_length" : "18204" "status" : "200" "length" : "27" "ref_url" : "-" "browser" : "aliyun-sdk-java"
```

Extract log fields by using start and stop keywords This method uses the `start` and `stop` keywords to extract fields. You can extract fields from the JSON string between the start and stop keywords. You can also expand the JSON string into other forms. The type of the plug-in is `processor_anchor` . Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field to extract. |
| Anchors | Array | Yes | The array of anchors. For more information, see the following table. |
| NoAnchorError | bool | No | Specifies whether to report an error if no specified keyword is found. Default value: false. |
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: false. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: false. This value specifies that the SourceKey parameter is not returned. |

Anchor fields

| Parameter | Type | Required | Description |
|---|---|---|---|
| Start | string | Yes | The start keyword. If you do not specify the parameter, Logtail matches the first character of a string. |
| Stop | string | Yes | The stop keyword. If you do not specify the parameter, Logtail matches the last character of a string. |
| FieldName | string | Yes | The name of the field to extract. |
| FieldType | string | Yes | The type of the field to extract. Valid values: string and json . |
| ExpondJson | bool | No | Specifies whether to expand JSON strings. Default value: false. This parameter is available only if you specify json for the FieldType parameter. |
| ExpondConnecter | string | No | The connector that combines separate field names into a string. Default value: . _ |
| MaxExpondDepth | int | No | The maximum depth of JSON expansion. Default value: 0 . This indicates no limit. |

The following example shows how to use this method to process input data of multiple types. Input data

```json
"content" : "time:2017.09.12 20:55:36\tjson:{\"key1\" : \"xx\", \"key2\": false, \"key3\":123.456, \"key4\" : { \"inner1\" : 1, \"inner2\" : false}}"
```

Configurations `{`

```json
   "type" : "processor_anchor",
   "detail" : {"SourceKey" : "content",
      "Anchors" : [
```

`{`

```json
              "Start" : "time",
              "Stop" : "\t",
              "FieldName" : "time",
              "FieldType" : "string",
              "ExpondJson" : false
```

`},` `{`

```json
              "Start" : "json:",
              "Stop" : "",
              "FieldName" : "val",
              "FieldType" : "json",
              "ExpondJson" : true
```

`}` `]` `}` `}` Output data

```json
"time" : "2017.09.12 20:55:36" "val_key1" : "xx" "val_key2" : "false" "val_key3" : "123.456" "value_key4_inner1" : "1" "value_key4_inner2" : "false"
```

Extract log fields by using a single-character delimiter This method uses `single-character delimiters` to split logs into several fields. You can enclose delimited fields by using characters that you specify in the Quote parameter. The type of the plug-in is `processor_split_char` . Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field to extract. |
| SplitSep | string | Yes | The single-character delimiter. You must specify a single character as a delimiter. You can specify a non-printable character such as \u0001 as a delimiter. |
| SplitKeys | String array | Yes | The names of the fields that are split, for example, ["key1", "key2"…]. |
| QuoteFlag | bool | No | Specifies whether to use the Quote parameter. Default value: false. |
| Quote | string | No | You must specify a single character. The parameter is available only if you specify true for the QuoteFlag parameter. You can specify non-printable characters, such as \u0001 . |
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: false. |
| NoMatchError | bool | No | Specifies whether to report an error if the specified delimiter is not found. Default value: false. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: false. This value specifies that the SourceKey parameter is not returned. |

The following example shows how to use this method to process logs. Input data

```json
"content" : "10. **. **. **|10/Aug/2017:14:57:51 +0800|POST|PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A 30%20GMT&Topic=raw&Signature=<yourSignature>|0.024|18204|200|37|-| aliyun-sdk-java"
```

Configurations `{`

```json
   "type" : "processor_split_char",
   "detail" : {"SourceKey" : "content",
      "SplitSep" : "|",
      "SplitKeys" : ["ip", "time", "method", "url", "request_time", "request_length", "status", "le
ngth", "ref_url", "browser"]
```

`}` `}` Output data

```json
"ip" : "10. **. **.**" "time" : "10/Aug/2017:14:57:51 +0800" "method" : "POST" "url" : "/PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun% 202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=<yourSignature>" "request_time" : "0.024" "request_length" : "18204" "status" : "200" "length" : "27" "ref_url" : "-" "browser" : "aliyun-sdk-java"
```

Extract log fields by using a multi-character delimiter Similar to the single-character delimiter method, this method uses multi-character delimiters to split logs into several fields. The Quote parameter is unavailable for this method. The type of the plug-in is `processor_split_string` . Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field to extract. |
| SplitSep | string | Yes | The multi-character delimiter. You can specify non-printable characters such as \u0001\u0002 . |
| SplitKeys | String array | Yes | The names of the fields that are split, for example, ["key1", "key2"…]. |
| PreserveOthers | bool | No | Specifies whether to retain excess fields when the number of split fields exceeds the number of fields defined in the SplitKeys parameter. Default value: false. |
| ExpandOthers | bool | No | Specifies whether to parse excess fields. Default value: false. |
| ExpandKeyPrefix | string | No | The prefix of the names of excess fields. For example, if you specify expand for the _ parameter, excess fields are named expand 1 and expand 2 . _ _ |
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: false. |

| og Service |   |   | User Guide·Data collectio |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| NoMatchError | bool | No | Specifies whether to report an error if no multi-character delimiter is found. Default value: false. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: false. The value false specifies that the SourceKey parameter is not returned. |

The following example shows how to use this method to process logs. Input data

```json
"content" : "10. **. **. **|#|10/Aug/2017:14:57:51 +0800|#|POST|#|PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A 30%20GMT&Topic=raw&Signature=<yourSignature>|#|0.024|#|18204|#|200|#|37|#|-|#| aliyun-sdk-java"
```

Configurations `{`

```json
   "type" : "processor_split_string",
   "detail" : {"SourceKey" : "content",
      "SplitSep" : "|#|",
      "SplitKeys" : ["ip", "time", "method", "url", "request_time", "request_length", "status"],
      "PreserveOthers" : true,
      "ExpandOthers" : true,
      "ExpandKeyPrefix" : "expand_"
```

`}` `}` Output data

```json
"ip" : "10. **. **.**" "time" : "10/Aug/2017:14:57:51 +0800" "method" : "POST" "url" : "/PutData? Category=YunOsAccountOpLog&AccessKeyId=<yourAccessKeyId>&Date=Fri%2C%2028%20Jun% 202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=<yourSignature>" "request_time" : "0.024" "request_length" : "18204" "status" : "200" "expand_1" : "27" "expand_2" : "-" "expand_3" : "aliyun-sdk-java"
```

Convert an IP address into a geographical location This method converts IP address into a geographical location, such as a country, province, city, or geographical coordinates.

> Not e By default, the Logtail installation package does not include GeoIP databases. You must download these databases to your local host and configure the required parameters. We recommend that you download a version of the GeoIP database that includes the `City` database.

The type of the plug-in is `processor_geoip` . Parameters

| Parameter | Type | Required |   | Description |   |
|---|---|---|---|---|---|
| SourceKey | string | Yes |   | The name of the field whose IP address you want to convert into a geographical location. |   |
| DBPath | string | Yes |   | The absolute path of the GeoIP database. The database format is MMDB , for example, /user/data/GeoLite2- |   |
|   |   |   |   |   | /user/data/GeoLite2- |
|   |   |   |   | City 20180102/GeoLite2-City.mmdb _ |   |
| NoKeyError | bool | No |   | Specifies whether to report an error if no match exists. Default value: false. |   |
| NoMatchError | bool | No |   | Specifies whether to report an error if the specified IP address is invalid or does not match the IP addresses stored in the library. Default value: false. |   |
| KeepSource | bool | No |   | Specifies whether to return the SourceKey parameter. Default value: true. |   |
| Language | string | No |   | The language of the GeoIP database. Default value: zh-CN . Make sure that your GeoIP database can be displayed in a language that is suitable for your business. |   |

The following example shows how to use this method to convert an IP address into a geographical location. Input data

```json
"source_ip" : "**. **. **. **"
```

Download a GeoIP database and install the database on the host where Logtail resides. We recommend that you download MaxMind GeoLite2 that includes the city database.

> Not e Make sure that the database format is MMDB.

Configurations `{`

```json
   "type": "processor_geoip",
    "detail": {
         "SourceKey": "ip",
         "NoKeyError": true,
         "NoMatchError": true,
         "KeepSource": true,
         "DBPath" : "/user/local/data/GeoLite2-City_20180102/GeoLite2-City.mmdb"
```

`}` `}` Output result

```json
"source_ip_city_" : "**. **. **.**" "source_ip_province_" : "Zhejiang" "source_ip_city_" : "Hangzhou" "source_ip_province_code_" : "ZJ" "source_ip_country_code_" : "CN" "source_ip_longitude_" : "120.********" "source_ip_latitude_" : "30. ********"
```

Filter log fields by using a regular expression This method uses regular expressions to filter logs. You can specify conditions in the `Include` and `Exclude` parameters. The type of the plug-in is `processor_filter_regex` . Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Include | The JSON object that includes key-value pairs. | No | Each key includes a log field. Each value includes a regular expression. If the field value matches the regular expression, the log is collected. |
| Exclude | The JSON object that includes key-value pairs. | No | Each key includes a log field. Each value includes a regular expression. If the field value matches the regular expression, the log is dropped. |

> Not e A log is collected only if the field value matches the regular expression specified in the `Include`
> parameter and does not match the regular expression specified in the `Exclude` parameter. Otherwise, the log is dropped.

The following example shows how to use this method to process logs. Input data Log 1

```json
"ip" : "10. **. **.**" "method" : "POST" ... "browser" : "aliyun-sdk-java"
```

Log 2

```json
"ip" : "10. **. **.**" "method" : "POST" ... "browser" : "chrome"
```

Log 3

```json
"ip" : "192.168. *.*" "method" : "POST" ... "browser" : "ali-sls-ilogtail"
```

Configurations `{`

```json
   "type" : "processor_filter_regex",
    "detail" : {
         "Include" : {
            "ip" : "10\\..*",
            "method" : "POST"
```

`},`

```json
         "Exclude" : {
            "browser" : "aliyun. *"
```

`}` `}` `}` Output data

| Log | Matched | Reason |   |   |
|---|---|---|---|---|
| Log 1 | No | The match failed because the value of the browser field matches the regular expression specified in the Exclude parameter. |   |   |
| Log 2 | Yes | - |   |   |
| Log 3 | No | The match failed because the value of the ip field does not match the regular expression specified in the Inclu de parameter. The regular expression matches IP addresses that start with 10 . |   |   |
|   |   |   | Inclu |   |
|   |   |   | IP |   |

|   | de |
|---|---|

Add log fields You can use this method to add multiple fields to a log. The type of the plug-in is `processor_add_fields` .

> Not e This method is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Fields | map | No | The JSON object that includes key-value pairs. You can specify multiple key-value pairs in the parameter. |
| IgnoreIfExist | bool | No | Specifies whether to ignore key-value pairs that have the same keys. Default value: false. |

The following example shows how to use this method to add fields to logs. Input data

```json
"aaa1":"value1"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_add_fields",
      "detail": {
        "Fields": {
          "aaa2": "value2",
          "aaa3": "value3"
```

`}` `}` `}` `]` `}` Output data

```json
"aaa1":"value1" "aaa2":"value2" "aaa3":"value3"
```

Remove log fileds You can use this method to remove specific fields from logs. The type of the plug-in is `processor_drop` .

> Not e The method is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| DropKeys | array | No | The array that includes a set of strings. You can remove multiple fields from a log. |

The following example shows how to remove the `aaa1` and `aaa2` fields from a log. Input data

```json
"aaa1":"value1" "aaa2":"value2" "aaa3":"value3"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_drop",
      "detail": {
        "DropKeys": ["aaa1","aaa2"]
```

`}` `}` `]` `}` Output data

```json
"aaa3":"value3"
```

Extract log time (Go) You can use this method to extract time from a log field and convert the time format. The type of the plug-in is `processor_gotime` .

> Not e This plug-in is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the log field from which you want to extract time. |
| SourceFormat | string | Yes | The time that is parsed in Go. |
| SourceLocation | int | Yes | The source time zone. If the parameter is not specified, it indicates the time zone of the local host. |
| DestKey | string | Yes | The destination field. |
| DestFormat | string | Yes | The destination time format in Go. |
| DestLocation | int | No | The destination time zone. If the parameter is not specified, it indicates the time zone of the local host. |
| SetTime | bool | No | Specifies whether to overwrite the original time. Default value: true. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: true. |
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: true. |
| AlarmIfFail | bool | No | Specifies whether to send alerts when extraction failed. Default value: true. |

| Use | 2006-01-02 15:04:05 |   |
|---|---|---|
| 15:04:05 |   | (UTC +9) and save |

| s key _ |   | field |
|---|---|---|
| the | d key _ |   |

method to process logs. Input data

```json
"s_key":"2019-07-05 19:28:01"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_gotime",
      "detail": {
        "SourceKey": "s_key",
        "SourceFormat":"2006-01-02 15:04:05",
        "SourceLocation":8,
        "DestKey":"d_key",
        "DestFormat":"2006/01/02 15:04:05",
        "DestLocation":9,
        "SetTime": true,
        "KeepSource": true,
        "NoKeyError": true,
        "AlarmIfFail": true
```

`}` `}` `]` `}` Output data

```json
"s_key":"2019-07-05 19:28:01" "d_key":"2019/07/05 20:28:01"
```

Expand log fields (JSON) You can use this method to expand a log field. The type of the plug-in is `processor_json` .

> Not e This plug-in is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field you want to expand. |
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: true. |
| ExpandDepth | int | No | The depth of JSON expansion. The value must be a non-negative integer. Default value: 0. This indicates the depth is not limited. The value n specifies that the number of levels to expand is n. |
| ExpandConnector | string | No | The delimiter that you use to connect expanded levels. Default value: . You _ can leave this parameter unspecified. |
| Prefix | string | No | The prefix that you want to add to the name of each new field after expansion. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: true. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| UseSourceKeyAsPrefi x | bool | No | Specifies whether to retain the name of the source field as the prefix of each new field after expansion. Default value: false. |

The following example shows how to use the field expansion (JSON) method to expand the `s_key` field. Input data

```json
"s_key":"{\"k1\":{\"k2\":{\"k3\":{\"k4\":{\"k51\":\"51\",\"k52\":\"52\"},\"k41\":\"41\"}}})"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_json",
      "detail": {
        "SourceKey": "s_key",
        "NoKeyError":true,
        "ExpandDepth":0,
        "ExpandConnector":"-",
        "Prefix":"j",
        "KeepSource": false,
        "UseSourceKeyAsPrefix": true
```

`}` `}` `]` `}` Output data

```json
"s_key":"{\"k1\":{\"k2\":{\"k3\":{\"k4\":{\"k51\":\"51\",\"k52\":\"52\"},\"k41\":\"41\"}}})" "js_key-k1-k2-k3-k4-k51":"51" "js_key-k1-k2-k3-k4-k52":"52" "js_key-k1-k2-k3-k41":"41"
```

Combine log fields (JSON) You can use this method to combine multiple log fields into one field. The type of the plug-in is `processor_packjson` .

> Not e This plug-in is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKeys | array | Yes | The array that includes the names of fields that you want to combine. |
| DestKey | string | No | The name of the destination field after combination. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: true. |

| og Service |   |   | User Guide·Data collectio |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| AlarmIfIncomplete | bool | No | Specifies whether to send alerts if no source fields exist. Default value: true. |

The following example shows how to use the method to combine the `a` and `b` fields into the `d_key` field. Input data

```json
"a":"1" "b":"2"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_packjson",
      "detail": {
        "SourceKeys": ["a","b"],
        "DestKey":"d_key",
        "KeepSource":true,
        "AlarmIfEmpty":true
```

`}` `}` `]` `}` Output data

```json
"a":"1" "b":"2" "d_key":"{\"a\":\"1\",\"b\":\"2\"}"
```

Rename fields You can use this method to rename multiple fields. The type of the plug-in is `processor_rename` .

> Not e This plug-in is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| NoKeyError | bool | No | Specifies whether to report an error if no match exists. Default value: true. |
| SourceKeys | array | Yes | The array that includes the names of fields that you want to rename. |
| DestKeys | array | Yes | The array that includes the new names of the fields. |

The following example shows how to use this method to rename the `aaa1` and `aaa2` fields to `bbb1` and `bbb2` fields. Input data

```json
"aaa1":"value1" "aaa2":"value2" "aaa3":"value3"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_rename",
      "detail": {
        "SourceKeys": ["aaa1","aaa2"],
        "DestKeys": ["bbb1","bbb2"],
        "NoKeyError": true
```

`}` `}` `]` `}` Output data

```json
"bbb1":"value1" "bbb2":"value2" "aaa3":"value3"
```

Extract log time (Strptime) You can use this method to extract time from a log field and parse the time by using the Linux strptime() function. The type of the plug-in is `processor_strptime` .

> Not e This plug-in is available for Logtail 0.16.28 or later.

Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceKey | string | Yes | The name of the field from which you want to extract time. |
| Format | string | Yes | The time format to parse the time. |
| AdjustUTCOffset | bool | No | Specifies whether to adjust the time zone. Default value: false. |
| UTCOffset | int | No | The offset that is used to adjust the time zone. Unit: seconds. For example, if you set the value to 14400, the time zone is changed to UTC+8. |
| AlarmIfFail | bool | No | Specifies whether to send alerts if a field fails to be extracted. |
| KeepSource | bool | No | Specifies whether to return the SourceKey parameter. Default value: true. |

Parse the value of the `log_time` in the %Y/%m/%d %H:%M:%S time format and use the time zone of your local host. The following examples show how to use this method to process logs. Example 1: The time zone is UTC +8. Input data

```json
"log_time":"2016/01/02 12:59:59"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_strptime",
      "detail": {
        "SourceKey": "log_time",
        "Format": "%Y/%m/%d %H:%M:%S"
```

`}` `}` `]` `}` Output data

```json
"log_time":"2016/01/02 12:59:59" Log.Time = 1451710799
```

Example 2: The time zone is UTC +7. Input data

```json
"log_time":"2016/01/02 12:59:59"
```

Configurations `{`

```json
  "processors":[
```

`{`

```json
      "type":"processor_strptime",
      "detail": {
        "SourceKey": "log_time",
        "Format": "%Y/%m/%d %H:%M:%S",
        "AdjustUTCOffset": true,
        "UTCOffset": 25200
```

`}` `}` `]` `}` Output data

```json
"log_time":"2016/01/02 12:59:59" Log.Time = 1451714399
```

Custom methods You can use a combination of multiple processing methods to process logs. The following example shows how to use a single-character delimiter to split a log into several fields and then specify anchor points to extract content from the `detail` field. Input data

```json
"content" : "ACCESS|QAS|11. **. **.**|1508729889935|52460dbed4d540b88a973cf5452b1447|1238|appKey=ba,env=pub,req uestTime=1508729889913,latency=22ms, request={appKey:ba,optional:{\\domains\\:\\daily\\,\\version\\:\\v2\\},rawQuery:{\\query\\:\\The ro ute to Location A\\,\\domain\\:\\Navigation\\,\\intent\\:\\navigate\\,\\slots\\:\\to_geo:level3=Loc ation A\\,\\location\\:\\Location B\\}, requestId:52460dbed4d540b88a973cf5452b1447}, response={answers:[],status:SUCCESS}|"
```

Configurations

```json
"processors" : [
```

`{`

```json
          "type" : "processor_split_char",
          "detail" : {"SourceKey" : "content",
              "SplitSep" : "|",
              "SplitKeys" : ["method", "type", "ip", "time", "req_id", "size", "detail"]
```

`}` `},` `{`

```json
          "type" : "processor_anchor",
          "detail" : "SourceKey" : "detail",
              "Anchors" : [
```

`{`

```json
                          "Start" : "appKey=",
                      "Stop" : ",env=",
                      "FieldName" : "appKey",
                      "FieldType" : "string"
```

`},` `{`

```json
                      "Start" : ",env",
                      "Stop" : ",requestTime=",
                      "FieldName" : "env",
                      "FieldType" : "string"
```

`},` `{`

```json
                      "Start" : ",requestTime=",
                      "Stop" : ",latency",
                      "FieldName" : "requestTime",
                      "FieldType" : "string"
```

`},` `{`

```json
                      "Start" : ",latency=",
                      "Stop" : ",request=",
                      "FieldName" : "latency",
                      "FieldType" : "string"
```

`},` `{`

```json
                      "Start" : ",request=",
                      "Stop" : ",response=",
                      "FieldName" : "request",
                      "FieldType" : "string"
```

`},` `{`

```json
                      "Start" : ",response=",
                      "Stop" : "",
                      "FieldName" : "response",
                      "FieldType" : "json"
```

`}` `]` `}` `}` `]` Output data

```json
"method" : "ACCESS" "type" : "QAS" "ip" : "**. **. **.**" "time" : "1508729889935" "req_id" : "52460dbed4d540b88a973cf5452b1447" "size" : "1238" "appKey" : "ba" "env" : "pub" "requestTime" : "1508729889913" "latency" : "22ms" "request" : "{appKey:nui-banma,optional:{\\domains\\:\\daily-faq\\,\\version\\:\\v2\\},rawQuery:{\\ query\\:\\\345\216\273\344\271\220\345\261\261\347\232\204\350\267\257\347\272\277\\,\\domain\\:\\\ 345\257\274\350\210\252\\,\\intent\\:\\navigate\\,\\slots\\:\\to_geo:level3=\344\271\220\345\261\26 1\\,\\location\\:\\\345\214\227\344\272\254\\},requestId:52460dbed4d540b88a973cf5452b1447}" "response_answers" : "[]" "response_status" : "SUCCESS"
```

#### 3.1.6 Collect container logs

##### 3.1.6.1 Collect standard Docker logs

This topic describes how to use Logtail to collect standard Docker logs and upload these logs together with the container metadata to Log Service.
1. Deploy a Logtail container.
2. Configure a Logtail server group.
Create a server group with a custom ID in the Log Service console. The container cluster can automatically scale up or down based on data traffic.
3. Create a Logtail configuration.
Create a Logtail configuration in the Log Service console. The Logtail configuration process is completed in the Log Service console. No local configuration is needed. Deploy a Logtail container
1. Run the following command to pull the Logtail image.

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/log-service/logtail
```

2. Start a Logtail container.

```
Set the ${your_region_name} , ${your_aliyun_user_id} , and ${your_machine_group_user_defined_id}
```

parameters in the startup template.

```bash
docker run -d -v /:/logtail_host:ro -v /var/run:/var/run --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/${your_region_name}/ilogtail_config.json --env ALIYUN_LOGTAIL_USER_ID=${your_aliyun_user_id} --env
 ALIYUN_LOGTAIL_USER_DEFINED_ID=${your_machine_group_user_defined_id} registry.cn-hangzhou.aliyunc
s.com/log-service/logtail
```

> Not ice Before you set the parameters, you must complete one of the following configurations. Otherwise, the `container text file busy` error may occur when you delete another container.

For CentOS 7.4 and later versions, set fs.may_detach_mounts to 1. For more information, see Bug 1468249, Bug 1441737, and Issue 34538.

> Grant the `privileged` permission to Logtail by adding the `--privileged` flag to the startup parameters. For more information, see Docker run reference.

| Parameter | Description |
|---|---|
| ${your region name} _ _ | The region of the project. For more information, see View the information of a project. |
| ${your aliyun user id} _ _ _ | The user ID. Set this parameter to the ID of your Alibaba Cloud account, which is a string. For information about how to view the ID, see Step 1 in Configure an account ID for a server. |
| ${your machine group user de _ _ _ _ fined id} _ | The custom ID of your server group. For information about how to set the custom ID, see Step 1 in Create a machine group based on a custom ID. |

|   | ${your machine group user de _ _ _ _ | The cus |
|---|---|---|
| fined id} _ |   |   |

After you set the parameters, run the following command to start the Logtail container.

```bash
docker run -d -v /:/logtail_host:ro -v /var/run:/var/run --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/cn_hangzhou/ilogtail_config.json --env
 ALIYUN_LOGTAIL_USER_ID=1654218******--env ALIYUN_LOGTAIL_USER_DEFINED_ID=log-docker-demo registry
.cn-hangzhou.aliyuncs.com/log-service/logtail
```

|   | Not ice You can customize the startup parameters of the Logtail container if the following conditions are met: The following environment variables exist before you start the Logtail container: ALIYUN LOGTAIL _ _ USER DEFINED ID , ALIYUN LOGTAIL USER ID , and ALIYUN LOGTAIL CONFIG . _ _ _ _ _ _ _ The /var/run directory is mounted on the /var/run directory of the Logtail container. To collect container standard output, container logs, or host files, you must mount the root directory on the /logtail host directory of the Logtail container. _ If an error showing The parameter is invalid : uuid=none occurs in the /usr/local/ilogtail/ilogta il.LOG Logtail log file, create a file named product uuid on the host. Add a valid UUID such as 1 _ 69E98C9-ABC0-4A92-B1D2-AA6239C0D261 to the file, and mount the file on the /sys/class/dmi/id/pr oduct uuid directory of the Logtail container. _ |
|---|---|
|   | il.LOG |

| ALIYUN LOGTAIL _ _ |   |
|---|---|

|   | USER DEFINED ID _ _ |
|---|---|

| /usr/local/ilogtail/ilogta |   |   |
|---|---|---|
|   | 1 |   |

Configure a Logtail server group
1. Log on to the Log Service console.
2. Click a project name.
3. In the left-side navigation pane, click the Server Groups icon to show the server group list.
4. Click the icon next to Server Groups, and then select Creat e Server Group.
You can also create a server group when you import data to Log Service.
5. In the dialog box that appears, select Cust om ID from the Identifier drop-down list. Enter the value of `ALIYU`
`N_LOGTAIL_USER_DEFINED_ID` set in the previous step in the Cust om Ident if ier field. Click OK. One minute later, click the name of the server group in the Server Groups list. On the Server Group Set t ings page that appears, you can view the heartbeat status of the Logtail container. For more information, see View the status of a server group. Create a Logtail configuration Create a Logtail configuration in the console. For more information about Docker logs, see Collect container text logs. For more information about Docker standard output, see Collect stdout and stderr logs from containers. Host text logs. The root directory of a host is mounted on the `/logtail_host` directory of the Logtail container by default. You must add the /logtail_host prefix to the log path. For example, if you want to collect data from the `/home` `/logs/app_log/` directory of the host, you must set the log path as `/logtail_host/home/logs/app_log/` . What to do next View the status of the Logtail container. You can run the docker exec ${logtail_container_id} /etc/init.d/ilogtaild status command to view the status of Logtail. View the version number, IP address, and startup time of Logtail. You can run the docker exec ${logtail_container_id} cat /usr/local/ilogtail/app_info.json command to view Logtail information. View the operations logs of Logtail.

| ile in the | /usr/local/ilogtail/ |   |
|---|---|---|
| ilogtail.LOG.x.gz |   | . |

The operations logs of Logtail are stored in the `ilogtail.LOG` file in the `/usr/local/ilogtail/` directory. If the log file is rotated and compressed, it is stored as a file named `ilogtail.LOG.x.gz` . For example:

```
[root@iZbp17enxc2us3624wexh2Z ilogtail]# docker exec a287de895e40 tail -n 5 /usr/local/ilogtail/ilo gtail.LOG [2018-02-06 08:13:35.721864] [INFO] [8] [build/release64/sls/ilogtail/LogtailPlugin.cpp:10 4] logtail plugin Resume:start [2018-02-06 08:13:35.722135] [INFO] [8] [build/release64/sls/ilogtail/LogtailPlugin.cpp:10 6] logtail plugin Resume:success [2018-02-06 08:13:35.722149] [INFO] [8] [build/release64/sls/ilogtail/EventDispatcher.cpp: 369] start add existed check point events, size:0 [2018-02-06 08:13:35.722155] [INFO] [8] [build/release64/sls/ilogtail/EventDispatcher.cpp: 511] add existed check point events, size:0 cache size:0 event size:0 success count:0 [2018-02-06 08:13:39.725417] [INFO] [8] [build/release64/sls/ilogtail/ConfigManager.cpp:37 76] check container path update flag:0 size:1
```

Ignore the following standard output:

```
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57 fe840c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44 beab6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640 b1e16c22dbe/merged: must be superuser to unmount ... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
```

Restart Logtail. To restart Logtail, use the following sample code:

```
[root@iZbp17enxc2us3624wexh2Z ilogtail]# docker exec a287de895e40 /etc/init.d/ilogtaild stop kill process Name: ilogtail pid: 7 kill process Name: ilogtail pid: 8 stop success [root@iZbp17enxc2us3624wexh2Z ilogtail]# docker exec a287de895e40 /etc/init.d/ilogtaild start ilogtail is running
```

##### 3.1.6.2 Collect Kubernetes logs

This topic describes how to install and use Logtail to collect logs from Kubernetes clusters. Configuration procedure Perform the following steps to collect logs from Kubernetes clusters:
1. Install the alibaba-log-controller Helm package.
2. Use the Log Service console to manage log collection configurations.
Step 1: Install Logtail Install Logtail in an Alibaba Cloud Container Service for Kubernetes cluster. If Log Service components are not installed in your cluster, you must manually install the components. i. Connect to the Kubernetes cluster by using CloudShell. ii. Run the following command in CloudShell to obtain the ID of your Apsara Stack tenant account.

```
echo $ALIBABA_CLOUD_ACCOUNT_ID
```

iii. After you set the ${your_k8s_cluster_id} , ${your_ali_uid} , and ${your_k8s_cluster_region_id} parameters, run the following command:

```
wget https://acs-logging.oss-cn-hangzhou.aliyuncs.com/alicloud-k8s-log-installer.sh -O alicloud -k8s-log-installer.sh; chmod 744 ./alicloud-k8s-log-installer.sh; ./alicloud-k8s-log-installer. sh --cluster-id ${your_k8s_cluster_id} --ali-uid ${your_ali_uid} --region-id ${your_k8s_cluster _region_id}
```

Install Logtail in a user-created Kubernetes cluster.

> Not ice
> The version of the Kubernetes cluster must be 1.8 or later.
> Helm 2.6.4 or later must be installed.

i. In the Log Service console, create a project whose name starts with `k8s-log-custom-` . ii. Replace the parameters in the following command based on your business requirements:

```
wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/kubernetes/alicloud-log-k8 s-custom-install.sh; chmod 744 ./alicloud-log-k8s-custom-install.sh; sh ./alicloud-log-k8s-cust om-install.sh {your-project-suffix} {region-id} {aliuid} {access-key-id} {access-key-secret}
```

The following table lists the parameters in the preceding command.

| Parameter | Description |
|---|---|
| {your-project-suffix} | The portion of the project name at the end of k8s-log-custom- . For example, if you create a project whose name is k8s-log-custom- xxxx , set this parameter to xxxx . |
| {regionId} | The ID of the region where the project resides. For more information, see View the information of a project. |
| {aliuid} | The user ID. Set this parameter to the ID of your Apsara Stack tenant account. Not e The ID of an Apsara Stack tenant account is a string. For more information about how to obtain the ID, see Configure an account ID for a server. |
| {access-key-id} | The AccessKey ID of your Apsara Stack tenant account. |
| {access-key-secret} | The AccessKey secret of your Apsara Stack tenant account. |

|   | xxxx |
|---|---|

After Logtail is installed in the Kubernetes cluster, Log Service automatically creates a machine group named k8s-group-${your_k8s_cluster_id} for the project.

> Not e
> A Logstore named `config-operation-log` is automatically created in the project. Do not delete the Logstore.
> When you install Logtail in a user-created Kubernetes cluster, Logtail is granted `privileged` permissions by default. This prevents the `container text file busy` error when you delete a pod. For more information, visit Bug 1468249, Bug 1441737, and Issue 34538.

The following example shows a successful installation:

```
[root@iZbp1dsxxxxxqfbiaZ ~]# wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/ kubernetes/alicloud-log-k8s-custom-install.sh; chmod 744 ./alicloud-log-k8s-custom-install.sh; sh . /alicloud-log-k8s-custom-install.sh xxxx cn-hangzhou 165xxxxxxxx050 LTAxxxxxxxxxxx AIxxxxxxxxxxxxxx xxxxxxxxxxxxxxxe .... .... .... NAME: alibaba-log-controller LAST DEPLOYED: Fri May 18 16:52:38 2018 NAMESPACE: default STATUS: DEPLOYED RESOURCES: ==> v1beta1/ClusterRoleBinding NAME AGE alibaba-log-controller 0s ==> v1beta1/DaemonSet NAME DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR AGE logtail-ds 2 2 0 2 0 <none> 0s ==> v1beta1/Deployment NAME DESIRED CURRENT UP-TO-DATE AVAILABLE AGE alibaba-log-controller 1 1 1 0 0s ==> v1/Pod(related) NAME READY STATUS RESTARTS AGE logtail-ds-7xf2d 0/1 ContainerCreating 0 0s logtail-ds-9j4bx 0/1 ContainerCreating 0 0s alibaba-log-controller-796f8496b6-6jxb2 0/1 ContainerCreating 0 0s ==> v1/ServiceAccount NAME SECRETS AGE alibaba-log-controller 1 0s ==> v1beta1/CustomResourceDefinition NAME AGE aliyunlogconfigs.log.alibabacloud.com 0s ==> v1beta1/ClusterRole alibaba-log-controller 0s [INFO] your k8s is using project : k8s-log-custom-xxx, region : cn-hangzhou, aliuid : *************
**, accessKeyId : LTA**********
[SUCCESS] install helm package : alibaba-log-controller success.
```

To check the status of each Log Service component in the Kubernetes cluster, run the `helm status alibaba-lo` `g-controller` command. If all pods are in the Running state, Logtail is installed. Log on to the Log Service console to find the project. If you have multiple projects, search for the project by using the `k8s-log` keyword. Step 2: Configure log collection Create Logtail configurations for log collection in the console as required. For information about how to collect Kubernetes text logs, see Collect container text logs. For information about how to collect Kubernetes stdout logs, see Collect stdout and stderr logs from containers. Host text logs. By default, the root directory of a host is mounted to the `/logtail_host` directory of the Logtail container. You must add the /logtail_host prefix to the log path. For example, if you want to collect data from the `/home` `/logs/app_log/` directory of the host, you must set the log path to `/logtail_host/home/logs/app_log/` . Other common commands Store logs of multiple clusters in one project You can collect logs from multiple Kubernetes clusters. If you want to store these logs in the same project, you can specify the same cluster ID for the ${your_k8s_cluster_id} parameter when you install Log Service components on multiple Kubernetes clusters. For example, if you have three Kubernetes clusters whose IDs are abc001, abc002, and abc003, specify `abc001` for the ${your_k8s_cluster_id} parameter when you install Log Service components for each Kubernetes cluster.

> Not ice This feature is unavailable for Kubernetes clusters that reside in different regions.

Logtail container logs Logtail log files named `ilogtail.LOG` and `logtail_plugin.LOG` are stored in the `/usr/local/ilogtail/` directory of a Logtail container. Ignore the following standard output:

```
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57 fe840c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44 beab6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640 b1e16c22dbe/merged: must be superuser to unmount ...... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
```

View the status of each Log Service component in a Kubernetes cluster

```
helm status alibaba-log-controller
```

Troubleshoot alibaba-log-controller startup failures Make sure that the following conditions are met: Log Service components are installed on the master node of the Kubernetes cluster. The Kubernetes cluster ID that you specified is valid when you install Log Service components. If Log Service components fail to be installled because the preceding conditions are not met, run the `helm del` `--purge alibaba-log-controller` command to delete the installation package and install Log Service components again. View the status of Logtail DaemonSet in a Kubernetes cluster Run the `kubectl get ds -n kube-system` command.

> Not e The default namespace of Logtail is `kube-system` .

View the version number, IP address, and startup time of Logtail. Example:

```
[root@iZbp1dsu6v77zfb40qfbiaZ ~]# kubectl get po -n kube-system | grep logtail NAME READY STATUS RESTARTS AGE logtail-ds-gb92k 1/1 Running 0 2h logtail-ds-wm7lw 1/1 Running 0 4d [root@iZbp1dsu6v77zfb40qfbiaZ ~]# kubectl exec logtail-ds-gb92k -n kube-system cat /usr/local/ilogt ail/app_info.json
```

`{`

```json
   "UUID" : "",
   "hostname" : "logtail-ds-gb92k",
   "instance_id" : "0EBB2B0E-0A3B-11E8-B0CE-0A58AC140402_172.20.4.2_1517810940",
   "ip" : "172.20.4.2",
   "logtail_version" : "0.16.2",
   "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64",
   "update_time" : "2018-02-05 06:09:01"
```

`}` View the operational logs of Logtail

| in the | /usr/local/ilogtail/ |   |
|---|---|---|
| ilogtail.LOG.x.gz |   | . |

Logtail operational logs are stored in the `ilogtail.LOG` file in the `/usr/local/ilogtail/` directory. If the log file is rotated and compressed, it is stored as a file named `ilogtail.LOG.x.gz` . Example:

```
[root@iZbp1dsu6v77zfb40qfbiaZ ~]# kubectl exec logtail-ds-gb92k -n kube-system tail /usr/local/ilog tail/ilogtail.LOG [2018-02-05 06:09:02.168693] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:104] logtai l plugin Resume:start [2018-02-05 06:09:02.168807] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:106] logtai l plugin Resume:success [2018-02-05 06:09:02.168822] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:369] star t add existed check point events, size:0 [2018-02-05 06:09:02.168827] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:511] add existed check point events, size:0 cache size:0 event size:0 success count:0
```

Restart Logtail in a pod Example:

```
[root@iZbp1dsu6v77zfb40qfbiaZ ~]# kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtail d stop kill process Name: ilogtail pid: 7 kill process Name: ilogtail pid: 9 stop success [root@iZbp1dsu6v77zfb40qfbiaZ ~]# kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtail d start ilogtail is running
```

##### 3.1.6.3 Collect container text logs

Logtail collects text logs generated in containers and uploads these logs together with the container-related metadata information to Log Service. Features Compared with basic log file collection, Docker file collection has the following characteristics: Allows you to configure the log path of a container, without the need to consider the mapping between the path and the host. Allows you to use labels to specify the containers whose logs are to be collected. Allows you to use labels to exclude specific containers. Allows you to use environment variables to specify the containers whose logs are to be collected. Allows you to use environment variables to exclude specific containers. Supports multiline logs such as Java Stack logs. Supports automatic labeling for container data. Supports automatic labeling for Kubernetes containers. Collection stop policy: When a container is stopped and Logtail detects the `die` event on the container, Logtail stops collecting logs of the container (with a latency of no more than 3 seconds). In this case, if a collection latency occurs, some logs generated before the stop action may be lost. Docker storage driver: Only overlay and overlay2 are supported. For other storage drivers, you must mount the log directory to the local host. Logtail running mode: Logtail must run in a container and must be deployed based on Logtail deployment solutions. Label: refers to the label information in docker inspect. It is not synonymous with labels in Kubernetes. Environment: refers to the environment information configured during container startup.
1. Deploy and configure the Logtail container.
2. Configure log collection in Log Service.
Logtail deployment and configuration Kubernetes For more information about Kubernetes log collection, see Logtail deployment solution for collecting Kubernetes logs. Management methods for other containers For more information about management methods for other containers, such as Swarm and Mesos, see Common deployment solution for collecting Docker logs. Collection configuration
1. Log on to the Log Service console.
2. Click the Import Dat a button. On the Import Dat a page that appears, select Docker File.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Configure Logtail.
The following table lists data source-specific parameters. For more information about common parameters, see Configure text log collection.

| Parameter | Description |
|---|---|
| Docker File | This parameter is used to check whether the collected target file is a Docker file. |
| Label Whitelist | LabelKey is required. If LabelValue is not empty, only containers whose labels contain LabelKey = LabelValue are collected. If LabelValue is empty, all the containers whose labels contain LabelKey are collected. Not e Key-value pairs are disjunctive with each other. If the label of a container contains one of the key-value pairs you specify, logs of the container are collected. Labels refer to Docker labels. |

| Parameter | Description |
|---|---|
| Label Blacklist | LabelKey is required. If LabelValue is not empty, only containers whose labels contain LabelKey = LabelValue are excluded. If LabelValue is empty, all containers whose labels contain LabelKey are excluded. Not e Key-value pairs are disjunctive with each other. If the label of a container contains one of the key-value pairs you specify, the container is excluded. Labels described in this topic refer to the label information in docker inspect. |
| Environment Variable Whitelist | EnvKey is required. If EnvValue is not empty, only containers whose environment variables contain EnvKey = EnvValue are collected. If EnvValue is empty, all containers whose environment variables contain EnvKey are collected. Not e Key-value pairs are disjunctive with each other. If the environment variable of a container contains one of the key-value pairs you specify, logs of the container are collected. The environment variable refers to the environment information configured in container startup. |
| Environment Variable Blacklist | EnvKey is required. If EnvValue is not empty, only containers whose environment variables contain EnvKey = EnvValue are excluded. If EnvValue is empty, all containers whose environment variables contain EnvKey are excluded. Not e Key-value pairs are disjunctive with each other. If the environment variable of a container contains one of the key-value pairs you specify, the container is excluded. The environment variable refers to the environment information configured in container startup. |

> Not e
> Labels in whitelist and blacklist are different from those defined in Kubernetes. Labels in this topic refer to the label information in docker inspect.
> A namespace and a container name in Kubernetes can be mapped to Docker labels. LabelKey corresponding to a namespace is `io.kubernetes.pod.namespace` . LabelKey corresponding to a container name is `io.kubernetes.container.name` . For example, the namespace of the pod you created is backend-prod and the container name is worker-server. In this case, you can configure a whitelist label: `io.kubernetes.pod.namespace : backend-prod` or `io.kubernetes.container.nam`
> `e : worker-server` , so that only logs of the container are collected.
> In Kubernetes, we recommend that you only use the `io.kubernetes.pod.namespace` and `io.kub`
> `ernetes.container.name` labels. In other cases, use an environment variable whitelist or blacklist.

7. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

Configuration examples Environment configuration Collect the logs of the container whose environment variable is `NGINX_PORT_80_TCP_PORT=80` but not `POD_NAM` `ESPACE=kube-system` . The log file path is `/var/log/nginx/access.log` and logs are parsed in simple mode.

> Not e The environment variable refers to the environment information configured in container startup.

Environment configuration example Label configuration Collect the logs of a container that meets the following conditions: the container label is `io.kubernetes.conta` `iner.name=nginx` , the log file path is `/var/log/nginx/access.log` , and logs are parsed in simple mode.

> Not e Labels refer to Docker labels.

Label configuration example Default fields Each uploaded log of a common Docker container contains the following fields.

| Field | Description: |
|---|---|
| image name _ _ _ | The name of the image. |
| container name _ _ _ | The name of the container. |
| container ip _ _ _ | The IP address of the container. |

If a Kubernetes cluster is used, each uploaded log contains the following fields.

| Field | Description |
|---|---|
| image name _ _ _ | The name of the image. |
| container name _ _ _ | The name of the container. |
| pod name _ _ _ | The name of the pod. |
| namespace _ _ | The namespace to which the pod belongs. |
| pod uid _ _ _ | The unique identifier of the pod. |
| container ip _ _ _ | The IP address of the pod. |

##### 3.1.6.4 Collect stdout and stderr logs from containers

This topic describes how to use Logtail to collect standard output (stdout) and standard error (stderr) logs from containers. After you collect stdout and stderr logs, you can upload the logs together with the container-related metadata to Log Service. Features Collects stdout and xxx logs. Labels the containers from which you want to collect stdout and stderr logs. Uses tags to exclude specific containers. Allows you to use environment variables to specify the containers whose logs are to be collected. Allows you to use environment variables to exclude specific containers. Supports multiline logs such as Java Stack logs. Supports automatic labeling for container data. Supports automatic labeling for Kubernetes containers. Implementation As shown in the following figure, Logtail communicates with the domain socket of the Docker engine to query containers that run on the Docker engine. Logtail also locates containers from which you want to collect logs based on the specified labels and environment variables. Logtail then uses the docker logs command to collect logs from the specified containers. When Logtail collects the stdout logs of a container, Logtail records information about log file positions to the checkpoint file at regular intervals. If Logtail is restarted, Logtail collects logs from the last log file position. This feature is available only for Logtail 0.16.0 or later that runs on Linux. For more information about Logtail versions and version updates, see Install Logtail in Linux. The domain socket must exist and can access the Docker engine. Otherwise, Logtail cannot access the Docker engine by running the `/var/run/docker.sock` file. The last multiline log that you collect must be cached for at least 1,000 seconds. By default, the retention period for a multiline log is 3 seconds. You can specify the period by configuring the `BeginLineTimeoutMs` parameter. The value of the parameter must be a minimum of 1,000 ms. Otherwise, a false positive error may occur. Collection stop policy: When a container is stopped and Logtail detects the `die` event on the container, Logtail stops collecting stdout logs of the container. In this case, if a collection latency occurs, some stdout logs that are generated before the stop action may be lost. Docker log driver: Only log drivers of the JSON type are supported in the collection of stdout logs. Context: By default, a collection configuration is in the same context. If you need to configure different types of containers in different contexts, configure each type separately. Data processing: By default, collected logs start with the `content` field. You can apply standard processing methods to these logs. For more information about how to configure one or more processing methods, see Configure data processing methods. Label: refers to the label information in docker inspect. It is not related to labels in Kubernetes configurations. Environment: refers to environment information that you specified during container startup.
1. Deploy and configure Logtail on one or more containers.
2. Create a Logtail configuration and deliver it to Logtail.
Logtail deployment and configuration Kubernetes For more information about how to collect Kubernetes logs, see Logtail deployment solution for collecting Kubernetes logs. Configure Logtail on other containers For more information about how to configure Logtail on other containers, such as Swarm and Mesos, see Common Logtail deployment solution for collecting Docker logs. Configure a data source
1. Log on to the Log Service console.
2. Click Import Dat a. On the Import Dat a page that appears, select Docker St andard Out put .
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Configure a data source.
In the Plug-in Conf ig section, set the required parameters. The following example shows how to set these parameters. For more information, see Parameters. `{`

```json
 "inputs": [
```

`{`

```json
         "type": "service_docker_stdout",
         "detail": {
             "Stdout": true,
             "Stderr": true,
             "IncludeLabel": {
                 "io.kubernetes.container.name": "nginx"
```

`},`

```json
             "ExcludeLabel": {
                 "io.kubernetes.container.name": "nginx-ingress-controller"
```

`},`

```json
             "IncludeEnv": {
                 "NGINX_SERVICE_PORT": "80"
```

`},`

```json
             "ExcludeEnv": {
                 "POD_NAMESPACE": "kube-system"
```

`}` `}` `}` `]` `}`
7. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

Parameters The type of the input source is `service_docker_stdout` .

> Not e Before Logtail uploads data to Log Service, Logtail can process collected data. For more information about processing methods, see Configure data processing methods.

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| IncludeLabel | JSON text. Key: JSON string. Value: JSON string. | Yes | By default, this parameter is not specified. If the parameter is not specified, Logtail collects logs from all containers. If you set the key field and leave the value field empty, Logtail collects logs from containers whose labels include this key. Not e Key-value pairs are disjunctive with each other. If the label of a container matches one of the key- value pairs, logs of the container are collected. Labels refer to docker labels. |
| ExcludeLabe l | JSON text. Key: JSON string. Value: JSON string. | No | This parameter is not specified by default. If the parameter is empty, no containers are excluded. If the key is not empty but the value is empty, the containers whose labels include this key are excluded. Not e Key-value pairs are disjunctive with each other. If the label of a container matches one of the key- value pairs, the container is excluded. Labels described in this topic refer to Docker labels. |
| IncludeEnv | Map. Key: string. Value: string | No | This parameter is empty by default. If the parameter is empty, logs of all containers are collected. If the key is not empty but the value is empty, logs of the containers whose environment variables include this key are collected. Not e Key-value pairs are disjunctive with each other. If the environment variable of a container includes one of the key-value pairs, the container is excluded. The environment variable refers to the environment information configured in container startup. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ExcludeEnv | Map. Key: string. Value: string | No | This parameter is empty by default. If you leave the parameter empty, no container is excluded. If you set the key and leave the value empty, the containers whose environment variables include this key are excluded. Not e Key-value pairs are disjunctive with each other. When the environment variable of a container includes one of the key-value pairs, the container is excluded. The environment variable refers to the environment information configured in container startup. |
| Stdout | Boolean | No | If the value of the parameter is false, stdout data is not collected. Default value: true. |
| Stderr | Boolean | No | Default value: true. If the value of the parameter is false, stderr data is not collected. |
| BeginLineRe gex | String | No | This parameter is not specified by default. If the parameter is not empty, the regular expression is used to match the first line of each log. If a line matches this regular expression, this line is assumed as the start of a new log. Otherwise, this line is assumed as part of the previous log. |
| BeginLineTi meoutMs | Integer | No | The timeout period for the regular expression to match a line. Default value: 3000. Unit: ms. If no new log appears within 3 seconds, the most recent log is uploaded. |
| BeginLineCh eckLength | Integer | No | The length of data for the regular expression to match. Default value: 10×1024. Unit: bytes. You can set this parameter to check whether the beginning part of a line can match the regular expression. This improves matching efficiency. |
| MaxLogSize | Integer | No | The maximum length of a log. Default value: 512×1024. Unit: bytes. If the length exceeds this value, the log data is uploaded directly without finding the first line of logs. |

|   | Not e Labels defined in IncludeLabel and ExcludeLabel are different from those defined in Kubernetes. Labels in this topic refer to Docker labels. A namespace and a container name in Kubernetes can be mapped to Docker labels. The LabelKey parameter corresponding to a namespace is io.kubernetes.pod.namespace . The LabelKey parameter corresponding to a container name is io.kubernetes.container.name . For example, the namespace of the pod you created is backend-prod and the container name is worker-server. In this case, you can configure a whitelist label: io.kubernetes.pod.namespace : backend-prod or io.kubernetes.contai ner.name : worker-server , so that only logs of the container are collected. In Kubernetes, we recommend that you use the io.kubernetes.pod.namespace and io.kubernetes. container.name labels. In other cases, use IncludeEnv or ExcludeEnv. |
|---|---|
|   | ner.name : worker-server |

| io.kubernetes. |   |
|---|---|

|   | container.name |
|---|---|

Default fields Common Docker containers Each uploaded log contains the following fields.

| Field | Description: |   |   |
|---|---|---|---|
| time _ _ | The data upload time. Example: 2018-02-02T02:18:41 .979147844Z . |   |   |
|   |   | 2018-02-02T02:18:41 |   |
| source _ _ | The type of the input source. Valid values: stdout and stderr. |   |   |
| image name _ _ _ | The name of the image. |   |   |
| container name _ _ _ | The name of the container. |   |   |
| container ip _ _ _ | The IP address of the container. |   |   |

|   | .979147844Z |
|---|---|

Kubernetes containers Each uploaded log contains the following fields.

| Field | Description |   |   |
|---|---|---|---|
| time _ _ | The data upload time. Example: 2018-02-02T02:18:41 .979147844Z . |   |   |
|   |   | 2018-02-02T02:18:41 |   |
| source _ _ | The type of input sources. Valid values: stdout and stderr. |   |   |
| image name _ _ _ | The name of the image. |   |   |
| container name _ _ _ | The name of the container. |   |   |
| pod name _ _ _ | The name of the pod. |   |   |
| namespace _ _ | The namespace where the pod is located. |   |   |
| pod uid _ _ _ | The unique identifier of the pod. |   |   |
| container id _ _ _ | The IP address of the pod. |   |   |

|   | .979147844Z |
|---|---|

Common configuration examples Environment configuration Collect the logs of the container whose environment variable is `NGINX_PORT_80_TCP_PORT=80` but not `POD_NAM`

```
ESPACE=kube-system .
```

> Not e The environment variable refers to the environment information configured in container startup.

Environment configuration example Collection configuration `{`

```json
    "inputs": [
```

`{`

```json
            "type": "service_docker_stdout",
            "detail": {
                "Stdout": true,
                "Stderr": true,
                "IncludeEnv": {
                    "NGINX_PORT_80_TCP_PORT": "80"
```

`},`

```json
                "ExcludeEnv": {
                    "POD_NAMESPACE": "kube-system"
```

`}` `}` `}` `]` `}` Label configuration Collect the stdout and stderr logs of the container whose label is `io.kubernetes.container.name=nginx` but not `type=pre` .

> Not e Labels refer to Docker labels.

Label configuration example `{`

```json
    "inputs": [
```

`{`

```json
            "type": "service_docker_stdout",
            "detail": {
                "Stdout": true,
                "Stderr": true,
                "IncludeLabel": {
                    "io.kubernetes.container.name": "nginx"
```

`},`

```json
                "ExcludeLabel": {
                    "type": "pre"
```

`}` `}` `}` `]` `}` Example of configuring multiline log collection Configuring multiline log collection is important for the collection of Java exception stack logs. The following section introduces a standard collection configuration for Java stdout logs. Sample log

```
2018-02-03 14:18:41.968 INFO [spring-cloud-monitor] [nio-8080-exec-4] c.g.s.web.controller.DemoCon troller : service start 2018-02-03 14:18:41.969 ERROR [spring-cloud-monitor] [nio-8080-exec-4] c.g.s.web.controller.DemoCon troller : java.lang.NullPointerException at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:193
```

`)`

```
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:166) at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:199) at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:96) ... 2018-02-03 14:18:41.968 INFO [spring-cloud-monitor] [nio-8080-exec-4] c.g.s.web.controller.DemoCon troller : service start done
```

Collection configuration Collect logs of the container whose label is `app=monitor` . The first line of each log to be collected is of the date type. To improve matching efficiency, only the first 10 bytes of each line are checked. `{`

```json
"inputs": [
```

`{`

```json
    "detail": {
      "BeginLineCheckLength": 10,
      "BeginLineRegex": "\\d+-\\d+-\\d+. *",
      "IncludeLabel": {
        "app": "monitor"
```

`}` `},`

```json
    "type": "service_docker_stdout"
```

`}` `]` `}` Process collected data Logtail can process the collected Docker stdout logs by using a common data processing method. Use a regular expression to extract the time, module, thread, class, and info fields. Collection configuration Collect logs from a container whose label is `app=monitor` . The first line of each log to be collected is of the date type. To improve matching efficiency, only the first 10 bytes of each line are checked. `{`

```json
"inputs": [
```

`{`

```json
    "detail": {
      "BeginLineCheckLength": 10,
      "BeginLineRegex": "\\d+-\\d+-\\d+. *",
      "IncludeLabel": {
        "app": "monitor"
```

`}` `},`

```json
    "type": "service_docker_stdout"
```

`}` `],`

```json
"processors": [
```

`{`

```json
        "type": "processor_regex",
        "detail": {
            "SourceKey": "content",
            "Regex": "(\\d+-\\d+-\\d+ \\d+:\\d+:\\d+\\.\\d+)\\s+(\\w+)\\s+\\[([^]]+)]\\s+\\[([^]]+)
]\\s+:\\s+([\\s\\S]*)",
            "Keys": [
                "time",
                "module",
                "thread",
                "class",
                "info"
```

`],`

```json
            "NoKeyError": true,
            "NoMatchError": true,
            "KeepSource": false
```

`}` `}` `]` `}` Sample output

```
After the 2018-02-03 14:18:41.968 INFO [spring-cloud-monitor] [nio-8080-exec-4] c.g.s.web.controller.D
```

`emoController : service start done` log is processed, the following output is returned:

```
__tag__:__hostname__:logtail-dfgef _container_name_:monitor _image_name_:registry.cn-hangzhou.aliyuncs.xxxxxxxxxxxxxxx _namespace_:default _pod_name_:monitor-6f54bd5d74-rtzc7 _pod_uid_:7f012b72-04c7-11e8-84aa-00163f00c369 _source_:stdout _time_:2018-02-02T14:18:41.979147844Z time:2018-02-02 02:18:41.968 level:INFO module:spring-cloud-monitor thread:nio-8080-exec-4 class:c.g.s.web.controller.DemoController message:service start done
```

#### 3.1.7 Limits

This topic describes the limits of Logtail. These limits apply when you collect files, manage resources, and resolve errors. Limits on file collection

| Item | Description |
|---|---|
| File encoding | Log files encoded in UTF-8 and GBK are supported. We recommend that you use UTF-8 encoding for better processing performance. If log files are encoded in other formats, errors such as garbled characters and data loss may occur. |
| Log file size | Unlimited. |
| Log file rotation | Supported. Both .log* and .log are supported for file names. |
| Log collection behavior when log parsing is restricted | When log parsing is restricted, Logtail keeps the log file descriptor (FD) open. If log file rotation occurs multiple times during the restriction, Logtail attempts to keep the log parsing sequence of each rotation. If the number of rotated logs to be parsed exceeds 20, Logtail does not process subsequent log files. |
| Symbolic link | Monitored directories can be soft links. |
| Size of a single log entry | The maximum size of a single log entry is 512 KB. If a multi-line log entry is divided by using a regular expression to match the first line, the maximum size of each log entry after division is still 512 KB. If the size of a log entry exceeds 512 KB, the log entry is forcibly separated into multiple parts for collection. For example, if the size of a log entry is 1,025 KB, it will be split into three parts: 512 KB, 512 KB, and 1 KB. These log parts are collected in sequence. |
| Regular expression | Perl-based regular expressions can be used. |
| Multiple Logtail configuration files for the same log file | Not supported. We recommend that you collect and store log files to one Logstore, and configure multiple subscriptions. If this feature is required, configure symbolic links for log files to bypass this limit. |

| Item | Description |
|---|---|
| File opening behavior | When Logtail collects a log file, Logtail opens the log file. If the log file is not modified for more than 5 minutes and log rotation does not occur, Logtail closes the log file. |
| First log collection behavior | Logtail collects only incremental log files. If a log file is modified for the first time and the log file size exceeds 1 MB, Logtail collects the logs from the last 1 MB. Otherwise, Logtail collects the logs from the beginning of the log file. If the log file is not modified after the Logtail configuration file is sent to the server where the log file resides, Logtail does not collect the log file. |
| Non-standard text logs | If a log entry contains \0 in multiple lines, the log entry is truncated at the first \0. |

Limits on checkpoints

| Item | Description |
|---|---|
| Checkpoint timeout period | If a log file is not modified for more than 30 days, the checkpoint of the log file is deleted. |
| Checkpoint storage policy | Checkpoints are saved every 15 minutes and are automatically saved when you exit Logtail. |
| Checkpoint storage path | By default, checkpoints are stored in the /tmp/logtail checkpoint directory. For more _ information about how to modify the values of the related parameters, see Set Logtail startup parameters. |

Limits on configurations

| Item | Description |
|---|---|
| Configuration update | A custom configuration update requires about 30 seconds to take effect. |
| Dynamic loading of Logtail configuration files | Supported. The update of a Logtail configuration file does not affect other Logtail configuration files. |
| Number of Logtail configuration files | Unlimited. However, we recommend that you create a maximum of 100 Logtail configuration files on a server. |
| Multi-tenant isolation | Logtail configuration files for different tenants are isolated. |

Limits on resources and performance metrics

| Item | Description |
|---|---|
| Throughput for log processing | The default traffic of raw logs is limited to 2 MB/s. Data is uploaded after it is encoded and compressed. The compression ratio ranges from 5:1 to 10:1. Logs may be lost if the traffic exceeds the limit. For more information about how to modify the values of the related parameters, see Set Logtail startup parameters. |

| Item | Description |
|---|---|
| Maximum processing speed | Single-core processing speed: The maximum processing speed is 100 MB/s for logs in simple mode, 40 MB/s for logs in delimiter mode, and 30 MB/s for logs in JSON mode. By default, the maximum processing speed is 20 MB/s for logs in full regex mode based on the complexity of regular expressions. If multiple processing threads are enabled, the performance can be improved by 1.5 to 3 times. |
| Number of monitored directories | Logtail limits the depth of monitored directories to reduce the consumption of your resources. If the upper limit is reached, Logtail stops monitoring additional directories and log files. Logtail monitors a maximum of 3,000 directories, including subdirectories. |
| Number of monitored files | A Logtail configuration file on each server can be used to monitor a maximum of 10,000 files by default. A Logtail client on each server can monitor a maximum of 100,000 files by default. Excessive files are not monitored. If the upper limit is reached, you can perform the following operations: Improve the depth of the monitored directory in each Logtail configuration file. Modify the value of the mem usage limit parameter to increase the Logtail _ _ memory usage threshold. For more information, see Set Logtail startup parameters. You can set a memory usage threshold of 2 GB for Logtail. In this case, the maximum number of files that each Logtail configuration file can be used to monitor is increased to 100,000. The maximum number of files that each Logtail client can monitor is increased to 1,000,000. |
| Default resources | By default, Logtail consumes up to 40% of CPU usage and 256 MB of memory. If logs are generated at a high speed, you can modify relevant parameters. For more information, see Set Logtail startup parameters. |
| Processing policy of threshold- crossing resources | If the resources occupied by Logtail exceed the upper limit and this issue lasts for five or more minutes, Logtail is forcibly restarted. The restart may cause data loss or duplication. |

Limits on error handling

| Item | Description |
|---|---|
| Network error handling | If a network error occurs, Logtail retries and adjusts the retry interval. |
| Processing policy of threshold- crossing resources | If the data transmission speed exceeds the quota of the Logstore, Logtail restricts the log collection speed and retries the log collection. |
| Maximum retry period before timeout | If data fails to be transmitted and the failure lasts for more than six consecutive hours, Logtail discards the data. |
| Status self-check | Logtail restarts if an exception occurs, for example, an application unexpectedly exits or the resource usage exceeds the quota. |

Other limits

| Item | Description |
|---|---|

| Item | Description |
|---|---|
| Log collection latency | A latency of less than 1 second exists between the time when a log is written to a disk and the time when Logtail collects the log. However, if the log collection speed is restricted, the latency increases. |
| Log upload policy | Before Logtail uploads logs, it aggregates the logs in the same file. The log upload starts if the number of logs exceeds 2,000, the total size of logs exceeds 2 MB, or the log collection duration exceeds 3 seconds. |

### 3.2 Other collection methods

#### 3.2.1 WebTracking

This topic describes how to use WebTracking to collect logs from websites that are written in HTML or HTML5, iOS, and Android. Context Log Service uses WebTracking to collect logs from websites written in HTML or HTML5, iOS, and Android. You can customize dimensions and metrics. In the preceding figure, WebTracking allows you to collect user information from various browsers, iOS apps, and Android apps (except for SDK for iOS or Android). For example: Browsers, operating systems, and resolutions used by users. Browsing history such as preferences on different websites. The length of time that users stay on an app and whether the users are active in the app. Precautions Dirty data may occur due to the use of WebTracking. This occurs because WebTracking allows unauthorized write access from Internet anonymous users to a Logstore. GET and POST requests are supported. The size of a request body cannot exceed 16 KB. The same limits apply to POST requests and the Putlogs API operation. The maximum number of logs that you can use a POST request to collect at a time is 4,096. The total size of these logs cannot exceed 3 MB. Step 1: Enable WebTracking Log on to the Log Service console and enable WebTracking.
1. Log on to the Log Service console.
2. Select the target Logstore, go to the Logst ore At t ribut es page.
Method 1: Click the Modify icon under the name of the Logstore. Method 1: Click the icon next to the name of the Logstore, and select Modif y.
3. On the Logst ore At t ribut es page, click Modif y in the upper-right corner.
4. Turn on the WebTracking switch.
Use SDK for Java to enable WebTracking Example:

```java
import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.LogStore; import com.aliyun.openservices.log.exception.LogException; public class WebTracking {
  static private String accessId = "your accesskey id";
  static private String accessKey = "your accesskey";
  static private String project = "your project";
  static private String host = "log service data address";
  static private String logStore = "your logstore";
  static private Client client = new Client(host, accessId, accessKey);
  public static void main(String[] args) {
      try {
          //Enable WebTracking on an existing Logstore.
          LogStore logSt = client.GetLogStore(project, logStore).GetLogStore();
          client.UpdateLogStore(project, new LogStore(logStore, logSt.GetTtl(), logSt.GetShardCount(),
true));
          //Disable WebTracking.
          //client.UpdateLogStore(project, new LogStore(logStore, logSt.GetTtl(), logSt.GetShardCount(
), false));
          //Create a Logstore on which you want to enable WebTracking.
          //client.UpdateLogStore(project, new LogStore(logStore, 1, 1, true));
```

`}`

```
      catch(LogException e){
          e.printStackTrace();
```

`}` `}` `}` Step 2: Collect logs After you enable WebTracking for a Logstore, you can use the following methods to upload data to the Logstore. Use the JavaScript SDK i. Copy the loghub-tracking.js file to the web directory and add the following script to the file. Click here to copy the script.

```
<script type="text/javascript" src="loghub-tracking.js" async></script>
```

> Not e To ensure that a page loads, the script asynchronously sends HTTP requests. If data must be sent several times during the page loading, the newest request overwrites the previous HTTP request. A message showing WebTracking is about to exit appears in the browser. To eliminate the issue, send requests in a synchronous manner. To implement the method, perform the following step.

Original statement:

```
this.httpRequest_.open("GET", url, true)
```

Replace the original statement with the following statement:

```
this.httpRequest_.open("GET", url, false)
```

ii. Create a tracker.

```
var logger = new window.Tracker('${host}','${project}','${logstore}'); logger.push('customer', 'zhangsan'); logger.push('product', 'iphone 6s'); logger.push('price', 5500); logger.logger(); logger.push('customer', 'lisi'); logger.push('product', 'ipod'); logger.push('price', 3000); logger.logger();
```

The following table lists the parameters:

| Parameter | Description |
|---|---|
| ${host} | The endpoint of the region where Log Service resides. For more information, see the Obtain an endpoint topi c in the Log Service Developer Guide . |
| ${project} | The name of the project that you create in Log Service. |
| ${logstore} | The name of the Logstore in the ${project} . |

After you run the following code, the following logs appear in Log Service.

```
customer:zhangsan product:iphone 6s price:5500 customer:lisi product:ipod price:3000
```

Use HTTP GET requests

```bash
curl --request GET 'http://${project}.${host}/logstores/${logstore}/track? APIVersion=0.6.0&key1=va l1&key2=val2'
```

The following table lists the parameters.

| Parameter | Description |
|---|---|
| ${project} | The name of the project that you create in Log Service. |
| ${host} | The endpoint of the region where Log Service resides. |
| ${logstore} | The name of a Logstore that has WebTracking enabled in the ${project} . |
| APIVersion=0.6.0 | (Required) A reserved parameter. |
| topic =yourtopic __ __ | (Optional) A reserved parameter that specifies the topic of the log. |
| key1=val1, key2=val2 | The key-value pairs that you want to upload to Log Service. You can specify multiple pairs. Make sure that the length of each request URL is less than 16 KB. |

Use HTML img tags

```
<img src='http://${project}.${host}/logstores/${logstore}/track.gif? APIVersion=0.6.0&key1=val1&key 2=val2'/> <img src='http://${project}.${host}/logstores/${logstore}/track_ua.gif? APIVersion=0.6.0&key1=val1& key2=val2'/>
```

The parameters that you need to specify are the same as the preceding parameters. In addition to custom parameters that are uploaded by track_ua.gif, Log Service also uses UserAgent and referer fields in the HTTP header as the fields of logs.

#### 3.2.2 Use SDKs to collect logs

##### 3.2.2.1 Producer Library

The Aliyun LOG Java Producer supports Java applications that run in big data processing scenarios with high concurrency. The library is easy to use and highly customizable. For more information about the related GitHub project, visit Aliyun LOG Java Producer.

##### 3.2.2.2 Log4j Appender

Log4j is an open-source logging framework of Apache. You can use Log4j to write logs to the Log Service console, files, graphical user interface (GUI) components, socket servers, NT kernel loggers, or Unix syslog daemons. You can specify the output format of each log. You can also specify the severity level of each log to implement a finegrained control on log generation. Log4j consists of three components: loggers, appenders, and layouts. Loggers allow you to specify the severity level of each log. Severity levels are sorted into ERROR, WARN, INFO, and DEBUG in descending order of severity. Appenders allow you to specify the destination of each log. A destination can be the Log Service console or a file. Layouts allow you to specify the output format of each log. The output format defines how logs are displayed. To write logs to Log Service, use the Alibaba Cloud Log Log4j Appender. For information about where to download the library and how to use it, see Log4j Appender.

##### 3.2.2.3 Logback Appender

Logback was created by the same developer of Log4j. Logback allows you to write logs to multiple destinations. These destinations include the Log Service console, files, graphical user interface (GUI) components, socket servers, NT kernel loggers, and Unix syslog daemons. You can define the output format of each log. If you define the severity level of each log, you can implement a fine-grained control on the log generation process. You can set the destination of logs to Log Service by using the Aliyun Log Logback Appender. The following example shows the format of logs that are uploaded to Log Service.

```
level: ERROR location: com.aliyun.openservices.log.logback.example.LogbackAppenderExample.main(LogbackAppenderExamp le.java:18) message: error log throwable: java.lang.RuntimeException: xxx thread: main time: 2018-01-02T03:15+0000 log: 2018-01-02 11:15:29,682 ERROR [main] com.aliyun.openservices.log.logback.example.LogbackAppenderE xample: error log __source__: xxx __topic__: yyy
```

For information about where to download the library and how to use it, see Logback Appender.

##### 3.2.2.4 Golang Producer Library

The Aliyun LOG Go Producer Library supports Go applications that run in big data processing scenarios with high concurrency. The library is easy to use and highly customizable. You can use the library to create producers that allow you to resend failed logs. Before Go applications send log data to Log Service, you can use these producers to compress the log data. This improves write performance. For more information about the related GitHub project, visit Aliyun Log Go Producer.

##### 3.2.2.5 Python logging

Configurations For more information about the configurations that are related to the Python logging module, see Logging configuration. The Python logging module allows you to configure logging by using code or a configuration file. The following example shows how to configure logging by using the `logging.conf` configuration file.

```
[loggers] keys=root,sls [handlers] keys=consoleHandler, slsHandler [formatters] keys=simpleFormatter, rawFormatter [logger_root] level=DEBUG handlers=consoleHandler [logger_sls] level=INFO handlers=consoleHandler, slsHandler qualname=sls propagate=0 [handler_consoleHandler] class=StreamHandler level=DEBUG formatter=simpleFormatter args=(sys.stdout,) [handler_slsHandler] class=aliyun.log.QueuedLogHandler level=INFO formatter=rawFormatter args=(os.environ.get('ALIYUN_LOG_SAMPLE_ENDPOINT', ''), os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSID', ' '), os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSKEY', ''), os.environ.get('ALIYUN_LOG_SAMPLE_TMP_PROJECT', ''), "logstore") [formatter_simpleFormatter] format=%(asctime)s - %(name)s - %(levelname)s - %(message)s [formatter_rawFormatter] format=%(message)s
```

| Two handlers named | root | an |
|---|---|---|
| aliyun.log.QueuedLogHandler |   |   |

Two handlers named `root` and `sls` are created. The `sls` handler is an object of the `aliyun.log.QueuedLogHandler` class. The following shows the parameters that are specified for the sls handler. For more information, see Parameters.

```
args=(os.environ.get('ALIYUN_LOG_SAMPLE_ENDPOINT', ''), os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSID', ' '), os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSKEY', ''), os.environ.get('ALIYUN_LOG_SAMPLE_TMP_PROJECT', ''), "logstore")
```

> Not e In this case, the `os.environ` function is used to retrieve configurations from environment variables. You can also specify values for these parameters based on your business requirements.

Upload logs You can use the configuration file to upload logs to Log Service.

```java
import logging import logging.config
# Configurations
logging.config.fileConfig('logging.conf') logger = logging.getLogger('sls')
# Use the logger
logger.info("test1") try:
    1/0
except ZeroDivisionError as ex:
    logger.exception(ex)
```

Then, logs are automatically uploaded to Log Service. To use the LogSearch/Analytics feature, you must enable the index feature on the corresponding Logstore. Configure an index for a Logstore Enable the index feature on the Logstore that receives logs and configure an index for specific fields. We recommend that you use CLI (Command Line Interface) to configure the index as follows:

```
aliyunlog log update_index --project_name="project1" --logstore_name="logstore1" --index_detail="file: ///Users/user1/loghandler_index.json"
```

For more information, see the python_logging_handler_index.json configuration file. Specify log fields to be collected The following table lists supported log fields that you can collect. By default, all of the fields are collected.

| Field | Description |
|---|---|
| message | The contents of a log. |
| record name _ | The name of a handler. In the preceding example, the name is sls . |
| level | The output level of a logger, such as INFO and ERROR. |
| file path _ | The full path of a configuration file. |
| func name _ | The name of a function. |
| line no _ | The number of a log line. |
| module | The name of a module where the function resides. |
| thread id _ | The ID of the thread that runs the function. |
| thread name _ | The name of the thread that runs the function. |
| process id _ | The ID of the process that runs the function. |
| process name _ | The name of the process that runs the function. |

You can specify log fields to be collected based on the fields parameter of the `QueuedLogHandler` class. For more information, see aliyun.log.LogFields. The following example shows how to modify the preceding configuration file and collect several fields, such as module and func_name.

```
[handler_slsHandler] class=aliyun.log.QueuedLogHandler level=INFO formatter=rawFormatter args=('cn-beijing.log.aliyuncs.com', 'ak_id', 'ak_key', 'project1', "logstore1", 'mytopic', ['level', 'func_name', 'module', 'line_no'] )
```

> Not e

The message field is collected regardless of your configurations. To add a prefix and suffix to the names of these fields, use the `buildin_fields_prefix` and `buildin_fields` `_suffix` parameters. For example, `__level__` . Configure logging by using a JSON text You can use a JSON text to create more flexible logging configurations than code does.

```java
#encoding: utf8
import logging, logging.config, os
# Configurations
conf = {'version': 1,
        'formatters': {'rawformatter': {'class': 'logging.Formatter',
                                        'format': '%(message)s'}
```

`},`

```json
        'handlers': {'sls_handler': {'()':
                                     'aliyun.log.QueuedLogHandler',
                                     'level': 'INFO',
                                     'formatter': 'rawformatter',
                                     # custom args:
                                     'end_point': os.environ.get('ALIYUN_LOG_SAMPLE_ENDPOINT', ''),
                                     'access_key_id': os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSID', '')
```

`,`

```json
                                     'access_key': os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSKEY', ''),
                                     'project': 'project1',
                                     'log_store': "logstore1"
```

`}` `},`

```json
        'loggers': {'sls': {'handlers': ['sls_handler', ],
                                   'level': 'INFO',
                                   'propagate': False}
```

`}` `}`

```bash
logging.config.dictConfig(conf)
# Use the logger
logger = logging.getLogger('sls') logger.info("Hello world")
```

> Not e To instantiate an object of the `aliyun.log.QueuedLogHandler` class, pass named parameters to the constructor. For more information, see Parameters.

#### 3.2.3 Common log formats

##### 3.2.3.1 Log4j logs

Log Service allows you to collect Log4j logs. Collect Log4j logs by using LogHub Log4j Appender For more information, see Log4j Appender. Configure Logtail to collect Log4j logs This topic describes how to configure regular expressions based on the default configuration of Log4j 1 logs. If Log4j 2 is used, you must modify the default configuration to record the complete date information. Log4j logs are sorted into Log4j 1 logs and Log4j 2 logs.

```xml
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss:SSS zzz} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="com.foo.Bar" level="trace">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="error">
      <AppenderRef ref="Console"/>
    </Root>
  </Loggers>
</Configuration>
```

For more information about how to configure Logtail to collect Log4j logs, see Python logs. Configure the required parameters based on your network environment and business requirements. The automatically generated regular expression is based on the sample log and may not be suitable for other logs. Therefore, you must make minor changes to the regular expression after it is automatically generated The following shows a sample log of the default Log4j format.

```
2013-12-25 19:57:06,954 [10.207.37.161] WARN impl.PermanentTairDaoImpl - Fail to Read Permanent Tair,k ey:e:470217319319741_1,result:com.example.tair.Result@172e3ebc[rc=code=-1, msg=connection error or tim eout,value=,flag=0]
```

Regular expression that matches IP addresses that each indicate the start of a line:

```
\d+-\d+-\d+\s. *
```

Regular expression used to extract log information:

```
(\d+-\d+-\d+\s\d+:\d+:\d+,\d+)\s\[([^\]]*)\]\s(\S+)\s+(\S+)\s-\s(. *)
```

Time conversion format:

```
%Y-%m-%d %H:%M:%S
```

The following table lists the extraction results of the sample log.

| Key | Value |
|---|---|
| time | 2013-12-25 19:57:06,954 |

| og Service | User Guide·Data collectio |
|---|---|

| Key | Value |
|---|---|
| ip | 10.207.37.161 |
| level | WARN |
| class | impl.PermanentTairDaoImpl |
| message | Fail to Read Permanent Tair,key:e:470217319319741 1,result:com.example.tair.Result@172e3ebc[rc=code=-1, _ msg=connection error or timeout,value=,flag=0] |

##### 3.2.3.2 Python logs

The Python logging module provides a general logging system, which can be used by third-party modules or applications. The Python logging module provides different log levels and logging methods, such as file-based, HTTP GET, HTTP POST, SMTP, and Socket logging. You can also create a custom logging method. The Python logging module works in the same way as the Log4j logging module except for some implementation details. The Python logging module includes the logger, handler, filter, and formatter objects. Use log handlers to automatically upload Python logs Use log handlers to automatically parse logs that consist of key-value pairs Use log handlers to automatically parse logs in the JSON format Log format A formatter specifies the output format of logs. To instantiate a formatter, pass two parameters to the constructor. One parameter includes a message format string and the other parameter includes a date format string. The parameters are optional. Log format:

```java
import logging import logging.handlers LOG_FILE = 'tst.log' handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # Inst antiate the handler fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' formatter = logging.Formatter(fmt) # Instantiate the formatter handler.setFormatter(formatter) # Add the formatter to the handler logger = logging.getLogger('tst') # Obtain a logger named tst logger.addHandler(handler) # Add the handler to the logger logger.setLevel(logging.DEBUG) logger.info('first info message') logger.debug('first debug message')
```

Attributes Formatter attributes are specified in the %(key)s format. The following table lists the attributes.

| Format | Description |
|---|---|
| %(name)s | The name of a logger that generates logs. |
| %(levelno)s | The log output level in the numeric format. Valid values: DEBUG, INFO, WARNING, ERROR, and CRITICAL |

| User Guide·Data collection | Log Servic |
|---|---|

| Format | Description |
|---|---|
| %(levelname)s | The log output level in the text format. Valid values: 'DEBUG', 'INFO', 'WARNING', 'ERROR', and 'CRITICAL'. |
| %(pathname)s | The full path of a source file that contains the logging module. |
| %(filename)s | The name of the source file. |
| %(module)s | The name of a module where the statement that you use to generate logs resides. |
| %(funcName)s | The name of the function that is used to call the log output function. |
| %(lineno)d | The number of a code line that contains the statement used to call the log output function. |
| %(created)f | The time when the log was created. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 (UTC). |
| %(relativeCreated)d | The interval between the time when a log was created and the time when the logging module was loaded. Unit: milliseconds. |
| %(asctime)s | The time when the log was created. The value of 2003-07-08 16:49:45,896 is an example of the default format. The number after the comma (,) indicates the number of milliseconds. |
| %(msecs)d | The time when the log was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 (UTC). |
| %(thread)d | The thread ID. |
| %(threadName)s | The thread name. |
| %(process)d | The process ID. |
| %(message)s | The contents of a log. |

Sample logs Sample log:

```
2015-03-04 23:21:59,682 - log_test.py:16 - tst - first info message 2015-03-04 23:21:59,682 - log_test.py:17 - tst - first debug message
```

Common Python logs and the corresponding regular expressions: Sample log:

```
2016-02-19 11:03:13,410 - test.py:19 - tst - first debug message
```

Regular expression:

```
(\d+-\d+-\d+\s\S+)\s+-\s+([^:]+):(\d+)\s+-\s+(\w+)\s+-\s+(. *)
```

Log format

```
%(asctime)s - %(filename)s:%(lineno)s - %(levelno)s %(levelname)s %(pathname)s %(module)s %(funcNam e)s %(created)f %(thread)d %(threadName)s %(process)d %(name)s - %(message)s
```

Sample log:

```
2016-02-19 11:06:52,514 - test.py:19 - 10 DEBUG test.py test <module> 1455851212.514271 13986599668 7072 MainThread 20193 tst - first debug message
```

Regular expression:

```
(\d+-\d+-\d+\s\S+)\s-\s([^:]+):(\d+)\s+-\s+(\d+)\s+(\w+)\s+(\S+)\s+(\w+)\s+(\S+)\s+(\S+)\s+(\d+)\s+ (\w+)\s+(\d+)\s+(\w+)\s+-\s+(. *)
```

Configure Logtail to collect Python logs
1. Log on to the Log Service console.
2. Click Import Dat a. On the Import Dat a page that appears, select RegEx-T ext Log.
3. Select a destination project and Logstore, and then click Next .
You can also click Creat e Now to create a project and a Logstore. If you enter the configuration procedure by clicking the plus sign (+) next to Dat a Import under a Logstore on the Logstores tab, the system skips this step.
4. Create a machine group and click Next .
Before you can create a machine group, you must install Logtail. Install Logtail as prompted. For more information, see Install Logtail in Linux or Install Logtail in Windows. After you install Logtail, click Complet e Inst allat ion to create a machine group. If a machine group is created, click Use Exist ing Machine Groups to select the machine group.
5. Select a machine group, move the machine group from Source Machine Groups to Applied Server Groups,
and then click Next .

> Not ice If you want to apply a machine group immediately after it is created, the heartbeat status of the machine group may be FAIL. This issue occurs because no servers in the machine group are connected to Log Service. In this case, you can click Aut omat ic Ret ry.

6. Create a Logtail configuration.
i. Enter a conf igurat ion name and log pat h and select Full Regex Mode in the Mode field. ii. Turn on Singleline. iii. Enter a snippet in the Log Sample field. iv. Turn on Ext ract Field. v. Set a regular expression in the RegEx field. a. Select fields to generate a regular expression If the regular expression that is automatically generated does not match your sample log, you can select fields in the sample log to generate a regular expression. Log Service can automatically parse the highlighted fields of the sample log to generate a regular expression. In the Log Sample field, select the required fields, and click Generat e Regular Expression. The regular expression of the selected field is displayed in the RegEx field. To obtain a full regular expression for the sample log, generate regular expressions for each log field. b. Modify the regular expression Actual data formats may vary. In this case, click Manual under the RegEx field to adjust the regular expression that is automatically generated based on your business requirements. This ensures that the regular expression is suitable for all formats of the collected logs. c. Verify the regular expression After you modify the regular expression, click Validat e next to the RegEx field. If the regular expression is valid, the extraction results are displayed. If the regular expression is invalid, modify the regular expression again. vi. Confirm t he ext ract ion result s of log f ields. View the extraction results of log fields and specify keys for the extracted fields. Specify an informative name for each log field in the extraction results. For example, time as the name for a time field. If you do not use the system time, you must specify the name of a time field in the Value fields and time in the Key field.
7. (Optional)Specify Advanced Opt ions and click Next .
Set the parameters in the Advanced Options section based on your business requirements. We recommend that you do not modify the settings. The following table describes the parameters in the Advanced Options section.

| Parameter | Description |
|---|---|
| Enable Plug-in Processing | Specifies whether to enable plug-in processing. If you turn on this switch, you can use the plug-in of Logtail to process text logs. Not e If you turn on Enable Plug-in Processing, specific parameters such as Upload Raw Log, Timezone, Drop Failed to Parse Logs, Filter Configuration, and Incomplete Entry Upload (Delimiter mode) become unavailable. |
| Upload Raw Log | If you turn on Upload Raw Log, each raw log is uploaded to Log Service as a value of the raw field together with the parsed log. __ __ |
| Topic Generation Mode | The topic generation mode. Null - Do not generat e t opic: This mode is selected by default. In this mode, the topic field is set to an empty string. You do not need to enter a topic to query logs. Machine Group T opic At t ribut es: This mode is used to differentiate logs that are generated by different servers. File Pat h RegEx: In this mode, you must specify a regular expression in the Cust om RegEx field. The part of a log path that matches the regular expression is used as the topic. This mode is used to differentiate logs that are generated by different users or instances. |
| Custom RegEx | If you set the Topic Generation Mode parameter to File Pat h RegEx, you must enter a custom regular expression. |

| Parameter | Description |
|---|---|
| Log File Encoding | The encoding format of log files. Valid values: utf8: UTF-8 encoding format gbk: GBK encoding format |
| Timezone | The time zone where logs are collected. Valid values: System Timezone: This option is selected by default. It indicates that the time zone where logs are collected is the same as the time zone to which the server belongs. Custom: If you select this value, you must select a time zone. |
| Timeout | The timeout period of log files. If a log file is not updated within the specified period, Logtail reckons the file to be timed out. Valid values: Never: All log files are continuously monitored and never time out. 30 Minute Timeout: If a log file is not updated within 30 minutes, Logtail considers the log file to be timed out and no longer monitors the file. If you select 30 Minut e T imeout , you must specify the Maximum T imeout Direct ory Dept h parameter. Valid values: 1 to 3. |
| Filter Configuration | Only logs that meet all f ilt er condit ions are collected. Examples: Collect logs that meet specified conditions: If you set Key to level and Regex to WARNING\|ERROR, only WARNING-level and ERROR-level logs are collected. Filter out logs that do not meet specified conditions. If you set Key to level and Regex to ^(?!.*(INFO\|DEBUG)).*, INFO-level or DEBUG-level logs are not collected. If you set Key to url and Regex to .*^(?!.*(healt hcheck)).*, logs whose URLs contain healthcheck are not collected. For example, the log is not collected if the value of the Key field is url and the value of the Value field is /inner/healthcheck/jiankong.html. |

8. Configure indexes in the Configure Query and Analysis step. Click Next .
By default, Log Service enables Full Text Index to query and analyze logs. You can manually or automatically configure Field Search. For more information, see Enable the index feature and configure indexes for a Logstore.

> Not e
> To query and analyze logs, you must enable Full Text Index or Field Search. If you enable both Full Text Index and Field Search, the settings of Field Search prevail.
> If the data type of the index is long or double, the Case-Sensitive switch and the Delimiter field are unavailable.

After the configuration is complete, apply the settings to the server group to collect Python logs.

##### 3.2.3.3 Node.js logs

Node.js logs are displayed in the Log Service console by default. This impedes data collection and troubleshooting. You can use the log4js function to write logs into files and customize the log format. This facilitates data collection and consolidation. Example:

```
var log4js = require('log4js'); log4js.configure({
  appenders: [
```

`{`

```
      type: 'file', //Output to a file
      filename: 'logs/access.log',
      maxLogSize: 1024,
      backups:3,
      category: 'normal'
```

`}` `]`

```
}); var logger = log4js.getLogger('normal'); logger.setLevel('INFO'); logger.info("this is a info msg"); logger.error("this is a err msg");
```

Log format After logs are written to text files by using the log4js function, these logs are displayed in the following format:

```
[2016-02-24 17:42:38.946] [INFO] normal - this is a info msg [2016-02-24 17:42:38.951] [ERROR] normal - this is a err msg
```

The log4js function defines six log severity levels. They are TRACE, DEBUG, INFO, WARN, ERROR, and FATAL in ascending order of severity. Use Logtail to collect Node.js logs For more information about how to configure Logtail to collect Python logs, see Python logs. Use configurations based on your network environment and business requirements. The automatically generated regular expression is based on the sample log and may not apply to other logs. Therefore, you must make minor changes to the regular expression after it is generated. You can use the following sample Node.js logs to configure appropriate regular expressions for your logs. Sample Node.js logs: Example 1 Sample log

```
[2016-02-24 17:42:38.946] [INFO] normal - this is a info msg
```

Regular expression:

```
\[([^]]+)]\s\[([^\]]+)]\s(\w+)\s-(. *)
```

Extracted fields: `time` , `level` , `loggerName` , and `message` Example 2 Sample log

```
[2016-01-31 12:02:25.844] [INFO] access - 42.120.73.203 - - "GET /user/projects/ali_sls_log? igno reError=true HTTP/1.1" 304 - "http:// aliyun.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gec ko) Chrome/48.0.2564.97 Safari/537.36"
```

Regular expression:

```
\[([^]]+)]\s\[(\w+)]\s(\w+)\s-\s(\S+)\s-\s-\s"([^"]+)"\s(\d+)[^"]+("[^"]+)"\s"([^"]+). *
```

Extracted fields: `time` , `level` , `loggerName` , `ip` , `request` , `status` , `referer` , and `user_agent`

##### 3.2.3.4 WordPress logs

This topic describes the format of WordPress logs and extraction results of a sample log. Log format Sample log:

```
172.64.0.2 - - [07/Jan/2016:21:06:39 +0800] "GET /wp-admin/js/password-strength-meter.min.js? ver=4.4 HTTP/1.0" 200 776 "http://wordpress.c4a1a0aecdb1943169555231dcc4adfb7.cn-hangzhou.alicontainer.com/wpadmin/install.php" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Ge cko) Chrome/47.0.2526.106 Safari/537.36"
```

Configure Logtail to collect WordPress logs Configurations required to collect WordPress logs: Regular expression that matches IP addresses that each indicate the start of a line

```
\d+\.\d+\.\d+\.\d+\s-\s. *
```

Regular expression used to extract information from the log:

```
(\S+) - - \[([^\]]*)] "(\S+) ([^"]+)" (\S+) (\S+) "([^"]+)" "([^"]+)"
```

Time conversion format:

```
%d/%b/%Y:%H:%M:%S
```

Results after Logtail extracts information from the sample log

| Key | Value |
|---|---|
| ip | 10.10.10.1 |
| time | 07/Jan/2016:21:06:39 +0800 |
| method | GET |
| url | /wp-admin/js/password-strength-meter.min.js? ver=4.4 HTTP/1.0 |
| status | 200 |
| length | 776 |
| ref | http://wordpress.c4a1a0aecdb1943169555231dcc4adfb7.cn- hangzhou.alicontainer.com/wp-admin/install.php |
| user-agent | Mozilla/5.0 (Macintosh; Intel Mac OS X 10 10 5) AppleWebKit/537.36 (KHTML, _ _ like Gecko) Chrome/47.0.2526.106 Safari/537.36 |

##### 3.2.3.5 Unity3D logs

Log Service can use the WebTracking feature to collect Unity3D logs. The following example shows how to collect Unity logs of the debug type. Context Unity3D is a cross-platform game engine developed by Unity Technologies. The engine allows you to create 3D video games, VR buildings, real-time 3D animation, and other interactive content.
1. Enable the WebTracking feature.
For more information about how to enable this feature, see WebTracking.
2. Create a Unity3D LogHandler.
In a Unity editor, create a C# file named LogOutputHandler.cs, add the following code, and modify the following variables. project: specifies the name of the project. logstore: specifies the name of the Logstore. serviceAddr: specifies the endpoint of the project. For more information about serviceAddr, see View the information of a project.

```java
using UnityEngine; using System.Collections; public class LogOutputHandler : MonoBehaviour
```

`{`

```
    //Register the HandleLog function on scene start to fire on debug.log events
    public void OnEnable()
```

`{`

```
        Application.logMessageReceived += HandleLog;
```

`}`

```
    //Remove callback when object goes out of scope
    public void OnDisable()
```

`{`

```
        Application.logMessageReceived -= HandleLog;
```

`}`

```
    string project = "your project name";
    string logstore = "your logstore name";
    string serviceAddr = "http address of your log service project";
    //Capture debug.log output, send logs to Loggly
    public void HandleLog(string logString, string stackTrace, LogType type)
```

`{`

```
        string parameters = "";
        parameters += "Level=" + WWW.EscapeURL(type.ToString());
        parameters += "&";
        parameters += "Message=" + WWW.EscapeURL(logString);
        parameters += "&";
        parameters += "Stack_Trace=" + WWW.EscapeURL(stackTrace);
        parameters += "&";
        //Add any User, Game, or Device MetaData that would be useful to finding issues later
        parameters += "Device_Model=" + WWW.EscapeURL(SystemInfo.deviceModel);
        string url = "http://" + project + "." + serviceAddr + "/logstores/" + logstore + "/track?
APIVersion=0.6.0&" + parameters;
        StartCoroutine(SendData(url));
```

`}`

```
    public IEnumerator SendData(string url)
```

`{`

```
        WWW sendLog = new WWW(url);
        yield return sendLog;
```

`}` `}` The preceding code allows you to send logs to Log Service in an asynchronous manner. In the code, you can specify more fields you want to collect.
3. Generate Unity logs.
In the project, create a C# file named LogglyTest.cs and add the following code.

```java
using UnityEngine; using System.Collections.Generic; public class LogglyTest : MonoBehaviour {
    void Start () {
        Debug.Log ("Hello world");
```

`}` `}`
4. View logs in the console.
After you complete the preceding steps, run the Unity application. In the Log Service console, view logs that are sent to Log Service. The preceding code shows how to use Debug.Log, Debug.LogError, and Debug.LogException methods to collect logs. Unity provides Component Object Model (COM)-based exception handling and log handling APIs. These APIs allow you to easily collect device details of clients.

## 4 Query and analysis

### 4.1 Overview

Log Service provides the LogSearch/Analytics feature that you can use to query and analyze a large number of logs. If you do not enable indexes, raw data is consumed in sequence based on shards. The procedure is similar to the sequential consumption of Kafka messages. If you enable indexes, you can query logs and perform statistical analysis on query results in addition to consuming logs in sequence. Benefits Real-time: Logs can be analyzed immediately after they are written. Fast: Query: Billions of data records can be processed and queried within one second. Each search statement has a maximum of five conditions specified. Analysis: Hundreds of millions of data records can be aggregated and analyzed within one second. Each query has a maximum of five aggregate functions and a GROUP BY clause specified. Flexible: Query and analysis conditions can be changed as required and the results are returned in real time. All-in-one: Reports and dashboards are available in the console for quick analysis. In addition to these features, Log Service can work together with Grafana, DataV, Jaeger, and other services. It also supports RESTful APIs, Java Database Connectivity (JDBC) APIs, and other APIs. Indexing Indexes refer to a data structure that you can use to sort the values of one or more columns of logs. Indexes allow you to obtain the required information in a timely manner from logs that Log Service collects. Before you use the LogSearch/Analytics feature, you must collect logs and Enable the index feature and configure indexes for a Logstore on the collected logs. In Log Service, indexes are sorted into f ull-t ext indexes and f ield-specif ic indexes. Full-t ext index: Indexing is enabled for the full contents of a log. The values of all fields in a log are queried by default. The log can be queried if one of the fields matches the search term. Field-specif ic index: You can configure a field-specific index for a key. Then, you can query logs based on specific keys to narrow the query scope. To use f ield-specif ic indexes, you must specify the data type for a field. Available data types for fields in Log Service include Text, JSON, Long, and Double. For more information about Overview. Query methods Console In the Log Service console, you can query logs by specifying time ranges and search statements. For more information about the procedure and search statements, see Query logs and Query syntax. API To query logs, you can call the GetLogs and GetHistograms API operations of the Log Service API. Not e Before you query logs, make sure that you collect logs and Enable the index feature and configure indexes for a Logstore. Search and analysis statements To apply real-time LogSearch/Analytics to collected logs, you must specify query statements. Each query statement includes the search section and the analytics section. Separate the sections with a vertical bar ( | ).

```
$Search |$Analytics
```

| Statement | Required | Description |
|---|---|---|
| Search | No | A search statement contains search conditions. These conditions include keywords, fuzzy keywords, values, ranges, and combined conditions. If you leave the statement empty or specify an asterisk (*) for the statement, it indicates that no condition is specified and all data is returned. For more information, see Query syntax. |
| Analytics | No | You can use an analytics statement to aggregate or analyze data based on query results. If you leave the statement empty, it indicates that no analytics is required and all query results are returned. For more information, see Real-time analysis. |

Precautions You may query a large number of logs. For example, if the number of logs to be queried is more than 1,000,000,000, Log Service may fail to return all results. Log Service returns a partial result set and notifies you that the returned data set includes partial results. Query results are cached every 15 minutes. If a partial result set is matched in the cache, Log Service continues to scan logs that are not cached. Log Service combines query results of the current query with results of cached results. Therefore, Log Service enables you to obtain results by calling the API operation multiple times with the same parameters.

### 4.2 Real-time analysis

Log Service supports SQL-like aggregate calculation. This feature integrates search statements with SQL aggregate functions to calculate query results. Sample statement:

```
status>200 |select avg(latency),max(latency) ,count(1) as c GROUP BY method ORDER BY c DESC LIMIT 2
```

Basic syntax:

```
[search query] | [sql query]
```

Separate a search statement and a calculation statement with a vertical bar ( | ). You can use the search statement to query logs and obtain the required results. Then, use the calculation statement for further aggregation. The search query syntax is specific to Log Service. For more information, see Query syntax. Prerequisites To use the statistical analysis feature, click Index At t ribut es. Turn on the Enable Analyt ics switch for the required field. For more information, see Enable the index feature and configure indexes for a Logstore. If you turn off the switch, Log Service calculates up to 10,000 rows of data in each shard along with high latency of calculation. If you turn on the switch, Log Service analyzes data in seconds. The update applies only to new data. No extra fee is incurred for the update. Supported SQL syntax Log Service supports the following SQL syntax. For more information about a specific topic, click the corresponding link. Aggregate functions that are available for SELECT statements include: Interval-valued comparison and periodicity-valued comparison functions Machine learning functions Precautions Before you use SQL statements, note the following items: You do not need to specify FROM and WHERE clauses for SQL statements. By default, Log Service queries logs from the current Logstore, and each WHERE clause is specified in the [search query] section. The supported clauses include SELECT, GROUP BY, ORDER BY [ASC,DESC], LIMIT, and HAVING.

> Not e By default, only the first 10 results are returned. If you want to return more results, add a LIMIT clause to the statement. For example, * | select count(1) as c, ip group by ip order by c desc limit
> `100` .

Built-in fields Log Service has multiple built-in fields for statistical analysis. A built-in field is automatically added to a valid column that you create.

| Field | Type | Description |
|---|---|---|
| time __ __ | Bigint | The time when a log was created. |
| source __ __ | Varchar | The source IP address of a log. When you query logs, the name of the field is source. If you specify the field for an SQL statement, you must add two underscores ( ) at both the start and _ end of source. |
| topic __ __ | Varchar | The topic of a log. |

Maximum number of Logstores from which you can query logs at the same time is 15. Maximum length for a field value of the varchar type is 2,048. Extra data will be truncated. By default, up to 100 lines of a log file are returned and pagination is not supported. If you want to return more lines, use LIMIT syntax. Example Calculate the hourly PV and UV, and the user request of the highest latency.

```
*|select date_trunc('hour',from_unixtime(__time__)) as time,
     count(1) as pv,
     approx_distinct(userid)  as uv,
     max_by(url,latency) as top_latency_url,
     max(latency,10) as top_10_latency
     group by  1
     order by time
```

### 4.3 Enable the indexing feature and configure indexes for a Logstore

configure indexes for a Logstore This topic describes how to enable the indexing feature and configure indexes for a Logstore. Context Before you can query logs that are stored in a Logstore, you must enable the indexing feature and configure indexes for the Logstore. We recommend that you configure indexes for your Logstores based on your business requirements.

> Not e After you enable the indexing feature, the indexes occupy extra storage space and transferring the indexes occupies extra bandwidth.

When you collect a log entry, Log Service adds the relevant information (such as the source and time fields) to the log entry as key-value pairs. These fields are reserved in Log Service. If you enable the indexing feature for a Logstore and configure indexes for fields in the Logstore, the indexing and analytics features are automatically enabled for these fields. Reserved fields in Log Service

| Field | Description |
|---|---|
| topic __ __ | The topic of a log entry. If you specify a topic for a log entry, Log Service adds the topic field to the log entry. The key of the field is topic and the value __ __ of the field is the log topic. For more information, see Specify a log topic . |
| source __ __ | The source of a log entry. The source device that generates the log entry. |
| time __ __ | The time when a log entry is written to the Logstore by using an SDK. |

|   | topic |
|---|---|

> Not e If the values of the `__topic__` and `__source__` fields are null, the keywords that you use to query the two fields must exactly match the field values.

1. Log on to the Log Service console.
2. In the Projects section, click the target project.
3. Find the target Logstore, and choose
> Search & Analysis.

4. On the page that appears, click Enable in the upper-right corner.

> Not e If you have created indexes for the Logstore, choose Index At t ribut es > Modif y to modify the indexes.

5. Configure the indexes.

> Not e If you enable a full-text index and a field-specific index at the same time, the field-specific index takes precedence over the full-text index.

Index types

| Index type | Description |
|---|---|
| Full text index | An index is created in the text format for all fields. You can search for key-value pairs that are included in these fields. For fields of the LONG type, you must specify the key name of a field when you query a value of the field. For fields of the other types, you do not need to specify a key name in queries. |
| Field-specific index | After you configure a field-specific index, you must specify the name of a key when you query logs. If you configure the field-specific index on a field, the field-specific index takes effect when you query logs. The full-text index does not take effect. Available data types that you can specify for fields include: Query text data JSON indexes Numeric (LONG and DOUBLE) |

Configure a full-text index. After you configure a full-text index for a Logstore, the values of all fields in the Logstore are queried by default.

| Parameter | Description | Example value |   |   |
|---|---|---|---|---|
| Full Text Index | If you turn on the switch, Log Service traverses the values of all fields in a log entry. If the value of one of the fields matches the keyword, the log entry is returned. | - |   |   |
| Case Sensitive | Specifies whether queries are case-sensitive. If you turn off the switch, queries are not case- sensitive. For example, if you search for internalError, you can use either INTERNALERROR or internalerror as the keyword. If you turn on the switch, queries are case-sensitive. For example, if you search for internalError, you can use only internalError as the keyword. | - |   |   |
| Include Chinese | Specifies whether to differentiate the Chinese content and English content. If you turn on the switch, Log Service separates the Chinese content based on the Chinese semantics and English content based on the specified delimiters. If you turn off the switch, the content of a log entry is separated by the specified delimiters. | - |   |   |
| Delimiter | The delimiters that you use to separate the content of a log entry into multiple keywords. For example, the content of a log entry is a,b;c;D-F . You can specify commas (,), semicolons (;), and hyphens (-) as delimiters to delimit the log content. Then you can use the five letters a, b, c, D, and F as keywords to match the log entry. | , '";=()[]{}? @&<>/ :\n\t |   |   |
|   |   |   | , '";=()[]{}? @&<>/ |   |

Configure a field-specific index. You can specify fields to be indexed. Field-specific indexes allow you to query log data based on the values of specific fields. This narrows down the query scope.

| Parameter | Description | Example value |
|---|---|---|

| Parameter | Description | Example value |
|---|---|---|
| Key Name | The name of a log field. Not e If you want to configure an index for fields of the tag type, such as fields that include public IP addresses or UNIX timestamps, you must set the value of the Key Name parameter in the tag :key format, __ __ for example, tag : receive time __ __ __ _ _ . _ Indexes of the numeric types are unavailable for tag fields. You must select text in the T ype field for all tag fields. | address _ _ |
| Type | The type of a field. Valid values: t ext : The data type of the field is TEXT. long: The data type of the field is LONG. You must specify a numeric range to query log data. double: The data type of the field is DOUBLE. You must specify a numeric range to query log data. json: The data type of the field is JSON. Not e The Case Sensit ive, Include Chinese, and Delimit er parameters are unavailable for fields of numeric types (LONG and DOUBLE). | - |
| Alias | The alias of a column. Aliases are applied only to SQL statistics. Original names are applied when you store and query log data in Log Service. For more information, see Field aliases. | address |
| Case Sensitive | Specifies whether queries are case-sensitive. If you turn off the switch, queries are not case- sensitive. For example, if you search for internalError, you can use either INTERNALERROR or internalerror as the keyword. If you turn on the switch, queries are case-sensitive. For example, if you search for internalError, you can use only internalError as the keyword. | - |

| tag : receive time __ __ __ _ _ |   |
|---|---|

|   |   | _ |
|---|---|---|

| Parameter | Description | Example value |   |   |
|---|---|---|---|---|
| Delimiter | The delimiters that you use to separate the content of a log entry into multiple keywords. For example, the content of a log entry is a,b;c;D-F . You can specify commas (,), semicolons (;), and hyphens (-) as delimiters to delimit the log content. Then you can use the five letters a, b, c, D, and F as keywords to match the log entry. | , '";=()[]{}? @&<>/ :\n\t |   |   |
|   |   |   | , '";=()[]{}? @&<>/ |   |
| Include Chinese | Specifies whether to differentiate the Chinese content and English content. If you turn on the switch, Log Service separates the Chinese content based on the Chinese semantics and English content based on the specified delimiters. If you turn off the switch, the content of a log entry is separated by the specified delimiters. | - |   |   |
| Enable Analytics | Specifies whether to enable the analytics feature. The switch is turned on by default. After you turn on the switch, you can use search and analytic statements to obtain statistical results. | - |   |   |

6. Click OK.

> Not e
> The index configurations take effect within one minute.
> After an index is enabled or modified, the updates on the index apply only to new data that is written to Log Service.

### 4.4 Query logs

This topic describes how to query logs in a Logstore. After you enable and configure the index of the Logstore, you can query and analyze logs in a Logstore in real time. Prerequisites Logs are collected and stored in a Logstore. Indexes are enabled and configured. For more information, see Enable the index feature and configure indexes for a Logstore.
1. Log on to the Log Service console.
2. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
3. Enter a query statement in the search box.
A query statement consists of a search statement and an analytic statement. The syntax is `search statement`
|analytic statement . For more information, see Search and analysis statements.
4. On the Search & Analysis page, select 15 Minut es in the Relative section to set the time range for the query.
You can select a relative time, time frame, or a custom time range.

> Not e The query results may contain logs that are generated 1 minute earlier or later than the specified time period.

5. Click Query & Analyze to view the query results.
Log Service illustrates query results on log distribution histograms, Raw Logs tab, or statistical graphs. Not e 100 results are returned by default. For information about how to retrieve more results, see LIMIT syntax. Log distribution histogram The log distribution histogram shows the distribution of query results across different time ranges. Move the pointer over a green block to view a time range and the number of logs obtained within the time range. Click a data block to view finer-grained log distribution. You can also view the query results on the Raw Logs tab. Raw Logs tab On the Raw Logs tab, view logs that match your search conditions. Quick analysis: Use this feature to analyze the distribution of values for a specific field within a period of time. For more information, see Quick analysis. Log download: Click the download icon in the upper-right corner of the tab, select a time range, and then click OK. Column settings: Click Column Set t ings in the upper-right corner of the tab, select the required fields and click Add to add the fields. Then, the columns that correspond to the fields appear on the tab. The field names are also column names. The columns list the field values.

> Not e To view the log contents on the tab, select Cont ent .

Content column settings: If the content of a field exceeds 3,000 characters, extra characters will be hidden. In this case, the message "The character string is too long and has been truncated" will be displayed before the Key field. Click Display Cont ent Column. In the dialog box that appears, set the Key-Value Arrangement and T runcat e Charact er St ring parameters.

> Not e If the content limit is set to 10,000 characters, no delimiter will be specified for extra characters.

| Parameter |   | Description |
|---|---|---|
| Key-Value Pair Arrangement |   | You can set this parameter to New Line or Full Line. |
| T runcat e Charact er St ring | Key | If a field value contains more than 3,000 characters, the field value is truncated. However, this parameter remains unspecified if no field value exceeds 3,000 characters. The value of this parameter is the key of the truncated value. |
|   | St at us | This parameter determines whether to enable the value truncation feature. By default, the feature is enabled. Enable: If the value in a key-value pair exceeds the specified T runcat e St ep, extra characters will be truncated. You can click the Show button at the end of the value to show the truncated characters. The increment per click is the specified truncate step. Disable: If the value in the key-value pair exceeds the specified T runcat e St ep, extra characters will not be truncated. |
|   | T runcat e St ep | This parameter specifies the maximum number of characters that a field value shows by default. The parameter also specifies the number of extra characters that you displayed each time you click the Show button. Valid values: 500 to 10000. Default value: 3000. |

Graph If you enable the Analytics feature on the Search & Analysis page and use search and analytic statements to query logs, you can view the analytical results on the Graph tab. Graphs of multiple types are provided in Log Service, including tables, line charts, and bar charts. You can select a graph to show the required analytical results. For more information, see Graphs. Log Service allows you to create dashboards for real-time data analysis. For more information, see Create and delete a dashboard. Click Add t o New Dashboard to save a common chart as query statements to a dashboard. Drill-down analysis allows you to move to deeper data layers, which reveals more detailed information. You can set the drill-down parameters and add the chart to the dashboard. Then, you can click the values in the chart to view the analysis results from more dimensions. For more information, see Drill-down analysis. You can also click Save Search or Save as Alarm on the Search & Analysis page to use the saved search and alarm features. For more information, see Save a query statement as a search and Configure an alert.

### 4.5 Export logs

You can export logs on the current page to a CSV file and save the file to your localhost.
1. Log on to the Log Service console.
2. Click a project name.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
4. Click the
icon next to the Raw Logs tab.
5. In the Download Log dialog box, select Download Log in Current Page.
6. Click OK to export logs of the current page to a .CSV file and save the file to the localhost.

### 4.6 Index data type

#### 4.6.1 Overview

Log Service allows you to use full-text indexes or field-specific indexes to query collected logs. If you set a fulltext index for a log, the value is the entire log. If you set a field-specific index for a log, you can specify a data type for each key. Date types The following table lists the supported data types.

|   | Query type | Data type (index) | Description |   | Example |   |   |
|---|---|---|---|---|---|---|---|
|   | Basic query | Text | The text type. You can use keywords and fuzzy matches to query logs. |   | uri:"login*" method:"post" |   |   |
|   |   | Long | The numeric type. You can specify numeric ranges to query logs. |   | status>200 and status in [200, 500] |   |   |
|   |   |   |   |   |   | status>200 and status in |   |
|   |   |   |   | ges to query logs. | [200, 500] |   |   |
|   |   | Double | The floating-point type. |   | price>28.95 and t in [20.0, 37] |   |   |
| 2 | 00 |   |   |   |   |   |   |

|   |   | price>28.95 and t in [20.0, |
|---|---|---|
| ating-point type. | 37] |   |

|   | og Service |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   | Query type | Data type (index) | Description |   | Example |   |   |
|   | Combined query | JSON | Indicates that the index is a JSON field that supports nested queries. By default, the data type of the field is text. You can set indexes of the Text, Long, and Double types for the b elements at layer a in the a.b path format. The fields adopt the configured types. |   | level0.key>29.95 level0.key2:"action" |   |   |
|   |   |   |   |   |   | level0.key>29.95 |   |
|   |   |   |   | es for the b | level0.key2:"action" |   |   |
|   |   | Text | Indicates that the full contents of the log are queried as text. |   | error and "login fail" |   |   |

Query examples The following table lists the keys included in the sample log.

| No. | Key | Type |
|---|---|---|
| 0 | time | N/A |
| 1 | class | text |
| 2 | status | long |
| 3 | latency | double |
| 4 | message | json |

```
0. time:2018-01-01 12:00:00
  1. class:central-log
  2. status:200
  3. latency:68.75
  4. message:
```

`{`

```json
      "methodName": "getProjectInfo",
      "success": true,
      "remoteAddress": "1.1.1.1:11111",
      "usedTime": 48,
      "param": {
              "projectName": "ali-log-test-project",
              "requestId": "d3f0c96a-51b0-4166-a850-f4175dde7323"
```

`},`

```json
      "result": {
          "message": "successful",
          "code": "200",
          "data": {
              "clusterRegion": "ap-southeast-1",
              "ProjectName": "ali-log-test-project",
              "CreateTime": "2017-06-08 20:22:41"
```

`},`

```json
          "success": true
```

`}` `}` You can set an index as follows. Set an index In the preceding figure, ① specifies that Log Service can query data of the string and Boolean types in JSON fields. ② specifies that Log Service can query data of the long type. ③ enables SQL analysis for specified fields. Example
1. Query data of the string and Boolean types
You do not need to configure JSON fields. JSON maps and arrays are automatically expanded and can contain nested fields. Separate multiple levels

| with periods ( | . | ). . |
|---|---|---|
| class : cental* message.traceInfo.requestId : 92.137 1518139699935 5599 _ _ message.param.projectName : ali-log-test-project message.success : true |   |   |

2. Query data of the double and long types
Each JSON field must be specified separately and cannot be contained in a JSON array.

```
latency>40 message.usedTime > 40
```

3. Combined query

```
class : cental* and message.usedTime > 40 not message.param.projectName:ali-log-test-project
```

#### 4.6.2 Query text data

This topic describes how to query text data. Similar to search engines, Log Service queries text data based on terms. Therefore, you must set the Delimiter, Case Sensitive fields. Configurations Case sensitivity You can specify whether log queries are case-sensitive. For example, you want to query logs by using a search term named `internalError` . false specifies a case-insensitive query. Both `INTERNALERROR` and `internalerror` can be the keywords. true specifies a case-sensitive query. Only the `internalError` can be the keyword. Delimiter You can use delimiters to split a search term into multiple keywords. For example, you want to query logs by using the following search term.

```
/url/pic/abc.gif
```

| /url/pic/abc.gif |   | string |
|---|---|---|
| string named | /url/pic/* |   |

If the delimiter is set to `/` , the search term is split into three words: `url` , `pic` , and `abc.gif` . You can use one of these words or a fuzzy word to query logs. For example, `url` , `abc.gif` , or `pi*` . You can also use the `/url/pic/abc.gif` string as a search term to query logs. However, the search term is split into three keywords named `url, pic, and abc.gif` . If the delimiter is set to `/.` , the search term is split into four keywords named `url` , `pic` , `abc` , and `gif` .

> Not e You can extend query ranges by setting appropriate delimiters.

Full-text index By default, full-text indexes treat each log except for the time field as text data. You do not need to specify any keys for a full-text index. For example, the following log includes the time field, status field, level field, and message field.

```
[20180102 12:00:00] 200,error,some thing is error in this field
 time:2018-01-02 12:00:00
 level:"error"
 status:200
 message:”some thing is error in this field”
```

> Not e
> Prefixes are not required for full-text indexes. If you set the search term to error, the level and message fields that include error match the search term.
> You must set delimiters for full-text indexes. For example, if you set a space () as a delimiter, the
> `status:200` string is a search term. If you set a colon ( `:` ) as a delimiter, the search term is split into two keywords named `status` and `200` .
> Numbers are treated as text data. For example, you can use 200 to query logs. Values in the time field are not treated as text data.
> You can query logs by using keys such as `status` .

#### 4.6.3 Numeric type

When you configure indexes, you can set the data type of a key to number. To query logs, you can specify a numeric range for the key. Configurations Supported types: `long` (long integers) and `double` (decimals). After you set the data type of a key to number, you must specify a numeric range for the key to query logs. Query examples To specify a numeric range from 1000 to 2000 (excluding 1000) for a key of the long type, you can use the following methods: Query syntax for numbers. For example:

```
  longKey > 1000 and longKey <= 2000
```

Query grammar for numeric ranges. For example:

```
  longKey in (1000 2000]
```

For more information about query syntax, see Query syntax.

#### 4.6.4 JSON indexes

Log Service can query and analyze logs in the JSON format. You can set the data type of indexes to JSON. JSON texts include data of multiple types, including string, Boolean, number, array, and map. JSON-formatted data is self-parsed and flexible. You can use JSON-formatted data in various scenarios. In most cases, variable log fields are recorded in the JSON format. For example, HTTP request and response parameters are recorded in a log in the JSON format. Log Service allows you to set the data type of index fields to JSON so that you can query and analyze logs in the JSON format. Configurations Log Service can parse JSON-formatted fields and generate indexes for all the fields of the text and Boolean types.

```
json_string.key_map.key_text : test_value json_string.key_map.key_bool : true
```

To query fields of the double or long type that is not in a JSON array, you can specify a JSON path.

```
Set the data type of the key_map.key_long field to long. Search condition: json_string.key_map.key_long > 50
```

To query fields of the text, double, or long type that is not in a JSON array, you can enable the Analytics feature and use SQL statements to analyze these fields.

```
json_string.key_map.key_long > 10 | select count(*) as c ,
    "json_string.key_map.key_text" group by
    "json_string.key_map.key_text"
```

> Not e
> JSON objects and JSON arrays are not supported.
> Fields cannot be contained in JSON arrays.
> Fields of the Boolean type can be converted into the text type.
> To query and analyze logs, JSON-formatted fields must be enclosed with double quotation marks (" ").

Log Service cannot parse invalid JSON-formatted data. Log Service does not stop parsing logs until it detects an invalid field. In the following example, data after the key_3 field is truncated and lost in the following text. Log Service can parse the json_string.key_map.key_2 field and the contents before this field.

```json
"json_string":
```

`{`

```json
     "key_1" :  "value_1",
     "key_map" :
```

`{`

```json
             "key_2" : "value_2",
             "key_3" : "valu
```

Query syntax To query a specific key, you must add the JSON parent path to the query statement as the prefix of the key. The query syntax for the fields of the text and numeric types is the same for both JSON-formatted data and other data. For more information, see Query syntax. Query example The following table lists the keys included in the sample log. The data type of the `message` key is JSON.

| Number | Key | Type |
|---|---|---|
| 0 | time | N/A |
| 1 | class | text |
| 2 | status | long |
| 3 | latency | double |
| 4 | message | json |

```
0. time:2018-01-01 12:00:00
  1. class:central-log
  2. status:200
  3. latency:68.75
  4. message:
```

`{`

```json
      "methodName": "getProjectInfo",
      "success": true,
      "remoteAddress": "1.1.1.1:11111",
      "usedTime": 48,
      "param": {
              "projectName": "ali-log-test-project",
              "requestId": "d3f0c96a-51b0-4166-a850-f4175dde7323"
```

`},`

```json
      "result": {
          "message": "successful",
          "code": "200",
          "data": {
              "clusterRegion": "ap-southeast-1",
              "ProjectName": "ali-log-test-project",
              "CreateTime": "2017-06-08 20:22:41"
```

`},`

```json
          "success": true
```

`}` `}` You can set indexes for the log as follows: Set an index In the preceding figure: ① specifies that Log Service can query data of the string and Boolean types in JSON fields. ② specifies that Log Service can query data of the long type. ③ enables SQL analysis for specified fields. Examples
1. Query data of the string and Boolean types

> Not e
> You do not need to configure JSON fields.
> JSON maps and arrays are automatically expanded and can include hierarchical levels. Separate multiple levels with periods ( `.` ) .

```
message.traceInfo.requestId : 92.137_1518139699935_5599 message.param.projectName : ali-log-test-project message.success : true message.result.data.ProjectStatus : Normal
```

2. Query fields of the double and long types

> Not e Each JSON field must be configured and cannot be contained in an array.

```
message.usedTime > 40
```

3. Use SQL statements to analyze fields

> Not e
> Each JSON field must be configured and cannot be contained in an array.
> Each field to be queried must be enclosed with double quotation marks (" ") or be configured with an alias.

```
* | select avg("message.usedTime") as avg_time ,
"message.methodName" group by "message.methodName"
```

### 4.7 Query syntax and functions

#### 4.7.1 Search syntax

This topic describes the search syntax that is used in Log Service. Search types After you enable and configure the index feature of a Logstore, you can enter a search statement on the search and analysis page to query logs. A query statement consists of two sub-statements in sequence: a search statement and an analytic statement. A search statement specifies one or more search conditions and returns the log entries that match the search conditions. You can execute a search statement to perform a full-text search or field-specific search. Full-text search During full-text search, a log entry is considered a key-value pair. The value in the key-value pair indicates the content of the log entry. A full-text search statement returns the log entries that include or exclude the specified keywords. Full-text search is divided into basic full-text search, phrase search, and wildcard-based search. Basic full-text search: You can specify keywords and operators in search conditions of a search statement. You can then execute the search statement to query the log entries that match the search conditions. For example, the `a and b` statement returns the log entries that include the `a` and `b` keywords. Phrase search: A phrase is a string that is enclosed in double quotation marks (""). Substrings in a phrase are separated by space characters. Each substring is a keyword.

| "http error" |   | statement retu |
|---|---|---|
| equivalent to | http and error |   |

For example, the `"http error"` statement returns the log entries that contain the http and error keywords. Wildcard-based search: You can use an asterisk ( `*` ) or a question mark ( ? ) as a wildcard character in a keyword. Each keyword that includes wildcards can contain 1 to 64 characters in length and cannot start with a wildcard character. If a search condition contains a keyword that includes a wildcard character, Log Service returns a maximum of 100 log entries and each log entry contains a word that matches the keyword pattern. For example, if you execute the addr? statement, Log Service returns a maximum of 100 log entries and each log entry contains a word that is prefixed with `addr` . When you use wildcard-based search, note the following information: A keyword cannot start with an asterisk ( `*` ) or a question mark ( ? ). The more accurate the keyword is, the more accurate the search results will be. Wildcard-based search is not supported for a keyword that contains more than 64 characters in length. A search statement returns a maximum of 100 log entries that match the search conditions. Field-specific search After you configure the field index, you can search log entries based on the keys and values of the fields in the field index. For a field of the DOUBLE or LONG type, you can specify a value range for search. For example, the `L` `atency>5000 and Method:Get* and not Status:200` statement returns the log entries that meet the following conditions: The value of the `Latency` field is greater than 5000, the value of the `Method` field is prefixed with `Get` , and the value of the `Status` field is not 200. You can perform a basic query or combined query, depending on the data types of the fields in the field index. For more information, see Overview. Additional considerations If you execute a search statement to perform both full-text search and field-specific search and you set different delimiters for the two search types, the delimiter that is set for field-specific search is used. You must set the data type of a field to DOUBLE or LONG before you specify a value range to search the field. If the data type of a field is not DOUBLE or LONG or the value range syntax is incorrect, the field-specific search condition is considered a full-text search condition. In this case, unexpected search results may be returned. If you change the data type of a field from TEXT to DOUBLE or LONG, only the equal-to operator ( `=` ) can be used to search for the log entries that are collected before the change. Operators The following table lists the operators that are supported by search statements.

| Operator | Description |   |   |
|---|---|---|---|
| and | A binary operator. The syntax is query1 and query2 . It indicates the intersection of the search results of query1 and query2 . The default operator between keywords is and . |   |   |
| or | A binary operator. The syntax is query1 or query2 . It indicates the union of the search results of query1 and query2 . |   |   |
| not | A binary operator. The syntax is query1 not query2 . It indicates that the log entries that match query1 but do not match query2 are returned. The syntax is equivalent to query1–query2 . You can also use the not query1 syntax. It indicates that the log entries that do not match query1 are returned. |   |   |
| ( , ) | The operator that merges one or more sub-conditions into one search condition. The search based on a sub-condition that is enclosed in parentheses () is performed first. |   |   |
| : | The operator that is used to specify a pattern of key-value pairs. The syntax is term1:term2 . If the key or value contains reserved characters such as spaces and colons (:), use double quotation marks ( "" ) to enclose the entire key or value. |   |   |
| " | The operator that converts another operator into a common character. All terms enclosed in double quotation marks ("") are considered keywords rather than operators. In a field-specific search statement, you can enclose the entire key or value in double quotation marks. |   |   |
| \ | The operator that escapes a double quotation mark. The escaped double quotation mark is considered a symbol instead of an operator. Example: "\"" . |   |   |
| \| | The pipeline operator that is used to chain a search statement and an analytic statement. The analytic statement that follows the pipeline operator is executed based on the result of the search statement that the pipeline operator follows. Example: query1 \| select count(1) . |   |   |
|   |   | query1 \| select |   |
| count | The count operator that is used to summarize the number of log entries. |   |   |
| * | The wildcard character that is used to replace zero or more characters. For example, the que* statement returns the log entries with a word that is prefixed with que . Not e A wildcard-based search statement returns a maximum of 100 log entries that match the search condition. |   |   |

|   | query1 and query2 |
|---|---|
| query1 |   |

|   | count(1) |
|---|---|

| Operator | Description |   |   |
|---|---|---|---|
| ? | The wildcard character that replaces a single character. The qu?ry statement returns the log entries with a word that is prefixed with qu , is suffixed with ry , and contains a character in between. |   |   |
| topic __ __ | The operator that specifies zero or more topics from which to query log entries. Example: topic :mytopicname . __ __ |   |   |
| tag __ __ | The operator that specifies a tag value of a tag key to query. Example: tag :tagkey:tagvalue . __ __ |   |   |
| source | The operator that specifies the IP address of a log source whose log entries you want to query. Example: source:127.0.0.1 . |   |   |
| > | The greater-than operator. You can use this operator to query the log entries whose value of a field is greater than a specified number. Example: latency > 100 . |   |   |
| >= | The greater-than-or-equal-to operator. You can use this operator to query the log entries whose value of a field is greater than or equal to a specified number. Example: latency >= 100 . |   |   |
|   |   | latency |   |
| < | The less-than operator. You can use this operator to query the log entries whose value of a field is less than a specified number. Example: latency < 100 . |   |   |
| <= | The less-than-or-equal-to operator. You can use this operator to query the log entries whose value of a field is less than or equal to a specified number. Example: latency <= 100 . |   |   |
| = | The equal-to operator. You can use this operator to query the log entries whose value of a field is equal to a specified number. Example: latency = 100 . |   |   |
| in | The operator that is used to query the log entries whose value of a field falls in a specified range. Brackets [] indicate closed intervals and parentheses () indicate open intervals. The beginning number and ending number of the range are enclosed in brackets or parentheses and separated by one or more space characters. The in operator must be in lowercase. Example: latency in [100 200] or latency in (100 200] . |   |   |

|   | >= 100 |
|---|---|

| latency <= |   |
|---|---|

|   | 100 |
|---|---|

> Not e
> All operators except the in operator are case-insensitive.
> You can use the following operators, which are sorted in descending order of precedence: `:` , `"` ,
> `()` , `and` , `not` , and `or` .
> Log Service uses the following operators: `sort` , `asc` , `desc` , `group by` , `avg` , `sum` , `min`
> , `max` , and `limit` . If you need to use these operators as keywords, enclose them in double quotation marks ("").

Search statement examples

| Expected search result | Search statement |
|---|---|
| Log entries that contain a and b | a and b or a b |
| Log entries that contain a or b | a or b |
| Log entries that contain a but do not contain b | a not b |

| Expected search result |   | Search statement |   |   |   |
|---|---|---|---|---|---|
| Log entries that do not contain a |   | not a |   |   |   |
| Log entries that contain a and b but do not contain c |   | a and b not c |   |   |   |
| Log entries that contain a or b and contain c |   | (a or b ) and c |   |   |   |
| Log entries that contain a or b but do not contain c |   | (a or b ) not c |   |   |   |
| Log entries that contain a and b and may contain c |   | a and b or c |   |   |   |
| Log entries whose FILE field contains apsara |   | FILE:apsara |   |   |   |
| Log entries whose FILE field contains apsara and shennong |   | FILE:"apsara shennong" , FILE:apsara FILE: |   |   |   |
|   |   |   | FILE:apsara FILE: |   |   |
|   | ara and shennong | shennong , or FILE:apsara and FILE:shennong |   |   |   |
| Log entries that contain the following keyword: and |   | and |   |   |   |
| Log entries whose FILE field contains apsara or shennong |   | FILE:apsara or FILE:shennong |   |   |   |
| Log entries whose file info field contains apsara |   | "file info":apsara |   |   |   |
| Log entries that contain double quotation mark (") |   | \" |   |   |   |
| Log entries with words that are prefixed with shen |   | shen* |   |   |   |
| Log entries whose FILE field is prefixed with shen |   | FILE:shen* |   |   |   |
| Log entries whose value of the FILE field is shen* |   | FILE: "shen*" |   |   |   |
| Log entries with words that are prefixed shen, are suffixed with ong, and contain a single character in between |   | shen?ong |   |   |   |
| Log entries with words that are prefixed with shen and words that are prefixed with aps |   | shen* and aps* |   |   |   |
| Log entries of topic1 and topic2 |   | topic :topic1 or topic : topic2 __ __ __ __ |   |   |   |
| Log entries with a tag whose key is tagkey1 and value is tagvalue2 |   | tag : tagkey1 : tagvalue2 __ __ |   |   |   |
| Log entries whose value of the latency field is greater than or equal to 100 and less than 200 |   | latency>= 100 and latency < 200 or latency in [100 200) |   |   |   |
|   |   |   |   | latency in |   |
| Log entries whose value of the latency field is greater than 100 |   | latency > 100 |   |   |   |
| Log entries that do not contain spider and whose http referer field does not contain opx _ |   | not spider not bot not http referer:opx _ |   |   |   |
| Log entries whose cdnIP field is not empty |   | not cdnIP:"" |   |   |   |
| Log entries that do not contain the cdnIP field |   | not cdnIP:* |   |   |   |
| Log entries that contain the cdnIP field |   | cdnIP:* |   |   |   |
| Log entries that contain a specified URL |   | * \| select * where url = 'www.xxxxx.com' |   |   |   |

|   |   | latency>= 100 and latency < 200 |
|---|---|---|
|   | [100 200) |   |

Topic-specific search Each Logstore is divided into one or more topics. You can divide a Logstore into multiple topics if you need level-2 categories of log entries. When you query logs, you can specify topics to increase efficiency. In a search statement, you can specify one or more topics to query. If no topic is specified, log entries are queried from all topics. For example, you can classify log entries into multiple topics based on domain names. Log topics Syntax of topic-specific search: In a search statement, you can specify one or more topics to query. If no topic is specified, log entries are queried from all topics. The topic-specific search syntax is `__topic__:topicName` . You can also specify a topic in a URL. You can query log entries from multiple topics. For example, the `__topic__:topic1 or __topic__:topic2` statement returns the log entries in topic1 and topic2.

#### 4.7.2 LiveTail

This topic describes how to use LiveTail to monitor and analyze log data. LiveTail is an interactive feature provided in the Log Service console to monitor and extract key log data in real time. Prerequisites LiveTail is available only after logs are collected. LiveTail can only monitor and extract log data collected by Logtail. Context In online O&M scenarios, you often need to monitor collected log data in real time and extract key information from the latest log data to locate error causes. In traditional O&M, you must run the `tail -f` command on servers to monitor log files in real time. To easily obtain the required real-time log information, you can include the `grep` or grep –v command to filter log entries by keyword. To simplify online O&M, Log Service provides LiveTail in the console to monitor and analyze online log data in real time. Benefits Monitors real-time log information and filters log data by keyword. Logs collected based on the log collection configurations are identified by index. Log fields are delimited. This allows you to query contextual logs that contain delimiters. Log files can be tracked based on a single log entry and monitored in real time without the need to connect to online servers. Use LiveTail to monitor logs in a Logstore in real time
1. Log on to the Log Service console.
2. In the Projects section, click the target project.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
4. (Optional)Start LiveTail.
i. On the Raw Logs tab, click the icon next to the sequence number of the specified raw log entry, and then select LiveT ail. The system starts LiveTail and starts timing. The Source T ype, Machine Name, and File Name fields are automatically filled in based on the specified raw log entry. After LiveTail is started, log data collected by Logtail is displayed in order on the page in real time. The latest log data is displayed at the bottom of the page by default. You can view the latest log data without the need to drag the scroll bar. Up to 1,000 log entries can be displayed on the page. If more than 1,000 log entries are collected, the page is automatically refreshed to show the latest 1,000 log entries. ii. (Optional)You can also enter keywords in the search box to display log entries that contain the keywords in the monitoring list. By filtering log entries that contain the keyword, you can monitor specific log entries in real time.
5. Customize LiveTail.
i. On the Search & Analysis page, click the LiveT ail tab. ii. Configure LiveTail.

| Parameter | Required | Description |
|---|---|---|
| Source T ype | Yes | The source of log entries. Valid values: Physical servers Kubernetes containers Docker |
| Machine Name | Yes | The name of the server from which log entries are collected. |
| File Name | Yes | The full path and name of the log file. |
| Filt er Keywords | No | A keyword. After you set a keyword, only log entries that contain the keyword are displayed in the log monitoring list. |

iii. Click St art LiveT ail. After LiveTail is started, log data collected by Logtail is displayed in order on the page in real time. The latest log data is displayed at the bottom of the page by default. You can view the latest log data without the need to drag the scroll bar. Up to 1,000 log entries can be displayed on the page. When more than 1,000 log entries are collected, the page is refreshed to show the latest 1,000 log entries.
6. To analyze logs during real-time log monitoring, click St op LiveT ail.
After you stop LiveTail, the LiveTail timing and the real-time log data update also stop. Log Service provides multiple methods to analyze exceptions that are found during log monitoring. For more information, see Use LiveTail to analyze logs. Use LiveTail to analyze logs After you stop LiveTail, real-time log updates in the log monitoring list also stop. You can analyze and fix errors that are found during log monitoring. View log entries that contain specified fields Log fields are delimited. You can click the value of the specified exception field on the LiveT ail tab. Then, you are automatically forwarded to the Raw logs tab and the value of the exception field is used as a keyword to filter all log entries that contain the field and the keyword. You can also analyze log entries that contain the keyword based on contextual queries and statistical charts. Narrow down the time range of a log query based on the log distribution histogram After LiveTail is started, the log distribution histogram is updated at the same time. If you find a distribution exception (for example, a big increase in the number of log entries) in a time range, you can click the corresponding green rectangle to narrow down the time range of the log query. The timeline of the raw logs is associated with the timeline that you click on the LiveTail tab. You can view all relevant raw logs and log distribution details during this time range. Highlight key information based on column settings On the LiveT ail tab, click Column Set t ings in the upper-right corner of the log monitoring list. Then, you can specify a field as a separate column to highlight relevant data. Analyze log data On the LiveT ail tab, click the arrow in the upper-left corner of the log monitoring list to show the Quick Analysis pane. The time range for quick analysis starts from the time when LiveTail is started and ends at the time when LiveTail is stopped. The quick analysis provided on the LiveTail tab is the same as that provided on the Raw Logs tab. For more information, see Quick analysis.

#### 4.7.3 LogReduce

This topic describes how to use LogReduce to group log data in Log Service. The LogReduce feature groups similar log entries by detecting same log patterns during text log collection. Context The LogReduce feature allows you to group text logs of multiple formats. You can locate errors, detect anomalies, roll back versions, and perform other O&M operations in DevOps scenarios. You can also detect network intrusions to ensure data security. In addition, you can save the log grouping result to a dashboard as an analysis chart, and then view the grouped data in real time. Benefits Various formats of logs such as Log4j logs, JSON-formatted logs, and syslog logs can be grouped. Hundreds of millions of log entries can be grouped in seconds. Log entries can be grouped in any pattern. Raw log entries can be retrieved based on the signature of log entries grouped in a pattern. The number of log entries grouped in a log pattern in different time ranges can be compared. The precision of log grouping can be adjusted based on your needs. Billing method After the LogReduce feature is enabled, the size of indexes increases by 10% of the raw log size. For example, if the size of raw log data is 100 GB per day, the size of log indexes increases by 10 GB.

| Raw log size | Index percentage | Size of indexes generated by LogReduce | Index size |
|---|---|---|---|
| 100 GB | 20% (20 GB) | 100 × 10% | 30 GB |
| 100 GB | 40% (40 GB) | 100 × 10% | 50 GB |
| 100 GB | 100% (100 GB) | 100 × 10% | 110 GB |

Enable LogReduce of a Logstore The LogReduce feature is disabled by default.
1. Log on to the Log Service console.
2. Click the target project in the Projects section.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
4. Configure an index.
If you have enabled the index feature and configured indexes for the Logstore, choose Index At t ribut es > Modif y. If you have not enabled the index feature, click Enable.
5. Set the index attributes and turn on the LogReduce switch. Click OK.
After LogReduce is enabled, Log Service groups log data that has been collected. Then, you can perform the following operations: View log grouping results and raw logs Adjust the precision of log grouping Compare the number of log entries grouped in different time ranges View log grouping results and raw logs
1. On the Search & Analysis page, enter a search and analytic statement in the search box, and then click Search
& Analyt ics. You can use keywords to filter grouped log entries.

> Not e SQL statements are not supported. This means analysis results cannot be grouped.

2. Click the LogReduce tab to view the log grouping result.
The filtered log grouping result is displayed on the LogReduce tab.

| Item | Description |
|---|---|
| Number | The sequence number of a log group. |
| Count | The number of log entries in a log group. |
| Pat t ern | The log pattern. Each log group has one or more sub-patterns. |

Move the pointer over a value in the Count column to view the sub-patterns of the corresponding log group and the percentage of each sub-pattern in the log group. You can also click the plus sign (+) before the count value to expand the sub-pattern list. Click a count value to view the raw log entries of the corresponding log group. Adjust the precision of log grouping
1. On the Search & Analysis page, click the LogReduce tab.
2. In the upper-right corner of the tab, drag the Pat t ern Count slider to adjust the precision of log grouping.
If you drag the slider towards Many, you can obtain a more precise log grouping result with more detailed patterns. If you drag the slider towards Lit t le, you can obtain a less precise log grouping result with less detailed patterns. Compare the number of log entries grouped in different time ranges Click Log Compare on the LogReduce tab, select a time range, and then click OK.

| Item | Description |
|---|---|
| Number | The sequence number of a log group. |
| Pre Count _ | The number of log entries grouped by the current pattern in the previous time range. |
| Count | The number of log entries grouped by the current pattern in the current time range. |
| Diff | The difference between the Pre Count value and Count _ value. |
| Pattern | The pattern of a log group. |

SQL statement examples: Obtain a log grouping result. SQL statement:

```
* | select a.pattern, a.count,a.signature, a.origin_signatures from (select log_reduce(3) as a fr
om log) limit 1000
```

> Not e When you view the log grouping result in the Log Service console, you can click Copy Query to obtain the relevant SQL statement.

Input parameter: log_reduce (precision) precision: an integer from 1 to 16 that can be set as the log grouping precision. A smaller value indicates a higher precision and more patterns. The default value is 3. Returned fields: pattern: the sub-patterns of log entries in a log group. count: the number of log entries in a log group. signature: the log pattern of a log group. origin_signatures: the original signature of a log group. You can use this field to query raw log entries of the log group. Compare the number of log entries grouped in different time ranges. SQL statement:

```
* | select v.pattern, v.signature, v.count, v.count_compare, v.diff from (select compare_log_redu
ce(3, 86400) as v from log) order by v.diff desc limit 1000
```

> Not e After you click Log Compare in the Log Service console, you can click Copy Query to obtain the SQL statement.

Input parameters: compare_log_reduce(precision, compare_interval) precision: an integer from 1 to 16 that can be set as the log grouping precision. A smaller value indicates a higher precision and more patterns. The default value is 3. compare_interval: the number of seconds between when the previous log entries and the current log entries were generated. The value of this parameter must be a positive integer. Returned fields: pattern: the sub-patterns of log entries in a log group. signature: the log pattern of a log group. count: the number of log entries in a log group. count_compare: the number of log entries for a same-pattern log group within the specified time range. Diff: the difference between the values of the count field and the count_compare field.

#### 4.7.4 Contextual query

This topic describes the contextual query feature provided in the Log Service console. You can use this feature to query the full context of the log file where specified log entries are obtained. Prerequisites The index feature is enabled. Context The contextual query feature identifies the server and file where a specified log entry resides. It then queries several log entries before and after the log entry in the original log file. This helps you locate errors during troubleshooting. Scenarios For example, a transaction on an O2O takeout website is logged in an application log file on a server as follows: User logon > Browse product s > Select an it em > Add t o a shopping cart > Place an order > Payment > Deduct ion > Generat e an order. If the order fails, the O&M personnel must locate the cause at the earliest opportunity. In traditional contextual queries, the O&M personnel must be authorized before logging on to each server where the application is deployed. Then, the O&M personnel must use the order ID as a keyword to search application log files to locate the cause of the failure. In Log Service, the O&M personnel can perform the following steps to locate the cause of the failure:
1. Install Logtail on servers. Then log on to the Log Service console to add the servers to machine groups and
configure log collection. After the configurations are complete, Logtail starts to upload incremental logs.
2. On the search and analysis page of the Log Service console, specify the time range and find the error log entry
based on the order ID.
3. Based on the error log entry, page up until you find log entries related to the error log entry. For example, you
may want to find a log entry that records a credit card payment failure.

> Not e The contextual query feature does not support syslog.

Benefits Intrusions into applications or changes to log file formats are avoided. You can view contextual log entries of a specified log entry in a log file on a server that has been registered in the Log Service console. This helps you avoid logging on to each server to search for logs that you want. You can specify the time range based on the time when an event occurs to locate suspicious log entries. Then you can perform a contextual query in the Log Service console. This improves troubleshooting efficiency. Data loss caused by log file rotation or insufficient storage space is avoided. You can view historical log data in the Log Service console at any time.
1. Log on to the Log Service console.
2. Click the target project in the Projects section.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
4. Enter a search and analytic statement, select a time range, and then click Search & Analyt ics.
On the query results page, if the Cont ext View icon is available in the drop-down list of the icon to the left of a log entry, the log entry supports contextual query.
5. Click the icon to the left of a log entry, and select Cont ext View from the drop-down list. On the page that
appears, view the contextual log entries of the selected log entry.
6. Scroll up and down to view more contextual log entries. To view earlier or later contextual log entries, click
Old or New.

#### 4.7.5 Saved search

This topic describes how to save a search and analytic statement as a saved search for a Logstore. The saved search feature allows you to search and analyze log data in an efficient way. Prerequisites The index feature is enabled and configured. Context If you need to frequently run a search and analytic statement, you can save the statement as a saved search. In later queries, you can click the name of the saved search on the left side of the search page to run the statement and view the result. You can also use the saved search in alert configurations. Log Service periodically runs the search and analytic statement and sends an alert if a query result meets the trigger condition. If you want to select Open Saved Search in the Event Action field when you configure drill-down analysis, you must preset a saved search and set a placeholder in the query statement. For more information, see Drill-down analysis.
1. Log on to the Log Service console.
2. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
3. Enter a search and analytic statement in the search box, set a time range, and then click Search & Analyze.
4. Click Save Search in the upper-right corner of the page.
5. Configure the saved search.
i. Enter a Saved Search Name. The name can contain only lowercase letters, digits, hyphens (-), and underscores (_). The name must start and end with a lowercase letter or digit. The name must be 3 to 63 characters in length. ii. Check the values of the Logst ores, T opic, and Query parameters. If the values of the Logst ores and T opic parameters do not meet your requirements, follow these steps: Return to the Logstores page. On this page, find and click the name of the target Logstore. On the page that appears, enter the search and analytic statement in the Search & Analyze search box, and then click Save Search again. iii. (Optional)Select a part of the query statement, and then click Generat e Variable. The generated variable is a placeholder variable. You can set the placeholder name in the Variable Name field. The selected characters are displayed in the Def ault Value field.

> Not e If you use this saved search for drill-down analysis in another chart where the variable is the same as the Variable Name, the Def ault Value is replaced with the chart value that you click to trigger the drill-down event. The search and analytic statement with the replaced chart value is executed. For more information, see Drill-down analysis.

6. Click OK.
What's next To modify a saved search, perform the following operations: Enter a new search and analytic statement, click Search & Analyt ics to run the statement, and then click Modif y Saved Search.

#### 4.7.6 Quick analysis

This topic describes the quick analysis feature of Log Service. You can use this feature to query log data with one click. This feature allows you to analyze the distribution of a field in a specified time range and reduce the query cost of key data. Features Groups the first 100,000 values of a `text` field and provides statistics for the top 10 groups. Generates `approx_distinct` statements for `text` fields. Allows you to perform histogram-based statistics for the approximate distribution of `long` or `double` fields. Allows you to search for the maximum, minimum, and average of `long` or `double` fields and calculate the sum of the fields. Generates a query statement based on the quick analysis feature. Prerequisites Field indexes are configured. Indexes are configured for the fields that you need to search and analyze. For more information about how to enable the indexing feature, see Enable the index feature and configure indexes for a Logstore. The name of a field is specified as the `key` . The data type, alias, and delimiter of the field are configured. For example, if a log entry contains the `request_method` and `request_time` fields, you can configure indexes for the two fields, as shown in the following figure. Instructions After you configure indexes for specified fields, you can go to the Search & Analysis page and click the Raw Logs tab to view the specified fields. The fields are listed in the Quick Analysis pane on the left of the raw log entries. You can click the icon above the serial number to hide the Quick Analysis pane. You can also click the Eye icon to perform quick analysis based on the Current T ime Zone and Current Search conditions. Data of the text type Group and analyze log data Click the Eye icon next to a t ext field to group the first 100,000 field values and return the percentages of the top 10 groups. The following statement is used:

```
$Search | select ${keyName} , pv, pv *1.0/sum(pv) over() as percentage from( select count(1) as pv , "${keyName}" from (select "${keyName}" from log limit 100000) group by "${keyName}" order by pv d esc) order by pv desc limit 10
```

The following figure shows the grouping and analytics result of the `request_method` field. `GET` requests account for the majority of requests. Calculate the number of unique values in a field Under the target fields in the Quick Analysis pane, click Count Dist inct Values to calculate the number of unique values in the ${keyName} field. Fill the Search & Analyze search box with the grouping and analytics statement Click the Count Dist inct Values button on the right of the icon. The Search & Analyze search box is filled with the grouping and analytics statement. You can edit the statement. Data of the long and double types Display approximate distribution by using histograms The number of `long and double` field values is large. The preceding grouping and analytics method is not suitable for the long and double data types. You can use the following statement to divide field values into 10 groups and display the approximate distribution of the values in a histogram:

```
$Search | select numeric_histogram(10, ${keyName})
```

The following figure shows the approximate distribution of the values in the `request_time` field. The largest percentage of request time is distributed around 0.059 seconds.

| Min , | Avg |
|---|---|

Perform quick analysis by using the `Max` , `Min` , `Avg` , and `Sum` functions You can click `Max` under a field to search for the maximum value, `Min` to search for the minimum value, `Av` `g` to calculate the average value, and `Sum` to calculate the sum of the values. Fill the Search & Analyze search box with the query statement of the histogram approximate distribution Click the icon next to `Sum` . The Search & Analyze search box is filled with the query statement of the histogram approximate distribution. You can edit the statement.

### 4.8 Analysis grammar

#### 4.8.1 General aggregate functions

This topic describes the syntax and examples of general aggregate functions. The search and analytics feature of Log Service allows you to use general aggregate functions for log analysis. The following table describes the supported general aggregate functions.

| Function | Description |   | Example |   |   |
|---|---|---|---|---|---|
| arbitrary(x) | Returns a random value from among the values in the x field. |   | latency > 100 \| select arbitrary(method) |   |   |
|   |   |   |   | latency > 100 \| select |   |
|   |   | he x field. | arbitrary(method) |   |   |
| avg(x) | Returns the arithmetic mean of all values in the x field. |   | latency > 100 \| select avg(latency) |   |   |
| checksum(x) | Returns a Base64-encoded checksum of the values of the x field. |   | latency > 100 \| select checksum(method) |   |   |
| count(*) | Calculates the number of values of a field. |   | - |   |   |

|   |   | latency > 100 \| select |   |
|---|---|---|---|
| field. | avg(latency) |   |   |

|   |   | latency > 100 \| select |   |
|---|---|---|---|
| of the x field. | checksum(method) |   |   |

| User Guide·Query and analysis |   |   | Log Servic |   |   |
|---|---|---|---|---|---|
| Function | Description |   | Example |   |   |
| count(x) | Counts the number of non-null values of the x field. |   | latency > 100 \| select count(method) |   |   |
| count(digit) | Counts the number of values of a field. The count(digit) function is equivalent to the count(1) and count(*) functions. |   | - |   |   |
| count if(x) _ | Returns the number of the occurrences of the TRUE value. |   | latency > 100 \| select count if(url like '%abc') _ |   |   |
| geometric mean(x) _ | Returns the geometric mean of the values in the x field. |   | latency > 100 \| select geometric mean(latency) _ |   |   |
| max by(x,y) _ | Returns the value of the x field that corresponds to the maximum value of the y field. |   | * \| select |   |   |
|   |   |   |   | * \| select |   |
|   |   | m value | min by(method,latency,3) _ |   |   |
| max by(x,y,n) _ | Returns n values of the x field that corresponds to the n largest value of the y field. |   | * \| select |   |   |
|   |   |   |   | * \| select |   |
|   |   | d that | min by(method,latency,3) _ |   |   |
| min by(x,y) _ | Returns the value of the x field that corresponds to the smallest value of the y field. |   | * \| select min by(x,y) : _ queries the method that corresponds to the minimum latency. |   |   |
| min by(x,y,n) _ | Returns n values of the x field that corresponds to the n smallest values of the y field. |   | * \| select |   |   |
|   |   |   |   | * \| select |   |
|   |   | d that | min by(method,latency,3) _ |   |   |
| max(x) | Returns the maximum value among all values in the x field. |   | latency > 100\| select max(inflow) |   |   |
| min(x) | Returns the minimum value among all values in the x field. |   | latency > 100\| select min(inflow) |   |   |
| sum(x) | Returns the sum among all values in the x field. |   | latency > 10 \| select sum(inflow) |   |   |
| bitwise and agg(x) _ _ | Returns the bitwise AND of all values in the x field in two's complement representation. |   | - |   |   |
| bitwise or agg(x) _ _ | Returns the bitwise OR of all values in the x field in two's complement representation. |   | - |   |   |

|   |   | latency > 100 \| select |   |
|---|---|---|---|
|   | count(method) |   |   |

|   |   | latency > 100 \| select |
|---|---|---|
| f the TRUE value. | count if(url like '%abc') _ |   |

| latency > 100 \| select |   |
|---|---|

|   |   | latency > 100\| select |   |
|---|---|---|---|
| e x field. | max(inflow) |   |   |

|   |   | latency > 100\| select |   |
|---|---|---|---|
| field. | min(inflow) |   |   |

|   |   | latency > 10 \| select |   |
|---|---|---|---|
|   | sum(inflow) |   |   |

#### 4.8.2 Security check functions

Security check functions in Log Services are designed based on the globally shared WhiteHat Security asset library. This topic describes security check functions that you can use to check whether an IP address, domain name, or URL in logs is secure. Scenarios O&M personnel of enterprises and institutions in Internet, gaming, information, and other industries that require robust O&M services can use security check functions to identify suspicious requests or attacks. They can also use the functions to implement in-depth analysis and defend against potential attacks. O&M personnel of enterprises and institutions in banking, securities, e-commerce, and other industries that require strong protection for internal assets can use security check functions to identify requests to suspicious websites and downloads initiated by trojans. Then the O&M personnel can take immediate actions to prevent potential losses. Features Reliability: built upon the globally shared WhiteHat Security asset library that is updated in a timely manner. Efficiency: capable of screening millions of IP addresses, domain names, and URLs within seconds. Ease of use: supports the analysis of network logs by using the security_check_ip, security_check_domain, and security_check_url functions. Flexibility: supports interactive queries, report creation, and alert configurations and subsequent actions. Functions

| Function |   | Description |   | Example |   |   |
|---|---|---|---|---|---|---|
| security check ip _ _ |   | Checks whether an IP address is secure. The value 1 indicates that the |   | select |   |   |
|   |   |   |   |   | select |   |
|   |   |   |   | security check ip(real client i _ _ _ _ |   |   |
|   |   | specified IP address is suspicious. | us. |   |   |   |
|   |   |   |   | p) |   |   |
|   |   | The value 0 indicates that the specified IP address is secure. |   |   |   |   |
| security check domain _ _ |   | Checks whether a domain name is secure. The value 1 indicates that the specified domain name is suspicious. The value 0 indicates that the specified domain name is secure. |   | select security check domain(site) _ _ |   |   |
| security check url _ _ |   | Checks whether a URL is secure. The value 1 indicates that the specified URL is suspicious. |   | select |   |   |
|   |   |   |   |   | select |   |
|   |   |   |   | security check domain(concat(ho _ _ |   |   |
|   |   | The value 0 indicates that the |   |   |   |   |
|   |   |   |   | st, url)) |   |   |
|   |   | specified URL is secure. |   |   |   |   |

|   |   | select |   |
|---|---|---|---|
|   | security check domain(site) _ _ |   |   |

Examples Check external suspicious requests and generate reports For example, an e-commerce enterprise collects logs from its NGINX servers and wants to scan suspicious client IP addresses. To do this, the enterprise can pass the ClientIP field in logs that are collected from the NGINX servers to the `security_check_ip` function and filter out IP addresses associated with the returned value 1. Then the enterprise can query the countries where the IP addresses are located and ISPs to which the IP addresses belong. SQL statement for this scenario:

```
* | select ClientIP, ip_to_country(ClientIP) as country, ip_to_provider(ClientIP) as provider, coun
t(1) as PV where security_check_ip(ClientIP) = 1 group by ClientIP order by PV desc
```

Display the ISPs and countries in a map. Check internal suspicious requests and send alerts For example, a securities operator collects logs of its internal devices that access the Internet through gateways. To check requests to suspicious websites, the operator can run the following statement:

```
* | select client_ip, count(1) as PV where security_check_ip(remote_addr) = 1 or security_check_sit
e(site) = 1 or security_check_url(concat(site, url)) = 1 group by client_ip order by PV desc
```

The operator can save this statement as a saved search and configure an alert. An alert is triggered when a client frequently accesses suspicious websites. The statement in the alert can be configured to run every five minutes to check if a client has frequently (more than five times) accessed suspicious websites in the past one hour. The following figure shows the configurations of an alert.

#### 4.8.3 Map functions

This topic describes the syntax and examples of map functions. The following table describes the supported map functions.

| Function | Description | Example |
|---|---|---|
| Subscript operator [] | Retrieves the value corresponding to a specified key from a map. | - |

|   | Function |   |   |   | Description |   |   |   |   |   |   |   |   | Example |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | histogram(x) |   |   |   | Groups the values of the parameter x and calculates the number of occurrences of each value. The syntax is equivalent to select count group by x . Not e The returned data is in the JSON format. |   |   |   |   |   |   |   |   | The statement latency > 10 \| |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | latency > 10 \| |   |
|   |   |   |   |   |   |   |   |   |   | select count |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ct count |   |   | sele |   |   |   |
|   | histogram u(x) _ |   |   |   | Groups the values of the parameter x and calculates the number of occurrences of each value. Not e The returned data is in the format of multiple rows and columns. |   |   |   |   |   |   |   |   | The statement latency > 10 \| |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | latency > 10 \| |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | select histogram u(status) _ |   |   |   |
|   |   |   |   |   |   | Not e The returned data is in the format of multiple rows and columns. |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | t of multiple rows . |   |   |   |   | count(1) group by status |   |   |   |
|   | map agg(Key,Value) _ |   |   |   | Returns a random value of the key in the format of a map that consists of key-value pairs. |   |   |   |   |   |   |   |   | latency > 100 \| select map agg(method,latency) _ |   |   |   |
|   | multimap agg(Key,Value) _ |   |   |   | Returns all values of the key in the format of a map that consists of key- value pairs. |   |   |   |   |   |   |   |   | latency > 100 \| select multimap agg(method,latency) _ |   |   |   |
|   | cardinality(x) → bigint |   |   |   | Returns the cardinality of the map x. |   |   |   |   |   |   |   |   | - |   |   |   |
|   | element at(map <K, V> , key) → V _ |   |   |   | Returns the value for the specified key. |   |   |   |   |   |   |   |   | - |   |   |   |
|   | map() → map <unknown, unknown> |   |   |   | Returns an empty map. |   |   |   |   |   |   |   |   | - |   |   |   |
|   | map(array <K> , array <V> ) → map <K,V> |   |   |   | Returns a map where each key-value |   |   |   |   |   |   |   |   | SELECT map(ARRAY[1,3], ARRAY[2,4]); - {1 -> 2, 3 -> |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | ARRAY[2,4]); - {1 -> 2, 3 -> |   |   |   |
|   |   |   |   |   | pair consists of two elements from two separate arrays. |   |   | f two elements from |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | 4} |   |   |   |
|   | map from entries(array <row<K, _ _ V>> ) → map <K,V> |   |   |   | Converts a multi-dimensional array to a map. |   |   |   |   |   |   |   |   | SELECT |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | SELECT |   |   |
|   |   |   |   | <row<K, |   |   |   |   |   |   |   | ay to |   | map from entries(ARRAY[(1, _ _ |   |   |   |
|   |   |   | <K,V> |   |   |   | map. |   |   |   |   |   |   | 'x'), (2, 'y')]); - {1 -> 'x', |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | 2 -> 'y'} |   |   |   |
|   | map concat(map1 <K, V> , _ map2 <K, V> , ..., mapN <K, V> ) → map <K,V> |   |   |   | Returns a map that is the union of all specified maps. If a key is found in multiple specified maps, the value of the key in the returned map is the value of the key that occurs in the last specified map. |   |   |   |   |   |   |   |   | - |   |   |   |
|   | map filter(map <K, V> , function) _ → map <K,V> |   |   |   | For more information, see the map filter function in Lambda _ functions. |   |   |   |   |   |   |   |   | - |   |   |   |
|   | map keys(x <K, V> ) → _ array <K> |   |   |   | Returns an array of keys in the specified map. |   |   |   |   |   |   |   |   | - |   |   |   |

|   | group by x |
|---|---|

| latency > 10 \| select |   |
|---|---|

| The returned data is |   | count(1) group by status |
|---|---|---|

| latency > 10 \| select |   |
|---|---|

|   |   | latency > 100 \| select |   |
|---|---|---|---|
| a map that consists of s. | map agg(method,latency) _ |   |   |

|   |   | latency > 100 \| select |
|---|---|---|
| ap that consists of key- | multimap agg(method,latency) _ |   |

|   | V>> |
|---|---|

|   | <K, V> |
|---|---|
| <K> |   |

| og Service |   | User Guide·Query and analysi |
|---|---|---|
| Function | Description | Example |
| map values(x <K, V> ) → _ array <V> | Returns an array of values in the specified map. | - |

#### 4.8.4 Approximate functions

This topic describes the syntax and examples of approximate functions that Log Service supports for log analysis. The following table describes the supported approximate functions.

| Function |   |   | Description |   |   |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| approx distinct(x) _ |   |   | Returns the approximate number of distinct values of the x field. |   |   |   |   | - |   |   |
| approx percentile(x,percentage _ ) |   |   | Returns the value located at the specified approximate percentage among the sorted values of the x field. |   |   |   |   | approx percentile(x,0.5) : _ returns the median among the sorted values of the x field. |   |   |
| approx percentile(x, _ percentages) |   |   | Returns values located at multiple specified approximate percentages among the sorted values of the x field. This function works in a similar manner to the approx percentile(x,percentage _ |   |   |   |   | approx percentile(x,array[0.1 _ ,0.2]) |   |   |
|   |   |   |   |   |   |   |   |   | approx percentile(x,array[0.1 _ |   |
|   |   |   |   |   |   | This function works in a similar er to the |   | ,0.2]) |   |   |
|   |   |   |   | approx percentile(x,percentage _ |   |   |   |   |   |   |
|   |   |   | ) |   |   |   |   |   |   |   |
| numeric histogram(buckets, _ Value) |   |   | Distributes all values of the Value field into multiple buckets. The buckets parameter specifies the number of buckets. The key of every bucket and the number of values in a bucket are returned. This function is equivalent to select count group by . Not e The response is in the JSON format. |   |   |   |   | method:POST \| select |   |   |
|   |   |   |   |   |   |   |   |   | method:POST \| select |   |
|   |   |   |   |   |   |   | bucket and the | numeric histogram(10,latency) _ |   |   |
| numeric histogram u(buckets, _ _ |   |   | Distribute all values of the Value field into multiple buckets. The buckets parameter specifies the number of buckets. The key of every bucket and the number of values in a bucket are returned. This function is equivalent to select count group by . Not e The returned data is in the format of multiple rows and columns. |   |   |   |   | method:POST \| select |   |   |
|   |   |   |   |   |   |   |   |   | method:POST \| select |   |
|   |   |   |   |   |   |   | s in a bucket are | numeric histogram(10,latency) _ |   |   |
|   | numeric histogram u(buckets, _ _ |   | ret |   |   |   |   |   |   |   |
| Value) |   |   |   |   | select count group by |   |   |   |   |   |

|   | approx percentile(x,percentage _ |   |
|---|---|---|
| ) |   |   |

|   | approx percentile(x, _ |   |
|---|---|---|
| percentages) |   |   |

|   | numeric histogram(buckets, _ |   |
|---|---|---|
| Value) |   |   |

> Not e The number of values in every bucket is evenly distributed. It is returned along with the average value of all values in a bucket.

#### 4.8.5 Mathematical statistics functions

This topic describes the syntax and examples of mathematical statistics functions. The search and analytics feature of Log Service allows you to use mathematical statistics functions for log analysis. The following table describes the supported mathematical statistics functions.

| Function |   | Description |   | Example |   |   |
|---|---|---|---|---|---|---|
| corr(y, x) |   | Returns the correlation coefficient of input values. The result ranges from 0 to 1. |   | latency>100\| select corr(latency,request size) _ |   |   |
| covar pop(y, x) _ |   | Returns the population covariance of |   | latency>100\| select |   |   |
|   |   |   |   |   | latency>100\| select |   |
|   |   |   | lation covariance of | covar pop(request size,latency) _ _ |   |   |
|   |   | input values. |   |   |   |   |
| covar samp(y, x) _ |   | Returns the sample covariance of |   | latency>100\| select |   |   |
|   |   |   |   |   | latency>100\| select |   |
|   |   |   | le covariance of | covar samp(request size,latency _ _ |   |   |
|   |   | input values. |   |   |   |   |
|   |   |   |   | ) |   |   |
| regr intercept(y, x) _ |   | Returns the linear regression intercept of input values. y is the dependent |   | latency>100\| select |   |   |
|   |   |   |   |   | latency>100\| select |   |
|   |   |   | is the dependent | regr intercept(request size,lat _ _ |   |   |
|   |   | value. x is the independent value. |   |   |   |   |
|   |   |   |   | ency) |   |   |
| regr slope(y,x) _ |   | Returns the linear regression slope of input values. y is the dependent |   | latency>100\| select |   |   |
|   |   |   |   |   | latency>100\| select |   |
|   |   |   | the dependent | regr slope(request size,latency _ _ |   |   |
|   |   | value. x is the independent value. |   |   |   |   |
|   |   |   |   | ) |   |   |
| stddev(x) or stddev samp(x) _ |   | Returns the sample standard deviation of the values in the x field. |   | latency>100\| select |   |   |
|   |   |   |   |   | latency>100\| select |   |
|   |   |   | alues in the x field. | stddev(latency) |   |   |
| stddev pop(x) _ |   | Returns the population standard deviation of the values in the x field. |   | latency>100\| select stddev pop(latency) _ |   |   |
| variance(x) or var samp(x) _ |   | Returns the sample variance of the values in the x field. |   | latency>100\| select variance(latency) |   |   |
| var pop(x) _ |   | Returns the population variance of the values in the x field. |   | latency>100\| select variance(latency) |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| result ranges from 0 | corr(latency,request size) _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| alues in the x field. | stddev pop(latency) _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| ld. | variance(latency) |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| x field. | variance(latency) |   |   |

#### 4.8.6 Mathematical calculation functions

This topic describes the syntax and examples of mathematical calculation functions. By including mathematical calculation functions in SQL statements, you can perform mathematical calculation on log query results. Mathematical operators Mathematical operators include the plus sign (+), minus sign (-), multiplication sign (*), division sign (/), and percent sign (%). These operators can be used in SELECT statements. Example:

```
*|select avg(latency)/100 , sum(latency)/count(1)
```

Log Service supports the following mathematical calculation functions.

| Function | Description |
|---|---|
| abs(x) | Returns the absolute values of the values in the x field. |
| cbrt(x) | Returns the cube roots of the values in the x field. |
| ceiling(x) | Returns the rounded-up nearest integers of the values in the x field. |
| cosine similarity(x,y) _ | Returns the cosine similarity between the sparse vectors x and y. |
| degrees | Converts angles in radians to degrees. |
| e() | Returns the Euler's number. |
| exp(x) | Returns Euler's number raised to the power of the values in the x field. |
| floor(x) | Returns the rounded-down nearest integers of the values in the x field. |
| from base(string,radix) _ | Returns the radix number representation of a string. |
| ln(x) | Returns the natural logarithm of x. |
| log2(x) | Returns the base 2 logarithm of x. |
| log10(x) | Returns the base 10 logarithm of x. |
| log(x,b) | Returns the base b logarithm of x. |
| pi() | Returns the constant Pi. |
| pow(x,b) | Returns x raised to the power of b. |
| radians(x) | Converts angle x in degrees to radians. |
| rand() | Returns a random number. |
| random(0,n) | Returns a random number from 0 to n (exclusive). |
| round(x) | Returns x rounded to the nearest integer. |
| round(x,y) | Returns x rounded to y decimal places. For example, round(1.012345,2) = 1.01. |
| sqrt(x) | Returns the square root of x. |
| to base(x,radix) _ | Returns the radix number representation of x. |
| truncate(x) | Returns x rounded to integer by dropping digits after the decimal point. |

| User Guide·Query and analysis | Log Servic |
|---|---|
| Function | Description |
| acos(x) | Returns the arc cosine of x. |
| asin(x) | Returns the arc sine of x. |
| atan(x) | Returns the arc tangent of x. |
| atan2(y,x) | Returns the arc tangent of y/x. |
| cos(x) | Returns the cosine of x. |
| sin(x) | Returns the sine of x. |
| cosh(x) | Returns the hyperbolic cosine of x. |
| tan(x) | Returns the tangent of x. |
| tanh(x) | Returns the hyperbolic tangent of x. |
| infinity() | Returns the value representing positive infinity. |
| is infinity(x) _ | Determines whether x is infinite. |
| is finity(x) _ | Determines whether x is finite. |
| is nan(x) _ | Determines whether x is not-a-number. |

#### 4.8.7 String functions

This topic describes string functions that Log Service supports for log data search and analytics. This following table lists the functions and their descriptions.

| Function | Description |
|---|---|
| chr(x) | Converts an integer to an ASCII character. For example, the result of chr(65) is A . |
| codepoint (x) | Converts an ASCII character to a code point of the integer type. For example, the result of codepoint('A') is 65 . |
| length(x) | Returns the length of a string. |
| levenshtein distance(string1, string2) _ | Returns the Levenshtein distance of string1 and string2. |
| lower(string) | Converts all uppercase characters in a string into lowercase characters. |
| lpad(string, size, padstring) | Pads a string to the specified size. If the length of the string is shorter than the specified size, padstring is used to left pad the string. If the length of the string is longer than the specified size, the string is truncated with the specified size. |
| rpad(string, size, padstring) | Right pads a string with the specified padding. The implementation is similar to that of the Ipad function. |

| og Service | User Guide·Query and analysi |
|---|---|

| Function | Description |
|---|---|
| ltrim(string) | Removes whitespace characters from the left side of a string. |
| replace(string, search) | Removes all occurrences of a substring search from a string. |
| replace(string, search,rep) | Replaces all occurrences of a substring search in a string with another substring rep. |
| reverse(string) | Reverses a string. |
| rtrim(string) | Removes whitespace characters from the right side of a string. |
| split(string,delimeter,limit) | Splits a string based on the specified delimiter and returns an array with the maximum number of elements at limit. The index of the first element in the array is 1. |
| split part(string,delimeter,offset) _ | Splits a string based on a delimiter into an array of substrings and returns the element with the index specified by the offset parameter. |
| split to map(string, entryDelimiter, _ _ keyValueDelimiter) → map<varchar, varchar> | Splits a string based on the entryDelemiter into multiple entries, each of which is then split based on the keyValueDelimiter into a key and value. This function returns a map. |
| position(substring IN string) | Returns the position of the first occurrence of the specified substring in a string. |
| strpos(string, substring) | Returns the position of the first occurrence of the specified substring in a string. Positions start with 1. If the substring is found, 0 is returned. |
| substr(string, start) | Returns a substring from the start position. Positions start with 1. |
| substr(string, start, length) | Returns a substring of a specified length from start position. Positions start with 1. The length parameter specifies the length of the substring returned. |
| trim(string) | Removes leading and trailing whitespace characters from a string. |
| upper(string) | Converts all lowercase characters in a string into uppercase characters. |
| concat(string,string...) | Concatenates multiple strings into a single string. |
| hamming distance (string1,string2) _ | Returns the Hamming distance of string1 and string2. |

|   | split to map(string, entryDelimiter, _ _ | entries, each of which is then split |
|---|---|---|
| keyValueDelimiter) → map<varchar, varchar> |   |   |

> Not e Strings must be enclosed in single quotation marks ('). Double quotation marks (") are used to enclose field names. For example, `a='abc'` indicates `field a = string 'abc'` , and `"a"="abc"`

|   | a='abc' |
|---|---|
| field a = field abc |   |

#### 4.8.8 Date and time functions

This topic describes the available time functions, date functions, interval functions, and a time series padding function in Log Service. You can use these functions when you analyze data. Date and time data types Unix timestamp: specifies the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC. The value is in the format of an integer. For example, `1512374067` indicates `Mon Dec 4 15:54:27 CST 2017` . The `__time` `__` field in every log entry is of this type. Timestamp: specifies the date and time in the format of a string. For example, `2017-11-01 13:30:00` . Date functions The following table lists the commonly used date functions that are supported in Log Service.

| Function |   |   | Description |   |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|
| current date _ |   |   | Returns the current date. |   |   |   | latency>100\| select current date _ |   |   |
| current time _ |   |   | Returns the current time. |   |   |   | latency>100\| select current time _ |   |   |
| current timestamp _ |   |   | Returns the current timestamp. This function is equivalent to the combination of the current date and _ current time functions. _ |   |   |   | latency>100\| select current timestamp _ |   |   |
| current timezone() _ |   |   | Returns the current time zone. |   |   |   | latency>100\| select current timezone() _ |   |   |
| from iso8601 timestamp(string) _ _ |   |   | Parses an ISO 8601 formatted string into a timestamp that specifies the |   |   |   | latency>100\| select |   |   |
|   |   |   |   |   |   |   |   | latency>100\| select |   |
|   | from iso8601 timestamp(string) _ _ |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | that specifies the | from iso8601 timestamp(iso8601) _ _ |   |   |
|   |   |   | time zone. |   |   |   |   |   |   |
| from iso8601 date(string) _ _ |   |   | Parses an ISO 8601 formatted string into a date. |   |   |   | latency>100\| select from iso8601 date(iso8601) _ _ |   |   |
| from unixtime(unixtime) _ |   |   | Parses a Unix timestamp into a timestamp. |   |   |   | latency>100\| select from unixtime(1494985275) _ |   |   |
| from unixtime(unixtime,string) _ |   |   | Parses a Unix timestamp into a timestamp based on the time zone that is specified by the string parameter. |   |   |   | latency>100\| select |   |   |
|   |   |   |   |   |   |   |   | latency>100\| select |   |
|   |   |   |   |   |   | on the time zone | from unixtime _ |   |   |
|   |   |   |   | at is specified by the string arameter. |   | y the string | _ |   |   |
|   |   |   |   |   |   |   | (1494985275,'Asia/Shanghai') |   |   |
| localtime |   |   | Returns the local time. |   |   |   | latency>100\| select localtime |   |   |
| localtimestamp |   |   | Returns the local timestamp. |   |   |   | latency>100\| select localtimestamp |   |   |
| now() |   |   | Returns the current date and time. This function is equivalent to the current timestamp function. _ |   |   |   | N/A |   |   |
| to unixtime(timestamp) _ |   |   | Parses a timestamp into a Unix |   |   |   | *\| select to unixtime('2017- _ |   |   |
|   |   |   |   |   |   |   |   | *\| select to unixtime('2017- _ |   |
|   |   |   |   |   | a timestamp into a Unix |   | 05-17 09:45:00.848 |   |   |
|   |   |   | timestamp. |   | amp. |   |   |   |   |
|   |   |   |   |   |   |   | Asia/Shanghai') |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| nt date. | current date _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| nt time. | current time _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| he current date and _ | current timestamp _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
| nt time zone. | current timezone() _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
|   | from iso8601 date(iso8601) _ _ |   |   |

|   |   | latency>100\| select |   |
|---|---|---|---|
|   | from unixtime(1494985275) _ |   |   |

|   | from unixtime(unixtime,string) _ |
|---|---|

| ns the local time. |   |   |
|---|---|---|

|   |   | latency>100\| select |   |
|---|---|---|---|
| timestamp. | localtimestamp |   |   |

Time functions The following table lists the time functions that you can use in Log Service to parse time in the formats supported in MySQL, such as %a, %b, and %y.

| Function |   |   |   |   |   | Description |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| date format(timestamp, _ |   |   |   |   |   | Formats a timestamp in the specified |   |   | latency>100 \| select |   |   |
|   | date format(timestamp, _ |   |   |   |   |   |   | ified | date format (date parse('2017- _ _ |   |   |
| format) |   |   |   |   |   | format. |   |   | 05-17 09:45:00','%Y-%m-%d |   |   |
|   |   |   |   |   |   |   |   |   | %H:%i:%S'), '%Y-%m-%d') |   |   |
| date parse(string, format) _ |   |   |   |   |   | Parses a formatted string into a timestamp. |   |   | latency>100 \| select |   |   |
|   |   |   |   |   |   |   |   |   |   | latency>100 \| | select |
|   |   |   |   |   |   |   |   |   | date format _ |   |   |
|   |   |   |   |   |   |   |   |   | (date parse(time,'%Y-%m-%d _ |   |   |
|   |   |   |   |   |   |   |   |   | _ |   |   |
|   |   |   |   |   |   |   |   |   | %H:%i:%S'), '%Y-%m-%d') |   |   |

Formats

| Format | Description |
|---|---|
| %a | The week day in abbreviation, such as Sun and Sat. |
| %b | The month in abbreviation, such as Jan and Dec. |
| %c | The month in the numeric format. Valid values: 1 to 12. |
| %D | The day of the month with a suffix, such as 0th, 1st, 2nd, and 3rd. |
| %d | The day of the month in the numeric format. Valid values: 01 to 31. |
| %e | The day of the month in the numeric format. Valid values: 1 to 31. |
| %H | The hour that applies the 24-hour clock convention. Valid values: 00 to 23. |
| %h | The hour that applies the 12-hour clock convention. Valid values: 01 to 12. |
| %I | The hour that applies the 12-hour clock convention. Valid values: 1 to 12. |
| %i | The minute in the numeric format. Valid values: 00 to 59. |
| %j | The day of the year. Valid values: 001 to 366. |
| %k | The hour. Valid values: 0 to 23. |
| %l | The hour. Valid values: 1 to 12. |
| %M | The month. Valid values: January to December. |
| %m | The month in the numeric format. Valid values: 01 to 12. |
| %p | The abbreviation that indicates the morning or afternoon. Valid values: a.m. and p.m.. |
| %r | The time that applies the 12-hour clock convention: hh:mm:ss AM/PM . |
| %S | The second. Valid values: 00 to 59. |
| %s | The second. Valid values: 00 to 59. |

| User Guide·Query and analysis | Log Servic |
|---|---|

| Format | Description |
|---|---|
| %T | The time that applies the 24-hour clock convention, formatted in hh:mm:ss . |
| %U | The week of the year. Sunday is the first day of a week. Valid values: 00 to 53. |
| %u | The week of the year. Monday is the first day of a week. Valid values: 00 to 53. |
| %V | The week of the year. Sunday is the first day of a week. This format is used together with %X. Valid values: 01 to 53. |
| %v | The week of the year. Monday is the first day of a week. This format is used in combination with %x. Valid values: 01 to 53. |
| %W | The day of the week. Valid values: Sunday to Saturday. |
| %w | The day of the week. Valid values: 0 to 6. The value 0 indicates Sunday. |
| %Y | The year in the 4-digit format. |
| %y | The year in the 2-digit format. |
| %% | Escapes the second percent sign (%). |

Truncation functions Log Service supports a truncation function, which can truncate a time by the second, minute, hour, day, month, or year. Typically, this function is used for time-based analytics. Syntax

```
date_trunc(unit, x)
```

Parameters The value of the x parameter can be a timestamp or Unix timestamp. The following table lists the values of the unit parameter and the responses when the x parameter is set to `20`

```
01-08-22 03:04:05.000 .
```

| Unit | Response |
|---|---|
| second | 2001-08-22 03:04:05.000 |
| minute | 2001-08-22 03:04:00.000 |
| hour | 2001-08-22 03:00:00.000 |
| day | 2001-08-22 00:00:00.000 |
| week | 2001-08-20 00:00:00.000 |
| month | 2001-08-01 00:00:00.000 |
| quarter | 2001-07-01 00:00:00.000 |
| year | 2001-01-01 00:00:00.000 |

Example The date_trunc function is applicable only to analytics at a fixed time interval. To implement analytics at a flexible interval, for example, every 5 minutes, you need to use a GROUP BY clause according to the mathematical modulus method.

```
* | SELECT count(1) as pv,  __time__ - __time__% 300 as minute5 group by minute5 limit 100
```

In the preceding statement, %300 indicates that modulo and truncation are performed every 5 minutes. The following example shows how to use the date_trunc function:

```
*|select date_trunc('minute' , __time__) as t,
       truncate (avg(latency) ) ,
       current_date
       group by   t
       order by t  desc
       limit 60
```

Interval functions Interval functions perform interval-related calculation. For example, you can use interval functions to add or subtract an interval based on a date, or calculate the interval between two dates.

| Function |   |   |   |   | Description |   |   |   |   |   |   |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| date add (unit, value, _ |   |   |   |   | Adds an interval value of the |   |   |   |   |   |   |   |   | date add('day', -7, '2018-08- |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | date add('day', -7, '2018-08- |   |
|   |   | date add _ | (unit, value, |   |   |   | unit |   |   |   |   |   |   | _ 09 00:00:00') : indicates seven days before August 9. |   |   |
| timestamp) |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| date diff(unit, timestamp1, _ |   |   |   |   | Returns the time difference between timestamp1 and timestamp2 |   |   |   |   |   |   |   |   | date diff('day', '2018-08-02 _ |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | date diff('day', '2018-08-02 _ |   |
|   |   |   |   |   | Return time |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | time |   | stamp1 | and | timestamp2 |   |   |   | 00:00:00', '2018-08-09 |   |   |
| timestamp2) |   |   |   |   | expressed in terms of |   |   |   |   |   | unit | . |   | 00:00:00') = 7 |   |   |

The following table lists the values of the unit parameter that are supported by the interval functions.

| Value | Description |
|---|---|
| millisecond | The millisecond. |
| second | The second. |
| minute | The minute. |
| hour | The hour. |
| day | The day. |
| week | The week. |
| month | The month. |
| quarter | The quarter, namely, three months. |
| year | The year. |

Time series padding function The time series padding function is used to pad time series and corresponding data.

> Not e This function must be used in combination with the `group by time order by time` clause. When used together, the `order by` clause does not support the `desc` sorting method.

Syntax

```
time_series(time_column, window, format, padding_data)
```

Parameters

| Parameter | Description |
|---|---|
| timecolumn _ | The name of the time field in a log entry. The default field name is time __ _ . The field value is of the LONG or TIMESTAMP type. _ |
| window | The time window for a data query. It is composed of a number and a unit. Unit: s (seconds), m (minutes), H (hours), and d (days). For example, 2h, 5m, or 3d. |
| format | The MySQL time format displayed. |
| paddingdata _ | The content to be added for a time point. Valid values: 0: adds 0. null: adds null. last: adds the value corresponding to the last time point. next: adds the value corresponding to the next time point. avg: adds the average value of the last and next values. |

|   | _ |
|---|---|

Example The following statement is used to format data every 2 hours:

```
* | select time_series(__time__, '2h', '%Y-%m-%d %H:%i:%s', '0')  as stamp, count(*) as num from lo
g group by stamp order by stamp
```

#### 4.8.9 URL functions

This topic describes the syntax of URL functions and provides examples. URL functions extract fields from standard URLs. A standard URL is described as follows:

```
[protocol:][//host[:port]][path][? query][#fragment]
```

Common URL functions

|   |   | Function |   |   | Description |   |   | Example |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | Statement |   |   |   |   |   | Response |   |   |
|   |   | url extract |   |   | Extracts the fragment identifier from a URL and |   |   | *\| select |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | *\| select |   |   |   |   |   | /project/da |   |
|   |   |   | url extract |   | identifier from |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | URL and | url extract fragment('https://sls.co |   |   |   |   |   |   |   |   |
|   |   | _ |   |   |   |   |   |   |   |   |   |   | nsole.ali | shboard- |   |   |
|   |   | fragment(ur _ |   |   |   | returns the fragment | ment | _ _ |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | yun.com/#/project/dashboard- |   |   |   |   |   |   | demo/categor |   |
|   |   | l) |   |   | identifier of the |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | VARCHAR type. |   |   | demo/categoryLis |   | t') |   |   |   | yList |   |   |

|   |   | Function |   |   |   | Description |   |   |   | Example |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | Statement |   |   |   |   |   |   |   | Response |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the host information from a URL and returns the host |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   | www.aliyun. |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | informati and retur |   |   |   |   |   |   |   |   |   |   |   |   | www.aliyun. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ost | url extract host('http://www.aliyun.com/produ _ _ |   |   |   |   |   |   |   |   | www. |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   |   |   |   | com/produ |   | com |   |   |   |   |   |   |   |   |   |
|   |   | host(url) _ |   |   |   | information of the |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ct/sls') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | VARCHAR type. |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the value of the name parameter in the query from a URL and |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | name parameter in the |   |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | parameter(u _ |   |   |   |   |   |   |   | url extract parameter('http://www.aliyun.com/ _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | query fr | om a URL |   |   |   |   |   |   |   |   |   |   |   | testuser |   |   |   |   |   |   |   |   |
|   |   | rl, name) |   |   |   |   |   |   |   | product/sls?userid=testuser','userid') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | VARCHAR type. |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the path from a URL and returns the path |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | Extracts t URL and r |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | he path | url extract path('http://www.aliyun.com/produ _ _ |   |   |   |   |   |   |   |   | /product/sl |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   |   |   |   | com/produ |   | s |   |   |   |   |   |   |   |   |   |
|   |   | path(url) _ |   |   |   | of the VARCHAR type. |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ct/sls?userid=testuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the port number from a URL and |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | number fr |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | RL and | url extract port('http://www.aliyun.com:80/pr _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 80 |   |   |   |   |   |   |   |   |
|   |   | port(url) _ |   |   |   | returns the port number of the BIGINT type. |   |   | umber | _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | oduct/sls?userid=testuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the protocol from a URL and returns |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | Extracts the pr from a URL an |   |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | protocol(ur _ |   |   |   |   |   |   | turns | url extract protocol('http://www.aliyun.com:8 _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | http |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | he |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | l) |   |   |   |   |   |   |   | 0/product/sls?userid=testuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url extract _ |   |   |   | Extracts the query string from a URL and returns |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | url extract _ |   |   | from a URL |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | turns | url extract query('http://www.aliyun.com:80/p _ _ |   |   |   |   |   |   |   |   | userid=test |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   |   |   |   | .com:80/p |   | user |   |   |   |   |   |   |   |   |   |
|   |   | query(url) _ |   |   |   | the query string of the VARCHAR type. |   |   | f the |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | roduct/sls?userid=testuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | url encode( _ |   |   |   | Encodes a URL. |   |   |   | *\|select |   |   |   |   |   |   |   | http%3a%2f% |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | http%3a%2f% |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   | 2fwww.aliyun |   |   |   |   |   |   |   |   |   |
|   |   |   | url encode( _ |   |   | Enco |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | url encode('http://www.aliyun.com:80/product/ _ |   |   |   |   |   |   |   | .com%3a80%2f |   |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   | http://www.aliyun.com:80/product/ |   | liyun.com:80/product/ |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | value) |   |   |   |   |   |   |   | _ |   |   |   |   |   |   |   | product%2fsl |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | sls?userid=testuser') |   | estuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | s%3fuserid%3 |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | dtestuser |   |   |   |   |   |   |   |   |   |
|   |   | url decode( _ |   |   |   | Decodes a URL. |   |   |   | *\|select |   |   |   |   |   |   |   | http://www. |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | http://www. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|select |   |   |   |   |   |   | aliyun.com:8 |   |   |   |   |   |   |   |   |   |
|   |   |   | url decode( _ |   |   | Deco |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | url decode('http%3a%2f%2 |   |   |   |   |   |   |   | 0/product/sl |   |   |   |   |   |   |   |   |   |
|   |   |   | _ |   |   |   |   |   |   |   |   |   | http%3a%2f%2 |   | fwww.aliyun.com%3a80% |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | value) |   |   |   |   |   |   |   | _ |   |   |   |   |   |   |   | s? |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | 2fproduct% |   | 2fsls%3fuserid%3dtestuser') | sls%3fuserid%3dtestuser') |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | userid=testu |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ser |   |   |   |   |   |   |   |   |   |

#### 4.8.10 Regular expression functions

This topic describes the available regular expression functions. You can use these functions when you query and analyze data in Log Service. A regular expression function parses a string and returns the required substrings. The following table lists common regular expression functions.

| Function |   |   |   |   | Description |   |   | Example |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| regexp extract all(string _ _ , pattern) |   |   |   |   | Returns an array where each element is a substring that |   |   | The returned result of *\| SELECT regexp extract all('5a 67b 890m', _ _ '\d+') is ['5','67','890'] . The returned result of *\|SELECT regexp extract all('5a _ _ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\| SELECT |   |
|   |   |   |   |   |   | hat |   | regexp extract all('5a 67b 890m', _ _ |   |   |   |   |
|   | regexp extract all(string _ _ |   |   |   | element is |   |   |   |   |   |   |   |
|   |   |   |   |   | matches t |   |   | '\d+') | is | ['5','67','890'] |   |   |
|   |   |   |   |   | These substrings derive from |   |   | result of | *\|SELECT regexp extract all('5a _ _ |   |   |   |
|   |   |   |   |   | the specified string. |   |   | 67a 890m', '(\d+)a') |   |   |   |   |
| regexp extract all(string _ _ , pattern, group) |   |   |   |   | Returns an array where each element is a part of a substring that matches the regular expression. This part is the |   |   | The returned result of *\| SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\| SELECT |   |
|   |   |   |   |   |   | he |   | regexp extract all('5a 67a 890m', _ _ |   |   |   |   |
|   |   |   |   |   | content in the group parameter value of the () of a |   |   | '(\d+)a',1) |   |   |   |   |
|   |   |   |   |   | substring that derives from the specified string. |   |   |   |   |   |   |   |
| regexp extract(string, _ pattern) |   |   |   |   | Returns the first substring of the specified string that matches the regular expression. |   |   | The returned result of *\|SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   |   |   |   | regexp extract('5a 67b 890m', '\d+') _ |   |   |   |   |
| regexp extract(string, _ pattern,group) |   |   |   |   | Returns a part of the first substring that matches the regular expression. This part is the content in the group |   |   | The returned result of *\|SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   | regular exp the content |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | regexp extract('5a 67b 890m', '(\d+)([a- _ |   |   |   |   |
|   |   |   |   |   | parameter value of the | () |   | z]+)',2) |   |   |   |   |
|   |   |   |   |   | of the substring that derives from the specified string. |   |   |   |   |   |   |   |
| regexp like(string, _ pattern) |   |   |   |   | Returns a Boolean value. If the string and its substrings cannot match the regular expression, the value False is returned. |   |   | The returned result of *\|SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   |   | ssion, |   | regexp like('5a 67b 890m', '\d+m') _ |   |   |   |   |
| regexp replace(string, _ pattern, replacement) |   |   |   |   | Replaces the substrings of the specified string that match the regular expression with the |   |   | The returned result of *\|SELECT regexp replace('5a 67b 890m', _ '\d+','a') is 'aa ab am' . |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   | specified string tha regular expression |   |   |   |   |   |   |   |
|   |   |   |   |   |   | the |   | regexp replace('5a 67b 890m', _ |   |   |   |   |
|   |   |   |   |   | value of the replacement |   |   | '\d+','a') |   |   |   |   |
|   |   |   |   |   | parameter. |   |   |   |   |   |   |   |
| regexp replace(string, _ pattern) |   |   |   |   | Removes the substrings of the specified string that match the regular expression. This function is equivalent to regexp replace(string,pat _ |   |   | The returned result of *\|SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   |   |   |   | regexp replace('5a 67b 890m', '\d+') _ |   |   |   |   |
|   |   |   |   |   |   |   |   | 'a b |   |   |   |   |
|   |   |   |   |   | term,'') |   |   |   |   |   |   |   |
| regexp split(string, _ pattern) |   |   |   |   | Returns an array where each element is a substring of the specified string that is split based on the regular expression. |   |   | The returned result of *\|SELECT |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | *\|SELECT |   |
|   |   |   |   |   |   | plit |   | regexp split('5a 67b 890m', '\d+') _ |   |   |   |   |

| regexp extract(string, _ | Ret the |
|---|---|

| regexp like(string, _ |   |
|---|---|

| regexp replace(string, _ | reg |
|---|---|

| regexp split(string, _ | el s |
|---|---|

#### 4.8.11 JSON functions

JSON functions can convert a string into a JSON type and extract JSON fields. The two major JSON data types are map and array. If a string cannot be converted to a value of the JSON type, null value is returned. For information about how to expand JSON data into multiple rows, see UNNEST function. The following table lists the JSON functions that Log Service supports:

| Function |   |   |   |   |   | Description |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| json parse(string) _ |   |   |   |   |   | Converts a string to a JSON- formatted data. |   |   | SELECT json parse('[1, 2, _ 3]') : returns a JSON array. |   |   |
| json format(json) _ |   |   |   |   |   | Converts JSON-formatted data to a string. |   |   | SELECT |   |   |
|   |   |   |   |   |   |   |   |   |   | SELECT |   |
|   |   |   |   |   |   |   |   | o a | json format(json parse('[1, 2, _ _ |   |   |
|   |   |   |   |   |   |   |   |   | 3]')) |   |   |
| json array contains(json, _ _ value) |   |   |   |   |   | Determines whether a value exists in |   |   | SELECT |   |   |
|   |   |   |   |   |   |   |   |   |   | SELECT |   |
|   |   |   |   |   |   |   |   | s in | json array contains(json parse( _ _ _ |   |   |
|   | json array contains(json, _ _ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | a JSON array or in a string that |   |   |   |   |
| _ value) | _ |   |   |   |   |   |   |   | '[1, 2, 3]'), 2) or SELECT |   |   |
|   |   | ) |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | contains a JSON array. |   |   | json array contains('[1, 2, _ _ |   |   |
|   |   |   |   |   |   |   |   |   | _ |   |   |
|   |   |   |   |   |   |   |   |   | 3]', 2) |   |   |
| json array get(json array, _ _ _ index) |   |   |   |   |   | Retrieves the element at the specified index in the JSON array. This function is equivalent to json array contains . _ _ |   |   | SELECT json array get('["a", _ _ "b", "c"]', 0): returns 'a' |   |   |
| json array length(json) _ _ |   |   |   |   |   | Returns the length of the JSON array. |   |   | SELECT json array length('[1, _ _ 2, 3]'): returns 3 |   |   |
| json extract(json, _ json path) _ |   |   |   |   |   | Extracts a value from a JSON object and returns a JSON object. The json path expression works in a _ similar manner to $.store.book[0].title . |   |   | SELECT json extract(json, _ '$.store.book') |   |   |
| json extract scalar(json, _ _ json path) _ |   |   |   |   |   | Returns a string. This function works in a similar manner to json extract ). _ |   |   | N/A |   |   |
| json size(json,json path) _ _ |   |   |   |   |   | Retrieves the length of a JSON object or array. |   |   | SELECT json size('[1, 2, _ 3]'): returns 3. |   |   |

| data. | 3]') |
|---|---|

|   | json array get(json array, _ _ _ |   |
|---|---|---|
| index) |   |   |

|   |   |   | SELECT json array get('["a", _ _ |
|---|---|---|---|
|   | valent to | "b", "c"]', 0): returns 'a' |   |
| json array contains _ _ |   |   |   |

|   |   | SELECT json array length('[1, _ _ |
|---|---|---|
| ns the length of the JSON array. | 2, 3]'): returns 3 |   |

|   | json extract(json, _ |
|---|---|
| json path) _ |   |

|   |   | SELECT json extract(json, _ |   |
|---|---|---|---|
| expression works in a nner to | '$.store.book') |   |   |

|   | json extract scalar(json, _ _ | Ret in a |
|---|---|---|
| json path) _ |   |   |

|   |   | SELECT json size('[1, 2, _ |   |
|---|---|---|---|
|   | 3]'): returns 3. |   |   |

#### 4.8.12 Type conversion functions

Type conversion functions convert the data type of a specified value or column in a query. You can use the index attribute feature of Log Service to set the data type of a field to LONG, DOUBLE, TEXT, or JSON. You can also query fields of various data types, including BIGINT, DOUBLE, VARCHAR, and TIMESTAMP. To query fields of a specific data type, you can use type conversion functions to convert the data type configured in an index into the data type that you use in a query. Syntax

> Not e We recommend that you use the try_cast() function if a log contains dirty data. Otherwise, a query may fail due to the dirty data.

Convert the data type of a column of values or a specific value into the specified type in a query. If the data type of a value fails to be converted, the query is terminated.

```
cast([key|value] AS type)
```

Convert the data type of a column of values or a specific value into the specified type in a query. If the data type of a value fails to be converted, NULL is returned for the value, and the query continues.

```
try_cast([key|value] AS type)
```

| Parameter | Description |
|---|---|
| key | The key of a field whose value data type is to be converted. |
| value | The field value whose data type is to be converted into the specified type. |

Example To convert the numeric value 123 to a value of the VARCHAR type, use the following statement:

```
cast(123 AS varchar)
```

To convert the data type of the uid field values to the VARCHAR type, use the following statement:

```
cast(uid AS varchar)
```

#### 4.8.13 IP functions

This topic describes the syntax of IP functions and provides examples. IP functions can identify whether an IP address is an intranet or Internet IP address. IP functions can also identify the country, province, and city where an IP address resides. For information about geohash functions, see Geography functions.

| Function | Description | Example |
|---|---|---|
| ip to domain(ip) _ _ | Identifies whether an IP address is an intranet or Internet IP address. This function returns intranet or internet. | SELECT ip to domain(ip) _ _ |
| ip to country(ip) _ _ | Identifies the country where an IP address resides. | SELECT ip to country(ip) _ _ |
| ip to province(ip) _ _ | Identifies the province where an IP address resides. | SELECT ip to province(ip) _ _ |
| ip to city(ip) _ _ | Identifies the city where an IP address resides. | SELECT ip to city(ip) _ _ |
| ip to geo(ip) _ _ | Identifies the longitude and latitude of the city where an IP address resides. The result is returned in the format of latitude, longitude . | SELECT ip to geo(ip) _ _ |
| ip to city geo(ip) _ _ _ | Identifies the longitude and latitude of the city where an IP address resides. Each city has only one longitude and latitude. The result is returned in the format of latitude, longitude . | SELECT ip to city geo(ip) _ _ _ |
| ip to provider(ip) _ _ | Identifies the network service provider that assigns an IP address. | SELECT ip to provider(ip) _ _ |

| Function | Description | Example |
|---|---|---|
| ip to country(ip,'en') _ _ | Identifies the country where an IP address resides. The function returns a country code. | SELECT ip to country(ip,'en') _ _ |
| ip to country code(ip) _ _ _ | Identifies the country where an IP address resides. The function returns a country code. | SELECT ip to country code(ip) _ _ _ |
| ip to province(ip,'en') _ _ | Identifies the province where an IP address resides. | SELECT ip to province(ip,'en') _ _ |
| ip to city(ip,'en') _ _ | Identifies the city where an IP address resides. | SELECT ip to city(ip,'en') _ _ |

|   |   | SELECT |
|---|---|---|
| urns | ip to country(ip,'en') _ _ |   |

|   |   | SELECT |
|---|---|---|
| urns | ip to country code(ip) _ _ _ |   |

|   |   | SELECT |
|---|---|---|
|   | ip to province(ip,'en') _ _ |   |

Example To query the number of requests that are not sent from an intranet, run the following statement:

```
* | SELECT count(1) where ip_to_domain(ip)! ='intranet'
```

To query the top 10 provinces from which requests are sent, run the following statement:

```
* | SELECT count(1) as pv, ip_to_province(ip) as province GROUP BY province order by pv desc limit
```

Sample response `[` `{`

```json
        "__source__": "",
        "__time__": "1512353137",
        "province": "Zhejiang",
        "pv": "4045"
    }, {
        "__source__": "",
        "__time__": "1512353137",
        "province": "Shanghai",
        "pv": "3727"
    }, {
        "__source__": "",
        "__time__": "1512353137",
        "province": "Beijing",
        "pv": "954"
    }, {
        "__source__": "",
        "__time__": "1512353137",
        "province": "intranet IP address",
        "pv": "698"
    }, {
        "__source__": "",
        "__time__": "1512353137",
        "province": "Guangdong",
        "pv": "472"
    }, {
        "__source__": "",
        "__time__": "1512353137",
        "province": "Fujian",
        "pv": "71"
```

`}` `]` The response contains an intranet IP address. You can use the SELECT statement to filter requests that are sent from the IP address. To query the top 10 provinces from which intranet requests are sent, run the following statement:

```
* | SELECT count(1) as pv, ip_to_province(ip) as province WHERE ip_to_domain(ip) ! = 'intranet'  GR
OUP BY province ORDER BY pv desc limit 10
```

To query the average request latency, the maximum request latency, and the request with the maximum latency from each country, run the following statement:

```
* | SELECT AVG(latency),MAX(latency),MAX_BY(requestId, latency) ,ip_to_country(ip) as country group
by country limit 100
```

To query the average latency of requests supported by each network service provider, run the following statement:

```
* | SELECT AVG(latency) , ip_to_provider(ip) as provider group by provider limit 100
```

To query the longitude and latitude of the city to which an IP address belongs and show the city on a map, run the following statement:

```
* | SELECT count(1) as pv , ip_to_geo(ip) as geo group by geo order by pv desc
```

The following table shows the format of the result.

| pv | geo |
|---|---|
| 100 | 35.3284,-80.7459 |

#### 4.8.14 GROUP BY syntax

This topic describes the GROUP BY syntax. GROUP BY statements support multiple columns. A GROUP BY statement allows you to specify a column alias in a SELECT statement to as the corresponding KEY. Example:

```
method:PostLogstoreLogs |select avg(latency),projectName,date_trunc('hour',__time__) as hour group b y projectName,hour
```

The hour alias indicates the third SELECT column `date_trunc('hour',__time__)` . This improves the performance of complicated queries. The GROUP BY statement supports the GROUPING SETS, CUBE, and ROLLUP clauses. Example:

```
method:PostLogstoreLogs |select avg(latency) group by cube(projectName,logstore) method:PostLogstoreLogs |select avg(latency) group by GROUPING SETS ( ( projectName,logstore), (proj ectName,method)) method:PostLogstoreLogs |select avg(latency) group by rollup(projectName,logstore)
```

Examples Use GROUP BY based on time Each log has a built-in time column named `__time__` . When the analytics feature is enabled on one of the columns, the statistics of the time column are included.

| The | date trunc _ |
|---|---|
| nc | function acce |

The `date_trunc` function can truncate the time column to minute, hour, day, month, and year. The `date_tru` `nc` function accepts an aligned unit and a column of the Unix timestamp type, such as `__time__` . PV statistics per hour and per minute

```
* | SELECT count(1) as pv , date_trunc('hour',__time__) as hour group by hour order by hour limit
* | SELECT count(1) as pv , date_trunc('minute',__time__) as minute group by minute order by minu
te limit 100
```

> Not e 100 specifies that up to 100 rows can be retrieved. If a LIMIT clause is not specified, up to 10 rows of data are retrieved by default.

date_trunc functions are available only for statistics at a fixed time interval. For statistics based on flexible time dimensions, for example, every 5 minutes, run a GROUP BY statement based on the mathematical modulus method.

```
* | SELECT count(1) as pv,  __time__ - __time__% 300 as minute5 group by minute5 limit 100
```

In the preceding statement, %300 indicates that the time is truncated in mod every 5 minutes. Retrieve non-aggregation columns from a GROUP BY statement In standard SQL, if a GROUP BY statement is used during the SELECT operation, Log Service selects only the raw data of the column specified in the GROUP BY statement or performs aggregation on any columns. For example, the following statement is invalid. Log Service cannot determine which row of b to return during the GROUP BY operation based on a, because b is not a GROUP BY column.

```
*|select a, b , count(c) group by a
```

Instead, you can use the `arbitrary()` function to return b.

```
*|select a, arbitrary(b), count(c) group by a
```

#### 4.8.15 Window functions

This topic describes the syntax for window functions. Window functions are used to perform calculations across rows of a log. Common SQL aggregate functions calculate the results of only one row or aggregate all rows into one row for calculation. Window functions support cross-row calculation and fill the calculation results in each row. Syntax for window functions is

```
SELECT key1, key2, value,
       rank() OVER (PARTITION BY key2
                    ORDER BY value DESC) AS rnk
FROM orders ORDER BY key1,rnk
```

The important part is

```
rank() OVER (PARTITION BY KEY1 ORDER BY KEY2 DESC)
```

rank() is an aggregate function. You can use any functions in analysis syntax or the function listed in this topic. PARTITION BY indicates the buckets based on which values are calculated. Special aggregate functions used in windows

| Function | Description |
|---|---|
| rank() | Returns the rank of a value within a group of values. The rank is one plus the number of preceding rows that are not peers of the current row. |
| row number() _ | Returns a unique, sequential number for each row. |
| first value(x) _ | Returns the first value of the window. In most cases, the function is used to obtain the maximum value after the values of the window are sorted. |
| last value(x) _ | Returns the last value of the window. In most cases, the function is used to obtain the minimum value after the values of the window are sorted. |
| nth value(x, offset) _ | Returns the value at the specified offset from the beginning of the window. |
| lead(x,offset,defaut value) _ | Returns the value at offset rows after the current row in the window. If the target row does not exist, the default value is returned. _ |

| Function | Description |
|---|---|
| lag(x,offset,defaut value) _ | Returns the value at offset rows after the current row in the window. If the target row does not exist, the default value is returned. _ |

Example Rank the salaries of employees in their respective departments

```
* | select department, persionId, sallary , rank() over(PARTITION BY department order by sallary de
sc) as sallary_rank order by department,sallary_rank
```

Results

| department | persionId | sallary | sallary rank _ |
|---|---|---|---|
| dev | john | 9000 | 1 |
| dev | Smith | 8000 | 2 |
| dev | Snow | 7000 | 3 |
| dev | Achilles | 6000 | 4 |
| Marketing | Blan Stark | 9000 | 1 |
| Marketing | Rob Stark | 8000 | 2 |
| Marketing | Sansa Stark | 7000 | 3 |

Calculate the salaries of employees as percentages in their respective departments

```
* | select department, persionId, sallary *1.0 / sum(sallary) over(PARTITION BY department ) as sal
lary_percentage
```

Results

| department | persionId | sallary | sallary percentage _ |
|---|---|---|---|
| dev | john | 9,000 | 0.3 |
| dev | Smith | 8,000 | 0.26 |
| dev | Snow | 7000 | 0.23 |
| dev | Achilles | 6000 | 0.2 |
| Marketing | Blan Stark | 9000 | 0.375 |
| Marketing | Rob Stark | 8000 | 0.333 |
| Marketing | Sansa Stark | 7000 | 0.29 |

Calculate the daily UV increase over the previous day

```
* | select day ,uv, uv *1.0 /(lag(uv,1,0) over() ) as diff_percentage from
```

`(`

```
select approx_distinct(ip) as uv, date_trunc('day',__time__) as day from log group by day order by day asc
```

`)` Results

| day | uv | diff percentage _ |
|---|---|---|
| 2017-12-01 00:00:00 | 100 | null |
| 2017-12-02 00:00:00 | 125 | 1.25 |
| 2017-12-03 00:00:00 | 1,500 | 1.2 |
| 2017-12-04 00:00:00 | 175 | 1.16 |
| 2017-12-05 00:00:00 | 2,000 | 1.14 |
| 2017-12-06 00:00:00 | 225 | 1.125 |
| 2017-12-07 00:00:00 | 250 | 1.11 |

#### 4.8.16 HAVING syntax

This topic describes the HAVING syntax. The LogSearch/Analytics feature of Log Service supports the standard SQL HAVING clause. The HAVING clause is used with the GROUP BY statement to filter GROUP BY results. Example:

```
method :PostLogstoreLogs |select avg(latency),projectName group by projectName HAVING avg(latency) >
```

Difference between HAVING and WHERE clauses The HAVING clause is used to filter the aggregation and calculation results after you run the GROUP BY statement. The WHERE clause is used to filter the raw data during the aggregation calculation. Example Calculate the average rainfall of each province where the temperature is higher than 10°C, and only show the provinces with average rainfall greater than 100 mL in the final results:

```
* | select avg(rain) ,province where temperature > 10 group by province having avg(rain) > 100
```

#### 4.8.17 ORDER BY syntax

This topic describes the ORDER BY syntax. The ORDER BY keyword is used to sort output results. You can sort output results based on only one column. Syntax format

```
order by column name [desc|asc]
```

Example

```
method :PostLogstoreLogs |select avg(latency) as avg_latency,projectName group by projectName HAVING avg(latency) > 5700000 order by avg_latency desc
```

#### 4.8.18 LIMIT syntax

The LIMIT clause is used to limit the number of returned rows. Syntax formats Log Service supports the following LIMIT syntax formats: Reads only the first N rows:

```
limit N
```

Reads N rows starting from the S-th row:

```
limit S , N
```

> Not e
> If you use the LIMIT clause to paginate results, the final results rather than the intermediate results of the SQL query are obtained.
> You cannot apply the LIMIT clause to subqueries. For example, the following statement is not supported:

```
* | select count(1) from ( select distinct(url) from limit 0,1000)
```

> If you use the LIMIT clause for pagination, the offset value cannot exceed 1,000,000. For example, in the
> `limit S , N` clause, the sum of S and N cannot exceed 1,000,000, and the value of N cannot exceed 10,000.

Example To obtain the first 100 rows of results, run the following statement.

```
* | select distinct(url) from log limit 100
```

To obtain a total of 1,000 results from row 0 to row 999, run the following statement.

```
* | select distinct(url) from log limit 0,1000
```

To obtain a total of 1,000 results from row 1,000 to row 1,999, run the following statement:

```
* | select distinct(url) from log limit 1000,1000
```

#### 4.8.19 Syntax for CASE statements and if() functions

This topic describes the syntax for CASE statements and if() functions. CASE statements are used to classify continuous data. For example, you can use the following CASE statement to extract information from http_user_agent and classify the information into two types: Android and iOS.

```
SELECT
 CASE
 WHEN http_user_agent like '%android%' then 'android'
 WHEN http_user_agent like '%ios%' then 'ios'
 ELSE 'unknown' END
 as http_user_agent,
    count(1) as pv
    group by  http_user_agent
```

Examples Calculate the ratio of requests whose status code is 200 to all requests

```
* | SELECT
 sum(
 CASE
 WHEN status =200 then 1
 ELSE 0 end
 ) *1.0 / count(1) as status_200_percentage
```

Calculate the distribution of latencies

```
* | SELECT `
 CASE
 WHEN latency < 10 then 's10'
 WHEN latency < 100 then 's100'
 WHEN latency < 1000 then 's1000'
 WHEN latency < 10000 then 's10000'
 else 's_large' end
 as latency_slot,
 count(1) as pv
 group by latency_slot
```

Syntax for if() functions An if() function works in the same way as a CASE statement does.

```
CASE
     WHEN condition THEN true_value
     [ ELSE false_value ]
 END
```

if(condition, true_value) If the condition is true, the true_value column is returned. Otherwise, null is returned. if(condition, true_value, false_value) If the condition is true, the true_value column is returned. Otherwise, the false_value column is returned. Syntax for coalesce() functions A coalesce() function returns the first non-null value from multiple columns.

```
COALESCE (value1, value2 [,...])
```

Syntax for the nullif() function If value1 is equal to value2, null is returned. Otherwise, value1 is returned.

```
nullif(value1, value2)
```

Syntax for the try() function The try() function catches underlying exceptions, such as division by zero errors, and returns null.

```
try(expression)
```

#### 4.8.20 Nested subqueries

This describes how to use nested subqueries when you query logs. You can use nested queries to perform more complicated queries. Nested queries differ from non-nested queries in the need for specifying the FROM clause in the SQL statement. You must specify the `from log` keyword in each SQL statement to read raw data from logs. Example:

```
* | select sum(pv) from
```

`(`

```
select count(1) as pv from log group by method
```

`)`

#### 4.8.21 Array functions

This topic describes the syntax of array functions. It also provides examples that show how to use these functions.

| Function | Description | Example |
|---|---|---|
| Subscript operator [] | The subscript operator [] is used to obtain an element in the array. | N/A |
| array distinct _ | Returns the distinct elements in the array. | N/A |
| array intersect(x, y) _ | Returns the intersection of the x and y arrays. | N/A |
| array union(x, y) → array _ | Returns the union of the x and y arrays. | N/A |
| array except(x, y) → array _ | Returns the subtraction of the x and y arrays. | N/A |
| array join(x, delimiter, _ null replacement) → varchar _ | Joins string arrays with the delimiter into a string and replaces null values with null replacement. _ Not e The maximum size of the returned result of this array join function is 1 KB. If the _ returned result exceeds 1 KB, the extra data will be truncated. | N/A |

| Function | Description | Example |
|---|---|---|
| array max(x) → x _ | Returns the maximum value in the x array. | N/A |
| array min(x) → x _ | Returns the minimum value in the x array. | N/A |
| array position(x, element) → bigint _ | Returns the subscript of the element in the x array. The subscript starts from 1. The value 0 is returned if no subscript is found. | N/A |
| array remove(x, element) → array _ | Removes the element from the array. | N/A |
| array sort(x) → array _ | Sorts the array and moves null values to the end. | N/A |
| cardinality(x) → bigint | Returns the array size. | N/A |
| concat(array1, array2, …, arrayN) → array | Concatenates arrays. | N/A |
| contains(x, element) → boolean | Returns true if the x array contains the specified element. | N/A |
| filter(array, function) → array | For more information about this Lambda function, see the filter() function in Lambda functions. | N/A |
| flatten(x) → array | Flattens an array(array(T)) to an array(T) by concatenating the contained arrays. | N/A |
| reduce(array, initialState, inputFunction, outputFunction) → x | For more information, see the reduce() function in Lambda functions. | N/A |
| reverse(x) → array | Returns an array that has the reversed order of the x array. | N/A |
| sequence(start, stop) → array | Generates a sequence of elements from start to stop. The difference between elements is 1. | N/A |
| sequence(start, stop, step) → array | Generates a sequence of elements from start to stop. The difference between elements is step. | N/A |
| sequence(start, stop, step) → array | Generates a sequence of timestamps from start to stop. The difference between timestamps is step. The type of step can be either INTERVAL DAY TO SECOND or INTERVAL YEAR TO MONTH. | N/A |
| shuffle(x) → array | Shuffles the array. | N/A |
| slice(x, start, length) → array | Returns a subset of the x array starting from the start value with the specified length. | N/A |

| L | og Service |   |   |   | User Guide·Query and analysi |   |   |
|---|---|---|---|---|---|---|---|
|   | Function |   | Description |   | Example |   |   |
|   | transform(array, function) → array |   | For more information, see the transform() function in Lambda functions. |   | N/A |   |   |
|   | zip(array1, array2[, …]) → array |   | Merges the specified arrays. The M-th element of the N-th argument will be |   | SELECT zip(ARRAY[1, 2], |   |   |
|   |   |   |   |   |   | SELECT zip(ARRAY[1, 2], |   |
|   |   |   |   | he N-th argument will be | ARRAY[‘1b’, null, ‘3b’]); — |   |   |
|   |   | → array | the N-th field of the M-th output |   |   |   |   |
|   |   |   |   |   | [ROW(1, ‘1b’), ROW(2, null), |   |   |
|   |   |   | element. |   | ROW(null, ‘3b’)] |   |   |
|   | zip with(array1, array2, function) → _ array |   | For more information, see the zip with() function in Lambda _ functions. |   | N/A |   |   |
|   | array agg (key) _ |   | An aggregate function that returns an array from values in the key column. |   | * \| select array agg(key) _ |   |   |
|   | array transpose(array[array[x,y,z], _ array[a,b,c]]) |   | Returns a new matrix by transposing the values of the previous matrix from rows to columns. |   | N/A |   |   |

#### 4.8.22 Binary string functions

This topic describes the syntax of binary string functions. It also provides examples that show how to use these functions. Data of the VARBINARY type is different from data of the VARCHAR type.

| Function | Description |
|---|---|
| Concatenation operator (\|\|) | The result of a \|\| b is ab . |
| length(binary) → bigint | Returns the length in binary. |
| concat(binary1, …, binaryN) → varbinary | Connects the binary strings, which is equivalent to \|\|. |
| to base64(binary) → varchar _ | Converts a binary string to a Base64 string. |
| from base64(string) → varbinary _ | Converts a Base64 string to a binary string. |
| to base64url(binary) → varchar _ | Converts a string to a URL-safe Base64 string. |
| from base64url(string) → varbinary _ | Converts a URL-safe Base64 string to a binary string. |
| to hex(binary) → varchar _ | Converts a binary string to a hexadecimal string. |
| from hex(string) → varbinary _ | Converts a hexadecimal string to a binary string. |
| to big endian 64(bigint) → varbinary _ _ _ | Convert a number to a binary string in big endian mode. |
| from big endian 64(binary) → bigint _ _ _ | Converts a binary string in big endian mode to a number. |
| md5(binary) → varbinary | Calculates the MD5 value of a binary string. |
| sha1(binary) → varbinary | Calculates the SHA1 value of a binary string. |
| sha256(binary) → varbinary | Calculates the SHA256 hash value of a binary string. |

| User Guide·Query and analysis | Log Servic |
|---|---|

| Function | Description |
|---|---|
| sha512(binary) → varbinary | Calculate the SHA512 value of a binary string. |
| xxhash64(binary) → varbinary | Calculates the xxhash64 value of a binary string. |

#### 4.8.23 Bitwise operations

This topic describes the syntax for bitwise operations. It also provides examples that show how to use these operations.

| Function | Description | Example |
|---|---|---|
| bit count(x, bits) → bigint _ | Count the number of 1 in the binary expression of x. | SELECT bit count(9, 64); — 2 _ SELECT bit count(9, 8); — 2 _ SELECT bit count(-7, 64); — _ 62 SELECT bit count(-7, 8); — 6 _ |
| bitwise and(x, y) → bigint _ | Perform the AND operation on x and y in the binary form. | N/A |
| bitwise not(x) → bigint _ | Calculate the opposite values of all bits of x in the binary form. | N/A |
| bitwise or(x, y) → bigint _ | Perform the OR operation on x and y in the binary form. | N/A |
| bitwise xor(x, y) → bigint _ | Perform the XOR operation on x and y in the binary form. | N/A |

|   |   | SELECT bit count(9, 64); — 2 _ |
|---|---|---|
|   |   | SELECT bit count(9, 8); — 2 _ |
|   |   | SELECT bit count(-7, 64); — _ |
| ion of x. | 62 |   |

#### 4.8.24 Interval-valued comparison and periodicity-valued comparison functions

valued comparison functions Log Service allows you to use interval-valued comparison and periodicity-valued comparison functions to query and analyze log data. You can use the functions to compare the value for one period with that for a previous period.

| Function | Description | Example |
|---|---|---|

| Function |   |   |   | Description |   |   |   | Example |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| compare(value, time window) _ |   |   |   | This function compares the value calculated for the current period with that calculated for the period before time window. _ The data type of the values to be compared is Double or Long. The time window parameter is measured _ in seconds. This function returns an |   |   |   | *\|select compare( pv , 86400) |   |   |
|   |   |   |   |   |   |   |   |   | *\|select compare( pv , 86400) |   |
|   |   |   |   |   | window parameter is measured onds. This function returns an |   |   | from (select count(1) as pv |   |   |
|   |   |   |   | array. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | from log) |   |   |
|   |   |   |   | Possible return values include the value for the current period, the value for the period before time window, _ and the ratio of the current value to the value before time window. _ |   |   |   |   |   |   |
| compare(value, time window1, _ time window2) _ |   |   |   | This function compares the current value with the values for periods before time window1 and _ time window2. The comparison _ results are in the JSON array format, where the values must be returned in |   |   |   | * \| select compare(pv, 86400, |   |   |
|   |   |   |   |   |   |   |   |   | * \| select compare(pv, 86400, |   |
|   | compare(value, time window1, _ |   |   | where the |   |   |   |   |   |   |
|   |   |   |   |   | e the | values must be returned in |   | 172800) from ( select count(1) |   |   |
| time window2) _ |   |   |   |   |   |   |   |   |   |   |
|   |   | ow2) |   | the following order: [current value, value before time window1, value | ollowing order: [current value, |   |   |   |   |   |
|   |   |   |   |   |   |   |   | as pv from log) |   |   |
|   |   |   |   | _ before time window2, current _ value/value before time window1, _ current value/value before time window2]. _ |   |   |   |   |   |   |
| compare(value, time window1, _ time window2, time window3) _ _ |   |   |   | This function compares the value for the current period with the values for periods before time window1, _ time window2, and time window3. _ _ The comparison results are in the JSON array format, where the values must be returned in the following order: [current value, value before |   |   |   | * \| select compare(pv, 86400, |   |   |
|   |   |   |   |   |   |   |   |   | * \| select compare(pv, 86400, |   |
|   | compare(value, time window1, _ |   |   | must be returned in the foll order: [current value, value |   |   |   |   |   |   |
|   |   |   |   |   | : [current value, value |   | before | 172800,604800) from ( select |   |   |
| _ time window2, time window3) _ _ | _ |   |   |   |   |   |   |   |   |   |
|   |   |   | 2, time window3) _ | time window1, value before _ |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | count(1) as pv from log) |   |   |
|   |   |   |   | time window2, value before _ time window3, current value/value _ before time window1, current _ value/value before time window2, _ current value/value before time window3]. _ |   |   |   |   |   |   |

|   | Function |   |   |   |   |   | Description |   |   |   |   |   |   |   | Example |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | This function compares the value for the current period with the values for |   |   |   |   |   |   |   | For example, * \| select t, |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | * \| select t, |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | he values for |   |   | ts compare(pv, 86400 ) as d _ |   |   |   |
|   |   |   |   |   |   |   | periods before |   | time window1 _ |   |   |   |   |   | from(select |   |   |   |
|   |   |   |   |   |   |   | and | time window2 |   |   | and returns a |   |   |   | date trunc('minute', time ) _ __ __ |   |   |   |
|   |   |   |   |   |   |   |   | _ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | JSON array. The comparison results |   |   |   |   |   |   |   | as t, count(1) as pv from log |   |   |   |
|   |   |   |   |   |   |   | are in the JSON array format, where |   |   |   |   |   |   |   | group by t order by t ) group |   |   |   |
|   |   |   |   |   |   |   | the values must be returned in the |   |   |   |   |   |   |   | by t |   |   |   |
|   |   | ts compare(value, _ |   |   |   |   | following order: [current value, value before time window1, current _ value/value before time window1, _ Unix timestamp that indicates the start time of the previous period]. This function is used to compare time series values. You must specify the |   |   |   |   |   |   |   |   |   |   |   |
|   | time window) _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | d: |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | [1251.0,1264.0, |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ust specify the |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 0.9897151898734177, |   |   |   |
|   |   |   |   |   |   |   | GROUP BY keyword for the time |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 1539843780.0,1539757380.0]t:201 |   |   |   |
|   |   |   |   |   |   |   | column in SQL statements. |   |   |   |   |   |   |   | 8-10-19 14:23:00.000 |   |   |   |

Examples Calculate the ratio of the PV for an hour on a day to that for the same time period on a previous day. The start time is 2018-07-25 14:00:00, and the end time is 2018-07-25 15:00:00. Statement for query and analysis:

```
* | select compare( pv , 86400) from (select count(1) as pv from log)
```

In the preceding statement, 86400 indicates 86,400 seconds before the current period. Return results:

```
[9.0,19.0,0.47368421052631579]
```

In the preceding results, 9.0 is the PV for the period from 2018-07-25 14:00:00 to 2018-07-25 15:00:00. 19.0 is the PV for the period from 2018-07-24 14:00:00 to 2018-07-24 15:00:00. 0.47368421052631579 is the ratio of the PV for the current period to that for a previous period. If you want to expand the array into three columns of numbers, the analysis statement is

```
* | select diff[1],diff[2],diff[3] from(select compare( pv , 86400) as diff from (select count(1) a
s pv from log))
```

Calculate the PV ratio for every minute of the current hour to that in the same time period as the day before, and output the results in a line chart. i. Calculate the PV ratio for every minute of the current hour to that in the same time period as the day before. The start time is 2018-07-25 14:00:00, and the end time is 2018-07-25 15:00:00. Statement for query and analysis:

```
*| select t, compare( pv , 86400) as diff from (select count(1) as pv, date_format(from_unixtim e(__time__), '%H:%i') as t from log group by t) group by t order by t
```

Return results:

| t | diff |
|---|---|
| 14:00 | [9520.0,7606.0,1.2516434393899554] |
| 14:01 | [8596.0,8553.0,1.0050274757395066] |
| 14:02 | [8722.0,8435.0,1.0340248962655603] |
| 14:03 | [7499.0,5912.0,1.2684370771312586] |

In the preceding table, t indicates the time in the format of `Hour:Minute` . The contents of the diff column are included in an array that contains the following values: The PV value of the current period. The PV value of the previous period. The ratio of the PV value for the current period to that for the previous period. ii. To show the query results in a line chart, use the following statement:

```
*|select t, diff[1] as current, diff[2] as yestoday, diff[3] as percentage from(select t, compa re( pv , 86400) as diff from (select count(1) as pv, date_format(from_unixtime(__time__), '%H:% i') as t from log group by t) group by t order by t)
```

The two lines indicate the PV values of a day and the day before. Line chart

#### 4.8.25 Comparison functions and operators

This topic describes the comparison functions and operators in Log Service. You can use these functions and operators to query and analyze log data. A comparison function compares two parameter values of any comparable data types, such as INTEGER, BIGINT, DOUBLE, and TEXT. Comparison operators A comparison operator is used to compare two values. If the statement is true, TRUE is returned. Otherwise, FALSE is returned.

| Operator | Description |
|---|---|
| < | Less than |
| > | Greater than |

| User Guide·Query and analysis | Log Servic |
|---|---|

| Operator | Description |
|---|---|
| <= | Less than or equal to |
| >= | Greater than or equal to |
| = | Equal to |
| <> | Not equal to |
| ! = | Not equal to |

Range operator BETWEEN The BETWEEN operator determines whether a value falls in a specified closed interval. If the value falls in the specified closed interval, TRUE is returned. Otherwise, FALSE is returned. Example: SELECT 3 BETWEEN 2 AND 6; . The statement is true, and TRUE is returned. The preceding statement is equivalent to SELECT 3 >= 2 AND 3 <= 6; . The BETWEEN operator can be put behind the NOT operator to test whether a value falls out of a specified closed interval. Example: SELECT 3 NOT BETWEEN 2 AND 6; . The statement is false, and FALSE is returned. The preceding statement is equivalent to SELECT 3 < 2 OR 3 > 6; . If any of the three values is NULL, NULL is returned. IS NULL and IS NOT NULL The IS NULL and IS NOT NULL operators test whether a value is NULL. IS DISTINCT FROM and IS NOT DISTINCT FROM These operators are similar to the EQUAL TO and NOT EQUAL TO operators. However, IS DISTINCT FROM and IS NOT DISTINCT FROM can determine whether a NULL value exists. Examples:

```
SELECT NULL IS DISTINCT FROM NULL; -- false SELECT NULL IS NOT DISTINCT FROM NULL; -- true
```

The DISTINCT operator compares parameter values under multiple conditions, as described in the following table.

| a | b | a = b | a <> b | a DISTINCT b | a NOT DISTINCT b |
|---|---|---|---|---|---|
| 1 | 1 | TRUE | FALSE | FALSE | TRUE |
| 1 | 2 | FALSE | TRUE | TRUE | FALSE |
| 1 | NULL | NULL | NULL | TRUE | FALSE |
| NULL | NULL | NULL | NULL | FALSE | TRUE |

GREATEST and LEAST These operators are used to obtain the maximum or minimum value from a row of field values. Example:

```
select greatest(1,2,3) -- Returns 3.
```

Quantified comparison predicates: ALL, ANY, and SOME The ALL, ANY, and SOME quantifiers can be used to determine whether a parameter value meets specified conditions. ALL is used to determine whether a parameter value meets all conditions. If the statement is true, TRUE is returned. Otherwise, FALSE is returned. ANY is used to determine whether a parameter value meets a condition. If the statement is true, TRUE is returned. Otherwise, FALSE is returned. SOME is used to determine whether a parameter value meets a condition. SOME is equivalent to ANY. ALL, ANY, and SOME must immediately follow comparison operators. ALL and ANY support comparison under multiple conditions, as described in the following table.

| Expression | Description |
|---|---|
| A = ALL (...) | Returns TRUE if A matches all values. |
| A <> ALL (...) | Returns TRUE if A does not match a value. |
| A < ALL (...) | Returns TRUE if A is smaller than the smallest value. |
| A = ANY (...) | Returns TRUE if A is equal to a value. This statement is equivalent to A IN (...). |
| A <> ANY (...) | Returns TRUE if A does not match a value. |
| A < ANY (...) | Returns TRUE if A is smaller than the largest value. |

Examples:

```
SELECT 'hello' = ANY (VALUES 'hello', 'world'); -- true SELECT 21 < ALL (VALUES 19, 20, 21); -- false SELECT 42 >= SOME (SELECT 41 UNION ALL SELECT 42 UNION ALL SELECT 43); -- true
```

#### 4.8.26 Lambda functions

This topic describes Lambda functions and provides some examples. You can use Lambda functions to analyze log data in Log Service Lambda expressions Lambda expressions use the arrow operator `->` . Examples:

```
x -> x + 1 (x, y) -> x + y x -> regexp_like(x, 'a+') x -> x[1] / x[2] x -> IF(x > 0, x, -x) x -> COALESCE(x, 0) x -> CAST(x AS JSON) x -> x + TRY(1 / 0)
```

Most MySQL expressions can be used in Lambda functions. filter(array<T>, function<T, boolean>) → ARRAY<T> Returns an array whose elements are filtered from the specified array based on the Lambda expression. Examples:

```
SELECT filter(ARRAY [], x -> true); -- [] SELECT filter(ARRAY [5, -6, NULL, 7], x -> x > 0); -- [5, 7] SELECT filter(ARRAY [5, NULL, 7, NULL], x -> x IS NOT NULL); -- [5, 7]
```

map_filter(map<K, V>, function<K, V, boolean>) → MAP<K,V> Returns a map whose elements are filtered based on the Lambda expression. The map is generated from the map function. Examples:

```
SELECT map_filter(MAP(ARRAY[], ARRAY[]), (k, v) -> true); -- {} SELECT map_filter(MAP(ARRAY[10, 20, 30], ARRAY['a', NULL, 'c']), (k, v) -> v IS NOT NULL); -- {10 -> a , 30 -> c} SELECT map_filter(MAP(ARRAY['k1', 'k2', 'k3'], ARRAY[20, 3, 15]), (k, v) -> v > 10); -- {k1 -> 20, k3 -> 15}
```

reduce(array<T>, initialState S, inputFunction<S, T, S>, outputFunction<S, R>) → R The reduce function starts from the initial state, traverses each element in the array, and then calls inputFunction(S,T) to generate a new state. After all the elements in the array are traversed and the final state is generated, the reduce function calls outputFunction to assign the final state value to the result R and output the result. The procedure is described as follows:
1. Start from the initial state S.
2. Traverse each element T.
3. Calculate inputFunction(S,T) to generate a new state S.
4. Repeat steps 2 and 3 until the last element is traversed and has a new state.
5. Turn the final state S into the final result R.
Examples:

```
SELECT reduce(ARRAY [], 0, (s, x) -> s + x, s -> s); -- 0 SELECT reduce(ARRAY [5, 20, 50], 0, (s, x) -> s + x, s -> s); -- 75 SELECT reduce(ARRAY [5, 20, NULL, 50], 0, (s, x) -> s + x, s -> s); -- NULL SELECT reduce(ARRAY [5, 20, NULL, 50], 0, (s, x) -> s + COALESCE(x, 0), s -> s); -- 75 SELECT reduce(ARRAY [5, 20, NULL, 50], 0, (s, x) -> IF(x IS NULL, s, s + x), s -> s); -- 75 SELECT reduce(ARRAY [2147483647, 1], CAST (0 AS BIGINT), (s, x) -> s + x, s -> s); -- 2147483648 SELECT reduce(ARRAY [5, 6, 10, 20], -- calculates arithmetic average: 10.25
              CAST(ROW(0.0, 0) AS ROW(sum DOUBLE, count INTEGER)),
              (s, x) -> CAST(ROW(x + s.sum, s.count + 1) AS ROW(sum DOUBLE, count INTEGER)),
              s -> IF(s.count = 0, NULL, s.sum / s.count));
```

transform(array<T>, function<T, U>) → ARRAY<U> This Lambda function traverses each element in an array to generate a new result U. Examples:

```
SELECT transform(ARRAY [], x -> x + 1); -- [] SELECT transform(ARRAY [5, 6], x -> x + 1); -- [6, 7] -- Increments each element by 1. SELECT transform(ARRAY [5, NULL, 6], x -> COALESCE(x, 0) + 1); -- [6, 1, 7] SELECT transform(ARRAY ['x', 'abc', 'z'], x -> x || '0'); -- ['x0', 'abc0', 'z0'] SELECT transform(ARRAY [ARRAY [1, NULL, 2], ARRAY[3, NULL]], a -> filter(a, x -> x IS NOT NULL)); -- [ [1, 2], [3]]
```

zip_with(array<T>, array<U>, function<T, U, R>) → array<R> This Lambda function merges two arrays and generates the element R in the new array based on element T and element U. Examples:

```
SELECT zip_with(ARRAY[1, 3, 5], ARRAY['a', 'b', 'c'], (x, y) -> (y, x)) --Transposes the elements of t he two arrays to generate a new array. Result: [['a', 1], ['b', 3],['c', 5]] SELECT zip_with(ARRAY[1, 2], ARRAY[3, 4], (x, y) -> x + y); -- Result: [4, 6] SELECT zip_with(ARRAY['a', 'b', 'c'], ARRAY['d', 'e', 'f'], (x, y) -> concat(x, y)) -- Concatenates th e elements of the two arrays to generate a new string. Result: ['ad', 'be', 'cf']
```

#### 4.8.27 Logical functions

This topic describes the available logical functions in Log Service. You can use these functions to query and analyze log data. Logical operators

| Operator | Description | Example |
|---|---|---|
| AND | The result is TRUE if both values are TRUE. | a AND b |
| OR | The result is TRUE if either value is TRUE. | a OR b |
| NOT | The result is TRUE if the value is FALSE. | NOT a |

Effect of NULL on logical operators The following tables list the truth values when the values of a and b are TRUE, FALSE, and NULL, respectively. Truth table 1

| a | b | a AND b | a OR b |
|---|---|---|---|
| TRUE | TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE | TRUE |
| TRUE | NULL | NULL | TRUE |
| FALSE | TRUE | FALSE | TRUE |
| FALSE | FALSE | FALSE | FALSE |
| FALSE | NULL | FALSE | NULL |

|   | User Guide·Query and analy | sis |   | Log Servic | e |
|---|---|---|---|---|---|

| a | b | a AND b | a OR b |
|---|---|---|---|
| NULL | TRUE | NULL | TRUE |
| NULL | FALSE | FALSE | NULL |
| NULL | NULL | NULL | NULL |

Truth table 2

| a | NOT a |
|---|---|
| TRUE | FALSE |
| FALSE | TRUE |
| NULL | NULL |

#### 4.8.28 Field aliases

This topic describes how to specify an alias for a field and provides some examples. A field name in an SQL statement must start with letters and contain digits and underscores (_). If you have configured a field name that does not conform to the SQL standard (such as User-Agent), you must specify an alias for the field on the field index configuration page. The alias takes effect only for the duration of the SQL statement. The data is still stored under the original field name. You must specify the original name when you perform a search. You can also specify an alias for a field in an SQL statement if the original name is long. Sample aliases

| Original field name | Alias |
|---|---|
| User-Agent | ua |
| User.Agent | ua |
| 123 | col |
| abceefghijklmnopqrstuvw | a |

#### 4.8.29 JOIN operations between Logstores and Relational Database Service (RDS) tables

Relational Database Service (RDS) tables This topic describes how to join Logstores in Log Service with RDS tables for queries and store the query results in RDS tables.
1. Create a VPC.
Create an RDS instance and specify the VPC to host the RDS instance. Then the VPC ID and the RDS instance ID are obtained.
2. Configure a whitelist for the RDS instance.
Add the following CIDR blocks to the whitelist: `100.104.0.0/16` , `11.194.0.0/16` , and `11.201.0.0/16`
3. Create an external store
Run the following statement to create an external store. Replace the parameter values based on your business needs. `{`

```json
"externalStoreName":"storeName", "storeType":"rds-vpc", "parameter":
```

`{`

```json
   "region":"cn-qingdao",
   "vpc-id":"vpc-m5eq4irc1pucp*******"
   "instance-id":"i-m5eeo2whsn*******"
   "host":"localhost",
   "port":"3306",
   "username":"root",
   "password":"****",
   "db":"scmc"
   "table":"join_meta"
```

`}` `}` Parameters

| Parameter | Description |
|---|---|
| region | The region where your RDS instance resides. |
| vpc-id | The ID of the VPC where your RDS instance resides. |
| instance-id | The ID of the RDS instance. |
| host | The ID of the ECS instance that is used to access the RDS instance. |
| port | The port of the ECS instance that is used to access the RDS instance. |
| username | The username that is used to log on to the RDS instance. |
| password | The password that is used to log on to the RDS instance. |
| db | The name of the database. |
| table | The name of the table with which the Logstore is joined. |

> Not e You can join a Logstore with an RDS table that resides only in the China (Beijing), China (Qingdao), and China (Hangzhou) regions.

4. JOIN query.
Log on to the Log Service console. In the Search & Analyze search box, run a JOIN statement. Supported JOIN syntax: INNER JOIN LEFT JOIN RIGHT JOIN FULL JOIN

```
[ INNER ] JOIN LEFT [ OUTER ] JOIN RIGHT [ OUTER ] JOIN FULL [ OUTER ] JOIN
```

> Not e
> You can join Logstores only to external tables.
> In the JOIN statement, you must first specify a Logstore before specifying an external store.
> You must specify the name of the external store instead of the name of an RDS table. The external store name automatically changes into the combination of the RDS database name and the name of the RDS table that you want to join with the Logstore.

Sample JOIN statement:

```
method:postlogstorelogs | select count(1) , histogram(logstore) from log l join join_meta m on l.projectid = cast( m.ikey as varchar)
```

5. Store the query results to the RDS table.
You can use the INSERT statement to insert the query results into the RDS table.

```
method:postlogstorelogs | insert into method_output select cast(methodasvarchar(65535)),count( 1)fromloggroupbymethod
```

Sample Python script:

```java
# encoding: utf-8
from __future__ import print_function from aliyun.log import * from aliyun.log.util import base64_encodestring from random import randint import time import os from datetime import datetime
    endpoint = os.environ.get('ALIYUN_LOG_SAMPLE_ENDPOINT', 'cn-chengdu.log.aliyuncs.com')
    accessKeyId = os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSID', '')
    accessKey = os.environ.get('ALIYUN_LOG_SAMPLE_ACCESSKEY', '')
    logstore = os.environ.get('ALIYUN_LOG_SAMPLE_LOGSTORE', '')
    project = "ali-yunlei-chengdu"
    client = LogClient(endpoint, accessKeyId, accessKey, token)
## Create an external store
    res = client.create_external_store(project,ExternalStoreConfig("rds_store","region","rds-vpc","vpc
id","instance-id","instance-ip","port","username","password","db","table"));
    res.log_print()
    ## Obtain external store details
    res = client.get_external_store(project,"rds_store");
    res.log_print()
    res = client.list_external_store(project,"");
    res.log_print();
    # Perform the JOIN operation.
    req = GetLogStoreLogsRequest(project,logstore,From,To,"","select count(1) from  "+ logstore +"  s
join meta m on s.projectid = cast(m.ikey as varchar)");
    res = client.get_logs(req)
    res.log_print();
     # Store query results to the RDS table
    req = GetLogStoreLogsRequest(project,logstore,From,To,""," insert into rds_store select count(1) f
rom "+ logstore );
    res = client.get_logs(req)
    res.log_print();
```

#### 4.8.30 Geospatial functions

This topic describes the available geospatial functions in Log Service. You can use these functions to query and analyze log data. Concept of geometry Geospatial functions support geometries in the well-known text (WKT) format. Geometry formats

| Geometry |   | WKT format |   |   |
|---|---|---|---|---|
| Point |   | POINT (0 0) |   |   |
| LineString |   | LINESTRING (0 0, 1 1, 1 2) |   |   |
| Polygon |   | POLYGON ((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)) |   |   |
|   |   |   | POLYGON ((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, |   |
|   | on | 2 2, 1 2, 1 1)) |   |   |
| MultiPoint |   | MULTIPOINT (0 0, 1 2) |   |   |
| MultiLineString |   | MULTILINESTRING ((0 0, 1 1, 1 2), (2 3, 3 2, 5 4)) |   |   |

|   |   | MULTILINESTRING ((0 0, 1 1, 1 2), (2 3, 3 2, 5 |   |
|---|---|---|---|
| ineString | 4)) |   |   |

| User Guide·Query and analysis | Log Servic |
|---|---|
| Geometry | WKT format |
| MultiPolygon | MULTIPOLYGON (((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)), ((-1 -1, -1 -2, |
| GeometryCollection | GEOMETRYCOLLECTION (POINT(2 3), LINESTRING (2 3, 3 4)) |

|   |   | MULTIPOLYGON (((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, |
|---|---|---|
| Polygon | 2 1, 2 2, 1 2, 1 1)), ((-1 -1, -1 -2, |   |

|   |   | GEOMETRYCOLLECTION (POINT(2 3), LINESTRING (2 |   |
|---|---|---|---|
| tryCollection | 3, 3 4)) |   |   |

Constructors Constructor description

| Function | Description |
|---|---|
| ST Point(double, double) → Point _ | Returns a geometry point instance with the specified coordinate values. |
| ST LineFromText(varchar) → LineString _ | Returns a geometry LineString instance from a WKT representation. |
| ST Polygon(varchar) → Polygon _ | Returns a geometry polygon instance from a WKT representation. |
| ST GeometryFromText(varchar) → Geometry _ | Returns a geometry instance from a WKT representation. |
| ST AsText(Geometry) → varchar _ | Returns the WKT representation of a geometry. |

Operations

| Function | Description |
|---|---|
| ST Boundary(Geometry) → Geometry _ | Returns the closure of the combinatorial boundary of a geometry. |
| ST Buffer(Geometry, distance) → Geometry _ | Returns the geometry that represents all points whose distance from the specified geometry is shorter than or equal to the specified distance. |
| ST Difference(Geometry, Geometry) → Geometry _ | Returns the geometry value that represents the point set difference of the specified geometries. |
| ST Envelope(Geometry) → Geometry _ | Returns the bounding rectangular polygon of a geometry. |
| ST ExteriorRing(Geometry) → Geometry _ | Returns a line string that represents the exterior ring of the input polygon. |
| ST Intersection(Geometry, Geometry) → Geometry _ | Returns the geometry value that represents the point set intersection of two geometries. |
| ST SymDifference(Geometry, Geometry) → Geometry _ | Returns the geometry value that represents the point set symmetric difference of two geometries. |

Relationship tests

| Function | Description |
|---|---|

| Function | Description |
|---|---|
| ST Contains(Geometry, Geometry) → boolean _ | Returns True if and only if no points of the second geometry lie in the exterior of the first geometry, and at least one point of the interior of the first geometry lies in the interior of the second geometry. Returns False if points of the second geometry are on the boundary of the first geometry. |
| ST Crosses(Geometry, Geometry) → boolean _ | Returns True if the specified geometries share some, but not all, interior points in common. |
| ST Disjoint(Geometry, Geometry) → boolean _ | Returns True if the specified geometries do not spatially intersect. |
| ST Equals(Geometry, Geometry) → boolean _ | Returns True if the specified geometries represent the same geometry. |
| ST Intersects(Geometry, Geometry) → boolean _ | Returns True if the specified geometries spatially intersect in two dimensions. |
| ST Overlaps(Geometry, Geometry) → boolean _ | Returns True if the specified geometries share space in the same dimension, but are not completely contained by each other. |
| ST Relate(Geometry, Geometry) → boolean _ | Returns True if the first geometry is spatially related to the second geometry. |
| ST Touches(Geometry, Geometry) → boolean _ | Returns True if the specified geometries have at least one point in common, but their interiors do not intersect. |
| ST Within(Geometry, Geometry) → boolean _ | Returns True if the first geometry is completely inside the second geometry. Returns False if the two geometries have points in common at the boundaries. |

Accessors

| Function | Description |
|---|---|
| ST Area(Geometry) → double _ | Returns the two-dimensional Euclidean area of a geometry. |
| ST Centroid(Geometry) → Geometry _ | Returns the point value that is the mathematical centroid of a geometry. |
| ST CoordDim(Geometry) → bigint _ | Returns the coordinate dimension of a geometry. |
| ST Dimension(Geometry) → bigint _ | Returns the inherent dimension of a geometry object, which must be less than or equal to the coordinate dimension. |
| ST Distance(Geometry, Geometry) → double _ | Returns the minimum two-dimensional Cartesian distance (based on spatial ref) between two geometries in projected units. |
| ST IsClosed(Geometry) → boolean _ | Returns True if the start and end points of the linestring are coincident. |

| Function | Description |
|---|---|
| ST IsEmpty(Geometry) → boolean _ | Returns True if the specified geometry is an empty geometry, such as geometry collection, polygon, and point. |
| ST IsRing(Geometry) → boolean _ | Returns True if and only if the line is closed and simple. |
| ST Length(Geometry) → double _ | Returns the length of a LineString or multi-LineString by using Euclidean measurement on a two-dimensional plane (based on spatial ref) in projected units. |
| ST XMax(Geometry) → double _ | Returns the X maximum of the bounding box of the geometry. |
| ST YMax(Geometry) → double _ | Returns the Y maximum of the bounding box of the geometry. |
| T XMin(Geometry) → double _ | Returns the X minimum of the bounding box of the geometry. |
| ST YMin(Geometry) → double _ | Returns the Y minimum of the bounding box of the geometry. |
| ST StartPoint(Geometry) → point _ | Returns the first point of a geometry LineString instance. |
| ST EndPoint(Geometry) → point _ | Returns the last point of a geometry LineString instance. |
| ST X(Point) → double _ | Returns the X coordinate of a point. |
| ST Y(Point) → double _ | Returns the Y coordinate of a point. |
| ST NumPoints(Geometry) → bigint _ | Returns the number of points in a geometry. |
| ST NumInteriorRing(Geometry) → bigint _ | Returns the cardinality of the collection of interior rings of a polygon. |

#### 4.8.31 Geography functions

This topic describes the syntax of geography functions and provides some examples. For information about functions that identify the country, province, city, ISP, and the longitude and latitude of a specified IP address, see IP functions.

| Function | Description | Example |
|---|---|---|
| geohash(string) | Returns the geohash value of the specified geographical location. The geographical location is represented by a string in the format of "latitude, longitude". The values for latitude and longitude are separated by a comma. | select geohash('34.1,120.6')= 'wwjcbrdnzs' |

| Function | Description | Example |
|---|---|---|
| geohash(lat,lon) | Returns the geohash value of the specified geographical location. The geographical location is represented by two parameters that indicate the latitude and longitude. | select geohash(34.1,120.6)= 'wwjcbrdnzs' |

#### 4.8.32 JOIN syntax

The JOIN operation joins multiple tables by using one or more fields in the tables. You can join a Logstore created in Log Service with the Logstore itself, with another Logstore, or with an RDS table. This topic describes how to join different Logstores.
1. Download the latest version of the SDK for Python.
2. Call the GetProjectLogs operation to query logs.
Sample SDK

```java
#! /usr/bin/env python
#encoding: utf-8
import time,sys,os from aliyun.log.logexception import LogException from aliyun.log.logitem import LogItem from aliyun.log.logclient import LogClient from aliyun.log.getlogsrequest import GetLogsRequest from aliyun.log.getlogsrequest import GetProjectLogsRequest from aliyun.log.putlogsrequest import PutLogsRequest from aliyun.log.listtopicsrequest import ListTopicsRequest from aliyun.log.listlogstoresrequest import ListLogstoresRequest from aliyun.log.gethistogramsrequest import GetHistogramsRequest from aliyun.log.index_config import * from aliyun.log.logtail_config_detail import * from aliyun.log.machine_group_detail import * from aliyun.log.acl_config import * if __name__=='__main__':
    token = None
    endpoint = "http://cn-hangzhou.log.aliyuncs.com"
    accessKeyId  = 'LTAIvKy7U'
    accessKey='6gXLNTLyCfdsfwrewrfhdskfdsfuiwu'
    client = LogClient(endpoint, accessKeyId, accessKey,token)
    logstore = "meta"
    # In the query statements, specify two Logstores, the query time ranges of both Logstores, and the
key that you want to use to join the two Logstores.
    req = GetProjectLogsRequest(project,"select count(1) from sls_operation_log  s join  meta m on s._
_date__ >'2018-04-10 00:00:00' and s.__date__ < '2018-04-11 00:00:00' and m.__date__ >'2018-04-23 00:0 0:00' and m.__date__ <'2018-04-24 00:00:00' and s.projectid = cast(m.ikey as varchar)");
    res = client.get_project_logs(req)
    res.log_print();
    exit(0)
```

> Not e For more information about the JOIN syntax and examples, see Join.

#### 4.8.33 UNNEST function

This topic describes the UNNEST function. Scenarios Log data is typically stored as primitive data types, such as string or number. In certain scenarios, log data may include complex data types, such as arrays, maps, and JSON objects. The UNNEST function can be used to transform complex data types into rows of primitive data types. This simplifies query and analysis. Example:

```
__source__: 1.1.1.1 __tag__:__hostname__: vm-req-170103232316569850-tianchi111932.tc __topic__: TestTopic_4 array_column: [1,2,3] double_column: 1.23 map_column: {"a":1,"b":2} text_column: Product
```

The values of the `array_column` field are arrays. To obtain the sum of elements of all `array_column` field values, you must traverse all elements of every array.

| Syntax | Description |
|---|---|
| unnest( array) as table alias(column name) _ _ | Expands an array into multiple rows. The column name of these rows is column name . _ |
| unnest(map) as table(key name, value name) _ _ | Expands a map into multiple rows. key name specifies _ the column name of the keys, and value name _ specifies the column name of the values. |

> Not e The UNNEST function is used to expand arrays or maps. If you want to expand a string, you must transform the string into a JSON object, and then convert the JSON object into an array or map. To do this, you can use the `cast(json_parse(array_column) as array(bigint))` function.

Traverse every element of an array Expands an array into multiple rows by using the following SQL SELECT statement:

```
* | select  array_column, a   from log, unnest( cast( json_parse(array_column)   as array(bigint) ) )
as t(a)
```

The UNNEST function `unnest( cast( json_parse(array_column) as array(bigint) ) ) as t(a)` expands the array into multiple rows. The rows are stored in a derived table referenced as t, with the column referenced as a. Calculate the sum of the elements in an array:

```
* | select   sum(a)    from log, unnest( cast( json_parse(array_column)   as array(bigint) ) ) as
t(a)
```

Perform a GROUP BY operation on all elements of an array:

```
* | select   a, count(1)    from log, unnest( cast( json_parse(array_column)   as array(bigint) ) )
as t(a) group by a
```

Traverse every key and value of a map Traverse every key and value of a map:

```
* | select  map_column , a,b    from log, unnest( cast( json_parse(map_column)   as map(varchar, bi
gint) ) ) as t(a,b)
```

Perform a GROUP BY operation on all keys of a map:

```
* | select   key,  sum(value)    from log, unnest( cast( json_parse(map_column)   as map(varchar, b
igint) ) ) as t(key,value) GROUP BY key
```

Visualize the query results of the histogram and numeric_histogram functions. histogram The histogram function works in a similar manner to the count group by syntax. For more information about the histogram function, see Map functions. In most cases, the histogram function returns a JSON object. The following is an example:

```
* | select histogram(method)
```

You can use the UNNEST function to expand JSON data into multiple rows. Then the data can be visualized. The following is an example:

```
* | select  key , value  from( select histogram(method) as his from log) , unnest(his ) as t(key,va
lue)
```

numeric_histogram The numeric_histogram function assigns a column of numeric values into multiple bins. This function is equivalent to a GROUP BY operation that is performed on a numeric value column. For more information about the syntax of the numeric_histogram function, see Approximate functions.

```
* | select numeric_histogram(10,Latency)
```

Use the following SELECT statement to visualize the result:

```
* |  select key,value from(select numeric_histogram(10,Latency) as his from log) , unnest(his) as t
(key,value)
```

### 4.9 Machine learning syntax and functions

functions

#### 4.9.1 Overview

The machine learning feature of Log Service supports multiple algorithms and calling methods. You can use SELECT statements and machine learning functions to analyze the characteristics of a field or fields within a period of time. Log Service offers multiple time series analysis algorithms to help you implement time series prediction, time series anomaly detection, time series decomposition, and multi-time series clustering. The algorithms are compatible with standard SQL statements. This greatly simplifies the use of the algorithms and improves the troubleshooting efficiency. Features Supports various smooth operations on single-time series data. Supports algorithms related to the prediction, anomaly detection, change point detection, inflection point detection, and multi-period estimation of single-time series data. Supports decomposition operations on single-time series data. Supports various clustering algorithms of multi-time series data. Supports multi-field pattern mining (based on the sequence of numeric data or text). The specified time series data must be sampled based on the same interval. The specified time series data cannot contain data repeatedly sampled from the same time point.

| Item | Description |
|---|---|
| Processing capacity of time-series data | Data can be collected from a maximum of 150,000 consecutive time points. If the data volume exceeds the processing capacity, you must aggregate the data or reduce the sampling amount. |
| Clustering capacity of the density- based clustering algorithm | A maximum of 5,000 time series curves, each of which cannot contain more than 1,440 time points. |
| Clustering capacity of the hierarchical clustering algorithm | A maximum of 2,000 time series curves, each of which cannot contain more than 1,440 time points. |

Machine learning functions

| Type | Function | Description |
|---|---|---|
| Smooth functions | ts smooth simple _ _ | Uses the Holt Winters algorithm to smooth time series data. |
|   | ts smooth fir _ _ | Uses the finite impulse response (FIR) filter to smooth time series data. |
|   | ts smooth iir _ _ | Uses the infinite impulse response (IIR) filter to smooth time series data. |
| Multi-period estimation functions | ts period detect _ _ | Forecasts time series data by period. |
| Change point detection functions | ts cp detect _ _ | Finds intervals with different statistical characteristics from time series data. The interval endpoints are change points. |
|   | ts breakout detect _ _ | Finds the time points when statistics steeply increases or decreases from time series data. |
| Maximum value detection function | ts find peaks _ _ | Finds the local maximum value of time series data in a specified window. |
|   | ts predicate simple _ _ | Uses default parameters to model time series data and performs simple time series prediction and anomaly detection. |
|   | ts predicate ar _ _ | Uses an autoregressive (AR) model to model time series data and performs simple time series prediction and anomaly detection. |

| og Service |   |   |
|---|---|---|
|   | User Guide·Query and analysi |   |
| PTryepdeiction and anomaly detection functions | Function | Description |
|   | ts predicate arma _ _ | Uses an autoregressive moving average (ARMA) model to model time series data and performs simple time series prediction and anomaly detection. |
|   | ts predicate arima _ _ | Uses an autoregressive integrated moving average (ARIMA) model to model time series data and performs simple time series prediction and anomaly detection. |
|   | ts regression predict _ _ | Accurately predicts the trend for a single periodic time series with a certain tendency. |
| Time series decomposition function | ts decompose _ | Uses the Seasonal and Trend decomposition using Loess (STL) algorithm to decompose time series data. |
| Time series clustering functions | ts density cluster _ _ | Uses a density-based clustering method to cluster multiple pieces of time series data. |
|   | ts hierarchical cluster _ _ | Uses a hierarchical clustering method to cluster multiple pieces of time series data. |
|   | ts similar instance _ _ | Queries curves that are similar to a specified curve. |
| Frequent pattern statistics function | pattern stat _ | Mines representative combinations of attributes among the given multi-attribute field samples to obtain the frequent pattern in statistical patterns. |
| Differential pattern statistics function | pattern diff _ | Finds the pattern that causes differences between two collections under specified conditions. |
| Root cause analysis function | rca kpi search _ _ | When a time series metric is abnormal, you can use the root cause analysis function to analyze the dimension attributes that result in the abnormal metric in a timely manner. |
| Correlation analysis functions | ts association analysis _ _ | Quickly finds the metrics that are correlated with a specified metric among multiple observed metrics in the system. |
| ts similar _ | Quickly finds the metrics that are correlated with specified time series data among multiple observed metrics in the system. |   |
| Kernel density estimation function | kernel density estimation _ _ | Uses the smooth peak function to fit the observed data points, thus simulating the real probability distribution curve. |

#### 4.9.2 Smooth functions

This topic describes the smooth functions that you can use to smooth and filter specified time series curves. Filtering is the first step to discover the shapes of time series curves. Functions

| Function | Description |
|---|---|
| ts smooth simple _ _ | Uses the Holt-Winters algorithm to filter time series data. This function is the default smooth function. |
| ts smooth fir _ _ | Uses a finite impulse response (FIR) filter to filter time series data. |
| ts smooth iir _ _ | Uses an infinite impulse response (IIR) filter to filter time series data. |

ts_smooth_simple Syntax:

```
select ts_smooth_simple(x, y)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | The Unix timestamp of the time series data. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |

Example The search and analytic statement is shown as follows:

```
* | select ts_smooth_simple(stamp, value) from ( select __time__ - __time__ % 120 as stamp, avg(v
) as value from log GROUP BY stamp order by stamp )
```

The following figure shows the response. The following table lists the display items.

| Item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of time series data. Unit: seconds. |
| Vertical axis | src | The unfiltered data. |
|   | filter | The filtered data. |

ts_smooth_fir Syntax: If you cannot determine filter parameters, use built-in window parameters in the following statement:

```
select ts_smooth_fir(x, y,winType,winSize)
```

If you can determine filter parameters, you can specify the parameters as needed in the following statement:

```
select ts_smooth_fir(x, y,array[])
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |
| winType | The type of window used for filtering. | Valid values: rectangle: rectangle window. hanning: hanning window hamming: hamming window. blackman: blackman window. Not e We recommend that you select the rectangle window for better display effects. |
| winSize | The length of the filtering window. | The value is of the LONG type. Valid values: 2 to 15. |
| array[] | The parameter used for FIR filtering. | The value is an array where the sum of elements is 1. For example, array[0.2, 0.4, 0.3, 0.1]. |

Example 1 The search and analytic statement is shown as follows:

```
* | select ts_smooth_fir(stamp, value, 'rectangle', 4) from ( select __time__ - __time__ % 120 as
stamp, avg(v) as value from log GROUP BY stamp order by stamp )
```

The following figure shows the response. Example 2 The search and analytic statement is shown as follows:

```
* | select ts_smooth_fir(stamp, value, array[0.2, 0.4, 0.3, 0.1]) from ( select __time__ - __time
__ % 120 as stamp, avg(v) as value from log GROUP BY stamp order by stamp )
```

The following figure shows the response. The following table lists the display items.

| Item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of the time series data. Unit: seconds. |
| Vertical axis | src | The unfiltered data. |
|   | filter | The filtered data. |

ts_smooth_iir Syntax:

```
select ts_smooth_iir(x, y, array[], array[] )
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |
| array[] | The parameter used for IIR filtering in terms of x i . | The value is an array where the sum of elements is 1. The length of the array ranges from 2 to 15. For example, array[0.2, 0.4, 0.3, 0.1]. |
| array[] | The parameter used for IIR filtering in terms of y i−1 . | The value is an array where the sum of elements is 1. The length of the array ranges from 2 to 15. For example, array[0.2, 0.4, 0.3, 0.1]. |

Example The search and analytic statement is shown as follows:

```
* | select ts_smooth_iir(stamp, value, array[0.2, 0.4, 0.3, 0.1], array[0.4, 0.3, 0.3]) from ( se
lect __time__ - __time__ % 120 as stamp, avg(v) as value from log GROUP BY stamp order by stamp )
```

The following figure shows the response. The following table lists the display items.

| Item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of the time series data. Unit: seconds. |
| Vertical axis | src | The unfiltered data. |
|   | filter | The filtered data. |

#### 4.9.3 Multi-period estimation functions

This topic describes the multi-period estimation functions that are supported by Log Service. You can use the functions to estimate the periods of time series data in different time intervals. You can also extract the periods by performing a series of operations such as Fourier transform (FT). Functions

| Function | Description |
|---|---|
| ts period detect _ _ | Estimates the periods of time series data that is distributed in different time intervals. |
| ts period classify _ _ | Uses FT to calculate the periodicity of specified time series curves. This function can be used to identify periodic curves. |

ts_period_detect Syntax:

```
select ts_period_detect(x,y,minPeriod,maxPeriod)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The points in time along the horizontal axis are sorted in ascending order. | Each point is a UNIX timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified point in time. | - |

| User Guide·Query and | analysis | Log Servic |
|---|---|---|

| Parameter | Description | Value |
|---|---|---|
| minPeriod | The ratio of the minimum length of the estimated period to the total length of the time series data. | The value must be a decimal number. Value range: (0, 1]. |
| maxPeriod | The ratio of the maximum length of the estimated period to the total length of the time series data. Not e The value of the maxPeriod parameter must be greater than the value of the minPeriod parameter. | The parameter value must be a decimal number. Value range: (0, 1]. |

Example: Query statement

```
* | select ts_period_detect(stamp, value, 0.2, 1.0) from ( select __time__ - __time__ % 120 as stam
p, avg(v) as value from log GROUP BY stamp order by stamp )
```

Result The following table lists the display items.

| Display item | Description |
|---|---|
| period id _ | An array with a length of 1. The element in the array indicates the sequence number of the period. The array [0] indicates the original time series curve. |
| time series _ | The sequence of timestamps. |
| data series _ | The sequence of data at each timestamp. If the value of period id is 0, the returned data is the original time series _ data. If the value of period id is not 0, the data returned is filtered time series _ data. |

ts_period_classify Syntax:

```
select ts_period_classify(stamp,value,instanceName)
```

The following table lists the parameters.

| Parameter | Description | Value |
|---|---|---|

| Parameter | Description | Value |
|---|---|---|
| stamp | The time sequence. The points in time along the horizontal axis are sorted in ascending order. | Each point in time is a UINX timestamp. Unit: seconds. |
| value | The sequence of numeric data at each specified point in time. | - |
| instanceName | The name of the time series curve. | - |

Example: The following query statement is executed:

```
* and h : nu2h05202.nu8 | select ts_period_classify(stamp, value, name) from log
```

Query result The following table lists the display items.

| Display item | Description |
|---|---|
| line name _ | An array with a length of 1. The element in the array indicates the sequence number of the period. The array [0] indicates the original time series curve. |
| prob | The ratio of the primary period length to the length of the time series curve. Value range: [0, 1]. You can set the value to 0.15 when you perform a test. |
| type | The type of the curve. Valid values: -1, -2, and 0. The value -1 indicates that the length of the time series curve is too short (less than 64 points). The value -2 indicates the time series curve has a high fault rate (the fault rate exceeds 20%). The value 0 indicates the time series curve is periodic. |

#### 4.9.4 Change point detection functions

This topic describes the change point detection functions in Log Service. You can use the functions to detect the change points in time series data. The change point detection functions can detect the following two kinds of change points: Statistics feature changes within a specified period of time Anomalies in time series data Functions

| Function | Description |
|---|---|
| ts cp detect _ _ | Finds intervals in which data has different statistics features. The interval endpoints are change points. |
| ts breakout detect _ _ | Finds the time points at which data experiences dramatic changes. |

ts_cp_detect Syntax: If you cannot specify an appropriate time window size, use the following syntax. The default window size used in the function is 10.

```
select ts_cp_detect(x, y, samplePeriod)
```

To adjust the effect specific to your business environment, you can specify the minSize parameter in the following function.

```
select ts_cp_detect(x, y, minSize)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |
| minSize | The minimum length of time series data in a continuous interval. | The minimum value is 3 and the maximum value cannot exceed ten percent of the length of the specified time series data. |

Example: The search and analytic statement is shown as follows:

```
* | select ts_cp_detect(stamp, value, 3) from (select __time__ - __time__ % 10 as stamp, avg(v) as
value from log GROUP BY stamp order by stamp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of time series data, measured in seconds, for example, 1537071480. |

| og Service |   | User Guide·Query and analysi |
|---|---|---|
| Display item |   | Description |
| Vertical axis | src | The unfiltered data, such as 1956092.7647745228. |
|   | prob | The probability that a time point is a change point. Valid values: 0 to 1. |

ts_breakout_detect Syntax:

```
select ts_breakout_detect(x, y, winSize)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |
| winSize | The minimum length of time series data in a continuous interval. | The minimum value is 3 and the maximum value cannot exceed ten percent of the length of the specified time series data. |

Example: The search and analytic statement is shown as follows:

```
* | select ts_breakout_detect(stamp, value, 3) from (select __time__ - __time__ % 10 as stamp, avg(
v) as value from log GROUP BY stamp order by stamp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of time series data, measured in seconds, for example, 1537071480. |
| Vertical axis | src | The unfiltered data, such as 1956092.7647745228. |
|   | prob | The probability that a time point is a change point. Valid values: 0 to 1. |

#### 4.9.5 Maximum value detection function

This topic describes the available maximum value detection function in Log Service. You can use the functions to find the local maximum value of time series data in a specified window. ts_find_peaks Syntax:

```
select ts_find_peaks(x, y, winSize)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | - |
| winSize | The minimum length of the detection window. | The value of the parameter is of the LONG type, ranging from 1 to the length of time series data. We recommend that you set this parameter to ten percent of the actual data length. |

Example: The search and analytic statement is shown as follows:

```
* and h : nu2h05202.nu8 and m: NET |  select ts_find_peaks(stamp, value, 30) from (select __time__
- __time__ % 10 as stamp, avg(v) as value from log GROUP  BY  stamp order by stamp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of time series data, measured in seconds, for example, 1537071480. |
|   | src | The unfiltered data, such as 1956092.7647745228. |

| og Service |   |   |
|---|---|---|
|   | User Guide·Query and analysi |   |
| Display item Vertical axis |   | Description |
|   | peak flag _ | Indicates whether the numeric value at the time point is the maximum value. Valid values: 1.0 and 0.0. 1.0: The numeric value at the time point is the maximum value. 0.0: The numeric value at the time point is not the maximum value. |

#### 4.9.6 Prediction and anomaly detection functions

Prediction and anomaly detection functions predict the trend of time series curves and identify the Ksigma and quantiles of the errors between a predicted curve and an actual curve. You can use the functions to detect anomalies. Introduction to Log Service machine learning (01): Time Series Statistics Modeling Introduction to Log Service machine learning (03): Time Series Anomaly Detection Modeling Introduction to Log Service machine learning (05): Time Series Prediction Best practices for Log Service machine learning: Time Series Anomaly Detection and Alert Functions

| Function | Description |
|---|---|
| ts predicate simple _ _ | Uses default parameters to model time series data and performs prediction and anomaly detection on time series data. |
| ts predicate ar _ _ | Uses an autoregressive (AR) model to model time series data and performs prediction and anomaly detection on time series data. |
| ts predicate arma _ _ | Uses an autoregressive moving average (ARMA) model to model time series data and performs prediction and anomaly detection on time series data. |
| ts predicate arima _ _ | Uses an autoregressive integrated moving average (ARIMA) model to model time series data and performs prediction and anomaly detection on time series data. |
| ts regression predict _ _ | Accurately predicts the trend for a periodic time series curve. Scenario: This function can be used to predict metering data, network traffic, financial data, and different business data that follows certain rules. |
| ts anomaly filter _ _ | Filters the anomalies detected from multiple time series curves based on the custom anomaly mode. The anomalies are detected during the anomaly detection. This function helps you find abnormal curves in a timely manner. |

ts_predicate_simple Syntax:

```
select ts_predicate_simple(x, y, nPred, isSmooth)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |
| nPred | The number of points for prediction. | The value is of the LONG data type and must be equal to or greater than 1. |
| isSmooth | Specifies whether to filter the raw data. | The value is of the Boolean type. The default value is True, which indicates to filter raw data. |

Example: A search and analytic statement is shown as follows:

```
* | select ts_predicate_simple(stamp, value, 6) from (select __time__ - __time__ % 60 as stamp, avg
(v) as value from log GROUP BY stamp order by stamp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of the data. Unit: seconds. |
| Vertical axis | src | The raw data. |
|   | predict | The predicted data. |
|   | upper | The upper limit of the prediction. The confidence level is 0.85. This value cannot be modified. |
|   | lower | The lower limit of the prediction. The confidence level is 0.85. This value cannot be modified. |
|   | anomaly prob _ | The probability that the point is an anomaly. Valid values: [0, 1]. |

ts_predicate_ar Syntax:

```
select ts_predicate_ar(x, y, p, nPred, isSmooth)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |
| p | The order of the AR model. | The value is of the LONG data type. Valid values: [2, 8]. |
| nPred | The number of points for prediction. | The value is of the LONG data type. Valid values: [1, 5 × p]. |
| isSmooth | Specifies whether to filter the raw data. | The value is of the Boolean type. The default value is true, which indicates to filter raw data. |

An example search and analytic statement is shown as follows:

```
* | select ts_predicate_ar(stamp, value, 3, 4) from (select __time__ - __time__ % 60 as stamp, avg(v)
as value from log GROUP BY stamp order by stamp)
```

> Not e The response is similar to that of the ts_predicate_simple function. For more information, see the response of the ts_predicate_simple function.

ts_predicate_arma Syntax:

```
select ts_predicate_arma(x, y, p, q, nPred, isSmooth)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |
| p | The order of the AR model. | The value is of the LONG data type. Valid values: [2, 100]. |
| q | The order of the ARMA model. | The value is of the LONG data type. Valid values: [2, 8]. |
| nPred | The number of points for prediction. | The value is of the LONG data type. Valid values: [p, 5p]. |
| isSmooth | Specifies whether to filter the raw data. | The value is of the Boolean type. The default value is true, which indicates to filter raw data. |

An example search and analytic statement is shown as follows:

```
* | select ts_predicate_arma(stamp, value, 3, 2, 4) from (select __time__ - __time__ % 60 as stamp, av
g(v) as value from log GROUP BY stamp order by stamp)
```

> Not e The response is similar to that of the ts_predicate_simple function. For more information, see the response of the ts_predicate_simple function.

ts_predicate_arima Syntax:

```
select ts_predicate_arima(x,y, p, d, q, nPred, isSmooth)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |
| p | The order of the AR model. | The value is of the LONG data type. Valid values: [2, 8]. |
| d | The order of the ARIMA model. | The value is of the LONG data type. Valid values: [1, 3]. |
| q | The order of the ARMA model. | The value is of the LONG data type. Valid values: [2, 8]. |
| nPred | The number of points for prediction. | The value is of the LONG type. Valid values: [p, 5p]. |
| isSmooth | Specifies whether to filter the raw data. | The value is of the Boolean type. The default value is True, which indicates to filter raw data. |

An example search and analytic statement is shown as follows:

```
* | select ts_predicate_arima(stamp, value, 3, 1, 2, 4) from (select __time__ - __time__ % 60 as stamp
, avg(v) as value from log GROUP BY stamp order by stamp)
```

> Not e The response is similar to that of the ts_predicate_simple function. For more information, see the response of the ts_predicate_simple function.

ts_regression_predict Syntax:

```
select ts_regression_predict(x, y, nPred, algotype,processType)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |
| nPred | The number of points for prediction. | The value is of the LONG data type. Valid values: [1, 500]. |
| algotype | The algorithm type for prediction. | Valid values: origin: uses the Gradient Boosted Regression Tree (GBRT) algorithm for prediction. forest: uses the GBRT algorithm for prediction based on the trend component decomposed by Seasonal and Trend decomposition using Loess (STL), and then uses the additive model to sum up the decomposed components and obtains the predicted data. linear: uses the Linear Regression algorithm for prediction based on the trend components decomposed by STL, and then uses the additive model to sum up the decomposed components and obtains the predicted data. |
| processType | Specifies whether to preprocess the data. | Valid values: 0: no additional data preprocessing is performed. 1: removes abnormal data before prediction. |

Example: A search and analytic statement is shown as follows:

```
* and h : nu2h05202.nu8 and m: NET |  select ts_regression_predict(stamp, value, 200, 'origin') fro
m (select __time__ - __time__ % 60 as stamp, avg(v) as value from log GROUP BY stamp order by sta mp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of the data. Unit: seconds. |
|   | src | The raw data. |
| Document Version: 20220 | 928 28 |   |

| User Guide·Query and analy | sis | Log Servic |
|---|---|---|
| Vertical axis Display item |   | Description |
|   | predict | The predicted data. |

ts_anomaly_filter Syntax:

```
select ts_anomaly_filter(lineName, ts, ds, preds, probs, nWatch, anomalyType)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| lineName | The name of each curve. The value is of the VARCHAR data type. | N/A |
| ts | The time sequence of the curve, which indicates the time of the current curve. The parameter value is an array of time points of the DOUBLE data type sorted in the ascending order. | N/A |
| ds | The actual value sequence of the curve. The parameter value is an array of data points with the same length as the ts parameter value. | N/A |
| preds | The predicted value sequence of the curve. The parameter value is an array of data points with the same length as the ts parameter value. | N/A |
| probs | The sequence of anomaly detection results of the curve. The parameter value is an array of data points with the same length as the ts parameter value. | N/A |
| nWatch | The number of the recently observed actual values on the curve. The value is of the LONG data type. The value must be smaller than the number of time points on the curve. | N/A |
| anomalyType | The type of anomaly to be filtered. The value is of the LONG data type. | Valid values: 0: all anomalies. 1: positive anomalies. -1: negative anomalies. |

Example: A search and analytic statement is shown as follows:

```
* | select res.name, res.ts, res.ds, res.preds, res.probs
     from (
         select ts_anomaly_filter(name, ts, ds, preds, probs, cast(5 as bigint), cast(1 as bigint))
as res
       from (
         select name, res[1] as ts, res[2] as ds, res[3] as preds, res[4] as uppers, res[5] as lowe
rs, res[6] as probs
     from (
         select name, array_transpose(ts_predicate_ar(stamp, value, 10)) as res
         from (
           select name, stamp, value from log where name like '%asg-%') group by name)) );
```

The following figure shows the response.

```
| name                     | ts                                                   | ds          | p
reds | probs |
| ------------------------ | ---------------------------------------------------- | ----------- | -
-------- | ----------- |
| asg-bp1hylzdi2wx7civ0ivk | [1.5513696E9, 1.5513732E9, 1.5513768E9, 1.5513804E9] | [1,2,3,NaN] | [
1,2,3,4] | [0,0,1,NaN] |
```

#### 4.9.7 Time series decomposition function

The time series decomposition function decomposes time series curves into curves that reveal the trend and periodicity of curves. ts_decompose Syntax:

```
select ts_decompose(x, y)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The time points along the x axis are sorted in the ascending order. | Each time point is a Unix timestamp. Unit: seconds. |
| y | The sequence of numeric data at each specified time point. | N/A |

Example: A search and analytic statement is shown as follows:

```
* | select ts_decompose(stamp, value) from (select __time__ - __time__ % 60 as stamp, avg(v) as val
ue from log GROUP BY stamp order by stamp)
```

The following figure shows the response. The following table lists the display items.

| Display item |   | Description |
|---|---|---|
| Horizontal axis | unixtime | The Unix timestamp of the data. Unit: seconds. |
| Vertical axis | src | The raw time series data. |
|   | trend | The decomposed data that indicates the trend of the time series data. |
|   | season | The decomposed data that indicates the periodicity of the time series data. |
|   | residual | The residual data decomposed from the time series data. |

#### 4.9.8 Time series clustering functions

You can use time series clustering functions to cluster multiple time series and obtain different curve shapes. Then, you can find the cluster center and identify curves with shapes that are different from other curve shapes in the cluster in a timely manner. Functions

| Function | Description |
|---|---|
| ts density cluster _ _ | Uses a density-based clustering method to cluster multiple time series. |
| ts hierarchical cluster _ _ | Uses a hierarchical clustering method to cluster multiple time series. |
| ts similar instance _ _ | Queries time series curves that are similar to a specified time series curve. |

ts_density_cluster Syntax:

```
select ts_density_cluster(x, y, z)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The points in time along the horizontal axis are sorted in ascending order. | Each point in time is a UNIX timestamp. Unit: seconds. |
| y | The sequence of numeric data that corresponds to a specified point in time. | - |
| z | The name of the curve corresponding to the data at a specified point in time. | The value is of the string type, for example, machine01.cpu usr. _ |

Example The query statement:

```
* and (h: "machine_01" OR h: "machine_02" OR h : "machine_03") | select ts_density_cluster(stamp, m
etric_value,metric_name ) from ( select __time__ - __time__ % 600 as stamp, avg(v) as metric_value, h as metric_name from log GROUP BY stamp, metric_name order BY metric_name, stamp )
```

Output result The following table lists the display items.

| Display item | Description |
|---|---|
| cluster id _ | The category of the cluster. The value -1 indicates that the cluster is not categorized in any cluster center. |
| rate | The proportion of instances in the cluster. |
| time series _ | The timestamp sequence of the cluster center. |
| data series _ | The data sequence of the cluster center. |
| instance names _ | The instances that are included in the cluster center. |
| sim instance _ | The name of an instance in the cluster. |

ts_hierarchical_cluster Syntax:

```
select ts_hierarchical_cluster(x, y, z)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| x | The time sequence. The points in time along the horizontal axis are sorted in ascending order. | Each point in time is a UNIX timestamp. Unit: seconds. |
| y | The sequence of numeric data that corresponds to a specified point in time. | - |
| z | The name of the curve corresponding to the data at a specified point in time. | The value is of the string type, for example, machine01.cpu usr. _ |

Examples The query statement:

```
* and (h: "machine_01" OR h: "machine_02" OR h : "machine_03") | select ts_hierarchical_cluster(sta
mp, metric_value, metric_name) from ( select __time__ - __time__ % 600 as stamp, avg(v) as metric_v alue, h as metric_name from log GROUP BY stamp, metric_name order BY metric_name, stamp )
```

Output result The following table lists the display items.

| Display item | Description |
|---|---|
| cluster id _ | The category of the cluster. The value -1 indicates that the cluster is not categorized in any cluster center. |
| rate | The proportion of instances in the cluster. |
| time series _ | The timestamp sequence of the cluster center. |
| data series _ | The data sequence of the cluster center. |
| instance names _ | The instances that are included in the cluster center. |
| sim instance _ | The name of an instance in the cluster. |

ts_similar_instance Syntax:

```
select ts_similar_instance(x, y, z, instance_name, topK, metricType)
```

The following table lists the parameters of the function.

|   | Parameter | Description | Value |
|---|---|---|---|
|   | x | The time sequence. The points in time along the horizontal axis are sorted in ascending order. | Each point in time is a UNIX timestamp. Unit: seconds. |
|   | y | The sequence of numeric data that corresponds to a specified point in time. | - |
|   | z | The name of the curve corresponding to the data at a specified point in time. | The value is of the string type, for example, machine01.cpu usr. _ |
|   | instancename _ | The name of a specified curve to be queried. | The value is of the string type, for example, machine01.cpu usr. _ Not e The curve to be queried must be an existing one. |
|   | topK | The maximum number of curves that are similar to the specified curve can be returned. | - |
|   |   | {'shape', 'manhattan', 'euclidean'} . The metric used to measure the similarity between time series curves. | - |
|   | metricType | 'euclidean'} |   |

The query statement:

```
* and m: NET and m: Tcp and (h: "nu4e01524.nu8" OR  h: "nu2i10267.nu8" OR  h : "nu4q10466.nu8") | sele
ct ts_similar_instance(stamp, metric_value, metric_name, 'nu4e01524.nu8' ) from ( select __time__ - __ time__ % 600 as stamp, sum(v) as metric_value, h as metric_name from log GROUP BY stamp, metric_name o rder BY metric_name, stamp )
```

The following table lists the display items.

| Display item | Description |
|---|---|
| instance name _ | The list of metrics that are similar to the specified metric. |
| time series _ | The timestamp sequence of the cluster center. |
| data series _ | The data sequence of the cluster center. |

#### 4.9.9 Frequent pattern statistics function

The frequent pattern statistics function combines representative attributes in a specified multi-attribute field sample. pattern_stat Syntax:

```
select pattern_stat(array[col1, col2, col3], array['col1_name', 'col2_name', 'col3_name'], array[col5, col6], array['col5_name', 'col6_name'], support_score, sample_ratio)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| array[col1, col2, col3] | A column of character values. | An array of values, for example, array[clientIP, sourceIP, path, logstore]. |
| array['col1name', _ 'col2name', _ 'col3name'] _ | The field names of the character values. | An array of field names, for example, array['clientIP', 'sourceIP', 'path', 'logstore']. |
| array[col5, col6] | A column of numeric values. | An array of values, for example, array[Inflow, OutFlow]. |
| array['col5name', _ 'col6name'] _ | The field names of the numeric values. | An array of field names, for example, array['Inflow', 'OutFlow']. |
| supportscore _ | The support ratio of samples for pattern mining. | The value is of the DOUBLE data type. Value range: (0,1]. |
| sampleratio _ | The sampling ratio. The default value is 0.1, which indicates that only 10% of the total samples are used. | The value is of the DOUBLE data type. Value range: (0,1]. |

Example: Query statement

```
* | select pattern_stat(array[ Category, ClientIP, ProjectName, LogStore, Method, Source, UserAgent
], array[ 'Category', 'ClientIP', 'ProjectName', 'LogStore', 'Method', 'Source', 'UserAgent' ], arr ay[ InFlow, OutFlow ], array[ 'InFlow', 'OutFlow' ], 0.45, 0.3) limit 1000
```

Display item

| Display item | Description |
|---|---|
| count | The number of samples in the current pattern. |
| support score _ | The score of the current pattern. The score indicates the degree to which the current pattern is supported. |
| pattern | The content of the pattern. The pattern is organized in the format that is defined by the query conditions. |

#### 4.9.10 Differential pattern statistics function

The differential pattern statistics function analyzes differential patterns of specified multi-field samples based on the specified condition. It helps you identify the causes of the differences under the current condition in a timely manner. pattern_diff Syntax:

```
select pattern_diff(array_char_value, array_char_name, array_numeric_value, array_numeric_name, condit ion, supportScore,posSampleRatio,negSampleRatio )
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| arraycharvalue _ _ | A column of values of the character data type. | An array of values, for example, array[clientIP, sourceIP, path, logstore]. |
| arraycharname _ _ | The field names of the values of the character data type. | An array of field names, for example, array['clientIP', 'sourceIP', 'path', 'logstore']. |
| arraynumericvalue _ _ | A column of values of the numeric data type. | An array of values, for example, array[Inflow, OutFlow]. |
| arraynumericname _ _ | The field names of the values of the numeric data type. | An array of field names, for example, array[originflow', 'OutFlow']. |
| condition | The condition for filtering data. The value True indicates positive samples, and the value False indicates negative samples. | For example, Latency <= 300. |
| supportScore | The support ratio of positive and negative samples for pattern mining. | The value is of the DOUBLE data type. Valid values: (0,1]. |
| posSampleRatio | The sampling ratio of positive samples. The default value is 0.5, indicating that 50% of positive samples are collected. | The value is of the DOUBLE data type. Valid values: (0,1]. |
| negSampleRatio | The sampling ratio of negative samples. The default value is 0.5, indicating that 50% of positive samples are collected. | The value is of the DOUBLE data type. Valid values: (0,1]. |

Example: A search and analytic statement is shown as follows:

```
* | select pattern_diff(array[ Category, ClientIP, ProjectName, LogStore, Method, Source, UserAgent
], array[ 'Category', 'ClientIP', 'ProjectName', 'LogStore', 'Method', 'Source', 'UserAgent' ], arr ay[ InFlow, OutFlow ], array[ 'InFlow', 'OutFlow' ], Latency > 300, 0.2, 0.1, 1.0) limit 1000
```

Display item

| Display item | Description |
|---|---|
| possupport | The support ratio of positive samples for the mined patterns. |
| posconfidence | The confidence level of the mined patterns in positive samples. |
| negsupport | The support ratio of negative samples for the mined patterns. |
| diffpattern | The content of the mined patterns. |

#### 4.9.11 Root cause analysis function

Log Service provides the alert and analytics features that help you quickly analyze data and locate anomalies of specific subdimensions of a metric. You can use the root cause analysis function to analyze the subdimension attributes that result in anomalies of the monitoring metric. rca_kpi_search Syntax

```
select rca_kpi_search(varchar_array, name_array, real, forecast, level)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| varchararray _ | The subdimension attributes. | The parameter value is formatted in an array, for example, array[col1, col2, col3]. |
| namearray _ | The subdimension attribute names. | The parameter value is formatted in an array, for example, array['col1', 'col2', 'col3']. |
| real | The actual value of each subdimension attribute specified by the varchar array parameter. _ | The parameter value is of the DOUBLE data type. Valid values: all real numbers. |
| forecast | The predicted value of each subdimension attribute specified by the varchar array parameter. _ | The parameter value is of the DOUBLE data type. Valid values: all real numbers. |
| level | The number of subdimension attributes identified in the returned root cause set. The value 0 indicates that all root causes that are found are returned. | The parameter value is of the LONG data type. Valid values: [0, number of analyzed subdimensions]. The number of analyzed subdimensions is the length of the array specified by the varchar array parameter. _ |

Example: The search and analytic statement is shown as follows: Use a subquery to obtain the actual value and predicted value of each subdimension attribute, and then call the rca_kpi_search function to analyze the root causes of anomalies.

```
* not Status:200 |
select rca_kpi_search(
 array[ ProjectName, LogStore, UserAgent, Method ],
 array[ 'ProjectName', 'LogStore', 'UserAgent', 'Method' ], real, forecast, 1)
from ( select ProjectName, LogStore, UserAgent, Method,
 sum(case when time < 1552436040 then real else 0 end) * 1.0 / sum(case when time < 1552436040
then 1 else 0 end) as forecast,
 sum(case when time >=1552436040 then real else 0 end) *1.0 / sum(case when time >= 1552436040
then 1 else 0 end) as real
 from (
select __time__ - __time__ % 60 as time, ProjectName, LogStore, UserAgent, Method, COUNT(*) as real from log GROUP by time, ProjectName, LogStore, UserAgent, Method ) GROUP BY ProjectName, LogStore, UserAgent, Method limit 100000000)
```

The following figure shows the response. The following figure shows the structured response. The following table lists the display items.

| Display item | Description |
|---|---|
| rcSets | The root cause sets. Each value of this parameter is an array. |
| rcItems | A specific root cause set. |
| kpi | A specific item in the root cause set. Each item is formatted in an array where each element is a JSON object. The attr parameter indicates the subdimension name, and the val parameter indicates the attribute name under the subdimension. |
| nleaf | The number of leaf nodes that an item (KPI) in the root cause set covers in the original data. Not e Leaf node: the log entry that contains the finest-grained attribute information. |
| change | The ratio of anomalies of leaf nodes in a KPI to the total anomalies in the root cause set that occurred at the same time point. |
| score | The abnormality score of the current KPI. Valid values: [0, 1]. |

The response is formatted in a JSON object as follows: `{`

```json
  "rcSets": [
```

`{`

```json
    "rcItems": [
```

`{`

```json
      "kpi": [
```

`{`

```json
        "attr": "country",
        "val": "*"
```

`},` `{`

```json
        "attr": "province",
        "val": "*"
```

`},` `{`

```json
        "attr": "provider",
        "val": "*"
```

`},` `{`

```json
        "attr": "domain",
        "val": "download.huya.com"
```

`},` `{`

```json
        "attr": "method",
        "val": "*"
```

`}` `],`

```json
      "nleaf": 119,
      "change": 0.3180687806279939,
      "score": 0.14436007709620113
```

`}` `]` `}` `]` `}`

#### 4.9.12 Correlation analysis functions

You can use a correlation analysis function to find the metrics that are correlated with a specified metric or time series data among multiple observed metrics in the system. Functions

| Function | Description |
|---|---|
| ts association analysis _ _ | Quickly finds the metrics that are correlated with a specified metric among multiple observed metrics in the system. |
| ts similar _ | Quickly finds the metrics that are correlated with specified time series data among multiple observed metrics in the system. |

ts_association_analysis Syntax

```
select ts_association_analysis(stamp, params, names, indexName, threshold)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| stamp | The Unix timestamp of the LONG data type. | - |
| params | The metrics to be analyzed, formatted in an array where each element is of the DOUBLE data type. | The parameter value is formatted in an array where each element is of the DOUBLE data type. For example, Latency, QPS, and NetFlow. |
| names | The names of the metrics to be analyzed. | The parameter value is formatted in an array where each element is of the VARCHAR data type. For example, Latency, QPS, and NetFlow. |
| indexName | The name of the target metric. | The parameter value is of the VARCHAR data type, for example, Latency. |
| threshold | The threshold of correlation between the metrics to be analyzed and the target metric. | The parameter value is of the DOUBLE data type. Valid values: [0, 1]. |

Response name: the name of the metric that meets the specified correlation condition with the target metric. score: the value of correlation between the returned metric and the target metric. Valid values: [0, 1]. Sample statement

```
* | select ts_association_analysis(
              time,
              array[inflow, outflow, latency, status],
              array['inflow', 'outflow', 'latency', 'status'],
              'latency',
              0.1) from log;
```

Sample response

```
| results               |
| --------------------- |
| ['latency', '1.0']    |
| ['outflow', '0.6265'] |
| ['status', '0.2270']  |
```

ts_similar Syntax 1

```
select ts_similar(stamp, value, ts, ds) select ts_similar(stamp, value, ts, ds, metricType)
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| stamp | The Unix timestamp of the LONG data type. | - |
| value | The value of the metric to be analyzed. The parameter value is of the DOUBLE data type. | - |
| ts | The time sequence of the specified time series curve. The parameter value is formatted in an array where each element is of the DOUBLE data type. | - |
| ds | The sequence of numeric data of the specified time series curve. | - |
| metricType | The type of correlation between the measured curves. The parameter value is of the VARCHAR data type. | Valid values: SHAPE, RMSE, PEARSON, SPEARMAN, R2, and KENDALL |

Syntax 2

```
select ts_similar(stamp, value, startStamp, endStamp, step, ds) select ts_similar(stamp, value, startStamp, endStamp, step, ds, metricType )
```

The following table lists the parameters of the function.

| Parameter | Description | Value |
|---|---|---|
| stamp | The Unix timestamp of the LONG data type. | - |
| value | The value of the metric to be analyzed. This parameter is of the DOUBLE data type. | - |
| startStamp | The start timestamp of the specified time series curve. The parameter value is of the LONG data type. | - |
| endStamp | The end timestamp of the specified time series curve. The parameter value is of the LONG data type. | - |
| step | The time interval between two adjacent data points in a time series. The parameter value is of the LONG data type. | - |
| ds | The sequence of numeric data of the specified time series curve. The parameter is formatted in an array where each element is of the DOUBLE data type. | - |

| Parameter | Description | Value |
|---|---|---|
| metricType | The type of correlation between the measured curves. The parameter value is of the VARCHAR data type. | Valid values: SHAPE, RMSE, PEARSON, SPEARMAN, R2, and KENDALL |

Response score: the correlation between the analyzed metric and the specified time series curve. Valid values: [-1, 1]. Sample statement

```
* | select vhost, metric, ts_similar(time, value, 1560911040, 1560911065, 5, array[5.1,4.0,3.3,5.6,
4.0,7.2], 'PEARSON') from log group by vhost, metric;
```

Sample response

```
| vhost  | metric          | score                |
| ------ | --------------- | -------------------- |
| vhost1 | redolog         | -0.3519082537204182  |
| vhost1 | kv_qps          | -0.15922168009772697 |
| vhost1 | file_meta_write | NaN                  |
```

#### 4.9.13 Kernel density estimation function

Kernel density estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable. The Kernel density estimation function uses the smooth peak function to fit the observed data points. In this way, the function simulates the real probability distribution curve. Syntax

```
select kernel_density_estimation(bigint stamp, double value, varchar kernelType)
```

Parameters

| Parameter | Description |
|---|---|
| stamp | The Unix timestamp of observed data. Unit: second. |
| value | The observed value. |
| kernelType | box: rectangle window. epanechniov: Epanechnikov curve. gausener: Gaussian curve. |

Response

| Display item | Description |
|---|---|
| unixtime | The Unix timestamp of observed data. |
| real | The observed value. |
| pdf | The probability of each observed data point. |

Example Sample statement

```
* |
select
    date_trunc('second', cast(t1[1] as bigint)) as time, t1[2] as real, t1[3] as pdf from (
        select kernel_density_estimation(time, num, 'gaussian') as res from (
            select __time__ - __time__ % 10 as time, COUNT(*) * 1.0 as num from log group by time
order by time)
        ), unnest(res) as t(t1)  limit 1000
```

Response

### 4.10 Advanced analysis

#### 4.10.1 Optimize queries

This topic describes how to optimize queries to improve query efficiency. You can use the following methods to optimize queries: Increase the number of shards. Reduce the query time range and data volume. Repeat queries multiple times. Optimize the SQL statement for queries. Increase the number of shards More shards represent more computing resources and faster computing speed. You can increase the number of shards to ensure that the average number of log entries to be scanned in each shard does not exceed 50 million. You can increase the number of shards by splitting shards. For more information, see Split a shard.

> Not e Splitting shards incurs more fees and only accelerates queries of new data. Existing data is still stored in old shards.

Reduce the query time range and data volume The larger the time range, the slower the query. If you query data within a year or a month, data is computed by day. To facilitate computing, you can reduce the query time range. The larger the data volume, the slower the query. Reduce the amount of data to be queried as much as possible. Repeat queries multiple times If you find that the result of a query is inaccurate, you can repeat the query multiple times. The underlying acceleration mechanism ensures that each query uses the previous query result to analyze data. In this way, multiple queries make the query result more accurate. Optimize the SQL statement for queries A time-consuming query statement has the following characteristics: Performs the GROUP BY operation on string-type columns. Performs the GROUP BY operation on more than five fields. Includes operations that generates strings. You can use the following methods to optimize a query statement: Avoid operations that generate strings if possible. If you use the date_format function to generate a formatted timestamp, the query is inefficient.

```
* | select date_format(from_unixtime(__time__) , '%H_%i') as t, count(1) group by t
```

If you use the substr() function, strings are generated. We recommend that you use the date_trunc or time_series function in a query statement. Avoid performing the GROUP BY operation on string-formatted columns if possible. Performing the GROUP BY operation on strings may result in a large number of hash calculations, which account for more than 50% of total calculations. Examples:

```
* | select count(1) as pv , date_trunc('hour',__time__) as time group by time
* | select count(1) as pv , from_unixtime(__time__-__time__%3600) as time group by __time__-__time_
_%3600
```

Both query 1 and query 2 count the number of log entries per hour. However, query 1 converts the time into a string, for example, 2017-12-12 00:00:00, and then performs the GROUP BY operation on this string. Query 2 calculates the on-the-hour time value, performs the GROUP BY operation on the result, and then converts the value into a string. Query 1 is less efficient than query 2 because query 1 needs to hash strings. List fields alphabetically based on the initial letter when performing the GROUP BY operation on multiple columns. For example, you need to query 100 million users who are from 13 provinces.

```
Fast: * | select province,uid,count(1)groupby province,uid Slow: * | select province,uid,count(1)groupby uid,province
```

Use estimating functions. Estimating functions provide stronger performance than accurate calculation. In estimation, accuracy is compromised to an acceptable extent for fast calculation.

```
Fast: * |select approx_distinct(ip) Slow: * | select count(distinct(ip))
```

Specify only required columns in the SQL statement if possible. You can specify all columns in the search statement. In the SQL statement, specify only required columns if possible. This will speed up calculation.

```
Fast: * |select a,b c Slow: * |select *
```

Place columns that do not need to be grouped in an aggregate function if possible. For example, a user ID is associated with a username. Therefore, you can execute the Group By operation on user IDs to analyze data.

```
Fast: * | select userid, arbitrary(username), count(1)groupby userid Slow: * | select userid, username, count(1)groupby userid,username
```

Avoid using the IN operator if possible. If possible, avoid using the IN clause in SQL statements. Instead, use the OR clause.

```
Fast: key : a or key :b or key:c | select count(1) Slow: * | select count(1) where key in ('a','b')
```

#### 4.10.2 Use cases

This topic provides some use cases of log data analysis. Trigger an alert when the error rate exceeds 40% over the last 5 minutes Calculate the percentage of 500 Internal Server Error every minute. An alert is triggered when the error rate exceeds 40% over the last 5 minutes.

```
status:500 | select __topic__, max_by(error_count,window_time)/1.0/sum(error_count) as error_ratio, su m(error_count) as total_error from ( select __topic__, count(*) as error_count , __time__ - __time__ % 300 as window_time from log group by __topic__, window_time
```

`)`

```
group by __topic__ having max_by(error_count,window_time)/1.0/sum(error_count) > 0.4 and sum(erro r_count) > 500 order by total_error desc limit 100
```

Calculate the amount of transferred data and configure alerts Calculate the amount of transferred data every minute. An alert is triggered when transferred data plunges. Transferred data counted in the last minute does not cover a full minute. The `(max(time) - min(time))` clause is used for normalization to count the average traffic per minute.

```
* | SELECT SUM(inflow) / (max(__time__) - min(__time__))  as inflow_per_minute, date_trunc('minute',__
time__) as minute group by minute
```

Calculate the average latency of traffic data in different sizes Distribute traffic data to multiple bins based on the data size and calculate the average latency of the data in the bins.

```
* | select avg(latency) as latency , case when originSize < 5000 then 's1' when originSize < 20000 the
n 's2' when originSize < 500000 then 's3' when originSize < 100000000 then 's4' else 's5' end as os gr oup by os
```

Retrieve the percentages of different results List the number and the percentage of each result for different departments. This query includes subqueries and window functions. The `sum(c) over()` clause indicates the sum of values in all rows.

```
* |  select   department, c*1.0/ sum(c) over ()  from(select  count(1) as c, department   from log gro
up by department)
```

Count the number of log entries that meet the query condition To count the number of URLs based on their characteristics, you can use the CASE WHEN clause or the COUNT_IF clause. The latter clause is simpler.

```
* | select  count_if(uri like '%login') as login_num, count_if(uri like '%register') as register_num,
date_format(date_trunc('minute', __time__), '%m-%d %H:%i') as time group by time order by time limit
```

#### 4.10.3 Time field conversion examples

During search and analytics, you often need to process time fields in log data, such as converting a timestamp to another time format. This topic uses some examples to describe how to convert time fields. A log entry may include multiple time fields, for example: `__time__` : the time that you specify when you use the API or SDK to write log data. This field can be used for log data shipping, search, and analytics. Original time field in log data: the field that records the time when the log data is generated. This field is in raw logs. Time fields in different formats are difficult to read. To simplify the read process, you can convert the time format during search and analytics. For example, you can perform the following conversions:
1. Convert __time__ to a timestamp
2. Display __time__ in a specified format
3. Convert a timestamp to a specified format
Convert __time__ to a timestamp You can use the from_unixtime function to convert the `__time__` field to a timestamp.

```
* | select from_unixtime(__time__)
```

Display __time__ in a specified format To display the `__time__` field in the format of `YYYY-MM-DD HH:MM:SS` , you can use the date_format function.

```
* | select date_format(__time__, '%Y-%m-%d %H:%i:%S')
```

Convert the time in a log to a specified format To convert the time field in a log to the specified format ( `YYYY-MM-DD HH:MM:SS` ) and perform the GROUP BY operation on the `YYYY-MM-DD` part, you can use the date_format function. Sample log entry

```
__topic__: body_byte_sent: 307 hostname: www.host1.com http_user_agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHT ML, like Gecko) Mobile/14G60 QQ/7.1.8.452 V1_IPH_SQ_7.1.8_1_APP_A Pixel/750 Core/UIWebView NetType/ WIFI QBWebViewType/1 method: GET referer: www.host0.com remote_addr: 36.63.1.23 request_length: 111 request_time: 2.705 status: 200 upstream_response_time: 0.225582883754 url: /? k0=v9& time:2017-05-17 09:45:00
```

Example SQL statement

```
* | select date_format (date_parse(time,'%Y-%m-%d %H:%i:%S'), '%Y-%m-%d') as day, count(1) as uv gr
oup by day order by day asc
```

### 4.11 Visual analysis

#### 4.11.1 Analysis graph

##### 4.11.1.1 Overview

All search and analytics results can be rendered by using visualized charts. Prerequisites The index feature is enabled and configured. The analytics switches are turned on. For more information, see Enable the index feature and configure indexes for a Logstore. An analytic statement is included in a query statement. You cannot use charts to show query results if you do not include an analytic statement in your query statement. Precautions When multiple search and analytic statements are being executed in sequence, the Value Column, X Axis, or Y Axis information cannot automatically change based on the search and analytic statement. The X and Y axis information may remain the same as the last search and analytic statement. If this happens, the query results of the current search and analytic statement cannot be automatically displayed in a chart. If the following messages are returned, configure parameters on the Propert ies tab based on the current search and analytic statement: The currently selected dimensions are not in the queried results. Check and configure the attributes. X-Axis or Y-Axis is not available. Check and configure the attributes. Chart configurations On the Graph tab, various charts are provided to show query results. You can select a type of chart from the chart bar to show results. On the Graph tab, you can view the Chart Preview and Dat a Preview of query results of the current search and analytic statement. Chart Preview is the preview of the query results that are displayed in the specified type of chart. Dat a Preview displays the query results in a table. On the Graph tab on the right, you can configure the following chart properties: Dat a Source: used to set placeholder variables. For example, you configure the drill-down event of Chart A to redirect to the dashboard where Chart B is located. The placeholder variable you configured for Chart B is the same as the variable that you click to trigger the drill-down event. Then the placeholder variable is replaced with the variable you click to trigger the drill-down event and the search and analytic statement of Chart B is executed. For more information, see Drill-down analysis. This feature is applicable to scenarios where you configure drill-down events to redirect to targeted dashboards. Propert ies: used to configure the display properties of a chart, including the X axis, left and right Y axes, margins, font size and other properties. The properties vary with different type of charts. This feature is applicable to all search and analytics scenarios. Int eract ive Behavior: used to configure drill-down events for a chart. After you configure a drill-down event for the chart, you can click the variable value in the chart to trigger the specified drill-down event. For more information, see Drill-down analysis. This feature is applicable to triggering drill-down events for charts.

##### 4.11.1.2 Display query results in a table

Tables are used to sort and display data for quick reference and analysis. All query results that match specified query statements can be rendered into visualized charts. By default, query results are displayed in a table. Components Table header Row Column Where: The number of columns can be specified by using a `SELECT` statement. The number of rows is calculated based on the number of log entries in a specified time range. The default clause is `LIMIT 100` .
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. View the query result.
By default, the query result is displayed in a table on the Graph tab.
6. On the Propert ies tab, configure the properties of the table.
If you want to modify the rows and columns of the table or the entries to return on each page, you can set the parameters on the Properties tab.

| Parameter | Description |   |   |
|---|---|---|---|
| Items per Page | The number of entries to return on each page. |   |   |
| Zebra Striping | Specifies whether to display the query result in a zebra-striped table. |   |   |
| Transpose Rows and Columns | Specifies whether to transpose rows and columns. |   |   |
| Hide Reserved Fields | Specifies whether to hide reserved fields, such as time and sou __ __ __ rce . __ |   |   |
|   |   | sou __ |   |
| Disable Sorting | Specifies whether to disable the sorting feature. |   |   |
| Disable Search | Specifies whether to disable the search feature. |   |   |
| Highlight Settings | If you turn on Highlight Settings, you can create rules to highlight matched rows or columns. |   |   |
| Sparkline | If you turn on Sparkline, you can add an area chart, a line chart, or a column chart for columns in the table. |   |   |

|   | rce __ |
|---|---|

Example To query and analyze the distribution of page views (PVs) for different users based on status, execute the following query statement:

```
* |select Status,AlertDisplayName as name,COUNT(*) as count group by Status,name
```

##### 4.11.1.3 Display query results on a line chart

This topic describes how to configure a line chart to display query results. Background information Line charts are used to analyze the changes of field values based on an ordered data type. In most cases, the analysis is based on a specified time range. You can use a line chart to analyze the following change characteristics of field values over a specified period of time: Increment or decrement Increment or decrement rate Increment or decrement pattern, for example, periodicity Peak value and bottom value You can use line charts to analyze the changes of field values over a specified period of time. You can also use line charts to analyze the changes of multiple field values in multiple lines over the same period. This way, you can analyze the relationship between different fields. For example, the values of a field are proportional or inversely proportional to the values of another field. Each line chart consists of the following elements: X-axis Left Y-axis Right Y-axis (optional) Data point Line of trend changes Legend
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the line chart.

| Parameter | Description |
|---|---|
| X Axis | The sequential data. In most cases, a time series is selected. |
| Left Y Axis | The numeric data. You can select one or more fields for the left Y-axis. |
| Right Y Axis | The numeric data. You can select one or more fields for the right Y-axis. The layer of the right Y-axis is higher than the layer of the left Y-axis. |
| Column Marker | The column on the left or right Y-axis. The column is displayed as a histogram. |
| Legend | The position of the legend in the chart. Valid values: Top, Bottom, Left, and Right. |
| Format Left Y-axis | The format in which the data on the left and right Y-axis is displayed. |
| Format Right Y-axis |   |
| Line Type | The type of line that is displayed in the line chart. Valid values: St raight Line and Curve. |

| Log S | ervice | User Guide·Query and analysi | s |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Anomaly Point Column | The column where anomaly points are located. You can set the Anomaly Point Lower Limit and Anomaly Point Upper Limit parameters for a column. Anomaly Point Lower Limit : Values that are less than the lower limit are highlighted in red. Anomaly Point Upper Limit : Values that exceed the upper limit are highlighted in red. |
| Upper Limit Column | The area that is formed based on the values. |
| Lower Limit Column |   |
| Time Series | A series of data points that are listed in chronological order. |
| Time Format | The time format of the time series fields. |
| Margin | The distance between the axis and the borders of the chart. The parameters include Top Margin, Bottom Margin, Left Margin, and Right Margin. |

> Not e Each line in a line chart must contain more than two data points. Otherwise, the data trend cannot be generated. We recommend that you select no more than five lines for a line chart.

Example of a simple line chart To query the page views (PVs) of the IP address `203.0.113.10` in the previous 24 hours, execute the following query statement:

```
remote_addr: 203.0.113.10 | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as PV group by time order by time limit 1000
```

Select `time` for X Axis and `PV` for Left Y Axis. Set the Legend parameter and adjust the margins based on your business requirements. Example of a dual Y-axis line chart To query the PVs and number of unique visitors (UVs) in the previous 24 hours, execute the following query statement:

```
* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as PV, approx_di
stinct(remote_addr) as UV group by time order by time limit 1000
```

Select `time` for X Axis, `PV` for Left Y Axis, `UV` for Right Y Axis, and `PV` for Column Marker.

##### 4.11.1.4 Display query results on a column chart

This topic describes how to configure a column chart to display query results. Background information A column chart uses vertical or horizontal bars to show the values of different categories. You can use a column chart to count the number of values in each category. Each column chart consists of the following elements: X-axis (horizontal) Y-axis (vertical) Rectangular bar Legend By default, column charts in Log Service use vertical bars. Each rectangular bar has a fixed width and a variable height that indicates a value. If you select multiple columns of data for the Y-axis, a grouped column chart is used to display the data.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the column chart.

> Not e If a query statement returns no more than 20 log entries, you can use a column chart to display the query results. You can use a `LIMIT` clause to limit the number of rectangular bars. If the chart contains a large number of rectangular bars, the analysis results may not be displayed as expected. We recommend that you select no more than five fields for the Y-axis.

| Parameter | Description |
|---|---|
| X Axis | The categorical data. |
| Y Axis | The numeric data. You can select one or more fields for the left Y-axis. |
| Legend | The position of the legend in the chart. Valid values: Top, Bottom, Left, and Right. |
| Format | The format in which the data on the Y-axis is displayed. |
| Margin | The distance between the axis and the borders of the chart. The parameters include Top Margin, Bottom Margin, Left Margin, and Right Margin. |

Example of a simple column chart To query the number of visits for each `http_referer` in the specified time range, execute the following query statement:

```
* | select http_referer, count(1) as count group by http_referer
```

Select `http_referer` for X Axis and `count` for Y Axis. Example of a grouped column chart To query the number of visits and the average bytes for each `http_referer` in the specified time range, execute the following query statement:

```
* | select http_referer, count(1) as count, avg(body_bytes_sent) as avg group by http_referer
```

Select `http_referer` for X Axis. Select `count` and `avg` for Y Axis.

##### 4.11.1.5 Display query results on a bar chart

This topic describes how to configure a bar chart to display query results. Background information A bar chart is a horizontal column chart that is used to analyze the top N values of fields. You can configure a bar chart in a similar manner in which you configure a column chart. Each bar chart consists of the following elements: X-axis (vertical) Y-axis (horizontal) Rectangular bar Legend Each rectangular bar has a fixed height and a variable width. The variable width indicates a value. If multiple columns of data are mapped to the Y-axis, you can use a grouped bar chart to display the data.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the bar chart.

> Not e
> If a query statement returns no more than 20 log entries , you can use a bar chart to display the query results. You can also use a LIMIT clause to limit the number of rectangular bars. If the chart contains a large number of rectangular bars, analysis results may not be displayed as expected. You can also use an `ORDER BY` clause to analyze Top N values of fields. We recommend that you select no more than five fields for the Y-axis.
> You can use a grouped bar chart to display query results. However, the values represented by each rectangular bar in a group must be positively or negatively associated with each other.

| Parameter | Description |
|---|---|
| X Axis | The categorical data. |
| Y Axis | The numeric data. You can select one or more fields for the Y-axis. |
| Legend | The position of the legend in the chart. Valid values: Top, Bottom, Left, and Right. |
| Format X-axis | The format in which the data on the X-axis is displayed. |
| Margin | The distance between the axis and the borders of the chart. The parameters include Top Margin, Bottom Margin, Left Margin, and Right Margin. |

Example To analyze the top 10 request URIs ( `request_uri` ) that are most frequently visited, execute the following query statement:

```
* | select request_uri, count(1) as count group by request_uri order by count desc limit 10
```

##### 4.11.1.6 Display query results on a pie chart

This topic describes how to configure a pie chart to display query results. Background information A pie chart is used to show the percentages of different categories of data. The arc length of each segment in a pie chart is proportionate to the quantity that is represented by each category. A pie chart is divided into multiple segments based on the percentages of categories. Each segment shows the percentage of a category. The sum of all percentages is equal to 100%. Each pie chart consists of the following elements: Segment Percentage in the text format Legend Types Log Service provides the following types of standard pie charts: pie chart, donut chart, and polar area chart. Donut chart A donut chart is a variant of a pie chart that has a hollow center. Compared with a pie chart, a donut chart provides the following advantages: Displays more information, such as the total number of occurrences of all field values. Allows you to compare data between two donut charts based on ring lengths. Data across different pie charts is difficult to compare. Polar area chart A polar area chart is a column chart in the polar coordinate system. Each category of data is represented by a segment with the same angle, and the radius of each segment varies based on the value. Compared with a pie chart, a polar area chart provides the following advantages: If a query statement returns no more than 10 log entries, you can use a pie chart to display the query results. If a query statement returns 10 to 30 log entries, you can use a polar area chart to display the query results. Enlarges the differences among the values of categories because the area of the segment correlates with the square of the radius. Therefore, the polar area chart is suitable for the comparison of similar values. A circle can be used to display a periodic pattern. Therefore, you can use a polar area chart to analyze value changes in different periods, such as weeks and months.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the pie chart.

> Not e
> If a query statement returns no more than 10 log entries, you can use a pie chart or donut chart to display the query results. You can use a `LIMIT` clause to limit the number of segments. If a chart contains a large number of segments with different colors, the analysis results may not be displayed as expected.
> If the number of log entries exceeds 10, we recommend that you use a polar area chart or column chart.

| Parameter | Description |
|---|---|
| Chart Types | The type of the chart. Valid values: Pie Chart, Donut Chart, and Polar Area Chart. |
| Legend Filter | The categorical data. |
| Value Column | The values that correspond to different categories of data. |
| Legend | If you turn on Show Legend, you can set this parameter to adjust the position of the legend in the chart. |
| Format | The format in which data is displayed. |
| Tick Text Format | Valid values: Percent age and Cat egory: Percent age. |
| Margin | The distance between the axis and the borders of the chart. The parameters include Top Margin, Bottom Margin, Left Margin, and Right Margin. |

Example of a pie chart To analyze the percentages of the `requestURI` field values, execute the following query statement:

```
* | select requestURI as uri , count(1) as c group by uri limit 10
```

Example of a donut chart To analyze the percentages of the `requestURI` field values, execute the following query statement:

```
* | select requestURI as uri , count(1) as c group by uri limit 10
```

Example of a polar area chart To analyze the percentages of the `requestURI` field values, execute the following query statement:

```
* | select requestURI as uri , count(1) as c group by uri limit 10
```

##### 4.11.1.7 Display query results on an area chart

This topic describes how to configure an area chart to display query results. Background information An area chart is built based on a line chart. The colored section between a line and the axis is an area. The color is used to highlight the trend. An area chart is similar to a line chart and shows the changes of numeric values over a specified period of time. An area chart is used to highlight the overall data trend. Both line charts and area charts display the trend and relationship between numeric values instead of specific values. Each area chart consists of the following elements: X-axis (horizontal) Y-axis (vertical) Area segment
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the area chart.

> Not e In an area chart, a single area segment must contain more than two data points. If a single area segment contains two or fewer data points, the data trend cannot be analyzed. We recommend that you select less than five area segments in an area chart.

| Parameter | Description |
|---|---|
| X Axis | The sequential data. In most cases, a time series is selected. |
| Y Axis | The numeric data. You can select one or more fields for the Y-axis. |
| Legend | The position of the legend in the chart. Valid values: Top, Bottom, Left, and Right. |
| Format | The format in which data is displayed. |

| ervice | User Guide·Query and analysi |
|---|---|

| Parameter | Description |
|---|---|
| Margin | The distance between the axis and the borders of the chart. The parameters include Top Margin, Bottom Margin, Left Margin, and Right Margin. |

Example of a simple area chart To query the page views (PVs) of the IP address `203.0.113.10` in the previous 24 hours, execute the following query statement:

```
remote_addr: 203.0.113.10 | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, c ount(1) as PV group by time order by time limit 1000
```

Select `time` for X Axis and `PV` for Y Axis. Example of a cascade chart To query the number of PVs and the number of unique visitors (UVs) for each hour within one day, execute the following query statement:

```
* | select date_format(date_trunc('hour', __time__), '%m-%d %H:%i') as time, count(1) as PV, approx_di
stinct(remote_addr) as UV group by time order by time limit 1000
```

Select `time` for X Axis. Select `PV` and `UV` for Y Axis.

##### 4.11.1.8 Display query results on a single value chart

This topic describes how to configure a single value chart to display query results. Background information A single value chart highlights a single value. Log Service supports the following types of single value charts: Rectangle Frame: shows a general value. Dial: shows the difference between the current value and a specified threshold value. Compare Numb Chart: shows the SQL query results of interval-valued comparison and periodicity-valued comparison functions. For more information, see Interval-valued comparison and periodicity-valued comparison functions. By default, Rectangle Frame is selected. Rectangle Frame is the most basic type of single value chart to display data at a specified point. In most cases, this chart type is used to show the key information at a specified point in time. To display a proportional metric, you can select Dial. Each single value chart consists of the following elements: Numeric value Unit (optional) Description (optional) Chart type
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the single value chart.

> Not e Log Service normalizes data in charts that contain numeric values. For example, `230000` is processed as `230K` . You can include mathematical calculation functions in query statements to customize numeric formats. For more information, see Mathematical calculation functions.

The following table describes the parameters of a rectangle frame.

| Parameter | Description |
|---|---|
| Chart T ypes | The type of the single value chart. If you select Rect angle Frame, query results are displayed in a rectangle frame. |
| Value Column | The value that is displayed in the chart. By default, the data in the first row of the specified column is displayed. |
| Unit | The unit of the data. |
| Unit Font Size | The font size of the unit. You can drag the slider to adjust the font size. Valid values: 10 to 100. Unit: pixels. |
| Descript ion | The description of the value. |
| Descript ion Font Size | The font size of the description. You can drag the slider to adjust the font size. Valid values: 10 to 100. Unit: pixels. |
| Format | The format in which data is displayed. |
| Font Size | The font size of the value. You can drag the slider to adjust the font size. Valid values: 10 to 100. Unit: pixels. |
| Font Color | The color of the value, unit, and description in the chart. You can use the default color or select a color. |
| Background Color | The color of the background. You can use the default color or select a color. |

The following table describes the parameters of a dial.

| Parameter | Description |
|---|---|
| Chart T ypes | The type of the single value chart. If you select Dial, query results are displayed on a dial. |
| Act ual Value | The value that is displayed in the chart. By default, the data in the first row of the specified column is displayed. |
| Unit | The unit of the value on the dial. |
| Font Size | The font size of the value and unit. Valid values: 10 to 100. Unit: pixels. |
| Descript ion | The description of the value. |
| Descript ion Font Size | The font size of the description. You can drag the slider to adjust the font size. Valid values: 10 to 100. Unit: pixels. |
| Dial Maximum | The maximum value of the scale on the dial. Default value: 100. |
| Use Query Result s | If you turn on Use Query Results, Dial Maximum is replaced by Maximum Value Column. Then, you can select the maximum value from query results for this parameter. |
| Format | The format in which data is displayed. |
| Colored Regions | The number of segments that divide the dial. Each segment is displayed in a different color. Valid values: 2, 3, 4, and 5. Default value: 3. |
| Region Max Value | The maximum value of the scale in each colored segment of the dial. By default, the maximum value in the last segment is the maximum value on the dial. You do not need to specify this value. Not e By default, a dial is evenly divided into three colored segments. If you change the value of Colored Regions, Region Max Value is not automatically adjusted. You can manually set the maximum value for each colored segment based on your business requirements. |
| Font Color | The color of the value on the dial. |
| Region | The colored segments that divide the dial. By default, a dial is evenly divided into three segments. The segments are displayed in blue, yellow, and red. If you set Colored Regions to a value greater than 3, the added segments are displayed in blue by default. You can change the color of each segment. |

The following table describes the parameters of a compare numb chart.

| Parameter | Description |
|---|---|
| Chart T ypes | The type of the single value chart. If you select Compare Numb Chart, query results are displayed on a compare numb chart. |

| uide·Query and analysis | Log Servic |
|---|---|

| Parameter | Description |
|---|---|
| Show Value | The value that is displayed in the center of the compare numb chart. In most cases, this value is set to the statistical result that is calculated by the related comparison function in the specified time range. |
| Compare Value | The value that is compared with the threshold. In most cases, this value is set to the result of the comparison between the statistical results that are calculated by the related comparison function in the specified time range and in the previously specified time range. |
| Font Size | The font size of the show value. Valid values: 10 to 100. Unit: pixels. |
| Unit | The unit of the show value. |
| Unit Font Size | The font size of the unit for the show value. Valid values: 10 to 100. Unit: pixels. |
| Compare Unit | The unit of the compare value. |
| Compare Font Size | The font size of the compare value and unit. Valid values: 10 to 100. Unit: pixels. |
| Description | The description of the show value and its growth trend. |
| Descript ion Font Size | The font size of the description. Valid values: 10 to 100. Unit: pixels. |
| T rend Comparison T hreshold | The value that is used to measure the variation trend of the compare value. For example, the compare value is -1. If you set T rend Comparison T hreshold to 0, a down arrow that indicates a value decrease is displayed on the page. If you set T rend Comparison T hreshold to -1, the value remains unchanged. The system does not display the trend on the page. If you set T rend Comparison T hreshold to -2, an up arrow that indicates a value increase is displayed on the page. |
| Format | The format in which data is displayed. |
| Font Color | The color of the show value and its description. |
| Growt h Font Color | The font color of the compare value that is greater than the threshold. |
| Growt h Background Color | The background color that is displayed when the compare value is greater than the threshold. |
| Decrease Font Color | The font color that is displayed when the compare value is less than the threshold. |
| Decrease Background Color | The background color that is displayed when the compare value is less than the threshold. |
| Equal Background Color | The background color that is displayed when the compare value is equal to the threshold. |

Examples To view the number of page views (PVs), execute the following query statements. The analysis results are displayed in charts. Rectangle frame To view the number of PVs in the previous 15 minutes, execute the following query statement:

```
* | select count(1) as pv
```

Dial To view the number of PVs in the previous 15 minutes, execute the following query statement:

```
* | select count(1) as pv
```

Compare numb chart To view and compare the PVs on the current day and in the previous day, execute the following query statement:

```
* | select diff[1],diff[2], diff[1]-diff[2] from (select compare( pv , 86400) as diff from (select
count(1) as pv from log))
```

##### 4.11.1.9 Display query results on a progress bar

This topic describes how to configure a progress bar to display query results. Background information A progress bar shows the percentage of the actual value of a field to the maximum value of the field. You can configure the properties of a progress bar to change the style and configure display rules for the progress bar. Each progress bar consists of the following elements: Actual value Unit (optional) Total value
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the progress bar.

| Parameter | Description |
|---|---|
| Actual Value | The actual value in the chart. By default, data in the first row of the specified column is displayed. |
| Unit | The unit of the value in the progress bar. |
| Total Value | The maximum value indicated by the progress bar. Default value: 100. |

| Parameter | Description |
|---|---|
| Maximum Value Column | The maximum value in the specified column. If you turn on Use Query Result s, T ot al Value is replaced by Maximum Value Column. Then, you can select the maximum value from the query results for this parameter. |
| Use Query Results | If you turn on Use Query Results, Total Value is replaced by Maximum Value Column. Then, you can select the maximum value from the query results for this parameter. |
| Edge Shape | The edge shape of the progress bar. |
| Vertical Display | Specifies whether to display the progress bar in vertical display mode. |
| Font Size | The font size of the value in the progress bar. |
| Thickness | The thickness of the progress bar. |
| Background Color | The background color of the progress bar. |
| Font color | The font color of the value in the progress bar. |
| Default Color | The default color of the progress bar. |
| Color Display Mode | The display mode of the progress bar. |
| Start Color | The start color of the progress bar. This parameter is available if you select Gradient for Color Display Mode. |
| End Color | The end color of the progress bar. This parameter is available if you select Gradient for Color Display Mode. |
| Display Color | The display color of the progress bar. This parameter is available if you select Display by Rule for Color Display Mode. Not e The value of Act ual Value is compared with the value of T hreshold based on the condition specified by Operat or. If the actual value matches the condition specified by Operat or, the progress bar is displayed in the color specified by Display Color. If the actual value does not match the condition, the progress bar is displayed in the default color. |
| Operator | The condition that is used to determine whether to display the progress bar in the color specified by Display Color. This parameter is available if you select Display by Rule for Color Display Mode. |
| Threshold | The threshold based on which the color of the progress bar is determined. This parameter is available if you select Display by Rule for Color Display Mode. |

Example To calculate the ratio of the page views (PVs) of the current hour to the PVs of the same period of time on the previous day, execute the following query statement:

```
* | SELECT diff[1] AS today, diff[2] AS yesterday, diff[3] AS ratio FROM (SELECT compare(PV,86400) AS
diff FROM (SELECT count(*) AS PV FROM log))
```

##### 4.11.1.10 Display query results on a map

This topic describes how to configure a map to display query results. Background information You can color and mark a map to display geographic data. Log Service provides the map of China. The display modes of an AMap include the anchor point and heat map. You can use specific functions in query statements to display analysis results as maps. Each map consists of the following elements: Map canvas Colored area
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyt ics.
5. On the Graph tab, use the map of China, click the
icon..
6. On the Propert ies tab, configure the properties of the map.
In this example, the map of China is selected.

| Parameter | Description |
|---|---|
| Provinces | The location information that is recorded in logs. The information is displayed in one of the following dimensions based on the map type: |
| Value Column | The amount of data at the location. |
| Show Legend | If you turn on Show Legend, the legend information is displayed. |

Example of a map of China To display query results on a map of China, you can execute the following query statement in which the ip_to_province function is used:

```
* | select ip_to_province(remote_addr) as address, count(1) as count group by address order by count d
esc limit 10
```

Select address for Provinces and count for Value Column.

##### 4.11.1.11 Display query results on a flow chart

This topic describes how to configure a flow chart to display query results. Background information A flow chart, also known as ThemeRiver, is a stacked area chart around a central axis. The banded branches with different colors indicate different categorical data. The width of the band indicates the numeric value. By default, the time information of the data is mapped to the X-axis. A flow chart can display the data in three dimensions. You can select Line Chart or Column Chart for the Chart Types parameter. If you select Column Chart, a stacked column chart is displayed. In a stacked column chart, each category of data starts from the top of the last column of categorical data.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the flow chart.

| Parameter | Description |
|---|---|
| Chart Types | The type of the chart. Valid values: Line Chart, Area Chart, and Column Chart. Default value: Line Chart. |
| X Axis | The sequential data. In most cases, a time series is selected. |
| Y Axis | The numeric data. You can select one or more fields for the Y-axis. |
| Aggregate Column | The field information that must be aggregated as the third point for comparison. |
| Legend | The position of the legend in the chart. Valid values: Top, Bottom, Left, and Right. |
| Format | The format in which data is displayed. |
| Margin | The distance between the axis and the borders of the chart. The parameters include T op Margin, Bot t om Margin, Right Margin, and Lef t Margin. |

Example A flow chart is suitable for displaying data in three dimensions, for example, time, category, and numeric value. In this example, the following query statement is executed:

```
* | select date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as minute, count(1) as c,
request_method group by minute, request_method order by minute asc limit 100000
```

Select minut e for X Axis, c for Y Axis, and request _met hod for Aggregate Column. Flow chart

##### 4.11.1.12 Display query results in a Sankey diagram

This topic describes how to configure a Sankey diagram to display query results. Background information A Sankey diagram is a type of flow chart. A Sankey diagram shows the flow from one set of values to another set of values. You can use Sankey diagrams to collect statistics about network traffic flows. A Sankey diagram

| target |   |
|---|---|
| value | f |

| source |   | and | target |   |
|---|---|---|---|---|
| rom the | source |   |   | node t |

contains the values of the `source` , `target` , and `value` fields. The `source` and `target` fields describe the source and target nodes, and the `value` field describes the flows from the `source` node to the `target` node. Each Sankey diagram consists of the following elements: Node Edge A Sankey diagram has the following features: The start flow is equal to the end flow. The sum of the widths of all main edges is equal to the sum of the widths of all branch edges. This allows you to manage and maintain a balanced flow of all traffic. The edge width in a row represents the volume of traffic in a specific status. The width of an edge between two nodes represents the flow volume in a status. The following table describes the data that can be displayed in a Sankey diagram.

| source | target | value |
|---|---|---|
| node1 | node2 | 14 |
| node1 | node3 | 12 |
| node3 | node4 | 5 |

The following figure shows the data relationships in a Sankey diagram.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the Sankey diagram.

| Parameter | Description |
|---|---|
| Start Column | The start node. |
| End Column | The end node. |
| Value Column | The volume of traffic between the start node and end node. |
| Margin | The distance between an axis and the borders of the chart. The parameters include T op Margin, Bot t om Margin, Right Margin, and Lef t Margin. |

Example

| g contains the | source |
|---|---|
| steamValue | values. |

If a log contains the `source` , `target` , and `value` fields, you can use a nested subquery to obtain the sum

```
* | select sourceValue, targetValue, sum(streamValue) as streamValue from (select sourceValue, targetV
alue,
 streamValue, __time__ from log group by  sourceValue, targetValue, streamValue, __time__ order by __t
ime__ desc) group by sourceValue,
 targetValue
```

##### 4.11.1.13 Display query results on a word cloud

This topic describes how to configure a word cloud to display query results. Background information A word cloud shows text data. A word cloud is a cloud-like and colored image composed of words. You can use a word cloud to display a large amount of text data. The font size or color of a word indicates the significance of the word. This allows you to identify whether a word is significant in an efficient manner. The words in a word cloud are sorted.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the word cloud.

| Parameter | Description |
|---|---|
| Word Column | The words that you want to display. |
| Value Column | The numeric value that corresponds to a word. |
| Font Size | The font size of a word. The minimum font size ranges from 10 pixels to 24 pixels. The maximum font size ranges from 50 pixels to 80 pixels. |

Example To query the distribution of hostnames in NGINX logs, execute the following query statement:

```
* | select hostname, count(1) as count group by hostname order by count desc limit 1000
```

Select `hostname` for Word Column and `count` for Value Column.

##### 4.11.1.14 Display query results on a treemap chart

This topic describes how to configure a treemap chart to display query results. Background information A treemap chart consists of multiple rectangles that represent the data volumes. A larger rectangle area represents a larger proportion of the categorical data.
1. Log on to the Log Service console.
2. In the Projects section, click the project in which you want to configure a chart.
3. Click the name of the Logstore in which you want to configure a chart.
4. Enter a query statement in the search box, specify a time range, and then click Search & Analyze.
5. On the Graph tab, click the
icon.
6. On the Propert ies tab, configure the properties of the treemap chart.

| Parameter | Description |
|---|---|
| Legend Filt er | The field that includes categorical data. |
| Value Column | The numeric value of a field. A greater field value represents a larger rectangle. |

Example To query the distribution of hostnames in NGINX logs, execute the following query statement:

```
* | select host, count(1) as count group by host order by count desc limit 1000
```

Select `host` for Legend Filt er and select `count` for Value Column.

#### 4.11.2 Dashboard

##### 4.11.2.1 Overview

A dashboard provided by Log Service is a platform where you can analyze data in real time. You can add multiple charts to a dashboard for data analysis. Each chart is a visualized search and analytic statement. A dashboard allows you to view the charts of multiple search and analytic statements at one time. When you open or refresh the dashboard, the statements of the charts run automatically. After you add a chart to a dashboard, you can configure Drill-down analysis for the chart. Then you can click the chart on the dashboard to further analyze data and obtain more fine-grained analysis results. You can create a maximum of 50 dashboards for a project. Each dashboard can contain a maximum of 50 analysis charts. Features A dashboard has two modes: display mode and edit mode. In the display mode, you can configure multiple display settings on the dashboard page. Dashboard: You can specify the time range, the automatic refresh interval, full screen, and the display mode of the title for the dashboard, configure alerts for all charts on the dashboard, and filter chart data based on the Configure and use a filter on a dashboard of a Logstore. Chart: You can view the analysis details of a specified chart, specify the time range and configure alerts for the chart, download logs and the chart, and check whether drill-down analysis is configured for the chart. In the edit mode, you can change the configurations of the dashboard and charts. Dashboard: You can use a dashboard as a canvas and add Markdown chart, custom charts, text, icons, and other chart elements to the dashboard. You can also add lines between chart elements that are self-adaptive to the positions of the charts. You can also add Configure and use a filter on a dashboard of a Logstore, which can be used to filter chart data in the display mode. In addition, you can configure display gridlines to help arrange chart elements such as icons in an orderly manner. Chart: You can also edit a chart on the dashboard. You can modify the statement, properties, and interactive behavior such as drill-down analysis of the chart.

##### 4.11.2.2 Create and delete a dashboard

This topic describes how to create and delete a dashboard in a Logstore. In the Log Service console, you can run a query statement and visualize the query result in a chart. After you complete the configurations of the chart, you can add the chart to a dashboard. Each dashboard can display up to 50 charts, which support multiple formats and custom settings. Prerequisites The indexing feature of the Logstore is enabled and configured. For more information, see Enable the index feature and configure indexes for a Logstore. Create a dashboard
1. Log on to the Log Service console.
2. Click a project name.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis.
4. Enter a query statement in the search box, and then click Search & Analyze.
5. On the Graph tab that appears, configure the chart properties on the Propert ies tab.
6. (Optional)Set a placeholder variable.
For example, you have configured a drill-down event for another chart. This drill-down event redirects you to the current dashboard. You have also specified a placeholder variable for the query statement of the preceding chart. When you click a chart value to trigger the drill-down event, you are redirected to the current dashboard. The placeholder variable is replaced by the chart value and the current dashboard is refreshed by the new query statement. For more information, see Drill-down analysis. i. Click the Dat a Source tab, and then select a part of the query statement in the Query field. ii. Click Generat e Variable to generate a placeholder variable. iii. Set the parameters in the Variable Conf ig section.

| Parameter | Description |
|---|---|
| Variable Name | The name of the placeholder variable. If the name of the placeholder variable is the same as the variable specified in the chart, the placeholder variable is replaced with the chart value when the drill-down event is triggered. |
| Def ault Value | The default value of the placeholder variable in the current dashboard. |
| Mat ching mode | You can select Global Match or Exact Match. |
| Result | The query statement that contains the specified variable. |

7. Configure a drill-down event.
After you configure a drill-down event, you can click the chart on the dashboard for a more detailed analysis. For example, you can be redirected to another dashboard or a saved search. For more information, see Drilldown analysis. i. Click the Int eract ive Behavior tab. ii. Select an Event Act ion. iii. Set the parameters of the selected event action.
8. Click Add t o New Dashboard and specify the dashboard name and chart name.

| Parameter | Description |
|---|---|
| Operat ion | Add t o Exist ing Dashboard: Add the chart to an existing dashboard. Creat e Dashboard: Create a dashboard and then add the chart to the dashboard. |
| Dashboards | Select an existing dashboard name. Not e This parameter is required only when you set the Operat ion parameter to Add t o Exist ing Dashboard. |
| Dashboard Name | Enter a dashboard name. Not e This parameter is required only when you set the Operat ion parameter to Creat e Dashboard. |
| Chart Name | Enter a name for the current chart. The chart name is displayed as the chart title in the dashboard. |

9. Click OK.
You can add multiple charts to a dashboard. Delete a dashboard You can delete a dashboard if you no longer need it. However, you cannot recover a deleted dashboard.
1. Log on to the Log Service console, and then click the destination project name.
2. In the left-side navigation pane, click the Dashboard icon.
3. Click the
icon next to the dashboard that you want to delete, and then select Delet e.

##### 4.11.2.3 Configure the display mode of a dashboard

This topic describes how to configure the display mode of a dashboard. By default, you can view all charts in a dashboard in the display mode. When you configure the display mode, you can add chart elements, enable automatic refresh, and set the title display mode. Set a query time range for a dashboard of a Logstore By default, all charts in a dashboard use the query time range that is set for the dashboard. For more information about how to set a query time range for a single chart, see Set a query time range for a chart.

> Not e On the dashboard page, you can click T ime Range to specify a time range for a query. The specified query time range is used only for the current query. The next time you open the dashboard, the system will display the analysis results in the default query time range.

1. Log on to the Log Service console.
2. Click a project name.
3. In the left-side navigation pane, click the Dashboard icon.
4. Click the
icon next to the dashboard, and then select Det ails from the drop-down list.
5. Click T ime Range to set a time range.
You can set one of the following time ranges: Relative: queries log data obtained in a time range of 1 minute, 5 minutes, 15 minutes, or other time ranges that end with the current time, accurate to the second. For example, if the current time is 19:20:31 and you select 1Hour as the relative time, the charts on the dashboard display the analysis results of the log data queried from 18:20:31 to 19:20:31. Time Frame: If you select or customize a time range less than one hour (for example, 1 minute, 5 minutes, and 15 minutes), log data obtained in the time range that ends with the current time is queried, accurate to the minute. If you select or customize a time range greater than one hour, log data obtained on the hour before the current time is queried. For example, if the current time is 19:20:31 and you select 1Hour as the time frame, the charts on the dashboard display the analysis results of the log data queried from 18:00:00 to 19:00:00. Custom: queries log data obtained in a specified time range.
6. Move the pointer over the T ime Range button to confirm the specified time range.
Switch to the edit mode Click Edit to switch to the edit mode of the dashboard. In the edit mode, you can add Markdown chart, custom charts, text, icons, and other chart elements to the dashboard. For more information, see Edit mode. Set alerts On the dashboard page, choose Alert s > Creat e to create an alert. Choose Alert s > Modif y to modify an alert. An alert must be associated with one or more charts. For more information, see Configure an alert rule. Set a refresh method You can manually refresh the dashboard, or set an automatic refresh interval for the dashboard. To manually refresh the dashboard, choose Ref resh > Once. To set an automatic refresh interval for the dashboard, choose Ref resh > Aut o Ref resh, and then select an interval. The Aut o Ref resh interval can be 15 seconds, 60 seconds, 5 minutes, or 15 minutes.

> Not e If your browser is inactive, the automatic refresh interval may be inaccurate.

Share a dashboard To share a dashboard with authorized users, click Share to copy the link of the dashboard page and then send the link to the users. The shared dashboard page uses the settings of the dashboard at the time of sharing. The settings include the time range of charts and chart title format.

> Not e Before you share the dashboard with other users, you must grant relevant permissions to them.

Display a dashboard in full screen Click Full Screen. Then the charts on a dashboard are displayed in full screen. Set the chart title format On the dashboard page, click T it le Conf igurat ion. Available title formats include: Single-line Title and Time Display Title Only Time Only Reset the query time range To restore the default query time ranges of all charts on the dashboard, click Reset T ime. Select chart view View analysis details of a chart To view analysis details of a chart, move the pointer over the More icon in the upper-right corner of the chart, and then select View Analysis Det ails. The corresponding Search & Analysis page appears, showing the query statement and property settings. Set the query time range for a chart To set the query time range for a chart, move the pointer over the More icon in the upper-right corner of the chart, and then select Select T ime Range. The settings are valid only for the current chart. Set an alert for a chart To set an alert for a chart, move the pointer over the More icon in the upper-right corner of the chart, and then select Creat e Alert . For more information, see Configure an alert rule. Download log analysis results of a chart To download analysis results of a chart, move the pointer over the More icon in the upper-right corner of the chart, and then select Download Log. Download a chart To download a chart, move the pointer over the More icon in the upper-right corner of the chart, and then select Download Chart . Check whether a drill-down event is configured for a chart To check whether a drill-down event is configured for a chart, move the pointer over the More icon in the upperright corner of the chart. Then, check the color of the hand icon at the bottom of the shortcut menu. If the icon is red, a drill-down event is configured for the chart. If the icon is gray, no drill-down event is configured for the chart.

> Not e Different charts in a dashboard have different shortcut menus. For example, you cannot use the shortcut menu of a custom chart or Markdown chart to view analysis details because they are not analysis charts.

##### 4.11.2.4 Edit mode

You can click the Edit button on the dashboard page to enter the edit mode. Then you can change the configurations of the dashboard and charts on the dashboard. Dashboard: You can modify the dashboard name in the upper-left corner of the page. You can use a dashboard as a canvas and add Markdown chart, custom charts, text, icons, and other chart elements to the dashboard. You can add lines between chart elements. The lines are adaptive to the positions of the charts. You can add a filter to the dashboard. Then you can filter chart data in the display mode. For more information, see Configure and use a filter on a dashboard of a Logstore. In addition, you can configure display grid lines to arrange chart elements such as icons in order. You can use the menu bar to manage the chart property settings on the dashboard. For example, you can perform the add, delete, and cancel operations on a chart. You can also configure the size and location of a chart and move a chart to the top or bottom of the dashboard. Chart: You can edit a chart on the dashboard. For example, you can modify the statement, properties, and interactive behavior such as drill-down analysis of a chart.

> Not e All changes to the dashboard take effect only after you click Save in the upper-right corner of the page.

Chart elements In the edit mode of a dashboard, you can add the following chart elements: Common icons Log Service allows you to display common icons on a dashboard page. You can drag an icon from the menu bar and drop the icon to a specified position. Text You can drag the text icon from the menu bar and drop the icon to a specified position. Double-click the text box to modify the text. You can add a Markdown chart to a dashboard and edit the chart with the Markdown syntax. Drag the Markdown icon from the menu bar and drop the icon to a specified position. Select Edit from the More icon. Then you can set the Markdown content. Filter You can add a filter to a dashboard. Then you can add search conditions or replace placeholder variables in query statements. Click the filter icon in the dashboard menu bar. On the page that appears, configure the filter based on your needs. By default, the filter is in the upper-left corner of the dashboard page. To modify the settings of a filter, you can select Edit on the More icon in the upper-right corner of the page. Customize SVG You can upload a Scalable Vector Graphics (SVG) file to a dashboard. Click the SVG icon in the menu bar. On the page that appears, click the box or drag an SVG file to the box to upload the file.

> Not e The size of an SVG file cannot exceed 10 KB.

Customize image's HTTP link You can upload the HTTP link of an image to a dashboard. Click the Customize image's HTTP link icon in the menu bar. On the page that appears, enter the HTTP link of an image and click OK. Layout In the edit mode, all charts and chart elements are placed on a canvas. You can drag and scale each chart, except for the lines. The horizontal width of a chart is up to 1,000 units. Each unit is equal to `current browser` `width/1,000` . The vertical height is unlimited and each unit is equal to 1 pixel. Before you arrange a chart on the dashboard, you can click Display gridlines to better arrange the position of the chart and the spacing between charts. You can perform the following operations to arrange a chart on the dashboard: Adjust the position of a chart You can drag a chart and drop the chart to a specified position. After you specify a chart, you can click L and T to adjust the chart position. Adjust the width and height of a chart After you specify a chart, you can drag the chart in the lower-right corner to resize the chart. After you specify a chart, you can also specify the W and H parameters to resize the chart. Add lines to connect charts You can add a directional line between two charts. When you adjust the position and size of the charts, the line automatically moves to display the relative position between the two charts. After you select a chart, four squares appear on the border of the chart. These squares indicate the starting point of the connection line. Press and hold one square, and the area where the end point of the connection line is automatically displayed. Move the pointer to this position to connect the two charts. You can move a chart to the top or bottom of the dashboard. After you select a chart, you can use the menu bar to move the chart to the top or bottom. Chart configurations In the edit mode of a dashboard, you can perform the following operations on chart elements: Edit: modifies the query statement, properties, and interactive behavior such as drill-down analysis of a chart. i. In the upper-right corner of the dashboard page, click Edit . ii. Find the target chart and choose
> Edit .

iii. Modify the query statement of the chart, Propert ies, Dat a Source, or Int eract ive Behavior. iv. Click Preview, and then click OK. v. In the upper-right corner of the dashboard page, click Save. Copy: creates a copy of the specified chart and retains all configurations. i. In the upper-right corner of the dashboard page, click Edit . ii. Find the target chart and choose
> Copy.

iii. Drag the chart copy and drop it to a specified position, and then set the top margin, left margin, and size of the copy. iv. In the upper-right corner of the dashboard page, click Save. Delete: deletes the specified chart from the dashboard. i. In the upper-right corner of the dashboard page, click Edit . ii. Find the target chart and choose
> Delet e.

iii. In the upper-right corner of the dashboard page, click Save.

##### 4.11.2.5 Drill-down analysis

This topic describes how to configure drill-down analysis for a chart of a Logstore. When you add a chart to a dashboard, you can modify the configurations in the drill-down list to obtain deeper data analysis results. Prerequisites The index feature of the Logstore is enabled and configured. For more information, see Enable the index feature and configure indexes for a Logstore. A saved search, a dashboard, and a custom link to which you want to be redirected are configured. A placeholder variable is specified in the saved search or the query statement of a chart added to a dashboard to which you are redirected if you want to add a variable. For more information, see Saved search and Create and delete a dashboard. Context Drilling is essential for data analysis. This feature allows you to analyze data in a fine-grained or coarse-grained way. This feature includes drill-up and drill-down analysis. You can implement drill-down analysis to gain a deeper insight into data and make a better decision. Log Service supports drill-down analysis of the following charts: tables, line charts, column charts, bar charts, pie charts, individual value plots, area charts, and treemap charts.
1. Log on to the Log Service console.
2. Click the target project name.
3. Click the
icon next to the name of the Logstore, and then select Search & Analysis from the drop-down list.
4. Enter a query statement in the search box, set a time range, and then click Search & Analyze.
5. On the Graph tab that appears, select a chart t ype, and then configure the parameters on the Propert ies
tab of the chart.
6. Click the Int eract ive Behavior tab. On this tab, configure the Event Act ion for drill-down analysis.
Disable: disables drill-down analysis. Open Logst ore: sets the drill-down event to open a Logstore. If you configure a filter statement on the Interactive Behavior tab, the filter statement automatically fills the Search & Analyze search box of the redirected Logstore page when you click a value on the chart.

| Parameter | Description |
|---|---|
| Select Logst ore | The name of the Logstore to which you want to be redirected. |
| Open in New T ab | If you turn on this switch, the specified Logstore is opened on a new tab when the interactive behavior is triggered. |
| T ime Range | The query time range of the Logstore to which you are redirected. Valid values: Def ault : The default time range (15 minutes, accurate to the second) is used for a query statement of the redirected Logstore. Inherit t able t ime: The time range that a statement queries in the redirected Logstore is the time range specified for the chart when the event is triggered. Relative: The time range that a statement queries in the redirected Logstore is accurate to the second. Time Frame: The time range that a statement queries in the redirected Logstore is accurate to the minute, hour, or day. Default value: Def ault . |
| Inherit Filt ering Condit ions | If you turn on the Inherit Filt ering Condit ions switch, the filtering conditions added to the dashboard are synchronized to a query statement of the specified Logstore. The filtering conditions are added before the query statement by using the logical AND operator. |
| Filt er | Enter a Filt er St at ement on the Filt er tab. The filter statement can contain the Opt ional Paramet er Fields. If you configure a filter statement on the Filt er tab, the f ilt er st at ement automatically fills the Search & Analyze search box of the redirected Logstore page when you click a chart value on the dashboard. |

Open Saved Search: sets the drill-down event to execute a saved search. You can configure variables and a filter statement for a chart at the same time. When you click a value on the chart: If you configure a variable for the chart, the variable value that you click replaces the placeholder variable that you have configured for the saved search and the saved search is executed for drill-down analysis. If you configure a filter statement, the filter statement is added to the saved search to which you are redirected.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Select Saved Search | The name of the saved search to which you want to be redirected. For more information about how to configure a saved search, see Saved search. |
| Open in New T ab | If you turn on this switch, the specified saved search is opened on a new tab when the interactive behavior is triggered. |
| T ime Range | The time range of the saved search to which you want to be redirected. Valid values: Def ault : The default time range (15 minutes, accurate to the second) is used for the saved search to which you are redirected. Inherit t able t ime: The time range of the saved search is the query time range of the chart that you configure on the dashboard. Relative: The time range of the saved search is accurate to the second. Time Frame: The time range of the saved search is accurate to the minute, hour, or day. Default value: Def ault . |
| Inherit Filt ering Condit ions | If you turn on the Inherit Filt ering Condit ions switch, the filtering conditions added on the dashboard are synchronized to the saved search of the specified Logstore. The filtering conditions are added before the saved search by using the logical AND operator. |
| Filt er | Click the Filt er tab, and then enter a Filt er St at ement . The filter statement can contain the Opt ional Paramet er Fields. If you configure a filter statement on the Filt er tab, the Filt er St at ement is added to the saved search when you click a chart value on the dashboard. |
| Variable | Click the Variable tab, click Add Variable, and then set the following parameters: Replace Variable Name: the variable that triggers the drill-down event. When you click this variable, you are redirected to the specified saved search. Replace t he value in t he column: the column where the value that you want to replace data with is located. To process multiple columns, you can specify the current column and other columns. The current column is the column on which you want to perform drill-down analysis. Specify the current column in the Replace t he value in t he column field. Other columns can be the fields in the chart for which you configure drill-down analysis. If the variable name of the saved search is the same as the added variable, the variable of the saved search is replaced with the chart value that triggers the drill- down event. This helps you use the saved search for analysis in an efficient way. Not e If you add a variable for drill-down analysis, you must first configure a placeholder variable for the saved search to which you want to be redirected. You can add up to five placeholder variables for a saved search. |

Open Dashboard: sets the drill-down event to open a dashboard. Analysis charts on a dashboard are visualized query results. When you click a chart value on the source dashboard: If you configure a variable for the chart and set a placeholder variable for the chart on the destination dashboard to which you want to be redirected, the placeholder variable is replaced with the chart value that you click. If you configure a filter statement, the filter statement is added to the query statement of the chart on the destination dashboard.

| Parameter | Description |
|---|---|
| Select Dashboard | The name of the dashboard to which you want to be redirected. For more information, see Create and delete a dashboard. |
| Open in New T ab | If you turn on this switch, the specified dashboard is opened on a new tab when interactive behavior is triggered. |
| T ime Range | Set the time range for the dashboard to which you want to be redirected. Valid values: Def ault : After you are redirected to the dashboard by clicking a chart value on the current dashboard, the selected dashboard uses its original time range. Inherit t able t ime: After you are redirected to the selected dashboard, the time range of the chart on the selected dashboard is the time range of the chart specified on the source dashboard when the event is triggered. Relative: After you are redirected to the selected dashboard, set the time range of the selected dashboard to the specified relative time. Time Frame: After you are redirected to the selected dashboard set the time range of the selected dashboard to the specified time frame. Default value: Def ault . |
| Inherit Filt ering Condit ions | If you turn on the Inherit Filt ering Condit ions switch, the filtering conditions added on the current dashboard are synchronized to the dashboard to which you are redirected. The filtering conditions are added before the query statement by using the logical AND operator. |
| Filt er | Click the Filt er tab, and then enter a Filt er St at ement . The filter statement can contain the Opt ional Paramet er Fields. If you have set the Filt er, a filtering condition is added to the selected dashboard when you click a chart value on the current dashboard. The filtering condition is the specified Filt er St at ement . |

| Parameter | Description |
|---|---|
| Variable | Click the Variable tab, click Add Variable, and then set the following parameters: Replace Variable Name: the variable that triggers drill-down analysis. When you click this variable, you are redirected to the selected dashboard. Replace t he value in t he column: the column where the value that you want to replace data with is located. To process multiple columns, you can specify the Def ault Column and other columns. The Def ault Column is the current column on which you want to perform drill-down analysis. Other columns can be fields in the chart for which you configure drill-down analysis. If the variable in the query statement of the chart on the selected dashboard is the same as the added variable, the variable is replaced with the chart value that triggers the drill-down event. This changes the query statement of the chart on the selected dashboard. Not e If you add a variable for drill-down analysis, you must first configure a placeholder in the query statement for the selected dashboard to which you want to be redirected. You can add up to five variables. |

Cust om HT T P Link: sets the drill-down event to open a custom HTTP link. The path in the HTTP link is the path of the destination file in the server. When you add optional parameter fields to the path and click the chart value on the dashboard, the added parameter fields are replaced with the chart value. At the same time, you are redirected to the new HTTP link.

| Parameter | Description |
|---|---|
| Ent er Link | The destination address to which you want to be redirected. |
| Opt ional Paramet er Fields | By clicking an optional parameter variable, you can replace a part of the HTTP link with the chart value that triggers a drill-down event. |

7. Click Add t o New Dashboard and set the dashboard name and chart name.
Example You want to store collected NGINX access logs in a Logstore named accesslog, display the relevant analysis results on a dashboard named RequestMethod, and display the page view (PV) changes over time on a dashboard named destination_drilldown. You can configure drill-down analysis for the table of request methods, add the table to the RequestMethod dashboard, and then configure the drill-down event that redirects you to the destination_drilldown dashboard. When you click a request method on the table on the RequestMethod dashboard, you are redirected to the destination_drilldown dashboard. Then you can view the PV changes on the dashboard.
1. Set the dashboard to which you want to be redirected.
i. Filter log data by request method and analyze how the PV of each request method changes over time. The query statement is shown as follows:

```
request_method: * | SELECT date_format(date_trunc('minute', __time__), '%H:%i:%s') AS time, CO UNT(1) AS PV GROUP BY time ORDER BY time
```

ii. Use a line chart to display the query result and add the line chart to the dashboard named destination_drilldown. Before you add the line chart to the dashboard, specify the asterisk ( `*` ) to generate a placeholder variable and set the variable name to method. If the variable name of another chart for which you configure drill-down analysis is method, when you click the variable value on the chart to trigger drilldown analysis, the asterisk ( `*` ) is replaced with the value that you click and the query statement of the line chart is performed.
2. Configure drill-down analysis for a chart and add the chart to the dashboard.
i. On the Search & Analysis page, enter a SQL statement to query the number of NGINX access log entries of each request method, and display the result in a table. The query statement is shown as follows:

```
*|SELECT request_method, COUNT(1) AS c GROUP BY request_method ORDER BY c DESC LIMIT 10
```

ii. Configure drill-down analysis for the `request_method` column in the table. iii. Click the GET request on the RequestMethod dashboard. iv. Redirected to the destination_drilldown dashboard. You are redirected to the dashboard configured in step . The asterisk ( `*` ) in the query statement is replaced with `GET` . The dashboard shows how the PV of the GET request changes over time.

##### 4.11.2.6 Configure and use a filter on a dashboard of a Logstore

Logstore This topic describes how to configure and use a filter on a dashboard of a Logstore. Filters help you refine search results or replace placeholder variables with specified values. Prerequisites The index feature of the Logstore is enabled and configured. For more information, see Enable the index feature and configure indexes for a Logstore. A dashboard is created. For more information, see Create and delete a dashboard. A placeholder variable is specified for charts on the dashboard if the filter type is set to Replace Variable. Context Each chart on a dashboard is a visualized query statement. When you configure a filter on a dashboard, the specified filtering condition or variables apply to all charts on the dashboard. You can configure the following two types of filters: Filter: Add key-value pairs as a filtering condition before the query statement `[search query]` . The new query statement is `key:value AND [search query]` , which means to search the result of the original query statement for log entries that contain `key:value` . For the Filt er type, you can select or enter multiple keyvalue pairs. When you select multiple key-value pairs as filtering conditions, the logical `OR` operator is used between the pairs. Replace Variable: Specify a variable. If the dashboard contains a chart configured with the same placeholder variable, the placeholder variable in the query statement of the chart is replaced with the selected value. Components Each filter chart has one or more filters. Each filter consists of the following two components: The key, which indicates a filter operation. The values of the key.
1. Log on to the Log Service console.
2. Click a project name.
3. In the left-side navigation pane, click the Dashboard icon.
4. In the dashboard list, click the name of the target dashboard.
5. On the dashboard page, click Edit to enter the edit mode.
6. Click the
icon, and then set the filter parameters. Click OK. Parameters of a filter

| Parameter | Description |
|---|---|
| Filt er Name | The name of the filter. |
| Display Set t ings | Valid values: Title: specifies to add a title for a filter. You can turn on the Title switch to add a title for a filter. Border: specifies to add borders for a filter. You can turn on the Border switch to add borders for a filter. Background: specifies to add a white background for a filter. You can turn on the Background switch to add a white background for a filter. |
| T ype | The filter type. Valid values: If you select Filt er, a List Item is a value of a key that is used to filter the results of a query statement. You can set multiple values for a key. After the filter takes effect, you can select one or more values on the dashboard to filter query results based on your needs. If you select Replace Variable, a List Item is the value that replaces a specified variable. You can set multiple values for a variable. After the filter takes effect, you can select one or more values on the dashboard to filter query results based on your needs. |
| Key | For the Filt er type, the Key parameter specifies the key in the filtering condition. For the Replace Variable type, the Key parameter specifies the variable. Not e The variable must be the same as the placeholder variable that you specified for charts. Otherwise, the placeholder variable cannot be replaced. |
| Alias | The alias of the key. This parameter is available only when you select Filt er. After you set an alias for a key, the alias is displayed in the filter on the dashboard. |
| Global f ilt er | This switch indicates whether to filter the specified values in all fields. This switch is turned off by default. The switch is available only when you select the Filt er type. To filter the specified values in all fields, turn on the Global f ilt er switch. To filter the specified values in specified keys, turn off the Global f ilt er switch. |
| St at ic List It ems | The values of the key that is used as a filtering condition. Click the plus sign and enter a value for the key in the text box. |

| Parameter | Description |
|---|---|
| Add Dynamic List It em | The dynamic value of the key retrieved by running the specified query statement. Turn on the Add Dynamic List It em switch, select a Logstore, and turn on the Inherit Filtering Conditions switch (specifies whether to include the filtering condition in the query statement). Enter a query statement in the search box, specify a time range, and then click Search to preview the dynamic values. |

Examples You can use a filter to modify the query statements of charts on a dashboard and replace placeholder variables in the charts on the dashboard. Each chart represents a query statement in the format of [search query] | [sql `query]` . The filter query is appended to the original query statement to filter data. If the filter type is Filter, the key-value pairs to be filtered are added before `[search query]` to form a new query statement by using the logical `AND` operator. The new query statement is `key:value AND [search que` `ry]` . If the filter type is Replace Variable, the filter queries all charts that contain the specified placeholder variables on the dashboard and replaces the placeholder variables with the selected `values` . Example 1: Use different time granularities to analyze logs After you collect NGINX access logs, you need to query and analyze these logs in real time. You can use a query statement to view the number of page views (PVs) per minute. However, if you want to view the number of PVs per second, you must modify the value of __time__ - __time__ % 60 in the query statement. To simplify this operation, you can use a filter to replace variables in the query statement.
1. Use the following query statement to view the number of PVs per minute:

```
* | SELECT date_format(__time__ - __time__ % 60, '%H:%i:%s') as time, count(1) as count GROUP BY t
ime ORDER BY time
```

2. Add the chart to a dashboard, and select `60` generate a variable with the name `interval` .
3. Add a filter on the dashboard page.
T ype: Select Replace Variable. Key: Enter `interval` . St at ic List It ems: Add `1` and `120` as values of the key. The default unit is seconds.
4. In the Filter section of the dashboard, select `1` from the Interval drop-down list to view statistics by
second. The following statement shows the query statement after the placeholder variable is replaced:

```
* | SELECT date_format(__time__ - __time__ % 1, '%H:%i:%s') as time, count(1) as count GROUP BY ti
me ORDER BY time
```

Example 2: Switch between request methods You can add dynamic values to a filter to dynamically switch between request methods. In example 1, the query statement starts with an asterisk ( `*` ), which means no condition is set to filter the query results and all logs are queried. You can add another filter to view the PV data of different request `methods` .
1. Add a filter on the dashboard and turn on the Add Dynamic List It em switch.
Set the parameters as follows: T ype: Select Filter. Key: Enter `method` . Select Logst ore: Select the Logstore to which the dashboard belongs. Add Dynamic List It em: Enter a query statement to obtain the relevant dynamic values, and then click OK.

| , select POST |   |
|---|---|
| POST | is displ |

follows:

```
(*) and (method: POST) | SELECT date_format(__time__ - __time__ % 60, '%H:%i:%s') as time, count(1 ) as count GROUP BY time ORDER BY time
```

##### 4.11.2.7 Markdown chart

Log Service allows you to add a Markdown chart to a dashboard. In the Markdown chart, you can insert images, links, videos, and other elements to make your dashboard page more intuitive. Context You can create different Markdown charts based on your business needs. Markdown charts can make a dashboard more informative. You can insert text such as background information, chart description, notes, extension information, and custom images in a Markdown chart. You can also insert saved searches or dashboard links of other projects to redirect to other query pages. Scenarios You can insert links in a Markdown chart to redirect to other dashboard pages of the current project. You can also insert an image corresponding to each link for better recognition. In addition, you can use a Markdown chart to describe parameters of analysis charts.
1. Log on to the Log Service console.
2. Click the destination project name.
3. In the left-side navigation pane, click the Dashboard icon.
4. In the dashboard list, click the name of the destination dashboard.
5. In the upper-right corner of the dashboard page, click Edit to enter the edit mode.
6. In edit mode, drag the Markdown icon
from the menu bar to the specified location to create a Markdown chart.
7. Click the created Markdown chart, find the More icon in the upper-right corner of the chart, and click edit .

| Parameter | Description |
|---|---|
| Chart Name | The name of the Markdown chart. |
| Show Border | Specifies whether to show the borders of a Markdown chart. You can turn on the Show Border switch to show the borders of a Markdown chart. |

| Log S | ervice | User Guide·Query and analysi | s |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Show Title | Specifies whether to show the title of a Markdown chart. You can turn on the Show T it le switch to show the title of a Markdown chart. |
| Show Background | Specifies whether to show the background of a Markdown chart. You can turn on the Show Background switch to show the background of a Markdown chart. |
| Query Binding | Specifies whether to bind a query statement to a Markdown chart. You can turn on the Query Binding switch and bind a query statement to a Markdown chart. Then, query results are dynamically displayed in the Markdown chart. |

8. (Optional)Bind a query statement.
i. Select the destination Logstore and enter a query statement in the search box. A query statement consists of a search statement and an analytic statement in the format of search statement|analytic s

```
tatement .
```

ii. On the Search & Analysis page, click 15 Minut es(Relat ive) to set the time range for the query. iii. Click Search to display the first values of the returned query result. iv. Click the plus sign next to a field to insert the corresponding query result to Markdown Cont ent .
9. Edit Markdown Cont ent .
Enter Markdown content in the Markdown cont ent column. Then, data preview is displayed in real time in the Show Chart column on the right. You can modify the Markdown content based on the data preview. Modify a Markdown chart Modify the location and size of a Markdown chart i. Click Edit in the upper-right corner of the Dashboard page. ii. Drag the Markdown icon to the specified location on the dashboard and drag the lower-right corner of the chart to adjust its size. iii. Click Save in the upper-right corner of the dashboard page to save the modification. Modify the title of a Markdown chart i. Click Edit in the upper-right corner of the Dashboard page. ii. Click the specified Markdown chart, find the More icon in the upper-right corner of the chart, and click Edit . iii. Enter a new title in the Chart name field and then click OK. iv. Click Save in the upper-right corner of the dashboard page. In the dialog box that appears, click OK. Modify the content of a Markdown chart i. Click Edit in the upper-right corner of the Dashboard page. ii. Click the specified Markdown chart, find the More icon in the upper-right corner of chart, and then click Edit . iii. Modify the chart content, and then click OK. iv. Click Save in the upper-right corner of the dashboard page. In the dialog box that appears, click OK. Delete a Markdown chart i. Click Edit in the upper-right corner of the Dashboard page. ii. Click the specified Markdown chart, find the More icon in the upper-right corner of chart, and then click Delet e. iii. Click Save in the upper-right corner of the dashboard page. In the dialog box that appears, click OK. Common Markdown syntax Title Markdown syntax:

```bash
# Level 1 heading
## Level 2 heading
### Level 3 heading
```

Link Markdown syntax:

```
### Contents
[Chart description](https:// xxx) [Dashboard](https:// xxx)
```

Link preview Image Markdown syntax:

```
<div align=center> ![ Alt txt][id] With a reference later in the document defining the URL location [id]: https://octodex.github.com/images/dojocat.jpg "The Dojocat"
```

Special tag Markdown syntax:

```
--- __Advertisement :)__ ==some mark== `some code`
> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>> Shortcuts (emoticons): :-) 8-) ;) __This is bold text__ *This is italic text* ---
```

## 5 Alerts

### 5.1 Overview

Log Service enables you to configure alerts for charts on a dashboard to monitor the service status in real time. You can configure alerts on the Search & Analysis page of a Logstore or on a Dashboard page. When you configure an alert, you must configure the alert name, trigger condition, notification method, and other parameters. After you Configure an alert rule, Log Service checks the query results on the dashboard at an interval and sends an alert notification if the check results meet the specified conditions. In this way, Log Service facilitates real-time monitoring of the service status.

| Item | Description |
|---|---|
| Associated charts | The number of charts that can be associated with an alert ranges from 1 to 3. |
| String | If the length of a string exceeds 1,024 characters, only the first 1,024 characters are computed during a query. |
| Conditional expression | The conditional expression must be 1 to 128 characters in length. The conditional expression is evaluated based on the first 100 log entries returned for a query. The conditional expression can be evaluated up to 1,000 times. If the conditional expression is not matched, the alert is not triggered. |
| Search Period | The time range of each query statement cannot exceed 24 hours. |

Query statement in an alert An alert is configured based on analysis charts on a dashboard. An analysis chart is a visualized query result of a query statement. A query statement can include a search statement and an analytic statement. If you use only a search statement for a query, log data that matches the search condition is returned. If you include search and analytic statements for a query, log data that matches the search condition is analyzed before being returned. Search statement For example, you want to query the data that contains "error" information in the last 15 minutes. The search statement is error. A total of 154 log entries are retrieved. Each log entry consists of key-value pairs. You can set an alert rule for the value of a key.

> Not e If over 100 log entries are returned for a query, only the first 100 log entries are used for evaluating the conditions set in an alert. An alert is triggered when any of the first 100 log entries returned meets the conditions.

Search and analytic statement For example, the following statement queries the ratio of log entries whose status field value is ok to all log entries. For more information about query syntax, see Query syntax.

```
* | select sum(case when status='ok' then 1 else 0 end) *1.0/count(1) as ratio
```

If you set the trigger condition of an alert to `ratio < 0.9` , the alert is triggered when the ratio of log entries whose status field value is ok to all log entries is less than 90%.

### 5.2 Configure an alarm

#### 5.2.1 Configure alerts

Log Service allows you to configure alerts on the Search & Analysis page of a Logstore or on a dashboard page. If the trigger condition of an alert is met, the alert is triggered and a notification is sent to specified recipients. Prerequisites Log data is collected. The indexing feature is enabled and indexes are configured. For more information, see Enable the index feature and configure indexes for a Logstore. Context Alerts are configured based on analysis charts. When you view an analysis chart, you can add the chart to a dashboard and configure an alert for the chart. You can also configure an alert for the existing charts on a dashboard. Create a chart and configure an alert for the chart You can save the results of a query statement as a chart on a dashboard, and configure an alert for the chart. When you configure an alert on the Search & Analysis page, you must specify the name of the dashboard on which the chart is saved and the chart name. Configure an alert for existing charts on a dashboard. You can configure an alert for one or more charts on a dashboard at a time. When you configure an alert for multiple charts, you can specify a conditional expression for each chart and combine the conditional expressions into the trigger condition for the alert. This topic describes how to configure an alert for existing charts on a dashboard.

> Not e If an alert is configured for a chart on a dashboard and you update the search and analytic statement of the chart, you must update the search and analytic statement in the alert configuration. For more information, see Modify an alert.

For information about example alert configurations, see FAQ about alerts.
1. Log on to the Log Service console.
2. In the Projects section, click the project that you want to manage.
3. In the left-side navigation pane, click the Dashboard icon.
4. Click the target dashboard name.
5. In the upper-right corner of the dashboard, choose Alert s > Creat e.
6. In the Create Alert wizard, configure an alert and click Next .
The following table describes the configuration parameters of an alert.

| Parameter | Description |
|---|---|
| Alert Name | The name of the alert. The name must be 1 to 64 characters in length. |
| Associat ed Chart | The chart that is associated with the alert. The Search Period parameter specifies the time range of log data that Log Service reads when you query data. You can select a relative time or a time frame. For example, if you set Search Period to 15 minutes (relative) and start the query at 14:30:06, Log Service reads the log data that was written from 14:15:06 to 14:30:06. If you set Search Period to 15 minutes (time frame) and start the query at 14:30:06, Log Service reads the log data that was written from 14:15:00 to 14:30:00. To associate the alert with multiple charts, you must separately add and configure the charts. The number before the chart name indicates the sequence number of the chart in the alert configuration. You can use the sequence number to associate a chart in the trigger condition. |
| Frequency | The time interval at which Log Service executes the alert. |

| Guide·Alerts | Log Servic |
|---|---|

| Parameter | Description |   |   |   |
|---|---|---|---|---|
| T rigger Condit ion | The conditional expression that determines whether to trigger the alert. If the condition is met, Log Service sends an alert notification based on the specified Check Frequency and Not if icat ion Int erval. For example, you can enter pv%100 > 0 && uv > 0 in the Trigger Condition field. Not e In the conditional expression, you can use $sequence nu mber to differentiate charts. For example, you can use $0 to identify the chart whose sequence number is 0. |   |   |   |
|   |   | $sequence nu |   |   |
| Advanced |   |   |   |   |
| Not if icat ion T rigger T hreshold | If the number of times that the trigger condition is met exceeds this threshold and the specified Not if icat ion Int erval elapses, Log Service sends an alert notification to the specified recipients. The default value of Not if icat ion T rigger T hreshold is 1. This value indicates that each time the specified T rigger Condit ion is met, Log Service checks Not if icat ion Int erval to determine whether to send notifications. You can set a custom value. This way, Log Service sends an alert notification to the specified recipient only after the trigger condition is met multiple times. For example, if you set the value to 100, Log Service checks Not if icat ion Int erval only after the trigger condition is met 100 times. If the Not if icat ion T rigger T hreshold and Not if icat ion Int erval are reached, Log Service sends an alert notifications to the specified recipients. The overall count is then reset to zero. If Log Service fails to check log data due to exceptions such as network failures, the overall count does not change. |   |   |   |
| Not if icat ion Int erval | The time interval at which Log Service sends an alert notification. If the number of times that the trigger condition is met exceeds the specified Not if icat ion T rigger T hreshold and the specified notification interval elapses, Log Service sends an alert notification to the specified recipients. If you set this parameter to 5 minutes, you can receive up to one alert notification every 5 minutes. The default value is No Interval. Not e You can use the Notification Trigger Threshold and Notification Interval parameters to control the number of alert notifications that you receive. |   |   |   |

|   |   | mber |
|---|---|---|

7. Set the notification method.
Notifications can be sent to a custom webhook address in a specified format. To use this notification method, you must set the Request URL, Request Met hod, and Request Cont ent parameters. For more information, see Notification methods. Request URL: a custom webhook address, for example, https://webhook.com/notify. Request Met hod: the request method. Request methods include GET, PUT, POST, DELETE, and OPTIONS. Request Cont ent : the content of the notification. The content must be 1 to 500 characters in length. Template variables are supported.
8. Click OK.

#### 5.2.2 Grant permissions on alerts to a RAM user

This topic describes how to grant a RAM user the permissions to enable the alerting feature. Context Grant a RAM user the permissions only to create and modify alerts. Create a custom authorization policy, and apply the policy to the RAM user. For more information, see Procedure in this topic. 1.
2. Create a RAM role.
3. Create a permission policy.

| Use the following policy and replace the | <Project name> | with the actual project name. |
|---|---|---|
| { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:CreateLogStore", "log:CreateIndex", "log:UpdateIndex" ], "Resource": "acs:log:*:*:project/<Project name>/logstore/internal-alert-history" }, { "Effect": "Allow", "Action": [ "log:CreateDashboard", "log:CreateChart", "log:UpdateDashboard" ], "Resource": "acs:log:*:*:project/<Project name>/dashboard/*" }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": "acs:log:*:*:project/<Project name>/job/*" } ] } |   |   |

4. Create a user.
5. Create a RAM user group.
7. Grant permissions to a RAM role.

#### 5.2.3 Configure alert notification methods

This topic describes how to configure the notification methods for an alert in Log Service. Log Service supports the following alert notification methods: custom webhooks and DingTalk chatbot webhooks. Custom webhooks You can set the alert notification method to WebHook-Custom. If an alert is triggered, Log Service sends an alert notification to the custom webhook URL.

> Not e The timeout period for this method is 5 seconds. If no response is received within 5 seconds after a notification is sent, it means that the notification has failed.

1. When you Configure an alert rule, select WebHook-Cust om from the Not if icat ions drop-down list.
2. Set the following parameters.

| Parameter | Description |
|---|---|
| Request URL | The custom webhook URL. |
| Request Met hod | The method that is used to send the notification. Request available methods include GET, POST, DELETE, PUT, and OPTIONS. The default request header is Content-Type: application/json;charset=utf-8. If you need to add request headers, click Add Request Headers. |
| Cont ent | The notification content is specified by default. The value must be 1 to 500 characters in length. You can specify a custom value. Template variables are supported. For more information, see Template variables. |

3. Click Submit .
DingTalk chatbot webhooks If you set the notification method to WebHook-DingTalk Bot, Log Service sends alert notifications by using a DingTalk chatbot to the DingTalk group to which a specified webhook URL points. The chatbot can also remind the specified contacts of the alert notifications.

> Not e Each DingTalk chatbot can send a maximum of 20 alert notifications per minute.

1. Create a DingTalk chatbot.
i. Open DingTalk and go to a DingTalk group. ii. In the upper-right corner of the chat window, click the Group Set t ings icon and choose Group Assist ant > Add Robot . iii. In the Chat Bot dialog box, click the + icon in the Add Robot section. iv. In the Robot details dialog box, select Cust om (Cust om message services via Webhook) and click Add. v. In the Add Robot dialog box, enter a chat bot name and select securit y opt ions based on your business requirements. Then, select I have read and accept ed DingT alk Cust om Robot Service T erms of Service and click Finished.

> Not e We recommend that you set the Securit y Set t ings parameter to Cust om Keywords. You can set a maximum of 10 keywords. Each message must contain at least one keyword. We recommend that you set a keyword to Alert . 关于安全设置，更多信息，请参见钉钉开放平台。

vi. Click Copy to copy the webhook URL.
2. Configure a notification method in the Log Service console.
i. When you Configure an alert rule, select WebHook-DingT alk Bot from the Not if icat ions drop-down list. ii. Set the following parameters.

| Parameter | Description |
|---|---|
| Request URL | The webhook URL of the DingTalk chatbot. Paste the webhook URL that you copied in Step 1. |
| T it le | The alert topic. The value must be 1 to 100 characters in length. You can specify a custom value. Template variables are supported. For more information, see Template variables. |
| Recipient s | The group members whom you want to remind to read the alert notification. Valid values: None, All, and Specified Members. If you select Specif ied Members, enter the mobile phone numbers of the group members in the T agged List field. Separate multiple mobile phone numbers with commas (,). |
| Cont ent | The notification content is specified by default. You can modify the content based on your business requirements. The value must be 1 to 500 characters in length. You can specify a custom value. Template variables are supported. For more information, see Template variables. Not e If you need to remind a group member to read the alert notification, use the @< Mobile phone number of t he group member> syntax in the Content field. |

iii. Click Submit . Template variables You must set Cont ent for each notification method. In the notification content, you can reference some template variables in the ${fieldName} format for the alert. When Log Service sends an alert notification, Log Service replaces the template variables referenced in the Cont ent field with the actual values. For example, Log Service replaces ${Project} with the name of the project to which the alert belongs.

> Not e You must reference valid variables. If a referenced variable does not exist or is invalid, Log Service processes the variable as a null string. If the value of a referenced variable is of the object type, the value is converted and displayed as a JSON string.

The following table describes all available variables and how to reference these variables for an alert.

| Variable | Description | Example | Reference example |
|---|---|---|---|
| Aliuid | The ID of the Apsara Stack tenant account to which the project belongs. | 1234567890 | The alert that is configured by the user ${Aliuid} is triggered. |
| Project | The project to which the alert belongs. | my-project | The alert that is configured in the project ${Project} is triggered. |
| AlertID | The alert ID | 0fdd88063a611aa114938f937 1daeeb6-1671a52eb23 | The ID of the triggered alert is ${AlertID}. |
| AlertName | The name of the alert. The name must be unique in a project. | alert-1542111415-153472 | The ${AlertName} alert is triggered. |

| Variable | Description | Example | Reference example |
|---|---|---|---|
| AlertDisplayName | The display name of the alert rule. | My alert | The ${AlertDisplayName} alert is triggered. |
| Condition | The conditional expression that triggers the alert. Each variable in the conditional expression is replaced by the value that triggers the alert. The value is enclosed in brackets []. | [5] > 1 | The conditional expression that triggers the alert is ${Condition}. |
| RawCondition | The original conditional expression that triggers the alert is ${RawCondition}. | count > 1 | The trigger condition is ${RawCondition}. |
| Dashboard | The name of the dashboard with which the alert is associated. | mydashboard | The alert rule is associated with the ${Dashboard} dashboard. |
| DashboardUrl | The URL of the dashboard with which the alert is associated. | https://sls.console.aliyun.co m/next/project/myproject/da shboard/mydashboard | The URL of the dashboard that is associated with the alert is ${DashboardUrl}. |
| FireTime | The time when the alert is triggered. | 2018-01-02 15:04:05 | The alert is triggered at ${FireTime}. |
| FullResultUrl | The URL that is used to query the history records that the alert was triggered. | https://sls.console.aliyun.co m/next/project/my- project/logsearch/internal- alert-history? endTime=1544083998&queryS tring=AlertID%3A9155ea1ec10 167985519fccede4d5fc7- 1678293caad&queryTimeType =99&startTime=1544083968 | Click ${FullResultUrl} to view details. |

| Variable | Description | Example | Reference example |
|---|---|---|---|
| Results | The parameters and results of each log data query. The value is of the array type. For more information, see Fields in alert log entries. Not e A maximum of 100 alert notifications can be sent. | [ { "EndTime": 1542507580, "FireResult": { " time ": __ __ "1542453580", "count": "0" }, "LogStore": "test- logstore", "Query": "* \| SELECT COUNT(*) as count", "RawResultCount": 1, "RawResults": [ { " time ": __ __ "1542453580", "count": "0" } ], "StartTime": 1542453580 } ] | The first query starts at ${Results[0].StartTime} and ends at ${Results[0].EndTime}. The alert has been triggered ${Results[0].FireResult.count} times. Not e In this example the value 0 is the sequence number of a chart. For more information, see How can I view the serial number of a chart? |

### 5.3 Modify and view an alarm

#### 5.3.1 Modify an alert

This topic describes how to modify an alert. After you create an alert, you can modify the alert and then update the alert. To modify an alert associated with a search statement, you can directly modify the search statement. Precautions You can modify only search statements with which alerts are associated. You cannot modify search statements to search and analytic statements, which are in the format of search statement|analytic statement . For example, after you associate the `request_method: GET` statement with an alert, you can modify the statement to `error` , but you cannot modify the statement to error| select count(1) as c . To modify an alert, you can click Modif y Set t ings on the Alert Overview page, or choose Alert s > Modif y on the associated dashboard. Modify the search statement associated with an alert If you associate a search statement with an alert, you can modify the search statement to modify the alert.
1. Log on to the Log Service console.
2. Click a project name.
3. In the left-side navigation pane, click the Dashboard icon.
4. In the dashboard list, click the name of the target dashboard.
5. On the dashboard, choose Alert s > Modif y.
6. Find the search statement, and then click
. You can modify only search statements with which alerts are associated. You cannot modify search statements to search and analytic statements, which are in the format of search statement|analytic statem `ent` .
7. On the dialog box that appears, enter a new search statement, click Preview, and then click OK after the
search statement is verified.
8. Modify other parameters specific to your environment, such as Frequency and T rigger Condit ion, and then
click Next .
9. Set the notification method, and then click Submit .
Modify the chart associated with an alert After you create an alert, you can modify the chart associated with the alert to modify the alert.
1. In the dashboard list, click the name of the target dashboard.
2. On the dashboard, choose Alert s > Modif y.
3. Find the Associat ed Chart , and then click
next to Query.
4. On the dialog box that appears, enter a new query statement, click Preview, and then click OK after the query
statement is verified.
5. Modify other parameters specific to your environment, such as Frequency and T rigger Condit ion, and then
click Next .
6. Set the notification method.
7. Click Submit . The new settings take effect immediately.

#### 5.3.2 View history alerts

This topic describes how to view history alerts in the Log Service console. Log Service records alerts as log data and creates a dashboard to display alert details. View history alerts in the Logstore When you create an alert, Log Service creates a Logstore named int ernal-alert -hist ory for the project to which the alert belongs. A log entry is generated and written to the Logstore each time the alert rule is executed, regardless of whether the alert is triggered. For more information about the fields in the log entry, see Fields in alert log entries.

> Not e The Logstore does not incur fees and cannot be deleted or modified. Each alert log entry is retained in the Logstore for seven days.

1. Log on to the Log Service console.
2. Click a project name.
3. Click the
icon next to the int ernal-alert -hist ory Logstore, and then select Search & Analysis.
4. On the page that appears, query alert log entries based on your needs.
View history alerts on the dashboard After you create an alert, Log Service creates a dashboard named int ernal-alert -analysis for the project to which the alert belongs. The dashboard displays the statistics of all previous alerts, including the number of triggered alerts, percentage of successful alerts and notifications, and top 10 alerts whose alert rules are executed.

> Not e The dashboard cannot be deleted or modified.

1. In the left-side navigation pane, click the Dashboard icon.
2. Click Alert Hist ory St at ist ics to open the dashboard page.
On the Alert Hist ory St at ist ics dashboard, the details of history alerts are displayed, including whether the alerts are triggered, why the alerts are triggered, error information, and other information.

#### 5.3.3 Manage an alert

This topic describes how to manage an alert after you create the alert. Context You can disable, enable, modify, and delete the alert, or view the details of the alert such as the update time. View the details of an alert
1. Log on to the Log Service console.
2. Click a project name.
3. In the left-side navigation pane, click the Alert s icon.
4. In the alert list, click the name of the target alert.
On the Alert Overview page, you can view the details of the alert, such as the dashboard, creation time, last update time, check frequency, alert status, and notification status. Disable and enable an alert After you create an alert, you can disable or enable the alert. If you disable an alert, Log Service no longer checks the alert or send alert notifications.
1. In the left-side navigation pane, click the Alert s icon.
2. In the alert list, click the name of the target alert.
On the Alert Overview page, click Enable or Close in the Alert St at us field. Disable and enable alert notifications You can disable notifications of enabled alerts. After you disable notifications of an alert, alert notifications are not sent even if the trigger condition is met.
1. In the left-side navigation pane, click the Alert s icon.
2. In the alert list, click the name of the target alert.
On the Alert Overview page, click Modif y in the Not if icat ion St at us field.
3. Set the time range for which notifications are disabled, and then click Conf irm.
After you disable alert notifications, you can view the time when alert notifications resume in the Not if icat ion St at us field. You can click Modif y in the Not if icat ion St at us field to manually resume alert notifications. Delete an alert You cannot recover a deleted alert. Proceed with caution when you delete an alert.
1. In the left-side navigation pane, click the Alert s icon.
2. In the alert list, click the name of the target alert.
3. On the Alert Overview page, click Delet e Alert .
4. In the dialog box that appears, click OK.

### 5.4 Relevant syntax and fields for reference

reference

#### 5.4.1 Conditional expression syntax of an alert

This topic describes how to configure a conditional expression for an alert in Log Service. An alert is triggered if the conditional expression configured for the alert is met. In determining whether the conditional expression of an alert is met, the results of query statements configured for the alert are used as the inputs and the log fields in the conditional expression are used as the variables. If the conditional expression is met, the alert is triggered. Negative numbers must be enclosed with parentheses (), for example, x +(-100)<100. Numeric data is treated as 64-bit floating-point numbers. If a comparison is performed, errors may occur. A variable can contain only letters and digits and must start with a letter. A conditional expression can be up to 128 characters in length. A conditional expression can be evaluated up to 1,000 times. If an alert is configured for multiple charts and the conditional expression of the alert is not met after 1,000 times of evaluation, the alert is not triggered. A maximum of three charts can be associated with an alert. An alert is triggered if and only if the Boolean value of its conditional expression is true. For example, the result of the expression 100+100 is 200, which cannot trigger the alert. `true` , `false` , $ , and `.` are reserved and cannot be used as variables. Basic syntax The following table lists the syntax supported in a conditional expression.

| Syntax | Description | Examples |
|---|---|---|
| Basic operators | Supports the addition operator (+), subtraction operator (-), multiplication operator (*), division operator (/), and modulus operator (%). | x*100+y>200 x%10>5 |
| Comparison operators | Supports eight comparison operators, including the greater than operator (>), greater than or equal to operator (>=), less than operator (<), less than or equal to operator (<=), equal to operator (==), not equal to operator (! =), match operator (=~), and mismatch operator (! ~). Not e Backslashes (/) must be escaped. Regular expressions support the RE2 syntax. | x >= 0 x < 100 x <= 100 x == 100 x == "foo" Regular expression: x =~ "\\w +" |
| Logical operators | Supports the logical operators AND (&&) and OR (\|\|). | x >=0&&y <=100 x > 0 \|\| y > 0 |
| Logical negation | Supports the logical negation operator (!). | !( a < 1 && a > 100) |
| Numeric constants | Numeric constants are processed as 64-bit floating-point numbers. | x > 100 |
| String constants | String constants are formatted in a string enclosed in single quotation marks (''). | foo == 'string' |
| Boolean constants | Supports true and false. | (x > 100) == true |
| Parentheses | Parentheses () can be used to enforce precedence order. | x*(y+100)>100 |
| contains function | Determines whether a substring is included in a string. For example, if the result of the contains(field, 'xxxx') function is true, the field string includes the xxxx substring. | contains(foo, 'hello') |

Conditional expression for results of multiple query statements Syntax If you configure an alert for multiple charts, the variables in a conditional expression must be prefixed. In this way, you can specify from which query result to obtain the corresponding values of the variables when it evaluates your expression. The format is $N.fieldname , where N is the sequence number of the query statement. You can configure up to three query statements in an alert. Therefore the value range of N is 0 to 2. For example, $0.foo indicates to obtain the value of the foo field returned from the first query statement. If you configure one query statement in an alert, you do not need to specify the prefix.

> Not e How can I view the sequence number of a query statement?

In the Alert Configuration step, the Associat ed Chart parameter specifies the sequence number of each query statement (chart). The first query statement is numbered 0, the second query statement is numbered 1, and the third statement is numbered 2. Evaluate a conditional expression If multiple query results are returned, the variables specified in the conditional expression determine how to use the results to evaluate the conditional expression. For example, if you configure three query statements in an alert, x, y, and z log entries are returned when you execute each of the three statements. The conditional expression that you configure for the alert is $0.foo > 100 && $1.bar < 100. Then the first two query results are used to evaluate the conditional expression. A maximum of x × y times of evaluation (or 1,000 if x × y is greater than 1,000) is performed. If the conditional expression is met within the maximum times of evaluation, true is returned. Otherwise, false is returned. Operations

> Not e
> 64-bit floating-point numbers are used in a conditional expression.
> Each string constant must be enclosed in single quotation marks ('') or double quotation marks (""), for example, 'string', and "string".
> Boolean values include true and false.

| Operator | Operation |   |   |
|---|---|---|---|
|   | Operation between variables | Operation between non- string constants and variables | Operation between string constants and variables |
| Basic operators, including the addition operator (+), subtraction operator (-), multiplication operator (*), division operator (/), and modulus operator (%) | The left and right operands are converted to numbers before being operated. |   | Unsupported. |

| Operator | Operation |   |   |
|---|---|---|---|
|   | Operation between variables | Operation between non- string constants and variables | Operation between string constants and variables |
| Comparison operators, including the greater than operator (>), greater than or equal to operator (>=), less than operator (<), less than or equal to operator (<=), equal to operator (==), not equal to operator (! =) | Operations are performed based on the following priorities: 1. The left and right operands are converted to numbers before being operated based on the numerical order. If the conversion fails, 2. operands are operated based on the alphabetical order of strings. | The left and right operands are converted to numbers before being operated based on the numerical order. | The left and right operands are operated based on the alphabetical order of strings. |
| Regular expression match operator (=~) and regular expression mismatch operator (! ~) | The left and right operands are operated based on the alphabetical order of strings. | Unsupported. | The left and right operands are operated based on the alphabetical order of strings. |
| Logical operators, including AND (&&) and OR (\|\|) | These two operators cannot be directly used on the fields in query results. The left and right operands must be sub-expressions, and the values of the sub-expressions are of the Boolean type. |   |   |
| Logical negation (!) | This operator cannot be directly used on the fields in query results. The left and right operands must be sub-expressions, and the values of the sub-expressions are of the Boolean type. |   |   |
| contains function | The left and right operands are operated based on the alphabetical order of strings. | Unsupported. | The left and right operands are operated based on the alphabetical order of strings. |
| Parentheses () | Parentheses () enforce precedence order. |   |   |

#### 5.4.2 Fields in alert log entries

After you configure an alert, Log Service automatically creates a Logstore to store log entries that are generated when alert rules are executed and notifications are sent. This topic describes fields in alert log entries. Fields

| Field | Description | Example |
|---|---|---|
| AlertDisplayName | The display name of an alert. | Test alert rules |
| AlertID | The unique ID of an alert. | 0fdd88063a611aa114938f9371daeeb6- 1671a52eb23 |
| AlertName | The unique name of an alert in a project. | alert-1542111415-153472 |
| Condition | The conditional expression configured for an alert. | $0.count > 1 |
| Dashboard | The dashboard associated with an alert. | my-dashboard |
| FireCount | The cumulative times that an alert has been triggered since the last notification was sent. | 1 |
| Fired | Indicates whether an alert was triggered. Valid values: true and false. | true |
| LastNotifiedAt | The time when the last notification was sent. The time is displayed in a Unix timestamp. | 1542164541 |
| NotifyStatus | The status of a notification. Valid values: Success: indicates that a notification was successfully sent. Failed: indicates that a notification failed to be sent. NotNotified: indicates that no notification was sent. PartialSuccess: indicates that the notification sending partially succeeded. | Success |
| Reason | The reason that a notification failed to be sent or no notification was sent. | result type is not bool |
| Results | The parameters and results of each log data query. The value is of the array type. For information about parameters in the Results field, see Parameters in the Result field. | [ { "EndTime": 1542334900, "FireResult": null, "LogStore": "test-logstore", "Query": "* \| select count(1) as count", "RawResultCount": 1, "RawResults": [ { " time ": "1542334840", __ __ "count": "0" } ], "StartTime": 1542334840 } ] |
| Status | The execution result of an alert. Valid values: Success and Failed. | Success |

Parameters in the Result field

| Parameter | Description | Example |
|---|---|---|
| Query | The query statement that is configured in an alert. | * \| select count(1) as count |
| LogStore | The target Logstore of a query. | my-logstore |
| StartTime | The time when a query starts. | 2019-01-02 15:04:05 |
| StartTimeTs | The time when a query starts. The time is in the Unix timestamp format. | 1542334840 |
| EndTime | The time when a query ends. | 2019-01-02 15:19:05 |
| EndTimeTs | The time when a query ends. The time is in the Unix timestamp format. The actual query time range is [StartTime, EndTime) . | 1542334900 |
| RawResults | The raw query result. The parameter value is formatted in an array where each element is a log entry. The maximum length of the array is 100. | [ { " time ": "1542334840", __ __ "count": "0" } ] |
| RawResultsAsKv | The query result that is formatted in key- value pairs. Not e This parameter can only be used as a template variable. It is not saved to a Logstore. | [foo:0] |
| RawResultCount | The number of log entries that are returned in the RawResults parameter. | 1 |
| FireResult | The log entry that records the triggering of an alert. If an alert is not triggered, the parameter value is null. | { " time ": "1542334840", __ __ "count": "0" } |
| FireResultAsKv | The log entry that records the triggering of an alert, formatted in key-value pairs. Not e This parameter can only be used as a template variable. It is not saved to a Logstore. | [foo:0] |

## 6 Real-time consumption

### 6.1 Overview

Log Service allows you to consume log data by using multiple methods. After data is collected to LogHub, you can consume the log data by using two methods. The following table describes the methods.

| Method | Scenarios | Timeliness | Retention period |
|---|---|---|---|
| Real-time consumption (LogHub) | Real-time computing | Real time | Custom |
| Indexing and query (LogSearch) | Online query of hot data | Real time | Custom |

LogHub allows you to pull log data and consume the data in real time. The following procedure describes how log data in a shard is consumed:
1. Obtain a cursor based on the start time and end time of data consumption.
2. Read log data based on the cursor and step parameters and return the position of the next cursor.
3. Move the cursor to continuously consume log data.
Consume log data by using an SDK You can use Log Service SDKs in multiple programming languages such as Java, Python, and Go to consume log data. Consume log data by using consumer groups Log Service provides an advanced method that allows you to consume logs by using consumer groups. A consumer group is a lightweight computing framework that allows multiple consumers to consume data from a Logstore at the same time. The consumers in a consumer group are automatically allocated shards. Data is consumed in order based on the time when it is written to the Logstore. In addition, the consumers can use checkpoints to resume consumption from a breakpoint. You can use consumer group SDKs in multiple programming languages such as Go, Python, and Java to consume log data. Log consumption by using real-time stream processing systems Use Spark Streaming clients to consume log data. Use Storm spouts to consume log data. Use Flink Connector to consume log data. Log consumption by using open-source services Use Flume to consume log data and import log data to Hadoop file system (HDFS) instances. Log search and analytics You can query log data in the Log Service console. You can also query log data by using an SDK or the API of Log Service. Log Service provides an HTTP-based RESTful API. You can call all log query API operations that are provided by Log Service.

### 6.2 Consume log data

Log Service provides SDKs in various programming languages, such as Java, Python, and Go. You can use an SDK to consume log data. Use an SDK to consume log data The following example shows how to use the SDK for Java to consume log data in a shard:

```java
Client client = new Client(host, accessId, accessKey);
    String cursor = client.GetCursor(project, logStore, shardId, CursorMode.END).GetCursor();
    System.out.println("cursor = " +cursor);
    try {
      while (true) {
        PullLogsRequest request = new PullLogsRequest(project, logStore, shardId, 1000, cursor);
        PullLogsResponse response = client.pullLogs(request);
        System.out.println(response.getCount());
        System.out.println("cursor = " + cursor + " next_cursor = " + response.getNextCursor());
        if (cursor.equals(response.getNextCursor())) {
            break;
```

`}`

```
        cursor = response.getNextCursor();
        Thread.sleep(200);
```

`}` `}`

```java
    catch(LogException e) {
      System.out.println(e.GetRequestId() + e.GetErrorMessage());
```

`}` Preview log data in the Log Service console Log preview is a way of log data consumption. To preview log data that is stored in a Logstore in the Log Service console, perform the following steps:
1. Log on to the Log Service console.
2. In the Projects section, click the target project.
3. In the Logstore list, find the target Logstore, click the
icon next to the Logstore, and then select Consumpt ion Preview.
4. In the Consumption Preview dialog box, select a shard, set a time range, and then click Preview.
The log preview page displays the log data of the first 10 packets in the specified time range.

### 6.3 Consumption by consumer groups

#### 6.3.1 Use consumer groups to consume log data

Log consumption by using consumer groups Consumer groups allow you to focus on the business logic during log data consumption. You do not need to consider factors such as Log Service implementation, load balancing among consumers, and failovers that may be introduced when you use an SDK to consume log data. Terms The following table describes the terms of consumer groups and consumers.

| Term | Description |
|---|---|
| consumer group | A consumer group consists of multiple consumers. Each consumer in a consumer group consumes different data in a Logstore. |
| consumer | The consumers in a consumer group consume data from specified data sources. Each consumer name in a consumer group must be unique. |

A Logstore has multiple shards. A consumer library allocates shards to consumers in a consumer group based on the following principles: Each shard can be allocated to one consumer. Each consumer can consume data from multiple shards. After a new consumer joins a consumer group, the shards allocated to the consumer group are reallocated to each consumer for load balancing. The reallocation is based on the preceding principles and cannot be viewed by users. A consumer library stores checkpoints. This allows consumers to resume consumption from a breakpoint and avoid repetitive consumption after a program fault is resolved. Log consumption by using consumer groups is implemented in Java or Python. The following procedure takes Java as an example to describe how consumer groups consume log data.
1. Add Maven dependencies.

```xml
<dependency>
  <groupId>com.google.protobuf</groupId>
  <artifactId>protobuf-java</artifactId>
  <version>2.5.0</version>
</dependency> <dependency>
  <groupId>com.aliyun.openservices</groupId>
  <artifactId>loghub-client-lib</artifactId>
  <version>0.6.16</version>
</dependency>
```

2. Create a file named main.java.

```java
import com.aliyun.openservices.loghub.client.ClientWorker; import com.aliyun.openservices.loghub.client.config.LogHubConfig; import com.aliyun.openservices.loghub.client.exceptions.LogHubClientWorkerException; public class Main {
    // The endpoint of Log Service.
    private static String sEndpoint = "cn-hangzhou.log.aliyuncs.com";
    // The name of a Log Service project.
    private static String sProject = "ali-cn-hangzhou-sls-admin";
    // The name of a Logstore.
    private static String sLogstore = "sls_operation_log";
    // The name of a consumer group.
    private static String sConsumerGroup = "consumerGroupX";
    // The AccessKey pair of an Apsara Stack tenant account or RAM user that is used to consume da
ta.
    private static String sAccessKeyId = "";
    private static String sAccessKey = "";
    public static void main(String[] args) throws LogHubClientWorkerException, InterruptedExceptio
n {
        // The second parameter is the consumer name. Each consumer name in a consumer group must
be unique. However, the names of consumer groups can be the same. When different consumers start m ultiple processes on multiple servers to consume the data of a Logstore, you can use a server IP a ddress to identify a consumer. The ninth parameter maxFetchLogGroupSize indicates the maximum numb er of log groups that are retrieved from the server at a time. Valid values: 1 to 1000. You can us e the default value or specify a value based on your requirements.
        LogHubConfig config = new LogHubConfig(sConsumerGroup, "consumer_1", sEndpoint, sProject,
sLogstore, sAccessKeyId, sAccessKey, LogHubConfig.ConsumePosition.BEGIN_CURSOR);
        ClientWorker worker = new ClientWorker(new SampleLogHubProcessorFactory(), config);
        Thread thread = new Thread(worker);
        // The ClientWorker instance automatically runs after the thread is executed and extends t
he Runnable interface.
        thread.start();
        Thread.sleep(60 * 60 * 1000);
        // The shutdown function of the ClientWorker instance is called to exit the consumption in
stance. The associated thread is automatically stopped.
        worker.shutdown();
        // Multiple asynchronous tasks are generated when the ClientWorker instance is running. We
recommend that you wait for 30 seconds to ensure that all running tasks exit after shutdown.
        Thread.sleep(30 * 1000);
```

`}` `}`
3. Create a file named SampleLogHubProcessor.java.

```java
import com.aliyun.openservices.log.common.FastLog; import com.aliyun.openservices.log.common.FastLogContent; import com.aliyun.openservices.log.common.FastLogGroup; import com.aliyun.openservices.log.common.FastLogTag; import com.aliyun.openservices.log.common.LogGroupData; import com.aliyun.openservices.loghub.client.ILogHubCheckPointTracker; import com.aliyun.openservices.loghub.client.exceptions.LogHubCheckPointException; import com.aliyun.openservices.loghub.client.interfaces.ILogHubProcessor; import com.aliyun.openservices.loghub.client.interfaces.ILogHubProcessorFactory; import java.util.List; public class SampleLogHubProcessor implements ILogHubProcessor {
    private int shardId;
    // Record the last persistent checkpoint time.
    private long mLastCheckTime = 0;
    public void initialize(int shardId) {
        this.shardId = shardId;
```

`}`

```java
    // The main logic of data consumption. All exceptions must be captured and cannot be thrown.
    public String process(List<LogGroupData> logGroups,
                          ILogHubCheckPointTracker checkPointTracker) {
        // Display the retrieved data.
        for (LogGroupData logGroup : logGroups) {
            FastLogGroup flg = logGroup.GetFastLogGroup();
            System.out.println(String.format("\tcategory\t:\t%s\n\tsource\t:\t%s\n\ttopic\t:\t%s\n
\tmachineUUID\t:\t%s",
                    flg.getCategory(), flg.getSource(), flg.getTopic(), flg.getMachineUUID()));
            System.out.println("Tags");
            for (int tagIdx = 0; tagIdx < flg.getLogTagsCount(); ++tagIdx) {
                FastLogTag logtag = flg.getLogTags(tagIdx);
                System.out.println(String.format("\t%s\t:\t%s", logtag.getKey(), logtag.getValue()
));
```

`}`

```java
            for (int lIdx = 0; lIdx < flg.getLogsCount(); ++lIdx) {
                FastLog log = flg.getLogs(lIdx);
                System.out.println("--------\nLog: " + lIdx + ", time: " + log.getTime() + ", GetC
ontentCount: " + log.getContentsCount());
                for (int cIdx = 0; cIdx < log.getContentsCount(); ++cIdx) {
                    FastLogContent content = log.getContents(cIdx);
                    System.out.println(content.getKey() + "\t:\t" + content.getValue());
```

`}` `}` `}`

```
        long curTime = System.currentTimeMillis();
        // Write checkpoints to the server every 30 seconds. If a ClientWorker instance does not r
espond within 30 seconds,
        // a new ClientWorker instance consumes data starting from the last checkpoint. A small am
ount of duplicate data may exist.
        if (curTime - mLastCheckTime > 30 * 1000) {
            try {
                // If the parameter is set to true, checkpoints are synchronized to the server imm
ediately. If the parameter is set to false, checkpoints are locally cached. The default synchroni zation interval of checkpoints is 60 seconds.
                checkPointTracker.saveCheckPoint(true);
            } catch (LogHubCheckPointException e) {
                e.printStackTrace();
```

`}`

```
            mLastCheckTime = curTime;
```

`}`

```
        return null;
```

`}`

```
    // The ClientWorker instance calls this function upon exit. You can perform a cleanup.
    public void shutdown(ILogHubCheckPointTracker checkPointTracker) {
        // Save consumption breakpoints to the server.
        try {
            checkPointTracker.saveCheckPoint(true);
        } catch (LogHubCheckPointException e) {
            e.printStackTrace();
```

`}` `}` `}`

```
class SampleLogHubProcessorFactory implements ILogHubProcessorFactory {
    public ILogHubProcessor generatorProcessor() {
        // Generate a consumption instance.
        return new SampleLogHubProcessor();
```

`}` `}`

> Not e Run the preceding code to display all data in a Logstore. If you want multiple consumers to consume data from the same Logstore, you can modify the code based on the comments. You can use the same consumer group name and different consumer names to start new consumption processes.

Limits and troubleshooting You can create a maximum of 10 consumer groups for each Logstore. The `ConsumerGroupQuotaExceed` error is reported if the number of consumer groups exceeds 10. We recommend that you configure Log4j for the consumer program to throw error messages within consumer groups. This improves the troubleshooting efficiency. If you save the log4j.properties file to the resources directory and run the program, the following error message appears:

```
[WARN ] 2018-03-14 12:01:52,747 method:com.aliyun.openservices.loghub.client.LogHubConsumer.sampleLogE rror(LogHubConsumer.java:159) com.aliyun.openservices.log.exception.LogException: Invalid loggroup count, (0,1000]
```

The following example is a typical log4j. properties configuration file:

```
log4j.rootLogger = info,stdout log4j.appender.stdout = org.apache.log4j.ConsoleAppender log4j.appender.stdout.Target = System.out log4j.appender.stdout.layout = org.apache.log4j.PatternLayout log4j.appender.stdout.layout.ConversionPattern = [%-5p] %d{yyyy-MM-dd HH:mm:ss,SSS} method:%l%n%m%n
```

Advanced operations The preceding code is suitable for log consumption in common scenarios. This section describes how to perform advanced operations in other scenarios. Consume data that is logged from a certain time point LoghubConfig in the preceding code has two constructors:

```
// The value of the consumerStartTimeInSeconds parameter is a UNIX timestamp representing the numbe r of seconds that have elapsed since 00:00:00 on January 1, 1970, 00:00:00 UTC. public LogHubConfig(String consumerGroupName,
                      String consumerName,
                      String loghubEndPoint,
                      String project, String logStore,
                      String accessId, String accessKey,
                      int consumerStartTimeInSeconds);
// The position parameter is an enumeration variable. LogHubConfig.ConsumePosition.BEGIN_CURSOR ind icates that the consumption starts from the earliest data. LogHubConfig.ConsumePosition.END_CURSOR indicates that the consumption starts from the latest data. public LogHubConfig(String consumerGroupName,
                      String consumerName,
                      String loghubEndPoint,
                      String project, String logStore,
                      String accessId, String accessKey,
                      ConsumePosition position);
```

You can use different constructors based on your requirements. However, if a checkpoint is stored on the server, you must start data consumption from this checkpoint. Reset a checkpoint In scenarios such as data padding or repeated computing, you may need to set the consumption position to a time point for a consumer group. Then data consumption is started from the consumption position. To set the consumption position, you can use either one of the following two methods: Delete the consumer group. a. Stop the consumption processes. b. Delete the consumer group from the Log Service console. c. Modify the code to specify the start time point for data consumption. d. Restart the consumption processes. Use an SDK to reset the start time point of data consumption for the consumer group. a. Stop the consumption processes. b. Use an SDK to modify the checkpoint. c. Restart the consumption processes.

```
public static void updateCheckpoint() throws Exception {
        Client client = new Client(host, accessId, accessKey);
        long timestamp = Timestamp.valueOf("2017-11-15 00:00:00").getTime() / 1000;
        ListShardResponse response = client.ListShard(new ListShardRequest(project, logStore));
        for (Shard shard : response.GetShards()) {
            int shardId = shard.GetShardId();
            String cursor = client.GetCursor(project, logStore, shardId, timestamp).GetCursor();
            client.UpdateCheckPoint(project, logStore, consumerGroup, shardId, cursor);
```

`}` `}` Use a RAM user to access consumer groups Before you use a RAM user to access consumer groups, you must grant relevant permissions to the RAM user. For more information, see Grant permissions to a RAM role. The following table lists the actions you can perform as a RAM user.

| Action | Resource |
|---|---|
| log:GetCursorOrData | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName} |
| log:CreateConsumerGroup | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/* |
| log:ListConsumerGroup | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/* |
| log:ConsumerGroupUpdateCheckPoin t | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/${consumerGroupName} |
| log:ConsumerGroupHeartBeat | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/${consumerGroupName} |
| log:UpdateConsumerGroup | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/${consumerGroupName} |
| log:GetConsumerGroupCheckPoint | acs:log:${regionName}:${projectOwnerAliUid}:project/${projectName}/logstore/ ${logstoreName}/consumergroup/${consumerGroupName} |

For example, a project named project-test resides in the China (Hangzhou) region. The ID of the Apsara Stack tenant account to which the project belongs is 1234567. The name of the Logstore to be consumed is logstoretest and the consumer group name is consumergroup-test. To allow a RAM user to access the consumer group, you must grant the following permissions to the RAM user: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "log:GetCursorOrData"
```

`],`

```json
      "Resource": "acs:log:cn-hangzhou:1234567:project/project-test/logstore/logstore-test"
```

`},` `{`

```json
      "Effect": "Allow",
      "Action": [
        "log:CreateConsumerGroup",
        "log:ListConsumerGroup"
```

`],`

```json
      "Resource": "acs:log:cn-hangzhou:1234567:project/project-test/logstore/logstore-test/consumergro
up/*"
```

`},` `{`

```json
      "Effect": "Allow",
      "Action": [
        "log:ConsumerGroupUpdateCheckPoint",
        "log:ConsumerGroupHeartBeat",
        "log:UpdateConsumerGroup",
        "log:GetConsumerGroupCheckPoint"
```

`],`

```json
      "Resource": "acs:log:cn-hangzhou:1234567:project/project-test/logstore/logstore-test/consumergro
up/consumergroup-test"
```

`}` `]` `}`

#### 6.3.2 View the status of a consumer group

This topic describes how to use the console, API, and SDK to view the status of a consumer group. Log data consumption by using consumer groups is an advanced real-time data consumption method provided by Log Service. Automatic load balancing is implemented among multiple consumption instances. Spark Streaming and Storm use consumer groups as the basic mode to consume log data. View the consumption progress in the console
1. Log on to the Log Service console.
2. In the Projects section, click the target project.
3. Find the target Logstore, and choose
> Dat a Consumpt ion.

4. Click the consumer group whose data consumption progress you want to view. The data consumption
progress of each shard in the Logstore is displayed. Use an API or SDK to view the data consumption progress The following example uses the SDK for Java to describe how to call API operations to view the data consumption progress.

```java
package test; import java.util.ArrayList; import com.aliyun.openservices.log.Client; import com.aliyun.openservices.log.common.Consts.CursorMode;
```

`p` `y` `p` `g` ;

```java
import com.aliyun.openservices.log.common.ConsumerGroup; import com.aliyun.openservices.log.common.ConsumerGroupShardCheckPoint; import com.aliyun.openservices.log.exception.LogException; public class ConsumerGroupTest {
    static String endpoint = "";
    static String project = "";
    static String logstore = "";
    static String accesskeyId = "";
    static String accesskey = "";
    public static void main(String[] args) throws LogException {
        Client client = new Client(endpoint, accesskeyId, accesskey);
        //Query all consumer groups of this Logstore. If no consumer group exists, the length of consu
merGroups is 0.
        ArrayList<ConsumerGroup>  consumerGroups;
        try{
            consumerGroups = client.ListConsumerGroup(project, logstore).GetConsumerGroups();
```

`}`

```java
        catch(LogException e){
            if(e.GetErrorCode() == "LogStoreNotExist")
                System.out.println("this logstore does not have any consumer group");
            else{
                //internal server error branch
```

`}`

```
            return;
```

`}`

```java
        for(ConsumerGroup c: consumerGroups){
            //Print consumer group properties, including the name, heartbeat timeout, and whether data
is consumed in order.
            System.out.println("Name: " + c.getConsumerGroupName());
            System.out.println("Heartbeat timeout: " + c.getTimeout());
            System.out.println("Consumption in order: " + c.isInOrder());
            for(ConsumerGroupShardCheckPoint cp: client.GetCheckPoint(project, logstore, c.getConsumer
GroupName()).GetCheckPoints()){
                System.out.println("shard: " + cp.getShard());
                //Format the returned time. The time is a long integer that is accurate to millisecond
```

`s.`

```java
                System.out.println("The last time when data was consumed: " + cp.getUpdateTime());
                System.out.println("Consumer name: " + cp.getConsumer());
                String consumerPrg = "";
                if(cp.getCheckPoint().isEmpty())
                    consumerPrg = "Consumption not started";
                else{
                    //The UNIX timestamp. Unit: seconds. Format the output value of the timestamp.
                    try{
                        int prg = client.GetPrevCursorTime(project, logstore, cp.getShard(), cp.getChe
ckPoint()).GetCursorTime();
                        consumerPrg = "" + prg;
```

`}`

```
                    catch(LogException e){
                        if(e.GetErrorCode() == "InvalidCursor")
                            consumerPrg = "Invalid. The previous consumption time has exceeded the ret
ention period of the data in the Logstore.";
                        else{
                            //internal server error
                            throw e;
```

`}` `}` `}`

```java
                System.out.println("Consumption progress: " + consumerPrg);
StringendCursor=client.GetCursor(project,logstore,cp.getShard(),CursorMode.END).
```

`St`

```
gedCuso
```

`c`

```
et.GetCuso(poject, ogstoe,cp.getSad(),Cuso ode.
```

`).`

```
GetCursor();
                int endPrg = 0;
                try{
                    endPrg = client.GetPrevCursorTime(project, logstore, cp.getShard(), endCursor).Get
CursorTime();
```

`}`

```
                catch(LogException e){
                    //do nothing
```

`}`

```java
                //The UNIX timestamp. Unit: seconds. Format the output value of the timestamp.
                System.out.println("The time when the last data entry was received: " + endPrg);
```

`}` `}` `}` `}`

### 6.4 Use LogHub Storm to consume log data

data Log Service provides efficient and reliable log collection and consumption channels. You can use Logtail or the SDK to collect log data in real time. After logs are collected to LogHub, you can use Apache Spark Streaming, Apache Storm, and other real-time computation systems to consume the log data. To reduce the consumption cost of LogHub data, Log Service provides LogHub Storm spouts for Storm users to read data from LogHub in real time. Basic architecture and flowchart LogHub Storm spouts are enclosed in the boxes with red dashed lines. Each Storm topology has a group of spouts that read data from a Logstore. Spouts in different topologies are independent of each other. Each topology is identified by a unique LogHub consumer group name. Spouts in the same topology use a consumer library to achieve load balancing and automatic failover. Spouts read data from LogHub in real time, send data to bolts in the same topology, and then save consumption checkpoints to the LogHub server on a regular basis. Basic architecture and flowchart You can create up to 10 consumer groups to consume log data from a Logstore. If a consumer group is no longer in use, you can call the DeleteConsumerGroup operation of the SDK for Java to delete the consumer group. We recommend that the number of spouts be equal to the number of shards in a Logstore. This is because a single spout may be unable to process a large amount of data in multiple shards. If the data volume in a shard exceeds the processing capacity of a single spout, you can split the shard to reduce its data volume. LogHub spouts and bolts must use the ack method to check whether log data is successfully sent from spouts to bolts and whether the data is successfully processed by the bolts. Examples Use the following code to create spouts and construct a topology:

```
     public static void main( String[] args )
```

`{`

```
        String mode = "Local"; // Specify to use the local test mode.
           String conumser_group_name = ""; // Specify a unique consumer group name for each topolo
gy. The name cannot be an empty string. It must be 3 to 63 characters in length and can contain low ercase letters, digits, hyphens (-), and underscores (_). It must start and end with a lowercase le tter or digit.
        String project = ""; // Specify the project in Log Service.
        String logstore = ""; // Specify the Logstore in Log Service.
        String endpoint = ""; // Specify the endpoint of Log Service.
        String access_id = ""; // Specify the AccessKey ID of the user.
        String access_key = "";
        // Configure a LogHub Storm spout.
        LogHubSpoutConfig config = new LogHubSpoutConfig(conumser_group_name,
                endpoint, project, logstore, access_id,
                access_key, LogHubCursorPosition.END_CURSOR);
        TopologyBuilder builder = new TopologyBuilder();
        // Create a LogHub Storm spout.
        LogHubSpout spout = new LogHubSpout(config);
        // You can create the same number of spouts as that of shards in a Logstore in actual busin
ess scenarios.
        builder.setSpout("spout", spout, 1);
```

```
        builder.setBolt("exclaim", new SampleBolt()).shuffleGrouping("spout");
        Config conf = new Config();
        conf.setDebug(false);
        conf.setMaxSpoutPending(1);
        // Configure the serialization method of LogGroupData by using the LogGroupDataSerializSeri
alizer class if Kryo is used to serialize and deserialize data.
        Config.registerSerialization(conf, LogGroupData.class, LogGroupDataSerializSerializer.class
```

);

```
        if (mode.equals("Local")) {
            logger.info("Local mode...") ;
            LocalCluster cluster  = new LocalCluster();
            cluster.submitTopology("test-jstorm-spout", conf, builder.createTopology());
            try {
                Thread.sleep(6000 * 1000);    //waiting for several minutes
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
```

`}`

```
            cluster.killTopology("test-jstorm-spout");
            cluster.shutdown();
        } else if (mode.equals("Remote")) {
            logger.info("Remote mode...");
            conf.setNumWorkers(2);
            try {
                StormSubmitter.submitTopology("stt-jstorm-spout-4", conf, builder.createTopology())
```

;

```
            } catch (AlreadyAliveException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            } catch (InvalidTopologyException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
```

`}`

```
        } else {
            logger.error("invalid mode: " + mode);
```

`}` `}` `}` Use the following example code of bolts to consume log data and display the content of each log entry:

```java
public class SampleBolt extends BaseRichBolt {
    private static final long serialVersionUID = 4752656887774402264L;
    private static final Logger logger = Logger.getLogger(BaseBasicBolt.class);
    private OutputCollector mCollector;
    @Override
    public void prepare(@SuppressWarnings("rawtypes") Map stormConf, TopologyContext context,
            OutputCollector collector) {
        mCollector = collector;
```

`}`

```java
    @Override
    public void execute(Tuple tuple) {
        String shardId = (String) tuple
                .getValueByField(LogHubSpout.FIELD_SHARD_ID);
        @SuppressWarnings("unchecked")
        List<LogGroupData> logGroupDatas = (ArrayList<LogGroupData>) tuple.getValueByField(LogHubSp
out.FIELD_LOGGROUPS);
        for (LogGroupData groupData : logGroupDatas) {
            // Each log group consists of one or more log entries.
            LogGroup logGroup = groupData.GetLogGroup();
            for (Log log : logGroup.getLogsList()) {
                StringBuilder sb = new StringBuilder();
                // Each log entry has a time field and other key-value pairs.
                int log_time = log.getTime();
                sb.append("LogTime:").append(log_time);
                for (Content content : log.getContentsList()) {
                    sb.append("\t").append(content.getKey()).append(":")
                            .append(content.getValue());
```

`}`

```
                logger.info(sb.toString());
```

`}` `}`

```
        // Spouts must use the ack method to indicate whether data has been successfully sent to bo
lts.
        // In addition, bolts must use the ack method to indicate whether data is successfully proc
essed by the bolts.
        mCollector.ack(tuple);
```

`}`

```java
    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        //do nothing
```

`}` `}` Maven Use the following code to add Maven dependencies for Storm versions earlier than Storm 1.0 (for example, Storm 0.9.6):

```xml
<dependency>
  <groupId>com.aliyun.openservices</groupId>
  <artifactId>loghub-storm-spout</artifactId>
  <version>0.6.6</version>
</dependency>
```

Use the following code to add Maven dependencies for Storm 1.0 and later versions:

```xml
<dependency>
  <groupId>com.aliyun.openservices</groupId>
  <artifactId>loghub-storm-1.0-spout</artifactId>
  <version>0.1.3</version>
</dependency>
```

### 6.5 Use Flume to consume log data

This topic describes how to use Flume to consume log data. You can use the aliyun-log-flume plug-in to connect LogHub of Log Service to Flume, and then write and consume log data. The aliyun-log-flume plug-in connects LogHub to Flume. When LogHub is connected to Flume, you can connect Log Service to other systems such as HDFS and Kafka through Flume. The aliyun-log-flume plug-in provides the Sink and Source methods to connect Log Service to Flume. Sink: uses Flume to read data from other data sources and then writes data to LogHub. Source: uses Flume to consume LogHub data and then writes data to other systems. LogHub Sink You can use the Sink method to transmit data from other data sources to LogHub through Flume. Data can be parsed into the following two formats: SIMPLE: writes a Flume event to LogHub as a field. DELIMITED: delimits a Flume event with delimiters, parses an event into fields based on the configured column names, and then writes the fields to LogHub. The following table lists the parameters you can configure when you use the Sink method to read data.

| Parameter | Required | Description |
|---|---|---|
| type | Yes | Valid value: com.aliyun.loghub.flume.sink.LoghubSink. |
| endpoint | Yes | The endpoint of Log Service. |
| project | Yes | The name of the project. |
| logstore | Yes | The name of the Logstore. |
| accessKeyId | Yes | The AccessKey ID of your Apsara Stack tenant account. |
| accessKey | Yes | The AccessKey secret of your Apsara Stack tenant account. |
| batchSize | No | The number of log entries that are written to LogHub at a time. Default value: 1000. |
| maxBufferSize | No | The maximum size of the queue in the buffer. Default value: 1000. |

| Parameter | Required | Description |
|---|---|---|
| serializer | No | The serialization format of log data. Valid values: DELIMIT ED: Data is parsed into the DELIMITED format. If you set this parameter to DELIMITED, you must set the columns parameter. SIMPLE: Data is parsed into the SIMPLE format. This is the default value. Custom serializer: Data is parsed into a custom serialization format. If you set this parameter to a custom serializer, you must specify the full name of the class. |
| columns | No | The configured column names. You must set this parameter if you set the serializer parameter to DELIMIT ED. Separate multiple columns with commas (,). Ensure that the columns are sorted in the same order as those of the log data. |
| separatorChar | No | The delimiter, which must be a single character. You can set this parameter if you set the serializer parameter to DELIMIT ED. Default value: , . |
| quoteChar | No | The quote character. You can set this parameter if you set the serializer parameter to DELIMIT ED. Default value: "" . |
| escapeChar | No | The escape character. You can set this parameter if you set the serializer parameter to DELIMIT ED. Default value: "" . |
| useRecordTime | No | Specifies whether to use the value of the timestamp field as the time when log data is written to Log Service. The default value false indicates that the current time is used. |

Loghub Source You can use the Source method to ship data from LogHub to other data systems through Flume. Data can be output in the following two formats: DELIMITED: writes delimited log data to Flume. JSON: writes JSON-formatted log data to Flume. The following table lists the parameters you can configure when you use the Source method to read data.

| Parameter | Required | Description |
|---|---|---|
| type | Yes | Valid value: com.aliyun.loghub.flume.source.LoghubSource. |
| endpoint | Yes | The endpoint of Log Service. |
| project | Yes | The name of the project. |
| logstore | Yes | The name of the Logstore. |
| accessKeyId | Yes | The AccessKey ID of your Apsara Stack tenant account. |

| User Guide·Real-time consu | mption | Log Servic |
|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| accessKey | Yes | The AccessKey secret of your Apsara Stack tenant account. |
| heartbeatIntervalMs | No | The heartbeat interval between the Flume client and LogHub. Unit: milliseconds. Default value: 30000. |
| fetchIntervalMs | No | The interval for pulling data from LogHub. Unit: milliseconds. Default value: 100. |
| fetchInOrder | No | Specifies whether to consume log data in the order that log data was generated. Default value: false. |
| batchSize | No | The number of log entries that are read at a time. Default value: 100. |
| consumerGroup | No | The name of the consumer group that reads data. The name is randomly generated. |
| initialPosition | No | The start point from which data is read. Valid values: begin, end, and timestamp. Default value: begin. Not e If a checkpoint exists on the server, the checkpoint is used. |
| timestamp | No | The Unix timestamp. You must set this parameter if you set the initialPosition parameter to t imest amp. Unix timestamp. |
| deserializer | Yes | The deserialization format of log data. Valid values: DELIMIT ED: Data is parsed into the DELIMITED format. This is the default value. If you set this parameter to DELIMITED, you must set the columns parameter. JSON: Data is parsed into the JSON format. Custom deserializer: Data is parsed into a custom deserialization format. If you set this parameter to a custom deserializer, you must specify the full name of the class. |
| columns | No | The configured column names. You must set this parameter if you set the deserializer parameter to DELIMIT ED. Separate multiple columns with commas (,). Ensure that the columns are sorted in the same order as those of the log data. |
| separatorChar | No | The delimiter, which must be a single character. You can set this parameter if you set the deserializer parameter to DELIMIT ED. Default value: , . |
| quoteChar | No | The quote character. You can set this parameter if you set the deserializer parameter to DELIMIT ED. Default value: "" . |
| escapeChar | No | The escape character. You can set this parameter if you set the deserializer parameter to DELIMIT ED. Default value: "" . |

| L | og Service |   | User Guide·Real-time consumptio | n |
|---|---|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| appendTimestamp | No | Specifies whether to append the timestamp as a field to the end of each log entry. You can set this parameter if you set the deserializer parameter to DELIMIT ED. Default value: false. |
| sourceAsField | No | Specifies whether to add the log source as a field named source . You can set this parameter if you set the __ __ deserializer parameter to JSON. Default value: false. |
| tagAsField | No | Specifies whether to add the log tags as a field with the field name tag : {tag names}. You can set this __ __ parameter if you set the deserializer parameter to JSON. Default value: false. |
| timeAsField | No | Specifies whether to add the log time as a field named time . You can set this parameter if you set the __ __ deserializer parameter to JSON. Default value: false. |
| useRecordTime | No | Specifies whether to use the value of the timestamp field as the time when log data is read from Log Service. The default value false indicates that the current time is used. Default value: false. |

### 6.6 Use open source Flink to consume log data

data Log Service provides the flink-log-connector plug-in to connect with Flink. This topic describes how to integrate the flink-log-connector plug-in with Flink to consume log data. Prerequisites An AccessKey pair, a Log Service project, and a Logstore are created. If you log on to Log Service with a RAM user, relevant permissions to access a Logstore are granted to a RAM user. For more information, see Grant permissions to a RAM role. Context The flink-log-collector plug-in includes flink-log-consumer and flink-log-producer. The flink-log-consumer plug-in reads data from Log Service. This plug-in supports the exactly-once semantics and load balancing among shards. The flink-log-producer plug-in writes data into Log Service. When you use the flink-log-producer plug-in, you must add the following Maven dependencies to a project:

```xml
<dependency>
   <groupId>com.aliyun.openservices</groupId>
   <artifactId>flink-log-connector</artifactId>
   <version>0.1.13</version>
</dependency> <dependency>
   <groupId>com.google.protobuf</groupId>
   <artifactId>protobuf-java</artifactId>
   <version>2.5.0</version>
</dependency>
```

Log Consumer The flink-log-consumer plug-in can consume the log data of a Logstore in Log Service. The exactly-once semantics is achieved during log consumption. The flink-log-consumer plug-in detects the change of the number of shards in a Logstore. This increases efficiency. Each Flink subtask consumes data of some shards in a Logstore. If shards in a Logstore are split or merged, the shards consumed by the subtask also change. When you use the flink-log-consumer plug-in to consume data from Log Service, you can call the following API operations: GetCursorOrData You can call this operation to pull log data from a shard. Frequent API requests may exceed the read speed and IOPS limits of the shard. You can specify the ConfigConstants.LOG_FETCH_DATA_INTERVAL_MILLIS and ConfigConstants.LOG_MAX_NUMBER_PER_FETCH parameters to control the interval of API requests and number of log entries pulled in each request.

```
configProps.put(ConfigConstants.LOG_FETCH_DATA_INTERVAL_MILLIS, "100"); configProps.put(ConfigConstants.LOG_MAX_NUMBER_PER_FETCH, "100");
```

ListShards You can call this operation to view all shards in a Logstore and the status of each shard. If the shards are frequently split and merged, you can adjust the call interval to detect the changes in the number of shards.

```
// Call the ListShards operation once every 30 seconds. configProps.put(ConfigConstants.LOG_SHARDS_DISCOVERY_INTERVAL_MILLIS, "30000");
```

CreateConsumerGroup You can call this operation to create a consumer group to synchronize checkpoints. This operation can be called only when consumption progress monitoring is enabled. ConsumerGroupUpdateCheckPoint You can call this operation to synchronize snapshots of Flink to a consumer group. The following table lists the Apsara Stack resources required for RAM users to call the preceding API operations.

| API |   | Alibaba Resource Name (ARN) |   |   |
|---|---|---|---|---|
| GetCursorOrData |   | acs:log:${regionName}:${projectOwnerAliUid}:pro ject/${projectName}/logstore/${logstoreName} |   |   |
| ListShards |   | acs:log:${regionName}:${projectOwnerAliUid}:pro ject/${projectName}/logstore/${logstoreName} |   |   |
| CreateConsumerGroup |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |   |
|   | teConsumerGroup | ject/${projectName}/logstore/${logstoreName}/cons |   |   |
|   |   | umergroup/* |   |   |
| ConsumerGroupUpdateCheckPoint |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |   |   |
|   |   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |   |
|   | umerGroupUpdateCheckPoint | ject/${projectName}/logstore/${logstoreName}/cons |   |   |
|   |   | umergroup/${consumerGroupName} |   |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |
|---|---|---|
| ursorOrData | ject/${projectName}/logstore/${logstoreName} |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |
|---|---|---|
| hards | ject/${projectName}/logstore/${logstoreName} |   |

For more information, see Grant permissions to a RAM role.
1. Configure startup parameters.
The following example shows how to consume log data. The java.util.Properties class is used as the configuration tool. You can find all constants to be configured in the ConfigConstants class.

```
Properties configProps = new Properties(); // Specify the endpoint of Log Service. configProps.put(ConfigConstants.LOG_ENDPOINT, "cn-hangzhou.log.aliyuncs.com"); // Specify the AccessKey pair. configProps.put(ConfigConstants.LOG_ACCESSSKEYID, ""); configProps.put(ConfigConstants.LOG_ACCESSKEY, ""); // Specify the project. configProps.put(ConfigConstants.LOG_PROJECT, "ali-cn-hangzhou-sls-admin"); // Specify the Logstore. configProps.put(ConfigConstants.LOG_LOGSTORE, "sls_consumergroup_log"); // Specify the start position to consume logs. configProps.put(ConfigConstants.LOG_CONSUMER_BEGIN_POSITION, Consts.LOG_END_CURSOR); // Specify the data deserialization method. RawLogGroupListDeserializer deserializer = new RawLogGroupListDeserializer(); final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); DataStream<RawLogGroupList> logTestStream = env.addSource(
        new FlinkLogConsumer<RawLogGroupList>(deserializer, configProps));
```

> Not e The number of subtasks in the Flink Streaming is independent of the number of shards in a Logstore. If the number of shards is greater than that of subtasks, each subtask consumes multiple shards exactly once. If the number of shards is less than that of subtasks, some subtasks are idle until new shards are generated.

2. Specify the start consumption position.
The flink-log-consumer plug-in enables you to specify the start consumption position of log data in a shard. By specifying the ConfigConstants.LOG_CONSUMER_BEGIN_POSITION parameter, you can start data consumption from the earliest, latest, or a specific time point. The flink-log-connector plug-in also allows a consumer group to resume consumption from a specific position. Valid values: Consts.LOG_BEGIN_CURSOR: The consumption starts from the earliest data. Consts.LOG_END_CURSOR: The consumption starts from the latest data. Consts.LOG_FROM_CHECKPOINT: The consumption starts from a checkpoint that is stored in a specific consumer group. You can use the ConfigConstants.LOG_CONSUMERGROUP parameter to specify the consumer group. UnixTimestamp: a string of the INTEGER data type. The timestamp is the number of seconds that have elapsed since 00:00:00 January 1, 1970. The value indicates that data in a shard is consumed from this time point. You can use the following code to specify a start consumption position:

```
configProps.put(ConfigConstants.LOG_CONSUMER_BEGIN_POSITION, Consts.LOG_BEGIN_CURSOR); configProps.put(ConfigConstants.LOG_CONSUMER_BEGIN_POSITION, Consts.LOG_END_CURSOR); configProps.put(ConfigConstants.LOG_CONSUMER_BEGIN_POSITION, "1512439000"); configProps.put(ConfigConstants.LOG_CONSUMER_BEGIN_POSITION, Consts.LOG_FROM_CHECKPOINT);
```

> Not e If you have configured consumption resumption from a state backend of Flink when you start a Flink job, the flink-log-connector plug-in uses checkpoints stored in the state backend.

3. (Optional)Configure consumption progress monitoring.
The flink-log-consumer plug-in enables you to configure consumption progress monitoring. Consumption progress indicates the real-time consumption position of each shard. These positions are indicated by timestamps. For more information, see View the status of a consumer group.

```
configProps.put(ConfigConstants.LOG_CONSUMERGROUP, "your consumer group name");
```

> Not e This configuration item is optional. If you specify this configuration item and no consumer group exists, the flink-log-consumer plug-in creates a consumer group. Snapshots in the flink-log- consumer plug-in are automatically synchronized to the consumer group of Log Service, and you can view the consumption progress of the flink-log-consumer plug-in in the Log Service console.

4. Configure consumption resumption and the exactly-once semantics.
If the checkpointing feature of Flink is enabled, the flink-log-consumer plug-in periodically stores the consumption progress of each shard. When a job fails, Flink restores the flink-log-consumer plug-in and starts to consume data from the latest checkpoint. While you configure the checkpointing period, the maximum amount of data to be re-consumed when a failure occurs is defined. You can use the following code to configure the checkpointing period:

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); // Configure the exactly-once semantics. env.getCheckpointConfig().setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE); // Store checkpoints every five seconds. env.enableCheckpointing(5000);
```

For more information about the Flink checkpoints, see Checkpoints in the Flink documentation. Log Producer The flink-log-producer plug-in writes data into Log Service.

> Not e The flink-log-producer plug-in supports the Flink at-least-once semantics. If a job fails, data written into Log Service may be duplicated but never lost.

When you use the flink-log-producer plug-in to writes data to Log Service, you can call the following API operations: PostLogStoreLogs ListShards The following table lists the Apsara Stack resources required for RAM users to call the preceding API operations.

| API | ARN |
|---|---|
| PostLogStoreLogs | acs:log:${regionName}:${projectOwnerAliUid}:pro ject/${projectName}/logstore/${logstoreName} |
| ListShards | acs:log:${regionName}:${projectOwnerAliUid}:pro ject/${projectName}/logstore/${logstoreName} |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |
|---|---|---|
| LogStoreLogs | ject/${projectName}/logstore/${logstoreName} |   |

|   |   | acs:log:${regionName}:${projectOwnerAliUid}:pro |
|---|---|---|
| hards | ject/${projectName}/logstore/${logstoreName} |   |

For more information about RAM users and how to authorize RAM users, see Grant permissions to a RAM role.
1. Initialize the flink-log-producer plug-in.
i. Configure startup parameters for the flink-log-producer plug-in. The initialization process for the flink-log-producer plug-in is similar to that for the flink-log-consumer plug-in. The following code shows the available parameters that you can configure for the flink-logproducer plug-in. You can use the default values of these parameters. You can also specify the parameters based on your needs.

```
// The number of I/O threads used to send data. Default value: 8. ConfigConstants.LOG_SENDER_IO_THREAD_COUNT // The time it takes to send the data after log data is cached. Default value: 3000. ConfigConstants.LOG_PACKAGE_TIMEOUT_MILLIS // The number of logs in the cached package. Default value: 4096. ConfigConstants.LOG_LOGS_COUNT_PER_PACKAGE // The size of the cached package. Default value: 3 Mbits. ConfigConstants.LOG_LOGS_BYTES_PER_PACKAGE // The total memory size that the job can use. Default value: 100 Mbits. ConfigConstants.LOG_MEM_POOL_BYTES
```

> Not e These parameters are optional. You can use their default values.

ii. Reload LogSerializationSchema to define the method of serializing data into RawLogGroup. To use the hash key to specify the shard for data writes, you can use the LogPartitioner method to generate the hash key for the data. Example:

```
FlinkLogProducer<String> logProducer = new FlinkLogProducer<String>(new SimpleLogSerializer(), configProps); logProducer.setCustomPartitioner(new LogPartitioner<String>() {
      // Generate a 32-bit hash value.
      public String getHashKey(String element) {
          try {
              MessageDigest md = MessageDigest.getInstance("MD5");
              md.update(element.getBytes());
              String hash = new BigInteger(1, md.digest()).toString(16);
              while(hash.length() < 32) hash = "0" + hash;
              return hash;
          } catch (NoSuchAlgorithmException e) {
```

`}`

```
          return  "0000000000000000000000000000000000000000000000000000000000000000";
```

`}`

```
  });
```

> Not e The LogPartitioner method is optional. If you do not configure this method, data is randomly written into a shard.

2. Run the following code and write the generated strings to Log Service.

```
// Serialize data into the format of raw log groups. class SimpleLogSerializer implements LogSerializationSchema<String> {
    public RawLogGroup serialize(String element) {
        RawLogGroup rlg = new RawLogGroup();
        RawLog rl = new RawLog();
        rl.setTime((int)(System.currentTimeMillis() / 1000));
        rl.addContent("message", element);
        rlg.addLog(rl);
        return rlg;
```

`}` `}`

```java
public class ProducerSample {
    public static String sEndpoint = "cn-hangzhou.log.aliyuncs.com";
    public static String sAccessKeyId = "";
    public static String sAccessKey = "";
    public static String sProject = "ali-cn-hangzhou-sls-admin";
    public static String sLogstore = "test-flink-producer";
    private static final Logger LOG = LoggerFactory.getLogger(ConsumerSample.class);
    public static void main(String[] args) throws Exception {
        final ParameterTool params = ParameterTool.fromArgs(args);
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(
```

);

```
        env.getConfig().setGlobalJobParameters(params);
        env.setParallelism(3);
        DataStream<String> simpleStringStream = env.addSource(new EventsGenerator());
        Properties configProps = new Properties();
        // Specify the endpoint of Log Service.
        configProps.put(ConfigConstants.LOG_ENDPOINT, sEndpoint);
        // Specify the AccessKey pair to access Log Service.
        configProps.put(ConfigConstants.LOG_ACCESSSKEYID, sAccessKeyId);
        configProps.put(ConfigConstants.LOG_ACCESSKEY, sAccessKey);
        // Specify the project to which logs are written.
        configProps.put(ConfigConstants.LOG_PROJECT, sProject);
        // Specify the Logstore to which logs are written.
        configProps.put(ConfigConstants.LOG_LOGSTORE, sLogstore);
        FlinkLogProducer<String> logProducer = new FlinkLogProducer<String>(new SimpleLogSerialize
r(), configProps);
        simpleStringStream.addSink(logProducer);
        env.execute("flink log producer");
```

`}`

```java
    // Simulate log generation.
    public static class EventsGenerator implements SourceFunction<String> {
        private boolean running = true;
        @Override
        public void run(SourceContext<String> ctx) throws Exception {
            long seq = 0;
            while (running) {
                Thread.sleep(10);
                ctx.collect((seq++) + "-" + RandomStringUtils.randomAlphabetic(12));
```

`}` `}`

```java
        @Override
        public void cancel() {
            running = false;
```

`}` `}` `}`

### 6.7 Use Logstash to consume log data

Log Service allows you to use SDKs developed in various languages and various stream computing systems to consume log data. In addition, Log Service allows you to use Logstash to consume log data. You can configure the Logstash input plug-in to read log data from Log Service and write the data to other systems, such as Kafka and Hadoop Distributed File System (HDFS). Features Dist ribut ed collaborat ive consumpt ion: Multiple servers can be configured to consume log data from a Logstore at the same time. High perf ormance: If you use consumer groups written in Java to consume log data, the consumption speed of a CPU core can reach up to 20 MB/s. High reliabilit y: Log Service saves the consumption progress. This mechanism enables automatic resumption of log consumption from the last checkpoint after a consumption exception is solved. Aut omat ic load balancing: Shards are automatically allocated based on the number of consumers in a consumer group. The shards are reallocated if consumers join or leave the consumer group.

### 6.8 Use Spark Streaming to consume log data

data This topic describes how to use Spark Streaming to consume log data. After logs are collected to Log Service, you can use the Spark SDK provided by Log Service to process log data in Spark Streaming. The Spark SDK supports two consumption modes: Receiver and Direct. The Maven dependency is as follows:

```xml
<dependency>
  <groupId>com.aliyun.emr</groupId>
  <artifactId>emr-logservice_2.11</artifactId>
  <version>1.7.2</version>
</dependency>
```

Receiver mode In the Receiver mode, a consumer group consumes data from Log Service and temporarily stores the data in Spark Executor. After a Spark Streaming job is started, it reads and processes data from Spark Executor. For more information, see Use consumer groups to consume log data. Each log entry is returned as a JSON string. The consumer group periodically saves checkpoints to Log Service. You do not need to update checkpoints. Example code

```java
import org.apache.spark.storage.StorageLevel import org.apache.spark.streaming.aliyun.logservice.LoghubUtils import org.apache.spark.streaming.{ Milliseconds, StreamingContext} import org.apache.spark.SparkConf object TestLoghub {
  def main(args: Array[String]): Unit = {
    if (args.length < 7) {
      System.err.println(
        """Usage: TestLoghub <project> <logstore> <loghub group name> <endpoint>
          |         <access key id> <access key secret> <batch interval seconds>
        """.stripMargin)
      System.exit(1)
```

`}`

```python
    val project = args(0)
    val logstore = args(1)
    val consumerGroup = args(2)
    val endpoint = args(3)
    val accessKeyId = args(4)
    val accessKeySecret = args(5)
    val batchInterval = Milliseconds(args(6).toInt * 1000)
    def functionToCreateContext(): StreamingContext = {
      val conf = new SparkConf().setAppName("Test Loghub")
      val ssc = new StreamingContext(conf, batchInterval)
      val loghubStream = LoghubUtils.createStream(
        ssc,
        project,
        logstore,
        consumerGroup,
        endpoint,
        accessKeyId,
        accessKeySecret,
        StorageLevel.MEMORY_AND_DISK)
      loghubStream.checkpoint(batchInterval * 2).foreachRDD(rdd =>
        rdd.map(bytes => new String(bytes)).top(10).foreach(println)
```

`)`

```
      ssc.checkpoint("hdfs:///tmp/spark/streaming") // set checkpoint directory
      ssc
```

`}`

```
    val ssc = StreamingContext.getOrCreate("hdfs:///tmp/spark/streaming", functionToCreateContext _
```

`)`

```
    ssc.start()
    ssc.awaitTermination()
```

`}` `}` Parameter description

| Parameter | Type | Description |
|---|---|---|
| project | String | The project in Log Service. |
| logstore | String | The Logstore in Log Service. |
| consumerGroup | String | The name of the consumer group. |
| endpoint | String | The endpoint of the region to which the project belongs. |

| Parameter | Type | Description |
|---|---|---|
| accessKeyId | String | The AccessKey ID used to access Log Service. |
| accessKeySecret | String | The AccessKey secret used to access Log Service. |

Notes In the Receiver mode, data loss may occur in some cases. To avoid data loss, you can turn on the Write-Ahead Logs switch, which is supported in Spark 1.2 and later versions. For more information, visit Spark Streaming Programming Guide. Direct mode In the Direct mode, no consumer group is required. API operations are called to request data from Log Service. Compared with the Receiver mode, the Direct mode has the following benefits: Simplified parallelism. The number of Spark partitions is the same as the number of shards in a Logstore. You can split shards to improve the parallelism of tasks. Increased efficiency. You no longer need to turn on the Write-Ahead Logs switch to prevent data loss. Exactly-once semantics. Data is read directly from Log Service. Checkpoints are submitted after the task is successful. In some cases, data may be repeatedly consumed if the task is not ended due to unexpected exit of Spark. You must configure the ZooKeeper service when you use the Direct mode. You must set a checkpoint directory in ZooKeeper to store intermediate state data. If you want to re-consume data after restarting a task, you must delete the directory from ZooKeeper and change the name of the consumer group. Example code

```java
import com.aliyun.openservices.loghub.client.config.LogHubCursorPosition import org.apache.spark.SparkConf import org.apache.spark.streaming.{ Milliseconds, StreamingContext} import org.apache.spark.streaming.aliyun.logservice.{ CanCommitOffsets, LoghubUtils} object TestDirectLoghub {
  def main(args: Array[String]): Unit = {
    if (args.length < 7) {
      System.err.println(
        """Usage: TestDirectLoghub <project> <logstore> <loghub group name> <endpoint>
          |         <access key id> <access key secret> <batch interval seconds> <zookeeper host:po
rt=localhost:2181>
        """.stripMargin)
      System.exit(1)
```

`}`

```python
    val project = args(0)
    val logstore = args(1)
    val consumerGroup = args(2)
    val endpoint = args(3)
    val accessKeyId = args(4)
    val accessKeySecret = args(5)
    val batchInterval = Milliseconds(args(6).toInt * 1000)
    val zkAddress = if (args.length >= 8) args(7) else "localhost:2181"
    def functionToCreateContext(): StreamingContext = {
      val conf = new SparkConf().setAppName("Test Direct Loghub")
      val ssc = new StreamingContext(conf, batchInterval)
      val zkParas = Map("zookeeper.connect" -> zkAddress,
        "enable.auto.commit" -> "false")
      val loghubStream = LoghubUtils.createDirectStream(
        ssc,
        project,
        logStore,
        consumerGroup,
        accessKeyId,
        accessKeySecret,
        endpoint,
        zkParas,
        LogHubCursorPosition.END_CURSOR)
      loghubStream.checkpoint(batchInterval).foreachRDD(rdd => {
        println(s"count by key: ${rdd.map(s => {
          s.sorted
          (s.length, s)
        }).countByKey().size}")
        loghubStream.asInstanceOf[CanCommitOffsets].commitAsync()
```

`})`

```
      ssc.checkpoint("hdfs:///tmp/spark/streaming") // set checkpoint directory
      ssc
```

`}`

```
    val ssc = StreamingContext.getOrCreate("hdfs:///tmp/spark/streaming", functionToCreateContext _
```

`)`

```
    ssc.start()
    ssc.awaitTermination()
```

`}` `}` Parameter description

| Parameter | Type | Description |
|---|---|---|
| project | String | The project in Log Service. |

| g Service |   | User Guide·Real-time consumptio |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| logstore | String | The Logstore in Log Service. |
| consumerGroup | String | The name of the consumer group (only used to save consumption checkpoints). |
| endpoint | String | The endpoint of the region to which the project belongs. |
| accessKeyId | String | The AccessKey ID used to access Log Service. |
| accessKeySecret | String | The AccessKey secret used to access Log Service. |
| zkAddress | String | The endpoint of ZooKeeper. |

Parameter settings In the Direct mode, you must specify the number of log entries that are consumed in each shard in each batch. Otherwise, the data reading process cannot be ended. You can throttle the transmission rate of a single batch by setting the two parameters listed in the following table.

| Parameter | Description | Default value |
|---|---|---|
| spark.loghub.batchGet.step | The number of log groups returned for a single request. | 100 |
| spark.streaming.loghub.maxRatePer Shard | The maximum number of log entries that are read in a shard. | 10,000 |

The number of log entries processed in each batch is calculated as follows: `number of shards x max(spark.log`

```
hub.batchGet.step x n x number of log entries in a log group, spark.streaming.loghub.maxRatePerShard x duration) .
```

n: the number of requests required to increase the returned rows to `spark.streaming.loghub.maxRatePerSha`

```
rd x duration .
```

duration: the interval between batch processing. Unit: milliseconds. If you need to combine multiple data streams, the number of shards refers to the total number of shards in all Logstores. Example For example, the number of shards is 100. Each log group contains 50 log entries. Batches are processed at an interval of two seconds. If you want to process 20,000 log entries in each batch, use the following configurations:

| spark.loghub.batchGet.step: 4 |   |
|---|---|
| spark.streaming.loghub.maxRatePerShard: 100 |   |

If each log group contains 60 log entries and you want to process 20,000 log entries in each batch, 24,000 log entries will be processed based on the preceding configurations ( `60 x 4 x 100 = 24,000` ). Accurate transmission rate throttling A smaller `spark.loghub.batchGet.step` value increases the accuracy of throttling and the number of requests. We recommend that you count the average number of log entries contained in a log group and then set the preceding two parameters.

### 6.9 Use Realtime Compute to consume log data

log data You can use Realtime Compute (Blink) to create a schema for Log Service data and consume the data. Log Service stores streaming data. Therefore, Realtime Compute can use the streaming data as input data. In Log Service, each log entry contains multiple fields and each field is a key-value pair. The following example is a sample log entry:

```
__source__: 11.85.123.199 __tag__:__receive_time__: 1562125591 __topic__: test-topic a: 1234 b: 0 c: hello
```

You can use the following data definition language (DDL) statement to create a table in Realtime Compute:

```
create table sls_stream(
  a int,
  b int,
  c varchar
) with (
  type ='sls',
  endPoint ='<your endpoint>',
  accessId ='<your access key id>',
  accessKey ='<your access key>',
  startTime = '2017-07-05 00:00:00',
  project ='ali-cloud-streamtest',
  logStore ='stream-test',
  consumerGroup ='consumerGroupTest1'
```

); Attribute fields Realtime Compute can extract fields from log content. In addition, Realtime Compute can extract three attribute fields and custom tag fields, such as `__receive_time__` . The following table lists the three attribute fields. Attribute fields

| Field name | Description |
|---|---|
| source __ __ | The source of the log entry. |
| topic __ __ | The topic of the log entry. |
| timestamp __ __ | The time when the log entry is generated. |

To extract the preceding fields, you must add HEADERs in the DDL statement. For example:

```
create table sls_stream(
  __timestamp__ bigint HEADER,
  __receive_time__ bigint HEADER
  b int,
  c varchar
) with (
  type ='sls',
  endPoint ='<your endpoint>',
  accessId ='<your access key id>',
  accessKey ='<your access key>',
  startTime = '2017-07-05 00:00:00',
  project ='ali-cloud-streamtest',
  logStore ='stream-test',
  consumerGroup ='consumerGroupTest1'
```

); Parameters in the WITH clause The following table describes the parameters in the WITH clause.

| Parameter | Required | Description |
|---|---|---|
| endPoint | Yes | The endpoint of Log Service. |
| accessId | Yes | The AccessKey ID of the Apsara Stack tenant account or RAM user that is used to access Log Service. |
| accessKey | Yes | The AccessKey secret of the Apsara Stack tenant account or RAM user that is used to access Log Service. |
| project | Yes | The name of the project in Log Service. |
| logStore | Yes | The name of the Logstore in Log Service. |
| consumerGroup | No | The name of the consumer group. |
| startTime | No | The time when Realtime Compute starts to consume data. |
| heartBeatIntervalMills | No | The heartbeat interval of the client that consumes log data. Unit: seconds. Default value: 10. |
| maxRetryTimes | No | The maximum number of retries to read data. Default value: 5. |
| batchGetSize | No | The number of log groups that are read at a time. Default value: 10. If the version of Blink is 1.4.2 or later, the default value is 100 and the maximum value is 1000. |

| Parameter | Required | Description |
|---|---|---|
| columnErrorDebug | No | Specifies whether to enable debugging. If debugging is enabled, log entries that fail to be parsed are displayed. Default value: false . |

Field type mapping All log fields in Log Service are of the string type. The following table lists the mapping between the type of Log Service fields and the type of Realtime Compute fields. We recommend that you declare the mapping in a data definition language (DDL) statement.

| Data type of Log Service | Data type of Realtime Compute |
|---|---|
| STRING | VARCHAR |

If you specify another data type to convert Log Service data, an automatic conversion attempt is performed. For example, you can specify BIGINT as the data type to convert the string "1000" and specify timestamp as the data type to convert the string "2018-01-12 12:00:00".

> Not e
> Blink versions earlier than 2.2.0 do not support shard scaling. If you split or merge shards when a job is reading data from a Logstore, the job fails and cannot continue. In this case, you must restart the job.
> No versions of Blink allow you to delete or recreate a Logstore whose log data is being consumed.
> For Blink version 1.6.0 and earlier, if you specify consumerGroup to consume log data from a Logstore that contains a large number of shards, the read performance may be affected.
> When you create a schema, Log Service data cannot be converted to data of the map type.
> Fields whose values are empty are set to null.
> Unordered field conversions are supported. However, we recommend that you convert the fields in the same order as the fields in the schema.
> The batchGetSize parameter specifies the number of log groups that are obtained based on the logGro up parameter. If the size of each log entry and the value of the batchGetSize parameter are both large, garbage collection (GC) of data in the memory may frequently occur.

Precautions If no new data is written to a shard, the overall latency of a job increases. In this case, you need to modify the number of concurrent tasks in the job to the number of shards from which data is read and written. We recommend that you set the number of concurrent tasks in a job to the same as the number of shards. Otherwise, data may be filtered out when the job reads historical data from two shards at significantly different speeds. To extract fields in tags such as `__tag__:__hostname__` and `__tag__:__path__` , you can delete the __tag__: prefix and use the method of extracting attribute fields.

> Not e This type of data cannot be extracted during debugging. We recommend that you use the local debugging method and the print method to display data in logs.

## 7 Data shipping

### 7.1 Ship logs to OSS

#### 7.1.1 Overview

Log Service provides the data shipping feature. You can use this feature to ship logs to Object Storage Service (OSS) in real time by using the Log Service console. This topic describes the benefits and scenarios of the data shipping feature. In the Log Service console, you can ship logs to other Apsara Stack services. Then, you can store or consume the log data by using other systems such as E-MapReduce. After you enable the log shipping feature, Log Service ships the collected logs to the specified cloud service at regular intervals. Scenarios The data shipping feature can be used to connect Log Service with data warehouses. Benefits The data shipping feature of Log Service has the following benefits: Ease of use You only need to complete a few settings in the Log Service console before you can ship logs from Logstores to other Apsara Stack services such as OSS. High efficiency Log Service stores logs that are collected from multiple servers. This improves efficiency when you ship log data to Apsara Stack services such as OSS. Effective management You can ship logs from different projects or Logstores to different OSS buckets. This way, you can efficiently manage the logs by log type or log source. Log shipping destinations For information about how to ship logs to OSS, see Ship log data from Log Service to OSS.

#### 7.1.2 Ship log data from Log Service to OSS

You can use Log Service to collect log data and ship the log data to Object Storage Service (OSS) for storage and analysis. This topic describes how to ship log data from Log Service to OSS. Prerequisites Log data is collected. For more information, see Log collection methods. OSS is activated. A bucket is created in the region where the Log Service project resides. For more information, see the Creat e bucket s section in the Service User Guide -Ojbect Storage Service(OSS). A Resource Access Management (RAM) role is created for the level-1 organization. For more information, see Obtain the ARN of a RAM role. Context Log Service can automatically ship log data from a Logstore to an OSS bucket. You can set a custom retention period for the log data in the OSS bucket. Permanent retention is supported. You can use data processing platforms such as E-MapReduce and Data Lake Analytics (DLA) or use custom programs to consume log data from the OSS bucket.
1. Log on to the Log Service console.
2. In the Projects section, click the project from which you want to ship log data to OSS.
3. On the Logstores tab, click the > icon on the left of the specific Logstore and choose Dat a T ransf ormat ion
> Export > Object St orage Service(OSS).

4. On the OSS Shipper page, click Enable.
5. In the OSS LogShipper pane, configure the shipping rules.
The following table describes the required parameters.

| Parameter | Description |
|---|---|
| OSS Shipper Name | The name of the shipping rule. The name can contain only lowercase letters, digits, hyphens (-), and underscores ( ). The name must start and end with a lowercase letter or digit and must be 2 _ to 128 characters in length. |
| OSS Bucket | The name of the OSS bucket to which you want to ship log data. Not ice You must specify the name of an existing OSS bucket. The specified OSS bucket must reside in the same region as the Log Service project. |
| OSS Prefix | The directory to which log data is shipped in the OSS bucket. |
| Partition format | The partition format of the bucket directory for the shipping task. The directory is automatically generated based on the time when the shipping task is created. The default format is %Y/%m/%d/%H/%M. The partition format cannot start with a forward slash (/). For information about partition format examples, see Partition format. For more information about parameters, see strptime API. |
| (Resource Access Management) RAM Role | The Alibaba Cloud Resource Name (ARN) of the RAM role. The RAM role is the identity that the OSS bucket owner creates for access control. Example: acs:ram::45643:role/aliyunlogdefaultrole. For information about how to obtain the ARN, see Obtain the ARN of a RAM role. |
| Shipping Size | The maximum size of raw log data that can be shipped to the OSS bucket in a shipping task. Valid values: 5 to 256. Unit: MB. If the size of shipped data exceeds the specified value, a new shipping task is automatically created. |
| Compress | Specifies whether to compress log data that is shipped to OSS. Valid values: No Compress: The log data that is shipped to OSS is not compressed. Compress (snappy): The snappy utility is used to compress the log data that is shipped to OSS. This way, the log data occupies less storage space of the OSS bucket. |
| Storage Format | The storage format of the log data that is shipped to OSS. Valid values: JSON, CSV, and Parquet. For more information, see Storage Formats. |
| Ship Tags | Specifies whether to ship log tags. |

| Parameter | Description |
|---|---|
| Shipping Time | The time period during which a shipping task runs. Valid values: 300 to 900. Default value: 300. Unit: seconds. If the specified time period expires, another shipping task is created. |

6. Click OK.

> Not e
> After you configure a shipping rule, multiple shipping tasks can concurrently run. If the size of the data shipped from a shard reaches the specified threshold or the specified time period expires, another task is created.
> After you create a shipping task, you can check whether the shipping rule satisfies your business requirements based on the task status and the data shipped to OSS.

View OSS data After log data is shipped to OSS, you can access the log data in the OSS console, or by using the OSS API, an SDK, or another method. For more information, see the Object s > Search f or object s section of the Service User Guide -Ojbect Storage Service(OSS). The following script shows a sample OSS directory:

```
oss://OSS-BUCKET/OSS-PREFIX/PARTITION-FORMAT_RANDOM-ID
```

OSS-BUCKET is the name of the OSS bucket. OSS-PREFIX is the prefix of the directory in the OSS bucket. PARTITION- FORMAT is the partition format of the directory for a shipping task. The partition format is calculated based on the time when the shipping task is created. For more information, see strptime API. RANDOM-ID is the unique identifier of the shipping task.

> Not e The directory in the OSS bucket is created based on the time when the shipping task is created. For example, the shipping task is created at 00:00:00 on June 23, 2016 to ship data to OSS. The data is written to Log Service after 23:55:00 on June 22, 2016. The shipping interval is 5 minutes. To retrieve all logs shipped on June 22, 2016, you must check all objects in the 2016/06/22 directory. You must also check the 2016/06/23/00/ directory for the objects that are generated in the first 10 minutes of June 23, 2020.

Partition format For each shipping task, log data is written to a directory of an OSS bucket. The directory is in the oss://OSS- BUCKET/OSS-PREFIX/PARTITION-FORMAT_RANDOM-ID format. A partition format is obtained by formatting the time when a shipping task is created. The following table describes the partition formats and directories that are obtained when a shipping task is created at 19:50:43 on January 20, 2017.

| OSS Bucket | OSS Prefix | Partition format | OSS directory |
|---|---|---|---|
| test-bucket | test-table | %Y/%m/%d/%H/%M | oss://test-bucket/test- table/2017/01/20/19/501484 _ 9130433515253512850008 _ |
| test-bucket | log ship oss example _ _ _ | year=%Y/mon=%m/day=%d/lo g %H%M%s _ | oss://test- bucket/logshipossexample/ _ _ _ year=2017/mon=01/day=20/lo g19504314849130433515253 _ _ 512850008.parquet _ |

|   | User Guide·Data | shipping |   | Log Servic | e |
|---|---|---|---|---|---|

| OSS Bucket | OSS Prefix | Partition format | OSS directory |
|---|---|---|---|
| test-bucket | log ship oss example _ _ _ | ds=%Y%m%d/%H | oss://test- bucket/logshipossexample/ _ _ _ ds=20170120/1914849130433 _ 515253512850008.snappy _ |
| test-bucket | log ship oss example _ _ _ | %Y%m%d/ | oss://test- bucket/logshipossexample/ _ _ _ 20170120/1484913043351525 _ 3512850008 _ Not e This format may prevent platforms such as Hive from parsing the log data in the OSS bucket. We recommend that you do not use this format. |
| test-bucket | log ship oss example _ _ _ | %Y%m%d%H | oss://test- bucket/logshipossexample/ _ _ _ 2017012019148491304335152 _ 53512850008 _ |

You can use Hive, MaxCompute, or Data Lake Analytics (DLA) to analyze OSS data. In this case, if you want to use partition information, you can set PARTITION-FORMAT in the key=value format. For example, you can set the partition format to oss://testbucket/log_ship_oss_example/year=2017/mon=01/day=20/log_195043_1484913043351525351_2850008.parquet. In this example, year, mon, and day are specified as three partition keys. What to do next After shipping tasks are created based on a shipping rule, you can modify the shipping rule. You can also disable the data shipping feature, view the statuses and error messages of the tasks, and retry failed tasks on the OSS Shipper page of a Logstore. Modify the shipping rule. Click Set t ings to modify the shipping rule. For information about the parameters, see Procedure. Disable the data shipping feature. Click Disable. The data in the Logstore is no longer shipped to OSS. View the statuses and error messages of the tasks. You can view the log shipping tasks of the last two days and their statuses. Statuses of a shipping task

| Status | Equivalent |
|---|---|
| Succeeded | The shipping task has succeeded. |
| Running | The shipping task is running. Check whether the task succeeds later. |
| Failed | The shipping task has failed. If the task cannot be restarted due to external causes, troubleshoot the failure based on the error message and retry the task. |

Error messages If a shipping task fails, an error message is returned for the task.

| Error message | Error cause | Solution |
|---|---|---|
| UnAuthorized | The error message returned because the AliyunLogDefaultRole role does not have the required permissions. | To fix the error, check the following configurations: Check whether the AliyunLogDefaultRole role is created by the OSS bucket owner. Check whether the specified ID of the Alibaba Cloud account in the permission policy is valid. Check whether the AliyunLogDefaultRole role is granted the write permissions on the OSS bucket. Check whether the ARN of the AliyunLogDefaultRole role that you entered in the RAM Role field is valid. |
| ConfigNotExist | The error message returned because the task does not exist. | Check whether the data shipping feature is disabled. If the feature is disabled, enable the feature, configure a shipping rule, and then retry the shipping task. |
| InvalidOssBucket | The error message returned because the specified OSS bucket does not exist. | To fix the error, check the following configurations: Check whether the OSS bucket resides in the same region as the Log Service project. Check whether the specified bucket name is valid. |
| InternalServerError | The error message returned because an internal error has occurred in Log Service. | Retry the failed shipping task. |

Retry a shipping task By default, if a shipping task fails, Log Service retries the task based on the retry policy. You can also manually retry the task. By default, Log Service retries all tasks of the last two days. The minimum interval between two consecutive retries is 15 minutes. If a task fails for the first time, Log Service retries the task 15 minutes later. If the task fails for the second time, Log Service retries the task 30 minutes later. If the task fails for the third time, Log Service retries the task 60 minutes later. A similar method is used for subsequent attempts. To immediately retry a failed task, you can click Ret ry All Failed T asks or Ret ry on the right of the task. You can also use the Log Service API or an SDK to retry a task.

#### 7.1.3 Obtain the ARN of a RAM role

When you use a RAM user to ship data from Log Service to Object Storage Service (OSS), you must first create a Resource Access Management (RAM) role and specify the ARN of the RAM role. This topic describes how to create a RAM role and obtain the ARN of a RAM role.
1. Log on to the Log Service console.
2. In the top navigation bar, click Conf igurat ions.
3. On the Service-Linked Roles page, click Creat e RAM Role.
4. In the Organizat ion Name drop-down list, select the organization that you created. In the Service Name
drop-down list, select Log Service, and click OK.
5. On the RAM Service Role page, enter `AliyunLogDefaultRole` in the Role Name search box and click
Search.
6. Obtain the ARN of the RAM role.
In the search results, the value in the role ident if ier column is the ARN of the RAM role.

#### 7.1.4 Storage Formats

Different storage formats are supported when Log Service ships logs to OSS, including JSON, CSV, and Parquet. This topic describes the field details of the formats. JSON format You can set the storage format for the data that is shipped to OSS. The following table shows how to set the st orage f ormat to JSON. For more information, see Configure a data shipping rule.

| Compression type | File extension | Example file address | Description |
|---|---|---|---|
| Uncompressed | N/A | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20/5 _ 4 1453812893059571256 937 _ _ | You can download the raw JSON object to the local host and open each object as a text file. The following example is the content of a sample file: {" time ":1453809242," to __ __ __ pic ":""," source ":"10.1 __ __ __ 70.***.***","ip":"10.200.**. ***","time":"26/Jan/2016:19: 54:02 +0800","url":"POST /PutData? Category=YunOsAccountOpLog&A ccessKeyId= <yourAccessKeyId>&Date=Fri%2 C%2028%20Jun%202013%2006%3A5 3%3A30%20GMT&Topic=raw&Signa ture=<yourSignature> HTTP/1.1","status":"200","us er-agent":"aliyun-sdk-java"} |
| snappy | .snappy | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20/5 _ 4 1453812893059571256 937.snappy _ _ | JSON objects are compressed by using Snappy. For more information, see Decompression tools for Snappy- compressed files. |

CSV-format You can set the storage format for the data that is shipped to OSS. The following table shows how to set the st orage f ormat to CSV. For more information, see Configure a data shipping rule. The following table describes the parameters. For more information, see Common Format and MIME Type for Comma-Separated Values (CSV) Files and PostgreSQL 9.4.26 Documentation.

| Parameter | Description |
|---|---|
| CSV Fields | The names of the log fields that you want to ship to OSS. You can view log fields on the Raw Logs tab of a Logstore and enter the names of the fields that you want to ship to OSS in the Key Name column. The log fields that you can ship to OSS include the fields in the log content and the reserved fields such as time , topic , and __ __ __ __ source . __ __ Not e The keys that you enter in the CSV Fields section must be unique. |
| Delimiter | You can use commas (,), vertical bars (\|), spaces, or tabs to delimit fields. |
| Escape Character | If a field contains a delimiter, you must use an escape character to enclose the field. This ensures that the field is not delimited. |
| Invalid Fields | If a key that you specify in the CSV Fields section does not exist, enter the value of the key in the Invalid Fields field. |
| Shipped Fields | If you turn on the Shipped Fields switch, field names are written in a CSV file. |

The following table lists the directories in OSS buckets that store the data shipped from Log Service.

| Compression type | File extension | Example | Description |
|---|---|---|---|
| No | .csv | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20 _ /54 1453812893059571256 937.cs _ _ v | You can download the raw JSON object to the local host and open the object as a text file. |
| snappy | .snappy.csv | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20 _ /54 1453812893059571256 937.sn _ _ appy.csv | Decompression tools for Snappy compressed files For more information, see Decompression tools for Snappy-compressed files. |

Parquet-format You can set the storage format for the data that is shipped to OSS. The following figure shows how to set the st orage f ormat to Parquet . For more information, see Configure a data shipping rule. The following table describes the related parameters.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Key Name | The name of the log field that you want to ship to OSS. You can view log fields on the Raw Logs tab of a Logstore. You can also enter the names of the fields that you want to ship to OSS in the Key Name column. When the fields are shipped to OSS, they are stored in the Parquet format in the order that the field names are entered. The names of the fields are the column names in OSS. The log fields that you can ship to OSS include the fields in the log content and the reserved fields such as time , topic , and source . The value of a __ __ _ __ __ __ field in the Parquet format is null in the following two scenarios: The field does not exist in logs. The value of the field fails to be converted from the string type to a non- string type, for example, double or Int64. Not e The keys that you enter in the Parquet Keys field must be unique. |
| Type | The Parquet storage format supports six data types: string, Boolean, Int32, Int64, float, and double. Log fields are converted from the string type to a data type that the Parquet storage format supports. If the data type of a log field fails to be converted, the value of the log field is null. |

The following table lists the directories in OSS buckets that store data shipped from Log Service.

| Compression type | File extension | Example | Description |
|---|---|---|---|
| Uncompressed | .parquet | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20 _ /54 1453812893059571256 937.pa _ _ rquet | You can download the OSS buckets to the local host and use the parquet-tools utility to open the objects. For more information about the parquet-tools utility, visit parquet-tools. |
| Snappy | .snappy.parquet | oss://oss-shipper- shenzhen/ecs test/2016/01/26/20 _ /54 1453812893059571256 937.sn _ _ appy.parquet | You can download the OSS buckets to the local host and use the parquet-tools utility to open the objects. For more information about the parquet-tools utility, visit parquet-tools. |

#### 7.1.5 Decompress Snappy compressed files

When you ship data from Log Service to Object Storage Service (OSS), you can use Snappy to compress OSS objects. After the data is shipped to OSS, you can decompress OSS objects by using the C++ library, Java library, Python library, and decompression tool for Linux. Use the C++ library to decompress OSS objects Download the C++ library from the snappy page and use the Snappy.Uncompress method to decompress Snappy compressed OSS objects. Use the Java library to decompress OSS objects Download the Java library from the xerial snappy-java page and use the Snappy.Uncompress or Snappy.SnappyInputStream method to decompress Snappy compressed OSS objects. The SnappyFramedInputStream method is not supported.

> Not e If you use Java Library 1.1.2.1, some Snappy compressed OSS objects may fail to be decompressed. For more information, see Bad handling of the MAGIC HEADER. To fix this issue, you can use Java Library 1.1.2.6 or later.

```xml
<dependency> <groupId>org.xerial.snappy</groupId> <artifactId>snappy-java</artifactId> <version>1.0.4.1</version> <type>jar</type> <scope>compile</scope> </dependency>
```

Snappy.Uncompress

```java
String fileName = "C:\\Downloads\\36_1474212963188600684_4451886.snappy"; RandomAccessFile randomFile = new RandomAccessFile(fileName, "r"); int fileLength = (int) randomFile.length(); randomFile.seek(0); byte[] bytes = new byte[fileLength]; int byteread = randomFile.read(bytes); System.out.println(fileLength); System.out.println(byteread); byte[] uncompressed = Snappy.uncompress(bytes); String result = new String(uncompressed, "UTF-8"); System.out.println(result);
```

Snappy.SnappyInputStream

```java
String fileName = "C:\\Downloads\\36_1474212963188600684_4451886.snappy"; SnappyInputStream sis = new SnappyInputStream(new FileInputStream(fileName)); byte[] buffer = new byte[4096]; int len = 0; while ((len = sis.read(buffer)) != -1) {
    System.out.println(new String(buffer, 0, len));
```

`}` Use the Python Library to decompress OSS objects
1. Download and install the Python library.
2. Run the decompression script.
The following example is a sample decompression script:

```java
import snappy compressed = open('/tmp/temp.snappy').read() snappy.uncompress(compressed)
```

> Not e The following two commands cannot be used to decompress Snappy compressed OSS objects. These commands can be used only in Hadoop mode (hadoop_stream_decompress) or streaming mode (stream_decompress).

```
python -m snappy -c uncompressed_file compressed_file.snappy python -m snappy -d compressed_file.snappy uncompressed_file
```

Use decompression tools for Linux to decompress OSS buckets Log Service allows you to decompress Snappy compressed files by using the decompression tool for Linux. Click snappy_tool to download the tool. Replace 03_1453457006548078722_44148.snappy and 03_1453457006548078722_44148 in the following code with the values specific to your environment and then run the following code:

```
./snappy_tool 03_1453457006548078722_44148.snappy 03_1453457006548078722_44148 compressed.size: 2217186 snappy::Uncompress return: 1 uncompressed.size: 25223660
```

## 8 RAM

### 8.1 Overview

Resource Access Management (RAM) is a resource access control service provided by Apsara Stack. You can use RAM to manage users, including employees, systems, and applications. You can also use RAM to grant users permissions to access resources. RAM provides the following features: RAM Role To authorize a cloud service in a level-1 organization to use other resources in the organization, you must create a RAM role. This role specifies the operations that the cloud service can perform on the resources. Only system administrators and level-1 organization administrators can create RAM roles. User group You can create multiple RAM users for an organization and grant the users different permissions on the same cloud resources in the organization. You can create RAM user groups to classify and authorize RAM users within your Apsara Stack tenant account. This simplifies the management of RAM users and their permissions. You can create RAM policies to grant permissions to different user groups.

### 8.2 Create a RAM role

To authorize a cloud service in a level-1 organization to use other resources in the organization, you must create a RAM role. This role specifies the operations that the cloud service can perform on the resources.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
For more information, see Log on to the Log Service console.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Roles.
4. In the upper-right corner of the page, click Creat e RAM Role.
5. On the Roles - Creat e RAM Role page that appears, set the Role Name and Descript ion parameters.
6. Click Creat e.

### 8.3 Create a user

This topic describes how an administrator creates a user and assigns a role to the user. The role varies based on the cloud resources that the user needs to access. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Users.
4. On the Users page, click Creat e.
5. In the dialog box that appears, set the parameters based on your requirements.

| Parameter | Description |
|---|---|
| Username | The username. |
| Display Name | The display name of the user. |
| Roles | The role that you want to assign to the user. |
| Organizat ion | The organization to which the user belongs. |
| Logon Policy | The logon policy that restricts the logon time and IP address of the user. If you do not specify this parameter, the default policy is attached to the created user. |
| Mobile Number | The mobile phone number of the user. If you need to send text messages about the usage and requests for resources to the mobile phone number, make sure that the specified mobile phone number is correct. |
| Landline Number | Optional. The landline number of the user. |
| Email | The email address of the user. If you need to send emails about the usage and requests for resources to the email address, make sure that the specified email address is correct. |
| DingT alk Key | Optional. The DingTalk key. |
| Not if y User by SMS | Specifies whether to send text messages about the usage and requests for resources to the specified mobile phone number. |
| Not if y User by Email | Specifies whether to send emails about the usage and requests for resources to the specified email address. |
| Not if y User by DingT alk | Specifies whether to send messages about the usage and requests for resources to the specified DingTalk user. |

6. Click OK.

### 8.4 Create a RAM user group

This topic describes how to create a RAM user group in an organization and grant permissions to RAM users in the RAM user group. Prerequisites An organization is created. Context The relationships between RAM user groups and RAM users: A RAM user group can contain zero or more RAM users. A RAM user does not need to belong to a RAM user group. You can add a RAM user to multiple RAM user groups. The relationships between RAM user groups and organizations: A RAM user group belongs to only one organization. You can create multiple RAM user groups in an organization. The relationships between RAM user groups and RAM roles: Only one RAM role can be assigned to each RAM user group. A RAM role can be assigned to multiple RAM user groups. When a RAM role is assigned to a RAM user group, the permissions that the RAM role has are automatically granted to RAM users in the RAM user group. The relationships between RAM user groups and resource sets: You can add zero or more user groups to a resource set. A user group can be added to multiple resource sets. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click User Groups.
4. In the upper-right corner of the page, click Creat e User Group.
5. In the dialog box that appears, set the User Group Name and Organizat ion parameters.
6. Click OK.

### 8.5 Add a RAM user to a RAM user group

This topic describes how to add a RAM user to a RAM user group. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click User Groups.
4. Find the user group to which you want to add a RAM user, and click Add User in the Act ions column.
5. In the dialog box that appears, select a RAM user from the left pane, and click the right arrow to move the
RAM user to the right pane.
6. Click OK.

### 8.6 Create a permission policy

If you want to use a cloud service to access the resources of other cloud services, you must create a permission policy for a RAM role. Then, the policy is automatically attached to the RAM user group to which the RAM role is assigned. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Roles.
4. In the list of role names, find the RAM role for which you want to create a permission policy and choose More
> Modif y.

5. Click Permissions.
6. Click Add Permission Policy.
7. In the Add Permission Policy dialog box, enter the policy information.
For more information about how to specify the policy information, see Use custom policies to grant RAM user the required permissions.

### 8.7 Grant a RAM user the permissions to manage a project

manage a project This topic describes how to grant a Resource Access Management (RAM) user the permissions to manage a specified project. Prerequisites A RAM user is created. For more information, see Create a user. A resource set is created and the RAM user is added to the resource set. For more information, see Ent erprise Cent er > Resource Set s in Apsara Uni-manager Management Console User Guide. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Dat a Permissions.
4. Click the resource set that you want to manage, for example, ResourceSet(appstreaming).
5. In the Product T ype section, click Log Service.
6. Find the instance that you want to manage and click Aut horize in the Actions column.
In this example, the instance is a Log Service project whose name is test-project.
7. Grant the RAM user the permissions to manage the project.
If you turn on the Action switch of the Updat e Project permission, the RAM user can modify the project that is selected in Step .

### 8.8 Grant permissions to a RAM role

This topic describes how to grant permissions to a RAM role. After a RAM role is granted permissions, the RAM users in the associated RAM user group inherit the permissions. 1.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Roles.
4.
5. On the Permissions tab, click Select Exist ing Permission Policy.
6. In the Select Exist ing Permission Policy dialog box, select a permission policy and click OK.
If no policies are available, create a policy. For more information, see Create a permission policy.

### 8.9 Use custom policies to grant RAM user the required permissions

the required permissions This topic describes how to use custom Resource Access Management (RAM) policies to grant RAM users the required permissions. You can grant permissions to the RAM users under your Apsara Stack tenant account. Context For data security, we recommend that you follow the principle of least privilege (PoLP) when you grant permissions to RAM users. You must grant the read-only permission on the project list to RAM users. Otherwise, the RAM users cannot view the projects in the project list. Use the RAM console to grant permissions to a RAM user The read-only permission on projects For example, you can use your Apsara Stack tenant account to grant RAM users the following permissions: The permission to view the list of projects that belong to the Apsara Stack tenant account The permission to read specific projects Use the following policy: `{`

```json
   "Version": "1",
   "Statement": [
```

`{`

```json
       "Action": ["log:ListProject"],
       "Resource": ["acs:log:*:*:project/*"],
       "Effect": "Alow"
```

`},` `{`

```json
       "Action": [
         "log:Get*",
         "log:List*"
```

`],`

```json
       "Resource": "acs:log:*:*:project/<The name of the project>/*",
       "Effect": "Allow"
```

`}` `]` `}` The permission to read a Logstore, save searches, and use saved searches. For example, you can use your Apsara Stack tenant account to grant RAM users the following permissions: The permission to view the project list of the Apsara Stack tenant account The permission to read a Logstore, save searches, and use saved searches Use the following policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "log:ListProject"
```

`],`

```json
      "Resource": "acs:log:*:*:project/*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:List*"
```

`],`

```json
      "Resource": "acs:log:*:*:project/<The name of the project>/logstore/*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:Get*",
        "log:List*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/logstore/<The name of the Logstore>"
```

`],`

```json
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:List*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/dashboard",
        "acs:log:*:*:project/<The name of the project>/dashboard/*"
```

`],`

```json
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:Get*",
        "log:List*",
        "log:Create*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/savedsearch",
        "acs:log:*:*:project/<The name of the project>/savedsearch/*"
```

`],`

```json
      "Effect": "Allow"
```

`}` `]` `}`

> Not e In the policy, a value of the Resource attribute that does not end with an asterisk (*) indicates the exact resource. A value that ends with an asterisk (*) indicates all resources that match the value.

The permission to read a Logstore and view all saved searches and dashboards in a project For example, you can use your Apsara Stack tenant account to grant a RAM user the following permissions: The permission to view the project list of the Apsara Stack tenant account The permission to read a Logstore and view all saved searches and dashboards in a project Use the following policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "log:ListProject"
```

`],`

```json
      "Resource": "acs:log:*:*:project/*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:List*"
```

`],`

```json
      "Resource": "acs:log:*:*:project/<The name of the project>/logstore/*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:Get*",
        "log:List*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/logstore/<The name of the Logstore>"
```

`],`

```json
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:Get*",
        "log:List*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/dashboard",
        "acs:log:*:*:project/<The name of the project>/dashboard/*"
```

`],`

```json
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "log:Get*",
        "log:List*"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/savedsearch",
        "acs:log:*:*:project/<The name of the project>/savedsearch/*"
```

`],`

```json
      "Effect": "Allow"
```

`}` `]` `}` Grant RAM users the permissions that are required to call Log Service operations The permission to write data to a project To grant RAM users only the permission to write data to a project, use the following policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "log:Post*"
```

`],`

```json
      "Resource": "acs:log:*:*:project/<The name of the project>/*",
      "Effect": "Allow"
```

`}` `]` `}` The permission to consume data of a project To grant RAM users only the permission to consume data of a project, use the following policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "log:ListShards",
        "log:GetCursorOrData",
        "log:GetConsumerGroupCheckPoint",
        "log:UpdateConsumerGroup",
        "log:ConsumerGroupHeartBeat",
        "log:ConsumerGroupUpdateCheckPoint",
        "log:ListConsumerGroup",
        "log:CreateConsumerGroup"
```

`],`

```json
      "Resource": "acs:log:*:*:project/<The name of the project>/*",
      "Effect": "Allow"
```

`}` `]` `}` The permission to consume data of a Logstore To grant RAM users only the permission to consume data of a Logstore, use the following policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "log:ListShards",
        "log:GetCursorOrData",
        "log:GetConsumerGroupCheckPoint",
        "log:UpdateConsumerGroup",
        "log:ConsumerGroupHeartBeat",
        "log:ConsumerGroupUpdateCheckPoint",
        "log:ListConsumerGroup",
        "log:CreateConsumerGroup"
```

`],`

```json
      "Resource": [
        "acs:log:*:*:project/<The name of the project>/logstore/<The name of the Logstore>",
        "acs:log:*:*:project/<the name of the project>/logstore/<the name of the Logstore>/*"
```

`],`

```json
      "Effect": "Allow"
```

`}` `]` `}`

## 9 FAQ

### 9.1 Log collection

#### 9.1.1 How do I troubleshoot Logtail collection errors?

If the Logtail preview page is blank or "No Data" is displayed on the query page, perform the following steps:
1. Check whether Log Service receives heartbeats from the server group.
You can view the Logtail heartbeat status in the Log Service console. For more information, see View the status of a server group. If the heartbeat status is OK, go to the next step. If the heartbeat status is FAIL, proceed with further troubleshooting. For more information, see What can I do if no heartbeat packet is received from a Logtail client?.
2. Check whether the Logtail configuration is created.
If the heartbeat status of Logtail is OK, check whether the Logtail configuration is created. Make sure that the path and name of monitored logs match the files that are stored on the server. The path can be a full path or a path that includes wildcards.
3. Make sure that the Logtail configuration is applied to the server group.
Check whether the target Logtail configuration is applied to the server group. For more information, see Manage server group configurations.
4. Check collection errors.
If Logtail is configured correctly, check whether new logs are generated in real time. Logtail only collects incremental log data. Logtail does not read log files in which no log is generated. If a log file is updated but the updates cannot be queried in Log Service, you can diagnose the problem as follows: View logs of the Logtail client The client logs include key INFO logs, all WARNING logs, and all ERROR logs. To view complete error information in real time, check the following client logs: Linux: /usr/local/ilogtail/ilogtail.LOG. Linux: /usr/local/ilogtail/logtail_plugin.LOG. The file contains the logs such as HTTP logs, MySQL binary logs, and MySQL query results. 64-bit Windows: C:\Program Files (x86)\Alibaba\Logtail\logtail_*.log. 32-bit Windows: C:\Program Files\Alibaba\Logtail\logtail_*.log. Check whether the log volume exceeds the limit. To collect large volumes of logs, you may need to modify the Logtail startup parameters for higher log collection throughput. For more information, see Set Logtail startup parameters.

#### 9.1.2 What can I do if Log Service does not receive heartbeats from a Logtail client?

heartbeats from a Logtail client? If Log Service does not receive heartbeats from a Logtail client, perform the steps that are described in the topic to troubleshoot the problem. Context After Logtail is installed on a server, the Logtail client sends heartbeats to Log Service. If the status page of the machine group shows that Log Service does not receive heartbeats from a Logtail client, it indicates that the Logtail client is not installed or disconnected from the server. Step 1: Check whether Logtail is installed Use the following method to check whether Logtail is installed: On a Linux server, run the following command:

```python
sudo /etc/init.d/ilogtaild status
```

If the command returns `ilogtail is running` , it indicates that Logtail is installed. The following script shows an example command and response:

```
[root@****************~]# sudo /etc/init.d/ilogtaild status ilogtail is running
```

On a Windows server: i. Press Win+R. In the Run dialog box, enter services.msc and click OK. ii. In the Services window, check the status of the LogtailDaemon and LogtailWorker services. If the services are in the Running state, it indicates that Logtail is installed. If Logtail is not installed, install it. For more information, see Install Logtail in Linux or Install Logtail in Windows. Ensure that the Log Service endpoint in the Logtail installation command corresponds to the region to which the Log Service project belongs. If Logtail is running, go to the next step. Step 2: Check the Log Service endpoint in the Logtail installation command When you install Logtail, you must specify a Log Service endpoint based on the region to which the Log Service project belongs. If the endpoint is incorrect or the Logtail installation command is invalid, Log Service cannot receive heartbeats from the Logtail client. You can view the Log Service endpoint and installation method in the Logtail configuration file named ilogtail_config.json. The file is stored in the following path: Linux: /usr/local/ilogtail/ilogtail_config.json 64-bit Windows: C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json 32-bit Windows: C:\Program Files\Alibaba\Logtail\ilogtail_config.json In the Logtail configuration file, check the value of the `config_server_address` parameter. This parameter specifies the Log Service endpoint. Then, check whether the Logtail client can connect to Log Service based on the endpoint. For example, if the endpoint that is recorded in the Logtail configuration file is `logtail.cn-qingdao-` `env25-d01.sls-pub.inter.env25.shuguang.com` , you can run the following command to check the connection: Linux:

```bash
curl logtail.cn-qingdao-env25-d01.sls-pub.inter.env25.shuguang.com
```

Windows:

```
telnet logtail.cn-qingdao-env25-d01.sls-pub.inter.env25.shuguang.com 80
```

If the Log Service endpoint in the Logtail installation command is incorrect, re-install Logtail. For more information, see Install Logtail in Linux or Install Logtail in Windows. If the Log Service endpoint in the Logtail installation command is correct, go to the next step. Step 3: Check the server IP addresses in the machine group The server IP address that is obtained by a Logtail client must be configured in the machine group. Otherwise, Log Service cannot receive heartbeats or collect logs from the Logtail client. Logtail uses the following methods to obtain the IP address of a server: If the server is not bound with a hostname, Logtail obtains the IP address of the first network interface controller (NIC) card of the server. If the server is bound with a hostname, Logtail obtains the IP address that corresponds to the hostname. You can view the hostname and IP address in the /etc/hosts file.

> Not e You can run the host name command to query the hostname.

Perform the following steps to check whether the server IP address that is obtained by the Logtail client is configured in the machine group.
1. Check the server IP address that is obtained by Logtail.
The `ip` field in the app_info.json file indicates the server IP address that is obtained by Logtail. The file is stored in the following path: Linux: /usr/local/ilogtail/app_info.json 64-bit Windows: C:\Program Files (x86)\Alibaba\Logtail\app_info.json 32-bit Windows: C:\Program Files\Alibaba\Logtail\app_info.json

> Not e
> If the `ip` field in the `app_info.json` file is empty, Logtail cannot work. In this case, you must configure an IP address for the server and restart Logtail.
> The `app_info.json` file is used only to record information. If you modify the IP address in the file, the server IP address obtained by Logtail is not updated.

2. Check the server IP addresses in the machine group.
Log on to the Log Service console. In the Project s section, click the project to which the machine group belongs. In the left-side navigation pane, click the Machine Groups icon. In the Machine Groups pane, click the machine group. In the Machine Group St at us section of the Machine Group Set t ings page, check the server IP addresses. If no server IP address in the machine group is the same as the IP address that is obtained by Logtail, perform the following step to modify the IP address configurations in the Log Service console: If a server IP address in the machine group is incorrect, change the IP address to the IP address that is obtained by Logtail. Then, check the heartbeat status 1 minute after you save the change. If you have modified the IP address of the server where Logtail is installed (for example, the /etc/hosts file is modified), restart Logtail. After Logtail obtains the new server IP address, set a server IP address in the machine group to the value of the `ip` field in the `app_info.json` file. You can use the following method to restart Logtail: On a Linux server, run the following commands:

```python
sudo /etc/init.d/ilogtaild stop sudo /etc/init.d/ilogtaild start
```

On a Windows server: Press Win+R. In the Run dialog box, enter services.msc and click OK. In the Services window, find and restart the LogtailWorker service.

#### 9.1.3 How do I query the local log collection statuses?

You can use Logtail to query the health status of Logtail and log collection statuses. The statuses help you troubleshoot log collection issues and customize status monitoring for log collection. Instructions After a Logtail client that supports the status query feature is installed, you can query the local log collection statuses by running commands on the client. For more information about how to install Logtail, see Install Logtail in Linux. You can run the `/etc/init.d/ilogtaild -h` command on the client to check whether a client supports the feature of querying the local log collection status. If the command output includes the `logtail insight,` `version` keyword, it indicates that the client supports the status query feature.

```
/etc/init.d/ilogtaild -h Usage: ./ilogtaild { start | stop (graceful, flush data and save checkpoints) | force-stop | status | -h for help}$ logtail insight, version : 0.1.0 commond list :
       status all [index]
             get logtail running status
       status active [--logstore | --logfile] index [project] [logstore]
             list all active logstore | logfile. if use --logfile, please add project and logstore. de
fault --logstore
       status logstore [--format=line | json] index project logstore
             get logstore status with line or json style. default --format=line
       status logfile [--format=line | json] index project logstore fileFullPath
             get log file status with line or json style. default --format=line
       status history beginIndex endIndex  project logstore [fileFullPath]
             query logstore | logfile history status.
index : from 1 to 60. in all, it means last $(index) minutes; in active/logstore/logfile/history, it means last $(index)*10 minutes
```

The following table describes the commands that are supported by Logtail:

| Command | Function | Maximum time range that can be queried | Time window |
|---|---|---|---|
| all | Queries the status of Logtail. | Last 60 minutes | 1 minute |
| active | Queries the active Logstores that are collecting logs and the active log files from which logs are being collected. | Last 600 minutes | 10 minutes |
| logstore | Queries the collection status of a Logstore. | Last 600 minutes | 10 minutes |
| logfile | Queries the collection status of a log file. | Last 600 minutes | 10 minutes |
| history | Queries the collection status of a Logstore or log file in the query time window. | Last 600 minutes | 10 minutes |

|   | Not e The index parameter in the preceding commands indicates the index of the time window. Valid values: 1 to 60. The index of the latest time window is 1 and the time window ends at the current system time. If you specify a 1-minute time window, the status in the past interval of (index, index-1 ] minutes is returned. If you specify a 10-minute time window, the status in the past interval of (10* index, 10*(index-1)] minutes is returned. All commands in the preceding table is the subcommands of the status command. |
|---|---|
|   | ] |

Command all Command syntax

```
/etc/init.d/ilogtaild status all [ index ]
```

> Not e The all command is used to query the status of Logtail. The index parameter is optional. Default value: 1.

Examples

```
/etc/init.d/ilogtaild status all 1
```

`ok`

```
/etc/init.d/ilogtaild status all 10 busy
```

Response

| Status | Description | Priority | Troubleshooting |
|---|---|---|---|
| ok | Logtail is running as expected. | N/A | No action is required. |
| busy | The collection speed is high, and Logtail is running as expected. | N/A | No action is required. |
| many log files _ _ | A large number of log files are being collected by Logtail. | Low | You can check the Logtail configuration for log files that do not need to be collected. |
| process block _ | The process of log parsing is blocked. | Low | You can check whether a large number of logs are generated in a short time. If you use the all command for multiple times and the returned value is always process block, you _ can modify the limit of CPU usage or the limit of concurrent packet sending. |
| send block _ | The process of sending log packets is blocked. | High | You can check whether a large number of logs are generated in a short time and the network connection is stable. If you use the all command for multiple times and the returned value is always send block, you can _ modify the limit of CPU usage or the limit of concurrent packet sending. |

Command active Command syntax

```
/etc/init.d/ilogtaild status active [--logstore] index
 /etc/init.d/ilogtaild status active --logfile index project-name logstore-name
```

|   | Not e You can use the active [--logstore] index command to query all active Logstores. The --logstor e parameter is optional. The command active --logfile index project-name logstore-name is used to query all active log files in the Logstore of a project. The active command is used to query log files. We recommend that you query active Logstores before querying active log files in the Logstores. |   |   |
|---|---|---|---|
|   |   | --logstor |   |
|   | e |   |   |

Examples

```
/etc/init.d/ilogtaild status active 1 sls-zc-test : release-test sls-zc-test : release-test-ant-rpc-3 sls-zc-test : release-test-same-regex-3 /etc/init.d/ilogtaild status active --logfile 1 sls-zc-test release-test /disk2/test/normal/access.log
```

Response

| active --logstore index |   |   | command |
|---|---|---|---|
|   | project-name : logstore-name |   |   |
|   |   | the paths of active log files |   |

If you run the `active --logstore index` command, the names of the active Logstores are returned in the following format: `project-name : logstore-name` . If you run the command `active --logfile index project` The status of the inactive Logstores or inactive log files in the query time window is not returned. Command logstore Command syntax

```
/etc/init.d/ilogtaild status logstore [--format={line|json}] index project-name logstore-name
```

> Not e

The logstore command is used to query the collection status of the specified project and Logstore in the LINE or JSON format.

| meter is | --format=line |   |
|---|---|---|
| --format= |   | parameter is |

If the Logstore specified in the preceding command does not exist or is not active in the query time window, an empty response in LINE format or the `null` value in the JSON format is returned. Examples

```
/etc/init.d/ilogtaild status logstore 1 sls-zc-test release-test-same time_begin_readable : 17-08-29 10:56:11 time_end_readable : 17-08-29 11:06:11 time_begin : 1503975371 time_end : 1503975971 project : sls-zc-test logstore : release-test-same status : ok config : ##1.0##sls-zc-test$same read_bytes : 65033430 parse_success_lines : 230615 parse_fail_lines : 0 last_read_time : 1503975970 read_count : 687 avg_delay_bytes : 0 max_unsend_time : 0 min_unsend_time : 0 max_send_success_time : 1503975968 send_queue_size : 0 send_network_error_count : 0 send_network_quota_count : 0 send_network_discard_count : 0 send_success_count : 302 send_block_flag : false sender_valid_flag : true /etc/init.d/ilogtaild status logstore --format=json 1 sls-zc-test release-test-same
```

`{`

```json
   "avg_delay_bytes" : 0,
   "config" : "##1.0##sls-zc-test$same",
   "last_read_time" : 1503975970,
   "logstore" : "release-test-same",
   "max_send_success_time" : 1503975968,
   "max_unsend_time" : 0,
   "min_unsend_time" : 0,
   "parse_fail_lines" : 0,
   "parse_success_lines" : 230615,
   "project" : "sls-zc-test",
   "read_bytes" : 65033430,
   "read_count" : 687,
   "send_block_flag" : false,
   "send_network_discard_count" : 0,
   "send_network_error_count" : 0,
   "send_network_quota_count" : 0,
   "send_queue_size" : 0,
   "send_success_count" : 302,
   "sender_valid_flag" : true,
   "status" : "ok",
   "time_begin" : 1503975371,
   "time_begin_readable" : "17-08-29 10:56:11",
   "time_end" : 1503975971,
   "time_end_readable" : "17-08-29 11:06:11"
```

`}` Response

| Parameter | Description | Unit |
|---|---|---|

| Parameter | Description | Unit |
|---|---|---|
| status | The status of the Logstore.For information about Logstore statuses and actions that are required to deal with each status, see the following table. | N/A |
| time begin readable _ _ | The time when logs become readable. | N/A |
| time end readable _ _ | The time when logs become unreadable. | N/A |
| time begin _ | The time when statistics collection starts. | Unix timestamp in seconds |
| time end _ | The time when statistics collection ends. | Unix timestamp in seconds |
| project | The name of the project. | N/A |
| logstore | The name of the Logstore. | N/A |
| config | The name of the Logtail configuration, which is globally unique. The format of the name is ##1.0## + project + $ + config. | N/A |
| read bytes _ | The amount of the log data that is read in the query time window. | Byte |
| parse success lines _ _ | The number of the log lines that are parsed in the query time window. | Line |
| parse fail lines _ _ | The number of the log lines that fail to be parsed in the query time window. | Line |
| last read time _ _ | The last time when logs are read in the query time window. | Unix timestamp in seconds |
| read count _ | The number of times that the log file is read in the query time window. | Times |
| avg delay bytes _ _ | The average of difference between the actual file size and the offset generated when reading log data each time in the query time window. | Byte |
| max unsend time _ _ | The maximum period of time for which an unsent packet waits in the sending queue. An unsent packet refers to a packet that has not been sent at the end of the query time window. If no packets exist in the queue, the value is 0. | Unix timestamp in seconds |

| Parameter | Description | Unit |
|---|---|---|
| min unsend time _ _ | The minimum period of time for which an unsent packet waits in the sending queue. Unsent packets refer to packets that have not been sent at the end of the query time window. If no packets exist in the queue, the value is 0. | Unix timestamp in seconds |
| max send success time _ _ _ | The maximum period of time when a packet waited in the sending queue. | Unix timestamp in seconds |
| send queue size _ _ | The number of the unsent packets in the sending queue at the end of the query time window. | Number of packets |
| send network error count _ _ _ | The number of the packets that cannot be sent due to network errors in the query time window. | Number of packets |
| send network quota count _ _ _ | The number of the packets that cannot be sent due to quota limit in the query time window. | Number of packets |
| send network discard count _ _ _ | The number of the packets that are discarded due to data errors or lack of permissions. | Number of packets |
| send success count _ _ | The number of the packets that are sent in the query time window. | Number of packets |
| send block flag _ _ | Indicates whether the sending queue is blocked at the end of the query time window. | N/A |
| sender valid flag _ _ | Indicates whether the sender flag of the Logstore is valid. The value true indicates that the sender flag is valid. The value false indicates that the sender flag is invalid and disabled because of a network error or quota error. | N/A |

Logstore statuses

| Status | Description | Troubleshooting |
|---|---|---|
| ok | Logtail is running as expected. | No action is required. |
| process block _ | The process of log parsing is blocked. | You can check whether a large number of logs are generated in a short time. If you use the all command for multiple times and the returned value is always process block, you can Set Logtail startup _ parametersmodify the limit of CPU usage or of concurrent packet sending. |
| parse fail _ | Logtail fails to parse logs. | You can check whether the format of logs is consistent with that you set in the Logtail configuration. |

|   | User Guide·FAQ |   | Log Service |   |
|---|---|---|---|---|

| Status | Description | Troubleshooting |
|---|---|---|
| send block _ | The process of sending log packets is blocked. | You can check whether a large number of logs are generated in a short time and the network connection is stable. If you use the all command for multiple times and the returned value is always send block, you can Set _ Logtail startup parametersmodify the limit of CPU usage or of concurrent packet sending. |

Command logfile Command syntax

```
/etc/init.d/ilogtaild status logfile [--format={line|json}] index project-name logstore-name fileFullP ath
```

> Not e
> The logfile command is used to query the collection status of the specified log files in the LINE or JSON format.
> The default value of the `--format=` parameter is `--format=line` , which indicates that the status is returned in the LINE format.
> If the log file specified in the command does not exist or is not active in the query time window, an empty response in the LINE format or the `null` value in the JSON format is returned.

| --format |   |
|---|---|
|   | filefullpath |

> The `--format` parameter is placed after the `logfile` parameter.
> The value of the `filefullpath` parameter must be the full path of the log file.

Examples

```
/etc/init.d/ilogtaild status logfile 1 sls-zc-test release-test-same /disk2/test/normal/access.log time_begin_readable : 17-08-29 11:16:11 time_end_readable : 17-08-29 11:26:11 time_begin : 1503976571 time_end : 1503977171 project : sls-zc-test logstore : release-test-same status : ok config : ##1.0##sls-zc-test$same file_path : /disk2/test/normal/access.log file_dev : 64800 file_inode : 22544456 file_size_bytes : 17154060 file_offset_bytes : 17154060 read_bytes : 65033430 parse_success_lines : 230615 parse_fail_lines : 0 last_read_time : 1503977170 read_count : 667 avg_delay_bytes : 0 /etc/init.d/ilogtaild status logfile --format=json 1 sls-zc-test release-test-same /disk2/test/normal/ access.log
```

`{`

```json
   "avg_delay_bytes" : 0,
   "config" : "##1.0##sls-zc-test$same",
   "file_dev" : 64800,
   "file_inode" : 22544456,
   "file_path" : "/disk2/test/normal/access.log",
   "file_size_bytes" : 17154060,
   "last_read_time" : 1503977170,
   "logstore" : "release-test-same",
   "parse_fail_lines" : 0,
   "parse_success_lines" : 230615,
   "project" : "sls-zc-test",
   "read_bytes" : 65033430,
   "read_count" : 667,
   "read_offset_bytes" : 17154060,
   "status" : "ok",
   "time_begin" : 1503976571,
   "time_begin_readable" : "17-08-29 11:16:11",
   "time_end" : 1503977171,
   "time_end_readable" : "17-08-29 11:26:11"
```

`}` Response

| Parameter | Description | Unit |
|---|---|---|
| status | The collection status of the log file in the query time window. For more information, see the status parameter in the Command logstore section. | N/A |
| time begin readable _ _ | The time when logs become readable. | N/A |

| Parameter | Description | Unit |
|---|---|---|
| time end readable _ _ | The time when logs become unreadable. | N/A |
| time begin _ | The time when statistics collection starts. | Unix timestamp in seconds |
| time end _ | The time when statistics collection ends. | Unix timestamp in seconds |
| project | The name of the project. | N/A |
| logstore | The name of the Logstore. | N/A |
| file path _ | The path of the log file. | N/A |
| file dev _ | The ID of the device from which the log file is collected. | N/A |
| file inode _ | The inode of the log file. | N/A |
| file size bytes _ _ | The size of the log file that is last scanned in the query time window. | Byte |
| read offset bytes _ _ | The parsing offset of the log file. | Byte |
| config | The name of the Logtail configuration, which is globally unique. The format of the name is ##1.0## + project + $ + config. | N/A |
| read bytes _ | The amount of the log data that is read in the query time window. | Byte |
| parse success lines _ _ | The number of the log lines that are parsed in the query time window. | Line |
| parse fail lines _ _ | The number of the log lines that fail to be parsed in the query time window. | Line |
| last read time _ _ | The last time when logs are read in the query time window. | Unix timestamp in seconds |
| read count _ | The number of times that the log file is read in the query time window. | Times |
| avg delay bytes _ _ | The average of difference between the actual file size and the offset generated when reading log data each time in the query time window. | Byte |

Command history Command syntax

```
/etc/init.d/ilogtaild status history beginIndex endIndex project-name logstore-name [fileFullPath]
```

> Not e
> The history command is used to query the collection status of a Logstore or log file in the query time window.
> The `beginIndex` and `endIndex` parameters specify the start and end indexes of the range of time
> windows that you want to query. You must ensure that `beginIndex <= endIndex` .
> The `fileFullPath` parameter is optional. If you specify the path of a log file, the collection status of the log file is queried. If the path is not specified, the collection status of the Logstore is queried.

Examples

```
/etc/init.d/ilogtaild status history 1 3 sls-zc-test release-test-same /disk2/test/normal/access.log
        begin_time          status      read  parse_success  parse_fail      last_read_time  read_coun
t avg_delay device inode file_size read_offset
 17-08-29 11:26:11              ok   62.12MB         231000           0   17-08-29 11:36:11         67
1 0B 64800 22544459 18.22MB 18.22MB
 17-08-29 11:16:11              ok   62.02MB         230615           0   17-08-29 11:26:10         66
7 0B 64800 22544456 16.36MB 16.36MB
 17-08-29 11:06:11              ok   62.12MB         231000           0   17-08-29 11:16:11         68
7 0B 64800 22544452 14.46MB 14.46MB $/etc/init.d/ilogtaild status history 2 5 sls-zc-test release-test-same
        begin_time          status      read  parse_success  parse_fail      last_read_time  read_coun
t avg_delay send_queue network_error quota_error discard_error send_success send_block send_va lid max_unsend min_unsend max_send_success
 17-08-29 11:16:11              ok   62.02MB         230615           0   17-08-29 11:26:10         66
7 0B 0 0 0 0 300 false t rue 70-01-01 08:00:00 70-01-01 08:00:00 17-08-29 11:26:08
 17-08-29 11:06:11              ok   62.12MB         231000           0   17-08-29 11:16:11         68
7 0B 0 0 0 0 303 false t rue 70-01-01 08:00:00 70-01-01 08:00:00 17-08-29 11:16:10
 17-08-29 10:56:11              ok   62.02MB         230615           0   17-08-29 11:06:10         68
7 0B 0 0 0 0 302 false t rue 70-01-01 08:00:00 70-01-01 08:00:00 17-08-29 11:06:08
 17-08-29 10:46:11              ok   62.12MB         231000           0   17-08-29 10:56:11         69
2 0B 0 0 0 0 302 false t rue 70-01-01 08:00:00 70-01-01 08:00:00 17-08-29 10:56:10
```

Response The collection status of the Logstore or log file in each query time window is listed in a line. For more information about response parameters, see the Command `logstore` and Command `logfile` sections. Response status codes Success code If parameters that you specify in a command is valid (even if the queried Logstore or log file is not found), the code 0 is returned. The following section provides two examples:

```
/etc/init.d/ilogtaild status logfile --format=json 1 error-project error-logstore /no/this/file null echo $? /etc/init.d/ilogtaild status all
```

`ok`

```
echo $?
```

Error codes If a non-zero code is returned, it indicates that an error occurs. The following table describes the possible nonzero codes.

| Code |   | Description |   |   | Message |   | Troubleshooting |   |
|---|---|---|---|---|---|---|---|---|
| 10 |   | The command is invalid or required parameters in the command are not specified. |   |   | invalid param, use -h for help. |   | You can run the -h command for help. |   |
| 1 |   | The value of the index parameter is not in the range from 1 to 60. |   |   | invalid query interval |   | You can run the -h command for help. |   |
| 1 |   | The collection status in the specified query time window cannot be queried. |   |   | query fail, error: |   | The startup time of Logtail is earlier than the query time window. Otherwise, you can submit a ticket for help. |   |
|   |   |   |   |   |   | query fail, error: | is e |   |
|   |   |   | d query time |   | $(error) |   |   |   |
| 1 |   | The start time of querying is out of the query time |   |   | no match time |   |   |   |
|   |   |   |   |   |   | no match time | You can check whether Logtail is running. If yes, |   |
|   |   |   |   | uery time | interval, please check |   | Logtail is runn |   |
|   |   |   |   |   |   |   | you can subm |   |
|   |   | window. |   |   |   |   |   |   |
|   |   |   |   |   | logtail status |   |   |   |
| 1 |   | No logs exist in the specified query time window. |   |   | invalid profile, maybe logtail restart |   | You can check whether Logtail is running. If yes, you can submit a ticket for help. |   |

|   |   | invalid param, use -h | You can |
|---|---|---|---|
| mand are not | for help. |   |   |

|   |   | invalid query |
|---|---|---|
| ot in the to 60. | interval |   |

|   |   | invalid profile, | Logtail is running |
|---|---|---|---|
| uery time | maybe logtail restart |   |   |

Examples

```
/etc/init.d/ilogtaild status nothiscmd invalid param, use -h for help. echo $? /etc/init.d/ilogtaild status/all 99 invalid query interval echo $?
```

Scenarios You can query the overall status of Logtail, and specific metrics by querying the collection status during collection. You can customize a mechanism to monitor the log collection status based on the queried information. Monitor the status of Logtail You can monitor the status of Logtail by using the `all` command. For example, you can run the command every minute to query Logtail status. If the `process_block` , `send_block` or `send_error` value is returned for 5 consecutive minutes, an alert is triggered. You can adjust the alert duration and monitoring scope based on the priorities of the collected log files. Monitor the log collection status You can monitor the log collection status of a Logstore by using the `logstore` command.

| e | logstore |   | comm |
|---|---|---|---|
|   | avg delay bytes _ _ |   |   |
| ok |   | , an alert is trig |   |

For example, you can run the `logstore` command every 10 minutes to query the collection status of the Logstore. If the value of the `avg_delay_bytes` parameter exceeds 1 MB (1024 × 1024 bytes) or the value of the You can adjust the alert threshold for the `avg_delay_bytes` metric based on the size of data that is generated during the log collection. Check whether Logtail has finished collecting log files You can check whether Logtail has finished collecting log files by using the `logfile` command.

| files, you can run the | logfile |
|---|---|
| read offset bytes _ _ | paramete |

parameter, it indicates that the log file is collected. Troubleshoot log collection issues If log collection latency occurs on a server, you can use the `history` command to query the status history of log collection.
1. The value of the `send_block_flag` parameter is true.This indicates that the log collection is blocked
because of unstable network connections. If the value of the `send_network_quota_count` parameter is greater than 0, split shards in the Logstore. For more information, see Split a shard. If the value of the `send_network_error_count` parameter is greater than 0, check the network connections. If no network error occurs, adjust the limit of concurrent packet sending and data transfer speed of Logtail.
2. The parameters related to packet sending are set to appropriate values. However, the value of the `avg_dela`
`y_bytes` parameter is large. Use the value of the `read_bytes` parameter to calculate the average speed of parsing logs, and then determine whether a large amount of data is transferred during log collection based on the average speed. Adjust the resource usage limits for Logtail.
3. The value of the `parse_fail_lines` parameter is greater than 0.
Check whether the regular expression can match all required log fields as expected.

#### 9.1.4 How do I test a regular expression?

If you select the full regex mode when you configure Logtail to collect and parse text logs, you must specify a regular expression based on your sample log entries. This topic describes how to test a regular expression. Context To test a regular expression that you have specified in the Log Service console, you can click Validat e in the console and check the results as follows: For the regular expression that matches the first line of logs, check whether the regular expression can match the expected number of log entries. For the fields extracted by the regular expression, check whether the value of each field meets your expectations. If you want to validate more items and test a regular expression, you can use online tools such as regex101.com and regextester.com. You can copy and paste the regular expression that is generated by Log Service to an online tool, and specify a sample log entry as the test string. If you use the full regex mode, Log Service automatically generates a regular expression based on a sample log entry. However, the regular expression may fail to match the message field in multi-line log entries as expected. The following example describes how to use the regex101.com tool to test the regular expression.
1. Copy the generated regular expression.
2. Visit the regex101.com website.
3. Paste the regular expression in the REGULAR EXPRESSION field.
On the right side of the page, you can view the explanation of the regular expression.
4. In the T EST ST RING field, paste a log sample entry.
In the following figure, the log contents that are included in the message field are highlighted in orange, and the log contents that are not included are highlighted in blue. The figure shows that the substring following the `at` word is not included in the `message` field. Therefore, this regular expression does not match fields in the sample log entry as expected and cannot be used to collect log data.
5. Check whether the regular expression can match fields in a sample log entry with two colons as expected.
The following figure shows that the regular expression fails to match fields in the sample log entry as expected.
6. Replace the last subexpression in the regular expression with [\S\s]+ , and check whether the regular
expression can match fields in the sample log entries as expected. The following figure shows how the modified regular expression matches the substring following the `at` word. The following figure shows how the modified regular expression matches the sample log entry with two colons. You can follow the preceding instructions to test your regular expression. After you validate the regular expression, you can apply it to a Logtail configuration.

#### 9.1.5 How do I optimize regular expressions?

You can optimize regular expressions to improve the Logtail performance. When you optimize regular expressions, we recommend that you follow these rules: Use precise characters We recommend that you do not use the wildcard characters `. *` in a regular expression to match fields in log entries. Using wildcard characters may lead to mismatches and low matching performance. For example, if a field that you want to match only consists of letters, use `[A-Za-z]` . Use appropriate quantifiers We recommend that you do not use plus signs (+) or asterisks (*). For example, you can use \d instead of \d+ or \d{1,3} to match the IP address. Test and modify regular expressions You can visit the regex101.com website to test and modify a regular expression to decrease the time required to match log entries.

#### 9.1.6 How do I use the full regex mode to collect log entries in multiple formats?

entries in multiple formats? The full regex mode requires that log entries to be collected be in the same format. Therefore, if you want to collect log entries that are in multiple formats, you must use the schema-on-write or schema-on-read solution. Taking Java logs as an example, the following section lists the types of error log entry and normal log entry. Multi-line WARNING log entries Simple text INFO log entries Key-value DEBUG log entries

```
[2018-10-01T10:30:31,000] [WARNING] java.lang.Exception: another exception happened
    at TestPrintStackTrace.f(TestPrintStackTrace.java:3)
    at TestPrintStackTrace.g(TestPrintStackTrace.java:7)
    at TestPrintStackTrace.main(TestPrintStackTrace.java:16)
[2018-10-01T10:30:32,000] [INFO] info something [2018-10-01T10:30:33,000] [DEBUG] key:value key2:value2
```

To collect log entries of these types, you can use the following solutions: Schema-on-write: To extract log fields, you must apply multiple Logtail configurations with different regular expressions to a log file.

> Not e However, Logtail cannot apply multiple Logtail configurations directly to the same log file. Therefore, you must set up multiple symbolic links for the directory in which the log file resides. Each Logtail configuration applies to a symbolic link to collect log entries in a specific format.

Schema-on-read: you can use a common regular expression to collect log entries in different formats. For example, if you want to collect log entries in multiple formats, you can configure a regular expression that matches the time and log level fields as the first line, and specify the rest of the log entries as the log message. If you want to parse the message, create an index for the message, specify a regular expression to extract log messages, and then extract target fields.

> Not e We recommend that you use this solution only for scenarios in which tens of millions of log entries are collected, or fewer.

#### 9.1.7 How do I set the time format for logs?

You must be familiar with the following rules before setting the time format for logs in Logtail configurations. The unit of the timestamp in Log Service is seconds. Therefore, you cannot set the unit as milliseconds or microseconds. You only need to set the time field. Other parameters are not required. The following section lists commonly used formats:

```
Custom1 2017-12-11 15:05:07 %Y-%m-%d %H:%M:%S Custom2 [2017-12-11 15:05:07.012] [%Y-%m-%d %H:%M:%S RFC822 02 Jan 06 15:04 MST %d %b %y %H:%M RFC822Z 02 Jan 06 15:04 -0700 %d %b %y %H:%M RFC850 Monday, 02-Jan-06 15:04:05 MST %A, %d-%b-%y %H:%M:%S RFC1123 Mon, 02 Jan 2006 15:04:05 MST %A, %d-%b-%y %H:%M:%S RFC3339 2006-01-02T15:04:05Z07:00 %Y-%m-%dT%H:%M:%S RFC3339Nano 2006-01-02T15:04:05.999999999Z07:00 %Y-%m-%dT%H:%M:%S
```

#### 9.1.8 How do I configure non-printable characters in a sample log?

sample log? This topic describes how to configure non-printable characters in a sample log entry. Context Log Service allows you to specify a non-printable character as the delimiter or quote to collect logs. Non-printable characters are those whose decimal ASCII codes are in the range of 1 to 31 and 127. If you want to specify a nonprintable character as the delimiter or quote, you must find the hexadecimal ASCII code of this character and enter this character in the following format: `0x` the hexadecimal ASCII code of the non-printable character. For example, a sample log entry is `123456780` . You can set 0x01 as the delimiter and 0x02 as the quote, and then enter a nonprintable character 0x01 between the digits 5 and 6.
1. Log on to the Log Service console.
2. Right-click the blank space on the browser and select Inspect from the shortcut menu.
3. Click the Console tab on the page that appears.
4. Enter "\x01" in the code editor and press Enter.
5. Copy the returned result.
A non-printable character is enclosed in quotation marks (").
6. Paste the returned result between the digits 5 and 6.
7. Delete the quotation marks between the digits 5 and 6.
Then, a non-printable character is configured in a sample log entry.

#### 9.1.9 How do I troubleshoot errors during container log collection?

log collection? Perform the steps that are described in this topic to troubleshoot an error that occurs when you use Logtail to collect logs from common containers or containers in a Kubernetes cluster. Related O&M operations Log on to a Logtail container View the operational logs of Logtail Ignore the stdout logs of a Logtail container View the status of Log Service components in a Kubernetes cluster View the version number, IP address, and startup time of Logtail Troubleshoot an error if Log Service does not receive heartbeats from Logtail clients Perform the following steps to check whether Logtail is installed:
1. In the machine group, count the number of the servers whose heartbeat status is OK.
i. Log on to the Log Service console. ii. Click the project to which the machine group belongs. iii. In the left-side navigation pane, click Machine Groups. iv. In the Machine Groups pane, click the name of the machine group. In the Machine Group St at us section, count the number of the servers whose heartbeat status is OK.
2. Count the number of worker nodes in the cluster.
Run the kubectl get node | grep -v master command to query the work nodes in the cluster. Count the number of the work nodes that are returned.

```
$kubectl get node | grep -v master NAME STATUS ROLES AGE VERSION cn-hangzhou.i-bp17enxc2us3624wexh2 Ready <none> 238d v1.10.4 cn-hangzhou.i-bp1ad2b02jtqd1shi2ut Ready <none> 220d v1.10.4
```

3. Check whether the number of servers whose heartbeat status is OK in the machine group is equal to the
number of worker nodes in the cluster. Troubleshoot the error based on the check result. The number of servers whose heartbeat status is OK is equal to the number of worker nodes. This means that the heartbeat status of all of the servers in the machine group is Failed. If Logtail is installed into a common container, check whether the values of the ${your_region_name}, ${yo ur_aliyun_user_id}, and ${your_machine_group_user_defined_id} parameters are correct. For information about how to set these parameters, see Collect standard Docker logs. If Logtail is installed into a container in a Container Service for Kubernetes cluster, submit a ticket. If Logtail is installed into a container in a user-created Kubernetes cluster, check whether the values of the {your-project-suffix}, {regionId}, {aliuid}, {access-key-id}, and {access-key-secret} parameters are correct. If the value of a parameter is incorrect, run the `helm del --purge alibaba-log-controller` command to delete the installation package and re-install Logtail. For information about how to set these parameters, see Collect Kubernetes logs. The number of servers whose heartbeat status is OK is less than the number of worker nodes. a. Check whether you used a YAML file to manually deploy a DaemonSet. Run the `kubectl get po -n kube-system -l k8s-app=logtail` command to perform the check. If the command returns pod information, it indicates that you manually deployed a DaemonSet by using a YAML file. b. Download the latest version of the Logtail DaemonSet template. c. Set the ${your_region_name}, ${your_aliyun_user_id}, and ${your_machine_group_name} parameters to the values that are specific to your environment. d. Run the `kubectl apply -f ./logtail-daemonset.yaml` command to update the DaemonSet YAML file. Submit a ticket if the error persists. Troubleshoot an error if Log Service collects no logs from containers If no log is displayed in the Consumpt ion Preview pane or on the Search & Analysis page of a Logstore, it indicates that Log Service does not collect logs from the machine group of the Logstore. Check the status of the containers that correspond to the servers in the machine group. If the containers are working as expected, perform the following steps to troubleshoot the error:
1. Check the heartbeat status of the servers in the machine group.
2. Check whether the parameter settings in the Logtail configuration files are correct.
Check whether the values of the IncludeLabel, ExcludeLabel, IncludeEnv, and ExcludeEnv parameters in the Logtail collection configuration files meet your requirements.

> Not e The `IncludeLabel` or `ExcludeLabel` parameter specifies whether to include or exclude the container images to which specified labels are attached. You can retrieve a list of container image labels by running the docker inspect command. The labels are not the labels that are defined by using Kubernetes. To check whether the parameter settings are correct in a Logtail configuration file, delete the IncludeLabel, ExcludeLabel, IncludeEnv, and ExcludeEnv parameters from the file. If Log Service can collect logs from the containers after the parameters are deleted, it indicates that the settings of the parameters are incorrect.

3. Check other items.
Log Service does not collect logs from containers in the following scenarios: Log files are not updated. The log files of a container are stored in locations that are neither the default storage nor a storage attached to the container. Log on to a Logtail container Common container i. Run the docker ps | grep logtail command on the host to search for the Logtail container. ii. Run the `docker exec -it ****** bash` command to log on to the container.

```
$docker ps | grep logtail 223fbd3ed2a6e registry.cn-hangzhou.aliyuncs.com/log-service/logtail "/usr/local/ilogta..." 8 days ago Up 8 days logtail-iba $docker exec -it 223fbd3ed2a6e bash
```

Container in a Kubernetes cluster i. Run the kubectl get po -n kube-system | grep logtail command to search for the pod where the Logtail container resides.

| ii. Run the | kubectl exec -it -n kube-system ****** bash | command to log on to the pod. |
|---|---|---|
| $kubectl get po -n kube-system \| grep logtail logtail-ds-g5wgd 1/1 Running 0 8d logtail-ds-slpn8 1/1 Running 0 8d $kubectl exec -it -n kube-system logtail-ds-g5wgd bash |   |   |

View the operational logs of Logtail The operational logs of Logtail are saved in the files named ilogtail.LOG and logtail_plugin.LOG under the /usr/local/ilogtail/ directory of a Logtail container.
1. Log on to a Logtail container.
2. Open the /usr/local/ilogtail/ directory.

```
cd /usr/local/ilogtail
```

3. View the ilogtail.LOG and logtail_plugin.LOG files.

```
cat ilogtail.LOG cat logtail_plugin.LOG
```

Ignore the stdout logs of a Logtail container The standard output (stdout) logs of a Logtail container are useless for troubleshooting. Ignore the following stdout logs:

```
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57fe8 40c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44bea b6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640b1e 16c22dbe/merged: must be superuser to unmount ...... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
```

View the status of Log Service components in a Kubernetes cluster Run the `helm status alibaba-log-controller` command to view the status of Log Service components in a Kubernetes cluster. View the version number, IP address, and startup time of Logtail View the information in the app_info.json file under the /usr/local/ilogtail/ directory of the Logtail container. For example, you can run the following command to view the content of the file:

```bash
kubectl exec logtail-ds-gb92k -n kube-system cat /usr/local/ilogtail/app_info.json
```

`{`

```json
   "UUID" : "",
   "hostname" : "logtail-gb92k",
   "instance_id" : "0EBB2B0E-0A3B-11E8-B0CE-0A58AC140402_10.10.10.10_1517810940",
   "ip" : "10.10.10.10",
   "logtail_version" : "0.16.2",
   "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64",
   "update_time" : "2018-02-05 06:09:01"
```

`}`

### 9.2 Log search and analysis

#### 9.2.1 FAQ about log query

This topic describes the common issues that may occur when you query log data in the Log Service console. It also includes solutions to these issues. How do I identify the source server from which Logtail collects logs during a query? If a server group uses IP addresses as its identifier when logs are collected by using Logtail, servers in the server group are distinguished from one another by internal IP addresses. When querying logs, you can use the hostname and custom IP address to identify the source server from which logs are collected. For example, you can use the following statement to count the times different hostnames appear in logs:

> Not e You must enable the index feature for the Logstore and enable the statistics feature for the __tag__:__hostname__ field in advance.

```
* | select "__tag__:__hostname__" , count(1) as count group by "__tag__:__hostname__"
```

How do I query IP addresses in logs? You can use the exact match method to query IP addresses in logs. For example, you can specify IP addresses to query log data that includes or excludes the specified IP addresses. However, you cannot use the partial match method to query log data related to specified IP addresses. This is because decimal points contained in an IP address are not default delimiters in Log Service. If you want to use the partial match method, you can configure the decimal point as a delimiter for indexes. For example, you can use the SDK to download data and then use regular expressions or the string.indexof method in the code. For example, you use the following statement to query projects that meet the specified conditions.

```
not ip:121.42.0 not status:200 not 360jk not DNSPod-Monitor not status:302 not jiankongbao
        not 301 and status:403
```

The retrieved log data still contains 121.42.0.x. An IP address such as 121.42.0.x is taken as a word in Log Service. To include or filter out 121.42.0.x in the query result, you must specify 121.42.0.x in the query statement. If you specify 121.42.0 in the query statement, you cannot retrieve log data that includes or excludes the keyword. How do I query log data by using a keyword that contains a whitespace character? If you use a keyword that contains a whitespace character to query log data, log data that contains the part of the keyword on the left or right of the whitespace character is retrieved. You can enclose the keyword that contains a whitespace character in double quotation marks (""). Then the entire enclosed content is regarded as a keyword to query the log data that you expect. For example, you want to query log data that contains the keyword `POS version` from the following log data:

```
post():351]:&nbsp;device_id:&nbsp;BTAddr&nbsp;:&nbsp;B6:xF:xx:65:xx:A1&nbsp;IMEI&nbsp;:&nbsp;35847xx22 xx81x9&nbsp;WifiAddr&nbsp;:&nbsp;4c:xx:0e:xx:4e:xx&nbsp;|&nbsp;user_id:&nbsp;bb07263xxd2axx43xx9exxea2 6e39e5f&nbsp;POS&nbsp;version:903
```

If you use `POS version` as the keyword, log data that contains `POS` and `version` is retrieved. This result does not meet your expectations. If you use `"POS version"` as the keyword, log data that contains the keyword `POS version` is retrieved. How do I use two query conditions to query log data? You can enter two query conditions at one time to query log data that you want. For example, you want to query log data whose status field value is neither OK nor Unknown in a Logstore. You can use the `not OK not Unknown` statement to retrieve the expected result. How can I query collected logs in Log Service? You can use one of the following methods to query logs in Log Service: Use the Log Service console. Use the SDK. Use the Restful API.

#### 9.2.2 What can I do if no log data is retrieved?

When you use the log search and analytics feature of Log Service to query data, you may not retrieve the data you want. In this case, you can troubleshoot the problem as follows: Log collection failure If log data fails to be collected by Log Service, the target log data cannot be queried. Check whether log data is available on the consumption preview page of the target Logstore. If data is available, log data is collected by Log Service. If data is unavailable, possible causes are as follows: The log source does not generate log data. In this case, no logs can be sent to Log Service. Check your log source. Logtail has no heartbeat. On the Server Group Set t ings page, check whether the relevant server has a heartbeat in the Server Group Status section. If it has no heartbeat, troubleshoot the problem. For more information, see What can I do if no heartbeat packet is received from a Logtail client? The monitoring file is not written in real time. If the monitoring file is written in real time, you can open the /usr/local/ilogtail/ilogtail.LOG file to view the error message. Common error messages are as follows: parse delimiter log fail: The error message is returned because an error has occurred when Log Service collects logs in the delimiter mode. parse regex log fail: The error message is returned because an error has occurred when Log Service collects logs in the regex mode. Delimiter setting errors View the configured delimiters. Check whether you can use a keyword to query log data after the log content is split by using a delimiter. For example, the default delimiters , ; = ( ) [ ] { } ? @ & < > / : ' are used. If a log entry contains abc"defg,hij, it is split into abc"defg and hij. In this case, you cannot retrieve this log entry by searching for abc. Fuzzy match is also supported. For more information, see Query syntax.

> Not e
> To save your indexing cost, Log Service has optimized the index feature. If you configure an index for a field, full-text indexing is ineffective for the key of this field. For example, an index is configured for a log field whose key is message, and a whitespace character is used as a delimiter. To use a whitespace character as a delimiter, put it in the middle of delimiters that you have configured for an index. You can retrieve the log entries that contain "message: this is a test message" by searching for the key-value- pair-formatted keyword message:this. However, if you use the keyword this to query the log entries, you cannot retrieve the data because an index is configured for the message field and full-text indexing is ineffective.
> You can create indexes or modify existing indexes. However, new or modified indexes take effect only for new data.
> You can click Index Attributes to check whether the configured delimiters meet the requirements.

Other reasons If log data is available, modify the time range of the query and try again. Log Service allows you to preview log data in real time. Due to a maximum latency of one minute, we recommend that you query log data at least one minute after logs are generated.

#### 9.2.3 What are the differences between log consumption and log search and analytics?

consumption and log search and analytics? Both the log consumption and log search and analytics features provided by Log Service need to read log data. The log consumption feature provides log collection and distribution channels. In contrast, the log search and analytics feature allows you to query log data. Both the log consumption and log search and analytics features need to read log data: Log collection and consumption (LogHub): provides public channels for log collection and distribution. It reads and writes full data in first-in, first-out (FIFO) order, which is similar to Kafka. Each Logstore has one or more shards. Data is written to a random shard. You can read multiple log entries at a time from a specified shard based on the order in which the log entries were written to the shard. You can set the start position (cursor) to pull log entries from shards based on the time when Log Service receives the log entries. Log search and analytics: enables you to set conditions to search and analyze large amounts of log data based on LogHub. This feature allows you to search for required data based on query conditions. This feature allows you to include a combination of Boolean keywords AND, NOT, and OR and SQL statements in a query. This feature is independent of shards. The following table lists the differences between the log search and analytics feature and the LogHub feature.

| Feature | Log search and analytics (LogSearch) | LogHub |
|---|---|---|
| Search by keyword | Supported. | Not supported. |
| Data read (a small amount of data) | Fast. | Fast. |
| Data read (full data) | Slow. LogSearch reads 100 log entries in 100 milliseconds. This method is not recommended. | Fast. LogHub reads 1 MB of log data in 10 milliseconds. This method is recommended. |
| Data read by topic | Yes. | No. Data is identified only by shard. |
| Data read by shard | No. Data in all shards of a Logstore is queried. | Yes. You need to specify a shard each time to read data. |
| Price | Relatively high. | Low. |
| Scenario | Monitoring, problem investigation, and analysis. | Full data processing scenarios, such as stream computing and batch processing. |

#### 9.2.4 How do I resolve common errors returned in log data queries?

data queries? Common errors returned in log data queries are as follows: line 1:44: Column 'my_key_field' cannot be resolved;please add the column in the index attribute Cause The `my_key_field` key cannot be included in the query statement because it does not exist. Solution In the upper-right corner of the Search & Analysis page, click Index Attributes to create an index for this field and enable the statistics feature for this field. Column 'xxxxline' not in GROUP BY clause;please add the column in the index attribute Cause You use the GROUP BY clause and include a non-aggregated field in a SELECT statement. However, this field is not specified in the GROUP BY clause. For example, the key1 field in the `select key1, avg(latency) group by k` `ey2` statement is not specified in the GROUP BY clause. Solution An example correct statement is `select key1,avg(latency) group by key1,key2` . sql query must follow search query,please read syntax doc Cause You do not include a filtering condition in a query statement, for example, `select ip,count(*) group by ip` . Solution An example correct statement is *|select ip,count(*) group by ip . please read syntax document,and make sure all related fields are indexed. error after select .error detail:line 1:10: identifiers must not start with a digit; surround the identifier with double quotes Cause The column name or variable name referenced in an SQL statement starts with a number and does not comply with the rules. Solution Change the name so the name starts with a letter. please read syntax document,and make sure all related fields are indexed. error after select .error detail:line 1:9: extraneous input '' expecting Cause Misspelled words exist in the query statement. Solution Correct the misspelled words. key (category) is not config as key value config,if symbol : is in your log,please wrap : with quotation mark " Cause No index is configured for the category field. It cannot be used in a query statement. Solution Configure an index for this field in the index attributes. For more information, see Enable the index feature and configure indexes for a Logstore. Query exceeded max memory size of 3GB Cause The size of memory used by the current query exceeds 3 GB. The common cause is that a large number of values are still returned in the query result after you use the GROUP BY clause to remove duplicates. Solution Reduce the number of keys specified in the GROUP BY clause. ErrorType:ColumnNotExists.ErrorPosition,line:0,column:1.ErrorMessage:line 1:123: Column '__raw_log__' cannot be resolved; it seems __raw_log__ is wrapper by ";if __raw_log__ is a string ,not a key field, please use '__raw_log__' Cause The `my_key_field` key cannot be included in the query statement because it does not exist. Solution In the upper-right corner of the Search & Analysis page, click Index Attributes to create an index for this field and enable the statistics feature for this field.

#### 9.2.5 Why data queries are inaccurate?

This topic describes the causes for inaccurate data queries. It also includes solutions to these issues. When you search and analyze log data, the message T he result s are inaccurat e may prompt in the console. This indicates that the returned result is inaccurate because some log data in a Logstore was not queried. Possible causes include: The time range for queries is excessive. Cause The time range for a query is excessively wide, for example, three months or a year. In this case, Log Service cannot scan all log data generated within this time period for one query. Solution Narrow down the query time range and perform multiple queries. Query statements are complex. Cause The query statement is exceedingly complex or contains multiple frequently used words. In this case, Log Service cannot scan all related log data or read the query results at one time. Solution Narrow down the query scope and perform multiple queries. The SQL computing needs to read an excessively large amount of data. Cause The SQL computing needs to read an excessively large amount of data. In this case, query results are likely to become inaccurate. A maximum of 1 GB of data can be read from each shard. For example, if the SQL computing needs to read strings from multiple columns, which exceed the threshold data volume, inaccurate query results will be returned. Solution Narrow down the query scope and perform multiple queries.

### 9.3 Alarm

#### 9.3.1 FAQ about alerts

This topic describes the common issues that may occur when you configure alerts in the Log Service console. It also includes solutions to these issues. How can I include the raw error log entries in the notification content? Issue More than five error log entries were generated in the past five minutes, which triggered an alert. How can I include the raw error log entries in notifications that were sent when the alert was triggered? Solution Associated query statements Number 0: `level:ERROR` Number 1: level:ERROR | select COUNT(*) as count Trigger condition: $1.count > 5 Notification content: ${results[0].rawresults} Configuration examples
