---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 MaxCompute Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 33
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 MaxCompute Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%A4%A7%E6%95%B0%E6%8D%AE/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20MaxCompute%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 MaxCompute Developer Guide 20220928

## Table of Contents

- 1 Java SDK
  - 1.1 SDK for Java
  - 1.2 Prerequisites
    - 1.2.1 Overview
    - 1.2.2 Obtain an AccessKey pair
      - 1.2.2.1 Log on to the ASCM console
      - 1.2.2.2 Obtain the AccessKey pair of an organization
      - 1.2.2.3 View the AccessKey pair of your Apsara Stack tenant account
    - 1.2.3 Obtain the endpoint
  - 1.3 Major APIs
    - 1.3.1 AliyunAccount
    - 1.3.2 Odps
    - 1.3.3 Projects
    - 1.3.4 Project
    - 1.3.5 SQLTask
    - 1.3.6 Instances
    - 1.3.7 Instance
    - 1.3.8 Tables
    - 1.3.9 Table
    - 1.3.10 Resources
    - 1.3.11 Resource
    - 1.3.12 Functions
    - 1.3.13 Function
    - 1.3.14 Spark Shell
    - 1.3.15 Spark R
    - 1.3.16 Spark SQL
    - 1.3.17 Spark JDBC
    - 1.3.18 Document APIs
    - 1.3.19 Search APIs
- 2 SDK for Python

## 1 Java SDK

### 1.1 SDK for Java

This topic describes the most commonly used APIs of MaxCompute SDK for Java. For more information, visit the following website: Comprehensive APIs of MaxCompute You can use Maven to configure the new version of the SDK. The following configuration is used:

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>xxxx-public</version>
</dependency>
```

The following table describes the overall information about SDK packages provided by MaxCompute.

| Package | Description |
|---|---|
| odps-sdk-core | Basic features of MaxCompute. This package encapsulates MaxCompute APIs such as odps, and basic features such as projects and tables. It also includes Tunnel-related features. |
| odps-sdk-core-internal | Extended features of MaxCompute. This package encapsulates the less commonly used MaxCompute features and operations, such as Event and XFlow. |
| odps-sdk-commons | MaxCompute infrastructure. This package includes TableSchema, Column, Record, OdpsType, and some util packages. |
| odps-sdk-udf | The UDF API for MaxCompute. |
| odps-sdk-mapred | The MapReduce API for MaxCompute. |
| odps-sdk-graph | The Graph API for MaxCompute. |

The SDK packages are available at SDK package download. Not e If your MaxCompute version is earlier than V3.8.0, download the 0.27.2-public/ version of SDK packages. If your MaxCompute version is V3.8.0 or later, download the 0.30.8-public/ or 0.30.9-public/ version of SDK packages.

### 1.2 Prerequisites

Before using the SDK for Java, you must perform the following operations: Create an account with authorization to access MaxCompute and obtain the AccessKey pair for the account. For more information about how to obtain and view your AccessKey pair in the Apsara Stack console, see Obtain an AccessKey pair. Obtain the endpoint. For more information, see Obtain an endpoint.

#### 1.2.1 Overview

Before using SDKs for MaxCompute, you must perform the following operations: Create an account that is authorized to access MaxCompute and obtain an AccessKey pair (AccessKey ID and AccessKey secret). Obtain the service endpoint.

#### 1.2.2 Obtain an AccessKey pair

You can obtain an AccessKey pair in the Apsara Stack Cloud Management (ASCM) console.

##### 1.2.2.1 Log on to the ASCM console

This topic describes how to log on to the Apsara Stack Cloud Management (ASCM) console. Prerequisites The IP address or domain name of the ASCM console is obtained from deployment personnel. The URL used to log on to the ASCM console is in the following format: https://IP address or domain name of the ASCM console. A browser is available. We recommend that you use Google Chrome. Procedure
1. In the address bar, enter the URL used to log on to the ASCM console. Press Enter.
2. Enter the correct username and password.
Obtain the username and password used to log on to the console from the operations administrator. Not e When you log on to the ASCM console for the first time, you must change the password as prompted. For security purposes, your password must meet the complexity requirements. Specifically, the password must be 8 to 20 characters in length and must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters such as ! @ # $ %
3. Click Login to go to the homepage of the ASCM console.

##### 1.2.2.2 Obtain the AccessKey pair of an organization

This topic describes how to obtain an AccessKey pair. Prerequisites Only the operation administrators or level-1 organization administrators can obtain the AccessKey pair of an organization. Procedure
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of an organization.
5. Select AccessKey from the shortcut menu.
6. In the message that appears, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations of the level-1 organization use the AccessKey pair of the level-1 organization.

##### 1.2.2.3 View the AccessKey pair of your Apsara Stack tenant account

tenant account To secure cloud resources, the system must verify the identity of visitors and ensure that they have the relevant permissions. You must obtain the AccessKey ID and AccessKey secret of your personal account to access cloud resources. Procedure
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair is made up of the AccessKey ID and AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

#### 1.2.3 Obtain the endpoint

This topic describes how to obtain the service endpoint in the Apsara Stack Operations (ASO) console. Context The URL, username, and password that are required to log on to the console are obtained from deployment personnel or administrators. The URL of the ASO console is in the following format: region-id.aso.intranet-domain-id.com. A browser is available. We recommend that you use Google Chrome. Procedure
1. Open your browser.
2. In the address bar, enter region-id.aso.intranet-domain-id.com and press Enter.
Not e You can select a language from the drop-down list in the upper-right corner.
3. Enter your username and password.
Not e Obtain the username and password that are required to log on to the ASO console from deployment personnel or administrators. By default, the following user roles are available: security: the user who has permissions to manage other users or roles auditor: the user who has permissions to view audit logs sysadmin: the user who has permissions that a security administrator and an auditor do not have When you log on to the ASO console for the first time, you must change the password as prompted. To enhance security, the password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters, such as ! @ # $ % It must be 10 to 20 characters in length.
4. Click Log On to go to the ASO page.
5. In the left-side navigation pane, click Product s and then Product List . In the Basic O&M section
of the Apsara St ack O&M pane, click Apsara Inf rast ruct ure Management Framework.
6. In the left-side navigation pane, click Operat ions and then Machine Operat ions to go to the
Machine Operat ions page.
7. In the Machines search box, search for a machine. Click T erminal in the Actions column of the
machine to log on to the machine.
8. Run the following command on the machine to obtain JSON data: curl -l
"ht t p://127.0.0.1:7070/api/v3/column/c.sr.service_regist rat ion,c.sr.id? c.sr.service_regist rat ion".
9. Find the MaxCompute endpoint based on the service ID (odps-service-frontend) and key (odps_fro
ntend_server.endpoint) of MaxCompute.

### 1.3 Major APIs

#### 1.3.1 AliyunAccount

The primary account created with Alibaba Cloud. The input parameters are AccessKey ID and AccessKey Secret. AccessKey ID uniquely identifies an Alibaba Cloud user, and AccessKey Secret is used to authenticate the identity of the user. This class is used to initialize MaxCompute.

#### 1.3.2 Odps

It is the entrance to MaxCompute SDK. You can use this class to obtain all object collections in a project, including Projects, Tables, Resources, Functions, and Instances. You can pass this class into the AliyunAccount instance to construct a MaxCompute object. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}` Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview .

#### 1.3.3 Projects

A collection of all projects in MaxCompute. A project is an element in a collection. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Project p = odps.projects().get("my_exists"); p.reload(); Map<String, String> properties = prj.getProperties(); ...
```

Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.4 Project

A description of project information. You can obtain a list of projects through Projects.

#### 1.3.5 SQLTask

An API for running and processing SQL tasks. You can use SQLTask.run to run SQL tasks. The SQLTask.run API returns an instance, and obtains the running status and results of SQL from the instance. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps( account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance instance = SQLTask.run(odps, "my_project", "select ...") ; String id = instance.getId(); instance.waitforsuccess(); Set<String> taskNames = instance.getTaskNames(); for (String name taskNames) { TaskSummary summary = instance.getTaskSummary(name); String s = summary.getSummaryText();
```

`}`

```
Map<String, String> results = instance.getTaskResults(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { String result = results.get(status.getKey());
```

`}` Not e To create a table, you must use the SQLTask API instead of the Table API. You must pass the CREATE TABLE statement into SQLTask. MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.6 Instances

A collection of all instances in MaxCompute. An instance is an element in a collection. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Instance i : odps.instances ()) { ....
```

`}` Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.7 Instance

A description of instance information. You can obtain a list of instances through Instances. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps (account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance ins = odps.instances().get("instance id"); Date startTime = instance.getStartTime(); Date endTime = instance.getEndTime(); ... Status instanceStatus = instance.getStatus(); String instanceStatusStr = null; if (instanceStatus == Status.TERMINATED) { instanceStatusStr = TaskStatus.Status.SUCCESS.toString(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { if (status.getValue().getStatus() ! = TaskStatus.Status.SUCCESS) { instanceStatusStr = status.getValue().getStatus().toString(); break;
```

`}` `}`

```
} else { instanceStatusStr = instanceStatus.toString();
```

`}`

```
... TaskSummary summary = instance.getTaskSummary("instance name"); String s = summary.getSummaryText();
```

Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.8 Tables

A collection of all tables in MaxCompute. A table is an element in a collection. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}` Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.9 Table

A description of table information. You can obtain a list of tables through Tables. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Table t = odps.tables().get("table name"); t.reload(); Partition part = t.getPartition(new PartitionSpec(tableSpec[1])); part.reload(); ...
```

Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.10 Resources

A collection of all resources in MaxCompute. A resource is an element in a collection. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Resource r : odps.resources()) { ....
```

`}` Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.11 Resource

A description of resource information. You can obtain a list of resources through Resources. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Resource r = odps.resources().get("resource name"); r.reload(); if (r.getType() == Resource.Type.TABLE) { TableResource tr = new TableResource(r); String tableSource = tr.getSourceTable().getProject() + "." + tr.getSourceTable().getName()
```

;

```
if (tr.getSourceTablePartition() ! = null) { tableSource += " partition(" + tr.getSourceTablePartition().toString() + ")";
```

`}`

```
....
```

`}` Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview. The following sample code shows how to create a file resource:

```
String projectName = "my_porject"; String source = "my_local_file.txt"; File file = new File(source); InputStream is = new FileInputStream(file); FileResource resource = new FileResource(); String name = file.getName(); resource.setName(name); odps.resources().create(projectName, resource, is);
```

The following sample code shows how to create a table resource:

```
TableResource resource = new TableResource(tableName, tablePrj, partitionSpec); //resource.setName(INVALID_USER_TABLE); resource.setName("table_resource_name"); odps.resources().update(projectName, resource);
```

#### 1.3.12 Functions

A collection of all functions in MaxCompute. A function is an element in a collection. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Function f : odps.functions()) { ....
```

`}` MaxCompute provides two endpoints. For more information, see Tunnel SDK overview.

#### 1.3.13 Function

A description of function information. You can obtain a list of functions through Functions. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Function f = odps.functions().get("function name"); List<Resource> resources = f.getResources();
```

Not e MaxCompute provides two endpoints. For more information, see Tunnel SDK overview. The following sample code shows how to create a function:

```
String resources = "xxx:xxx"; String classType = "com.aliyun.odps.mapred.open.example.WordCount"; ArrayList<String> resourceList = new ArrayList<String>(); for (String r : resources.split(":")) { resourceList.add(r);
```

`}`

```
Function func = new Function(); func.setName(name); func.setClassType(classType); func.setResources(resourceList); odps.functions().create(projectName, func);
```

#### 1.3.14 Spark Shell

An API commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the spark directory. $bin/spark-shell --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
sc.parallelize(0 to 100, 2).collect sql("show tables").show sql("select * from spark_user_data").show(200,100)
```

#### 1.3.15 Spark R

An API commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$mkdir -p /home/admin/R && unzip . /R/R.zip -d /home/admin/R/ -- Create a directory named R and decompress R.zip in the directory. $export PATH=/home/admin/R/bin/:$PATH -- Configure environment variables. $bin/sparkR --master yarn --archives . /R/R.zip -- Select a running mode and enable the API.
```

Sample code:

```
df <- as.DataFrame(faithful)
```

`df`

```
head(select(df, df$eruptions)) head(select(df, "eruptions")) head(filter(df, df$waiting < 50)) results <- sql("FROM spark_user_data SELECT *") head(results)
```

#### 1.3.16 Spark SQL

An API commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the spark directory. $bin/spark-sql --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
show tables; select * from spark_user_data limit 3; quit;
```

#### 1.3.17 Spark JDBC

An API commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$sbin/stop-thriftserver.sh -- Stop a thread. $sbin/start-thriftserver.sh -- Restart a thread. $bin/beeline -- Enable the API.
```

Sample code:

```
! connect jdbc:hive2://localhost:10000/odps_smoke_test show tables; select * from mr_input limit 3; ! quit
```

#### 1.3.18 Document APIs

An open-source API repository compatible with Elasticsearch on MaxCompute. For more information about the APIs, see the following link:

#### 1.3.19 Search APIs

An open-source API repository compatible with Elasticsearch on MaxCompute. For more information about the APIs, see the following link:

## 2 SDK for Python

This topic describes how to use SDK for Python to create, view, and delete tables. PyODPS is MaxCompute SDK for Python. PyODPS provides the DataFrame framework and basic operations on MaxCompute objects to allow you to easily analyze data in MaxCompute. For more information, visit GitHub and Docs that include details about all interfaces and classes. For more information about PyODPS, see MaxCompute User Guide. The following sections describe how to use SDK for Python to create, view, and delete tables. Not e The following examples are for reference only. Install PyODPS PyODPS supports Python 2.6 and later (including Python 3). After you install pip in the system, you only need to run the `pip install pyodps` command. The related dependencies of PyODPS are automatically installed. For more information, see the Inst allat ion guide section in MaxCompute User Guide. Perform initialization Use your Apsara Stack tenant account to initialize a MaxCompute entry object. Example:

```python
from odps import ODPS odps = ODPS('**your-access-id**', '**your-secret-access-key**', '**your-default-project**',
            endpoint='**your-end-point**')
```

After initialization, you can perform operations on tables, resources, and functions. Not e Unless otherwise specified, objects in the following sections all refer to MaxCompute entry objects. Obtain a PyODPS project A project is the basic organizational unit in MaxCompute, similar to a database. You can use the `get_project` method to obtain information about a project. Example:

```
project = odps.get_project('my_project') # Obtain information about a project. project = odps.get_project() # Obtain information about the default project.
```

Not e If no parameters are specified, information about the default project is obtained. You can use the exist_project method to check whether a project exists. A table is the data storage unit in MaxCompute. Perform operations on PyODPS tables Call `list_tables` to query all tables in a project. Example:

```
for table in odps.list_tables(): # Process each table.
```

Call `exist_table` to check whether a table exists. Call `get_table` to obtain information about a table.

```
 t = odps.get_table('dual')
 t.schema
odps.Schema {
  c_int_a                 bigint
  c_int_b                 bigint
  c_double_a              double
  c_double_b              double
  c_string_a              string
  c_string_b              string
  c_bool_a                boolean
  c_bool_b                boolean
  c_datetime_a            datetime
  c_datetime_b            datetime
```

`}`

```python
 t.lifecycle
 print(t.creation_time)
2014-05-15 14:58:43
 t.is_virtual_view
False
 t.size
 t.schema.columns
[<column c_int_a, type bigint>,
 <column c_int_b, type bigint>,
 <column c_double_a, type double>,
 <column c_double_b, type double>,
 <column c_string_a, type string>,
 <column c_string_b, type string>,
 <column c_bool_a, type boolean>,
 <column c_bool_b, type boolean>,
 <column c_datetime_a, type datetime>,
 <column c_datetime_b, type datetime>]
```

Create a schema for a PyODPS table Use one of the following methods to initialize the schema of a PyODPS table: Initialize the schema based on table columns and optional partitions.

```
 from odps.models import Schema, Column, Partition
 columns = [Column(name='num', type='bigint', comment='the column')]
 partitions = [Partition(name='pt', type='string', comment='the partition')]
 schema = Schema(columns=columns, partitions=partitions)
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

Call `Schema.from_lists` . Although this method is more convenient, you cannot directly set comments for columns and partitions.

```
 schema = Schema.from_lists(['num'], ['bigint'], ['pt'], ['string'])
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

Create a PyODPS table You can create a table based on the table schema. Example:

```
table = odps.create_table('my_new_table', schema) table = odps.create_table('my_new_table', schema, if_not_exists=True) # Create a table onl y if no table with the same name exists. table = o.create_table('my_new_table', schema, lifecycle=7) # Configure the lifecycle for a table.
```

You can also use a comma-connected string in the format of Field name, Field data type to create a table. Example:

```bash
 # Create a non-partitioned table.
 table = o.create_table('my_new_table', 'num bigint, num2 double', if_not_exists=True)
 # To create a partitioned table, you can specify (Table field list, Partition field list).
 table = o.create_table('my_new_table', ('num bigint, num2 double', 'pt string'), if_not_ex
ists=True)
```

By default, when you create a table, you can use only the following data types: BIGINT, DOUBLE, DECIMAL, STRING, DATETIME, BOOLEAN, MAP, and ARRAY. If you want to use other data types, such as TINYINT and STRUCT, set `options.sql.use_odps2_extension` to True. Example:

```python
 from odps import options
 options.sql.use_odps2_extension = True
 table = o.create_table('my_new_table', 'cat smallint, content struct<title:varchar(100), b
ody string>')
```

Obtain PyODPS table data Use one of the following methods to obtain table data: Call the `head` method to retrieve up to the first 10,000 data records in a table. Example:

```python
 t = odps.get_table('dual')
 for record in t.head(3):
     print(record[0])  # Obtain the value at position 0.
     print(record['c_double_a'])  # Obtain a value based on a field.
     print(record[0: 3])  # Perform slicing operations.
     print(record[0, 2, 3])  # Obtain values at multiple positions.
     print(record['c_int_a', 'c_double_a'])  # Obtain values based on multiple fields.
```

Call the `open_reader` method for a table to open a reader and read the table data. You can open the reader with or without a WITH clause.

```bash
# Open the reader with a WITH clause:
 with t.open_reader(partition='pt=test') as reader:
     count = reader.count
     for record in reader[5:10]  # You can execute the statement multiple times until all
records are read. The number of records is specified by count. You can change it to paral lel-operation code.
         # Process a record.
# Open the reader without a WITH clause:
 reader = t.open_reader(partition='pt=test')
 count = reader.count
 for record in reader[5:10]
     # Process a record.
```

Call the Tunnel API to read table data. The `open_reader` method is an encapsulation of the Tunnel API. Use PyODPS to write data Similar to `open_reader` , you can use `open_writer` for a table to open a writer and write data to a table. Example:

```bash
 # Open the writer with a WITH clause:
 with t.open_writer(partition='pt=test') as writer:
     writer.write(records)  # records can be iterable records and are written to block 0 by
default.
 with t.open_writer(partition='pt=test', blocks=[0, 1]) as writer:  # Enable two blocks.
     writer.write(0, gen_records(block=0))
     writer.write(1, gen_records(block=1))  # The two write operations can be performed in
parallel by using the multi-threading technology. Each block is independent.
 # Open the writer without a WITH clause:
 writer = t.open_writer(partition='pt=test', blocks=[0, 1])
 writer.write(0, gen_records(block=0))
 writer.write(1, gen_records(block=1))
 writer.close()  # You must close the writer. Otherwise, the written data may be incomplete
```

`.` Writing data to a table is an encapsulation of the Tunnel API. Delete a PyODPS table Delete a table. Example:

```
 odps.delete_table('my_table_name', if_exists=True)  # Delete a table only if the table exi
sts.
 t.drop()  # Directly drop a table if the table exists.
```

Perform operations on PyODPS table partitions Perform basic operations Traverse all partitions of a table. Example:

```python
 for partition in table.partitions:
     print(partition.name)
 for partition in table.iterate_partitions(spec='pt=test'):
     # Traverse subpartitions.
```

Check whether a partition exists. Example:

```
table.exist_partition('pt=test,sub=2019')
```

Obtain information about a partition. Example:

```python
 partition = table.get_partition('pt=test')
 print(partition.creation_time)
2019-09-18 22:22:27
 partition.size
```

Create a partition

```
t.create_partition('pt=test', if_not_exists=True) # Create a partition only if no partiti on with the same name exists.
```

Delete a partition

```
t.delete_partition('pt=test', if_exists=True) # Delete a partition only if the partition exists.
 partition.drop()  # Directly drop a partition if the partition exists.
```

PyODPS SQL PyODPS supports MaxCompute SQL queries and provides methods to obtain execution results. Run SQL statements

```
odps.execute_sql('select * from dual') # Execute the SQL statement in synchronous mode. Blocking continues until the execution of the SQL statement is complete. instance = odps.run_sql('select * from dual') # Execute the SQL statement in asynchronou s mode. instance.wait_for_success() # Blocking continues until the execution of the SQL statemen t is complete.
```

Obtain SQL query results You can directly call the `open_reader` method to obtain SQL query results. In the following example, structured data is returned.

```bash
 with odps.execute_sql('select * from dual').open_reader() as reader:
     for record in reader:
         # Process each record.
```

If the `desc` command is run, you can use the `reader.raw` method to obtain the raw SQL query results.

```python
 with odps.execute_sql('desc dual').open_reader() as reader:
     print(reader.raw)
```

PyODPS resources Resources commonly apply to UDFs and MapReduce on MaxCompute. You can call the `list_resources` method to query all resources, the `exist_resource` method to check whether a resource exists, and the `delete_resource` method to delete a resource. You can also call the `drop` method to delete a resource. PyODPS supports two resource types: files and tables. File resources Files of basic file types and the .py, jar, and .archive types are supported. Create a file resource You can specify a resource name, a file type, and a file-like or string object to create a file resource. Example:

```
resource = odps.create_resource('test_file_resource', 'file', file_obj=open('/to/path/f ile')) # Use a file-like object. resource = odps.create_resource('test_py_resource', 'py', file_obj='import this') # Us e a string.
```

Read and modify a file resource You can call the `open` method for a file resource or call the `open_resource` method at the MaxCompute entry to open a file resource. The opened object is a file-like object. Similar to the `o` `pen` method built in Python, file resources also support various opening modes. Example:

```
 with resource.open('r') as fp:  # Open the file in read mode.
    content = fp.read()  # Read all content.
     fp.seek(0)  # Return to the beginning of the resource.
     lines = fp.readlines()  # Read multiple lines.
     fp.write('Hello World')  # Error. Data cannot be written to a file in read mode.
 with odps.open_resource('test_file_resource', mode='r+') as fp:  # Open the file in re
ad/write mode.
     fp.read()
     fp.tell()  # Current position.
     fp.seek(10)
     fp.truncate()  # Truncate the file to the specified length.
     fp.writelines(['Hello\n', 'World\n'])  # Write multiple lines to the file.
     fp.write('Hello World')
     fp.flush()  # Manually calling the method to submit the update to MaxCompute.
```

PyODPS supports the following opening modes: r: read mode. The file can be opened but data cannot be written to it. w: write mode. Data can be written to the file, but data in the file cannot be read. If a file is opened in write mode, the file content is cleared first. a: append mode. Data can be added to the end of the file. r+: read/write mode. You can read data from and write data to the file. w+: This mode is similar to r+, but the file content is cleared first. a+: This mode is similar to r+, but data can only be written to the end of the file. In PyODPS, file resources can be opened in binary mode. For example, some compressed files must be opened in binary mode. rb indicates that a file is opened in binary read mode, and r+b indicates that a file is opened in binary read/write mode. Table resources Create a table resource

```
 odps.create_resource('test_table_resource', 'table', table_name='my_table', partition='p
t=test')
```

Update a table resource

```
 table_resource = odps.get_resource('test_table_resource')
 table_resource.update(partition='pt=test2', project_name='my_project2')
```

DataFrame PyODPS provides a pandas-like API called PyODPS DataFrame. This API makes full use of the computing power of MaxCompute. For more information, see DataFrame. The following DataFrame examples are provided for reference only. Not e You must create a MaxCompute object before you perform subsequent steps.

```
 odps = ODPS('**your-access-id**', '**your-secret-access-key**',
             project='**your-project**', endpoint='**your-end-point**'))
```

Assume that the following tables exist: pyodps_ml_100k_movies that contains movie-related data, pyodps_ml_100k_users that contains user-related data, and pyodps_ml_100k_ratings that contains rating-related data. You only need to specify a table object to create a DataFrame object. Example:

```
 from odps.df import DataFrame
 users = DataFrame(o.get_table('pyodps_ml_100k_users'))
```

You can use the dtypes attribute to view the fields of DataFrame and the types of these fields. Example:

```
users.dtypes
```

You can use the `head` method to obtain the first N data records for a quick data preview. Example:

```
 users.head(10)
```

|   | user id _ | age | sex | occupation | zip code _ |
|---|---|---|---|---|---|
| 0 | 1 | 24 | M | technician | 85711 |

| MaxCompute |   |   |   | Developer Gu | ide·SDK for Pytho |
|---|---|---|---|---|---|

|   | user id _ | age | sex | occupation | zip code _ |
|---|---|---|---|---|---|
| 1 | 2 | 53 | F | other | 94043 |
| 2 | 3 | 23 | M | writer | 32067 |
| 3 | 4 | 24 | M | technician | 43537 |
| 4 | 5 | 33 | F | other | 15213 |
| 5 | 6 | 42 | M | executive | 98101 |
| 6 | 7 | 57 | M | administrator | 91344 |
| 7 | 8 | 36 | M | administrator | 05201 |
| 8 | 9 | 29 | M | student | 01002 |
| 9 | 10 | 53 | M | lawyer | 90703 |

You can add a filter condition on the fields to view the required fields. Example:

```
 users[['user_id', 'age']].head(5)
```

|   | user id _ | age |
|---|---|---|
| 0 | 1 | 24 |
| 1 | 2 | 53 |
| 2 | 3 | 23 |
| 3 | 4 | 24 |
| 4 | 5 | 33 |

You can also exclude several fields from results. Example:

```
users.exclude('zip_code', 'age').head(5)
```

|   | user id _ | sex | occupation |
|---|---|---|---|
| 0 | 1 | M | technician |
| 1 | 2 | F | other |
| 2 | 3 | M | writer |
| 3 | 4 | M | technician |
| 4 | 5 | F | other |

If you exclude some fields, you may want to obtain new columns by using computation. For example, add the sex_bool attribute and set it to True if sex is M. Otherwise, set it to False.

```
users.select(users.exclude('zip_code', 'sex'), sex_bool=users.sex == 'M').head(5)
```

|   | user id _ | age | occupation | sex bool _ |
|---|---|---|---|---|
| 0 | 1 | 24 | technician | True |
| 1 | 2 | 53 | other | False |
| 2 | 3 | 23 | writer | True |
| 3 | 4 | 24 | technician | True |
| 4 | 5 | 33 | other | False |

Obtain the number of users aged between 20 and 25. Example:

```
users.age.between(20, 25).count().rename('count')
```

Obtain the numbers of male and female users. Example:

```
users.groupby(users.sex).count()
```

|   | sex | count |
|---|---|---|
| 0 | F | 273 |
| 1 | M | 670 |

To divide users by occupation, obtain the top 10 occupations, and sort the occupations in descending order based on population. Example:

```
df = users.groupby('occupation').agg(count=users['occupation'].count()) df.sort(df['count'], ascending=False)[:10]
```

|   | occupation | count |
|---|---|---|
| 0 | student | 196 |
| 1 | other | 105 |
| 2 | educator | 95 |
| 3 | administrator | 79 |
| 4 | engineer | 67 |

| MaxCompute |   | Developer Guide·SDK for Pytho |
|---|---|---|

|   | occupation | count |
|---|---|---|
| 5 | programmer | 66 |
| 6 | librarian | 51 |
| 7 | writer | 45 |
| 8 | executive | 32 |
| 9 | scientist | 31 |

The DataFrame API provides the value_counts method for the same purpose. Example:

```
users.occupation.value_counts()[:10]
```

|   | occupation | count |
|---|---|---|
| 0 | student | 196 |
| 1 | other | 105 |
| 2 | educator | 95 |
| 3 | administrator | 79 |
| 4 | engineer | 67 |
| 5 | programmer | 66 |
| 6 | librarian | 51 |
| 7 | writer | 45 |
| 8 | executive | 32 |
| 9 | scientist | 31 |

Show data in an intuitive graph. Example:

```
 %matplotlib inline
```

Use a horizontal column chart to visualize data. Example:

```
 users['occupation'].value_counts().plot(kind='barh', x='occupation',
ylabel='prefession')
```

Divide users into 30 groups by age and view the histogram of age distribution. Example:

```
users.age.hist(bins=30, title="Distribution of users' ages", xlabel='age', ylabel='count of users')
```

Use the join method to join three tables and save the joined tables as a new table. Example:

```
movies = DataFrame(o.get_table('pyodps_ml_100k_movies')) ratings = DataFrame(o.get_table('pyodps_ml_100k_ratings')) o.delete_table('pyodps_ml_100k_lens', if_exists=True) lens = movies.join(ratings).join(users).persist('pyodps_ml_100k_lens') lens.dtypes odps.Schema {
  movie_id                            int64
  title                               string
  release_date                        string
  video_release_date                  string
  imdb_url                            string
  user_id                             int64
  rating                              int64
  unix_timestamp                      int64
  age                                 int64
  sex                                 string
  occupation                          string
  zip_code                            string
```

`}` Divide users aged 0 to 80 into eight age groups. Example:

```
 labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
 cut_lens = lens[lens, lens.age.cut(range(0, 81, 10), right=False, labels=labels).rename('a
ge_group')]
```

View the first 10 data records of a single age in a group. Example:

```
cut_lens['age_group', 'age'].distinct()[:10]
```

|   | age group _ | age |
|---|---|---|
| 0 | 0-9 | 7 |
| 1 | 10-19 | 10 |
| 2 | 10-19 | 11 |
| 3 | 10-19 | 13 |
| 4 | 10-19 | 14 |
| 5 | 10-19 | 15 |
| 6 | 10-19 | 16 |
| 7 | 10-19 | 17 |

| MaxCompute |   | Developer Guide·SDK for Pytho |
|---|---|---|

|   | age group _ | age |
|---|---|---|
| 8 | 10-19 | 18 |
| 9 | 10-19 | 19 |

View the total rating and average rating of users in each age group. Example:

```
 cut_lens.groupby('age_group').agg(cut_lens.rating.count().rename('total_rating'), cut_lens
.rating.mean().rename('average_rating'))
```

|   | age group _ | average rating _ | total rating _ |
|---|---|---|---|
| 0 | 0-9 | 3.767442 | 43 |
| 1 | 10-19 | 3.486126 | 8181 |
| 2 | 20-29 | 3.467333 | 39535 |
| 3 | 30-39 | 3.554444 | 25696 |
| 4 | 40-49 | 3.591772 | 15021 |
| 5 | 50-59 | 3.635800 | 8704 |
| 6 | 60-69 | 3.648875 | 2623 |
| 7 | 70-79 | 3.649746 | 197 |

Configuration PyODPS provides a series of configuration options, which can be obtained by using `odps.options` . The following table describes configurable MaxCompute options. General configurations

| Option | Description | Default |
|---|---|---|
| end point _ | MaxCompute endpoint. | N/A |
| default project _ | The default project. | N/A |
| log view host _ _ | The hostname of Logview. | N/A |
| log view hours _ _ | The retention time of Logview. Unit: hours. | 24 |
| local timezone _ | The time zone. True indicates local time, and False indicates UTC. The pytz time zone can also be used. | 1 |
| lifecycle | The lifecycle of all tables. | N/A |

| veloper Guide·SDK for Python |   | MaxComput |
|---|---|---|
| Option | Description | Default |
| temp lifecycle _ | The lifecycle of temporary tables. | 1 |
| biz id _ | The ID of the user. | N/A |
| verbose | Specifies whether to display logs. | False |
| verbose log _ | The log receiver. | N/A |
| chunk size _ | The size of the write buffer. | 1496 |
| retry times _ | The number of request retries. | 4 |
| pool connections _ | The number of cached connections in the connection pool. | 10 |
| pool maxsize _ | The maximum capacity of the connection pool. | 10 |
| connect timeout _ | The time to wait before the connection times out. | 5 |
| read timeout _ | The time to wait before the read operation times out. | 120 |
| completion size _ | The limit on the number of object completion listing items. | 10 |
| notebook repr widget _ _ | Specifies whether to use interactive graphs. | True |
| sql.settings | MaxCompute SQL runs global hints. | N/A |
| sql.use odps2 extension _ _ | Specifies whether to enable MaxCompute V2.0 language extension. | False |

Data upload/download configurations

| Option | Description | Default |
|---|---|---|
| tunnel.endpoint | Tunnel endpoint. | N/A |
| tunnel.use instance tunnel _ _ | Specifies whether to use Instance Tunnel to obtain execution results. | True |

| Option | Description | Default |
|---|---|---|
| tunnel.limited instance tunnel _ _ | Specifies whether to limit the number of data records obtained by using Instance Tunnel. | True |
| tunnel.string as binary _ _ | Specifies whether to use bytes instead of unicode for data of the STRING type. | False |

DataFrame configurations

| Option | Description | Default |
|---|---|---|
| interactive | Specifies whether DataFrame is used in an interactive environment. | Depending on the measured value |
| df.analyze | Specifies whether to enable non-MaxCompute built-in functions. | True |
| df.optimize | Specifies whether to enable full DataFrame optimization. | True |
| df.optimizes.pp | Specifies whether to enable DataFrame predicate push optimization. | True |
| df.optimizes.cp | Specifies whether to enable DataFrame column pruning optimization. | True |
| df.optimizes.tunnel | Specifies whether to enable DataFrame tunnel optimization. | True |
| df.quote | Specifies whether to use a pair of grave accents (``) to mark fields and table names in the backend of MaxCompute SQL. | True |
| df.libraries | The resource name of the third- party library that is used for DataFrame operations. | N/A |

PyODPS ML configurations

| Option | Description | Default |
|---|---|---|
| ml.xflow project _ | The default XFlow project name. | algo public _ |

| Option | Description | Default |
|---|---|---|
| ml.use model transfer _ _ | Specifies whether to use ModelTransfer to obtain the model PMML. | True |
| ml.model volume _ | The volume name used when ModelTransfer is used. | pyodps volume _ |
