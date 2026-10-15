---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Developer Guide 20260826"
product_version: "V3.18.6_2607"
doc_version: "20260826"
pdf_pages: 552
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Developer Guide 20260826.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AE%A1%E7%AE%97%E6%9C%8D%E5%8A%A1%20MaxCompute/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20MaxCompute%20Developer%20Guide%2020260826.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Developer Guide 20260826

## Java SDK

### Java SDK

This document introduces the MaxCompute Java SDK packages and links to the complete API reference. Complete API reference for MaxCompute Use Maven to manage the SDK version. The following shows an example configuration.

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.36.2</version>
</dependency>
```

The MaxCompute SDK includes the following packages:

| Package name | Description |
|---|---|
| odps-sdk-core | Provides the core functionality of MaxCompute. This package encapsulates fundamental concepts and programming interfaces, such as Odps , Project , and Table , as well as Tunnel- related features. |
| odps-sdk-core-internal | Provides extended functionality for MaxCompute. It encapsulates less commonly used concepts and operations, such as Event and XFlow . |
| odps-sdk-commons | Provides infrastructure components for MaxCompute. It includes infrastructure elements such as TableSchema , Column , Record , and OdpsType , as well as various utilities. |
| odps-sdk-udf | Provides programming interfaces for MaxCompute UDFs. |
| odps-sdk-mapred | Provides programming interfaces for MaxCompute MapReduce jobs. |

To download an SDK package, go to Download SDK package.

**Note**

For the SDK packages provided for MaxCompute, if you use a MaxCompute version earlier than V3.8.0, download and use SDK package version **0.27.2**. If you use a MaxCompute version from V3.8.0 to V3.11.0, download and use SDK package version **0.30.8** or
**0.30.9**. If you use MaxCompute V3.12.0 or later, download and use SDK package version
**0.36.2**.

### Prerequisites

#### Overview

Before you use MaxCompute SDKs, you must prepare the required environment. Create an Alibaba Cloud account that is authorized to access MaxCompute and obtain an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. Obtain the endpoint of MaxCompute.

#### Obtain an AccessKey pair

##### Log on to the Apsara Uni-manager

**Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters such as the exclamation point (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%).
3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Manage MFA** section in **Apsara Uni-manager**
**Management Console User Guide**.

##### Obtain the AccessKey pair of an

**organization**

This topic describes how to obtain the AccessKey pair of an organization.

**Prerequisites**

Only the operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the Organizations navigation tree, find the organization that you want to add and click
the icon on the right of an organization.
5. Select **AccessKey** from the drop-down list.
6. In the message that appears, view the AccessKey pair of the organization.

**Note**

An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations of the level-1 organization use the AccessKey pair of the level-1 organization.

##### Obtain the AccessKey pair of an Alibaba

**Cloud account**

To ensure the security of cloud resources, the system must verify the identity of visitors and ensure that they have the relevant permissions. You must obtain the AccessKey ID and AccessKey secret of your Apsara Stack tenant to access cloud resources. This topic describes how to obtain the AccessKey pair of an Alibaba Cloud account.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

The AccessKey pair provides full access to cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

#### Obtain an endpoint

This topic describes how to obtain the endpoint of MaxCompute in the Apsara Uni-manager Operations Console.

**Background information**

The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser. In the address bar, enter the URL (ops.asconsole.intranet-domain-
id.com). Then, press Enter.

**Note**

You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, the password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
3. Click **Log On** to log on to the Apsara Uni-manager Operations Console.
4. In the top navigation bar of the Apsara Uni-manager Operations Console, click **O&M**. In the
left-side navigation pane, choose **Product Management > Products**. In the **Apsara**
**Stack O&M** section, click **Apsara Infrastructure Management Framework**.
5. In the left-side navigation pane, choose **Operations > Machine Operations**. The
**Machine Operations** page appears.
6. In the Machines search box, search for a machine. Click **Terminal** in the Actions column of
the machine to log on to the machine.
7. Run the following command on the machine to obtain JSON data:

```bash
curl -l "http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?c.sr.s ervice_registration"
```

8. Find the endpoint of MaxCompute based on the service ID (odps-service-frontend) and the
key value (odps_frontend_server.endpoint) of MaxCompute.

### Major APIs

#### AliyunAccount

This topic describes the AliyunAccount API provided by SDK for Java. You can call this API to obtain your Alibaba Cloud account. The input parameters are
**accessId** and **accessKey**. This API is also considered a class that is used to initialize
MaxCompute.

**Note**

**accessId** indicates the AccessKey ID that uniquely identifies an Alibaba
Cloud account. **accessKey** indicates the AccessKey secret that is used to authenticate the identity of the account.

#### Odps

This topic describes the Odps API provided by SDK for Java. This API is also considered a class that is the entry point of MaxCompute SDK for Java. This class allows you to access all types of objects in MaxCompute, including projects, tables, resources, functions, and instances. You can pass this class into the AliyunAccount instance to construct a MaxCompute object. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}`

#### Projects

This topic describes the Projects API provided by SDK for Java. This API is a collection of all projects in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Project p = odps.projects().get("my_exists"); p.reload(); Map<String, String> properties = prj.getProperties(); ...
```

#### Project

This topic describes the Project API provided by SDK for Java. This API provides descriptions of projects. You can call the Projects API to obtain the projects.

#### SQLTask

This topic describes the SQLTask API provided by SDK for Java. You can call this API to run and process SQL tasks. You can use SQLTask.run to run SQL tasks. SQLTask.run returns an instance, and obtains the running status and results of SQL tasks from the instance. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new O dps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance instance = SQLTask.run(odps, "my_project", "select ...") ; String id = instance.getId(); instance.waitforsuccess(); Set<String> taskNames = instance.getTaskNames(); for (String name taskNames) { TaskSummary summary = instance.getTaskSummary(name); String s = summary.getSummaryText();
```

`}`

```
Map<String, String> results = instance.getTaskResults(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { String result = results.get(status.getKey());
```

`}`

**Note**

To create a table, you must call the SQLTask API instead of the Table API. In this case, you must pass the CREATE TABLE statement into SQLTask.

#### Instances

This topic describes the Instances API provided by SDK for Java. This API is a collection of all instances in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Instance i : odps.instances ()) { ....
```

`}`

#### Instance

This topic describes the Instance API provided by SDK for Java. This API provides descriptions of instances. You can call the Instances API to obtain the instances. Sample code:

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

#### Tables

This topic describes the Tables API provided by SDK for Java. This API is a collection of tables in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}`

#### Table

This topic describes the Table API provided by SDK for Java. This API provides descriptions of tables in MaxCompute. You can call the Tables API to obtain the tables. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Table t = odps.tables().get("table name"); t.reload(); Partition part = t.getPartition(new PartitionSpec(tableSpec[1])); part.reload(); ...
```

#### Resources

This topic describes the Resources API provided by SDK for Java. This API is a collection of resources in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Resource r : odps.resources()) { ....
```

`}`

#### Resource

This topic describes the Resource API provided by SDK for Java. This API provides descriptions of resources. You can call the Resources API to obtain the resources. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Resource r = odps.resources().get("resource name"); r.reload(); if (r.getType() == Resource.Type.TABLE) { TableResource tr = new TableResource(r); String tableSource = tr.getSourceTable().getProject() + "." + tr.getSourceTable().getName(); if (tr.getSourceTablePartition() ! = null) { tableSource += " partition(" + tr.getSourceTablePartition().toString() + ")";
```

`}`

```
....
```

`}` The following sample code shows how to create a file resource:

```
String projectName = "my_porject"; String source = "my_local_file.txt"; File file = new File(source); InputStream is = new FileInputStream(file); FileResource resource = new FileResource(); String name = file.getName(); resource.setName(name); odps.resources().create(projectName, resource, is);
```

The following sample code shows how to create a table resource:

```
TableResource resource = new TableResource(tableName, tablePrj, partitionSpec); //resource.setName(INVALID_USER_TABLE); resource.setName("table_resource_name"); odps.resources().update(projectName, resource);
```

#### Functions

This topic describes the Functions API provided by SDK for Java. This API is a collection of functions in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Function f : odps.functions()) { ....
```

`}`

#### Function

This topic describes the Function API provided by SDK for Java. This API provides descriptions of functions. You can call the Functions API to obtain the functions. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Function f = odps.functions().get("function name"); List<Resource> resources = f.getResources();
```

The following sample code shows how to create a function:

```
String resources = "xxx:xxx"; String classType = "com.aliyun.odps.mapred.open.example.WordCount"; ArrayList<String> resourceList = new ArrayList<String>(); for (String r : resources.split(":")) { resourceList.add(r);
```

`}`

```
Function func = new Function(); func.setName(name); func.setClassType(classType); func.setResources(resourceList); odps.functions().create(projectName, func);
```

#### Spark Shell

This topic describes the Spark Shell API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the Spark directory. $bin/spark-shell --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
sc.parallelize(0 to 100, 2).collect sql("show tables").show sql("select * from spark_user_data").show(200,100)
```

#### Spark R

This topic describes the Spark R API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$mkdir -p /home/admin/R && unzip . /R/R.zip -d /home/admin/R/ -- Create a directory named R and decompress R.zip in the directory. $export PATH=/home/admin/R/bin/:$PATH -- Configure environment variables. $bin/sparkR --master yarn --archives . /R/R.zip -- Select the running mode and enable the API.
```

Sample code:

```
df <- as.DataFrame(faithful)
```

`df`

```
head(select(df, df$eruptions)) head(select(df, "eruptions")) head(filter(df, df$waiting < 50)) results <- sql("FROM spark_user_data SELECT *") head(results)
```

#### Spark SQL

This topic describes the Spark SQL API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the Spark directory. $bin/spark-sql --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
show tables; select * from spark_user_data limit 3; quit;
```

#### Spark JDBC

This topic describes the Spark JDBC API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$sbin/stop-thriftserver.sh -- Stop a thread. $sbin/start-thriftserver.sh -- Restart a thread. $bin/beeline -- Enable the API.
```

Sample code:

```
! connect jdbc:hive2://localhost:10000/odps_smoke_test show tables; select * from mr_input limit 3; ! quit
```

#### Document APIs

This topic describes the Document APIs provided by SDKs for Java. Document APIs are a set of open source APIs that are compatible with Elasticsearch on MaxCompute. For more information, see Document APIs.

#### Search APIs

This topic describes the Search APIs provided by SDK for Java. It is an open source API repository that is compatible with Elasticsearch on MaxCompute. For more information, see Search APIs.

#### CheckPermissionTest

This topic describes the CheckPermissionTest API provided by SDK for Java. You can call this API to check whether a specified user has the specified permission on a resource. Sample code:

```java
Account account = new AliyunAccount("accessId", "accessKey"); Odps odps = new Odps(account); SecurityManager sm = odps.projects().get().getSecurityManager(); SecurityManager.PermissionDesc desc = new SecurityManager.PermissionDesc(
    odps.getDefaultProject(),
    CheckPermissionConstants.ObjectType.Table,
    "table_name",
    CheckPermissionConstants.ActionType.Describe);
desc.setColumns(Arrays.asList("col1", "col2")); desc.setPrincipal("ALIYUN$test@aliyun.com"); SecurityManager.CheckPermissionResultInfo res = sm.checkPermission(desc); System.out.println("Result: " + res.getResult()); System.out.println("Message: " + res.getMessage());
```

#### Volume2

This topic describes the Volume2 API provided by SDK for Java. If you use the Volume2 API on Apsara Stack with type set to `new` , you do not need to specify Apsara Stack external volumn information, such as `extLocationt` .

**Project dependency**

Before you manage external volumes by using the SDK for Java, you need to add the following dependency:

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.44.0-SNAPSHOT</version>
</dependency>
```

**Create an external volume**

Create

```
/**
* Create an external volume.
* @param builder Parameter settings of the external volume
* @throws OdpsException
```

`*/`

```
public void create(VolumeBuilder builder) throws OdpsException
    /**
* Create an external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the
external volume for the VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @throws OdpsException
```

`*/`

```
public void create(String volumeName, String comment, Volume.Type type)
    /**
* Create an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the
external volume for the VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type)
    /**
* Create an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the
external volume for the VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @param lifecycle Lifecycle
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type, Long lifecycle) throws OdpsException
```

Example `/*`

```
 Create an external volume.
```

`*/`

```
public void createExternalVolume() throws Exception {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    String externalLocation = "oss://...";
    Long lifecycle;
    String comment;
    String roleArn;
    Volumes.VolumeBuilder builder = new Volumes.VolumeBuilder();
builder.project(projectName).volumeName(extVolumeName).type(Volume.Type.EXTERNAL).extLo tion(externalLocation);
    if (lifecycle != null) {
        builder.lifecycle(lifecycle);
```

`}`

```
    if (comment != null) {
        builder.comment(comment);
```

`}`

```
    if (roleArn != null) {
        builder.addProperty(Volumes.EXTERNAL_VOLUME_ROLEARN_KEY, roleArn);
```

`}`

```
    getCurrentOdps().volumes().create(builder);
```

`}`

**Obtain the information about a specified external volume**

Get

```
/**
* Obtain the information about a specified external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @return
```

`*/`

```
public Volume get(String volumeName) /**
* Obtain the information about a specified external volume.
```

`*`

```
* @param projectName Name of the project
* @param volumeName Name of the external volume
* @return
```

`*/`

```
public Volume get(String projectName, String volumeName)
```

Example `/*`

```
Obtain the information about a specified external volume.
```

`*/`

```
public Volume getVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    Volume volume = odps.volumes().get(projectName, extVolumeName);
    return volume;
```

`}`

**Obtain an external volume iterator**

Iterator

```
/**
* Obtain all external volume iterators of the default project.
```

`*`

```
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator()
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param projectName Name of the project
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final String projectName)
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param filter Filter condition
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final VolumeFilter filter)
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param projectName Name of the project
* @param filter Filter condition
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final String projectName, final VolumeFilter filter)
```

Example `/*`

```
Obtain an external volume iterator.
```

`*/`

```
public Iterator<Volume> getVolumeIterator() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    VolumeFilter volumeFilter = new VolumeFilter();
    volumeFilter.setName(extVolumeName);
    Iterator<Volume> iterator = odps.volumes().iterator(projectName, volumeFilter);
    return iterator;
```

`}`

**Delete an external volume**

Delete

```
/**
* Delete an external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @throws OdpsException
```

`*/`

```
public void delete(String volumeName) /**
* Delete an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @throws OdpsException
```

`*/`

```
public void delete(String projectName, String volumeName)
```

Example `/*`

```
Delete an external volume.
```

`*/`

```
public void deleteVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    try {
        odps.volumes().delete(projectName, extVolumeName);
    } catch (OdpsException e) {
        throw new RuntimeException(e);
```

`}` `}`

**Obtain the FS file of an external volume**

getVolumeFSFile

```
/**
* Obtain the FS file of an external volume from a path.
```

`*`

```
* @param path The path
```

`*` `*/`

```
public VolumeFSFile getVolumeFSFile(String path) throws VolumeException;
```

Example `/*`

```
Obtain detailed information about the FS file of an external volume.
```

`*/`

```
public void getVolumeIterator() {
    String projectName = "test_project";
    String volumeName = "test_volume";
    String testFilePath = "/" + volumeName + "/file";;
    VolumeFSFile volumeFSFile = odps.volumes().get(projectName,
volumeName).getVolumeFSFile(testFilePath);
    bool isDir = volumeFSFile.getIsdir());
    long length = volumeFSFile.getLength();
```

`}`

## SDK for Python

This topic describes how to use SDK for Python to create, view, and delete tables. PyODPS is MaxCompute SDK for Python. It provides easy-to-use Python programming interfaces. Similar to pandas, PyODPS provides fast, flexible, and expressive data structures. You can use the data processing feature of PyODPS, which is similar to that of pandas, by calling the DataFrame API provided by PyODPS. For more information, see aliyun-odpspython-sdk and PyODPS: ODPS Python SDK and data analysis framework. For more information about PyODPS, see the relevant description in MaxCompute User Guide. The following sections describe how to use SDK for Python to create, view, and delete tables.

**Install PyODPS**

PyODPS supports Python 2.6 and later (including Python 3.0). After you install pip in the system, you need only to run the `pip install pyodps` command. After you run this command, related dependencies of PyODPS are automatically installed. For more information, see the **Installation guide** section in MaxCompute User Guide.

**Perform initialization**

Use your Apsara Stack tenant account to initialize a MaxCompute entry object. Example:

```python
from odps import ODPS odps = ODPS('**your-access-id**', '**your-secret-access-key**', '**your-default-project
**',
            endpoint='**your-end-point**')
```

After initialization, you can perform operations on tables, resources, and functions.

**Note**

Unless otherwise specified, **objects** in the following sections all refer to MaxCompute entry objects.

**Obtain a PyODPS project**

A project is the basic organizational unit in MaxCompute, similar to a database.

| You can call the | get project _ | method to obtain information about a project. Example: |
|---|---|---|
| project = odps.get project('my project') # Obtain information about a project. _ _ project = odps.get project() # Obtain information about the default _ project. |   |   |

**Note**

If no parameters are specified, information about the default project is obtained. You can call the `exist_project` method to check whether a project exists. A table is the data storage unit in MaxCompute.

**Perform operations on PyODPS tables**

| Call the | list tables _ | method to query all tables in a project. Example: |
|---|---|---|
| for table in odps.list tables(): # Process each table. _ |   |   |

Call the `exist_table` method to check whether a table exists. Call the `get_table` method to obtain information about a table.

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

**Create the schema of a PyODPS table**

Use one of the following methods to initialize the schema of a PyODPS table: Initialize the schema by using table columns and optional partitions.

```
 from odps.models import Schema, Column, Partition
 columns = [Column(name='num', type='bigint', comment='the column')]
 partitions = [Partition(name='pt', type='string', comment='the partition')]
 schema = Schema(columns=columns, partitions=partitions)
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

Call the `Schema.from_lists` method. Although this method is more convenient, you cannot directly set comments for columns and partitions when you use this method.

```
 schema = Schema.from_lists(['num'], ['bigint'], ['pt'], ['string'])
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

**Create a PyODPS table**

You can use a table schema to create a table. Example:

```
table = odps.create_table('my_new_table', schema) table = odps.create_table('my_new_table', schema, if_not_exists=True) # Create a table only if no table with the same name exists. table = o.create_table('my_new_table', schema, lifecycle=7) # Set the lifecycle of the table.
```

You can also use a comma-delimited string of field names and field data types to create a table. Example:

```bash
 # Create a non-partitioned table.
 table = o.create_table('my_new_table', 'num bigint, num2 double', if_not_exists=True)
 # Create a partitioned table with table columns and partitions specified.
 table = o.create_table('my_new_table', ('num bigint, num2 double', 'pt string'), if_no
t_exists=True)
```

When you create a table, you can only use the BIGINT, DOUBLE, DECIMAL, STRING, DATETIME, BOOLEAN, MAP, and ARRAY data types, unless otherwise specified. To use other data types, such as TINYINT and STRUCT, you can set

| options.sql.use odps2 extension _ _ | to True. Example: |
|---|---|
| from odps import options options.sql.use odps2 extension = True _ _ table = o.create table('my new table', 'cat smallint, content _ _ _ struct<title:varchar(100), body string>') |   |

**Obtain PyODPS table data**

Use one of the following methods to obtain table data: Call the `head` method to retrieve up to the first 10,000 data records in a table. Example:

```python
 t = odps.get_table('dual')
 for record in t.head(3):
     print(record[0])  # Obtain the value at position 0.
     print(record['c_double_a'])  # Obtain a value based on a field.
     print(record[0: 3])  # Perform slicing operations.
     print(record[0, 2, 3])  # Obtain values at multiple positions.
     print(record['c_int_a', 'c_double_a'])  # Obtain values based on multiple fields
```

`.` Call the `open_reader` method for a table to open a reader and use the reader to read the table data. You can open the reader with or without a WITH clause.

```bash
# Open the reader with a WITH clause:
 with t.open_reader(partition='pt=test') as reader:
     count = reader.count
     for record in reader[5:10]  # You can execute the statement multiple times until
all records are read. The number of records is specified by count. You can change it to parallel-operation code.
         # Process a record.
# Open the reader without a WITH clause:
 reader = t.open_reader(partition='pt=test')
 count = reader.count
 for record in reader[5:10]
     # Process a record.
```

Call the Tunnel API to read table data. The `open_reader` method encapsulates the Tunnel API.

**Use PyODPS to write data**

Similar to `open_reader` , you can use `open_writer` for a table to open a writer and use the writer to write data to a table. Example:

```bash
 # Open the writer with a WITH clause:
 with t.open_writer(partition='pt=test') as writer:
     writer.write(records)  # records can be iterable records and are written to block
0 by default.
 with t.open_writer(partition='pt=test', blocks=[0, 1]) as writer:  # Enable two blocks
```

`.`

```bash
     writer.write(0, gen_records(block=0))
     writer.write(1, gen_records(block=1))  # The two write operations can be performed
at the same time by using the multithreading technology. Each block is independent.
 # Open the writer without a WITH clause:
 writer = t.open_writer(partition='pt=test', blocks=[0, 1])
 writer.write(0, gen_records(block=0))
 writer.write(1, gen_records(block=1))
 writer.close()  # You must close the writer. Otherwise, the written data may be incomp
lete.
```

Writing data to a table is a process that encapsulates the Tunnel API.

**Delete a PyODPS table**

Delete a table. Example:

```
 odps.delete_table('my_table_name', if_exists=True)  #  Delete a table only if the tabl
e exists.
 t.drop()  # Call the drop() method to delete a table if the table exists.
```

**Perform operations on PyODPS table partitions**

Basic operations Traverse all partitions of a table. Example:

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
t.create_partition('pt=test', if_not_exists=True) # Create a partition only if no par tition with the same name exists.
```

Delete a partition

```
t.delete_partition('pt=test', if_exists=True) # Delete a partition only if the parti tion exists.
 Use the drop() method to delete a partition only if the partition exists.
```

**PyODPS SQL**

PyODPS supports MaxCompute SQL queries and provides methods to obtain query results. Execute SQL statements

```
odps.execute_sql('select * from dual') # Execute SQL statements in synchronous mode . Threads are blocked until the SQL statements are executed. instance = odps.run_sql('select * from dual') # Execute SQL statements in asynchrono us mode. instance.wait_for_success() # Threads are blocked until the SQL statements are execu ted.
```

Obtain SQL query results You can call the `open_reader` method to obtain SQL query results. In the following example, structured data is returned.

```bash
 with odps.execute_sql('select * from dual').open_reader() as reader:
     for record in reader:
         # Process each record.
```

When you run the `DESC` command, you can use `reader.raw` to obtain the raw SQL query results.

```python
 with odps.execute_sql('desc dual').open_reader() as reader:
     print(reader.raw)
```

**PyODPS Resource**

Resources commonly apply to user-defined functions (UDFs) and MapReduce on MaxCompute.

|   | exist resource _ |
|---|---|
| delete resource _ |   |

You can call the `list_resources` method to query all resources, the `exist_resource` method to check whether a resource exists, and the `delete_resource` method to delete a resource. You can also call the `drop()` method to delete a resource. PyODPS supports two resource types: files and tables. File resources Files of basic file types and the .py, .jar, and .archive types are supported. Create a file resource You can specify a resource name, a file type, and a **file-like** or string object to create a file resource. Example:

```bash
resource = odps.create_resource('test_file_resource', 'file', file_obj=open('/to/path/file')) # Create a file-like object. resource = odps.create_resource('test_py_resource', 'py', file_obj='import this')
# Create a string object.
```

Read and modify a file resource You can call the `open` method for a file resource or call the `open_resource` method at the MaxCompute entry to open a file resource. The opened object is a **file-like** object. Similar to the `open` method built in Python, file resources also support various opening modes. Example:

```
 with resource.open('r') as fp:  # Open the file in read mode.
    content = fp.read()  # Read all content.
     fp.seek(0)  # Return to the beginning of the file.
     lines = fp.readlines()  # Read multiple lines.
     fp.write('Hello World')  # Error. Data cannot be written to a file in read mod
```

`e.`

```
 with odps.open_resource('test_file_resource', mode='r+') as fp:  # Open the file i
n read/write mode.
     fp.read()
     fp.tell()  # Current position.
     fp.seek(10)
     fp.truncate()  # Truncate the file to the specified length.
     fp.writelines(['Hello\n', 'World\n'])  # Write multiple lines into the file.
     fp.write('Hello World')
     fp.flush()  # Manually call the method to submit the update to MaxCompute.
```

PyODPS supports the following opening modes: r: read mode. The file can be opened but data cannot be written to it. w: write mode. Data can be written to the file, but data in the file cannot be read. If a file is opened in write mode, the file content is deleted first. a: append mode. Data can be appended to the file. r+: read/write mode. You can read data from and write data to the file. w+: This mode is similar to r+, but the file content is deleted first. a+: This mode is similar to r+, but data can only be appended to the file. In PyODPS, file resources can be opened in binary mode. For example, some compressed files must be opened in binary mode. **rb** indicates that a file is opened in binary read mode, and **r+b** indicates that a file is opened in binary read/write mode. Table resources Create a table resource.

```
 odps.create_resource('test_table_resource', 'table', table_name='my_table', partitio
n='pt=test')
```

Update a table resource.

```
 table_resource = odps.get_resource('test_table_resource')
 table_resource.update(partition='pt=test2', project_name='my_project2')
```

**DataFrame**

PyODPS provides a pandas-like API called PyODPS DataFrame. This API makes full use of the computing power of MaxCompute. For more information, see DataFrame. The following DataFrame examples are provided for reference only.

**Note**

You must create a MaxCompute object before you perform the following steps.

```
 odps = ODPS('**your-access-id**', '**your-secret-access-key**',
             project='**your-project**', endpoint='**your-end-point**'))
```

Assume that the following tables exist: **pyodps_ml_100k_movies** (movie-related data),
**pyodps_ml_100k_users** (user-related data), and **pyodps_ml_100k_ratings** (rating-related
data). You need only to specify a table object to create a DataFrame object. Example:

```
 from odps.df import DataFrame
 users = DataFrame(o.get_table('pyodps_ml_100k_users'))
```

You can use the **dtypes** attribute to view the fields of DataFrame and the types of these fields. Example:

```
users.dtypes
```

| You can call the | head | method to obtain the first N data records for data preview. Example: |
|---|---|---|
| users.head(10) |   |   |

| number | user id _ | age | sex | occupation | zip code _ |
|---|---|---|---|---|---|
| 0 | 1 | 24 | M | technician | 85711 |
| 1 | 2 | 53 | F | other | 94043 |
| 2 | 3 | 23 | M | writer | 32067 |
| 3 | 4 | 24 | M | technician | 43537 |
| 4 | 5 | 33 | F | other | 15213 |
| 5 | 6 | 42 | M | executive | 98101 |
| 6 | 7 | 57 | M | administrator | 91344 |

| 7 | 8 | 36 | M | administrator | 05201 |
|---|---|---|---|---|---|
| 8 | 9 | 29 | M | student | 01002 |
| 9 | 10 | 53 | M | lawyer | 90703 |

You can add a filter on the fields to view specified fields. Example:

```
 users[['user_id', 'age']].head(5)
```

| number | user id _ | age |
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

| number | user id _ | sex | occupation |
|---|---|---|---|
| 0 | 1 | M | technician |
| 1 | 2 | F | other |
| 2 | 3 | M | writer |
| 3 | 4 | M | technician |
| 4 | 5 | F | other |

If you exclude some fields, you may want to obtain new columns by using computation. For example, add the sex_bool attribute and set this attribute to True if sex is M. Otherwise, set this attribute to False. Example:

```
users.select(users.exclude('zip_code', 'sex'), sex_bool=users.sex == 'M').head(5)
```

| number | user id _ | age | occupation | sex bool _ |
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

| number | sex | count |
|---|---|---|
| 0 | F | 273 |
| 1 | M | 670 |

To divide users by occupation, obtain the top 10 occupations, and sort the occupations in descending order based on population. Example:

```
df = users.groupby('occupation').agg(count=users['occupation'].count()) df.sort(df['count'], ascending=False)[:10]
```

| number | occupation | count |
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

The DataFrame API provides the value_counts method for the same purpose. Example:

```
users.occupation.value_counts()[:10]
```

| number | occupation | count |
|---|---|---|
| 0 | student | 196 |
| 1 | other | 105 |
| 2 | educator | 95 |

| 3 | administrator | 79 |
|---|---|---|
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

Use JOIN to join three tables and save the joined tables as a new table. Example:

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

`}` Divide users who are aged from 0 to 80 into eight age groups. Example:

```
 labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
 cut_lens = lens[lens, lens.age.cut(range(0, 81, 10), right=False,
labels=labels).rename('age_group')]
```

View the first 10 data records of a single age in a group. Example:

```
cut_lens['age_group', 'age'].distinct()[:10]
```

| number | age group _ | age |
|---|---|---|
| 0 | 0-9 | 7 |
| 1 | 10-19 | 10 |
| 2 | 10-19 | 11 |
| 3 | 10-19 | 13 |
| 4 | 10-19 | 14 |
| 5 | 10-19 | 15 |
| 6 | 10-19 | 16 |
| 7 | 10-19 | 17 |
| 8 | 10-19 | 18 |
| 9 | 10-19 | 19 |

View the total rating and average rating of users in each age group. Example:

```
 cut_lens.groupby('age_group').agg(cut_lens.rating.count().rename('total_rating'), cut_
lens.rating.mean().rename('avg_rating'))
```

| number | age group _ | average rating _ | total rating _ |
|---|---|---|---|
| 0 | 0-9 | 3.767442 | 43 |
| 1 | 10-19 | 3.486126 | 8181 |
| 2 | 20-29 | 3.467333 | 39535 |
| 3 | 30-39 | 3.554444 | 25696 |
| 4 | 40-49 | 3.591772 | 15021 |
| 5 | 50-59 | 3.635800 | 8704 |
| 6 | 60-69 | 3.648875 | 2623 |
| 7 | 70-79 | 3.649746 | 197 |

**Configurations**

PyODPS provides a series of configuration options, which can be obtained by using `odps.options` . The following table describes configurable MaxCompute options. General configurations

| Option | Description | Default value |
|---|---|---|
| end point _ | MaxCompute Endpoint | None |
| default project _ | The default project. | None |
| log view host _ _ | The hostname of Logview. | None |
| log view hours _ _ | The retention time of Logview. Unit: hours. | 24 |
| local timezone _ | The time zone to be used. True indicates local time, and False indicates UTC. You can also use the pytz time zone. | 1 |
| lifecycle | The lifecycle of all tables. | None |
| temp lifecycle _ | The lifecycle of temporary tables. | 1 |
| biz id _ | The ID of a user. | None |
| verbose | Specifies whether to display logs. | False |
| verbose log _ | The log receiver. | None |
| chunk size _ | The size of the write buffer. | 1496 |
| retry times _ | The number of request retries. | 4 |
| pool connections _ | The number of cached connections in the connection pool. | 10 |
| pool maxsize _ | The maximum capacity of the connection pool. | 10 |
| connect timeout _ | The time to wait before the connection times out. | 5 |
| read timeout _ | The time to wait before the read operation times out. | 120 |
| completion size _ | The limit on the number of object completion listing items. | 10 |
| notebook repr widget _ _ | Specifies whether to use interactive graphs. | True |
| sql.settings | MaxCompute SQL runs global hints. | None |

| sql.use odps2 extension _ _ | Specifies whether to enable MaxCompute V2.0 language extension. | False |
|---|---|---|

Data upload and download configurations

| Option | Description | Default value |
|---|---|---|
| tunnel.endpoint | Tunnel Endpoint | None |
| tunnel.use instance tunnel _ _ | Specifies whether to use Instance Tunnel to obtain the upload or download results. | True |
| tunnel.limited instance tunnel _ _ | Specifies whether to limit the number of data records obtained by using Instance Tunnel. | True |
| tunnel.string as binary _ _ | Specifies whether to use bytes instead of unicode for data of the STRING type. | False |

DataFrame configurations

| Option | Description | Default value |
|---|---|---|
| interactive | Specifies whether DataFrame is used in an interactive environment. | Based on the measured value |
| df.analyze | Specifies whether to enable non-MaxCompute built-in functions. | True |
| df.optimize | Specifies whether to enable full DataFrame optimization. | True |
| df.optimizes.pp | Specifies whether to enable DataFrame predicate push optimization. | True |
| df.optimizes.cp | Specifies whether to enable DataFrame column pruning optimization. | True |
| df.optimizes.tunnel | Specifies whether to enable DataFrame tunnel optimization. | True |
| df.quote | Specifies whether to use a double grave accent (``) to mark fields and table names in the backend of MaxCompute SQL. | True |
| df.libraries | The resource name of the third-party library that is used for the DataFrame operation. | None |

PyODPS ML configurations

| Option | Description | Default value |
|---|---|---|
| ml.xflow project _ | The default name of the XFlow project. | algo public _ |
| ml.use model transfer _ _ | Specifies whether to use ModelTransfer to obtain the PMML model. | True |
| ml.model volume _ | The volume name used when ModelTransfer is used. | pyodps volume _ |

## MaxCompute SQL

### Overview

#### Scenarios

This topic describes the scenarios of MaxCompute SQL.

**Introduction**

**Applicable scenarios**

MaxCompute SQL offline computing is applicable to scenarios where you need to process terabytes of data but do not require real-time processing. It requires a relatively long time to prepare and submit jobs for MaxCompute SQL offline computing. Therefore, MaxCompute SQL is not well-suited for scenarios where thousands or even tens of thousands of transactions need to be processed per second. MaxCompute SQL online computing provides near real-time (NRT) processing capabilities.

**Usage notes**

The MaxCompute SQL syntax is similar to the SQL syntax. The MaxCompute SQL syntax can be considered a subset of standard SQL. MaxCompute SQL lacks many database features, such as transactions, primary key constraints, and indexes. Therefore, MaxCompute SQL cannot be regarded as a database. The maximum size of each SQL statement supported by MaxCompute is `2 MB` .

#### Reserved words

The keywords of SQL statements are reserved words in MaxCompute. Do not use the reserved words when you name tables, columns, or partitions. If you use the reserved words, an error is reported. Reserved words are not case-sensitive.

**List of reserved words**

The following table lists common reserved words. For a complete list of reserved words, see Reserved words and keywords.

| Category | Reserved word |
|---|---|

| Special symbols | % & && ( ) * + - . / ; < <= <> = > >= ? |
|---|---|
| DDL and table operations | ADD ALTER COLUMN COMMENT CREATE DROP LIFECYCLE PARTITION RENAME REPLACE TABLE TOUCH VIEW |
| DML and data operations | FROM INSERT INTO OVERWRITE SELECT WHERE |

| Query, join, and sort operations | ALL ASC BY DESC DISTINCT DISTRIBUTE FULL GROUP JOIN LEFT LIMIT MAPJOIN ON ORDER OUTER RIGHT SORT UNION |
|---|---|
| Logic and conditions | AND BETWEEN CASE ELSE FALSE IF IN IS LIKE NOT NULL OR RLIKE THEN TRUE WHEN |

| Data types | BIGINT BOOLEAN CAST DOUBLE STRING |
|---|---|
| Other keywords | AS |

#### Partitioned tables

This topic introduces the usage notes and limits for MaxCompute partitioned tables to ensure proper usage.

**Instructions for partitioned tables**

You can specify a partition key column as a filter condition in the WHERE clause of a `SELECT` statement. This provides the following benefits: Improves SQL execution efficiency. Locates the required data range precisely and reduces I/O overhead and computing resource consumption.

**Usage notes**

Some SQL statements for partition operations are less efficient: For example, if more than 10,000 partitions exist in an output table for a job, a large number of parallel operations are performed to write data to partitions. As a result, the SQL statements may fail. When you use partitioned tables, evaluate the number of partitions and partition levels based on the data source to avoid performance and stability issues. MaxCompute allows a maximum of six levels of partitions in a partitioned table. The statements that are used to process partitioned and non-partitioned tables are different in MaxCompute. For more information, see DDL statements and DML statements. For more information about the statements that are used to create tables, see Create a table.

#### Type conversion

##### Explicit conversions of data types

An explicit conversion uses CAST to convert a value type into another one. This topic describes explicit conversions.

**Explicit conversion description**

The following table lists the explicit conversions supported by MaxCompute SQL. For more information about CAST, see CAST.

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|

| BIGINT | N/A | Y | Y | N | N | Y |
|---|---|---|---|---|---|---|
| DOUBLE | Y | N/A | Y | N | N | Y |
| STRING | Y | Y | N/A | Y | N | Y |
| DATETIME | N | N | Y | N/A | N | N |
| BOOLEAN | N | N | N | N | N/A | N |
| DECIMAL | Y | Y | Y | N | N | N/A |

Y indicates that the conversion is supported. N indicates that the conversion is not supported. N/A indicates that the conversion is not required.

|   | Note If the DOUBLE type is converted into the BIGINT type, the fractional part is truncated. Example: CAST(1.6 AS BIGINT) = 1. If the STRING type that meets the format of the DOUBLE type is converted into the BIGINT type, the STRING type is first converted into the DOUBLE type and then to the BIGINT type. Therefore, the fractional part is truncated. Example: CAST("1.6" AS BIGINT) = 1 . If the STRING type that meets the format of the BIGINT type is converted into the DOUBLE type, one digit is retained after the decimal point. Example: CAST("1" AS DOUBLE) = 1.0 . To convert a constant string into the DECIMAL type, enclose the constant string within a pair of double quotation marks ("). If the value is not enclosed in quotation marks, it is considered a DOUBLE-type value. Example: CAST("1.234567890123456789" AS DECIMAL). An unsupported explicit conversion causes an exception. If a conversion fails, the system returns an error and exits. The conversion of the DATETIME type uses the default format yyyy-mm-dd hh:mi:ss:ff3. For more information, see Conversions between the STRING and DATETIME types. Some data types cannot be explicitly converted, but can be converted by using SQL built-in functions. For example, you can use the TO CHAR function to convert _ the BOOLEAN type into the STRING type. For more information, see TO CHAR. You _ can also use the TO DATE function to convert the STRING type into the DATETIME _ type. If the values of the DECIMAL type are not within the value range, the CAST(STRING TO DECIMAL) operation may return an error, such as most significant bit overflow or least significant bit overflow truncation. |   |   |
|---|---|---|---|
|   |   | CAST("1.6" |   |
|   | DOUBLE) = 1.0 |   |   |
|   | TO DECIMAL) |   |   |

|   | AS BIGINT) = 1 |
|---|---|

| CAST("1" AS |   |
|---|---|

| CAST(STRING |   |
|---|---|

##### Implicit type conversion and its application

**scope**

An implicit type conversion allows MaxCompute to automatically convert data types based on the context and predefined rules. This topic describes the rules of implicit type conversions.

**Implicit type conversions**

The following table lists the rules of implicit type conversions supported by MaxCompute.

| From/To | BOOLEAN | TINYINT | SMALLINT | INT | BIGINT | FLOAT |
|---|---|---|---|---|---|---|
| BOOLEAN | T | F | F | F | F | F |
| TINYINT | F | T | T | T | T | T |
| SMALLINT | F | F | T | T | T | T |
| INT | F | F | F | T | T | T |
| BIGINT | F | F | F | F | T | T |
| FLOAT | F | F | F | F | F | T |
| DOUBLE | F | F | F | F | F | F |
| DECIMAL | F | F | F | F | F | F |
| STRING | F | F | F | F | F | F |
| VARCHAR | F | F | F | F | F | F |
| TIMESTA MP | F | F | F | F | F | F |
| BINARY | F | F | F | F | F | F |

| From/To | DOUBLE | DECIMAL | STRING | VARCHAR | TIMESTA MP | BINARY |
|---|---|---|---|---|---|---|

| BOOLEAN | F | F | F | F | F | F |
|---|---|---|---|---|---|---|
| TINYINT | T | T | T | T | F | F |
| SMALLINT | T | T | T | T | F | F |
| INT | T | T | T | T | F | F |
| BIGINT | T | T | T | T | F | F |
| FLOAT | T | T | T | T | F | F |
| DOUBLE | T | T | T | T | F | F |
| DECIMAL | F | T | T | T | F | F |
| STRING | T | T | T | T | F | F |
| VARCHAR | T | T | T | T | F | F |
| TIMESTA MP | F | F | T | T | T | F |
| BINARY | F | F | F | F | F | T |

T indicates that the conversion is supported. F indicates that the conversion is not supported.

**Note**

If an unsupported implicit type conversion is performed, an error is returned. If a conversion fails, the system returns an error and exits. MaxCompute automatically performs implicit type conversions on data types based on the context. If the types do not match, you can use the CAST function to explicitly convert data types. The rules of implicit type conversions apply to specific scopes. In specific scenarios, only some rules take effect.

**Implicit type conversions with relational operators**

Relational operators include =, <>, <, ≤, >, ≥, IS NULL, IS NOT NULL, LIKE, RLIKE, and IN. The following section describes the rules of implicit type conversions when relational operations are used for data of different types.

**Implicit type conversions with relational operators**

The rules for implicit type conversions that use LIKE, RLIKE, and IN are different from those that use other relational operators. The rules described in this section do not apply to the three operators.

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|
| BIGINT | N/A | DOUBLE | DOUBLE | N | N | DECIMAL |
| DOUBLE | DOUBLE | N/A | DOUBLE | N | N | DECIMAL |
| STRING | DOUBLE | DOUBLE | N/A | DATETIME | N | DECIMAL |
| DATETIME | N | N | DATETIME | N/A | N | N |
| BOOLEAN | N | N | N | N | N/A | N |
| DECIMAL | DECIMAL | DECIMAL | DECIMAL | N | N | N/A |

**Note**

If an implicit type conversion is not supported between two values that you want to compare, the relational operation cannot be performed and an error is returned. For more information about relational operators, see Relational operators.

**Implicit type conversions with special relational operators**

Special relational operators include LIKE, RLIKE, and IN.

**Syntax of LIKE and RLIKE**

```
Source LIKE Pattern; Source RLIKE Pattern;
```

Take note of the following points for the two relational operators in implicit type conversions: The **Source** and **Pattern** parameters of LIKE and RLIKE must be of the STRING type. Other types can neither be involved in the operation nor be implicitly converted into the STRING type. If the value of **Source** or **Pattern** is NULL, NULL is returned.

**Syntax of IN**

```
key IN (value1, value2,…);
```

Rules of implicit type conversions for IN: The data types of the **values** on the right of the IN keyword must be consistent. MaxCompute automatically compares the values in the column specified by **key** with
**values** on the right of the IN keyword. If these values are of the BIGINT, DOUBLE, and
STRING types, the values are converted into the DOUBLE type for comparison. If these values are of the DATETIME and STRING types, the values are converted into the DATETIME type for comparison. Conversions between other types are not allowed.

**Note**

The memory used by the compiler increases with the number of parameters used in the IN operation. If 5,000 parameters are used in an IN operation, the GCC compiler consumes 17 GB of memory for compilation. We recommend that you limit the number of parameters to 1,024. In this case, the compiler consumes a maximum of 1 GB of memory and requires 39 seconds for compilation.

**Implicit type conversions with arithmetic operators**

Arithmetic operators include addition (+), subtraction (−), multiplication (×), division (/), and percent (%). This section describes the rules for implicit type conversions that use these operators. Only the STRING, BIGINT, DECIMAL, and DOUBLE types can be used in arithmetic operations. Before an arithmetic operation, STRING data is implicitly converted into DOUBLE data. If an arithmetic operation involves data of the BIGINT and DOUBLE types, BIGINT data is implicitly converted into DOUBLE data. The DATETIME and BOOLEAN types cannot be used in arithmetic operations.

**Note**

For more information about arithmetic operators, see Arithmetic operators.

**Implicit type conversions with logical operators**

Logical operators include AND, OR, and NOT. This section describes the rules for implicit type conversions that use these operators. Only the BOOLEAN type can be used in logical operations. The other types are not supported by logical operations or implicit type conversions.

**Note**

For more information about logical operators, see Logical operators.

##### SQL built-in functions

MaxCompute SQL provides a variety of built-in functions. These functions can be used to calculate one or more columns of a row and provide data of any type.

**Conversion rules**

If you call a function and the data type of an input parameter is different from that defined in the function, the data type of the input parameter is converted into the function-defined data type. The support for implicit type conversions of parameters differs for each MaxCompute SQL built-in function. For more information, see Built-in functions.

##### CASE WHEN

This topic describes the implicit type conversion rules for CASE WHEN.

**Conversion rules**

CASE WHEN uses the following implicit type conversion rules: If return values are of the BIGINT and DOUBLE types, all the values are converted into the DOUBLE type. If return values include those of the STRING type, all the values are converted into the STRING type. If a conversion, such as conversion from BOOLEAN into STRING, fails, an error is returned. Conversions between other types are not allowed.

##### Conversions between the STRING and

**DATETIME types**

MaxCompute supports conversions between the STRING and DATETIME types. This topic describes the format specifications, valid values, and usage notes for these conversions.

**Conversion format**

The format used in conversions is **yyyy-mm-dd hh:mi:ss.ff3**.

**Valid values for units**

| Time unit | String (case- insensitive) | Valid value |
|---|---|---|
| Year | yyyy | 0001 to 9999 |
| Month | mm | 01 to 12 |
| Day | dd | 01 to 31 |
| Hour | hh | 00 to 23 |
| Minute | mi | 00 to 59 |
| Second | ss | 00 to 59 |
| Millisecond | ff3 | 00 to 999 |

**Usage notes**

If the first digit of a valid value for each time unit is 0, 0 cannot be omitted. For example,
**2017-1-9 12:12:12** is an invalid DATETIME format and it cannot be converted from the
STRING type into the DATETIME type. It must be written as **2017-01-09 12:12:12**. Only the STRING type that meets the preceding format requirements can be converted into the DATETIME type. For example, **cast("2017-12-31 02:34:34" as datetime)** converts
**2017-12-31 02:34:34** of the STRING type into the DATETIME type. Similarly, if the
DATETIME type is converted into the STRING type, the default conversion format is **yyyy-**
**mm-dd hh:mi:ss**. Conversions that use the following or similar statements may fail, and
errors are returned.

```
CAST("2017/12/31 02/34/34" AS datetime); CAST("20171231023434" AS datetime); CAST("2017-12-31 2:34:34" AS datetime);
```

MaxCompute provides the TO_DATE function to convert the STRING type that does not meet the DATETIME format requirements into the DATETIME type. For more information, see TO_DATE.

### Operators

#### Relational operators

This topic describes the relational operators in MaxCompute SQL operators.

**Relational operators**

| Operator | Description |
|---|---|
| A=B | If A or B is NULL, NULL is returned. If A is equal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A<>B | If A or B is NULL, NULL is returned. If A is unequal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A<B | If A or B is NULL, NULL is returned. If A is less than B, TRUE is returned. Otherwise, FALSE is returned. |
| A<=B | If A or B is NULL, NULL is returned. If A is less than or equal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A>B | If A or B is NULL, NULL is returned. If A is greater than B, TRUE is returned. Otherwise, FALSE is returned. |
| A>=B | If A or B is NULL, NULL is returned. If A is greater than or equal to B, TRUE is returned. Otherwise, FALSE is returned. |

| A IS NULL | If A is NULL, TRUE is returned. Otherwise, FALSE is returned. |
|---|---|
| A IS NOT NULL | If A is not NULL, TRUE is returned. Otherwise, FALSE is returned. |
| A LIKE B | If A or B is NULL, NULL is returned. A is a string, and B is the pattern that you want to match. If A matches B, TRUE is returned. Otherwise, FALSE is returned. The percent sign (%) is a wildcard character that matches an arbitrary number of characters. The underscore ( ) is a wildcard character that matches a single _ character. To use these two characters as regular characters, use backslashes (\) to escape them: \% and \ . _ 'aaa' LIKE 'a' = FALSE 'aaa' LIKE 'a%' = TRUE 'aaa' LIKE 'aab' = FALSE 'a%b' LIKE 'a\%b' = TRUE 'axb' LIKE 'a\%b' = FALSE |
| A RLIKE B | If A or B is NULL, NULL is returned. A is a string, and B is a regular expression consisting of string constants. If A matches B, TRUE is returned. Otherwise, FALSE is returned. If B is an empty string, the system returns an error and exits. |
| A IN B | B is a set. If A is NULL, NULL is returned. If A is in B, TRUE is returned. Otherwise, FALSE is returned. If B contains only one element NULL, namely, A IN (NULL), NULL is returned. If B contains NULL, the type of NULL is considered the same as the other elements in B. B must be a constant and have at least one element. All elements must be of the same type. |

**Usage notes**

The values of the DOUBLE type in MaxCompute are different in precision. We recommend that you do not use the equal sign (=) for comparison between two values of the DOUBLE type. You can deduct a value of the DOUBLE type from the other value of the DOUBLE type and use the absolute value of the difference to determine whether the two values are equal. If the absolute value is negligible, the two values of the DOUBLE type are considered equal. Example:

```
ABS(0.9999999999 - 1.0000000000) < 0.000000001 -- 0.9999999999 and 1.0000000000 have 10-digit precision, while 0.000000001 has 9-digit precision. -- In this case, the system considers 0.9999999999 and 1.0000000000 equal.
```

**Note**

ABS is a built-in function provided by MaxCompute to take the absolute value of its input. For more information, see ABS. In most cases, a value of the DOUBLE type in MaxCompute can retain 16 valid digits.

#### Arithmetic operators

This topic describes arithmetic operators in MaxCompute SQL operators.

**List of arithmetic operators**

| Operato r | Description |
|---|---|
| A + B | If A or B is NULL, NULL is returned. Otherwise, the result of A + B is returned. |
| A – B | If A or B is NULL, NULL is returned. Otherwise, the result of A - B is returned. |
| A * B | If A or B is NULL, NULL is returned. Otherwise, the result of A × B is returned. |
| A / B | If A is NULL, B is NULL, or B is 0 , NULL is returned. Otherwise, the result of A/B is returned. Note If both A and B are of the BIGINT type, a value of the DOUBLE type is returned. |
| A % B | If A or B is NULL, NULL is returned. Otherwise, the result of A % B is returned. |
| +A | A is returned. |
| -A | If A is NULL, NULL is returned. Otherwise, -A is returned. |

**Note**

You can use only the values of the STRING, BIGINT, DOUBLE, or DECIMAL type to perform arithmetic operations. You cannot use the values of the DATETIME or BOOLEAN type to perform arithmetic operations. Values of the STRING type are implicitly converted into values of the DOUBLE type before arithmetic operations. If you use the values of the BIGINT and DOUBLE types to perform arithmetic operations, the value of the BIGINT type is implicitly converted into the value of the DOUBLE type before arithmetic operations. A value of the DOUBLE type is returned. If both A and B are of the BIGINT type, a value of the DOUBLE type is returned after you perform the A/B operation. For other arithmetic operations, a value of the BIGINT type is returned.

#### Bitwise operators

This topic describes bitwise operators in MaxCompute SQL operators.

**List of bitwise operators**

| Operat or | Description |
|---|---|
| A & B | The bitwise AND result of A and B is returned. For example, the result of 1&2 is 0, and the result of 1&3 is 1. The bitwise AND result of NULL and a value is NULL. Both A and B must be of the BIGINT type. |
| A \| B | The bitwise OR result of A and B is returned. For example, the result of 1\|2 is 3, and the result of 1\|3 is 3. The bitwise OR result of NULL and a value is NULL. Both A and B must be of the BIGINT type. |

**Important**

Bitwise operators do not support implicit type conversions. You can use the values only of the BIGINT type in bitwise operations.

#### Logical operators

This topic describes the operation rules and type constraints of the `AND` , `OR` , and `NOT` logical operators in MaxCompute SQL.

**Operation rules**

| Operator | Description |
|---|---|
| A and B | TRUE and TRUE = TRUE |
|   | TRUE and FALSE = FALSE |
|   | FALSE and TRUE = FALSE |
|   | FALSE and NULL = FALSE |
|   | FALSE and FALSE = FALSE |
|   | NULL and FALSE = FALSE |
|   | TRUE and NULL = NULL |
|   | NULL and TRUE = NULL |
| 0 | > Document Version: 2026082 |

|   | NULL and NULL = NULL |
|---|---|
|   | TRUE or TRUE = TRUE |
|   | TRUE or FALSE = TRUE |
|   | FALSE or TRUE = TRUE |
| A or B |   |
|   | FALSE or NULL = NULL |
|   | NULL or FALSE = NULL |
|   | TRUE or NULL = TRUE |
|   | NULL or TRUE = TRUE |
|   | NULL or NULL = NULL |
| NOT A | If A is NULL, NULL is returned. |
|   | If A is TRUE, FALSE is returned. |
|   | If A is FALSE, TRUE is returned. |

**Note**

Logical operators do not support implicit type conversions. You can use only the values of the BOOLEAN type in logical operations.

### LOAD

This topic describes how to use LOAD statements to import data from external storage, such as Object Storage Service (OSS), to a table or a table partition in MaxCompute.

**Precautions**

MaxCompute must be authorized to access data in external storage. The methods used to authorize MaxCompute to access external data by using LOAD statements are the same as the methods used to authorize MaxCompute external tables. You can use one of the following methods for authorization: Specify the AccessKey ID and AccessKey secret in the directory in which data is stored. In this example, a directory on OSS is used.

```
'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhouzmf.aliyuncs.com/my_bucket_id/my_location/'
```

**Important**

If you use this authorization method, you must use the plaintext of the AccessKey ID and AccessKey secret. This may pose security risks. We recommend that you do not use this method. Use Security Token Service (STS). For more information about the STS mode authorization for OSS, see STS mode authorization for OSS.

**Use an extractor or a storage handler to import data**

Syntax

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [STORED BY StorageHandler] [WITH SERDEPROPERTIES (Options)];
```

Parameters:
**table_name**: the name of the destination table into which you want to insert data. You
must create a destination table before you insert data into the table. The schema of the destination table must be the same as the format of the external data.
**LOAD INTO**: inserts data into a table or partition.
**LOAD OVERWRITE**: clears the existing data from a table or partition and inserts data into
the table or partition.
**SORTED BY**: specifies the name of the storage handler. You can use this clause in the
same way as you use the clause for MaxCompute external tables.
**LOCATION**: specifies the OSS directory in which the data files you want to read are saved.
The system reads all files in the directory by default.
**WITH SERDEPROPERTIES**: specifies the properties of the MaxCompute external table.
The properties supported by WITH SERDEPROPERTIES are the same as those supported by the MaxCompute external table. For example, the vehicle.csv file contains the following data:

```
1,1,51,1,46.81006,-92.08174,9/14/2014 0:00,S 1,2,13,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,3,48,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,4,30,1,46.81006,-92.08174,9/14/2014 0:00,W 1,5,47,1,46.81006,-92.08174,9/14/2014 0:00,S 1,6,9,1,46.81006,-92.08174,9/14/2014 0:00,S 1,7,53,1,46.81006,-92.08174,9/14/2014 0:00,N 1,8,63,1,46.81006,-92.08174,9/14/2014 0:00,SW 1,9,4,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,10,31,1,46.81006,-92.08174,9/14/2014 0:00,N
```

Examples:

```
oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/ -- Save the vehicle.csv file to a folder in an OSS bucket. Obtain the structure of the directory where the MaxCompute external table is saved. CREATE TABLE ambulance_data_csv_load ( vehicleId INT, recordId INT, patientId INT, calls INT, locationLatitute DOUBLE, locationLongtitue DOUBLE, recordTime STRING, direction STRING ); -- Create a destination table named ambulance_data_csv_load. LOAD OVERWRITE TABLE ambulance_data_csv_load FROM LOCATION 'oss://oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/' STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES ( 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole', -- The Alibaba Cloud Resource Name (ARN) of the AliyunODPSDefaultRole role. 'odps.text.option.delimiter'=','
```

);

```
-- Import the CSV file from OSS to the destination table.
```

**Import data stored in an open source format**

Syntax

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [ROW FORMAT SERDE '<serde class>'
  [WITH SERDEPROPERTIES ('odps.properties.rolearn'='${roleran}'
[,'name2'='value2',...])]
```

`]`

```
STORED AS <file format>;
```

Parameters:
**table_name**: the name of the destination table into which you want to insert data. You
must create a destination table before you insert data into it. The schema of the destination table must be the same as the format of the external data.
**LOAD INTO**: inserts data into a table or partition.
**LOAD OVERWRITE**: clears the existing data from a table or partition and inserts data into
the table or partition.
**STORED AS**: specifies the format of the imported data file. Valid values include ORC,
PARQUET, RCFILE, SEQUENCEFILE, and TEXTFILE. You can use this clause in the same way as you use the clause for MaxCompute external tables.
**ROW FORMAT SERDE**: This clause is optional. You can use this clause in the same way as
you use the clause for MaxCompute external tables. Mappings between file formats and SerDe classes: SEQUENCEFILE: org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe TEXTFILE: org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe RCFILE: org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe ORC: org.apache.hadoop.hive.ql.io.orc.OrcSerde ORCFILE: rg.apache.hadoop.hive.ql.io.orc.OrcSerde PARQUET: org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe AVRO: org.apache.hadoop.hive.serde2.avro.AvroSerDe
**SERDEPROPERTIES**: If you use STS to grant MaxCompute the required permissions, you
must use this parameter to specify the value of the **odps.properties.rolearn** property. This property indicates the ARN of the **AliyunODPSDefaultRole** role. If the owner of MaxCompute and the owner of OSS use the same account, one-click authorization is allowed. Examples:

```
oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/ds=20200910/' -- The OSS directory where the MaxCompute external table is saved uses the preceding st ructure. The MaxCompute external table in the directory does not include partition key columns. The information of partition key columns is included in the directory informat ion. CREATE TABLE ambulance_data_csv_load_pt ( vehicleId STRING, recordId STRING, patientId STRING, calls STRING, locationLatitute STRING, locationLongtitue STRING, recordTime STRING, direction STRING) PARTITIONED BY (ds STRING); -- Create a destination table named ambulance_data_csv_load_pt. LOAD OVERWRITE TABLE ambulance_data_csv_load_pt PARTITION(ds='20200910') FROM LOCATION 'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/' ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' STORED AS TEXTFILE; -- Import data stored in open source formats from OSS to the destination table.
```

**Note**

If you download data to a partitioned table, the schema of the external table in the OSS directory does not include partition key columns. In the preceding example, the external table in the directory contains only the business fields. The table does not include partition key columns.

### DDL statements

#### Table operations

##### Create a table

This topic describes how to use DDL statements to create a table. Syntax:

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name [(col_name data_type [DEFAULT value] [COMMENT col_comment], ...)] [COMMENT table_comment] [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] [CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [A SC | DESC] [, col_name [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] -- Specify t he shuffle and sort attributes when you create a clustered table. [STORED BY StorageHandler] -- Used only for external tables. [WITH SERDEPROPERTIES (Options)] -- Used only for external tables. [LOCATION OSSLocation] -- Used only for external tables. [STORED AS AliOrc]-- Specify the storage format of the table. You can specify AliORC on ly for newly created internal tables. [TBLPROPERTIES("compressionstrategy"="normal/high/extreme",-- Specify the compression p olicy for data storage.
               "transactional"="true")] -- Specify a transactional table. You can then
execute UPDATE or DELETE statements on the table. [LIFECYCLE days]; CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE existing_table_name];
```

Parameters:
**table_name** and **col_name**: the table name and column name. The names are not case-
sensitive. The names cannot contain special characters. A table or column name can contain only letters, digits, and underscores (_) and can be up to 128 bytes in length. We recommend that you start the table or column name with a letter. A table can contain a maximum of 1,200 columns.
**data_type**: the type of data. Valid values: BIGINT, DOUBLE, BOOLEAN, DATETIME,
DECIMAL, STRING, ARRAY<T>, and MAP<T1,T2>.

| Note If you want to use new data types, such as TINYINT, SMALLINT, INT, FLOAT, VARCHAR, TIMESTAMP, and BINARY, you must enable these data types. To enable new data types at the session level, add set odps.sql.type.system.odps2=true; before the SQL statement. Then, commit them for execution. To enable new data types at the project level, run the following command as the project owner: setproject odps.sql.type.system.odps2=true; |   |   |
|---|---|---|
|   | set |   |

**DEFAULT value**: the default value of the column. If you do not specify the value of the
column in an INSERT operation, the default value is used for the column.
**COMMENT table_comment**: the comment of the table. The comment must be a valid
string that can be up to 1,024 bytes in length.
**PARTITIONED BY (col_name data_type [COMMENT col_comment], …)** : the partition
field of the table. The following data types are supported: TINYINT, SMALLINT, INT, BIGINT, VARCHAR, and STRING. The value of the partition field cannot contain double-byte characters. It must start with a letter, followed by letters, digits, or special characters. The value can be a maximum of 128 bytes in length. The value can contain the following special characters: spaces, colons (:), underscores (_), dollar signs ($), number signs (#), periods (.), exclamation points (!), and at signs (@). Other characters, such as \t, \n, and /, are considered undefined characters. After you use partition fields to partition a table, a full table scan is not triggered when you add partitions, update partition data, or read partition data. This makes data processing more efficient.

**Note**

A table can contain a maximum of 60,000 partitions at six or lower levels.

**CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, …]) [SORTED BY**

**(col_name [ASC | DESC] [, col_name [ASC | DESC] …])] INTO number_of_buckets**

**BUCKETS**: specifies the shuffle and sort attributes when you create a clustered table.
Clustered tables are classified into hash-clustered tables and range-clustered tables. Hash-clustered tables
**CLUSTERED BY**: the hash key. MaxCompute performs a hash operation on specified
columns and distributes data to each bucket based on the hash values. We recommend that you specify a column that has large value ranges and a small number of duplicate key-value pairs in **CLUSTERED BY**. This prevents data skew and hot spots and makes concurrent execution more efficient. To optimize JOIN operations, we recommend that you select commonly used join or aggregation keys. The join and aggregation keys are similar to the primary keys in conventional databases.
**SORTED BY**: specifies how the data in a bucket is sorted. To achieve better
performance, we recommend that you set **SORTED BY** and **CLUSTERED BY** to the same value. If you specify the **SORTED BY** clause, MaxCompute automatically generates indexes and uses these indexes to speed up your queries.
**INTO number_of_buckets BUCKETS**: the number of hash buckets. This parameter is
required, and the value of this parameter varies based on the amount of data. By default, MaxCompute supports a maximum of 1,111 reducers. Therefore, MaxCompute supports a maximum of 1,111 hash buckets. You can run the `set` odps.sql.reducer.instances=xxx; command to increase the number of hash buckets. The maximum number of hash buckets that is supported is 4,000. If the value exceeds 4000, computing performance deteriorates.

**Note**

To ensure optimal performance, we recommend that you take note of the following rules when you specify the number of hash buckets: Keep the size of each bucket around 500 MB. For example, if you want to add 1,000 buckets to a partition whose size is 500 GB, you must make sure that the average size of each bucket is 500 MB. If a table contains a large amount of data, you can increase the size of each bucket from 500 MB to a size in the range of 2 GB to 3 GB. You can also execute the `set` odps.sql.reducer.instances=xxx; statement to set the maximum number of hash buckets to a value greater than 1111. To optimize JOIN operations, we recommend that you do not specify the shuffle and sort attributes. The number of hash buckets of a table must be a multiple of the number of hash buckets of the other table. For example, one table has 256 hash buckets and the other table has 512 hash buckets. We recommend that you set the number of hash buckets to 2n, such as 512, 1,024, 2,048, or 4,096. This way, MaxCompute can automatically split and merge hash buckets. To make the execution more efficient, we recommend that you do not specify the shuffle and sort attributes. Range-clustered tables
**RANGE CLUSTERED BY**: the column for range clustering. MaxCompute performs the
bucket operation on the specified columns and distributes data to each bucket based on the bucket ID.
**SORTED BY**: specifies how the data in a bucket is sorted. You can use this clause in
the same way you use it for a hash-clustered table.
**INTO number_of_buckets BUCKETS**: the number of hash buckets. Compared with
hash-clustered tables, range-clustered tables have no limits on the number of buckets if the data is reasonably distributed. If you do not specify the number of buckets for a range-clustered table, MaxCompute automatically determines the optimal number of buckets based on your data volume.

**Note**

If join and aggregate operations are performed on range-clustered tables and the join or group key is the range clustering key or the prefix of the range clustering key, you can control flags to remove data shuffling. This makes the execution more efficient. You can set `odps.optimizer.enable.range.partial.repartitioning` to true or false to control shuffling. By default, this parameter is set to false. The default value indicates that shuffling is disabled.
**STORED AS**: the storage format of the table. The default value is CFile2. AliORC in C++ is
now available. It is developed by the MaxCompute storage team. AliORC is fully compatible with the open source Optimized Row Columnar (ORC). Compared with CFile2, AliORC frees up more than 10% of storage and improves read performance by more than 20%.
**LIFECYCLE**: the lifecycle of the table, in days. If you execute the **CREATE TABLE LIKE**
statement to create a table based on the schema of the source table, the lifecycle settings of the source table are not replicated.

**CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE**

**existing_table_name]**:
If you execute the CREATE TABLE…AS select_statement… statement to create a table, the data is replicated from the source table to the table. However, the CREATE TABLE…AS select_statement… statement does not replicate the partition attributes of the source table. Partition key columns in the source table become standard columns in the destination table. If you execute the CREATE TABLE…LIKE existing_table_name statement to create a table, the destination table has the same schema as the source table. However, the statement does not replicate data or lifecycle settings from the source table to the destination table. Clauses related to external tables:
**STORED BY StorageHandler**: the storage handler that is specified based on the format
of data in the external table.
**WITH SERDEPROPERTIES (Options)**: the parameters for authorization, compression,
and character parsing in the external table.
**LOCATION OSSLocation**: the Object Storage Service (OSS) directory where the external
table is saved.
**TBLPROPERTIE("compressionstrategy"="xxx")**: the attribute of the transactional table.
You can specify the lifecycle and comment attributes in this clause. **compressionstrategy** specifies the compression policy for data storage. The valid values are normal, high, and extreme. The **compressionstrategy** parameter must be in lowercase. However, the value of this parameter is not case-sensitive. This attribute applies only to the internal tables of MaxCompute. The default compression policy is normal for non-archived data and high for archived data. Definitions of the valid values: normal: indicates zstd level 1. high: indicates zstd level 4. extreme: indicates zstd level 9. You can also specify the compression policy for a project. The project owner must use
**odps.storage.compression.strategy** to specify the compression policy in the common
attributes for project management. After this attribute is specified, the configuration applies to all generated non-archived data and does not affect the archive policy.
**TBLPROPERTIES("transactional"="true")**: indicates that the table that you want to
create is a transactional table. You can execute the UPDATE or DELETE statement to update or delete data by row.

**Note**

If you do not specify **IF NOT EXISTS** in a table creation statement and another table with the same name exists, an error is returned. If you specify **IF NOT EXISTS** in a table creation statement, a success message is returned regardless of whether a table with the same name exists. The message is returned even if the schema of the existing table is different from that of the table to create. In addition, the metadata of the existing table remains unchanged.

**Example for creating a partitioned table**

The following example shows how to create a table named sale_detail to store sales records. The table has two partition key columns: **sale_date** and **region**. Syntax:

```
CREATE TABLE IF NOT EXISTS sale_detail
```

`(`

```
shop_name STRING, customer_id STRING, total_price DOUBLE
```

`)`

```
PARTITIONED BY (sale_date STRING,region STRING); -- Create a partitioned table named sale_detail.
```

**Example of CREATE TABLE...AS...**

You can execute the `CREATE TABLE...AS select_statement...` statement to create a table and replicate data from the source table to the table. Example:

```
CREATE TABLE sale_detail_ctas1 AS SELECT * FROM sale_detail;
```

If the sale_detail table contains data, all data in the sale_detail table is replicated to the sale_detail_ctas1 table after you execute the preceding statement.

**Note**

The sale_detail table is a partitioned table. When you execute the `CREATE TABLE...AS` `select_statement...` statement to create the sale_detail_ctas1 table, partition attributes of the sale_detail table are not replicated to the sale_detail_ctas1 table, and partition key columns in the sale_detail table are considered standard columns in the sale_detail_ctas1 table. sale_detail_ctas1 is a non-partitioned table that has five columns. If the SELECT clause in the `CREATE TABLE...AS select_statement...` statement uses constants as column values, we recommend that you specify the names of columns. Example:

```
CREATE TABLE sale_detail_ctas2
```

`AS`

```
SELECT shop_name, customer_id, total_price, '2013' AS sale_date, 'China' AS region FROM sale_detail;
```

Example without column aliases specified:

```
CREATE TABLE sale_detail_ctas3
```

`AS`

```
SELECT shop_name, customer_id, total_price, '2013', 'China' FROM sale_detail;
```

**Example of CREATE TABLE...LIKE...**

If you want the source and destination tables to have the same schema, you can execute the `CREATE TABLE...LIKE...` statement. Example:

```
CREATE TABLE sale_detail_like LIKE sale_detail;
```

The schema of sale_detail_like is exactly the same as that of sale_detail. The two tables have the same attributes, such as column names, column comments, and table comments, aside from the lifecycle. However, data in the sale_detail table is not replicated to the sale_detail_like table.

**Create clustered tables**

The following example shows how to create a hash-clustered table.

```
CREATE TABLE T1 (a STRING, b STRING, c BIGINT) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS; -- Create a hash-clustered non-partitioned table. CREATE TABLE T1 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS; -- Create a hash-clustered partitioned table.
```

The following example shows how to create a range-clustered table.

```
CREATE TABLE T2 (a STRING, b STRING, c BIGINT) RANGE CLUSTERED BY (c) SORTED by (c) INT O 1024 BUCKETS; -- Create a range-clustered non-partitioned table. CREATE TABLE T2 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY (c) SORTED by (c) ; -- Create a range-clustered partitioned table. The number of bucket s can be empty.
```

**Create transactional tables**

```
-- Create a transactional table. create table txn_table(id bigint) tblproperties("transactional"="true"); -- Create a partitioned transactional table. create table if not exists txn_table_pt(id bigint) partitioned by(ds string) tblproperties ("transactional"="true");
```

**Query information about a table**

MaxCompute allows you to execute the DESC statement to query table information.

```
DESC <table_name>; -- Query table information. DESC EXTENDED <table_name>; -- Query information about an external table. -- You can also check whether the table is a transactional table. If you want to check whether the table is a transactional table, you must upgrade the version of the MaxComp ute client to V0.35.0.
```

**Query the statements that are used to create tables**

MaxCompute allows you to execute the SHOW CREATE TABLE statement to query the statements that are used to create tables.

```
SHOW CREATE TABLE <table_name>;
```

**Note**

You can use this statement to generate SQL DDL statements that are used to create tables. These DDL statements can be used to rebuild the table schema.

##### Drop a table

This topic describes how to use a DDL statement to drop a table in MaxCompute. You can use this statement to drop a table that you no longer need.

```
DROP TABLE [IF EXISTS] table_name;
```

**Note**

If you do not specify **IF EXISTS** and the table does not exist, an error is returned. If you specify this parameter, the system returns a success message regardless of whether the table exists. table_name: required. This parameter specifies the name of the table that you want to drop.

```
CREATE TABLE sale_detail_drop LIKE sale_detail; -- If the table exists, the system returns a success message. If the table does not e xist, the system returns an exception. DROP TABLE sale_detail_drop; -- The system returns a success message regardless of whether the sale_detail_drop2 t able exists. DROP TABLE IF EXISTS sale_detail_drop2;
```

##### Rename a table

This topic describes how to use a DDL statement to rename a table in MaxCompute. You can use this statement to rename a table.

```
ALTER TABLE table_name RENAME TO new_table_name;
```

**Note**

The **RENAME** operation modifies only the table name and does not change the data in the table. If a table with the same name as new_table_name already exists, the system returns an error. If **table_name** does not exist, the system returns an error. table_name: required. This parameter specifies the name of the table that you want to rename. new_table_name: required. This parameter specifies the new name of the table.

```
--Create a table for the example CREATE TABLE sale_detail_rename1 LIKE sale_detail; --Rename the table ALTER TABLE sale_detail_rename1 RENAME TO sale_detail_rename2; --Check whether the renamed table exists SHOW TABLES;
```

##### Change the owner of a table

This topic describes how to use a DDL statement to change the owner of a table. MaxCompute SQL allows you to execute the `CHANGEOWNER` statement to change the owner of a table. Syntax:

```
ALTER TABLE table_name CHANGEOWNER TO 'ALIYUN$xxx@aliyun.com';
```

##### Modify the comment of a table

This topic describes how to use a DDL statement to modify the comment of a table. Syntax:

```
ALTER TABLE table_name SET COMMENT 'tbl comment';
```

**Note**

The table specified by **table_name** must exist. The value of **comment** can be up to 1,024 bytes. Examples:

```
ALTER TABLE sale_detail SET COMMENT 'new coments for table sale_detail';
```

You can execute the DESC statement in MaxCompute to view the comment of the table after modification.

##### Modify the lifecycle settings of a table

MaxCompute provides the lifecycle management feature to facilitate storage release and simplify data reclamation. This topic describes how to use a DDL statement to modify the lifecycle settings of a table. Syntax:

```
ALTER TABLE table_name SET lifecycle days;
```

**Note**

**days**: the lifecycle duration, which must be a positive integer in days.
**table_name**: the name of the table whose lifecycle settings you want to modify.
You can specify the lifecycle when you create a table. The lifecycle can be specified only for a table rather than a partition. After a lifecycle is specified for a partitioned table, the lifecycle applies to the partitions of the table. If data in a table is modified, the value of **LastDataModifiedTime** is updated. Therefore, MaxCompute determines whether to reclaim this table based on the value of **LastDataModifiedTime** and the lifecycle settings. For a non-partitioned table, if the data remains unchanged for the duration specified by **days** after data is last modified, MaxCompute automatically executes a statement such as DROP TABLE to reclaim the table. For a partitioned table, MaxCompute determines whether to reclaim a partition based on the value of **LastDataModifiedTime** for the partition. Unlike nonpartitioned tables, a partitioned table is not deleted even if all of the partitions are reclaimed. You can only modify the lifecycle settings instead of disabling the lifecycle for nonpartitioned tables. You can disable the lifecycle for a specific partition in a partitioned table. Examples:

```
create table test_lifecycle(key string) lifecycle 100; -- Create a table named test_lifecycle with a lifecycle of 100 days. alter table test_lifecycle set lifecycle 50; -- Change the lifecycle of the test_lifecycle table to 50 days.
```

##### Disable or enable the lifecycle feature

In some cases, if you do not want some partitions to be automatically reclaimed based on the lifecycle feature, you can disable the lifecycle feature for these partitions. This topic describes how to use a DDL statement to disable or enable the lifecycle feature. Syntax:

```
ALTER TABLE table_name partition[partition_spec] ENABLE|DISABLE LIFECYCLE;
```

**Note**

**DISABLE LIFECYCLE**: disables the lifecycle feature for a table or partition.
It prevents the reclamation of a table and its partitions based on the lifecycle feature. This parameter has a higher priority than partition_spec enable lifecycle. If you use **table disable lifecycle**, **partition_spec enable**
**lifecycle** is invalid.
After the lifecycle feature of a table is disabled, the table lifecycle settings and the ENABLE and DISABLE tags of partitions in the table are retained. After the lifecycle feature of a table is disabled, you can still modify the lifecycle settings of the table and its partitions.
**ENABLE LIFECYCLE**: enables the lifecycle feature for a table or partition.
A table and its partitions can be reclaimed based on the lifecycle feature again. The lifecycle settings of the current table and its partitions are used by default. Before you enable the lifecycle feature for a table, you can modify the lifecycle settings of the table and its partitions. This prevents data from being mistakenly reclaimed due to the use of previous settings. Examples:

```
ALTER TABLE trans DISABLE LIFECYCLE; -- Disable the lifecycle feature for the trans table. ALTER TABLE trans PARTITION(dt='20141111') DISABLE LIFECYCLE; -- Disable the lifecycle feature for the dt='20141111' partition in the trans table. ALTER TABLE trans ENABLE LIFECYCLE; -- Enable the lifecycle feature for the trans table. ALTER TABLE trans PARTITION(dt='20141111') ENABLE LIFECYCLE; -- Enable the lifecycle feature for the dt='20141111' partition in the trans table.
```

##### Modify the value of LastDataModifiedTime

**for a table**

MaxCompute SQL allows you to perform the TOUCH operation to modify the value of
**LastDataModifiedTime** for a table. This operation changes the value of
**LastDataModifiedTime** for a table to the current time. This topic describes how to use a
DDL statement to modify the value of LastDataModifiedTime for a table. Syntax:

```
ALTER TABLE table_name TOUCH;
```

**Note**

If the table specified by **table_name** does not exist, an error is returned. This operation modifies the value of **LastDataModifiedTime** for a table. In this case, MaxCompute considers a change to the table data and recalculates the lifecycle.

##### Modify the clustering attributes of a table

This topic describes how to use a DDL statement to modify the clustering attributes of a table. MaxCompute allows you to add or remove the clustering attributes of a partitioned table by using the `ALTER TABLE` statement.

**Note**

The `ALTER TABLE` statement can modify only the clustering attributes of a partitioned table. The clustering attributes of a non-partitioned table cannot be modified after these attributes are added. The `ALTER TABLE` statement is applicable to the tables that already exist. After new clustering attributes are added, new partitions are stored based on the modified clustering attributes. The `ALTER TABLE` statement affects only the new partitions of partitioned tables, including the partitions generated by using the INSERT OVERWRITE statement. New partitions are stored based on the new clustering attributes, while the clustering attributes and storage of existing partitions remain unchanged. After you specify the clustering attributes for a table, you can remove the clustering attributes and add clustering attributes for the table again. You can specify different clustering columns, sort columns, and numbers of buckets for new partitions. The `ALTER TABLE` statement takes effect only on the new partitions of a table. Therefore, you cannot specify a partition in this statement.

**Add hash clustering attributes to a table**

Syntax:

```
ALTER TABLE table_name [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_nam e [ASC | DESC] ...])] INTO number_of_buckets BUCKETS]
```

**Remove hash clustering attributes from a table**

Syntax:

```
ALTER TABLE table_name NOT CLUSTERED;
```

**Add range clustering attributes to a table**

If you do not specify the number of buckets, MaxCompute automatically determines the optimal number based on the data volume. Syntax:

```
ALTER TABLE table_name [RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, c ol_name [ASC | DESC] ...])] INTO number_of_buckets BUCKETS]
```

**Remove range clustering attributes from a table or partition**

Syntax:

```
ALTER TABLE table_name NOT CLUSTERED; ALTER TABLE table_name partition_spec NOT CLUSTERED;
```

##### Delete data from a non-partitioned table

This topic describes how to use a DDL statement to delete data from a non-partitioned table. Syntax:

```
TRUNCATE TABLE table_name;
```

**Note**

This statement is used to delete data from a specific non-partitioned table. To delete data from a partitioned table, execute the `ALTER TABLE table_name DROP` `PARTITION(partition_spec)` statement.

##### Archive table data

This topic describes how to use a DDL statement to archive the data of a table. If a project does not have enough space and data needs to be compressed or deleted, you can use table archiving of MaxCompute to compress data by about 50%. Table archiving uses a compression algorithm with a high compression ratio. It saves data as redundant array of independent disks (RAID) files. Data is no longer simply stored in three copies. Instead, six copies and three check blocks are maintained to increase the compression ratio from 1:3 to 1:1.5. Table archiving allows data to consume only half of the physical space. However, this feature comes at a price. If a data block or machine is faulty, it requires a long time to restore the data block, and read performance deteriorates. Therefore, this feature is suitable for the compression of cold data. For example, you can use this feature to store a large number of logs that are less used as RAID files for a long time. Syntax:

```
ALTER TABLE [table_name] <PARTITION(partition_name='partition_value')> ARCHIVE;
```

**Note**

If the table specified by **table_name** does not exist, an error is returned. If the partition specified by **partition_name** does not exist, an error is returned. Examples:

```
alter table my_log partition(ds='20170101') archive;
```

Output:

```
Summary: table name: test0128 /pt=a instance count: 1 run time: 21 before merge, file count: 1 file size: 456 file physical size: 1368 after merge, file count: 1 file size: 512 file physical size: 768
```

**Note**

The output shows the changes in the logical size and physical size after the data is archived. In the archiving process, multiple small files are automatically merged. After the data is archived, you can execute the `DESC EXTENDED` statement to check whether the data in the partition has been archived and view the usage of physical space:

```
desc extended my_log partition(ds='20170101'); -- The following result is returned: +------------------------------------------------------------------------------------ PartitionSize: 512 | +------------------------------------------------------------------------------------ CreateTime: 2017-01-28 07:05:20 | LastDDLTime: 2017-01-28 07:05:20 | LastModifiedTime: 2017-01-28 07:05:21 | +------------------------------------------------------------------------------------
```

##### Forcibly delete data from a table or

**partition**

This topic describes how to use a DDL statement to forcibly delete data from a table or partition. If you want to forcibly and irrecoverably delete data from a table or partition to immediately release storage, you can execute a DROP statement with the PURGE option. Syntax:

```
DROP TABLE tblname PURGE; ALTER TABLE tblname DROP PARTITION(part_spec) PURGE;
```

Examples:

```
drop table my_log purge; alter table my_log drop partition (ds='20170618') purge;
```

#### View-based operation

##### Create a view

This topic describes how to use a DDL statement to create a view. Syntax:

```
CREATE [OR REPLACE] VIEW [IF NOT EXISTS] view_name [(col_name [COMMENT col_comment], ...)] [COMMENT view_comment] [AS select_statement];
```

| Note To create a view, you must have read permissions on the table referenced by the view. A view can contain only one valid SELECT statement. A view can reference other views but cannot reference itself. Circular references are not supported. You cannot write data to a view. For example, the INSERT INTO and INSERT OVERWRITE statements do not work on views. If the table referenced by a view changes, you may no longer be able to access the view. For example, a view becomes inaccessible after the table it references is deleted. You must maintain the mappings between referenced tables and views. If the CREATE VIEW statement is executed without the IF NOT EXISTS option and the view already exists, an exception is returned. In this case, you can execute CREATE VIEW or REPLACE VIEW to recreate the view. The permissions on the view remain unchanged after the view is recreated. |   |   |
|---|---|---|
|   | INSERT |   |

Examples:

```
create view if not exists sale_detail_view (store_name, customer_id, price, sale_date, region) comment 'a view for table sale_detail' as select * from sale_detail; -- Create a view named sale_detail_view.
```

##### Delete a view

This topic describes how to use a DDL statement to delete a view. Syntax:

```
DROP VIEW [IF EXISTS] view_name;
```

**Note**

If the partition does not exist and **IF EXISTS** is not specified, an error is returned. Examples:

```
DROP VIEW IF EXISTS sale_detail_view;
```

##### Rename a view

This topic describes how to use a DDL statement to rename a view. Syntax:

```
ALTER VIEW view_name RENAME TO new_view_name;
```

**Note**

If a view with the same name already exists, an error is returned. Examples:

```
alter view sale_detail_view rename to market;
```

#### Materialized view operations

A materialized view is a database object that stores the pre-calculation results of timeconsuming queries, such as JOIN and AGGREGATE. You can directly reuse the pre-calculation results when you want to perform the same queries. This accelerates the speed of queries.

**Background information**

A view is a stored query accessible as a virtual table. Each time you query a view, the query statement is converted into the SQL statement that is used to define the view. A materialized view is a special physical table that occupies storage resources to store real data. Materialized views are suitable for the following queries: Queries that are in a fixed mode and are frequently executed Queries that involve time-consuming operations, such as JOIN or AGGREGATE Queries that involve only a small portion of data in a table The following table compares traditional queries and queries based on materialized views.

| Item | Traditional query | Query based on a materialized view |
|---|---|---|

| Query statements | SQL statements are used to query data. SELECT empid, deptname FROM emps JOIN depts ON emps.deptno=depts.dept no WHERE hire date >= _ '2018-01-01'; | Data is queried based on the materialized view that you created. Statements that are used to create a materialized view: CREATE MATERIALIZED VIEW mv AS SELECT empid, deptname, hire date _ FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2016-01-01'; _ Statements that are used to query data based on the materialized view that you created: SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ If the query rewrite feature is enabled for the materialized view, data is directly obtained from the query result that is contained in the materialized view when you execute the first SQL statement in the following code: SELECT empid, deptname FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2018-01-01'; _ -- The preceding statement is equivalent to the following statement: SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ |
|---|---|---|
| Query characteris tics | Queries involve table reading, JOIN, and filter (WHERE clause) operations. If the source table contains a large amount of data, the query speed is slow. The query operation is complex, and the query efficiency is low. | Queries involve table reading and filter operations. JOIN operations are not involved. MaxCompute automatically matches the optimal materialized view and reads data from the optimal materialized view. This greatly improves query efficiency. |

**Operations**

| Operation | Description | Authorized user |
|---|---|---|

| Create a materialized view that supports clustering or partitioning | Creates a materialized view based on a query statement. | Users who have the CreateTable permission on a project |
|---|---|---|
| Update a materialized view | Updates an existing materialized view. | Users who have the Alter permission on tables |
| Change the lifecycle of an existing materialized view | Changes the lifecycle of an existing materialized view. | Users who have the Alter permission on tables |
| Enable or disable the lifecycle feature for an existing materialized view | Enables or disables the lifecycle feature for an existing materialized view. | Users who have the Alter permission on tables |
| Query information about a materialized view | Queries the basic information about a materialized view. | Users who have the Describe permission on the metadata of a table |
| Query the status of a materialized view | Queries the status of a materialized view. | Users who have the Describe permission on the metadata of a table |
| List all materialized views within a project | Lists all materialized views in a project or the materialized views that meet specific rules in a project. | Users who have the List permission on objects in a project |
| Drop an existing materialized view | Drops an existing materialized view. | Users who have the Drop permission on tables |
| Drop partitions from an existing materialized view | Drops partitions from an existing materialized view. | Users who have the Drop permission on tables |

| Perform a penetration query on a materialized view | Queries data from the source partitioned table if the partition data that you want to query is not contained in the materialized view. | Users who have the Write and CreateTable permissions on a project |
|---|---|---|

**Limits**

Window functions, User-defined table-valued functions (UDTFs), and non-deterministic functions, such as user-defined scalar functions (UDFs) and user-defined aggregate functions (UDAFs), are not supported.

|   | Note If you must use non-deterministic functions, run the set odps.sql.materialized.view.support.nondeterministic.function=true; command at the session level. |   |
|---|---|---|
|   |   | set |
|   | odps.sql.materialized.view.support.nondeterministic.function=true; |   |

**Create a materialized view that supports clustering or**

**partitioning**

You can create a materialized view that supports clustering or partitioning based on the data for materialized view scenarios. Limits The name of the materialized view that you want to create cannot be the same as the name of an existing table, view, or materialized view in the current project. You can run the SHOW TABLES; command to view the names of all tables and materialized views in a project. You cannot create a materialized view based on an existing materialized view. You cannot create a materialized view based on an external table. Usage notes If the query statement based on which you create a materialized view fails to be executed, you cannot create the materialized view. Partition key columns in a materialized view must be derived from a source table. The sequence and number of the columns in the materialized view must be the same as the sequence and number of the columns in the source table. Column names can be different. You must specify comments for all columns, including partition key columns. If you specify comments only for some columns, an error is returned. You can specify both the partitioning and clustering attributes for a materialized view. In this case, the data in each partition has the specified clustering attribute. If the query statement based on which you create a materialized view contains operators that are not supported by the materialized view, an error is returned. By default, MaxCompute does not allow you to create materialized views by using nondeterministic functions, such as UDFs or UDAFs. If you must use non-deterministic

| functions, run the | set |   |
|---|---|---|
| odps.sql.materialized.view.support.nondeterministic.function=true; |   |   |
|   |   | command at the |

session level. If the source table of a materialized view contains an empty partition, you can refresh the materialized view to generate an empty partition in the materialized view. Command syntax

```
CREATE MATERIALIZED VIEW [IF NOT EXISTS][project_name.]<mv_name> [LIFECYCLE <days>] -- The lifecycle of the materialized view. [BUILD DEFERRED] -- Specifies that only the schema is created and no data is updat ed when you create the materialized view. [(<col_name> [COMMENT <col_comment>],...)] -- The column comments. [DISABLE REWRITE] -- Specifies whether to disable the query rewrite operation that is performed based on the materialized view. [COMMENT 'table comment'] -- The materialized view comments. [PARTITIONED BY (<col_name> [, <col_name>, ...]) -- The partitions in the material ized view. This parameter is required when you create a partitioned materialized view
```

`.`

```
[CLUSTERED BY|RANGE CLUSTERED BY (<col_name> [, <col_name>, ...]) [SORTED BY (<col_name> [ASC | DESC] [, <col_name> [ASC | DESC] ...])]
    INTO <number_of_buckets> BUCKETS]    -- The shuffle and sort attributes of the ma
terialized view. This parameter is required when you create a clustered materialized view. [REFRESH EVERY <num> MINUTES/HOURS/DAYS] [TBLPROPERTIES("compressionstrategy"="normal/high/extreme", -- The compression pol icy for data storage of the materialized view.
                "enable_auto_substitute"="true",    -- Specifies whether to query data
from the source partitioned table if the partition data that you want to query is not contained in the materialized view.
                "enable_auto_refresh"="true",    -- Specifies whether to enable the sc
heduled update feature.
                "refresh_interval_minutes"="120",    -- The update interval.
                "only_refresh_max_pt"="true"    -- Specifies whether to automatically
update the latest partition data in the source table to the materialized view.
```

`)]`

```
AS <select_statement>;
```

Parameters and descriptions

| Parameter | Req uire d | Description |
|---|---|---|
| IF NOT EXISTS | No | If you do not specify IF NOT EXISTS and the materialized view already exists, an error is returned. |
| project name _ | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to create. |
| days | No | The lifecycle of the materialized view that you want to create. Unit: days. Valid values: 1 to 37231. |

| BUILD DEFERRED | No |   | If this keyword is added, only the schema is created and the data is not updated when you create the materialized view. |   |   |   |
|---|---|---|---|---|---|---|
| col name _ | No |   | The name of a column in the materialized view that you want to create. |   |   |   |
| col comment _ | No |   | The comment on a column in the materialized view that you want to create. |   |   |   |
| DISABLE |   |   | Specifies whether to disable the query rewrite operation that is performed based on this materialized view. If you do not configure this parameter, the query rewrite operation based on this materialized view is allowed. In this case, you can execute the ALTER |   |   |   |
|   |   |   |   |   | ALTER |   |
|   |   |   | MATERIALIZED VIEW [project name.]<mv name> DISABLE _ _ |   |   |   |
| REWRITE | No | No |   |   |   |   |
|   |   |   | REWRITE; |   |   |   |
|   |   |   |   | ALTER MATERIALIZED VIEW [project name.]<mv name> ENABLE _ _ |   |   |
|   |   |   | REWRITE; |   |   |   |
| PARTITIONED BY | No |   | The partition key columns in the materialized view that you want to create. If you want to create a partitioned materialized view, you must configure this parameter. |   |   |   |
| CLUSTERED BY\|RANGE CLUSTERED BY | No |   | The shuffle attribute of the materialized view that you want to create. If you want to create a clustered materialized view, you must specify the clustered by or range clustered by parameter. |   |   |   |
| SORTED BY | No |   | The sort attribute of the materialized view that you want to create. If you want to create a clustered materialized view, you must configure this parameter. |   |   |   |
| REFRESH EVERY | No |   | The scheduled update interval for materialized views. Supported units: minutes, hours, days, and days. |   |   |   |
| number of buck _ _ ets | No |   | The number of buckets in the materialized view that you want to create. If you want to create a clustered materialized view, you must configure this parameter. |   |   |   |

| TBLPROPERTIES | No | compressionstrategy specifies the compression policy for data storage of the materialized view that you want to create. Valid values: normal, high, and extreme. enable auto substitute _ _ specifies whether to automatically query data from the source table if the materialized view does not contain the partition from which you want to query data. enable auto refresh: optional. Set this parameter to true if _ _ you want the system to automatically update data. refresh interval minutes: conditionally optional. If _ _ enable auto refresh is set to true , you need to configure _ _ this parameter. Unit: minutes. only refresh max pt: optional. This parameter is valid for _ _ _ partitioned materialized views. If this parameter is set to true , the latest partition data in the source table is updated to the materialized view. |
|---|---|---|
| select statement _ | Yes | The SELECT statement. For more information about the syntax of the SELECT statement, see SELECT syntax. |

Example 1: Create a materialized view. a. Create tables named `mf_t` and `mf_t1` and insert data into the tables.

```
CREATE TABLE IF NOT EXISTS mf_t(
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t ADD PARTITION (ds='1'); INSERT INTO mf_t PARTITION (ds='1') VALUES (1,10,'kyle'),(2,20,'xia'); SELECT * FROM mf_t WHERE ds ='1'; -- The following result is returned: +------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 2          | 20         | xia        | 1          |
+------------+------------+------------+------------+ CREATE TABLE IF NOT EXISTS mf_t1(
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t1 ADD PARTITION (ds='1'); INSERT INTO mf_t1 PARTITION (ds='1') VALUES (1,10,'kyle'),(3,20,'john'); SELECT * FROM mf_t1 WHERE ds ='1'; -- The following result is returned: +------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 3          | 20         | john       | 1          |
+------------+------------+------------+------------+
```

b. Create a materialized view. Sample 1: Create a materialized view that contains a partition key column named ds.

```
CREATE MATERIALIZED VIEW mf_mv LIFECYCLE 7
```

`(`

```
  key comment 'unique id',
  value comment 'input value',
  ds comment 'partitiion'
```

`)`

```
PARTITIONED BY (ds) AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
     FROM mf_t AS t1 JOIN mf_t1 AS t2
       ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
-- Query data from the created materialized view. SELECT * FROM mf_mv WHERE ds =1; +------------+------------+------------+
| key        | value      | ds         |
+------------+------------+------------+
| 1          | 10         | 1          |
+------------+------------+------------+
```

Sample 2: Create a non-partitioned materialized view that is clustered.

```
CREATE MATERIALIZED VIEW mf_mv2 LIFECYCLE 7 CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

Sample 3: Create a partitioned materialized view that is clustered.

```
CREATE MATERIALIZED VIEW mf_mv3 LIFECYCLE 7 PARTITIONED BY (ds) CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

Example 2: Update a materialized view whose source table contains an empty partition. An empty partition is generated in the materialized view.

```
CREATE TABLE mf_blank_pts(id bigint ,name string) PARTITIONED BY (ds bigint); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 1); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 2); INSERT INTO TABLE mf_blank_pts PARTITION(ds=1) VALUES (1,"aba"),(2,"cbd"); CREATE MATERIALIZED VIEW IF NOT EXISTS mf_mv_blank_pts PARTITIONED BY (ds) AS SELECT id,name,ds FROM mf_blank_pts; ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>0); SHOW PARTITIONS mf_mv_blank_pts; -- The partition ds=2 in the source table does not contain any data. After you exec ute an ALTER statement that contains the expression ds>0, an empty partition is gen erated in the materialized view. ds=1 ds=2 SELECT * FROM mf_mv_blank_pts WHERE ds>0; -- The returned result shows that only the ds=1 partition has data. +------------+------------+------------+
| id         | name       | ds         |
+------------+------------+------------+
| 1          | aba        | 1          |
| 2          | cbd        | 1          |
+------------+------------+------------+
```

**Update a materialized view**

If you perform operations, such as insert, overwrite, update, and delete operations on the table or partition that corresponds to a materialized view, the materialized view becomes invalid and cannot be used for query rewrite operations. You can check the status of a materialized view. If the materialized view is invalid, you must update the materialized view. Usage notes Data in a materialized view or a partition in a materialized view is updated only when data in the source table or a partition in the source table changes. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name>
      REBUILD [PARTITION (<ds>=max_pt(<table_name>),<expression1>...)];
```

Parameters and descriptions

| Parameter | Req uire d | Description |
|---|---|---|
| project na _ me | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |

| mv name _ | Yes | The name of the materialized view that you want to update. |
|---|---|---|
| ds | No | The name of the partition field in the materialized view. |
| max pt _ | No | The maximum partition value of the table or materialized view that is specified by table name. _ |
| expression | No | The expression that is used to specify the partitions that you want to update. If you want to update a partitioned materialized view, you must configure this parameter. |

Example 1: Update a non-partitioned materialized view.

```
-- Create a non-partitioned table. CREATE TABLE count_test(a BIGINT, b BIGINT); -- Create a non-partitioned materialized view. CREATE MATERIALIZED VIEW count_mv LIFECYCLE 7 AS SELECT COUNT(*) FROM count_test; -- Update the non-partitioned materialized view. ALTER MATERIALIZED VIEW count_mv rebuild;
```

Example 2: Update a partition of a partitioned materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds='1');
```

Example 3: Update the partitions of a partitioned materialized view. The partitions meet the specified conditions.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>='1', ds<='2');
```

Example 4: Update the latest partition data to a partitioned materialized view.

```
-- Create a partitioned table. CREATE TABLE IF NOT EXISTS sale_detail_jt (shop_name STRING , customer_id STRING , total_price DOUBLE ) PARTITIONED BY (sale_date STRING ,region STRING ); ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='china'); INSERT INTO sale_detail_jt PARTITION (sale_date='2013',region='china') VALUES
    ('s1','c1',100.1),
    ('s2','c2',100.2),
    ('s3','c3',100.3);
ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='en'); INSERT INTO sale_detail_jt PARTITION (sale_date='2013',region='en') VALUES
    ('t1','c5',200.0),
    ('t2','c6',300.0);
-- View partition data.
```

```
SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='china'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| s1        | c1          | 100.1       | 2013      | china  |
| s2        | c2          | 100.2       | 2013      | china  |
| s5        | c2          | 100.2       | 2013      | china  |
+-----------+-------------+-------------+-----------+--------+ -- View partition data. SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='en'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| t1        | c5          | 200.0       | 2013      | en     |
| t2        | c6          | 300.0       | 2013      | en     |
+-----------+-------------+-------------+-----------+--------+ -- Create a materialized view. CREATE MATERIALIZED VIEW mv_deferred BUILD DEFERRED AS SELECT * FROM sale_detail_jt; -- Query data from the mv_deferred materialized view. SELECT * FROM mv_deferred; -- The following result is returned: +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+ +-----------+-------------+-------------+-----------+--------+ -- Create a partitioned table. CREATE TABLE mf_part (id bigint,name string) PARTITIONED BY (dt string); -- Insert data into the table. INSERT INTO mf_part PARTITION(dt='2013') VALUES(1,'name1'),(2,'name2'); -- Query data from the table. SELECT * FROM mf_part WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+ -- Create a partitioned materialized view. CREATE MATERIALIZED VIEW mv_rebuild BUILD DEFERRED PARTITIONED BY (dt) AS SELECT * FROM mf_part; -- Query data from the materialized view. SELECT * FROM mv_rebuild WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+ +------------+------+----+
```

```
-- Update the latest partition data to the materialized view. ALTER MATERIALIZED VIEW mv_rebuild REBUILD PARTITION(dt=max_pt('mf_part')); -- Query data from the materialized view. SELECT * FROM mv_rebuild WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+
```

**Change the lifecycle of an existing materialized view**

You can change the lifecycle of an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> SET LIFECYCLE <days>;
```

Parameters and descriptions

| Parameter | Req uire d | Description |
|---|---|---|
| project nam _ e | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to update. |
| days | Yes | The new lifecycle of the materialized view. Unit: days. |

```
-- Change the lifecycle of an existing materialized view to 10 days. ALTER MATERIALIZED VIEW count_mv SET LIFECYCLE 10;
```

**Enable or disable the lifecycle feature for an existing**

**materialized view**

You can enable or disable the lifecycle feature for an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> [<pt_spec>] enable|disable LIFECY CLE;
```

Parameters and descriptions

| Parame ter |   | Requir ed | Description |   |
|---|---|---|---|---|
| project _ name |   | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |   |
| mv nam _ e |   | Yes | The name of the materialized view for which you want to enable or disable the lifecycle feature. |   |
| pt spec |   |   | The partition information of the materialized view for which you want to enable or disable the lifecycle feature. Format: (partition col1 = _ |   |
|   |   |   |   | (partition col1 = _ |
|   | pt spec | No | partition col value1, partition col2 = partition col value2, _ _ _ _ _ |   |
| _ | _ |   |   |   |
|   |   |   | ...) |   |
| enable\|d isable |   | Yes | The enable option specifies that the lifecycle feature is enabled for a materialized view or a partition of a materialized view. The disable option specifies that the lifecycle feature is disabled for a materialized view or a partition of a materialized view. If you disable the lifecycle feature, lifecycle management is not required for the materialized view or partition. |   |

Example 1: Enable the lifecycle feature for a materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') enable LIFECYCLE;
```

Example 2: Disable the lifecycle feature for a materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') disable LIFECYCLE;
```

**Query information about a materialized view**

You can query the information about a materialized view, including the schema and modification time of the materialized view. Command syntax

```
DESC EXTENDED [<project_name>.]<mv_name>;
```

Parameters and descriptions

| Parame ter | Requir ed | Description |
|---|---|---|
| project _ name | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |

| mv nam _ e | Yes | The name of the materialized view that you want to query. |
|---|---|---|

```
DESC EXTENDED mv;
```

Sample query result:

**Note**

The following sample result can be returned only if the version of the MaxCompute client is V0.43 or later.

```
+------------------------------------------------------------------------------------+
| Owner:                    ALIYUN$$****@***.aliyunid.com                       |
| Project:                  m****                                                |
| TableComment:                                                                      |
+------------------------------------------------------------------------------------+
| CreateTime:               2023-05-30 13:16:07                                      |
| LastDDLTime:              2023-05-30 13:16:07                                      |
| LastModifiedTime:         2023-05-30 13:16:07                                      |
+------------------------------------------------------------------------------------+
| MaterializedView: YES                                                              |
| ViewText: select id,name from mf_refresh                                           |
| Rewrite Enabled: true                                                              |
| AutoRefresh Enabled: true                                                          |
| Refresh Interval Minutes: 10                                                       |
+------------------------------------------------------------------------------------+
| Native Columns:                                                                    |
+------------------------------------------------------------------------------------+
| Field    | Type   | Label | ExtendedLabel | Nullable | DefaultValue | Comment
```

|

```
+------------------------------------------------------------------------------------+
| id       | bigint |       |               | true     | NULL         |              |
| name     | string |       |               | true     | NULL         |              |
+------------------------------------------------------------------------------------+
| Extended Info:                                                                     |
+------------------------------------------------------------------------------------+
| IsOutdated:               false                                                    |
| TableID:                  569ec712873e44b3868e79b7a8beabab                         |
| IsArchived:               false                                                    |
| PhysicalSize:             1875                                                     |
| FileNum:                  2                                                        |
| StoredAs:                 CFile                                                    |
| CompressionStrategy:      normal                                                   |
| odps.timemachine.retention.days: 1
```

|

```
| ColdStorageStatus:        N/A                                                      |
| encryption_enable:        false                                                    |
+------------------------------------------------------------------------------------+
| AutoRefresh History:                                                               |
+------------------------------------------------------------------------------------+
```

```
| InstanceId                | Status     | StartTime           | EndTime             |
+------------------------------------------------------------------------------------+
| 20230619070546735ghwl1****** | TERMINATED | 2023-06-19 15:05:46 | 2023-06-19 15:05:
47 |
| 20230619065545586gwllc****** | TERMINATED | 2023-06-19 14:55:45 | 2023-06-19 14:55:
46 |
| 20230619064544463gcjgom****** | TERMINATED | 2023-06-19 14:45:44 | 2023-06-19 14:45
:45 |
| 20230619063543334gzxs2d****** | TERMINATED | 2023-06-19 14:35:43 | 2023-06-19 14:35
:44 |
| 2023061906254257gi21w2****** | TERMINATED | 2023-06-19 14:25:42 | 2023-06-19 14:25:
43 |
| 20230619061540813giacg8****** | TERMINATED | 2023-06-19 14:15:41 | 2023-06-19 14:15
:41 |
| 20230619060539674gswjq9****** | TERMINATED | 2023-06-19 14:05:39 | 2023-06-19 14:05
:40 |
| 20230619055538578gvdjk****** | TERMINATED | 2023-06-19 13:55:38 | 2023-06-19 13:55:
40 |
| 20230619054537356glqdne****** | TERMINATED | 2023-06-19 13:45:37 | 2023-06-19 13:45
:38 |
| 2023061905353687gcc5pl****** | TERMINATED | 2023-06-19 13:35:36 | 2023-06-19 13:35:
37 | +------------------------------------------------------------------------------------+
```

**Query the status of a materialized view**

You can query the status of a materialized view. This operation allows you to view changes to the source table and determines whether the materialized view is valid. A materialized view can be in one of the following states: Valid When you execute a query statement, MaxCompute queries data from the materialized view instead of querying data from the source table. Invalid When you execute a query statement, MaxCompute cannot directly query data from the materialized view. In this case, MaxCompute queries data from the source table. As a result, the query speed is not accelerated. You can use a function to check whether data in a materialized view is valid.

```
boolean materialized_view_is_valid(<mv_name>,<partition_value>);
```

Check whether data in the materialized view mf_mv_refresh4 is consistent with the latest data in the source table. If the data is consistent, `true` is returned. Otherwise, `false` is returned.

```
SELECT materialized_view_is_valid("count_mv"); SELECT materialized_view_is_valid("mf_mv_blank_pts","1");
```

**List all materialized views within a project**

You can use this feature to list all materialized views in a project or the materialized views that meet specific rules in a project.

**Note**

To run the `SHOW MATERIALIZED VIEWS` command on the MaxCompute client (odpscmd), the version of the MaxCompute client must be 0.43.0 or later. Command syntax

```
-- List all materialized views in a project. SHOW MATERIALIZED VIEWS; -- List the materialized views whose names match the condition specified by materialized_view in a project. SHOW MATERIALIZED VIEWS LIKE '<materialized_view>'; -- List the materialized views whose names match the test* keyword in a project. The asterisk (*) indicates any character. SHOW MATERIALIZED VIEWS LIKE 'test*';
```

Sample query result:

```
ALIYUN$account_name:test_two_mv ALIYUN$account_name:test_create_one_mv
```

**Drop an existing materialized view**

You can drop an existing materialized view. Command syntax

```
DROP MATERIALIZED VIEW [IF EXISTS] [<project_name>.]<mv_name> [purge];
```

Parameters and descriptions

| Parame ter | Requi red | Description |
|---|---|---|
| IF EXISTS | No | If you do not specify IF EXISTS and the materialized view does not exist, an error is returned. |
| project _ name | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv nam _ e | Yes | The name of the materialized view that you want to drop. |
| purge | No | If you specify the purge parameter, data in a materialized view is deleted when you drop the materialized view. |

Drop the `mv` materialized view.

```
DROP MATERIALIZED VIEW count_mv;
```

Drop the `mv` materialized view and delete the data in the materialized view at the same time.

```
DROP MATERIALIZED VIEW count_mv purge;
```

**Drop partitions from an existing materialized view**

You can drop one or more partitions from an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> DROP [IF EXISTS] PARTITION <pt_spe c> [PARTITION <pt_spec>, PARTITION <pt_spec>....];
```

Parameters and descriptions

| Parame ter |   | Requi red | Description |   |
|---|---|---|---|---|
| project _ name |   | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |   |
| mv nam _ e |   | Yes | The name of the partitioned materialized view from which you want to drop one or more partitions. |   |
| IF EXISTS |   | No | If you do not specify IF EXISTS and the materialized view does not exist, an error is returned. |   |
| pt spec |   |   | You must specify at least one partition. The partitions that you want to drop. You must specify at least one partition. Format: (partition col1 = _ |   |
|   |   |   |   | (partition col1 = _ |
|   | pt spec | Yes | partition col value1, partition col2 = partition col value2, _ _ _ _ _ |   |
| _ | _ |   |   |   |
|   |   |   | ...) |   |

Example 1: Drop a partition from a partitioned materialized view. Sample command:

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds='1');
```

Example 2: Drop the partitions that meet the specific conditions from a partitioned materialized view. Sample command:

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds>='1' AND ds<='2');
```

**Perform a penetration query on a materialized view**

A partitioned materialized view does not contain the data of all partitions in a source partitioned table if only the latest partition data is updated to the partitioned materialized view. If the partition data that you want to query does not exist in a partitioned materialized view, the system performs a penetration query to query data from the source partitioned table. The following figure shows how to perform a penetration query. To allow a materialized view to support penetration query, you must configure the following parameters: When you create a materialized view, add `"enable_auto_substitute"="true"` to
**tblproperties**.
The following example shows how to perform a penetration query based on a materialized view.
1. Create a partitioned materialized view that supports penetration query.

```
-- Create a table named src. CREATE TABLE src(id bigint,name string) PARTITIONED BY (dt string); -- Insert data into the table. INSERT INTO src PARTITION(dt='20210101') VALUES(1,'Alex'); INSERT INTO src PARTITION(dt='20210102') VALUES(2,'Flink'); -- Create a partitioned materialized view that supports penetration query. CREATE MATERIALIZED VIEW IF NOT EXISTS mv LIFECYCLE 7 PARTITIONED BY (dt) tblproperties("enable_auto_substitute"="true") AS SELECT id, name, dt FROM src;
```

2. Query the data of the 20210101 partition in the src table from the mv materialized view.

```
SELECT * FROM mv WHERE dt='20210101';
```

3. Query the data of the 20210102 partition in the src table from the mv materialized view.
The mv materialized view does not contain the partition data. Therefore, a penetration query is performed to query the partition data from the src table.

```
SELECT * FROM mv WHERE dt = '20210102'; -- The preceding statement is equivalent to the following statement because the mv ma terialized view does not contain the data of the 20210102 partition, and the partitio n data needs to be queried from the src table. SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20210102') t;
```

4. Query the data of partitions 20201230 to 20210102 from the mv materialized view. The mv
materialized view does not contain all partition data. Therefore, a penetration query is performed to obtain the data that is not contained in the mv materialized view, and a UNION operation is performed on the obtained data and the data that is queried from the mv materialized view to return the final result.

```
SELECT * FROM mv WHERE dt >= '20201230' AND dt<='20210102' AND id='5'; -- The mv materialized view does not contain the data of the 20210102 partition, and a penetration query is performed to query the data of the 20210102 partition from the source table. The preceding statement is equivalent to the following statement: SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20211231' OR dt='20210102'
 UNION ALL
 SELECT * FROM mv WHERE dt='20210101'
) t WHERE id = '5';
```

#### Column and partition operations

##### Add partitions

This topic describes how to use a DDL statement to add partitions. Syntax:

```
alter table table_name add [if not exists] partition partition_spec; -- Add one partition at a time. alter table table_name add [if not exists] partition partition_spec [PARTITION partitio n_spec PARTITION partition_spec...] ; -- Add multiple partitions at a time.
```

**Note**

If you do not specify **IF NOT EXISTS** and another partition with the same name exists, an error is returned. A MaxCompute table can contain a maximum of 60,000 partitions. To add a partition to a table that has multi-level partitions, you must specify all partition values. Examples:

```
alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou'); -- Add a partition to store the sales records of the China (Hangzhou) region for Decemb er 2017. alter table sale_detail add if not exists partition (sale_date='201712', region='shanghai'); -- Add a partition to store the sales records of the China (Shanghai) region for Decemb er 2017. alter table sale_detail add if not exists partition(sale_date='20171011'); -- Specify only the sale_date partition. An error is returned. alter table sale_detail add if not exists partition(region='shanghai'); -- Specify only the region partition. An error is returned. alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou') partition (sale_date='201712', region='shanghai'); -- Add two partitions to store the sales records of the China (Hangzhou) and China (Sha nghai) regions for December 2017.
```

##### Delete a partition

This topic describes how to use DDL statements to delete a partition. MaxCompute allows you to delete partitions that meet a specific filter condition. If you want to delete one or more partitions that meet a filter condition at a time, you can use an expression to specify the condition, use the condition to filter partitions, and then delete the partitions. If you do not specify a filter condition, execute the following statements:

```
alter table table_name drop [if exists] PARTITION partition_spec; -- Delete one partition at a time. alter table table_name drop [if exists] PARTITION partition_spec,PARTITION partition_spec,[PARTITION partition_spec....] ; -- Delete multiple partitions at a time.
```

**Note**

Syntax for **partition_spec**:

```
partition_spec:(partition_col1 = partition_col_value1, partition_col2 = partiton_col_value2, ...)
```

If you specify a filter condition, execute the following statement:

```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION partition_filtercondition; -- Delete a partition based on the specified filter condition.
```

**Note**

Syntax for **PARTITION partition_filtercondition**:

```
PARTITION partition_filtercondition
    : PARTITION (partition_col relational_operators partition_col_value)
    | PARTITION (scalar(partition_col) relational_operators partition_col_value)
    | PARTITION (partition_filtercondition1 AND|OR partition_filtercondition2)
    | PARTITION (NOT partition_filtercondition)
    | PARTITION (partition_filtercondition1)[,PARTITION
(partition_filtercondition2), ...]
```

Parameters:
**table_name**: the name of the partitioned table from which you want to delete a partition.
**IF EXISTS**: If **IF EXISTS** is not specified and the partition does not exist, an error is
returned.
**partition_spec**: the name of the partition that you want to delete. The value is not case-
sensitive. **partition_col** indicates the name of the partition key column, and
**partition_col_value** indicates the value of the partition key column.
**PARTITION partition_filtercondition**: the partition that you want to delete. The value is
not case-sensitive.
**partition_col**: the name of the partition key column.
**relational_operators**: the relational operator.
**partition_col_value**: a value in the partition key column, which is a comparison value or
regular expression. The data type of this value must be the same as that of the partition key column.
**scalar()**: the scalar function. This function generates a scalar based on the input value,
processes the value in **partition_col**, and uses the relational operator specified by
**relational_operators** to compare the processed value with **partition_col_value**.
The filter condition that is used to delete partitions supports the following logical operators: NOT, AND, and OR. You can use PARTITION (NOT partition_filtercondition) to obtain the complementary set of the condition. You can use PARTITION (partition_filtercondition1 AND|OR partition_filtercondition2) to obtain the condition that is used to match the partitions you want to delete. Multiple PARTITION partition_filtercondition clauses are supported. If these clauses are separated by commas (,), OR is used for each clause to obtain the condition that is used to match the partitions you want to delete. Limits: Each PARTITION partition_filtercondition clause can be used for only one partition key column. If you use an expression to specify PARTITION partition_filtercondition, only the built-in scalar function can be used for the expression. Examples: The filter condition is not specified.

```
-- Delete a partition from the sale_detail table. The partition stores the sales record s of the China (Hangzhou) region in December 2017. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date='201712',region='hangzhou'); -- Delete two partitions from the sale_detail table at a time. The partitions store the sales records of the China (Hangzhou) and China (Shanghai) regions in December 2017. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date='201712',region='hangzhou'),PARTITION(sale_date='201712',region='shan ai');
```

The filter condition is specified.

```
-- Create a partitioned table. CREATE TABLE IF NOT EXISTS sale_detail( shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING); -- Add partitions. ALTER TABLE sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '201910') PARTITION (sale_date= '201911') PARTITION (sale_date= '201912') PARTITION (sale_date= '202001') PARTITION (sale_date= '202002') PARTITION (sale_date= '202003') PARTITION (sale_date= '202004') PARTITION (sale_date= '202005') PARTITION (sale_date= '202006') PARTITION (sale_date= '202007'); -- Delete multiple partitions from the table at a time. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date >= '202007'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date LIKE '20191%'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date IN ('202002','202004','202006')); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date BETWEEN '202001' AND '202007 '); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(substr(sale_date, 1, 4) = '2020'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201912' OR sale_date >= ' 202006'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date > '201912' AND sale_date <= '202004'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(NOT sale_date > '202004'); -- Delete partitions by using a condition. The condition is specified by expressions th at have the OR relationship. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'), PARTITION(sale_date >= '202007'); -- Add partitions in other formats. ALTER TABLE sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '2019-10-05'); PARTITION (sale_date= '2019-10-06') PARTITION (sale_date= '2019-10-07'); -- Delete multiple partitions at a time and use regular expressions to match the partit ions you want to delete.
```

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date RLIKE '2019-\\d+-\\d+'); -- Create a table that has multi-level partitions. CREATE TABLE IF NOT EXISTS region_sale_detail( shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING , region STRING ); -- Add partitions. ALTER TABLE region_sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '201910',region = 'shanghai') PARTITION (sale_date= '201911',region = 'shanghai') PARTITION (sale_date= '201912',region = 'shanghai') PARTITION (sale_date= '202001',region = 'shanghai') PARTITION (sale_date= '202002',region = 'shanghai') PARTITION (sale_date= '201910',region = 'beijing') PARTITION (sale_date= '201911',region = 'beijing') PARTITION (sale_date= '201912',region = 'beijing') PARTITION (sale_date= '202001',region = 'beijing') PARTITION (sale_date= '202002',region = 'beijing'); -- Delete the partitions that meet the sale_date < '201911' and region = 'beijing' cond itions from the table at a time. ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'),PARTITION(region = 'beijing');
```

If you execute the following statement, the following error is returned: `FAILED: ODPS-0130071:`

```
[1,82] Semantic analysis exception - invalid column reference region, partition expression must have one and only one column reference . -- An error is returned because PARTITION partition_filtercondition can be specified on ly for one partition key column. ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911' AND region = 'beijing');
```

##### Add columns or comments

This topic describes how to use DDL statements to add columns or comments. Syntax:

```
ALTER TABLE table_name ADD COLUMNS (col_name1 type1,col_name2 type2...) ; -- Add columns. ALTER TABLE table_name ADD COLUMNS (col_name1 type1 comment 'XXX',col_name2 type2 comme nt 'XXX'); -- Add both columns and comments.
```

Examples:

```
ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING, education BIGINT); -- Add two columns to the sale_detail table. ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING comment 'Customer', education BIGINT comment 'Education' ); -- Add two columns and their comments to the sale_detail table.
```

##### Change the name of a column

This topic describes how to use a DDL statement to change the name of a column. Syntax:

```
ALTER TABLE table_name CHANGE COLUMN old_col_name RENAME TO new_col_name;
```

**Note**

The column specified by **old_col_name** must exist in the table. The table cannot contain the column specified by **new_col_name**. Examples:

```
ALTER TABLE sale_detail CHANGE COLUMN customer_name RENAME TO customer; -- Change the name of a column in the sale_detail table.
```

##### Modify the comment of a column

This topic describes how to use a DDL statement to modify the comment of a column. Syntax:

```
ALTER TABLE table_name CHANGE COLUMN col_name COMMENT 'comment_string';
```

**Note**

The value of **comment_string** cannot exceed 1,024 bytes. The data type and position of a column cannot be changed. The column specified by **col_name** must exist. Examples:

```
ALTER TABLE sale_detail CHANGE COLUMN customer COMMENT 'customer'; -- Modify the comment of a column in the sale_detail table.
```

##### Modify the name and comment of a

**column at the same time**

This topic describes how to use a DDL statement to modify the name and comment of a column at the same time. Syntax:

```
ALTER TABLE table_name CHANGE COLUMN old_col_name new_col_name column_type COMMENT 'col umn_comment';
```

**Note**

The column specified by **old_col_name** must exist. The table cannot contain the column specified by **new_col_name**. The data type and position of a column cannot be changed. The value of **column_comment** cannot exceed 1,024 bytes. Examples:

```
ALTER TABLE sale_detail CHANGE COLUMN customer customer_name string COMMENT 'Customer'; -- Modify the name and comment of a column in the sale_detail table.
```

##### Change LastDataModifiedTime of a non-

**partitioned table or a partition in a partitioned**

**table.**

MaxCompute SQL allows you to execute the TOUCH operation to modify the value of
**LastDataModifiedTime** for a non-partitioned table or a partition in a partitioned table. This
operation changes the value of **LastDataModifiedTime** to the current time. This topic describes how to use a DDL statement to change the value of LastDataModifiedTime for a non-partitioned table or a partition in a partitioned table. Syntax:

```
ALTER TABLE table_name TOUCH; -- Change the value of LastDataModifiedTime for a non-partitioned table. ALTER TABLE table_name TOUCH PARTITION(partition_col='partition_col_value', ...); -- Change the value of LastDataModifiedTime for a partition in a partitioned table.
```

**Note**

If the table specified by **table_name** does not exist, an error is returned. If the partition specified by **partition_col='partition_col_value'** does not exist, an error is returned. This operation changes the value of **LastDataModifiedTime** for a non-partitioned table or a partition in a partitioned table. In this case, MaxCompute considers a change to the table data and recalculates the lifecycle. Sample statements:

```
ALTER TABLE result_table TOUCH; -- Change the value of LastDataModifiedTime for a non-partitioned table. ALTER TABLE sale_detail TOUCH PARTITION(sale_date='201712'); -- Change the value of LastDataModifiedTime for a partition in a partitioned table.
```

##### Modify partition values

This topic describes how to use a DDL statement to modify partition values. Syntax:

```
ALTER TABLE table_name PARTITION (partition_col1 = 'partition_col_value1', partition_col2 = 'partiton_col_value2', ...) RENAME TO PARTITION (partition_col1 = 'partition_col_newvalue1', partition_col2 = 'part iton_col_newvalue2', ...) ;
```

**Note**

This statement can modify only the values rather than the names of partition key columns. To modify the values of one or more partitions in a table that has multi-level partitions, you must specify the partition values at each level. If the table specified by **table_name** does not exist, an error is returned. Examples:

```
ALTER TABLE sale_detail PARTITION (sale_date = '201712', region = 'hangzhou') RENAME TO PARTITION (sale_date = '201710', region = 'beijing'); -- Modify the partition values in the sale_detail table.
```

##### Merge partitions

MaxCompute SQL allows you to execute the `MERGE PARTITION` statement to merge multiple partitions of a partitioned table into one partition. This operation deletes the dimension information about the merged partitions and moves data to a specific partition. This topic describes how to use a DDL statement to merge partitions. Syntax

```
ALTER TABLE <tableName> MERGE [IF EXISTS] PARTITION(<predicate>) [, PARTITION(<predicate2>) ...] OVERWRITE PARTITION(<fullPartitionSpec>) [PURGE];
```

**Note**

If you do not specify **IF EXISTS** and the partition that you want to merge does not exist, an error is returned. If you specify **IF EXISTS** but no partitions meet the merge conditions, no new partitions are generated. If operations such as INSERT, RENAME, and DROP are performed at the same time to modify the source data when you execute the preceding statement, an error is returned even if you specified **IF EXISTS**. If the PURGE attribute is specified, you cannot back up or restore merged partitions by using metadata snapshots. Limits and troubleshooting: Partitions of external tables cannot be merged. After partitions of a clustered table are merged into one partition, the partition does not have the clustering attribute. You can merge a maximum of 4,000 partitions at a time. If an error that indicates the catalog server is busy is returned, you can try again later. If a hard link in Apsara Distributed File System is faulty, you can clear the recycle bin and try again. Sample code:

```
odps@ jet_zwz>SHOW PARTITIONS intpstringstringstring; ds=20181101/hh=00/mm=00 ds=20181101/hh=00/mm=10 ds=20181101/hh=10/mm=00 ds=20181101/hh=10/mm=10
```

`OK`

```
odps@ jet_zwz>DESC intpstringstringstring; +------------+------------+------------+------------+
| value      | ds         | hh         | mm         |
+------------+------------+------------+------------+
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 00         | 10         |
| 1          | 20181101   | 10         | 00         |
| 1          | 20181101   | 10         | 10         |
+------------+------------+------------+------------+ -- Partitions and data of a partitioned table: odps@ jet_zwz>ALTER TABLE intpstringstringstring MERGE PARTITION(hh='00') OVERWRITE PAR TITION(ds='20181101', hh='00', mm='00'); ID = 20190404025755844g80qwa7a
```

`OK`

```
-- Merge all partitions that meet the hh='00' condition into the ds=20181101/hh=00/mm=00 partition. odps@ jet_zwz>SHOW PARTITIONS intpstringstringstring; ds=20181101/hh=00/mm=00 ds=20181101/hh=10/mm=00 ds=20181101/hh=10/mm=10
```

`OK`

```
-- Query the partitions of the table after the merge operation is performed. odps@ jet_zwz>DESC intpstringstringstring; +------------+------------+------------+------------+
| value      | ds         | hh         | mm         |
+------------+------------+------------+------------+
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 10         | 00         |
| 1          | 20181101   | 10         | 10         |
+------------+------------+------------+------------+ -- Data in two partitions that meet the specified condition is merged into the specifie d partition.
```

### DML statements

#### INSERT

##### Update data in a table

This topic describes how to use an INSERT statement to update data in a table. The `INSERT OVERWRITE` and `INSERT INTO` statements are used to write the data processing results of MaxCompute SQL to a destination table. The `INSERT INTO` statement inserts data into a table or partition. The `INSERT INTO` statement cannot be used to insert data into clustered tables. If you want to insert a small amount of test data, you can use this statement with VALUES. The `INSERT OVERWRITE` statement clears the original data in a table or partition and inserts data into the table or partition. The `INSERT OVERWRITE` statement cannot be used to insert data into specific columns. Syntax:

```
INSERT OVERWRITE|INTO TABLE table_name [PARTITION (partcol1=val1, partcol2=val2 ...)] [ (col1,col2 ...)] select_statement FROM from_statement [ZORDER BY zcol1 [, zcol2 ...]] ;
```

**Note**

The INSERT syntax in MaxCompute is different from that in MySQL or Oracle. In MaxCompute, `INSERT OVERWRITE` or `INSERT INTO` must be followed by the keyword TABLE, instead of directly followed by the **table_name** parameter. To ensure data consistency during concurrent writes, MaxCompute uses the atomicity, consistency, isolation, durability (ACID) properties. The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. If the destination table consists of static partitions and you want to insert data into a static partition, partition key columns cannot be included in the SELECT clause. Parameters:
**table_name**: the name of the table into which you want to insert data.
**PARTITION (partcol1=val1, partcol2=val2 ...)**: the name of the partition into which you
want to insert data. The value must be a constant. It cannot be an expression, such as a function.
**[(col1,col2 ...)]**: the names of the columns into which you want to insert data. This
parameter is not supported in the `INSERT OVERWRITE` statement.
**select_statement**: the SELECT clause used to query the data that you want to insert from
the source table.
**from_statement**: the FROM clause used to indicate the data source. For example, the
value can be the name of the source table.
**[ZORDER BY zcol1 [, zcol2 ...]]**: the columns that are used to sort data. If you write data
to a table or partition, you can use this clause to place rows with similar data records in the columns specified in select_statement in adjacent positions. This improves filtering performance for queries and reduces storage costs. The `ORDER BY x, y` clause sorts data records based on the ordering of x coming before y. The `ZORDER BY x, y` clause places rows that have similar x values in adjacent positions and rows that have similar y values in adjacent positions. If the filter condition of an SQL query statement includes sort columns, the ORDER BY clause filters and sorts data based on x, whereas the ZORDER BY clause filters and sorts data based on x or on both x and y. ZORDER BY increases the column store ratio.

**Note**

The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. If the destination table consists of static partitions and you want to insert data into a partition, partition key columns cannot be included in the SELECT clause. The ZORDER BY clause occupies a large number of resources to write data. As a result, data writes based on ZORDER BY require a longer time than data writes without ordering. If the destination table is a clustered table, ZORDER BY is not supported. ZORDER BY can be used with DISTRIBUTE BY. However, ZORDER BY cannot be used with ORDER BY, CLUSTER BY, or SORT BY. Examples: Calculate the sales of different regions listed in the sale_detail table. Then, insert the obtained data into the sale_detail_insert table.

```
-- Create a partitioned table named sale_detail, add partitions, and insert data into t he table. You do not need to define partition key columns as standard columns in the st atement that is used to create the source table. CREATE TABLE IF NOT EXISTS sale_detail
```

`(`

```
shop_name string, customer_id string, total_price double
```

`)`

```
PARTITIONED BY (sale_date STRING,region STRING); -- Add partitions to the source table. ALTER TABLE sale_detail ADD PARTITION (sale_date='2013', region='china'); -- Insert data into the source table. INSERT INTO TABLE table_name can be abbreviated a s INSERT INTO table_name. However, INSERT OVERWRITE TABLE table_name has no abbreviatio
```

`n.`

```
INSERT INTO sale_detail PARTITION (sale_date='2013', region='china') VALUES ('s1','c1',100.1),('s2','c2',100.2),('s3','c3',100.3); -- Create a destination table named sale_detail_insert that has the same schema as the source table. CREATE TABLE sale_detail_insert LIKE sale_detail; -- Add partitions to the destination table. ALTER TABLE sale_detail_insert ADD PARTITION (sale_date='2013', region='china'); -- Extract data from the sale_detail table and insert the data into the sale_detail_insert table. -- Fields in the destination table do not need to be declared or rearranged. -- If the destination table consists of static partitions and partition fields have bee n declared in PARTITION(), you do not need to include these fields in the SELECT clause . You only need to search for the fields based on the sequence of standard columns in t he destination table and sequentially map these fields to those in the destination tabl e. If the destination table consists of dynamic partitions, partition fields must be in cluded in the SELECT clause. For more information, see Insert data into dynamic partiti ons. INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
  SELECT
  shop_name,
  customer_id,
  total_price
  FROM sale_detail
  ZORDER BY customer_id, total_price;
```

Take note of the following points: The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. Example:

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
    SELECT customer_id, shop_name, total_price FROM sale_detail;
```

In the created sale_detail_insert table, the columns **shop_name STRING**, **customer_id**
**STRING**, and **total_price BIGINT** are listed in sequence. If you insert data from the
sale_detail table to the sale_detail_insert table, the data is inserted from the **customer_id**,
**shop_name**, and **total_price** columns in sequence. In this case, data in
**sale_detail.customer_id** is inserted into **sale_detail_insert.shop_name**, and data in
**sale_detail.shop_name** is inserted into **sale_detail_insert.customer_id**.
If you insert data into a partition, partition key columns cannot be included in the SELECT clause. If you execute the following statement, an error is returned because **sale_date** and
**region** are partition key columns. These columns cannot be included in the INSERT
statement that is used to insert table data into a static partition.

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
   SELECT shop_name, customer_id, total_price, sale_date, region FROM sale_detail;
```

The value of **PARTITION** must be a constant and cannot be an expression. The following example shows invalid settings:

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date=datepart('2016-09-18 0 1:10:00', 'yyyy') , region='china')
   SELECT shop_name, customer_id, total_price FROM sale_detail;
```

**Precautions**

If you want to update table data to a dynamic partition, take note of the following points: If you execute the `INSERT INTO PARTITION` statement and the specified partition does not exist, the system automatically creates this partition. If multiple jobs that use the `INSERT INTO PARTITION` statement concurrently run and the specified partitions do not exist, the system attempts to create these partitions. However, only one partition can be created. If you cannot control the concurrency of the jobs that use the `INSERT INTO PARTITION` statement, we recommend that you use the `ALTER TABLE` statement to create partitions in advance.

##### Insert data into multiple objects

This topic describes how to use an INSERT statement to insert data to multiple objects. MaxCompute SQL allows you to insert data into different result tables or partitions by using one SQL statement. Syntax:

```
FROM from_statement INSERT OVERWRITE | INTO TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...)] select_statement1 [FROM from_statement] [INSERT OVERWRITE | INTO TABLE tablename2 [PARTITION (partcol1=val3, partcol2=val4 ...)
```

`]`

```
select_statement2 [FROM from_statement]];
```

**Note**

In most cases, an SQL statement supports up to 256 outputs. If the number of outputs exceeds 256, a syntax error is returned. In a MULTI INSERT statement, non-partitioned tables and destination partitions in a partitioned table must be unique. The `INSERT OVERWRITE` and `INSERT INTO` operations cannot be simultaneously performed on different partitions of a table. If these operations are simultaneously performed on the partitions, an error is returned.
**PARTITION (partcol1=val1, partcol2=val2 ...)**: The parameter values can be
only constants rather than expressions, such as functions. Examples:

```
-- Create a destination table named sale_detail_multi. create table sale_detail_multi like sale_detail; -- Insert data from sale_detail into sale_detail_multi. set odps.sql.allow.fullscan=true; -- Enable the full table scan, which is valid only fo r this session. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price ; -- An error is returned because the same partition appears more than once. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price; -- An error is returned because the INSERT OVERWRITE and INSERT INTO operations are sim ultaneously performed on different partitions of a partitioned table. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert into table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price;
```

##### Insert data into dynamic partitions

This topic describes how to use an INSERT statement to insert data into dynamic partitions. You can use the INSERT OVERWRITE statement to insert data into the following partitions of a partitioned table: Static partitions: You must specify partition values in the INSERT statement to insert data into the specified partitions. Dynamic partitions: You need only to specify the names of partition key columns in the INSERT statement. The values of the partition key columns are provided in the SELECT clause. The system automatically inserts data into the required partitions based on the values. Syntax:

```
INSERT OVERWRITE|INTO TABLE tablename PARTITION (partcol1, partcol2 ...) select_statement FROM from_statement;
```

**Note**

A maximum of 10,000 dynamic partitions can be generated by using the INSERT INTO statement. A maximum of 60,000 dynamic partitions can be generated by using the INSERT OVERWRITE statement. An SQL statement that is used to insert data into dynamic partitions in a distributed environment can generate a maximum of 512 dynamic partitions in a single process. If the number of dynamic partitions exceeds this limit, an exception occurs. The dynamically generated partition values cannot be NULL or contain special characters. If a value is NULL or contains special characters, an exception occurs.

```
FAILED: ODPS-0123031:Partition exception - invalid dynamic partition value: p rovince=xxx
```

If the destination table has multi-level partitions, you can specify some partitions as static partitions in an INSERT statement. However, the static partitions must be high-level partitions. If the destination table is a hash-clustered table, dynamic partitions are not supported. If you insert data into dynamic partitions, the mappings between the columns in
**select_statement** and dynamic partitions in the destination table are determined
by the column sequence, not by the column names. If the sequence of columns in the source table is different from that in the destination table, we recommend that you specify the columns in **select_statement** based on the column sequence in the destination table. Examples: Insert data from a source table into a destination table. You can obtain the partitions generated based on the region field only after the required statement is executed.

```
-- Create a destination table named total_revenues. create table total_revenues (revenue bigint) partitioned by (region string); -- Insert the data from sale_detail into total_revenues. insert overwrite table total_revenues partition(region) select total_price as revenue, region from sale_detail;
```

Insert data from a source table into a destination table. If the destination table has multi-level partitions, level-1 partition sale_date must be specified.

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price,region from sale_detail;
```

To insert data into dynamic partitions, the dynamic partition key columns must be specified in the SELECT clause. Otherwise, the execution fails.

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price from sale_detail;
```

If you specify only low-level subpartitions when you insert data into dynamic partitions, you may fail to insert data into high-level partitions.

```
insert overwrite table sales partition (region='china', sale_date) select shop_name,customer_id,total_price,sale_date from sale_detail;
```

If the data types of values in partition key columns are inconsistent with those in the SELECT clause, an error is returned when data is inserted into dynamic partitions in MaxCompute V1.0. MaxCompute V2.0 supports the implicit conversions of data types.

```
-- Create a destination table named parttable. create table parttable(a int, b double) partitioned by (p string); -- Insert the data from source table src into destination table parttable. insert into parttable partition(p) select key, value, current_timestmap() from src; -- Query data in parttable. select * from parttable;
```

##### VALUES

This topic describes how to use the INSERT...VALUES statement to insert data into a table that contains small amounts of data. Syntax:

```
INSERT INTO TABLE tablename [PARTITION (partcol1=val1, partcol2=val2,...)][(co1name1,colname2,...)] [VALUES (col1_value,col2_value,...),(col1_value,col2_value,...),...]
```

Parameters:
**tablename**: the name of the table into which you want to insert data. The table must be an
existing table.
**[PARTITION (partcol1=val1, partcol2=val2,...)]**: the information about partitions. If you
want to insert data into a partitioned table, you must configure this parameter.
**[(co1name1,colname2,...)]**: the names of the columns in the destination table.
**col_value**: the value in the specified column in the destination table. Separate multiple
values with commas (,). Each value in the column must be a constant. If no values are specified, the default value NULL is used.

**Note**

You can use only the `INSERT INTO` statement rather than the `INSERT OVERWRITE` statement to insert data into specific columns. Functions cannot be used to construct constants for some complex data types, such as ARRAY, in VALUES. However, you can use the following statement to pass the values of the ARRAY type to VALUES:

```
INSERT INTO TABLE srcp (p='abc') SELECT 'a', ARRAY('1', '2', '3');
```

To pass the values of the DATETIME or TIMESTAMP type, you must specify the data type in VALUES.

```
INSERT INTO TABLE srcp (p='abc') VALUES (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789');
```

Example: Insert data into a specific partition.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into the abc partition of the srcp table. INSERT INTO TABLE srcp PARTITION (p='abc') VALUES ('a',1),('b',2),('c',3); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| a          | 1          | abc        |
| b          | 2          | abc        |
| c          | 3          | abc        |
+------------+------------+------------+
```

Insert data into a random partition.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into a partition of the srcp table. INSERT INTO TABLE srcp PARTITION (p)(key,p) VALUES ('d','20170101'),('e','20170101'),(' f','20170101'); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='20170101';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| d          | NULL       | 20170101   |
| e          | NULL       | 20170101   |
| f          | NULL       | 20170101   |
+------------+------------+------------+
```

Use complex data types to construct constants and execute an `INSERT` statement to import data.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string,value array<int>) partitioned by (p string)
```

;

```
-- Add a partition to the srcp table. alter table srcp add if not exists partition (p='abc'); -- Insert data into the abc partition of the srcp table. insert into table srcp partition (p='abc') select 'a', array(1, 2, 3); -- Query data from the srcp table. select * from srcp where p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| a          | [1,2,3]    | abc        |
+------------+------------+------------+
```

Use the `INSERT...VALUES` statement to write data of the DATETIME or TIMESTAMP type.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string, value timestamp) partitioned by (p string)
```

;

```
-- Add a partition to the srcp table. alter table srcp add if not exists partition (p='abc'); -- Insert data into the abc partition of the srcp table. insert into table srcp partition (p='abc') values (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789'); -- Query data from the srcp table. select * from srcp where p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| 2017-11-11 00:00:00 | 2017-11-11 00:00:00.123456789 | abc        |
+------------+------------+------------+
```

**Features of VALUES TABLE**

When you use INSERT…VALUES, the values after VALUES must be constants. If you want to perform simple computing operations on the inserted data, we recommend that you use VALUES TABLE of MaxCompute. Syntax:

```
values (<col1_value>,<col2_value>,...),(<col1_value>,<col2_value>,...),<table_name> (<c ol1_name> ,<col2_name>,...)...
```

You can use VALUES TABLE in the following scenarios: If no physical tables are available, create a table that contains multiple rows of data and perform computing operations on the table. For example, VALUES (…), (...) t(a, b) defines that a table named t contains the a and b columns. The a column is of the STRING data type and the b column is of the BIGINT data type. The data type of a column must be derived from the VALUES list.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into the srcp table. INSERT INTO TABLE srcp PARTITION (p) SELECT concat(a,b), length(a)+length(b),'20170102' FROM VALUES ('d',4),('e',5),('f',6) t(a,b); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='20170102';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| d4         | 2          | 20170102   |
| e5         | 2          | 20170102   |
| f6         | 2          | 20170102   |
+------------+------------+------------+
```

Use VALUES TABLE rather than the combination of `SELECT * FROM` and `UNION ALL` to create a constant-type table.

```
SELECT 1 c UNION ALL SELECT 2 c; -- The preceding statement is equivalent to the following statement: SELECT * FROM VALUES (1), (2) t(c);
```

The following result is returned:

```
+------------+
| c          |
+------------+
| 1          |
| 2          |
+------------+
```

Use the special forms of VALUES TABLE. If the expressions of the SELECT statement do not contain upstream table data, you can execute the SELECT statement without the FROM clause. In this case, the underlying implementation is to select data from an anonymous VALUES table that contains only one row and no columns. This way, you can test userdefined functions (UDFs) or other functions without the need to manually create DUAL tables.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string,value bigint) partitioned by (p string); -- Insert data into the srcp table. insert into table srcp partition (p) select abs(-1), length('abc'), getdate(); -- Query data from the srcp table. select * from srcp;
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| 1          | 3          | 2020-11-25 18:39:48 |
+------------+------------+------------+
```

**Support for expressions that do not contain constants**

Constant expressions are supported in VALUES expressions. Expressions that do not contain constants are also supported in VALUES expressions. Syntax:

```
select * from values (udf(1)),(to_date('20190101', 'yyyyMMdd')),(getdate()) t(d);
```

#### SELECT

##### SELECT operations

This topic describes how to use SELECT statements for SELECT operations. Syntax

```
SELECT [ALL | DISTINCT] select_expr, select_expr, ... FROM table_reference [WHERE where_condition] [GROUP BY col_list] [ORDER BY order_condition] [DISTRIBUTE BY distribute_condition [SORT BY sort_condition] ] [LIMIT number];
```

**Limits**

A SELECT statement can return a maximum of 10,000 rows of results. However, no limits are imposed when the SELECT statement is used as a clause. If the SELECT statement is used as a clause, the clause returns all results in response to the query from the upper layer. You are not allowed to perform full table scans on partitioned tables by using SELECT statements. If you want to perform a full table scan on a partitioned table, add `set` odps.sql.allow.fullscan=true; before the SQL statement that is used for the full table scan. Then, commit and run the added command with the SQL statement. To enable the full table scan for the entire project, run the following command:

```
setproject odps.sql.allow.fullscan=true;
```

**Column expression (select_expr)**

Each select_expr expression indicates a column from which you want to read data. You can use the following select_expr expressions to read data from a table. Specify the names of the columns from which you want to read data.

```
select shop_name from sale_detail;
```

Use an asterisk (*) to represent all columns.

```
select * from sale_detail; -- You can also use a WHERE clause to specify filter conditions. select * from sale_detail where shop_name like 'hang%';
```

**Use a regular expression.**

Use DISTINCT before the name of a column to filter out duplicate values from the column and return only distinct values. If you use ALL before the name of a column, all values including the duplicate values in the column are returned. If DISTINCT is not used, the default value ALL is used.

```
-- Query data from the region column in the sale_detail table and return only distinc t values. select distinct region from sale_detail;
```

The following result is returned:

```
+------------+
| region     |
+------------+
| shanghai   |
+------------+ -- If you use DISTINCT in a SELECT statement where multiple columns are specified, DI STINCT applies to all the columns you specified, instead of a single column. Mappings exist between columns. If you perform deduplication on multiple columns, the mappings may be destroyed. select distinct region, sale_date from sale_detail;
```

The following result is returned:

```
+------------+------------+
| region     | sale_date  |
+------------+------------+
| shanghai   | 20191110   |
+------------+------------+
```

**Information about a queried destination table (table_reference)**

table_reference specifies the table that you want to query. Nested subqueries are also supported in table_reference. Sample code:

```
select * from (select region from sale_detail) t where region = 'shanghai';
```

**WHERE**

The following table describes the operators that are used as filter conditions supported by the WHERE clause.

| Operator | Description |
|---|---|
| >, <, =, ≥, ≤, and <> | The relational operators. |
| LIKE and RLIKE | The source and pattern parameters of LIKE and RLIKE must be of the STRING type. |
| IN and NOT IN | If a subquery is added after the IN or NOT IN operator, the values in only one column can be returned for the subquery and the number of return values cannot exceed 1,000. |
| BETWEEN…AND | The operator that specifies the query range. |

In the WHERE clause of a SELECT statement, you can specify the partitions that you want to scan in a table to avoid a full table scan.

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date >= '2008' AND sale_detail.sale_date <= '2014';
```

User-defined functions (UDFs) support partition pruning. UDFs are run as small jobs and then replaced with the execution results. You can use one of the following methods to implement UDF-based partition pruning: Add an annotation to the UDF class when you write a UDF.

```
@com.aliyun.odps.udf.annotation.UdfProperty(isDeterministic=true)
```

**Important**

**com.aliyun.odps.udf.annotation.UdfProperty** defines that the version of
referenced **odps-sdk-udf** must be 0.30.x or later in odps-sdk-udf.jar. Add the set odps.sql.udf.ppr.deterministic = true; flag before the SQL statement that you want to execute. Then, all UDFs in the SQL statement are considered
**deterministic** UDFs.

| Note The preceding SET command backfills partitions with the results of jobs. A maximum of 1,000 partitions can be backfilled with the results of jobs. If you add an annotation to a UDF class, an error that indicates more than 1,000 partitions are backfilled may be returned. To ignore this error, you can run the set odps.sql.udf.ppr.to.subquery = false; command. After you run this command, UDF-based partition pruning is no longer in effect. |   |   |
|---|---|---|
|   | set odps.sql.udf.ppr.to.subquery |   |

Precautions When you use a UDF to perform partition pruning, the UDF must be placed in the `WHERE` clause that is used to query a table. UDF-based partition pruning takes effect only when you place the UDF in the WHERE clause. Sample statement of correct usage:

```
-- Place a UDF in the WHERE clause that is used to query the source table. SELECT key, value from srcp where udf(ds) = 'xx';
```

Sample statement of incorrect usage:

```
-- Place a UDF after the ON condition in the JOIN clause. UDF-based partition pruni ng does not take effect. SELECT A.c1, A.c2 from srcp1 A join srcp2 B on A.c1 = B.c1 and udf(A.ds) ='xx';
```

The WHERE clause in an SQL statement can include the BETWEEN...AND operator. Sample code:

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date BETWEEN '2008' AND '2014';
```

**GROUP BY**

In most cases, the GROUP BY clause is used with aggregate functions. If a SELECT statement contains aggregate functions, you must comply with the following rules: The operation specified by the GROUP BY clause takes precedence over the operation specified by the SELECT statement. Therefore, columns in the GROUP BY clause can be specified by column names of the input table of the SELECT statement or an expression that is formed by columns of the input table of the SELECT statement. The columns in GROUP BY cannot be the aliases of the output columns from SELECT. The value of GROUP BY may be both a column name or an expression composed of input table columns and the alias of an output column from SELECT. In this case, the column name or expression is used as the value of GROUP BY. If set hive.groupby.position.alias=true; is added before an SQL statement, integer constants in the GROUP BY clause are considered column numbers in a SELECT operation.

```
set hive.groupby.position.alias=true; -- Run this command with the next SELECT statement. select region, sum(total_price) from sale_detail group by 1; -- 1 indicates the region column, which is the first column read by the SELECT statem ent. This statement groups the table data based on the values in the region column an d returns distinct region values and total sales of each group. -- The statement uses the name of the region column in the input table as the value of the GROUP BY clause and groups the table data based on the values in the region column. select region from sale_detail group by region; -- The statement groups the table data based on the values in the region column and ret urns the total sales of each group. select sum(total_price) from sale_detail group by region; -- The statement groups the table data based on the values in the region column and ret urns distinct values and total sales of each group. select region, sum(total_price) from sale_detail group by region; -- An error is returned because the alias of the column in the SELECT operation is used as the value of the GROUP BY clause. select region as r from sale_detail group by r; -- A complete expression of the column is required. select 2 + total_price as r from sale_detail group by 2 + total_price; -- An error is returned because all the columns that do not use aggregate functions in the SELECT operation must be included in the GROUP BY clause. select region, total_price from sale_detail group by region; -- The statement can be successfully executed because all the columns that do not use a ggregate functions are included in the GROUP BY clause. select region, total_price from sale_detail group by region, total_price;
```

**ORDER BY|DISTRIBUTE BY|SORT BY**

ORDER BY: This clause is used to sort all data records based on the specified columns. To sort data records in descending order, use the **desc** keyword. By default, data records are sorted in ascending order. When you use ORDER BY to sort data records, null is considered the smallest value. This rule is consistent with MySQL, but is different from Oracle. The columns in the ORDER BY clause must be the aliases of the columns in the SELECT operation. If you want to query a column but the column alias is not specified in the SELECT statement, the column name is used as the column alias. If set hive.orderby.position.alias=true; is added before an SQL statement, integer constants in the ORDER BY clause are considered column numbers in a SELECT operation.

```
-- Configure the flag. set hive.orderby.position.alias=true; -- Create a table named src. create table src(key BIGINT,value BIGINT); -- Query the src table and sort the records that are returned in ascending order by value. SELECT * FROM src ORDER BY 2 limit 100; The preceding statement is equivalent to the following statement: SELECT * FROM src ORDER BY value limit 100;
```

You can use the OFFSET clause with the ORDER BY LIMIT clause to skip the number of rows specified by OFFSET.

```
-- Sort the rows of the src table in ascending order by key, and return row 11 to r ow 30. OFFSET 10 indicates that the first 10 rows are skipped, and LIMIT 20 indicat es that a maximum of 20 rows can be returned. SELECT * FROM src ORDER BY key LIMIT 20 OFFSET 10; -- Query the sale_detail table and sort the first 100 records that are returned in as cending order by region. SELECT * FROM sale_detail ORDER BY region LIMIT 100; -- By default, the LIMIT clause is used with the ORDER BY clause. If only the ORDER B Y clause is used, an error is returned. SELECT * FROM sale_detail ORDER BY region; -- ORDER BY is followed by a column alias. SELECT region AS r FROM sale_detail ORDER BY region LIMIT 100; SELECT region AS r FROM sale_detail ORDER BY r LIMIT 100;
```

DISTRIBUTE BY: This clause is used to shard data based on hash values of specific columns. You must specify the alias of an output column from the SELECT operation as the value of the DISTRIBUTE BY clause.

```
-- The statement queries the values of the region column from the sale_detail table a nd performs hash partitioning on data based on the values of the region column. SELECT region FROM sale_detail DISTRIBUTE BY region; -- The statement can be executed because the column name is used as the alias. SELECT region AS r FROM sale_detail DISTRIBUTE BY region; The preceding statement is equivalent to the following statement: SELECT region AS r FROM sale_detail DISTRIBUTE BY r;
```

SORT BY: This clause is used to sort specific data records. You can add a keyword, such as ASC or DESC, to sort specific data records. If ASC is used, data records are sorted in ascending order. If DESC is used, data records are sorted in descending order. If SORT BY is not followed by a keyword, data records are sorted in ascending order by default. If the SORT BY clause is preceded by the DISTRIBUTE BY clause, the SORT BY clause sorts specific results of the DISTRIBUTE BY clause. The DISTRIBUTE BY clause determines how to distribute the output values of the map stages to reducers. To prevent duplicate output values from being distributed to different reducers or to process the same group of data together, you can use the DISTRIBUTE BY clause. This ensures that the same group of data is distributed to the same reducer. Then, use SORT BY to sort the group of data. Example

```
-- The statement queries values in the region column of the sale_detail table, shar ds data based on the hash values of the region column, and then sorts the sharded d ata. SELECT region FROM sale_detail DISTRIBUTE BY region SORT BY region;
```

If the SORT BY clause is not preceded by the DISTRIBUTE BY clause, the SORT BY clause sorts the data of each reducer. This process sorts specific data records. This ensures that the output values of each reducer are sorted and increases the data compression ratio. If data is filtered during data reading, the amount of data read from disks is reduced, which makes subsequent global sorting more efficient. Example

```
SELECT region FROM sale_detail SORT BY region;
```

**Note**

The value of ORDER BY, DISTRIBUTE BY, or SORT BY must be the alias of an output column from the SELECT statement. Column aliases can be Chinese. During the parsing of MaxCompute SQL statements, the ORDER BY, DISTRIBUTE BY, or SORT BY clause is executed after the SELECT operation. Therefore, the value of ORDER BY, DISTRIBUTE BY, or SORT BY must be the alias of an output column from the SELECT operation. The ORDER BY clause cannot be used with the DISTRIBUTE BY or SORT BY clause. The GROUP BY clause cannot be used with the DISTRIBUTE BY or SORT BY clause.

**LIMIT**

The **number** in the LIMIT clause is a constant that limits the number of rows to return. Remove the limit on the simultaneous execution of the ORDER BY and LIMIT clauses The ORDER BY clause needs to sort all data of a single node. By default, the ORDER BY clause is used with the LIMIT clause to prevent a single node from processing large amounts of data. You can remove the limit on the simultaneous execution of the ORDER BY and LIMIT clauses for a project or session.

| To remove the limit for a project, run the | setproject |
|---|---|
| odps.sql.validate.orderby.limit=false; |   |
|   | command. |

| To remove the limit for a session, run the | setproject command with the SQL statement. |
|---|---|
| odps.sql.validate.orderby.limit=false; |   |

**Note**

If a single node has large amounts of data to sort after the limit is removed, more resources and time are required. Limits on the number of rows to return If you use a SELECT statement without the LIMIT clause or the number in the LIMIT clause exceeds the specified upper limit, you can view only the rows within the upper limit. The maximum number of rows that can be displayed varies based on projects. You can use one of the following methods to control the maximum number: If project data protection is disabled by setting **use_instance_tunnel** to true and
**instance_tunnel_max_record** is not specified, no limits are imposed on the number of
rows to return. For more information about project data protection, see Data protection. For more information about the configurations of **use_instance_tunnel=true** and
**instance_tunnel_max_record**, see Tunnel operations.
If project data protection is enabled, the number of rows to return is limited by
**READ_TABLE_MAX_ROW**. The maximum value of this parameter is 10000.

**Note**

You can run the SHOW SecurityConfiguration; command to view the value of
**ProjectProtection**. If **ProjectProtection** is set to true, you can determine whether to
disable project data protection. You can run the set ProjectProtection=false; command to disable project data protection. By default, **ProjectProtection** is disabled. For more information about project data protection, see Data protection.

##### Subquery

This topic describes how to use a SELECT statement to perform subqueries. A common SELECT statement reads data from multiple tables, such as, `select column_1,` `column_2 ... from table_name` . The query object can be another SELECT operation, which is a subquery. Syntax:

```
select * from (select shop_name from sale_detail) a;
```

**Important**

A subquery must have an alias. Examples:

```
create table shop as select * from sale_detail; select a.shop_name, a.customer_id, a.total_price from (select * from shop) a join sale_detail on a.shop_name = sale_detail.shop_name;
```

**Note**

In a FROM clause, a subquery can be used as a table, which supports a JOIN operation with other tables or subqueries.

##### UNION ALL

This topic describes how to use a SELECT statement to perform UNION ALL operations. Syntax:

```
select_statement union all select_statement
```

**Note**

The UNION ALL clause is used to combine two or more datasets returned from a SELECT operation into one dataset. If duplicate rows exist in the results, all rows that meet the condition are returned, with duplicate rows retained. MaxCompute SQL does not support UNION ALL between two top-level query statements. To combine the query results of the two statements, you must rewrite the UNION ALL clause as a subquery. Syntax before rewriting:

```
select * from sale_detail where region = 'hangzhou' union all select * from sale_detail where region = 'shanghai';
```

Syntax after rewriting:

```
select * from ( select * from sale_detail where region = 'hangzhou' union all select * from sale_detail where region = 'shanghai') t;
```

The syntax that uses a pair of parentheses to specify the priority of UNION ALL is supported. Examples:

```
SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3); -- Execute the UNION ALL clause for the src2 and src3 tables. Then, execute the UNION A LL clause for the src table and the result of the first UNION ALL operation.
```

**Important**

For a UNION ALL operation, all subqueries must have the same number of columns, column names, and column types. If the column names are inconsistent, use column aliases. In most cases, MaxCompute allows a UNION ALL operation for a maximum of 256 subqueries. If the limit is exceeded, a syntax error is returned.

##### JOIN

This topic describes how to use SELECT statements to perform JOIN operations. MaxCompute supports multiple JOIN operations in an SQL statement. MaxCompute does not support CROSS JOIN. A CROSS JOIN operation joins two tables without the need to specify conditions in the ON clause. Syntax:

```
join_table:
        table_reference JOIN table_factor [join_condition]
        | table_reference {LEFT OUTER|RIGHT OUTER|FULL OUTER|INNER|NATURAL} JOIN
table_reference join_condition
    table_reference:
        table_factor
        | join_table
    table_factor:
        tbl_name [alias]
        | table_subquery alias
        | ( table_references )
    join_condition:
        ON equality_expression ( AND equality_expression )
```

**Note**

**equality_expression** indicates an equality expression.
Types of JOIN operations: LEFT OUTER JOIN: shortened as LEFT JOIN. It returns all rows in the left table, including the rows that do not match any rows in the right table.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a LEFT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name; -- Both the shop and sale_detail tables have the shop_name column. You must use alias es to distinguish the columns in the SELECT operation.
```

**Note**

If the values in some rows of the right table are duplicate, we recommend that you do not consecutively use LEFT JOIN. If you consecutively use LEFT JOIN, data bloat may occur and interrupt your jobs. RIGHT OUTER JOIN: shortened as RIGHT JOIN. It returns all rows in the right table, including rows that do not match any rows in the left table.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a RIGHT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

FULL OUTER JOIN: shortened as FULL JOIN. It returns all rows in both the left and right tables.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

INNER JOIN: The INNER keyword can be omitted. INNER JOIN only returns rows in which a match between the two tables exists.

```
SELECT a.shop_name FROM shop a INNER JOIN sale_detail b ON a.shop_name=b.shop_name; SELECT a.shop_name FROM shop a JOIN sale_detail b ON a.shop_name=b.shop_name;
```

NATURAL JOIN: In a NATURAL JOIN operation, the conditions used to join two tables are automatically determined based on the common fields in the two tables. MaxCompute supports OUTER NATURAL JOIN. You can use the USING clause so that the JOIN operation returns common fields only once.

```
SELECT * FROM src NATURAL JOIN src2; -- Both the src and src2 tables include the key1 and key2 fields. In this case, the p receding statement is equivalent to the following statement: SELECT src.key1 AS key1, src.key2 AS key2, src.a1, src.a2, src2.b1, src2.b2 FROM src INNER JOIN src2 ON src.key1 = src2.key1 AND src.key2 = src2.key2;
```

Implicit JOIN operation: A JOIN operation that is performed without the need to specify the JOIN keyword.

```
SELECT * FROM table1, table2 WHERE table1.id = table2.id; -- The preceding statement is equivalent to the following statement: SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;
```

Join conditions: You must use equi-joins and combine conditions by using AND. You can use non-equi joins or combine multiple conditions by using OR in a MAPJOIN operation.

```
-- MaxCompute supports multiple JOIN operations in an SQL statement. SELECT a. * FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name
        FULL OUTER JOIN sale_detail c ON a.shop_name=c.shop_name;
-- MaxCompute does not support non-equi joins and returns an error. SELECT a. * FROM shop a JOIN sale_detail b ON a.shop_name ! = b.shop_name;
```

You can use parentheses () to specify the priority of JOIN operations. The JOIN operation enclosed in parentheses () has a high priority.

```
SELECT * FROM src JOIN (src2 JOIN src3 on xxx) ON yyy; -- In the preceding statement, src2 JOIN src3 is first executed. Then, the JOIN operati on is performed for the src table and the result of the first JOIN operation.
```

Examples: The test_table_a and test_table_b tables are available. You want to query the two tables for the rows whose values in the **origin** column are equal to those in the **id** column and whose data timestamp is greater than 20180101. If you use LEFT JOIN, all rows in the left table test_table_a are returned.

```
SELECT s.id
    ,s.name
    ,s.origin
    ,d.value
FROM (SELECT * FROM test_table_a WHERE ds > "20180101" ) s LEFT JOIN (SELECT * FROM test_table_b WHERE ds > "20180101") d ON s.origin = d.id;
```

##### MAPJOIN hint

This topic describes how to specify MAPJOIN in a SELECT statement to join a large table with one or more small tables.

**Background information**

You can explicitly specify MAPJOIN in a SELECT statement to join a large table with one or more small tables. MAPJOIN speeds up your query. A JOIN operation contains three stages: map, shuffle, and reduce. In most cases, tables are joined in the reduce stage. MAPJOIN joins tables in the map stage instead of the reduce stage. This reduces data transmission time and system resource consumption and optimizes jobs. In the map stage, MAPJOIN loads all data in the specified tables into the memory of the program that executes the JOIN operation. The tables specified for MAPJOIN must be small tables, and the total memory occupied by the table data cannot exceed 512 MB. When a large table is joined with one or more small tables, MAPJOIN loads all data in the specified small tables into the memory of the program that executes the JOIN operation. This way, tables are connected in the map stage to accelerate the execution of the JOIN operation.

**Usage**

To use MAPJOIN, you must specify the hint `/*+ MAPJOIN(table) */` in a SELECT statement. For example, sale_detail is a large table whose alias is b, and shop is a small table whose alias is a. The following statement is used to perform a common JOIN operation:

```
SELECT a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

The following statement is used to perform a JOIN operation with MAPJOIN specified:

```
SELECT /* + MAPJOIN(a) */
        a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

**Limits**

When you use MAPJOIN and reference a small table or a subquery, you must reference the alias of the table or subquery. MAPJOIN supports small tables in subqueries. The left table in a LEFT OUTER JOIN operation must be a large table. The right table in a RIGHT OUTER JOIN operation must be a large table. Either the left or right table in an INNER JOIN operation can be a large table. MAPJOIN cannot be used in a FULL OUTER JOIN operation. For MAPJOIN, you can use non-equi joins or combine conditions by using OR. You can leave

| MAPJOIN ON 1 = 1 |   |
|---|---|
|   | , to calcu |

However, this calculation method may increase the data amount. MaxCompute allows you to specify a maximum of 128 small tables for MAPJOIN. If you specify more than 128 small tables, a syntax error is returned. Separate small tables with commas (,), such as `/*+MAPJOIN(a,b,c)*/` . The total memory occupied by small tables cannot exceed 512 MB. MaxCompute compresses your data before storage. As a result, the data amount of small tables sharply increases after they are loaded into the memory. 512 MB indicates the maximum data amount after small tables are loaded into the memory. In a MaxCompute SQL statement, you cannot use complex join conditions, such as non-equi joins or the OR logical operator, in the ON condition for a common JOIN operation. However, you can use them for a JOIN operation with MAPJOIN specified.

```
SELECT /* + MAPJOIN(a) */
        a.total_price,
        b.total_price
FROM shop a JOIN sale_detail b ON a.total_price < b.total_price OR a.total_price + b.total_price < 500;
```

##### SELECT TRANSFORM

###### Overview

This topic describes the syntax of the SELECT TRANSFORM statement in MaxCompute. The SELECT TRANSFORM statement allows you to start a specific child process and insert data in the required format into the child process by using standard input. Then, the SELECT TRANSFORM statement parses the standard output of the child process to obtain the output data. The SELECT TRANSFORM statement allows you to run scripts in other programming languages without the need to write user-defined functions (UDFs). Syntax:

```
SELECT TRANSFORM(arg1, arg2 ...) (ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value)) USING 'unix_command_line' (RESOURCES 'res_name' (',' 'res_name')*) ( AS col1, col2 ...) (ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value))
```

Parameters:
**SELECT TRANSFORM**: the keyword, which can be replaced with the **MAP** or **REDUCE**
keyword. These keywords have the same syntax. We recommend that you use **SELECT**
**TRANSFORM** to make the syntax clearer.
**(arg1, arg2 ...)**: the input data. The data format is similar to that of the SELECT statement.
In the default format, the results of expressions for each parameter are implicitly converted into a value of the STRING type. Then, the parameters are combined by **\t** and passed to the specified child process.

**Note**

The format is configurable. For more information, see **ROW FORMAT**.
**USING**: the commands that are used to start a child process. Take note of the following
points: In most MaxCompute SQL statements, the USING clause specifies resources. However, in the SELECT TRANSFORM statement, the USING clause specifies the commands to start a child process. The USING clause is used to ensure compatibility with the Hive syntax. The syntax of the USING clause is similar to that of a shell script. However, instead of running the shell script, the USING clause creates a child process based on the input commands. Therefore, some shell features, such as input and output redirection, pipe, and loop, cannot be used. A shell script can be used as the commands to start a child process if necessary.
**RESOURCES**: the resources that the specified child process can access. You can use one of
the following methods to specify resources: Use the RESOURCES clause. Example: `using 'sh foo.sh bar.txt' resources`

```
'foo.sh','bar.txt' .
```

Add the set odps.sql.session.resources=foo.sh,bar.txt; flag before SQL statements to specify resources.

**Note**

This is a global configuration. It allows all **SELECT TRANSFORM** statements to access the specified resources. Separate multiple resource files with commas (,).
**ROW FORMAT**: the input and output formats. The syntax includes two ROW FORMAT
clauses. The first clause specifies the format of the input data, and the second clause specifies the format of the output data. By default, **\t** is used as a column delimiter, **\n** is used as a row delimiter, and **\N** is used to represent NULL values.

**Note**

For field_delimiter, character_escape, and line_separator, only one character is accepted. If you specify a string, the first character in the string takes priority over the others. MaxCompute supports syntax in the formats that are specified by Hive, such as
**inputRecordReader**, **outputRecordReader**, and **SerDe**. You must enable the
Hive-compatible mode to use the syntax. To enable the Hive-compatible mode, add set odps.sql.hive.compatible=true; before SQL statements. If you specify the syntax that is supported by Hive, such as **inputRecordReader** and **outputRecordReader**, the performance of SQL queries may deteriorate.
**AS**: the output columns.

**Note**

If you do not specify the data types for output columns, the STRING type is used. The output data is obtained after the standard output of the child process is parsed. If the data is not of the STRING type, the system implicitly calls the CAST function to convert the data into the STRING type. Exceptions may occur during the conversion process. You must specify data types for all output columns. If you omit the AS keyword, the field before the first **\t** in the standard output data is the key and all the following parts are values. This is equivalent to
**AS(key, value)**.

###### SELECT TRANSFORM examples

###### Call shell scripts

This topic describes how to use SELECT TRANSFORM to call shell scripts and provides examples. Assume that you use a shell script to generate 50 rows of data. The values are from 1 to 50. The following code shows the output of the data field:

```
SELECT TRANSFORM(script) USING 'sh' AS (data) FROM (
            SELECT  'for i in `seq 1 50`; do echo $i; done' AS script
        ) t
```

; You can use shell commands as the input for SELECT TRANSFORM.

**Note**

SELECT TRANSFORM allows you to use the scripts of multiple programming languages, such as AWK, Python, Perl, and shell, as the input to implement simple features. You do not need to compile script files or upload resources, which simplifies development. You can upload a script to implement complex features. For more information, see Call Python scripts.

###### Call Python scripts

This topic describes how to use SELECT TRANSFORM to call Python scripts and provides examples.
1. Compile a Python script file. In this example, the file name is myplus.py.

```java
#! /usr/bin/env python
import sys line = sys.stdin.readline() while line:
    token = line.split('\t')
    if (token[0] == '\\N') or (token[1] == '\\N'):
        print '\\N'
    else:
        print str(token[0]) +'\t' + str(token[1])
    line = sys.stdin.readline()
```

2. Add the Python script file as a resource to MaxCompute.

```
add py ./myplus.py -f;
```

3. Execute SELECT TRANSFORM to call the resource.

```
-- Create a test table. CREATE TABLE testdata(c1 bigint,c2 bigint); -- Insert test data into the test table. INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); -- Execute the following statement: SELECT TRANSFORM (testdata.c1, testdata.c2) USING 'python myplus.py'resources 'myplus.py' AS (result1,result2) FROM testdata; -- The preceding statement is equivalent to the following statement: set odps.sql.session.resources=myplus.py; SELECT TRANSFORM (testdata.c1, testdata.c2) USING 'python myplus.py' AS (result1,result2) FROM testdata;
```

**Note**

In MaxCompute, you can use Python scripts as the input for SELECT TRANSFORM. For example, you can run Python commands to call shell scripts.

```
SELECT TRANSFORM('for i in xrange(1, 50): print i;') USING 'python' AS (data);
```

The following result is returned:

```
+------------+------------+
| result1    | result2    |
+------------+------------+
| 1          | 4          |
|            | NULL       |
| 2          | 5          |
|            | NULL       |
| 3          | 6          |
|            | NULL       |
+------------+------------+
```

###### Call Java scripts

This topic describes how to use SELECT TRANSFORM to call Java scripts and provides examples. Java scripts are called in a similar way to Python scripts. In this example, you must prepare a Java script file, export it as a JAR package, and then execute the `ADD FILE` statement to add the JAR package as a resource to MaxCompute. Then, the resource can be called by using SELECT TRANSFORM.
1. Prepare a Java script file and export it as a JAR package. In this example, the name of the
JAR package is Sum.jar. Sample code:

```java
package com.aliyun.odps.test; import java.util.Scanner public class Sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            String s = sc.nextLine();
            String[] tokens = s.split("\t");
            if (tokens.length < 2) {
                throw new RuntimeException("illegal input");
```

`}`

```java
            if (tokens[0].equals("\\N") || tokens[1].equals("\\N")) {
                System.out.println("\\N");
```

`}`

```java
            System.out.println(Long.parseLong(tokens[0]) +
Long.parseLong(tokens[1]));
```

`}` `}` `}`
2. Add the JAR package as a resource to MaxCompute.

```
add jar . /Sum.jar -f;
```

3. Execute the SELECT TRANSFORM statement to call the resource.

```
-- Create a test table. CREATE TABLE testdata(c1 bigint,c2 bigint); -- Insert test data into the test table. INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); -- Execute the SELECT TRANSFORM statement. SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' resources 'Sum.jar' FROM testdata; -- The preceding statement is equivalent to the following statement: set odps.sql.session.resources=Sum.jar; SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' FROM testdata;
```

The following result is returned:

```
+-----+
| cnt |
+-----+
| 5   |
| 7   |
| 9   |
+-----+
```

You can use the preceding method to run most Java utilities. Although UDTF frameworks are provided for Java and Python, SELECT TRANSFORM makes it easier to compile code. SELECT TRANSFORM is a simpler process because it is not subject to dependencies or format requirements and can be called offline. The paths for Java and Python offline scripts can be obtained from the JAVA_HOME and PYTHON_HOME environment variables.

###### Call the scripts of other programming

**languages**

This topic describes how to use SELECT TRANSFORM to call the scripts of other programming languages and provides examples. SELECT TRANSFORM supports the programming languages described in the preceding topics. It also supports commonly used UNIX commands and script interpreters, such as AWK and Perl interpreters. Example on how to call an AWK script to display the second column:

```
SELECT TRANSFORM(*) USING "awk '//{print $2}'" as (data) from testdata;
```

Example on how to call a Perl script:

```
SELECT TRANSFORM (testdata.c1, testdata.c2) USING "perl -e 'WHILE($input = <STDIN>){pri nt $input;}'" FROM testdata;
```

**Note**

PHP and Ruby are not deployed in MaxCompute compute clusters. Therefore, you cannot call PHP or Ruby scripts in MaxCompute.

###### Call scripts in series

This topic describes how to use SELECT TRANSFORM to call scripts in series and provides examples. SELECT TRANSFORM allows you to call scripts in series. For example, you can use DISTRIBUTE BY and SORT BY to pre-process data.

```
SELECT TRANSFORM(key, value) USING 'cmd2' FROM
```

`(`

```
    SELECT TRANSFORM(*) USINg 'cmd1' FROM
```

`(`

```
        SELECt * FROM data DISTRIBUTE BY col2 SORT BY col1
    ) t DISTRIBUTE BY key SORT BY value
) t2;
```

You can also use the MAP or REDUCE keyword to obtain the same results.

```
@a := select * from data distribute by col2 sort by col1; @b := map * using 'cmd1' distribute by col1 sort by col2 from @a; reduce * using 'cmd2' from @b;
```

###### Performance

This topic describes the advantages of SELECT TRANSFORM and user-defined table-valued functions (UDTFs). The performance of SELECT TRANSFORM and UDTFs varies based on specific scenarios. In most cases, SELECT TRANSFORM performs better. However, UDTFs perform better as the data amount increases. SELECT TRANSFORM is more suitable for ad hoc data analytics because the development of SELECT TRANSFORM is easier. The following sections describe the advantages of UDTFs and SELECT TRANSFORM.

**Advantages of UDTFs**

For UDTFs, the input parameters and output results support multiple data types. For SELECT TRANSFORM, the child process transfers data based on the standard input and output and processes all data as the STRING type. Therefore, SELECT TRANSFORM requires one more step of data type conversions than UDTFs. For SELECT TRANSFORM, data transfer depends on the operating system pipe. The pipe has only a 4 KB cache that cannot be specified. If the operating system pipe is empty or fully occupied, SELECT TRANSFORM cannot respond. For UDTFs, the constant parameters do not need to be transferred. However, SELECT TRANSFORM does not support this feature.

**Advantages of SELECT TRANSFORM**

SELECT TRANSFORM supports two processes: parent and child processes. UDTFs support only a single process. If the usage of computing resources is high and the data throughput is low, SELECT TRANSFORM can take advantage of the multi-core feature of the server. SELECT TRANSFORM calls underlying systems to read and write data during data transfer. This allows SELECT TRANSFORM to provide better performance in data transfer than Java programs. SELECT TRANSFORM supports the native code of tools such as AWK. This allows SELECT TRANSFORM to deliver more performance benefits than Java programs.

##### GROUPING SETS

###### Overview

This topic describes GROUPING SETS in MaxCompute. In some cases, you must execute the UNION ALL clause multiple times to aggregate and analyze data from multiple dimensions. For example, you want to aggregate Column A, aggregate Column B, and then aggregate Column A and Column B. The GROUPING SETS clause is a better choice in these cases. GROUPING SETS is an extension to the GROUP BY clause in a SELECT statement. GROUPING SETS allows you to group results by using various methods without the need to execute multiple SELECT statements. This allows the MaxCompute engine to generate more efficient execution plans with high performance.

**Note**

Most examples in this topic are demonstrated by using MaxCompute Studio. We recommend that you install MaxCompute Studio before you proceed with subsequent operations. For more information, see MaxCompute Studio.

###### Example

This topic provides an example on how to execute the GROUPING SETS statement. Example:
1. Prepare data.

```
create table requests LIFECYCLE 20 as select * from values
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city);
```

2. Execute the GROUPING SETS statement.

```
SELECT os,device, city ,COUNT(*) FROM requests GROUP BY os, device, city GROUPING SETS((os, device), (city), ());
```

The following result is returned:

```
+----+--------+------+------------+
| os | device | city | cnt        |
+----+--------+------+------------+
| NULL | NULL   | NULL | 7          |
| NULL | NULL   | Beijing | 4          |
| NULL | NULL   | Shijiazhuang | 3          |
| ios | Phone  | NULL | 1          |
| linux | PC     | NULL | 1          |
| linux | Phone  | NULL | 1          |
| windows | PC     | NULL | 3          |
| windows | Phone  | NULL | 1          |
+----+--------+------+------------+
```

You can also execute multiple SELECT statements to obtain the same result.

```
SELECT NULL, NULL, NULL, COUNT(*) FROM requests UNION ALL SELECT os, device, NULL, COUNT(*) FROM requests GROUP BY os, device UNION ALL SELECT null, null, city, COUNT(*) FROM requests GROUP BY city;
```

However, the execution of GROUPING SETS is simpler and more efficient.

**Note**

NULL is used as placeholders for the expressions that are not used in GROUPING SETS. This way, you can perform UNION operations on the result sets.

###### CUBE and ROLLUP

This topic describes the CUBE and ROLLUP functions for GROUPING SETS. CUBE and ROLLUP are special GROUPING SETS functions. CUBE lists all the possible combinations of specific columns as grouping sets. ROLLUP aggregates data by level to generate grouping sets. Examples:

```
GROUP BY CUBE(a, b, c) -- Equivalent to the following statement: GROUPING SETS((a,b,c),(a,b),(a,c),(b,c),(a),(b),(c),()) GROUP BY ROLLUP(a, b, c) -- Equivalent to the following statement: GROUPING SETS((a,b,c),(a,b),(a), ()) GROUP BY CUBE ( (a, b), (c, d) ) -- Equivalent to the following statement: GROUPING SETS (
    ( a, b, c, d ),
    ( a, b       ),
    (       c, d ),
    (            )
```

`)`

```
GROUP BY ROLLUP ( a, (b, c), d ) -- Equivalent to the following statement: GROUPING SETS (
    ( a, b, c, d ),
    ( a, b, c    ),
    ( a          ),
    (            )
```

`)`

```
GROUP BY a, CUBE (b, c), GROUPING SETS ((d), (e)) -- Equivalent to the following statement: GROUP BY GROUPING SETS (
    (a, b, c, d), (a, b, c, e),
    (a, b, d),    (a, b, e),
    (a, c, d),    (a, c, e),
    (a, d),       (a, e)
```

`)`

```
GROUP BY grouping sets((b), (c),rollup(a,b,c)) -- Equivalent to the following statement: GROUP BY GROUPING SETS (
    (b), (c),
    (a,b,c), (a,b), (a), ()
```

`)`

###### GROUPING and GROUPING_ID

This topic describes the GROUPING and GROUPING_ID functions in GROUPING SETS. NULL is used as placeholders in the results of GROUPING SETS. As a result, the NULL placeholders cannot be distinguished from the NULL values. To address this issue, MaxCompute provides the GROUPING function. GROUPING allows you to specify the name of a column as a parameter. If specific rows are aggregated based on the column specified in the GROUPING function, 0 is returned, which indicates that NULL is an input value. Otherwise, 1 is returned, which indicates that NULL is a placeholder in GROUPING SETS. GROUPING_ID allows you to specify the names of one or more columns as parameters. The GROUPING results of these columns are formed into integers by using bitmap. Examples:

```
SELECT a,b,c ,COUNT(*), GROUPING(a) ga, GROUPING(b) gb, GROUPING(c) gc, GROUPING_ID(a,b,c) groupingid FROM VALUES (1,2,3) as t(a,b,c) GROUP BY CUBE(a,b,c);
```

The following result is returned:

```
+------------+------------+------------+------------+------------+------------+---------- -+------------+
| a          | b          | c          | _c3        | ga         | gb         | gc
| groupingid |
+------------+------------+------------+------------+------------+------------+---------- -+------------+
| NULL       | NULL       | NULL       | 1          | 1          | 1          | 1
| 7          |
| NULL       | NULL       | 3          | 1          | 1          | 1          | 0
| 6          |
| NULL       | 2          | NULL       | 1          | 1          | 0          | 1
| 5          |
| NULL       | 2          | 3          | 1          | 1          | 0          | 0
| 4          |
| 1          | NULL       | NULL       | 1          | 0          | 1          | 1
| 3          |
| 1          | NULL       | 3          | 1          | 0          | 1          | 0
| 2          |
| 1          | 2          | NULL       | 1          | 0          | 0          | 1
| 1          |
| 1          | 2          | 3          | 1          | 0          | 0          | 0
| 0          |
+------------+------------+------------+------------+------------+------------+---------- -+------------+
```

By default, the columns that are not used in the GROUP BY clause are filled with NULL. You can use the GROUPING function to obtain more useful data.

```
-- Prepare table data. create table requests lifecycle 20 as select * from values
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city); -- Sample code select
  if(grouping(os) == 0, os, 'ALL') as os,
  if(grouping(device) == 0, device, 'ALL') as device,
  if(grouping(city) == 0, city, 'ALL') as city,
  count(*) as count
from requests group by os, device, city grouping sets((os, device), (city), ());
```

The following result is returned:

```
+------------+------------+------------+------------+
| os         | device     | city       | count      |
+------------+------------+------------+------------+
| ALL        | ALL        | ALL        | 7          |
| ALL        | ALL        | Beijing    | 4          |
| ALL        | ALL        | Shijiazhuang | 3          |
| ios        | Phone      | ALL        | 1          |
| linux      | PC         | ALL        | 1          |
| linux      | Phone      | ALL        | 1          |
| windows    | PC         | ALL        | 3          |
| windows    | Phone      | ALL        | 1          |
+------------+------------+------------+------------+
```

##### UNION, INTERSECT, and EXCEPT

This topic describes the SQL statements that use the UNION, INTERSECT, and EXCEPT set operators, such as UNION, UNION ALL, UNION DISTINCT, INTERSECT, INTERSECT ALL, INTERSECT DISTINCT, EXCEPT, EXCEPT ALL, and EXCEPT DISTINCT. Syntax:

```
select_statement UNION ALL select_statement; select_statement UNION [DISTINCT] select_statement; select_statement INTERSECT ALL select_statement; select_statement INTERSECT [DISTINCT] select_statement; select_statement EXCEPT ALL select_statement; select_statement EXCEPT [DISTINCT] select_statement; select_statement MINUS ALL select_statement; select_statement MINUS [DISTINCT] select_statement;
```

Parameters: UNION: the union of two datasets. The UNION operation combines two datasets into one dataset. INTERSECT: the intersection of two datasets. The INTERSECT operation returns the records contained in both datasets. EXCEPT: the complement of the second dataset in the first dataset. The EXCEPT operation returns the records that are contained in the first dataset, but not in the second dataset. MINUS: equivalent to EXCEPT. Examples: UNION: If UNION ALL is used, all records of the two datasets are returned.

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4) t(a, b) UNION ALL SELECT * FROM VALUES (1, 2), (1, 4) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

If multiple UNION ALL clauses are used, parentheses can be used to prioritize the clauses.

```
SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3);
```

If UNION is used, duplicate records are not included in the returned records. UNION is equivalent to UNION DISTINCT.

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4) t(a, b) UNION SELECT * FROM VALUES (1, 2), (1, 4) t(a, b); -- The preceding statement is equivalent to the following statement: SELECT DISTINCT * FROM (<Result of UNION ALL>)t;
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 3          | 4          |
+------------+------------+
```

Assume that UNION is followed by a CLUSTER BY, DISTRIBUTE BY, SORT BY, ORDER BY, or LIMIT clause. If set odps.sql.type.system.odps2=false; is used, the clause works on the result of the last **select_statement** after the UNION operator. If odps.sql.type.system.odps2=true; is used, the clause works on the result of all the UNION operations.

```
set odps.sql.type.system.odps2=true; SELECT explode(array(3, 1)) AS (a) UNION ALL SELECT explode(array(0, 4, 2)) AS (a) OR DER BY a LIMIT 3;
```

The following result is returned:

```
+------+
| a    |
+------+
| 0    |
| 1    |
| 2    |
+------+
```

INTERSECT: INTERSECT ALL:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 6) t(a, b) INTERSECT ALL SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

INTERSECT DISTINCT:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 6) t(a, b) INTERSECT DISTINCT SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

The following result is returned. The preceding statement is equivalent to the `SELECT`

| DISTINCT * FROM (< Result of INTERSECT ALL >) t; statement. |   |   |
|---|---|---|
|   | +------------+------------+ \| a \| b \| +------------+------------+ \| 1 \| 2 \| \| 3 \| 4 \| +------------+------------+ |   |

EXCEPT: EXCEPT ALL:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (3, 4), (5, 6), (7, 8) t(a, b) EXCEPT ALL SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
| 7          | 8          |
+------------+------------+
```

EXCEPT DISTINCT:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (3, 4), (5, 6), (7, 8) t(a, b) EXCEPT SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b);
```

| The following result is returned. The preceding statement is equivalent to the |   |
|---|---|
| DISTINCT * FROM left branch EXCEPT ALL SELECT DISTINCT * FROM right branch; _ _ |   |

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 7          | 8          |
+------------+------------+
```

**Note**

Set operations do not necessarily return sorted results. The two branches for a set operation must have the same number of output columns with consistent data types. If data types are inconsistent, implicit conversion of the data types may be performed. To ensure compatibility for set operations, MaxCompute forbids the implicit conversion between STRING and other data types. MaxCompute supports a maximum of 256 branches for a set operation. If the limit is exceeded, an error is returned.

#### EXPLAIN

This topic describes the EXPLAIN statement in MaxCompute SQL. This statement shows the structure of the execution plan of a DML statement. An execution plan is a program that executes SQL statements. Syntax:

```
EXPLAIN <DML query>;
```

**Note**

The execution results of an EXPLAIN statement include: Dependencies among all the jobs of this DML statement Dependencies among all the tasks of each job Dependencies among all operators in a task Examples:

```
EXPLAIN SELECT abs(a.key), b.value FROM src a JOIN src1 b ON a.value = b.value;
```

The output of the EXPLAIN statement consists of the following three parts: Job dependencies: `job0 is root job` . This query requires only one **job (job0)**. Therefore, only one row of information is displayed. Task dependencies. Example:

```
In Job job0: root Tasks: M1_Stg1, M2_Stg1 J3_1_2_Stg1 depends on: M1_Stg1, M2_Stg1
```

**Note**

Job0 contains three tasks, M1_Stg1, M2_Stg1, and J3_1_2_Stg1. J3_1_2_Stg1 is executed after the M1_Stg1 and M2_Stg1 tasks are complete. Naming conventions for a task: MaxCompute provides the task types of map, reduce, join, and local work. The first letter in a task name indicates the type of the task. For example, M2Stg1 is a map task. The number following the first letter indicates the task ID. This ID is unique among all tasks that correspond to the current query. Digits that are combined by underscores (_) indicate the task dependencies. For example, J3_1_2_Stg1 indicates that the current task with the ID of 3 depends on two tasks whose IDs are 1 and 2. Operator structure, where each operator string describes the execution semantics of a task.

```
In Task M1_Stg1:
  Data source: yudi_2.src                       # Data source describes the input of t
he task.
  TS: alias: a                                  # TableScanOperator
      RS: order: +                              # ReduceSinkOperator
          keys:
               a.value
          values:
               a.key
          partitions:
               a.value
In Task J3_1_2_Stg1:
  JOIN: a INNER JOIN b                          # JoinOperator
      SEL: Abs(UDFToDouble(a._col0)), b._col5   # SelectOperator
          FS: output: None                      # FileSinkOperator
In Task M2_Stg1:
  Data source: yudi_2.src1
  TS: alias: b
      RS: order: +
          keys:
               b.value
          values:
               b.value
          partitions:
               b.value
```

The following table describes the operators.

| Operator | Description |
|---|---|
| TableScanOperator | Describes the logic of FROM statement blocks in a query statement. The alias of the input table is displayed in the EXPLAIN results. |
| SelectOperator | Describes the logic of SELECT statement blocks in a query statement. The columns that are transferred to the next operator are displayed in the EXPLAIN results. Separate multiple columns with commas (,). If columns are referenced, the value is in the < alias >.< column name > format. _ If the result of an expression is transferred, the value is displayed as a function, such as func1(arg1 1, arg1 2, _ _ func2(arg2 1, arg2 2)). _ _ If constants are transferred, the value is immediately displayed. |
| FilterOperator | Describes the logic of WHERE statement blocks in a query statement. The EXPLAIN results include a WHERE clause, with the display rules that are similar to those of SelectOperator. |
| JoinOperator | Describes the logic of JOIN statement blocks in a query statement. The EXPLAIN results show which tables are joined in which way. |
| GroupByOperator | Describes the logic of aggregate operations. This operator is displayed if an aggregate function is used in a query. The content of the aggregate function is displayed in the EXPLAIN results. |
| ReduceSinkOperator | Describes the logic of data distribution between tasks. If the result of the current task is transferred to another task, ReduceSinkOperator must be used to distribute data at the last stage of the current task. The sorting method of output data records, the distributed keys and values, and the columns used to calculate the hash value are displayed in the EXPLAIN results. |
| FileSinkOperator | Describes the logic of storage operations on final data records. If an INSERT statement block exists in a query, the name of the required table is displayed in the EXPLAIN results. |
| LimitOperator | Describes the logic of LIMIT statement blocks in a query statement. The number of records specified by LIMIT is displayed in the EXPLAIN results. |
| MapjoinOperator | Describes JOIN operations on large tables. This operator is similar to JoinOperator. |

**Note**

If a query statement is complex, the EXPLAIN statement returns excessive results. As a result, API limits are reached and complete results cannot be obtained. In this case, you can split a query and execute the EXPLAIN statement on each subquery to understand the structure of the job. If you specify more than 10,000 partitions in a query, large amounts of source data needs to be read. To circumvent this limit, you can add filter conditions in the query to filter out most partitions.

#### IF statement

This topic describes the IF statement that MaxCompute SQL supports. MaxCompute SQL supports the IF-ELSE statement. You can use the IF-ELSE statement to execute SQL scripts with specific conditions. A condition in the IF-ELSE statement can be a standard variable or a scalar subquery that returns only one column value from one row. The IF statement allows the system to automatically select the execution logic based on the specified conditions. MaxCompute supports the following IF syntax:

```
IF (condition) BEGIN
  statement 1
  statement 2
  ...
END IF (condition) BEGIN
  statements
END ELSE IF (condition2) BEGIN
  statements
END ELSE BEGIN
  statements
END
```

**Note**

The BEGIN and END conditional clause can be omitted if it contains only one statement, similar to '{ }' in Java. The IF statement can contain two types of conditions: expressions and scalar subqueries. Both of them are of the BOOLEAN type. Expressions: A BOOLEAN-type expression in the IF-ELSE statement determines which branch is executed at the compiling stage. Example:

```
@date := '20190101'; @row TABLE(id STRING); -- Declare the row variable. The type of the row is Table and schema is STRING. IF ( cast(@date as bigint) % 2 == 0 ) BEGIN @row := SELECT id from src1; END ELSE BEGIN @row := SELECT id from src2; END INSERT OVERWRITE TABLE dest SELECT * FROM @row;
```

Scalar subqueries: A BOOLEAN-type scalar subquery in the IF-ELSE statement determines which branch is executed at the running stage. Therefore, you must submit multiple jobs. Example:

```
@i bigint; @t table(id bigint, value bigint); IF ((SELECT count(*) FROM src WHERE a = '5') > 1) BEGIN @i := 1; @t := select @i, @i*2; END ELSE BEGIN @i := 2; @t := select @i, @i*2; END select id, value from @t;
```

#### UPDATE and DELETE

This topic describes the UPDATE and DELETE statements in MaxCompute SQL. The UPDATE and DELETE statements are used to manage data of specific rows in tables or partitions.

**Background information**

MaxCompute data manipulation language (DML) statements have limits on table operations. MaxCompute allows you to use only the INSERT OVERWRITE and INSERT INTO statements to delete and update some rows in a table. For example, if you use an INSERT statement to modify small amounts of data in a table or partition, you must use a SELECT statement to read all data and modify the data. Then, you can execute the INSERT statement to insert the modified data into the table or partition. This is a low-efficiency process. However, if you use the UPDATE and DELETE statements, the amount of data read or written in a query significantly decreases. History tables were considered the best to perform multiple UPDATE operations at a time. If you use a history table, you must add auxiliary columns, such as **start_date** and **end_date**, in the table. These columns indicate the lifecycle of the data records in a row. To query the current status of a table, you must find the latest status from large amounts of data based on the timestamp. This is a time-consuming process. However, the UPDATE and DELETE statements directly read data from the current table. When you execute a DELETE statement, the system automatically generates a Delta file.
**txnid(bigint)** and **rowid(bigint)** in the Delta file indicate which rows in which transactional
table are deleted from the Base file.

**Note**

The Delta file stores the row numbers that are used to indicate the deleted rows in the Base file. If you execute a DELETE statement again, another Delta file named f2.del is generated. The f2.del file also stores the row numbers based on the Base file. During data reading, all Delta files are queried and data that is not deleted is returned. Similarly, the UPDATE statement is converted into the combination of the DELETE and INSERT INTO statements. If jobs are run in parallel and the tables on which you want to perform operations are the same, conflicts may occur. For more information, see ACID semantics of MaxCompute concurrent write jobs.

**Precautions**

The UPDATE and DELETE operations must be performed based on transactional tables. For more information about how to create a transactional table, see Create a table. When you execute an UPDATE statement, you must add set odps.service.mode=off; before the statement and commit them at the same time. If the ratio of the rows that you want to delete or update to all rows is small, the performance of the data that is read from a table is slightly affected. In this case, we recommend that you use the UPDATE or DELETE statement. If the ratio is less than 5%, we recommend that you use the UPDATE or DELETE statement. The maximum ratio varies based on your business scenarios. If you perform the UPDATE or DELETE operation multiple times to update or delete a small number of rows in a table, we recommend that you execute the COMPACT statement after the UPDATE and DELETE statements. This reduces the storage usage of the table. If you perform less UPDATE or DELETE operations to update or delete a large number of rows in a table and will frequently read data from the table, we recommend that you use the INSERT OVERWRITE and INSERT INTO statements. For example, a total of 10% of the data in a table needs to be updated or deleted ten times a day. In this case, we recommend that you evaluate the sum of the costs of the UPDATE or DELETE statement and the read performance consumption based on the generated Delta file. Then, compare it with that of the INSERT OVERWRITE and INSERT INTO statements to select an efficient method. After you delete data, a Delta file is generated. As a result, the storage resources may not be released. If you want to use the DELETE statement to delete data and release the storage resources, you can use the ALTER TABLE COMPACT statement to merge the Base files with Delta files.

**Limits**

If you use the ALTER TABLE COMPACT statement in MaxCompute SQL mode of DataWorks, a compatibility issue occurs. To handle this issue, we recommend that you use the MaxCompute client whose version must be 0.35.0. You can specify the transactional attribute for a table only when you create the table. However, you are not allowed to modify the transactional attribute of an existing table by using the ALTER TABLE COMPACT statement. If you modify the transactional attribute of an existing table, an error is returned.

```
alter table not_txn_tbl set tblproperties("transactional"="true"); -- FAILED is returned. Catalog Service Failed, Error Code: 151, Error Message: Set tr ansactional is not supported.
```

You cannot specify clustered tables or external tables as transactional tables. Existing internal tables or external tables cannot be converted into transactional tables, and transactional tables cannot be converted into standard tables. Tasks from peripheral systems, such as Graph and Machine Learning Platform for AI (PAI), are not supported. If these tasks access a transactional table, an error is returned. CLONE TABLE, MERGE PARTITION, and incremental replication operations cannot be performed on transactional tables. Before you perform the UPDATE, DELETE, or INSERT OVERWRITE operation on data in transactional tables, make sure that you back up the data in advance. You must have the Select and Update permissions on a table to perform the UPDATE and DELETE operations.

**DELETE**

Syntax:

```
delete from <table_name> [WHERE where_condition];
```

Description: This statement is used to delete some rows from a table. The following examples are provided: Example 1: Delete some rows from a table.

```
-- Create a transactional table. create table if not exists acid_delete(id bigint) tblproperties ("transactional"="true"); -- Insert data into the table. insert overwrite table acid_delete values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_delete;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+ -- Delete the row whose id value is 2. You must enter Yes or No to confirm the operatio n in the MaxCompute client. delete from acid_delete where id = 2; -- Read data from the table. Only the rows whose id values are 1 and 3 are retained in the table. select * from acid_delete;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 3          |
+------------+
```

Example 2: Delete some rows from a partitioned table.

```
-- Create a transactional table. create table if not exists acid_delete_pt(id bigint) partitioned by(ds string) tblprope rties ("transactional"="true"); -- Add partitions to the table. alter table acid_delete_pt add if not exists partition (ds= '2019'); -- Insert data into the partitions. insert overwrite table acid_delete_pt partition (ds='2019') values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_delete_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+ -- Delete data from the partitions. You must enter Yes or No to confirm the operation i n the MaxCompute client. delete from acid_delete_pt where ds='2019' and id= 2; -- Read data from the table. Only the rows whose id values are 1 and 3 are retained in the table. select * from acid_delete_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

**UPDATE**

Syntax:

```
update <table_name> set col1 = value1 [, col2 = value2 ...] [WHERE where_condition]; update <table_name> set (col1 [, col2 ...]) = (value1 [, value2 ...]);
```

Description: This statement is used to update some rows in a table.

**Note**

The UPDATE statement is converted into the combination of the DELETE and INSERT INTO statements to update some rows. The following examples are provided: Example 1: Update some rows in a table.

```
-- Create a transactional table. create table if not exists acid_update(id bigint) tblproperties ("transactional"="true"); -- Insert data into the table. insert overwrite table acid_update values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_update;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+ -- Update the value 2 in the id column to 4. set odps.service.mode=off; update acid_update set id = 4 where id = 2; -- Query the table to check whether the value 2 is updated to 4 in the id column. select * from acid_update;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 4          |
| 1          |
| 3          |
+------------+
```

Example 2: Update some rows in a partitioned table.

```
-- Create a transactional table. create table if not exists acid_update_pt(id bigint) partitioned by(ds string) tblprope rties ("transactional"="true");-- Add a partition. -- Add partitions to the table. alter table acid_update_pt add if not exists partition (ds= '2019'); -- Insert data into the partitions. insert overwrite table acid_update_pt partition (ds='2019') values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_update_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+
```

```
-- Update the id values of rows in partition 2019 to 4. The rows must have the id value s of 2. set odps.service.mode=off; update acid_update_pt set id = 4 where ds = '2019' and id = 2; -- Query the table to check whether the value 2 is updated to 4 in the id column. select * from acid_update_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 4     | 2019   |
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

Example 3: Update several columns and update a destination table by using the data in a source table.

```
-- Create a destination table named acid_update_t and create a table named acid_update_s for joins. create table if not exists acid_update_t(id bigint,value1 bigint,value2 bigint) tblprop erties ("transactional"="true"); create table if not exists acid_update_s(id bigint,value1 bigint,value2 bigint); -- Insert data into these tables. insert overwrite table acid_update_t values(2,20,21),(3,30,31),(4,40,41); insert overwrite table acid_update_s values(1,100,101),(2,200,201),(3,300,301); -- Use constants to update the acid_update_t table. set odps.service.mode=off; update acid_update_t set (value1, value2) = (3, 4); -- Use the data in the acid_update_s table to update the acid_update_t table. Left join the acid_update_t table with the acid_update_s table. If you want to update only the in tersection of the two tables, you must add a WHERE clause to the update <table_name> st atement. set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s w here acid_update_t.id = acid_update_s.id); -- Use the data in the acid_update_s table to update the acid_update_t table. Add filte r conditions for the acid_update_t table to update only the intersection of the two tab les. set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s w here acid_update_t.id = acid_update_s.id) where acid_update_t.id in (select id from aci d_update_s); -- Use the aggregate results of the acid_update_t and acid_update_s tables to update th e acid_update_t table. set odps.service.mode=off; update acid_update_t set (id, value1, value2) = (select id, max(value1),max(value2) fro m acid_update_s where acid_update_t.id = acid_update_s.id group by acid_update_s.id) wh ere acid_update_t.id in (select id from acid_update_s);
```

**MERGE INTO**

The MERGE INTO statement encapsulates the INSERT, UPDATE, and DELETE operations. You can use this statement to perform multiple operations on a destination table after the table is joined with a source table. MaxCompute DML provides the UPDATE and DELETE statements to enrich its expressions. However, if you want to use several INSERT, UPDATE, and DELETE statements to perform multiple UPDATE operations on a destination table at a time, you must execute several statements. These statements trigger multiple full table scans. The MERGE INTO statement requires only one full table scan for you to complete the operations. The MERGE INTO statement is more efficient than the INSERT, UPDATE, and DELETE statements. If you use the INSERT, UPDATE, and DELETE statements in a job to update a table, the update succeeds only when all the statements are successfully executed. If only some of these statements are successfully executed, the execution cannot be rolled back. However, the MERGE INTO statement is atomic, which can be used to prevent this issue. Syntax:

```
MERGE INTO <target table> AS T USING <source expression/table> AS S ON <boolean expression1> WHEN MATCHED [AND <boolean expression2>] THEN UPDATE SET <set clause list> WHEN MATCHED [AND <boolean expression3>] THEN DELETE WHEN NOT MATCHED [AND <boolean expression4>] THEN INSERT VALUES <value list>
```

Description: This statement is used to update or insert data from the **source expression or**
**table** into the **destination table**. This statement is also used to delete data from the source
expression or table from the destination table. Parameters:
**source expression/table**: the source table. The value of this parameter can be a table,
view, or subquery.
**target table**: the destination table, which must be an existing physical table.
**ON**: the clause that is used to determine whether the source table is joined with the
destination table. **boolean expression** specifies the join condition.
**WHEN MATCHED…THEN**: specifies the action when the **ON** clause determines that the
two tables are joined. Data obtained from multiple **WHEN MATCHED [AND <boolean**
**expression>]** clauses must have no intersections. The MERGE INTO statement has clear
objectives. You are not allowed to perform the INSERT or UPDATE operation on the same row in a single MERGE INTO statement. When you execute the MERGE INTO statement, make sure that the data in the source tables that meet the ON joint condition is unique. Otherwise, an error is returned.

**Note**

If a MERGE INTO statement has three WHEN clauses, the UPDATE, DELETE, and INSERT operations can appear at most once in each clause.
**WHEN NOT MATCHED** must be the last WHEN clause and can be used only for
an INSERT operation. If both the UPDATE and DELETE statements are included in a MERGE INTO statement, the statement that appears first must include **[AND <boolean**
**expression>]**.
The following example is provided: Prepare the test data.

```
-- Create a destination table. create table if not exists acid_address_book_base1 (id bigint,first_name string,last_name string,phone string) partitioned by(year string, month string, day string, hour string) tblproperties ("transactional"="true"); -- Create a source table. create table if not exists tmp_table1 (id bigint, first_name string, last_name string, phone string, _event_type_ string); -- Insert the test data into the destination table. insert overwrite table acid_address_book_base1 partition(year='2020', month='08', day='20', hour='16') values (4, 'nihaho', 'li', '222'), (5, 'tahao', 'ha', '333'), (7, 'djh', 'hahh', '555'); -- Insert the test data into the source table. insert overwrite table tmp_table1 values (1, 'hh', 'liu', '999', 'I'), (2, 'cc', 'zhang', '888', 'I'), (3, 'cy', 'zhang', '666', 'I'),(4, 'hh', 'liu', '999', 'U'), (5, 'cc', 'zhang', '888', 'U'),(6, 'cy', 'zhang', '666', 'U');
```

If data meets the ON joint condition and is from the source table, you can use the data to perform the MERGE INTO operation on the destination table. If data does not meet the ON joint condition but is of the **I** type specified by **event_type** in the source table, you can insert the data into the destination table.

```
merge into acid_address_book_base1 as t using tmp_table1 as s on s.id = t.id and t.year='2020' and t.month='08' and t.day='20' and t.hour='16' when matched then update set t.first_name = s.first_name, t.last_name = s.last_name, t.phone = s.pho
```

`ne`

```
when not matched and (s._event_type_='I') then insert values(s.id, s.first_name, s.last_name,s.phone,'2020','08','20','16'); -- Query the destination table after the preceding operations are complete. select * from acid_address_book_base1;
```

The following result is returned:

```
+------------+------------+-----------+-------+------+-------+-----+------+
| id         | first_name | last_name | phone | year | month | day | hour |
+------------+------------+-----------+-------+------+-------+-----+------+
| 4          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 5          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 7          | djh        | hahh      | 555   | 2020 | 08    | 20  | 16   |
| 1          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 2          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 3          | cy         | zhang     | 666   | 2020 | 08    | 20  | 16   |
+------------+------------+-----------+-------+------+-------+-----+------+
```

**ALTER TABLE COMPACT**

If you perform DELETE operations on a transactional table, the Base file that you want to delete is not modified. A Delta file is generated every time you perform a DELETE operation. As a result, if you perform multiple DELETE operations, the generated Delta files occupy more storage resources. If you perform several DELETE operations on the same table or partition, a large number of Delta files may be generated based on the amount of the data that you delete. Similarly, if you perform an UPDATE operation which is converted into the combination of the DELETE and INSERT INTO operations, Delta files are also generated. If the system reads data from the table, it must load the generated Delta files to find the deleted rows. A large number of Delta files reduce data reading efficiency. In this case, you can use the ALTER TABLE COMPACT statement to merge the Base files with Delta files to reduce storage usage and improve data reading efficiency. Syntax:

```
alter table <table_name> [partition (partition_key = 'partition_value' [, ...])] compac t [major|minor];
```

Description: This statement is used to merge the Base files with Delta files to reduce storage usage and improve data reading efficiency.
**Minor compaction**: merges all Delta files with their Base files. The Delta files must be
generated based on the same Base file. Delta files that are generated based on different Base files cannot be merged.
**Major compaction**: merges all Delta files generated based on the same Base file with the
Base file, deletes the Delta files, and merges small files in multiple Base files that correspond to tables. If the size of the Base file is less than 32 MB or a Delta file is generated, the INSERT OVERWRITE operation is performed on the table. However, if the size of the Base file is greater than or equal to 32 MB or no Delta files are generated, the INSERT OVERWRITE operation is not performed on the table. Sample statements:

```
alter table acid_delete compact minor; alter table acid_update_pt partition (ds = '2019') compact major;
```

The following result is returned:

```
Summary: table name: acid_update_pt /ds=2019 instance count: 2 run time: 16
  before merge, file count:        8  file size: 2423  file physical size: 7269
   after merge, file count:        2  file size: 642  file physical size: 1926
```

### Built-in functions

#### Mathematical functions

##### ABS

This topic describes how to use the ABS mathematical function in MaxCompute. This function calculates the absolute value.

```
DOUBLE ABS(DOUBLE number); BIGINT ABS(BIGINT number) ; DECIMAL ABS(DECIMAL number);
```

number: This parameter supports the BIGINT, DOUBLE, or DECIMAL type. The return type is the same as the input type. If the input is of the STRING type, the system implicitly converts it to the DOUBLE type before the calculation. If the input is of any other type, the system returns an error. The type of the return value depends on the input parameter type and can be DOUBLE, BIGINT, or DECIMAL. If the input parameter is NULL, the function returns NULL.

**Note**

If the input BIGINT value exceeds the maximum representation range of the BIGINT type, the function returns a DOUBLE value, which may cause a loss of precision.

```
SELECT ABS(null); -- Result +-------+
|  _c0  |
+-------+
|  NULL |
+-------+ SELECT ABS(-1); -- Result +-------+
|  _c0  |
+-------+
|    1  |
+-------+ SELECT ABS(-1.2); -- Result +-------+
|  _c0  |
+-------+
|  1.2 |
+-------+ SELECT ABS("-2"); -- Result +-------+
|  _c0  |
+-------+
|  2.0  |
+-------+ SELECT ABS(122320837456298376592387456923748); -- Result +------------------------+
|           _c0          |
+------------------------+
|  1.2232083745629837e32 |
+------------------------+
```

The following example shows how to use the ABS function in SQL. Other built-in functions, except window functions and aggregate functions, follow a similar usage pattern.

```
CREATE TABLE IF NOT EXISTS tbl1 (
    id BIGINT COMMENT 'Test ID'
) COMMENT 'ABS function test table'; INSERT INTO tbl1 VALUES (10), (-25), (0), (NULL); SELECT ABS(id) FROM tbl1; -- Calculate the absolute value of the id field in the tbl1 table.
```

##### ACOS

This topic describes how to use the ACOS mathematical function in MaxCompute. This function calculates the arc cosine of a specified **number**.

```
DOUBLE ACOS(DOUBLE number); DECIMAL ACOS(DECIMAL number);
```

**number**: The DOUBLE or DECIMAL type. The value range is [-1, 1]. If the input value is of
the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input is of any other type, the system returns an error. The return value is of the DOUBLE or DECIMAL type, and the value range is [0, π]. If the input value is NULL, the function returns NULL.

```
SELECT ACOS("0.87"); -- Result +---------------------+
|          _c0        |
+---------------------+
|  0.5155940062460905 |
+---------------------+ SELECT ACOS(0); -- Result +---------------------+
|         _c0         |
+---------------------+
|  1.5707963267948966 |
+---------------------+
```

##### ASIN

This topic describes how to use the ASIN mathematical function in MaxCompute to calculate the arcsine of an input value. This function calculates the arcsine of a specified `number` and returns the result in radians.

```
DOUBLE ASIN(DOUBLE number); DECIMAL ASIN(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type and fall within the range of [-1, 1]. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. The function returns a value of the DOUBLE or DECIMAL type. The return value falls within the range of -π/2 to π/2. If the input value is NULL, the function returns NULL.

```
SELECT ASIN(1); -- Result +----------------------+
|          _c0         |
+----------------------+
|  1.5707963267948966  |
+----------------------+ SELECT ASIN(-1); -- Result +----------------------+
|         _c0          |
+----------------------+
|  -1.5707963267948966 |
+----------------------+
```

##### ATAN

This topic describes how to use the ATAN mathematical function in MaxCompute to calculate the arc tangent of an input value. This function calculates the arc tangent of a specified number and returns the result in radians.

```
DOUBLE ATAN(DOUBLE number);
```

number: required. The DOUBLE type. If the input value is of the STRING or BIGINT type, the function implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the function returns an error. The function returns a value of the DOUBLE type in the range of -π/2 to π/2. If the input value is NULL, the function returns NULL.

```
SELECT ATAN(1); -- Return result +----------------------+
|          _c0         |
+----------------------+
|  0.7853981633974483  |
+----------------------+ SELECT ATAN(-1); -- Return result +----------------------+
|         _c0          |
+----------------------+
|  -0.7853981633974483 |
+----------------------+
```

##### CEIL

This topic describes how to use the CEIL mathematical function in MaxCompute to round up an input value. This function rounds up an input value and returns the smallest integer that is greater than or equal to the input value.

```
BIGINT CEIL(DOUBLE value); BIGINT CEIL(DECIMAL value);
```

value: Required. The data type is DOUBLE or DECIMAL. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. This function returns a value of the BIGINT type. If the input value is NULL, the function returns NULL.

```
SELECT CEIL(1.1); -- Result +-------+
|  _c0  |
+-------+
|   2   |
+-------+ SELECT CEIL(-1.1); -- Result +-------+
|  _c0  |
+-------+
|  -1   |
+-------+
```

##### CONV

This topic describes how to use the CONV mathematical function in MaxCompute for base conversion. This function converts a numeric value from a specified base to another.

```
STRING CONV(STRING input, BIGINT from_base, BIGINT to_base);
```

input: required. This parameter must be of the STRING type. It specifies the integer value to be converted. This parameter supports implicit conversions from the BIGINT and DOUBLE types. from_base: required. This parameter must be of the BIGINT type. It specifies the original base. Valid values are 2, 8, 10, and 16. This parameter supports implicit conversions from the STRING and DOUBLE types. to_base: required. This parameter must be of the BIGINT type. It specifies the target base. Valid values are 2, 8, 10, and 16. This parameter supports implicit conversions from the STRING and DOUBLE types. This function returns a value of the STRING type. If any input value is NULL, the function returns NULL. If any input value is a negative value that starts with a hyphen (-), the system returns an error. If any input value is a decimal, the system converts the value to an integer before the base conversion and discards the decimal part.

```
SELECT CONV('1100', 2, 10); -- Result +------+
| _c0  |
+------+
|  12  |
+------+ SELECT CONV('1100', 2, 16); -- Result +------+
| _c0  |
+------+
|  C   |
+------+ SELECT CONV('ab', 16, 10); -- Result +------+
| _c0  |
+------+
| 171  |
+------+ SELECT CONV('ab', 16, 16); -- Result +------+
| _c0  |
+------+
|  AB  |
+------+
```

##### COS

This topic describes how to use the COS mathematical function in MaxCompute to calculate the cosine of an input radian value. This function calculates the cosine of number, which is a radian value.

```
DOUBLE COS(DOUBLE number); DECIMAL COS(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the DOUBLE or DECIMAL type. If the input parameter is NULL, the function returns NULL.

```
SELECT COS(3.1415926/2); -- Result +-------------------------+
|           _c0           |
+-------------------------+
|  2.6794896585028633e-8  |
+-------------------------+ SELECT COS(3.1415926); -- Result +----------------------+
|         _c0          |
+----------------------+
|  -0.9999999999999986 |
+----------------------+
```

##### COSH

This topic describes how to use the COSH mathematical function in MaxCompute to calculate the hyperbolic cosine of an input value. This function calculates the hyperbolic cosine of a number.

```
DOUBLE COSH(DOUBLE number); DECIMAL COSH(DECIMAL number);
```

number: required. The data type is DOUBLE or DECIMAL. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. The return value is of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT COSH(1); -- Result +----------------------+
|          _c0         |
+----------------------+
|  1.5430806348152437  |
+----------------------+ SELECT COSH(0); -- Result +------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### COT

This topic describes how to use the COT mathematical function in MaxCompute to calculate the cotangent of an input value in radians. This function calculates the cotangent of a number. The input value is in radians.

```
DOUBLE COT(DOUBLE number); DECIMAL COT(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT COT(0.7853981633974483); -- Output +--------------------+
| _c0                |
+--------------------+
| 1.0000000000000002 |
+--------------------+ SELECT COT(1); -- Output +---------------------+
| _c0                 |
+---------------------+
| 0.6420926159343308  |
+---------------------+
```

##### EXP

This topic describes how to use the EXP mathematical function in MaxCompute to calculate the power of the natural constant e. This function calculates the exponential value of a specified number.

```
DOUBLE EXP(DOUBLE number); DECIMAL EXP(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input data type is STRING or BIGINT, the system implicitly converts the value to the DOUBLE type before calculation. If the input is of any other type, the system reports an error. The function returns a value of the DOUBLE or DECIMAL type. The value indicates e raised to the power of number. If the input parameter is NULL, the function returns NULL.

```
SELECT EXP(1); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2.718281828459045   |
+---------------------+ SELECT EXP(0); -- Result +------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### FLOOR

This topic describes how to use the FLOOR mathematical function in MaxCompute to round down an input value. This function rounds down a number and returns the largest integer that is less than or equal to the number.

```
BIGINT FLOOR(DOUBLE number); BIGINT FLOOR(DECIMAL number);
```

number: required. The value is of the DOUBLE or DECIMAL type. If the input is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input is of any other type, an error occurs. The return value is of the BIGINT type. If the input value is NULL, the function returns NULL.

```
SELECT FLOOR(1.2); -- Return result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT FLOOR(1.9);
```

```
-- Return result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT FLOOR(0.1); -- Return result +------+
| _c0  |
+------+
| 0    |
+------+ SELECT FLOOR(-1.2); -- Return result +------+
| _c0  |
+------+
| -2   |
+------+ SELECT FLOOR(-0.1); -- Return result +------+
| _c0  |
+------+
| -1   |
+------+ SELECT FLOOR(0.0); -- Return result +------+
| _c0  |
+------+
| 0    |
+------+ SELECT FLOOR(-0.0); -- Return result +------+
| _c0  |
+------+
| 0    |
+------+
```

##### LN

This topic describes how to use the LN mathematical function in MaxCompute to calculate the natural logarithm of an input value. This function returns the natural logarithm of a number.

```
DOUBLE LN(DOUBLE number); DECIMAL LN(DECIMAL number);
```

number: required. The data type is DOUBLE or DECIMAL. If the input value is of the STRING or BIGINT type, the system implicitly converts the value into the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. The return value is of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL. If the input value is a negative number or 0, the system returns an error.

```
SELECT LN(1000); -- Result +--------------------+
| _c0                |
+--------------------+
| 6.907755278982137  |
+--------------------+
```

##### LOG

This topic describes the LOG mathematical function. Function syntax:

```
double log(double base, double x) decimal log(decimal base, decimal x)
```

Description: This function calculates the logarithm of **x** whose base number is **base**. Parameters:
**base**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT
type, it is implicitly converted into a value of the DOUBLE type before the calculation. If the input value is of another data type, an error is returned.
**x**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT
type, it is implicitly converted into a value of the DOUBLE type before the calculation. If the input value is of another data type, an error is returned. Return value: The logarithm value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned. If an input value is a negative value or 0, an error is returned. If the value of **base** is 1, an error is returned. The value 1 causes division by zero. Examples:

```
select log(10,100);
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 2.0        |
+------------+
```

##### POW

This topic describes how to use the POW mathematical function in MaxCompute to calculate x raised to the power of y. This function returns x raised to the power of y, which is xy.

```
DOUBLE POW(DOUBLE x, DOUBLE y); DECIMAL POW(DECIMAL x, DECIMAL y);
```

x: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, an error occurs. y: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, an error occurs. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT POW(10, 2); -- Return result +-------+
| _c0   |
+-------+
| 100.0 |
+-------+
```

##### RAND

This topic describes how to use the RAND mathematical function in MaxCompute to generate a random number with a specified seed. This function returns a random number of the DOUBLE type based on the specified seed, and the return value ranges from 0 to 1.

```
DOUBLE RAND(BIGINT seed);
```

seed: optional. The data type is BIGINT. This parameter specifies the random number seed and determines the starting value of the random number sequence. If you do not specify this parameter, the function returns a different random value each time it runs. The return value is of the DOUBLE type and ranges from 0 to 1. If you specify the same seed, the function returns the same random number sequence. If the input value is NULL, the function returns NULL.

```
-- Do not specify a seed. The function returns a different result each time it runs. SELECT RAND(); -- Return result (example; the actual value varies based on the execution time) +--------------------+
| _c0                |
+--------------------+
| 0.5432178901234567 |
+--------------------+ -- Specify a seed. The function returns the same result each time it runs. SELECT RAND(1); -- Return result +--------------------+
| _c0                |
+--------------------+
| 0.7308781907032909 |
+--------------------+
```

##### ROUND

This topic describes how to use the ROUND mathematical function in MaxCompute to round a number to a specified number of decimal places. This function rounds a number to a specified number of decimal places.

```
DOUBLE ROUND(DOUBLE number [, BIGINT decimal_places]); DECIMAL ROUND(DECIMAL number [, BIGINT decimal_places]);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, an error occurs. decimal_places: optional. The value must be a BIGINT constant that specifies the number of decimal places to which the function rounds the number. If the value is of any other type, an error occurs. If you omit this parameter, the function rounds the number to the nearest integer. The default value is 0.

**Note**

This parameter can be a negative number. A negative value causes the function to count digits to the left of the decimal point and discard the fractional part. If the absolute value of decimal_places exceeds the number of digits in the integer part, the function returns 0. The function returns a value of the DOUBLE or DECIMAL type. If an input value is NULL, the function returns NULL.

```
SELECT ROUND(125.315); -- Return result +-------+
| _c0   |
+-------+
| 125.0 |
+-------+ SELECT ROUND(125.315, 0); -- Return result +-------+
| _c0   |
+-------+
| 125.0 |
+-------+ SELECT ROUND(125.315, 1); -- Return result +-------+
| _c0   |
+-------+
|1253|
```

```
| 125.3 |
+-------+ SELECT ROUND(125.315, 2); -- Return result +--------+
| _c0    |
+--------+
| 125.32 |
+--------+ SELECT ROUND(125.315, 3); -- Return result +---------+
| _c0     |
+---------+
| 125.315 |
+---------+ SELECT ROUND(-125.315, 2); -- Return result +---------+
| _c0     |
+---------+
| -125.32 |
+---------+ SELECT ROUND(123.345, -2); -- Return result +-------+
| _c0   |
+-------+
| 100.0 |
+-------+ SELECT ROUND(NULL); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT ROUND(123.345, 4); -- Return result +---------+
| _c0     |
+---------+
|123345|
```

```
| 123.345 |
+---------+ SELECT ROUND(123.345, -4); -- Return result +------+
| _c0  |
+------+
| 0.0  |
+------+
```

##### SIN

This topic describes how to use the SIN mathematical function in MaxCompute to calculate the sine of an input value in radians. This function calculates the sine of a number. The input value must be in radians.

```
DOUBLE SIN(DOUBLE number); DECIMAL SIN(DECIMAL number);
```

number: required. The data type is DOUBLE or DECIMAL. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, an error occurs. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT SIN(0); -- Return result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SIN(3.1415926/2); -- Return result +---------------------+
|          _c0        |
+---------------------+
| 0.9999999999999997  |
+---------------------+
```

##### SINH

This topic describes how to use the SINH mathematical function in MaxCompute to calculate the hyperbolic sine of an input value. This function calculates the hyperbolic sine of a number.

```
DOUBLE SINH(DOUBLE number); DECIMAL SINH(DECIMAL number);
```

number: Required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the system returns an error. This function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, this function returns NULL.

```
SELECT SINH(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SINH(1); -- Result +---------------------+
| _c0                 |
+---------------------+
| 1.1752011936438014  |
+---------------------+
```

##### SQRT

This topic describes how to use the SQRT mathematical function in MaxCompute to calculate the square root of an input value. This function calculates the square root of a number.

```
DOUBLE SQRT(DOUBLE number); DECIMAL SQRT(DECIMAL number);
```

number: Required. The data type is DOUBLE or DECIMAL. The value must be greater than 0. If the value is less than 0, the function returns NULL. If the input data type is STRING or BIGINT, the system implicitly converts the value to the DOUBLE type before the calculation. If the input data type is of any other type, the system returns an error. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT SQRT(4); -- Result +------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT SQRT(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+
```

##### TAN

This topic describes how to use the TAN mathematical function in MaxCompute to calculate the tangent of an input value in radians. This function calculates the tangent of a number. The input value must be in radians.

```
DOUBLE TAN(DOUBLE number); DECIMAL TAN(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, an error occurs. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT TAN(0); -- Return result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT TAN(0.7853981633974483); -- Return result +--------------------+
| _c0                |
+--------------------+
| 0.9999999999999999 |
+--------------------+
```

##### TANH

This topic describes how to use the TANH mathematical function in MaxCompute to calculate the hyperbolic tangent of an input value. This function calculates the hyperbolic tangent of a number.

```
DOUBLE TANH(DOUBLE number); DECIMAL TANH(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the DOUBLE or DECIMAL type. If the input value is NULL, the function returns NULL.

```
SELECT TANH(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT TANH(1); -- Result +---------------------+
| _c0                 |
+---------------------+
| 0.7615941559557649  |
```

##### TRUNC

This topic describes how to use the TRUNC mathematical function and provides examples. Function syntax:

```
double trunc(double number[, bigint decimal_places]) decimal trunc(decimal number[, bigint decimal_places])
```

Description: This function truncates the input value of **number** to a specified number of decimal places. Parameters:
**number**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or
BIGINT type, it is implicitly converted into a value of the DOUBLE type before the calculation. If the input value is of another data type, an error is returned.
**decimal_places**: the decimal place, which is a constant of the BIGINT type. This parameter
indicates the position where the number is truncated. If it is of another data type, it is implicitly converted into the BIGINT type. If you do not specify this parameter, the number is truncated to the ones place.

**Note**

**decimal_places** can be a negative value, which indicates that the number is truncated
from the decimal point to the left and the decimal part is left out. If **decimal_places** exceeds the length of the integer part, 0 is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned.

**Note**

If a value of the DOUBLE type is returned, the return value may not be properly displayed. This issue exists in all systems. For more information, see
**trunc(125.815,1)** in the following example.
The number is filled with zeros from the specified position. Examples:

```
trunc(125.815) = 125.0 trunc(125.815, 0) =125.0 trunc(125.815, 1) = 125.80000000000001 trunc(125.815, 2) = 125.81 trunc(125.815, 3) = 125.815 trunc(-125.815, 2) = -125.81 trunc(125.815, -1) = 120.0 trunc(125.815, -2) = 100.0 trunc(125.815, -3) = 0.0 trunc(123.345, 4) = 123.345 trunc(123.345, -4) = 0.0
```

##### Additional mathematical functions

###### Usage notes

This topic describes the settings for using the newly extended mathematical functions. MaxCompute 2.0 introduces new mathematical functions. To use these new functions in SQL statements, you must add the following SET statement.

```
SET odps.sql.type.system.odps2=true;
```

**Note**

You must submit and run the preceding SET statement together with the SQL statements that use the new functions.

###### LOG2

This topic describes how to use the LOG2 mathematical function in MaxCompute to calculate the base-2 logarithm of a number. This function returns the base-2 logarithm of a number.

```
DOUBLE LOG2(DOUBLE number); DOUBLE LOG2(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the function implicitly converts it to the DOUBLE type before the calculation. If the input value is of any other type, the function returns an error. This function returns a value of the DOUBLE type. If the input value is NULL, the function returns NULL. If the input value is 0, the function returns NULL.

```
SELECT LOG2(NULL); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG2(0); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG2(8); -- Return result +------+
| _c0  |
+------+
| 3.0  |
+------+
```

###### LOG10

This topic describes how to use the LOG10 function in MaxCompute to calculate the base-10 logarithm of a number. This function returns the base-10 logarithm of a number.

```
DOUBLE LOG10(DOUBLE number); DOUBLE LOG10(DECIMAL number);
```

number: required. The value must be of the DOUBLE or DECIMAL type. This function returns a value of the DOUBLE type. If the input value is NULL, the function returns NULL. If the input value is 0, the function returns NULL.

```
SELECT LOG10(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG10(0); -- Result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG10(8); -- Result +----------------------+
| _c0                  |
+----------------------+
| 0.9030899869919435   |
+----------------------+
```

###### BIN

This topic describes how to use the BIN mathematical function in MaxCompute to return the binary representation of an input value. This function returns the binary representation of a number.

```
STRING BIN(BIGINT number);
```

number: required. The value is of the BIGINT type. The function returns a value of the STRING type. If the input value is 0, the function returns
0. If the input value is NULL, the function returns NULL.

```
SELECT BIN(0); -- Result +------+
| _c0  |
+------+
| 0    |
+------+ SELECT BIN(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT BIN(12); -- Result +------+
| _c0  |
+------+
| 1100 |
+------+
```

###### HEX

This topic describes how to use the HEX mathematical function in MaxCompute to convert integers or strings into hexadecimal. This function converts an integer or a string into hexadecimal.

```
STRING HEX(BIGINT number); STRING HEX(STRING number); STRING HEX(BINARY number);
```

number: required. If number is of the BIGINT type, the function returns the hexadecimal representation of number. If number is of the STRING type, the function returns the hexadecimal representation of the string. The return value is of the STRING type. If the input value is 0, the function returns 0. If the input value is NULL, the function returns an error.

```
SELECT HEX(0); -- Result +------+
| _c0  |
+------+
| 0    |
+------+ SELECT HEX('abc'); -- Result +--------+
| _c0    |
+--------+
| 616263 |
+--------+ SELECT HEX(17); -- Result +------+
| _c0  |
+------+
| 11   |
+------+ SELECT HEX('17'); -- Result +------+
| _c0  |
+------+
| 3137 |
+------+ SELECT HEX(NULL); -- The function returns an error message and the execution fails.
```

###### UNHEX

This topic describes how to use the UNHEX mathematical function in MaxCompute to convert a hexadecimal string into the corresponding string. This function converts a hexadecimal string into the corresponding string.

```
BINARY UNHEX(STRING number);
```

number: required. This parameter specifies a hexadecimal string. This function returns a value of the BINARY type. If the input value is 0, the system reports an error. If the input value is NULL, the function returns NULL.

```
SELECT UNHEX('616263'); -- Result +------+
| _c0  |
+------+
| abc  |
+------+ SELECT UNHEX(616263); -- Result +------+
| _c0  |
+------+
| abc  |
+------+
```

###### RADIANS

This topic describes how to use the RADIANS mathematical function in MaxCompute to convert degreesto radians. This function converts degreesto radians.

```
DOUBLE RADIANS(DOUBLE number);
```

number: required. This parameter is of the DOUBLE type. This function returns a value of the DOUBLE type. If the input value is NULL, this function returns NULL.

```
SELECT RADIANS(90); -- Result +----------------------+
| _c0                  |
+----------------------+
| 1.5707963267948966   |
+----------------------+ SELECT RADIANS(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT RADIANS(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### DEGREES

This topic describes how to use the DEGREES mathematical function in MaxCompute to convert radians to degrees. This function converts radians to degrees.

```
DOUBLE DEGREES(DOUBLE number); DOUBLE DEGREES(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. This function returns a value of the DOUBLE type. If the input value is NULL, this function returns NULL.

```
SELECT DEGREES(1.5707963267948966); -- Result +------+
| _c0  |
+------+
| 90.0 |
+------+ SELECT DEGREES(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT DEGREES(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### SIGN

This topic describes how to use the SIGN mathematical function in MaxCompute to obtain the sign of an input parameter. This function obtains the sign of an input parameter.

```
DOUBLE SIGN(DOUBLE number); DOUBLE SIGN(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. This function returns a value of the DOUBLE type. If the input value is a positive number, this function returns 1.0. If the input value is a negative number, this function returns -1.0. If the input value is 0, this function returns 0.0. If the input value is NULL, this function returns NULL.

```
SELECT SIGN(-2.5); -- Result +------+
| _c0  |
+------+
| -1.0 |
+------+ SELECT SIGN(2.5); -- Result +------+
| _c0  |
+------+
| 1.0  |
+------+ SELECT SIGN(0); -- Result +------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SIGN(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### E

This topic describes how to use the E mathematical function in MaxCompute to return the value of a natural constant e. This function returns the value of e.

```
DOUBLE E();
```

None. This function returns a value of the DOUBLE type.

```
SELECT E(); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2.718281828459045   |
+---------------------+
```

###### PI

This topic describes how to use the PI mathematical function in MaxCompute to return the value of pi (π). This function returns the value of pi (π).

```
DOUBLE PI()
```

None. This function returns a value of the DOUBLE type.

```
SELECT PI(); -- Result +---------------------+
| _c0                 |
+---------------------+
| 3.141592653589793   |
+---------------------+
```

###### FACTORIAL

This topic describes how to use the FACTORIAL mathematical function in MaxCompute to calculate the factorial of an input value. This function returns the factorial of a number.

```
BIGINT FACTORIAL(INT number);
```

number: required. This parameter is of the INT type. Valid values: 0 to 20. This function returns a value of the BIGINT type. If the input value is 0, this function returns 1. If the input value is NULL or a value outside `[0,20]` , this function returns NULL.

```
SELECT FACTORIAL(5); -- Result +------+
| _c0  |
+------+
| 120  |
+------+
```

###### CBRT

This topic describes how to use the CBRT mathematical function in MaxCompute to calculate the cube root of an input value. This function calculates the cube root of a number.

```
DOUBLE CBRT(DOUBLE number);
```

number: Required. This parameter must be of the BIGINT, INT, SMALLINT, TINYINT, DOUBLE, FLOAT, or STRING type. This function returns a value of the DOUBLE type. If the data type of number is not BIGINT, INT, SMALLINT, TINYINT, DOUBLE, FLOAT, or STRING, the system returns an error. If the input value is NULL, this function returns NULL.

```
SELECT CBRT(8); -- Result +------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT CBRT(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### SHIFTLEFT

This topic describes how to use the SHIFTLEFT mathematical function in MaxCompute to perform a bitwise left shift operation. This function performs a bitwise left shift operation (<<).

```
INT SHIFTLEFT(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTLEFT(BIGINT number1, INT number2);
```

number1: required. This parameter must be of the TINYINT, SMALLINT, INT, or BIGINT type. number2: required. This parameter must be of the INT type. This function returns an INT or BIGINT value.

```
-- Shift the binary representation of 1 to the left by 2 bits (1<<2, 0001 shifted lef t by 2 bits is 0100) SELECT SHIFTLEFT(1, 2); -- Result +------+
| _c0  |
+------+
| 4    |
+------+ -- Shift the binary representation of 4 to the left by 3 bits (4<<3, 0100 shifted lef t by 3 bits is 100000) SELECT SHIFTLEFT(4, 3); -- Result +------+
| _c0  |
+------+
| 32   |
+------+
```

###### SHIFTRIGHT

This topic describes how to use the SHIFTRIGHT mathematical function in MaxCompute to perform a bitwise right shift operation. This function performs a bitwise right shift operation (>>).

```
INT SHIFTRIGHT(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTRIGHT(BIGINT number1, INT number2);
```

number1: required. This parameter must be of the TINYINT, SMALLINT, INT, or BIGINT type. number2: required. This parameter must be of the INT type. This function returns a value of the INT or BIGINT type.

```
- Shift the binary representation of 4 to the right by 2 bits (4>>2, shifting 0100 to
the right by 2 bits yields 0001) SELECT SHIFTRIGHT(4, 2); -- Result +------+
| _c0  |
+------+
| 1    |
+------+ -- Shift the binary representation of 32 to the right by 3 bits (32>>3, shifting 1000 00 to the right by 3 bits yields 0100) SELECT SHIFTRIGHT(32, 3); -- Result +------+
| _c0  |
+------+
| 4    |
+------+
```

###### SHIFTRIGHTUNSIGNED

This topic describes how to use the SHIFTRIGHTUNSIGNED mathematical function in MaxCompute to perform unsigned bitwise right shift operations. This function performs an unsigned bitwise right shift operation (>>>).

```
INT SHIFTRIGHTUNSIGNED(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTRIGHTUNSIGNED(BIGINT number1, INT number2);
```

number1: required. This parameter must be of the TINYINT, SMALLINT, INT, or BIGINT type. number2: required. This parameter must be of the INT type. This function returns a value of the INT or BIGINT type.

```
-- Perform an unsigned bitwise right shift of 2 bits on the binary representation of 8 (8>>>2, shifting 1000 right by 2 bits results in 0010) SELECT SHIFTRIGHTUNSIGNED(8, 2); -- Return result +------+
| _c0  |
+------+
| 2    |
+------+ -- Perform an unsigned bitwise right shift of 2 bits on the binary representation of -14 (-14>>>2, shifting 11111111 11111111 11111111 11110010 right by 2 bits results in 00111111 11111111 11111111 11111100) SELECT SHIFTRIGHTUNSIGNED(-14, 2); -- Return result +------------+
| _c0        |
+------------+
| 1073741820 |
+------------+
```

###### FORMAT_NUMBER

This topic describes how to use the FORMAT_NUMBER mathematical function in MaxCompute to convert a number into a string of a specified format. This function converts a number into a string of a specified format.

```
STRING FORMAT_NUMBER(FLOAT|DOUBLE|DECIMAL expr1, expr2);
```

expr1: required. This parameter specifies the data that you want to format. expr2: required. This parameter specifies the target format for the conversion.

**Note**

The parameter can be of the INT type to specify the number of decimal places to retain. The parameter can also be a format string such as `#,###,###.##` . If expr2 is greater than 0, this function rounds the value to the specified number of decimal places. If expr2 equals 0, the result contains no decimal point or decimal part. If expr2 is less than 0 or greater than 340, an error is returned. This function returns a value of the STRING type.

```
SELECT FORMAT_NUMBER(5.230134523424545456, 3); -- Result +------+
| _c0  |
+------+
| 5.230|
+------+ SELECT FORMAT_NUMBER(12332.123456, '#,###,###,###.###'); -- Result +---------+
| _c0     |
+---------+
| 12,332.123 |
+---------+
```

###### WIDTH_BUCKET

This topic describes how to use the WIDTH_BUCKET mathematical function in MaxCompute to define bucket ranges and return the ID of the bucket into which the value of a specific expression falls. This function specifies the number of buckets and the minimum and maximum values of the acceptable range for a bucket. This function allows you to construct equi-width buckets, in which the bucket range is divided into intervals that have an identical size. This function returns the ID of the bucket into which the value of a specific expression falls. This function supports the following data types: DECIMAL(precision,scale) in the MaxCompute V2.0 data type edition, BIGINT, INT, FLOAT, DOUBLE, and DECIMAL.

```
BIGINT WIDTH_BUCKET(NUMERIC expr, NUMERIC min_value, NUMERIC max_value, INT num_buckets);
```

expr: required. This parameter specifies the expression for which you want to identify the matching bucket ID. min_value: required. This parameter specifies the minimum value of the acceptable range for the bucket.. max_value: required. This parameter specifies the maximum value of the acceptable range for the bucket.. The maximum value must be greater than the minimum value. num_buckets: required. This parameter specifies the number of buckets. The value must be greater than 0. This function returns a value of the BIGINT type. The value ranges from 0 to num_buckets plus 1. If the value of expr is less than min_value, the function returns 0. If the value of expr is greater than max_value, the function returns num_buckets plus 1. If the value of expr is NULL, the function returns NULL. In other cases, the function returns the ID of the bucket into which the value of expr falls. The ID of the bucket is calculated by using the following formula: `FLOOR(num_buckets x`

```
(expr - min_value)/(max_value - min_value) + 1) . SELECT key, value, WIDTH_BUCKET(value, 100, 500, 5) AS value_group FROM VALUES
    (1, 99),
    (2, 100),
    (3, 199),
    (4, 200),
    (5, 499),
    (6, 500),
    (7, 501),
    (8, NULL)
AS t(key, value); -- Return result +-------+--------+-------------+
| key   | value  | value_group |
+-------+--------+-------------+
| 1     | 99     | 0           |
| 2     | 100    | 1           |
| 3     | 199    | 2           |
| 4     | 200    | 2           |
| 5     | 499    | 5           |
| 6     | 500    | 6           |
| 7     | 501    | 6           |
| 8     | \N     | \N          |
+-------+--------+-------------+
```

#### String functions

##### CHAR_MATCHCOUNT

The CHAR_MATCHCOUNT function counts the number of identical characters between two strings. Specifically, it counts how many characters in `str1` also appear in `str2` . This topic describes how to use the CHAR_MATCHCOUNT function in MaxCompute. This function counts the number of characters in the first string that also appear in the second string.

```
BIGINT char_matchcount(STRING str1, STRING str2);
```

**Note**

The strings must be valid UTF-8 strings. If the comparison detects invalid characters, the function returns `0` . str1: required. This parameter is of the STRING type and specifies the source string to match. str2: required. This parameter is of the STRING type and specifies the target string for comparison. The function returns a value of the BIGINT type. If any input parameter is NULL, the function returns NULL.

```
SELECT CHAR_MATCHCOUNT('abd', 'aabc'); -- Return result +--------+
|   _c0  |
+--------+
|    2   |
+--------+
```

##### CHR

This topic describes how to use the CHR string function in MaxCompute to convert a specified ASCII code into the corresponding character. This function converts a specified ASCII code into a character.

```
STRING CHR(BIGINT ascii);
```

ascii: required. An ASCII value of the BIGINT type. If the input is of the STRING, DOUBLE, or DECIMAL type, the system implicitly converts it into the BIGINT type before the calculation. If the input is of any other type, the system returns an error. A value of the STRING type is returned. The input value must range from 0 to 255. If the value exceeds this range, the system returns an error. If the input value is NULL, the system returns NULL.

```
SELECT CHR(65); -- Result +------+
| _c0  |
+------+
| A    |
+------+ SELECT CHR(NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### CONCAT

This topic describes how to use the CONCAT string function in MaxCompute to concatenate all input strings. This function concatenates all input strings and returns the result.

```
STRING CONCAT(STRING a, STRING b...);
```

a, b...: required. The STRING type. If an input parameter is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts it to the STRING type for calculation. If an input parameter is of any other type, the system returns an error. This function returns a value of the STRING type. If you do not provide any parameters or if any input parameter is NULL, this function returns NULL.

```
SELECT CONCAT('ab', 'c'); -- Result +------+
| _c0  |
+------+
| abc  |
+------+ SELECT CONCAT(); -- Result +------+
| _c0  |
+------+
| NULL |
+------+ SELECT CONCAT('a', NULL, 'b'); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### INSTR

This topic describes how to use the INSTR string function in MaxCompute to calculate the position of a substring in a string. This function calculates the position of the substring str2 in the string str1.

```
BIGINT INSTR(STRING str1, STRING str2 [, BIGINT start_position [, BIGINT nth_appearance]]);
```

str1: required. This parameter must be of the STRING type. It specifies a string in which you search for a substring. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of a data type that cannot be converted into a value of the STRING type, an error is returned. str2: required. This parameter must be of the STRING type. It specifies a substring you want to search for. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of a data type that cannot be converted into a value of the STRING type, an error is returned. start_position: optional. This parameter must be of the BIGINT type. If the input value is of another data type, an error is returned. This parameter specifies the position of the character in str1 from which the search starts. The default start position is the first character, marked as 1. If start_position is a negative value, the search starts from the end to the start of the string and the last character is -1. nth_appearance: optional. This parameter must be of the BIGINT type. If the value is greater than 0, it indicates the position where the substring matches the string for the nth_appearance time. If the value is of another data type or less than or equal to 0, an error is returned. This function returns a value of the BIGINT type. If the system does not find str2 in str1, the function returns 0. If str2 is an empty string, the match always succeeds. For example, SELECT INSTR('abc','') returns 1. If the value of str1, str2, start_position, or nth_appearance is NULL, the function returns NULL.

```
-- Example 1: Calculate the position of the character e in the string Tech on the net SELECT INSTR('Tech on the net', 'e'); -- Result +------+
| _c0  |
+------+
| 2    |
+------+ -- Example 2: Calculate the position of the substring on in the string Tech on the ne
```

`t`

```
SELECT INSTR('Tech on the net', 'on'); -- Result +------+
| _c0  |
+------+
| 6    |
+------+ -- Example 3: Calculate the position of the second occurrence of the character e in t he string Tech on the net, starting from the third character SELECT INSTR('Tech on the net', 'e', 3, 2); -- Result +------+
| _c0  |
+------+
| 14   |
+------+ -- Example 4: Any input parameter is NULL SELECT INSTR('Tech on the net', NULL); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### IS_ENCODING

This topic describes how to use the IS_ENCODING string function in MaxCompute to determine whether an input string can be converted between specified character sets. This function determines whether the input string str can be converted from a specified source character set from_encoding to another character set to_encoding. You can also use this function to detect corrupted data. A common approach is to set from_encoding to UTF- 8 and to_encoding to GBK.

```
BOOLEAN IS_ENCODING(STRING str, STRING from_encoding, STRING to_encoding);
```

str: required. This parameter is of the STRING type. An empty string belongs to any character set. from_encoding: required. This parameter is of the STRING type. The source character set. to_encoding: required. This parameter is of the STRING type. The destination character set. A value of the BOOLEAN type is returned. If str is successfully converted, the function returns True. Otherwise, it returns False. If any input parameter is NULL, the function returns NULL.

```
SELECT IS_ENCODING('测试', 'utf-8', 'gbk'); -- Result +------+
| _c0  |
+------+
| true |
+------+ -- The GBK character set includes these two traditional Chinese characters. SELECT IS_ENCODING('測試', 'utf-8', 'gbk'); -- Result +------+
| _c0  |
+------+
| true |
+------+ -- The GB2312 character set does not include these two characters. SELECT IS_ENCODING('測試', 'utf-8', 'gb2312'); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### KEYVALUE

This topic describes how to use the KEYVALUE string function in MaxCompute to split a source string into key-value pairs by using specified delimiters and return the value that corresponds to a specified key. The function splits the source string srcStr into key-value pairs by using split1, separates the keys and values by using split2, and returns the value that corresponds to the specified key.

```
KEYVALUE(STRING srcStr, STRING split1, STRING split2, STRING key); KEYVALUE(STRING srcStr, STRING key);
```

srcStr: required. This parameter must be of the STRING type. It specifies the source string to be split. key: required. This parameter must be of the STRING type. The target key whose corresponding value will be returned after the string is split. split1: optional. This parameter must be of the STRING type. It specifies the delimiter for key-value pairs. If this parameter is not specified, the default value is a semicolon (;). split2: optional. This parameter must be of the STRING type. It specifies the delimiter used to separate keys from values. If this parameter is not specified, the default value is a colon (:). The function returns a value of the STRING type. If split1 or split2 is NULL, the function returns NULL. If the srcStr or key is NULL, or if no matching key exists, the function returns NULL. If multiple matching key-value pairs exist, the function returns the value of the first matching key.

```
-- Example 1: Use the default delimiters and return the Value that corresponds to the key 1 SELECT KEYVALUE('0:1\;1:2', 1); -- Result +------+
| _c0  |
+------+
| 2    |
+------+ -- Example 2: Specify "\;" as split1 and ":" as split2, and return the Value that cor responds to the key tf SELECT KEYVALUE('\;decreaseStore:1\;xcard:1\;isB2C:1\;tf:21910\;cart:1\;shipping:2\;pf:0\;mark :shoes\;instPayAmount:0\;', '\;', ':', 'tf'); -- Result +-------+
| _c0   |
+-------+
| 21910 |
+-------+
```

##### LENGTH

This topic describes how to use the LENGTH string function in MaxCompute to return the length of a string. This function returns the length of the string str.

```
BIGINT LENGTH(STRING str);
```

str: required. The STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the function implicitly converts the input value to the STRING type before calculation. If the input value is of any other type, an error is returned. This function returns a value of the BIGINT type. If the input value is NULL, the function returns NULL. If the input value is not in UTF-8 encoding, the function returns -1.

```
SELECT LENGTH('hi! China'); -- Return result +------+
| _c0  |
+------+
| 6    |
+------+
```

##### LENGTHB

This topic describes how to use the LENGTHB string function in MaxCompute to return the length of a string in bytes. This function returns the length of the string str in bytes.

```
BIGINT LENGTHB(STRING str);
```

str: required. The data type is STRING. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts the value to the STRING type before calculation. If the input value is of any other type, the system reports an error. This function returns a value of the BIGINT type. If the input value is NULL, the function returns NULL.

```
SELECT LENGTHB('hi! 中国'); -- Return result +------+
| _c0  |
+------+
| 10   |
+------+
```

##### MD5

This topic describes how to use the string function MD5 in MaxCompute to compute the MD5 hash of an input string.

**Usage notes**

Computes the MD5 hash of the input string value.

**Syntax**

```
STRING MD5(STRING value);
```

value: required. The value is of the STRING type. If the input is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts it to the STRING type before computation. If the input is of any other type, an error occurs. The return value is of the STRING type. If the input parameter is NULL, the function returns NULL.

```
SELECT MD5('abc'); -- Return result +----------------------------------+
| _c0                              |
+----------------------------------+
| 900150983cd24fb0d6963f7d28e17f72 |
+----------------------------------+ SELECT MD5(NULL); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### PARSE_URL

This topic describes how to use the PARSE_URL string function in MaxCompute to parse URLs and extract information based on specified parts. This function parses a URL and extracts information based on a key.

```
STRING PARSE_URL(STRING url, STRING part [, STRING key]);
```

url: required. The URL to parse. If the URL is NULL, the function returns NULL. If the URL is invalid, an error is returned. part: required. The STRING type. Valid values include HOST, PATH, QUERY, REF, PROTOCOL, AUTHORITY, FILE, and USERINFO. This parameter is case-insensitive. If you specify a value outside this range, an error is returned. key: optional. The STRING type. When the part parameter is QUERY, the function extracts the value from the query string based on the key. Otherwise, the function ignores the key parameter. The function returns a value of the STRING type.

```
-- Example URL: file://username:password@example.com:8042/over/there/index.dtb?type=a nimal&name=narwhal#nose SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'HOST'); -- Result +--------------+
| _c0          |
+--------------+
| example.com  |
+--------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'PATH'); -- Result +----------------------------+
| _c0                        |
+----------------------------+
| /over/there/index.dtb      |
+----------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'QUERY'); -- Result +-------------------------------+
| _c0                           |
+-------------------------------+
| type=animal&name=narwhal      |
+-------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'QUERY', 'name'); -- Result +----------+
| _c0      |
+----------+
| narwhal  |
+----------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'REF'); -- Result +------+
| _c0  |
+------+
```

```
| nose |
+------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'PROTOCOL'); -- Result +------+
| _c0  |
+------+
| file |
+------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'AUTHORITY'); -- Result +----------------------------------------------+
| _c0                                          |
+----------------------------------------------+
| username:password@example.com:8042            |
+----------------------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'FILE'); -- Result +-------------------------------------------------------------+
| _c0                                                         |
+-------------------------------------------------------------+
| /over/there/index.dtb?type=animal&name=narwhal              |
+-------------------------------------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'USERINFO'); -- Result +---------------------+
| _c0                 |
+---------------------+
| username:password   |
+---------------------+
```

##### REGEXP_EXTRACT

This topic describes how to use the REGEXP_EXTRACT string function in MaxCompute to extract the content of a specified group from a string based on a regular expression. This function splits the source string based on the regular expression pattern and returns the characters of the group at the specified occurrence index.

```
STRING REGEXP_EXTRACT(STRING source, STRING pattern [, BIGINT occurrence]);
```

source: required. This parameter is of the STRING type and specifies the string to search. pattern: required. This parameter is a STRING constant. If the pattern is an empty string or does not specify a group, the system returns an error. occurrence: optional. This parameter is a BIGINT constant. The value must be greater than or equal to 0. If the value is of another data type or less than 0, the system returns an error. If you do not specify this parameter, the default value is 1, which indicates that the system returns the first group. If the occurrence is 0, the system returns the substring that matches the entire pattern. The return value is of the STRING type. If any input parameter is NULL, the system returns NULL. The system stores data in UTF- 8 format. Chinese characters can be represented by their corresponding hexadecimal encodings, with a valid range of [\x{4e00},\x{9fa5}].

```
SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 1); -- Result +------+
| _c0  |
+------+
| the  |
+------+ SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 2); -- Result +------+
| _c0  |
+------+
| bar  |
+------+ SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 0); -- Result +-----------+
| _c0       |
+-----------+
| foothebar |
+-----------+ SELECT REGEXP_EXTRACT('8d99d8', '8d(\\d+)d8'); -- Result +------+
| _c0  |
+------+
| 99   |
+------+ -- If you submit SQL statements for regular expression calculations on the MaxCompute client, you must use two backslashes (\\) as escape characters. -- If the pattern does not specify a group, the system returns an error: -- SELECT REGEXP_EXTRACT('foothebar', 'foothebar'); -- Error
```

##### REGEXP_INSTR

This topic describes how to use the REGEXP_INSTR string function in MaxCompute to return the start or end position of the substring that matches a regular expression for the nth time in a string. This function returns the start or end position of the substring in the source string that matches the pattern for the nth occurrence, starting from start_position.

```
BIGINT REGEXP_INSTR(STRING source, STRING pattern [, BIGINT start_position [, BIGINT nth_occurrence [, BIGINT return_option]]]);
```

source: required. This parameter is of the STRING type and specifies the string to search. pattern: required. This parameter is a STRING constant. An error is returned if pattern is an empty string. start_position: optional. This parameter is a BIGINT constant and specifies the position where the search starts. The default value is 1 if you do not specify this parameter. An error is returned if the value is of another type or is less than or equal to 0. nth_occurrence: optional. This parameter is a BIGINT constant. The default value is 1 if you do not specify this parameter, which indicates the first occurrence. An error is returned if the value is of another type or is less than or equal to 0. return_option: optional. This parameter is a BIGINT constant. The value is 0 or 1. An error is returned if the value is of another type or is not an allowed value. A value of 0 indicates that the function returns the start position of the match. A value of 1 indicates that the function returns the end position of the match. The function returns a value of the BIGINT type. The function returns the start or end position of the matched substring in the source string based on the value of return_option. If any input parameter is NULL, the function returns NULL.

```
SELECT REGEXP_INSTR('i love www.taobao.com', 'o[[:alpha:]]{1}', 3, 2); -- Return result +------+
| _c0  |
+------+
| 14   |
+------+
```

##### REGEXP_SUBSTR

This topic describes how to use the REGEXP_SUBSTR string function in MaxCompute to return a substring that matches a regular expression for the nth time in a string. This function returns the substring that matches the specified pattern for the nth_occurrence time in source, starting from the start_position.

```
STRING REGEXP_SUBSTR(STRING source, STRING pattern [, BIGINT start_position [, BIGINT nth_occurrence]]);
```

source: required. This parameter is of the STRING type and specifies the string to search. pattern: required. This parameter is a STRING constant and specifies the pattern to match. An error is returned if pattern is an empty string. start_position: optional. This parameter is a BIGINT constant and must be greater than 0. An error is returned if the value is of another type or is less than or equal to 0. If you do not specify this parameter, the default value is 1, which indicates that the match starts from the first character of source. nth_occurrence: optional. This parameter is a BIGINT constant and must be greater than
0. An error is returned if the value is of another type or is less than or equal to 0. If you do
not specify this parameter, the default value is 1, which indicates that the function returns the substring of the first match. This function returns a value of the STRING type. If any input parameter is NULL, this function returns NULL. This function also returns NULL when no match is found.

```
SELECT REGEXP_SUBSTR('I love aliyun very much', 'a[[:alpha:]]{5}'); -- Return result +--------+
| _c0    |
+--------+
| aliyun |
+--------+ SELECT REGEXP_SUBSTR('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 1); -- Return result +-------+
| _c0   |
+-------+
|  have |
+-------+ SELECT REGEXP_SUBSTR('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 2); -- Return result +------+
| _c0  |
+------+
|  2   |
+------+
```

##### REGEXP_COUNT

This topic describes how to use the REGEXP_COUNT string function in MaxCompute to count the occurrences of substrings that match a regular expression in a string. This function counts the occurrences of substrings that match the specified pattern in the source string, starting from start_position.

```
BIGINT REGEXP_COUNT(STRING source, STRING pattern [, BIGINT start_position]);
```

source: required. This parameter is of the STRING type and specifies the string to search. The function returns an error if the value is of another data type. pattern: required. The parameter must be a STRING constant and specifies the pattern to match. The function returns an error if the pattern is an empty string or of another data type. start_position: optional. The value must be a BIGINT constant greater than 0. The function returns an error if the value is of another data type or is less than or equal to 0. If you do not specify this parameter, the default value is 1, which indicates that the match starts from the first character of the source string. The function returns a value of the BIGINT type. The function returns NULL if any input parameter is NULL. The function returns 0 if it finds no match.

```
SELECT REGEXP_COUNT('abababc', 'a.c'); -- Result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT REGEXP_COUNT('abcde', '[[:alpha:]]{2}', 3); -- Result +------+
| _c0  |
+------+
| 1    |
+------+
```

##### REGEXP_REPLACE

This topic describes how to use the REGEXP_REPLACE string function in MaxCompute to replace substrings that match a regular expression in a string with a specified string. This function replaces the substring in the source string that matches the pattern for the specified occurrence time with the replace_string and returns the result.

```
STRING REGEXP_REPLACE(STRING source, STRING pattern, STRING replace_string[, BIGINT o ccurrence]);
```

source: required. This parameter is of the STRING type and specifies the string that you want to process. pattern: required. This parameter is a STRING constant and specifies the pattern to match. If pattern is an empty string, the system returns an error. replace_string: required. This parameter is of the STRING type and specifies the string that replaces the matched pattern. occurrence: optional. This parameter is a BIGINT constant and must be greater than or equal to 0. This parameter specifies which match to replace with replace_string. A value of 0 indicates that the function replaces all matched substrings. If the value is of another type or less than 0, the system returns an error. If this parameter is omitted, the default value is 0. This function returns a value of the STRING type. When you reference a non-existent group, the function does not perform the replacement. If replace_string is NULL and the pattern has a match, the function returns NULL. If replace_string is NULL but the pattern does not match, the function returns the original string. If any input parameter is NULL, the function returns NULL.

```
-- Example 1: Replace all matches (occurrence is 0) SELECT REGEXP_REPLACE("123.456.7890", "([[:digit:]]{3})\\.([[:digit:]]{3})\\.([[:digi t:]]{4})", "(\\1)\\2-\\3", 0); -- Return result +------------------+
|  (123)456-7890   |
+------------------+ -- Example 2: Add a space after each single character (occurrence is 0) SELECT REGEXP_REPLACE("abcd", "(.)", "\\1 ", 0); -- Return result +-----------+
|  a b c d  |
+-----------+ -- Example 3: Replace only the first match (occurrence is 1) SELECT REGEXP_REPLACE("abcd", "(.)", "\\1 ", 1); -- Return result +-----------+
|   a bcd   |
+-----------+ -- Example 4: Reference a non-existent group (Avoid this usage. The result of referen cing a non-existent group is undefined.) SELECT REGEXP_REPLACE("abcd", "(.)", "\\2", 1); -- Return result +------+
| abcd |
+------+ -- Example 5: Reference an existing group for replacement SELECT REGEXP_REPLACE("abcd", "(.*)(.)$", "\\2", 0); -- Return result +------+
|   d  |
+------+ -- Example 6: Reference a non-existent group (The pattern does not define any group. Avoid this usage. The result of referencing a non-existent group is undefined.) SELECT REGEXP_REPLACE("abcd", "a", "\\1", 0); -- Return result +------+
|  bcd |
+------+
```

##### SPLIT_PART

This topic describes how to use the SPLIT_PART string function in MaxCompute to split a string by a delimiter and return the substring of a specified segment. This function splits the string str by the specifiedseparator and returns the substring from the start segment to the end segment (inclusive).

```
STRING SPLIT_PART(STRING str, STRING separator, BIGINT start[, BIGINT end]);
```

str: required. This parameter is of the STRING type and specifies the string to split. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the function returns an error. separator: required. This parameter is a STRING constant and specifies the delimiter for splitting. It can be a single character or a string. If the value is of any other type, the function returns an error. start: required. This parameter is a BIGINT constant greater than 0. If the value is not a constant or is of any other type, the function returns an error. This parameter specifies the starting segment number (starting from 1). If you do not specify end, the function returns the segment specified by start. end: optional. This parameter is a BIGINT constant. The value must be greater than or equal to start. Otherwise, the function returns an error. This parameter specifies the ending segment number. If the value is not a constant or is of any other type, the function returns an error. You can omit this parameter. If you omit this parameter, the function returns the last segment. The function returns a value of the STRING type. If the value of start exceeds the actual number of segments after splitting, the function returns an empty string. If separator does not exist in str and start is set to 1, the function returns the entire str. If str is an empty string, the function returns an empty string. If separator is an empty string, the function returns the original string str. If end exceeds the number of segments, the function processes the value as the total number of segments. If any input parameter is NULL, the function returns NULL.

```
-- Example 1: Split a string and return the first segment SELECT SPLIT_PART('a,b,c,d', ',', 1); -- Result +------+
|   a  |
+------+ -- Example 2: Split a string and return the first to second segments SELECT SPLIT_PART('a,b,c,d', ',', 1, 2); -- Result +------+
|  a,b |
+------+ -- Example 3: start exceeds the actual number of segments SELECT SPLIT_PART('a,b,c,d', ',', 10); -- Result +------+
|      |
+------+
```

##### SUBSTR

This topic describes how to use the SUBSTR string function in MaxCompute to return a substring of a specified length starting from a specified position in a string. This function returns a substring of the string str, starting at start_position with a length of length.

```
STRING SUBSTR(STRING str, BIGINT start_position[, BIGINT length]);
```

str: required. The data type is STRING. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts the value to the STRING type before calculation. If the input value is of any other type, the system reports an error. start_position: required. The data type is BIGINT. The starting position is 1. If start_position is 0, the function returns NULL. If start_position is a negative number, the starting position counts backward from the end of the string, and the last character is -1. If the input value is of any other type, the system reports an error. length: optional. The data type is BIGINT. This parameter specifies the length of the substring and must be greater than 0. If the input value is of any other type or is less than or equal to 0, the system reports an error. The return value is of the STRING type. If any input parameter is NULL, the function returns NULL. If you omit length, the function returns the substring of str from start_position to the end of str.

```
-- Example 1: Extract a substring from the second character to the end SELECT SUBSTR('abc', 2); -- Result +------+
|  bc  |
+------+ -- Example 2: Extract one character starting from the second character SELECT SUBSTR('abc', 2, 1); -- Result +------+
|   b  |
+------+ -- Example 3: Extract two characters starting from the second to last character SELECT SUBSTR('abc', -2, 2); -- Result +------+
|  bc  |
+------+
```

##### TOLOWER

This topic describes how to use the TOLOWER string function in MaxCompute to convert an English string to lowercase. This function converts the English string specified by source to lowercase.

```
STRING TOLOWER(STRING source);
```

source: required. The value is of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts the value to the STRING type before calculation. If the input value is of any other type, the system returns an error. The return value is of the STRING type. If the input parameter is NULL, the function returns NULL.

```
-- Convert an English string to lowercase. SELECT TOLOWER("aBcd"); -- Result +------+
| abcd |
+------+ -- Mixed Chinese and English string. SELECT TOLOWER("哈哈Cd"); -- Result +--------+
```

| 哈哈cd |

```
+--------+
```

##### TOUPPER

This topic describes how to use the TOUPPER string function in MaxCompute to convert an English string to uppercase. This function converts the English string specified by source to uppercase.

```
STRING TOUPPER(STRING source);
```

source: required. The value is of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the function implicitly converts it to the STRING type before calculation. If the input value is of any other type, an error is returned. This function returns a value of the STRING type. If the input parameter is NULL, this function returns NULL.

```
-- Convert an English string to uppercase. SELECT TOUPPER("aBcd"); -- Result +------+
| ABCD |
+------+ -- Mixed Chinese and English string. SELECT TOUPPER("Cd"); -- Result +--------+
| CD     |
+--------+
```

##### TO_CHAR

This topic describes how to use the TO_CHAR string function in MaxCompute to convert BOOLEAN, BIGINT, DECIMAL, or DOUBLE values into their corresponding STRING representations. This function converts BOOLEAN, BIGINT, DECIMAL, or DOUBLE values into their corresponding STRING representations.

```
STRING TO_CHAR(BOOLEAN value); STRING TO_CHAR(BIGINT value); STRING TO_CHAR(DOUBLE value); STRING TO_CHAR(DECIMAL value);
```

value: Required. This parameter accepts BOOLEAN, BIGINT, DECIMAL, or DOUBLE values. If you specify a value of another type, the system returns an error. This function returns a STRING value. If the input parameter is NULL, this function returns NULL.

```
SELECT TO_CHAR(123); -- Result +------+
| 123  |
+------+ SELECT TO_CHAR(TRUE); -- Result +-------+
| TRUE  |
+-------+ SELECT TO_CHAR(1.23); -- Result +-------+
| 1.23  |
+-------+ SELECT TO_CHAR(NULL); -- Result +-------+
| NULL  |
+-------+
```

##### TRIM

This topic describes how to use the TRIM string function in MaxCompute to remove leading and trailing spaces from an input string. This function removes leading and trailing spaces from the input string str.

```
STRING TRIM(STRING str);
```

**Parameter description**

str: required. The value is of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. This function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

```
SELECT TRIM(' abc '); -- Return result +------+
| abc  |
+------+
```

##### LTRIM

This topic describes how to use the LTRIM string function in MaxCompute to remove leading spaces from an input string. This function removes leading spaces from the input string str.

```
STRING LTRIM(STRING str);
```

str: required. The value is of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

```
SELECT LTRIM(' abc '); -- Result +------+
| abc  |
+------+
```

##### RTRIM

This topic describes how to use the RTRIM string function in MaxCompute to remove trailing spaces from an input string. This function removes trailing spaces from the input string str.

```
STRING RTRIM(STRING str);
```

**Parameter description**

str: required. The value is of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

```
SELECT RTRIM('a abc '); -- Return result +------+
| a abc|
+------+
```

##### REVERSE

This topic describes how to use the REVERSE string function in MaxCompute to return a reversed string. The function returns a reversed string.

```
STRING REVERSE(STRING str);
```

str: required. The value is of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the function implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

**Example**

```
SELECT REVERSE('abcedfg'); -- Result +---------+
| gfdecba |
+---------+
```

##### SPACE

This topic describes how to use the SPACE string function in MaxCompute to return a string of spaces with a specified length. The function returns a string of spaces with a length of n.

```
STRING SPACE(BIGINT n);
```

n: required. The value must be of the BIGINT type and must not exceed `2 MB` . If the value is null, an error is returned. The function returns a value of the STRING type.

```
-- Verify the length of the spaces returned by SPACE(10). SELECT LENGTH(SPACE(10)); -- Result +------+
| 10   |
+------+ -- An error occurs if the length exceeds 2 MB. SELECT SPACE(400000000000);
```

##### REPEAT

This topic describes how to use the REPEAT string function in MaxCompute to repeat a string a specified number of times. This function returns the str string repeated n times.

```
STRING REPEAT(STRING str, BIGINT n);
```

str: Required. The value must be of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. n: Required. The value must be of the BIGINT type. The length must not exceed 2 MB. If this parameter is empty, the system returns an error. This function returns a value of the STRING type.

```
-- Repeat the string 'abc' 5 times. SELECT REPEAT('abc', 5); -- Result +-------------------+
| abcabcabcabcabc   |
+-------------------+
```

##### ASCII

This topic describes how to use the ASCII string function in MaxCompute. This function returns the ASCII code of the first character in the string **str**.

```
BIGINT ascii(STRING str);
```

str: This parameter must be of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. The function returns a value of the BIGINT type.

```
SELECT ASCII('abcde'); -- Result +-------+
|  _c0  |
+-------+
|   97  |
+-------+
```

##### Additional string functions

###### Usage notes

This topic describes the settings that you must configure to use the newly extended string functions. After an upgrade to MaxCompute 2.0, MaxCompute provides newly extended string functions. To use these new functions in SQL statements, you must add the following SET statement.

```
SET odps.sql.type.system.odps2=true;
```

**Note**

You must submit and run the preceding SET statement and the SQL statements that use the new functions at the same time.

###### CONCAT_WS

This topic describes the CONCAT_WS function in string functions and provides examples. Syntax:

```
string concat_ws(string SEP, string a, string b...) string concat_ws(string SEP, array)
```

Description: This function concatenates all input strings in an array by using a specified delimiter. Parameters:
**SEP**: the delimiter of the STRING type. If this parameter is not specified, an error is
returned.
**a, b...**: a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or
DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If no input values are specified or an input value is NULL, NULL is returned. Examples:

```
concat_ws(':','name','hanmeimei')='name:hanmeimei' concat_ws(':','avg',null,'34')=null
```

###### LPAD

This topic describes how to use the LPAD string function in MaxCompute to pad a string to a specified length on the left. This function pads the string `a` to the length `len` on the left using the string `b` .

```
STRING LPAD(STRING a, INT len, STRING b);
```

a: required. The data type is STRING. len: required. The data type is INT. b: required. The data type is STRING. This function returns a value of the STRING type. If len is less than the length of string a, the function returns the leftmost len characters of string a. If len is 0, the function returns an empty string. If you do not specify any input parameters or if any input parameter is NULL, the function returns NULL. If len is greater than the length of string a but less than the sum of the lengths of strings a and b, the function left-pads string a to a length of len by using the characters of string b from left to right.

```
-- Left-pad to a length of 10 characters. The function returns 12abcdefgh. SELECT LPAD('abcdefgh', 10, '12'); -- Result +----------------+
| 12abcdefgh     |
+----------------+ -- len is less than the length of string a. The function truncates 5 characters from the left and returns abcde. SELECT LPAD('abcdefgh', 5, '12'); -- Result +---------+
| abcde   |
+---------+ -- len is 0. The function returns an empty string. SELECT LPAD('abcdefgh', 0, '12'); -- Result +------+
|      |
+------+ -- An input parameter is NULL. The function returns NULL. SELECT LPAD(NULL, 0, '12'); -- Result +------+
| NULL |
+------+ -- Left-pad to a length of 9 characters. The function returns 1abcdefgh. SELECT LPAD('abcdefgh', 9, '12'); -- Result +---------------+
| 1abcdefgh     |
+---------------+
```

###### RPAD

This topic describes how to use the RPAD string function in MaxCompute to pad a string to a specified length on the right. This function pads the string a to the length len on the right using the string b.

```
STRING RPAD(STRING a, INT len, STRING b);
```

a: required. The data type is STRING. len: required. The data type is INT. b: required. The data type is STRING. This function returns a value of the STRING type. If len is less than the length of a, the function returns the leftmost len characters of a. If len is 0, the function returns an empty string. If you do not specify any input parameters or any input parameter is NULL, the function returns NULL. If len is greater than the length of a and less than the sum of the lengths of a and b, the function right-pads string a to a length of len by using the characters of string b from left to right.

```
-- Right-pad to a length of 10 characters. The function returns abcdefgh12. SELECT RPAD('abcdefgh', 10, '12'); -- Result +----------------+
| abcdefgh12     |
+----------------+ -- len is less than the length of a. The function truncates 5 characters from the lef t and returns abcde. SELECT RPAD('abcdefgh', 5, '12'); -- Result +---------+
| abcde   |
+---------+ -- len is 0. The function returns an empty string. SELECT RPAD('abcdefgh', 0, '12'); -- Result +------+
|      |
+------+ -- An input parameter is NULL. The function returns NULL. SELECT RPAD(NULL, 0, '12'); -- Result +------+
| NULL |
+------+ -- Right-pad to a length of 9 characters. The function returns abcdefgh1. SELECT RPAD('abcdefgh', 9, '12'); -- Result +---------------+
| abcdefgh1     |
+---------------+
```

###### REPLACE

This topic describes how to use the REPLACE string function in MaxCompute to replace matched substrings in a source string with a specified string. This function replaces the exact matches of the OLD string in string a with the NEW string, and returns string a.

```
STRING REPLACE(STRING a, STRING OLD, STRING NEW);
```

a: required. This parameter must be of the STRING type and specifies the source string. OLD: required. This parameter must be of the STRING type and specifies the substring to be replaced. NEW: required. This parameter must be of the STRING type and specifies the replacement string. This function returns a value of the STRING type. If any input parameter is NULL, this function returns NULL.

```
-- Replace matched substrings. SELECT REPLACE('ababab', 'abab', '12'); -- Result +------+
| 12ab |
+------+ -- If OLD does not exist in the source string, the function returns the original stri ng. SELECT REPLACE('ababab', 'cdf', '123'); -- Result +--------+
| ababab |
+--------+ -- If OLD is NULL, the function returns NULL. SELECT REPLACE('123abab456ab', NULL, 'abab'); -- Result +------+
| NULL |
+------+
```

###### SOUNDEX

This topic describes how to use the SOUNDEX string function in MaxCompute to convert a regular string into a SOUNDEX string. This function converts a regular string into a SOUNDEX string.

```
STRING SOUNDEX(STRING a);
```

a: required. This parameter must be of the STRING type. The function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

```
-- Convert a string to a Soundex code. SELECT SOUNDEX('hello'); -- Result +------+
| H400 |
+------+
```

###### SUBSTRING_INDEX

This topic describes how to use the SUBSTRING_INDEX string function in MaxCompute to extract the substring before a specified segment of a string by using a delimiter. This function extracts the substring before the count-th delimiter in string a. If count is positive, the extraction starts from the left. If count is negative, it starts from the right.

```
STRING SUBSTRING_INDEX(STRING a, STRING SEP, INT count);
```

a: required. This parameter must be of the STRING type and specifies the source string. SEP: required. This parameter must be of the STRING type and specifies the delimiter. count: required. This parameter must be of the INT type and specifies the occurrence of the delimiter. The function returns a value of the STRING type. If an input parameter is NULL, the function returns NULL.

```
-- Extract the substring before the second delimiter from the left. The function retu rns https://help.aliyun. SELECT SUBSTRING_INDEX('https://help.aliyun.com', '.', 2); -- Result +----------------------+
| https://help.aliyun  |
+----------------------+ -- Extract the substring after the second delimiter from the right. The function retu rns aliyun.com. SELECT SUBSTRING_INDEX('https://help.aliyun.com', '.', -2); -- Result +------------+
| aliyun.com |
+------------+ -- If the delimiter is NULL, the function returns NULL. SELECT SUBSTRING_INDEX('https://help.aliyun.com', NULL, 2); -- Result +------+
| NULL |
+------+
```

###### TRANSLATE

This topic describes how to use the TRANSLATE string function in MaxCompute to replace specified characters in a string with corresponding characters one by one. This function replace each character in str1 that appears in str2 with the character at the corresponding position in str3.

```
STRING TRANSLATE(STRING|VARCHAR str1, STRING|VARCHAR str2, STRING|VARCHAR str3);
```

str1: required. This parameter must be of the STRING or VARCHAR type and specifies the source string to be replaced. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type, the system returns an error. str2: required. This parameter must be of the STRING or VARCHAR type and specifies the set of characters to be replaced. str3: required. This parameter must be of the STRING or VARCHAR type and specifies the set of target characters for replacement. The function returns a value of the STRING type. If any input parameter is NULL, the function returns NULL.

```
-- Replace each character in 'puter' with the corresponding character in 'pute'. SELECT TRANSLATE('MaxComputer', 'puter', 'pute'); -- Result +--------------+
| MaxCompute   |
+--------------+ -- If characters in str2 do not exist in str1, the function returns the original stri ng. SELECT TRANSLATE('aaa', 'b', 'c'); -- Result +------+
| aaa  |
+------+ -- If str3 is NULL, the function returns NULL. SELECT TRANSLATE('MaxComputer', 'puter', NULL); -- Result +------+
| NULL |
+------+
```

###### URL_ENCODE

This topic describes how to use the URL_ENCODE string function in MaxCompute to encode an input string into the application/x-www-form-urlencoded MIME format. This function encodes an input string into the application/x-www-form-urlencoded MIME format. Letters a through z and A through Z remain unchanged. Periods (.), hyphens (-), asterisks (*), and underscores (_) also remain unchanged. The function converts spaces to plus signs (+). For all other characters, the function converts them to byte values based on the specified encoding format and then represents each byte value in the %xy format, where xy is the hexadecimal representation of the character.

```
STRING URL_ENCODE(STRING input[, STRING encoding]);
```

input: required. This parameter must be of the STRING type and specifies the input string. encoding: optional. This parameter must be of the STRING type and specifies the encoding format. Standard encoding formats such as GBK and UTF-8 are supported. If you do not specify this parameter, the default value is UTF-8. The function returns a value of the STRING type. If the input parameter is NULL, the function returns NULL.

```
-- Use the default UTF-8 encoding. SELECT URL_ENCODE('Example for URL_ENCODE:// (fdsf)'); -- Result +----------------------------------------------------+
| %CA%BE%EF%BF%BD%EF%BF%BDfor+URL_ENCODE%3A%2F%2F+%28fdsf%29 |
+----------------------------------------------------+ -- Specify GBK encoding. SELECT URL_ENCODE('Example for URL_ENCODE:// dsf(fasfs)', 'GBK'); -- Result +---------------------------------------------------+
| Example+for+URL_ENCODE%3A%2F%2F+dsf%28fasfs%29    |
+---------------------------------------------------+
```

###### URL_DECODE

This topic describes how to use the URL_DECODE string function in MaxCompute to convert a URL-encoded string to a regular string, which is the reverse process of URL_ENCODE. This function converts an input string from the application/x-www-form-urlencoded MIME format to a regular string, which is the reverse process of URL_ENCODE. Characters a through z and A through Z remain unchanged. Periods (.), hyphens (-), asterisks (*), and underscores (_) remain unchanged. Plus signs (+) are converted to spaces. The function first performs percent-decoding, converting %xy sequences into their corresponding byte values. Then, it decodes continuous byte values into a string based on the encoding format specified by the second parameter. All other characters remain unchanged. The final return value is a UTF-8 encoded string.

```
STRING URL_DECODE(STRING input[, STRING encoding]);
```

input: required. This parameter must be of the STRING type and specifies the input string. encoding: optional. This parameter must be of the STRING type and specifies the encoding format. Standard encoding formats such as GBK and UTF-8 are supported. If you do not specify this parameter, the default value is UTF-8. The return value is of the STRING type. If the input parameter is NULL, the function returns NULL.

```
-- Decode the string by using the default UTF-8 encoding. SELECT URL_DECODE('%E7%A4%BA%E4%BE%8Bfor+url_decode%3A%2F%2F+%28fdsf%29'); -- Result +--------------------------------+
| 示例for url_decode:// (fdsf)   |
+--------------------------------+ -- Decode the string by using GBK encoding. SELECT URL_DECODE('Example+for+url_decode+%3A%2F%2F+dsf%28fasfs%29', 'GBK'); -- Result +---------------------------------------+
| Example for url_decode :// dsf(fasfs) |
+---------------------------------------+
```

###### JSON_TUPLE

This topic describes how to use the JSON_TUPLE string function in MaxCompute to extract strings from a standard JSON string based on a set of keys. This function extracts the strings specified by a set of keys (key1, key2, ...) from a standard JSON string.

```
STRING JSON_TUPLE(STRING json, STRING key1, STRING key2, ...);
```

json: required. The value is of the STRING type and must be a standard JSON string. key: required. The value is of the STRING type and specifies a path in the JSON string. You can specify multiple keys at a time. A key must not start with a dollar sign ($). The function returns a value of the STRING type. If the JSON string is empty or in an invalid JSON Format, the function returns NULL. If a key is empty or invalid (does not exist in the JSON string), the function returns NULL. If the JSON string is valid and the key exists, the function returns the corresponding string. The function supports parsing of JSON data that contains Chinese characters, multi-level nested JSON data, and JSON data that contains multi-level nested arrays. The parsing behavior is consistent with the behavior of GET_JSON_OBJECT after you

```
set SET odps.sql.udf.getjsonobj.new=true; .
```

When you need to parse the same JSON string multiple times, JSON_TUPLE provides higher efficiency than multiple calls to GET_JSON_OBJECT because JSON_TUPLE accepts multiple keys at a time and parses the JSON string only once. JSON_TUPLE is a UDTF. When you need to select other columns, it must be used with LATERAL VIEW.

```
-- Assume that the school table contains the following data. CREATE TABLE school (Id BIGINT, json STRING); INSERT INTO school VALUES (1, '{"School Name":"Lake University","Address":"Hangzhou","SchoolRank":"00","Class1":{"Student": [{"studentId":1,"scoreRankIn3Year":[1,2,[3,2,6]]},{"studentId":2,"scoreRankIn3Year":[ 2,3,[4,3,1]]}]}}'); -- Extract information from the JSON object. SELECT JSON_TUPLE(school.json, "SchoolRank", "Class1") AS (item0, item1) FROM school; -- This statement is equivalent to the following statement. SELECT GET_JSON_OBJECT(school.json, "$.SchoolRank") item0, GET_JSON_OBJECT(school.json, "$.Class1") item1 FROM school; -- Result +-------+------------------------------------------------------------------------------ -----------------------------+
| item0 | item1
```

|

```json
+-------+------------------------------------------------------------------------------ -----------------------------+
| 00    | {"Student":[{"studentId":1,"scoreRankIn3Year":[1,2,[3,2,6]]},
{"studentId":2,"scoreRankIn3Year":[2,3,[4,3,1]]}]} | +-------+------------------------------------------------------------------------------ -----------------------------+ -- Parse JSON data that contains Chinese characters. SELECT JSON_TUPLE(school.json, "School Name", "Address") AS (item0, item1) FROM schoo
```

l;

```
-- Result +----------+--------+
| item0    | item1  |
+----------+--------+
| Lake University | Hangzhou   |
+----------+--------+ -- Parse multi-level nested JSON data. SELECT sc.Id, q.item0, q.item1 FROM school sc LATERAL VIEW JSON_TUPLE(sc.json, "Class1.Student.[*].studentId", "Clas s1.Student.[0].scoreRankIn3Year") q AS item0, item1; -- Result +------+-------+------------------+
| Id   | item0 | item1            |
+------+-------+------------------+
| 1    | [1,2] | [1,2,[3,2,6]]    |
+------+-------+------------------+ -- Parse JSON data that contains multi-level nested arrays. SELECT sc.Id, q.item0, q.item1 FROM school sc LATERAL VIEW JSON_TUPLE(sc.json, "Class1Student[0]scoreRankIn3Year[2]" "Class1Student[0]scoreRankIn3Year[2][1]")
```

```
"Class1.Student[0].scoreRankIn3Year[2]", "Class1.Student[0].scoreRankIn3Year[2][1]") q AS item0, item1; -- Result +------+---------+-------+
| Id   | item0   | item1 |
+------+---------+-------+
| 1    | [3,2,6] | 2     |
+------+---------+-------+
```

###### FROM_JSON

This topic describes how to use the FROM_JSON string function in MaxCompute to return an object of the ARRAY, MAP, or STRUCT type based on a JSON string and schema information. This function returns an object of the ARRAY, MAP, or STRUCT type based on the specified JSON string and schema information.

```
FROM_JSON(STRING jsonStr, STRING schema);
```

jsonStr: required. This parameter must be of the STRING type and specifies the input JSON string. schema: required. This parameter must be of the STRING type and specifies the data structure. The syntax is the same as that used in CREATE TABLE statements. Examples:

| array<bigint> | , | map<string, array<string>> |
|---|---|---|

`c:map<string,string>>` . The STRUCT type also supports the syntax `'a INT, b DOUBLE'` , which is equivalent to `struct<a:int, b:double>` . The following table lists the mappings between JSON types and MaxCompute types.

| JSON | MaxCompute |
|---|---|
| Object | STRUCT/MAP/STRING |
| Array | ARRAY/STRING |
| Number | TINYINT/SMALLINT/IBT/BIGINT/FLOAT/DOUBLE/DECIMAL/STRING |
| true/false | BOOLEAN/STRING |
| String | STRING |
| null | All types |

**Note**

For the Object and Array types, the function parses as many elements as possible and ignores elements of mismatched types. The function returns a value of the ARRAY, MAP, or STRUCT type. If the schema is empty, an error is returned.

```
-- Parse a JSON object into the STRUCT type. SELECT FROM_JSON('{"a":1, "b":0.8}', 'a INT, b DOUBLE'); -- Result +--------------------------+
| {"a":1, "b":0.8}         |
+--------------------------+ -- Parse a JSON object that contains a string value. SELECT FROM_JSON('{"time":"26/08/2015"}', 'time STRING'); -- Result +-----------------------------+
| {"time":"26/08/2015"}       |
+-----------------------------+ -- If the schema contains a field that does not exist in the JSON object, the functio n returns NULL for that field. SELECT FROM_JSON('{"a":1, "b":0.8}', 'a INT, b DOUBLE, c STRING'); -- Result +---------------------------------+
| {"a":1, "b":0.8, "c":NULL}      |
+---------------------------------+ -- Parse a JSON array into the ARRAY type. SELECT FROM_JSON('[1, 2, 3, "a"]', 'ARRAY<BIGINT>'); -- Result +--------------+
| [1, 2, 3]    |
+--------------+
```

###### TO_JSON

This topic describes how to use the TO_JSON string function in MaxCompute. This function converts a given data type to a JSON string.

```
TO_JSON(expr);
```

expr: required. This parameter must be of the ARRAY, MAP, or STRUCT type. This function returns a string in JSON format.

```
SELECT TO_JSON(named_struct('a', 1, 'b', 2)); -- Result +---------------+
|      _c0      |
+---------------+
| {"a":1,"b":2} |
+---------------+ SELECT TO_JSON(named_struct('time', "26/08/2015")); -- Result +-------------------------+
|           _c0           |
+-------------------------+
|  {"time":"26/08/2015"}  |
+-------------------------+ SELECT TO_JSON(array(named_struct('a', 1, 'b', 2))); -- Result +-----------------+
|       _c0       |
+-----------------+
| [{"a":1,"b":2}] |
+-----------------+ SELECT TO_JSON(map('a', named_struct('b', 1))); -- Result +---------------+
|      _c0      |
+---------------+
| {"a":{"b":1}} |
+---------------+ SELECT TO_JSON(map('a', 1)); -- Result +---------+
|   _c0   |
+---------+
| {"a":1} |
+---------+ SELECT TO_JSON(array((map('a', 1)))); -- Result +-----------+
|    _c0    |
+-----------+
| [{"a":1}] |
+-----------+
```

#### Date functions

##### DATEADD

This topic describes how to use the DATEADD date function in MaxCompute to modify a date value based on a specified datepart and delta. This function modifies a date value based on a specified datepart and delta.

```
DATETIME DATEADD(DATETIME date, BIGINT delta, STRING datepart);
```

date: This parameter specifies the date value of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, the function implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, an error is returned. delta: This parameter must be of the BIGINT type and specifies the modification magnitude. If the input value is of the STRING or DOUBLE type, the function implicitly converts it to the BIGINT type before calculation. If the input value is of any other data type, an error is returned. If delta is greater than 0, the function adds the value. Otherwise, it subtracts the value.

**Note**

When you add or subtract delta by the specified unit, carry-over or borrow may occur to higher units. Years, months, hours, and minutes and seconds use base-10, base-12, base-24, and base-60 calculations, respectively. When the unit of delta is month, if adding delta to the month part of the DATETIME value does not cause the day to overflow, the day value remains unchanged. Otherwise, the function sets the day value to the last day of the resulting month. datepart: This parameter must be a STRING constant and specifies the datepartfor modification. If the value is a non-constant, an unsupported format, or any other type, an error is returned. The valid values for this parameter follow the conventions for converting between the STRING and DATETIME types (such as, yyyy for year and mm for month). Extended date formats are also supported, including year, month or mon, day, and hour. For more information about the conversion rules, see Conversions between the STRING and DATETIME types. The return value is of the DATETIME type. If any input parameter is NULL, the function returns NULL. Example 1: common usage of DATEADD.

```
-- Add 1 day SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 1, 'dd'); -- Result: The result exceeds the last day of February in that year, so the actual value is the first day of the next month. +---------------------+
| _c0                 |
+---------------------+
| 2005-03-01 00:00:00 |
+---------------------+ -- Subtract 1 day SELECT DATEADD(DATETIME '2005-02-28 00:00:00', -1, 'dd'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2005-02-27 00:00:00 |
+---------------------+ -- Add 20 months SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 20, 'mm'); -- Result: The month overflows, so the year increases by 1. +---------------------+
| _c0                 |
+---------------------+
| 2006-10-28 00:00:00 |
+---------------------+ -- Add 1 month SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 1, 'mm'); -- Result: +---------------------+
| _c0                 |
+---------------------+
| 2005-03-28 00:00:00 |
+---------------------+ SELECT DATEADD(DATETIME '2005-01-29 00:00:00', 1, 'mm'); -- Result: February 2005 does not have a 29th day, so the date is truncated to the last day of that month. +---------------------+
| _c0                 |
+---------------------+
| 2005-02-28 00:00:00 |
+---------------------+ -- Subtract 1 month SELECT DATEADD(DATETIME '2005-03-30 00:00:00', -1, 'mm'); -- Result: February 2005 does not have a 30th day, so the date is truncated to the last day of that month. +---------------------+
| _c0                 |
+---------------------+
| 2005-02-28 00:00:00 |
+---------------------+
```

Example 2: DATETIME represented as a constant.

```
SELECT DATEADD(DATETIME '2005-03-30 00:00:00', -1, 'mm'); -- In MaxCompute SQL, the DATETIME type does not have a direct constant representat ion. This is an incorrect usage. SELECT DATEADD(CAST("2005-03-30 00:00:00" AS DATETIME), -1, 'mm'); -- To specify a DATETIME constant, you must explicitly cast a STRING constant to th e DATETIME type.
```

##### DATEDIFF

This topic describes how to use the DATEDIFF date function in MaxCompute to calculate the difference between two dates in a specified datepart. This function calculates the difference between `date1` and `date2` in the specified

```
 datepart .
```

If the precision of the input dates is higher than `datepart` , the system discards the more precise parts. For example, if `datepart` specifies days, the system discards hours, minutes, and seconds. The system truncates the lower-unit parts based on `datepart` before calculating the result. The lower-unit parts refer to the discarded parts described above.

```
BIGINT DATEDIFF(DATETIME date1, DATETIME date2, STRING datepart);
```

`date1` and `date2` : the minuend and subtrahend. The value must be of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. An error is returned if the input value is of any other data type. `datepart` : the time unit. The value must be a STRING constant. Extended date formats are supported. An error is returned if `datepart` does not conform to the specified format or is of any other data type. The function returns a value of the BIGINT type. If any input parameter is NULL, the function returns NULL. If `date1` is earlier than `date2` , the function returns a negative value.

```
-- Assume that start='2005-12-31 23:59:59' and end='2006-01-01 00:00:00'. SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'dd')
```

;

```
-- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+
```

```
SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'mm')
```

;

```
-- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'yyyy '); -- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'hh')
```

;

```
-- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'mi')
```

;

```
-- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'ss')
```

;

```
-- Result +--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2013-05-31 13:00:00', TO_DATE('2013-05-31 12:30:00', 'yyyymm-dd hh:mi:ss'), 'ss'); -- Result +--------+
| _c0    |
+--------+
| 1800   |
+--------+
```

```
SELECT DATEDIFF(DATETIME '2013-05-31 13:00:00', TO_DATE('2013-05-31 12:30:00', 'yyyymm-dd hh:mi:ss'), 'mi'); -- Result +--------+
| _c0    |
+--------+
| 30     |
+--------+ -- Assume that start='2018-06-04 19:33:23.234' and end='2018-06-04 19:33:23.250'. Dat es with milliseconds do not conform to the standard DATETIME format and cannot be imp licitly converted. You must explicitly convert them. SELECT DATEDIFF(TO_DATE('2018-06-04 19:33:23.250', 'yyyy-MM-dd hh:mi:ss.ff3'), TO_DAT E('2018-06-04 19:33:23.234', 'yyyy-MM-dd hh:mi:ss.ff3'), 'ff3'); -- Result +--------+
| _c0    |
+--------+
| 16     |
+--------+
```

##### DATEPART

This topic describes how to use the DATEPART date function in MaxCompute to extract a value from a date based on a specified datepart. This function extracts a value from `date` based on the specified `datepart` .

```
BIGINT DATEPART(DATETIME date, STRING datepart);
```

`date` : This parameter must be of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, the system returns an error. `datepart` : This parameter must be a STRING constant. Extended date formats are supported. If `datepart` does not match the specified format or data type, the system returns an error. The function returns a value of the BIGINT type. If any input parameter is NULL, the function returns NULL.

```
SELECT DATEPART(TO_DATE('2017-06-08 01:10:00', 'yyyy-mm-dd hh:mi:ss'), 'yyyy'); -- Result +--------+
| _c0    |
+--------+
| 2017   |
+--------+ SELECT DATEPART(TO_DATE('2017-06-08 01:10:00', 'yyyy-mm-dd hh:mi:ss'), 'mm'); -- Result +--------+
| _c0    |
+--------+
| 6      |
+--------+
```

##### DATETRUNC

This topic describes how to use the DATETRUNC date function in MaxCompute to truncate a date to a specified datepart and return the resulting date value. This function returns the date value after the specified datepart has been truncated from a date.

```
DATETIME DATETRUNC(DATETIME date, STRING datepart);
```

date: The value must be of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, the system returns an error. datepart: a constant of the STRING type. Extended date formats are supported. If the value of datepart does not conform to the specified format or data type, the system returns an error. This function returns a value of the DATETIME type. If any input parameter is NULL, the function returns NULL.

```
-- Return the date value truncated to the specified time unit yyyy. In this example, the date is truncated to yyyy=2017. SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'yyyy'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-01-01 00:00:00 |
+---------------------+ -- Return the date value truncated to the specified time unit month. In this example, the date is truncated to month=12. SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'month'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-12-01 00:00:00 |
+---------------------+ -- Return the date value truncated to the specified time unit DD. In this example, th e date is truncated to DD=7. SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'DD'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-12-07 00:00:00 |
+---------------------+
```

##### GETDATE

This topic describes how to use the GETDATE date function in MaxCompute to obtain the current system time. This function obtains the current system time. MaxCompute uses UTC+8 as its standard time zone.

```
DATETIME GETDATE();
```

None. This function returns the current date and time. The return value is of the DATETIME type.

**Note**

In a MaxCompute SQL task that runs in a distributed manner, GETDATE returns a fixed value, which is a random time during the execution of the task. The time is accurate to seconds, or to milliseconds if the new data type 2.0 is enabled.

```
SELECT GETDATE(); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2026-06-26 09:39:59 |
+---------------------+
```

##### ISDATE

This topic describes how to use the ISDATE date function in MaxCompute to determine whether a date string can be converted to a date value based on a format string. This function checks whether a date string can be converted to a date value based on the specified format string. If the conversion succeeds, the function returns `true` . Otherwise, it returns `false` .

```
BOOLEAN ISDATE(STRING date, STRING format);
```

date: the date string, which is of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the function implicitly converts it to the STRING type before calculation. If the input value is of any other data type, an error is returned. format: a format string constant of the STRING type. Extended date formats are not supported. If the input value is of any other data type, an error is returned. If the format string contains duplicate format patterns, the function uses only the date value that corresponds to the first pattern and treats the remaining patterns as delimiters. For example, ISDATE("1234-yyyy", "yyyy-yyyy") returns `true` . The return value is of the BOOLEAN type. If any input parameter is NULL, the function returns NULL.

```
SELECT ISDATE('2023-01-15', 'yyyy-MM-dd'); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ISDATE('2023-13-15', 'yyyy-MM-dd'); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### LASTDAY

This topic describes how to use the LASTDAY date function in MaxCompute to obtain the last day of the month for a given date. This function returns the last day of the month for the specified date. The result is truncated to the day, with the time portion set to 00:00:00.

```
DATETIME LASTDAY(DATETIME date)
```

date: the DATETIME type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, the system returns an error. This function returns a DATETIME value. If the input parameter is NULL, the function returns NULL.

```
SELECT LASTDAY(DATETIME '2023-02-15 10:30:45'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2023-02-28 00:00:00 |
+---------------------+ SELECT LASTDAY(DATETIME '2024-02-15 10:30:45'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2024-02-29 00:00:00 |
+---------------------+
```

##### TO_DATE

This topic describes how to use the TO_DATE date function in MaxCompute to convert a string in a specified format into a date value. This function converts a string in a specified format into a date value.

```
DATETIME TO_DATE(STRING date, STRING format);
```

date: The value of this parameter must be of the STRING type. It specifies the date value to be converted. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, the system implicitly converts it to the STRING type before calculation. If the input value is of any other type or is an empty string, an error is returned. format: a constant of the STRING type. This parameter specifies the date format. An error is returned if the value is not a constant or is of another type. The function does not support extended date formats and ignores other characters during parsing. The parameter must contain at least yyyy. Otherwise, an error is returned. If redundant format strings exist, the function uses only the date value that corresponds to the first format string and treats the remaining strings as delimiters. For example,

```
 TO_DATE('1234-2234 ', 'yyyy-yyyy ')  returns  1234-01-01 00:00:00 .
```

The function returns a value of the DATETIME type in the `yyyy-mm-dd hh:mi:ss:ff3` format. If any input parameter is NULL, the function returns NULL.

**Note**

yyyy represents a 4-digit year, mm represents a 2-digit month, and dd represents a 2digit day. hh represents the hour in 24-hour format, mi represents a 2-digit minute, and ss represents a 2-digit second. ff3 represents milliseconds with a precision of 3 digits.

```
SELECT TO_DATE('Alibaba2017-12*03', 'Alibabayyyy-mm*dd'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-12-03 00:00:00 |
+---------------------+ SELECT TO_DATE('20170718', 'yyyymmdd'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-07-18 00:00:00 |
+---------------------+ SELECT TO_DATE('201707182030', 'yyyymmddhhmi'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-07-18 20:30:00 |
+---------------------+ SELECT TO_DATE('2017718', 'yyyymmdd'); -- Result (format mismatch, returns NULL) +------+
| _c0  |
+------+
| NULL |
+------+ SELECT TO_DATE('Alibaba2017-12*3', 'Alibabayyyy-mm*dd'); -- Result (format mismatch, returns NULL) +------+
| _c0  |
+------+
| NULL |
+------+ SELECT TO_DATE('2017-24-01', 'yyyy'); -- Result (format mismatch, returns NULL) +------+
| _c0  |
+------+
| NULL |
```

`+` `+`

```
+------+ SELECT TO_DATE('20181030 15-13-12.345', 'yyyymmdd hh-mi-ss.ff3'); -- Result +--------------------------+
| _c0                      |
+--------------------------+
| 2018-10-30 15:13:12.000  |
+--------------------------+
```

##### TO_CHAR

This topic describes how to use the TO_CHAR date function in MaxCompute to convert a date value into a string based on a specified format. The function converts a date value into a string based on the specified format.

```
STRING TO_CHAR(DATETIME date, STRING format);
```

date: a DATETIME value to be converted. If the input value is of the STRING type, the function implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, the function returns an error. format: a constant of the STRING type. If the value is not a constant or is of another data type, the function returns an error. The function replaces the date format elements in the format string with the corresponding data values and outputs all other characters as-is. The function returns a value of the STRING type. If any input parameter is NULL, the function returns NULL.

```
SELECT TO_CHAR(TO_DATE('2017-12-03 00:00:00', 'yyyy-mm-dd hh:mi:ss'), 'Alibaba Cloud Financial Services yyyy-mm*dd'); -- Result +--------------------+
| _c0                |
+--------------------+
| Alibaba Cloud Financial Services 2017-12*03 |
+--------------------+ SELECT TO_CHAR(TO_DATE('2017-07-18 00:00:00', 'yyyy-mm-dd hh:mi:ss'), 'yyyymmdd'); -- Result +----------+
| _c0      |
+----------+
| 20170718 |
+----------+ -- The following examples use invalid formats and return errors. SELECT TO_CHAR('Alibaba 2017-12*3', 'Alibaba yyyy-mm*dd'); SELECT TO_CHAR('2017-24-01', 'yyyy'); SELECT TO_CHAR('2017718', 'yyyymmdd');
```

##### UNIX_TIMESTAMP

This topic describes how to use the UNIX_TIMESTAMP date function in MaxCompute to convert a date into an integer UNIX timestamp. This function converts a `date` into an integer UNIX timestamp.

```
BIGINT UNIX_TIMESTAMP(DATETIME date)
```

`date` : a date value of the DATETIME type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. If the input value uses any other data type, the system returns an error. When the new data type flag is enabled, implicit conversion fails. In this case, you must use the CAST function for conversion, such as `UNIX_TIMESTAMP(CAST(... AS DATETIME))` . The function returns a value of the BIGINT type, which represents a UNIX timestamp. If the input parameter is NULL, the function returns NULL.

```
SELECT UNIX_TIMESTAMP(DATETIME '2009-03-20 11:11:00'); -- Result +------------+
| _c0        |
+------------+
| 1237518660 |
+------------+
```

##### FROM_UNIXTIME

This topic describes how to use the FROM_UNIXTIME date function in MaxCompute to convert a numeric UNIX timestamp into a date value. This function converts a numeric UNIX timestamp unixtime into a date value.

```
DATETIME FROM_UNIXTIME(BIGINT unixtime)
```

unixtime: a value of the BIGINT type. It represents the number of seconds in a UNIX timestamp. The function returns a date value of the DATETIME type. If the input parameter is NULL, the function returns NULL.

```
SELECT FROM_UNIXTIME(123456789); -- Result +---------------------+
|         _c0         |
+---------------------+
| 1973-11-30 05:33:09 |
+---------------------+
```

##### WEEKDAY

This topic describes how to use the WEEKDAY date function in MaxCompute to return the day of the week for a given date. This function returns the day of the week for the specified date.

```
BIGINT WEEKDAY(DATETIME date);
```

date: a date value of the DATETIME type. If you enter a value of another data type, the system returns an error. The function returns a value of the BIGINT type. If the input parameter is NULL, the function returns NULL. The function treats Monday as the first day of the week and returns 0. The return value increases by 1 for each subsequent day, and the function returns 6 for Sunday.

```
SELECT WEEKDAY(DATETIME '2023-06-26 00:00:00'); -- Return result (Monday) +------+
| _c0  |
+------+
|  0   |
+------+ SELECT WEEKDAY(DATETIME '2023-06-27 00:00:00'); -- Return result (Tuesday) +------+
| _c0  |
+------+
|  1   |
+------+ SELECT WEEKDAY(DATETIME '2023-07-02 00:00:00'); -- Return result (Sunday) +------+
| _c0  |
+------+
|  6   |
+------+
```

##### WEEKOFYEAR

This topic describes how to use the WEEKOFYEAR date function in MaxCompute to return the week number of the year for a given date. This function returns the week number of the year for the specified date. Monday is the first day of each week.

**Note**

If a week spans two years, the year to which the week belongs depends on which year contains the majority of the days in that week (four or more days). If the majority of the days fall in the previous year, the week is the last week of the previous year. If the majority of the days fall in the next year, the week is the first week of the next year.

**Functionsyntax**

```
BIGINT WEEKOFYEAR(DATETIME date)
```

date: a date value of the DATETIME type. If the input value is of the STRING type, the system implicitly converts it to the DATETIME type before calculation. If the input value is of any other data type, an error is returned. The function returns a value of the BIGINT type. If the input parameter is NULL, the function returns NULL.

```
SELECT WEEKOFYEAR(TO_DATE("20141229", "yyyymmdd")); -- Result +------------+
| _c0        |
+------------+
| 1          |
+------------+ -- Although 20141229 belongs to 2014, the majority of the days in that week fall in 2 015. Therefore, the function returns 1, which indicates the first week of 2015. SELECT WEEKOFYEAR(TO_DATE("20141231", "yyyymmdd")); -- Result +------------+
| _c0        |
+------------+
| 1          |
+------------+ SELECT WEEKOFYEAR(TO_DATE("20151229", "yyyymmdd")); -- Result +------------+
| _c0        |
+------------+
| 53         |
+------------+
```

##### Additional date functions

###### Usage notes

This topic describes the settings required for using the newly extended date functions. MaxCompute 2.0 introduces new date functions. To use these new functions in SQL statements, you must add the following SET statement.

```
SET odps.sql.type.system.odps2=true;
```

**Note**

You must submit and run the preceding SET statement and the SQL statements that use the new functions at the same time.

###### YEAR

This topic describes how to use the YEAR date function in MaxCompute to return the year of a given date. This function returns the year of the specified `date` .

```
INT YEAR(DATETIME/STRING date);
```

`date` : a date value of the DATETIME or STRING type. The date format must contain at least yyyy-mm-dd without any extra characters. Otherwise, the function returns NULL. The function returns a value of the INT type.

```
SELECT YEAR('1970-01-01 12:30:00'); -- Result +--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('1970-01-01'); -- Result +--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('70-01-01'); -- Result +--------+
| _c0    |
+--------+
| 70     |
+--------+ SELECT YEAR('1970-01-01'); -- Result +--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('1970/03/09'); -- Result +--------+
| _c0    |
+--------+
| NULL   |
+--------+ SELECT YEAR(NULL); -- Result +--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### QUARTER

This topic describes how to use the QUARTER date function in MaxCompute to return the quarter of a date. This function returns the quarter of a date. The return value ranges from 1 to 4.

```
INT QUARTER(DATETIME/TIMESTAMP/STRING date);
```

date: a date value of the DATETIME, TIMESTAMP, or STRING type. The date format must include at least `yyyy-mm-dd` . The function returns NULL for other data types. The function returns a value of the INT type. If the input parameter is NULL, the function returns NULL.

```
SELECT QUARTER('1970-11-12 10:00:00'); -- Return result +------------+
| _c0        |
+------------+
| 4          |
+------------+ SELECT QUARTER('1970-11-12'); -- Return result +------------+
| _c0        |
+------------+
| 4          |
+------------+
```

###### MONTH

This topic describes how to use the MONTH date function in MaxCompute to return the month of a date. This function returns the month of a date.

```
INT MONTH(DATETIME/STRING date)
```

date: a date value of the DATETIME or STRING type. The date format must include at least yyyy-mm-dd. If the date is of another data type, the system returns an error. The function returns a value of the INT type.

```
SELECT MONTH('2014-09-01'); -- Result +------+
| _c0  |
+------+
| 9    |
+------+ SELECT MONTH('20140901'); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### DAY

This topic describes how to use the DAY date function in MaxCompute to return the day of a date. This function returns the day of a date.

```
INT DAY(DATETIME/STRING date);
```

date: a date value of the DATETIME or STRING type. The format must be yyyy-mm-dd or yyyy-mm-dd hh:mi:ss. The system returns an error for other data types. The function returns a value of the INT type.

```
SELECT DAY('2014-09-01'); -- Result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT DAY('20140901'); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### DAYOFMONTH

This topic describes how to use the DAYOFMONTH date function in MaxCompute to return the day part of a date. This function returns the day part in a date. For example, if you run the `INT` `DAYOFMONTH(2019-10-13)` command for October 13, 2019, the function returns 13.

```
INT DAYOFMONTH(STRING date);
```

date: a date value of the STRING type. The date format must include at least yyyy-mm-dd. If the date is of another data type, an error is returned. The function returns a value of the INT type.

```
SELECT DAYOFMONTH('2019-09-01'); -- Result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT DAYOFMONTH('20190901'); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### HOUR

This topic describes how to use the HOUR date function in MaxCompute to return the hour part of a date. This function returns the hour part of a date.

```
INT HOUR(DATETIME/STRING date);
```

`date` : A date value of the DATETIME or STRING type. The system returns an error if you specify a value of another data type. The function returns a value of the INT type.

```
SELECT HOUR('2014-09-01 12:00:00'); -- Result +--------+
| _c0    |
+--------+
| 12     |
+--------+ SELECT HOUR('12:00:00'); -- Result +--------+
| _c0    |
+--------+
| 12     |
+--------+ SELECT HOUR('20140901120000'); -- Result +--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### MINUTE

This topic describes how to use the MINUTE date function in MaxCompute to return the minute part of a date. The function returns the minute part of a date.

```
INT MINUTE(DATETIME/STRING date);
```

date: a date value of the DATETIME or STRING type. The system returns an error if you specify a value of another data type. The function returns a value of the INT type.

```
SELECT MINUTE('2014-09-01 12:30:00'); -- Result +------------+
| _c0        |
+------------+
| 30         |
+------------+ SELECT MINUTE('12:30:00'); -- Result +------------+
| _c0        |
+------------+
| 30         |
+------------+ SELECT MINUTE('20140901120000'); -- Result +------------+
| _c0        |
+------------+
| NULL       |
+------------+
```

###### SECOND

This topic describes how to use the SECOND date function in MaxCompute to return the second part of a date. The function returns the second part of a date.

```
INT SECOND(DATETIME/STRING date);
```

`date` : a date value of the DATETIME or STRING type. If you specify a value of another data type, the system returns an error. The function returns a value of the INT type.

```
SELECT SECOND('2014-09-01 12:30:45'); -- Result +--------+
| _c0    |
+--------+
| 45     |
+--------+ SELECT SECOND('12:30:45'); -- Result +--------+
| _c0    |
+--------+
| 45     |
+--------+ SELECT SECOND('20140901123045'); -- Result +--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### FROM_UTC_TIMESTAMP

This topic describes how to use the FROM_UTC_TIMESTAMP function in MaxCompute to convert a Coordinated Universal Time (UTC) timestamp to a timestamp in a specified time zone. This function converts a UTC timestamp to a timestamp in a specified time zone.

```
TIMESTAMP FROM_UTC_TIMESTAMP({any primitive type}*, STRING timezone);
```

{any primitive type}*: the timestamp. The data type must be TIMESTAMP, DATETIME, TINYINT, SMALLINT, INT, or BIGINT. If the parameter is of the TINYINT, SMALLINT, INT, or BIGINT type, the unit is milliseconds. timezone: the destination time zone for the conversion, such as PST. The return value must be of the TIMESTAMP type.

```
-- The input parameter is in milliseconds (ms), and the function returns 2017-08-01 0 4:24:00. SELECT FROM_UTC_TIMESTAMP(1501557840000, 'PST'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 2017-08-01 04:24:00 |
+---------------------+ SELECT FROM_UTC_TIMESTAMP(TO_DATE('1970-01-30 16:00:00', 'yyyy-mm-dd hh:mi:ss'), 'PST '); -- Result +-----------------------+
| _c0                   |
+-----------------------+
| 1970-01-30 08:00:00.0 |
+-----------------------+ SELECT FROM_UTC_TIMESTAMP(DATETIME '1970-01-30 00:00:00', 'PST'); -- Result +-----------------------+
| _c0                   |
+-----------------------+
| 1970-01-29 16:00:00.0 |
+-----------------------+
```

###### CURRENT_TIMESTAMP

This topic describes how to use the CURRENT_TIMESTAMP date function in MaxCompute to return a timestamp of the TIMESTAMP type. This function returns the current timestamp of the TIMESTAMP type. The returned value is not fixed.

```
TIMESTAMP CURRENT_TIMESTAMP();
```

None. The function returns a value of the TIMESTAMP type.

```
SELECT CURRENT_TIMESTAMP(); -- Result +-------------------------+
|           _c0           |
+-------------------------+
| 2017-08-03 11:50:30.661 |
+-------------------------+
```

###### ADD_MONTHS

This topic describes how to use the ADD_MONTHS date function in MaxCompute to return a date that results from adding a specified number of months to a start date. This function returns the date that results from adding nummonths months to the start date startdate.

```
STRING ADD_MONTHS(STRING startdate, INT num_months);
```

startdate: a date value of the STRING type. The date format must include at least yyyymm-dd. Otherwise, the function returns NULL. num_months: a numeric value of the INT type. The function returns a date value of the STRING type in the yyyy-mm-dd format.

```
SELECT ADD_MONTHS('2017-02-14', 3); -- Result +------------+
| _c0        |
+------------+
| 2017-05-14 |
+------------+ SELECT ADD_MONTHS('17-2-14', 3); -- Result +------------+
| _c0        |
+------------+
| 0017-05-14 |
+------------+ SELECT ADD_MONTHS('2017-02-14 21:30:00', 3); -- Result +------------+
| _c0        |
+------------+
| 2017-05-14 |
+------------+ SELECT ADD_MONTHS('20170214', 3); -- Result +------+
| _c0  |
+------+
| NULL |
+------+
```

###### LAST_DAY

This topic describes how to use the LAST_DAY date function in MaxCompute to return the last day of the month for a given date. This function returns the last day of the month for a given date.

```
STRING LAST_DAY(STRING date);
```

`date` : a date value of the STRING type. The format is yyyy-mm-dd hh:mi:ss or yyyy-mmdd. The function returns a date value of the STRING type in the yyyy-mm-dd format.

```
SELECT LAST_DAY('2017-03-04'); -- Result +------------+
| _c0        |
+------------+
| 2017-03-31 |
+------------+ SELECT LAST_DAY('2017-07-04 11:40:00'); -- Result +------------+
| _c0        |
+------------+
| 2017-07-31 |
+------------+ SELECT LAST_DAY('20170304'); -- Result +--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### NEXT_DAY

This topic describes how to use the NEXT_DAY date function in MaxCompute to return the first date that is later than the specified date and falls on the specified day of the week. This function returns the first date that is later than the specified startdate and falls on the specified day of the week.

```
STRING NEXT_DAY(STRING startdate, STRING week);
```

startdate: a date value of the STRING type in the yyyy-mm-dd hh:mi:ss or yyyy-mm-dd format. week: a date value of the STRING type. It can be the first 2 or 3 letters of a day of the week, or the full name of the day. Example: MO, TUE, or FRIDAY. The function returns a date value of the STRING type in the yyyy-mm-dd format.

```
SELECT NEXT_DAY('2017-08-01','TU'); -- Return result +------------+
|    _c0     |
+------------+
| 2017-08-08 |
+------------+ SELECT NEXT_DAY('2017-08-01 23:34:00','TU'); -- Return result +------------+
|    _c0     |
+------------+
| 2017-08-08 |
+------------+ SELECT NEXT_DAY('20170801','TU'); -- Return result +------------+
| _c0        |
+------------+
| NULL       |
+------------+
```

###### MONTHS_BETWEEN

This topic describes how to use the MONTHS_BETWEEN function in MaxCompute to return the number of months between date1 and date2. This function returns the number of months between date1 and date2.

```
DOUBLE MONTHS_BETWEEN(DATETIME/TIMESTAMP/STRING date1, DATETIME/TIMESTAMP/STRING date 2);
```

date1: the DATETIME, TIMESTAMP, or STRING type in the `yyyy-mm-dd hh:mi:ss` or `yyyy-mm-dd` format. date2: the DATETIME, TIMESTAMP, or STRING type in the `yyyy-mm-dd hh:mi:ss` or `yyyy-mm-dd` format. The function returns a value of the DOUBLE type. If date1 is later than date2, the function returns a positive value. If date2 is later than date1, the function returns a negative value. If date1 and date2 correspond to the last day of their respective months, the function returns an integer number of months. Otherwise, the function calculates the result by dividing the number of days between date1 and date2 by 31.

```
SELECT MONTHS_BETWEEN('1997-02-28 10:30:00', '1996-10-30'); -- Result +---------------------+
| _c0                 |
+---------------------+
| 3.9495967741935485  |
+---------------------+ SELECT MONTHS_BETWEEN('1996-10-30', '1997-02-28 10:30:00'); -- Result +---------------------+
| _c0                 |
+---------------------+
| -3.9495967741935485 |
+---------------------+ SELECT MONTHS_BETWEEN('1996-09-30', '1996-12-31'); -- Result +------------+
| _c0        |
+------------+
| -3.0       |
+------------+
```

###### EXTRACT

This topic describes how to use the EXTRACT date function in MaxCompute to extract a specified datepart from a date. The function extracts the specified `datepart` unit from the date `timestamp` . If the time value is invalid, such as exceeding the valid range, the function returns the remainder of the out-of-range value divided by the maximum value of the corresponding valid time range.

```
INT EXTRACT(<datepart> FROM <timestamp>);
```

`datepart` : Supported time units include YEAR, MONTH, DAY, HOUR, and MINUTE. `timestamp` : data of the TIMESTAMP type. The function returns a value of the INT type.

```
SET odps.sql.type.system.odps2=true; SELECT EXTRACT(YEAR FROM '2019-05-01 11:21:00') AS year
     , EXTRACT(MONTH FROM '2019-05-01 11:21:00') AS month
     , EXTRACT(DAY FROM '2019-05-01 11:21:00') AS day
     , EXTRACT(HOUR FROM '2019-05-01 11:21:00') AS hour
     , EXTRACT(MINUTE FROM '2019-05-01 11:21:00') AS minute;
-- Result +------+-------+------+------+--------+
| year | month | day  | hour | minute |
+------+-------+------+------+--------+
| 2019 | 5     | 1    | 11   | 21     |
+------+-------+------+------+--------+ SET odps.sql.type.system.odps2=true; SELECT EXTRACT(HOUR FROM '2019-05-01 31:01:01') AS hour
     , EXTRACT(MINUTE FROM '2019-05-01 23:61:01') AS minute;
-- Result +------+--------+
| hour | minute |
+------+--------+
| 7    | 1      |
+------+--------+ -- The maximum valid value for hour is 24. The out-of-range value is 31. The remainde r of 31 divided by 24 is 7. -- The maximum valid value for minute is 60. The out-of-range value is 61. The remain der of 61 divided by 60 is 1.
```

#### Window functions

##### Overview

MaxCompute SQL supports window functions for flexible data analysis and processing. This topic describes the usage notes and syntax for window functions. MaxCompute SQL supports window functions for flexible data analysis and processing.

**Important**

Window functions can appear only in SELECT clauses. You cannot nest window functions or aggregation functions inside a window function. You cannot use a window function together with an aggregation function at the same level. A single MaxCompute SQL statement supports a maximum of five window functions.

```
window_func() OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC| DESC]…]] windowing_clause);
```

PARTITION BY: specifies the columns used for partitioning. Rows with the same values in the partition columns are considered to be in the same window. A single window can contain up to 100 million rows of data. We recommend that you limit the number to no more than 5 million rows. Otherwise, a runtime error occurs. ORDER BY: specifies the sorting order of data within a window. windowing_clause: You can use ROWS to specify the window frame. The following two methods are available: ROWS BETWEEN x PRECEDING|FOLLOWING AND y PRECEDING|FOLLOWING : The window frame spans from x rows before or after the current row to y rows before or after the current row. ROWS x PRECEDING|FOLLOWING : The window frame spans from the x-th row before or after the current row to the current row.

**Note**

x, y: must be integer constants greater than or equal to 0, with a valid range of 0 to 10000. A value of 0 indicates the current row. You must specify ORDER BY before you can use ROWS to define the window frame. The window functions that support specifying the window frame using ROWS include AVG, COUNT, MAX, MIN, STDDEV, and SUM.

##### COUNT

This topic describes how to use the COUNT window function in MaxCompute to calculate the count. This function calculates the count.

```
BIGINT COUNT([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|D ESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. This parameter accepts any data type. If the value is NULL, the system excludes the row from the calculation. If the DISTINCT keyword is specified, the function returns the count of unique values. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the count of expr within the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the cumulative count from the first row to the current row within the window. ORDER BY cannot be used when the DISTINCT keyword is specified. The function returns a value of the BIGINT type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- If you do not specify ORDER BY, the function returns the count of user_id within t he current window. SELECT user_id, COUNT(user_id) OVER (PARTITION BY user_id) AS count FROM test_src; -- Result +------------+------------+
| user_id    | count      |
+------------+------------+
| 1          | 4          |
| 1          | 4          |
| 1          | 4          |
| 1          | 4          |
| 2          | 2          |
| 2          | 2          |
| 3          | 2          |
| 3          | 2          |
+------------+------------+ -- If you specify ORDER BY, the function returns the cumulative count from the first row to the current row within the window. SET odps.sql.hive.compatible=false; SELECT user_id, COUNT(user_id) OVER (PARTITION BY user_id ORDER BY user_id) AS count FROM test_src; -- Result +------------+------------+
| user_id    | count      |
+------------+------------+
| 1          | 1          | -- The window starts from this row.
| 1          | 2          | -- Two records exist up to the current row. The function r
eturns 2.
| 1          | 3          |
| 1          | 4          |
| 2          | 1          |
| 2          | 2          |
| 3          | 1          |
| 3          | 2          |
+------------+------------+
```

```
-- Non-Hive-compatible mode: if the ORDER BY values are duplicated, the function retu rns the COUNT for each individual row. SET odps.sql.hive.compatible=false; SELECT user_id, price, COUNT(price) OVER (PARTITION BY user_id ORDER BY price) AS cou nt FROM test_src; -- Result +---------+-------+-------+
| user_id | price | count |
+---------+-------+-------+
| 1       | 4.5   | 1     | -- The first row of the window.
| 1       | 5.5   | 2     | -- The count for the second row is 2.
| 1       | 5.5   | 3     | -- The count for the third row is 3.
| 1       | 6.5   | 4     |
| 2       | NULL  | 0     |
| 2       | 3.0   | 1     |
| 3       | NULL  | 0     |
| 3       | 4.0   | 1     |
+---------+-------+-------+ -- Hive-compatible mode: if the ORDER BY values are duplicated, the function returns the COUNT of the last row that shares the same value. SET odps.sql.hive.compatible=true; SELECT user_id, price, COUNT(price) OVER (PARTITION BY user_id ORDER BY price) AS cou nt FROM test_src; -- Result +---------+-------+-------+
| user_id | price | count |
+---------+-------+-------+
| 1       | 4.5   | 1     | -- The first row of the window.
| 1       | 5.5   | 3     | -- The second and third rows have the same price value. T
he count for the second row equals the count for the third row.
| 1       | 5.5   | 3     | -- The count for the third row is 3.
| 1       | 6.5   | 4     |
| 2       | NULL  | 0     |
| 2       | 3.0   | 1     |
| 3       | NULL  | 0     |
| 3       | 4.0   | 1     |
+---------+-------+-------+
```

##### AVG

This topic describes how to use the AVG window function in MaxCompute to calculate the average value. This function calculates the average value.

```
DOUBLE AVG([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DES C], col2 [ASC|DESC]…]] [windowing_clause]);
```

expr: Required. This parameter must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other data type, an error is returned. If the value is NULL, the system excludes the row from calculation. BOOLEAN values are not allowed in the calculation. If the DISTINCT keyword is specified, the function calculates the average of distinct values. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the average of all values within the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the cumulative average from the first row to the current row within the window. ORDER BY cannot be used when the DISTINCT keyword is specified. The function returns a value of the DOUBLE type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Non-Hive-compatible mode: When ORDER BY values are duplicated, the function return s the AVG for each individual row. SET odps.sql.hive.compatible=false; SELECT user_id, price, AVG(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Result +---------+-------+---------------------+
| user_id | price | _c2                 |
+---------+-------+---------------------+
| 1       | 4.5   | 4.5                 | -- First row of the window.
| 1       | 5.5   | 5.0                 | -- AVG from row 1 to row 2.
| 1       | 5.5   | 5.166666666666667   | -- AVG from row 1 to row 3.
| 1       | 6.5   | 5.5                 |
| 2       | NULL  | NULL                |
| 2       | 3.0   | 3.0                 |
| 3       | NULL  | NULL                |
| 3       | 4.0   | 4.0                 |
+---------+-------+---------------------+ -- Hive-compatible mode: When ORDER BY values are duplicated, the function returns th e AVG of the last row with the same value. SET odps.sql.hive.compatible=true; SELECT user_id, price, AVG(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Result +---------+-------+---------------------+
| user_id | price | _c2                 |
+---------+-------+---------------------+
| 1       | 4.5   | 4.5                 | -- First row of the window.
| 1       | 5.5   | 5.166666666666667   | -- AVG from row 1 to row 3.
| 1       | 5.5   | 5.166666666666667   | -- AVG from row 1 to row 3.
| 1       | 6.5   | 5.5                 |
| 2       | NULL  | NULL                |
| 2       | 3.0   | 3.0                 |
| 3       | NULL  | NULL                |
| 3       | 4.0   | 4.0                 |
+---------+-------+---------------------+
```

##### MAX

This topic describes how to use the MAX window function in MaxCompute to calculate the maximum value. This function calculates the maximum value.

```
MAX([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. This parameter accepts any data type except BOOLEAN. If the value is NULL, the system excludes the row from the calculation. If the DISTINCT keyword is specified, the function returns the maximum value among unique values. Specifying this keyword does not affect the result. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the maximum value in the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the maximum value from the start row to the current row within the current window. ORDER BY cannot be used when the DISTINCT keyword is specified. The return value has the same data type as expr.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Do not specify ORDER BY to return the maximum value in the window. SELECT user_id, price, MAX(price) OVER (PARTITION BY user_id) FROM test_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 6.5  |
| 1       | 5.5   | 6.5  |
| 1       | 5.5   | 6.5  |
| 1       | 6.5   | 6.5  |
| 2       | NULL  | 3.0  |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | 4.0  |
| 3       | 4.0   | 4.0  |
+---------+-------+------+ -- Specify ORDER BY to return the cumulative maximum value from the start row to the current row. SELECT user_id, price, MAX(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 4.5  |
| 1       | 5.5   | 5.5  |
| 1       | 5.5   | 5.5  |
| 1       | 6.5   | 6.5  |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

##### MIN

This topic describes how to use the MIN window function in MaxCompute to calculate the minimum value. This function calculates the minimum value.

```
MIN([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. This parameter accepts any data type except BOOLEAN. If the value is NULL, the system excludes the row from the calculation. If the DISTINCT keyword is specified, the function calculates the minimum value among distinct values. Specifying this keyword does not affect the result. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the minimum value in the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the minimum value from the first row to the current row in the current window. ORDER BY cannot be used when the DISTINCT keyword is specified. The return value has the same data type as the expr parameter.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Return the minimum value in the window without specifying ORDER BY. SELECT user_id, price, MIN(price) OVER (PARTITION BY user_id) FROM test_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 4.5  |
| 1       | 5.5   | 4.5  |
| 1       | 5.5   | 4.5  |
| 1       | 6.5   | 4.5  |
| 2       | NULL  | 3.0  |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | 4.0  |
| 3       | 4.0   | 4.0  |
+---------+-------+------+ -- Specify ORDER BY to return the cumulative minimum value from the first row to the current row. SELECT user_id, price, MIN(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 4.5  |
| 1       | 5.5   | 4.5  |
| 1       | 5.5   | 4.5  |
| 1       | 6.5   | 4.5  |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

##### MEDIAN

This topic describes how to use the MEDIAN window function in MaxCompute to calculate the median. This function calculates the median.

```
DOUBLE MEDIAN(DOUBLE number1, number2...) OVER (PARTITION BY [col1, col2…]); DECIMAL MEDIAN(DECIMAL number1, number2...) OVER (PARTITION BY [col1, col2…]);
```

number1, number2...: required. These parameters must be numbers of the DOUBLE or DECIMAL type. A minimum of 1 and a maximum of 255 numbers can be specified. If an input value is of the DOUBLE type, the system converts it to a DOUBLE array for calculation by default. If an input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If an input value is of any other data type, an error is returned. If an input value is NULL, the function returns NULL. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. The function returns a value of the DOUBLE or DECIMAL type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Calculate the median within the window. SELECT user_id, price, MEDIAN(price) OVER (PARTITION BY user_id) FROM test_src; -- Return result +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 5.5  |
| 1       | 5.5   | 5.5  |
| 1       | 5.5   | 5.5  |
| 1       | 6.5   | 5.5  |
| 2       | NULL  | 3.0  |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | 4.0  |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

##### STDDEV

This topic describes how to use the STDDEV window function in MaxCompute to calculate the population standard deviation. This function calculates the population standard deviation.

```
DOUBLE STDDEV([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC| DESC], col2 [ASC|DESC]…]] [windowing_clause]); DECIMAL STDDEV([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC
|DESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, an error is returned. If the input value is NULL, the system excludes the row from the calculation. If the DISTINCT keyword is specified, the function calculates the population standard deviation of distinct values. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the population standard deviation within the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the population standard deviation from the first row to the current row within the window. ORDER BY cannot be used when the DISTINCT keyword is specified. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. Otherwise, the function returns a value of the DOUBLE type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Non-Hive-compatible mode: When ORDER BY values are duplicated, the function return s the STDDEV for each individual row. SET odps.sql.hive.compatible=false; SELECT user_id, price, STDDEV(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src; -- Results +---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.0                  | -- First row of the window.
| 1       | 5.5   | 0.5                  | -- STDDEV from row 1 to row 2.
| 1       | 5.5   | 0.4714045207910316   | -- STDDEV from row 1 to row 3.
| 1       | 6.5   | 0.7071067811865475   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | 0.0                  |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | 0.0                  |
+---------+-------+----------------------+ -- Hive-compatible mode: When ORDER BY values are duplicated, the function returns th e STDDEV of the last row among the identical values. SET odps.sql.hive.compatible=true; SELECT user_id, price, STDDEV(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src; -- Results +---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.0                  | -- First row of the window.
| 1       | 5.5   | 0.4714045207910316   | -- STDDEV from row 1 to row 3.
| 1       | 5.5   | 0.4714045207910316   | -- STDDEV from row 1 to row 3.
| 1       | 6.5   | 0.7071067811865475   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | 0.0                  |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | 0.0                  |
+---------+-------+----------------------+
```

##### STDDEV_SAMP

This topic describes how to use the STDDEV_SAMP window function in MaxCompute to calculate the sample standard deviation. This function calculates the sample standard deviation.

```
DOUBLE STDDEV_SAMP([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]] [windowing_clause]); DECIMAL STDDEV_SAMP([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. The data type is DOUBLE or DECIMAL. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, an error is returned. If the input value is NULL, the system excludes the row from the calculation. If the DISTINCT keyword is specified, the function calculates the sample standard deviation of distinct values. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the sample standard deviation within the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the cumulative sample standard deviation from the first row to the current row within the window. ORDER BY cannot be used when the DISTINCT keyword is specified. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. Otherwise, the function returns a value of the DOUBLE type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Do not specify ORDER BY. The function returns the sample standard deviation within the window. SELECT user_id, price, STDDEV_SAMP(price) OVER (PARTITION BY user_id) FROM test_src; -- Result +---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.8164965809277259   |
| 1       | 5.5   | 0.8164965809277259   |
| 1       | 5.5   | 0.8164965809277259   |
| 1       | 6.5   | 0.8164965809277259   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | NULL                 |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | NULL                 |
+---------+-------+----------------------+ -- Specify ORDER BY. The function returns the cumulative sample standard deviation fr om the first row to the current row. SELECT user_id, price, STDDEV_SAMP(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src; -- Result +---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.0                  | -- Only one row of data exists. The functio
n cannot calculate the sample standard deviation.
| 1       | 5.5   | 0.7071067811865476   |
| 1       | 5.5   | 0.5773502691896258   |
| 1       | 6.5   | 0.8164965809277259   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | 0.0                  |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | 0.0                  |
+---------+-------+----------------------+
```

##### SUM

This topic describes how to use the SUM window function in MaxCompute to calculate the sum. This function calculates the sum.

```
SUM([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

expr: required. The data type must be of the DOUBLE, DECIMAL, or BIGINT type. If the input value is of the STRING type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, the system returns an error. If the input value is NULL, the system skips the row in the calculation. If the DISTINCT keyword is specified, the function calculates the sum of distinct values. PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: If ORDER BY is not specified, the function returns the sum of expr within the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the cumulative sum from the first row to the current row within the window. ORDER BY cannot be used when the DISTINCT keyword is specified. If the input value is of the BIGINT type, the function returns a value of the BIGINT type. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. If the input value is of the DOUBLE or STRING type, the function returns a value of the DOUBLE type.

```
-- Create a test table and insert data. CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Non-Hive-compatible mode: when ORDER BY values are duplicated, the function return s the SUM for each individual row. SET odps.sql.hive.compatible=false; SELECT user_id, price, SUM(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 4.5  | -- First row of the window.
| 1       | 5.5   | 10.0 | -- SUM from row 1 to row 2.
| 1       | 5.5   | 15.5 | -- SUM from row 1 to row 3.
| 1       | 6.5   | 22.0 |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+ -- Hive-compatible mode: when ORDER BY values are duplicated, the function returns th e SUM of the last row that shares the same value. SET odps.sql.hive.compatible=true; SELECT user_id, price, SUM(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src; -- Results +---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
| 1       | 4.5   | 4.5  | -- First row of the window.
| 1       | 5.5   | 15.5 | -- SUM from row 1 to row 3.
| 1       | 5.5   | 15.5 | -- SUM from row 1 to row 3.
| 1       | 6.5   | 22.0 |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

##### DENSE_RANK

This topic describes how to use the DENSE_RANK window function in MaxCompute to calculate consecutive ranks. This function calculates consecutive ranks. Rows with the same values in the ORDER BY columns receive the same rank.

```
BIGINT DENSE_RANK() OVER (PARTITION BY [col1, col2…] ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]);
```

PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: specifies the values used for ranking. This function returns a value of the BIGINT type.

```
-- Create a test table and insert data. CREATE TABLE emp (
  empno BIGINT,
  ename STRING,
  job STRING,
  mgr BIGINT,
  hiredate STRING,
  sal DOUBLE,
  comm DOUBLE,
  deptno BIGINT
```

);

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800, NUL L, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20 00:00:00', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250 , 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17 00:00:00', 5000, NULL, 10);
```

```
INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500 , 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23 00:00:00', 1100, NU LL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950, NUL L, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000, N ULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300, N ULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, '1981-04-12 00:00:00', 5000, N ULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, '1982-07-20 00:00:00', 2450, NU LL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, '1982-12-30 00:00:00', 1300, N ULL, 10); -- Group all employees by department, sort by salary in descending order within each group, and obtain the consecutive rank within each group. -- deptno (department) serves as the partition column, and sal (salary) serves as the ranking basis. SELECT deptno, ename, sal, DENSE_RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS nums FROM emp; -- Result +--------+--------+---------+------+
| deptno | ename  | sal     | nums |
+--------+--------+---------+------+
| 10     | JACCKA | 5000.0  | 1    |
| 10     | KING   | 5000.0  | 1    |
| 10     | CLARK  | 2450.0  | 2    |
| 10     | WELAN  | 2450.0  | 2    |
| 10     | TEBAGE | 1300.0  | 3    |
| 10     | MILLER | 1300.0  | 3    |
| 20     | SCOTT  | 3000.0  | 1    |
| 20     | FORD   | 3000.0  | 1    |
| 20     | JONES  | 2975.0  | 2    |
| 20     | ADAMS  | 1100.0  | 3    |
| 20     | SMITH  | 800.0   | 4    |
| 30     | BLAKE  | 2850.0  | 1    |
| 30     | ALLEN  | 1600.0  | 2    |
| 30     | TURNER | 1500.0  | 3    |
| 30     | MARTIN | 1250.0  | 4    |
| 30     | WARD   | 1250.0  | 4    |
| 30     | JAMES  | 950.0   | 5    |
+--------+--------+---------+------+
```

##### RANK

This topic describes how to use the RANK window function in MaxCompute to calculate ranks. This function calculates ranks. If rows have identical values in the ORDER BY columns, the function assigns them the same rank and skips the subsequent ranks.

```
BIGINT RANK() OVER (PARTITION BY [col1, col2…] ORDER BY [col1 [ASC|DESC], col2 [ASC|D ESC]…]);
```

PARTITION BY [col1, col2...]: specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]: specifies the values by which to rank the rows. This function returns a value of the BIGINT type.

```
-- Create a test table and insert data. CREATE TABLE emp (
  empno BIGINT,
  ename STRING,
  job STRING,
  mgr BIGINT,
  hiredate STRING,
  sal DOUBLE,
  comm DOUBLE,
  deptno BIGINT
```

);

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800, NUL L, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20 00:00:00', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250 , 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500 , 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23 00:00:00', 1100, NU LL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950, NUL L, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000, N ULL 20);
```

```
ULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300, N ULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, '1981-04-12 00:00:00', 5000, N ULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, '1982-07-20 00:00:00', 2450, NU LL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, '1982-12-30 00:00:00', 1300, N ULL, 10); -- Group all employees by department, sort them in descending order of salary within each group, and obtain the rank within each group. -- Use deptno (department) as the partition column and sal (salary) as the ranking ba sis. SELECT deptno, ename, sal, RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS num s FROM emp; -- Results +--------+--------+---------+------+
| deptno | ename  | sal     | nums |
+--------+--------+---------+------+
| 10     | JACCKA | 5000.0  | 1    |
| 10     | KING   | 5000.0  | 1    |
| 10     | CLARK  | 2450.0  | 3    |
| 10     | WELAN  | 2450.0  | 3    |
| 10     | TEBAGE | 1300.0  | 5    |
| 10     | MILLER | 1300.0  | 5    |
| 20     | SCOTT  | 3000.0  | 1    |
| 20     | FORD   | 3000.0  | 1    |
| 20     | JONES  | 2975.0  | 3    |
| 20     | ADAMS  | 1100.0  | 4    |
| 20     | SMITH  | 800.0   | 5    |
| 30     | BLAKE  | 2850.0  | 1    |
| 30     | ALLEN  | 1600.0  | 2    |
| 30     | TURNER | 1500.0  | 3    |
| 30     | MARTIN | 1250.0  | 4    |
| 30     | WARD   | 1250.0  | 4    |
| 30     | JAMES  | 950.0   | 6    |
+--------+--------+---------+------+
```

##### LAG

This topic describes how to use the LAG window function in MaxCompute to retrieve the value of a preceding row at a specified offset. This function retrieves the value of a row that precedes the current row by a specified offset. For example, if the current row number is rn, the function retrieves the value from the row numbered rn-offset.

```
LAG(expr, BIGINT offset, default) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col 1 [ASC|DESC], col2 [ASC|DESC], ...]]);
```

expr: required. This parameter can be of any data type. offset: required. This parameter must be a BIGINT constant greater than 0. If the input value is of the STRING or DOUBLE type, the system implicitly converts the value to the BIGINT type. default: optional. This parameter must be a constant and defines the default value when the range specified by the offset exceeds the boundary. The default value is NULL. PARTITION BY [col1, col2, ...]: optional. This parameter specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. This parameter specifies the sort order of the returned results. The function returns a value of the same data type as expr.

```
-- Create a table CREATE TABLE IF NOT EXISTS sliding_window (
    window STRING,
    seq BIGINT
```

);

```
-- Insert test data INSERT INTO sliding_window VALUES ('all', 0); INSERT INTO sliding_window VALUES ('all', 1); INSERT INTO sliding_window VALUES ('all', 2); INSERT INTO sliding_window VALUES ('all', 3); INSERT INTO sliding_window VALUES ('all', 4); INSERT INTO sliding_window VALUES ('all', 5); INSERT INTO sliding_window VALUES ('all', 6); INSERT INTO sliding_window VALUES ('all', 7); INSERT INTO sliding_window VALUES ('all', 8); INSERT INTO sliding_window VALUES ('all', 9); -- Retrieve the value of seq+100 from the previous row based on the offset SELECT seq, LAG(seq + 100, 1) OVER (PARTITION BY window ORDER BY seq) AS r FROM slidi ng_window; -- Results +-----+------+
| seq | r    |
+-----+------+
| 0   | NULL |
| 1   | 100  |
| 2   | 101  |
| 3   | 102  |
| 4   | 103  |
| 5   | 104  |
| 6   | 105  |
| 7   | 106  |
| 8   | 107  |
| 9   | 108  |
+-----+------+
```

##### LEAD

This topic describes how to use the LEAD window function in MaxCompute to return the expression value from a subsequent row at a specified offset. The LEAD function returns the value of the expression expr from the offset-th row after the current row towards the end of the partition. The expression expr can be a column, a column operation, or a function operation.

```
LEAD(expr, BIGINT offset, default) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [co l1 [ASC|DESC], col2 [ASC|DESC], ...]]);
```

expr: required. This parameter accepts any data type. offset: required. This parameter must be a BIGINT constant greater than 0. If the input value is of the STRING or DOUBLE type, the system implicitly converts the value to the BIGINT type. default: optional. This parameter must be a constant. It specifies the default value when the offset exceeds the partition boundary. The default value is NULL. PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. This clause specifies the sort order of the results. The return value is of the same data type as expr.

```
-- Create a table CREATE TABLE IF NOT EXISTS emp (
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
```

);

```
-- Insert test data INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950,NULL,30);
```

```
950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10); -- Group all employees by department and calculate the salary offset for each employe
```

`e`

```
SELECT deptno, ename, sal, LEAD(sal, 1) OVER (PARTITION BY deptno ORDER BY sal) AS sa l_new FROM emp; -- Results +--------+--------+------+---------+
| deptno | ename  | sal  | sal_new |
+--------+--------+------+---------+
| 10     | TEBAGE | 1300 | 1300    |
| 10     | MILLER | 1300 | 2450    |
| 10     | CLARK  | 2450 | 2450    |
| 10     | WELAN  | 2450 | 5000    |
| 10     | KING   | 5000 | 5000    |
| 10     | JACCKA | 5000 | NULL    |
| 20     | SMITH  | 800  | 1100    |
| 20     | ADAMS  | 1100 | 2975    |
| 20     | JONES  | 2975 | 3000    |
| 20     | SCOTT  | 3000 | 3000    |
| 20     | FORD   | 3000 | NULL    |
| 30     | JAMES  | 950  | 1250    |
| 30     | MARTIN | 1250 | 1250    |
| 30     | WARD   | 1250 | 1500    |
| 30     | TURNER | 1500 | 1600    |
| 30     | ALLEN  | 1600 | 2850    |
| 30     | BLAKE  | 2850 | NULL    |
+--------+--------+------+---------+
```

##### PERCENT_RANK

This topic describes how to use the PERCENT_RANK window function in MaxCompute to calculate the relative rank of a row within a group of data. This function calculates the relative rank of a row within a group of data.

```
PERCENT_RANK() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [ ASC|DESC], ...]);
```

PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: required. This clause specifies the values used for ranking. The function returns a value of the DOUBLE type within the range of `[0,1]` . The relative rank is calculated by using the formula `(rank-1)/(partition_row_count -`
1. ` .

**Note**

A single window cannot contain more than 10 million rows. `rank` is the return value of the RANK window function for the row, and `partition_row_count` is the total number of rows in the partition to which the row belongs. If the partition contains only one row, the function returns 0.0.

```
-- Create a table. CREATE TABLE IF NOT EXISTS emp (
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
```

);

```
-- Insert test data. INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0
```

`0'`

```
30)
```

```
0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10); -- Calculate the relative rank of employee salaries within each department. SELECT deptno, ename, sal, PERCENT_RANK() OVER (PARTITION BY deptno ORDER BY sal) AS pct_rank FROM emp; -- Return result +--------+--------+------+---------------------+
| deptno | ename  | sal  | pct_rank            |
+--------+--------+------+---------------------+
| 10     | TEBAGE | 1300 | 0.0                 |
| 10     | MILLER | 1300 | 0.0                 |
| 10     | CLARK  | 2450 | 0.4                 |
| 10     | WELAN  | 2450 | 0.4                 |
| 10     | KING   | 5000 | 0.8                 |
| 10     | JACCKA | 5000 | 0.8                 |
| 20     | SMITH  | 800  | 0.0                 |
| 20     | ADAMS  | 1100 | 0.25                |
| 20     | JONES  | 2975 | 0.5                 |
| 20     | SCOTT  | 3000 | 0.75                |
| 20     | FORD   | 3000 | 0.75                |
| 30     | JAMES  | 950  | 0.0                 |
| 30     | MARTIN | 1250 | 0.2                 |
| 30     | WARD   | 1250 | 0.2                 |
| 30     | TURNER | 1500 | 0.6                 |
| 30     | ALLEN  | 1600 | 0.8                 |
| 30     | BLAKE  | 2850 | 1.0                 |
+--------+--------+------+---------------------+
```

##### ROW_NUMBER

This topic describes how to use the ROW_NUMBER window function in MaxCompute to calculate the row number. This function calculates the row number, starting from 1.

```
ROW_NUMBER() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [AS C|DESC], ...]);
```

PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. This clause specifies the values used for sorting the returned results. This function returns a value of the BIGINT type.

```
-- Create a table CREATE TABLE IF NOT EXISTS emp (
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
```

);

```
-- Insert test data INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00',
```

```
1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10); -- Group all employees by department, sort them in descending order of salary within each group, and obtain the sequence number of each employee within the group SELECT deptno, ename, sal, ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal DESC) AS nums FROM emp; -- Results +--------+--------+--------+------+
| deptno | ename  | sal    | nums |
+--------+--------+--------+------+
| 10     | JACCKA | 5000.0 | 1    |
| 10     | KING   | 5000.0 | 2    |
| 10     | CLARK  | 2450.0 | 3    |
| 10     | WELAN  | 2450.0 | 4    |
| 10     | TEBAGE | 1300.0 | 5    |
| 10     | MILLER | 1300.0 | 6    |
| 20     | SCOTT  | 3000.0 | 1    |
| 20     | FORD   | 3000.0 | 2    |
| 20     | JONES  | 2975.0 | 3    |
| 20     | ADAMS  | 1100.0 | 4    |
| 20     | SMITH  | 800.0  | 5    |
| 30     | BLAKE  | 2850.0 | 1    |
| 30     | ALLEN  | 1600.0 | 2    |
| 30     | TURNER | 1500.0 | 3    |
| 30     | MARTIN | 1250.0 | 4    |
| 30     | WARD   | 1250.0 | 5    |
| 30     | JAMES  | 950.0  | 6    |
+--------+--------+--------+------+
```

##### CLUSTER_SAMPLE

This topic describes how to use the CLUSTER_SAMPLE window function in MaxCompute for cluster sampling. This function performs cluster sampling.

```
BOOLEAN CLUSTER_SAMPLE([BIGINT x, BIGINT y]) OVER (PARTITION BY [col1, col2, ...]);
```

x: required. The value must be a BIGINT constant greater than or equal to 1. If the y parameter is specified, x divides a window into x parts. Otherwise, x extracts x rows of records from a window, which means the function returns True for x rows. If x is NULL, the function returns NULL. y: optional. The value must be a BIGINT constant greater than or equal to 1. In addition, the value of y must not exceed the value of x. This parameter specifies the number of partitions to sample from the x partitions of a window (that is, the return value is True for y partitions). If y is NULL, the function returns NULL. PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. This function returns a value of the BOOLEAN type.

```
- Create a table
CREATE TABLE IF NOT EXISTS test_tbl (
    key STRING,
    value DOUBLE
```

);

```
-- Insert test data INSERT INTO test_tbl VALUES ('groupa', -1.34764165478145); INSERT INTO test_tbl VALUES ('groupa', 0.740212609046718); INSERT INTO test_tbl VALUES ('groupa', 0.167537127858695); INSERT INTO test_tbl VALUES ('groupa', 0.630314566185241); INSERT INTO test_tbl VALUES ('groupa', 0.0112401388646925); INSERT INTO test_tbl VALUES ('groupa', 0.199165745875297); INSERT INTO test_tbl VALUES ('groupa', -0.320543343353587); INSERT INTO test_tbl VALUES ('groupa', -0.273930924365012); INSERT INTO test_tbl VALUES ('groupa', 0.386177958942063); INSERT INTO test_tbl VALUES ('groupa', -1.09209976687047); INSERT INTO test_tbl VALUES ('groupb', -1.10847690938643); INSERT INTO test_tbl VALUES ('groupb', -0.725703978381499); INSERT INTO test_tbl VALUES ('groupb', 1.05064697475759); INSERT INTO test_tbl VALUES ('groupb', 0.135751224393789); INSERT INTO test_tbl VALUES ('groupb', 2.13313102040396); INSERT INTO test_tbl VALUES ('groupb', -1.11828960785008); INSERT INTO test_tbl VALUES ('groupb', -0.849235511508911); INSERT INTO test_tbl VALUES ('groupb', 1.27913806620453); INSERT INTO test_tbl VALUES ('groupb', -0.330817716670401); INSERT INTO test_tbl VALUES ('groupb', -0.300156896191195); INSERT INTO test_tbl VALUES ('groupb', 2.4704244205196); INSERT INTO test_tbl VALUES ('groupb', -1.28051882084434); -- Extract approximately 10% of the values from each group SELECT key, value FROM (SELECT key, value, CLUSTER_SAMPLE(10, 1) OVER (PARTITION BY k ey) AS flag FROM test_tbl) sub WHERE flag = true; -- Return results (sampling results are random; the following are reference results) +--------+---------------------+
| key    | value               |
+--------+---------------------+
| groupa | -0.273930924365012  |
| groupb | -1.11828960785008   |
```

##### NTILE

This topic describes how to use the NTILE window function in MaxCompute. This function divides grouped data into **n** sequential slices and returns the current slice value. If the slices are uneven, the system adds the extra rows to the first slice by default.

```
BIGINT NTILE(BIGINT n) OVER(PARTITION BY [col1, col2…] [ORDER BY [col1[ASC|DESC], col2[ASC|DESC]…]] [windowing_clause]));
```

n: the BIGINT data type. The function returns a value of the BIGINT type.

**Prepare sample data**

```
CREATE TABLE IF NOT EXISTS emp (
    empno    BIGINT    COMMENT 'Employee ID',
    ename    STRING    COMMENT 'Employee name',
    job      STRING    COMMENT 'Job title',
    mgr      BIGINT    COMMENT 'Manager ID',
    hiredate DATETIME  COMMENT 'Hire date',
    sal      DOUBLE    COMMENT 'Salary',
    comm     DOUBLE    COMMENT 'Commission',
    deptno   BIGINT    COMMENT 'Department ID'
) COMMENT 'Employee information table'; INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20), (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00', 1600, 300, 30), (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00', 1250, 500, 30), (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00', 2975, NULL, 20), (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:00', 1250, 1400, 30), (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00', 2850, NULL, 30), (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00', 2450, NULL, 10), (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00', 3000, NULL, 20), (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00', 5000, NULL, 10), (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:00', 1500, 0, 30), (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20), (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30), (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20), (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10), (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10), (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10), (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

**Query results**

This function divides all employees into three groups based on their departments, sorts them by **sal** in descending order, and obtains the sequence number of each employee within their respective group.

```
SELECT deptno,ename,sal,NTILE(3) OVER(PARTITION BY deptno ORDER BY sal DESC) AS nt 3 FROM emp; -- Results +------------+--------+------------+------------+
| deptno     | ename  |     sal    |    nt3     |
+------------+--------+------------+------------+
| 10         | JACCKA | 5000.0     | 1          |
| 10         | KING   | 5000.0     | 1          |
| 10         | CLARK  | 2450.0     | 2          |
| 10         | WELAN  | 2450.0     | 2          |
| 10         | TEBAGE | 1300.0     | 3          |
| 10         | MILLER | 1300.0     | 3          |
| 20         | SCOTT  | 3000.0     | 1          |
| 20         | FORD   | 3000.0     | 1          |
| 20         | JONES  | 2975.0     | 2          |
| 20         | ADAMS  | 1100.0     | 2          |
| 20         | SMITH  | 800.0      | 3          |
| 30         | BLAKE  | 2850.0     | 1          |
| 30         | ALLEN  | 1600.0     | 1          |
| 30         | TURNER | 1500.0     | 2          |
| 30         | MARTIN | 1250.0     | 2          |
| 30         | WARD   | 1250.0     | 3          |
| 30         | JAMES  | 950.0      | 3          |
+------------+--------+------------+------------+
```

##### NTH_VALUE

This topic describes how to use the NTH_VALUE window function in MaxCompute to calculate the nth value in a window. This function calculates the nth value in a window. If n exceeds the maximum length of the window, the function returns NULL.

```
NTH_VALUE(expr, number [, skipNull]) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [ col1 [ASC|DESC], col2 [ASC|DESC], ...]] [windowing_clause]);
```

expr: required. This parameter accepts any basic data type. number: required. This parameter must be an integer greater than or equal to 1. skipNull: optional. This parameter must be of the BOOLEAN type. It specifies whether to ignore rows with NULL values when calculating the nth value. The default value is False. PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. If ORDER BY is not specified, the function returns the expr value of the nth row in the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the expr value of the nth row from the start row to the current row in the window. The return value is of the same type as expr.

```
-- Create a table. CREATE TABLE IF NOT EXISTS test_src (
    user_id BIGINT,
    price DOUBLE
```

);

```
-- Insert test data. INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Example 1: When ORDER BY is not specified, the current window spans from the first row to the last row. The function returns the value of the second row. SELECT user_id, price, NTH_VALUE(price, 2) OVER (PARTITION BY user_id) AS nth_value F ROM test_src; -- Result +------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 4.5        | 6.5        |
| 1          | 6.5        | 6.5        | -- The second row in the current window.
| 1          | 5.5        | 6.5        |
| 1          | 5.5        | 6.5        |
| 2          | NULL       | 3.0        |
| 2          | 3.0        | 3.0        | -- The second row in the current window.
| 3          | NULL       | 4.0        |
| 3          | 4.0        | 4.0        | -- The second row in the current window.
+------------+------------+------------+ -- Example 2: When ORDER BY is not specified, the current window spans from the first row to the last row. The function returns the value of the third row. -- Note that the second and third windows each contain only two rows. SELECT user_id, price, NTH_VALUE(price, 3) OVER (PARTITION BY user_id) AS nth_value F ROM test_src; -- Result +------------+------------+------------+
```

```
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 4.5        | 5.5        |
| 1          | 6.5        | 5.5        |
| 1          | 5.5        | 5.5        | -- The third row in the current window.
| 1          | 5.5        | 5.5        |
| 2          | NULL       | NULL       |
| 2          | 3.0        | NULL       |
| 3          | NULL       | NULL       |
| 3          | 4.0        | NULL       |
+------------+------------+------------+ -- Example 3: When ORDER BY is specified, the current window spans from the first row to the current row. The function returns the value of the second row. SELECT user_id, price, NTH_VALUE(price, 2) OVER (PARTITION BY user_id ORDER BY price) AS nth_value FROM test_src; -- Result +---------+-------+-----------+
| user_id | price | nth_value |
+---------+-------+-----------+
| 1       | 4.5   | NULL      |  -- The current window contains only one row. The sec
ond row exceeds the window length.
| 1       | 5.5   | 5.5       |
| 1       | 5.5   | 5.5       |
| 1       | 6.5   | 5.5       |
| 2       | NULL  | NULL      |
| 2       | 3.0   | 3.0       |
| 3       | NULL  | NULL      |
| 3       | 4.0   | 4.0       |
+---------+-------+-----------+ -- Example 4: When ORDER BY is not specified, the current window spans from the first row to the last row. -- The function returns the value of the first row, and skipNull is set to True. SELECT user_id, price, NTH_VALUE(price, 1, true) OVER (PARTITION BY user_id) AS nth_v alue FROM test_src; -- Result +------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 4.5        | 4.5        |
| 1          | 6.5        | 4.5        |
| 1          | 5.5        | 4.5        |
| 1          | 5.5        | 4.5        |
| 2          | NULL       | 3.0        | -- The first row is NULL and is skipped.
| 2          | 3.0        | 3.0        |
| 3          | NULL       | 4.0        |
| 3          | 4.0        | 4.0        |
+------------+------------+------------+
```

##### CUME_DIST

This topic describes how to use the CUME_DIST window function in MaxCompute to calculate the cumulative distribution. The function calculates the cumulative distribution, which is the ratio of the number of rows with values greater than or equal to the current value to the total number of rows in the group. The ORDER BY clause specifies the values used for comparison.

```
CUME_DIST() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [ASC
|DESC], ...]);
```

PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: required. This clause specifies the values used for sorting. The function returns a DOUBLE value that represents the ratio of the number of rows with values greater than or equal to the current value to the total number of rows in the group.

```
-- Create a table CREATE TABLE IF NOT EXISTS emp (
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
```

);

```
-- Insert test data INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20);
```

```
INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10); -- Group all employees by department and calculate the cumulative distribution percen tage of sal within each group SELECT deptno, ename, sal, CONCAT(ROUND(CUME_DIST() OVER (PARTITION BY deptno ORDER B Y sal DESC) * 100, 2), '%') AS cume_dist FROM emp; -- Result +--------+--------+--------+-----------+
| deptno | ename  | sal    | cume_dist |
+--------+--------+--------+-----------+
| 10     | JACCKA | 5000.0 | 33.33%    |
| 10     | KING   | 5000.0 | 33.33%    |
| 10     | CLARK  | 2450.0 | 66.67%    |
| 10     | WELAN  | 2450.0 | 66.67%    |
| 10     | TEBAGE | 1300.0 | 100.0%    |
| 10     | MILLER | 1300.0 | 100.0%    |
| 20     | SCOTT  | 3000.0 | 40.0%     |
| 20     | FORD   | 3000.0 | 40.0%     |
| 20     | JONES  | 2975.0 | 60.0%     |
| 20     | ADAMS  | 1100.0 | 80.0%     |
| 20     | SMITH  | 800.0  | 100.0%    |
| 30     | BLAKE  | 2850.0 | 16.67%    |
| 30     | ALLEN  | 1600.0 | 33.33%    |
| 30     | TURNER | 1500.0 | 50.0%     |
| 30     | MARTIN | 1250.0 | 83.33%    |
| 30     | WARD   | 1250.0 | 83.33%    |
| 30     | JAMES  | 950.0  | 100.0%    |
+--------+--------+--------+-----------+
```

##### FIRST_VALUE

This topic describes how to use the FIRST_VALUE window function in MaxCompute to obtain the first value up to the current row after sorting within a group. This function obtains the first value from the start of a group up to the current row after sorting.

```
FIRST_VALUE(expr) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col1 [ASC|DESC], co l2 [ASC|DESC], ...]] [windowing_clause]);
```

expr: required. This parameter can be any basic data type. PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. If ORDER BY is not specified, the function returns the expr value of the first row in the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the expr value of the first row in the current window. The return value has the same data type as expr.

```
-- Create a table. CREATE TABLE IF NOT EXISTS test_src (
    user_id BIGINT,
    price DOUBLE
```

);

```
-- Insert test data. INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Example 1: If you do not specify ORDER BY, the current window spans from the first row to the last row, and the function returns the value of the first row in the curre nt window. SELECT user_id, price, FIRST_VALUE(price) OVER (PARTITION BY user_id) AS first_value FROM test_src; -- Result +---------+-------+-------------+
| user_id | price | first_value |
+---------+-------+-------------+
| 1       | 5.5   | 5.5         |  -- First row of the current window.
| 1       | 4.5   | 5.5         |
| 1       | 6.5   | 5.5         |
| 1       | 5.5   | 5.5         |
| 2       | NULL  | NULL        |  -- First row of the current window.
| 2       | 3.0   | NULL        |
```

```
| 3       | 4.0   | 4.0         |  -- First row of the current window.
| 3       | NULL  | 4.0         |
+---------+-------+-------------+ -- Example 2: If you specify ORDER BY, the current window spans from the first row to the current row, and the function returns the value of the first row in the current w indow. SELECT user_id, price, FIRST_VALUE(price) OVER (PARTITION BY user_id ORDER BY price) AS first_value FROM test_src; -- Result +---------+-------+-------------+
| user_id | price | first_value |
+---------+-------+-------------+
| 1       | 4.5   | 4.5         |  -- First row of the current window.
| 1       | 5.5   | 4.5         |
| 1       | 5.5   | 4.5         |
| 1       | 6.5   | 4.5         |
| 2       | NULL  | NULL        |  -- First row of the current window.
| 2       | 3.0   | NULL        |
| 3       | NULL  | NULL        |  -- First row of the current window.
| 3       | 4.0   | NULL        |
+---------+-------+-------------+
```

##### LAST_VALUE

This topic describes how to use the LAST_VALUE window function in MaxCompute to obtain the last value up to the current row after sorting within a group. This function obtains the last value from the start of a group up to the current row after sorting.

```
LAST_VALUE(expr) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC], ...]] [windowing_clause]);
```

expr: required. This parameter can be any basic data type. PARTITION BY [col1, col2, ...]: optional. This clause specifies the columns used for partitioning. ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]: optional. If ORDER BY is not specified, the function returns the expr value of the last row in the current window. If ORDER BY is specified, the function sorts the results in the specified order and returns the expr value of the current row in the current window. The return value is of the same data type as expr.

```
-- Create a table
```

```
CREATE TABLE IF NOT EXISTS test_src (
    user_id BIGINT,
    price DOUBLE
```

);

```
-- Insert test data INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); -- Example 1: If you do not specify ORDER BY, the current window ranges from the firs t row to the last row, and the function returns the value of the last row in the curr ent window. SELECT user_id, price, LAST_VALUE(price) OVER (PARTITION BY user_id) AS last_value FR OM test_src; -- Results +---------+-------+------------+
| user_id | price | last_value |
+---------+-------+------------+
| 1       | 5.5   | 5.5        |
| 1       | 4.5   | 5.5        |
| 1       | 6.5   | 5.5        |
| 1       | 5.5   | 5.5        |  -- The last row of the current window.
| 2       | NULL  | 3.0        |
| 2       | 3.0   | 3.0        |  -- The last row of the current window.
| 3       | NULL  | 4.0        |
| 3       | 4.0   | 4.0        |  -- The last row of the current window.
+---------+-------+------------+ -- Example 2: If you specify ORDER BY, the current window ranges from the first row t o the current row, and the function returns the value of the current row in the curre nt window. SELECT user_id, price, LAST_VALUE(price) OVER (PARTITION BY user_id ORDER BY price) A S last_value FROM test_src; -- Results +---------+-------+------------+
| user_id | price | last_value |
+---------+-------+------------+
| 1       | 4.5   | 4.5        |  -- The current row of the current window.
| 1       | 5.5   | 5.5        |  -- The current row of the current window.
| 1       | 5.5   | 5.5        |  -- The current row of the current window.
| 1       | 6.5   | 6.5        |  -- The current row of the current window.
| 2       | NULL  | NULL       |  -- The current row of the current window.
| 2       | 3.0   | 3.0        |  -- The current row of the current window.
| 3       | NULL  | NULL       |  -- The current row of the current window.
| 3       | 4.0   | 4.0        |  -- The current row of the current window.
+---------+-------+------------+
```

#### Aggregate functions

##### Expressions of filter conditions in

#### aggregate functions

This topic describes how to use filter condition expressions in MaxCompute to specify filter conditions for aggregate functions. You can add a filter condition expression to any aggregate function. If you specify the FILTER clause, the system passes only the rows where where_condition evaluates to TRUE to the corresponding aggregate function for processing.

**Note**

Currently, only built-in aggregate functions support a FILTER (WHERE where_condition) clause. User-defined aggregate functions (UDAFs) do not support this clause. You cannot use COUNT(*) together with a FILTER (WHERE where_condition) clause. If you need to use them together, use the COUNT_IF function.

```
aggregate_name(expression [, ...]) [FILTER (WHERE where_condition)];
```

aggregate_name: the name of the aggregate function. expression: the expression parameter of the aggregate function. FILTER (WHERE where_condition): optional. The filter condition expression. Only the rows where where_condition evaluates to TRUE participate in aggregate computing. The type of the return value depends on the aggregate function that you use.

```
-- Use the VALUES clause to construct test data and demonstrate the FILTER condition SELECT
    SUM(x),
    SUM(x) FILTER (WHERE y > 1),
    SUM(x) FILTER (WHERE y > 2)
FROM VALUES (NULL, 1), (1, 2), (2, 3), (3, NULL) AS t(x, y); -- Output +-----+-----+-----+
| _c0 | _c1 | _c2 |
+-----+-----+-----+
| 6   | 3   | 2   |
+-----+-----+-----+
```

##### COUNT

This topic describes how to use the COUNT function in MaxCompute to calculate the number of records and provides reference examples. This function calculates the number of records.

```
BIGINT COUNT([DISTINCT|ALL] value);
```

distinct|all: specifies whether to remove duplicate records during counting. The default value is **all**, which counts all records. If **distinct** is specified, the function counts only the number of distinct values. value: This parameter can be of any data type. When **value** is NULL, the function excludes that row from the calculation. **value** can be *. When count(*) is used, the function returns the total number of rows. The function returns a value of the BIGINT type. Example 1: Simple counting

```
CREATE TABLE IF NOT EXISTS tbla (
    col1 BIGINT
```

);

```
INSERT INTO tbla VALUES (1), (2), (NULL); SELECT COUNT(*) FROM tbla; -- Result +--------+
|   _c0  |
+--------+
|    3   |
+--------+ SELECT COUNT(col1) FROM tbla; -- Result +--------+
|   _c0  |
+--------+
|    2   |
+--------+
```

Example 2: Aggregate counting Aggregate functions can be used with GROUP BY.

```
CREATE TABLE IF NOT EXISTS test_src (
    key   STRING COMMENT 'Key',
    value DOUBLE COMMENT 'Value'
```

);

```
INSERT INTO test_src VALUES ('a', 2.0), ('a', 4.0), ('b', 1.0), ('b', 3.0); SELECT key, COUNT(value) AS count FROM test_src GROUP BY key; -- Result +-----+-------+
| key | count |
+-----+-------+
| a   | 2     |
+-----+-------+
| b   | 2     |
+-----+-------+
```

##### COUNT_IF

This topic describes how to use the COUNT_IF aggregation function in MaxCompute to count the number of records where the value of expr is TRUE. This function counts the number of records where the value of expr is TRUE.

```
BIGINT COUNT_IF(BOOLEAN expr);
```

expr: required. This parameter must be of the BOOLEAN type. If the value of expr is FALSE or NULL, the system excludes the row from the calculation. This function returns a value of the BIGINT type.

```
SELECT COUNT_IF(x > 1), COUNT_IF(x <= 1) FROM VALUES (NULL), (0), (1), (2) AS t(x); -- Result +-----+-----+
| _c0 | _c1 |
+-----+-----+
| 1   | 2   |
+-----+-----+
```

##### AVG

This topic describes how to use the AVG aggregate function in MaxCompute to calculate the average value. This function calculates the average value.

```
DOUBLE AVG(DOUBLE value); DECIMAL AVG(DECIMAL value);
```

value: required. The value must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If the input value is of any other type, an error is returned. If the value is NULL, the system excludes the row from calculation. The BOOLEAN type is not allowed for calculation. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. If the input value is of any other valid type, the function returns a value of the DOUBLE type.

```
-- Create a table. CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data. INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (NULL); -- Calculate the average value of the value column, which is (1+2)/2=1.5. SELECT AVG(value) AS avg FROM tbla; -- Return result +------+
| avg  |
+------+
| 1.5  |
+------+
```

##### MAX

This topic describes how to use the MAX aggregate function in MaxCompute to calculate the maximum value. This function calculates the maximum value.

```
MAX(value);
```

value: required. This parameter accepts any data type. If a value in the column is NULL, the system skips the row during the calculation. The system does not allow BOOLEAN data types in calculations. The return value has the same data type as the value parameter.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    col1 BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); -- Calculate the maximum value of the col1 column SELECT MAX(col1) FROM tbla; -- Return the result +------+
| _c0  |
+------+
| 2    |
+------+
```

##### MIN

This topic describes how to use the MIN aggregate function in MaxCompute to calculate the minimum value. This function calculates the minimum value.

```
MIN(value);
```

value: required. This parameter accepts any data type. If a column value is NULL, the system excludes the row from the calculation. The system does not allow BOOLEAN values in calculations. The return value has the same data type as the value parameter.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); -- Calculate the minimum value of the value column SELECT MIN(value) FROM tbla; -- Result +------+
| _c0  |
+------+
| 1    |
+------+
```

##### MEDIAN

This topic describes how to use the MEDIAN aggregate function in MaxCompute to calculate the median. This function calculates the median.

```
DOUBLE MEDIAN(DOUBLE number); DECIMAL MEDIAN(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts the value to the DOUBLE type for calculation. If a value of another type is specified, the system returns an error. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. If the input value is of another valid type, the function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5); -- Calculate the median of the value column SELECT MEDIAN(value) FROM tbla; -- Result +------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### STDDEV

This topic describes how to use the aggregation function STDDEV in MaxCompute to calculate the population standard deviation. This function calculates the population standard deviation.

```
DOUBLE STDDEV(DOUBLE number); DECIMAL STDDEV(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If you enter a value of another type, the system returns an error. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. If the input value is of another valid type, the function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5); -- Calculate the population standard deviation of the value column SELECT STDDEV(value) FROM tbla; -- Result +---------------------+
| _c0                 |
+---------------------+
| 1.4142135623730951  |
+---------------------+
```

##### STDDEV_SAMP

This topic describes how to use the STDDEV_SAMP aggregation function in MaxCompute to calculate the sample standard deviation. This function calculates the sample standard deviation.

```
DOUBLE STDDEV_SAMP(DOUBLE number); DECIMAL STDDEV_SAMP(DECIMAL number);
```

number: required. This parameter must be of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, the system implicitly converts it to the DOUBLE type before calculation. If you specify a value of any other type, the system returns an error. If the input value is of the DECIMAL type, the function returns a value of the DECIMAL type. If the input value is of any other valid type, the function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5); -- Calculate the sample standard deviation of the value column SELECT STDDEV_SAMP(value) FROM tbla; -- Result +----------------------+
| _c0                  |
+----------------------+
|  1.5811388300841898  |
+----------------------+
```

##### SUM

This topic describes how to use the SUM aggregate function in MaxCompute to calculate the aggregate sum. This function calculates the aggregate sum.

```
SUM(value);
```

value: required. This parameter must be of the DOUBLE, DECIMAL, or BIGINT. If the input value is of the STRING type, the system implicitly converts it to the DOUBLE type before calculation. If the value in a column is NULL, the system excludes that row from the calculation. The BOOLEAN type is not allowed in the calculation. If the input value is of the BIGINT type, the function returns a BIGINT value. If the input value is of the DOUBLE or STRING type, the function returns a DOUBLE value.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    value BIGINT
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (NULL); -- Calculate the aggregate value of the value column SELECT SUM(value) FROM tbla; -- Return result +------+
| _c0  |
+------+
| 3    |
+------+
```

##### WM_CONCAT

This topic describes how to use the WM_CONCAT aggregate function in MaxCompute to concatenate values with a specified delimiter. This function concatenates values in str by using the specified separator as the delimiter.

```
STRING WM_CONCAT(STRING separator, STRING str);
```

separator: required. This parameter must be a STRING constant that specifies the delimiter. An error is returned if a value of another type or a non-constant value is specified. str: required. This parameter must be of the STRING type. If the input value is of the BIGINT, DOUBLE, or DATETIME type, the system implicitly converts the value to the STRING type before calculation. An error is returned if a value of another type is specified. This function returns a value of the STRING type.

**Note**

In the statement SELECT WM_CONCAT(',', name) FROM test_src; , if test_src is an empty collection, this statement returns NULL.

```
-- Create a table. CREATE TABLE IF NOT EXISTS test (
    id INT,
    alphabet STRING
```

);

```
-- Insert test data. INSERT INTO test VALUES (1, 'a'), (1, 'b'), (1, 'c'), (2, 'D'), (2, 'E'), (2, 'F'); -- Group and sort data by the id column, and concatenate values in each group with co mmas. SELECT id, WM_CONCAT(',', alphabet) FROM test GROUP BY id ORDER BY id LIMIT 100; -- Returned result +----+-------+
| id | _c1   |
+----+-------+
| 1  | a,b,c |
| 2  | D,E,F |
+----+-------+
```

##### PERCENTILE

This topic describes how to use the PERCENTILE aggregate function in MaxCompute to return the exact p-th percentile of a specified column. This function returns the exact p-th percentile of a specified column. The value of p must be between 0 and 1. Only integer values produce true percentiles.

```
DOUBLE PERCENTILE(BIGINT col, DOUBLE p); ARRAY<DOUBLE> PERCENTILE(BIGINT col, ARRAY(DOUBLE p1 [, DOUBLE p2, ...]));
```

col: required. The name of a BIGINT column. p: required. This parameter specifies the exact percentile to be calculated. It must be of the DOUBLE type and have a value between 0 and 1. If p is a single DOUBLE value, the function returns a DOUBLE value. If p is of the ARRAY type, the function returns an ARRAY value.

```
-- Create a table CREATE TABLE IF NOT EXISTS var_test (
    c1 BIGINT
```

);

```
-- Insert test data INSERT INTO var_test VALUES (8); INSERT INTO var_test VALUES (9); INSERT INTO var_test VALUES (10); INSERT INTO var_test VALUES (11); -- Example 1: Calculate the p-th percentile of the c1 column (single p value) SELECT PERCENTILE(c1, 0), PERCENTILE(c1, 0.3), PERCENTILE(c1, 0.5), PERCENTILE(c1, 1) FROM var_test; -- Result +------+------+------+------+
| _c0  | _c1  | _c2  | _c3  |
+------+------+------+------+
| 8.0  | 8.9  | 9.5  | 11.0 |
+------+------+------+------+ -- Example 2: Calculate the p-th percentile of the c1 column (multiple p values, retu rns ARRAY) SELECT PERCENTILE(c1, ARRAY(0, 0.3, 0.5, 1)) FROM var_test; -- Result +-------------------+
| _c0               |
+-------------------+
| [8, 8.9, 9.5, 11] |
+-------------------+
```

##### Additional aggregate functions

###### Usage notes

This topic describes the settings that you must configure to use the new aggregation functions. MaxCompute 2.0 introduces new aggregation functions. To use these new functions in SQL statements, you must add the following SET statement.

```
SET odps.sql.type.system.odps2=true;
```

**Note**

You must submit the preceding SET statement and the SQL statements that use the new functions at the same time.

###### COLLECT_LIST

This topic describes how to use the COLLECT_LIST aggregate function in MaxCompute to aggregate the values of a specified column into an array. Within a given group, the function aggregates the expression specified by col into an array.

```
ARRAY COLLECT_LIST(col);
```

col: required. This parameter specifies the name of a column. It can be of any data type. The function returns a value of the ARRAY type.

```
-- Create a table. CREATE TABLE IF NOT EXISTS tbla (
    col1 BIGINT,
    col2 STRING
```

);

```
-- Insert test data. INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (1, 'b'); INSERT INTO tbla VALUES (1, 'c'); INSERT INTO tbla VALUES (2, 'd'); INSERT INTO tbla VALUES (2, 'e'); -- Group data by col1 and aggregate col2 into an array. SELECT col1, COLLECT_LIST(col2) FROM tbla GROUP BY col1; -- Result +------+-----------------+
| col1 | _c1             |
+------+-----------------+
| 1    | [a, b, c]       |
| 2    | [d, e]          |
+------+-----------------+
```

###### COLLECT_SET

This topic describes how to use the COLLECT_SET aggregate function in MaxCompute to aggregate the values of a specified column into an array of unique elements. This function aggregates the expression specified by col within a given group into an array of unique elements.

```
ARRAY COLLECT_SET(col);
```

col: required. This parameter specifies the name of a column and can be of any data type. This function returns a value of the ARRAY type.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    col1 BIGINT,
    col2 STRING
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (1, 'b'); INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (2, 'd'); INSERT INTO tbla VALUES (2, 'd'); -- Group data by col1 and aggregate col2 into an array of unique elements SELECT col1, COLLECT_SET(col2) FROM tbla GROUP BY col1; -- Output +------+----------+
| col1 | _c1      |
+------+----------+
| 1    | [a, b]   |
| 2    | [d]      |
+------+----------+
```

###### VARIANCE/VAR_POP

This topic describes how to use the VARIANCE/VAR_POP aggregate function in MaxCompute to calculate the variance of a specified numeric column. This function calculates the variance of a specified numeric column.

```
DOUBLE VARIANCE(col); DOUBLE VAR_POP(col);
```

col: required. The column must be of the numeric type. If the column is of another data type, the function returns NULL. The function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS test (
    c1 BIGINT
```

);

```
-- Insert test data INSERT INTO test VALUES (8); INSERT INTO test VALUES (9); INSERT INTO test VALUES (10); INSERT INTO test VALUES (11); -- Calculate the variance of the c1 column (VARIANCE and VAR_POP are equivalent) SELECT VARIANCE(c1) FROM test; SELECT VAR_POP(c1) FROM test; -- Return result +------+
| _c0  |
+------+
| 1.25 |
+------+
```

###### VAR_SAMP

This topic describes how to use the VAR_SAMP aggregate function in MaxCompute to calculate the sample variance of a specified numeric column. This function calculates the sample variance of a specified numeric column.

```
DOUBLE VAR_SAMP(col);
```

col: required. This parameter specifies a numeric column. If a column of another data type is specified, the function returns NULL. The function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS test (
    c1 BIGINT
```

);

```
-- Insert test data INSERT INTO test VALUES (8); INSERT INTO test VALUES (9); INSERT INTO test VALUES (10); INSERT INTO test VALUES (11); -- Calculate the sample variance of the c1 column SELECT VAR_SAMP(c1) FROM test; -- Output +---------------------+
| _c0                 |
+---------------------+
| 1.6666666666666667  |
+---------------------+
```

###### COVAR_POP

This topic describes how to use the COVAR_POP aggregate function in MaxCompute to calculate the population covariance of two specified numeric columns. This function calculates the population covariance of two specified numeric columns.

```
DOUBLE COVAR_POP(col1, col2);
```

col1: required. This parameter specifies a numeric column. The function returns NULL for columns of other data types. col2: required. This parameter specifies a numeric column. The function returns NULL for columns of other data types. The function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS test (
    c1 BIGINT,
    c2 BIGINT
```

);

```
-- Insert test data INSERT INTO test VALUES (3, 2); INSERT INTO test VALUES (14, 5); INSERT INTO test VALUES (50, 14); INSERT INTO test VALUES (26, 75); -- Calculate the population covariance of c1 and c2 SELECT COVAR_POP(c1, c2) FROM test; -- Result +----------------------+
| _c0                  |
+----------------------+
| 123.49999999999997   |
+----------------------+
```

###### COVAR_SAMP

This topic describes how to use the COVAR_SAMP aggregate function in MaxCompute to calculate the sample covariance of two specified numeric columns. This function calculates the sample covariance of two specified numeric columns.

```
DOUBLE COVAR_SAMP(col1, col2);
```

col1: required. This parameter specifies a numeric column. The function returns NULL if col1 is of another data type. col2: required. This parameter specifies a numeric column. The function returns NULL if col2 is of another data type. The function returns a value of the DOUBLE type.

```
-- Create a table CREATE TABLE IF NOT EXISTS test (
    c1 BIGINT,
    c2 BIGINT
```

);

```
-- Insert test data INSERT INTO test VALUES (3, 2); INSERT INTO test VALUES (14, 5); INSERT INTO test VALUES (50, 14); INSERT INTO test VALUES (26, 75); -- Calculate the sample covariance of c1 and c2 SELECT COVAR_SAMP(c1, c2) FROM test; -- Result +----------------------+
| _c0                  |
+----------------------+
| 164.66666666666663   |
+----------------------+
```

###### ANY_VALUE

This topic describes how to use the ANY_VALUE aggregate function in MaxCompute to return an arbitrary non-NULL value from a specified range. The function returns an arbitrary value from a specified range.

```
ANY_VALUE(value);
```

value: required. This parameter can be of any data type. If the value is NULL, the system excludes the row from the calculation. The type of the return value is the same as the input type.

```
SELECT key, ANY_VALUE(value) FROM VALUES (1, 'value1'), (1, 'value2'), (2, 'value3'), (2, NULL), (3, NULL) AS t(ke y, value) GROUP BY key; -- Results +------------+------------+
| key        | _c1        |
+------------+------------+
| 1          | value1     |
| 2          | value3     |
| 3          | NULL       |
+------------+------------+
```

###### NUMERIC_HISTOGRAM

This topic describes how to use the NUMERIC_HISTOGRAM aggregate function in MaxCompute to calculate the approximate histogram of a specified column. This function calculates the approximate histogram of a specified column.

```
MAP<DOUBLE, DOUBLE> NUMERIC_HISTOGRAM(BIGINT buckets, DOUBLE value);
```

buckets: required. This parameter must be of the BIGINT type. It specifies the maximum number of buckets (columns) in the returned approximate histogram. value: required. This parameter must be of the DOUBLE type. It specifies the data column for which the approximate histogram needs to be calculated. The return value is of the MAP<DOUBLE, DOUBLE> type. In the return value, the key represents the x-axis coordinate of the approximate histogram, and the value represents the approximate height of a histogram bucket.

```
SELECT NUMERIC_HISTOGRAM(5, value) FROM VALUES (1.0), (2.0), (3.0), (4.0), (5.0), (6.0), (7.0), (8.0), (9.0), (10.0) AS t(value); -- Result +-------------------------------------+
|               _c0                   |
+-------------------------------------+
| {1.5:2, 3.5:2, 5.5:2, 7.5:2, 9.5:2} |
+-------------------------------------+
```

###### PERCENTILE_APPROX

This topic describes how to use the PERCENTILE_APPROX aggregate function in MaxCompute to return the approximate value for a specified percentile in a specified numeric column. This function returns the value that corresponds to a specified percentile p in a specified numeric column col.

```
DOUBLE PERCENTILE_APPROX(DOUBLE col, p [, B]); ARRAY<DOUBLE> PERCENTILE_APPROX(DOUBLE col, ARRAY(p1 [, p2]...) [, B]);
```

col: required. This parameter must be of the DOUBLE type. It specifies the numeric column for which you want to calculate the approximate percentile. p: required. This parameter must be a percentile. Valid values: [0.0, 1.0]. It can specify a single percentile value or an array of percentile values to be returned. B: optional. This parameter specifies the accuracy. A higher accuracy yields a smaller error for the approximate value. If this parameter is not specified, the default value is 10000. When the number of values in col is less than B, the function returns the exact percentile value. PERCENTILE_APPROX(DOUBLE col, p [, B]) returns a single percentile value. PERCENTILE_APPROX(DOUBLE col, ARRAY(p1 [, p2]...) [, B]) returns an array of percentile values.

```
SELECT PERCENTILE_APPROX(10.0, 0.5, 100); -- Result +------+
| _c0  |
+------+
| 10.0 |
+------+ SELECT PERCENTILE_APPROX(10.0, ARRAY(0.5, 0.4, 0.1), 100); -- Result +------------------+
| _c0              |
+------------------+
| [10.0,10.0,10.0] |
+------------------+
```

###### APPROX_DISTINCT

This topic describes how to use the APPROX_DISTINCT aggregate function in MaxCompute to return the approximate number of distinct values in input data. This function returns the approximate number of distinct values in input data.

```
BIGINT APPROX_DISTINCT(value);
```

value: required. This parameter specifies the input data for deduplication. The function returns a value of the BIGINT type. If all input values are null, the function returns 0. This function has a standard error of 5%.

```
SELECT APPROX_DISTINCT(value) FROM VALUES (1), (2), (2), (3), (3), (3), (4) AS t(valu e); -- Result +------+
| _c0  |
+------+
|  4   |
+------+
```

#### Other functions

##### ARRAY

This topic describes how to use the ARRAY function in MaxCompute to construct an array from specified values. This function constructs an array from specified values.

```
ARRAY ARRAY(value1, value2, ...);
```

value: required. This parameter can be of any data type, but all values must be of the same type. This function returns a value of the ARRAY type.

```
SELECT ARRAY(123, 456, 789); -- Result +---------------+
| _c0           |
+---------------+
| [123,456,789] |
+---------------+
```

##### ARRAY_CONTAINS

This topic describes how to use the ARRAY_CONTAINS function in MaxCompute to check whether a given ARRAY contains a specified value. This function checks whether ARRAY a contains v.

```
BOOLEAN ARRAY_CONTAINS(ARRAY<T> a, value v);
```

a: required. This parameter must be of the ARRAY type. v: required. The data type of this parameter must match the data type of the elements in the ARRAY. This function return a value of the BOOLEAN type.

```
SELECT ARRAY_CONTAINS(ARRAY('a', 'b'), 'a'); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ARRAY_CONTAINS(ARRAY(456, 789), 123); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### CAST

This topic describes how to use the CAST function in MaxCompute to convert the result of an expression to a target data type and provides reference examples. This function converts the result of an expression to a target data type. For example, `cast('1' as bigint)` converts the string **1** to the integer **1**.

```
CAST(expr AS <type>);
```

**Note**

CAST(DOUBLE AS BIGINT): converts a DOUBLE value to the BIGINT type. CAST(STRING AS BIGINT): converts a string to the BIGINT type. The function directly converts a string to BIGINT if the string represents an integer. If a string represents a floating-point number or a number in exponential notation, the function first converts the string to DOUBLE and then to BIGINT. For CAST(STRING AS DATETIME) or CAST(DATETIME AS STRING), the function applies the default date format **yyyy-mm-dd hh:mi:ss**. expr: required. This parameter specifies the source expression to be converted. type: required. This parameter specifies the target data type, such as BIGINT, STRING, or DATETIME. The type of the return value matches the specified target type `<type>` . If the conversion fails or the types are incompatible, the function throws an exception.

```
SELECT CAST('12' AS BIGINT); -- Result +--------+
|   _c0  |
+--------+
|   12   |
+--------+
```

##### COALESCE

This topic describes how to use the COALESCE function in MaxCompute to return the first non-NULL value in a list. This function returns the first non-NULL value in a list.

```
COALESCE(expr1, expr2, ...);
```

expr: required. This parameter specifies the values to test. All values must be of the same data type or be NULL. Otherwise, an error is returned. At least one parameter must be specified. Otherwise, an error is returned. The return value must be of the same data type as the parameters.

```
SELECT COALESCE(NULL, NULL, 3); -- Result +------+
| _c0  |
+------+
|  3   |
+------+ SELECT COALESCE(NULL, 'hello', 'world'); -- Result +-------+
| _c0   |
+-------+
| hello |
+-------+
```

##### DECODE

This topic describes how to use the DECODE function in MaxCompute to implement if-thenelse conditional branching. This function implements if-then-else conditional branching.

```
DECODE(expression, search, result[, search, result]...[, default]);
```

expression: required. This parameter specifies the expression to be compared. search: required. This parameter specifies the search item to be compared with the expression. result: required. This parameter specifies the value to be returned when the search item matches the expression. default: optional. This parameter specifies the default value to be returned if no search item matches. If this parameter is not specified, the function returns NULL. The function returns the matched result. If no match is found, the function returns the default value. If no default value is specified, the function returns NULL. You must specify at least three parameters. All result parameters must be of the same data type or be NULL. Inconsistent data types cause an error. All search items and the expression must be of the same data type. Otherwise, an error is returned. If the DECODE function contains duplicate search items and a match is found, the function returns the first matched value.

```
SELECT DECODE(customer_id, 1, 'Taobao', 2, 'Alipay', 3, 'Aliyun', NULL, 'N/A', 'Other s') AS result FROM VALUES (1, 10),
            (1, 10),
            (2, NULL),
            (3, 13),
            (4, 0),
            (NULL, 6),
            (5, 18) AS t(customer_id, value);
-- Result +--------+
| result |
+--------+
| Taobao |
| Taobao |
| Alipay |
| Aliyun |
| Others |
| N/A    |
| Others |
+--------+ -- The DECODE function in the preceding example implements the same logic as the foll owing if-then-else statement: IF customer_id = 1 THEN result := 'Taobao'; ELSIF customer_id = 2 THEN result := 'Alipay'; ELSIF customer_id = 3 THEN result := 'Aliyun'; ... ELSE
  result := 'Others';
END IF;
```

**Note**

By default, MaxCompute SQL returns NULL when it evaluates NULL=NULL. However, in the **decode** function, NULL equals NULL. In the preceding example, when the value of **customer_id** is NULL, the **decode** function returns N/A.

##### EXPLODE

This topic describes how to use the EXPLODE function in MaxCompute. EXPLODE is a User- Defined Table-generating Function (UDTF) that converts one row of data into multiple rows. EXPLODE is a UDTF that converts one row of data into multiple rows. If var is of the ARRAY type, the function converts the array stored in the column into multiple rows. If var is of the MAP<K, V> type, the function converts each key-value pair of the map stored in the column into a row with two columns, where one column stores the key and the other stores the value.

**Note**

You can use only one EXPLODE function in a SELECT statement, and you cannot include other columns from the table in the same statement. You cannot use the EXPLODE function with GROUP BY, CLUSTER BY, DISTRIBUTE BY, or SORT BY.

```
EXPLODE(var);
```

var: required. This parameter must be of the ARRAY or MAP<K, V> type. This function returns the converted rows.

```
SELECT EXPLODE(ARRAY(NULL, 'a', 'b', 'c')); -- Result +------+
| col  |
+------+
| NULL |
| a    |
| b    |
| c    |
+------+
```

##### GET_IDCARD_AGE

This topic describes how to use the GET_IDCARD_AGE function in MaxCompute to return the current age based on an ID card number. This function returns the current age based on an ID card number. The return value is the difference between the current year and the birth year specified in the ID card number.

```
BIGINT GET_IDCARD_AGE(STRING idcardno);
```

`idcardno` : required. This parameter must be of the STRING type. The value is a 15-digit or 18-digit ID card number. During calculation, the system checks the validity of the ID card number based on the province code and the last check digit. If the verification fails, the system returns NULL. The function returns a value of the BIGINT type. If the input value is NULL, the function returns NULL. If the difference between the current year and the birth year is greater than 100, the function returns NULL.

```
SELECT GET_IDCARD_AGE('id_card_number'); -- Return result (Enter a valid ID card number. The function returns the age, such as "18".) SELECT GET_IDCARD_AGE(NULL); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### GET_IDCARD_BIRTHDAY

This topic describes how to use the GET_IDCARD_BIRTHDAY function in MaxCompute to return the date of birth based on an ID card number. This function returns the date of birth based on an ID card number.

```
DATETIME GET_IDCARD_BIRTHDAY(STRING idcardno);
```

idcardno: required. This parameter must be of the STRING type and must be a 15-digit or 18-digit ID card number. During calculation, the system checks the validity of the ID card based on the province code and the last check digit. If the verification fails, the function returns NULL. The function returns a value of the DATETIME type. If the input is NULL, the function returns NULL.

```
SELECT GET_IDCARD_BIRTHDAY('ID card number'); -- Returned result (returns the birth date based on a real ID card number, for exampl e, "2001-01-01 00:00:00") SELECT GET_IDCARD_BIRTHDAY(NULL); -- Returned result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### GET_IDCARD_SEX

This topic describes how to use the GET_IDCARD_SEX function in MaxCompute to return the gender based on an ID card number. The function returns the gender based on an ID card number. The return value is M (male) or F (female).

```
STRING GET_IDCARD_SEX(STRING idcardno);
```

idcardno: required. The value must be of the STRING type and contain a 15-digit or 18-digit ID card number. The function checks the validity of the ID card number based on the province code and the last check digit during calculation. If the verification fails, the function returns NULL. The return value is of the STRING type. If the input value is NULL, the function returns NULL.

```
SELECT GET_IDCARD_SEX('ID card number'); -- Return result: The function returns the gender based on the actual ID card number, such as "M". SELECT GET_IDCARD_SEX(NULL); -- Return result +------+
| _c0  |
+------+
| NULL |
+------+
```

##### GREATEST

This topic describes how to use the GREATEST function in MaxCompute to return the maximum value among the input parameters. The function returns the maximum value among the input parameters.

```
GREATEST(var1, var2, ...);
```

var1: required. The data type can be BIGINT, DOUBLE, DECIMAL, DATETIME, or STRING. var2: required. The data type can be BIGINT, DOUBLE, DECIMAL, DATETIME, or STRING.

**Note**

If all parameter values are NULL, the function returns NULL. The function returns the maximum value among the input parameters. When no implicit type conversion occurs, the return value type is the same as the input parameter type. When type conversion occurs, the following rules apply: Comparisons among DOUBLE, BIGINT, and STRING types return the DOUBLE type; comparisons between STRING and DATETIME types return the DATETIME type; and comparisons between the DECIMAL type and the DOUBLE, BIGINT, or STRING type return the DECIMAL type. No other implicit type conversions are allowed. When SET odps.sql.hive.compatible=true; is configured, the function returns NULL if any input parameter is NULL.

```
SELECT GREATEST(1, 2, 3); -- Result +------+
| _c0  |
+------+
|  3   |
+------+ SELECT GREATEST('a', 'b', 'c'); -- Result +------+
| _c0  |
+------+
| c    |
+------+ SELECT GREATEST(NULL, 1, 2); -- Result +------+
| _c0  |
+------+
|  2   |
+------+
```

##### INDEX

This topic describes how to use the INDEX function in MaxCompute to return the element value at a specified position in an array or a map. If var1 is of the ARRAY type, the function returns the value of the var2-th element. If var1 is of the MAP<K, V> type, the function returns the value whose key is var2 in var1.

**Note**

When you use this function, omit INDEX and directly execute `var1[var2]` . Otherwise, a syntax error is returned. If **var1** is NULL, the function returns NULL.

```
INDEX(var1[var2]);
```

var1: required. This parameter must be of the ARRAY or MAP<K, V> type. var2: required. If var1 is of the ARRAY type, var2 must be of the BIGINT type and must be greater than or equal to 0. If var1 is of the MAP<K, V> type, var2 must be of the K type. If var1 is of the ARRAY type, the function returns a value of the T type. If var2 exceeds the number of elements in the array, the function returns NULL. If var1 is of the MAP<K, V> type, the function returns a value of the V type. If no key in the MAP<K, V> matches var2, the function returns NULL. If var1 is NULL, the function returns NULL.

```
-- When var1 is an array SELECT ARRAY('a', 'b', 'c')[2]; -- Result +-----+
| _c0 |
+-----+
| c   |
+-----+ -- When var1 is of the MAP<K, V> type SELECT STR_TO_MAP("test1=1,test2=2")["test1"]; -- Result +-----+
| _c0 |
+-----+
| 1   |
+-----+
```

##### MAX_PT

This topic describes how to use the MAX_PT function in MaxCompute to return the maximum value of a level-1 partition in a partitioned table and read the data files in the partition. For a partitioned table, this function returns the maximum value of a level-1 partition in lexicographic order and reads the data files in the partition.

```
MAX_PT(table_full_name);
```

table_full_name: required. This parameter must be of the STRING type. It specifies the table name, which must include the project name, such as prj.src. You must have read permissions on this table. This function returns the maximum value of a level-1 partition. If a new partition is added by using the ALTER TABLE statement but contains no data files, this partition will not be returned as a value.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbl (
    id BIGINT,
    name STRING
) PARTITIONED BY (pt STRING); -- Insert test data INSERT INTO tbl PARTITION (pt = '20120901') VALUES (1, 'Alice'); INSERT INTO tbl PARTITION (pt = '20120902') VALUES (2, 'Bob'); -- Query data in the maximum partition SELECT * FROM tbl WHERE pt = MAX_PT('myproject.tbl'); -- Return results +----+-------+----------+
| id | name  | pt       |
+----+-------+----------+
| 2  | Bob   | 20120902 |
+----+-------+----------+
```

##### ORDINAL

This topic describes the ORDINAL function and provides examples of using this function. Syntax:

```
ordinal(bigint nth, var1, var2, ...)
```

Description: This function sorts the input variables in ascending order, and returns the value in the **nth** bit. Parameters:
**nth**: a value of the BIGINT type. This parameter specifies the position in which the value is
to be returned. The value of this parameter starts from `1` . If the value of this parameter is null, null is returned.
**var**: a value of the BIGINT, DOUBLE, DATETIME, or STRING type.
Return value: The value in the **nth** bit is returned. If no implicit conversion is required, the return value is of the same data type as the input parameter. If a data type conversion is performed among the DOUBLE, BIGINT, and STRING types, a value of the DOUBLE type is returned. If a data type conversion is performed between the STRING and DATETIME types, a value of the DATETIME type is returned. Implicit conversions of other data types are not allowed. The value null is interpreted as the minimum value. Example:

```
-- The return value is 2. select ordinal(3, 1, 3, 2, 5, 2, 4, 6);
```

##### LEAST

This topic describes how to use the LEAST function in MaxCompute to return the minimum value among input parameters. This function returns the minimum value among the input parameters.

```
LEAST(var1, var2, ...);
```

var: required. This parameter must be of the BIGINT, DOUBLE, DECIMAL, DATETIME, or STRING type. If all parameter values are NULL, the function returns NULL. This function returns the minimum value among the input parameters. When no implicit conversion occurs, the return type is the same as the input parameter type. When type conversion occurs, the following rules apply: Comparisons among DOUBLE, BIGINT, and STRING types return a DOUBLE value; comparisons between STRING and DATETIME types return a DATETIME value; and comparisons between the DECIMAL type and the DOUBLE, BIGINT, or STRING type return a DECIMAL value. No other implicit type conversions are allowed. NULL is considered the minimum value.

```
SELECT LEAST(1, 2, 3); -- Result +------+
| _c0  |
+------+
|  1   |
+------+ SELECT LEAST('a', 'b', 'c'); -- Result +------+
| _c0  |
+------+
| a    |
+------+ SELECT LEAST(NULL, 1, 2); -- Result +------+
| _c0  |
+------+
|  1   |
+------+
```

##### SIZE

This topic describes how to use the SIZE function in MaxCompute to return the number of key-value pairs in a specified MAP or the number of elements in a specified ARRAY. SIZE(MAP) returns the number of key-value pairs in a specified MAP. SIZE(ARRAY) returns the number of elements in a specified ARRAY.

```
INT SIZE(MAP map); INT SIZE(ARRAY array);
```

map: required. This parameter must be of the MAP type. array: required. This parameter must be of the ARRAY type. The function returns a value of the INT type.

```
SELECT SIZE(MAP('a', 123, 'b', 456)); -- Return result +------+
| _c0  |
+------+
|  2   |
+------+ SELECT SIZE(MAP('a', 123, 'b', 456, 'c', 789)); -- Return result +------+
| _c0  |
+------+
|  3   |
+------+ SELECT SIZE(ARRAY('a', 'b')); -- Return result +------+
| _c0  |
+------+
|  2   |
+------+ SELECT SIZE(ARRAY(123, 456, 789)); -- Return result +------+
| _c0  |
+------+
|  3   |
+------+
```

##### SPLIT

This topic describes how to use the SPLIT function in MaxCompute to split a string with a specified delimiter and return an array. This function splits str by using pat and returns an array.

```
ARRAY<STRING> SPLIT(STRING str, STRING pat);
```

str: required. This parameter must be of the STRING type. It specifies the string to be split. pat: required. This parameter must be of the STRING type. It specifies the delimiter used for splitting, which supports regular expressions. The function returns a value of the ARRAY type. The return value contains the substrings that result from splitting str by pat.

```
SELECT SPLIT("a,b,c", ","); -- Result +-----------+
| _c0       |
+-----------+
| [a, b, c] |
+-----------+
```

##### STR_TO_MAP

This topic describes how to use the STR_TO_MAP function in MaxCompute to split a string into key-value pairs by using specified delimiters and return a MAP. This function uses delimiter1 to split text into key-value pairs and then uses delimiter2 to split the key and value of each key-value pair.

```
MAP<STRING, STRING> STR_TO_MAP(STRING text [, STRING delimiter1 [, STRING delimiter2]]);
```

text: required. This parameter must be of the STRING type. It specifies the string to be split. delimiter1: optional. This parameter must be of the STRING type. It specifies the delimiter. If you do not specify this parameter, the default value is a comma (,). delimiter2: optional. This parameter must be of the STRING type. It specifies the delimiter. If you do not specify this parameter, the default value is an equal sign (=). The return value is of the MAP<STRING, STRING> type. The function returns the result of splitting text by using delimiter1 and delimiter2.

```
SELECT STR_TO_MAP("test1=1,test2=2"); -- Result +------------------------+
| _c0                    |
+------------------------+
| {test1:1, test2:2}     |
+------------------------+
```

##### UUID

This topic describes how to use the UUID function in MaxCompute to return a random globally unique identifier (GUID). This function returns a random ID in the format of 29347a88-1e57-41ae-bb68a9edbdd94212. A UUID is a random GUID with a very low probability of duplication.

```
STRING UUID();
```

None. The function returns a value of the STRING type.

```
SELECT UUID(); -- Result +--------------------------------------+
| _c0                                  |
+--------------------------------------+
| 623b7436-f12c-486f-892a-e66f93679db5 |
+--------------------------------------+
```

##### UNIQUE_ID

This topic describes how to use the UNIQUE_ID function in MaxCompute to return a random unique ID. This function returns a random unique ID in the format of 29347a88-1e57-41ae-bb68a9edbdd94212_1. It runs more efficiently than the UUID function.

```
STRING UNIQUE_ID();
```

None. This function returns a value of the STRING type.

```
SELECT UNIQUE_ID(); -- Result +----------------------------------------+
| _c0                                    |
+----------------------------------------+
| 94465fb0-cb34-4156-8bcf-2d94c0f42730_0 |
+----------------------------------------+
```

##### SAMPLE

This topic describes how to use the SAMPLE function in MaxCompute to sample and filter data based on specified conditions. For all values in column_name, the SAMPLE function performs sampling based on the values of x and y, and filters out rows that do not meet the sampling conditions.

```
BOOLEAN SAMPLE(BIGINT x, BIGINT y [, column_name1, column_name2, ...]);
```

x: required. This parameter must be of the BIGINT type. The value must be an integer constant greater than 0. It indicates that the data is divided into x parts by hash, and the y-th part is selected. y: required. This parameter must be of the BIGINT type. The value must be an integer constant greater than 0. You can omit y. If you omit y, the function selects the first part by default. If you omit y, you must also omit column_name. column_name: optional. This parameter specifies the target column for sampling. You can omit this parameter. If you omit it, the function performs random sampling based on the values of x and y. The column can be of any type, and its values can be NULL. The function does not perform implicit type conversion. If column_name is a constant, an error is returned.

**Note**

If x or y is of a different type or has a value less than or equal to 0, an error is returned. If y is greater than x, an error is also returned. If either x or y is NULL, the function returns NULL. The function returns a value of the BOOLEAN type. To prevent data skew caused by NULL values, the function evenly distributes NULL values in column_name across x hash parts. If you do not specify column_name and the data volume is small, the output may not be evenly distributed. In such cases, we recommend that you specify column_name to obtain better results.

```
-- Create a table CREATE TABLE IF NOT EXISTS tbla (
    cola BIGINT,
    colb STRING
```

);

```
-- Insert test data INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (2, 'b'); INSERT INTO tbla VALUES (3, 'c'); INSERT INTO tbla VALUES (4, 'd'); INSERT INTO tbla VALUES (5, 'e'); INSERT INTO tbla VALUES (6, 'f'); INSERT INTO tbla VALUES (7, 'g'); INSERT INTO tbla VALUES (8, 'h'); -- Hash cola into 4 buckets and select the first bucket SELECT * FROM tbla WHERE SAMPLE(4, 1, cola) = true; -- Result (actual results vary based on hash distribution) +------+------+
| cola | colb |
+------+------+
| 4    | d    |
+------+------+ -- Randomly hash each row into 4 buckets and select the second bucket SELECT * FROM tbla WHERE SAMPLE(4, 2) = true; -- Result (actual results vary based on hash distribution) +------+------+
| cola | colb |
+------+------+
| 3    | c    |
| 5    | e    |
+------+------+
```

##### CASE WHEN expression

This topic describes how to use the CASE WHEN expression function in MaxCompute to return different values based on calculation results of expressions. The CASE WHEN expression returns different values based on the calculation result of the value expression. MaxCompute supports two syntax formats for the CASE WHEN expression:

```
-- Syntax 1 CASE value
  WHEN value1 THEN result1
  WHEN value2 THEN result2
  ...
  ELSE resultn
END; -- Syntax 2 CASE
  WHEN (_condition1) THEN result1
  WHEN (_condition2) THEN result2
  WHEN (_condition3) THEN result3
  ...
  ELSE resultn
END;
```

value: required. This parameter specifies the expression to be compared. value1, value2, ...: required. This parameter specifies the values to be compared with value. result1, result2, ...: required. This parameter specifies the results to return when value matches the corresponding values. _condition1, _condition2, ...: required. This parameter specifies the conditional expressions. resultn: optional. This parameter specifies the default value to be returned when no conditions match, which corresponds to the ELSE clause. If the result types include only BIGINT and DOUBLE, the system converts all results to the DOUBLE type before returning them. If the result types include STRING, the system converts all results to the STRING type before returning them. If the conversion fails, the system returns an error. For example, the system cannot convert the BOOLEAN type to the STRING type. The system does not allow conversions between other types.

```
-- Create a table CREATE TABLE IF NOT EXISTS sale_detail (
    shop_name STRING,
    sale_amount BIGINT
```

);

```
-- Insert test data INSERT INTO sale_detail VALUES ('hangzhou_shop', 100); INSERT INTO sale_detail VALUES ('shanghai_shop', 200); INSERT INTO sale_detail VALUES ('beijing_shop', 300); INSERT INTO sale_detail VALUES (NULL, 400); -- Determine the region based on the shop_name value SELECT
  CASE
    WHEN shop_name IS NULL THEN 'default_region'
    WHEN shop_name LIKE 'hang%' THEN 'zj_region'
  END AS region
FROM sale_detail; -- Output +---------------+
| region        |
+---------------+
| zj_region     |
| NULL          |
| NULL          |
| default_region|
+---------------+
```

##### IF

This topic describes how to use the IF function in MaxCompute to return different values based on a conditional expression and provides examples. The IF function returns a value based on whether a conditional expression evaluates to true or false.

```
IF(testCondition, valueTrue, valueFalseOrNull);
```

testCondition: This parameter must be of the BOOLEAN type. It specifies the expression to be evaluated. valueTrue: the value that the function returns when the **testCondition** expression evaluates to true. valueFalseOrNull: the value that the function returns when the **testCondition** expression does not evaluate to true. You can set this value to NULL. The return value has the same data type as either valueTrue or valueFalseOrNull.

```
SELECT IF(1=2,100,200); -- Result +--------+
|   _c0  |
+--------+
|   200  |
+--------+
```

##### Additional functions

###### Usage notes

This topic describes the configurations required for using other newly extended functions. After an upgrade to MaxCompute 2.0, MaxCompute provides other newly extended functions. To use these new functions in SQL statements, you must add the following SET statement.

```
SET odps.sql.type.system.odps2=true;
```

**Note**

You must submit and run the preceding SET statement and the SQL statements for the new functions at the same time.

###### MAP

This topic describes how to use the MAP function and provides reference examples. The MAP function creates a map from the specified key-value pairs.

```
MAP MAP(K key1, V value1, K key2, V value2, ...);
```

key: All **keys** must be of the same data type (including after implicit conversion) and must use primitive data types. value: All **values** must be of the same data type (including after implicit conversion) and can be of any data type. The function returns a value of the MAP type.

```
CREATE TABLE IF NOT EXISTS t_table (
    c1 BIGINT,
    c2 STRING,
    c3 STRING,
    c4 BIGINT,
    c5 BIGINT
```

);

```
INSERT INTO t_table VALUES (1000, 'k11', 'k21', 86, 15), (1001, 'k12', 'k22', 97, 2), (1002, 'k13', 'k23', 99, 1); SELECT map(c2,c4,c3,c5) FROM t_table; -- Output +------------------+
|        _c0       |
+------------------+
| {k11:86, k21:15} |
| {k12:97, k22:2}  |
| {k13:99, k23:1}  |
+------------------+
```

###### MAP_KEYS

This topic describes how to use the MAP_KEYS function in MaxCompute to return all keys in a map as an array. This function returns all keys in a map as an array.

```
ARRAY MAP_KEYS(MAP<K, V> map);
```

map: required. This parameter must be of the MAP type. This function returns a value of the ARRAY type. If the input is NULL, the function returns NULL.

```
-- Create a table CREATE TABLE IF NOT EXISTS t_table_map (
    c1 BIGINT,
    t_map MAP<STRING, BIGINT>
```

);

```
-- Insert test data INSERT INTO t_table_map VALUES (1000, MAP('k11', 86, 'k21', 15)); INSERT INTO t_table_map VALUES (1001, MAP('k12', 97, 'k22', 2)); INSERT INTO t_table_map VALUES (1002, MAP('k13', 99, 'k23', 1)); SELECT c1, MAP_KEYS(t_map) FROM t_table_map; -- Return results +------+--------------+
| c1   | _c1          |
+------+--------------+
| 1000 | [k11, k21]   |
| 1001 | [k12, k22]   |
| 1002 | [k13, k23]   |
+------+--------------+
```

###### MAP_VALUES

This topic describes how to use the MAP_VALUES function in MaxCompute to return all values in a map as an array. This function returns all values in a map as an array.

```
ARRAY MAP_VALUES(MAP<K, V> map);
```

map: required. This parameter must be of the MAP type. The return value is of the ARRAY type. If the input is NULL, the function returns NULL.

```
SELECT MAP_VALUES(MAP('a', 123, 'b', 456)); -- Result +------------+
| _c0        |
+------------+
| [123, 456] |
+------------+
```

###### SORT_ARRAY

This topic describes how to use the SORT_ARRAY function in MaxCompute to sort the data in a specified array. This function sorts data in a specified array.

```
ARRAY SORT_ARRAY(ARRAY<T>);
```

ARRAY: required. This parameter must be of the ARRAY type. The elements in the array can be of any type. This function returns a value of the ARRAY type.

```
-- Create a table. CREATE TABLE IF NOT EXISTS t_array (
    c1 ARRAY<STRING>,
    c2 ARRAY<INT>,
    c3 ARRAY<STRING>
```

);

```
-- Insert test data. INSERT INTO t_array VALUES (ARRAY('a', 'c', 'f', 'b'), ARRAY(4, 5, 7, 2, 5, 8), ARRAY ('you', 'me', 'him')); SELECT SORT_ARRAY(c1), SORT_ARRAY(c2), SORT_ARRAY(c3) FROM t_array; -- Return result +-----------------+---------------------+-----------------+
| _c0             | _c1                 | _c2             |
+-----------------+---------------------+-----------------+
| [a, b, c, f]    | [2, 4, 5, 5, 7, 8] | [him, me, you]  |
+-----------------+---------------------+-----------------+
```

###### POSEXPLODE

This topic describes how to use the POSEXPLODE function in MaxCompute to expand a given ARRAY into multiple rows of data with subscripts. The function expands a given ARRAY and generates one row for each value. Each row consists of two columns, which represent the zero-based subscript and the array element, respectively.

```
POSEXPLODE(ARRAY<T>);
```

ARRAY: required. This parameter must be of the ARRAY type. The elements in the array can be of any type. The function returns a table that contains two columns: pos (the 0-based subscript) and val (the array element).

```
SELECT POSEXPLODE(ARRAY('a', 'c', 'f', 'b')); -- Result +-----+-----+
| pos | val |
+-----+-----+
| 0   | a   |
| 1   | c   |
| 2   | f   |
| 3   | b   |
+-----+-----+
```

###### STRUCT

This topic describes how to use the STRUCT function in MaxCompute to create a STRUCT from a specified list of values. This function creates a STRUCT from a specified list of values.

```
STRUCT STRUCT(value1, value2, ...);
```

value: required. Each value can be of any data type. The function returns a value of the STRUCT type. The field names are col1, col2, and so on.

```
SELECT STRUCT('a', 123, 'true', 56.90); -- Result +------------------------------------------+
| _c0                                      |
+------------------------------------------+
| {col1:a, col2:123, col3:true, col4:56.9} |
+------------------------------------------+
```

###### NAMED_STRUCT

This topic describes how to use the NAMED_STRUCT function in MaxCompute to create a STRUCT from a given list of name and value pairs. This function creates a STRUCT from a given list of name and value pairs.

```
STRUCT NAMED_STRUCT(STRING name1, T1 value1, STRING name2, T2 value2, ...);
```

name: required. This parameter specifies the name of the field. The value must be a STRING constant. value: required. This parameter specifies the value of the field. The value can be of any data type. This function returns a value of the STRUCT type. The field names are name1, name2, and so on in sequence.

```
SELECT NAMED_STRUCT('user_id', 10001, 'user_name', 'bob', 'married', 'F', 'weight', 6 3.50); -- Return result +------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| {user_id:10001, user_name:bob, married:F, weight:63.5}    |
+------------------------------------------------------------+
```

###### INLINE

This topic describes how to use the INLINE function in MaxCompute to expand a given STRUCT array into multiple rows and columns. The function expands a given STRUCT array, where each array element corresponds to a row and each STRUCT element within the row corresponds to a column.

```
INLINE(ARRAY<STRUCT<f1:T1, f2:T2, ...>>);
```

STRUCT: required. The values in the array can be of any data type. This function generates a table.

```
-- Create a table CREATE TABLE IF NOT EXISTS t_table (
    t_struct STRUCT<user_id:BIGINT, user_name:STRING, married:STRING, weight:DOUBLE>
```

);

```
-- Insert test data INSERT INTO t_table VALUES (NAMED_STRUCT('user_id', 10001, 'user_name', 'LiLei', 'mar ried', 'N', 'weight', 63.5)); INSERT INTO t_table VALUES (NAMED_STRUCT('user_id', 10002, 'user_name', 'HanMeiMei', 'married', 'Y', 'weight', 43.5)); SELECT INLINE(ARRAY(t_struct)) FROM t_table; -- Results +---------+-----------+---------+--------+
| user_id | user_name | married | weight |
+---------+-----------+---------+--------+
| 10001   | LiLei     | N       | 63.5   |
| 10002   | HanMeiMei | Y       | 43.5   |
+---------+-----------+---------+--------+
```

###### BETWEEN AND expression

This topic describes how to use the BETWEEN AND expression function in MaxCompute to determine whether a value falls within a specified range. If A, B, or C is null, the result is null. If A is greater than or equal to B and less than or equal to C, the result is true. Otherwise, the result is false.

```
A [NOT] BETWEEN B AND C;
```

A: required. This parameter specifies the expression to be evaluated. B: required. This parameter specifies the lower bound of the range. C: required. This parameter specifies the upper bound of the range. This function returns a value of the BOOLEAN type. If A, B, or C is null, the function returns NULL. If A is greater than or equal to B and less than or equal to C, the function returns true. Otherwise, the function returns false.

```
-- Create a table CREATE TABLE IF NOT EXISTS emp (
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
hiredateDATETIME
```

```
    hiredate DATETIME,
    sal DOUBLE,
    comm DOUBLE,
    deptno BIGINT
```

);

```
-- Insert test data INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME '1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME '1981-02-20 00:00:0 0', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME '1981-02-22 00:00:00 ', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME '1981-04-02 00:00:00 ', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME '1981-09-28 00:00: 00', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME '1981-05-01 00:00:00 ', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME '1981-06-09 00:00:00 ', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME '1987-04-19 00:00:00 ', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME '1981-11-17 00:00:0 0', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME '1981-09-08 00:00: 00', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME '1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME '1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME '1981-12-03 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME '1982-01-23 00:00:00' , 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME '1981-04-12 00:00:00' , 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME '1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME '1982-12-30 00:00:00' , 1300, NULL, 10); -- Query data where sal is greater than or equal to 1000 and less than or equal to 15 SELECT * FROM emp WHERE sal BETWEEN 1000 AND 1500; -- Return results +-------+--------+----------+------+---------------------+--------+--------+--------+
| empno | ename  | job      | mgr  | hiredate            | sal    | comm   | deptno |
+-------+--------+----------+------+---------------------+--------+--------+--------+
| 7521  | WARD   | SALESMAN | 7698 | 1981-02-22 00:00:00 | 1250.0 | 500.0  | 30     |
| 7654  | MARTIN | SALESMAN | 7698 | 1981-09-28 00:00:00 | 1250.0 | 1400.0 | 30     |
| 7844  | TURNER | SALESMAN | 7698 | 1981-09-08 00:00:00 | 1500.0 | 0.0    | 30     |
| 7876  | ADAMS  | CLERK    | 7788 | 1987-05-23 00:00:00 | 1100.0 | NULL   | 20     |
| 7934  | MILLER | CLERK    | 7782 | 1982-01-23 00:00:00 | 1300.0 | NULL   | 10     |
```

|
|
|
|
|
|
|
|
|

```
| 7956  | TEBAGE | CLERK    | 7748 | 1982-12-30 00:00:00 | 1300.0 | NULL   | 10     |
+-------+--------+----------+------+---------------------+--------+--------+--------+
```

###### NVL

When you need to replace a NULL value with a specific value in a query, you can use the NVL function in MaxCompute to replace the NULL value with a specified value. This prevents unexpected null values in the results during data analysis or report generation. This topic describes how to use the NVL function in MaxCompute. If the value is NULL, the function returns default_value. Otherwise, it returns value. The two parameters of this function must be of the same type.

```
NVL(T value, T default_value);
```

value: required. This parameter specifies an input parameter. T represents the input data type and can be any data type that MaxCompute supports. default_value: required. This parameter specifies the replacement value. The data type of this parameter must be the same as the data type of value. If the value is NULL, the function returns default_value. Otherwise, it returns value.

```
-- Create a table CREATE TABLE nvl_test (
    c1 STRING,
    c2 BIGINT,
    c3 DATETIME
```

);

```
-- Insert test data INSERT INTO nvl_test VALUES ('aaa', 23, DATETIME '2024-01-11 00:00:00'); INSERT INTO nvl_test VALUES ('bbb', NULL, DATETIME '2024-01-12 08:00:00'); INSERT INTO nvl_test VALUES (NULL, 20, DATETIME '2024-01-13 05:00:00'); INSERT INTO nvl_test VALUES ('ddd', 25, NULL); SELECT NVL(c1, '00000'), NVL(c2, 0), NVL(c3,'-') FROM nvl_test; -- Output +-------+------------+--------------------+
| _c0   | _c1        | _c2                 |
+-------+------------+---------------------+
| ddd   | 25         | -                   |
| 00000 | 20         | 2024-01-13 05:00:00 |
| aaa   | 23         | 2024-01-11 00:00:00 |
| bbb   | 0          | 2024-01-12 08:00:00 |
+-------+--------+-------------------------+
```

###### TABLE_EXISTS

This topic describes how to use the TABLE_EXISTS function in MaxCompute to query whether a specified table exists. This function queries whether a specified table exists.

```
BOOLEAN TABLE_EXISTS(STRING table_name);
```

table_name: required. This parameter specifies the name of the table. It must be of the STRING type. You can specify the project name in the table name (for example, my_proj.my_table). If you do not specify a project name, the system uses the current project by default. This function returns a value of the BOOLEAN type. It returns True if the specified table exists. Otherwise, the function returns False.

```
-- Create a table CREATE TABLE IF NOT EXISTS abd (
    col1 STRING,
    col2 STRING
```

);

```
-- Insert test data INSERT INTO abd VALUES ('value1', 'value2'); -- Use TABLE_EXISTS in a SELECT list SELECT IF(TABLE_EXISTS('abd'), col1, col2) FROM abd; -- Result +--------+
| _c0    |
+--------+
| value1 |
+--------+
```

###### PARTITION_EXISTS

This topic describes how to use the PARTITION_EXISTS function in MaxCompute to check whether a specified partition exists. This function checks whether a specified partition exists.

```
BOOLEAN PARTITION_EXISTS(STRING table_name, STRING... partitions);
```

table_name: required. This parameter specifies the name of the table. It must be of the STRING type. You can specify a project name in the table name, such as my_project.my_table. If you do not specify a project name, the system uses the current project by default. partitions: required. This parameter specifies the partition names. It must be of the STRING type. The partition values must be specified in the order of the partition columns in the table, and the number of partition values must match the number of partition columns. This function returns a value of the BOOLEAN type. If the specified partition exists, the function returns `true` . Otherwise, the function returns `false` .

```
-- Create a partitioned table named foo CREATE TABLE IF NOT EXISTS foo (
    id BIGINT
) PARTITIONED BY (ds STRING, hr STRING); -- Add a partition to the partitioned table foo ALTER TABLE foo ADD PARTITION (ds = '20190101', hr = '1'); -- Check whether the partition where ds='20190101' and hr='1' exists SELECT PARTITION_EXISTS('foo', '20190101', '1'); -- Returned result +-------+
| _c0   |
+-------+
| true  |
+-------+
```

### UDFs

#### Java UDFs

##### Overview

This topic describes the categories, invocation rules, and cross-project usage of User-Defined Functions (UDFs) in MaxCompute. When built-in functions do not meet your business requirements, you can extend SQL computing capabilities by using UDFs.

**Feature overview**

MaxCompute provides various built-in functions to meet your computing requirements, and you can also create UDFs to address additional computing needs. You use UDFs in a similar way to built-in functions. For the mapping between Java and MaxCompute data types, see Parameters and return value types.

|   | Note When a UDF has the same name as a built-in function, use the select ::function name(expression) ; statement to call the built-in function. For example, if _ MaxCompute contains a UDF named CONCAT, the system calls this UDF by default instead of the built-in CONCAT function. To call the built-in CONCAT function, execute the select ::concat('ab', 'c') ; statement. |   |   |
|---|---|---|---|
|   |   | select |   |
|   | ::function name(expression) ; _ |   |   |

**UDF categories**

MaxCompute supports three types of UDFs, as described in the following table.

| UDF category | Description |
|---|---|

| UDF | A user-defined scalar function. It has a one-to-one mapping between input and output, meaning it reads one row of data and writes one output value. |
|---|---|
| UDTF | A User-Defined Table-Valued Function (UDTF). It addresses the need to output multiple rows of data from a single function call. It is the only type of UDF that can return multiple fields. A UDTF is different from a UDT. |
| UDAF | A User Defined Aggregation Function (UDAF). It has a many-to-one mapping between input and output, meaning it aggregates multiple input records into one output value. You can use it together with the GROUP BY statement in SQL. |

**Note**

When you use UDFs in SQL statements, the system may report an out-of-memory (OOM) error. This occurs when the data volume is excessively large and data skew exists, causing the task to exceed the default allocated memory. In this case, you can use the set odps.sql.udf.joiner.jvm.memory=xxxx; statement to manually configure the memory and resolve this issue. MaxCompute UDFs support cross-project sharing, which allows you to use a UDF from Project B in Project A. The SQL statement for cross-project sharing is as follows.

```
SELECT other_project:udf_in_other_project(arg0, arg1) AS res FROM table_t;
```

**Note**

`other_project` : the name of the project where the UDF resides. `udf_in_other_project` : the name of the UDF registered in the `other_project` project.

**Obtain SDK dependencies**

If you use Maven, you can search for `odps-sdk-udf` in the Maven repository to obtain the SDK dependency version.

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>odps-sdk-udf</artifactId>
   <version>0.29.10-public</version>
</dependency>
```

##### Parameters and return value types

This topic describes the parameters and return value types of UDFs in MaxCompute and the mapping rules between Java data types and MaxCompute data types. This information helps you accurately declare types for UDFs and avoid runtime errors or data precision loss due to data type mismatches.

**Feature description**

After an upgrade to MaxCompute 2.0, Java UDFs support more data types in addition to the original BIGINT, STRING, DOUBLE, and BOOLEAN types. The upgrade also adds support for complex types such as ARRAY, MAP, STRUCT, and Writable.

**Usage notes for new data types**

You can use new data types in UDFs by using the following methods: UDAFs and UDTFs obtain signatures through the **@Resolve** annotation, such as

```
 @Resolve("smallint->varchar(10)") .
```

UDFs obtain signatures by analyzing the **evaluate** method through reflection. In this case, MaxCompute built-in types and Java types follow a one-to-one mapping relationship.

**Important**

You can use `type,*` to accept any number of parameters, such as @resolve("string,*->array<string>"). Note that you must add a subtype after array. Reflection cannot determine the field name and field type of com.aliyun.odps.data.Struct, so you must use the @Resolve annotation for assistance. If you need to use struct in a UDF, you must also add the @Resolve annotation to the UDF class. This annotation only affects overloads whose parameters or return values include com.aliyun.odps.data.Struct. Currently, a class can have only one @Resolve annotation. Therefore, a UDF can have only one overload that contains struct parameters or return values.

**Usage notes for complex types**

You can use complex types in UDFs by using the following methods: UDTFs specify signatures through the **@Resolve** annotation, such as

| @Resolve("array<string>,struct<a1:bigint,b1:string>,string- |   |
|---|---|
|   | . |

UDFs map input and output types through the signature of the **evaluate** method. In this case, refer to the mapping relationship between MaxCompute types and Java types. The mappings are as follows: ARRAY maps to **java.util.List**. MAP maps to **java.util.Map**. STRUCT maps to **com.aliyun.odps.data.Struct**. UDAFs obtain signatures through the **@Resolve** annotation, such as `@Resolve("smallint-`

```
>varchar(10)") .
```

**Data type mappings**

The following table describes the mappings between MaxCompute data types and Java data types.

| MaxCompute type | Java type |
|---|---|
| TINYINT | java.lang.Byte |
| SMALLINT | java.lang.Short |
| INT | java.lang.Integer |
| BIGINT | java.lang.Long |
| FLOAT | java.lang.Float |
| DOUBLE | java.lang.Double |
| DECIMAL | java.math.BigDecimal |
| BOOLEAN | java.lang.Boolean |
| STRING | java.lang.String |
| VARCHAR | com.aliyun.odps.data.Varchar |
| BINARY | com.aliyun.odps.data.Binary |
| DATETIME | java.util.Date |
| TIMESTAMP | java.sql.Timestamp |
| ARRAY | java.util.List |
| MAP | java.util.Map |
| STRUCT | com.aliyun.odps.data.Struct |

**Note**

You must use Java types for input or output parameters in UDFs. Otherwise, the ODPS-0130071 error occurs. The corresponding Java data types and return value data types are objects, so the first letter of a data type must be uppercase. NULL values in SQL map to NULL references in Java. Therefore, you cannot use Java primitive types because they cannot represent NULL values in SQL. The Java type that corresponds to the ARRAY type is List, not an array.

**Writable type mappings**

MaxCompute 2.0 allows you to use Writable types as parameters and return values when you define Java UDFs. The following table shows the mappings between MaxCompute data types and Java Writable types.

| MaxCompute type | Java Writable type |
|---|---|
| TINYINT | ByteWritable |
| SMALLINT | ShortWritable |
| INT | IntWritable |
| BIGINT | LongWritable |
| FLOAT | FloatWritable |
| DOUBLE | DoubleWritable |
| DECIMAL | BigDecimalWritable |
| BOOLEAN | BooleanWritable |
| STRING | Text |
| VARCHAR | VarcharWritable |
| BINARY | BytesWritable |
| DATETIME | DatetimeWritable |

| TIMESTAMP | TimestampWritable |
|---|---|
| INTERVAL YEAR MONTH _ _ | IntervalYearMonthWritable |
| INTERVAL DAY TIME _ _ | IntervalDayTimeWritable |
| ARRAY | N/A |
| MAP | N/A |
| STRUCT | N/A |

##### UDF

This topic describes user-defined scalar functions (UDFs) and provides reference examples.

**Usage notes**

To implement a UDF, you must extend the **com.aliyun.odps.udf.UDF** class and implement the **evaluate** method. The **evaluate** method must be a non-static `public` method. The parameter types and return value type of the **evaluate** method serve as the function signature of the UDF in SQL. You can implement multiple **evaluate** methods in a UDF. When you call the UDF, the framework matches the correct **evaluate** method based on the parameter types of the UDF call.

**Note**

Do not include classes with the same name but different implementation logic in different JAR packages. For example, if **UDF(UDAF/UDTF): udf1 and udf2** correspond to the resources **udf1.jar** and **udf2.jar** respectively, and both JAR packages contain a **com.aliyun.UserFunction** class, the system randomly loads one of the classes when a single SQL statement uses both UDFs. This causes inconsistent UDF execution behavior or even compilation failures. If a single SQL statement uses two UDFs, the two UDFs share one classpath during execution without isolation. If the resources referenced by both UDFs contain the same class, the class that the classloader references is unpredictable. Therefore, avoid using the same class in different resources. You can implement `void setup(ExecutionContext ctx)` and `void close()` to define the initialization and termination code of a UDF respectively.

**Java type**

The following example uses a Java type to convert an input string to lowercase.

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.udf.UDF; public final class Lower extends UDF {
    public String evaluate(String s) {
        if (s == null) {
            return null;
```

`}`

```
        return s.toLowerCase();
```

`}` `}`

**Java Writable type**

The following example uses the Writable type to implement Concat.

```java
package com.aliyun.odps.udf.example; import com.aliyun.odps.io.Text; import com.aliyun.odps.udf.UDF; public class MyConcat extends UDF {
    private Text ret = new Text();
    public Text evaluate(Text a, Text b) {
        if (a == null || b == null) {
            return null;
```

`}`

```
        ret.clear();
        ret.append(a.getBytes(), 0, a.getLength());
        ret.append(b.getBytes(), 0, b.getLength());
        return ret;
```

`}` `}`

##### UDAF

This topic describes user-defined aggregation functions (UDAFs) among UDFs and provides reference examples.

**Usage notes**

To implement a UDAF class, extend the **com.aliyun.odps.udf.Aggregator** class and implement the following methods.

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.ContextFunction; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; public abstract class Aggregator implements ContextFunction {
    @Override
    public void setup(ExecutionContext ctx) throws UDFException {
```

`}`

```java
    @Override
    public void close() throws UDFException {
```

`}`

```
    /**
     * Creates an aggregation buffer. * @return Writable The aggregation buffer.
```

`*/`

```
    abstract public Writable newBuffer();
    /**
     * @param buffer The aggregation buffer. * @param args The parameters specified whe
n you call the UDAF in SQL. This parameter cannot be null, but elements in args can be null, which indicates that the corresponding input data is null. * @throws UDFException.
```

`*/`

```
    abstract public void iterate(Writable buffer, Writable[] args) throws UDFException;
    /**
     * Generates the final result. * @param buffer * @return Object The final result of
the UDAF. * @throws UDFException.
```

`*/`

```
    abstract public Writable terminate(Writable buffer) throws UDFException;
    abstract public void merge(Writable buffer, Writable partial) throws UDFException;
```

`}`

**Implementation process**

The three most important methods are **iterate**, **merge**, and **terminate**. The core logic of a UDAF depends on the implementation of these three methods. In addition, you must implement a custom Writable buffer. The average function (**avg**) is used as an example.The following figure briefly describes the implementation logic and computing process of the **avg** function in MaxCompute UDAF. iterate(a): r.count += 1; r.sum += a; terminate: r.sum/r.count merge(PartialResult pr): 4.2 r.count += pr.count; r.sum += pr.sum; iterate(a): r.count += 1; In the preceding figure, the system splits input data into shards of a specific size. Each shard has a size suitable for a worker to process within an appropriate time period. You must manually configure the shard size. The UDAF computing process consists of two phases: Phase 1: Each worker counts the number of data records and calculates the sum within a shard. You can regard the record count and sum within each shard as an intermediate result. Phase 2: A worker aggregates the information from each shard produced in the previous phase. In the final output, **r.sum / r.count** represents the average value of all input data. The following example shows a UDAF that calculates the average value.

```java
package org.alidata.odps.udf.examples; import java.io.DataInput; import java.io.DataOutput; import java.io.IOException; import com.aliyun.odps.io.DoubleWritable; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.Aggregator; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve("double->double") public class AggrAvg extends Aggregator {
    private static class AvgBuffer implements Writable {
        private double sum = 0;
        private long count = 0;
        @Override
        public void write(DataOutput out) throws IOException {
            out.writeDouble(sum);
            out.writeLong(count);
```

`}`

```java
        @Override
        public void readFields(DataInput in) throws IOException {
            sum = in.readDouble();
            count = in.readLong();
```

`}` `}` `}`

```java
    private DoubleWritable ret = new DoubleWritable();
    @Override
    public Writable newBuffer() {
        return new AvgBuffer();
```

`}`

```java
    @Override
    public void iterate(Writable buffer, Writable[] args) throws UDFException {
        DoubleWritable arg = (DoubleWritable) args[0];
        AvgBuffer buf = (AvgBuffer) buffer;
        if (arg != null) {
            buf.count += 1;
            buf.sum += arg.get();
```

`}` `}`

```java
    @Override
    public Writable terminate(Writable buffer) throws UDFException {
        AvgBuffer buf = (AvgBuffer) buffer;
        if (buf.count == 0) {
            ret.set(0);
        } else {
            ret.set(buf.sum / buf.count);
```

`}`

```
        return ret;
```

`}`

```java
    @Override
    public void merge(Writable buffer, Writable partial) throws UDFException {
        AvgBuffer buf = (AvgBuffer) buffer;
        AvgBuffer p = (AvgBuffer) partial;
        buf.sum += p.sum;
        buf.count += p.count;
```

`}` `}`

##### UDTFs

###### Overview

This topic describes User-Defined Table-Valued Functions (UDTFs) and provides reference examples.

**Usage notes**

A UDTF must extend the **com.aliyun.odps.udf.UDTF** class. This class requires you to implement the following four methods.

| API definition | Description |
|---|---|
| public void setup(ExecutionContext ctx) throws UDFException | The initialization method. The system calls this method to run your custom initialization logic before the UDTF processes input data. The system calls setup once in each worker. |
| public void process(Object[] args) throws UDFException | The framework calls this method once for each record in the SQL statement. The parameters of process are the UDTF input parameters that the SQL statement specifies. The system passes input parameters as an Object[] array, and you use the forward function to produce output. You must call forward within the process function to determine the output data. |
| public void close() throws UDFException | The termination method of the UDTF. The framework calls this method only once after it processes the last record. |
| public void forward(Object …o) throws UDFException | The system calls the forward method to output data. Each call to forward produces one output record. The columns that the AS clause of the UDTF in the SQL statement specifies must match the columns in this record. |

1. Prepare the sample code.

```java
package org.alidata.odps.udtf.examples; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.annotation.Resolve; import com.aliyun.odps.udf.UDFException; @Resolve("string,bigint->string,bigint") public class MyUDTF extends UDTF {
    @Override
    public void process(Object[] args) throws UDFException {
        String a = (String) args[0];
        Long b = (Long) args[1];
        for (String t : a.split("\\s+")) {
            forward(t, b);
```

`}` `}` `}`
2. Register the UDTF.
Assume that the registered function name is `user_udtf` when you create a UDTF in MaxCompute.
3. Use the UDTF.
Execute the following statements to use the UDTF.

```
CREATE TABLE IF NOT EXISTS my_table (
    col0 STRING,
    col1 BIGINT
```

);

```
INSERT INTO TABLE my_table VALUES ('A B', 1), ('C D', 2); SELECT user_udtf(col0, col1) AS (c0, c1) FROM my_table; -- Output +----+------------+
| c0 | c1         |
+----+------------+
| A  | 1          |
| B  | 1          |
| C  | 2          |
| D  | 2          |
+----+------------+
```

###### Examples of using UDTFs

This topic provides examples of using UDTFs.

**Use a UDTF to read resources in MaxCompute**

You can use a UDTF to read resources in MaxCompute. Example:
1. Compile a UDTF program. After the compilation is successful, export the JAR package. In
this example, the JAR package is named udtfexample1.jar.

```java
package com.aliyun.odps.examples.udf; import java.io.BufferedReader; import java.io.IOException; import java.io.InputStream; import java.io.InputStreamReader; import java.util.Iterator; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.annotation.Resolve; /**
 * project: example_project
 * table: wc_in2
 * partitions: p2=1,p1=2
 * columns: colc,colb
```

`*/`

```java
@Resolve("string,string->string,bigint,string") public class UDTFResource extends UDTF {
  ExecutionContext ctx;
  long fileResourceLineCount;
  long tableResource1RecordCount;
  long tableResource2RecordCount;
```

`g`

```java
  @Override
  public void setup(ExecutionContext ctx) throws UDFException {
  this.ctx = ctx;
  try {
   InputStream in = ctx.readResourceFileAsStream("file_resource.txt");
   BufferedReader br = new BufferedReader(new InputStreamReader(in));
   String line;
   fileResourceLineCount = 0;
   while ((line = br.readLine()) ! = null) {
     fileResourceLineCount++;
```

`}`

```
   br.close();
   Iterator<Object[]> iterator = ctx.readResourceTable("table_resource1").iterator();
   tableResource1RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource1RecordCount++;
     iterator.next();
```

`}`

```
   iterator = ctx.readResourceTable("table_resource2").iterator();
   tableResource2RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource2RecordCount++;
     iterator.next();
```

`}`

```
 } catch (IOException e) {
   throw new UDFException(e);
```

`}` `}`

```java
   @Override
   public void process(Object[] args) throws UDFException {
     String a = (String) args[0];
     long b = args[1] == null ? 0 : ((String) args[1]).length();
     forward(a, b, "fileResourceLineCount=" + fileResourceLineCount +
"|tableResource1RecordCount="
     + tableResource1RecordCount + "|tableResource2RecordCount=" +
tableResource2RecordCount);
```

`}` `}`
2. Add resources to MaxCompute.

```
Add file file_resource.txt; Add jar udtfexample1.jar; Add table table_resource1 as table_resource1; Add table table_resource2 as table_resource2;
```

3. Create the my_udtf UDTF in MaxCompute.

```
create function mp_udtf as com.aliyun.odps.examples.udf.UDTFResource using 'udtfexample1.jar, file_resource.txt, table_resource1, table_resource2';
```

4. Run this UDTF.

```
select mp_udtf("10","20") as (a, b, fileResourceLineCount) from table_resource1;
```

Returned result:

```
+-------+------------+-------+
| a | b      | fileResourceLineCount |
+-------+------------+-------+
| 10    | 2          |
fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 |
| 10    | 2          |
fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 | +-------+------------+-------+
```

**Use complex data types in a UDF**

The following example defines a UDF with three overloads. The first overload uses the ARRAY type, the second overload uses the MAP type, and the third overload uses the STRUCT type. The third overload uses STRUCT as the data type of parameters or returned values. Therefore, the **@Resolve** annotation must be added to the UDF class to specify the STRUCT type.

```java
import com.aliyun.odps.udf.UDF; import com.aliyun.odps.udf.annotation.Resolve; @Resolve("struct,string->string") public class UdfArray extends UDF {
    public String evaluate(List vals, Long len) {
        return vals.get(len.intValue());
```

`}`

```
    public String evaluate(Map map, String key) {
        return map.get(key);
```

`}`

```
    public String evaluate(Struct struct, String key) {
        return struct.getFieldValue("a") + key;
```

`}` `}` You can pass complex data types into a UDF.

```
create function my_index as 'UdfArray' using 'myjar.jar'; select id, my_index(array('red', 'yellow', 'green'), colorOrdinal) as color_name from c
```

`o`

**Use Hive UDFs**

MaxCompute V2.0 supports Hive UDFs. Some Hive UDFs and UDTFs can be directly used in MaxCompute.

**Note**

MaxCompute V2.0 is compatible with Hive 2.1.0 and Hadoop 2.7.2. If you develop a UDF by using other versions of Hive or Hadoop, you may need to recompile the UDF on the compatible Hive or Hadoop version. The following example shows how to use a Hive UDF in MaxCompute:

```java
package com.aliyun.odps.compiler.hive; import org.apache.hadoop.hive.ql.exec.UDFArgumentException; import org.apache.hadoop.hive.ql.metadata.HiveException; import org.apache.hadoop.hive.ql.udf.generic.GenericUDF; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspector; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspectorFactory; import java.util.ArrayList; import java.util.List; import java.util.Objects; public class Collect extends GenericUDF {
  @Override
  public ObjectInspector initialize(ObjectInspector[] objectInspectors) throws UDFArgum
entException {
    if (objectInspectors.length == 0) {
      throw new UDFArgumentException("Collect: input args should >= 1");
```

`}`

```
    for (int i = 1; i < objectInspectors.length; i++) {
      if (objectInspectors[i] ! = objectInspectors[0]) {
        throw new UDFArgumentException("Collect: input oi should be the same for all ar
gs");
```

`}` `}`

```
    return ObjectInspectorFactory.getStandardListObjectInspector(objectInspectors[0]);
```

`}`

```java
  @Override
  public Object evaluate(DeferredObject[] deferredObjects) throws HiveException {
    List<Object> objectList = new ArrayList<>(deferredObjects.length);
    for (DeferredObject deferredObject : deferredObjects) {
      objectList.add(deferredObject.get());
```

`}`

```
    return objectList;
```

`}`

```java
  @Override
  public String getDisplayString(String[] strings) {
    return "Collect";
```

`}` `}` The Hive UDF in the example packages any type and number of parameters into arrays. In this example, the output JAR package is named test.jar.

```
-- Add a resource. Add jar test.jar; -- Create a Hive UDF. CREATE FUNCTION hive_collect as 'com.aliyun.odps.compiler.hive.Collect' using 'test.jar
```

';

```
-- Use the Hive UDF. set odps.sql.hive.compatible=true; select hive_collect(4y,5y,6y) from dual;
```

Returned result:

```
+------+
| _c0  |
+------+
| [4, 5, 6] |
+------+
```

**Note**

Take note of the following items when you use Hive UDFs that are compatible with MaxCompute: Specify the JAR package when you create a Hive UDF. MaxCompute cannot automatically add all JAR packages to the classpath. The `add jar` command in MaxCompute creates a permanent resource in the project. Insert set odps.sql.hive.compatible=true; before an SQL statement, and commit and execute the SET statement with the SQL statement. Pay attention to the limits imposed by the Java sandbox on MaxCompute.

#### Python UDFs

##### Prerequisites

This topic describes the prerequisites for using Python UDFs. Before you use Python UDFs, you must enable the isolation sandbox feature for your project. To do this, navigate to project management in adminconsole and set **ISOLATION SETTING >**
**odps.isolation.enable** to True.

**Note**

The Python UDF feature currently is supported only in the Job Scheduler (sp44 kernel) version. The Unified Scheduling (sp52 kernel) version does not support this feature. To use Python UDFs in the Unified Scheduling version, submit a ticket.

##### Usage limits

This topic describes the limits of using Python UDFs.

**Limits**

MaxCompute uses Python 2.7 to run Python UDFs. User code is executed in a sandbox mode, which means the code runs in a restricted environment. In this environment, the following operations are prohibited: Reads or writes local files. Starts subprocesses. Starts threads. Uses socket connections. Makes other system calls. For these reasons, all uploaded code must be implemented using standard Python, and C extension modules are not allowed.

**Available modules**

In addition, standard library modules that involve the aforementioned functionalities are also prohibited. The following section describes the available modules in the standard library: All modules in standard Python implementations that do not depend on extension modules are available. The following C extension modules are available: array audioop binascii _bisect cmath _codecs_cn _codecs_hk _codecs_iso2022 _codecs_jp _codecs_kr _codecs_tw _collections cStringIO datetime _functools future_builtins _hashlib _heapq itertools _json _locale _lsprof math _md5 _multibytecodec operator _random _sha256 _sha512 _sha _struct strop time unicodedata _weakref cPickle Some modules have limited functionalities. For example, the sandbox limits the data size that your code can write to Stdout and standard error output to 20 KB. This means `sys.stdout/sys.stderr` can write a maximum of 20 KB, and the system ignores any additional characters.

##### Third-party libraries

This topic describes third-party libraries for Python UDFs.

**Usage notes**

The runtime environment also includes common third-party libraries such as NumPy to supplement the standard libraries.

**Warning**

The system restricts third-party libraries by prohibiting local access and limiting network I/O. Therefore, you cannot use APIs in third-party libraries that involve these features.

##### Parameters and return value types

This topic describes the parameters and return value types for Python UDFs. Specify parameters and return values in the following way:

```
@odps.udf.annotate(signature)
```

**Usage notes**

Python UDFs support the following MaxCompute SQL data types: BIGINT, STRING, DOUBLE, BOOLEAN, DATETIME, DECIMAL, complex data types (ARRAY, MAP, and STRUCT), and nested complex data types. Before the system executes an SQL statement, it must determine the parameter types and return value types of all functions. Therefore, for Python, a dynamically typed language, you must specify function signatures by adding decorators to UDF classes. A function signature is specified as a string in the following format:

```
arg_type_list '->' type_list arg_type_list: type_list | '*' | '' | 'char(n)' | 'varchar(n)' type_list: [type_list ','] type type: 'bigint' | 'string' | 'double' | 'boolean' | 'datetime' | 'float' | 'binary' | 'd ate' | 'decimal' | 'decimal(precision,scale)'
```

**Note**

The left side of the arrow indicates the parameter types, and the right side indicates the return value types. Only UDTFs can return multiple columns. UDFs and UDAFs can return only one column. An asterisk (*) represents variable-length parameters. When you use variablelength parameters, UDFs, UDTFs, and UDAFs can match any input parameters. If a project uses MaxCompute V2.0 data types, you can set precision and scale for
**decimal**.
Return values do not support the CHAR and VARCHAR types. The following examples show valid function signatures.

```
'bigint,double->string' # The parameter types are BIGINT and DOUBLE, and the return value type is STRING. 'bigint,boolean->string,datetime' # The UDTF parameter types are BIGINT and BOOLEAN, a nd the return value types are STRING and DATETIME. '*->string' # Variable-length parameters. The input parameter typ es are arbitrary, and the return value type is STRING. '->double' # No parameters. The return value type is DOUBLE. 'array<bigint>->struct<x:string, y:int>' # The parameter type is ARRAY<BIGINT>, and the return value type is STRUCT<x:STRING, y:BIGINT>. '->map<bigint, string>' # No parameters. The return value type is MAP<INT, S TRING>.
```

**Data types**

During the query semantic parsing phase, the system checks for usage that does not conform to the function signature and returns an error to prevent execution of the function. At runtime, the system passes UDF parameters in the types specified by the function signature. The return value type must also match the type specified by the function signature. Otherwise, the system reports an error when it detects a type mismatch. The following table describes the mappings between MaxCompute SQL data types and Python data types.

| MaxCompute SQL type | Python type |
|---|---|
| BIGINT | INT |
| STRING | STR |
| DOUBLE | FLOAT |
| BOOLEAN | BOOL |
| DATETIME | INT |

| Developer Guide·MaxCompute S QL | MaxComput |
|---|---|

| FLOAT | FLOAT |
|---|---|
| CHAR | STR |
| VARCHAR | STR |
| BINARY | BYTEARRAY |
| DATE | INT |
| DECIMAL | DECIMAL.DECIMAL |
| ARRAY | LIST |
| MAP | DICT |
| STRUCT | COLLECTIONS.NAMEDTUPLE |

**Note**

The Python type that corresponds to the DATETIME type is INT. The value represents the number of milliseconds elapsed since the Epoch UTC time. You can use the DATETIME module in the Python standard library to process date and time types. `odps.udf.int(value,[silent=True])` adds the **silent** parameter. When **silent** is set to True, the function returns None instead of an exception if it cannot convert
**value** to INT.
A NULL value corresponds to None in Python.

##### UDF

This topic introduces user-defined scalar functions in Python UDFs and provides reference examples. To implement a Python UDF, define a new-style class and use the **evaluate** method.

```python
from odps.udf import annotate @annotate("bigint,bigint->bigint") class MyPlus(object):
    def evaluate(self, arg0, arg1):
        if None in (arg0, arg1):
            return None
        return arg0 + arg1
```

**Note**

Python UDFs must specify a function signature using the **annotate** decorator.

##### UDAF

This topic describes user-defined aggregation functions (UDAFs) in Python UDFs and provides reference examples.

| Class/Method | Description |
|---|---|
| class odps.udf.BaseUDAF | Inherits this class to implement a Python UDAF. |
| BaseUDAF.new buffer() _ | Returns the buffer for intermediate values of the aggregation function. The buffer must be a Marshal object, such as LIST or DICT, and the size of the buffer must not increase with the data volume. In extreme cases, the size of the buffer after object serialization must not exceed 2 MB. |
| BaseUDAF.iterate(buffer[, args, ...]) | Aggregates args into the intermediate value buffer. |
| BaseUDAF.merge(buffer, pbuffer) | Aggregates two intermediate value buffer objects by merging pbuffer into buffer. |
| BaseUDAF.terminate(buffer ) | Converts the intermediate value buffer into a basic MaxCompute SQL data type. |

The following example uses a UDAF to calculate the average value.

```python
from odps.udf import BaseUDAF, annotate @annotate('double->double') class Average(BaseUDAF):
    def new_buffer(self):
        return [0, 0]
    def iterate(self, buffer, number):
        if number is not None:
            buffer[0] += number
            buffer[1] += 1
    def merge(self, buffer, pbuffer):
        buffer[0] += pbuffer[0]
        buffer[1] += pbuffer[1]
    def terminate(self, buffer):
        if buffer[1] == 0:
            return 0.0
        return buffer[0] / buffer[1]
```

##### UDTF

This topic describes user-defined table-valued functions (UDTFs) in Python UDFs and provides reference examples.

| Class or method | Description |
|---|---|
| class odps.udf.BaseUDTF | The base class for Python UDTFs. You can inherit this class to implement methods such as process or close. |
| BaseUDTF. init () __ __ | The initialization method. If an inherited class needs to implement this method, it must call the initialization method of the base class super(BaseUDTF, self). init () at the beginning. The init __ __ method runs only once throughout the UDTF lifecycle, specifically before the system processes the first record. When the UDTF needs to maintain internal state, you can use this method to initialize all states. |
| BaseUDTF.process([args, ...]) | The MaxCompute SQL framework calls this method. The framework calls process once for each record in the SQL query. The parameters of process are the UDTF input parameters specified in the SQL statement. |

| BaseUDTF.forward([args, ...]) | The output method of the UDTF. User code calls this method. Each call to forward outputs one record. The parameters of forward are the UDTF output parameters specified in the SQL statement. |
|---|---|
| BaseUDTF.close() | The termination method of the UDTF. The MaxCompute SQL framework calls this method only once, specifically after the system processes the last record. |

```python
# coding:utf-8
# explode.py
from odps.udf import annotate from odps.udf import BaseUDTF @annotate('string -> string') class Explode(BaseUDTF):
    # Split a string by commas and output each part as a separate record.
    def process(self, arg):
        props = arg.split(',')
        for p in props:
            self.forward(p)
```

**Note**

A Python UDTF does not need to use **annotate** to specify parameter types and return value types. In this case, the function can accept any input parameters when you use it in SQL, but the system cannot infer the return value types and treats all output parameters as the STRING type. Therefore, when you call **forward**, you must convert all output values to the STRING type.

##### Reference resources

This topic describes how to reference resources in Python UDFs and provides examples. Python UDFs can reference file and table resources through the **odps.distcache** module.

**Reference file resources**

**Syntax**

```
odps.distcache.get_cache_file(resource_name) -- Returns the content of the specified resource.
```

**resource_name**: the STRING type. This parameter specifies the name of an existing
resource in the current project. If the resource name is invalid or the resource does not exist, the system returns an exception. The return value is a file-like object. After this object is used, the `close` method must be called to release the opened resource file.

```python
from odps.udf import annotate from odps.distcache import get_cache_file @annotate('bigint->string') class DistCacheExample(object):
    def __init__(self):
        cache_file = get_cache_file('test_distcache.txt')
        kv = {}
        for line in cache_file:
            line = line.strip()
            if not line:
                continue
            k, v = line.split()
            kv[int(k)] = v
        cache_file.close()
        self.kv = kv
    def evaluate(self, arg):
        return self.kv.get(arg)
```

**Reference table resources**

**Syntax**

```
odps.distcache.get_cache_table(resource_name)
```

**resource_name**: the STRING type. This parameter specifies the name of an existing
resource table in the current project. If the resource name is invalid or the resource does not exist, the system returns an exception. The return value is of the GENERATOR type. The caller obtains the table content by traversing the table. Each traversal returns a record from the table in the form of an array.

```python
from odps.udf import annotate from odps.distcache import get_cache_table @annotate('->string') class DistCacheTableExample(object):
    def __init__(self):
        self.records = list(get_cache_table('udf_test'))
        self.counter = 0
        self.ln = len(self.records)
    def evaluate(self):
        if self.counter > self.ln - 1:
            return None
        ret = self.records[self.counter]
        self.counter += 1
        return str(ret)
```

#### Python 3 UDF

This topic describes the precautions for writing UDFs in Python 3.

**Background information**

Python 2 has reached End of Life (EOL). MaxCompute supports Python 3 and uses CPython- 3.7.3.

**Usage limits**

Python 3 is not compatible with Python 2. A SQL job can use only one Python version at a time. Before you use Python 3, you must consider compatibility issues. You cannot use Python 3 and Python 2 in the same SQL statement.

**Enable Python 3**

MaxCompute supports Python 3 only at the job level. To enable Python 3 when you execute SQL statements, add the following command:

```
SET odps.sql.python.version=cp37;
```

**Third-party libraries**

MaxCompute Python UDFs support third-party libraries. The Python 2 runtime environment includes the third-party library NumPy as a supplement to the standard library. The built-in Python 3 runtime environment of MaxCompute does not include the third-party library NumPy. If your UDF requires NumPy, you must manually upload the NumPy WHEEL package. When you download the NumPy package from PyPI, the file name follows the format
**numpy-<version>-cp37-cp37m-manylinux1_x86_64.whl**.

**Migrate Python 2 UDFs**

Python 2 has reached EOL. We recommend that you perform migration based on the project type: New projects: applicable to new projects or projects where you write UDFs in Python for the first time. We recommend that you write all Python UDFs in Python 3. Existing projects: applicable to projects that use a large number of Python 2 UDFs. Exercise caution when you enable Python 3. You cannot use Python 3 and Python 2 in the same SQL statement. If you plan to gradually migrate all Python 2 UDFs to Python 3 UDFs, we recommend the following approach: New jobs and new UDFs: Write them in Python 3 and enable Python 3 at the job level. Python 2 UDFs: Rewrite Python 2 UDFs to make them compatible with both Python 2 and Python 3. For more information about the rewrite method, see How to port Python 2 Code to Python 3.

**Note**

If you need to write public UDFs and authorize multiple projects to use them, we recommend that you make the UDFs compatible with both Python 2 and Python 3.

#### SQL Function

This topic describes how to use SQL-defined UDFs in SQL scripts through the SQL FUNCTION statement.

**Background information**

You can use SQL Function in MaxCompute to resolve the following issues: Code often contains many similar sections, which makes maintenance difficult and errorprone. Furthermore, if you introduce a UDF, you must write the code, compile it in Java, create resources, and create the function. This process is tedious, and the performance is inferior to that of built-in functions. Sample syntax:

```
SELECT
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key1')), 'default') AS key1,
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key2')), 'default') AS key2,
    ...
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.keyN')), 'default') AS keyN
FROM t;
```

Similar to Lambda expressions in Java, a function is passed to other functions as parameters.

**Feature introduction**

As a type of UDF, SQL Function addresses the limitation that the system supports only UDFs created in Java or Python. It also extends parameter support to function types and adds anonymous function capabilities, which increases the flexibility of business logic expression. You can use SQL Function to implement simple features and improve code reuse. The following list describes the specific features: Supports defining and calling UDFs within SQL scripts. Support function-type parameters. When you call a function, you can pass built-in functions, UDFs, or SQL-defined functions as arguments. Support anonymous functions as function-type parameters. When you call a function, you can pass anonymous functions as arguments.

**Create a permanent SQL Function**

**Syntax**

After you create a permanent SQL Function and store it in the Meta system, all queries can reference the function. To reference a SQL Function, you must have Function-level permissions. The syntax is as follows:

```
CREATE SQL FUNCTION function_name(@parameter_in1 datatype[, @parameter_in2 datatype.. .]) [RETURNS @parameter_out datatype] AS [BEGIN] function_expression [END];
```

**function_name**: the name of the new SQL-defined function. The function name must be
unique. You can register a function with the same name only once, and the name must not conflict with any built-in function name in the system.
**parameter_in**: the input parameters of the function.
**RETURNS**: the return value variable of the function. If you do not specify this parameter,
the function returns a variable with the same name as function_name by default.
**parameter_out**: the return parameter of the function.
**function_expression**: the function expression.

```
CREATE SQL FUNCTION my_add(@a BIGINT) AS @a + 1;
```

**@a + 1** is the function implementation logic. You can write it directly as an expression, and
it supports built-in operators, built-in functions, and UDFs. If the logic is complex, you can use BEGIN and END in the definition and write multiple statements inside the block. The RETURNS clause specifies the return value variable. If you do not specify this clause, the function returns a variable with the same name as function_name by default.

```
CREATE SQL FUNCTION my_sum(@a BIGINT, @b BIGINT, @c BIGINT) RETURNS @my_sum BIGINT AS BEGIN
    @temp := @a + @b;
    @my_sum := @temp + @c;
END;
```

**Query a SQL Function**

You query a SQL Function in the same way as you query a Java UDF or a Python UDF. Sample syntax:

```
DESC FUNCTION my_add;
```

**Delete a SQL Function**

You delete a SQL Function in the same way as you delete a Java UDF or a Python UDF. Sample syntax:

```
DROP FUNCTION my_add;
```

**Call a SQL Function**

You call a SQL Function in the same way as you call an existing built-in function. Sample syntax:

```
SELECT my_sum(col1, col2 ,col3) FROM t;
```

**Temporary SQL Function**

If you do not need to store a SQL Function in the MaxCompute Meta system, you can use a temporary SQL Function. A temporary SQL Function is valid only in the current script. Sample syntax:

```
FUNCTION my_add(@a BIGINT) AS @a + 1; SELECT my_add(key), my_add(value) FROM src;
```

**Support for function-type parameters**

SQL Function supports function-type parameters. When you call a SQL Function, you can pass built-in functions, UDFs, or SQL-defined functions as arguments. Sample syntax:

```
FUNCTION ADD(@a BIGINT) AS @a + 1; FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, ADD), OP(key, ABS) FROM VALUES (1),(2) AS t (key); -- Output +------------+------------+
| _c0        | _c1        |
+------------+------------+
| 2          | 1          |
| 3          | 2          |
+------------+------------+
```

In this example, the OP function defines two input parameters. **@a** defines a BIGINT value.
**@fun** defines a function whose input and output are both of the BIGINT type. The OP function
passes **@a** to the **@fun** function, and the ADD and ABS functions to perform operations on
**@a**.

**Support for anonymous functions**

Function-type parameters can be anonymous functions. When you call a SQL Function, you can pass anonymous functions as arguments. Sample syntax:

```
FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, FUNCTION (@a) AS @a + 1) FROM VALUES (1),(2) AS t (key);
```

In this example, **FUNCTION (@a) AS @a + 1** is an anonymous function. You do not need to specify the type of the input parameter **@a** for the anonymous function. The Compiler infers the type of **@a** based on the parameter definition of the OP function.

#### Embedded UDF

##### Background

This topic describes the background of embedded UDFs.

**Background**

You can use embedded UDFs in MaxCompute to resolve the following issues, where code implementation is tedious and difficult to read and maintain: After you create a UDF and complete code development, you must also compile the code in Java, create resources, and create functions, which makes the process tedious. If an SQL script contains a UDF, you cannot directly view the implementation logic or obtain the source code of the JAR package, which makes maintenance difficult. When you use Java library functions through UDTs, you must write lengthy code to convert Java code into expressions, which makes reading and maintenance difficult. Additionally, you cannot convert some Java code into expressions. The following code shows an example.

```
Foo f = new Foo(); f.execute(); f.getResult();
```

##### Feature overview

This topic describes the features supported by embedded UDFs. Embedded UDFs allow you to embed Java or Python code in SQL scripts. The Janino compiler identifies and extracts the embedded code to compile the Java code, dynamically generate resources, and create temporary functions. Embedded UDFs allow you to place SQL scripts and third-party code in the same source code file, reducing the steps to use UDTs or UDFs and facilitating routine development.

##### Usage limits

This topic describes the usage limits of embedded UDFs.

**Limits**

Embedded Java code uses the Janino Compiler for compilation, and the supported Java syntax is only a subset of the standard Java JDK. The usage limits of embedded Java code include but are not limited to the following items: Lambda expressions are not supported. Catching multiple exception types is not supported, such as **catch(Exception1 |**
**Exception2 e)**.
Automatic type inference for generics is not supported, such as **Map map = new**
**HashMap<>();**.
The compiler ignores type parameter inference, and you must use explicit casting, such as
**(String) myMap.get(key)**.
The Assert statement is always enabled and is not controlled by the JVM parameter -ea. Language features from Java versions later than Java 8 are not supported.

##### Examples

This topic describes how to use the embedded UDF feature and provides reference examples.

**Reference embedded code in UDT**

```
SELECT
```

`s,`

```java
  com.mypackage.Foo.extractNumber(s)
FROM VALUES ('abc123def'),('apple') AS t(s);
#CODE ('lang'='JAVA')
package com.mypackage; import java.util.regex.Matcher; import java.util.regex.Pattern; public class Foo {
  final static Pattern compile = Pattern.compile(".*?([0-9]+).*");
  public static String extractNumber(String input) {
    final Matcher m = compile.matcher(input);
    if (m.find()) {
      return m.group(1);
```

`}`

```
    return null;
```

`}` `}`

```
#END CODE;
```

**Note**

**#CODE** and **#END CODE**: indicate the start and end positions of the embedded
code. An embedded code block at the end of a script applies to the entire script.
**'lang'='JAVA'**: specifies that the embedded code is Java code. **PYTHON** is also
supported. You can use UDT syntax in an SQL script to directly call **Foo.extractNumber**.

**Embedded UDF in Java code**

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA')
package com.mypackage; import com.aliyun.odps.udf.UDF; public class Reverse extends UDF {
  public String evaluate(String input) {
    if (input == null) return null;
    StringBuilder ret = new StringBuilder();
    for (int i = input.toCharArray().length - 1; i >= 0; i--) {
      ret.append(input.toCharArray()[i]);
```

`}`

```
    return ret.toString();
```

`}` `}`

```
#END CODE;
SELECT foo('abdc');
```

**Note**

You can place an embedded code block after **USING** or at the end of the script. A code block placed after **USING** applies only to the `CREATE TEMPORARY FUNCTION` statement. Functions created by the `CREATE TEMPORARY FUNCTION` statement are temporary functions. They take effect only in the current execution and are not stored in the MaxCompute meta system.

**Embedded UDTF in Java code**

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA', 'filename'='embedded.jar')
package com.mypackage; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve({"string->string,string"}) public class Reverse extends UDTF {
  @Override
  public void process(Object[] objects) throws UDFException {
    String str = (String) objects[0];
    String[] split = str.split(",");
    forward(split[0], split[1]);
```

`}` `}`

```
#END CODE;
SELECT foo('ab,dc') AS (a,b);
```

**Note**

The return value of **@Resolve** must be **string[]**, but the Janino compiler cannot recognize **"string->string,string"** as **string[]**. Therefore, the parameter of the
**@Resolve** annotation requires braces ({}), which is specific to embedded code. You can
omit the braces ({}) when you create a Java UDTF by using the standard method.

**Embedded UDF in Python code**

```python
CREATE TEMPORARY FUNCTION foo AS 'embedded.UDFTest' USING
#CODE ('lang'='PYTHON', 'filename'='embedded')
from odps.udf import annotate @annotate("bigint->bigint") class UDFTest(object):
  def evaluate(self, a):
    return a * a
#END CODE;
SELECT foo(4);
```

**Note**

The indentation of Python code must conform to Python language specifications. When you register a Python UDF, the class name after **AS** must include the file name of the Python source code. You can use `'filename'='embedded'` to specify a virtual file name.

### UDTs

#### Common scenarios and usage limits

This topic describes the common scenarios and usage limits of the User Defined Type (UDT) feature.

**Background information**

MaxCompute introduces the User Defined Type (UDT) feature based on the new-generation SQL engine. The UDT feature allows you to directly call classes of third-party languages and use their methods in SQL statements, or directly use third-party objects to obtain their data content.

**Common scenarios**

You can use UDTs for features that MaxCompute does not natively provide but you can easily implement in other languages. For example, you can implement a feature by calling a method of a built-in Java class only once, but MaxCompute does not provide a simple method to implement this feature. If you use a UDF to implement the feature, the entire process becomes overly complex. You need to call third-party libraries in SQL statements to implement specific features. UDT allows you to directly call these libraries in SQL statements without wrapping them in a UDF. You need to directly call the source code of third-party languages in SQL statements. The SELECT TRANSFORM syntax allows you to write scripts in SQL statements to improve readability and code maintainability. However, you cannot use this method for certain languages. For example, you must compile Java source code before execution. The UDT feature allows you to directly write the source code of these languages in SQL statements.

**Usage limits**

UDT supports only Java, and Java SDK classes are available by default.

**Note**

The current runtime uses JDK 1.8 and may not support later JDK versions. All operators use MaxCompute SQL semantics, not UDT semantics. UDTs cannot be used as Shuffle keys, including the keys for structures such as JOIN, GROUP BY, DISTRIBUTE BY, SORT BY, ORDER BY, and CLUSTER BY. DDL statements do not support UDTs. You cannot insert UDT objects into tables, and the final display results cannot be of the UDT type.

#### Feature overview

This topic describes UDT features and provides examples. In many SQL engines, UDTs are similar to the complex STRUCT type in MaxCompute. In contrast, UDTs in MaxCompute resemble the CREATE TYPE concept more closely, where a type includes data fields and methods. MaxCompute does not require special DDL syntax to define new types. You can use new types directly in SQL statements by using UDTs. The following examples demonstrate UDT features. You can call the `java.lang` package in SQL by using one of the following two methods.

**UDT method**

You can call java.lang directly in SQL statements by using the UDT feature.

```
-- Enable new types because the following operations use the INTEGER (INT) type. SET odps.sql.type.system.odps2=true; SELECT java.lang.Integer.MAX_VALUE;
```

As in Java, you can omit the java.lang package. Therefore, you can simplify the preceding example into the following statement.

```
SET odps.sql.type.system.odps2=true; SELECT Integer.MAX_VALUE; -- Result +------------+
| max_value  |
+------------+
| 2147483647 |
+------------+
```

**UDF method**

You can call java.lang in SQL statements by using a UDF.
1. Define a UDF class.

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.udf.UDF; public class IntegerMaxValue extends UDF {
    public Integer evaluate() {
        return Integer.MAX_VALUE;
```

`}` `}`
2. Compile the UDF, package it into a JAR file, upload the JAR file, and create a function.

```
ADD jar odps-test.jar; CREATE FUNCTION integer_max_value AS 'com.aliyun.odps.test.IntegerMaxValue' USING 'od ps-test.jar';
```

3. Use the function in SQL.

```
SELECT integer_max_value(); -- Result +------------+
| _c0        |
+------------+
| 2147483647 |
+------------+
```

The preceding examples show that UDTs simplify these processes and allow you to extend SQL features by using other languages.

#### Implementation principles and features

This topic describes the implementation principles of UDTs and provides detailed feature descriptions.

**Implementation principles**

**Execution process**

The following example shows the execution process of UDT.

```
-- Sample data. @table1 := SELECT * FROM VALUES ('100000000000000000000') AS t(x); @table2 := SELECT * FROM VALUES (100L) AS t(y); -- Code logic. -- Create an object by using new. @a := SELECT new java.math.BigInteger(x) x FROM @table1; -- Call a static method. @b := SELECT java.math.BigInteger.valueOf(y) y FROM @table2; -- Call an instance method. SELECT /*+mapjoin(b)*/ x.add(y).toString() FROM @a a JOIN @b b; -- Result +-----------------------+
| _c0                   |
+-----------------------+
| 100000000000000000100 |
+-----------------------+
```

**Runtime principles**

The following figure shows the runtime process of the entire example. This UDT has three stages: M1, R2, and J3. If you are familiar with MapReduce principles, you know that the **Join** operation requires data reshuffling, which results in multiple stages. Typically, different stages run in different processes and on different physical machines. M1 only executes the `new java.math.BigInteger(x)` operation. J3 executes the `java.math.BigInteger.valueOf(y)` and `x.add(y).toString()` operations in different phases. These operations run not only in separate phases but also in different processes and on different physical machines. UDT encapsulates this process and makes it appear almost identical to execution within a single JVM. The preceding example shows that subquery results allow columns of UDT types. For example, column x of variable a is of the **java.math.BigInteger** type instead of a built-in type. UDT data can flow into the next operator, where you can call other methods or even use the data in data shuffling.

**Feature description**

UDT supports only the Java language. All classes in the Java SDK are available by default. UDT allows you to upload your own JAR packages and reference them directly. The system provides several flags for your convenience.
**set odps.sql.session.resources**: specifies the resources to reference. You can specify
multiple resources separated by commas (,). Example: `set`

```
odps.sql.session.resources=foo.sh,bar.txt; .
```

**Note**

This flag is the same as the flag that specifies resources in **select transform**, so this flag affects both features.

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.resources=odps-test.jar; -- Specify the JAR packages to reference. You must upload these JAR packages to the project in advance. SELECT new com.aliyun.odps.test.IntegerMaxValue().evaluate();
```

**odps.sql.session.java.imports**: specifies the default Java packages. You can specify
multiple packages separated by commas (,). Similar to the **import** statement in Java, you can provide a full class path such as java.math.BigInteger, or use an asterisk (*). **static**
**import** is not supported.

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.resources=odps-test.jar; SET odps.sql.session.java.imports=com.aliyun.odps.test.*; -- Specify the default packages. SELECT new IntegerMaxValue().evaluate();
```

UDT supports resource access. You can use the `com.aliyun.odps.udf.impl.UDTExecutionContext.get()` static method in SQL to obtain the
**ExecutionContext** object, which allows you to access the current **ExecutionContext** and
then access resources such as file resources and table resources. UDT supports the following operations: The `new` operation for instantiating objects.

| new |   | operation for instantiating |
|---|---|---|
| as |   |   |

The `new` operation for instantiating arrays, including creating arrays with initializer lists Method calls, including static method calls.

**Note**

Identifiers, including packages, class names, method names, and field names, in UDT are case-sensitive. Anonymous classes and Lambda expressions are not supported. Function calls without return values are not supported because UDT always appears in expressions, and function calls without return values cannot be embedded in expressions. UDT supports the following data types:

| cast(1 as java.lang.Object) |   |   |
|---|---|---|
| ersion, such as | (Object)1 | . |

UDT supports type conversion in SQL style, such as `cast(1 as java.lang.Object)` . However, UDT does not support Java-style type conversion, such as `(Object)1` . UDT built-in types have a one-to-one mapping with specific Java types. You can directly call methods of the mapped Java type on built-in type data, such as

```
 '123'.length() , 1L.hashCode() .
```

UDT types can directly participate in built-in function or UDF operations. For example, in `chr(Long.valueOf('100'))` , **Long.valueOf** returns data of the **java.lang.Long** type, while the built-in function Chr accepts the built-in type BIGINT. Java primitive types can automatically convert to their boxing types, and the preceding two rules apply.

|   | Note Some new built-in data types require you to set set odps.sql.type.system.odps2=true; before use. Otherwise, an error is returned. |   |
|---|---|---|
|   | odps.sql.type.system.odps2=true; |   |

UDT extends the type conversion rules: UDT objects can be implicitly converted to objects of their base classes. UDT objects can be explicitly converted to objects of their base classes or subclasses. The original type conversion rules apply to two objects without an inheritance relationship. Note that this may cause data changes. For example, you can convert data of the **java.lang.Long** type to **java.lang.Integer**. This applies the built-in type conversion from BIGINT to INT, which may change the data content and even cause precision loss. UDT supports relatively complete generics. For example, in `java.util.Arrays.asList(new` `java.math.BigInteger('1'))` , the compiler can determine that the return value of this method is of the **java.util.List<java.math.BigInteger>** type based on the parameter type.

**Note**

Type parameters must be specified for constructors. Otherwise, **java.lang.Object** is used. This behavior is consistent with Java. All operators follow MaxCompute SQL semantics, not UDT semantics. Examples: STRING addition: The result of `String.valueOf(1) + String.valueOf(2)` is 3 (STRINGs are implicitly converted to DOUBLEs, and then DOUBLE addition is performed), rather than 12. This differs from Java, where STRING addition uses concatenation semantics. In Java, you should use the `equals()` method instead of the **=** operator to check equality. In contrast, in SQL, the**=** operator is used to check for equality. UDT has an ambiguous concept of object identity due to data reshuffling. Objects may be transmitted between different processes and different physical machines. During the transmission, the same object may reference different objects at different times. For example, the system may shuffle an object to two machines and then shuffle it back together in the next phase. Therefore, when you use UDT, you should use the `equals()` method to check for equality and avoid inaccurate results from using the **=** operator for equality checks. The system guarantees the data correlation among internal data objects within an object at a specific row and column. However, the system does not guarantee data correlation between objects in different rows or different columns. You cannot use UDTs as shuffle keys, including keys in Join, Group By, Distribute By, Sort By, Order By, and Cluster By structures. You can use a UDT at any intermediate stage in an expression, but you cannot use it as the final output. UDTs can implement scalar function capabilities. Combined with built-in functions COLLECT_SET and EXPLODE, UDTs can also implement aggregator and table-valued function capabilities.

#### Benefits

This topic describes the benefits of UDTs.

**Feature overview**

UDTs provide the following benefits: UDTs are easy to use and do not require you to define any functions. They support all JDK features, thereby extending the capabilities of SQL. You can place code and SQL statements in the same file for easier management. UDTs can directly use other class libraries, resulting in high code reusability.

#### Performance advantages

This topic describes the performance advantages of UDTs.

**Performance overview**

In terms of performance, UDTs and UDFs deliver almost identical performance because their execution processes are very similar. However, the optimized compute engine enables UDTs to achieve higher performance in specific scenarios. UDT objects require serialization and deserialization only when they are transferred across processes. Therefore, when you execute operations that do not require data reshuffling, such as JOIN or AGGREGATE, UDTs save the overhead of serialization and deserialization. The UDT runtime is implemented based on Codegen instead of reflection, which eliminates the performance overhead of reflection. During execution, the system merges multiple consecutive UDT operations into a single function call. For example, in the following code snippet, the code appears to call UDTs multiple times, but it actually calls the UDF only once. Therefore, although UDT operations are granular, they do not incur additional API overhead from multiple function calls.

```
values[x].add(values[y]).divide(java.math.BigInteger.valueOf(2))
```

#### Security advantages

This topic describes the security advantages of UDTs.

**Security overview**

In terms of security control, UDTs and UDFs are identical. Both are subject to the restrictions of the Java sandbox policy. Therefore, to perform restricted operations, you must either enable sandbox isolation or apply for a sandbox whitelist.

#### More examples

##### Java array examples

This topic provides Java array examples for UDTs for your reference.

**Usage examples**

```
SET odps.sql.type.system.odps2=true; SET odps.sql.udt.display.tostring=true; SELECT -- Create an array with 10 elements.
    new Integer[10],
-- Create an array of length 3 by using a collection initializer.
    new Integer[] {c1, c2, c3},
-- Create a multi-dimensional array.
    new Integer[][] { new Integer[] {c1, c2}, new Integer[] {c3, c4} },
-- Access array elements by using indexes.
    new Integer[] {c1, c2, c3} [2],
-- Create a List<Integer> that you can also use as an array<int>. This is another metho d to create built-in ARRAY data.
    java.util.Arrays.asList(c1, c2, c3)
FROM VALUES (1,2,3,4) AS t(c1, c2, c3, c4);
```

##### JSON examples

This topic provides UDT JSON examples for your reference.

**Usage notes**

The UDT runtime includes a built-in JSON dependency (version 2.2.4), so you can use JSON directly.

**Note**

In addition to JSON, the MaxCompute runtime also includes built-in dependencies such as commons-logging (version 1.1.1), commons-lang (version 2.5), commons-io (version 2.4), and protobuf-java (version 2.4.1).

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.java.imports=java.util.*,java,com.google.gson.*; -- Separate multi ple packages with commas when you import them. @a := SELECT new Gson() gson; -- Create a Gson object. SELECT gson.toJson(new ArrayList<Integer>(Arrays.asList(1, 2, 3))), -- Convert any object to a JSON string. cast(gson.fromJson('["a","b","c"]', List.class) as List<String>) -- Deserialize the JSO N string. Note that the Gson API returns a List<Object> type after direct deserialization. This example forcibly converts it to a List<String> type for subsequen t use. FROM @a;
```

Query results:

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| [1,2,3]    | 1          |
+------------+------------+
```

Compared with the built-in GET_JSON_OBJECT function, this method is easier to use and deserializes JSON strings into formatted data during extraction, which improves efficiency.

##### Complex type operation examples

This topic provides examples of complex type operations on UDTs for your reference.

**Usage notes**

Built-in types have the following mapping relationships with Java types: ARRAY maps to
**java.util.List** and MAP maps to **java.util.Map**:
Objects of classes that implement the **java.util.List** or **java.util.Map** interface in Java can be used in complex type operations in MaxCompute SQL. ARRAY or MAP data in MaxCompute can directly call the methods of the List or Map interfaces.

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.java.imports=java.util.*; SELECT
    size(new ArrayList<Integer>()),        -- Call the built-in Size function on
ArrayList data.
    array(1,2,3).size(),                   -- Call the Size method of List on the built-
in type ARRAY.
    sort_array(new ArrayList<Integer>()),  -- Sort ArrayList data.
    al[1],                                 -- Java List does not support index operations
, but ARRAY does.
    Objects.toString(a),        -- Previously, you could not cast the ARRAY type to
STRING. Now a workaround exists.
    array(1,2,3).subList(1, 2)             -- Compute the subList.
FROM (select new ArrayList<Integer>(array(1,2,3)) as al, array(1,2,3) as a) t;
```

The following results are returned.

```
+------------+------------+------------+------------+------------+------------+
| _c0        | _c1        | _c2        | _c3        | _c4        | _c5        |
+------------+------------+------------+------------+------------+------------+
| 0          | 3          | []         | 2          | [1, 2, 3]  | [2]        |
+------------+------------+------------+------------+------------+------------+
```

##### Aggregate operation examples

This topic provides UDT aggregate operation examples for your reference.

**Usage notes**

To implement aggregation, a UDT first uses the built-in COLLECT_SET or COLLECT_LIST function to convert data into a list, and then applies a UDT scalar method to the list to calculate the aggregate value. The following example calculates the median of BigInteger values. Because the data is of the java.math.BigInteger type, you cannot directly use the built-in MEDIAN function.

```
SET odps.sql.session.java.imports=java.math.*; @test_data := SELECT * FROM VALUES (1),(2),(3),(5) AS t(value); @a := SELECT collect_list(new BigInteger(value)) VALUES FROM @test_data; -- Aggregate the data into a list first. @b := SELECT sort_array(values) AS VALUES, values.size() cnt FROM @a; -- Calculate the median: sort the data first. @c := SELECT if(cnt % 2 == 1, new BigDecimal(values[cnt div 2]), new BigDecimal(values[cnt div 2 - 1].add(values[cnt div 2])).divide(new BigDecimal(2))) med from @b; -- Final result. SELECT med.toString() FROM @c;
```

The following results are returned.

```
+------------+
| _c0        |
+------------+
| 2.5        |
+------------+
```

The **collect_list** function collects all data together first and cannot implement partial aggregation. Therefore, it processes data less efficiently than built-in aggregate functions or UDAFs. Use built-in aggregate functions whenever possible. Additionally, collecting all data of a single group together increases the risk of data skew. If a UDAF needs to aggregate all data together (similar to the built-in WM_CONCAT aggregate function), the preceding method offers higher processing efficiency than a UDAF.

##### Table-valued function examples

This topic provides table-valued function examples for UDTs for your reference.

**Usage notes**

Table-valued functions allow you to input and output multiple rows and columns of data. You can implement this feature by performing the following steps: Input multiple rows and columns of data. For more information, see Aggregate operation examples. Output multiple rows and columns of data. You can use a UDT method to output a Collection type (List or MAP) and then call the Explode function to expand the collection into multiple rows. Since a UDT can contain multiple data fields, you can expand it into multiple columns by calling different Getter methods to obtain the content of each field. The following example expands the content of a JSON string.

```
@a := SELECT '[{"a":"1","b":"2"},{"a":"1","b":"2"}]' str; -- Sample data. @b := SELECT new com.google.gson.Gson().fromJson(str, java.util.List.class) l FROM @a; -- Deserialize JSON. @c := SELECT cast(e AS java.util.Map<Object,Object>) m FROM @b lateral view explode(l) t AS e; -- Use explode to expand the data into multiple rows. @d := SELECT m.get('a') AS a, m.get('b') AS b FROM @c; -- Expand the data into multiple columns. SELECT a.toString() a, b.toString() b FROM @d; -- Output the final result. Note that co lumns a and b in the output of variable d are of the Object type.
```

The following results are returned.

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
+------------+------------+
| 1          | 2          |
+------------+------------+
```

### UDJ

#### UDJ background

This topic introduces the background of the User Defined Join (UDJ) mechanism.

**Background**

MaxCompute provides multiple JOIN methods, including INNER JOIN, RIGHT JOIN, OUTER JOIN, LEFT JOIN, FULL JOIN, SEMI JOIN, and ANTI-SEMI JOIN. You can use the built-in JOIN methods in most scenarios. However, these methods are insufficient if you want to perform cross join operations. In most cases, you can use UDFs to describe your code framework. However, the current UDF, user-defined table-valued function (UDTF), and user-defined aggregate function (UDAF) frameworks can only handle one table at a time. For custom operations on multiple tables, you often need to combine built-in joins with various UDFs and UDTFs, and write complex SQL statements. In such scenarios, you must use a custom MapReduce framework instead of SQL to complete the required computing tasks. Both the combination of Joins, various UDFs/UDTFs, and complex SQL, as well as custom MapReduce, have high barriers to entry and introduce several issues: Combination of Joins, various UDFs/UDTFs, and complex SQL: Multiple complex joins and code distributed throughout SQL statements create multiple logical black boxes. This prevents the system from generating an optimal execution plan. Using MapReduce: This approach significantly limits the execution optimization capabilities of the system. Furthermore, because developers write most MapReduce code in Java, MapReduce jobs run much less efficiently than the LLVM-based code generator of MaxCompute when you deeply optimize on-premises code. To resolve these issues, MaxCompute introduces UDJ as a new extension mechanism in the UDF framework based on the MaxCompute 2.0 compute engine. UDJ allows more userdefined operations by flexibly joining tables and simplifies MapReduce-based operations in the underlying distributed system.

#### Examples of using UDJ

##### Cross join operations by using UDJ

This topic describes the cross-table join feature of user-defined join (UDJ) and provides reference examples.

**Usage notes**

**Test data**

Assume that two log tables named payment and user_client_log exist. The payment table stores the payment records of users. Each payment record contains the user ID, payment time, and payment content. The following table lists the sample data.

| user id _ | Time | pay info _ |
|---|---|---|
| 2656199 | 2018-02-13 22:30:00 | gZhvdySOQb |
| 8881237 | 2018-02-13 08:30:00 | pYvotuLDIT |
| 8881237 | 2018-02-13 10:32:00 | KBuMzRpsko |

The user_client_log table stores the client logs of users. Each log contains the user ID, logging time, and log content. The following table describes the sample data.

| user id _ | Time | Content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL |

**Verification objectives**

For each record in the user_client_log table, find the payment record that has the closest time to this record in the payment table. Then, join the two records and generate results. The following table describes the results.

| user id _ | Time | Content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn, pay pYvotuLDIT |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL, pay pYvotuLDIT |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL, pay KBuMzRpsko |

To meet this requirement, use the UDJ method.
1. Create a UDJ function.
i. Configure the SDK of the new version.

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-udf</artifactId>
  <version>0.30.8-public</version>
</dependency>
```

ii. Write UDJ code and package the code into odps-udj-example.jar.

```java
package com.aliyun.odps.udf.example.udj; import com.aliyun.odps.Column; import com.aliyun.odps.OdpsType; import com.aliyun.odps.Yieldable; import com.aliyun.odps.data.ArrayRecord; import com.aliyun.odps.data.Record; import com.aliyun.odps.udf.DataAttributes; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDJ; import com.aliyun.odps.udf.annotation.Resolve; import java.util.ArrayList; import java.util.Iterator; /**
 * For each record in the right table, find the nearest record in the left table
 * and merge the two records.
```

`*/`

```java
@Resolve("->string,bigint,string") public class PayUserLogMergeJoin extends UDJ {
```

```java
    private Record outputRecord;
    /**
     * The system calls this method before the data processing phase. You can imple
ment this method to perform initialization.
```

`*/`

```java
    @Override
    public void setup(ExecutionContext executionContext, DataAttributes
dataAttributes) {
```

`//`

```
        outputRecord = new ArrayRecord(new Column[]{
                new Column("user_id", OdpsType.STRING),
                new Column("time", OdpsType.BIGINT),
                new Column("content", OdpsType.STRING)
        });
```

`}`

```
    /** Override this method to implement the join logic.
     * @param key The current join key.
     * @param left The group of records in the left table that correspond to the cu
rrent key.
     * @param right The group of records in the right table that correspond to the
current key.
     * @param output The output for the UDJ results.
```

`*/`

```java
    @Override
    public void join(Record key, Iterator<Record> left, Iterator<Record> right, Yie
ldable<Record> output) {
        outputRecord.setString(0, key.getString(0));
        if (!right.hasNext()) {
            // Empty right group. Do nothing.
            return;
        } else if (!left.hasNext()) {
            // Empty left group. Output all records in the right group without
merging.
            while (right.hasNext()) {
                Record logRecord = right.next();
                outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
                outputRecord.setString(2, logRecord.getString(1));
                output.yield(outputRecord);
```

`}`

```
            return;
```

`}`

```
        ArrayList<Record> pays = new ArrayList<>();
        // The iterator for the left record group iterates from start to end.
        // The iterator cannot reset for each record in the right group.
        // Therefore, save each left record to an ArrayList.
        left.forEachRemaining(pay -> pays.add(pay.clone()));
        while (right.hasNext()) {
            Record log = right.next();
            long logTime = log.getDatetime(0).getTime();
            long minDelta = Long.MAX_VALUE;
            Record nearestPay = null;
            // Iterate through all records in the left group to find the record
with the smallest time difference. for(Recordpay:pays){
```

```
            for (Record pay : pays) {
                long delta = Math.abs(logTime - pay.getDatetime(0).getTime());
                if (delta < minDelta) {
                    minDelta = delta;
                    nearestPay = pay;
```

`}` `}`

```
            // Merge the log record with the nearest payment record and output the
result.
            outputRecord.setBigint(1, log.getDatetime(0).getTime());
            outputRecord.setString(2, mergeLog(nearestPay.getString(1),
log.getString(1)));
            output.yield(outputRecord);
```

`}` `}`

```
    String mergeLog(String payInfo, String logContent) {
        return logContent + ", pay " + payInfo;
```

`}`

```java
    @Override
    public void close() {
```

`}` `}` iii. Add the JAR package to MaxCompute.

```
ADD jar odps-udj-example.jar;
```

iv. Register the UDJ function pay_user_log_merge_join in MaxCompute.

```
CREATE FUNCTION pay_user_log_merge_join AS 'com.aliyun.odps.udf.example.udj.PayUserLogMergeJoin' USING 'odps-udj-example.jar';
```

2. Prepare sample data.
i. Create the payment table and user_client_log table.

```
CREATE TABLE payment(user_id string,time datetime,pay_info string); CREATE TABLE user_client_log(user_id string,time datetime,content string);
```

ii. Insert data into the tables.

```
-- Insert data into the payment table. INSERT OVERWRITE TABLE payment VALUES ('1335656', datetime '2018-02-13 19:54:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 12:21:00', 'pYvotuLDIT'), ('2656199', datetime '2018-02-13 20:50:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 22:30:00', 'gZhvdySOQb'), ('8881237', datetime '2018-02-13 08:30:00', 'pYvotuLDIT'), ('8881237', datetime '2018-02-13 10:32:00', 'KBuMzRpsko'), ('9890100', datetime '2018-02-13 16:01:00', 'gZhvdySOQb'), ('9890100', datetime '2018-02-13 16:26:00', 'MxONdLckwa')
```

;

```
-- Insert data into the user_client_log table. INSERT OVERWRITE TABLE user_client_log VALUES ('1000235', datetime '2018-02-13 00:25:36', 'click FNOXAibRjkIaQPB'), ('1000235', datetime '2018-02-13 22:30:00', 'click GczrYaxvkiPultZ'), ('1335656', datetime '2018-02-13 18:30:00', 'click MxONdLckpAFUHRS'), ('1335656', datetime '2018-02-13 19:54:00', 'click mKRPGOciFDyzTgM'), ('2656199', datetime '2018-02-13 08:30:00', 'click CZwafHsbJOPNitL'), ('2656199', datetime '2018-02-13 09:14:00', 'click nYHJqIpjevkKToy'), ('2656199', datetime '2018-02-13 21:05:00', 'click gbAfPCwrGXvEjpI'), ('2656199', datetime '2018-02-13 21:08:00', 'click dhpZyWMuGjBOTJP'), ('2656199', datetime '2018-02-13 22:29:00', 'click bAsxnUdDhvfqaBr'), ('2656199', datetime '2018-02-13 22:30:00', 'click XIhZdLaOocQRmrY'), ('4356142', datetime '2018-02-13 18:30:00', 'click DYqShmGbIoWKier'), ('4356142', datetime '2018-02-13 19:54:00', 'click DYqShmGbIoWKier'), ('8881237', datetime '2018-02-13 00:30:00', 'click MpkvilgWSmhUuPn'), ('8881237', datetime '2018-02-13 06:14:00', 'click OkTYNUHMqZzlDyL'), ('8881237', datetime '2018-02-13 10:30:00', 'click OkTYNUHMqZzlDyL'), ('9890100', datetime '2018-02-13 16:01:00', 'click vOTQfBFjcgXisYU'), ('9890100', datetime '2018-02-13 16:20:00', 'click WxaLgOCcVEvhiFJ')
```

;
3. Use the UDJ function in SQL.

```
SELECT
    r.user_id,
    from_unixtime(CAST(time / 1000 AS BIGINT)) AS time,
    content
FROM (
    SELECT user_id, time, pay_info FROM payment
) p JOIN (
    SELECT user_id, time, content FROM user_client_log
) u ON p.user_id = u.user_id USING pay_user_log_merge_join(p.time, p.pay_info, u.time, u.content) r AS (user_id, time, content);
```

**Note**

Parameters in the USING clause:
**pay_user_log_merge_join**: the name of the UDJ function in SQL.
**(p.time, p.pay_info, u.time, u.content)**: the columns in both of the tables
used in the UDJ function.
**r**: the alias of the result returned by the UDJ function. You can reference this alias
in other SQL statements.
**(user_id, time, content)**: the columns returned by the UDJ function.
The following result is returned.

```
+---------+---------------------+---------------------------------------+
| user_id | time                | content                               |
+---------+---------------------+---------------------------------------+
| 1000235 | 2018-02-13 00:25:36 | click FNOXAibRjkIaQPB                 |
| 1000235 | 2018-02-13 22:30:00 | click GczrYaxvkiPultZ                 |
| 9890100 | 2018-02-13 16:01:00 | click vOTQfBFjcgXisYU, pay gZhvdySOQb |
| 9890100 | 2018-02-13 16:20:00 | click WxaLgOCcVEvhiFJ, pay MxONdLckwa |
| 1335656 | 2018-02-13 18:30:00 | click MxONdLckpAFUHRS, pay PEqMSHyktn |
| 1335656 | 2018-02-13 19:54:00 | click mKRPGOciFDyzTgM, pay PEqMSHyktn |
| 2656199 | 2018-02-13 22:29:00 | click bAsxnUdDhvfqaBr, pay gZhvdySOQb |
| 2656199 | 2018-02-13 08:30:00 | click CZwafHsbJOPNitL, pay pYvotuLDIT |
| 2656199 | 2018-02-13 09:14:00 | click nYHJqIpjevkKToy, pay pYvotuLDIT |
| 2656199 | 2018-02-13 21:05:00 | click gbAfPCwrGXvEjpI, pay PEqMSHyktn |
| 2656199 | 2018-02-13 21:08:00 | click dhpZyWMuGjBOTJP, pay PEqMSHyktn |
| 2656199 | 2018-02-13 22:30:00 | click XIhZdLaOocQRmrY, pay gZhvdySOQb |
| 4356142 | 2018-02-13 18:30:00 | click DYqShmGbIoWKier                 |
| 4356142 | 2018-02-13 19:54:00 | click DYqShmGbIoWKier                 |
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn, pay pYvotuLDIT |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL, pay pYvotuLDIT |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL, pay KBuMzRpsko |
+---------+---------------------+---------------------------------------+
```

##### UDJ pre-sorting

This topic describes the pre-sorting feature of user-defined join (UDJ) and provides an example for reference.

**Usage notes**

An iterator is used to iterate all records in the payment table and find the payment record that has the closest time to a specific log record in the user_client_log table. To perform this operation, you must load all payment records with the same user_id to an ArrayList. This method can be applied when the number of payment records is small. Due to the limits of the memory size, you must find another method to load the data if a large number of payment records have been generated. This topic describes how to address this issue by using the SORT BY clause. If the number of payment records is too large to be stored in the memory and all the data in the table has been sorted by time, you need to only compare the first element in the two lists. This method uses the SORT BY clause to pre-sort the UDJ data. To achieve the same effect by using the previous method, you need to only cache a maximum of three data records during pre-sorting. The following code shows an example:

```java
@Override public void join(Record key, Iterator<Record> left, Iterator<Record> right, Yieldable<R ecord> output) {
  outputRecord.setString(0, key.getString(0));
  if (!right.hasNext()) {
    return;
  } else if (!left.hasNext()) {
    while (right.hasNext()) {
      Record logRecord = right.next();
      outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
      outputRecord.setString(2, logRecord.getString(1));
      output.yield(outputRecord);
```

`}`

```
    return;
```

`}`

```
  long prevDelta = Long.MAX_VALUE;
  Record logRecord = right.next();
  Record payRecord = left.next();
  Record lastPayRecord = payRecord.clone();
  while (true) {
    long delta = logRecord.getDatetime(0).getTime() -
payRecord.getDatetime(0).getTime();
    if (left.hasNext() && delta > 0) {
      // The time difference between the two records is decreasing. You can continue pr
ocessing.
      // Explore the left group to try to obtain a smaller delta.
      lastPayRecord = payRecord.clone();
      prevDelta = delta;
      payRecord = left.next();
    } else {
     // The minimum delta point is reached. Check the last record,
     // output the merged result, and prepare to process the next record
     // in the right group.
      Record nearestPay = Math.abs(delta) < prevDelta ? payRecord : lastPayRecord;
      outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
      String mergedString = mergeLog(nearestPay.getString(1), logRecord.getString(1));
      outputRecord.setString(2, mergedString);
      output.yield(outputRecord);
      if (right.hasNext()) {
        logRecord = right.next();
        prevDelta = Math.abs(
          logRecord.getDatetime(0).getTime() - lastPayRecord.getDatetime(0).getTime()
```

);

```
      } else {
        break;
```

`}` `}` `}` `}`

#### Performance benefits

This topic describes the performance benefits of user-defined join (UDJ).

**Performance comparison**

A real online MapReduce job is used as an example to verify the performance of UDJ. The job runs based on a complex algorithm. In this example, two tables are joined, UDJ is used to rewrite the MapReduce job, and the correctness of the UDJ results is checked. The following figure shows the MapReduce and UDJ performance under the same data concurrency. As shown in the figure, UDJ conveniently describes the complex logic of how to handle multiple tables and greatly improves performance. The code is called only within UDJ. The entire Mapper logic in this example is executed by the native runtime engine of MaxCompute. The data exchange logic between the MaxCompute UDJ runtime engine and Java interfaces is optimized in Java code. The JOIN logic of UDJ is more efficient than that of a reducer.

### Parameterized views

This topic describes the parameterized view feature that the MaxCompute SQL Engine supports.

**Usage notes**

In the traditional views of MaxCompute, complex SQL scripts are encapsulated at the underlying layer. You can call views like reading a standard table without the need to understand the implementation mechanism at the underlying layer. Traditional views are widely used because they implement code encapsulation and reuse. However, traditional views do not support parameters. For example, you cannot pass filter conditions to filter data in the underlying tables of a view or pass other parameters to the view. This makes code reuse efficiency low. The MaxCompute SQL engine supports parameterized views and allows you to import tables or variables to customize views.

**Define a parameterized view**

**View syntax**

You can use the following syntax to create a parameterized view:

```
-- view with parameters -- param @a -a table parameter -- param @b -a string parameter -- returns a table with schema (key STRING,value STRING) CREATE VIEW IF NOT EXISTS pv1(@a table (k STRING,v BIGINT), @b STRING)
```

`AS`

```
SELECT srcp.key,srcp.value FROM srcp JOIN @a ON srcp.key=a.k AND srcp.p=@b;
```

**Syntax description**

To create a parameterized view, you must specify parameters. Therefore, you must use Script Mode SQL to create a parameterized view. The created view pv1 has two parameters: TABLE and STRING. The parameter value can be a table or of a basic data type. You can also use a subquery, such as `SELECT * FROM view_name( (SELECT 1 FROM src` WHERE a > 0), 1); , as a parameter value. When you create a view, you can set ANY for a parameter, which indicates any data type.

```
For example, CREATE VIEW paramed_view (@a ANY) AS SELECT * FROM src WHERE CASE WHEN
```

@a IS NULL THEN key1 ELSE key2 END = key3; defines that the first parameter of the view can be a value of any data type. However, the ANY type cannot be used in a specific operation, such as **+** and **AND**, which requires specific data types. A field of the ANY type is often used as a PassThrough column in the TABLE parameter. Example:

```
CREATE VIEW paramed_view (@a TABLE(name STRING, id ANY, age BIGINT)) AS SELECT * FR OM @a WHERE name = 'foo' AND age < 25; -- Call example. SELECT * FROM paramed_view((SELECT name, id, age FROM students));
```

**Note**

After you execute the `CREATE VIEW` statement to create a view, you can run the `DESC` command to obtain the description of the view. This description contains the return type of the view. The return type of a view is recalculated when the view is called. It may be different from the return type, such as ANY, that you specify when you create the view. When you create a view, you can use an asterisk (*) in the TABLE parameter to retrieve any columns. If an asterisk (*) is used to indicate any columns, you can specify a specific data type for the columns or use the value any. Example:

```
CREATE VIEW param_view (@a TABLE(key STRING, * ANY), @b TABLE(key STRING, * STRING) ) AS SELECT a.* FROM @a JOIN @b ON a.key = b.key; -- Call example. SELECT name, address FROM param_view((SELECT school, name, age, address FROM studen t), school) WHERE age < 20;
```

In this example, the view accepts two TABLE parameters. In the table specified by the first Table parameter, the first column is of the STRING type and can be followed by any columns of any data types. In the table specified by the second Table parameter, the first column is of the STRING type and can be followed by any columns of the STRING type. Take note of the following points: The varied-length part must be placed at the end of the table that is specified by the TABLE parameter. This means that the columns indicated by an asterisk (*) cannot be followed by other columns. Therefore, the table that is specified by the TABLE parameter can contain only one varied-length column. The varied-length part must be placed at the end of the table that is specified by the TABLE parameter. However, the columns of an input table may not be arranged in this sequence. In this case, the columns need to be rearranged. A subquery can be used as a parameter value and must be enclosed in a pair of parentheses (). No name is specified for the varied-length part of the table that is specified by the TABLE parameter. As a result, data in the varied-length part cannot be referenced or calculated when you define the view. Although you cannot calculate the varied-length part, you can use the SELECT * statement to transfer data in the varied-length part out of the table. The columns of the table that is specified by the Table parameter may be different from the fixed-length columns that you specify when you define the view. If the column names are different, the compiler automatically renames them. If the data types are different, the compiler performs an implicit conversion. If the implicit conversion fails, an error occurs.

**Call a parameterized view**

You can execute the following statement to call the pv1 view that you defined:

```
@a := SELECT * FROM src WHERE value >0; --call view with table variable and scalar @b := SELECT * FROM pv1(@a,'20170101'); @another_day := '20170102'; --call view with table name and scalar variable @c := SELECT * FROM pv1(src2, @another_day); @d := SELECT * FROM @c UNION ALL SELECT * FROM @b; WITH t AS(SELECT * FROM src3) SELECT * FROM @c UNION ALL SELECT * FROM @d UNION ALL SELECT * FROM pv1(t,@another_day);
```

**Note**

You can use different parameters to call the pv1 view. The value of the TABLE parameter can be the name of a physical table, view, or table variable. You can also set the TABLE parameter to a table alias by using common table expressions (CTEs). The values of common parameters can be variables or constants.

**Parameterized view description**

The script of a parameterized view can contain only data manipulation language (DML) statements. The statements, such as INSERT, CREATE TABLE, or PRINT, cannot be contained. A parameterized view can contain multiple SQL statements.

```
-- view with parameters -- param @a -a table parameter -- param @b -a string parameter -- returns a table with schema (key string,value string) CREATE VIEW IF NOT EXISTS pv2(@a TABLE (k STRING,v BIGINT), @b STRING) AS BEGIN @srcp := SELECT * FROM srcp WHERE p=@b; @pv2 := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k; END;
```

**Note**

Statements between BEGIN and END are the script of this view. The `@pv2 :=...` statement is similar to the RETURN statement in other programming languages. You can use the @pv2 :=... statement to assign a value to a variable of an implicit table that has the same name as the view. The matching rules for actual and formal view parameters are the same as those specified in a common weakly-typed language. Specifically, if a view parameter can be implicitly converted, it can match the defined parameter. For example, a value of the BIGINT type can match parameters of the DOUBLE type. For table variables, if the schema of Table a can be inserted into Table b, Table a can be used to match the table-type parameters that have the same schema as Table b. You can explicitly declare the return type to make the code easier to read.

```
CREATE VIEW IF NOT EXISTS pv3(@a table (k STRING,v BIGINT), @b STRING) RETURNS @ret TABLE (x STRING,y STRING)
```

`AS`

```
BEGIN
    @srcp := SELECT * FROM srcp WHERE p=@b;
    @ret := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k;
end;
```

**Note**

**RETURNS @ret TABLE (x STRING,y STRING)** defines the following information:
The return type is **TABLE (x STRING,y STRING)** , which is the type that the system returns to the caller. You can use this parameter to customize the table schema. The return parameter is **@ret**. The script of the view assigns a value to this parameter, which effectively defines the name of the return parameter. You can consider a view that contains no **BEGIN/END** or return variables as a simplified parameterized view.

### CLONE TABLE

This topic describes how to use the CLONE TABLE statement. This statement is used to clone data from one table to another, which improves data migration efficiency.

**Usage limits**

The schema of the destination table must be compatible with the schema of the source table. The CLONE TABLE statement can be executed for partitioned tables and non-partitioned tables. This statement cannot be executed for hash clustering tables. If you have created the destination table before the CLONE TABLE statement is executed, you can execute the CLONE TABLE statement to clone data from a maximum of 10,000 partitions at the same time. If you have not created the destination table before the CLONE TABLE statement is executed, the number of partitions from which you can clone data at the same time is unlimited. This way, the atomicity of the cloning operation is ensured. You can execute the CLONE TABLE statement for up to seven times in the same nonpartitioned table or in the same partition of a partitioned table. You cannot execute the CLONE TABLE statement for projects across regions.

**Operation instructions**

**Usage notes**

The CLONE TABLE statement is used to clone data from the src_table_name table to the desc_table_name table. After you clone data to the desc_table_name table, we recommend that you verify the data accuracy. For example, you can execute the SELECT COUNT statement to view the number of rows in the destination table or execute the DESC statement to view the table size.

```
CLONE TABLE <[src_project_name.]src_table_name> [PARTITION(spec), ...] TO <[dest_project_name.]desc_table_name> [IF EXISTS (OVERWRITE | IGNORE)];
```

`src_table_name` : required. This parameter specifies the name of the source table. `src_project_name` : optional. This parameter specifies the name of the project to which the source table belongs. If you do not specify this parameter, the name of the current project is used by default. `desc_table_name` : required. This parameter specifies the name of the destination table. If a destination table is not created, the table is created by using the CREATE TABLE LIKE statement when you execute the CLONE TABLE statement. If a destination table is created and IF EXISTS OVERWRITE is specified, data in the partitions of the destination table is overwritten when you execute the CLONE TABLE statement. If a destination table is created and IF EXISTS IGNORE is specified, the existing partitions in the table are skipped and the data in these partitions is not overwritten when you execute the CLONE TABLE statement. `dest_project_name` : optional. The name of the project to which the destination table belongs. If you do not specify this parameter, the name of the current project is used by default. None. i. Prepare sample data To help you better understand how to use this statement, this section provides sample source data。 The following example shows how to create the source table and insert data:

```
-- Create a non-partitioned table CREATE TABLE IF NOT EXISTS src_copy (
    key STRING,
    value STRING
```

);

```
INSERT INTO src_copy VALUES ('1', 'ok'); -- Create a partitioned table CREATE TABLE IF NOT EXISTS srcpart_copy (
    key STRING,
    value STRING
) PARTITIONED BY (ds STRING, hr STRING); INSERT INTO srcpart_copy PARTITION (ds = '2008-04-09', hr = '11') VALUES ('1', 'ok4 9'); INSERT INTO srcpart_copy PARTITION (ds = '2008-04-08', hr = '12') VALUES ('1', 'ok4 8');
```

ii. Operation examples

```
-- Example 1: Copy all data from the non-partitioned table src_copy to the destinat ion table src_clone CLONE TABLE src_copy TO src_clone; -- Verify data accuracy SELECT * FROM src_clone; -- Result +-----+-------+
| key | value |
+-----+-------+
```

```
+-----+-------+
| 1   | ok    |
+-----+-------+ -- Example 2: Copy data from a specified partition of the partitioned table srcpart _copy to the destination table srcpart_clone CLONE TABLE srcpart_copy PARTITION(ds = '2008-04-09', hr = '11') TO srcpart_clone I F EXISTS OVERWRITE; -- Verify data accuracy SELECT * FROM srcpart_clone; -- Result +-----+-------+------------+----+
| key | value | ds         | hr |
+-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
+-----+-------+------------+----+ -- Example 3: Copy all data from the partitioned table and skip existing partitions in the destination table CLONE TABLE srcpart_copy TO srcpart_clone IF EXISTS IGNORE; -- Verify data accuracy SELECT * FROM srcpart_clone; -- Result +-----+-------+------------+----+
| key | value | ds         | hr |
+-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
| 1   | ok48  | 2008-04-08 | 12 |
+-----+-------+------------+----+ -- Example 4: Copy all data from the partitioned table to the destination table src part_clone2 CLONE TABLE srcpart_copy TO srcpart_clone2; -- Verify data accuracy SELECT * FROM srcpart_clone2; -- Result +-----+-------+------------+----+
| key | value | ds         | hr |
+-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
| 1   | ok48  | 2008-04-08 | 12 |
+-----+-------+------------+----+
```

### Geographic functions

#### Usage notes

Geographic functions use a set of Java user-defined functions (UDFs) to allow you to perform geometric computing in MaxCompute. Before you use geographic functions, understand the following information:

**What are geographic functions?**

The application of geographic functions requires extensive knowledge in the field. Esri developed a set of open-source Hive UDFs that support simple geometric computing (see spatial-framework-for-hadoop). MaxCompute supports Hive UDFs and conducted secondary development on the functions to develop more features, such as spherical functions, grid functions, and indexing. The names of most functions remain the same as those of PostGIS, which simplifies the learning process. Supported features: Geometry models that comply with OpenGIS standards. You can use the Well-Known Text (WKT) and Well-Known Binary (WKB) formats to input and output spatial geometry objects, such as ST_Point, ST_MultiPoint, ST_LineString, ST_MultiLineString, ST_Polygon, and ST_MultiPolygon. A set of functions based on the preceding geometry models to construct objects, test geometric relationships, obtain geometry object attributes, and calculate plane and sphere measurements, such as areas and distances. A set of indexing functions, such as GeoHash, S2, and RTree, to optimize spatial joins. All algorithms used by the geographic function are based on open source technologies. For example, spatial-sdk-odps.jar contains encapsulated open-source resources that are free of charge. MaxCompute cannot control or provide support for external capabilities because they are encapsulated by using open-source algorithms. Therefore, MaxCompute does not provide explanation, maintenance, or technical support for the business, performance, and accuracy of UDFs. In case of issues, you can compare and test functions, fix errors, or replace functions based on open source implementations. Therefore, the geographic functions are suitable only for users who have a deep understanding of open-source geographic functions.

**Register geographic functions with MaxCompute**

Perform the following steps to register the geographic functions with MaxCompute and use them in your project:
1. Download three compiled JAR packages.
Click Spatial JAR to download the Spatial JAR package and rename the package name to

```
 spatial-sdk-hive.jar .
```

Click esri-geometry-api to download the Esri Geometry JAR package and rename the package to `esri-geometry-api.jar` . Obtain the spatial-sdk-odps.jar package.
2. Use the MaxCompute client (odpscmd) to access the project. Run the following script to
upload the JAR package and register the functions. Then, you can use the functions in the project or authorize other users to use the functions in other projects.

```
ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar; CREATE FUNCTION ST_Aggr_ConvexHull AS 'com.esri.hadoop.hive.ST_Aggr_ConvexHull' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Aggr_Intersection AS 'com.esri.hadoop.hive.ST_Aggr_Intersection' USING 'spatial-sdk-hive.jar,esri-geomet ry-api.jar'; CREATE FUNCTION ST_Aggr_Union AS 'com.esri.hadoop.hive.ST_Aggr_Union' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar';
```

```
CREATE FUNCTION ST_Area AS 'com.esri.hadoop.hive.ST_Area' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsBinary AS 'com.esri.hadoop.hive.ST_AsBinary' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsGeoJson AS 'com.esri.hadoop.hive.ST_AsGeoJson' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsJson AS 'com.esri.hadoop.hive.ST_AsJson' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsShape AS 'com.esri.hadoop.hive.ST_AsShape' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsText AS 'com.esri.hadoop.hive.ST_AsText' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Bin AS 'com.esri.hadoop.hive.ST_Bin' USING 'spatial-sdk-hive.jar ,esri-geometry-api.jar'; CREATE FUNCTION ST_BinEnvelope AS 'com.esri.hadoop.hive.ST_BinEnvelope' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Boundary AS 'com.esri.hadoop.hive.ST_Boundary' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Buffer AS 'com.esri.hadoop.hive.ST_Buffer' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Centroid AS 'com.esri.hadoop.hive.ST_Centroid' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Contains AS 'com.esri.hadoop.hive.ST_Contains' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_ConvexHull AS 'com.esri.hadoop.hive.ST_ConvexHull' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_CoordDim AS 'com.esri.hadoop.hive.ST_CoordDim' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Crosses AS 'com.esri.hadoop.hive.ST_Crosses' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Difference AS 'com.esri.hadoop.hive.ST_Difference' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Dimension AS 'com.esri.hadoop.hive.ST_Dimension' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Disjoint AS 'com.esri.hadoop.hive.ST_Disjoint' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Distance AS 'com.esri.hadoop.hive.ST_Distance' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_EndPoint AS 'com.esri.hadoop.hive.ST_EndPoint' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Envelope AS 'com.esri.hadoop.hive.ST_Envelope' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_EnvIntersects AS 'com.esri.hadoop.hive.ST_EnvIntersects' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Equals AS 'com.esri.hadoop.hive.ST_Equals' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_ExteriorRing AS 'com.esri.hadoop.hive.ST_ExteriorRing' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeodesicLengthWGS84 AS 'com.esri.hadoop.hive.ST_GeodesicLengthWGS84' USING 'spatial-sdk-hive.jar,esri-geomet ry-api.jar'; CREATE FUNCTION ST_GeomCollection AS 'com.esri.hadoop.hive.ST_GeomCollection' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Geometry AS 'com.esri.hadoop.hive.ST_Geometry' USING 'spatialsdkhiejaresrigeometr apijar'
```

```
sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeometryN AS 'com.esri.hadoop.hive.ST_GeometryN' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeometryType AS 'com.esri.hadoop.hive.ST_GeometryType' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromGeoJson AS 'com.esri.hadoop.hive.ST_GeomFromGeoJson' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromJson AS 'com.esri.hadoop.hive.ST_GeomFromJson' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromShape AS 'com.esri.hadoop.hive.ST_GeomFromShape' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromText AS 'com.esri.hadoop.hive.ST_GeomFromText' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromWKB AS 'com.esri.hadoop.hive.ST_GeomFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_InteriorRingN AS 'com.esri.hadoop.hive.ST_InteriorRingN' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersection AS 'com.esri.hadoop.hive.ST_Intersection' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersects AS 'com.esri.hadoop.hive.ST_Intersects' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Is3D AS 'com.esri.hadoop.hive.ST_Is3D' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsClosed AS 'com.esri.hadoop.hive.ST_IsClosed' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsEmpty AS 'com.esri.hadoop.hive.ST_IsEmpty' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsMeasured AS 'com.esri.hadoop.hive.ST_IsMeasured' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsRing AS 'com.esri.hadoop.hive.ST_IsRing' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsSimple AS 'com.esri.hadoop.hive.ST_IsSimple' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Length AS 'com.esri.hadoop.hive.ST_Length' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_LineFromWKB AS 'com.esri.hadoop.hive.ST_LineFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_LineString AS 'com.esri.hadoop.hive.ST_LineString' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_M AS 'com.esri.hadoop.hive.ST_M' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxM AS 'com.esri.hadoop.hive.ST_MaxM' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxX AS 'com.esri.hadoop.hive.ST_MaxX' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxY AS 'com.esri.hadoop.hive.ST_MaxY' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxZ AS 'com.esri.hadoop.hive.ST_MaxZ' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinM AS 'com.esri.hadoop.hive.ST_MinM' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinX AS 'com.esri.hadoop.hive.ST_MinX' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinY AS 'com.esri.hadoop.hive.ST_MinY' USING 'spatial-sdk-hive jar,esri-geometry-apijar';
```

```
.jar,esrigeometryapi.jar; CREATE FUNCTION ST_MinZ AS 'com.esri.hadoop.hive.ST_MinZ' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MLineFromWKB AS 'com.esri.hadoop.hive.ST_MLineFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPointFromWKB AS 'com.esri.hadoop.hive.ST_MPointFromWKB' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPolyFromWKB AS 'com.esri.hadoop.hive.ST_MPolyFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiLineString AS 'com.esri.hadoop.hive.ST_MultiLineString' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiPoint AS 'com.esri.hadoop.hive.ST_MultiPoint' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiPolygon AS 'com.esri.hadoop.hive.ST_MultiPolygon' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumGeometries AS 'com.esri.hadoop.hive.ST_NumGeometries' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumInteriorRing AS 'com.esri.hadoop.hive.ST_NumInteriorRing' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumPoints AS 'com.esri.hadoop.hive.ST_NumPoints' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Overlaps AS 'com.esri.hadoop.hive.ST_Overlaps' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Point AS 'com.esri.hadoop.hive.ST_Point' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointFromWKB AS 'com.esri.hadoop.hive.ST_PointFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointN AS 'com.esri.hadoop.hive.ST_PointN' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointZ AS 'com.esri.hadoop.hive.ST_PointZ' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PolyFromWKB AS 'com.esri.hadoop.hive.ST_PolyFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Polygon AS 'com.esri.hadoop.hive.ST_Polygon' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Relate AS 'com.esri.hadoop.hive.ST_Relate' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SetSRID AS 'com.esri.hadoop.hive.ST_SetSRID' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SRID AS 'com.esri.hadoop.hive.ST_SRID' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_StartPoint AS 'com.esri.hadoop.hive.ST_StartPoint' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SymmetricDiff AS 'com.esri.hadoop.hive.ST_SymmetricDiff' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Touches AS 'com.esri.hadoop.hive.ST_Touches' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Union AS 'com.esri.hadoop.hive.ST_Union' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Within AS 'com.esri.hadoop.hive.ST_Within' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_X AS 'com.esri.hadoop.hive.ST_X' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Y AS 'com.esri.hadoop.hive.ST_Y' USING 'spatial-sdkhive.jar,esri-geometry-api.jar';
```

`j` `,` `g` `y` `p` `j`

```
CREATE FUNCTION ST_Z AS 'com.esri.hadoop.hive.ST_Z' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHash' USI NG 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_PointFromGeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_PointFromGeoHash' USING 'spatial-sdk-odps. jar'; CREATE FUNCTION ST_GeoHashNeighbours AS 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHashNeighbours' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_EnvelopeFromGeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_EnvelopeFromGeoHash' USING 'spatial-sdk-od ps.jar'; CREATE FUNCTION ST_AreaWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_AreaWGS84' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_BufferWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_BufferWGS84' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_DistanceWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_DistanceWGS84' USING 'spatial-sdk-odps.jar
```

';

```
CREATE FUNCTION ST_GeodesicDistance AS 'com.aliyun.odps.geospatial.udf.compute.ST_GeodesicDistance' USING 'spatial-sdk-odps. jar'; CREATE FUNCTION ST_Transform AS 'com.aliyun.odps.geospatial.udf.compute.ST_Transform' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_TransformWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_TransformWGS84' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_IsValid AS 'com.aliyun.odps.geospatial.udf.compute.ST_IsValid' USI NG 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_S2CellCenterPoint AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellCenterPoint' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_S2CellIdsFromGeom AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromGeom' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_S2CellIdsFromText AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromText' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_S2CellNeighbours AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellNeighbours' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_Area_Sphere AS 'com.aliyun.odps.geospatial.udf.compute.ST_Area_Sphere' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_Distance_Sphere AS 'com.aliyun.odps.geospatial.udf.compute.ST_Distance_Sphere' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_BuildRTreeIndex AS 'com.aliyun.odps.geospatial.udf.index.ST_BuildRTreeIndex' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_ContainsFromRTree AS
```

```
'com.aliyun.odps.geospatial.udf.index.ST_ContainsFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_CrossesFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_CrossesFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_EqualsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_EqualsFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_IntersectsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_IntersectsFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_OverlapsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_OverlapsFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_TouchesFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_TouchesFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_WithinFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_WithinFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_KNNFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_KNNFromRTree' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_Simplify AS 'com.aliyun.odps.geospatial.udf.compute.ST_Simplify' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_SimplifyVW AS 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyVW' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_SimplifyPreserveTopology AS 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyPreserveTopology' USING 'spatial-s dk-odps.jar'; CREATE FUNCTION ST_LineLocatePoint AS 'com.aliyun.odps.geospatial.udf.compute.ST_LineLocatePoint' USING 'spatial-sdk-odps.j ar';
```

To perform a bug fix or version upgrade, run the following command to rename the JAR package to the name in Step 1 after compilation:

```
DROP resource esri-geometry-api.jar; DROP resource spatial-sdk-hive.jar; DROP resource spatial-sdk-odps.jar; ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar;
```

Before you run SQL statements to call the functions, submit the following flags. The isolation flag provides a secure and isolated environment for running UDFs.

```
SET odps.sql.hive.compatible=true; SET odps.sql.udf.java.retain.legacy=false; SET odps.isolation.session.enable=true;
```

**Test the functions**

Submit SQL statements in the MaxCompute client to test whether a UDF can work as expected. Sample commands:

```
set odps.sql.hive.compatible=true; select ST_AsText(ST_Point(1, 2));
```

The following output indicates that the UDF is registered with MaxCompute.

```
+-----+
| _c0 |
+-----+
| POINT (1 2) |
+-----+
```

For more information about how to use the geographic function, see UDF-Documentation.

#### Constructors

##### ST_AsBinary

This topic describes how to use the ST_AsBinary function in MaxCompute and provides reference examples. This function returns the Well-Known Binary (WKB) representation of a geometry.

```
ST_AsBinary(ST_Geometry);
```

ST_Geometry: required. This parameter specifies a geometry. This function returns the WKB representation of a geometry.

```
SELECT ST_AsBinary(ST_Point(1, 2)); -- Result +--------------------------------------------------------------+
| _c0                                                          |
+--------------------------------------------------------------+
| =01=01=00=00=00=00=00=00=00=00=00=F0?=00=00=00=00=00=00=00@  |
+--------------------------------------------------------------+
```

##### ST_AsGeoJson

This topic describes how to use the ST_AsGeoJson function in MaxCompute and provides reference examples. This function returns the GeoJSON expression of a geometry.

```
ST_ASGEOJSON(ST_GEOMETRY geometry);
```

geometry: required. This parameter specifies a geometry. This function returns the GeoJSON expression of a geometry.

```
SELECT ST_ASGEOJSON(ST_POINT(1.0, 2.0)); -- Result +-------------------------------------------------+
| _c0                                             |
+-------------------------------------------------+
| {"type":"Point","coordinates":[1,2],"crs":null} |
+-------------------------------------------------+
```

##### ST_AsJson

This topic describes how to use the ST_ASJSON function in MaxCompute and provides reference examples. This function returns the JSON expression of a geometry.

```
ST_ASJSON(ST_GEOMETRY);
```

ST_GEOMETRY: required. This parameter specifies a geometry. This function returns the JSON expression of a geometry.

```
SELECT ST_ASJSON(ST_POINT(1.0, 2.0)); -- Result +-----------------------+
| _c0                   |
+-----------------------+
| {"x":1.0,"y":2.0}     |
+-----------------------+ SELECT ST_ASJSON(ST_SETSRID(ST_POINT(1, 1), 4326)); -- Result +-----------------------------------------------------------+
| _c0                                                       |
+-----------------------------------------------------------+
| {"x":1.0,"y":1.0,"spatialReference":{"wkid":4326}}        |
+-----------------------------------------------------------+
```

##### ST_AsShape

This topic describes how to use the ST_AsShape function in MaxCompute and provides reference examples. This function returns the Esri shape representation of a geometry.

```
ST_AsShape(ST_GEOMETRY);
```

ST_GEOMETRY: required. This parameter specifies a geometry. This function returns the Esri shape representation of a geometry.

```
SELECT ST_AsShape(ST_POINT(1, 2));
```

##### ST_AsText

This topic describes how to use the ST_AsText function in MaxCompute and provides reference examples. This function returns the Well-Known Text (WKT) expression of a geometry.

```
ST_ASTEXT(ST_GEOMETRY);
```

ST_GEOMETRY: required. This parameter specifies a geometry. This function returns the WKT expression of a geometry.

```
SELECT ST_ASTEXT(ST_POINT(1, 2)); -- Result +-------------+
| _c0         |
+-------------+
| POINT (1 2) |
+-------------+
```

##### ST_GeomCollection

This topic describes how to use the ST_GeomCollection function in MaxCompute and provides reference examples. This function constructs a multi-part geometry by using a Well-Known Text (WKT) expression of the Open Geospatial Consortium (OGC). ST_GeomCollection in MaxCompute does not support the collection feature and supports only multi-part geometries.

```
ST_GeomCollection(STRING wkt);
```

wkt: required. This parameter must be of the STRING type. It specifies an OGC WKT expression. This function returns a multi-part geometry.

```
SELECT ST_GeomCollection('MULTIPOINT ((1 0), (2 3))'); -- The following usage is not supported (collection feature) -- ST_GeomCollection('POINT(1 1), LINESTRING(2 0,3 0)')
```

##### ST_GeomFromGeoJson

This topic describes how to use the ST_GeomFromGeoJson function in MaxCompute and provides reference examples. This function constructs a geometry from a GeoJSON expression.

```
ST_GeomFromGeoJson(STRING json);
```

json: required. This parameter must be of the STRING type. It specifies a GeoJSON expression. This function returns a geometry.

```
SELECT ST_GeomFromGeoJson('{"type":"Point", "coordinates":[1.2, 2.4]}'); -- Construct an ST_LineString SELECT ST_GeomFromGeoJson('{"type":"LineString", "coordinates":[[1,2], [3,4]]}');
```

##### ST_GeomFromJSON

This topic describes how to use the ST_GeomFromJSON function in MaxCompute and provides reference examples. This function constructs a geometry from an Esri JSON expression.

```
ST_GeomFromJSON(STRING json);
```

json: required. This parameter must be of the STRING type. It specifies an Esri JSON expression. This function returns a geometry.

```
SELECT ST_GeomFromJSON('{"x":0.0,"y":0.0}');
```

##### ST_GeomFromShape

This topic describes how to use the ST_GeomFromShape function in MaxCompute and provides reference examples. This function constructs a geometry from an Esri shape expression.

```
ST_GeomFromShape(shape);
```

shape: required. This parameter specifies an Esri shape expression. This function returns a geometry.

```
SELECT ST_GeomFromShape(ST_AsShape(ST_Point(1, 2)));
```

##### ST_GeomFromText

This topic describes how to use the ST_GeomFromText function in MaxCompute and provides reference examples. This function constructs a geometry from a Well-Known Text (WKT) expression of Open Geospatial Consortium (OGC).

```
ST_GeomFromText(STRING wkt);
```

wkt: required. This parameter must be of the STRING type. It specifies an OGC WKT expression. This function returns a geometry.

```
-- Construct an ST_Linestring SELECT ST_GeomFromText('linestring (1 0, 2 3)'); -- Construct an ST_MultiPoint SELECT ST_GeomFromText('multipoint ((1 0), (2 3))');
```

##### ST_GeomFromWKB

This topic describes how to use the ST_GeomFromWKB function in MaxCompute and provides reference examples. This function constructs a geometry from a Well-Known Binary (WKB) expression of Open Geospatial Consortium (OGC).

```
ST_GeomFromWKB(BINARY wkb);
```

wkb: required. This parameter specifies an OGC WKB expression of the BINARY type. The function returns a geometry.

```
-- Construct an ST_Linestring SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)'))); -- Construct an ST_MultiPoint SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))')));
```

##### ST_GeometryType

This topic describes how to use the ST_GeometryType function in MaxCompute and provides reference examples. This function returns the type of a geometry.

```
ST_GeometryType(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the STRING type. This function returns the type name, such as ST_Point, ST_LineString, or ST_Polygon, of a geometry.

```
SELECT ST_GeometryType(ST_Point(1.5, 2.5)); -- Result +----------+
| _c0      |
+----------+
| ST_POINT |
+----------+ SELECT ST_GeometryType(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +---------------+
| _c0           |
+---------------+
| ST_LINESTRING |
+---------------+ SELECT ST_GeometryType(ST_Polygon(2, 0, 2, 3, 3, 0)); -- Result +------------+
| _c0        |
+------------+
| ST_POLYGON |
+------------+
```

##### ST_LineString

This topic describes how to use the ST_LineString function in MaxCompute and provides reference examples. This function constructs a 2D line string.

```
ST_LineString(x, y, [x, y]*); ST_LineString('linestring( ... )'); ST_LineString(ARRAY(x+), ARRAY(y+)); ST_LineString(ARRAY(ST_Point(x,y)+));
```

x, y: required. These parameters specify the coordinate values of a point. The values must be of the DOUBLE type. linestring( ... ): required. This parameter specifies a linestring expression in Well-Known Text (WKT) format. The value must be of the STRING type. ARRAY(x+), ARRAY(y+): required. These parameters specify the arrays of x-coordinates and y-coordinates. The values must be of the ARRAY type. ARRAY(ST_Point(x,y)+): required. This parameter specifies an ST_Point object array. The value must be of the ARRAY type. This function returns a geometry of the ST_LineString type.

```
-- Construct a line string from coordinate values. SELECT ST_LineString(1, 1, 2, 2, 3, 3); -- Construct a line string from a WKT expression. SELECT ST_LineString('linestring(1 1, 2 2, 3 3)'); -- Construct a line string from coordinate arrays. SELECT ST_LineString(ARRAY(1, 2, 3), ARRAY(1, 2, 3)); -- Construct a line string from an array of ST_Point objects. SELECT ST_LineString(ARRAY(ST_Point(1, 1), ST_Point(2, 2), ST_Point(3, 3)));
```

##### ST_LineFromWKB

This topic describes how to use the ST_LineFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D line string by using the well-known binary (WKB) format of Open Geospatial Consortium (OGC).

```
ST_LineFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type. It specifies an OGC WKB expression. This function returns a geometry of the ST_LineString type.

```
SELECT ST_LineFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)')));
```

##### ST_MultiLineString

This topic describes how to use the ST_MultiLineString function in MaxCompute and provides reference examples. This function constructs 2D multilinestrings.

```
ST_MultiLineString(ARRAY(x1, y1, x2, y2, ...), ARRAY(x1, y1, x2, y2, ...), ...); ST_MultiLineString('multilinestring( ... )');
```

ARRAY(x1, y1, x2, y2, ...): required. This parameter must be of the ARRAY type and it specifies the coordinate values for each line. multilinestring( ... ): required. This parameter must be of the STRING type and it specifies a multilinestring expression in Well-Known Text (WKT) format. This function returns a geometry of the ST_MultiLineString type.

```
-- Construct a two-dimensional multilinestring from coordinate arrays SELECT ST_MultiLineString(ARRAY(1, 1, 2, 2), ARRAY(10, 10, 20, 20)); -- Construct a two-dimensional multilinestring from a WKT expression SELECT ST_MultiLineString('multilinestring ((1 1, 2 2), (10 10, 20 20))');
```

##### ST_MLineFromWKB

This topic describes how to use the ST_MLineFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D multilinestring from a Well-Known Binary (WKB) expression of Open Geospatial Consortium (OGC).

```
ST_MLineFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type. It specifies an OGC WKB expression. This function returns a geometry of the ST_MultiLineString type.

```
-- Construct a 2D multilinestring. SELECT ST_MLineFromWKB(ST_AsBinary(ST_GeomFromText('multilinestring ((1 0, 2 3), (5 7 , 7 5))')));
```

##### ST_MultiPoint

This topic describes how to use the ST_MultiPoint function in MaxCompute and provides reference examples. This function constructs a multipoint geometry.

```
ST_MultiPoint(x1, y1, x2, y2, x3, y3); ST_MultiPoint('multipoint( ... )');
```

x1, y1, x2, y2, ...: required. These parameters must be of the DOUBLE type. They specify the coordinate values of points. multipoint( ... ): required. This parameter must be of the STRING type. It specifies a multipoint expression in Well-Known Text (WKT) format. This function returns a multipoint geometry of the GEOMETRY (MULTIPOINT) type.

```
-- Construct three points from coordinate values SELECT ST_MultiPoint(1, 1, 2, 2, 3, 3); -- Construct two points from a WKT expression SELECT ST_MultiPoint('MULTIPOINT ((10 40), (40 30))');
```

##### ST_MPointFromWKB

This topic describes how to use the ST_MPointFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D multipoint geometry from a Well-Known Binary (WKB) representation of Open Geospatial Consortium (OGC).

```
ST_MPointFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type. It specifies an OGC WKB representation. This function returns a geometry of the ST_MultiPoint type.

```
SELECT ST_MPointFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))')));
```

##### ST_MultiPolygon

This topic describes how to use the ST_MultiPolygon function in MaxCompute and provides reference examples. This function constructs a 2D polygon.

```
ST_MultiPolygon(ARRAY(x1, y1, x2, y2, ...), ARRAY(x1, y1, x2, y2, ...), ...); ST_MultiPolygon('multipolygon ( ... )');
```

ARRAY(x1, y1, x2, y2, ...): required. This parameter must be of the ARRAY type. It specifies the coordinate values for a polygon. multipolygon ( ... ): required. This parameter specifies a multipolygon expression in Well- Known Text (WKT) format. It must be of the STRING type. This function returns a geometry of the ST_MultiPolygon type.

```
SELECT ST_MultiPolygon(ARRAY(1, 1, 1, 2, 2, 2, 2, 1), ARRAY(3, 3, 3, 4, 4, 4, 4, 3)); SELECT ST_MultiPolygon('multipolygon (((0 0, 0 1, 1 0, 0 0)), ((2 2, 2 3, 3 2, 2 2))) ');
```

##### ST_MPolyFromWKB

This topic describes how to use the ST_MPolyFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D polygon from a Well-Known Text (WKB) expression of Open Geospatial Consortium (OGC).

```
ST_MPolyFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type. It specifies an OGC WKB expression. This function returns a geometry of the ST_MultiPolygon type.

```
SELECT ST_MPolyFromWKB(ST_AsBinary(ST_GeomFromText('multipolygon (((0 0, 1 0, 0 1, 0 0)), ((2 2, 1 2, 2 1, 2 2)))')));
```

##### ST_Point

This topic describes how to use the ST_Point function in MaxCompute and provides reference examples. This function constructs a 2D point.

```
ST_Point(DOUBLE x, DOUBLE y); ST_Point(STRING 'point (x y)');
```

x, y: required. These parameters must be of the DOUBLE type. They specify the coordinate values of a point. point (x y): required. This parameter must be of the STRING type. It specifies a point expression in the Well-Known Text (WKT) format. The function returns a geometry of the ST_Point type.

```
-- Use coordinate values to construct a two-dimensional point SELECT ST_Point(1, 2); -- Use a WKT expression to construct a two-dimensional point SELECT ST_Point('point (0 0)');
```

##### ST_PointFromWKB

This topic describes how to use the ST_PointFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D point from a Well-Known Binary (WKB) expression of Open Geospatial Consortium (OGC).

```
ST_PointFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type. It specifies an OGC WKB expression. This function returns a geometry of the ST_Point type.

```
SELECT ST_PointFromWKB(ST_AsBinary(ST_GeomFromText('point (1 0)')));
```

##### ST_PointZ

This topic describes how to use the ST_PointZ function in MaxCompute and provides reference examples. This function constructs a 3D point.

```
ST_PointZ(DOUBLE x, DOUBLE y, DOUBLE z);
```

x: required. This parameter must be of the DOUBLE type. It specifies the X-coordinate of a point. y: required. This parameter must be of the DOUBLE type. It specifies the Y-coordinate of a point. z: required. This parameter must be of the DOUBLE type. It specifies the Z-coordinate of a point. This function returns a 3D geometry of the ST_Point type.

```
-- Construct a 3D point SELECT ST_PointZ(1, 2, 3);
```

##### ST_Polygon

This topic describes how to use the ST_Polygon function in MaxCompute and provides reference examples. This function constructs a 2D polygon.

```
ST_Polygon(DOUBLE x, DOUBLE y, [DOUBLE x, DOUBLE y]*); ST_Polygon(STRING 'polygon( ... )');
```

x, y: required. These parameters must be of the DOUBLE type. They specify the coordinate values for each vertex of a polygon. polygon( ... ): required. This parameter must be of the STRING type. It specifies a polygon expression in Well-Known Text (WKT) format. This function returns a geometry of the ST_Polygon type.

```
-- Construct a square from coordinate values SELECT ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1); -- Construct a triangle from a WKT expression SELECT ST_Polygon('polygon ((1 1, 4 1, 1 4, 1 1))');
```

##### ST_PolyFromWKB

This topic describes how to use the ST_PolyFromWKB function in MaxCompute and provides reference examples. This function constructs a 2D polygon from a Well-Known Binary (WKB) expression of Open Geospatial Consortium (OGC).

**Syntax**

```
ST_PolyFromWKB(BINARY wkb);
```

wkb: required. This parameter must be of the BINARY type and it specifies an OGC WKB expression. This function returns a geometry of the ST_Polygon type.

```
SELECT ST_PolyFromWKB(ST_AsBinary(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))') ));
```

##### ST_SetSRID

This topic describes how to use the ST_SetSRID function and provides reference examples. This function sets the Spatial Reference Identifier (SRID) of a geometry.

```
ST_SetSRID(ST_Geometry, SRID);
```

ST_Geometry: required. This parameter specifies a geometry. SRID: required. This parameter specifies an SRID of the BIGINT type. This function returns a geometry with a specified SRID.

```
SELECT ST_SetSRID(ST_Point(1.5, 2.5), 4326);
```

#### Accessors

##### ST_Area

This topic describes how to use the ST_Area function in MaxCompute and provides reference examples. This function returns the area of one or more polygons.

```
ST_Area(ST_Polygon);
```

ST_Polygon: required. This parameter specifies a geometry of the ST_Polygon type. This function returns the area of a polygon. The return value is of the DOUBLE type.

```
SELECT ST_Area(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +------------+
| _c0        |
+------------+
| 9.0        |
+------------+
```

##### ST_Centroid

This topic describes how to use the ST_Centroid function in MaxCompute and provides reference examples. This function returns the center point of the minimum bounding rectangle of a polygon.

```
ST_Centroid(ST_Polygon polygon);
```

polygon: required. This parameter specifies a geometry of the ST_Polygon type. This function returns a geometry of the ST_Point type, which represents the center point of the minimum bounding rectangle of a polygon.

```
SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 3 6, 6 0, 0 0))')); SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 0 8, 8 0, 0 0))'));
```

##### ST_CoordDim

This topic describes how to use the ST_CoordDim function in MaxCompute and provides reference examples. This function returns the number of coordinate dimensions of a point.

```
ST_CoordDim(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. This function returns a value of the BIGINT type. It indicates the number of coordinate dimensions of a point, which can be 2, 3, or 4.

```
-- 2D point SELECT ST_CoordDim(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 2    |
+------+ -- 3D point SELECT ST_CoordDim(ST_PointZ(1.5, 2.5, 3)); -- Result +------+
| _c0  |
+------+
| 3    |
+------+ -- 4D point SELECT ST_CoordDim(ST_Point(1.5, 2.5, 3., 4.)); -- Result +------+
| _c0  |
+------+
| 4    |
+------+
```

##### ST_Dimension

This topic describes how to use the ST_Dimension function in MaxCompute and provides reference examples. This function returns the spatial dimension of a geometry.

```
ST_Dimension(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. This function returns a value of the BIGINT type. The value indicates the spatial dimension of a geometry. A value of 0 indicates a point, 1 indicates a line, and 2 indicates a surface.

```
SELECT ST_Dimension(ST_Point(1.5, 2.5)); -- Return result +------+
| _c0  |
+------+
| 0    |
+------+ -- Spatial dimension of a line SELECT ST_Dimension(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Return result +------+
| _c0  |
+------+
| 1    |
+------+ -- Spatial dimension of a surface SELECT ST_Dimension(ST_Polygon(2, 0, 2, 3, 3, 0)); -- Return result +------+
| _c0  |
+------+
| 2    |
+------+
```

##### ST_Distance

This topic describes how to use the ST_Distance function in MaxCompute and provides reference examples. This function returns the distance between two geometries.

```
ST_Distance(ST_Geometry, ST_Geometry);
```

ST_Geometry1: required. This parameter specifies the first geometry. ST_Geometry2: required. This parameter specifies the second geometry. This function returns a DOUBLE value that represents the distance between two geometries.

```
SELECT ST_Distance(ST_Point(0.0, 0.0), ST_Point(3.0, 4.0)); -- Result +------+
| _c0  |
+------+
| 5.0  |
+------+
```

##### ST_GeodesicLengthWGS84

This topic describes how to use the ST_GeodesicLengthWGS84 function in MaxCompute and provides reference examples. The function returns the distance along a line on the WGS84 spheroid in meters. The geometry must use the WGS84 coordinate system. Otherwise, the function returns NULL.

```
ST_GeodesicLengthWGS84(ST_Geometry line);
```

line: required. This parameter must be of the ST_Geometry type. It specifies a geometry that uses the WGS84 coordinate system with an SRID of 4326. Otherwise, the function returns NULL. This function returns a DOUBLE value that represents the distance along a line on the WGS84 spheroid in meters.

```
SELECT ST_GeodesicLengthWGS84(ST_SetSRID(ST_LineString(0.0, 0.0, 0.3, 0.4), 4326)); -- Result +---------------------+
| _c0                 |
+---------------------+
| 55421.408578278686  |
+---------------------+ SELECT ST_GeodesicLengthWGS84(ST_SetSRID(ST_GeomFromText('MultiLineString((0.0 80.0, 0.3 80.4))'), 4326)); -- Result +--------------------+
| _c0                |
+--------------------+
| 45026.96274781222  |
+--------------------+
```

##### ST_GeometryN

This topic describes how to use the ST_GeometryN function in MaxCompute and provides reference examples. The function returns the nth ST_Geometry object in a collection, where n starts from 1.

```
ST_GeometryN(ST_GeometryCollection, BIGINT n);
```

ST_GeometryCollection: required. This parameter specifies a geometry collection. n: required. This parameter must be of the BIGINT type. It specifies the offset of the geometry to be returned in the collection, starting from 1. The function returns the nth geometry in a collection.

```
-- Return the third point in the multipoint SELECT ST_GeometryN(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 10))' ), 3); -- Return the second line in the multilinestring SELECT ST_GeometryN(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8))'), 2);
```

##### ST_Is3D

This topic describes how to use the ST_Is3D function in MaxCompute and provides reference examples. This function determines whether a geometry is a 3D geometry. It returns true if the geometry is 3D, and false otherwise.

```
ST_Is3D(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. This function returns a value of the BOOLEAN type. The function returns true if the geometry is a 3D geometry, and false otherwise.

```
-- 2D polygon SELECT ST_Is3D(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ -- 2D line SELECT ST_Is3D(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ -- 2D point SELECT ST_Is3D(ST_Point(3., 4.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ -- 3D point SELECT ST_Is3D(ST_PointZ(3., 4., 2)); -- Result +------+
| _c0  |
+------+
| true |
+------+
```

##### ST_IsClosed

This topic describes how to use the ST_IsClosed function in MaxCompute and provides reference examples. If a linestring or multiple linestrings are closed, this function returns True. Otherwise, it returns False.

```
ST_IsClosed(ST_[Multi]LineString);
```

ST_[Multi]LineString: required. This parameter specifies a geometry of the ST_LineString or ST_MultiLineString type. This function returns a value of the BOOLEAN type. The function returns true if the linestring is closed. Otherwise, it returns false.

```
-- Closed linestring SELECT ST_IsClosed(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.)); -- Result +------+
| _c0  |
+------+
| true |
+------+ -- Non-closed linestring SELECT ST_IsClosed(ST_LineString(0., 0., 3., 4.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_IsEmpty

This topic describes how to use the ST_IsEmpty function in MaxCompute and provides reference examples. The function returns true if a geometry is empty and returns false otherwise.

```
ST_IsEmpty(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. This function returns a value of the BOOLEAN type. The function returns true if a geometry is empty and returns false otherwise.

```
-- Non-empty geometry object SELECT ST_IsEmpty(ST_Point(1.5, 2.5)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ -- Empty geometry object SELECT ST_IsEmpty(ST_GeomFromText('point empty')); -- Result +------+
| _c0  |
+------+
| true |
+------+
```

##### ST_IsMeasured

This topic describes the Accessor function ST_IsMeasured and provides an example for reference. Function declaration:

```
ST_IsMeasured(geometry)
```

Description: If the input geometry has M coordinates (measures), this function returns True. Otherwise, it returns False. Example:

```
SELECT ST_IsMeasured(ST_Polygon(1,1, 1,4, 4,4, 4,1)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_Point(3., 4.)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_PointM(3., 4., 2)) FROM src LIMIT 1; -- True is returned.
```

##### ST_IsSimple

This topic describes how to use the ST_IsSimple function in MaxCompute and provides reference examples. This function determines whether a geometry is a simple object. The function returns true if the geometry is simple, and returns false otherwise. Simple geometries include the following types: Simple point: A point has no interior rings and consists of only one coordinate. Simple line: A linestring has no self-intersections or intersections, no overlapping parts, and no interior rings. Simple multipoint: A multipoint geometry consists of multiple simple points, and each point has no interior rings. Simple multilinestring: A multilinestring geometry consists of multiple simple linestrings, and each linestring has no self-intersections or intersections, no overlapping segments, and no interior rings. Simple polygon: A polygon geometry consists of one exterior ring and zero or more interior rings. Each ring is a simple linestring, and no self-intersections, intersections, or overlapping segments exist between the exterior ring and the interior rings.

```
ST_IsSimple(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. This function returns a value of the BOOLEAN type. The function returns true if a geometry is a simple object, and returns false otherwise.

```
-- Simple object (point) SELECT ST_IsSimple(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| true |
+------+ -- Non-simple object (self-intersecting linestring) SELECT ST_IsSimple(ST_LineString(0., 0., 1., 1., 0., 1., 1., 0.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_IsRing

This topic describes how to use the ST_IsRing function in MaxCompute and provides reference examples. This function determines whether a geometry is a closed ring, meaning that the start point and end point are identical. The function returns true if the geometry is a closed ring, and returns false otherwise.

```
ST_IsRing(ST_LineString);
```

ST_LineString: required. This parameter specifies a geometry of the ST_LineString type. This function returns a value of the BOOLEAN type. The function returns true if a linestring is a closed ring (the start point and end point are identical, and the linestring does not intersect itself), and returns false otherwise.

```
-- Closed ring SELECT ST_IsRing(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.)); -- Result +------+
| _c0  |
+------+
| true |
+------+ -- Self-intersecting closed linestring (non-simple ring) SELECT ST_IsRing(ST_LineString(0., 0., 1., 1., 1., 2., 2., 1., 1., 1., 0., 0.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ -- Non-closed linestring SELECT ST_IsRing(ST_LineString(0., 0., 3., 4.)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Length

This topic describes how to use the ST_Length function in MaxCompute and provides reference examples. This function returns the length of a linestring.

```
ST_Length(line);
```

line: required. This parameter specifies a geometry of the ST_LineString type. This function returns a value of the DOUBLE type. The value indicates the length of a linestring.

```
SELECT ST_Length(ST_LineString(0.0, 0.0, 3.0, 4.0)); -- Result +------+
| _c0  |
+------+
| 5.0  |
+------+
```

##### ST_M

This topic describes the Accessor function ST_M and provides an example for reference. Function declaration:

```
ST_M(geometry)
```

Description: This function returns the M coordinate of the input geometry. Example:

```
SELECT ST_M(ST_PointM(3., 4., 2)) FROM src LIMIT 1;
```

Returned results:

##### ST_MaxM

This topic describes the Accessor function ST_MaxM and provides examples for reference. Function declaration:

```
ST_MaxM(geometry)
```

Description: This function returns the maximum M coordinate of the input geometry. Examples:

```
SELECT ST_MaxM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MaxM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### ST_MinM

This topic describes the Accessor function ST_MinM and provides examples for reference. Function declaration:

```
ST_MinM(geometry)
```

Description: This function returns the minimum M coordinate of the input geometry. Examples:

```
SELECT ST_MinM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MinM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### ST_X

This topic describes how to use the ST_X function in MaxCompute and provides reference examples. This function returns the X-axis coordinate of a point.

```
ST_X(ST_Point point);
```

point: required. This parameter specifies a geometry of the ST_Point type. This parameter returns a value of the DOUBLE type. This value indicates the X-axis coordinate of a point.

```
SELECT ST_X(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 1.5  |
+------+
```

##### ST_Y

This topic describes how to use the ST_Y function in MaxCompute and provides reference examples. This function returns the Y-axis coordinate of a point.

```
ST_Y(ST_Point point);
```

point: required. This parameter specifies a geometry of the ST_Point type. This function returns a value of the DOUBLE type. The value indicates the Y-axis coordinate of a point.

```
SELECT ST_Y(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 2.5  |
+------+
```

##### ST_Z

This topic describes how to use the ST_Z function in MaxCompute and provides reference examples. This function returns the Z-axis coordinate of a point.

```
ST_Z(ST_Point point);
```

point: required. This parameter specifies a geometry of the ST_Point type. This function returns a value of the DOUBLE type. This value indicates the Z-axis coordinate of a point.

```
SELECT ST_Z(ST_Point(1.5, 2.5, 3.0)); -- Result +------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### ST_MaxX

This topic describes how to use the ST_MaxX function in MaxCompute and provides reference examples. This function returns the maximum X-axis coordinate of a geometry.

```
ST_MaxX(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. The function returns the maximum X-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MaxX(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 1.5  |
+------+ SELECT ST_MaxX(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### ST_MaxY

This topic describes how to use the ST_MaxY function in MaxCompute and provides reference examples. This function returns the maximum Y-axis coordinate of a geometry.

```
ST_MaxY(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. The function returns the maximum Y-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MaxY(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 2.5  |
+------+ SELECT ST_MaxY(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +------+
| _c0  |
+------+
| 2.5  |
+------+
```

##### ST_MaxZ

This topic describes how to use the ST_MaxZ function in MaxCompute and provides reference examples. This function returns the maximum Z-axis coordinate of a geometry.

```
ST_MaxZ(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. The function returns the maximum Z-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MaxZ(ST_PointZ(1.5, 2.5, 2)); -- Return result +------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT ST_MaxZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)')); -- Return result +------+
| _c0  |
+------+
| 2.0  |
+------+
```

##### ST_MinX

This topic describes how to use the ST_MinX function in MaxCompute and provides reference examples. This function returns the minimum X-axis coordinate of a geometry.

```
ST_MinX(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. The function returns the minimum X-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MinX(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 1.5  |
+------+ SELECT ST_MinX(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +------+
| _c0  |
+------+
| 1.5  |
+------+
```

##### ST_MinY

This topic describes how to use the ST_MinY function in MaxCompute and provides reference examples. This function returns the minimum Y-axis coordinate of a geometry.

```
ST_MinY(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. This function returns the minimum Y-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MinY(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 2.5  |
+------+ SELECT ST_MinY(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +------+
| _c0  |
+------+
| 2.2  |
+------+
```

##### ST_MinZ

This topic describes how to use the ST_MinZ function in MaxCompute and provides reference examples. This function returns the minimum Z-axis coordinate of a geometry.

```
ST_MinZ(ST_Geometry geometry);
```

geometry: required. This parameter specifies a geometry. The return value is of the DOUBLE type. The function returns the minimum Z-axis coordinate among all coordinate points of a geometry.

```
SELECT ST_MinZ(ST_PointZ(1.5, 2.5, 2)); -- Result +------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT ST_MinZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)')); -- Result +------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### ST_NumGeometries

This topic describes how to use the ST_NumGeometries function in MaxCompute and provides reference examples. This function returns the number of geometries in a geometry collection.

```
ST_NumGeometries(ST_GeometryCollection);
```

ST_GeometryCollection: required. This parameter specifies a geometry collection. The return value is of the BIGINT type. This function returns the number of geometries in a geometry collection.

```
SELECT ST_NumGeometries(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 1 0))')); -- Result +------+
| _c0  |
+------+
| 4    |
+------+ SELECT ST_NumGeometries(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8)) ')); -- Result +------+
| _c0  |
+------+
| 2    |
+------+
```

##### ST_NumInteriorRing

This topic describes how to use the ST_NumInteriorRing function in MaxCompute and provides reference examples. This function returns the number of interior rings of a polygon.

```
ST_NumInteriorRing(ST_Polygon);
```

ST_Polygon: required. This parameter specifies a geometry of the ST_Polygon type. The function returns a value of the BIGINT type. This value indicates the number of interior rings of a polygon.

```
-- A polygon without interior rings SELECT ST_NumInteriorRing(ST_Polygon(1, 1, 1, 4, 4, 1)); -- Result +------+
| _c0  |
+------+
| 0    |
+------+ -- A polygon with one interior ring SELECT ST_NumInteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))')); -- Result +------+
| _c0  |
+------+
| 1    |
+------+
```

##### ST_NumPoints

This topic describes how to use the ST_NumPoints function in MaxCompute and provides reference examples. This function returns the number of points in a geometry.

```
BIGINT ST_NumPoints(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input geometry. This function returns a value of the BIGINT type. This value indicates the number of points in a geometry.

```
SELECT ST_NumPoints(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 1    |
+------+ SELECT ST_NumPoints(ST_LineString(1.5, 2.5, 3.0, 2.2)); -- Result +------+
| _c0  |
+------+
| 2    |
+------+ SELECT ST_NumPoints(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))')); -- Result +------+
| _c0  |
+------+
| 4    |
+------+
```

##### ST_PointN

This topic describes how to use the ST_PointN function in MaxCompute and provides reference examples. This function returns the nth vertex of one or more linestrings.

```
GEOMETRY ST_PointN(GEOMETRY geometry, BIGINT n);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input linestring geometry. n: required. This parameter must be of the BIGINT type. It specifies the sequence number of the vertex to be returned. This function returns a value of the GEOMETRY type. The value indicates the nth vertex of a linestring. If n is out of range, this function returns NULL.

```
SELECT ST_PointN(ST_LineString(1.5, 2.5, 3.0, 2.2), 2);
```

##### ST_StartPoint

This topic describes how to use the ST_StartPoint function in MaxCompute and provides reference examples. The function returns the first point of a linestring.

```
GEOMETRY ST_StartPoint(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input linestring geometry. The function returns a value of the GEOMETRY type. The value indicates the first point of a linestring.

```
SELECT ST_StartPoint(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

##### ST_EndPoint

This topic describes how to use the ST_EndPoint function in MaxCompute and provides reference examples. This function returns the last point of a linestring.

```
GEOMETRY ST_EndPoint(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input linestring geometry. The return value is of the GEOMETRY type and indicates the last point of a linestring.

```
SELECT ST_EndPoint(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

##### ST_SRID

This topic describes how to use the ST_SRID function in MaxCompute and provides reference examples.

**s**

**uc**

**os**

This function returns the Spatial Reference Identifier (SRID) of a geometry.

```
BIGINT ST_SRID(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input geometry. This function returns a value of the BIGINT type. The value indicates the SRID of a geometry.

```
SELECT ST_SRID(ST_Point(1.5, 2.5)); -- Result +------+
| _c0  |
+------+
| 0    |
+------+
```

#### Operations

##### ST_Aggr_ConvexHull

This topic describes how to use the ST_Aggr_ConvexHull function in MaxCompute and provides reference examples. This function returns the convex hull geometry after aggregating all geometries.

```
GEOMETRY ST_Aggr_ConvexHull(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies the column of geometries to be aggregated. This function returns a value of the GEOMETRY type. The value indicates the convex hull geometry after aggregating all input geometries.

```
SELECT ST_Aggr_ConvexHull(ST_Point(1.5, 2.5));
```

##### ST_Aggr_Intersection

This topic describes how to use the ST_Aggr_Intersection function in MaxCompute and provides reference examples. This function returns a geometry formed by the intersection of all specified geometries.

```
GEOMETRY ST_Aggr_Intersection(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies the column of geometries to be aggregated. This function returns a value of the GEOMETRY type. It indicates the geometry formed by the intersection of all input geometries.

```
SELECT ST_Aggr_Intersection(ST_Point(1.5, 2.5));
```

##### ST_Aggr_Union

This topic describes how to use the ST_Aggr_Union function in MaxCompute and provides reference examples. This function returns a geometry formed by the union of all specified geometries.

```
GEOMETRY ST_Aggr_Union(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies the column of geometries to be aggregated. This function returns a value of the GEOMETRY type. The value indicates a geometry formed by the union of all input geometries.

```
SELECT ST_Aggr_Union(ST_Point(1.5, 2.5));
```

##### ST_Bin

This topic describes the Operation function ST_Bin. Function declaration:

```
ST_Bin(placeholder)
```

Description: This function returns the bin ID of the input point.

##### ST_BinEnvelope

This topic describes the Operation function ST_BinEnvelop. Function declaration:

```
ST_BinEnvelope(binsize, point)
```

Description: This function returns the binary envelope for the input point. Function declaration:

```
ST_BinEnvelope(binsize, binid)
```

Description: This function returns the binary envelope for the input bin ID.

##### ST_Boundary

This topic describes how to use the ST_Boundary function in MaxCompute and provides reference examples. This function returns the boundary of an input geometry.

```
GEOMETRY ST_Boundary(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input geometry. This function returns a value of the GEOMETRY type. The value indicates the boundary of an input geometry.

```
SELECT ST_Boundary(ST_LineString(0, 1, 1, 0)); SELECT ST_Boundary(ST_Polygon(1, 1, 4, 1, 1, 4));
```

##### ST_Buffer

This topic describes how to use the ST_Buffer function in MaxCompute and provides reference examples. This function takes a geometry and a distance, and returns a geometry consisting of all points whose distance from the input geometry is less than or equal to the specified distance.

```
GEOMETRY ST_Buffer(GEOMETRY geometry, DOUBLE distance);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input geometry. distance: required. This parameter must be of the DOUBLE type. It specifies a buffer distance. This function returns a value of the GEOMETRY type. The value indicates a geometry consisting of all points whose distance from the input geometry is less than or equal to the specified distance.

```
SELECT ST_Buffer(ST_Point(1.5, 2.5), 1.0);
```

##### ST_ConvexHull

This topic describes how to use the ST_ConvexHull function in MaxCompute and provides reference examples. This function returns the convex hull of geometries.

```
GEOMETRY ST_ConvexHull(GEOMETRY geometry1, GEOMETRY geometry2, ...);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the GEOMETRY type. It indicates the convex hull of all input geometries.

```
SELECT ST_AsText(ST_ConvexHull(ST_Point(0, 0), ST_Point(0, 1), ST_Point(1, 1))); -- Return result +---------------------------------------+
| _c0                                   |
+---------------------------------------+
| MULTIPOLYGON (((0 0, 1 1, 0 1, 0 0))) |
+---------------------------------------+
```

##### ST_Difference

This topic describes how to use the ST_Difference function in MaxCompute and provides reference examples. This function returns the first geometry minus its intersection with the second geometry.

```
GEOMETRY ST_Difference(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the GEOMETRY type. The value indicates the first geometry minus its intersection with the second geometry.

```
SELECT ST_AsText(ST_Difference(ST_MultiPoint(1, 1, 1.5, 1.5, 2, 2), ST_Point(1.5, 1.5 ))); -- Return result +--------------------------+
| _c0                      |
+--------------------------+
| MULTIPOINT((1 1), (2 2)) |
+--------------------------+ SELECT ST_AsText(ST_Difference(ST_Polygon(0, 0, 0, 10, 10, 10, 10, 0), ST_Polygon(0, 0, 0, 5, 5, 5, 5, 0))); -- Return result +---------------------------------------------------+
| _c0                                               |
+---------------------------------------------------+
| POLYGON ((5 0, 10 0, 10 10, 0 10, 0 5, 5 5, 5 0)) |
+---------------------------------------------------+
```

##### ST_Envelope

This topic describes how to use the ST_Envelope function in MaxCompute and provides reference examples. This function returns the envelope of a geometry. If the geometry is a point or a vertical or horizontal line, this function may return a degenerate envelope or an empty envelope.

```
GEOMETRY ST_Envelope(GEOMETRY geometry);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input geometry. This function returns a value of the GEOMETRY type. The value indicates the envelope (minimum bounding rectangle) of an input geometry.

```
SELECT ST_Envelope(ST_LineString(0, 0, 2, 2)); SELECT ST_Envelope(ST_Polygon(2, 0, 2, 3, 3, 0));
```

##### ST_ExteriorRing

This topic describes how to use the ST_ExteriorRing function in MaxCompute and provides reference examples. This function returns the exterior ring of a polygon as a linestring.

```
GEOMETRY ST_ExteriorRing(GEOMETRY polygon);
```

polygon: required. This parameter must be of the GEOMETRY type. It specifies an input polygon geometry. This function returns a value of the GEOMETRY type (LINESTRING). The value indicates the exterior ring of a polygon.

```
SELECT ST_ExteriorRing(ST_Polygon(1, 1, 1, 4, 4, 1)); SELECT ST_ExteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1 ))'));
```

##### ST_InteriorRingN

This topic describes how to use the ST_InteriorRingN function in MaxCompute and provides reference examples. This function returns the nth interior ring of a polygon as a linestring.

```
GEOMETRY ST_InteriorRingN(GEOMETRY polygon, BIGINT n);
```

polygon: required. This parameter must be of the GEOMETRY type. It specifies an input polygon geometry. n: required. This parameter must be of the BIGINT type. It specifies the index of the interior ring to be returned. This function returns a value of the GEOMETRY type (LINESTRING). The value indicates the nth interior ring of a polygon.

```
SELECT ST_InteriorRingN(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))'), 1);
```

##### ST_Intersection

This topic describes how to use the ST_Intersection function in MaxCompute and provides reference examples. This function returns the intersection of two geometries. If the dimension of the intersection is lower than the dimension of the input geometries, the ST_Intersection function may drop the lower-dimensional intersection geometry or return it as a closed linestring.

```
GEOMETRY ST_Intersection(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the GEOMETRY type. The value indicates the intersection of the two geometries. The dimension of the intersection may be lower than the dimension of the input geometries.

```
SELECT ST_AsText(ST_Intersection(ST_Point(1, 1), ST_Point(1, 1))); -- Result +--------------+
| _c0          |
+--------------+
| POINT(1 1)   |
+--------------+ SELECT ST_AsText(ST_Intersection(ST_GeomFromText('linestring(0 2, 0 0, 2 0)'), ST_Geo mFromText('linestring(0 3, 0 1, 1 0, 3 0)'))); -- Result +--------------------------------------------------+
| _c0                                              |
+--------------------------------------------------+
| MULTILINESTRING((1 0, 2 0), (0 2, 0 1))          |
+--------------------------------------------------+ SELECT ST_AsText(ST_Intersection(ST_LineString(0, 2, 2, 3), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4))); -- Result +-------------------------------+
| _c0                           |
+-------------------------------+
| LINESTRING((1 2.5, 2 3))      |
+-------------------------------+ SELECT ST_AsText(ST_Intersection(ST_Polygon(2, 0, 2, 3, 3, 0), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4))); -- Result +--------------------------------------------------------+
| _c0                                                    |
+--------------------------------------------------------+
| POLYGON ((2 1, 2.6666666666666665 1, 2 3, 2 1))        |
+--------------------------------------------------------+ SELECT ST_AsText(ST_Intersection(ST_Polygon(2, 0, 3, 1, 2, 1), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4))); -- Result +-----------------------+
| _c0                   |
+-----------------------+
| LINESTRING (2 1, 3 1) |
+-----------------------+
```

##### ST_SymmetricDiff

This topic describes how to use the ST_SymmetricDiff function in MaxCompute and provides reference examples. This function returns a geometry that consists of the non-intersecting portions of two geometries.

```
GEOMETRY ST_SymmetricDiff(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the GEOMETRY type. The value indicates a geometry that consists of the non-intersecting portions of two geometries.

```
SELECT ST_AsText(ST_SymmetricDiff(ST_LineString('linestring(0 2, 2 2)'), ST_LineString('linestring(1 2, 3 2)'))); -- Result +------------------------------------------+
| _c0                                      |
+------------------------------------------+
| MULTILINESTRING ((0 2, 1 2), (2 2, 3 2)) |
+------------------------------------------+ SELECT ST_AsText(ST_SymmetricDiff(ST_Polygon('polygon((0 0, 2 0, 2 2, 0 2, 0 0))'), S T_Polygon('polygon((1 1, 3 1, 3 3, 1 3, 1 1))'))); -- Result +-------------------------------------------------------------------------------------- ------+
| _c0
```

|

```
+-------------------------------------------------------------------------------------- ------+
| MULTIPOLYGON (((0 0, 2 0, 2 1, 1 1, 1 2, 0 2, 0 0)), ((2 1, 3 1, 3 3, 1 3, 1 2, 2 2
, 2 1))) | +-------------------------------------------------------------------------------------- ------+
```

##### ST_Union

This topic describes how to use the ST_Union function in MaxCompute and provides reference examples. This function returns a geometry that represents the union of two or more geometries.

```
GEOMETRY ST_Union(GEOMETRY geometry1, GEOMETRY geometry2, ...);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the GEOMETRY type. The value indicates the union of all input geometries.

```
SELECT ST_AsText(ST_Union(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Polygon(4, 1, 4, 4, 4, 8, 8, 1))); -- Output +------------------------------------------------------+
| _c0                                                  |
+------------------------------------------------------+
| MULTIPOLYGON (((1 1, 4 1, 8 1, 4 8, 4 4, 1 4, 1 1))) |
+------------------------------------------------------+
```

#### Relationship tests

##### ST_Contains

This topic describes how to use the ST_Contains function in MaxCompute and provides reference examples. If a geometry geometry1 contains another geometry geometry2, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Contains(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies a container geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies a geometry to be checked for containment. The return value is of the BOOLEAN type. If geometry1 contains geometry2, the function returns true. Otherwise, it returns false.

```
SELECT ST_Contains(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Point(2, 3)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Contains(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Point(8, 8)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Crosses

This topic describes how to use the ST_Crosses function in MaxCompute and provides reference examples. This function determines whether two geometries intersect, excluding tangent or containment relationships. The function returns true if the two geometries have a crossing point, and returns false otherwise. This function is applicable to the relationship evaluation between lines and lines, lines and polygons, and polygons and polygons.

```
BOOLEAN ST_Crosses(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. The function returns a value of the BOOLEAN type. If the two geometries have a crossing point, excluding tangent or containment relationships, the function returns true. Otherwise, the function returns false.

```
SELECT ST_Crosses(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Crosses(ST_LineString(2, 0, 2, 3), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Crosses(ST_LineString(0, 2, 0, 1), ST_LineString(2, 0, 1, 0)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Disjoint

This topic describes how to use the ST_Disjoint function in MaxCompute and provides reference examples. This function determines whether two geometries are completely disjoint. If the two geometries share no intersecting points, lines, or surfaces, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Disjoint(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. The function returns a value of the BOOLEAN type. If the two geometries are completely disjoint and have no intersection, the function returns true. Otherwise, it returns false.

```
SELECT ST_Disjoint(ST_LineString(0, 0, 0, 1), ST_LineString(1, 1, 1, 0)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Disjoint(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_EnvIntersects

This topic describes how to use the ST_EnvIntersects function in MaxCompute and provides reference examples. This function determines whether the bounding rectangles of two geometries intersect. If the bounding rectangles intersect, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_EnvIntersects(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the BOOLEAN type. If the bounding rectangles of the two geometries intersect, the function returns true. Otherwise, it returns false.

```
SELECT ST_EnvIntersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 3, 2, 2)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ SELECT ST_EnvIntersects(ST_LineString(0, 0, 2, 2), ST_LineString(1, 0, 3, 2)); -- Result +------+
| _c0  |
+------+
| true |
+------+
```

##### ST_Equals

This topic describes how to use the ST_Equals function in MaxCompute and provides reference examples. The function determines whether two geometries are identical. If geometry1 and geometry2 are spatially identical, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Equals(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. The return value is of the BOOLEAN type. If the two geometries are spatially identical, the function returns true. Otherwise, it returns false.

```
SELECT ST_Equals(ST_LineString(0, 0, 1, 1), ST_LineString(1, 1, 0, 0)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Equals(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Intersects

This topic describes how to use the ST_Intersects function in MaxCompute and provides reference examples. This function determines whether two geometries share a common intersection. If geometry1 and geometry2 share a common intersection, the function returns true. Otherwise, the function returns false.

```
BOOLEAN ST_Intersects(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. The function returns a value of the BOOLEAN type. If the two geometries share a common intersection, the function returns true. Otherwise, the function returns false.

```
SELECT ST_Intersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 1, 0, 0)); -- Return result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1)); -- Return result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(2, 0, 2, 3), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4)); -- Return result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(8, 7, 7, 8), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4)); -- Return result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Overlaps

This topic describes how to use the ST_Overlaps function in MaxCompute and provides reference examples. This function determines whether two geometries overlap (excluding tangency). This function returns true if geometry1 and geometry2 overlap, and returns false otherwise.

```
BOOLEAN ST_Overlaps(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. This function returns a value of the BOOLEAN type. It returns true if the two geometries overlap (excluding tangency), and returns false otherwise.

```
SELECT ST_Overlaps(ST_Polygon(2, 0, 2, 3, 3, 0), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Overlaps(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Relate

This topic describes how to use the ST_Relate function in MaxCompute and provides reference examples. This function determines whether two geometries have a DE-9IM topological relationship. If geometry1 and geometry2 match the specified DE-9IM topological pattern, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Relate(GEOMETRY geometry1, GEOMETRY geometry2, STRING pattern);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. pattern: required. This parameter must be of the STRING type. It specifies a DE-9IM topological pattern string. The string is 9 characters in length and represents a pattern matrix consisting of T, F, and *. The function returns a value of the BOOLEAN type. If the two geometries match the specified DE-9IM topological pattern, the function returns true. Otherwise, it returns false.

```
SELECT ST_Relate(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), '*
***T****');
-- Return result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Relate(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), 'T
********');
-- Return result +-------+
| _c0   |
+-------+
| false |
+-------+ SELECT ST_Relate(ST_LineString(0, 0, 3, 3), ST_LineString(1, 1, 4, 4), 'T********'); -- Return result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Relate(ST_LineString(0, 0, 3, 3), ST_LineString(1, 1, 4, 4), '****T****'); -- Return result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Touches

This topic describes how to use the ST_Touches function in MaxCompute and provides reference examples. This function determines whether two geometries touch only at their boundaries. If geometry1 and geometry2 intersect at least at one point and their interiors do not intersect, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Touches(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies the first input geometry. geometry2: required. This parameter must be of the GEOMETRY type. It specifies the second input geometry. The function returns a value of the BOOLEAN type. If the two geometries touch only at their boundaries (they share at least one point and their interiors do not intersect), the function returns true. Otherwise, it returns false.

```
SELECT ST_Touches(ST_Point(1, 2), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Touches(ST_Point(8, 8), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Within

This topic describes how to use the ST_Within function in MaxCompute and provides reference examples. The function determines whether one geometry contains another. If geometry2 contains geometry1, the function returns true. Otherwise, it returns false.

```
BOOLEAN ST_Within(GEOMETRY geometry1, GEOMETRY geometry2);
```

geometry1: required. This parameter must be of the GEOMETRY type. It specifies a geometry to be checked for containment. geometry2: required. This parameter must be of the GEOMETRY type. It specifies a container geometry. The function returns a value of the BOOLEAN type. If geometry2 contains geometry1, the function returns true. Otherwise, it returns false.

```
SELECT ST_Within(ST_Point(2, 3), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Within(ST_Point(8, 8), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1)); -- Result +-------+
| _c0   |
+-------+
| false |
+-------+
```

#### Geohash index functions

##### ST_GeoHash

This topic describes how to use the ST_GeoHash function in MaxCompute and provides reference examples. This function calculates the GeoHash value of an input point geometry and returns the result as a string. The function accepts longitude and latitude values or geometries returned by ST_ functions. If the precision is not specified, the maximum precision is used by default. The precision value depends on your application requirements and the characteristics of your spatial data.

```
STRING ST_GeoHash(GEOMETRY geometry, INT precision); STRING ST_GeoHash(DOUBLE longitude, DOUBLE latitude, INT precision);
```

geometry: required. This parameter must be of the GEOMETRY type. It specifies an input point geometry. longitude: required. This parameter must be of the DOUBLE type. It specifies a longitude value. latitude: required. This parameter must be of the DOUBLE type. It specifies a latitude value. precision: optional. This parameter must be of the INT type. It specifies the precision of GeoHash encoding. The default value is the maximum precision. This function returns a value of the STRING type. The value indicates the GeoHash encoding of an input point geometry.

```
SELECT ST_GeoHash(ST_Point(-102.849854, 36.451113), 8); -- Return result +----------+
| _c0      |
+----------+
| 9wqz7eep |
+----------+ SELECT ST_GeoHash(ST_GeomFromText('POINT(-102.849854 36.451113)')); -- Return result +--------------+
| _c0          |
+--------------+
| 9wqz7eep0eyq |
+--------------+ SELECT ST_GeoHash(-102.849854, 36.451113, 10); -- Return result +------------+
| _c0        |
+------------+
| 9wqz7eep0e |
+------------+
```

##### ST_PointFromGeoHash

This topic describes how to use the ST_PointFromGeoHash function in MaxCompute and provides reference examples. This function returns a point geometry based on an input GeoHash value. If the precision is not specified, the function uses the maximum precision by default. The precision value depends on your application requirements and the characteristics of your spatial data.

```
GEOMETRY ST_PointFromGeoHash(STRING geohash, INT precision);
```

geohash: required. This parameter must be of the STRING type. It specifies an input GeoHash encoded value. precision: optional. This parameter must be of the INT type. It specifies the precision of GeoHash encoding. The default value is the maximum precision. This function returns a value of the GEOMETRY type (POINT). The value indicates the point geometry that corresponds to the GeoHash encoded value.

```
SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq')); -- Result +------------------------------------------------+
| _c0                                            |
+------------------------------------------------+
| POINT (-102.84985402598977 36.451112972572446) |
+------------------------------------------------+ SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq', 4)); -- Result +------------------------------------+
| _c0                                |
+------------------------------------+
| POINT (-102.83203125 36.474609375) |
+------------------------------------+
```

##### ST_EnvelopeFromGeoHash

This topic describes how to use the ST_EnvelopeFromGeoHash function in MaxCompute and provides reference examples. This function returns a bounding rectangle of a specified precision based on an input GeoHash value. If the precision is not specified, the maximum precision is used by default. The precision value depends on your application requirements and the characteristics of your spatial data.

```
GEOMETRY ST_EnvelopeFromGeoHash(STRING geohash, INT precision);
```

geohash: required. This parameter must be of the STRING type. It specifies an input GeoHash encoded value. precision: optional. This parameter must be of the INT type. It specifies the precision of GeoHash encoding. The default value is the maximum precision. This function returns a value of the GEOMETRY type (POLYGON). The value indicates the bounding rectangle of the specified precision corresponding to the GeoHash encoded value.

```
SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq', 8)); -- Result +------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| POLYGON ((-102.84988403320312 36.45109176635742, -102.84954071044922
36.45109176635742, -102.84954071044922 36.451263427734375, -102.84988403320312 36.451 263427734375, -102.84988403320312 36.45109176635742)) | +------------------------------------------------------------+ SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq')); -- Result +------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| POLYGON ((-102.84985419362783 36.451112888753414, -102.84985385835171
36.451112888753414, -102.84985385835171 36.45111305639148, -102.84985419362783 36.451 11305639148, -102.84985419362783 36.451112888753414)) | +------------------------------------------------------------+
```

##### ST_GeoHashNeighbours

This topic describes how to use the ST_GeoHashNeighbours function in MaxCompute and provides reference examples. This function is a User-Defined Table-Generating Function (UDTF) that generates nine rows of data. Based on the input longitude, latitude, and precision, this function returns nine GeoHash string values that represent the current point and its surrounding neighbors. The precision parameter must be specified.

```
list_of_string ST_GeoHashNeighbours(DOUBLE longitude, DOUBLE latitude, INT precision)
```

; longitude: required. This parameter must be of the DOUBLE type. It specifies a longitude value. latitude: required. This parameter must be of the DOUBLE type. It specifies a latitude value. precision: required. This parameter must be of the INT type. It specifies the precision of GeoHash encoding. The function returns nine GeoHash string values, which represent the GeoHash encodings of the current point and its eight surrounding neighbors. This function is a UDTF that generates nine rows of data.

```
SELECT ST_GeoHashNeighbours(-102.849854, 36.451113, 10) AS geohash; -- Result +------------+
| geohash    |
+------------+
| 9wqz7eep0e |
| 9wqz7eep0s |
| 9wqz7eep0u |
| 9wqz7eep0g |
| 9wqz7eep0f |
| 9wqz7eep0d |
| 9wqz7eep06 |
| 9wqz7eep07 |
| 9wqz7eep0k |
+------------+
```

#### S2 mesh functions

##### ST_S2CellIdsFromGeom

This topic describes the ST_S2CellIdsFromGeom function and provides an example of using this function. Function declaration:

```
list_of_string ST_S2CellIdsFromGeom(st_geometry geometry, integer level)
```

Description: This function overwrites the input geometry by using S2 cells at the specified level. Then, it returns the IDs of all S2 cells. Example:

```
SELECT ST_S2CellIdsFromGeom(ST_Point(-102.849854, 36.451113), 4); SELECT ST_S2CellIdsFromGeom(ST_LineString('LINESTRING(-71.160281 42.258729,-71.160837 4 2.259113,-71.161144 42.25932)'), 17) as cellid;
```

##### ST_S2CellIdsFromText

This topic describes the ST_S2CellIdsFromText function and provides an example of using this function. Function declaration:

```
list_of_string ST_S2CellIdsFromText(string wkt, integer level)
```

Description: This function overwrites the well-known text (WKT) representation of the input geometry by using S2 cells at the specified level. Then, it returns the IDs of all S2 cells. Example:

```
SELECT ST_S2CellIdsFromText(ST_GeomFromText('POINT(-102.849854 36.451113)'), 4); SELECT ST_S2CellIdsFromText('LINESTRING(-71.160281 42.258729,-71.160837 42.259113,-71.1 61144 42.25932)', 17) as cellid;
```

##### ST_S2CellCenterPoint

This topic describes the ST_S2CellCenterPoint function and provides an example of using this function. Function declaration:

```
st_point ST_S2CellCenterPoint(string cellId)
```

Description: This function calculates the center point of the cell specified by the cellId parameter in the input S2 cell. Example:

```
SELECT ST_S2CellCenterPoint('549015'); SELECT ST_AsText(ST_S2CellCenterPoint('89e37f091'));
```

##### ST_S2CellNeighbours

This topic describes how to use the ST_S2CellNeighbours function in MaxCompute and provides reference examples. The function calculates all neighboring cells of a specified S2 cell at a given level, and returns a list of S2 cell IDs for all neighboring cells.

```
list_of_string ST_S2CellNeighbours(STRING cellId, INT level);
```

cellId: required. This parameter must be of the STRING type. It specifies the ID of an S2 cell. level: required. This parameter must be of the INT type. It specifies the level of the S2 cell. The function returns a list of strings (LIST_OF_STRING). The value includes the S2 cell IDs for all neighboring cells of the given cell at the specified level.

```
SELECT ST_S2CellNeighbours('549015', 10) AS neighbour; -- Return result +-----------+
| neighbour |
+-----------+
| 549011    |
| 54903d    |
| 549017    |
| 54906b    |
| 549013    |
| 54903f    |
| 54906d    |
| 549041    |
+-----------+ SELECT ST_S2CellNeighbours('89e37f091', 16) AS neighbour; -- Return result +-----------+
| neighbour |
+-----------+
| 89e37f095 |
| 89e37f099 |
| 89e37f097 |
| 89e37f08f |
| 89e37f093 |
| 89e37f09b |
| 89e37f08d |
| 89e37f085 |
+-----------+
```

#### Geodesic functions

##### ST_AreaWGS84

This topic describes the ST_AreaWGS84 function and provides an example of using this function. Function declaration:

```
double ST_AreaWGS84(st_geometry geometry)
```

Description: This function returns the approximate geodesic area of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane area in square meters. Example:

```
SELECT ST_AreaWGS84(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 296 7450,743265.625 2967416,743238 2967416))'));
```

##### ST_DistanceWGS84

This topic describes the ST_DistanceWGS84 function and provides an example of using this function. Function declaration:

```
double ST_DistanceWGS84(st_geometry geometry1, st_geometry geometry2)
```

Description: This function returns the approximate geodesic distance of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane distance in meters. Example:

```
SELECT ST_DistanceWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), ST_GeomFromText('LINESTRING(-72.1260 42.45, -72.123 42.1546)'));
```

##### ST_BufferWGS84

This topic describes the ST_BufferWGS84 function and provides an example of using this function. Function declaration:

```
st_geometry ST_BufferWGS84(st_geometry geometry, double radius)
```

Description: This function returns the approximate geodesic buffer of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane buffer and converts the coordinates back to EPSG:4326. Example:

```
SELECT ST_AsText(ST_BufferWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), 10));
```

##### ST_GeodesicDistance

This topic describes the ST_GeodesicDistance function and provides an example of using this function. Function declaration:

```
double ST_GeodesicDistance(double lon1, double lat1, double lon2, double lat2, string m ethod = VINCENTY) double ST_GeodesicDistance(st_geometry geo1, st_geometry geo2, string method = VINCENTY
```

`)` Description: This function calculates the geodesic distance between two points by using the specified method. The supported methods are Vincenty, LawOfCosines, and Haversine. The default value of the method parameter is VINCENTY. The return value is in radians. Example:

```
SELECT ST_GeodesicDistance(ST_GeomFromText('POINT(152.352298 -24.875975)'), ST_GeomFromText('POINT(151.960336 -24.993289)'), 'LawOfCosines');
```

##### ST_Distance_Sphere

This topic describes the ST_Distance_Sphere function and provides an example of using this function. Syntax:

```
double ST_Distance_Sphere(st_point geo1, st_point2 geo2) double ST_Distance_Sphere(double lng1, double lat1, double lng2, double lat2)
```

Description: This function uses the algorithm provided by AMAP to calculate the approximate geodesic distance between two input points. The distance specified in this function is measured in meters. This function uses ST_Point or the specified longitudes and latitudes as input parameters. Example:

```
SELECT ST_Distance_Sphere(
            ST_GeomFromText('POINT(116.292078 39.919622)'),
            ST_GeomFromText('POINT(116.286676 39.919593)'));
```

Returned result:

```
+------------+
| _c0        |
+------------+
| 460.6965312526471 |
+------------+
```

##### ST_Area_Sphere

This topic describes the ST_Area_Sphere function and provides an example of using this function. Syntax:

```
double ST_Area_Sphere(st_geometry geo)
```

Description: This function uses the algorithm provided by AMAP to calculate the geodesic area of the input geometry. Unit: square meters. This function uses only ST_Polygon and ST_MultiPolygon as input parameters.

```
SELECT geospatial.ST_Area_Sphere(geospatial.ST_GeomFromText('POLYGON((116.259097 40.202 114,116.259024 40.20199,116.258768 40.201662,116.258376 40.201341,116.258031 40.201036,116.257675 40.200734,116.257429 40.200656,116.257357 40.200562,116.257392 40. 200051,116.257506 40.199433,116.257569 40.198586,116.257564 40.19756,116.257561 40.1973 72,116.257552 40.197036,116.257554 40.19675,116.257539 40.196647,116.257502 40.19653,116.257343 40.196389,116.257153 40.196276,116.256733 40.196071,116.25582 40.19 5646,116.255628 40.195611,116.255468 40.195653,116.255385 40.195742,116.255347 40.19584 9,116.255258 40.197143,116.255103 40.199576,116.255078 40.200585,116.251227 40.20059,116.251098 40.203978,116.259433 40.204111,116.259247 40.203079,116.259097 40.2 02114))'));
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 353493.765625 |
+------------+
```

#### R-tree index functions

##### ST_BuildRTreeIndex

This topic describes the ST_BuildRTreeIndex function and provides an example of using this function. Function declaration:

```
RTree ST_BuildRTreeIndex(string uniqueId, string geometryWkt)
```

Description: This function is a user-defined aggregate function (UDAF). It uses the unique ID and well-known text (WKT) string of each geometry as input parameters to create the R-tree index. This function must be used with other R-tree functions. Example:

```
SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index FROM poi_sample;
```

##### ST_ContainsFromRTree

This topic describes the ST_ContainsFromRTree function. Function declaration:

```
ST_ContainsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that are contained by the geometry from the R-tree index. This function is used to accelerate the ST_Contains query.

##### ST_CrossesFromRTree

This topic describes the ST_CrossesFromRTree function. Function declaration:

```
ST_CrossesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that cross the geometry from the R-tree index. This function is used to accelerate the ST_Crosses query.

##### ST_EqualsFromRTree

This topic describes the ST_EqualsFromRTree function. Function declaration:

```
ST_EqualsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that equal the geometry from the R-tree index. This function is used to accelerate the ST_Equals query.

##### ST_IntersectsFromRTree

This topic describes the ST_IntersectsFromRTree function. Function declaration:

```
ST_IntersectsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that intersect with the geometry from the R-tree index. This function is used to accelerate the ST_Intersects query.

##### ST_OverlapsFromRTree

This topic describes the ST_OverlapsFromRTree function. Function declaration:

```
ST_OverlapsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that overlap with the geometry from the R-tree index. This function is used to accelerate the ST_Overlaps query.

##### ST_TouchesFromRTree

This topic describes the ST_TouchesFromRTree function. Function declaration:

```
ST_TouchesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that spatially touch the geometry from the R-tree index. This function is used to accelerate the ST_Touches query.

##### ST_WithinFromRTree

This topic describes the ST_WithinFromRTree function and provides an example of using this function. Function declaration:

```
ST_WithinFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that include the geometry from the R-tree index. This function is used to accelerate the ST_Within query. Example: Query the intersections of line segments in the A table and polygons in the B table.

```
set odps.sql.allow.cartesian=true; SELECT a.id as link_id, b.id as shape_id FROM link_sample_wkt a, poi_sample_wkt b WHERE geospatial.ST_IsValid(b.shape) AND geospatial.ST_Intersects(
        geospatial.ST_LineString(a.line),
        geospatial.ST_Multipolygon(b.shape));
```

Returned result:

```
Summary: resource cost: cpu 3.28 Core * Min, memory 5.76 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
  meta_dev.link_sample_wkt: 1000 (105940 bytes)
outputs: Job run time: 111.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

After optimization by using the new function:

```
SELECT /*+mapjoin(i)*/
      geospatial.ST_IntersectsFromRTree(id, line, i.index)
      AS (link_id, shape_id)
FROM link_sample_wkt JOIN
```

`(`

```
      SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index
      FROM poi_sample_wkt
      WHERE geospatial.ST_IsValid(shape)
) i;
```

Returned result:

```
Summary: resource cost: cpu 1.03 Core * Min, memory 1.99 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
  meta_dev.link_sample_wkt: 1000 (105940 bytes)
outputs: Job run time: 41.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

##### ST_KNNFromRTree

This topic describes the ST_KNNFromRTree function and provides an example of using this function. Function declaration:

```
ST_KNNFromRTree(string uniqueId, string geometryWkt, int k, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of k objects that are near to the geometry from the R-tree index. Example: Create an R-tree for all points in a table and use the KNN function to find the nearest point of each point.

```
SELECT /*+mapjoin(i)*/
    geospatial.ST_KNNFromRTree(id, point, 1, i.index) AS (id1, id2)
FROM poi_sample_wkt JOIN
```

`(`

```
    SELECT geospatial.ST_BuildRTreeIndex(id, point) AS index
    FROM poi_sample_wkt
) i;
```

Returned result:

```
Summary: resource cost: cpu 1.17 Core * Min, memory 2.24 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
outputs: Job run time: 46.000 +-----+-----+
| id1 | id2 |
+-----+-----+
| B000A01B4E | B000A01B4E |
| B000A01C19 | B000A01C19 |
| B000A023A5 | B000A023A5 |
| B000A02F81 | B000A02F81 |
| B000A07BEE | B000A07BEE |
| B000A07E06 | B000A07E06 |
| B000A08863 | B000A08863 |
... -- The table has 1,000 rows of data. This function returns 1,000 rows of data, which me ets your expectations.
```

#### Other functions

##### ST_IsValid

This topic describes the ST_IsValid function and provides an example of using this function. Function declaration:

```
boolean ST_IsValid(st_geometry geometry) boolean ST_IsValid(string wkt)
```

Description: This function checks whether the input geometry or well-known text (WKT) string meets the requirements. Example:

```
SELECT ST_IsValid('POINT(-102.849854 36.451113)'); SELECT ST_IsValid(ST_Point('POINT(-102.849854 36.451113)'));
```

##### ST_Transform

This topic describes the ST_Transform function and provides an example of using this function. Function declaration:

```
st_geometry ST_TransformWGS84(st_geometry geometry) st_geometry ST_Transform(st_geometry geometry, integer toSRID) st_geometry ST_Transform(st_geometry geometry, integer fromSRID, integer toSRID)
```

Description: This function converts the coordinates of the input geometry from one spatial reference system to another. The ST_TransformWGS84 function converts the coordinates of the geometry from EPSG:4326 to EPSG:3857. The ST_Transform function converts the geometry from fromSRID to toSRID. If the overload function contains only toSRID, you must call the ST_SetSRID function first. Example:

```
SELECT ST_AsText(ST_Transform(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 2967450,743265.625 2967416,743238 2967416))', 2249, 4326))); SELECT ST_AsText(ST_TransformWGS84(ST_GeomFromText('POLYGON((-71.1776848522251 42.39028 96512902,-71.1776843766326 42.3903829478009, -71.1775844305465 42.3903826677917,-71.177 5825927231 42.3902893647987,-71.1776848522251 42.3902896512902))')));
```

### MaxCompute Hash Clustering

#### Feature background

This topic describes the background of MaxCompute Hash Clustering.

**Background information**

**Feature overview**

JOIN operations are commonly used for queries in MaxCompute. MaxCompute provides the following methods to implement JOIN operations:
**Broadcast hash join**: This method is used when a JOIN operation involves a small table.
The small table is broadcasted and transferred to all instances in a join task. Then, the hash join operation is performed to join the small table with a large table.
**Shuffle hash join**: This method is used when a JOIN operation involves large tables that
cannot be directly broadcasted. In this case, the hash shuffle operation is performed on two tables based on join keys. The hash results for the same key-value pairs are the same. This ensures that results that have the same key are collected to the same instance of a join task. For each instance, a hash table is created by using a small table, probe operations are performed by using a large table, and then the tables are joined.
**Sort merge join**: This method is used when a JOIN operation involves larger tables and the
preceding methods cannot be used because the memory is insufficient to create a hash table. In this case, the hash shuffle operation is performed on two tables based on join keys, the obtained values are sorted by using join keys, and then the sorted values are merged. The following figure shows the process.

**Storage features**

The sort merge join method is commonly used in MaxCompute because MaxCompute processes large amounts of data in most cases. If you use this method, shuffle and join operations are repeatedly performed. The physical execution plan of Job Scheduler of a JOIN operation requires multiple stages, which consumes excessive amounts of resources.

**Execution optimization**

To address this issue, MaxCompute allows you to configure the hash shuffle and sort attributes when the data is initially generated in a table. This prevents data from being repeatedly shuffled and sorted in subsequent queries. The number of stages in the physical execution plan of Job Scheduler of a JOIN operation is also reduced. The preceding figure shows that only one stage is required. MaxCompute Hash Clustering allows you to configure the shuffle and sort attributes of a table when you create the table. Then, MaxCompute optimizes the execution plan, improves the efficiency, and saves resources based on the existing storage characteristics.

#### Descriptions

##### Enable Hash Clustering

This topic describes how to enable the Hash Clustering feature of MaxCompute.

**Enable the Hash Clustering feature**

The Hash Clustering feature has been launched. By default, this feature is enabled. If you want to use clustered indexes, add the following flag:

```
SET odps.sql.cfile2.enable.read.write.index.flag=true;
```

**Usage notes**

After the flag is set to true, the system automatically creates indexes for sorted hash buckets to improve query efficiency. To use clustered indexes, you must add this flag during table creation and subsequent queries. If you want to use clustered indexes in your project at all times, contact the MaxCompute team.

**Note**

Clustered indexes improve the efficiency of queries (equivalent values or ranges) based on sort keys. You can experience the superior performance provided by Hash Clustering even if you do not add this flag.

##### Create a hash-clustered table

This topic describes how to create a hash-clustered table.

**Syntax for creating a hash-clustered table**

You can use the following statement to create a hash-clustered table. You must specify cluster keys or hash keys and the number of hash buckets. The sort operation is optional. However, we recommend that you use the same parameter values as the cluster keys to achieve optimal performance.

```
CREATE TABLE [IF NOT EXISTS] table_name [(col_name data_type [comment col_comment], ...)] [comment table_comment] [PARTITIONED BY (col_name data_type [comment col_comment], ...)] [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_nam e [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] [AS select_statement]
```

The following sections describe the CLUSTERED BY, SORTED BY, and INTO number_of_buckets BUCKETS clauses.

**CLUSTERED BY**

The CLUSTERED BY clause specifies hash keys. MaxCompute performs the hash operation on the specified column and distributes data to buckets based on the hash values. To prevent data skew and hot spots, and to concurrently execute statements, we recommend that you specify a column that has large value ranges and a small number of duplicate key-value pairs in CLUSTERED BY. In addition, to optimize the JOIN operation, we recommend that you select commonly used join or aggregation keys. The join and aggregation keys are similar to the primary keys in conventional databases.

**SORTED BY**

The SORTED BY clause specifies how fields are sorted in a bucket. We recommend that you specify the same column in SORTED BY as that in CLUSTERED BY to improve execution efficiency. After you specify the column in SORTED BY, MaxCompute automatically generates indexes and then executes SQL statements faster when you query data based on these indexes.

**INTO number_of_buckets BUCKETS**

The INTO number_of_buckets BUCKETS clause specifies the number of hash buckets, which is required. The number of hash buckets is determined by the volume of data. More buckets indicate higher concurrency, which shortens the job running time. However, if a large number of buckets exist, excessive small files may be generated. In addition, high concurrency increases CPU time. We recommend that you set the data size of each bucket to a value that ranges from 500 MB to 1 GB. If a large table is used, you can adjust the value to a larger value based on your business requirements. You can remove the shuffle operation only for tables with the same number of buckets in MaxCompute. The maximum number of buckets is 4,096. If the number of buckets exceeds the value, the performance and resource usage may be affected. If you want to remove the shuffle and sort operations during a JOIN operation on two tables, the numbers of hash buckets in the tables must be the same. If the numbers that are calculated based on the aforementioned method are inconsistent, we recommend that you use the larger number for the JOIN operation. This ensures that SQL statements can be concurrently executed in an efficient manner. If the size of the large table is much larger than the size of the small table, you can set the number of buckets for the large table to a value that is several times the number of buckets for the small table. For example, you can set the number of buckets for the large table to 1,024 and set the number of buckets for the small table to 256. If automatic hash bucket split and merging are supported, you can perform the JOIN operation based on the data characteristics of MaxCompute. You can use the following statement to create a standard table:

```
CREATE TABLE t1 (a string, b string, c bigint) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS;
```

You can use the following statement to create a partitioned table:

```
CREATE TABLE t2 (a string, b string, c bigint) PARTITIONED BY (dt string) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS;
```

##### Modify table attributes

This topic describes how to modify the attributes of a hash-clustered table.

**Syntax**

For a partitioned table, MaxCompute allows you to execute the ALTER TABLE statement to add the Hash Clustering attribute to a table or remove the Hash Clustering attribute from a table.

```
ALTER TABLE table_name
 [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_na
me [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] ALTER TABLE table_name NOT CLUSTERED;
```

**Usage notes**

When you use the ALTER TABLE statement, take note of the following points: The ALTER TABLE statement can modify only the Hash Clustering attribute of a partitioned table. The Hash Clustering attribute cannot be modified after it is added to a nonpartitioned table. The ALTER TABLE statement takes effect only on the new partitions of a table, which include the partitions generated by using the INSERT OVERWRITE statement. New partitions are stored based on the Hash Clustering attribute. The storage formats of existing partitions remain unchanged. The ALTER TABLE statement takes effect only on the new partitions of a table. Therefore, you cannot specify a partition in this statement. The ALTER TABLE statement is suitable for existing tables. After the Hash Clustering attribute is added, new partitions are stored based on the Hash Clustering attribute.

##### View and verify table attributes

This topic describes how to view and verify attributes of a hash-clustered table.

**View table attributes**

After you create a hash-clustered table, execute the following statement to view table attributes:

```
DESC EXTENDED table_name;
```

The table attributes are displayed in the Extended Info section.

**View partition attributes**

You can execute the following statement to view partition attributes of a partitioned table:

```
DESC EXTENDED table_name PARTITION(pt_spec);
```

The following figure shows the execution result.

#### Benefits

##### Bucket pruning and index optimization

This topic describes bucket pruning and index optimization.

**Optimization description**

The following code provides a syntax sample:

```
CREATE TABLE t1 (id bigint, a string, b string) CLUSTERED BY (id) SORTED BY (id) into 1 000 BUCKETS; ... SELECT t1.id, t1.a, t1.b FROM t1 WHERE t1.id=12345;
```

This syntax indicates a full scan for a standard table. A full scan for a large table consumes a large number of resources. However, if the hash shuffle operation is performed on all **id** fields and the **id** fields are sorted, the query is greatly simplified.
1. Find the hash bucket that corresponds to **12345**. This query is performed in only one
bucket, not all 1,000 buckets. This process is called **bucket pruning**.
2. Data in a bucket is stored based on IDs. MaxCompute automatically creates indexes and
uses the INDEX LOOKUP function to locate relevant records. The simplified procedure not only greatly reduces the number of mappers, but also allows mappers to locate the page where the data is stored by using the INDEX function. Therefore, the volume of loaded data is greatly reduced.

##### Aggregation optimization

This topic describes how the hash clustering feature optimizes aggregation.

**Optimization description**

Consider the following query example.

```
SELECT department, SUM(salary) FROM employee GROUP BY (department);
```

Typically, the system performs shuffle and sort operations on the **department** column and then executes a stream aggregate to calculate statistics for each **department group**. However, if the table data already uses `CLUSTERED BY (department) SORTED BY (department)` , the system can skip these shuffle and sort operations.

##### Storage optimization

This topic describes storage optimization.

**Optimization description**

In addition to computation optimization, storage space is greatly saved if tables are shuffled and stored in a sorted manner. MaxCompute uses column store at the underlying layer. Records that have the same or similar key-value pairs are stored together by the sort function, which facilitates encoding and compression. This way, compression efficiency is improved. In some extreme cases, a sorted table can save 50% more storage space than an unsorted table. Therefore, Hash Clustering is suitable for storing tables that have long lifecycles. The following figure shows a sample table with 100 GB of TPC-H line items and multiple data types, such as INT, DOUBLE, and STRING. If Hash Clustering is used, about 10% of the storage space is saved when the volume of data and compression format remain unchanged.

#### ShuffleRemove

This topic describes the operations that are related to ShuffleRemove. Range-clustered tables support the join and aggregate operations. If a join key or group key is a range-clustered key or its prefix, data redistribution is not required. This mechanism is called ShuffleRemove, which improves execution efficiency.
**Usage**: The `odps.optimizer.enable.range.partial.repartitioning` flag specifies whether
to enable this feature. By default, this feature is disabled. If the two hash-clustered tables you want to join have different numbers of buckets but the numbers are multiples of each other, data redistribution is not required. This improves execution efficiency.
**Usage**: The `odps.optimizer.enable.hash.partial.repartitioning` flag specifies whether to
enable this feature. By default, this feature is enabled. Correlated Shuffle Remove is supported. If data meets distribution requirements but does not meet the sorting requirements, you can add a sort operator to avoid data redistribution.

#### Usage limits

This topic describes limits on MaxCompute Hash Clustering.

**Usage limits**

The Hash clustering feature has the following usage limits: The INSERT INTO statement is not supported. You can insert data only by using the INSERT OVERWRITE statement. Small files cannot be merged. Most data is evenly distributed in buckets when it is split. Therefore, the number of small files is not large. If you merge files, the data distribution is affected. However, you can still use the merge and archive commands to change the storage format of a table file and the format of a RAID file. You cannot use Tunnel to upload data to a range-clustered table because the data uploaded by using Tunnel is unsorted.

### Common MaxCompute SQL

**parameter settings**

#### Map configurations

This topic describes the common SET parameters that are used in MaxCompute to control Map task resources and input blocks. You can properly adjust these parameters to optimize job performance and prevent data skew or resource waste.

**Set the number of CPUs**

This parameter specifies the number of CPUs used by each instance in a Map task. Default value: 100. Valid values: [50, 800].

**SET command**

```
SET odps.sql.mapper.cpu=100;
```

**Set the memory size**

This parameter specifies the memory size of each instance in a Map task. Unit: MB. Default value: 1024. Valid values: [256, 12288].

**SET command**

```
SET odps.sql.mapper.memory=1024;
```

**Set the file merge threshold**

This parameter specifies the maximum size of control files to be merged. Unit: MB. Default value: 64. Valid values: [0, Integer.MAX_VALUE]. You can configure this variable to control the input of mappers.

**SET command**

```
SET odps.sql.mapper.merge.limit.size=64;
```

**Set the Map input size**

This parameter specifies the maximum data input volume for a Map task. Unit: MB. Default value: 256. Valid values: [1, Integer.MAX_VALUE]. You can configure this variable to control the input of mappers.

**SET command**

```
SET odps.sql.mapper.split.size=256;
```

#### Join configurations

This topic describes common SET parameters that are used to configure Join task resources in MaxCompute.

**Set the number of instances**

This parameter specifies the number of instances of a Join task. Default value: -1. Valid values: [0, 2000].

**SET command**

```
SET odps.sql.joiner.instances=-1;
```

**Set the number of CPUs**

This parameter specifies the number of CPUs used by each instance of a Join task. Default value: 100. Valid values: [50, 800].

**SET command**

```
SET odps.sql.joiner.cpu=100;
```

**Set the memory size**

This parameter specifies the memory size of each instance of a Join task. Unit: MB. Default value: 1024. Valid values: [256, 12288].

**SET command**

```
SET odps.sql.joiner.memory=1024;
```

#### Reduce configurations

This topic describes the common SET parameters that are used to configure Reduce task resources in MaxCompute.

**Set the number of instances**

This parameter specifies the number of instances in a Reduce task. Default value: -1. Valid values: [0, 2000].

**SET command**

```
SET odps.sql.reducer.instances=-1;
```

**Set the number of CPUs**

This parameter specifies the number of CPUs used by each instance in a Reduce task. Default value: 100. Valid values: [50, 800].

**SET command**

```
SET odps.sql.reducer.cpu=100;
```

**Set the memory size**

This parameter specifies the memory size of each instance in a Reduce task. Unit: MB. Default value: 1024. Valid values: [256, 12288].

**SET command**

```
SET odps.sql.reducer.memory=1024;
```

#### UDF configurations

This topic describes common SET parameters that are used to control the execution behavior of user-defined functions (UDFs) in MaxCompute.

**Set the number of CPUs**

This parameter specifies the maximum memory size used by the UDF JVM heap. Unit: MB. Default value: 1024. Valid values: [256, 12288].

**SET command**

```
SET odps.sql.udf.jvm.memory=1024;
```

**Set the timeout period**

This parameter specifies the timeout period of a UDF. Unit: seconds. Default value: 600. Valid values: [0, 3600].

**SET command**

```
SET odps.sql.udf.timeout=600;
```

**Set the maximum memory**

This parameter specifies the maximum memory size used by the UDF Python API. Unit: MB. Default value: 256. Valid values: [64, 3072].

**SET command**

```
SET odps.sql.udf.python.memory=256;
```

**Enable result reuse**

When this parameter is set to true, each UDF function expression can be calculated only once. This improves performance. Default value: true.

**SET command**

```
SET odps.sql.udf.optimize.reuse=true/false;
```

**Enable strict mode**

This parameter specifies whether functions return NULL or an error if dirty data is found. If the parameter is set to true, an error is returned. Otherwise, NULL is returned.

**SET command**

```
SET odps.sql.udf.strict.mode=false/true;
```

#### MapJoin configurations

This topic describes MapJoin configurations.

**Set the maximum memory**

This parameter specifies the maximum memory size for a small table that is involved in a MapJoin operation. Unit: MB. Default value: 512.

**SET command**

```
SET odps.sql.mapjoin.memory.max=512;
```

**Configure reshuffle**

Dynamic partitioning is time-consuming in some scenarios. Disabling dynamic partitioning can accelerate SQL. If the number of dynamic partitions is small, disabling dynamic partitioning can prevent data skew.

**SET command**

```
SET odps.sql.reshuffle.dynamicpt=true/false;
```

#### Configurations of data skew

This topic describes configurations of data skew.

**Enable GROUP BY optimization**

This parameter allows you to enable GROUP BY optimization.

**SET command**

```
SET odps.sql.groupby.skewindata=true/false;
```

**Enable JOIN optimization**

This parameter allows you to enable JOIN optimization. This is effective only when
**odps.sql.skewinfo** is specified.

**SET command**

```
SET odps.sql.skewjoin=true/false;
```

**Configure JOIN optimization**

This parameter allows you to configure detailed information for JOIN optimization.

**SET command**

```
SET odps.sql.skewinfo;
```

Command syntax:

```
SET odps.sql.skewinfo=skewed_src:(skewed_key)[("skewed_value")]
```

Configure a single skewed value for a single field.

```
SET odps.sql.skewinfo=src_skewjoin1:(key)[("0")];
```

Configure multiple skewed values for a single field.

```
SET odps.sql.skewinfo=src_skewjoin1:(key)[("0")("1")];
```

### MapReduce-to-SQL

**conversion for execution**

#### Overview

This topic describes the MapReduce-to-SQL execution feature.

**Usage notes**

MaxCompute provides a series of Java APIs for MapReduce to process data. MaxCompute supports the automatic conversion of MapReduce jobs to SQL for execution. After the conversion, MapReduce jobs can use the next-generation compiler, cost-based optimizer, and vectorized execution engine released with MaxCompute V2.0. This allows them to continuously benefit from the ongoing iterations and optimizations of the SQL engine in terms of features, performance, and stability.

**Note**

This feature brings the following benefits: You do not need to change the original APIs and job logic. Only MapReduce jobs of the OpenMR type, which are written by using MapReduce APIs, can be converted to SQL. This feature can be used only for projects and jobs. This feature supports views as the input. This feature supports external tables as the input. This feature supports TemporaryFile reads and writes. This feature allows you to read data from and write data to hash-clustered tables. This feature supports near-real-time execution of small jobs.

#### Configure the MaxCompute client

This topic describes how to configure the MaxCompute client when you use the MapReduceto-SQL conversion feature.
1. Download the latest version of the MaxCompute client package to your on-premises
machine and configure the MaxCompute client.

**Note**

On the download page, you can obtain the MaxCompute client package of the required version in the **Other Resources** section.
2. Configure the execution mode.
You can configure the execution mode based on your business requirements. The default execution mode is lot. In lot mode, jobs are run by MapReduce. The new compiler, optimizer, and execution engine are not used. You can enable the execution mode by setting the **odps.mr.run.mode** parameter. Valid values: **lot**, **sql**, and **hybrid**. Method 1: Enable the execution mode at the project level. In this case, the configuration takes effect on all jobs in the project. Therefore, only the project administrator can apply to enable the execution mode. Set the **odps.mr.run.mode** parameter to **hybrid** or **sql**. If SQL execution fails in **hybrid** mode, the job is run by MapReduce. If SQL execution fails in **sql** mode, an error is reported. Method 2: Enable the execution mode at the session level. This method applies only to the current job. To enable the execution mode, use one of the following methods: Add a set flag, such as set odps.mr.run.mode=hybrid; before JAR statements. Configure job parameters. Example:

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

MaxCompute O&M personnel can enable the execution mode at the project level at a later point in time.

#### Configure running settings in

**DataWorks**

This topic describes how to configure running settings in DataWorks. Jobs that run in DataWorks are updated by the O&M personnel of MaxCompute and DataWorks. You do not need to update your client. Enable the conversion for a single job. You can add a set flag before the statement of a MapReduce job or configure job parameters for the set flag. These methods take effect at the session level and apply only to the current job. The following examples show how to use these methods: Add a set flag, such as set odps.mr.run.mode=hybrid; before JAR statements. Configure job parameters. Example:

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

Enable the conversion at the project level by setting **odps.mr.run.mode** for a project.

#### View details

This topic describes how to view MapReduce-to-SQL conversion results and running details of SQL jobs. You can use Logview and MaxCompute Studio to view MapReduce-to-SQL conversion results and running details of SQL jobs. Logview XML Open Logview and click the LOT node in the center of the page. The SQL jobs that are converted from MapReduce jobs are included in the XML information about the node. Example:

```
create temporary function mr2sql_mapper_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotMapperUDTF' using ; create temporary function mr2sql_reducer_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotReducerUDTF' using ;
 @sub_query_mapper :=
 SELECT
k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku_ ock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_i ge_version,v_currency_code FROM( SELECT mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku ttr,sku_price,sku_stock,sku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discou ,sku_image_version,currency_code ) as (k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku tock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_ age_version,v_currency_code) FROM ae_antispam.product_sku_tt_inc WHERE ds = "20180615" AND hh = "21" UNION ALL SELECT mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku ttr,sku_price,sku_stock,sku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discou ,sku_image_version,currency_code ) as (k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku tock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_ age_version,v_currency_code) FROM ae_antispam.product_sku ) open_mr_alias1
 DISTRIBUTE BY k_id SORT BY k_id ASC;
@sub_query_reducer := SELECT mr2sql_reducer_152955927079392291755(k_id,v_gmt_create,v_gmt_modified,v_product_id,v_ad n_seq,v_sku_attr,v_sku_price,v_sku_stock,v_sku_code,v_sku_image,v_delivery_time,v_sku_b k_order,v_sku_bulk_discount,v_sku_image_version,v_currency_code) as (id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code, u_image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code) FROM @sub_query_mapper; FROM @sub_query_reducer INSERT OVERWRITE TABLE ae_antispam.product_sku SELECT id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code,s _image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code
```

; Logview details or summary A new execution engine is used to run jobs.

```
Job run mode: fuxi job Job run engine: execution engine
```

Logview details or JSON summary The JSON summary information in MapReduce contains only the input and output information about Map and Reduce. However, the JSON summary information in SQL allows you to view details about each stage of SQL execution, such as all execution parameters, logical execution plans, physical execution plans, and execution details. Example:

```json
 "midlots" :
```

`[`

```
 "LogicalTableSink(table=
[[odps_flighting.flt_20180621104445_step1_ad_quality_tech_qp_algo_antifake_wordbag_filt _bag_change_result_lv2_20, auctionid,word,match_word(3) {0, 1, 2}]]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$2], word=[$3], match_word=[$4]) OdpsLogicalTableFunctionScan(invocation=[[MR2SQL_MAPPER_152955294118813063732($0, $1) ]()], rowType=[RecordType(VARCHAR(2147483647) item_id, VARCHAR(2147483647) text, VARC HAR(2147483647) __tf_0_0, VARCHAR(2147483647) __tf_0_1, VARCHAR(2147483647) __tf_0_2)
```

`])`

```
OdpsLogicalTableScan(table= [[ad_quality_tech.qp_algo_antifake_wordbag_filter_bag_change_lv2_20, item_id,text(2) {0, 1}]])
```

`]`

#### Perform operations on the distributed

**file system**

This topic describes how to perform operations on the distributed file system.

**Procedure**

1. Specify volume files.
You can use one of the following methods to specify volume files: Use a utility class to specify the input and output files:

```
com.aliyun.odps.mapred.utils.InputUtils.addVolume( new VolumeInfo([project,]inVolume,inPartition, "inLabel"), new JobConf()); com.aliyun.odps.mapred.utils.OutputUtils.addVolume( new VolumeInfo([project,]outVolume, outPartition, "outLabel"), new JobConf());
```

In the preceding commands, **project** and **label** are optional, and the current project and default label are used by default. If multiple input and output files are used, labels are used to distinguish the files from each other. Authorization is required before you access the volume files of other projects. Configure parameters to specify the volume and partition of the input and output files. If multiple input or output files are used, separate the parameters with commas (,).

```
set odps.sql.volume.input[/output].desc = [<project>.]<table>.<partition>[:<label>]
```

;
2. Call the following method by using a **context** object in the map and reduce steps to write
data to the distributed file system or write data stream input and output files:

```
context.getOutputVolumeFileSystem();
```

### Analysis of the mapping

**between SQL input and output**

**fields**

#### Overview

This topic describes the feature of analyzing the mapping between fields in input and output tables.

**Feature introduction**

This feature analyzes the mapping between the fields in the output table and those in the input table of an SQL statement. Example:

```
SELECT key, SUM(value) AS total FROM src GROUP BY key;
```

The result shown in the following figure is returned. Two columns are returned: **key** and **total**. The **key** column corresponds to the **src.key** column of the input table, and the **total** column corresponds to the **src.value** column of the input table.

#### Usage notes

This topic provides an example on how to use the feature of analyzing the mapping between fields in input and output tables.

**Output format**

Field mapping analysis supports human-readable and JSON formats. You can use the `set` `odps.sql.select.output.format=HumanReadable/json` flag to specify the output format.

**SDK-based field mapping analysis**

Example

```java
Odps odps = initOdps(); // To perform analysis, use LineageTask. LineageTask task = new LineageTask("task_name", "select * from dual;"); // Optional. Use the preceding flag to specify the output format. Map<String, String> settings = new LinkedHashMap<>(); settings.putIfAbsent("odps.sql.select.output.format", "json"); task.setProperty("settings", JSON.toJSONString(settings)); // Submit code to the server for field mapping analysis. Instance instance = odps.instances().create(task); System.out.println(instance.getId()); String logView = odps.logview().generateLogView(instance, 72); System.out.println(logView); instance.waitForSuccess(); // Obtain the analysis result. System.out.println(instance.getTaskResults().get("task_name"));
```

**odpscmd-based field mapping analysis**

CLI mode: Use the **-X** parameter for field mapping analysis.

```
./bin/odpscmd.bat -X D:\lineage.q
```

Interactive mode: After you enter the interactive mode of odpscmd, you can use the preceding flag to specify the output format. The usage method is similar to that used to submit SQL jobs.

```
lineage_test>set odps.sql.task.mode=LINEAGE; -- OK is returned. Continue to run the following command: odps@ lineage_test>set odps.sql.select.output.format=Humanreadable; -- OK is returned. Continue to run the following command: lineage_test>select * from dual;
```

Returned result:

```
== Column Lineage Column : id Source Columns :
  test2.dual.id
```

### Common MaxCompute SQL

**errors and solutions**

#### Data skew

##### Overview

This topic provides an overview of data skew issues.

**Usage notes**

In most cases, data skew occurs if the min, max, and avg values of the instance time, input records, and output records parameters are unbalanced in an instance on which jobs run. For example, if the max value is significantly larger than the avg value, data skew may occur. You can use Logview to identify data skew issues, as shown in the following figure. The **Long Tails** tab of each task displays the instances on which data skew occurs. The root cause of data skew is that the amount of data processed by a specific instance far exceeds that processed by other instances. As a result, the running time of this instance is also much longer than the average running time of other instances, and the entire job slows down. Different types of data skew issues in SQL are resolved by using different methods. The subsequent topics describe possible causes of data skew issues and provide solutions.

##### GROUP BY data skew

This topic describes possible causes of the GROUP BY data skew and provides a solution.

**Problem analysis and solutions**

**Possible cause**: GROUP BY keys are unevenly distributed, which results in data skew on
reducers.
**Solution**: Set the anti-skew parameter before you execute SQL statements.

```
SET odps.sql.groupby.skewindata=true;
```

**Note**

If you set this parameter to true, when the Shuffle hash algorithm is used, the system automatically adds a random factor and introduces a new task to prevent data skew.

##### DISTRIBUTE BY data skew

This topic describes possible causes of the DISTRIBUTE BY data skew and provides a solution.

**Problem analysis and solutions**

**Possible cause**: Constants are used to execute the DISTRIBUTE BY clause for full sorting of
the entire table. This results in data skew on reducers.
**Solution**:
The DISTRIBUTE BY clause determines how to distribute the output values of the map stages to reducers. To prevent duplicate output values from being distributed to different reducers or to process the same group of data together, use the DISTRIBUTE BY clause. This ensures that the same group of data is distributed to the same reducer. Specify the alias of an output column of a SELECT statement. If you execute a SELECT statement to query data of a column and the alias of this column is not specified, the column name is used as the alias. Examples:

```
-- Query the region column from the sale_detail table and distribute data by hash on the region values. SELECT region FROM sale_detail DISTRIBUTE BY region;
```

To prevent data skew and hot spots, you must specify a column that has large value ranges in the DISTRIBUTE BY clause.

##### Data skew caused by JOIN operations

This topic describes the data skew caused by JOIN operations and provides a solution.

**Problem analysis and solutions**

**Possible cause**: JOIN ON keys are unevenly distributed. For example, a key has a large
number of duplicates in multiple tables that you want to join. This results in a Cartesian explosion of data in the instance on which the JOIN statement is executed and causes data skew.
**Solution**: You can use one of the following methods to resolve the data skew issue based
on scenarios: If one of the tables that you want to join is a small table, execute the MAP JOIN statement, instead of the JOIN statement. Use separate logic to handle skewed keys. For example, if data skew occurs because a large number of null key values exist in both tables, you must filter out these null key values or use a CASE WHEN expression to replace the null key values with random values before you perform a JOIN operation. If you do not want to change the SQL statement, configure the following parameters to enable automatic optimization on MaxCompute:

```
SET odps.sql.skewinfo=tab1:(col1,col2)[(v1,v2),(v3,v4),...]; SET odps.sql.skewjoin=true;
```

##### Data skew caused by multiple DISTINCT

#### operations

This topic describes the data skew caused by multiple DISTINCT operations and provides a solution.

**Problem analysis and solutions**

**Possible cause**: Multiple DISTINCT operations aggravate the GROUP BY skew.
**Solution**: Execute two GROUP BY clauses to alleviate the data skew issue. In most cases,
do not use multiple DISTINCT operations at the same time.

##### Data skew caused by misuse of dynamic

**partitions**

This topic describes the data skew caused by misuse of dynamic partitions and provides a solution.

**Problem analysis and solutions**

**Possible cause**: In scenarios where dynamic partitions are used, if K Map instances and N
destination partitions are deployed, K × N small files may be generated. This significantly increases the management workload of the file system. Therefore, the following configuration takes effect by default:

```
SET odps.sql.reshuffle.dynamicpt=true;
```

An additional level of Reduce task is introduced. The same or a small number of other Reduce instances are used to write data to the same destination partition. This prevents a large number of small files from being generated. However, dynamic partition shuffle may cause data skew.
**Solution**: If the number of destination partitions is small, only an appropriate number of
small files are generated. In this case, you can run the following command to set odps.sql.reshuffle.dynamicpt to false to prevent the data skew caused by dynamic partition shuffle.

```
SET odps.sql.reshuffle.dynamicpt=false;
```

If the number of destination partitions is large, we recommend that you do not use dynamic partitions because a large number of small files are generated.

##### Use SKEWJOIN HINT to avoid skewed hot

**key values**

This topic describes how to avoid skewed hot key values by using SKEWJOIN HINT. This topic also provides reference examples.

**Methods**

Method 1: Specify the name of a table in SKEWJOIN HINT. Note that the name specified in the hint is the alias of the table. Sample statement:

```
SELECT /*+ skewjoin(a) */ * FROM T0 a JOIN T1 b ON a.c0 = b.c0 AND a.c1 = b.c1;
```

Method 2: Specify the table name and possibly skewed columns in SKEWJOIN HINT. In the following statement, the **c0** and **c1** columns of Table a are skewed columns.

```
SELECT /*+ skewjoin(a(c0, c1)) */ * FROM T0 a JOIN T1 b ON a.c0 = b.c0 AND a.c1 = b.c 1 AND a.c2 = b.c2;
```

Method 3: Specify the table name, columns, and skewed hot key values in SKEWJOIN HINT. If the skewed key values are of the STRING type, enclose each value with double quotation marks ("). In the following statement, **(a.c0=1 and a.c1="2")** and **(a.c0=3 and**
**a.c1="4")** contain skewed hot key values.

```
SELECT /*+ skewjoin(a(c0, c1)(("1", "2"), ("3", "4"))) */ * FROM T0 a JOIN T1 b ON a. c0 = b.c0 AND a.c1 = b.c1;
```

**Differences between the methods**

Method 3 in which the **skewvalue** parameter is specified is more efficient than Method 1 and Method 2 in which the skewvalue parameter is not specified. If you use Analyze and Freeride to collect TopK skewed hot key values, SKEWJOIN may automatically take effect without requiring you to specify a hint.

**Identify the JOIN statement that causes data skew**

1. In the following screenshot captured on LogView, J5_3_4 is the Fuxi task that took the
longest time to run.
2. Click the J5_3_4 task and query the instances of this task on the tab that appears. The
query results show that the **J5_3_4#215_0** instance takes the longest time to run and its I/O records and I/O bytes are much more than those of other instances.
3. This indicates that data skew occurs on the J5_3_4#215_0 instance. However, the JOIN
statement that causes the data skew needs to be further determined. You can open the stdout of the skewed instance and the stdout of a non-skewed instance. The stdout of the skewed instance is enclosed in the yellow rectangle in the preceding figure. The Stdout dialog box shown in the following figure appears. In most cases, the web page cannot display all the content of stdout. To view all the content, you can click **Download** in this dialog box.
4. The following figures show that the value of **read count** in StreamLineRead7 of the skewed
instance is much greater than that of the non-skewed instance. Therefore, data skew occurs when data in StreamLineWrite7 and SreamLineRead7 is shuffled. Skewed instance Non-skewed instance
5. On the directed acyclic graph (DAG), you can right-click the skewed instance and select
**expand all** to find StreamLineWrite7 and StreamLineRead7.
6. The DAG shows that data skew occurs on StreamLineRead7 in MergeJoin2. MergeJoin2 is
generated after the **dim_hm_item** and **dim_tb_itm_brand** tables are joined, and then the generated new table and the **dim_tb_brand** table are joined.

**Modify the problematic SQL statement**

Locate the join based on the names of the related tables in Step 1. The result shows that data skew occurs in **left outer join** in the SQL statements and table t1 has data skew. To resolve this data skew issue, add the following command to the SQL statements:

```
/*+ skewjoin(t1) */
```

**Usage notes**

Supported join types: INNER JOIN allows you to specify a hint for either the right or left table of the JOIN operation. LEFT JOIN, SEMI JOIN, and ANTI JOIN allow you to specify a hint only for the left table. RIGHT JOIN allows you to specify a hint only for the right table. FULL JOIN does not support SKEWJOIN HINT. An Aggregate is run after SKEWJOIN HINT is added, which slows down the JOIN operation. Therefore, we recommend that you add SKEWJOIN HINT only to the JOIN statements that cause data skew. The data type of Left Side Join Key must be the same as that of Right Side Join Key for the JOIN statement to which SKEWJOIN HINT is added. If the data types are different, SKEWJOIN HINT becomes ineffective. After a hint is added, the optimizer runs an Aggregate to dynamically obtain the hot key values of the first 20 rows with the most duplicate key values. 20 is a default value. You can add the following flag parameter and specify the number of the rows whose hot key values you want to return.

```
SET odps.optimizer.skew.join.topk.num = xx;
```

You can specify a hint only for one of the two tables in the JOIN operation. In the JOIN statement to which SKEWJOIN HINT is added, **left key** = **right key** must be included. SKEWJOIN HINT cannot be added to a CARTESIAN JOIN statement. When you use SKEWJOIN HINT with other hints, note that SKEWJOIN HINT cannot be added to a JOIN statement to which MAPJOIN HINT is added. On the Json Summary tab of LogView, you can search for the **topk_agg** field to check whether SKEWJOIN HINT takes effect. If such a field exists, SKEWJOIN HINT takes effect.

#### Insufficient computing resources

This topic describes the issue of insufficient computing resources and provides a solution.

**Symptoms of insufficient resources**

Computing resources in MaxCompute may be insufficient due to improper planning and misuse of cluster resources. Jobs with insufficient computing resources typically exhibit the following two symptoms: The job output stops at a stage and the progress remains unchanged. For example, in the following figure, the progress of M1_Stg1 in the job remains at 0%. R2_1_Stg1 depends on M1_Stg1. Therefore, the progress of R2_1_Stg1 remains at 0% before M1_Stg1 is complete. Task instances are in the **Ready** state on Logview, as shown in the following figure. This state indicates that resources are insufficient to run these task instances. After an instance obtains the necessary resources, its state changes to **Running**. If an instance is in the
**Waiting** state, the instance waits for the completion of the task on which it depends.

**Cause analysis**

Each job is split into multiple tasks based on an execution plan. These tasks form a directed acyclic graph (DAG). Multiple instances are concurrently invoked in each task to complete the computation. In most cases, the resources required to invoke an instance are a single-core CPU and 2 GB memory. To properly allocate resources, a quota group is assigned to each project. The quota group determines the upper limit of resources (CPU and memory) that are available for all jobs in the project. If the resources used by the jobs that concurrently run reach the upper limit of the quota group, the jobs stop running due to insufficient resources.

**Solutions**

You can use one of the following methods to resolve this issue: Run jobs in off-peak hours. Contact O&M personnel to increase the resource capacity of the quota group for the project.

#### Methods to optimize storage in

## MaxCompute SQL

This topic describes the methods to optimize storage in MaxCompute SQL.

**Configure partitioned tables properly**

MaxCompute supports the concept of partitioning in a table. A partition refers to a partition space that is specified when a table is created. That is, a few fields in the table serve as partition key columns. In most cases, you can consider a partition as a directory in a file system. MaxCompute divides each value of the partition key column into a partition (directory). You can group multiple fields of a table to a single partition to create a multi-level partition. Multi-level partitions are analogous to multi-level directories. If you specify the name of the partition that you want to access, MaxCompute scans only the specified partition. This makes data processing more efficient and reduces costs.

**Example of a partitioning statement**

```
CREATE TABLE src (key string, value bigint) PARTITIONED BY (pt string); SELECT * FROM src WHERE pt='20160901'; -- Specify the correct partition format. When MaxCompute generates the query plan, it i ncludes only the data in the 20160901 partition as input.
```

**Example of a non-partitioning statement**

```
SELECT * FROM src WHERE key = 'MaxCompute'; -- The query plan scans the entire table.
```

**Partition configuration example**

You can configure partitions by date or geographical region. You can also configure partitions based on your business requirements. The following code provides an example:

```
CREATE TABLE IF NOT EXISTS sale_detail( shop_name string, customer_id string, total_price double) PARTITIONED BY (sale_date string,region string); -- Create a two-level partitioned table. The first-level partition sale_date represents the date, and the second-level partition region represents the region.
```

**Configure the lifecycle of a table properly**

Storage resources in MaxCompute are valuable. You can configure the lifecycle of a table based on data usage. MaxCompute deletes data that exceeds the lifecycle threshold at the earliest opportunity to save storage space. The following code provides an example:

```
CREATE TABLE test3 (key boolean) PARTITIONED BY (pt string, ds string) lifecycle 100; -- Create a table with a lifecycle of 100 days. MaxCompute deletes the table or partiti on if its last modification time exceeds 100 days.
```

**Important**

The lifecycle takes a partition as the smallest unit. For a partitioned table, if some partitions reach the lifecycle threshold, they will be directly deleted. Partitions that have not reached the lifecycle threshold are not affected. You can run the following command to change the lifecycle of a created table:

```
ALTER TABLE table_name SET lifecycle days;
```

#### UDF OOM

This topic describes the UDF Out-of-Memory (OOM) issue and provides a solution.

**Common issues**

Some jobs may encounter OOM errors during execution. Detailed error information:

```
FAILED: ODPS-0123144: Fuxi job failed - WorkerRestart errCode:9,errMsg:SigKill(OOM), us ually caused by OOM(out of memory)
```

**Solution**

You can configure UDF runtime parameters to fix the error. Example:

```
SET odps.sql.mapper.memory=3072; SET odps.sql.udf.jvm.memory=2048; SET odps.sql.udf.python.memory=1536;
```

### Limits of MaxCompute SQL

**statements**

This topic describes all the limits of MaxCompute SQL statements.

**Limit description**

| Limit | Maximum value/Limit | Categ ory | Description |
|---|---|---|---|
| Table name length | 128 bytes | Size | A table or column name can contain only letters, digits, and underscores ( ). It must start with a _ letter. |
| Comment length | 1,024 bytes | Size | A comment is a valid string that cannot exceed 1,024 bytes in length. |
| Column definitions in a table | 1,200 | Quantit y | A table can contain a maximum of 1,200 column definitions. |
| Partitions in a table | 60,000 | Quantit y | A table can contain a maximum of 60,000 partitions. |
| Partition levels of a table | 6 | Quantit y | A table can contain a maximum of six levels of partitions. |
| Destination INSERT objects | 256 | Quantit y | In a MULTI-INSERT operation, you can insert data into a maximum of 256 tables at a time. |
| UNION ALL | 256 | Quantit y | A UNION ALL operation can be performed on a maximum of 256 tables. |

| MAPJOIN | 128 | Quantit y | A MAPJOIN operation can be performed on a maximum of 128 small tables. |   |   |
|---|---|---|---|---|---|
| MAPJOIN memory | 512 MB | Size | The memory size for all small tables on which a MAPJOIN operation is performed cannot exceed 512 MB. |   |   |
| Window functions | 5 | Quantit y | A SELECT statement can contain a maximum of five window functions. |   |   |
| ptinsubq | 1,000 | Quantit y | A PT IN SUBQUERY statement can generate a maximum of 1,000 rows. |   |   |
| Length of an SQL statement | 2 MB | Size | An SQL statement cannot exceed 2 MB in length. This limit is suitable for the scenarios where you use an SDK to call SQL statements. |   |   |
| Conditions of a WHERE clause | 256 | Quantit y | A WHERE clause can contain up to 256 conditions. |   |   |
| Length of a column record | 8 MB | Size | A column record in a table cannot exceed 8 MB in length. |   |   |
| Parameters in an IN clause | 1,024 | Quantit y | This item specifies the maximum number of parameters in an IN clause, such as, in (1,2,3….,1024) . If the number of parameters in an in(…) clause is too large, the compilation performance is affected. We recommend that you use no more than 1,024 parameters, but this is not a fixed upper limit. |   |   |
|   |   |   |   | in |   |
| jobconf.json | 1 MB | Size | The maximum size of the jobconf.json file is 1 MB. If a table contains a large number of partitions, the size of the jobconf.json file may exceed 1 MB. |   |   |
| View | Not writable | Operati on | A view is not writable and does not support the INSERT operation. |   |   |
| Data type and position of a column | Unmodifiable | Operati on | The data type and position of a column cannot be modified. |   |   |

| it | (1,2,3….,1024) |
|---|---|

| Java UDFs |   | Not allowed to be ABSTRACT or STATIC . | Operati on | Java UDFs cannot be ABSTRACT or STATIC . |   |   |
|---|---|---|---|---|---|---|
| Partitions that can be queried |   | 10,000 | Quantit y | A maximum of 10,000 partitions can be queried. |   |   |
| SQL execution plans |   | 1 MB | Size | The size of the execution plan generated by MaxCompute SQL cannot exceed 1 MB. Otherwise, FAILED: ODPS-0010000:System |   |   |
|   |   |   |   |   | FAILED: ODPS-0010000:System |   |
|   |   |   |   | internal error - The Size of Plan is too |   |   |
|   |   |   |   | large |   |   |

**Important**

The preceding limits cannot be manually modified.

### Appendix

#### Escape characters

This topic describes the escape characters in MaxCompute SQL.

**List of escape characters**

In MaxCompute SQL, the backslash (\) is an escape character that invokes an alternative representation on the special characters in a character string. This escape character may also indicate a literal interpretation of the characters that follow the escape character. If the backslash (\) in a string constant is followed by three valid octal digits in the range from 001 to 177, the system converts the ASCII values to the corresponding characters. The following table describes the mapping between escape characters and represented special characters.

| Escape character | Represented special character |
|---|---|
| \b | A backspace that is used to move the current position to the previous column. |
| \t | A tab. |
| \n | A new line that is used to move the current position to the beginning of the next line. |
| \r | A carriage return that is used to reset the current position to the beginning of the current line. |
| \’ | A single quotation mark. |

| \” | A double quotation mark. |
|---|---|
| \ \ | A backslash. |
| \; | A semicolon. |
| \Z | Ctrl-Z. |
| \0 or \00 | An end character. |

Use an escape character to indicate a literal interpretation of the characters that follow the escape character. String constants in MaxCompute SQL can be expressed in single quotation marks (' ') or double quotation marks ('' ''). You can include double quotation marks ('' '') in a string that is enclosed in single quotation marks (' ') or include single quotation marks (' ') in a string that is enclosed in double quotation marks ('' ''). Examples:

```
"I'm a happy manong." 'I\'m a happy manong.'
```

Use an escape character to represent special characters. Examples:

```
SELECT length('a\tb'); -- The result is 3. This indicates that the string contains three characters, and the system treats \t as a single character. SELECT 'a\ab',length('a\ab'); -- The result is aab, 3. The system interprets \a as a regular a.
```

#### LIKE usage

This topic describes how to use the LIKE operator for character matching.

**Usage notes**

In LIKE character matching, a percent sign (%) is a wildcard character that matches an arbitrary number of characters. An underscore (_) is a wildcard character that matches a single character. To match percent signs (**%**) or underscores (**_**), escape them with double backslashes (\\). Specifically, **\\%**or **\\_** is used for the match.

```
SELECT 'abcd' LIKE 'ab%' ; -- Result +-------+
| _c0   |
+-------+
| true  |
+-------+ SELECT 'abcd' LIKE 'ab_' ; -- Result +-------+
| _c0   |
+-------+
| false |
+-------+ SELECT 'ab_cde' LIKE 'ab\\_c%'; -- Result +-------+
| _c0   |
+-------+
| true  |
+-------+
```

**Note**

MaxCompute SQL statements support only UTF-8 character sets. If data is encoded in another format, the calculation result may be incorrect.

#### Regular expressions

This topic describes regular expressions in MaxCompute SQL.

**Usage notes**

Regular expressions in MaxCompute SQL use the Perl Compatible Regular Expressions (PCRE) standards to match strings by character.

**RLIKE**

You can use the RLIKE operator to match regular expressions. The following table lists the supported metacharacters.

| Metacharacter | Description |
|---|---|
| ^ | Matches the start of a line. |
| $ | Matches the end of a line. |

| . | Matches any character. |
|---|---|
| * | Matches zero or more occurrences. |
| + | Matches one or more occurrences. |
| ? | Matches zero or one occurrence. Acts as a modifier. When this character follows any other quantifier ( *, +, ?, {n}, {n,}, {n,m} ), the match pattern becomes non-greedy. A non-greedy pattern matches as few characters of the searched string as possible, while the default greedy pattern matches as many characters as possible. |
| A\|B | Matches A or B. |
| (abc)* | Matches the sequence abc zero or more times. |
| {n} or {m,n} | Specifies the number of matches. |
| [ab] | Matches any single character in the brackets. The pattern matches a or b. |
| [a-d] | Matches any single character: a, b, c, or d. |
| [^ab] | The caret (^) indicates negation. Matches any character that is not a or b. |
| [::] | For more information, see the following table. |
| \ | The escape character. |
| \n | n is a digit ranging from 1 to 9 and indicates backward reference. |
| \d | Matches a digit. |
| \D | Matches a non-digit character. |

|   | +, ?, {n}, {n,}, {n,m} |
|---|---|

**POSIX character groups**

| Character group | Description | Valid value |
|---|---|---|

| [[:alnum:]] | Letters and digits | [a-zA-Z0-9] |
|---|---|---|
| [[:alpha:]] | Letters | [a-zA-Z] |
| [[:ascii:]] | ASCII characters | [\x00-\x7F] |
| [[:blank:]] | Spaces and tab characters | [ \t] |
| [[:cntrl:]] | Control characters | [\x00-\x1F\x7F] |
| [[:digit:]] | Digits | [0-9] |
| [[:graph:]] | Characters other than whitespace characters | [\x21-\x7E] |
| [[:lower:]] | Lowercase letters | [a-z] |
| [[:print:]] | [:graph:] and whitespace characters | [\x20-\x7E] |
| [[:punct:]] | Punctuations | [][!”#$%&’()*+,./:;<=>? @\^ `{\|}~-] _ |
| [[:space:]] | Whitespace characters | [ \t\r\n\v\f] |
| [[:upper:]] | Uppercase letters | [A-Z] |
| [[:xdigit:]] | Hexadecimal characters | [A-Fa-f0-9] |

**Escape characters**

The system uses a backslash (\) as the escape character. A backslash (\) in a regular expression indicates a second escape. For example, a regular expression is used to match the `a+b` string. The plus sign ( `+` ) is a special character in the expression and must be escaped. In the regular expression engine, the string is expressed as a\\+b . The system must perform another escape in the expression. Therefore, the expression that can match the string is a\\\+b . The following example shows how to use escape characters in a regular expression. The test_dual table is used.

```
SELECT 'a+b' rlike 'a\\\+b'; -- Result +------+
| _c1  |
+------+
| true |
+------+
```

The \ character is a special character in the regular expression engine. To match this character, it is expressed as **\\** in the engine. Then, the system performs an escape on the expression. As a result, the \ character is expressed as **\\\**.

```
SELECT 'a\\b', 'a\\b' rlike 'a\\\b'; -- Result +------+------=+
| _c0  | _c1   |
+------+------=+
| a\b  | false |
+------+------=+
```

**Note**

If a MaxCompute SQL statement contains a\\b , MaxCompute returns a\b because MaxCompute escapes the expression. If a string contains tab characters, MaxCompute stores \t as one character when MaxCompute reads this expression. In this case, \t is a common character in regular expressions.

```
SELECT 'a\tb', 'a\tb' rlike 'a\tb'; -- Result +---------+------+
| _c0     | _c1  |
+---------+------+
| a     b | true |
+---------+------+
```

#### Reserved words and keywords

This topic describes all reserved words and keywords in MaxCompute SQL.

**Overview**

**Important**

When you name a table, column, or partition, do not use reserved words or keywords. Otherwise, an error may occur. Reserved words and keywords are not case-sensitive.

```
+---------------+---------------------+---------------+--------------+-----------------+
| %             | &                   | &&            | (            | )               |
+---------------+---------------------+---------------+--------------+-----------------+
| *             | +                   | -             | .            | /               |
+---------------+---------------------+---------------+--------------+-----------------+
| ;             | <                   | <=            | <>           | =               |
+---------------+---------------------+---------------+--------------+-----------------+
| >             | >=                  | ?             | ADD          | AFTER           |
+---------------+---------------------+---------------+--------------+-----------------+
| ALL           | ALTER               | ANALYZE       | AND          | ARCHIVE         |
+---------------+---------------------+---------------+--------------+-----------------+
| ARRAY         | AS                  | ASC           | BEFORE       | BETWEEN         |
+---------------+---------------------+---------------+--------------+-----------------+
| BIGINT        | BINARY              | BLOB          | BOOLEAN      | BOTH            |
+---------------+---------------------+---------------+--------------+-----------------+
| BUCKET        | BUCKETS             | BY            | CASCADE      | CASE            |
+---------------+---------------------+---------------+--------------+-----------------+
| CAST          | CFILE               | CHANGE        | CLUSTER      | CLUSTERED       |
+---------------+---------------------+---------------+--------------+-----------------+
| CLUSTERSTATUS | COLLECTION          | COLUMN        | COLUMNS      | COMMENT         |
+---------------+---------------------+---------------+--------------+-----------------+
| COMPUTE       | CONCATENATE         | CONTINUE      | CREATE       | CROSS           |
+---------------+---------------------+---------------+--------------+-----------------+
| CURRENT       | CURSOR              | DATA          | DATABASE     | DATABASES       |
+---------------+---------------------+---------------+--------------+-----------------+
| DATE          | DATETIME            | DBPROPERTIES  | DECIMAL      | DEFERRED        |
+---------------+---------------------+---------------+--------------+-----------------+
| DELETE        | DELIMITED           | DESC          | DESCRIBE     | DIRECTORY       |
+---------------+---------------------+---------------+--------------+-----------------+
| DISABLE       | DISTINCT            | DISTRIBUTE    | DIV          | DOUBLE          |
+---------------+---------------------+---------------+--------------+-----------------+
| DROP          | ELSE                | ENABLE        | END          | EXCEPT          |
+---------------+---------------------+---------------+--------------+-----------------+
| ESCAPED       | EXCLUSIVE           | EXISTS        | EXPLAIN      | EXPORT          |
+---------------+---------------------+---------------+--------------+-----------------+
| EXTENDED      | EXTERNAL            | FALSE         | FETCH        | FIELDS          |
+---------------+---------------------+---------------+--------------+-----------------+
| FILEFORMAT    | FIRST               | FLOAT         | FOLLOWING    | FORMAT          |
+---------------+---------------------+---------------+--------------+-----------------+
| FORMATTED     | FROM                | FULL          | FUNCTION     | FUNCTIONS       |
+---------------+---------------------+---------------+--------------+-----------------+
| GRANT         | GROUP               | HAVING        | HOLD_DDLTIME | IDXPROPERTIES   |
+---------------+---------------------+---------------+--------------+-----------------+
| IF            | IMPORT              | IN            | INDEX        | INDEXES         |
+---------------+---------------------+---------------+--------------+-----------------+
| INPATH        | INPUTDRIVER         | INPUTFORMAT   | INSERT       | INT             |
+---------------+---------------------+---------------+--------------+-----------------+
```

```
| INTERSECT     | INTO                | IS            | ITEMS        | JOIN            |
+---------------+---------------------+---------------+--------------+-----------------+
| KEYS          | LATERAL             | LEFT          | LIFECYCLE    | LIKE            |
+---------------+---------------------+---------------+--------------+-----------------+
| LIMIT         | LINES               | LOAD          | LOCAL        | LOCATION        |
+---------------+---------------------+---------------+--------------+-----------------+
| LOCK          | LOCKS               | LONG          | MAP          | MAPJOIN         |
+---------------+---------------------+---------------+--------------+-----------------+
| MATERIALIZED  | MINUS               | MSCK          | NOT          | NO_DROP         |
+---------------+---------------------+---------------+--------------+-----------------+
| NULL          | OF                  | OFFLINE       | OFFSET       | ON              |
+---------------+---------------------+---------------+--------------+-----------------+
| OPTION        | OR                  | ORDER         | OUT          | OUTER           |
+---------------+---------------------+---------------+--------------+-----------------+
| OUTPUTDRIVER  | OUTPUTFORMAT        | OVER          | OVERWRITE    | PARTITION       |
+---------------+---------------------+---------------+--------------+-----------------+
| PARTITIONED   | PARTITIONPROPERTIES | PARTITIONS    | PERCENT      | PLUS            |
+---------------+---------------------+---------------+--------------+-----------------+
| PRECEDING     | PRESERVE            | PROCEDURE     | PURGE        | RANGE           |
+---------------+---------------------+---------------+--------------+-----------------+
| RCFILE        | READ                | READONLY      | READS        | REBUILD         |
+---------------+---------------------+---------------+--------------+-----------------+
| RECORDREADER  | RECORDWRITER        | REDUCE        | REGEXP       | RENAME          |
+---------------+---------------------+---------------+--------------+-----------------+
| REPAIR        | REPLACE             | RESTRICT      | REVOKE       | RIGHT           |
+---------------+---------------------+---------------+--------------+-----------------+
| RLIKE         | ROW                 | ROWS          | SCHEMA       | SCHEMAS         |
+---------------+---------------------+---------------+--------------+-----------------+
| SELECT        | SEMI                | SEQUENCEFILE  | SERDE        | SERDEPROPERTIES |
+---------------+---------------------+---------------+--------------+-----------------+
| SET           | SHARED              | SHOW          | SHOW_DATABASE| SMALLINT        |
+---------------+---------------------+---------------+--------------+-----------------+
| SORT          | SORTED              | SSL           | STATISTICS   | STATUS          |
+---------------+---------------------+---------------+--------------+-----------------+
| STORED        | STREAMTABLE         | STRING        | STRUCT       | TABLE           |
+---------------+---------------------+---------------+--------------+-----------------+
| TABLES        | TABLESAMPLE         | TBLPROPERTIES | TEMPORARY    | TERMINATED      |
+---------------+---------------------+---------------+--------------+-----------------+
| TEXTFILE      | THEN                | TIMESTAMP     | TINYINT      | TO              |
+---------------+---------------------+---------------+--------------+-----------------+
| TOUCH         | TRANSFORM           | TRIGGER       | TRUE         | TYPE            |
+---------------+---------------------+---------------+--------------+-----------------+
| UNARCHIVE     | UNBOUNDED           | UNDO          | UNION        | UNIONTYPE       |
+---------------+---------------------+---------------+--------------+-----------------+
| UNIQUEJOIN    | UNLOCK              | UNSIGNED      | UPDATE       | USE             |
+---------------+---------------------+---------------+--------------+-----------------+
| USING         | UTC                 | UTC_TMESTAMP  | VIEW         | WHEN            |
+---------------+---------------------+---------------+--------------+-----------------+
| WHERE         | WHILE               |               |              |                 |
+---------------+---------------------+---------------+--------------+-----------------+
```

#### Settings of new data types

This topic describes the precautions for configuring new data types in MaxCompute SQL.

**Precautions**

If you want to read a table that includes new data types, you are not required to add the setodps.sql.type.system.odps2=true; flag. However, you must take note of the following points: If the flag is not added, the read data is implicitly converted into the original data type for all computations. If the flag is not added for integer constants, the BIGINT type is used, and an error message is reported. If you write data to a table and the data is in passthrough mode, you can choose not to add the new data type flag. However, if you want to calculate the data, an error is reported because the implicit data type conversion is invalid.

#### ACID semantics of concurrent write

**operations in MaxCompute**

This topic describes the ACID semantics of MaxCompute during concurrent job execution.

**Terms**

Operation: a single job submitted in MaxCompute. Data object: an object that stores data, such as a non-partitioned table or a partition. INTO job: a SQL job that contains the INTO keyword, such as INSERT INTO and DYNAMIC INSERT INTO. OVERWRITE job: a SQL job that contains the OVERWRITE keyword, such as INSERT OVERWRITE and DYNAMIC INSERT OVERWRITE. Data upload by using Tunnel: an INTO or OVERWRITE job.

**Description of ACID semantics**

Atomicity: An operation is either fully complete or not performed at all. That is, an operation is not partially performed. Consistency: The integrity of data objects is maintained when an operation is performed. Isolation: An operation runs independently of other concurrent operations. Durability: After an operation is complete, modified data is permanently valid and is not lost even if a system failure occurs.

**Scenarios of ACID semantics for MaxCompute**

Atomicity When multiple jobs conflict with each other, MaxCompute ensures that only one job succeeds. The atomicity of the CREATE, OVERWRITE, and DROP operations on a single table or partition is ensured. The atomicity of cross-table operations such as MULTI-INSERT cannot be ensured. In extreme cases, the following operations may not guarantee atomicity: A `DYNAMIC INSERT OVERWRITE` operation that is performed on more than 10,000 partitions. An INTO operation. INTO operations cannot ensure atomicity because data cleansing fails during a transaction rollback. However, the transaction rollback does not cause raw data loss. Consistency OVERWRITE jobs guarantee consistency. If an INTO job fails due to a conflict, data from the failed job may remain. Isolation Non-INTO operations ensure that read operations are submitted. In INTO operations, some read operations may not be submitted. Durability MaxCompute guarantees data durability.

**ACID semantics of transactional tables**

Based on existing ACID semantics, INTO operations ensure that read operations are submitted and no data remains after an operation fails due to a conflict. The atomicity of the UPDATE and DELETE operations on a single non-partitioned table or a partition is ensured. For example, if two update jobs concurrently run to modify the data of a partition, only one job succeeds. The partition is not partially updated by one job. It is also not updated by both jobs with part of the updated data remained. Conflicts among concurrent operations: When two jobs concurrently run and write data to the same destination table, a conflict may occur. In the event of a conflict, the job that ends earlier will succeed, and the job that ends later will fail due to the conflict. The following table describes the conflicts that may occur when two jobs concurrently run and write data to the same non-partitioned table or partition. The first column lists the job that ends earlier. The other columns list the jobs that end later.

| Before/After | INSERT OVERWRITE | INSERT INTO | UPDATE/DELET E | MERGE SMALLFILES |
|---|---|---|---|---|

| INSERT OVERWRITE | Both jobs succeed. The job that finishes later overwrites the data from the job that finishes first. | Both jobs succeed. INSERT INTO appends data to the result of the INSERT OVERWRITE job that finishes first. | The non- partitioned table or partition targeted by the UPDATE job that finishes later was modified by the INSERT OVERWRITE job that finishes first. The UPDATE job that finishes later reports an error. | The non- partitioned table or partition targeted by the MERGE SMALLFILES job that finishes later was modified by the INSERT OVERWRITE job that finishes first. The MERGE SMALLFILES job that finishes later reports an error. |
|---|---|---|---|---|
| INSERT INTO | Both jobs succeed. The INSERT OVERWRITE job that finishes later overwrites the data from the INSERT INTO job that finishes first. | Both jobs succeed. The results of the two INSERT INTO jobs are appended sequentially. | The non- partitioned table or partition targeted by the UPDATE job that finishes later was modified by the INSERT INTO job that finishes first. The UPDATE job that finishes later reports an error. | The non- partitioned table or partition targeted by the MERGE SMALLFILES job that finishes later was modified by the INSERT INTO job that finishes first. The MERGE SMALLFILES job that finishes later reports an error. |
| UPDATE/DELETE | Both jobs succeed. The INSERT OVERWRITE job that finishes later overwrites the data from the UPDATE job that finishes first. | Both jobs succeed. INSERT INTO appends data to the result of the UPDATE job that finishes first. | The non- partitioned table or partition targeted by the UPDATE job that finishes later was modified by the UPDATE job that finishes first. The UPDATE job that finishes later reports an error. | The non- partitioned table or partition targeted by the MERGE SMALLFILES job that finishes later was modified by the UPDATE job that finishes first. The MERGE SMALLFILES job that finishes later reports an error. |

| MERGE SMALLFILES | Both jobs succeed. The INSERT OVERWRITE job that finishes later overwrites the data from the MERGE SMALLFILES job that finishes first. | Both jobs succeed. The INSERT INTO job that finishes later appends data to the result of the MERGE SMALLFILES job that finishes first. | The non- partitioned table or partition targeted by the UPDATE job that finishes later was modified by the MERGE SMALLFILES job that finishes first. The UPDATE job that finishes later reports an error. | The non- partitioned table or partition targeted by the MERGE SMALLFILES job that finishes later was modified by the MERGE SMALLFILES job that finishes first. The MERGE SMALLFILES job that finishes later reports an error. |
|---|---|---|---|---|

The following table simplifies the preceding rules and describes only whether an error is reported for an operation after data changes.

| Operation | Error reported upon data changes |
|---|---|
| INSERT OVERWRITE | N |
| INSERT INTO | N |
| UPDATE/DELETE | Y |
| MERGE SMALLFILES | Y |

No conflict occurs for INSERT operations in the event of data changes. An error is reported in the UPDATE/DELETE or MERGE SMALLFILES operation if the destination non-partitioned table or partition has data changes.

**Note**

MINOR/MAJOR COMPACT is classified as MERGE SMALLFILES operations. In extreme scenarios, if multiple jobs are all in the metadata update phase, an error may be reported due to a concurrency conflict among these update operations. atures of MaxCompute

## Open source features of

**MaxCompute**

This topic describes open source features of MaxCompute.

**SDK**

MaxCompute provides APIs for SDK for Java and SDK for Python to create, view, and delete MaxCompute tables. You can use SDKs to edit code and perform required operations on Technical support: View the official documentation or submit a ticket.

**MaxCompute RODPS**

MaxCompute RODPS is an R plug-in for MaxCompute. For more information, see aliyun-odpsr-plugin on GitHub. Technical support: Leave a message or create an issue in aliyun-odps-r-plugin on GitHub.

**MaxCompute JDBC**

MaxCompute JDBC is an official JDBC driver provided by MaxCompute. It provides a set of interfaces to run SQL tasks for Java programs. The project is hosted in aliyun-odps-jdbc on GitHub. Technical support: Leave a message or create an issue in aliyun-odps-jdbc on GitHub.

**Data Collector**

Data Collector is a collection of the major open source data collection tools of MaxCompute, such as the Flume plug-in, OGG plug-in, Sqoop, Kettle plug-in, and Hive Data Transfer UDTF. Flume and OGG plug-ins are implemented based on the DataHub SDK, whereas Sqoop, Kettle plug-in, and Hive Data Transfer UDTF are implemented based on the Tunnel SDK. DataHub is a real-time data transfer channel, and Tunnel is a batch data transfer channel. The Flume and OGG plug-ins are used to transfer data in real time. Sqoop, Kettle plug-in, and Hive Data Transfer UDTF are used to transfer data in offline mode. For information about the source code, see aliyun-maxcompute-data-collectors on GitHub. For more information about these tools, see wiki on GitHub. Technical support: Leave a message or create an issue in aliyun-maxcompute-data-collectors on GitHub.
