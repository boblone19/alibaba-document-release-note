---
title: "大数据计算服务 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 511
source_pdf: "07_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/odps/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 大数据计算服务 开发指南

大数据计算服务

## Java SDK

### Java SDK介绍

本文为您介绍MaxCompute提供的SDK包整体信息，并提供完整接口信息的链接。 MaxCompute完整接口信息。 您可以通过Maven管理配置新SDK的版本，Maven的配置示例如下。

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.36.2</version>
</dependency>
```

MaxCompute提供的SDK包整体信息，如下表所示。

| 包名 | 描述 |
|---|---|
| odps-sdk-core | MaxCompute基础功能。 封装了基础的MaxCompute概念及其编程接口，包括Odps、Project和Table 等，Tunnel相关的功能也在此包。 |
| odps-sdk-core-internal | MaxCompute扩展功能。 封装了一些不常用的MaxCompute概念和操作，例如Event和XFlow等。 |
| odps-sdk-commons | MaxCompute基础设施。 包含TableSchema、Column、Record和OdpsType等基础设施以及一些Util的封装。 |
| odps-sdk-udf | MaxCompute UDF编程接口。 |
| odps-sdk-mapred | MaxCompute MapReduce作业编程接口。 |

SDK包下载地址为SDK包下载。

**说明**

对于MaxCompute提供的SDK包，如果您使用的MaxCompute版本在V3.8.0以下，请下载**0.27.2**版本的SDK包使用；如果您使用的MaxCompute版本是V3.8.0到V3.11.0，请下载**0.30.8**或**0.30.9**版本的SDK包使用；如果您使用的MaxCompute版本是V3.12.0及以上，请下载**0.36.2**版本的SDK包使用。

### 环境准备

#### 概述

大数据计算服务本章节为您介绍使用SDK前需要进行的环境准备。 需要一个授权账号以及一对AccessKey ID和AccessKey Secret。 需要获取产品的Endpoint。

#### 获取Accesskey

##### 登录Apsara Uni-manager运营控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为8~20位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（！）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《**Apsara Uni-manager****运营控制台用户指南》**中的章节**《管理**
**多因素认证》**。

##### 获取组织Accesskey

**前提条件**

大数据计算服务

**操作步骤**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在页面顶部菜单栏上，单击**企业**。
3. 在**企业**页面的左侧导航栏中，单击**组织管理**。
4. 在组织结构中，选择目标组织。
5. 在对应组织页面，单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织Accesskey信息。

**说明**

一级组织的AccessKey为系统自动分配，下级组织使用一级组织的AccessKey。

##### 获取阿里云AccessKey

为了保障云资源的安全性，系统需要验证访问者的身份，以确保访问者具有相关权限。如果您需要访问云资源，您需要获取个人账号的AccessKey ID和AccessKey Secret，用于登录授权。本章节为您介绍如何获取阿里云AccessKey。

**操作步骤**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户的头像，选择**个人信息**。
3. 在**AccessKey**模块，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

#### 获取Endpoint

本章节为您介绍如何通过Apsara Uni-manager运维控制台获取产品的Endpoint。

##### 背景信息

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为ops.asconsole.intranet-domain-id.com。 推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器，地址栏中输入Apsara Uni-manager运维控制台的访问地址ops.asconsole.intranet-dom
ain-id.com，按回车键。 大数据计算服务您可以单击页面右上角的下拉按钮来进行语言切换。

**说明**

2. 输入正确的用户名及密码。
登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。

**说明**

首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 英文大小写字母阿拉伯数字（0~9） 特殊符号，包括感叹号（！）、at（@）、井号（#）、美元符号（$）、百分号（%）等密码长度10~20个字符
3. 单击**登录**，进入Apsara Uni-manager运维控制台。
4. 在Apsara Uni-manager运维控制台的顶部菜单栏单击**运维**。在左侧导航栏单击**产品运维管理** > **产品列**
表，在**云平台运维**区域单击**飞天基础运维平台**，直接打开并进入飞天基础运维平台首页。
5. 在飞天基础运维平台页面左侧导航栏中，单击**运维** > **机器运维**，进入**机器运维**页面。
6. 在机器列表中，通过筛选，选择任意一台机器，单击**Terminal**，登录到机器。
大数据计算服务
7. 在机器中执行如下命令，获取JSON数据。

```bash
curl -l "http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?c.sr.s ervice_registration"
```

8. 根据MaxCompute产品的ID（odps-service-frontend）和Key值
（odps_frontend_server.endpoint），找到MaxCompute的Endpoint。 大数据计算服务

### 核心接口

#### AliyunAccount

阿里云认证账号。输入参数为**accessId**及**accessKey**，是阿里云用户的身份标识和认证密钥。您可以通过传入AliyunAccount实例来构造MaxCompute对象，代码示例详情，请参见Odps。

**说明**

**accessId**对应AccessKey ID，**accessKey**对应AccessKey Secret。

#### Odps

MaxCompute SDK的入口，您可以通过此类来获取项目空间下的所有对象集合，包括Projects、Tables、 您可以通过传入AliyunAccount实例来构造MaxCompute对象，程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); .... }
```

#### Projects

大数据计算服务程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Project p = odps.projects().get("my_exists"); p.reload(); Map<String, String> properties = prj.getProperties(); ...
```

#### Project

#### SQLTask

用于运行和处理SQL任务的接口。可以通过Run接口直接运行SQL。Run接口返回Instance实例，通过程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new O dps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance instance = SQLTask.run(odps, "my_project", "select ..."); String id = instance.getId(); instance.waitforsuccess(); Set<String> taskNames = instance.getTaskNames(); for (String name taskNames) { TaskSummary summary = instance.getTaskSummary(name); String s = summary.getSummaryText(); } Map<String, String> results = instance.getTaskResults(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { String result = results.get(status.getKey()); }
```

**说明**

#### Instances

MaxCompute中所有实例（Instance）的集合，集合中的元素为Instance。 程序示例如下。 大数据计算服务

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); .... }
```

#### Instance

程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps (account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance ins = odps.instances().get("instance id"); Date startTime = instance.getStartTime(); Date endTime = instance.getEndTime(); ... Status instanceStatus = instance.getStatus(); String instanceStatusStr = null; instanceStatusStr = TaskStatus.Status.SUCCESS.toString(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { if (status.getValue().getStatus() != TaskStatus.Status.SUCCESS) { instanceStatusStr = status.getValue().getStatus().toString(); break; } } } else { instanceStatusStr = instanceStatus.toString(); } ... TaskSummary summary = instance.getTaskSummary("instance name"); String s = summary.getSummaryText();
```

#### Tables

程序示例如下。 大数据计算服务

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); .... }
```

#### Table

程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Table t = odps.tables().get("table name"); t.reload(); Partition part = t.getPartition(new PartitionSpec(tableSpec[1])); part.reload(); ...
```

#### Resources

程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); .... }
```

#### Resource

程序示例如下。 大数据计算服务

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Resource r = odps.resources().get("resource name"); r.reload(); if (r.getType() == Resource.Type.TABLE) { TableResource tr = new TableResource(r); String tableSource = tr.getSourceTable().getProject() + "." + tr.getSourceTable().getName(); tableSource += " partition(" + tr.getSourceTablePartition().toString() + ")"; } .... }
```

创建文件资源的示例。

```
String projectName = "my_porject"; String source = "my_local_file.txt"; File file = new File(source); InputStream is = new FileInputStream(file); FileResource resource = new FileResource(); String name = file.getName(); resource.setName(name); odps.resources().create(projectName, resource, is);
```

创建表资源的示例。

```
TableResource resource = new TableResource(tableName, tablePrj, partitionSpec); //resource.setName(INVALID_USER_TABLE); resource.setName("table_resource_name"); odps.resources().update(projectName, resource);
```

#### Functions

程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); .... }
```

#### Function

大数据计算服务程序示例如下。

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Function f = odps.functions().get("function name"); List<Resource> resources = f.getResources();
```

创建函数的示例。

```
String resources = "xxx:xxx"; String classType = "com.aliyun.odps.mapred.open.example.WordCount"; ArrayList<String> resourceList = new ArrayList<String>(); resourceList.add(r); } Function func = new Function(); func.setName(name); func.setClassType(classType); func.setResources(resourceList); odps.functions().create(projectName, func);
```

#### Spark Shell

Spark向集群提交任务时的常用接口之一。 执行如下命令，启动接口应用。

```
$cd $SPARK_HOME
```

`--` 进入`Spark`目录。 `--` 选择运行模式并启动应用。 示例如下。

```
sc.parallelize(0 to 100, 2).collect sql("select * from spark_user_data").show(200,100)
```

#### Spark R

Spark向集群提交任务时的常用接口之一。 执行如下命令，启动接口应用。 大数据计算服务

```
$mkdir -p /home/admin/R && unzip ./R/R.zip -d /home/admin/R/
```

`--` 创建一个目录R并解压该目录下的`R.zip`。

```
$export PATH=/home/admin/R/bin/:$PATH
```

`--` 设置环境变量。 `--` 选择运行模式并启动应用。 示例如下。

```
df <- as.DataFrame(faithful)
```

`df`

```
head(select(df, df$eruptions)) head(select(df, "eruptions")) head(filter(df, df$waiting < 50)) results <- sql("FROM spark_user_data SELECT *") head(results)
```

#### Spark SQL

Spark向集群提交任务时的常用接口之一。 执行如下命令，启动接口应用。

```
$cd $SPARK_HOME
```

`--` 进入`Spark`目录。 `--` 选择运行模式并启动应用。 示例如下。

```
show tables; select * from spark_user_data limit 3; quit;
```

#### Spark JDBC

Spark向集群提交任务时的常用接口之一。 执行如下命令，启动接口应用。

```
$sbin/stop-thriftserver.sh
```

`--` 停止线程。

```
$sbin/start-thriftserver.sh
```

`--` 重启线程。

```
$bin/beeline
```

`--` 启动应用。 示例如下。 大数据计算服务

```
!connect jdbc:hive2://localhost:10000/odps_smoke_test show tables; select * from mr_input limit 3; !quit
```

#### Document APIs

ElasticSearch on MaxCompute兼容的开源API接口集合之一，具体接口信息请参见Document APIs。

#### Search APIs

ElasticSearch on MaxCompute兼容的开源API接口集合之一，具体接口信息请参见Search APIs。

#### CheckPermissionTest

本章节为您介绍Java SDK核心接口中的CheckPermissionTest接口。 通过CheckPermissionTest接口，提供上层应用指定用户是否拥有某资源指定权限的查询接口。 程序示例如下。

```java
Account account = new AliyunAccount("accessId", "accessKey"); Odps odps = new Odps(account); SecurityManager sm = odps.projects().get().getSecurityManager(); SecurityManager.PermissionDesc desc = new SecurityManager.PermissionDesc(
    odps.getDefaultProject(),
    CheckPermissionConstants.ObjectType.Table,
    "table_name",
    CheckPermissionConstants.ActionType.Describe);
desc.setColumns(Arrays.asList("col1", "col2")); desc.setPrincipal("ALIYUN$test@aliyun.com"); SecurityManager.CheckPermissionResultInfo res = sm.checkPermission(desc); System.out.println("Result: " + res.getResult()); System.out.println("Message: " + res.getMessage());
```

#### Volume2

本章节为您介绍Java SDK核心接口中的Volume2接口。专有云使用的Volume2，type使用 `new` ，无需指定 `extLocationt` 等公共云External Volume等信息。

**项目依赖**

使用SDK操作External Volume前需要添加如下依赖。 大数据计算服务

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.44.0-SNAPSHOT</version>
</dependency>
```

**创建 Volume**

Create 大数据计算服务

```
/**
```

* 创建 `volume`
`* @param builder volume` 的参数配置

```
* @throws OdpsException
```

`*/`

```
public void create(VolumeBuilder builder) throws OdpsException
    /**
```

* 创建`Volume`
*

```
* @param volumeName volume名
* @param comment
```

`* @param type` 创建原有`Volume`传入 `{@link Volume}.Type.Old,`创建新`VolumeFS`功能的`volume`传入`{@l`

```
ink Volume}
* @throws OdpsException
```

`*/`

```
public void create(String volumeName, String comment, Volume.Type type)
    /**
```

* 创建`Volume`
* `* @param volumeName` 所要创建的`volume`名

```
* @param comment
```

`* @param type` 创建原有`Volume`传入 `{@link Volume}.Type.Old,`创建新`VolumeFS`功能的`volume`传入`{@l`

```
ink Volume}
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type)
    /**
```

* 创建`Volume`
* `* @param volumeName` 所要创建的`volume`名

```
* @param comment
```

`* @param type` 创建原有`Volume`传入 `{@link Volume}.Type.Old,`创建新`VolumeFS`功能的`volume`传入`{@l`

```
ink Volume}
```

`* @param lifecycle` 生命周期

```
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type, Long lifecycle) throws OdpsException
```

Create示例大数据计算服务 `/*` 创建`volume` `*/`

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
    }
    if (comment != null) {
        builder.comment(comment);
    }
    if (roleArn != null) {
        builder.addProperty(Volumes.EXTERNAL_VOLUME_ROLEARN_KEY, roleArn);
    }
    getCurrentOdps().volumes().create(builder);
}
```

**获取指定Volume信息**

Get 大数据计算服务

```
/**
```

* 获得指定`Volume`信息
*

```
* @param volumeName Volume名
* @return
```

`*/`

```
public Volume get(String volumeName) /**
```

* 获得指定`Volume`信息
*

```
* @param volumeName  Volume名
* @return
```

`*/`

```
public Volume get(String projectName, String volumeName)
```

Get示例 `/*` 获取 `volume` `*/`

```
public Volume getVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    Volume volume = odps.volumes().get(projectName, extVolumeName);
    return volume;
}
```

**获取Volume信息迭代器**

Iterator 大数据计算服务

```
/**
```

* `* @return Volume`迭代器 `*/`

```
public Iterator<Volume> iterator()
    /**
```

* 获取`Volume`信息迭代器
* `* @return Volume`迭代器 `*/`

```
public Iterator<Volume> iterator(final String projectName)
    /**
```

* 获取`Volume`信息迭代器
* `* @param filter` 过滤条件 `* @return Volume`迭代器 `*/`

```
public Iterator<Volume> iterator(final VolumeFilter filter)
    /**
```

* 获取`Volume`信息迭代器
* `* @param filter` 过滤条件 `* @return Volume`迭代器 `*/`

```
public Iterator<Volume> iterator(final String projectName, final VolumeFilter filter)
```

Iterator示例 `/*` 获取`volume`迭代器 `*/`

```
public Iterator<Volume> getVolumeIterator() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    VolumeFilter volumeFilter = new VolumeFilter();
    volumeFilter.setName(extVolumeName);
    Iterator<Volume> iterator = odps.volumes().iterator(projectName, volumeFilter);
    return iterator;
}
```

**删除Volume**

大数据计算服务

```
/**
```

* 删除`Volume`
*

```
* @param volumeName 表名
* @throws OdpsException
```

`*/`

```
public void delete(String volumeName) /**
```

* 删除`Volume`
*

```
* @param volumeName 表名
* @throws OdpsException
```

`*/`

```
public void delete(String projectName, String volumeName)
```

Delete示例 `/*` 删除`Volume` `*/`

```
public void deleteVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    try {
        odps.volumes().delete(projectName, extVolumeName);
    } catch (OdpsException e) {
        throw new RuntimeException(e);
    }
}
```

**获取VolumeFsFile**

getVolumeFSFile

```
/**
```

* 获取 `volume path` 下的 `Fs File`
*

```
* @param path 路径
```

* `*/`

```
public VolumeFSFile getVolumeFSFile(String path) throws VolumeException;
```

使用VolumeFsFile示例大数据计算服务 `/*` 获取 `volume file` 的详细信息 `*/`

```
public void getVolumeIterator() {
    String projectName = "test_project";
    String volumeName = "test_volume";
    String testFilePath = "/" + volumeName + "/file";;
    VolumeFSFile volumeFSFile = odps.volumes().get(projectName,
volumeName).getVolumeFSFile(testFilePath);
    bool isDir = volumeFSFile.getIsdir());
    long length = volumeFSFile.getLength();
}
```

大数据计算服务

## Python SDK

PyODPS是MaxCompute的Python版本的SDK，提供简单方便的Python编程接口。PyODPS支持类似 Pandas的快速、灵活和富有表现力的数据结构。您可以通过PyODPS提供的DataFrame API使用Pandas 的数据结果处理功能。更多详细信息请参见Github项目和PyODPS文档。 如果您需要了解更多关于PyODPS的内容，请参见《大数据计算服务(MaxCompute)用户指南》中的**PyODPS**章节。

**安装PyODPS**

PyODPS支持Python2.6以上（包括Python3），系统安装pip后，只需运行 `pip install` `pyodps` ，PyODPS的相关依赖便会自动安装。具体操作请参见《大数据计算服务(MaxCompute)用户指南》中的**安装指南**章节。

**初始化**

您需要用阿里云账号初始化一个MaxCompute的入口，示例如下。

```python
from odps import ODPS odps = ODPS('**your-access-id**', '**your-secret-access-key**', '**your-default-project
**',
            endpoint='**your-end-point**')
```

根据上述操作初始化后，便可以对表、资源及函数等进行操作。 后文中的o对象如无特殊说明，均指的是MaxCompute入口对象。

**说明**

**获取PyODPS项目空间**

项目空间是MaxCompute的基本组织单元，类似于Database的概念。

| 您可通过 | get project _ | 命令获取到某个项目空间，示例如下。 |
|---|---|---|
| project = odps.get project('my project') # 取到某个项目。 _ _ project = odps.get project() # 取到默认项目。 _ |  |  |

**说明**

如果不提供参数，则获取到默认项目空间。 表是MaxCompute的数据存储单元。

**PyODPS表操作**

| 通过调用 | list tables _ | 可以列出项目空间下的所有表，示例如下。 |
|---|---|---|
| for table in odps.list tables(): # 处理每张表。 _ |  |  |

通过调用 `exist_table` 可以判断表是否存在，通过调用 `get_table` 可以获取表。 大数据计算服务

```
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
}
 t.lifecycle
```

`-1`

```xml
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

**创建PyODPS表的Schema**

初始化的方法有两种，如下所示： 通过表的列和可选的分区来初始化。

```
 from odps.models import Schema, Column, Partition
 columns = [Column(name='num', type='bigint', comment='the column')]
 partitions = [Partition(name='pt', type='string', comment='the partition')]
 schema = Schema(columns=columns, partitions=partitions)
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

通过调用 `Schema.from_lists` 。此方法虽然调用更加方便，但是无法直接设置列和分区的注释。

```
 schema = Schema.from_lists(['num'], ['bigint'], ['pt'], ['string'])
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

**创建PyODPS表**

大数据计算服务您可以使用表的Schema来创建表，示例如下。

```
table = odps.create_table('my_new_table', schema, if_not_exists=True) # 只有不存在表时才
```

创建。

```
table = o.create_table('my_new_table', schema, lifecycle=7) # 设置生命周期。
```

也可以使用英文逗号（,）连接的字段名+字段类型的字符串组合来创建表，示例如下。
# 创建非分区表。

```
 table = o.create_table('my_new_table', 'num bigint, num2 double', if_not_exists=True)
```

# 创建分区表可传入 (表字段列表, 分区字段列表)。

```
 table = o.create_table('my_new_table', ('num bigint, num2 double', 'pt string'), if_no
t_exists=True)
```

在未经设置的情况下，创建表时，只允许使用BIGINT、DOUBLE、DECIMAL、STRING、DATETIME、 如果需要支持TINYINT、STRUCT等新类型，可以设置 `options.sql.use_odps2_extension =` `True`；，以打开这些类型的支持，示例如下。

```python
 from odps import options
 options.sql.use_odps2_extension = True
 table = o.create_table('my_new_table', 'cat smallint, content
```

**获取PyODPS表数据**

您可通过以下三种方法获取表数据： 通过调用 `head` 获取表数据，但仅限于查看每张表开始的小于1万条的数据，示例如下。

```
 for record in t.head(3):
```

`print(record[0]) #` 取第0个位置的值。 `print(record['c_double_a']) #` 通过字段取值。 `print(record[0: 3]) #` 切片操作。 `print(record[0, 2, 3]) #` 取多个位置的值。 `print(record['c_int_a', 'c_double_a']) #` 通过多个字段取值。 通过在Table上执行 `open_reader` 操作，打开一个Reader来读取数据。您可以使用With表达式，也可以不使用。
# 使用`With`表达式。

```
 with t.open_reader(partition='pt=test') as reader:
```

`for record in reader[5:10] #` 可以执行多次，直到将`Count`数量的`Record`读完，这里可以改造成并行操作。
# 处理一条记录。
# 不使用`With`表达式。

```
 reader = t.open_reader(partition='pt=test')
 for record in reader[5:10]
```

# 处理一条记录。
通过使用Tunnel API读取表数据， `open_reader` 操作其实也是对Tunnel API的封装。 大数据计算服务

**PyODPS写入数据**

| 类似于 | open reader _ | ，Table对象同样可以执行 | open writer _ | 来打开Writer，并写数据。示例如下。 |
|---|---|---|---|---|
| # 使用With表达式。 with t.open writer(partition='pt=test') as writer: _ writer.write(records) # 这里records可以是任意可迭代的records，默认写到block 0。 with t.open writer(partition='pt=test', blocks=[0, 1]) as writer: # 这里同是打开两个bloc _ k。 writer.write(0, gen records(block=0)) _ writer.write(1, gen records(block=1)) # 这里两个写操作可以多线程并行，各个block间是独立 _ 的。 # 不使用With表达式。 writer = t.open writer(partition='pt=test', blocks=[0, 1]) _ writer.write(0, gen records(block=0)) _ writer.write(1, gen records(block=1)) _ writer.close() # 不要忘记关闭 writer，否则数据可能写入不完全。 |  |  |  |  |

同样，向表中写入数据也是对Tunnel API的封装。

**删除PyODPS表**

删除表的操作，示例如下。

```
 odps.delete_table('my_table_name', if_exists=True)  #  只有表存在时删除。
```

**PyODPS表分区**

基本操作。 遍历表的全部分区，示例如下。

```python
 for partition in table.partitions:
     print(partition.name)
 for partition in table.iterate_partitions(spec='pt=test'):
```

# 遍历二级分区。
判断分区是否存在，示例如下。 获取分区，示例如下。

```python
 print(partition.creation_time)
2019-09-18 22:22:27
 partition.size
```

创建分区。 `t.create_partition('pt=test', if_not_exists=True) #` 不存在的时候才创建。 删除分区。 大数据计算服务 `t.delete_partition('pt=test', if_exists=True) #` 存在的时候才删除。 `partition.drop() # Partition`对象存在的时候直接`drop`。

**PyODPS SQL**

执行SQL。 `odps.execute_sql('select * from dual') #` 同步的方式执行，会阻塞直到`SQL`执行完成。

```
instance = odps.run_sql('select * from dual') # 异步的方式执行。
```

读取SQL执行结果。 运行SQL的instance能够直接执行 `open_reader` 的操作，一种情况是SQL返回了结构化的数据。

```
 with odps.execute_sql('select * from dual').open_reader() as reader:
     for record in reader:
```

# 处理每一个`record`。
另一种情况是SQL可能执行的是例如 `desc` 操作，这时通过 `reader.raw` 属性取到原始的SQL执行结果。

```python
 with odps.execute_sql('desc dual').open_reader() as reader:
     print(reader.raw)
```

资源在MaxCompute上常用在UDF和MapReduce中。

| 可以使用 | list resources _ |  |
|---|---|---|
| delete resource _ |  |  |
|  |  | ，或直 |

|  | exist resource _ |
|---|---|
| drop |  |

在PyODPS中，主要支持两种资源类型，一种是文件，另一种是表。 文件资源。 文件资源包括基础的FILE类型、以及PY、JAR和ARCHIVE类型。 创建文件资源。 创建文件资源可以通过给定资源名、文件类型、以及一个**file-like**的对象（或者是字符串对象）来创建，示例如下。

```
resource = odps.create_resource('test_file_resource', 'file', file_obj=open('/to/path/file')) # 使用file-like的对象。 resource = odps.create_resource('test_py_resource', 'py', file_obj='import this')
```

# 使用字符串。
大数据计算服务读取和修改文件资源。

|  | open resource _ |
|---|---|
| open |  |

示例如下。 `content = fp.read() #` 读取全部的内容。 `fp.seek(0) #` 回到资源开头。 `lines = fp.readlines() #` 读成多行。 `fp.write('Hello World') #` 报错，读模式下无法写资源。

```
 with odps.open_resource('test_file_resource', mode='r+') as fp:  # 读写模式打开。
     fp.read()
```

`fp.tell() #` 当前位置。

```
     fp.seek(10)
     fp.writelines(['Hello\n', 'World\n'])  # 写入多行。
     fp.write('Hello World')
```

`fp.flush() #` 手动调用会将更新提交到`MaxCompute`。 所有支持的打开类型包括： r：读模式，只能打开不能写。 w：写模式，只能写入而不能读文件，注意用写模式打开，文件内容会被先清空。 a：追加模式，只能写入内容到文件末尾。 r+：读写模式，能任意读写内容。 w+：类似于r+，但会先清空文件内容。 a+：类似于r+，但写入时只能写入文件末尾。 同时，PyODPS中，文件资源支持以二进制模式打开，例如一些压缩文件等就需要以这种模式打开，因此**rb**就是指以二进制读模式打开文件，**r+b**是指以二进制读写模式打开。 表资源。 创建表资源。

```
 odps.create_resource('test_table_resource', 'table', table_name='my_table', partitio
n='pt=test')
```

更新表资源。

```
 table_resource = odps.get_resource('test_table_resource')
 table_resource.update(partition='pt=test2', project_name='my_project2')
```

**DataFrame**

PyODPS提供了DataFrame API，它提供了类似pandas的接口，但是能充分利用MaxCompute的计算能力。完整的DataFrame文档请参见DataFrame。 DataFrame的相关示例如下。 在所有步骤开始前，需要创建MaxCompute对象。

**说明**

```
 odps = ODPS('**your-access-id**', '**your-secret-access-key**',
             project='**your-project**', endpoint='**your-end-point**'))
```

大数据计算服务假设已经有三张表，分别是**pyodps_ml_100k_movies**（电影相关的数据）、**pyodps_ml_100k_users**（用户相关的数据）以及**pyodps_ml_100k_ratings**（评分有关的数据）。

```
 from odps.df import DataFrame
 users = DataFrame(o.get_table('pyodps_ml_100k_users'))
```

通过**dtypes**属性来查看这个DataFrame有哪些字段，分别是什么类型，示例如下。

```
users.dtypes
```

| 通过 | head | 方法，可以获取前N条数据，方便快速预览数据。示例如下。 |
|---|---|---|
| users.head(10) |  |  |

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
| 8 | 9 | 29 | M | student | 01002 |
| 9 | 10 | 53 | M | lawyer | 90703 |

有时候，并不需要都看到所有字段，便可以从中筛选出一部分。示例如下。

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

大数据计算服务有时候只是排除个别字段。示例如下。

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

排除掉一些字段的同时，想要通过计算得到一些新的列，例如将sex为M的置为True，否则为False，并取名叫sex_bool。示例如下。

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

如果想知道年龄在20到25岁之间的人有多少个，示例如下。 如果想知道男女用户分别有多少，示例如下。

| number | sex | count |
|---|---|---|
| 0 | F | 273 |
| 1 | M | 670 |

如果想将用户按职业划分，从高到底，获取人数最多的前10个职业，示例如下。

```
df = users.groupby('occupation').agg(count=users['occupation'].count())
```

| number | occupation | count |
|---|---|---|

大数据计算服务

| 0 | student | 196 |
|---|---|---|
| 1 | other | 105 |
| 2 | educator | 95 |
| 3 | administrator | 79 |
| 4 | engineer | 67 |
| 5 | programmer | 66 |
| 6 | librarian | 51 |
| 7 | writer | 45 |
| 8 | executive | 32 |
| 9 | scientist | 31 |

DataFrame API提供了value_counts方法来快速达到同样的目的。示例如下。

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

使用更直观的图来查看这份数据，示例如下。 使用横向的柱状图来可视化，示例如下。

```
 users['occupation'].value_counts().plot(kind='barh', x='occupation',
ylabel='prefession')
```

将年龄分成30组，查看各年龄分布的直方图，示例如下。 大数据计算服务

```
users.age.hist(bins=30, title="Distribution of users' ages", xlabel='age',
```

使用Join把这三张表进行联合后，把它保存成一张新的表。示例如下。

```
movies = DataFrame(o.get_table('pyodps_ml_100k_movies')) ratings = DataFrame(o.get_table('pyodps_ml_100k_ratings')) o.delete_table('pyodps_ml_100k_lens', if_exists=True) lens = movies.join(ratings).join(users).persist('pyodps_ml_100k_lens') lens.dtypes odps.Schema {
  movie_id                            int64
  title                               string
  release_date                        string
  video_release_date                  string
  imdb_url                            string
  user_id                             int64
  rating                              int64
  age                                 int64
  sex                                 string
  occupation                          string
  zip_code                            string
}
```

把0到80岁的年龄，分成8个年龄段，示例如下。

```
 labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
 cut_lens = lens[lens, lens.age.cut(range(0, 81, 10), right=False,
labels=labels).rename('年龄分组')]
```

取分组和年龄唯一的前10条数据来进行查看，示例如下。

```
cut_lens['年龄分组', 'age'].distinct()[:10]
```

| number | 年龄分组 | age |
|---|---|---|
| 0 | 0-9 | 7 |
| 1 | 10-19 | 10 |
| 2 | 10-19 | 11 |
| 3 | 10-19 | 13 |
| 4 | 10-19 | 14 |
| 5 | 10-19 | 15 |
| 6 | 10-19 | 16 |
| 7 | 10-19 | 17 |

大数据计算服务

| 8 | 10-19 | 18 |
|---|---|---|
| 9 | 10-19 | 19 |

对各个年龄分组下，用户的评分总数和评分均值进行查看，示例如下。

```
 cut_lens.groupby('年龄分组').agg(cut_lens.rating.count().rename('评分总数'), cut_lens.rat
```

`ing.mean().rename('`评分均值`'))`

| number | 年龄分组 | 评分均值 | 评分总数 |
|---|---|---|---|
| 0 | 0-9 | 3.767442 | 43 |
| 1 | 10-19 | 3.486126 | 8181 |
| 2 | 20-29 | 3.467333 | 39535 |
| 3 | 30-39 | 3.554444 | 25696 |
| 4 | 40-49 | 3.591772 | 15021 |
| 5 | 50-59 | 3.635800 | 8704 |
| 6 | 60-69 | 3.648875 | 2623 |
| 7 | 70-79 | 3.649746 | 197 |

**Configuration**

PyODPS提供了一系列的配置选项，可通过 `odps.options` 获得。可配置的MaxCompute选项，如下所示： 通用配置。

| 选项 | 说明 | 默认值 |
|---|---|---|
| end point _ | MaxCompute Endpoint | None |
| default project _ | 默认Project | None |
| log view host _ _ | LogView主机名 | None |
| log view hours _ _ | LogView保持时间（小时） | 24 |
| local timezone _ | 使用的时区，True表示本地时间，False表示UTC，也可用pytz 的时区 | 1 |
| lifecycle | 所有表生命周期 | None |
| temp lifecycle _ | 临时表生命周期 | 1 |
| biz id _ | 用户ID | None |
| verbose | 是否打印日志 | False |
| verbose log _ | 日志接收器 | None |

大数据计算服务

| chunk size _ | 写入缓冲区大小 | 1496 |
|---|---|---|
| retry times _ | 请求重试次数 | 4 |
| pool connections _ | 缓存在连接池的连接数 | 10 |
| pool maxsize _ | 连接池最大容量 | 10 |
| connect timeout _ | 连接超时 | 5 |
| read timeout _ | 读取超时 | 120 |
| completion size _ | 对象补全列举条数限制 | 10 |
| notebook repr widget _ _ | 使用交互式图表 | True |
| sql.settings | MaxCompute SQL运行全局hints | None |
| sql.use odps2 extension _ _ | 启用MaxCompute2.0语言扩展 | False |

数据上传和下载配置。

| 选项 | 说明 | 默认值 |
|---|---|---|
| tunnel.endpoint | Tunnel Endpoint | None |
| tunnel.use instance tunnel _ _ | 使用Instance Tunnel获取执行结果 | True |
| tunnel.limited instance tunnel _ _ | 限制Instance Tunnel获取结果的条数 | True |
| tunnel.string as binary _ _ | 在string类型中使用bytes而非 unicode | False |

DataFrame配置。

| 选项 | 说明 | 默认值 |
|---|---|---|
| interactive | 是否在交互式环境 | 根据检测值 |
| df.analyze | 是否启用非MaxCompute内置函数 | True |
| df.optimize | 是否开启DataFrame全部优化 | True |
| df.optimizes.pp | 是否开启DataFrame谓词下推优化 | True |
| df.optimizes.cp | 是否开启DataFrame列剪裁优化 | True |
| df.optimizes.tunnel | 是否开启DataFrame使用tunnel 优化执行 | True |
| df.quote | MaxCompute SQL后端是否用`` 来标记字段和表名 | True |
| df.libraries | DataFrame运行使用的第三方库 （资源名） | None |

大数据计算服务 PyODPS ML配置。

| 选项 | 说明 | 默认值 |
|---|---|---|
| ml.xflow project _ | 默认Xflow工程名 | algo public _ |
| ml.use model transfer _ _ | 是否使用ModelTransfer获取模型 PMML | True |
| ml.model volume _ | 在使用ModelTransfer时使用的 Volume名称 | pyodps volume _ |

大数据计算服务

## MaxCompute SQL

### 概述

#### 使用场景

**使用介绍**

**适用场景**

MaxCompute SQL离线计算适用于海量数据（TB级别）且实时性要求不高的场景。 MaxCompute SQL离线计算的每个作业的准备及提交等阶段耗时较长，因此要求每秒处理几千至数万笔事务的业务是不能用MaxCompute SQL完成的。准实时场景可以使用MaxCompute SQL的在线模式处理。

**注意事项**

MaxCompute SQL采用类似于SQL的语法，可以看作是标准SQL的子集，但不能等价成一个数据库，它在很多方面并不具备数据库的特征，如事务、主键约束以及索引等。在MaxCompute中允许的最大SQL长度是 `2 MB` 。

#### 保留字

MaxCompute将SQL语句的关键字作为保留字。在命名表、列或分区时请不要使用这些保留字，否则会报错。保留字不区分大小写。

**保留字列表**

| 类别 | 保留字 |
|---|---|

大数据计算服务

| 特殊符号 | % & && ( ) * + - . / ; < <= <> = > >= ? |
|---|---|
| DDL操作/表操作 | ADD ALTER COLUMN COMMENT CREATE DROP LIFECYCLE PARTITION RENAME REPLACE TABLE TOUCH VIEW |
| DML操作/数据操作 | FROM INSERT INTO OVERWRITE SELECT WHERE |

大数据计算服务

| 查询/连接/排序 | ALL ASC BY DESC DISTINCT DISTRIBUTE FULL GROUP JOIN LEFT LIMIT MAPJOIN ON ORDER OUTER RIGHT SORT UNION |
|---|---|
| 逻辑/条件 | AND BETWEEN CASE ELSE FALSE IF IN IS LIKE NOT NULL OR RLIKE THEN TRUE WHEN |

大数据计算服务

| 数据类型 | BIGINT BOOLEAN CAST DOUBLE STRING |
|---|---|
| 其他关键字 | AS |

#### 分区表

本文介绍MaxCompute分区表的使用注意事项及限制，帮助您规范使用分区表。

**分区表使用说明**

例如在 `SELECT` 语句的WHERE条件过滤中使用分区列作为过滤条件。指定分区列会给您带来诸多便利： 例如提高SQL运行效率。 精准定位所需数据范围，降低I/O开销与计算资源消耗等。

**注意事项**

与此同时，部分对分区操作的SQL的运行效率则较低： 例如单个作业涉及的输出表分区数量过多（大于10000个），即并发写分区数量过多时，会造成SQL执行失败。 在使用分区表时，根据数据源的数据情况合理评估分区数和分区级别，避免性能和稳定性问题。 MaxCompute分区表最大支持创建6级分区。 对于部分MaxCompute操作命令，处理分区表和非分区表时的语法有差别，详情请参见DDL语句及DML 语句，建表语句请参见创建表。

#### 类型转换

##### 显式类型转换

显式类型转换是用CAST将一种数据类型的值转换为另一种类型的值的行为。本文介绍显式类型转换的相关信息。 MaxCompute SQL支持的显式类型转换如下所示。更多关于CAST的详细信息请参见CAST。

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|
| BIGINT | 不涉及 | Y | Y | N | N | Y |
| DOUBLE | Y | 不涉及 | Y | N | N | Y |
| STRING | Y | Y | 不涉及 | Y | N | Y |

大数据计算服务

| DATETIME | N | N | Y | 不涉及 | N | N |
|---|---|---|---|---|---|---|
| BOOLEAN | N | N | N | N | 不涉及 | N |
| DECIMAL | Y | Y | Y | N | N | 不涉及 |

其中，Y表示可以转换，N表示不可以转换，不涉及表示不需要转换。

|  | 说明将DOUBLE类型转换为BIGINT类型时，小数部分会被截断，例如CAST(1.6 AS BIGINT) = 1。 满足DOUBLE类型格式的STRING类型转换为BIGINT时，会先将STRING类型转换为DOUBLE 类型，再将DOUBLE类型转换为BIGINT类型，因此，小数部分会被截断，例如 CAST("1.6" AS BIGINT) = 1 。 满足BIGINT类型格式的STRING类型可以被转换为DOUBLE类型，小数点后保留一位，例如 CAST("1" AS DOUBLE) = 1.0 。 常量字符串转为DECIMAL类型时，需要加上双引号（'' '' 或“ ”），不加引号的数值会被当作 DOUBLE类型处理，例如CAST("1.234567890123456789" AS DECIMAL)。 不支持的显式类型转换会导致异常。 如果在执行转换时失败，报错退出。 日期类型转换时采用默认格式yyyy-mm-dd hh:mi:ss:ff3，详细信息请参见STRING类型与 DATETIME类型之间的转换。 部分类型之间不可以进行显式类型转换，但可以通过SQL内建函数进行转换，例如从BOOLEAN 类型转换到STRING类型，可使用函数TO CHAR，详细信息请参见TO CHAR，而TO DATE函 _ _ _ 数同样支持从STRING类型到DATETIME类型的转换。 DECIMAL类型超出值域， CAST(STRING TO DECIMAL) 可能会出现最高位溢出报错，最低位溢出截断等情况。 |  |  |
|---|---|---|---|
|  |  | CAST("1.6" |  |
|  | AS BIGINT) = 1 |  |  |

##### 隐式类型转换及其作用域

隐式类型转换是指在运行时，由MaxCompute依据上下文使用环境及类型转换规则自动进行的类型转换。 本文介绍隐式类型转换的相关信息。

**隐式类型转换说明**

MaxCompute支持的隐式类型转换规则如下所示。

| From/To | BOOLEAN | TINYINT | SMALLINT | INT | BIGINT | FLOAT |
|---|---|---|---|---|---|---|
| BOOLEAN | T | F | F | F | F | F |
| TINYINT | F | T | T | T | T | T |

大数据计算服务

| SMALLINT | F | F | T | T | T | T |
|---|---|---|---|---|---|---|
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
| TINYINT | T | T | T | T | F | F |
| SMALLINT | T | T | T | T | F | F |
| INT | T | T | T | T | F | F |
| BIGINT | T | T | T | T | F | F |
| FLOAT | T | T | T | T | F | F |
| DOUBLE | T | T | T | T | F | F |

大数据计算服务

| DECIMAL | F | T | T | T | F | F |
|---|---|---|---|---|---|---|
| STRING | T | T | T | T | F | F |
| VARCHAR | T | T | T | T | F | F |
| TIMESTA MP | F | F | T | T | T | F |
| BINARY | F | F | F | F | F | T |

其中，T表示可以转换，F表示不可以转换。

**说明**

不支持的隐式类型转换会导致异常。 如果在执行转换时失败，报错退出。 由于隐式类型转换是MaxCompute依据上下文使用环境自动进行的类型转换，因此，推荐在类型不匹配时显式的用CAST进行转换。 隐式类型转换规则是有发生作用域的。在某些作用域中，只有一部分规则可以生效。

**关系运算符作用下的隐式转换**

关系运算符包括：等于（=）、不等于（<>）、小于（<）、小于等于（<=）、大于（>）、大于等于 （>=）、IS NULL、IS NOT NULL、LIKE、RLIKE和IN。 当不同类型的数据共同参与关系运算时，按照下述原则进行隐式类型转换。

**关系运算符作用下的隐式转换**

由于LIKE、RLIKE和IN的隐式类型转换规则不同于其他关系运算符，此处的说明不包含这三种特殊的关系运算符。

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|
| BIGINT | 不涉及 | DOUBLE | DOUBLE | N | N | DECIMAL |
| DOUBLE | DOUBLE | 不涉及 | DOUBLE | N | N | DECIMAL |
| STRING | DOUBLE | DOUBLE | 不涉及 | DATETIME | N | DECIMAL |
| DATETIME | N | N | DATETIME | 不涉及 | N | N |
| BOOLEAN | N | N | N | N | 不涉及 | N |

大数据计算服务

| DECIMAL | DECIMAL | DECIMAL | DECIMAL | N | N | 不涉及 |
|---|---|---|---|---|---|---|

**说明**

如果需要比较的两个类型间不能进行隐式类型转换，则该关系运算不能完成，报错退出。

**特殊的关系运算符作用下的隐式转换**

特殊的关系运算符包括LIKE、RLIKE和IN。

**LIKE和RLIKE的使用方式**

```
Source LIKE Pattern; Source RLIKE Pattern;
```

两者在隐式类型转换中的注意事项如下： LIKE和RLIKE的**Source**和**Pattern**参数均仅接受STRING类型。 其他类型不允许参与运算，也不能进行到STRING类型的隐式类型转换。 如果**Source**或**Pattern**为NULL，则返回NULL。

**IN的使用方式**

```
key IN (value1, value2,…);
```

IN的隐式转换规则如下： IN右侧的**Value**值列表中的数据类型必须一致。 当**Key**与**Values**之间比较时，如果是BIGINT类型、DOUBLE类型以及STRING类型之间比较，统一转换为DOUBLE类型；如果是DATETIME类型和STRING类型之间比较，统一转换为DATETIME类型。 除此之外不允许其他类型之间的转换。

**说明**

IN如果参数过多，会造成编译时的压力，在5000个参数时，Gcc编译会占用到17GB的内存。因此建议限制到1024个参数，此时，内存峰值占用1GB，编译时间39秒。

**算术运算符作用下的隐式转换**

算术运算符包括：加（+）、减（-）、乘（*）、除（/）以及百分比（%），其隐式转换规则如下所示： 只有STRING类型、BIGINT类型、DECIMAL类型以及DOUBLE类型才能参与算术运算。 STRING在参与运算前会进行隐式类型转换到DOUBLE类型。 BIGINT类型和DOUBLE类型共同参与计算时，会将BIGINT隐式转换为DOUBLE类型。 日期型和布尔型不允许参与算术运算。

**说明**

**逻辑运算符作用下的隐式转换**

大数据计算服务逻辑运算符包括：AND、OR和NOT，其隐式转换规则如下所示： 只有BOOLEAN类型才能参与逻辑运算。 其他类型不允许参与逻辑运算，也不允许其他类型的隐式类型转换。

**说明**

##### SQL内建函数

MaxCompute SQL提供了大量的系统函数，方便您对任意行的一列或多列进行计算，输出任意种类的数据类型。

**转换规则说明**

在调用函数时，如果输入参数的数据类型与函数定义的参数数据类型不一致，把输入参数的数据类型转换为函数定义的数据类型。 每个MaxCompute SQL内建函数对参数隐式类型转换的支持范围各不相同，详细信息请参见内建函数。

##### CASE WHEN

**转换规则说明**

如果返回类型只有BIGINT类型和DOUBLE类型，统一转换为DOUBLE类型。 如果返回类型中有STRING类型，统一转换为STRING类型；如果不能转换，则报错（如BOOLEAN类型）。 除此之外不允许其他类型之间的转换。

##### STRING类型与DATETIME类型之间的转换

MaxCompute支持STRING与DATETIME类型的相互转换。本文介绍转换时的格式规范、有效值域及注意事项。

**转换格式**

转换时使用的格式为**yyyy-mm-dd hh:mi:ss.ff3**。

**单位有效值域**

| 单位 | 字符串（忽略大小写） | 有效值域 |
|---|---|---|
| 年 | yyyy | 0001~9999 |
| 月 | mm | 01~12 |
| 日 | dd | 01~31 |

大数据计算服务

| 时 | hh | 00~23 |
|---|---|---|
| 分 | mi | 00~59 |
| 秒 | ss | 00~59 |
| 毫秒 | ff3 | 00~999 |

**注意事项**

各个单位的值域中，如果首位为0，不可省略，例如**2017-1-9 12:12:12**就是非法的DATETIME格式， 无法从STRING类型数据转换为DATETIME类型，必须写为**2017-01-09 12:12:12**。 只有符合上述格式描述的STRING类型才能够转换为DATETIME类型，例如**cast(“2017-12-31**
**02:34:34” as datetime)**将会把STRING类型的**2017-12-31 02:34:34**转换为DATETIME类型。
同理，DATETIME类型转换为STRING类型时，默认转换为**yyyy-mm-dd hh:mi:ss**的格式。类似于下面的转换尝试，将会失败导致异常。

```
CAST("2017/12/31 02/34/34" AS datetime); CAST("20171231023434" AS datetime); CAST("2017-12-31 2:34:34" AS datetime);
```

MaxCompute提供了TO_DATE函数，用以将不满足日期格式的STRING类型数据转换为DATETIME类型。

### 运算符

#### 关系操作符

| 操作符 | 说明 |
|---|---|
| A=B | 如果A或B为NULL，返回NULL；如果A等于B，返回TRUE，否则返回FALSE。 |
| A<>B | 如果A或B为NULL，返回NULL；如果A不等于B，返回TRUE，否则返回FALSE。 |
| A<B | 如果A或B为NULL，返回NULL；如果A小于B，返回TRUE，否则返回FALSE。 |
| A<=B | 如果A或B为NULL，返回NULL；如果A小于等于B，返回TRUE，否则返回FALSE。 |
| A>B | 如果A或B为NULL，返回NULL；如果A大于B，返回TRUE，否则返回FALSE。 |

大数据计算服务

| A>=B | 如果A或B为NULL，返回NULL；如果A大于等于B，返回TRUE，否则返回FALSE。 |
|---|---|
| A IS NULL | 如果A为NULL，返回TRUE，否则返回FALSE。 |
| A IS NOT NULL | 如果A不为NULL，返回TRUE，否则返回FALSE。 |
| A LIKE B | 如果A或B为NULL，返回NULL；A为字符串，B为要匹配的模式，如果匹配成功，返回TRUE， 否则返回FALSE。百分号（%）匹配任意多个字符，下划线（ ）匹配单个字符，要匹配百分号 _ （%）或下划线（ ）需要用转义符表示：反斜线百分号（\%），反斜线下划线（\ ）。 _ _ 'aaa' LIKE 'a' = FALSE 'aaa' LIKE 'a%' = TRUE 'aaa' LIKE 'aab' = FALSE 'a%b' LIKE 'a\%b' = TRUE 'axb' LIKE 'a\%b' = FALSE |
| A RLIKE B | 如果A或B为NULL，返回NULL；A是字符串，B是字符串常量正则表达式，如果匹配成功，返回 TRUE，否则返回FALSE；如果B为空串会报错退出。 |
| A IN B | B是一个集合，如果A为NULL，返回NULL，如果A在B中则返回TRUE，否则返回FALSE；如果B 仅有一个元素NULL，即A IN （NULL），则返回NULL；如果B含有NULL元素，将NULL视为B 集合中其他元素的类型。B必须是常数并且至少有一项，所有类型要一致。 |

**注意事项**

由于DOUBLE值存在一定的精度差，因此，不建议直接使用等号对两个DOUBLE类型数据进行比较。您可以使用两个DOUBLE类型相减，而后取绝对值的方式判断。当绝对值足够小时，认为两个DOUBLE数值相等，示例如下。

```
ABS(0.9999999999 - 1.0000000000) < 0.000000001
```

`-- 0.9999999999`和`1.0000000000`为`10`位精度，而`0.000000001`为9位精度。 `--` 此时可以认为`0.9999999999`和`1.0000000000`相等。

**说明**

ABS是MaxCompute提供的内建函数，意为取绝对值，详细信息请参见ABS。 通常情况下，MaxCompute的DOUBLE类型能够保障16位有效数字。

#### 算术操作符

| 操作符 | 说明 |
|---|---|

大数据计算服务

| A + B | 如果A或B为NULL，返回NULL；否则返回A + B的结果。 |
|---|---|
| A – B | 如果A或B为NULL，返回NULL；否则返回A – B的结果。 |
| A * B | 如果A或B为NULL，返回NULL；否则返回A * B的结果。 |
| A / B | 如果A为NULL、B为NULL或 0 ，返回NULL；否则返回A / B的结果。 说明如果A和B为BIGINT类型，结果为DOUBLE类型。 |
| A % B | 如果A或B为NULL，返回NULL；否则返回A % B的结果。 |
| +A | 仍然返回A。 |
| -A | 如果A为NULL，返回NULL；否则返回-A。 |

**说明**

只有STRING类型、BIGINT类型、DOUBLE类型以及DECIMAL类型才能参与算术运算，日期型和布尔型不允许参与运算。 STRING类型在参与运算前会隐式类型转换为DOUBLE类型。 BIGINT类型和DOUBLE类型共同参与运算时，会将BIGINT类型隐式类型转换为DOUBLE类型再进行运算，返回结果为DOUBLE类型。 A和B都是BIGINT类型，进行A / B运算，返回结果为DOUBLE类型，进行上述其他运算仍然返回BIGINT类型。

#### 位运算操作符

| 操作符 | 说明 |
|---|---|
| A & B | 返回A与B进行按位与的结果。例如1&2返回0、1&3返回1。NULL与任何值按位与都为NULL。A和B必须为BIGINT类型。 |
| A \| B | 返回A与B进行按位或的结果。例如1 \| 2返回3、1 \| 3返回3，NULL与任何值按位或都为NULL。A和B必须为BIGINT类型。 |

大数据计算服务

**重要**

位运算符只允许BIGINT类型参与运算，不支持隐式类型转换。

#### 逻辑操作符

本文介绍MaxCompute SQL中 `AND` 、 `OR` 、 `NOT` 三种逻辑操作符的运算规则与类型约束。

**运算规则**

| 操作符 | 说明 |
|---|---|
| A and B | TRUE and TRUE = TRUE |
|  | TRUE and FALSE = FALSE |
|  | FALSE and TRUE = FALSE |
|  | FALSE and NULL = FALSE |
|  | FALSE and FALSE = FALSE |
|  | NULL and FALSE = FALSE |
|  | TRUE and NULL = NULL |
|  | NULL and TRUE = NULL |
|  | NULL and NULL = NULL |
| A or B | TRUE or TRUE = TRUE |
|  | TRUE or FALSE = TRUE |
|  | FALSE or TRUE = TRUE |
|  | FALSE or NULL = NULL |
|  | NULL or FALSE = NULL |

大数据计算服务

|  | TRUE or NULL = TRUE |
|---|---|
|  | NULL or TRUE = TRUE |
|  | NULL or NULL = NULL |
| NOT A | 如果A是NULL，返回NULL。 |
|  | 如果A是TRUE，返回FALSE。 |
|  | 如果A是FALSE，返回TRUE。 |

**说明**

### LOAD语句

本章节为您介绍如何通过LOAD命令将外部存储（例如OSS）数据导入表或表分区。

**注意事项**

使用外部存储数据前，请您对MaxCompute进行授权。LOAD命令的授权沿用了MaxCompute外部表的授权模式，授权方式有如下两种： 使用LOAD命令时，在数据路径中直接指定AccessKey ID和AccessKey Secret。以OSS为例，指定方式如下。

```
'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhouzmf.aliyuncs.com/my_bucket_id/my_location/'
```

**重要**

此方式会在授权时明文显示AccessKey ID和AccessKey Secret，存在一定安全隐患，不建议您使用。 通过STS模式授权。 OSS的STS模式授权请参见OSS的STS模式授权。 命令格式如下。

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [STORED BY StorageHandler] [WITH SERDEPROPERTIES (Options)];
```

大数据计算服务参数说明：
**table_name**：需要插入数据的目标表名称，目标表需要提前创建，目标表的Schema需要和外部数据
格式一致。
**LOAD INTO**：直接向表或分区中追加数据。
**LOAD OWERWRITE**：先清空表中的原有数据，再向表或分区中插入数据。
**SORTED BY**：指定StorageHandler名称。使用方法和MaxCompute外部表一致。
**LOCATION**：指定需要读取数据的OSS目录，系统会默认读取该目录下所有的文件。
**WITH SERDEPROPERTIES**：指定外部表相关参数，SERDEPROPERTIES支持的属性和
MaxCompute外部表一致。 假设vehicle.csv文件的数据如下。

```
1,1,51,1,46.81006,-92.08174,9/14/2014 0:00,S 1,2,13,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,3,48,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,4,30,1,46.81006,-92.08174,9/14/2014 0:00,W 1,5,47,1,46.81006,-92.08174,9/14/2014 0:00,S 1,6,9,1,46.81006,-92.08174,9/14/2014 0:00,S 1,7,53,1,46.81006,-92.08174,9/14/2014 0:00,N 1,8,63,1,46.81006,-92.08174,9/14/2014 0:00,SW 1,9,4,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,10,31,1,46.81006,-92.08174,9/14/2014 0:00,N
```

示例如下。

```
oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/
```

`--`将`vehicle.csv`文件保存至`OSS Bucket`目录下，并获取`OSS`表目录的组织方式。

```
vehicleId INT, recordId INT, patientId INT, calls INT, locationLatitute DOUBLE, locationLongtitue DOUBLE, recordTime STRING, direction STRING );
```

`--` 创建目标表`ambulance_data_csv_load`。

```
FROM LOCATION 'oss://oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/' STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES ( 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole', -- AliyunODPSDefaultRole的ARN信息 'odps.text.option.delimiter'=',' );
```

`--` 将`OSS`上的`CSV`文件导入目标表。 大数据计算服务

**导入开源格式数据**

命令格式如下。

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [ROW FORMAT SERDE '<serde class>'
  [WITH SERDEPROPERTIES ('odps.properties.rolearn'='${roleran}'
[,'name2'='value2',...])]
```

]

```
STORED AS <file format>;
```

参数说明：
**table_name**：需要插入数据的目标表名称，目标表需要提前创建，Schema需要和外部数据格式一
致。
**LOAD INTO**：直接向表或分区中追加数据。
**LOAD OWERWRITE**：先清空表中的原有数据，再向表或分区中插入数据。
**STORED AS**：指定文件格式，例如ORC、PARQUET、RCFILE、SEQUENCEFILE和TEXTFILE。使用
方法和MaxCompute外部表一致。
**ROW FORMAT SERDE**：非必选选项。使用方法和MaxCompute外部表一致。不同文件格式对应的
默认Serde Class如下： SEQUENCEFILE：org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe TEXTFILE：org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe RCFILE：org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe ORC：org.apache.hadoop.hive.ql.io.orc.OrcSerde ORCFILE：org.apache.hadoop.hive.ql.io.orc.OrcSerde PARQUET：org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe AVRO：org.apache.hadoop.hive.serde2.avro.AvroSerDe
**SERDEPROPERTIES**：当MaxCompute使用STS模式授权时，通过该参数指
定**odps.properties.rolearn**的属性值，属性值为RAM中**AliyunODPSDefaultRole**的ARN信息。 当MaxCompute和OSS的Owner是同一个账号时，可以一键授权。 示例如下。 大数据计算服务

```
oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/ds=20200910/'
```

`-- OSS`表目录的组织方式如上。外部路径的数据中不包含分区列，分区列信息为路径的一部分。

```
vehicleId STRING, recordId STRING, patientId STRING, calls STRING, locationLatitute STRING, locationLongtitue STRING, recordTime STRING, direction STRING) PARTITIONED BY (ds STRING);
```

`--` 创建目标表`ambulance_data_csv_load_pt`。

```
LOAD OVERWRITE TABLE ambulance_data_csv_load_pt PARTITION(ds='20200910') FROM LOCATION 'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhouzmf.aliyuncs.com/bucket/data_location/' ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' STORED AS TEXTFILE;
```

`--` 将`OSS`上的开源数据导入目标表。

**说明**

将数据下载到分区表，外部路径下数据的Schema不包含分区列。上述示例中，外部路径数据只包含业务字段，不包含分区列。

### DDL语句

#### 表操作

##### 创建表

命令格式如下。 大数据计算服务

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name [(col_name data_type [DEFAULT value] [COMMENT col_comment], ...)] [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] [CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [A SC | DESC] [, col_name [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] -- 用于创建聚
```

簇表时设置表的`Shuffle`和`Sort`属性。 `[STORED BY StorageHandler] --` 仅限外部表。

```
[WITH SERDEPROPERTIES (Options)] -- 仅限外部表。
```

`[LOCATION OSSLocation] --` 仅限外部表。 `[STORED AS AliOrc] --` 指定表底层存储文件格式，目前仅限创建新内部表可使用。 `[TBLPROPERTIES("compressionstrategy"="normal/high/extreme",--` 指定表数据存储压缩策略。 `"transactional"="true")] --` 指定为`Transactional`表，后续可以使用`Update/Delete` 语句操作该表。

```
[LIFECYCLE days]; [AS select_statement | LIKE existing_table_name];
```

参数说明：
**table_name**和**col_name**：表名与列名，均对大小写不敏感。不能有特殊字符，只能包含a~z、
A~Z、数字和下划线（_），且建议以字母开头，名称的长度不超过128字节。单表的列个数最多为1200 列。
**data_type**：数据类型，包含BIGINT、DOUBLE、BOOLEAN、DATETIME、DECIMAL、STRING、

**说明**

如果要使用新数据类型（TINYINT、SMALLINT、INT、FLOAT、VARCHAR、TIMESTAMP及 BINARY），您需执行如下命令打开新数据类型开关： Session级别：需要在SQL语句前增加 set odps.sql.type.system.odps2=true; 语句， 并与SQL语句一起提交执行。 Project级别：支持在Project级别打开新数据类型。项目所有者可根据需要对Project进行设置。

```
setproject odps.sql.type.system.odps2=true;
```

**DEFAULT value**：指定列的默认值，当INSERT操作不指定该列时，该列写入默认值。
**COMMENT table_comment**：注释内容，是长度不超过1024字节的有效字符串。
**PARTITIONED BY (col_name data_type [COMMENT col_comment], …)** ：指定表的分区
字段，支持TINYINT、SMALLINT、INT、BIGINT、VARCHAR和STRING类型。 分区值不允许有双字节字符（例如中文），必须是以字母开头，包含字母、数字或字符，长度不超过128 字节。允许的字符包括：空格、英文冒号（:）、下划线（_）、美元符（$）、井号（#）、点（.），感叹号（!）和at（@），其他字符行为未定义，例如（\t）、（\n）、（/）等。当利用分区字段对表进行分区时，新增分区、更新分区内数据和读取分区数据均不需要做全表扫描，可以提高处理效率。

**说明**

一张表最多允许60000个分区，单表的分区层次不能超过6级。 大数据计算服务

**CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, …]) [SORTED BY**

**(col_name [ASC | DESC] [, col_name [ASC | DESC] …])] INTO number_of_buckets**

**BUCKETS**：用于创建聚簇表时设置表的Shuffle和Sort属性。聚簇表分为Hash聚簇表和Range聚簇表
两种： Hash聚簇表。
**CLUSTERED BY**：指定Hash Key。MaxCompute将对指定列进行Hash运算，按照Hash值分散
到各个Bucket中。为避免数据倾斜和热点，取得较好的并行执行效果，**CLUSTERED BY**列适宜选择取值范围大，重复键值少的列。此外，为了达到JOIN优化的目的，也应该考虑选取常用的 Join/Aggregation Key，即类似于传统数据库中的主键。
**SORTED BY**：指定Bucket内字段的排序方式。建议**SORTED BY**和**CLUSTERED BY**保持一
致，以取得较好的性能。此外，当指定**SORTED BY**子句后，MaxCompute将自动生成索引，并且在查询时利用索引来加快执行。
**INTO number_of_buckets BUCKETS**：指定哈希桶的数量。该值必须填写，且由数据量大小
决定。此外，MaxCompute默认支持最多1111个Reducer，所以此处最多也只支持1111个哈希桶。您可以使用 set odps.sql.reducer.instances=xxx; 来提升这个限制，但最大不超过 4000，否则会影响性能。

**说明**

选择哈希桶数目时，请您遵循以下两个原则： 哈希桶大小适中：经验值是每个Bucket的大小在500 MB左右比较合理。例如分区大小估计为500 GB，初略估算Bucket数目应该设为1000，这样平均每个Bucket大小约为 500 MB。对于特别大的表，500 MB的限制可以突破，每个Bucket在2 GB~3 GB左右比较合适。同时，可以结合 set odps.sql.reducer.instances=xxx; 来突破1111个桶的限制。 对于JOIN优化的场景，去除Shuffle和Sort步骤能显著提升性能。因此要求两个表的哈希桶数目成倍数关系，例如256和512。建议哈希桶的数目统一使用2n，例如512、 1024、2048或4096，这样系统可以自动进行哈希桶的分裂和合并，也可以去除 Shuffle和Sort的步骤，提升执行效率。 Range聚簇表。
**RANGE CLUSTERED BY**：指定范围聚簇列。MaxCompute将对指定列进行分桶运算，按照分
桶编号分散到各个Bucket中。
**SORTED BY**：指定Bucket内字段的排序方式，使用方法与Hash聚簇表相同。
**INTO number_of_buckets BUCKETS**：指定哈希桶的数量。Range聚簇表的Bucket桶数不像
Hash聚簇表那样有2n的最佳实践，在数据量分布合理的情况下，任何桶数都可以。但是Range聚簇表的Bucket数不是必须的，可以省略，此时系统会根据数据量自动决定最佳的Bucket数目。

**说明**

当Join和Aggregate的对象是Range聚簇表，且Join Key或Group Key是Range Clustering Key或其前缀时，可以通过控制Flag消除数据的重分布，即Shuffle Remove，提升执行效率。您

```
可以通过 set odps.optimizer.enable.range.partial.repartitioning=true/false; 进行
```

设置，默认关闭。
**STORED AS**：指定表文件存储格式，现有默认是CFile2格式。目前新增AliOrc文件格式，是
MaxCompute存储团队用C++语言开发的，与开源ORC标准完全兼容高效存储文件格式。较之CFile2， 使用AliORC文件格式可以在存储空间上节省10%以上，而读取时间的性能也能提升20%以上。
**LIFECYCLE**：表的生命周期，单位为天。**CREATE TABLE LIKE**语句不会复制源表的生命周期属性。
大数据计算服务

**CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE**

通过 CREATE TABLE…AS select_statement… 语句再创建一个表，并在建表的同时将数据复制到新表中，但通过 CREATE TABLE…AS select_statement… 语句创建的表不会复制分区属性，只会把源表的分区列作为目标表的一般列处理。 通过 CREATE TABLE…LIKE existing_table_name 语句再创建一个表，可以使目标表和源表具有相同的表结构，但不复制数据，也不会复制源表的生命周期属性。 外部表相关子句：
**STORED BY StorageHandler**：按照外表数据格式指定StorageHandler。
**WITH SERDEPROPERTIES (Options)**：外表的授权、压缩及字符解析等相关参数。
**LOCATION OSSLocation**：外部数据OSS的存储位置。
**TBLPROPERTIE("compressionstrategy"="xxx")**：Transactional表的属性，Lifecycle和
Comment等属性也可以放在此处表达。其中**compressionstrategy**是指数据存储压缩策略，取值范围是normal、high和extreme。**compressionstrategy**必须为全小写，normal、high和extreme 大小写都可以。该属性仅作用于MaxCompute内部表。 默认压缩策略：非归档数据默认为normal，归档数据默认为high。 各压缩策略的定义： normal：默认zstd level 1。 high：默认zstd level 4。 extreme：默认zstd level 9。 也可以对Project级别进行压缩策略的指定，需要Owner在Project管理的公共属性中设置，关键字**odps.storage.compression.strategy**。设置此项后，所有的生成的非归档数据都将采用此策略，且不影响归档策略。
**TBLPROPERTIES("transactional"="true")**：创建Transactional表，后续可以使用

**说明**

在创建表时，如果不指定**IF NOT EXISTS**且存在同名表，则返回报错；如果指定**IF NOT EXISTS**， 则无论是否存在同名表，即使原表结构与要创建的目标表结构不一致，均返回成功，已存在的同名表的元信息不会被改动。

**创建分区表示例**

假设创建表sale_detail来保存销售记录，该表使用销售时间**sale_date**和销售区域**region**作为分区列，建表语句如下所示。

```
( shop_name STRING, customer_id STRING, total_price DOUBLE
```

)

```
PARTITIONED BY (sale_date STRING,region STRING);
```

`--` 创建一张分区表`sale_detail`。 大数据计算服务通过 `CREATE TABLE...AS select_statement...` 语句再创建一个表，并在建表的同时将数据复制到新表中，示例如下。

```
SELECT * FROM sale_detail;
```

此时，如果表sale_detail中存在数据，上述语句会将表sale_detail的数据全部复制到表 sale_detail_ctas1。

**说明**

此处sale_detail是一张分区表，而通过 `CREATE TABLE...AS select_statement...` 语句创建的表 sale_detail_ctas1不会复制分区属性，只会把源表的分区列作为目标表的一般列处理。即 sale_detail_ctas1是一个含有5列的非分区表。 在 `CREATE TABLE...AS select_statement...` 语句中，如果在SELECT子句中使用常量作为列的值，建议您指定列的名字，示例如下。 `AS`

```
SELECT shop_name, customer_id, total_price, '2013' AS sale_date, 'China' AS region FROM sale_detail;
```

如果不加列的别名，示例如下。 `AS`

```
SELECT shop_name, customer_id, total_price, '2013', 'China' FROM sale_detail;
```

如果希望源表和目标表具有相同的表结构，可以尝试使用 `CREATE TABLE...LIKE...` 语句，示例如下。

```
CREATE TABLE sale_detail_like LIKE sale_detail;
```

此时，sale_detail_like的表结构与sale_detail完全相同。除生命周期属性外，列名、列注释以及表注释等均相同。但sale_detail中的数据不会被复制到sale_detail_like表中。

**创建聚簇表**

```
CREATE TABLE T1 (a STRING, b STRING, c BIGINT) CLUSTERED BY (c) SORTED by (c) INTO 1024
```

BUCKETS; --创建`Hash`聚簇非分区表。

```
CREATE TABLE T1 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY
```

(c) SORTED by (c) INTO 1024 BUCKETS; --创建`Hash`聚簇分区表。 创建Range聚簇表的示例如下。 大数据计算服务

```
CREATE TABLE T2 (a STRING, b STRING, c BIGINT) RANGE CLUSTERED BY (c) SORTED by (c) INT
```

O 1024 BUCKETS; --创建`Range`聚簇非分区表。

```
CREATE TABLE T2 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY
```

(c) SORTED by (c) ; --创建`Range`聚簇分区表，可以不指定`BUCKETS`数。

**创建Transactional表**

`--`创建`Transactional`表。

```
create table txn_table(id bigint) tblproperties("transactional"="true");
```

`--`创建带分区的`Transactional`表。

```
create table if not exists txn_table_pt(id bigint) partitioned by(ds string) tblproperties ("transactional"="true");
```

**查看表信息**

MaxCompute支持通过DESC语句查看表信息。

```
DESC <table_name>;
```

`--` 查看表信息

```
DESC EXTENDED <table_name>;
```

`--` 查看外部表信息。 `--` 该命令还可以查看表是否是`Transactional`表，此功能需要`Odpscmd`升级到`0.35.0`版本。

**查看建表语句**

```
SHOW CREATE TABLE <table_name>;
```

**说明**

##### 删除表

**操作说明**

###### 使用说明

删除无需使用的表。

**函数语法**

```
DROP TABLE [IF EXISTS] table_name;
```

**说明**

如果不指定**IF EXISTS**且表不存在，则返回异常；如果指定此参数，无论表是否存在，均返回成功。

**参数说明**

大数据计算服务

##### 使用示例

```
CREATE TABLE sale_detail_drop LIKE sale_detail;
```

`--` 如果表存在，返回成功；如果不存在，返回异常。

```
DROP TABLE sale_detail_drop;
```

`--` 无论是否存在`sale_detail_drop2`表，均返回成功。

```
DROP TABLE IF EXISTS sale_detail_drop2;
```

##### 重命名表

**操作说明**

###### 使用说明

使用当前函数可对表名进行重命名操作。

**函数语法**

```
ALTER TABLE table_name RENAME TO new_table_name;
```

**说明**

**RENAME**操作仅修改表的名字，不改动表中的数据。

**参数说明**

##### 使用示例

`--`创建示例所需操作的表

```
CREATE TABLE sale_detail_rename1 LIKE sale_detail;
```

`--`修改表名称

```
ALTER TABLE sale_detail_rename1 RENAME TO sale_detail_rename2;
```

`--`查看修改后的表是否存在

```
SHOW TABLES;
```

##### 修改表的Owner

MaxCompute SQL支持通过 `CHANGEOWNER` 命令来修改表的拥有人（表Owner）。 命令格式如下。 大数据计算服务

```
ALTER TABLE table_name CHANGEOWNER TO 'ALIYUN$xxx@aliyun.com';
```

##### 修改表的注释

命令格式如下。

```
ALTER TABLE table_name SET COMMENT 'tbl comment';
```

**说明**

**COMMENT**最长为1024字节。
示例如下。

```
ALTER TABLE sale_detail SET COMMENT 'new coments for table sale_detail';
```

通过MaxCompute的DESC命令，可以查看表中COMMENT的修改结果。

##### 修改表的生命周期属性

MaxCompute提供数据生命周期管理功能，方便您释放存储空间，简化回收数据的流程。本章节为您介绍命令格式如下。

```
ALTER TABLE table_name SET lifecycle days;
```

**说明**

**days**为生命周期时间，只接受正整数，单位为天。
您可以在创建表的时候指定生命周期，生命周期只能在表级别设置，不能在分区级别设置。分区表设置生命周期后，生命周期也会在分区级别生效。 在MaxCompute中，每当表的数据被修改后，表的**LastDataModifiedTime**将会被更新。 因此，MaxCompute会根据每张表的**LastDataModifiedTime**以及生命周期的设置来判断是否要回收此表。 如果表是非分区表，自最后一次数据被修改开始计算，经过**days**天后数据仍未被改动，则此表如果表是分区表，则根据各分区的**LastDataModifiedTime**判断该分区是否该被回收。不同于非分区表，分区表的最后一个分区被回收后，该表不会被删除。 非分区表不支持取消生命周期，只能修改生命周期。分区表可以取消某个具体分区的生命周期。 示例如下。

```
create table test_lifecycle(key string) lifecycle 100;
```

`--` 新建`test_lifecycle`表，生命周期为`100`天。

```
alter table test_lifecycle set lifecycle 50;
```

`--` 修改`test_lifecycle`表，将生命周期设为`50`天。 大数据计算服务

##### 禁止和恢复生命周期

在某些情况下，有些特定的分区可能不希望被生命周期功能自动回收掉。此时，可以禁止该分区被生命周期命令格式如下。

```
ALTER TABLE table_name partition[partition_spec] ENABLE|DISABLE LIFECYCLE;
```

**说明**

**DISABLE LIFECYCLE**：禁止表和分区的生命周期功能。
禁止表本身及其所有分区被生命周期回收，优先级高于恢复表分区生命周期功能。即当使用**table disable lifecycle**时，**partition_spec enable lifecycle**设置无效。 禁止表的生命周期功能后，表的生命周期配置及其分区的ENABLE和DISABLE标记会被保留。 禁止表生命周期功能后，仍然可以修改表及分区的生命周期配置。
**ENABLE LIFECYCLE**：撤销对表和分区生命周期的禁止，恢复表和分区生命周期功能。
表及其分区重新参与生命周期回收，默认使用当前表及分区上的生命周期配置。 开启表生命周期前可以修改表及分区的生命周期配置，防止开启表生命周期后因使用之前的配置导致数据被误回收。 示例如下。

```
ALTER TABLE trans DISABLE LIFECYCLE;
```

`--` 禁止表`trans`的生命周期功能。

```
ALTER TABLE trans PARTITION(dt='20141111') DISABLE LIFECYCLE;
```

`--` 禁止表`trans`中时间为`20141111`分区生命周期功能。

```
ALTER TABLE trans ENABLE LIFECYCLE;
```

`--` 恢复表`trans`的生命周期功能。

```
ALTER TABLE trans PARTITION(dt='20141111') ENABLE LIFECYCLE;
```

`--` 恢复表`trans`中时间为`20141111`分区生命周期功能。

##### 修改表的修改时间

MaxCompute SQL提供TOUCH操作，用来修改表的**LastDataModifiedTime**。效果是会将表的**LastDataModifiedTime**修改为当前时间。本章节为您介绍如何使用DDL语句完成修改表的修改时间操作。 命令格式如下。

```
ALTER TABLE table_name TOUCH;
```

**说明**

此操作会改变表的**LastDataModifiedTime**的值。此时，MaxCompute会认为数据有变动，生命周期的计算会重新开始。

##### 修改表的聚簇属性

大数据计算服务对于分区表，MaxCompute支持通过 `ALTER TABLE` 命令增加或去除聚簇属性。

**说明**

通过 `ALTER TABLE` 改变聚集属性，只对于分区表有效，非分区表一旦建立聚集属性就无法改变。 `ALTER TABLE` 命令适用于存量表，在增加了新的聚集属性之后，新的分区将按设置的聚簇属性存储。 `ALTER TABLE` 只会影响分区表的新建分区（包括INSERT OVERWRITE生成的），新分区将按新的聚集属性存储，老的数据分区聚簇属性和存储保持不变。即在一张曾经做过聚簇属性设置的表上，关闭了聚簇属性，再增加聚簇设置，可以在新分区设置不同于之前的聚簇列、排序列及分桶数。

**增加表的Hash聚簇属性**

命令格式如下。

```
[CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_nam e [ASC | DESC] ...])] INTO number_of_buckets BUCKETS]
```

**去除表的Hash聚簇属性**

命令格式如下。

```
ALTER TABLE table_name NOT CLUSTERED;
```

**增加表的Range聚簇属性**

其中，Bucket数不是必须的，可以省略，此时系统会根据数据量自动决定最佳的Bucket数目。 命令格式如下。

```
[RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, c ol_name [ASC | DESC] ...])] INTO number_of_buckets BUCKETS]
```

**去除表或分区的Range聚簇属性**

命令格式如下。

```
ALTER TABLE table_name NOT CLUSTERED; ALTER TABLE table_name partition_spec NOT CLUSTERED;
```

##### 清空非分区表里的数据

命令格式如下。

```
TRUNCATE TABLE table_name;
```

大数据计算服务作用是将指定的非分区表中的数据清空。该命令不支持分区表，对于分区表，可以

**说明**

用 `ALTER TABLE table_name DROP PARTITION`（`partition_spec`）的方式将分区里的数据清除。

##### 归档表的数据

如果Project里的空间比较紧张，需要进行数据删除或数据压缩，可以考虑MaxCompute里对表的Archive 功能，效果是可以将存储空间压缩50%左右。Archive功能将数据存为Raid File，数据不再简单的存三份， 而是6份数据+3份校验块的方式，这样有效的将存储比从1:3提高到1:1.5，可以节省一半的物理空间，同时也采用了更高压缩比的压缩算法。 上述的操作也是有代价的，如果某个数据块损坏或某台机器损坏，恢复数据块的时间要比原来的方式更长， 读的性能也会有一定损失。所以现在这种功能可以用在一些冷数据的压缩存储上，例如一些非常大的日志数据，超过一定时间期限后使用的频率非常低，但是又需要长期保存，则可以考虑用Raid File来存储。 命令格式如下。

```
ALTER TABLE [table_name] <PARTITION(partition_name='partition_value')> ARCHIVE;
```

**说明**

如果**partition_name**不存在，则会报错。 示例如下。

```
alter table my_log partition(ds='20170101') archive;
```

输出信息如下。

```
Summary: table name: test0128 /pt=a instance count: 1 run time: 21 before merge, file count: 1 file size: 456 file physical size: 1368 after merge, file count: 1 file size: 512 file physical size: 768
```

**说明**

从输出信息中可以看到，在Archive前后的Logical和Physical Size的变化情况，并且在这个过程中会将多个小文件自动的合并。在Archive后，可以用 `desc extended` 命令检查该分区是否Archive以及查看物理空间占用情况。

```
desc extended my_log partition(ds='20170101');
```

`--`返回结果如下。

```
+------------------------------------------------------------------------------------ PartitionSize: 512 | +------------------------------------------------------------------------------------ CreateTime: 2017-01-28 07:05:20 | LastDDLTime: 2017-01-28 07:05:20 | LastModifiedTime: 2017-01-28 07:05:21 | +------------------------------------------------------------------------------------
```

大数据计算服务

##### 强制删除表或分区数据

如果您需要强制删除表数据或者分区数据，并确定该删除操作不需要恢复，需要即时的释放存储空间，可以在执行删除操作时加上Purge选项。 命令格式如下。

```
DROP TABLE tblname PURGE; ALTER TABLE tblname DROP PARTITION(part_spec) PURGE;
```

示例如下。

```
drop table my_log purge; alter table my_log drop partition (ds='20170618') purge;
```

#### 视图操作

##### 创建视图

命令格式如下。

```
CREATE [OR REPLACE] VIEW [IF NOT EXISTS] view_name [(col_name [COMMENT col_comment], ...)] [COMMENT view_comment] [AS select_statement];
```

**说明**

创建视图时，您必须有对视图所引用表的读权限。 视图可以引用其他视图，但不能引用自己，也不能循环引用。 不可以向视图写入数据。例如使用 `insert into` 或 `insert overwrite` 操作视图。 创建好视图后，如果视图的引用表发生了变更，有可能导致视图无法访问，例如删除被引用表。 您需要自行维护引用表及视图之间的对应关系。 如果没有指定**if not exists**，在视图已经存在时用 `create view` 会导致异常。这种情况可以用 `create or replace view` 来重建视图，重建后视图本身的权限保持不变。 示例如下。

```
create view if not exists sale_detail_view (store_name, customer_id, price, sale_date, region) as select * from sale_detail;
```

`--` 创建视图`sale_detail_view`。

##### 删除视图

大数据计算服务命令格式如下。

```
DROP VIEW [IF EXISTS] view_name;
```

如果视图不存在且没有指定**IF EXISTS**，则会报错。

**说明**

示例如下。

```
DROP VIEW IF EXISTS sale_detail_view;
```

##### 重命名视图

命令格式如下。

```
ALTER VIEW view_name RENAME TO new_view_name;
```

如果已存在同名视图，则会报错。

**说明**

示例如下。

```
alter view sale_detail_view rename to market;
```

#### 物化视图操作

物化视图（Materialized View）是一种预先计算的方式，通过保存某些耗时操作（例如JOIN、 AGGREGATE）的结果，以便在查询时直接复用，从而避免重复执行这些耗时操作，最终实现加速查询的目的。

##### 背景信息

视图是一种虚拟表，任何对视图的查询，都会转换为视图SQL语句的查询。而物化视图是一种特殊的物理表，物化视图会存储实际的数据，占用存储资源。 物化视图适用于如下场景： 模式固定、且执行频次高的查询。 查询包含非常耗时的操作，比如聚合、连接操作等。 查询仅涉及表中的很小部分数据。 物化视图与传统查询的对比如下。

| 对比项 | 传统查询方式 | 物化视图查询方式 |
|---|---|---|

大数据计算服务

| 查询语句 | 直接使用SQL语句查询数据。 SELECT empid，deptname FROM emps JOIN depts ON emps.deptno=depts.dept no WHERE hire date >= _ '2018-01-01'; | 您需要创建物化视图，然后基于物化视图查询数据。 创建物化视图语句如下： CREATE MATERIALIZED VIEW mv AS SELECT empid，deptname, hire date _ FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2016-01-01'; _ 基于创建的物化视图查询数据： SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ 如果物化视图开启了查询改写功能，使用如下SQL语句查询数据时会直接从物化视图中查询数据： SELECT empid，deptname FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2018-01-01'; _ --相当于如下语句。 SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ |
|---|---|---|
| 查询特点 | 查询涉及读表、JOIN、过滤 （WHERE）操作。当源表数据量很大时，查询速度会很慢。操作复杂度较高，运行效率低。 | 查询涉及读表、过滤操作。不涉及JOIN操作。MaxCompute会自动匹配到最优物化视图，并直接从物化视图中读取数据，从而大大提高查询效率。 |

**操作命令**

| 类型 | 功能 | 角色 |
|---|---|---|
| 创建物化视图（支持分区和聚簇） | 基于查询语句创建物化视图。 | 具备项目创建表权限（CreateTable）的用户。 |
| 更新物化视图 | 更新已创建的物化视图。 | 具备修改表权限（Alter）的用户。 |
| 修改物化视图的生命周期 | 修改已创建的物化视图的生命周期。 | 具备修改表权限（Alter）的用户。 |
| 开启或禁用物化视图的生命周期 | 开启或禁用已创建的物化视图的生命周期。 | 具备修改表权限（Alter）的用户。 |

大数据计算服务

| 查询物化视图信息 | 查询物化视图的基本信息。 | 具备读取表元信息权限（Describe）的用户。 |
|---|---|---|
| 查询物化视图状态 | 查看物化视图有效或无效。 | 具备读取表元信息权限（Describe）的用户。 |
| 列出项目下物化视图 | 列出项目下所有的物化视图，或符合某些规则的物化视图。 | 具备项目查看对象列表权限（List）的用户。 |
| 删除物化视图 | 删除已创建的物化视图。 | 具备删除表权限（Drop）的用户。 |
| 删除物化视图分区 | 删除已创建的物化视图的分区。 | 具备删除表权限（Drop）的用户。 |
| 物化视图查询穿透 | 当查询的分区数据不存在时，需要自动实现到原始分区表查询数据。 | 具备项目写权限（Write）及创建表权限 （CreateTable）的用户。 |

##### 使用限制

不支持窗口函数、UDTF函数和非确定性函数（例如UDF、UDAF等）。

|  | 说明当您的业务场景必须要使用非确定性函数时，请在Session级别设置属性 set odps.sql.materialized.view.support.nondeterministic.function=true; 。 |  |
|---|---|---|
|  |  | set |
|  | odps.sql.materialized.view.support.nondeterministic.function=true; |  |

**创建物化视图（支持分区和聚簇）**

基于满足物化视图场景的数据创建物化视图，支持分区和聚簇场景。

##### 使用限制

物化视图的名称不允许和当前项目中的已有表、视图、物化视图名称重复。您可以通过 `SHOW` 不支持基于现有的物化视图创建新的物化视图。 不支持基于外部表创建物化视图。 注意事项当查询语句执行失败时，物化视图也会创建失败。 物化视图分区列必须来源于某张源表，其顺序和列数目必须和源表一样，列名称可以不一样。 列注释需要指定所有列，包含分区列。如果只指定部分列，会报错。 可以同时指定分区和聚簇，此时每个分区中的数据都有指定的聚簇属性。 当查询语句中包含不支持的算子时会报错。 MaxCompute默认不支持使用非确定性函数（例如UDF、UDAF等）创建物化视图。当您的业务场景必须要使用非确定性函数时，请在Session级别设置属性 `set`

```
odps.sql.materialized.view.support.nondeterministic.function=true; 。
```

物化视图支持生成空分区，原始表分区为空的时候，刷新物化视图，自动生成空分区。 命令格式大数据计算服务

```
CREATE MATERIALIZED VIEW [IF NOT EXISTS][project_name.]<mv_name>
```

`[LIFECYCLE <days>] --`指定生命周期 `[BUILD DEFERRED] --` 指定是在创建时只生成表结构，不生成数据

```
[(<col_name> [COMMENT <col_comment>],...)] --列注释
```

`[DISABLE REWRITE] --`指定是否用于改写 `[PARTITIONED BY (<col_name> [, <col_name>, ...]) --`创建物化视图表为分区表

```
[CLUSTERED BY|RANGE CLUSTERED BY (<col_name> [, <col_name>, ...]) [SORTED BY (<col_name> [ASC | DESC] [, <col_name> [ASC | DESC] ...])]
```

`INTO <number_of_buckets> BUCKETS] --`用于创建聚簇表时设置表的`Shuffle`和`Sort`属性

```
[TBLPROPERTIES("compressionstrategy"="normal/high/extreme", --指定表数据存储压缩策略
```

`"enable_auto_substitute"="true", --`指定当分区不存在时是否转化视图来查询 `"enable_auto_refresh"="true", --`指定是否开启自动刷新 `"only_refresh_max_pt"="true" --`针对分区物化视图，只自动刷新源表最新分区 `)]`

```
AS <select_statement>;
```

参数说明

| 参数 |  | 是否必填 | 说明 |  |  |  |
|---|---|---|---|---|---|---|
| IF NOT EXISTS |  | 否 | 如果没有指定IF NOT EXISTS且物化视图已经存在，会返回报错。 |  |  |  |
| project name _ |  | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在 MaxCompute项目。 |  |  |  |
| mv name _ |  | 是 | 新建物化视图的名称。 |  |  |  |
| days |  | 否 | 指定物化视图的生命周期，单位为天。取值范围为1~37231。 |  |  |  |
| BUILD DEFERRED |  | 否 | 如果加上这个关键字代表创建物化视图时，只生成表结构，不刷新数据。 |  |  |  |
| col name _ |  | 否 | 指定物化视图的列名称。 |  |  |  |
| col comment _ |  | 否 | 指定物化视图的列的注释。 |  |  |  |
| DISABLE REWRITE |  |  | 设置禁止通过物化视图执行查询改写操作。不指定时表示允许通过物化视图执行查询改写操作，您可以执行 ALTER MATERIALIZED VIEW [project name.]<mv name> DISABLE REWRITE; 命令禁止通过物化视图 _ _ 执行查询改写操作。同理您可以执行 ALTER MATERIALIZED VIEW [project name.]<mv name> ENABLE REWRITE; 命令允许通过物化视图 _ _ 执行查询改写操作。 |  |  |  |
|  |  |  |  | ALTER MATERIALIZED VIEW |  |  |
|  | DISABLE | 否 | [project name.]<mv name> DISABLE REWRITE; _ _ |  |  |  |
|  |  |  |  |  |  | 命令禁止通过物化视图 |
|  |  |  | 执行查询改写操作。同理您可以执行 |  |  |  |
|  |  |  | [project name.]<mv name> ENABLE REWRITE; _ _ |  |  |  |

大数据计算服务

| PARTITIONED BY | 否 | 指定物化视图分区字段，表示创建的物化视图表为分区表。 |
|---|---|---|
| CLUSTERED BY\|RANGE CLUSTERED BY | 否 | 用于创建聚簇表时设置表的Shuffle属性。 |
| SORTED BY | 否 | 用于创建聚簇表时设置表的Sort属性。 |
| REFRESH EVERY | 否 | 用于设置物化视图定时更新间隔。单位可选择：分钟/小时/天。 |
| number of buck _ _ ets | 否 | 用于创建聚簇表时设置表分桶数。 |
| TBLPROPERTIES | 否 | compressionstrategy指定表数据的存储压缩策略，可以选normal、 high或extreme。enable auto substitute指定当分区不存在时是否自 _ _ 动穿透到原始分区表去查询数据。 enable auto refresh：可选，当需要自动刷新数据时需要设置 _ _ 为 true 。 refresh interval minutes：条件可选， _ _ 当 enable auto refresh 为 true 时，需要配置刷新间隔时间，单 _ _ 位为分钟。 only refresh max pt：可选，只适用于带分区的物化视图，但设置 _ _ _ 为 true 时，只会刷新源表最新分区。 |
| select statement _ | 是 | 查询语句，详细格式请参见SELECT操作。 |

##### 使用示例

示例一：创建物化视图。 创建和张表并插数据大数据计算服务 a. 创建 `mf_t` 和 `mf_t1` 两张表并插入数据。

```
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t ADD PARTITION (ds='1'); INSERT INTO mf_t PARTITION (ds='1') VALUES (1,10,'kyle'),(2,20,'xia'); SELECT * FROM mf_t WHERE ds ='1';
```

`--` 返回结果如下。

```
+------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 2          | 20         | xia        | 1          |
+------------+------------+------------+------------+
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t1 ADD PARTITION (ds='1'); INSERT INTO mf_t1 PARTITION (ds='1') VALUES (1,10,'kyle'),(3,20,'john'); SELECT * FROM mf_t1 WHERE ds ='1';
```

`--` 返回结果如下。

```
+------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 3          | 20         | john       | 1          |
+------------+------------+------------+------------+
```

大数据计算服务 b. 创建物化视图。 示例1：创建以ds为分区列的物化视图。

```
CREATE MATERIALIZED VIEW mf_mv LIFECYCLE 7 (
  key comment 'unique id',
  value comment 'input value',
  ds comment 'partitiion'
```

)

```
PARTITIONED BY (ds) AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
     FROM mf_t AS t1 JOIN mf_t1 AS t2
       ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

`--`查询物化视图

```
SELECT * FROM mf_mv WHERE ds =1; +------------+------------+------------+ +------------+------------+------------+
| 1          | 10         | 1          |
+------------+------------+------------+
```

示例2：创建带有聚簇属性的非分区物化视图。

```
CREATE MATERIALIZED VIEW mf_mv2 LIFECYCLE 7 CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

示例3：创建带有聚簇属性的分区物化视图。

```
CREATE MATERIALIZED VIEW mf_mv3 LIFECYCLE 7 PARTITIONED BY (ds) CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

大数据计算服务示例二：原始表分区为空的时候，刷新物化视图，自动生成空分区。

```
CREATE TABLE mf_blank_pts(id bigint ,name string) PARTITIONED BY (ds bigint); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 1); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 2); INSERT INTO TABLE mf_blank_pts PARTITION(ds=1) VALUES (1,"aba"),(2,"cbd"); CREATE MATERIALIZED VIEW IF NOT EXISTS mf_mv_blank_pts PARTITIONED BY (ds) AS SELECT id,name,ds FROM mf_blank_pts; ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>0); SHOW PARTITIONS mf_mv_blank_pts;
```

`--`原表分区`ds=2`是没有值，当刷新`ds>0`分区时，物化视图里有了空分区

```
ds=1 ds=2 SELECT * FROM mf_mv_blank_pts WHERE ds>0;
```

`--`返回只有分区1有值

```
+------------+------------+------------+
| id         | name       | ds         |
+------------+------------+------------+
| 1          | aba        | 1          |
| 2          | cbd        | 1          |
+------------+------------+------------+
```

**更新物化视图**

当物化视图的数据对应的表或分区产生插入、覆写、更新、删除等操作时，物化视图会自动失效，无法用于查询改写。您可以先查看物化视图状态，当物化视图失效时，执行更新操作。 注意事项物化视图的更新操作只会更新源表有数据变化的表或者分区。 命令格式

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name>
      REBUILD [PARTITION (<ds>=max_pt(<table_name>),<expression1>...)];
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| project na _ me | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv name _ | 是 | 待更新物化视图的名称。 |
| ds | 否 | 物化视图分区字段名称。 |

大数据计算服务

| max pt _ | 否 | 取指定表或者物化视图（table name）的最大分区值。 _ |
|---|---|---|
| expression | 否 | 当更新分区物化视图时，需要指定待更新分区信息，支持表达式。 |

##### 使用示例

示例一：更新非分区物化视图。 `--` 创建非分区表

```
CREATE TABLE count_test(a BIGINT, b BIGINT);
```

`--`创建非分区物化视图

```
CREATE MATERIALIZED VIEW count_mv LIFECYCLE 7 AS SELECT COUNT(*) FROM count_test;
```

`--`更新非分区物化视图

```
ALTER MATERIALIZED VIEW count_mv rebuild;
```

示例二：更新分区物化视图的某个分区。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds='1');
```

示例三：更新分区物化视图的满足指定条件的分区。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>='1', ds<='2');
```

示例四：更新分区物化视图的最新分区数据。 `--` 创建示例分区表

```
(shop_name STRING , customer_id STRING , total_price DOUBLE ) PARTITIONED BY (sale_date STRING ,region STRING ); ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='china'); INSERT INTO sale_detail_jt PARTITION (sale_date='2013',region='china') VALUES
    ('s1','c1',100.1),
    ('s2','c2',100.2),
    ('s3','c3',100.3);
ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='en'); INSERT INTO sale_detail_jt PARTITION (sale_date='2013',region='en') VALUES
    ('t1','c5',200.0),
    ('t2','c6',300.0);
```

`--`查看分区数据

```
SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='china'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| s1        | c1          | 100.1       | 2013      | china  |
| s2        | c2          | 100.2       | 2013      | china  |
| s5        | c2          | 100.2       | 2013      | china  |
+-----------+-------------+-------------+-----------+--------+
```

`--`查看分区数据大数据计算服务

```
SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='en'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| t1        | c5          | 200.0       | 2013      | en     |
| t2        | c6          | 300.0       | 2013      | en     |
+-----------+-------------+-------------+-----------+--------+
```

`--`创建物化视图

```
CREATE MATERIALIZED VIEW mv_deferred BUILD DEFERRED AS SELECT * FROM sale_detail_jt;
```

`--`查询物化视图 mv_deferred;

```
SELECT * FROM mv_deferred;
```

`--`返回

```
+-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+ +-----------+-------------+-------------+-----------+--------+
```

`--`创建分区表

```
CREATE TABLE mf_part (id bigint,name string) PARTITIONED BY (dt string);
```

`--`插入数据

```
INSERT INTO mf_part PARTITION(dt='2013') VALUES(1,'name1'),(2,'name2');
```

`--`查询数据

```
SELECT * FROM mf_part WHERE dt='2013';
```

`--`返回：

```
+------------+------+----+
| id         | name | dt |
+------------+------+----+
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+
```

`--`创建带分区的物化视图

```
CREATE MATERIALIZED VIEW mv_rebuild BUILD DEFERRED PARTITIONED BY (dt) AS SELECT * FROM mf_part;
```

`--`查询物化视图数据

```
SELECT * FROM mv_rebuild WHERE dt='2013';
```

`--`返回

```
+------------+------+----+
| id         | name | dt |
+------------+------+----+ +------------+------+----+
```

`--`刷新最新分区数据

```
ALTER MATERIALIZED VIEW mv_rebuild REBUILD PARTITION(dt=max_pt('mf_part'));
```

`--`查询物化视图数据

```
SELECT * FROM mv_rebuild WHERE dt='2013';
```

`--`返回

```
+------------+------+----+
| id         | name | dt |
+------------+------+----+
```

大数据计算服务

```
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+
```

**修改物化视图的生命周期**

修改已创建的物化视图的生命周期。 命令格式

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> SET LIFECYCLE <days>;
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| project nam _ e | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv name _ | 是 | 待更新物化视图的名称。 |
| days | 是 | 设置物化视图的新生命周期。单位为天。 |

##### 使用示例

`--`修改物化视图的生命周期为`10`天。

```
ALTER MATERIALIZED VIEW count_mv SET LIFECYCLE 10;
```

**开启或禁用物化视图的生命周期**

开启或禁用已创建的物化视图的生命周期。 命令格式

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> [<pt_spec>] enable|disable LIFECY CLE;
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| project _ name | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv nam _ e | 是 | 待开启或禁用生命周期的物化视图的名称。 |

大数据计算服务

| pt spec |  |  | 待开启或禁用生命周期的物化视图的分区。格式为 (partition col1 = _ |  |
|---|---|---|---|---|
|  |  |  |  | (partition col1 = _ |
|  | pt spec | 否 | partition col value1, partition col2 = partition col value2, _ _ _ _ _ |  |
| _ | _ |  |  |  |
|  |  |  | ...) |  |
| enable\|d isable |  | 是 | enable 代表开启， disable 代表禁用，禁用后该分区或表就不涉及生命周期管理。 |  |

##### 使用示例

示例一：开启物化视图的生命周期管理。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') enable LIFECYCLE;
```

示例二：禁用物化视图的生命周期管理。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') disable LIFECYCLE;
```

**查询物化视图信息**

查看物化视图的结构、修改时间等信息。 命令格式

```
DESC EXTENDED [<project_name>.]<mv_name>;
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| project _ name | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv nam _ e | 是 | 待查询物化视图的名称。 |

##### 使用示例

```
DESC EXTENDED mv;
```

返回结果如下：

**说明**

如下结果示例需要MaxCompute客户端升级至v0.43及以上版本。

```
+------------------------------------------------------------------------------------+
| Owner:                    ALIYUN$$****@***.aliyunid.com                       |
+------------------------------------------------------------------------------------+
| CreateTime:               2023-05-30 13:16:07                                      |
```

大数据计算服务

```
| LastDDLTime:              2023-05-30 13:16:07                                      |
| LastModifiedTime:         2023-05-30 13:16:07                                      |
+------------------------------------------------------------------------------------+
| MaterializedView: YES                                                              |
| ViewText: select id,name from mf_refresh                                           |
| Rewrite Enabled: true                                                              |
| AutoRefresh Enabled: true                                                          |
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
+------------------------------------------------------------------------------------+ +------------------------------------------------------------------------------------+
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
37|
```

大数据计算服务

```
37 | +------------------------------------------------------------------------------------+
```

**查询物化视图状态**

查询物化视图状态，以便及时知晓源表变更，确保物化视图有效。物化视图状态分为如下两种： 物化视图有效执行查询语句时，MaxCompute会从物化视图中直接查询数据，不会从源数据中查询数据。 物化视图无效执行查询语句时，MaxCompute无法从物化视图中直接查询数据，会从源数据中查询数据，无法实现查询加速。 用户可以通过下面的函数查看物化视图的数据是否有效。 函数声明。

```
boolean materialized_view_is_valid(<mv_name>,<partition_value>);
```

使用示例。 检查mf_mv_refresh4的数据是否与原表最新的数据一致，如果一致返回 `true` ，否则返回 `false` 。

```
SELECT materialized_view_is_valid("count_mv"); SELECT materialized_view_is_valid("mf_mv_blank_pts","1");
```

**列出项目下物化视图**

列出项目下所有的物化视图，或符合某些规则的物化视图。

**说明**

`SHOW MATERIALIZED VIEWS` 命令需要在MaxCompute客户端（odpscmd）0.43.0及以上版本中执行。 命令格式 `--`列出项目下所有的物化视图。

```
SHOW MATERIALIZED VIEWS;
```

`--`列出项目下名称与`materialized_view`匹配的物化视图。

```
SHOW MATERIALIZED VIEWS LIKE '<materialized_view>';
```

##### 使用示例

`--`列出项目下名称与`test*`匹配的物化视图名。*表示任意字段。

```
SHOW MATERIALIZED VIEWS LIKE 'test*';
```

返回结果如下。

**删除物化视图**

删除已创建的物化视图。 命令格式大数据计算服务

```
DROP MATERIALIZED VIEW [IF EXISTS] [<project_name>.]<mv_name> [purge];
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| IF EXISTS | 否 | 如果没有指定IF EXISTS且物化视图不存在会返回报错。 |
| project _ name | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv nam _ e | 是 | 待删除物化视图的名称。 |
| purge | 否 | 指定 purge ，在删除物化视图时，直接删除数据。 |

##### 使用示例

删除物化视图 `mv` 。

```
DROP MATERIALIZED VIEW count_mv;
```

删除物化视图 `mv` 的同时也删除数据。

```
DROP MATERIALIZED VIEW count_mv purge;
```

**删除物化视图分区**

删除已创建的物化视图的单个或多个分区。 命令格式

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> DROP [IF EXISTS] PARTITION <pt_spe c> [PARTITION <pt_spec>, PARTITION <pt_spec>....];
```

参数说明

| 参数 | 是否必填 | 说明 |
|---|---|---|
| project _ name | 否 | 物化视图所属目标MaxCompute项目名称。不填写时表示当前所在MaxCompute项目。 |
| mv nam _ e | 是 | 待删除分区的分区物化视图的名称。 |

大数据计算服务

| IF EXISTS |  | 否 | 如果没有指定IF EXISTS且物化视图不存在会返回报错。 |  |
|---|---|---|---|---|
| pt spec |  |  | 至少要指定一个分区。待删除的分区。格式为 (partition col1 = _ |  |
|  |  |  |  | (partition col1 = _ |
|  | pt spec | 是 | partition col value1, partition col2 = partition col value2, _ _ _ _ _ |  |
| _ | _ |  |  |  |
|  |  |  | ...) |  |

##### 使用示例

示例一：删除分区物化视图的某个分区。命令示例如下。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds='1');
```

示例二：删除分区物化视图的满足指定条件的分区。命令示例如下。

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds>='1' AND ds<='2');
```

**物化视图查询穿透**

对于分区物化视图，不一定所有分区都有数据，可能只刷新了最新的一些分区数据。但用户查询数据时，实际并不知道查询的所有分区数据是否都存在，当查询的分区数据不存在时，需要自动实现到原始分区表去查询数据，流程如下图所示。 如果需要物化视图支持穿透查询能力，您需要设置如下参数： 创建物化视图时，在**tblproperties**属性中添加 `"enable_auto_substitute"="true"` 配置。 物化视图支持穿透查询示例如下。
1. 创建物化视图支持分区并且支持查询穿透。
大数据计算服务 `--` 创建`src`表。

```
CREATE TABLE src(id bigint,name string) PARTITIONED BY (dt string);
```

`--` 插入数据。

```
INSERT INTO src PARTITION(dt='20210101') VALUES(1,'Alex'); INSERT INTO src PARTITION(dt='20210102') VALUES(2,'Flink');
```

`--`创建分区物化视图支持穿透。

```
CREATE MATERIALIZED VIEW IF NOT EXISTS mv LIFECYCLE 7 PARTITIONED BY (dt) tblproperties("enable_auto_substitute"="true") AS SELECT id, name, dt FROM src;
```

2. 查询表src中的分区为20210101的数据。

```
SELECT * FROM mv WHERE dt='20210101';
```

3. 查询物化视图mv中的分区为20210102的数据，自动穿透到源表查询数据。

```
SELECT * FROM mv WHERE dt = '20210102';
```

`--`因为`20210102`的数据没有物化，则需要把查询转化到对应的源表，等价于

```
SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20210102') t;
```

4. 查询物化视图mv中分区为20201230~20210102的数据，自动穿透到源表查询的数据与物化视图的数
据执行UNION操作后再返回结果。

```
SELECT * FROM mv WHERE dt >= '20201230' AND dt<='20210102' AND id='5';
```

`--`因为`20210102`的数据没有物化，则需要把查询转化到对应的源表。等价于：

```
SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20211231' OR dt='20210102'
 SELECT * FROM mv WHERE dt='20210101'
) t WHERE id = '5';
```

#### 列及分区操作

##### 添加分区

命令格式如下。

```
alter table table_name add [if not exists] partition partition_spec;
```

`--` 一次添加一个分区。

```
alter table table_name add [if not exists] partition partition_spec [PARTITION partitio n_spec PARTITION partition_spec...];
```

`--` 一次添加多个分区。

**说明**

如果未指定**if not exists**且同名的分区已存在，则报错返回。 MaxCompute单表支持的分区数量上限为6万。 对于多级分区的表，如果想添加新的分区，必须指明全部的分区值。 大数据计算服务示例如下。

```
alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou');
```

`--` 成功添加分区，用来存储`2017`年`12`月杭州地区的销售记录。

```
alter table sale_detail add if not exists partition (sale_date='201712', region='shanghai');
```

`--` 成功添加分区，用来存储`2017`年`12`月上海地区的销售记录。

```
alter table sale_detail add if not exists partition(sale_date='20171011');
```

`--` 仅指定一个分区`sale_date`，报错返回。

```
alter table sale_detail add if not exists partition(region='shanghai');
```

`--` 仅指定一个分区`region`，报错返回。

```
alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou') partition (sale_date='201712', region='shanghai');
```

`--` 成功同时添加两个分区，用来存储`2017`年`12`月杭州和上海地区的销售记录。

##### 删除分区

MaxCompute支持通过条件筛选方式删除分区。如果您希望一次性删除符合某个规则条件的一个或多个分区，可以使用表达式指定筛选条件，通过筛选条件匹配分区并批量删除分区。 未指定筛选条件时，命令格式如下。

```
alter table table_name drop [if exists] PARTITION partition_spec;
```

`--` 一次删除一个分区。

```
alter table table_name drop [if exists] PARTITION partition_spec,PARTITION partition_spec,[PARTITION partition_spec....];
```

`--` 一次删除多个分区。 其中**partition_spec**的格式如下。

**说明**

```
partition_spec:(partition_col1 = partition_col_value1, partition_col2 = partiton_col_value2, ...)
```

指定筛选条件时，命令格式如下。

```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION partition_filtercondition;
```

`--` 按照指定筛选条件删除分区。 其中分区过滤子句**PARTITION partition_filtercondition**的格式如下。

**说明**

```
PARTITION partition_filtercondition
    : PARTITION (partition_col relational_operators partition_col_value)
    | PARTITION (scalar(partition_col) relational_operators partition_col_value)
    | PARTITION (partition_filtercondition1 AND|OR partition_filtercondition2)
    | PARTITION (NOT partition_filtercondition)
    | PARTITION (partition_filtercondition1)[,PARTITION
(partition_filtercondition2), ...]
```

大数据计算服务参数说明：
**IF EXISTS**：如果未指定**IF EXISTS**，且分区不存在，会执行失败并返回报错。
**partition_spec**：删除的分区，不区分大小写。其格式中的**partition_col**是分区名
称，**partition_col_value**是分区值。
**PARTITION partition_filtercondition**：删除的分区，不区分大小写。
**partition_col**：分区名称。
**relational_operators**：关系运算符
**partition_col_value**：分区列比较值或正则表达式，与分区列数据类型保持一致。
**scalar()**：Scalar函数。Scalar函数基于输入值生成对应的标量，对分区列的值（**partition_col**的
值）进行处理后再按照指定的关系运算符**relational_operators**与**partition_col_value**做比较。 分区过滤条件支持逻辑运算符NOT、AND和OR。支持通过NOT过滤条件子句，取过滤规则的补集。支持多个过滤条件子句以AND或OR的关系组成整体分区匹配规则。 支持多个分区过滤子句，当多个分区过滤子句以英文逗号（,）分隔时，每个过滤子句的逻辑以OR的关系组成整体分区匹配规则。 限制条件： 每个分区过滤子句只能访问一个分区列。 表达式用到的函数必须是内建的Scalar函数。 示例如下。 未指定筛选条件。 `--`从表`sale_detail`中删除一个分区，`2017`年`12`月杭州分区的销售记录。

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date='201712',region='hangzhou');
```

`--`从表`sale_detail`中同时删除两个分区，`2017`年`12`月杭州和上海分区的销售记录。

```
PARTITION(sale_date='201712',region='hangzhou'),PARTITION(sale_date='201712',region='shan ai');
```

指定筛选条件。 `--`创建分区表。

```
shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING);
```

`--`添加分区。

```
PARTITION (sale_date= '201910') PARTITION (sale_date= '201911') PARTITION (sale_date= '201912') PARTITION (sale_date= '202001') PARTITION (sale_date= '202002') PARTITION (sale_date= '202003') PARTITION (sale_date= '202004') PARTITION (sale_date= '202005') PARTITION (sale_date= '202006') PARTITION (sale_date= '202007');
```

`--`批量删除分区。

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date >= '202007'); ALTER TABLE saledetail DROP IF EXISTS PARTITION(saledate LIKE '20191%');
```

大数据计算服务 _ _

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date IN ('202002','202004','202006')); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date BETWEEN '202001' AND '202007 '); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(substr(sale_date, 1, 4) = '2020'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201912' OR sale_date >= ' 202006'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date > '201912' AND sale_date <= '202004'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(NOT sale_date > '202004');
```

`--`支持多个分区过滤表达式，表达式之间是`OR`的关系。

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'), PARTITION(sale_date >= '202007');
```

`--`添加其他格式分区。

```
PARTITION (sale_date= '2019-10-05'); PARTITION (sale_date= '2019-10-06') PARTITION (sale_date= '2019-10-07');
```

`--`批量删除分区，使用正则表达式匹配分区。

```
ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date RLIKE '2019-\\d+-\\d+');
```

`--`创建多级分区表。

```
shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING , region STRING );
```

`--`添加分区。

```
PARTITION (sale_date= '201910',region = 'shanghai') PARTITION (sale_date= '201911',region = 'shanghai') PARTITION (sale_date= '201912',region = 'shanghai') PARTITION (sale_date= '202001',region = 'shanghai') PARTITION (sale_date= '202002',region = 'shanghai') PARTITION (sale_date= '201910',region = 'beijing') PARTITION (sale_date= '201911',region = 'beijing') PARTITION (sale_date= '201912',region = 'beijing') PARTITION (sale_date= '202001',region = 'beijing') PARTITION (sale_date= '202002',region = 'beijing');
```

`--`批量删除多级分区，会将`sale_date`小于`201911`和`region`等于`beijing`的分区都删除掉。

```
ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'),PARTITION(region = 'beijing');
```

如下语句会报错，报错信息为 `FAILED: ODPS-0130071:[1,82] Semantic analysis exception -`

```
invalid column reference region, partition expression must have one and only one column reference 。
```

`--`分区过滤子句只能访问一个分区列，返回报错。

```
ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911' AND region = 'beijing');
```

##### 添加列或注释

大数据计算服务命令格式如下。

```
ALTER TABLE table_name ADD COLUMNS (col_name1 type1,col_name2 type2...);
```

`--` 添加列。

```
ALTER TABLE table_name ADD COLUMNS (col_name1 type1 comment 'XXX',col_name2 type2 comme nt 'XXX');
```

`--` 同时添加列和注释。 示例如下。

```
ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING, education BIGINT);
```

`--` 给表`sale_detail`添加两个列。

```
ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING comment '客户', education BIGINT comment '教育' );
```

`--` 给表`sale_detail`添加两个列并同时添加列注释。

##### 修改列名

命令格式如下。

```
ALTER TABLE table_name CHANGE COLUMN old_col_name RENAME TO new_col_name;
```

**说明**

**old_col_name**必须是已存在的列。
表中不能有名为**new_col_name**的列。 示例如下。

```
ALTER TABLE sale_detail CHANGE COLUMN customer_name RENAME TO customer;
```

`--` 修改表`sale_detail`的列名。

##### 修改列注释

命令格式如下。

```
ALTER TABLE table_name CHANGE COLUMN col_name COMMENT 'comment_string';
```

**说明**

**comment_string**的长度不超过1024字节。
列的数据类型和位置不能修改。
**col_name**必须是已存在的列。
示例如下。 大数据计算服务

```
ALTER TABLE sale_detail CHANGE COLUMN customer COMMENT 'customer';
```

`--` 修改表`sale_detail`的列注释。

##### 同时修改列名及列注释

命令格式如下。

```
ALTER TABLE table_name CHANGE COLUMN old_col_name new_col_name column_type COMMENT 'col umn_comment';
```

**说明**

**old_col_name**必须是已存在的列。
表中不能有名为**new_col_name**的列。 列的数据类型和位置不能修改。
**column_commen**的长度不超过1024字节。
示例如下。

```
ALTER TABLE sale_detail CHANGE COLUMN customer customer_name string COMMENT '客户';
```

`--` 修改表`sale_detail`的列名和列注释。

##### 修改非分区表或分区表中分区的修改时间

MaxCompute SQL提供TOUCH操作，用来修改非分区表或分区表中分区的**LastDataModifiedTime**。 效果是会将该非分区表或分区表中分区的**LastDataModifiedTime**修改为当前时间。本章节为您介绍如命令格式如下。

```
ALTER TABLE table_name TOUCH;
```

`--` 修改非分区表的修改时间。

```
ALTER TABLE table_name TOUCH PARTITION(partition_col='partition_col_value', ...);
```

`--` 修改分区表中分区的修改时间。

**说明**

**partition_col='partition_col_value'**不存在，则报错返回。
此操作会改变非分区表和分区表中分区的**LastDataModifiedTime**的值。此时，MaxCompute会认为数据有变动，生命周期的计算会重新开始。 示例如下。

```
ALTER TABLE result_table TOUCH;
```

`--` 修改非分区表的修改时间。

```
ALTER TABLE sale_detail TOUCH PARTITION(sale_date='201712');
```

`--` 修改分区表中分区的修改时间。 大数据计算服务

##### 修改分区值

命令格式如下。

```
ALTER TABLE table_name PARTITION (partition_col1 = 'partition_col_value1', partition_col2 = 'partiton_col_value2', ...) RENAME TO PARTITION (partition_col1 = 'partition_col_newvalue1', partition_col2 = 'part iton_col_newvalue2', ...);
```

**说明**

不支持修改分区列列名，只能修改分区列对应的值。 修改多级分区的一个或多个分区值，多级分区的每一级的分区值都必须填写。 示例如下。

```
ALTER TABLE sale_detail PARTITION (sale_date = '201712', region = 'hangzhou') RENAME TO PARTITION (sale_date = '201710', region = 'beijing');
```

`--` 修改表`sale_detail`的分区值。

##### 合并分区

MaxCompute SQL提供 `MERGE PARTITION` 命令对分区表的分区进行合并，即同一个分区表下的多个分区合并成一个分区，同时删除被合并的分区维度的信息，把数据移动到指定分区。本章节为您介绍如何使用命令格式如下。

```
ALTER TABLE <tableName> MERGE [IF EXISTS] PARTITION(<predicate>) [, PARTITION(<predicate2>) ...] OVERWRITE PARTITION(<fullPartitionSpec>) [PURGE];
```

**说明**

如果没有指定**IF EXISTS**且分区不存在，则报错返回。 如果指定**IF EXISTS**后不存在满足**MERGE**条件的分区，则不生成新分区。 如果运行过程中出现源数据被并发修改（包括INSERT、RENAME或DROP）时，即使指定**IF**
**EXISTS**也会报错。
如果带PURGE属性，被合并分区不能再被元数据快照备份恢复。 限制项与报错处理： 不支持外部表，聚簇表合并后的分区会消除聚簇属性。 一次性合并分区数量限制为4000个。 CatalogServer Busy则等待后重试。 遇到Pangu Hardlink报错时，则可以Purge回收站后再重试。 示例如下。 大数据计算服务

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
+------------+------------+------------+------------+
```

`--` 分区表的分区和数据。

```
odps@ jet_zwz>ALTER TABLE intpstringstringstring MERGE PARTITION(hh='00') OVERWRITE PAR TITION(ds='20181101', hh='00', mm='00'); ID = 20190404025755844g80qwa7a
```

`OK` `--` 合并所有满足`hh='00'`的分区到`hh='00'`，`mm='00'`中。

```
odps@ jet_zwz>SHOW PARTITIONS intpstringstringstring; ds=20181101/hh=00/mm=00 ds=20181101/hh=10/mm=00 ds=20181101/hh=10/mm=10
```

`OK` `--` 查看合并后的分区。

```
odps@ jet_zwz>DESC intpstringstringstring; +------------+------------+------------+------------+
| value      | ds         | hh         | mm         |
+------------+------------+------------+------------+
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 10         | 00         |
| 1          | 20181101   | 10         | 10         |
+------------+------------+------------+------------+
```

`--` 两个分区的数据已经合并到了一个分区中。

### DML语句

#### INSERT语句

##### 更新表中的数据

大数据计算服务在MaxCompute SQL处理数据的过程中， INSERT OVERWRITE|INTO 用于将计算的结果保存目标表中。 其中 `INSERT INTO` 直接向表或表的分区中追加数据，不支持 `INSERT INTO` 到聚簇表。如果您需要插入 `INSERT OVERWRITE` 则先清空表中的原有数据，再向表或分区中插入数据。 `INSERT OVERWRITE` 不支持指定插入列的功能。 命令格式如下。

```
INSERT OVERWRITE|INTO TABLE table_name [PARTITION (partcol1=val1, partcol2=val2 ...)] [ (col1,col2 ...)] select_statement FROM from_statement [ZORDER BY zcol1 [, zcol2 ...]];
```

**说明**

MaxCompute的INSERT语句与通常使用的MySQL或Oracle的INSERT语句有差别， 在 INSERT OVERWRITE|INTO 后需要加入TABLE关键字，而非直接使用**tablename**。 遇到并发写入时，MaxCompute会根据ACID保障并发写入操作。 源表与目标表的对应关系依赖于在SELECT子句中列的顺序，而不是表与表之间列名的对应关系。 目标表是静态分区，向某个分区插入数据时，分区列不允许出现在SELECT子句中。 参数说明：
**PARTITION (partcol1=val1, partcol2=val2 ...)**：需要插入数据的分区名称，此参数不允许使
用函数等表达式，只能是常量。
**[(col1,col2 ...)]**：需要插入目标表的列名称。 `INSERT OVERWRITE` 不支持。
**select_statement**：SELECT子句，从源表中查询需要插入的数据。
**from_statement**：FROM子句，代表数据来源。例如，源表名称。
**[ZORDER BY zcol1 [, zcol2 ...]]**：向表或分区写入数据时，支持根据指定的一列或多列
（select_statement对应表中的列），把排序列数据相近的行排列在一起，提升查询时的过滤性能，在一定程度上降低存储成本。 需要注意， `ORDER BY x, y` 会严格地按照先x后y的顺序对数据进行排序， `ZORDER BY x, y` 会把相近的<x, y>尽量排列在一起。当SQL查询语句的过滤条件中包含排序列时，ORDER BY后的数据仅对包含x的表达式有较好的过滤效果，ZORDER BY后的数据对包含x或同时包含x、y的表达式均有较好的过滤效果，列压缩比例更高。

**说明**

源表与目标表的对应关系依赖于在SELECT子句中列的顺序，而不是表与表之间列名的对应关系。 如果目标表是静态分区，向某个分区插入数据时，分区列不允许出现在SELECT子句中。 使用ZORDER BY子句语句写入数据时，会占用较多资源，比不排序花费时间更多。 目标表为聚簇表时，不支持ZORDER BY子句。 ZORDER BY新增Distribute by支持，但不支持与Order by、Cluster by及Sort by一起使用。 示例如下。 大数据计算服务计算sale_detail表中不同地区的销售额存入表sale_detail_insert中。 `--`创建一张分区表`sale_detail`，并插入分区和数据。注意源表建表语句中，分区列不需要在普通列中重复定义。

```
( shop_name string, customer_id string, total_price double
```

)

```
PARTITIONED BY (sale_date STRING,region STRING);
```

`--`向源表增加分区。

```
ALTER TABLE sale_detail ADD PARTITION (sale_date='2013', region='china');
```

`--`向源表增加数据，其中`INSERT INTO TABLE table_name`可以简写为`INSERT INTO table_name`，但`INSERT`

```
INSERT INTO sale_detail PARTITION (sale_date='2013', region='china') VALUES ('s1','c1',100.1),('s2','c2',100.2),('s3','c3',100.3);
```

`--`创建目标表`sale_detail_insert`，与源表有相同的结构。

```
CREATE TABLE sale_detail_insert LIKE sale_detail;
```

`--`给目标表增加分区。

```
ALTER TABLE sale_detail_insert ADD PARTITION (sale_date='2013', region='china');
```

`--`从源表`sale_detail`中取出数据插入目标表`sale_detail_insert`。 `--`注意不需要声明目标表字段，也不支持重排目标表字段顺序。 `--`对于静态分区目标表，分区字段赋值已经在`PARTITION()`部分声明，不需要在`select_statement`中包含，只要按照目标表普通列顺序查出对应字段，按顺序映射到目标表即可。动态分区表则需要在`SELECT`中包含分区字段，详情请

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
  shop_name,
  customer_id,
  total_price
  FROM sale_detail
  ZORDER BY customer_id, total_price;
```

您需要注意： 源表与目标表的对应关系依赖于在SELECT子句中列的顺序，而不是表与表之间列名的对应关系。命令示例如下。

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
    SELECT customer_id, shop_name, total_price FROM sale_detail;
```

在创建sale_detail_insert表时，列的顺序为**shop_name STRING**、**customer_id**
**STRING**、**total_price BIGINT**，而从sale_detail向sale_detail_insert插入数据的顺序
为**customer_id**、**shop_name**、**total_price**。此时，会将**sale_detail.customer_id**的数据插入**sale_detail_insert.shop_name**，将**sale_detail.shop_name**的数据插入**sale_detail_insert.customer_id**。 向某个分区插入数据时，分区列不允许出现在SELECT子句中。如下语句会返回报错，**sale_date**和**region**为分区列，不允许出现在静态分区的INSERT语句中。 大数据计算服务

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
   SELECT shop_name, customer_id, total_price, sale_date, region FROM sale_detail;
```

**PARTITION**的值只能是常量，不可以为表达式。如下为错误用法。

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date=datepart('2016-09-18 0 1:10:00', 'yyyy') , region='china')
   SELECT shop_name, customer_id, total_price FROM sale_detail;
```

**使用动态分区注意事项**

如果您需要更新表数据到动态分区，请注意以下事项：

| INSERT INTO PARTITION |  | 时， |
|---|---|---|
| 多个 | INSERT INTO PARTITION |  |

如果不能控制 `INSERT INTO PARTITION` 作业并发，建议您通过 `ALTER TABLE` 命令提前创建分区来避免问题。

##### 多路输出

命令格式如下。

```
FROM from_statement INSERT OVERWRITE | INTO TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...)] select_statement1 [FROM from_statement] [INSERT OVERWRITE | INTO TABLE tablename2 [PARTITION (partcol1=val3, partcol2=val4 ...)
```

]

```
select_statement2 [FROM from_statement]];
```

**说明**

通常，单个SQL中最多可以写256路输出。超过256路，则报语法错误。 在一个多路输出中，对于分区表，同一个目标分区不允许出现多次；对于非分区表，该表不能出现多次。 对于同一张分区表的不同分区，不能同时有 `INSERT OVERWRITE` 和 `INSERT INTO` 操作，否则报错返回。
**PARTITION (partcol1=val1, partcol2=val2 ...)**参数不允许使用函数等表达式，只能
是常量。 示例如下。 大数据计算服务 `--`创建表`sale_detail_multi`。

```
create table sale_detail_multi like sale_detail;
```

`--`将表`sale_detail`中的数据插入到表`sale_detail_multi`。 set odps.sql.allow.fullscan=true; --开启全表扫描，仅此`session`有效。

```
from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price ;
```

`--`同一分区出现多次，报错返回。

```
from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price;
```

`--`同一张分区表的不同分区，同时有`INSERT OVERWRITE`和`INSERT INTO`操作，报错返回。

```
from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert into table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price;
```

##### 输出到动态分区

在使用INSERT OVERWRITE语句将数据插入到分区表时，MaxCompute提供了如下两种方式： 输出到动态分区：在INSERT语句中不直接指定分区值，只指定分区列名。分区列的值在SELECT子句中提供，系统自动根据分区字段的值将数据插入到相应分区。 命令格式如下。

```
INSERT OVERWRITE|INTO TABLE tablename PARTITION (partcol1, partcol2 ...) select_statement FROM from_statement;
```

大数据计算服务

**说明**

使用INSERT INTO最多可以生成10000个动态分区，使用INSERT OVERWRITE最多可以生成 60000个动态分区。 分布式环境下，使用动态分区功能的SQL中，单个进程最多只能输出512个动态分区，否则会引发运行时异常。 动态生成的分区值不允许为NULL，也不支持含特殊字符和中文，否则会引发运行时异。

```
FAILED: ODPS-0123031:Partition exception - invalid dynamic partition value: p rovince=xxx
```

如果目标表有多级分区，在运行INSERT语句时允许指定部分分区为静态，但是静态分区必须是高级分区。 动态分区中，**select_statement**字段和目标表动态分区的对应是按字段顺序决定，并不是按照列名称决定的。当源表的字段与目标表字段顺序不一致时，建议您按照目标表顺序在**select_statement**语句中指定字段。 示例如下。 将源表中的数据插入到目标表中。在SQL运行之前，您无法得知会产生哪些分区。只有在语句运行结束后， 才能通过region字段产生的值确定产生的分区。 `--`创建目标表`total_revenues`。

```
create table total_revenues (revenue bigint) partitioned by (region string);
```

`--`将源表`sale_detail`中的数据插入到目标表`total_revenues`。

```
insert overwrite table total_revenues partition(region) select total_price as revenue, region from sale_detail;
```

将源表中的数据插入到目标表中。多级分区，指定一级分区sale_date。

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price,region from sale_detail;
```

动态分区插入时，动态分区列必须在SELECT列表中，否则会执行失败。

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price from sale_detail;
```

动态分区插入时，不能仅指定低级子分区，而动态插入高级分区，否则会执行失败。

```
insert overwrite table sales partition (region='china', sale_date) select shop_name,customer_id,total_price,sale_date from sale_detail;
```

MaxCompute 1.0在进行动态分区时，如果分区列的类型与对应SELECT列表中列的类型不严格一致，会发生报错。MaxCompute 2.0则支持隐式类型转换。

```
create table parttable(a int, b double) partitioned by (p string); insert into parttable partition(p) select key, value, current_timestmap() from src; select * from parttable;
```

大数据计算服务

##### VALUES

命令格式如下。

```
[PARTITION (partcol1=val1, partcol2=val2,...)][(co1name1,colname2,...)] [VALUES (col1_value,col2_value,...),(col1_value,col2_value,...),...]
```

参数说明：
**[PARTITION (partcol1=val1, partcol2=val2,...)]**：分区信息。如果需要更新的表为分区表，您
需要指定该参数。
**[(co1name1,colname2,...)]**：目标表中的字段名称。
**col_value**：目标表中列对应的列值。多个列值之间用英文逗号（,）分隔。该列值必须为常量，未指定
列值时，默认值为NULL。

**说明**

不支持通过 `insert overwrite` 操作指定插入列，只能通过 `insert into` 操作指定插入列。 复杂数据类型无法在VALUES中通过函数构造对应的常量，例如ARRAY，此时您可以通过如下

```
INSERT INTO TABLE srcp (p='abc') SELECT 'a', ARRAY('1', '2', '3');
```

通过VALUES写入DATETIME或TIMESTAMP数据类型时，需要在VALUES中指定类型名称。

```
INSERT INTO TABLE srcp (p='abc') VALUES (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789');
```

示例如下。 特定分区内插入数据。 `--`删除已存在的表`srcp`。

```
DROP TABLE IF EXISTS srcp;
```

`--`创建分区表`srcp`。

```
CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string);
```

`--`给表`srcp`的指定分区`abc`中插入数据。

```
INSERT INTO TABLE srcp PARTITION (p='abc') VALUES ('a',1),('b',2),('c',3);
```

`--`查询表`srcp`。

```
SELECT * FROM srcp WHERE p='abc';
```

返回结果如下。 大数据计算服务

```
+------------+------------+------------+ +------------+------------+------------+
| a          | 1          | abc        |
| b          | 2          | abc        |
| c          | 3          | abc        |
+------------+------------+------------+
```

非特定分区内插入数据。 `--`删除已存在的表`srcp`。

```
DROP TABLE IF EXISTS srcp;
```

`--`创建分区表`srcp`。

```
CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string);
```

`--`给表`srcp`的分区插入数据。

```
INSERT INTO TABLE srcp PARTITION (p)(key,p) VALUES ('d','20170101'),('e','20170101'),(' f','20170101');
```

`--`查询表`srcp`。

```
SELECT * FROM srcp WHERE p='20170101';
```

返回结果如下。

```
+------------+------------+------------+ +------------+------------+------------+
| d          | NULL       | 20170101   |
| e          | NULL       | 20170101   |
| f          | NULL       | 20170101   |
+------------+------------+------------+
```

使用复杂数据类型构造常量，通过 `insert` 操作导入数据。 `--`创建分区表`srcp`。

```
create table if not exists srcp (key string,value array<int>) partitioned by (p string) ;
```

`--`向分区表`srcp`添加分区。

```
alter table srcp add if not exists partition (p='abc');
```

`--`向表`srcp`的指定分区`abc`中插入数据。

```
insert into table srcp partition (p='abc') select 'a', array(1, 2, 3);
```

`--`查询表`srcp`。

```
select * from srcp where p='abc';
```

返回结果如下。

```
+------------+------------+------------+ +------------+------------+------------+
| a          | [1,2,3]    | abc        |
+------------+------------+------------+
```

通过 insert … values 操作写入DATETIME或TIMESTAMP数据类型。 大数据计算服务 `--`创建分区表`srcp`。

```
create table if not exists srcp (key string, value timestamp) partitioned by (p string) ;
```

`--`向分区表`srcp`添加分区。

```
alter table srcp add if not exists partition (p='abc');
```

`--`向表`srcp`的指定分区`abc`中插入数据。

```
insert into table srcp partition (p='abc') values (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789');
```

`--`查询表`srcp`。

```
select * from srcp where p='abc';
```

返回结果如下。

```
+------------+------------+------------+ +------------+------------+------------+
| 2017-11-11 00:00:00 | 2017-11-11 00:00:00.123456789 | abc        |
+------------+------------+------------+
```

使用INSERT VALUES语句时，VALUES后的取值必须是常量。如果需要对插入的数据进行简单的运算，建命令格式如下。

```
values (<col1_value>,<col2_value>,...),(<col1_value>,<col2_value>,...),<table_name> (<c ol1_name> ,<col2_name>,...)...
```

在没有任何物理表时，您可以模拟一个有任意数据的、多行的表，并进行任意运算。 例如 VALUES (…), (…) t(a, b) 相当于定义了一个名为t，列为a和b，类型分别为STRING和BIGINT `--`删除已存在的表`srcp`。

```
DROP TABLE IF EXISTS srcp;
```

`--`创建分区表`srcp`。

```
CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string);
```

`--`为表`srcp`中插入数据。

```
INSERT INTO TABLE srcp PARTITION (p) SELECT concat(a,b), length(a)+length(b),'20170102' FROM VALUES ('d',4),('e',5),('f',6) t(a,b);
```

`--`查询表`srcp`。

```
SELECT * FROM srcp WHERE p='20170102';
```

返回结果如下。

```
+------------+------------+------------+ +------------+------------+------------+
| d4         | 2          | 20170102   |
| e5         | 2          | 20170102   |
| f6         | 2          | 20170102   |
+------------+------------+------------+
```

大数据计算服务

```
SELECT 1 c UNION ALL SELECT 2 c;
```

`--`等同于以下语句。

```
SELECT * FROM VALUES (1), (2) t(c);
```

返回结果如下。

```
+------------+
| c          |
+------------+
| 1          |
| 2          |
+------------+
```

VALUES TABLE的特殊形式。您可以不通过FROM语句，直接执行SELECT（SELECT表达式列表中不可以出现上游表的数据）。其底层实现为从一个1行0列的匿名VALUES表中进行选取操作。在测试UDF或其它函数时，您可以通过该方式免去手工创建DUAL表的过程。 `--`创建分区表`srcp`。

```
create table if not exists srcp (key string,value bigint) partitioned by (p string);
```

`--`向表`srcp`中插入数据。

```
insert into table srcp partition (p) select abs(-1), length('abc'), getdate();
```

`--`查询表`srcp`。

```
select * from srcp;
```

返回结果如下。

```
+------------+------------+------------+ +------------+------------+------------+
| 1          | 3          | 2020-11-25 18:39:48 |
+------------+------------+------------+
```

VALUES表达式从只支持常量进行了扩展，目前VALUES表达式还支持非常量表达式，支持语法如下。

```
select * from values (udf(1)),(to_date('20190101', 'yyyyMMdd')),(getdate()) t(d);
```

#### SELECT语句

##### SELECT操作

命令格式如下。 大数据计算服务

```
SELECT [ALL | DISTINCT] select_expr, select_expr, ... [WHERE where_condition] [GROUP BY col_list] [ORDER BY order_condition] [DISTRIBUTE BY distribute_condition [SORT BY sort_condition] ] [LIMIT number];
```

##### 使用限制

当使用SELECT语句时，屏显目前最多只能显示10000行结果。当SELECT语句作为子句时则无此限制，SELECT子句会将全部结果返回给上层查询。 SELECT语句查询分区表时禁止全表扫描。如果您需要对分区表进行全表扫描，可以在对分区表全表扫描的SQL语句前加上命令 set odps.sql.allow.fullscan=true; ，并和SQL语句一起提交执行。如果整个项目都需要全表扫描，执行如下命令打开开关。

```
setproject odps.sql.allow.fullscan=true;
```

**列表达式（select_expr）**

用列名指定要读取的列。

```
select shop_name from sale_detail;
```

用*代表所有的列。

```
select * from sale_detail;
```

`--`在`WHERE`中可以指定过滤的条件。

```
select * from sale_detail where shop_name like 'hang%';
```

**select_expr**支持正则表达式。
DISTINCT去重。您可以在选取的列名前使用DISTINCT去掉重复字段，只返回一个值；而使用ALL会返回字段中所有重复的值。不指定此选项时，默认值为ALL。 `--`查询表`sale_detail`中`region`列数据，如果有重复值时仅显示一条。

```
select distinct region from sale_detail;
```

返回结果如下。

```
+------------+
| region     |
+------------+
| shanghai   |
+------------+
```

`--DISTINCT`多列时，`DISTINCT`的作用域是`select`的列集合，不是单个列。列之间存在对应关系，多列去重时可能会破坏对应关系。

```
select distinct region, sale_date from sale_detail;
```

返回结果如下。 大数据计算服务

```
+------------+------------+
| region     | sale_date  |
+------------+------------+
| shanghai   | 20191110   |
+------------+------------+
```

TABLE_REFERENCE为查询的目标表信息。除了支持已存在的目标表名称还支持使用嵌套子查询。示例如下。

```
select * from (select region from sale_detail) t where region = 'shanghai';
```

**WHERE子句过滤**

WHERE子句支持的过滤条件，如下表所示。

| 过滤条件 | 描述 |
|---|---|
| > 、 < 、 =、 >=、 <=、 <> | 关系操作符。 |
| LIKE、RLIKE | LIKE和RLIKE的Source和Pattern参数均仅接受STRING类型。 |
| IN、NOT IN | 如果在IN\|NOT IN条件后加子查询，子查询只能返回一列值，且返回值的数量不能超过1000。 |
| BETWEEN…AND | 限定查询范围。 |

在SELECT语句的WHERE子句中，您可以指定分区范围，只扫描表的指定部分，避免全表扫描。

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date >= '2008' AND sale_detail.sale_date <= '2014';
```

UDF支持分区裁剪。支持的方式是将UDF语句先当作一个小作业执行，再将执行的结果替换到原来UDF出现的位置。 实现方式在编写UDF的时候，UDF类上加入Annotation。

```
@com.aliyun.odps.udf.annotation.UdfProperty(isDeterministic=true)
```

**重要**

**com.aliyun.odps.udf.annotation.UdfProperty**定义在odps-sdk-udf.jar文件中，您需
要把引用的**odps-sdk-udf**的版本提高到0.30.x 或以上。 大数据计算服务在SQL语句前设置Flag语句 set odps.sql.udf.ppr.deterministic = true; ，此时SQL中所有的 UDF均被视为**deterministic**。

**说明**

该操作执行的原理是进行执行结果回填，但是结果回填最多回填1000个Partition。因此，如果 UDF类加入Annotation，则可能会导致出现超过1000个回填结果的报错。此时您如果需要忽视此错误，可以通过设置Flag： set odps.sql.udf.ppr.to.subquery = false; 全局关闭此功能。关闭后，UDF分区裁剪也会失效。 注意事项使用UDF实现分区裁剪时，UDF必须在查询表的 `where` 条件里才能生效。 用UDF实现分区裁剪正确示例如下。 `--UDF`必须放在查询的源表的`where`条件中：

```
SELECT key, value from srcp where udf(ds) = 'xx';
```

用UDF实现分区裁剪错误示例如下。 `--`放在`join on`后面分区裁剪不会生效

```
SELECT A.c1, A.c2 from srcp1 A join srcp2 B on A.c1 = B.c1 and udf(A.ds) ='xx';
```

MaxCompute SQL的WHERE子句支持BETWEEN…AND条件查询。示例如下。

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date BETWEEN '2008' AND '2014';
```

**GROUP BY分组查询**

通常，GROUP BY和聚合函数配合使用。在SELECT中包含聚合函数时有以下规则： 在SQL解析中，GROUP BY操作先于SELECT操作，因此GROUP BY的取值是SELECT输入表的列名或者 GROUP BY的值既是输入表的列或表达式，又是SELECT的输出列时，取值为输入表的列名。 当SQL语句设置Flag，即 set hive.groupby.position.alias=true; 时，GROUP BY中的整型常量会被当做SELECT的列序号处理。

```
set hive.groupby.position.alias=true;
```

`--`与下一条`sql`语句一起执行。

```
select region, sum(total_price) from sale_detail group by 1;
```

`-- 1`代表`select`的列中第一列即`region`，以`region`值分组，返回每一组的`region`值(组内唯一)及销售额总量。 示例如下。 大数据计算服务 `--`直接使用输入表列名`region`作为`group by`的列，即以`region`值分组。

```
select region from sale_detail group by region;
```

`--`以`region`值分组，返回每一组的销售额总量。

```
select sum(total_price) from sale_detail group by region;
```

`--`以`region`值分组，返回每一组的`region`值（组内唯一）及销售额总量。

```
select region, sum(total_price) from sale_detail group by region;
```

`--`使用`select`列的别名运行，报错返回。

```
select region as r from sale_detail group by r;
```

`--`必须使用列的完整表达式。

```
select 2 + total_price as r from sale_detail group by 2 + total_price;
```

`--`报错返回，`select`的所有列中没有使用聚合函数的列，必须出现在`group by`中。

```
select region, total_price from sale_detail group by region;
```

`--`没有使用聚合函数的列出现在`group by`中后，运行成功。

```
select region, total_price from sale_detail group by region, total_price;
```

**ORDER BY|DISTRIBUTE BY|SORT BY**

ORDER BY：用于对所有数据按照指定列进行全局排序。 对记录进行降序排序，需要使用**desc**关键字。默认以升序排列。 在使用ORDER BY排序时，NULL会被认为比任何值都小，这个行为与MySQL一致，但是与Oracle不一致。 ORDER BY后面须加SELECT列的别名。当SELECT某列时，如果没有指定列的别名，则列名会被作为列的别名。 当SQL语句设置Flag，即 set hive.orderby.position.alias=true; 时，ORDER BY 中的整型常量会被当做SELECT的列序号处理。 `--`设置`Flag`。

```
set hive.orderby.position.alias=true;
```

`--`创建表`src`。

```
creat table src(key BIGINT，value BIGINT);
```

`--`以`value`值分组，返回表`src`的所有信息。

```
SELECT * FROM src ORDER BY 2 limit 100;
```

等同于

```
SELECT * FROM src ORDER BY value limit 100;
```

OFFSET和ORDER BY LIMIT语句配合，可以指定跳过OFFSET数目的行。 `--`将`src`按照`key`从小到大排序后，输出第`11`到第`30`行（`OFFSET 10`指定跳过前`10`行，`LIMIT 20`指定最多输出 `20`行）。

```
SELECT * FROM src ORDER BY key LIMIT 20 OFFSET 10；
```

示例如下。 `--`查询表`sale_detail`的信息，并按照`region`升序排列前`100`条。

```
SELECT * FROM sale_detail ORDER BY region LIMIT 100;
```

`--ORDER BY`默认要求带`LIMIT`数据行数限制，没有`LIMIT`会返回报错。

```
SELECT * FROM sale_detail ORDER BY region;
```

`--ORDER BY`加列的别名。

```
SELECT region AS r FROM sale_detail ORDER BY region LIMIT 100; SELECT region AS r FROM sale_detail ORDER BY r LIMIT 100;
```

DISTRIBUTE BY：用于对数据按照某几列的值做Hash分片，必须使用SELECT的输出列别名。 大数据计算服务示例如下。 `--`查询表`sale_detail`中的列`region`值并按照`region`值进行哈希分片。

```
SELECT region FROM sale_detail DISTRIBUTE BY region;
```

`--` 列名即是别名，可以运行。

```
SELECT region AS r FROM sale_detail DISTRIBUTE BY region;
```

等同于

```
SELECT region AS r FROM sale_detail DISTRIBUTE BY r;
```

SORT BY：局部排序。您可以在字段后面加上关键字，ASC表示升序，DESC表示降序，不带关键字默认为升序。 如果SORT BY语句前有DISTRIBUTE BY，SORT BY对DISTRIBUTE BY的结果进行局部排序。 DISTRIBUTE BY控制Map的输出在Reduer中如何划分，如果不希望Reducer的输出内容存在重叠， 或需要对同一分组的数据一起处理，您可以使用DISTRIBUTE BY来保证同组数据分发到同一个 Reducer中，然后使用SORT BY对局部数据进行排序。示例如下。 `--`查询表`sale_detail`中的列`region`值并按照`region`值进行哈希分片，然后对哈希分片结果进行局部排序。

```
SELECT region FROM sale_detail DISTRIBUTE BY region SORT BY region;
```

如果SORT BY语句前没有DISTRIBUTE BY，SORT BY对每个Reduce中的数据进行排序，同样是执行一个局部排序过程。这可以保证每个Reduce的输出数据都是有序的，从而增加存储压缩率。同时，读取时如果有过滤，能够减少真正从磁盘读取的数据量，提高后续全局排序的效率。示例如下。

```
SELECT region FROM sale_detail SORT BY region;
```

**说明**

ORDER BY|DISTRIBUTE BY|SORT BY的取值必须是SELECT语句的输出列，即列的别名。列的别名可以为中文。 在MaxCompute SQL解析中，ORDER BY|DISTRIBUTE BY|SORT BY在SELECT操作之后， ORDER BY不和DISTRIBUTE BY、SORT BY同时使用，同时GROUP BY也不和DISTRIBUTE BY、SORT BY同时使用。

**LIMIT NUMBER限制输出行数**

LIMIT number中的**number**参数是常数，限制输出行数。 解除ORDER BY必须带LIMIT的限制。 因为ORDER BY需要对单个执行节点做全局排序，所以默认带LIMIT限制，避免误用导致单点处理大量数据。如果您的使用场景确实需要ORDER BY放开LIMIT限制，可以通过如下两种方式实现： Project级别：设置 setproject odps.sql.validate.orderby.limit=false; 关闭ORDER BY必须带LIMIT的限制。 Session级别：设置 setproject odps.sql.validate.orderby.limit=false; 关闭ORDER BY必须带LIMIT的限制，需要与SQL语句一起提交。

**说明**

如果关闭ORDER BY必须带LIMIT的限制，在单个执行节点有大量数据排序的情况下，资源消耗或处理时长等性能表现会受到影响。 屏显限制说明。 大数据计算服务当使用无LIMIT的SELECT语句或LIMIT的number数量超过设置的屏显上限时，如果您直接从屏显窗口查看结果，最多只能输出屏显上限设置的行数。 每个项目空间的屏显上限可能不同，您可以参考如下方法控制： 如果关闭了项目空间数据保护（即set ProjectProtection=false） 且**use_instance_tunnel=true**，同时**instance_tunnel_max_record**未配置，则查看屏显不受限。项目空间数据保护的详细信息请参见数据保护机制，**use_instance_tunnel=true**及**instance_tunnel_max_record**配置的详细信息请参见Tunnel操作。 如果打开了项目空间数据保护，屏显行数受限制项**READ_TABLE_MAX_ROW**配置的参数值限制， 配置上限为10000行。

**说明**

您可以执行 show SecurityConfiguration; 命令查看**ProjectProtection**属性配置。如果**ProjectProtection=true**，根据项目空间数据保护需求判断是否关闭数据保护机制。如果可以关闭，通过 set ProjectProtection=false; 命令关闭。**ProjectProtection**属性默认不开启。 项目空间数据保护的详细信息请参见数据保护机制。

##### 子查询

普通的SELECT是从几张表中读数据，例如 `select column_1, column_2 ... from table_name` ，但查命令格式如下。

```
select * from (select shop_name from sale_detail) a;
```

子查询必须要有别名。

**重要**

示例如下。

```
create table shop as select * from sale_detail; select a.shop_name, a.customer_id, a.total_price from (select * from shop) a join sale_detail on a.shop_name = sale_detail.shop_name;
```

在FROM子句中，子查询可以当作一张表来使用，与其他的表或子查询进行JOIN操作。

**说明**

##### UNION ALL

命令格式如下。 将两个或多个SELECT操作返回的数据集联合成一个数据集，如果结果有重复行时，会返回

**说明**

所有符合条件的行，不进行重复行的去重处理。 MaxCompute SQL不支持顶级的两个查询结果合并，要改写为一个子查询的形式。 大数据计算服务改写前错误示例如下。

```
select * from sale_detail where region = 'hangzhou' select * from sale_detail where region = 'shanghai';
```

改写后正确示例如下。

```
select * from ( select * from sale_detail where region = 'hangzhou' union all select * from sale_detail where region = 'shanghai') t;
```

示例如下。

```
SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3);
```

`--` 先执行括号中`src2`、`src3`的`UNION ALL`并得出结果后，再执行与`src`的`UNION ALL`

**重要**

UNION ALL对应的各个子查询的列个数、名称及类型必须一致。如果列名不一致时，可以使用列的别名解决。 通常情况下，MaxCompute最多允许256路UNION ALL，超过此限制时报语法错误。

##### JOIN

MaxCompute的JOIN支持多路连接，但不支持CROSS JOIN操作，即无ON条件的连接。 命令格式如下。

```
join_table:
        table_reference JOIN table_factor [join_condition]
        | table_reference {LEFT OUTER|RIGHT OUTER|FULL OUTER|INNER|NATURAL} JOIN
    table_reference:
    table_factor:
        tbl_name [alias]
    join_condition:
        ON equality_expression ( AND equality_expression )
```

**equality_expression**是一个等式表达式。

**说明**

JOIN操作类型如下： LEFT OUTER JOIN：左连接，可简写为LEFT JOIN。返回左表中的所有记录，即使右表中没有与之匹配的记录。 大数据计算服务

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a LEFT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

`--`由于表`shop`及`sale_detail`中都有`shop_name`列，因此需要在`select`子句中使用别名进行区分。 如果右表值不唯一，建议不要连续使用过多LEFT JOIN，以免在JOIN过程中产生数据膨

**说明**

胀，导致作业停滞。 RIGHT OUTER JOIN：右连接，可简写为RIGHT JOIN。返回右表中的所有记录，即使左表中没有与之匹配的记录。

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a RIGHT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

FULL OUTER JOIN：全连接，可简写为FULL JOIN。返回左右表中的所有记录。

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

INNER JOIN：内连接。关键字INNER可以省略。表中至少存在一个匹配值时，INNER JOIN返回数据行。

```
SELECT a.shop_name FROM shop a INNER JOIN sale_detail b ON a.shop_name=b.shop_name; SELECT a.shop_name FROM shop a JOIN sale_detail b ON a.shop_name=b.shop_name;
```

NATURAL JOIN：自然连接，即参与JOIN的两张表根据字段名称自动决定连接字段。支持OUTER NATURAL JOIN，支持使用Using子句执行JOIN，输出字段中公共字段只出现一次。

```
SELECT * FROM src NATURAL JOIN src2;
```

`--`由于`src`和`src2`有两个同名字段`(key1, key2)`，所以上面的`JOIN`操作相当于：

```
SELECT src.key1 AS key1, src.key2 AS key2, src.a1, src.a2, src2.b1, src2.b2 FROM src INNER JOIN src2 ON src.key1 = src2.key1 AND src.key2 = src2.key2;
```

隐式连接，即不指定JOIN关键字执行连接。

```
SELECT * FROM table1, table2 WHERE table1.id = table2.id;
```

`--`执行的效果相当于以下语句。

```
SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;
```

连接条件：只允许AND连接的等值条件。您可以通过MAPJOIN操作使用不等值连接或OR连接多个条件。 `--`支持多路`JOIN`连接示例。

```
SELECT a.* FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name
        FULL OUTER JOIN sale_detail c ON a.shop_name=c.shop_name;
```

`--`不支持不等值`JOIN`连接条件，返回报错。

```
SELECT a.* FROM shop a JOIN sale_detail b ON a.shop_name != b.shop_name;
```

当前版本中，支持通过括号指定JOIN的优先级，括号内的JOIN优先级较高。

```
SELECT * FROM src JOIN (src2 JOIN src3 on xxx) ON yyy;
```

`--` 先执行`src2 JOIN src3`并得出结果后，再执行与`src`的`JOIN`。 示例如下。 假设表A为test_table_a，表B为test_table_b。查询两表中分区大于20180101且**origin**和**id**一致的记录大数据计算服务

```
SELECT s.id
    ,s.name
    ,s.origin
    ,d.value
FROM (SELECT * FROM test_table_a WHERE ds > "20180101" ) s LEFT JOIN (SELECT * FROM test_table_b WHERE ds > "20180101") d ON s.origin = d.id;
```

##### MAPJOIN HINT

##### 背景信息

当一个大表和一个或多个小表JOIN时，您可以在SELECT语句中显式指定MAPJOIN以提升查询性能。 通常情况下，JOIN操作在Reduce阶段执行表连接。整个JOIN过程包含Map、Shuffle和Reduce三个阶段。 MAPJOIN在Map阶段执行表连接，而非等到Reduce阶段才执行表连接。这样就节省了大量数据传输的时间以及系统资源，从而起到了优化作业的作用。 MAPJOIN在Map阶段会将指定表的数据全部加载在内存中。因此指定的表仅能为小表，且表被加载到内存后占用的总内存不得超过512 MB。 在大表和一个或多个小表JOIN的场景下，MAPJOIN会将您指定的小表全部加载到执行JOIN操作的程序的内存中，在Map阶段完成表连接从而加快JOIN的执行速度。

**使用方法**

您需要在SELECT语句中使用Hint提示 `/*+ MAPJOIN(table) */` 才会执行MAPJOIN。 假设表sale_detail为大表，别名为b，表shop为小表，别名为a。 普通JOIN操作，查询语句如下。

```
SELECT a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

使用MAPJOIN，查询语句如下。

```
SELECT /* + MAPJOIN(a) */
        a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

##### 使用限制

使用MAPJOIN时，在引用小表或子查询时，需要引用别名。 MAPJOIN支持小表为子查询。 LEFT OUTER JOIN的左表必须是大表。 RIGHT OUTER JOIN的右表必须是大表。 大数据计算服务 INNER JOIN的左表或右表均可以作为大表。 FULL OUTER JOIN不能使用MAPJOIN。

| 多个条件。您可以通过不写ON语句而通过 | MAPJOIN |
|---|---|

| ON 1 = 1 | 的形式，实现笛卡 |
|---|---|

MaxCompute在MAPJOIN中最多支持指定128张小表，否则报语法错误。MAPJOIN中多个小表用半角逗号（,）隔开，例如 `/*+MAPJOIN(a,b,c)*/` 。 如果使用MAPJOIN，则小表占用的总内存不得超过512 MB。由于MaxCompute是压缩存储，因此小表在被加载到内存后，数据大小会急剧膨胀。此处的512 MB是指加载到内存后的空间大小。 MAPJOIN时小表需要先写入到内存，再分发到每台机器和大表本地数据关联计算。默认情况下，小表会根据每200个mapper文件起一个mincopy的规则进行复制，即小表副本数=大表分区数或文件数`/200` 。如果大表分区内文件切分很小或分区很多，最终小表副本数也会很多，副本数超过集群剩余可用台数会报错。例如1200个分区会产生6个副本，而6台计算节点中有一台故障会造成可复制机器数小于副本数错误。此时您可以调整SQL输入大表分区数或调整切片文件大小减少并发，例如使用 `set` odps.sql.mapper.split.size=<value>; 命令调整切片文件大小。

##### 使用示例

MaxCompute SQL不支持在普通JOIN的ON条件中使用不等值表达式、OR逻辑等复杂的JOIN条件，但是在 MAPJOIN中可以进行上述操作。

```
SELECT /* + MAPJOIN(a) */
        a.total_price,
        b.total_price
FROM shop a JOIN sale_detail b ON a.total_price < b.total_price OR a.total_price + b.total_price < 500;
```

##### SELECT TRANSFORM

###### 概述

Select Transform语法允许您启动一个指定的子进程，将输入数据按照一定的格式通过标准输入至子进程，并且通过解析子进程的标准输出获取输出数据。Select Transform让您无需编写UDF，便可以实现命令格式如下。

```
(ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value)) USING 'unix_command_line' ( AS col1, col2 ...) (ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value))
```

参数说明：
**SELECT TRANSFORM**：关键字，可以用**MAP**或**REDUCE**关键字替换，语义是完全一样的为使语法
大数据计算服务关键字可以用或关键字替换语义是完全样的为使语法
**(arg1, arg2 ...)**：指定输入数据。其格式和SELECT语句类似。默认格式下，参数的各个表达式结果在
隐式转换成STRING类型后，用**\t**拼接，输入到子进程中。 这个格式是可以配置的，具体信息请参考后面关于**ROW FORMAT**的解释说明。

**说明**

**USING****子句**：指定要启动的子进程的命令。此处需要注意以下两点：
大多数的MaxCompute SQL命令中USING子句指定的是资源（Resources），但此处使用USING子句指定的子进程的命令。使用USING子句是为了和Hive的语法兼容。 USING中的格式和Shell的语法类似，但并非真的启动Shell来执行，而是直接根据命令的内容创建子进程。因此，很多Shell的功能不能使用。例如输入输出重定向、管道、循环等。如果有需要，Shell本身也可以作为子进程命令来使用。

| using ‘sh foo.sh bar.txt’ resources ‘foo.sh’,’bar.txt’ |  |
|---|---|
| 句前使用 | set odps.sql.session.resources=foo.sh,bar.txt; |

定资源。 此配置是全局配置，即整个SQL中所有的**SELECT TRANSFORM**都可以访问此资

**说明**

源。多个资源文件之间使用英文逗号（,）分隔。
**ROW FORMAT****子句**：允许自定义输入输出的格式。语法中有两个ROW FORMAT子句，第一个子句指
定输入的格式，第二个指定输出的格式。默认情况下使用**\t**作为列分隔符，使用**\n**作为行分隔符，使

| 说明 field delimiter、character escape和line separator只接受一个字符，如果指定的是字 _ _ _ 符串，则以第一个字符为准。 MaxCompute支持Hive指定格式的语法，例如inputRecordReader、outputRecordReader、SerDe等，但您需要打开Hive兼容模式才能使用。打开方式为在SQL语句前加set语句 set odps.sql.hive.compatible=true; 。 如果使用Hive的inputRecordReader、outputRecordReader等自定义类，可能会降低执行性能。 |  |  |
|---|---|---|
|  | set |  |

**AS****子句**：指定输出列。

**说明**

输出列可以不指定类型，默认为STRING类型。 由于输出数据实际是解析子进程标准输出获取的，如果指定的数据不是STRING类型，系统会隐式调用CAST函数进行转换，转换过程有可能出现运行异常。 输出列类型不支持部分指定。 关键字AS可以省略，此时默认标准输出数据中第一个**\t**之前的字段为Key，后面的部分全部为

###### SELECT TRANSFORM示例

###### 调用Shell脚本示例

本章节为您介绍如何使用Select Transform实现Shell脚本调用，并提供参考示例。 假设通过Shell脚本生成50行数据，值是从1到50，对应data字段输出如下。 大数据计算服务

```
FROM (
            SELECT  'for i in `seq 1 50`; do echo $i; done' AS script
        ) t
;
```

此时，可以直接将Shell命令作为TRANSFORM数据输入。

**说明**

Select Transform不仅是语言支持的扩展，一些简单的功能，例如AWK、Python、Perl和Shell都支持直接在命令中写脚本，不需要专门编写脚本文件、上传资源等，开发过程更简单。 如果出现功能复杂的情况，您可以上传脚本文件来执行，详细信息请参见调用Python脚本示例。

###### 调用Python脚本示例

本章节为您介绍如何使用Select Transform实现Python脚本调用，并提供参考示例。
1. 准备Python文件，假设脚本文件名为myplus.py，示例代码如下。

```java
#!/usr/bin/env python
import sys line = sys.stdin.readline() while line:
    if (token[0] == '\\N') or (token[1] == '\\N'):
        print '\\N'
    else:
        print str(token[0]) +'\t' + str(token[1])
    line = sys.stdin.readline()
```

2. 将该Python脚本文件添加为MaxCompute资源（Resource）。

```
add py ./myplus.py -f;
```

3. 使用Select Transform语法调用资源。
`--` 创建测试表。

```
CREATE TABLE testdata(c1 bigint,c2 bigint);
```

`--` 测试表中插入测试数据。

```
INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); TRANSFORM (testdata.c1, testdata.c2) AS (result1,result2) FROM testdata;
```

`--` 等同于下面语句。

```
set odps.sql.session.resources=myplus.py; USING 'python myplus.py' AS (result1,result2) FROM testdata;
```

大数据计算服务 MaxCompute也支持直接将Python命令作为TRANSFORM数据输入。例如调用Shell

**说明**

脚本示例也可以用Python命令实现。

```
SELECT TRANSFORM('for i in xrange(1, 50): print i;') USING 'python' AS (data);
```

返回结果如下。

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

###### 调用Java脚本示例

本章节为您介绍如何使用Select Transform实现Java脚本调用，并提供参考示例。 与调用Python脚本类似，在本例中，您需要编辑好Java文件，导出JAR包，再通过 `ADD FILE` 方式将JAR
1. 准备好JAR文件，假设脚本文件名为Sum.jar，示例代码如下。

```java
package com.aliyun.odps.test; import java.util.Scanner public class Sum {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            String s = sc.nextLine();
            String[] tokens = s.split("\t");
                throw new RuntimeException("illegal input");
            }
            if (tokens[0].equals("\\N") || tokens[1].equals("\\N")) {
                System.out.println("\\N");
            }
            System.out.println(Long.parseLong(tokens[0]) +
Long.parseLong(tokens[1]));
        }
    }
}
```

2. 将JAR文件添加为MaxCompute的资源。

```
add jar ./Sum.jar -f;
```

3. 使用Select Transform语法调用资源。
大数据计算服务 `--` 创建测试表。

```
CREATE TABLE testdata(c1 bigint,c2 bigint);
```

`--` 测试表中插入测试数据。

```
INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' resources 'Sum.jar' FROM testdata;
```

`--` 等同于如下语句。

```
set odps.sql.session.resources=Sum.jar; SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' FROM testdata;
```

返回结果如下。

```
+-----+
| cnt |
+-----+
| 5   |
| 7   |
| 9   |
+-----+
```

大多数Java的方法可以直接使用本方法运行。 Java和Python虽然有现成的UDTF框架，但是用Select Transform编写更简单、不需要额外依赖以及没有格式要求，甚至可以实现直接使用离线脚本（Java和Python离线脚本的实际路径，可以从JAVA_HOME和 PYTHON_HOME环境变量中得到）。

###### 调用其他脚本语言

本章节为您介绍如何使用Select Transform实现其他脚本语言调用，并提供参考示例。 Select Transform不仅仅支持上述语言扩展，还支持其它的常用Unix命令或脚本解释器，例如AWK、Perl 等。 调用AWK，将第二列原样输出，示例如下。

```
SELECT TRANSFORM(*) USING "awk '//{print $2}'" as (data) from testdata;
```

调用Perl，示例如下。

```
SELECT TRANSFORM (testdata.c1, testdata.c2) USING "perl -e 'WHILE($input = <STDIN>){pri nt $input;}'" FROM testdata;
```

由于MaxCompute计算集群上未部署PHP和Ruby，所以不支持调用这两种脚本。

**说明**

###### 串联使用示例

本章节为您介绍如何使用Select Transform实现串联使用，并提供参考示例。 Select Transform还可以串联使用，例如使用DISTRIBUTE BY和SORT BY对输入数据做预处理。 大数据计算服务

```
(
    (
        SELECt * FROM data DISTRIBUTE BY col2 SORT BY col1
    ) t DISTRIBUTE BY key SORT BY value
) t2;
```

或使用MAP、REDUCE关键字，可能更符合某些用户的认知习惯。

```
@a := select * from data distribute by col2 sort by col1; @b := map * using 'cmd1' distribute by col1 sort by col2 from @a; reduce * using 'cmd2' from @b;
```

###### 性能优势

性能方面，通常是拿Select Transform和UDTF进行比较。在大多数场景下，Select Transform相对有优势，而在数据量大时，则是UDTF相对有优势。同时，由于Select Transform的开发更加简便，因此在做两者优势如下所示。

**UDTF的优势**

UDTF的输出结果和输入参数支持多种数据类型，而Select Transform的子进程基于标准输入和标准输出传输数据，所有数据都当做STRING类型处理，因此Select Transform比UDTF多了一步类型转换。 Select Transform数据传输依赖于操作系统的管道，而目前管道的缓存仅有4 KB且不能设置。Select Transform读空或管道写满会导致进程被挂起。 子进程和父进程是两个进程，而UDTF是单线程的，如果计算占比比较高，数据吞吐量比较小，Select Transform可以利用服务器的多核特性。 数据的传输通过更底层的系统调用来读写，效率比Java高。 Select Transform支持的部分工具，例如AWK是由Natvie代码实现的。理论上，和Java相比，使用

##### GROUPING SETS

###### 概述

对于经常需要对数据进行多维度的聚合分析的场景，您既需要对a列做聚合，也要对b列做聚合，同时还要按照a、b两列同时做聚合，因此需要多次使用UNION ALL。使用Grouping Sets功能可以快速解决此类问题。 MaxCompute中的Grouping Sets功能是对SELECT语句中Group By子句的扩展，允许您采用多种方式对结果分组，而不必使用多个SELECT语句来实现这一目的。这样能够使MaxCompute的引擎给出更有效的执行计划，从而提高执行性能。 大数据计算服务在下面章节的示例中，大部分采用MaxCompute Studio进行展示。因此，建议您安

**说明**

装MaxCompute Studio后，再进行后续操作。

###### 实现示例

示例如下。
1. 准备数据。

```
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city);
```

2. 使用Grouping Sets进行分组。

```
FROM requests GROUP BY os, device, city GROUPING SETS((os, device), (city), ());
```

返回结果如下。

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

本示例中，其实也可以使用多个SELECT语句进行分组，两种方式产生的结果是相同的。

```
FROM requests FROM requests GROUP BY os, device FROM requests GROUP BY city;
```

大数据计算服务分组集中不使用的表达式，会使用NULL充当占位符，使得这些结果集可以做UNION操

**说明**

作。

###### CUBE和ROLLUP函数

CUBE和ROLLUP可以认为是特殊的Grouping Sets。其中，CUBE会枚举指定列的所有可能组合作为 Grouping Sets，而ROLLUP会以按层级聚合的方式产生Grouping Sets。 示例如下。

```
GROUP BY CUBE(a, b, c)
```

`--`等价于以下语句。

```
GROUP BY ROLLUP(a, b, c)
```

`--`等价于以下语句。

```
GROUP BY CUBE ( (a, b), (c, d) )
```

`--`等价于以下语句。

```
    ( a, b, c, d ),
    ( a, b       ),
    (       c, d ),
    (            )
```

)

```
GROUP BY ROLLUP ( a, (b, c), d )
```

`--`等价于以下语句。

```
    ( a, b, c, d ),
    ( a, b, c    ),
    ( a          ),
    (            )
```

) `--`等价于以下语句。

```
    (a, b, c, d), (a, b, c, e),
    (a, b, d),    (a, b, e),
    (a, c, d),    (a, c, e),
    (a, d),       (a, e)
```

) `--`等价于以下语句。

```
    (b), (c),
    (a,b,c), (a,b), (a), ()
```

) 大数据计算服务

###### GROUPING和GROUPING_ID函数

本章节为您介绍Grouping Sets中的GROUPING和GROUPING_ID函数。 Grouping Sets结果中使用NULL充当占位符。会导致您无法区分占位符NULL与数据中真正的NULL。因此，MaxCompute为您提供了GROUPING函数。 GROUPING函数接受一个列名作为参数。如果结果对应行使用了参数列做聚合，返回0，此时意味着NULL 来自输入数据。否则将返回1，此时意味着NULL是Grouping Sets的占位符。 MaxCompute还提供了GROUPING_ID函数，此函数接受一个或多个列名作为参数。结果是将参数列的 GROUPING结果按照BitMap的方式组成整数。 示例如下。

```
SELECT a,b,c ,COUNT(*), GROUPING(a) ga, GROUPING(b) gb, GROUPING(c) gc, GROUPING_ID(a,b,c) groupingid GROUP BY CUBE(a,b,c);
```

返回结果如下。

```
+------------+------------+------------+------------+------------+------------+---------- -+------------+
| a          | b          | c          | _c3        | ga         | gb         | gc
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

默认情况，GROUP BY列表中不被使用的列，会被填充为NULL。您可以通过GROUPING函数输出更有实际意义的值。 大数据计算服务 `--`准备表数据

```
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city);
```

`--`命令示例

```
  if(grouping(os) == 0, os, 'ALL') as os,
  if(grouping(device) == 0, device, 'ALL') as device,
  if(grouping(city) == 0, city, 'ALL') as city,
from requests group by os, device, city grouping sets((os, device), (city), ());
```

返回结果如下。

```
+------------+------------+------------+------------+ +------------+------------+------------+------------+
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

##### 交集、并集和补集

本章节为您介绍UNION、UNOIN ALL、UNION DISTINCT，INTERSECT、INTERSECT ALL、 INTERSECT DISTINCT交集，EXCEPT、EXCEPT ALL、EXCEPT DISTINCT补集等SQL语法。 语法格式如下。

```
select_statement UNION ALL select_statement; select_statement UNION [DISTINCT] select_statement; select_statement INTERSECT ALL select_statement; select_statement INTERSECT [DISTINCT] select_statement; select_statement EXCEPT ALL select_statement; select_statement EXCEPT [DISTINCT] select_statement; select_statement MINUS ALL select_statement; select_statement MINUS [DISTINCT] select_statement;
```

参数说明： 大数据计算服务 UNION：求两个数据集的并集，即将两个数据集合并成一个数据集。 INTERSECT：求两个数据集的交集。即输出两个数据集均包含的记录。 EXCEPT：求第二个数据集在第一个数据集中的补集。即输出第一个数据集包含而第二个数据集不包含的记录。 MINUS：等同于EXCEPT。 示例如下。 UNION示例： 当UNION后指定参数ALL时，返回两个数据集的所有记录。

```
SELECT * FROM VALUES (1, 2), (1, 4) t(a, b);
```

返回结果如下。

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+ SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3);
```

当UNION后不指定参数时，返回记录中会去掉重复的记录，效果等同于UNION DISTINCT。

```
SELECT * FROM VALUES (1, 2), (1, 4) t(a, b);
```

`--` 等同于如下语句。

```
SELECT DISTINCT * FROM (<UNION ALL的结果>）t;
```

返回结果如下。

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 3          | 4          |
+------------+------------+
```

| set odps.sql.type.system.odps2=false; |  | 时，其作用于UNION的最后一 |
|---|---|---|
| select statement；当设置 _ |  |  |

```
set odps.sql.type.system.odps2=true; SELECT explode(array(3, 1)) AS (a) UNION ALL SELECT explode(array(0, 4, 2)) AS (a) OR DER BY a LIMIT 3;
```

大数据计算服务返回结果如下。

```
+------+
| a    |
+------+
| 0    |
| 1    |
| 2    |
+------+
```

INTERSECT示例： INTERSECT ALL示例。

```
INTERSECT ALL SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

返回结果如下。

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

INTERSECT DISTINCT示例。

```
INTERSECT DISTINCT SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

返回结果如下，等同于 `SELECT DISTINCT * FROM (< INTERSECT ALL`的结果 >) t; 。

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

EXCEPT示例： EXCEPT ALL示例。

```
EXCEPT ALL SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b);
```

返回结果如下。 大数据计算服务

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

EXCEPT DISTINCT示例。

```
EXCEPT SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b); 返回结果如下，等同于 SELECT DISTINCT * FROM left_branch EXCEPT ALL SELECT DISTINCT * FROM right_branch; 。 +------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 7          | 8          |
+------------+------------+
```

**说明**

集合操作的结果不保证排序。 集合操作左右两个分支要求列个数必须一致。同时，如果类型不一致，可能会插入隐式类型转换。由于兼容性原因，MaxCompute禁用了STRING类型和非STRING类型在集合操作中的隐式转换。 MaxCompute最多允许256个分支的集合操作，超出将报错。

#### EXPLAIN语句

该语句可以显示对应的DML语句执行计划（执行计划是指用于执行SQL语义的程序）的结构。 命令格式如下。

```
EXPLAIN <DML query>;
```

**说明**

EXPLAIN的执行结果包含： Task中所有Task的依赖结构。 Task中所有Operator的依赖结构。 示例如下。 大数据计算服务

```
SELECT abs(a.key), b.value FROM src a JOIN src1 b ON a.value = b.value;
```

Explain的输出结果包含如下三个部分： Job间的依赖关系： `job0 is root job` 。因为该查询只需要一个**Job**（**job0**），所以只显示一行信息。 Task间的依赖关系。

```
In Job job0: root Tasks: M1_Stg1, M2_Stg1 J3_1_2_Stg1 depends on: M1_Stg1, M2_Stg1
```

**说明**

job0包含三个Task，M1_Stg1和M2_Stg1两个Task会先执行，两者执行完成后 J3_1_2_Stg1执行。 Task的命名规则：在MaxCompute中，共有四种Task类型：MapTask、ReduceTask、 JoinTask和LocalWork。Task名称的第一个字母表示了当前Task的类型（如M2Stg1就是一个MapTask）；紧跟着第一个字母后的数字代表了当前Task的ID，这个ID在所有对应当前 query的Task中是唯一的；之后用下划线（_）分隔的数字代表了当前Task的直接依赖（如 J3_1_2_Stg1意味着当前Task（ID为3）依赖ID为1和ID为2的两个Task）。 Task中的Operator结构，Operator串描述了一个Task的执行语义。

```
In Task M1_Stg1:
  Data source: yudi_2.src                       # "Data source"描述了当前Task的输入内容。
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

各个Operator的含义如下所示。

| Operator名称 | 含义 |
|---|---|

大数据计算服务

| TableScanOperator | 描述了查询语句中的FROM语句块的逻辑。EXPLAIN结果中会显示输入表的名称（Alias）。 |
|---|---|
| SelectOperator | 描述了查询语句中的SELECT语句块的逻辑。EXPLAIN结果中会显示向下一个Operator传递的列，多个列由逗号分隔。 如果是列的引用，则显示为< alias >.< column name >。 _ 如果是表达式的结果，则显示为函数形式，例如func1(arg1 1, _ arg1 2, func2(arg2 1, arg2 2))。 _ _ _ 如果是常量，则直接显示值内容。 |
| FilterOperator | 描述了查询语句中的WHERE语句块的逻辑。EXPLAIN结果中会显示一个WHERE条件表达式，形式类似SelectOperator的显示规则。 |
| JoinOperator | 描述了查询语句中的JOIN语句块的逻辑。EXPLAIN结果中会显示哪些表以哪种方式Join在一起。 |
| GroupByOperator | 描述了聚合操作的逻辑。如果查询中使用了聚合函数，就会出现该结构，EXPLAIN结果中会显示聚合函数的内容。 |
| ReduceSinkOperator | 描述了Task间数据分发操作的逻辑。如果当前Task的结果会传递给另一个Task，则必然需要在当前Task的最后，使用 ReduceSinkOperator执行数据分发操作。EXPLAIN的结果中会显示输出结果的排序方式、分发的Key、Value以及用来求Hash值的列。 |
| FileSinkOperator | 描述了最终数据的存储操作。如果查询中有INSERT语句块，EXPLAIN结果中会显示目标表名称。 |
| LimitOperator | 描述了查询语句中的LIMIT语句块的逻辑。EXPLAIN结果中会显示 LIMIT数。 |
| MapjoinOperator | 类似JoinOperator，描述了大表的JOIN操作。 |

**说明**

如果查询语句足够复杂，EXPLAIN的结果太多，则会触发API的限制，无法得到完整的 EXPLAIN结果。此时您可以拆分查询，对各部分分别执行EXPLAIN语句，以了解Job的结构。 最多查询的partition数目不超过10000个，输入的partition过多，会导致**Data source**的内容过长。此时可以通过在query中加入partition的过滤条件，过滤掉大部分的partition， 以此规避这个限制。

#### IF语句

MaxCompute SQL支持IF-ELSE分支语句。您可以通过IF-ELSE语句，实现脚本的条件执行。其中，条件可以为普通变量，也可以是结果为1行1列的子查询（Scalar SubQuery）。 IF语句，可以让程序根据条件，自动选择执行逻辑。MaxCompute的IF语法有如下几种。 大数据计算服务

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

BEGIN和END内部只有1条语句，则可以省略（类似于Java中的’{ }’）。

**说明**

IF语句中的Condition可以有2种：分别是BOOLEAN表达式和类型为BOOLEAN的Scalar subquery。 BOOLEAN的表达式：这种类型的IF-ELSE可以在编译阶段决定执行哪个分支，示例如下。

```
@date := '20190101';
```

@row TABLE(id STRING); --声明变量`row`，其类型为`TABLE`，`Schema`为`STRING`。

```
IF ( cast(@date as bigint) % 2 == 0 ) BEGIN @row := SELECT id from src1; END ELSE BEGIN @row := SELECT id from src2; END INSERT OVERWRITE TABLE dest SELECT * FROM @row;
```

类型为BOOLEAN的Scalar subquery：这种类型的IF-ELSE在编译阶段无法决定执行哪个分支，在运行时才能决定。因此，需要提交多个作业，示例如下。

```
@i bigint; @t table(id bigint, value bigint); @i := 1; @t := select @i, @i*2; END ELSE BEGIN @i := 2; @t := select @i, @i*2; END select id, value from @t;
```

#### Update/Delete语句

Update/Delete是MaxCompute在行级别操纵表或者分区数据的语句。

##### 背景信息

目前，MaxCompute DML对表的部分行进行更新和删除时，仅支持使用Insert Overwrite和Insert Into 语句，表达能力受限。例如用户需要订正表或分区中的少量数据，如果使用Insert语句，需要读取全量数据，Select做数据订正之后，Insert写回全量数据，效率较低,。使用Update/Delete语句之后，Query读写数据量显著下降。 大数据计算服务此外，以前处理批量更新场景的最佳实践是使用拉链表，该方式需要在表中增加**start_date**和**end_date**等辅助列，表示某一行记录的生命周期。查询当前状态时需要从大量数据中根据时间戳找到最新状态，使用上不够直观。使用Update/Delete语句之后，可以直接读取当前表。

##### 功能介绍

Delete语句实际运行时，系统会生成Delta文件，Delta文件中使用**txnid(bigint**)和**rowid(bigint)**表示 Base文件中哪个Transaction中的哪些行被删除。

**说明**

Delta文件中存储了行号，标示原文件中的哪些行被删除了。 如果再做一次删除，则又会生成一个f2.del文件。第二个文件编号仍然是根据Base文件编号，读取时候会把所有Delta文件一起比较，显示没有删除的数据。 Update语句会转成Delete和Insert Into逻辑，原理相同。 当作业并发运行且操作目标表相同时，可能出现冲突，详细说明请参见MaxCompute并发写行为的ACID语义。

**注意事项**

Update/Delete操作必须基于Transactional表，Transactional表的创建方法请参见创建表。 执行Update操作时，必须增加 set odps.service.mode=off; 属性配置，并与Update语句一起提交执行。 如果更新或删除行的占比较小，对该表读取性能影响不大，建议直接使用Update/Delete语句。具体阈值和用户场景相关，通常建议更新或删除行的占比在5%以下时使用。 如果更新或删除行的数量不多但是操作次数较多，建议您在使用Update/Delete语句完成多次更新或删除行的操作之后，使用Compact语句降低表的实际存储。 如果更新或删除行的数量较多但是操作不频繁，并且后续对该表读取操作较频繁，建议您使用原本的 Insert Overwrite和Insert Into语句。例如业务场景为每次更新或删除10%的数据，一天更新10次。此时建议根据实际情况评估使用Update/Delete语句的代价加上产生的Delta文件对读取的性能消耗之和是否小于每次都使用Insert Overwrite和Insert Into语句的代价加上读取的性能消耗之和，比较两种方式在具体场景中的效率，选择更优方案。 因为删除数据会生成Delta文件，所以删除数据不一定能降低存储，如果希望通过Delete操作删除数据降低存储，可以使用Alter Table Compact语句将Base文件和Delta合并，减少存储。

##### 使用限制

在DataWorks数据开发的Odps SQL模式下，使用Alter Table Compact语句存在版本兼容性问题。请使用Odpscmd，且Odpscmd需要升级到0.35.0版本。 只允许创建表时设置Transactional属性，已有表不允许通过Alter Table Compact语句修改 Transactional属性，类似如下语句会报错。

```
alter table not_txn_tbl set tblproperties("transactional"="true"); -- 报错信息为FAILED: Catalog Service Failed, ErrorCode: 151, Error Message: Set transac tional is not supported。
```

聚簇表（Cluster Table）及外部表不能设置成Transactional表。 现有内部表和外部表不支持转成Transactional表，Transactional表也不支持转成普通表。 暂不支持外围其他系统的任务（如Graph、PAI等Task），此类任务访问Transactional表会报错。 Transactional表不支持Clone Table、Merge Partition及增量复制等操作。 对Transactional表数据进行Update、Delete及Insert Overwrite操作时，请您提前对重要数据进行手工备份。 大数据计算服务 Update/Delete表需要如下权限：Table Select和Table Update权限。

**删除行（Delete）**

命令格式如下。

```
delete from <table_name> [WHERE where_condition];
```

用途：用于删除表中部分行。 示例如下。 示例一：删除表的部分行。 `--`创建`Transactional`表。

```
create table if not exists acid_delete(id bigint) tblproperties ("transactional"="true");
```

`--`插入数据。

```
insert overwrite table acid_delete values(1),(2),(3);
```

`--`查看插入结果。

```
select * from acid_delete;
```

返回结果如下。

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+
```

`--`删除`id`为2的行`,Odpscmd`中需要输入`Yes`或`No`确认。

```
delete from acid_delete where id = 2;
```

`--`读取数据，表中数据只有1、3。

```
select * from acid_delete;
```

返回结果如下。

```
+------------+
| id         |
+------------+
| 1          |
| 3          |
+------------+
```

示例二：删除分区表部分行。 大数据计算服务 `--`创建`Transactional`表。

```
create table if not exists acid_delete_pt(id bigint) partitioned by(ds string) tblprope rties ("transactional"="true");
```

`--`添加分区。

```
alter table acid_delete_pt add if not exists partition (ds= '2019');
```

`--`插入数据。

```
insert overwrite table acid_delete_pt partition (ds='2019') values(1),(2),(3);
```

`--`查看插入结果。

```
select * from acid_delete_pt where ds = '2019';
```

返回结果如下。

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+
```

`--`删除分区上的数据`,Odpscmd`中需要输入`Yes`或`No`确认。

```
delete from acid_delete_pt where ds='2019' and id= 2;
```

`--`读取数据，表中数据只有1、3。

```
select * from acid_delete_pt where ds = '2019';
```

返回结果如下。

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

**更新行（Update）**

命令格式如下。

```
update <table_name> set col1 = value1 [, col2 = value2 ...] [WHERE where_condition]; update <table_name> set (col1 [, col2 ...]) = (value1 [, value2 ...]);
```

用途：用于将表中部分Cell数据更新成新的值。

**说明**

Update语句实际系统实现，是将Update语句转成了Delete和Insert Into语句。 示例如下。 示例一：涉及单个表的Update。 大数据计算服务 `--`创建`Transactional`表。

```
create table if not exists acid_update(id bigint) tblproperties ("transactional"="true");
```

`--`插入数据。

```
insert overwrite table acid_update values(1),(2),(3);
```

`--`查看插入结果。

```
select * from acid_update;
```

返回结果如下。

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+
```

`--`更新一列，将所有`id`为2的行，`id`值更新成4。

```
set odps.service.mode=off; update acid_update set id = 4 where id = 2;
```

`--`查看更新结果，2被更新为4。

```
select * from acid_update;
```

返回结果如下。

```
+------------+
| id         |
+------------+
| 4          |
| 1          |
| 3          |
+------------+
```

示例二：更新分区表部分行。 `--`创建`Transactional`表。

```
create table if not exists acid_update_pt(id bigint) partitioned by(ds string) tblprope rties ("transactional"="true");--添加分区
```

`--`添加分区。

```
alter table acid_update_pt add if not exists partition (ds= '2019');
```

`--`插入数据。

```
insert overwrite table acid_update_pt partition (ds='2019') values(1),(2),(3);
```

`--`查看插入结果。

```
select * from acid_update_pt where ds = '2019';
```

返回结果如下。 大数据计算服务

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+
```

`--`更新分区上的数据，将分区为`2019`的所有`id=2`的行，`id`值更新成4。

```
set odps.service.mode=off; update acid_update_pt set id = 4 where ds = '2019' and id = 2;
```

`--`查看更新结果，2被更新为4。

```
select * from acid_update_pt where ds = '2019';
```

返回结果如下。

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 4     | 2019   |
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

示例三：更新多列及关联更新。 大数据计算服务 `--`创建更新目标表`acid_update_t`和关联表`acid_update_s`

```
create table if not exists acid_update_t(id bigint,value1 bigint,value2 bigint) tblprop erties ("transactional"="true"); create table if not exists acid_update_s(id bigint,value1 bigint,value2 bigint);
```

`--`插入数据

```
insert overwrite table acid_update_t values(2,20,21),(3,30,31),(4,40,41); insert overwrite table acid_update_s values(1,100,101),(2,200,201),(3,300,301);
```

`--1.`用常量更新。

```
set odps.service.mode=off; update acid_update_t set (value1, value2) = (3, 4);
```

`--2.`关联更新, 规则为`acid_update_t`表左关联`acid_update_s`表，如果只更新`acid_update_t`中与`acid_upda`

```
set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s w here acid_update_t.id = acid_update_s.id);
```

`--3.`关联更新，目标表增加过滤条件，只取交集。

```
set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s w here acid_update_t.id = acid_update_s.id) where acid_update_t.id in (select id from aci d_update_s);
```

`--4.`用汇总结果关联更新。

```
set odps.service.mode=off; update acid_update_t set (id, value1, value2) = (select id, max(value1),max(value2) fro m acid_update_s where acid_update_t.id = acid_update_s.id group by acid_update_s.id) wh ere acid_update_t.id in (select id from acid_update_s);
```

**Merge Into**

Merge Into语句能将Insert、Update及Delete操作并为一句，根据与源表联接的结果，对目标表执行插入、更新或删除操作。 MaxCompute DML为了丰富表达能力新支持了Update/Delete语句，但当同时需要使用多个Update、 Delete和Insert对目标表进行批量更新操作时，需要写多个语句进行多次全表扫描才能完成相关操作。而 Merge Into语句只需要写一个Query进行一次全表扫描就可以完成全部工作，执行效率高于Insert＋ Update + Delete。 同时Merge Into语句整体作为一个操作具备原子性，在一批任务中Insert、Update及Delete都成功时任务才成功，任意一个内部逻辑失败则整体失败，避免了分别操作Insert、Dpdate和Delete，结果可能部分成功部分失败，其中成功部分无法回退的问题。 命令格式如下。

```
MERGE INTO <target table> AS T USING <source expression/table> AS S ON <boolean expression1> WHEN MATCHED [AND <boolean expression2>] THEN UPDATE SET <set clause list> WHEN MATCHED [AND <boolean expression3>] THEN DELETE WHEN NOT MATCHED [AND <boolean expression4>] THEN INSERT VALUES <value list>
```

用途：通过Merge Into语句将源表**source expression/tabletarget table**中。 参数说明： 大数据计算服务
**ON**：用来进行源表和目标表的数据关联判断，**boolean expression**是判断条件，判断结果必须为是
或否。
**WHEN MATCHED…THEN**：指定**ON**的判断结果为是时的行为，多个**WHEN MATCHED [AND**
**<boolean expression>]**之间的数据必须没有交集。Merge Into是一个目标性明确的语句，不允许
在一个Merge Into语句中对相同的行进行Insert或Update操作，即需要保证符合联接ON条件的源表的数据是唯一的，否则执行时会报错。

**说明**

当Merge Into语句中有三个WHEN子句时，UPDATE、DELETE和INSERT操作在子句中每个最多出现一次。
**WHEN NOT MATCHED**只能出现在最后一个WHEN子句，并且只能是INSER操作。
如果UPDATE和DELETE操作同时出现，先出现的操作必须包括**[AND <boolean**
**expression>]**。
示例如下。 准备数据。 `--`创建目标表。

```
create table if not exists acid_address_book_base1 (id bigint,first_name string,last_name string,phone string) partitioned by(year string, month string, day string, hour string) tblproperties ("transactional"="true");
```

`--`创建源表。

```
(id bigint, first_name string, last_name string, phone string, _event_type_ string);
```

`--`向目标表插入测试数据。

```
partition(year='2020', month='08', day='20', hour='16') values (4, 'nihaho', 'li', '222'), (5, 'tahao', 'ha', '333'), (7, 'djh', 'hahh', '555');
```

`--`向源表插入测试数据。

```
(1, 'hh', 'liu', '999', 'I'), (2, 'cc', 'zhang', '888', 'I'), (3, 'cy', 'zhang', '666', 'I'),(4, 'hh', 'liu', '999', 'U'), (5, 'cc', 'zhang', '888', 'U'),(6, 'cy', 'zhang', '666', 'U');
```

执行Merge Into操作，对符合ON条件的数据，用源表的数据对目标表进行更新操作；对不符合ON条件并且满足源表的**event_type**为I的数据，将其插入到目标表。

```
merge into acid_address_book_base1 as t using tmp_table1 as s on s.id = t.id and t.year='2020' and t.month='08' and t.day='20' and t.hour='16' when matched then update set t.first_name = s.first_name, t.last_name = s.last_name, t.phone = s.pho
```

`ne`

```
when not matched and (s._event_type_='I') then insert values(s.id, s.first_name, s.last_name,s.phone,'2020','08','20','16');
```

`--`执行完成后查询目标表。

```
select * from acid_address_book_base1;
```

返回结果如下。 大数据计算服务

```
+------------+------------+-----------+-------+------+-------+-----+------+ +------------+------------+-----------+-------+------+-------+-----+------+
| 4          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 5          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 7          | djh        | hahh      | 555   | 2020 | 08    | 20  | 16   |
| 1          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 2          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 3          | cy         | zhang     | 666   | 2020 | 08    | 20  | 16   |
+------------+------------+-----------+-------+------+-------+-----+------+
```

**Transactional表文件合并**

Transactional表执行Delete语句不会修改原始文件，只会追加delta文件，所以会出现删除次数越多，实际存储越大的情况。 另一方面，对同一个表或分区做了多次Delete操作，根据实际数据删除情况，可能会生成较多Delta文件 （Update会转成Delete+Insert Into，所以情况类似）。读数据的时候系统需要加载这些Delta文件来确定哪些行被删除，较多的Delta文件会影响数据读取效率。 此时可以使用Alter Table Compact语句将Base文件和Delta合并，减少存储和提升数据读取效率。 命令格式如下。

```
alter table <table_name> [partition (partition_key = 'partition_value' [, ...])] compac t [major|minor];
```

用途：用于将Base文件和Delta合并，减少存储和提升数据读取效率。
**Minor Compaction**：只将同一个Base File的所有Delta File与其Base File合并，不会跨Base File
合并。
**Major Compaction**：不仅将同一个Base File的所有Delta File与Base File合并，消除Delta File，
还会把表对应的多个Base文件中的小文件进行合并。在Base File较小（小于32 MB ）或有Delta File 情况下，逻辑上等价于重新将表Insert Overwrite一遍。但当Base File足够大（大于等于32 MB ）且不存在Delta File的情况下，不会重写。 示例如下。

```
alter table acid_delete compact minor; alter table acid_update_pt partition (ds = '2019') compact major;
```

返回结果如下。

```
Summary: table name: acid_update_pt /ds=2019 instance count: 2 run time: 16
  before merge, file count:        8  file size: 2423  file physical size: 7269
   after merge, file count:        2  file size: 642  file physical size: 1926
```

### 内建函数

#### 数学函数

##### ABS

大数据计算服务本文介绍如何在MaxCompute中使用数学函数ABS。

**操作说明**

###### 使用说明

计算绝对值。

**函数语法**

```
DOUBLE ABS(DOUBLE number); BIGINT ABS(BIGINT number) ; DECIMAL ABS(DECIMAL number);
```

**参数说明**

number：支持BIGINT、DOUBLE或DECIMAL类型，返回值类型与输入类型保持一致。若输入为 STRING类型，将隐式转换为DOUBLE类型后参与运算；输入其他类型则报错。

**返回值**

取决于输入参数的类型，包含DOUBLE、BIGINT或DECIMAL类型。如果输入参数为NULL，返回NULL。

**说明**

当输入BIGINT类型的值超过BIGINT的最大表示范围时，会返回DOUBLE类型，但可能会损失精度。

##### 使用示例

大数据计算服务

```
SELECT ABS(null);
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|  NULL |
+-------+ SELECT ABS(-1);
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|    1  |
+-------+ SELECT ABS(-1.2);
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|  1.2 |
+-------+ SELECT ABS("-2");
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|  2.0  |
+-------+ SELECT ABS(122320837456298376592387456923748);
```

`--` 返回结果

```
+------------------------+
|           _c0          |
+------------------------+
|  1.2232083745629837e32 |
+------------------------+
```

下面是一个完整的ABS函数在SQL中使用的示例，其他内建函数（除窗口函数、聚合函数外）的使用方式与其类似，不再一一举例。 大数据计算服务

```
    id BIGINT COMMENT '测试ID'
```

`) COMMENT 'ABS`函数测试表';

```
(10), (-25), (0), (NULL); SELECT ABS(id) FROM tbl1;
```

`--` 取`tbl1`表内`id`字段的绝对值。

##### ACOS

本文介绍如何在MaxCompute中使用数学函数ACOS。

**操作说明**

###### 使用说明

计算**number**的反余弦函数。

**函数语法**

```
DOUBLE ACOS(DOUBLE number); DECIMAL ACOS(DECIMAL number);
```

**参数说明**

**number**，DOUBLE类型或DECIMAL类型，取值范围是[-1,1]。如果输入为STRING类型或BIGINT类
型，会隐式转换到DOUBLE类型后参与运算。输入为其他类型时会报错。

**返回值**

DOUBLE类型或DECIMAL类型，值域在0~π之间。如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT ACOS("0.87");
```

`--` 返回结果

```
+---------------------+
|          _c0        |
+---------------------+
|  0.5155940062460905 |
+---------------------+ SELECT ACOS(0);
```

`--` 返回结果

```
+---------------------+
|         _c0         |
+---------------------+
|  1.5707963267948966 |
+---------------------+
```

大数据计算服务

##### ASIN

本文介绍如何在MaxCompute中使用数学函数ASIN，用于计算输入值的反正弦值。

**操作说明**

###### 使用说明

计算 `number` 的反正弦函数，返回值为弧度值。

**函数语法**

```
DOUBLE ASIN(DOUBLE number); DECIMAL ASIN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型，取值范围为[-1,1]。如果输入为STRING或BIGINT类型， 会隐式转换为DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型，值域在-π/2~π/2之间。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT ASIN(1);
```

`--` 返回结果

```
+----------------------+
|          _c0         |
+----------------------+
|  1.5707963267948966  |
+----------------------+ SELECT ASIN(-1);
```

`--` 返回结果

```
+----------------------+
|         _c0          |
+----------------------+
|  -1.5707963267948966 |
+----------------------+
```

##### ATAN

本文介绍如何在MaxCompute中使用数学函数ATAN，用于计算输入值的反正切值。

**操作说明**

###### 使用说明

计算number的反正切函数，返回值为弧度值。

**函数语法**

```
DOUBLE ATAN(DOUBLE number);
```

大数据计算服务

**参数说明**

number：必填，DOUBLE类型。如果输入为STRING或BIGINT类型，会隐式转换为DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型，值域在-π/2~π/2之间。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT ATAN(1);
```

`--` 返回结果

```
+----------------------+
|          _c0         |
+----------------------+
|  0.7853981633974483  |
+----------------------+ SELECT ATAN(-1);
```

`--` 返回结果

```
+----------------------+
|         _c0          |
+----------------------+
|  -0.7853981633974483 |
+----------------------+
```

##### CEIL

本文介绍如何在MaxCompute中使用数学函数CEIL，用于对输入值进行向上取整。

**操作说明**

###### 使用说明

向上取整，返回不小于输入值value的最小整数。

**函数语法**

```
BIGINT CEIL(DOUBLE value); BIGINT CEIL(DECIMAL value);
```

**参数说明**

value：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为DOUBLE 类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回BIGINT类型。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT CEIL(1.1);
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|   2   |
+-------+ SELECT CEIL(-1.1);
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|  -1   |
+-------+
```

##### CONV

本文介绍如何在MaxCompute中使用数学函数CONV，用于进制转换。

**操作说明**

###### 使用说明

进制转换函数，将指定进制的数值转换为另一种进制的表示。

**函数语法**

```
STRING CONV(STRING input, BIGINT from_base, BIGINT to_base);
```

**参数说明**

input：必填，STRING类型，表示要转换的整数值。支持BIGINT类型和DOUBLE类型的隐式转换。 from_base：必填，BIGINT类型，表示原始进制值。支持的值为2、8、10和16。支持STRING类型及 DOUBLE类型的隐式转换。 to_base：必填，BIGINT类型，表示目标进制值。支持的值为2、8、10和16。支持STRING类型及 DOUBLE类型的隐式转换。

**返回值**

返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。如果任意一个输入参数为NULL，返回NULL。如果输入的是负值（以短划线"-"开头），会报错。如果输入的是小数，会先转为整数值再进行进制转换，小数部分会被舍弃。

##### 使用示例

大数据计算服务

```
SELECT CONV('1100', 2, 10);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  12  |
+------+ SELECT CONV('1100', 2, 16);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  C   |
+------+ SELECT CONV('ab', 16, 10);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 171  |
+------+ SELECT CONV('ab', 16, 16);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  AB  |
+------+
```

##### COS

本文介绍如何在MaxCompute中使用数学函数COS，用于计算输入弧度值的余弦值。

**操作说明**

###### 使用说明

计算number的余弦函数，输入为弧度值。

**函数语法**

```
DOUBLE COS(DOUBLE number); DECIMAL COS(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。 大数据计算服务

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT COS(3.1415926/2);
```

`--` 返回结果

```
+-------------------------+
|           _c0           |
+-------------------------+
|  2.6794896585028633e-8  |
+-------------------------+ SELECT COS(3.1415926);
```

`--` 返回结果

```
+----------------------+
|         _c0          |
+----------------------+
|  -0.9999999999999986 |
+----------------------+
```

##### COSH

本文介绍如何在MaxCompute中使用数学函数COSH，用于计算输入值的双曲余弦值。

**操作说明**

###### 使用说明

计算number的双曲余弦函数。

**函数语法**

```
DOUBLE COSH(DOUBLE number); DECIMAL COSH(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT COSH(1);
```

`--` 返回结果

```
+----------------------+
|          _c0         |
+----------------------+
|  1.5430806348152437  |
+----------------------+ SELECT COSH(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### COT

本文介绍如何在MaxCompute中使用数学函数COT，用于计算输入弧度值的余切值。

**操作说明**

###### 使用说明

计算number的余切函数，输入为弧度值。

**函数语法**

```
DOUBLE COT(DOUBLE number); DECIMAL COT(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT COT(0.7853981633974483);
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
| 1.0000000000000002 |
+--------------------+ SELECT COT(1);
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 0.6420926159343308  |
+---------------------+
```

##### EXP

本文介绍如何在MaxCompute中使用数学函数EXP，用于计算自然常数e的幂次值。

**操作说明**

###### 使用说明

计算number的指数函数，即e的number次方。

**函数语法**

```
DOUBLE EXP(DOUBLE number); DECIMAL EXP(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型，值为e的number次方。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT EXP(1);
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2.718281828459045   |
+---------------------+ SELECT EXP(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### FLOOR

本文介绍如何在MaxCompute中使用数学函数FLOOR，用于对输入值向下取整。

**操作说明**

###### 使用说明

向下取整，返回不大于number的最大整数值。

**函数语法**

```
BIGINT FLOOR(DOUBLE number); BIGINT FLOOR(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回BIGINT类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT FLOOR(1.2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+ SELECT FLOOR(1.9);
```

`--` 返回结果

```
+------+
```

大数据计算服务 + +

```
| _c0  |
+------+
| 1    |
+------+ SELECT FLOOR(0.1);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+ SELECT FLOOR(-1.2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| -2   |
+------+ SELECT FLOOR(-0.1);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| -1   |
+------+ SELECT FLOOR(0.0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+ SELECT FLOOR(-0.0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+
```

##### LN

本文介绍如何在MaxCompute中使用数学函数LN，用于计算输入值的自然对数。 大数据计算服务

**操作说明**

###### 使用说明

返回number的自然对数。

**函数语法**

```
DOUBLE LN(DOUBLE number); DECIMAL LN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。 如果输入参数为负数或0，会报错。

##### 使用示例

```
SELECT LN(1000);
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
| 6.907755278982137  |
+--------------------+
```

##### LOG

本章节为您介绍数学函数中的LOG函数。 函数声明如下。

```
double log(double base, double x) decimal log(decimal base, decimal x)
```

用途：返回以**base**为底的x的对数。 参数说明：
**base**：DOUBLE类型或DECIMAL类型。如果输入为STRING类型或BIGINT类型，会隐式转换到
DOUBLE类型后参与运算。如果输入为其他类型会报错。 x：DOUBLE类型或DECIMAL类型。如果输入为STRING类型或BIGINT类型，会隐式转换到DOUBLE类型后参与运算。如果输入为其他类型会报错。 返回值：DOUBLE类型或DECIMAL类型的对数值。如果任意一个输入参数为NULL，返回NULL。如果任意一个输入参数为负数或0，则会报错。如果**base**为1（会引发一个除零行为），也会报错。 示例如下。

```
select log(10,100);
```

返回结果如下。 大数据计算服务

```
+------------+
| _c0        |
+------------+
| 2.0        |
+------------+
```

##### POW

本文介绍如何在MaxCompute中使用数学函数POW，用于计算x的y次方。

**操作说明**

###### 使用说明

返回x的y次方，即 x^y。

**函数语法**

```
DOUBLE POW(DOUBLE x, DOUBLE y); DECIMAL POW(DECIMAL x, DECIMAL y);
```

**参数说明**

x：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为DOUBLE类型后参与运算。如果输入为其他类型会报错。 y：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT POW(10, 2);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 100.0 |
+-------+
```

##### RAND

本文介绍如何在MaxCompute中使用数学函数RAND，用于生成指定种子的随机数。

**操作说明**

###### 使用说明

以seed为种子返回DOUBLE类型的随机数，返回值的区间是0～1。

**函数语法**

```
DOUBLE RAND(BIGINT seed);
```

大数据计算服务

**参数说明**

seed：选填，BIGINT类型，随机数种子，决定随机数序列的起始值。如果不指定seed，则每次执行返回不同的随机值。

**返回值**

返回DOUBLE类型，值域在0～1之间。 指定相同seed时，返回相同的随机数序列。 如果输入参数为NULL，返回NULL。

##### 使用示例

`--` 不指定种子，每次执行结果不同

```
SELECT RAND();
```

`--` 返回结果（示例，实际值因执行时间不同而变化）

```
+--------------------+
| _c0                |
+--------------------+
| 0.5432178901234567 |
+--------------------+
```

`--` 指定种子，每次执行结果相同

```
SELECT RAND(1);
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
| 0.7308781907032909 |
+--------------------+
```

##### ROUND

本文介绍如何在MaxCompute中使用数学函数ROUND，用于将数值四舍五入到指定小数位数。

**操作说明**

###### 使用说明

四舍五入到指定小数点位置。

**函数语法**

```
DOUBLE ROUND(DOUBLE number [, BIGINT decimal_places]); DECIMAL ROUND(DECIMAL number [, BIGINT decimal_places]);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。 大数据计算服务 decimal_places：选填，BIGINT类型常量，四舍五入计算到小数点后的位置，为其他类型会报错。如果省略表示四舍五入到个位数，默认值为0。

**说明**

可以是负数，负数会从小数点向左开始计数，并且不保留小数部分。如果decimal_places超过了整数部分长度，返回0。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT ROUND(125.315);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 125.0 |
+-------+ SELECT ROUND(125.315, 0);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 125.0 |
+-------+ SELECT ROUND(125.315, 1);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 125.3 |
+-------+ SELECT ROUND(125.315, 2);
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 125.32 |
+--------+ SELECT ROUND(125.315, 3);
```

`--` 返回结果

```
+---------+
```

大数据计算服务

```
| _c0     |
+---------+
| 125.315 |
+---------+ SELECT ROUND(-125.315, 2);
```

`--` 返回结果

```
+---------+
| _c0     |
+---------+
| -125.32 |
+---------+ SELECT ROUND(123.345, -2);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 100.0 |
+-------+ SELECT ROUND(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT ROUND(123.345, 4);
```

`--` 返回结果

```
+---------+
| _c0     |
+---------+
| 123.345 |
+---------+ SELECT ROUND(123.345, -4);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+
```

##### SIN

本文介绍如何在MaxCompute中使用数学函数SIN，用于计算输入弧度值的正弦值。 大数据计算服务

**操作说明**

###### 使用说明

计算number的正弦函数，输入为弧度值。

**函数语法**

```
DOUBLE SIN(DOUBLE number); DECIMAL SIN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT SIN(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SIN(3.1415926/2);
```

`--` 返回结果

```
+---------------------+
|          _c0        |
+---------------------+
| 0.9999999999999997  |
+---------------------+
```

##### SINH

本文介绍如何在MaxCompute中使用数学函数SINH，用于计算输入值的双曲正弦值。

**操作说明**

###### 使用说明

计算number的双曲正弦函数。

**函数语法**

```
DOUBLE SINH(DOUBLE number); DECIMAL SINH(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。 大数据计算服务

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT SINH(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SINH(1);
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 1.1752011936438014  |
+---------------------+
```

##### SQRT

本文介绍如何在MaxCompute中使用数学函数SQRT，用于计算输入值的平方根。

**操作说明**

###### 使用说明

计算number的平方根。

**函数语法**

```
DOUBLE SQRT(DOUBLE number); DECIMAL SQRT(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。必须大于0，小于0时会返回NULL。如果输入为STRING或 BIGINT类型，会隐式转换为DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT SQRT(4);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT SQRT(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+
```

##### TAN

本文介绍如何在MaxCompute中使用数学函数TAN，用于计算输入弧度值的正切值。

**操作说明**

###### 使用说明

计算number的正切函数，输入为弧度值。

**函数语法**

```
DOUBLE TAN(DOUBLE number); DECIMAL TAN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT TAN(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT TAN(0.7853981633974483);
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
| 0.9999999999999999 |
+--------------------+
```

##### TANH

本文介绍如何在MaxCompute中使用数学函数TANH，用于计算输入值的双曲正切值。

**操作说明**

###### 使用说明

计算number的双曲正切函数。

**函数语法**

```
DOUBLE TANH(DOUBLE number); DECIMAL TANH(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型或DECIMAL类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT TANH(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT TANH(1);
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 0.7615941559557649  |
```

##### TRUNC

函数声明如下。

```
double trunc(double number[, bigint decimal_places]) decimal trunc(decimal number[, bigint decimal_places])
```

用途：将输入值**number**截取到指定小数点位置。 参数说明：
**number**：DOUBLE类型或DECIMAL类型。如果输入为STRING类型或BIGINT类型，会隐式转换到
DOUBLE类型后参与运算。如果输入其他类型会报错。
**decimal_places**：BIGINT类型常量，要截取到的小数点位置。其他类型参数会隐式转为BIGINT类
型，省略此参数时默认截取到个位数。
**decimal_places**可以是负数，负数会从小数点向左开始截取，并且不保留小数部分。

**说明**

如果**decimal_places**超过了整数部分长度，则返回0。 返回值：DOUBLE或DECIMAL类型。如果任意一个输入参数为NULL，返回NULL。

**说明**

返回DOUBLE类型时，返回的结果显示可能不符合预期，例如**trunc(125.815,1)**，这个 DOUBLE类型显示问题任何系统都存在，无法避免。 截取掉的部分补0。 示例如下。 大数据计算服务

##### 新扩展数学函数

###### 使用说明

本文介绍使用新扩展的数学函数要进行的设置。

**操作说明**

升级到MaxCompute 2.0以后，产品扩展了新的数学函数，在使用新函数的SQL前，需要添加如下SET语句。

```
SET odps.sql.type.system.odps2=true;
```

**说明**

上述SET语句和新函数的SQL语句需要同时提交运行。

###### LOG2

本文介绍如何在MaxCompute中使用数学函数LOG2，用于计算以2为底的对数值。

**操作说明**

###### 使用说明

返回以2为底，number的对数。

**函数语法**

```
DOUBLE LOG2(DOUBLE number); DOUBLE LOG2(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。如果输入为其他类型会报错。

**返回值**

返回DOUBLE类型。 如果输入参数为NULL，返回NULL。如果输入参数为0，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT LOG2(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG2(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG2(8);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3.0  |
+------+
```

###### LOG10

**操作说明**

###### 使用说明

返回以10为底，number的对数。

**函数语法**

```
DOUBLE LOG10(DOUBLE number); DOUBLE LOG10(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。

**返回值**

返回DOUBLE类型。 如果输入参数为NULL，返回NULL。如果输入参数为0，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT LOG10(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG10(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT LOG10(8);
```

`--` 返回结果

```
+----------------------+
| _c0                  |
+----------------------+
| 0.9030899869919435   |
+----------------------+
```

###### BIN

本文介绍如何在MaxCompute中使用数学函数BIN，用于返回输入值的二进制代码表示。

**操作说明**

###### 使用说明

返回number的二进制代码表示。

**函数语法**

```
STRING BIN(BIGINT number);
```

**参数说明**

number：必填，BIGINT类型。

**返回值**

返回STRING类型。如果输入参数为0，返回0。如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT BIN(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+ SELECT BIN(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT BIN(12);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1100 |
+------+
```

###### HEX

本文介绍如何在MaxCompute中使用数学函数HEX，用于将整数或字符串转换为十六进制格式。

**操作说明**

###### 使用说明

将整数或字符串转换为十六进制格式。

**函数语法**

```
STRING HEX(BIGINT number); STRING HEX(STRING number); STRING HEX(BINARY number);
```

**参数说明**

number：必填。如果number是BIGINT类型，返回number的十六进制表示。如果number是STRING 类型，返回该字符串的十六进制表示。

**返回值**

返回STRING类型。 如果输入参数为0，返回0。如果输入参数为NULL，返回会报错。

##### 使用示例

大数据计算服务

```
SELECT HEX(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+ SELECT HEX('abc');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 616263 |
+--------+ SELECT HEX(17);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 11   |
+------+ SELECT HEX('17');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3137 |
+------+ SELECT HEX(NULL);
```

`--` 返回异常信息执行失败。

###### UNHEX

本文介绍如何在MaxCompute中使用数学函数UNHEX，用于将十六进制字符串转换为对应的字符串。

**操作说明**

###### 使用说明

返回十六进制字符串所代表的字符串。

**函数语法**

```
BINARY UNHEX(STRING number);
```

**参数说明**

number：必填，为十六进制字符串。 大数据计算服务

**返回值**

返回BINARY类型。 如果输入参数为0，会报错。如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT UNHEX('616263');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| abc  |
+------+ SELECT UNHEX(616263);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| abc  |
+------+
```

###### RADIANS

本文介绍如何在MaxCompute中使用数学函数RADIANS，用于将角度转换为弧度。

**操作说明**

###### 使用说明

将角度转换为弧度。

**函数语法**

```
DOUBLE RADIANS(DOUBLE number);
```

**参数说明**

number：必填，DOUBLE类型。

**返回值**

返回DOUBLE类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT RADIANS(90);
```

`--` 返回结果

```
+----------------------+
| _c0                  |
+----------------------+
| 1.5707963267948966   |
+----------------------+ SELECT RADIANS(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT RADIANS(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### DEGREES

本文介绍如何在MaxCompute中使用数学函数DEGREES，用于将弧度转换为角度。

**操作说明**

###### 使用说明

将弧度转换为角度。

**函数语法**

```
DOUBLE DEGREES(DOUBLE number); DOUBLE DEGREES(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。

**返回值**

返回DOUBLE类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT DEGREES(1.5707963267948966);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 90.0 |
+------+ SELECT DEGREES(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT DEGREES(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### SIGN

本文介绍如何在MaxCompute中使用数学函数SIGN，用于获取输入参数的符号。

**操作说明**

###### 使用说明

获取输入参数的符号。

**函数语法**

```
DOUBLE SIGN(DOUBLE number); DOUBLE SIGN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。

**返回值**

返回DOUBLE类型。 如果输入参数为正数，返回1.0。如果输入参数为负数，返回-1.0。 如果输入参数为0，返回0.0。如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT SIGN(-2.5);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| -1.0 |
+------+ SELECT SIGN(2.5);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.0  |
+------+ SELECT SIGN(0);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0.0  |
+------+ SELECT SIGN(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### E

本文介绍如何在MaxCompute中使用数学函数E，用于返回自然常数e的值。

**操作说明**

###### 使用说明

返回e的值。

**函数语法**

```
DOUBLE E();
```

**参数说明**

无。

**返回值**

返回DOUBLE类型。 大数据计算服务

##### 使用示例

```
SELECT E();
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2.718281828459045   |
+---------------------+
```

###### PI

本文介绍如何在MaxCompute中使用数学函数PI，用于返回圆周率π的值。

**操作说明**

###### 使用说明

返回π的值。

**函数语法**

```
DOUBLE PI()
```

**参数说明**

无。

**返回值**

返回DOUBLE类型。

##### 使用示例

```
SELECT PI();
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 3.141592653589793   |
+---------------------+
```

###### FACTORIAL

本文介绍如何在MaxCompute中使用数学函数FACTORIAL，用于计算输入值的阶乘。

**操作说明**

###### 使用说明

返回number的阶乘。

**函数语法**

```
BIGINT FACTORIAL(INT number);
```

**参数说明**

number：必填，INT类型，值域在[0,20]之间。 大数据计算服务

**返回值**

返回BIGINT类型。 如果输入参数为0，返回1。如果输入参数为NULL或 `[0,20]` 之外的数值，返回NULL。

##### 使用示例

```
SELECT FACTORIAL(5);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 120  |
+------+
```

###### CBRT

本文介绍如何在MaxCompute中使用数学函数CBRT，用于计算输入值的立方根。

**操作说明**

###### 使用说明

计算number的立方根。

**函数语法**

```
DOUBLE CBRT(DOUBLE number);
```

**参数说明**

number：必填，BIGINT、INT、SMALLINT、TINYINT、DOUBLE、FLOAT、STRING类型数据。

**返回值**

返回DOUBLE类型。 number非BIGINT、INT、SMALLINT、TINYINT、DOUBLE、FLOAT、STRING类型时，返回报错。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT CBRT(8);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT CBRT(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### SHIFTLEFT

本文介绍如何在MaxCompute中使用数学函数SHIFTLEFT，用于按位左移运算。

**操作说明**

###### 使用说明

按位左移（<<）。

**函数语法**

```
INT SHIFTLEFT(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTLEFT(BIGINT number1, INT number2);
```

**参数说明**

number1：必填，TINYINT、SMALLINT、INT或BIGINT整型数据。 number2：必填，INT整型数据。

**返回值**

返回INT类型或BIGINT类型。

##### 使用示例

大数据计算服务 `-- 1`的二进制左移2位（`1<<2, 0001`左移两位是`0100`）

```
SELECT SHIFTLEFT(1, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 4    |
+------+
```

`-- 4`的二进制左移3位（`4<<3, 0100`左移3位是`100000`）

```
SELECT SHIFTLEFT(4, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 32   |
+------+
```

###### SHIFTRIGHT

本文介绍如何在MaxCompute中使用数学函数SHIFTRIGHT，用于按位右移运算。

**操作说明**

###### 使用说明

按位右移（>>）。

**函数语法**

```
INT SHIFTRIGHT(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTRIGHT(BIGINT number1, INT number2);
```

**参数说明**

number1：必填，TINYINT、SMALLINT、INT或BIGINT整型数据。 number2：必填，INT整型数据。

**返回值**

返回INT类型或BIGINT类型。

##### 使用示例

大数据计算服务
    - `- 4`的二进制右移2位（`4>>2, 0100`右移两位是`0001`）

```
SELECT SHIFTRIGHT(4, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+
```

`-- 32`的二进制右移3位（`32>>3, 100000`右移3位是`0100`）

```
SELECT SHIFTRIGHT(32, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 4    |
+------+
```

###### SHIFTRIGHTUNSIGNED

本文介绍如何在MaxCompute中使用数学函数SHIFTRIGHTUNSIGNED，用于无符号按位右移运算。

**操作说明**

###### 使用说明

无符号按位右移（>>>）。

**函数语法**

```
INT SHIFTRIGHTUNSIGNED(TINYINT|SMALLINT|INT number1, INT number2); BIGINT SHIFTRIGHTUNSIGNED(BIGINT number1, INT number2);
```

**参数说明**

number1：必填，TINYINT、SMALLINT、INT或BIGINT整型数据。 number2：必填，INT整型数据。

**返回值**

返回INT类型或BIGINT类型。

##### 使用示例

大数据计算服务 `-- 8`的二进制无符号右移2位（`8>>>2, 1000`右移两位是`0010`）

```
SELECT SHIFTRIGHTUNSIGNED(8, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

`-- -14`的二进制无符号右移2位（`-14>>>2, 11111111 11111111 11111111 11110010`右移2位是`00111111`

```
11111111 11111111 11111100） SELECT SHIFTRIGHTUNSIGNED(-14, 2);
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 1073741820 |
+------------+
```

###### FORMAT_NUMBER

本文介绍如何在MaxCompute中使用数学函数FORMAT_NUMBER，用于将数字转化为指定格式的字符串。

**操作说明**

###### 使用说明

将数字转化为指定格式的字符串。

**函数语法**

```
STRING FORMAT_NUMBER(FLOAT|DOUBLE|DECIMAL expr1, expr2);
```

**参数说明**

expr1：必填，需要格式化的数据。 expr2：必填，需要转化的目标格式。

**说明**

可以为INT类型，指定需要保留小数位数。 也可以是类似 #,###,###.## 的格式。 如果expr2>0，则四舍五入到小数点后指定位数。 如果expr2=0，则没有小数点或小数部分。如果expr2<0或者expr2>340，则会报错。

**返回值**

返回STRING类型。

##### 使用示例

大数据计算服务

```
SELECT FORMAT_NUMBER(5.230134523424545456, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 5.230|
+------+ SELECT FORMAT_NUMBER(12332.123456, '#,###,###,###.###');
```

`--` 返回结果

```
+---------+
| _c0     |
+---------+
| 12,332.123 |
+---------+
```

###### WIDTH_BUCKET

本文介绍如何在MaxCompute中使用数学函数WIDTH_BUCKET，用于设定分组范围并返回指定字段值落入的分组编号。

**操作说明**

###### 使用说明

设定分组范围的最小值、最大值和分组个数，构建指定个数的大小相同的分组，返回指定字段值落入的分组编号。支持的数据类型为BIGINT、INT、FLOAT、DOUBLE、DECIMAL类型以及数据类型2.0的 DECIMAL(precision,scale)。

**函数语法**

```
BIGINT WIDTH_BUCKET(NUMERIC expr, NUMERIC min_value, NUMERIC max_value, INT num_buckets);
```

**参数说明**

expr：必填，需要判断分组编号的字段。 min_value：必填，分组范围最小值。 max_value：必填，分组范围最大值，最大值必须比最小值大。 num_buckets：必填，分组个数，必须大于0。

**返回值**

返回BIGINT类型，范围为0到设定的分组个数+1。 如果expr值小于min_value，返回0。如果expr大于max_value，返回设定的分组个数+1。 如果字段值为NULL，分组编号返回值也为NULL。 其他情况返回字段值落入的分组编号。字段值对应的分组编号取值规则为 `FLOOR(num_buckets *`

```
(expr - min_value) / (max_value - min_value) + 1) 。
```

##### 使用示例

大数据计算服务

```
SELECT key, value, WIDTH_BUCKET(value, 100, 500, 5) AS value_group
    (1, 99),
    (2, 100),
    (3, 199),
    (4, 200),
    (5, 499),
    (6, 500),
    (7, 501),
    (8, NULL)
AS t(key, value);
```

`--` 返回结果

```
+-------+--------+-------------+ +-------+--------+-------------+
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

#### 字符串函数

##### CHAR_MATCHCOUNT

CHAR_MATCHCOUNT函数用于计算两个字符串之间相同字符的个数，即计算 `str1` 中有多少个字符出现在 `str2` 中。本文介绍如何在MaxCompute中使用CHAR_MATCHCOUNT函数。

**操作说明**

###### 使用说明

统计第一个字符串中出现在第二个字符串里的字符个数。

**函数语法**

```
BIGINT char_matchcount(STRING str1, STRING str2);
```

**参数说明**

**说明**

必须为有效的UTF-8字符串。如果对比中发现有无效字符，则返回 0 。 str1：必填，STRING 类型，待匹配的源字符串。 str2：必填，STRING 类型，用于比对的目标字符串。

**返回值**

返回BIGINT类型。如果任意一个输入参数为NULL，返回NULL。 大数据计算服务

##### 使用示例

```
SELECT CHAR_MATCHCOUNT('abd', 'aabc');
```

`--` 返回结果

```
+--------+
|   _c0  |
+--------+
|    2   |
+--------+
```

##### CHR

本文介绍如何在MaxCompute中使用字符串函数CHR，用于将给定ASCII码转换为对应的字符。

**操作说明**

###### 使用说明

**函数语法**

```
STRING CHR(BIGINT ascii);
```

**参数说明**

ascii：必填，BIGINT类型ASCII值。如果输入为STRING、DOUBLE或DECIMAL类型，会隐式转换为 BIGINT类型后参与运算。输入为其他类型会报错。

**返回值**

返回STRING类型。 输入参数范围是0~255，超过此范围会报错。如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT CHR(65);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| A    |
+------+ SELECT CHR(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### CONCAT

大数据计算服务本文介绍如何在MaxCompute中使用字符串函数CONCAT，用于将所有参数中的字符串连接在一起。

**操作说明**

###### 使用说明

返回将参数中的所有字符串连接在一起的结果。

**函数语法**

```
STRING CONCAT(STRING a, STRING b...);
```

**参数说明**

a, b...：必填，STRING类型。如果输入参数为BIGINT、DOUBLE、DECIMAL或DATETIME类型，会隐式转换为STRING类型后参与运算。输入为其他类型会报错。

**返回值**

返回STRING类型。 如果没有参数或任意一个输入参数为NULL，均返回NULL。

##### 使用示例

```
SELECT CONCAT('ab', 'c');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| abc  |
+------+ SELECT CONCAT();
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT CONCAT('a', NULL, 'b');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### INSTR

本文介绍如何在MaxCompute中使用字符串函数INSTR，用于计算子串在字符串中的位置。

**操作说明**

###### 使用说明

大数据计算服务计算子串str2在字符串str1中的位置。

**函数语法**

```
BIGINT INSTR(STRING str1, STRING str2 [, BIGINT start_position [, BIGINT nth_appearance]]);
```

**参数说明**

str1：必填，STRING类型，要搜索的字符串。如果输入为BIGINT、DOUBLE、DECIMAL或 DATETIME类型，会隐式转换为STRING类型后参与运算。如果输入不支持转化为STRING的类型则返回报错。 str2：必填，STRING类型，要搜索的子串。如果输入为BIGINT、DOUBLE、DECIMAL或DATETIME 类型，会隐式转换为STRING类型后参与运算。如果输入不支持转化为STRING的类型则返回报错。 start_position：选填，BIGINT类型，为其他类型会报错。表示从str1的第几个字符开始搜索，默认起始位置是第一个字符位置1。当start_position为负数时表示开始位置是从字符串的结尾往前倒数，最后一个字符是-1，依次往前倒数。 nth_appearance：选填，BIGINT类型。大于0，表示子串在字符串中的第nth_appearance次匹配的位置。如果nth_appearance为其他数据类型或小于等于0，则会报错。

**返回值**

返回BIGINT类型。 如果在str1中未找到str2，则返回0。如果str2为空串，则总能匹配成功，例如SELECT str1、str2、start_position或nth_appearance值为NULL时，返回NULL。

##### 使用示例

大数据计算服务 `--` 示例1：计算字符e在字符串`Tech on the net`中的位置

```
SELECT INSTR('Tech on the net', 'e');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

`--` 示例2：计算子串`on`在字符串`Tech on the net`中的位置

```
SELECT INSTR('Tech on the net', 'on');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 6    |
+------+
```

`--` 示例3：计算字符e在字符串`Tech on the net`中，从第3个字符开始，第2次出现的位置

```
SELECT INSTR('Tech on the net', 'e', 3, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 14   |
+------+
```

`--` 示例4：任一输入参数为`NULL`

```
SELECT INSTR('Tech on the net', NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### IS_ENCODING

本文介绍如何在MaxCompute中使用字符串函数IS_ENCODING，用于判断输入字符串是否可以在指定字符集之间转换。

**操作说明**

###### 使用说明

判断输入字符串str是否可以从指定的一个字符集from_encoding转为另一个字符集to_encoding。也可以判断输入是否为乱码，通常的用法是将from_encoding设为UTF-8，to_encoding设为GBK。

**函数语法**

```
BOOLEAN IS_ENCODING(STRING str, STRING from_encoding, STRING to_encoding);
```

大数据计算服务

**参数说明**

str：必填，STRING类型，空字符串属于任何字符集。 from_encoding：必填，STRING类型，源字符集。 to_encoding：必填，STRING类型，目标字符集。

**返回值**

返回BOOLEAN类型。 如果str能够成功转换，则返回True，否则返回False。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT IS_ENCODING('测试', 'utf-8', 'gbk');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

`-- GBK`字库中有这两个繁体字

```
SELECT IS_ENCODING('測試', 'utf-8', 'gbk');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

`-- GB2312`库中不包括这两个字

```
SELECT IS_ENCODING('測試', 'utf-8', 'gb2312');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### KEYVALUE

本文介绍如何在MaxCompute中使用字符串函数KEYVALUE，用于将源字符串按分隔符拆分为Key-Value 对并返回指定key对应的Value。

**操作说明**

###### 使用说明

将srcStr（源字符串）按split1分成Key-Value对，并按split2将Key-Value对分开，返回key所对应的 Value。

**函数语法**

大数据计算服务

```
KEYVALUE(STRING srcStr, STRING split1, STRING split2, STRING key); KEYVALUE(STRING srcStr, STRING key);
```

**参数说明**

srcStr：必填，STRING类型，输入待拆分的字符串。 key：必填，STRING类型。源字符串按照split1和split2拆分后，根据该key值的指定，返回其对应的 Value。 split1：选填，STRING类型，用于分隔Key-Value对的分隔符。如果表达式中没有指定，默认为";"。 split2：选填，STRING类型，用于分隔Key和Value的分隔符。如果表达式中没有指定，默认为":"。

**返回值**

返回STRING类型。 split1或split2为NULL时，返回NULL。srcStr或key为NULL，或者没有匹配的key时，返回NULL。

##### 使用示例

`--` 示例1：使用默认分隔符，返回`key`为1所对应的`Value`值

```
SELECT KEYVALUE('0:1\;1:2', 1);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

`--` 示例2：指定`split1`为"\;"，`split2`为`":"`，返回`key`为`tf`对应的`Value`值

```
KEYVALUE('\;decreaseStore:1\;xcard:1\;isB2C:1\;tf:21910\;cart:1\;shipping:2\;pf:0\;mark :shoes\;instPayAmount:0\;', '\;', ':', 'tf');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| 21910 |
+-------+
```

##### LENGTH

本文介绍如何在MaxCompute中使用字符串函数LENGTH，用于返回字符串的长度。

**操作说明**

###### 使用说明

返回字符串str的长度。

**函数语法**

```
BIGINT LENGTH(STRING str);
```

**参数说明**

大数据计算服务 str：必填，STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或DATETIME类型，会隐式转换为STRING类型后参与运算。输入为其他类型会报错。

**返回值**

返回BIGINT类型。 如果输入参数为NULL，返回NULL。如果输入参数为非UTF-8编码格式，返回-1。

##### 使用示例

```
SELECT LENGTH('hi! 中国');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 6    |
+------+
```

##### LENGTHB

本文介绍如何在MaxCompute中使用字符串函数LENGTHB，用于返回字符串以字节为单位的长度。

**操作说明**

###### 使用说明

返回字符串str中以字节为单位的长度。

**函数语法**

```
BIGINT LENGTHB(STRING str);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或DATETIME类型，会隐式转换为STRING类型后参与运算。输入为其他类型会报错。

**返回值**

返回BIGINT类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT LENGTHB('hi! 中国');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 10   |
+------+
```

##### MD5

本文介绍如何在MaxCompute中使用字符串函数MD5，用于计算输入字符串的MD5值。

**操作说明**

大数据计算服务

###### 使用说明

计算输入字符串value的MD5值。

**函数语法**

```
STRING MD5(STRING value);
```

**参数说明**

value：必填，STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或DATETIME类型，会隐式转换为STRING类型后参与运算。输入为其他类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT MD5('abc');
```

`--` 返回结果

```
+----------------------------------+
| _c0                              |
+----------------------------------+
| 900150983cd24fb0d6963f7d28e17f72 |
+----------------------------------+ SELECT MD5(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### PARSE_URL

本文介绍如何在MaxCompute中使用字符串函数PARSE_URL，用于解析URL并按指定部分提取信息。

**操作说明**

###### 使用说明

对url解析，按key提取信息。

**函数语法**

```
STRING PARSE_URL(STRING url, STRING part [, STRING key]);
```

**参数说明**

url：必填，待解析链接。url为NULL时，返回NULL。url为无效链接会报错。 part：必填，STRING类型。支持HOST、PATH、QUERY、REF、PROTOCOL、AUTHORITY、FILE 和USERINFO，不区分大小写，不在此范围会报错。 key：选填，STRING类型。当part为QUERY时，根据key的值取出在query string中的Value值，否则忽略key参数。 大数据计算服务

**返回值**

返回STRING类型。

##### 使用示例

```
-- 示例URL：file://username:password@example.com:8042/over/there/index.dtb? type=animal&name=narwhal#nose SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'HOST');
```

`--` 返回结果

```
+--------------+
| _c0          |
+--------------+
| example.com  |
+--------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'PATH');
```

`--` 返回结果

```
+----------------------------+
| _c0                        |
+----------------------------+ +----------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'QUERY');
```

`--` 返回结果

```
+-------------------------------+
| _c0                           |
+-------------------------------+
| type=animal&name=narwhal      |
+-------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'QUERY', 'name');
```

`--` 返回结果

```
+----------+
| _c0      |
+----------+
| narwhal  |
+----------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'REF');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
```

大数据计算服务

```
| nose |
+------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'PROTOCOL');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| file |
+------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'AUTHORITY');
```

`--` 返回结果

```
+----------------------------------------------+
| _c0                                          |
+----------------------------------------------+
| username:password@example.com:8042            |
+----------------------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'FILE');
```

`--` 返回结果

```
+-------------------------------------------------------------+
| _c0                                                         |
+-------------------------------------------------------------+
| /over/there/index.dtb?type=animal&name=narwhal              |
+-------------------------------------------------------------+ SELECT PARSE_URL('file://username:password@example.com:8042/over/there/index.dtb?type =animal&name=narwhal#nose', 'USERINFO');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| username:password   |
+---------------------+
```

##### REGEXP_EXTRACT

本文介绍如何在MaxCompute中使用字符串函数REGEXP_EXTRACT，用于按正则表达式规则提取字符串中指定分组的内容。

**操作说明**

###### 使用说明

将字符串source按照pattern正则表达式的规则拆分，返回第occurrence个group的字符。

**函数语法**

大数据计算服务

```
STRING REGEXP_EXTRACT(STRING source, STRING pattern [, BIGINT occurrence]);
```

**参数说明**

source：必填，STRING类型，需要搜索的字符串。 pattern：必填，STRING类型常量。如果pattern为空串或者pattern中没有指定group，则会报错。 occurrence：选填，BIGINT类型常量。必须大于等于0，为其他类型或小于0时会报错。不指定时默认为1，表示返回第一个group。如果occurrence等于0，返回满足整个pattern的子串。

**返回值**

返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。数据以UTF-8格式保存。对于中文字符可以用对应的16 进制编码表示，中文字符编码的范围是[\x{4e00},\x{9fa5}]。

##### 使用示例

大数据计算服务

```
SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 1);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| the  |
+------+ SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| bar  |
+------+ SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 0);
```

`--` 返回结果

```
+-----------+
| _c0       |
+-----------+
| foothebar |
+-----------+ SELECT REGEXP_EXTRACT('8d99d8', '8d(\\d+)d8');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 99   |
+------+
```

`--` 如果在`MaxCompute`客户端上提交正则计算的`SQL`，需要使用两个反斜线（\\）作为转义字符。 `-- pattern`中没有指定`group`，会报错：

```
-- SELECT REGEXP_EXTRACT('foothebar', 'foothebar'); -- 报错
```

##### REGEXP_INSTR

本文介绍如何在MaxCompute中使用字符串函数REGEXP_INSTR，用于返回字符串中与正则表达式第n次匹配的子串的起始或结束位置。

**操作说明**

###### 使用说明

返回字符串source从start_position开始，和pattern第n次（nth_occurrence）匹配的子串的起始或结束位置。

**函数语法**

大数据计算服务

```
BIGINT REGEXP_INSTR(STRING source, STRING pattern [, BIGINT start_position [, BIGINT nth_occurrence [, BIGINT return_option]]]);
```

**参数说明**

source：必填，STRING类型，待搜索的字符串。 pattern：必填，STRING类型常量。pattern为空串时会报错。 start_position：选填，BIGINT类型常量，搜索的开始位置。不指定时默认值为1，为其他类型或值小于等于0时会报错。 nth_occurrence：选填，BIGINT类型常量。不指定时默认值为1，表示搜索第一次出现的位置。为其他类型或值小于等于0时会报错。 return_option：选填，BIGINT类型常量，值为0或1，为其他类型或不允许的值时会报错。0表示返回匹配的开始位置，1表示返回匹配的结束位置。

**返回值**

返回BIGINT类型，return_option指定的类型返回匹配的子串在source中的开始或结束位置。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT REGEXP_INSTR('i love www.taobao.com', 'o[[:alpha:]]{1}', 3, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 14   |
+------+
```

##### REGEXP_SUBSTR

本文介绍如何在MaxCompute中使用字符串函数REGEXP_SUBSTR，用于返回字符串中与正则表达式第n 次匹配的子串。

**操作说明**

###### 使用说明

返回从start_position位置开始，source中第nth_occurrence次匹配指定模式pattern的子串。

**函数语法**

```
STRING REGEXP_SUBSTR(STRING source, STRING pattern [, BIGINT start_position [, BIGINT nth_occurrence]]);
```

**参数说明**

source：必填，STRING类型，搜索的字符串。 pattern：必填，STRING类型常量，要匹配的模式。pattern为空串时会报错。 start_position：选填，BIGINT常量，必须大于0。为其他类型或小于等于0时会报错。不指定时默认为1，表示从source的第一个字符开始匹配。 nth_occurrence：选填，BIGINT常量，必须大于0。为其他类型或小于等于0时会报错。不指定时默认为1，表示返回第一次匹配的子串。

**返回值**

大数据计算服务返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。没有匹配时也返回NULL。

##### 使用示例

```
SELECT REGEXP_SUBSTR('I love aliyun very much', 'a[[:alpha:]]{5}');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+ +--------+ SELECT REGEXP_SUBSTR('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 1);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
|  have |
+-------+ SELECT REGEXP_SUBSTR('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  2   |
+------+
```

##### REGEXP_COUNT

本文介绍如何在MaxCompute中使用字符串函数REGEXP_COUNT，用于计算字符串中与正则表达式匹配的子串出现次数。

**操作说明**

###### 使用说明

计算source中从start_position开始，匹配指定模式pattern的子串的次数。

**函数语法**

```
BIGINT REGEXP_COUNT(STRING source, STRING pattern [, BIGINT start_position]);
```

**参数说明**

source：必填，STRING类型，搜索的字符串。为其他类型时会报错。 pattern：必填，STRING类型常量，要匹配的模式。pattern为空串或其他类型时，会报错。 start_position：选填，BIGINT类型常量，必须大于0。为其他类型或值小于等于0时会报错。不指定时默认为1，表示从source的第一个字符开始匹配。 大数据计算服务

**返回值**

返回BIGINT类型。 如果任意一个输入参数为NULL，返回NULL。没有匹配时返回0。

##### 使用示例

```
SELECT REGEXP_COUNT('abababc', 'a.c');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+ SELECT REGEXP_COUNT('abcde', '[[:alpha:]]{2}', 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+
```

##### REGEXP_REPLACE

本文介绍如何在MaxCompute中使用字符串函数REGEXP_REPLACE，用于将字符串中匹配正则表达式的子串替换为指定字符串。

**操作说明**

###### 使用说明

将source字符串中第occurrence次匹配pattern的子串替换成指定字符串replace_string后返回。

**函数语法**

```
STRING REGEXP_REPLACE(STRING source, STRING pattern, STRING replace_string[, BIGINT o ccurrence]);
```

**参数说明**

source：必填，STRING类型，要替换的字符串。 pattern：必填，STRING类型常量，要匹配的模式，pattern为空串时会报错。 replace_string：必填，STRING类型，将匹配的pattern进行替换的指定字符串。 occurrence：选填，BIGINT类型常量，必须大于等于0，表示将第几次匹配替换成replace_string， 为0时表示替换所有的匹配子串。为其他类型或小于0时会报错。可缺省，默认值为0。

**返回值**

返回STRING类型。 当引用不存在的组时，不进行替换。 如果replace_string为NULL且pattern有匹配，返回NULL。如果replace_string为NULL但pattern不匹配，返回原字符串。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 示例1：替换所有匹配（`occurrence`为0）

```
SELECT REGEXP_REPLACE("123.456.7890", "([[:digit:]]{3})\\.([[:digit:]]{3})\\.([[:digi t:]]{4})", "(\\1)\\2-\\3", 0);
```

`--` 返回结果

```
+------------------+
|  (123)456-7890   |
+------------------+
```

`--` 示例2：替换所有单字符后加空格（`occurrence`为0）

```
SELECT REGEXP_REPLACE("abcd", "(.)", "\\1 ", 0);
```

`--` 返回结果

```
+-----------+
|  a b c d  |
+-----------+
```

`--` 示例3：仅替换第1次匹配（`occurrence`为1）

```
SELECT REGEXP_REPLACE("abcd", "(.)", "\\1 ", 1);
```

`--` 返回结果

```
+-----------+
|   a bcd   |
+-----------+
```

`--` 示例4：引用不存在的组（请避免这样使用，引用不存在的组的结果未定义）

```
SELECT REGEXP_REPLACE("abcd", "(.)", "\\2", 1);
```

`--` 返回结果

```
+------+
| abcd |
+------+
```

`--` 示例5：引用存在的组进行替换

```
SELECT REGEXP_REPLACE("abcd", "(.*)(.)$", "\\2", 0);
```

`--` 返回结果

```
+------+
|   d  |
+------+
```

`--` 示例6：引用不存在的组（`pattern`中没有组的定义，请避免这样使用，引用不存在的组的结果未定义）

```
SELECT REGEXP_REPLACE("abcd", "a", "\\1", 0);
```

`--` 返回结果

```
+------+
|  bcd |
+------+
```

##### SPLIT_PART

本文介绍如何在MaxCompute中使用字符串函数SPLIT_PART，用于依照分隔符拆分字符串并返回指定段的子串。 大数据计算服务

**操作说明**

###### 使用说明

依照分隔符separator拆分字符串str，返回从第start部分到第end部分的子串（闭区间）。

**函数语法**

```
STRING SPLIT_PART(STRING str, STRING separator, BIGINT start[, BIGINT end]);
```

**参数说明**

str：必填，STRING类型，要拆分的字符串。如果输入为BIGINT、DOUBLE、DECIMAL或者 DATETIME类型，则会隐式转换为STRING类型后参加运算，输入为其他类型时会报错。 separator：必填，STRING类型常量，拆分用的分隔符，可以是一个字符，也可以是一个字符串，为其他类型时会报错。 start：必填，BIGINT类型常量，必须大于0，非常量或为其他类型时会报错。返回段的开始编号（从1 开始），如果没有指定end，则返回start指定的段。 end：选填，BIGINT类型常量，大于等于start，否则会报错。返回片段的截止编号，非常量或为其他类型会报错。可省略，缺省时表示最后一部分。

**返回值**

返回STRING类型。 如果start的值大于拆分后实际的分段数，返回空串。如果separator不存在于str中，且start指定为 1，返回整个str。 如果str为空串，则输出空串。如果separator为空串，则返回原字符串str。如果end大于片段个数， 按片段个数处理。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

`--` 示例1：拆分字符串返回第1段

```
SELECT SPLIT_PART('a,b,c,d', ',', 1);
```

`--` 返回结果

```
+------+
|   a  |
+------+
```

`--` 示例2：拆分字符串返回第1到第2段

```
SELECT SPLIT_PART('a,b,c,d', ',', 1, 2);
```

`--` 返回结果

```
+------+
|  a,b |
+------+
```

`--` 示例3：`start`大于实际分段数

```
SELECT SPLIT_PART('a,b,c,d', ',', 10);
```

`--` 返回结果

```
+------+
|      |
+------+
```

大数据计算服务

##### SUBSTR

本文介绍如何在MaxCompute中使用字符串函数SUBSTR，用于返回字符串指定位置和长度的子串。

**操作说明**

###### 使用说明

**函数语法**

```
STRING SUBSTR(STRING str, BIGINT start_position[, BIGINT length]);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其他类型会报错。 start_position：必填，BIGINT类型。起始位置为1。当start_position为0时，返回NULL；当 start_position为负数时表示开始位置是从字符串的结尾往前倒数，最后一个字符是-1。输入为其他类型时会报错。 length：选填，BIGINT类型。表示子串的长度值，大于0，输入为其他类型或值小于等于0时会报错。

**返回值**

返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。当length被省略时，返回字符串str从start_position开始到str结尾的子串。

##### 使用示例

`--` 示例1：从第2位开始截取到结尾

```
SELECT SUBSTR('abc', 2);
```

`--` 返回结果

```
+------+
|  bc  |
+------+
```

`--` 示例2：从第2位开始截取1个字符

```
SELECT SUBSTR('abc', 2, 1);
```

`--` 返回结果

```
+------+
|   b  |
+------+
```

`--` 示例3：从倒数第2位开始截取2个字符

```
SELECT SUBSTR('abc', -2, 2);
```

`--` 返回结果

```
+------+
|  bc  |
+------+
```

大数据计算服务

##### TOLOWER

本文介绍如何在MaxCompute中使用字符串函数TOLOWER，用于将英文字符串转换为小写形式。

**操作说明**

###### 使用说明

输出英文字符串source对应的小写字符串。

**函数语法**

```
STRING TOLOWER(STRING source);
```

**参数说明**

source：必填，STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

`--` 将英文字符串转换为小写。

```
SELECT TOLOWER("aBcd");
```

`--` 返回结果

```
+------+
| abcd |
+------+
```

`--` 中英文混合字符串。

```
SELECT TOLOWER("哈哈Cd");
```

`--` 返回结果

```
+--------+
```

| 哈哈cd |

```
+--------+
```

##### TOUPPER

本文介绍如何在MaxCompute中使用字符串函数TOUPPER，用于将英文字符串转换为大写形式。

**操作说明**

###### 使用说明

输出英文字符串source对应的大写字符串。

**函数语法**

```
STRING TOUPPER(STRING source);
```

**参数说明**

source：必填，STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。 大数据计算服务

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

`--` 将英文字符串转换为大写。

```
SELECT TOUPPER("aBcd");
```

`--` 返回结果

```
+------+
| ABCD |
+------+
```

`--` 中英文混合字符串。

```
SELECT TOUPPER("哈哈Cd");
```

`--` 返回结果

```
+--------+
```

| 哈哈CD |

```
+--------+
```

##### TO_CHAR

本文介绍如何在MaxCompute中使用字符串函数TO_CHAR，用于将BOOLEAN、BIGINT、DECIMAL或者 DOUBLE类型转换为对应的STRING类型表示。

**操作说明**

###### 使用说明

将BOOLEAN、BIGINT、DECIMAL或者DOUBLE类型转换为对应的STRING类型表示。

**函数语法**

```
STRING TO_CHAR(BOOLEAN value); STRING TO_CHAR(BIGINT value); STRING TO_CHAR(DOUBLE value); STRING TO_CHAR(DECIMAL value);
```

**参数说明**

value：必填，可以支持BOOLEAN、BIGINT、DECIMAL或者DOUBLE类型输入，输入为其它类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT TO_CHAR(123);
```

`--` 返回结果

```
+------+
| 123  |
+------+ SELECT TO_CHAR(TRUE);
```

`--` 返回结果

```
+-------+
| TRUE  |
+-------+ SELECT TO_CHAR(1.23);
```

`--` 返回结果

```
+-------+
| 1.23  |
+-------+ SELECT TO_CHAR(NULL);
```

`--` 返回结果

```
+-------+
| NULL  |
+-------+
```

##### TRIM

本文介绍如何在MaxCompute中使用字符串函数TRIM，用于去除输入字符串的左右空格。

**操作说明**

###### 使用说明

去除输入字符串str的左右空格。

**函数语法**

```
STRING TRIM(STRING str);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT TRIM(' abc ');
```

`--` 返回结果

```
+------+
| abc  |
+------+
```

##### LTRIM

本文介绍如何在MaxCompute中使用字符串函数LTRIM，用于去除输入字符串的左边空格。

**操作说明**

###### 使用说明

去除输入字符串str的左边空格。

**函数语法**

```
STRING LTRIM(STRING str);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT LTRIM(' abc ');
```

`--` 返回结果

```
+------+
| abc  |
+------+
```

##### RTRIM

本文介绍如何在MaxCompute中使用字符串函数RTRIM，用于去除输入字符串的右边空格。

**操作说明**

###### 使用说明

去除输入字符串str的右边空格。

**函数语法**

```
STRING RTRIM(STRING str);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。

**返回值**

大数据计算服务返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT RTRIM('a abc ');
```

`--` 返回结果

```
+------+
| a abc|
+------+
```

##### REVERSE

本文介绍如何在MaxCompute中使用字符串函数REVERSE，用于返回倒序字符串。

**操作说明**

###### 使用说明

返回倒序字符串。

**函数语法**

```
STRING REVERSE(STRING str);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT REVERSE('abcedfg');
```

`--` 返回结果

```
+---------+
| gfdecba |
+---------+
```

##### SPACE

本文介绍如何在MaxCompute中使用字符串函数SPACE，用于返回指定长度的空格字符串。

**操作说明**

###### 使用说明

返回长度为n的字符串。

**函数语法**

```
STRING SPACE(BIGINT n);
```

大数据计算服务

**参数说明**

n：必填，BIGINT类型。长度不超过 `2MB` 。如果为空，则会报错。

**返回值**

返回STRING类型。

##### 使用示例

```
SELECT LENGTH(SPACE(10));
```

`--` 返回结果

```
+------+
| 10   |
+------+
```

`--` 长度超过`2 MB`，会报错。

```
SELECT SPACE(400000000000);
```

##### REPEAT

本文介绍如何在MaxCompute中使用字符串函数REPEAT，用于将字符串重复指定次数后返回。

**操作说明**

###### 使用说明

返回重复n次后的str字符串。

**函数语法**

```
STRING REPEAT(STRING str, BIGINT n);
```

**参数说明**

str：必填，STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。 n：必填，BIGINT类型。长度不超过2 MB。如果为空，则会报错。

**返回值**

返回STRING类型。

##### 使用示例

`--` 将字符串`'abc'`重复5次。

```
SELECT REPEAT('abc', 5);
```

`--` 返回结果

```
+-------------------+
| abcabcabcabcabc   |
+-------------------+
```

##### ASCII

**操作说明**

大数据计算服务

###### 使用说明

**函数语法**

```
BIGINT ascii(STRING str);
```

**参数说明**

str：STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换为 STRING类型后参与运算，输入为其他类型会报错。

**返回值**

BIGINT类型。

##### 使用示例

```
SELECT ASCII('abcde');
```

`--` 返回结果

```
+-------+
|  _c0  |
+-------+
|   97  |
+-------+
```

##### 新扩展字符串函数

###### 使用说明

**操作说明**

升级到MaxCompute 2.0以后，产品扩展了新的字符串函数，在使用新函数的SQL前，需要添加如下Set语句。

```
SET odps.sql.type.system.odps2=true;
```

**说明**

上述Set语句和新函数的SQL语句需要同时提交运行。

###### CONCAT_WS

函数声明如下。 用途：返回将参数中的所有字符串按照指定的分隔符连接在一起的结果。 参数说明：
**SEP**：STRING类型的分隔符。如果不指定，返回结果时会报错。
大数据计算服务
**a, b...**：STRING类型。如果输入为BIGINT、DECIMAL、DOUBLE或者DATETIME类型，则会隐式转换
为STRING类型后参与运算，输入为其它类型会报错。 返回值：STRING类型。如果没有输入参数或者某个输入参数为NULL，结果均返回NULL。 示例如下。

```
concat_ws(':','name','hanmeimei')='name:hanmeimei'
```

###### LPAD

本文介绍如何在MaxCompute中使用字符串函数LPAD，用于将字符串向左补足到指定长度。

**操作说明**

###### 使用说明

用b字符串将a字符串向左补足到len位。

**函数语法**

```
STRING LPAD(STRING a, INT len, STRING b);
```

**参数说明**

a：必填，STRING类型。 len：必填，INT整型。 b：必填，STRING类型。

**返回值**

返回STRING类型。 如果len小于a的位数，则返回a从左开始截取len位字符。如果len为0，则返回空。 如果没有输入参数或任一输入参数值为NULL，返回NULL。如果len大于a的位数且小于a和b的位数之和，则按照b字符从左到右的顺序将a字符串向左补足到len位。

##### 使用示例

大数据计算服务 `--` 向左补足到`10`位，返回`12abcdefgh`。

```
SELECT LPAD('abcdefgh', 10, '12');
```

`--` 返回结果

```
+----------------+
| 12abcdefgh     |
+----------------+
```

`-- len`小于a的位数，从左截取5位，返回`abcde`。

```
SELECT LPAD('abcdefgh', 5, '12');
```

`--` 返回结果

```
+---------+
| abcde   |
+---------+
```

`-- len`为0，返回空串。

```
SELECT LPAD('abcdefgh', 0, '12');
```

`--` 返回结果

```
+------+
|      |
+------+
```

`--` 输入参数为`NULL`，返回`NULL`。

```
SELECT LPAD(NULL, 0, '12');
```

`--` 返回结果

```
+------+
| NULL |
+------+
```

`--` 向左补足到9位，返回`1abcdefgh`。

```
SELECT LPAD('abcdefgh', 9, '12');
```

`--` 返回结果

```
+---------------+
| 1abcdefgh     |
+---------------+
```

###### RPAD

本文介绍如何在MaxCompute中使用字符串函数RPAD，用于将字符串向右补足到指定长度。

**操作说明**

###### 使用说明

用b字符串将a字符串向右补足到len位。

**函数语法**

```
STRING RPAD(STRING a, INT len, STRING b);
```

**参数说明**

大数据计算服务 a：必填，STRING类型。 len：必填，INT整型。 b：必填，STRING类型。

**返回值**

返回STRING类型。 如果len小于a的位数，则返回a从左开始截取len位字符。如果len为0，则返回空。 如果没有输入参数或任一输入参数值为NULL，返回NULL。如果len大于a的位数且小于a和b的位数之和，则按照b字符从左到右的顺序将a字符串向右补足到len位。

##### 使用示例

`--` 向右补足到`10`位，返回`abcdefgh12`。

```
SELECT RPAD('abcdefgh', 10, '12');
```

`--` 返回结果

```
+----------------+
| abcdefgh12     |
+----------------+
```

`-- len`小于a的位数，从左截取5位，返回`abcde`。

```
SELECT RPAD('abcdefgh', 5, '12');
```

`--` 返回结果

```
+---------+
| abcde   |
+---------+
```

`-- len`为0，返回空串。

```
SELECT RPAD('abcdefgh', 0, '12');
```

`--` 返回结果

```
+------+
|      |
+------+
```

`--` 输入参数为`NULL`，返回`NULL`。

```
SELECT RPAD(NULL, 0, '12');
```

`--` 返回结果

```
+------+
| NULL |
+------+
```

`--` 向右补足到9位，返回`abcdefgh1`。

```
SELECT RPAD('abcdefgh', 9, '12');
```

`--` 返回结果

```
+---------------+
| abcdefgh1     |
+---------------+
```

大数据计算服务

###### REPLACE

本文介绍如何在MaxCompute中使用字符串函数REPLACE，用于用指定字符串替换源字符串中匹配的子串。

**操作说明**

###### 使用说明

用NEW字符串替换a字符串中与OLD字符串完全重合的部分并返回a。

**函数语法**

```
STRING REPLACE(STRING a, STRING OLD, STRING NEW);
```

**参数说明**

a：必填，STRING类型。源字符串。 OLD：必填，STRING类型。要被替换的子串。 NEW：必填，STRING类型。用于替换的目标字符串。

**返回值**

返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

`--` 替换匹配的子串。

```
SELECT REPLACE('ababab', 'abab', '12');
```

`--` 返回结果

```
+------+
| 12ab |
+------+
```

`-- OLD`不存在于源字符串中，返回原字符串。

```
SELECT REPLACE('ababab', 'cdf', '123');
```

`--` 返回结果

```
+--------+
| ababab |
+--------+
```

`-- OLD`为`NULL`，返回`NULL`。

```
SELECT REPLACE('123abab456ab', NULL, 'abab');
```

`--` 返回结果

```
+------+
| NULL |
+------+
```

###### SOUNDEX

本文介绍如何在MaxCompute中使用字符串函数SOUNDEX，用于将普通字符串转换成soundex字符串。 大数据计算服务

**操作说明**

###### 使用说明

**函数语法**

```
STRING SOUNDEX(STRING a);
```

**参数说明**

a：必填，STRING类型。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT SOUNDEX('hello');
```

`--` 返回结果

```
+------+
| H400 |
+------+
```

###### SUBSTRING_INDEX

本文介绍如何在MaxCompute中使用字符串函数SUBSTRING_INDEX，用于按分隔符截取字符串指定段之前的内容。

**操作说明**

###### 使用说明

截取字符串a第count个分隔符之前的字符串，如果count为正，则从左边开始截取；如果为负，则从右边开始截取。

**函数语法**

```
STRING SUBSTRING_INDEX(STRING a, STRING SEP, INT count);
```

**参数说明**

a：必填，STRING类型，待截取的字符串。 SEP：必填，STRING类型，分隔符。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 从左截取第2个分隔符之前的内容，返回`https://help.aliyun`。

```
SELECT SUBSTRING_INDEX('https://help.aliyun.com', '.', 2);
```

`--` 返回结果

```
+----------------------+
| https://help.aliyun  |
+----------------------+
```

`--` 从右截取第2个分隔符之后的内容，返回`aliyun.com`。

```
SELECT SUBSTRING_INDEX('https://help.aliyun.com', '.', -2);
```

`--` 返回结果

```
+------------+
| aliyun.com |
+------------+
```

`--` 分隔符为`NULL`，返回`NULL`。

```
SELECT SUBSTRING_INDEX('https://help.aliyun.com', NULL, 2);
```

`--` 返回结果

```
+------+
| NULL |
+------+
```

###### TRANSLATE

本文介绍如何在MaxCompute中使用字符串函数TRANSLATE，用于将字符串中指定字符逐个替换为对应字符。

**操作说明**

###### 使用说明

将str1中出现在str2中的字符逐个替换成str3中对应位置的字符。

**函数语法**

```
STRING TRANSLATE(STRING|VARCHAR str1, STRING|VARCHAR str2, STRING|VARCHAR str3);
```

**参数说明**

str1：必填，STRING或VARCHAR类型，待替换的源字符串。如果输入为BIGINT、DECIMAL、 DOUBLE或DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型会报错。 str2：必填，STRING或VARCHAR类型，要被替换的字符集合。 str3：必填，STRING或VARCHAR类型，替换目标字符集合。

**返回值**

返回STRING类型。 如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 将`'puter'`逐个替换为`'pute'`。

```
SELECT TRANSLATE('MaxComputer', 'puter', 'pute');
```

`--` 返回结果

```
+--------------+ +--------------+
```

`-- str2`中的字符不存在于`str1`中，返回原字符串。

```
SELECT TRANSLATE('aaa', 'b', 'c');
```

`--` 返回结果

```
+------+
| aaa  |
+------+
```

`-- str3`为`NULL`，返回`NULL`。

```
SELECT TRANSLATE('MaxComputer', 'puter', NULL);
```

`--` 返回结果

```
+------+
| NULL |
+------+
```

###### URL_ENCODE

本文介绍如何在MaxCompute中使用字符串函数URL_ENCODE，用于将输入字符串编码为application/x-

**操作说明**

###### 使用说明

将输入字符串编码为application/x-www-form-urlencoded MIME格式。a~z、A~Z保持不变。英文句点（.）、短划线（-）、星号（*）和下划线（_）保持不变。空格转为加号（+）。其余字符根据指定的 encoding转为字节值，然后将每个字节值表示为%xy的格式，xy是该字符的十六进制表示方式。

**函数语法**

```
STRING URL_ENCODE(STRING input[, STRING encoding]);
```

**参数说明**

input：必填，STRING类型，要输入的字符串。 encoding：选填，STRING类型，指定的编码格式，支持GBK或UTF-8等标准编码格式，不输入默认为UTF-8。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 默认`UTF-8`编码。

```
SELECT URL_ENCODE('示例for URL_ENCODE:// (fdsf)');
```

`--` 返回结果

```
+----------------------------------------------------+
| %CA%BE%EF%BF%BD%EF%BF%BDfor+URL_ENCODE%3A%2F%2F+%28fdsf%29 |
+----------------------------------------------------+
```

`--` 指定`GBK`编码。

```
SELECT URL_ENCODE('Example for URL_ENCODE:// dsf(fasfs)', 'GBK');
```

`--` 返回结果

```
+---------------------------------------------------+
| Example+for+URL_ENCODE%3A%2F%2F+dsf%28fasfs%29    |
+---------------------------------------------------+
```

###### URL_DECODE

本文介绍如何在MaxCompute中使用字符串函数URL_DECODE，用于将URL编码的字符串转换为正常字

**操作说明**

###### 使用说明

将输入字符串从application/x-www-form-urlencoded MIME格式转换为正常字符串，是 URL_ENCODE的逆过程。a~z、A~Z保持不变。英文句点（.）、短划线（-）、星号（*）和下划线 （_）保持不变。加号（+）转为空格。首先按照百分号（%）解码，%xy格式的序列转换为对应的字节值，然后按照第二个参数的编码格式解码，连续的字节值根据输入的encoding编码格式解码成对应的字符串。其余的字符保持不变。函数最终的返回值是UTF-8编码的字符串。

**函数语法**

```
STRING URL_DECODE(STRING input[, STRING encoding]);
```

**参数说明**

input：必填，STRING类型，要输入的字符串。 encoding：选填，STRING类型，指定的编码格式，支持GBK或UTF-8等标准编码格式，不输入默认为UTF-8。

**返回值**

返回STRING类型。 如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 默认`UTF-8`解码。

```
SELECT URL_DECODE('%E7%A4%BA%E4%BE%8Bfor+url_decode%3A%2F%2F+%28fdsf%29');
```

`--` 返回结果

```
+--------------------------------+ +--------------------------------+
```

`--` 指定`GBK`解码。

```
SELECT URL_DECODE('Example+for+url_decode+%3A%2F%2F+dsf%28fasfs%29', 'GBK');
```

`--` 返回结果

```
+---------------------------------------+ +---------------------------------------+
```

###### JSON_TUPLE

本文介绍如何在MaxCompute中使用字符串函数JSON_TUPLE，用于从标准JSON字符串中按一组键提取对应的字符串。

**操作说明**

###### 使用说明

用于一个标准的JSON字符串中，按照输入的一组键（key1, key2, ...）抽取各个键指定的字符串。

**函数语法**

```
STRING JSON_TUPLE(STRING json, STRING key1, STRING key2, ...);
```

**参数说明**

json：必填，STRING类型，标准的JSON格式字符串。 key：必填，STRING类型，用于描述在JSON中的path，一次可输入多个，不能以美元符号（$）开头。

**返回值**

返回STRING类型。 如果JSON为空或者为非法的JSON格式，返回NULL。 如果键key为空或者不合法（JSON中不存在），返回NULL。如果JSON合法，键key也存在，则返回对应字符串。 支持包含中文的JSON数据解析。支持多层嵌套的JSON数据解析。支持包含多重嵌套的数组的JSON数据解析。 解析行为和设置了 SET odps.sql.udf.getjsonobj.new=true; 后的GET_JSON_OBJECT的行为保持一致。 在需要对同一个JSON字符串多次解析的情况下，相比于多次调用GET_JSON_OBJECT，JSON_TUPLE 可以一次输入多个key，且JSON字符串只被解析一次，效率更高。 JSON_TUPLE是UDTF，在需要选取其他的列的时候应配合LATERAL VIEW使用。

##### 使用示例

`--` 假设表`school`的值如下。

```
CREATE TABLE school (Id BIGINT, json STRING);
```

`'{"`校名`":"`湖畔大学""地址`":"`杭大数据计算服务 `INSERT INTO school VALUES (1, '{"`校名`":"`湖畔大学`","`地址`":"`杭

```
州","SchoolRank":"00","Class1":{"Student":[{"studentId":1,"scoreRankIn3Year":[1,2,[3, 2,6]]},{"studentId":2,"scoreRankIn3Year":[2,3,[4,3,1]]}]}}');
```

`--` 提取`JSON`对象信息。

```
SELECT JSON_TUPLE(school.json, "SchoolRank", "Class1") AS (item0, item1) FROM school;
```

`--` 本语句相当于下面的语句。

```
SELECT GET_JSON_OBJECT(school.json, "$.SchoolRank") item0, GET_JSON_OBJECT(school.json, "$.Class1") item1 FROM school;
```

`--` 返回结果

```
+-------+------------------------------------------------------------------------------ -----------------------------+
| item0 | item1
```

|

```json
+-------+------------------------------------------------------------------------------ -----------------------------+
| 00    | {"Student":[{"studentId":1,"scoreRankIn3Year":[1,2,[3,2,6]]},
{"studentId":2,"scoreRankIn3Year":[2,3,[4,3,1]]}]} | +-------+------------------------------------------------------------------------------ -----------------------------+
```

`--` 支持包含中文的`JSON`数据解析。

```
SELECT JSON_TUPLE(school.json, "校名", "地址") AS (item0, item1) FROM school;
```

`--` 返回结果

```
+----------+--------+
| item0    | item1  |
+----------+--------+
```

| 湖畔大学 | 杭州 |

```
+----------+--------+
```

`--` 支持多层嵌套的`JSON`数据解析。

```
SELECT sc.Id, q.item0, q.item1 FROM school sc LATERAL VIEW JSON_TUPLE(sc.json, "Class1.Student.[*].studentId", "Clas s1.Student.[0].scoreRankIn3Year") q AS item0, item1;
```

`--` 返回结果

```
+------+-------+------------------+
| Id   | item0 | item1            |
+------+-------+------------------+
| 1    | [1,2] | [1,2,[3,2,6]]    |
+------+-------+------------------+
```

`--` 支持包含多重嵌套的数组的`JSON`数据解析。

```
SELECT sc.Id, q.item0, q.item1 FROM school sc LATERAL VIEW JSON_TUPLE(sc.json, "Class1.Student[0].scoreRankIn3Year[2]", "Class1.Student[0].scoreRankIn3Year[2][1]") q AS item0, item1;
```

`--` 返回结果

```
+------+---------+-------+
| Id   | item0   | item1 |
+------+---------+-------+
```

大数据计算服务 + + + +

```
| 1    | [3,2,6] | 2     |
+------+---------+-------+
```

###### FROM_JSON

本文介绍如何在MaxCompute中使用字符串函数FROM_JSON，用于根据JSON字符串和Schema信息返回

**操作说明**

###### 使用说明

根据给定的JSON字符串和Schema信息，返回一个ARRAY、MAP或STRUCT类型的对象。

**函数语法**

```
FROM_JSON(STRING jsonStr, STRING schema);
```

**参数说明**

jsonStr：必填，STRING类型，输入的JSON字符串。

| array<bigint> | 、 | map<string, array<string>> |
|---|---|---|

JSON和MaxCompute的类型对应关系如下。

| JSON | MaxCompute |
|---|---|
| Object | STRUCT/MAP/STRING |
| Array | ARRAY/STRING |
| Number | TINYINT/SMALLINT/IBT/BIGINT/FLOAT/DOUBLE/DECIMAL/STRING |
| true/false | BOOLEAN/STRING |
| String | STRING |
| null | 所有类型 |

**说明**

对于Object和Array类型，会采用尽可能解析的方式，对于不匹配的类型会忽略。

**返回值**

如果schema为空，则会报错。 大数据计算服务

##### 使用示例

```
SELECT FROM_JSON('{"a":1, "b":0.8}', 'a INT, b DOUBLE');
```

`--` 返回结果

```
+--------------------------+
| {"a":1, "b":0.8}         |
+--------------------------+
```

`--` 解析包含字符串值的`JSON`对象。

```
SELECT FROM_JSON('{"time":"26/08/2015"}', 'time STRING');
```

`--` 返回结果

```
+-----------------------------+
| {"time":"26/08/2015"}       |
+-----------------------------+
```

`-- schema`中包含`JSON`中不存在的字段，返回`NULL`。

```
SELECT FROM_JSON('{"a":1, "b":0.8}', 'a INT, b DOUBLE, c STRING');
```

`--` 返回结果

```
+---------------------------------+
| {"a":1, "b":0.8, "c":NULL}      |
+---------------------------------+ SELECT FROM_JSON('[1, 2, 3, "a"]', 'ARRAY<BIGINT>');
```

`--` 返回结果

```
+--------------+
| [1, 2, 3]    |
+--------------+
```

###### TO_JSON

**操作说明**

###### 使用说明

根据给定的类型转换为一个JSON字符串。

**函数语法**

```
TO_JSON(expr);
```

**参数说明**

**返回值**

返回JSON格式的字符串。

##### 使用示例

大数据计算服务

```
SELECT TO_JSON(named_struct('a', 1, 'b', 2));
```

`--` 返回结果

```
+---------------+
|      _c0      |
+---------------+
| {"a":1,"b":2} |
+---------------+ SELECT TO_JSON(named_struct('time', "26/08/2015"));
```

`--` 返回结果

```
+-------------------------+
|           _c0           |
+-------------------------+
|  {"time":"26/08/2015"}  |
+-------------------------+ SELECT TO_JSON(array(named_struct('a', 1, 'b', 2)));
```

`--` 返回结果

```
+-----------------+
|       _c0       |
+-----------------+
| [{"a":1,"b":2}] |
+-----------------+ SELECT TO_JSON(map('a', named_struct('b', 1)));
```

`--` 返回结果

```
+---------------+
|      _c0      |
+---------------+
| {"a":{"b":1}} |
+---------------+ SELECT TO_JSON(map('a', 1));
```

`--` 返回结果

```
+---------+
|   _c0   |
+---------+
| {"a":1} |
+---------+ SELECT TO_JSON(array((map('a', 1))));
```

`--` 返回结果

```
+-----------+
|    _c0    |
+-----------+
| [{"a":1}] |
+-----------+
```

大数据计算服务

#### 日期函数

##### DATEADD

本文介绍如何在MaxCompute中使用日期函数DATEADD，用于按照指定的单位（datepart）和幅度 （delta）修改时间数据的值。

**操作说明**

###### 使用说明

**函数语法**

```
DATETIME DATEADD(DATETIME date, BIGINT delta, STRING datepart);
```

**参数说明**

date：日期值，DATE、DATETIME、TIMESTAMP类型。如果输入为STRING类型，则会隐式转换为 DATETIME类型后参与运算。输入为其他数据类型时会报错。 delta：修改幅度，BIGINT类型。如果输入为STRING类型或DOUBLE类型，则会隐式转换为BIGINT 类型后参与运算。输入为其他数据类型时报错。如果delta大于0，修改幅度为加；否则为减。

**说明**

按照指定的单位增减delta时，会导致更高单位的进位或退位。年、月、时和分秒分别按照 10进制、12进制、24进制和60进制进行计算。 当delta的单位是月时，如果DATETIME的月部分在增加delta值之后不造成day溢出，则保持day值不变，否则将day值设置为结果月份的最后1天。 datepart：指定修改的单位，STRING类型常量。非常量、不支持的格式或其他类型时会报错。此字段的取值遵循STRING与DATETIME类型转换的约定，即yyyy表示年，mm表示月。此外也支持扩展的日期格式：年-year、月-month或-mon、日-day和小时-hour。关于类型转换的规则请参见STRING类型与DATETIME类型之间的转换。

**返回值**

DATETIME类型。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务 `--` 加1天

```
SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 1, 'dd');
```

`--` 返回结果：结果超出当年2月份的最后一天，实际值为下个月的第1天。

```
+---------------------+
| _c0                 |
+---------------------+
| 2005-03-01 00:00:00 |
+---------------------+
```

`--` 减1天

```
SELECT DATEADD(DATETIME '2005-02-28 00:00:00', -1, 'dd');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2005-02-27 00:00:00 |
+---------------------+
```

`--` 加`20`个月

```
SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 20, 'mm');
```

`--` 返回结果：月份溢出，年份加1。

```
+---------------------+
| _c0                 |
+---------------------+
| 2006-10-28 00:00:00 |
+---------------------+
```

`--` 加1个月

```
SELECT DATEADD(DATETIME '2005-02-28 00:00:00', 1, 'mm');
```

`--` 返回结果：

```
+---------------------+
| _c0                 |
+---------------------+
| 2005-03-28 00:00:00 |
+---------------------+ SELECT DATEADD(DATETIME '2005-01-29 00:00:00', 1, 'mm');
```

`--` 返回结果：`2005`年2月没有`29`日，日期截取至当月最后1天。

```
+---------------------+
| _c0                 |
+---------------------+
| 2005-02-28 00:00:00 |
+---------------------+
```

`--` 减1个月

```
SELECT DATEADD(DATETIME '2005-03-30 00:00:00', -1, 'mm');
```

`--` 返回结果：`2005`年2月没有`30`日，日期截取至当月最后1天。

```
+---------------------+
| _c0                 |
+---------------------+
| 2005-02-28 00:00:00 |
+---------------------+
```

大数据计算服务示例2：DATETIME用常量表示。

```
SELECT DATEADD(DATETIME '2005-03-30 00:00:00', -1, 'mm');
```

`--` 在`MaxCompute SQL`中，`DATETIME`类型没有直接的常量表示方式，此处为错误的使用方式。

```
SELECT DATEADD(CAST("2005-03-30 00:00:00" AS DATETIME), -1, 'mm');
```

`--` 如果需要描述`DATETIME`类型的常量，要将`STRING`类型常量显式转换为`DATETIME`类型。

##### DATEDIFF

本文介绍如何在MaxCompute中使用日期函数DATEDIFF，用于计算两个时间在指定时间单位的差值。

**操作说明**

###### 使用说明

如果相减的时间精度更高，比 `datepart` 更精确的部分会被舍弃。例如 `datepart` 的单位是天，则系统计算时会按照 `datepart` 切掉低单位部分，然后再计算结果。此处的低单位部分即为上面舍弃的部分。

**函数语法**

```
BIGINT DATEDIFF(DATETIME date1, DATETIME date2, STRING datepart);
```

**参数说明**

`date1` 、 `date2` ：被减数和减数，DATE、DATETIME、TIMESTAMP类型。如果输入为STRING 类型，则会隐式转换为DATETIME类型后参与运算，输入为其它数据类型会报错。 `datepart` ：时间单位，STRING类型常量。支持扩展的日期格式。如果 `datepart` 不符合指定格式或为其它数据类型，则会报错。

**返回值**

BIGINT类型。如果任意一个输入参数为NULL，返回NULL。如果 `date1` 小于 `date2` ，返回值为负数。

##### 使用示例

```
-- 假设start='2005-12-31 23:59:59'，end='2006-01-01 00:00:00'，则： SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'dd') ;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'mm') ;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
```

|1
|
大数据计算服务

```
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'yyyy ');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'hh') ;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'mi') ;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2006-01-01 00:00:00', DATETIME '2005-12-31 23:59:59', 'ss') ;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1      |
+--------+ SELECT DATEDIFF(DATETIME '2013-05-31 13:00:00', TO_DATE('2013-05-31 12:30:00', 'yyyymm-dd hh:mi:ss'), 'ss');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1800   |
+--------+ SELECT DATEDIFF(DATETIME '2013-05-31 13:00:00', TO_DATE('2013-05-31 12:30:00', 'yyyymm-dd hh:mi:ss'), 'mi');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
|30
```

|
大数据计算服务

```
| 30     |
+--------+
```

`--` 假设 `start='2018-06-04 19:33:23.234'`，`end='2018-06-04 19:33:23.250'`，含毫秒的日期不属于标准 `DATETIME` 样式，不能直接隐式转换，此处需进行显示转换。

```
SELECT DATEDIFF(TO_DATE('2018-06-04 19:33:23.250', 'yyyy-MM-dd hh:mi:ss.ff3'), TO_DAT E('2018-06-04 19:33:23.234', 'yyyy-MM-dd hh:mi:ss.ff3'), 'ff3');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 16     |
+--------+
```

##### DATEPART

本文介绍如何在MaxCompute中使用日期函数DATEPART，用于提取日期中符合指定时间单位的值。

**操作说明**

###### 使用说明

**函数语法**

```
BIGINT DATEPART(DATETIME date, STRING datepart);
```

**参数说明**

`date` ：DATE、DATETIME、TIMESTAMP类型。如果输入为STRING类型，则会隐式转换为 DATETIME类型后参与运算，输入为其它数据类型会报错。 `datepart` ：STRING类型常量，支持扩展的日期格式。如果 `datepart` 不符合指定格式或数据类型则会报错。

**返回值**

BIGINT类型。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT DATEPART(TO_DATE('2017-06-08 01:10:00', 'yyyy-mm-dd hh:mi:ss'), 'yyyy');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 2017   |
+--------+ SELECT DATEPART(TO_DATE('2017-06-08 01:10:00', 'yyyy-mm-dd hh:mi:ss'), 'mm');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 6      |
+--------+
```

大数据计算服务

##### DATETRUNC

本文介绍如何在MaxCompute中使用日期函数DATETRUNC，用于返回日期被截取指定时间单位后的日期值。

**操作说明**

###### 使用说明

**函数语法**

```
DATETIME DATETRUNC(DATETIME date, STRING datepart);
```

**参数说明**

date：DATE、DATETIME、TIMESTAMP类型。如果输入为STRING类型，则会隐式转换为 DATETIME类型后参与运算。输入为其它数据类型则会报错。 datepart：STRING类型常量。支持扩展的日期格式。如果datepart不符合指定格式或者数据类型则会报错。

**返回值**

DATETIME类型。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

`--` 返回日期被截取指定时间单位`yyyy`后的日期值。本示例截取为`yyyy=2017`后的日期值。

```
SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'yyyy');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-01-01 00:00:00 |
+---------------------+
```

`--` 返回日期被截取指定时间单位`month`后的日期值。本示例截取为`month=12`后的日期值。

```
SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'month');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-12-01 00:00:00 |
+---------------------+
```

`--` 返回日期被截取指定时间单位`DD`后的日期值。本示例截取为`DD=7`后的日期值。

```
SELECT DATETRUNC(TO_DATE('2017-12-07 16:28:46', 'yyyy-mm-dd hh:mi:ss'), 'DD');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-12-07 00:00:00 |
+---------------------+
```

大数据计算服务

##### GETDATE

本文介绍如何在MaxCompute中使用日期函数GETDATE，用于获取当前系统时间。

**操作说明**

###### 使用说明

获取当前系统时间。使用东八区时间作为MaxCompute标准时间。

**函数语法**

```
DATETIME GETDATE();
```

**参数说明**

无。

**返回值**

返回当前日期和时间，DATETIME类型。

**说明**

在一个MaxCompute SQL任务中（以分布式方式执行），GETDATE返回一个固定的值。返回结果会是MaxCompute SQL执行期间的任意时间，时间精度精确到秒（如果开启了新数据类型2.0，时间精度精确到毫秒）。

##### 使用示例

```
SELECT GETDATE();
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2026-06-26 09:39:59 |
+---------------------+
```

##### ISDATE

本文介绍如何在MaxCompute中使用日期函数ISDATE，用于判断日期字符串能否根据格式串转换为日期值。

**操作说明**

###### 使用说明

判断一个日期字符串能否根据对应的格式串转换为一个日期值，如果转换成功返回 `true` ，否则返回 `false` 。

**函数语法**

```
BOOLEAN ISDATE(STRING date, STRING format);
```

**参数说明**

date：STRING类型。如果输入为BIGINT、DOUBLE、DECIMAL或DATETIME类型，会隐式转换为 STRING类型后参与运算。输入为其它数据类型会报错。 大数据计算服务 format：STRING类型常量，不支持日期扩展格式。输入为其它数据类型会报错。如果format中出现多余的格式串，则只取第一个格式串对应的日期数值，其余的会被视为分隔符。例如ISDATE("1234yyyy", "yyyy-yyyy")，会返回 `true` 。

**返回值**

BOOLEAN类型。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT ISDATE('2023-01-15', 'yyyy-MM-dd');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ISDATE('2023-13-15', 'yyyy-MM-dd');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### LASTDAY

本文介绍如何在MaxCompute中使用日期函数LASTDAY，用于取日期所在月的最后一天。

**操作说明**

###### 使用说明

取date所在月的最后一天，截取到天，时分秒部分为00:00:00。

**函数语法**

**参数说明**

date：DATETIME类型。如果输入为STRING类型，则会隐式转换为DATETIME类型后参与运算。输入为其它数据类型会报错。

**返回值**

DATETIME类型。如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT LASTDAY(DATETIME '2023-02-15 10:30:45');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2023-02-28 00:00:00 |
+---------------------+ SELECT LASTDAY(DATETIME '2024-02-15 10:30:45');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2024-02-29 00:00:00 |
+---------------------+
```

##### TO_DATE

本文介绍如何在MaxCompute中使用日期函数TO_DATE，用于将一个format格式的字符串转成日期值。

**操作说明**

###### 使用说明

将一个format格式的字符串date转成日期值。

**函数语法**

```
DATETIME TO_DATE(STRING date, STRING format);
```

**参数说明**

date：STRING类型，要转换的字符串格式的日期值。如果输入为BIGINT、DOUBLE、DECIMAL或 DATETIME类型，则会隐式转换为STRING类型后参与运算，输入为其它类型或者空字符串时会报错。 format：STRING类型常量，日期格式。非常量或为其他类型会报错。不支持日期扩展格式，其他字符在解析时作为无用字符忽略。参数至少包含yyyy，否则报错。如果出现多余的格式串，则只取第一个格式串对应的日期数值，其余的会被视为分隔符。例如 `TO_DATE('1234-2234 ', 'yyyy-yyyy ')` 会

```
返回 1234-01-01 00:00:00 。
```

**返回值**

DATETIME类型。格式为 `yyyy-mm-dd hh:mi:ss:ff3` 。如果任意一个输入参数为NULL，返回NULL。

**说明**

yyyy为4位数的年，mm为2位数的月，dd为2位数的日，hh为24小时制的时，mi为2位数的分钟，ss为2位数秒，ff3为3位精度毫秒。

##### 使用示例

`SELECT TO_DATE('`阿里巴巴`2017-12*03', '`阿里巴巴yyyy-mm*dd'); `--` 返回结果

```
+---------------------+
| _c0                 |
```

大数据计算服务

```
+---------------------+
| 2017-12-03 00:00:00 |
+---------------------+ SELECT TO_DATE('20170718', 'yyyymmdd');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-07-18 00:00:00 |
+---------------------+ SELECT TO_DATE('201707182030', 'yyyymmddhhmi');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-07-18 20:30:00 |
+---------------------+ SELECT TO_DATE('2017718', 'yyyymmdd');
```

`--` 返回结果（格式不符合，返回`NULL`）

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

`SELECT TO_DATE('`阿里巴巴`2017-12*3', '`阿里巴巴yyyy-mm*dd'); `--` 返回结果（格式不符合，返回`NULL`）

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT TO_DATE('2017-24-01', 'yyyy');
```

`--` 返回结果（格式不符合，返回`NULL`）

```
+------+
| _c0  |
+------+
| NULL |
+------+ SELECT TO_DATE('20181030 15-13-12.345', 'yyyymmdd hh-mi-ss.ff3');
```

`--` 返回结果

```
+--------------------------+
| _c0                      |
```

大数据计算服务

```
+--------------------------+
| 2018-10-30 15:13:12.000  |
+--------------------------+
```

##### TO_CHAR

本文介绍如何在MaxCompute中使用日期函数TO_CHAR，用于将日期类型按照指定格式转成字符串。

**操作说明**

###### 使用说明

将日期类型date按照format指定的格式转成字符串。

**函数语法**

```
STRING TO_CHAR(DATETIME date, STRING format);
```

**参数说明**

date：DATETIME类型，要转换的日期值。如果输入为STRING类型，会隐式转换为DATETIME类型后参与运算。输入为其它数据类型会报错。 format：STRING类型常量。非常量或其他类型会报错。format中的日期格式部分会被替换成相应的数据，其他字符直接输出。

**返回值**

STRING类型。如果任意一个输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT TO_CHAR(TO_DATE('2017-12-03 00:00:00', 'yyyy-mm-dd hh:mi:ss'), '阿里金融yyyy-mm *dd');
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
```

| 阿里金融2017-12*03 |

```
+--------------------+ SELECT TO_CHAR(TO_DATE('2017-07-18 00:00:00', 'yyyy-mm-dd hh:mi:ss'), 'yyyymmdd');
```

`--` 返回结果

```
+----------+
| _c0      |
+----------+
| 20170718 |
+----------+
```

`--` 以下示例格式不符合，返回报错。 `SELECT TO_CHAR('`阿里巴巴`2017-12*3', '`阿里巴巴yyyy-mm*dd');

```
SELECT TO_CHAR('2017-24-01', 'yyyy'); SELECT TO_CHAR('2017718', 'yyyymmdd');
```

##### UNIX_TIMESTAMP

大数据计算服务本文介绍如何在MaxCompute中使用日期函数UNIX_TIMESTAMP，用于将日期转化为整型的UNIX格式日期时间值。

**操作说明**

###### 使用说明

将日期 `date` 转化为整型的UNIX格式的日期时间值。

**函数语法**

**参数说明**

`date` ：DATETIME类型日期值。如果输入为STRING类型，则会隐式转换为DATETIME类型后参与运算。输入为其它数据类型会报错。当打开新数据类型Flag时，隐式转换会失败，此时需要通过CAST函数

**返回值**

BIGINT类型，表示UNIX格式日期值。如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT UNIX_TIMESTAMP(DATETIME '2009-03-20 11:11:00');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 1237518660 |
+------------+
```

##### FROM_UNIXTIME

本文介绍如何在MaxCompute中使用日期函数FROM_UNIXTIME，用于将数字型的UNIX时间日期值转为日期值。

**操作说明**

###### 使用说明

将数字型的UNIX时间日期值unixtime转为日期值。

**函数语法**

**参数说明**

unixtime：BIGINT类型，秒数，UNIX格式的日期时间值。

**返回值**

DATETIME类型的日期值。如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT FROM_UNIXTIME(123456789);
```

`--` 返回结果

```
+---------------------+
|         _c0         |
+---------------------+
| 1973-11-30 05:33:09 |
+---------------------+
```

##### WEEKDAY

本文介绍如何在MaxCompute中使用日期函数WEEKDAY，用于返回日期当前周的第几天。

**操作说明**

###### 使用说明

返回date日期当前周的第几天。

**函数语法**

```
BIGINT WEEKDAY(DATETIME date);
```

**参数说明**

date：DATETIME类型日期值。输入为其他数据类型会报错。

**返回值**

BIGINT类型。如果输入参数为NULL，返回NULL。周一作为一周的第一天，返回值为0。其他日期依次递增，周日返回6。

##### 使用示例

大数据计算服务

```
SELECT WEEKDAY(DATETIME '2023-06-26 00:00:00');
```

`--` 返回结果（周一）

```
+------+
| _c0  |
+------+
|  0   |
+------+ SELECT WEEKDAY(DATETIME '2023-06-27 00:00:00');
```

`--` 返回结果（周二）

```
+------+
| _c0  |
+------+
|  1   |
+------+ SELECT WEEKDAY(DATETIME '2023-07-02 00:00:00');
```

`--` 返回结果（周日）

```
+------+
| _c0  |
+------+
|  6   |
+------+
```

##### WEEKOFYEAR

本文介绍如何在MaxCompute中使用日期函数WEEKOFYEAR，用于返回日期date位于那一年的第几周。

**操作说明**

###### 使用说明

返回日期date位于哪一年的第几周。周一作为一周的第一天。

**说明**

如果这一周跨年，关于这一周属于上一年还是下一年，取决于这一周的大多数日期（4天以上）在哪一年。属于前一年，就是前一年的最后一周。属于后一年，就是后一年的第一周。

**函数语法**

**参数说明**

date：DATETIME类型日期值。如果输入为STRING类型，则会隐式转换为DATETIME类型后参与运算， 为其他数据类型会报错。

**返回值**

BIGINT类型。如果输入参数为NULL，返回NULL。

##### 使用示例

大数据计算服务

```
SELECT WEEKOFYEAR(TO_DATE("20141229", "yyyymmdd"));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 1          |
+------------+
```

`--` 虽然`20141229`属于`2014`年，但是这一周的大多数日期是在`2015`年，因此返回结果为1，表示是`2015`年的第一周。

```
SELECT WEEKOFYEAR(TO_DATE("20141231", "yyyymmdd"));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 1          |
+------------+ SELECT WEEKOFYEAR(TO_DATE("20151229", "yyyymmdd"));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 53         |
+------------+
```

##### 新扩展日期函数

###### 使用说明

本文介绍使用新扩展的日期函数要进行的设置。

**操作说明**

升级到MaxCompute 2.0以后，产品扩展了新的日期函数，在使用新函数的SQL前，需要添加如下SET语句。

```
SET odps.sql.type.system.odps2=true;
```

**说明**

上述SET语句和新函数的SQL语句需要同时提交运行。

###### YEAR

本文介绍如何在MaxCompute中使用日期函数YEAR，用于返回日期的年。

**操作说明**

###### 使用说明

返回日期 `date` 的年。 大数据计算服务

**函数语法**

```
INT YEAR(DATETIME/STRING date);
```

**参数说明**

`date` ：DATETIME或STRING类型日期值，日期格式至少包含yyyy-mm-dd且不含多余的字符串，否则返回NULL值。

**返回值**

INT类型。

##### 使用示例

大数据计算服务

```
SELECT YEAR('1970-01-01 12:30:00');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('1970-01-01');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('70-01-01');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 70     |
+--------+ SELECT YEAR('1970-01-01');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 1970   |
+--------+ SELECT YEAR('1970/03/09');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| NULL   |
+--------+ SELECT YEAR(NULL);
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### QUARTER

本文介绍如何在MaxCompute中使用日期函数QUARTER，用于返回一个日期的季度。 大数据计算服务

**操作说明**

###### 使用说明

返回一个日期的季度，范围是1~4。

**函数语法**

```
INT QUARTER(DATETIME/TIMESTAMP/STRING date);
```

**参数说明**

date：DATETIME、TIMESTAMP或STRING类型日期值，日期格式至少包含 `yyyy-mm-dd` ，其他数据类型会返回NULL。

**返回值**

INT类型。如果输入参数为NULL，返回NULL。

##### 使用示例

```
SELECT QUARTER('1970-11-12 10:00:00');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 4          |
+------------+ SELECT QUARTER('1970-11-12');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 4          |
+------------+
```

###### MONTH

**操作说明**

###### 使用说明

返回一个日期的月份。

**函数语法**

**参数说明**

date：DATETIME或STRING类型日期值，日期格式至少包含yyyy-mm-dd，其他数据类型会报错。

**返回值**

INT类型。

##### 使用示例

大数据计算服务

```
SELECT MONTH('2014-09-01');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 9    |
+------+ SELECT MONTH('20140901');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### DAY

本文介绍如何在MaxCompute中使用日期函数DAY，用于返回一个日期的天。

**操作说明**

###### 使用说明

返回一个日期的天。

**函数语法**

```
INT DAY(DATETIME/STRING date);
```

**参数说明**

date：DATETIME或STRING类型日期值，格式为yyyy-mm-dd或yyyy-mm-dd hh:mi:ss，其他数据类型会报错。

**返回值**

INT类型。

##### 使用示例

```
SELECT DAY('2014-09-01');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+ SELECT DAY('20140901');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

大数据计算服务

###### DAYOFMONTH

本文介绍如何在MaxCompute中使用日期函数DAYOFMONTH，用于返回日期内日部分的值。

**操作说明**

###### 使用说明

返回日期内日部分的值。例如2019年10月13日，执行命令 `INT DAYOFMONTH(2019-10-13)` ，返回结果为13。

**函数语法**

```
INT DAYOFMONTH(STRING date);
```

**参数说明**

date：STRING类型日期值，日期格式至少包含yyyy-mm-dd，其他数据类型会报错。

**返回值**

INT类型。

##### 使用示例

```
SELECT DAYOFMONTH('2019-09-01');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+ SELECT DAYOFMONTH('20190901');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### HOUR

本文介绍如何在MaxCompute中使用日期函数HOUR，用于返回日期内小时部分的值。

**操作说明**

###### 使用说明

返回日期内小时部分的值。

**函数语法**

```
INT HOUR(DATETIME/STRING date);
```

**参数说明**

`date` ：DATETIME或STRING类型日期值，为其他数据类型会报错。

**返回值**

大数据计算服务 INT类型。

##### 使用示例

```
SELECT HOUR('2014-09-01 12:00:00');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 12     |
+--------+ SELECT HOUR('12:00:00');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 12     |
+--------+ SELECT HOUR('20140901120000');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### MINUTE

本文介绍如何在MaxCompute中使用日期函数MINUTE，用于返回日期内分钟部分的值。

**操作说明**

###### 使用说明

返回日期内分钟部分的值。

**函数语法**

```
INT MINUTE(DATETIME/STRING date);
```

**参数说明**

date：DATETIME或STRING类型日期值，其他数据类型会报错。

**返回值**

INT 类型。

##### 使用示例

大数据计算服务

```
SELECT MINUTE('2014-09-01 12:30:00');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 30         |
+------------+ SELECT MINUTE('12:30:00');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 30         |
+------------+ SELECT MINUTE('20140901120000');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| NULL       |
+------------+
```

###### SECOND

本文介绍如何在MaxCompute中使用日期函数SECOND，用于返回日期内秒数部分的值。

**操作说明**

###### 使用说明

返回日期内秒数部分的值。

**函数语法**

```
INT SECOND(DATETIME/STRING date);
```

**参数说明**

`date` ：DATETIME或STRING类型日期值，其他数据类型会报错。

**返回值**

INT类型。

##### 使用示例

大数据计算服务

```
SELECT SECOND('2014-09-01 12:30:45');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 45     |
+--------+ SELECT SECOND('12:30:45');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| 45     |
+--------+ SELECT SECOND('20140901123045');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### FROM_UTC_TIMESTAMP

本文介绍如何在MaxCompute中使用日期函数FROM_UTC_TIMESTAMP，用于将UTC时区的时间戳转换成指定时区的时间戳。

**操作说明**

###### 使用说明

将一个UTC时区的时间戳转换成一个指定时区的时间戳。

**函数语法**

```
TIMESTAMP FROM_UTC_TIMESTAMP({any primitive type}*, STRING timezone);
```

**参数说明**

{any primitive type}*：时间戳，TIMESTAMP、DATETIME、TINYINT、SMALLINT、INT或 BIGINT类型。如果该参数为TINYINT、SMALLINT、INT或BIGINT类型，则单位为毫秒。 timezone：指定需要转换的目标时区，例如PST。

**返回值**

TIMESTAMP类型。

##### 使用示例

大数据计算服务 `--` 输入参数为毫秒（`ms`），返回`2017-08-01 04:24:00`。

```
SELECT FROM_UTC_TIMESTAMP(1501557840000, 'PST');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 2017-08-01 04:24:00 |
+---------------------+ SELECT FROM_UTC_TIMESTAMP(TO_DATE('1970-01-30 16:00:00', 'yyyy-mm-dd hh:mi:ss'), 'PST ');
```

`--` 返回结果

```
+-----------------------+
| _c0                   |
+-----------------------+
| 1970-01-30 08:00:00.0 |
+-----------------------+ SELECT FROM_UTC_TIMESTAMP(DATETIME '1970-01-30 00:00:00', 'PST');
```

`--` 返回结果

```
+-----------------------+
| _c0                   |
+-----------------------+
| 1970-01-29 16:00:00.0 |
+-----------------------+
```

###### CURRENT_TIMESTAMP

本文介绍如何在MaxCompute中使用日期函数CURRENT_TIMESTAMP，用于返回当前TIMESTAMP类型的时间戳。

**操作说明**

###### 使用说明

返回当前TIMESTAMP类型的时间戳，值不固定。

**函数语法**

```
TIMESTAMP CURRENT_TIMESTAMP();
```

**参数说明**

无。

**返回值**

TIMESTAMP类型。

##### 使用示例

大数据计算服务

```
SELECT CURRENT_TIMESTAMP();
```

`--` 返回结果

```
+-------------------------+
|           _c0           |
+-------------------------+
| 2017-08-03 11:50:30.661 |
+-------------------------+
```

###### ADD_MONTHS

本文介绍如何在MaxCompute中使用日期函数ADD_MONTHS，用于返回开始日期增加指定月份后的日期。

**操作说明**

###### 使用说明

**函数语法**

```
STRING ADD_MONTHS(STRING startdate, INT num_months);
```

**参数说明**

startdate：STRING类型日期值。日期格式至少包含yyyy-mm-dd的日期，否则返回NULL。

**返回值**

STRING类型日期值，格式为yyyy-mm-dd。

##### 使用示例

大数据计算服务

```
SELECT ADD_MONTHS('2017-02-14', 3);
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 2017-05-14 |
+------------+ SELECT ADD_MONTHS('17-2-14', 3);
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 0017-05-14 |
+------------+ SELECT ADD_MONTHS('2017-02-14 21:30:00', 3);
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 2017-05-14 |
+------------+ SELECT ADD_MONTHS('20170214', 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

###### LAST_DAY

本文介绍如何在MaxCompute中使用日期函数LAST_DAY，用于返回该日期所在月份的最后一天日期。

**操作说明**

###### 使用说明

返回该日期所在月份的最后一天日期。

**函数语法**

```
STRING LAST_DAY(STRING date);
```

**参数说明**

`date` ：STRING类型日期值，格式为yyyy-mm-dd hh:mi:ss或yyyy-mm-dd。

**返回值**

STRING类型日期值，格式为yyyy-mm-dd。 大数据计算服务

##### 使用示例

```
SELECT LAST_DAY('2017-03-04');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 2017-03-31 |
+------------+ SELECT LAST_DAY('2017-07-04 11:40:00');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 2017-07-31 |
+------------+ SELECT LAST_DAY('20170304');
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| NULL   |
+--------+
```

###### NEXT_DAY

本文介绍如何在MaxCompute中使用日期函数NEXT_DAY，用于返回大于指定日期并且与week相匹配的第一个日期，即下周几的具体日期。

**操作说明**

###### 使用说明

返回大于指定日期startdate并且与week相匹配的第一个日期，即下周几的具体日期。

**函数语法**

```
STRING NEXT_DAY(STRING startdate, STRING week);
```

**参数说明**

startdate：STRING类型日期值，格式为yyyy-mm-dd hh:mi:ss或yyyy-mm-dd。 week：STRING类型日期值。一个星期前2个或3个字母，或者一个星期的全名，例如MO、TUE或 FRIDAY。

**返回值**

STRING类型日期值，格式为yyyy-mm-dd。

##### 使用示例

大数据计算服务

```
SELECT NEXT_DAY('2017-08-01','TU');
```

`--` 返回结果

```
+------------+
|    _c0     |
+------------+
| 2017-08-08 |
+------------+ SELECT NEXT_DAY('2017-08-01 23:34:00','TU');
```

`--` 返回结果

```
+------------+
|    _c0     |
+------------+
| 2017-08-08 |
+------------+ SELECT NEXT_DAY('20170801','TU');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| NULL       |
+------------+
```

###### MONTHS_BETWEEN

本文介绍如何在MaxCompute中使用MONTHS_BETWEEN，用于返回日期date1和date2之间的月数。

**操作说明**

###### 使用说明

返回日期date1和date2之间的月数。

**函数语法**

```
DOUBLE MONTHS_BETWEEN(DATETIME/TIMESTAMP/STRING date1, DATETIME/TIMESTAMP/STRING date 2);
```

**参数说明**

date1：DATETIME、TIMESTAMP或STRING类型。格式为 `yyyy-mm-dd hh:mi:ss` 或 `yyyy-mm-` `dd` 。 date2：DATETIME、TIMESTAMP或STRING类型。格式为 `yyyy-mm-dd hh:mi:ss` 或 `yyyy-mm-` `dd` 。

**返回值**

DOUBLE类型。 当date1晚于date2时，返回值为正。当date2晚于date1时，返回值为负。 当date1和date2分别对应两个月的最后一天，返回整数月，否则计算方式为date1减去date2的天数除以31天。 大数据计算服务

##### 使用示例

```
SELECT MONTHS_BETWEEN('1997-02-28 10:30:00', '1996-10-30');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 3.9495967741935485  |
+---------------------+ SELECT MONTHS_BETWEEN('1996-10-30', '1997-02-28 10:30:00');
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| -3.9495967741935485 |
+---------------------+ SELECT MONTHS_BETWEEN('1996-09-30', '1996-12-31');
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| -3.0       |
+------------+
```

###### EXTRACT

本文介绍如何在MaxCompute中使用日期函数EXTRACT，用于提取日期中指定时间单位的部分。

**操作说明**

###### 使用说明

如果时间取值不正确，例如超过规定范围，返回值为超限数值除以对应的正确时间范围最大值后取余。

**函数语法**

```
INT EXTRACT(<datepart> FROM <timestamp>);
```

**参数说明**

`datepart` ：支持YEAR、MONTH、DAY、HOUR或MINUTE等时间描述。 `timestamp` ：TIMESTAMP类型的数据。

**返回值**

INT类型。

##### 使用示例

大数据计算服务

```
SET odps.sql.type.system.odps2=true; SELECT EXTRACT(YEAR FROM '2019-05-01 11:21:00') AS year
     , EXTRACT(MINUTE FROM '2019-05-01 11:21:00') AS minute;
```

`--` 返回结果

```
+------+-------+------+------+--------+ +------+-------+------+------+--------+
| 2019 | 5     | 1    | 11   | 21     |
+------+-------+------+------+--------+ SET odps.sql.type.system.odps2=true; SELECT EXTRACT(HOUR FROM '2019-05-01 31:01:01') AS hour
     , EXTRACT(MINUTE FROM '2019-05-01 23:61:01') AS minute;
```

`--` 返回结果

```
+------+--------+ +------+--------+
| 7    | 1      |
+------+--------+
```

`--`即`hour`的正确取值范围最大值是`24`，超限数值为`31`，`31`除以`24`后取余等于7。 `--`即`minute`的正确取值范围最大值是`60`，超限数值为`61`，`61`除以`60`后取余等于1。

#### 窗口函数

##### 概述

MaxCompute SQL中可以使用窗口函数进行灵活的分析处理工作，本文为您介绍窗口函数使用时的注意事项及语法说明。

**操作说明**

###### 使用说明

**重要**

窗口函数只能出现在SELECT子句中。 窗口函数中不能嵌套使用窗口函数和聚合函数。 窗口函数不能和同级别的聚合函数一起使用。

**函数语法**

```
window_func() OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC| DESC]…]] windowing_clause);
```

**参数说明**

PARTITION BY：指定开窗的列。分区列的值相同的行被视为在同一个窗口内。同一窗口内最多包含1 亿行数据（建议不超过500万行），否则运行时报错。 大数据计算服务 ORDER BY：指定数据在一个窗口内如何排序。 windowing_clause：可以用ROWS指定开窗方式，目前包含如下两种方式：

```
 ROWS BETWEEN x PRECEDING|FOLLOWING AND y PRECEDING|FOLLOWING ：表示窗口范围是从前
```

或后x行到前或后y行。 ROWS x PRECEDING|FOLLOWING ：表示窗口范围是从前或后第x行到当前行。

**说明**

x, y：必须为大于等于0的整数常量，限定范围0~10000，值为0时表示当前行。 必须指定ORDER BY才可以用ROWS方式指定窗口范围。 支持使用ROWS指定开窗方式的窗口函数包含AVG、COUNT、MAX、MIN、STDDEV和 SUM。

##### COUNT

**操作说明**

###### 使用说明

计算计数值。

**函数语法**

```
BIGINT COUNT([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|D ESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，任意数据类型。当值为NULL时，该行不参与计算。当指定DISTINCT关键字时，表示取唯一值的计数值。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内expr的计数值。指定ORDER BY时，返回结果以指定的顺序排序，并且值为当前窗口内从开始行到当前行的累计计数值。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

返回BIGINT类型。

##### 使用示例

`--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 不指定`ORDER BY`时，返回当前窗口内`user_id`的计数值。 大数据计算服务

```
SELECT user_id, COUNT(user_id) OVER (PARTITION BY user_id) AS count FROM test_src;
```

`--` 返回结果

```
+------------+------------+ +------------+------------+
| 1          | 4          |
| 1          | 4          |
| 1          | 4          |
| 1          | 4          |
| 2          | 2          |
| 2          | 2          |
| 3          | 2          |
| 3          | 2          |
+------------+------------+
```

`--` 指定`ORDER BY`时，返回当前窗口内从开始行到当前行的累计计数值。

```
SET odps.sql.hive.compatible=false; SELECT user_id, COUNT(user_id) OVER (PARTITION BY user_id ORDER BY user_id) AS count FROM test_src;
```

`--` 返回结果

```
+------------+------------+ +------------+------------+
```

| 1 | 1 | -- 窗口为起始点。
| 1 | 2 | -- 到当前行共计两条记录，返回2。

```
| 1          | 3          |
| 1          | 4          |
| 2          | 1          |
| 2          | 2          |
| 3          | 1          |
| 3          | 2          |
+------------+------------+ SET odps.sql.hive.compatible=false; SELECT user_id, price, COUNT(price) OVER (PARTITION BY user_id ORDER BY price) AS cou nt FROM test_src;
```

`--` 返回结果

```
+---------+-------+-------+ +---------+-------+-------+
```

| 1 | 4.5 | 1 | -- 窗口起始行。

```
| 1       | 6.5   | 4     |
| 2       | NULL  | 0     |
| 2       | 3.0   | 1     |
| 3       | NULL  | 0     |
| 3       | 4.0   | 1     |
+---------+-------+-------+
```

兼容模式：当`ORDER``BY`的值重复时返回值为相同值的最后 `Hi` 大数据计算服务 `-- Hive`兼容模式：当`ORDER BY`的值重复时，返回值为相同值的最后一行的`COUNT`。

```
SET odps.sql.hive.compatible=true; SELECT user_id, price, COUNT(price) OVER (PARTITION BY user_id ORDER BY price) AS cou nt FROM test_src;
```

`--` 返回结果

```
+---------+-------+-------+ +---------+-------+-------+
```

| 1 | 4.5 | 1 | -- 窗口起始行。
| 1 | 5.5 | 3 | -- 第2行和第3行的`price`一致，则第2行的`count`为第3行的`count`。

```
| 1       | 6.5   | 4     |
| 2       | NULL  | 0     |
| 2       | 3.0   | 1     |
| 3       | NULL  | 0     |
| 3       | 4.0   | 1     |
+---------+-------+-------+
```

##### AVG

本文介绍如何在MaxCompute中使用窗口函数AVG，用于计算平均值。

**操作说明**

###### 使用说明

计算平均值。

**函数语法**

```
DOUBLE AVG([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DES C], col2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型时，会隐式转换为 DOUBLE类型后参与运算，输入其它数据类型时报错。当值为NULL时，该行不参与计算。BOOLEAN 类型不允许参与计算。当指定DISTINCT关键字时，表示取唯一值的平均值。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内所有值的平均值。指定ORDER BY时，返回结果以指定的方式排序，并且返回窗口内从开始行到当前行的累计平均值。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 非`Hive`兼容模式：当`ORDER BY`的值重复时，返回值为各自行的`AVG`。

```
SET odps.sql.hive.compatible=false; SELECT user_id, price, AVG(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+---------------------+
| user_id | price | _c2                 |
+---------+-------+---------------------+
| 1       | 4.5   | 4.5                 | -- 窗口起始行。
| 1       | 5.5   | 5.0                 | -- 从第1行到第2行的AVG。
| 1       | 5.5   | 5.166666666666667   | -- 从第1行到第3行的AVG。
| 1       | 6.5   | 5.5                 |
| 2       | NULL  | NULL                |
| 2       | 3.0   | 3.0                 |
| 3       | NULL  | NULL                |
| 3       | 4.0   | 4.0                 |
+---------+-------+---------------------+
```

`-- Hive`兼容模式：当`ORDER BY`的值重复时，返回值为相同值的最后一行的`AVG`。

```
SET odps.sql.hive.compatible=true; SELECT user_id, price, AVG(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+---------------------+
| user_id | price | _c2                 |
+---------+-------+---------------------+
| 1       | 4.5   | 4.5                 | -- 窗口起始行。
| 1       | 5.5   | 5.166666666666667   | -- 从第1行到第3行的AVG。
| 1       | 5.5   | 5.166666666666667   | -- 从第1行到第3行的AVG。
| 1       | 6.5   | 5.5                 |
| 2       | NULL  | NULL                |
| 2       | 3.0   | 3.0                 |
| 3       | NULL  | NULL                |
| 3       | 4.0   | 4.0                 |
+---------+-------+---------------------+
```

##### MAX

本文介绍如何在MaxCompute中使用窗口函数MAX，用于计算最大值。 大数据计算服务

**操作说明**

###### 使用说明

计算最大值。

**函数语法**

```
MAX([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，除BOOLEAN外的任意类型。当值为NULL时，该行不参与计算。当指定DISTINCT关键字时，表示取唯一值的最大值（指定该参数与否对结果没有影响）。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内的最大值。指定ORDER BY时，返回结果以指定的方式排序，并且值为当前窗口内从开始行到当前行的最大值。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

返回值类型同expr类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 不指定`ORDER BY`，返回窗口内最大值。

```
SELECT user_id, price, MAX(price) OVER (PARTITION BY user_id) FROM test_src;
```

`--` 返回结果

```
+---------+-------+------+
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
+---------+-------+------+
```

`--` 指定`ORDER BY`，返回从开始行到当前行的累计最大值。

```
SELECT user_id, price, MAX(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+------+
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

本文介绍如何在MaxCompute中使用窗口函数MIN，用于计算最小值。

**操作说明**

大数据计算服务

###### 使用说明

计算最小值。

**函数语法**

```
MIN([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，除BOOLEAN外的任意类型。当值为NULL时，该行不参与计算。当指定DISTINCT关键字时，表示取唯一值的最小值（指定该参数与否对结果没有影响）。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内的最小值。指定ORDER BY时，返回结果以指定的方式排序，并且值为当前窗口内从开始行到当前行的最小值。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

返回值类型同expr类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 不指定`ORDER BY`，返回窗口内最小值。

```
SELECT user_id, price, MIN(price) OVER (PARTITION BY user_id) FROM test_src;
```

`--` 返回结果

```
+---------+-------+------+
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
+---------+-------+------+
```

`--` 指定`ORDER BY`，返回从开始行到当前行的累计最小值。

```
SELECT user_id, price, MIN(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+------+
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

**操作说明**

大数据计算服务

###### 使用说明

计算中位数。

**函数语法**

```
DOUBLE MEDIAN(DOUBLE number1, number2...) OVER (PARTITION BY [col1, col2…]); DECIMAL MEDIAN(DECIMAL number1, number2...) OVER (PARTITION BY [col1, col2…]);
```

**参数说明**

number1, number2...：必填，DOUBLE或DECIMAL类型的数字。最多支持输入255个数字，至少要输入1个数字。如果输入为DOUBLE类型，会默认转换为DOUBLE类型的数组参与计算。输入为 STRING或BIGINT类型，会隐式转换为DOUBLE类型后参与运算，输入其他数据类型时报错。当输入为NULL时，返回NULL。 PARTITION BY [col1, col2...]：指定开窗口的列。

**返回值**

返回DOUBLE或DECIMAL类型。

##### 使用示例

`--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 计算窗口内中位数。

```
SELECT user_id, price, MEDIAN(price) OVER (PARTITION BY user_id) FROM test_src;
```

`--` 返回结果

```
+---------+-------+------+
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

本文介绍如何在MaxCompute中使用窗口函数STDDEV，用于计算总体标准差。

**操作说明**

大数据计算服务

###### 使用说明

计算总体标准差。

**函数语法**

```
DOUBLE STDDEV([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC| DESC], col2 [ASC|DESC]…]] [windowing_clause]); DECIMAL STDDEV([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC
|DESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型时，会隐式转换为 DOUBLE类型后参与运算，输入其他类型时报错。当输入值为NULL时，该行不参与计算。当指定 DISTINCT关键字时，表示计算唯一值的总体标准差。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内的总体标准差。指定ORDER BY时，返回结果以指定的方式排序，并且值为当前窗口内从开始行到当前行的总体标准差。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

输入值为DECIMAL类型时，返回DECIMAL类型，否则返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0); SET odps.sql.hive.compatible=false; SELECT user_id, price, STDDEV(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src;
```

`--` 返回结果

```
+---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.0                  | -- 窗口起始行。
| 1       | 6.5   | 0.7071067811865475   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | 0.0                  |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | 0.0                  |
+---------+-------+----------------------+
```

`-- Hive`兼容模式：当`ORDER BY`的值重复时，返回值为相同值的最后一行的`STDDEV`。

```
SET odps.sql.hive.compatible=true; SELECT user_id, price, STDDEV(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src;
```

`--` 返回结果

```
+---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
| 1       | 4.5   | 0.0                  | -- 窗口起始行。
| 1       | 6.5   | 0.7071067811865475   |
| 2       | NULL  | NULL                 |
| 2       | 3.0   | 0.0                  |
| 3       | NULL  | NULL                 |
| 3       | 4.0   | 0.0                  |
+---------+-------+----------------------+
```

##### STDDEV_SAMP

本文介绍如何在MaxCompute中使用窗口函数STDDEV_SAMP，用于计算样本标准差。 大数据计算服务

**操作说明**

###### 使用说明

计算样本标准差。

**函数语法**

```
DOUBLE STDDEV_SAMP([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]] [windowing_clause]); DECIMAL STDDEV_SAMP([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型时，会隐式转换为 DOUBLE类型后参与运算，输入其他类型时报错。当输入值为NULL时，该行不参与计算。当指定 DISTINCT关键字时，表示计算唯一值的样本标准差。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内的样本标准差。指定ORDER BY时，返回结果以指定的方式排序，并且值为当前窗口内从开始行到当前行的样本标准差。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

输入值为DECIMAL类型时，返回DECIMAL类型，否则返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 不指定`ORDER BY`，返回窗口内样本标准差。

```
SELECT user_id, price, STDDEV_SAMP(price) OVER (PARTITION BY user_id) FROM test_src;
```

`--` 返回结果

```
+---------+-------+----------------------+
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
+---------+-------+----------------------+
```

`--` 指定`ORDER BY`，返回从开始行到当前行的累计样本标准差。

```
SELECT user_id, price, STDDEV_SAMP(price) OVER (PARTITION BY user_id ORDER BY price) FROM test_src;
```

`--` 返回结果

```
+---------+-------+----------------------+
| user_id | price | _c2                  |
+---------+-------+----------------------+
```

| 1 | 4.5 | 0.0 | -- 仅1行数据，无法计算样本标准差。

```
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

本文介绍如何在MaxCompute中使用窗口函数SUM，用于计算汇总值。

**操作说明**

大数据计算服务

###### 使用说明

计算汇总值。

**函数语法**

```
SUM([DISTINCT] expr) OVER (PARTITION BY [col1, col2…] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC]…]] [windowing_clause]);
```

**参数说明**

expr：必填，DOUBLE、DECIMAL或BIGINT类型。如果输入为STRING类型时，会隐式转换为 DOUBLE类型后参与运算，输入其他类型时报错。当输入值为NULL时，该行不参与计算。当指定 DISTINCT关键字时，表示计算唯一值的汇总值。 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：不指定ORDER BY时，返回当前窗口内expr的汇总值。指定ORDER BY时，返回结果以指定的方式排序，并且值为当前窗口内从开始行到当前行的累计汇总值。当指定DISTINCT关键字时，不能使用ORDER BY。

**返回值**

输入值为BIGINT类型时，返回BIGINT类型。 输入值为DECIMAL类型时，返回DECIMAL类型。 输入值为DOUBLE或STRING类型时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 创建测试表并插入数据。

```
CREATE TABLE test_src (user_id BIGINT, price DOUBLE); INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 非`Hive`兼容模式：当`ORDER BY`的值重复时，返回值为各自行的`SUM`。

```
SET odps.sql.hive.compatible=false; SELECT user_id, price, SUM(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
```

| 1 | 4.5 | 4.5 | -- 窗口起始行。
| 1 | 5.5 | 10.0 | -- 从第1行到第2行的`SUM`。
| 1 | 5.5 | 15.5 | -- 从第1行到第3行的`SUM`。

```
| 1       | 6.5   | 22.0 |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

`-- Hive`兼容模式：当`ORDER BY`的值重复时，返回值为相同值的最后一行的`SUM`。

```
SET odps.sql.hive.compatible=true; SELECT user_id, price, SUM(price) OVER (PARTITION BY user_id ORDER BY price) FROM tes t_src;
```

`--` 返回结果

```
+---------+-------+------+
| user_id | price | _c2  |
+---------+-------+------+
```

| 1 | 4.5 | 4.5 | -- 窗口起始行。
| 1 | 5.5 | 15.5 | -- 从第1行到第3行的`SUM`。
| 1 | 5.5 | 15.5 | -- 从第1行到第3行的`SUM`。

```
| 1       | 6.5   | 22.0 |
| 2       | NULL  | NULL |
| 2       | 3.0   | 3.0  |
| 3       | NULL  | NULL |
| 3       | 4.0   | 4.0  |
+---------+-------+------+
```

##### DENSE_RANK

本文介绍如何在MaxCompute中使用窗口函数DENSE_RANK，用于计算连续排名。 大数据计算服务

**操作说明**

###### 使用说明

计算连续排名。ORDER BY的列值相同的行数据获得的排名相同。

**函数语法**

```
BIGINT DENSE_RANK() OVER (PARTITION BY [col1, col2…] ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]…]);
```

**参数说明**

PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：指定排名依据的值。

**返回值**

返回BIGINT类型。

##### 使用示例

`--` 创建测试表并插入数据。

```
  empno BIGINT,
  ename STRING,
  job STRING,
  mgr BIGINT,
  hiredate STRING,
  sal DOUBLE,
  comm DOUBLE,
  deptno BIGINT
); INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800, NUL L, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20 00:00:00', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250 , 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500 , 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23 00:00:00', 1100, NU LL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950, NUL L, 30);
```

大数据计算服务

```
INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000, N ULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300, N ULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, '1981-04-12 00:00:00', 5000, N ULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, '1982-07-20 00:00:00', 2450, NU LL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, '1982-12-30 00:00:00', 1300, N ULL, 10);
```

`--` 将所有职工根据部门分组，组内根据`sal`降序排序，获取组内连续排名序号。 `-- deptno`（部门）作为开窗列，`sal`（薪水）作为排名依据。

```
SELECT deptno, ename, sal, DENSE_RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS nums FROM emp;
```

`--` 返回结果

```
+--------+--------+---------+------+
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

本文介绍如何在MaxCompute中使用窗口函数RANK，用于计算排名。

**操作说明**

###### 使用说明

计算排名。ORDER BY的列值相同的行数据获得排名顺序下降。

**函数语法**

```
BIGINT RANK() OVER (PARTITION BY [col1, col2…] ORDER BY [col1 [ASC|DESC], col2 [ASC|D ESC]…]);
```

**参数说明**

大数据计算服务 PARTITION BY [col1, col2...]：指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC]]：指定排名依据的值。

**返回值**

返回BIGINT类型。

##### 使用示例

`--` 创建测试表并插入数据。

```
  empno BIGINT,
  ename STRING,
  job STRING,
  mgr BIGINT,
  hiredate STRING,
  sal DOUBLE,
  comm DOUBLE,
  deptno BIGINT
); INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800, NUL L, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20 00:00:00', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250 , 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500 , 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23 00:00:00', 1100, NU LL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950, NUL L, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000, N ULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300, N ULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, '1981-04-12 00:00:00', 5000, N ULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, '1982-07-20 00:00:00', 2450, NU LL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, '1982-12-30 00:00:00', 1300, N ULL, 10);
```

大数据计算服务 `--` 将所有职工根据部门分组，组内根据`sal`降序排序，获取组内排名序号。 `-- deptno`（部门）作为开窗列，`sal`（薪水）作为排名依据。

```
SELECT deptno, ename, sal, RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS num s FROM emp;
```

`--` 返回结果

```
+--------+--------+---------+------+
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

本文介绍如何在MaxCompute中使用窗口函数LAG，用于按偏移量取当前行之前指定行的值。

**操作说明**

###### 使用说明

按偏移量取当前行之前第几行的值。如当前行号为rn，则取行号为rn-offset的值。

**函数语法**

```
LAG(expr, BIGINT offset, default) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col 1 [ASC|DESC], col2 [ASC|DESC], ...]]);
```

**参数说明**

expr：必填，任意数据类型。 offset：必填，BIGINT类型常量，取值大于0。输入值为STRING或DOUBLE类型则隐式转换为 BIGINT类型。 default：选填，常量。当offset指定的范围越界时的缺省值，默认值为NULL。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填，指定返回结果的排序方式。

**返回值**

返回值类型同expr类型。 大数据计算服务

##### 使用示例

`--` 建表

```
    window STRING,
    seq BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO sliding_window VALUES ('all', 0); INSERT INTO sliding_window VALUES ('all', 1); INSERT INTO sliding_window VALUES ('all', 2); INSERT INTO sliding_window VALUES ('all', 3); INSERT INTO sliding_window VALUES ('all', 4); INSERT INTO sliding_window VALUES ('all', 5); INSERT INTO sliding_window VALUES ('all', 6); INSERT INTO sliding_window VALUES ('all', 7); INSERT INTO sliding_window VALUES ('all', 8); INSERT INTO sliding_window VALUES ('all', 9);
```

`--` 按偏移量取前一行的`seq+100`的值

```
SELECT seq, LAG(seq + 100, 1) OVER (PARTITION BY window ORDER BY seq) AS r FROM slidi ng_window;
```

`--` 返回结果

```
+-----+------+
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

本文介绍如何在MaxCompute中使用窗口函数LEAD，用于返回当前行往后指定偏移行对应的表达式值。

**操作说明**

###### 使用说明

返回当前行往后（朝分区尾部方向）第offset行数据对应的表达式expr的值。表达式expr可以是列、列运算或函数运算等。

**函数语法**

```
LEAD(expr, BIGINT offset, default) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [co l1 [ASC|DESC], col2 [ASC|DESC], ...]]);
```

大数据计算服务

**参数说明**

expr：必填，任意类型。 offset：必填，BIGINT类型常量，取值大于0。输入值为STRING或DOUBLE类型，会隐式转换为 BIGINT类型。 default：选填，常量。当offset指定的范围越界时的缺省值，默认值为NULL。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填，指定返回结果的排序方式。

**返回值**

返回值类型同expr类型。

##### 使用示例

`--` 建表

```
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00',
```

大数据计算服务

```
1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

`--` 将所有职工根据部门分组，每位员工的薪水做偏移

```
SELECT deptno, ename, sal, LEAD(sal, 1) OVER (PARTITION BY deptno ORDER BY sal) AS sa l_new FROM emp;
```

`--` 返回结果

```
+--------+--------+------+---------+
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

本文介绍如何在MaxCompute中使用窗口函数PERCENT_RANK，用于计算一组数据中某行的相对排名。

**操作说明**

###### 使用说明

计算一组数据中某行的相对排名。

**函数语法**

```
PERCENT_RANK() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [ ASC|DESC], ...]);
```

**参数说明**

PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：必填，指定排名依据的值。

**返回值**

大数据计算服务返回值为DOUBLE类型，值域为 `[0,1]` 。

**说明**

单个窗口内的行数不超过1000万条。 `rank` 为该行数据的RANK窗口函数的返回结果， `partition_row_count` 为该行数据所属分区的数据行数。当分区中只有一行数据时，输出结果为0.0。

##### 使用示例

`--` 建表

```
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00',
```

大数据计算服务

```
5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

`--` 计算各部门内员工薪水的相对排名

```
SELECT deptno, ename, sal, PERCENT_RANK() OVER (PARTITION BY deptno ORDER BY sal) AS pct_rank FROM emp;
```

`--` 返回结果

```
+--------+--------+------+---------------------+
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

本文介绍如何在MaxCompute中使用窗口函数ROW_NUMBER，用于计算行号。

**操作说明**

###### 使用说明

计算行号，从1开始。

**函数语法**

```
ROW_NUMBER() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [AS C|DESC], ...]);
```

**参数说明**

PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填，指定结果返回时需要排序的值。

**返回值**

返回BIGINT类型。 大数据计算服务

##### 使用示例

`--` 建表

```
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

`--` 将所有职工根据部门分组，每个组内根据`sal`做降序排序，获得职工自己组内的序号

```
SELECT deptno, ename, sal, ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal DESC) AS nums FROM emp;
```

返回结果大数据计算服务 `--` 返回结果

```
+--------+--------+--------+------+
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

本文介绍如何在MaxCompute中使用窗口函数CLUSTER_SAMPLE，用于分组抽样。

**操作说明**

###### 使用说明

分组抽样。

**函数语法**

```
BOOLEAN CLUSTER_SAMPLE([BIGINT x, BIGINT y]) OVER (PARTITION BY [col1, col2, ...]);
```

**参数说明**

x：必填，BIGINT类型常量，x>=1。如果指定参数y，x表示将一个窗口分为x份；否则，x表示在一个窗口中抽取x行记录（即有x行返回值为True）。x为NULL时，返回值为NULL。 y：选填，BIGINT类型常量，y>=1且y<=x。表示从一个窗口分的x份中抽取y份记录（即y份记录返回值为True）。y为NULL时，返回值为NULL。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。

**返回值**

返回BOOLEAN类型。

##### 使用示例

大数据计算服务
    - 建表

```
    key STRING,
    value DOUBLE
);
```

`--` 插入测试数据

```
INSERT INTO test_tbl VALUES ('groupa', -1.34764165478145); INSERT INTO test_tbl VALUES ('groupa', 0.740212609046718); INSERT INTO test_tbl VALUES ('groupa', 0.167537127858695); INSERT INTO test_tbl VALUES ('groupa', 0.630314566185241); INSERT INTO test_tbl VALUES ('groupa', 0.0112401388646925); INSERT INTO test_tbl VALUES ('groupa', 0.199165745875297); INSERT INTO test_tbl VALUES ('groupa', -0.320543343353587); INSERT INTO test_tbl VALUES ('groupa', -0.273930924365012); INSERT INTO test_tbl VALUES ('groupa', 0.386177958942063); INSERT INTO test_tbl VALUES ('groupa', -1.09209976687047); INSERT INTO test_tbl VALUES ('groupb', -1.10847690938643); INSERT INTO test_tbl VALUES ('groupb', -0.725703978381499); INSERT INTO test_tbl VALUES ('groupb', 1.05064697475759); INSERT INTO test_tbl VALUES ('groupb', 0.135751224393789); INSERT INTO test_tbl VALUES ('groupb', 2.13313102040396); INSERT INTO test_tbl VALUES ('groupb', -1.11828960785008); INSERT INTO test_tbl VALUES ('groupb', -0.849235511508911); INSERT INTO test_tbl VALUES ('groupb', 1.27913806620453); INSERT INTO test_tbl VALUES ('groupb', -0.330817716670401); INSERT INTO test_tbl VALUES ('groupb', -0.300156896191195); INSERT INTO test_tbl VALUES ('groupb', 2.4704244205196); INSERT INTO test_tbl VALUES ('groupb', -1.28051882084434);
```

`--` 从每组中抽取约10%的值

```
SELECT key, value FROM (SELECT key, value, CLUSTER_SAMPLE(10, 1) OVER (PARTITION BY k ey) AS flag FROM test_tbl) sub WHERE flag = true;
```

`--` 返回结果（抽样结果具有随机性，以下为参考结果）

```
+--------+---------------------+ +--------+---------------------+
| groupa | -0.273930924365012  |
| groupb | -1.11828960785008   |
```

##### NTILE

**操作说明**

###### 使用说明

将分组数据按照顺序切分成n片，并返回当前切片值。如果切片不均匀，默认增加第一个切片的分布。

**函数语法**

大数据计算服务

```
BIGINT NTILE(BIGINT n) OVER(PARTITION BY [col1, col2…] [ORDER BY [col1[ASC|DESC], col2[ASC|DESC]…]] [windowing_clause]));
```

**参数说明**

n：BIGINT数据类型。

**返回值**

BIGINT类型。

##### 使用示例

**准备示例数据**

```
    empno    BIGINT    COMMENT '员工编号',
    ename    STRING    COMMENT '员工姓名',
    job      STRING    COMMENT '职位',
```

`mgr BIGINT COMMENT '`上级经理编号`',`

```
    hiredate DATETIME  COMMENT '入职日期',
    sal      DOUBLE    COMMENT '薪资',
    comm     DOUBLE    COMMENT '佣金',
    deptno   BIGINT    COMMENT '部门编号'
```

`) COMMENT '`员工信息表';

```
(7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20), (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00', 1600, 300, 30), (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00', 1250, 500, 30), (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00', 2975, NULL, 20), (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:00', 1250, 1400, 30), (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00', 2850, NULL, 30), (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00', 2450, NULL, 10), (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00', 3000, NULL, 20), (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00', 5000, NULL, 10), (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:00', 1500, 0, 30), (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20), (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30), (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20), (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10), (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10), (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10), (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

大数据计算服务

**使用函数查询结果**

现在需要将所有职工根据部门按**sal**由高到低切分为3组，并获得职工自己组内的序号。

```
SELECT deptno,ename,sal,NTILE(3) OVER(PARTITION BY deptno ORDER BY sal DESC) AS nt 3 FROM emp;
```

`--` 返回结果

```
+------------+--------+------------+------------+
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

本文介绍如何在MaxCompute中使用窗口函数NTH_VALUE，用于计算窗口中的第n个值。

**操作说明**

###### 使用说明

计算窗口中的第n个值。如果n超过窗口的最大长度，返回NULL。

**函数语法**

```
NTH_VALUE(expr, number [, skipNull]) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [ col1 [ASC|DESC], col2 [ASC|DESC], ...]] [windowing_clause]);
```

**参数说明**

expr：必填，任意基础数据类型。 number：必填，大于等于1的整数。 skipNull：选填，BOOLEAN类型。计算第n个值时是否忽略NULL值的行，默认为False。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填。不指定ORDER BY时，返回当前窗口第n行的expr值。指定ORDER BY时，返回结果以指定的顺序排序，并且值为当前窗口从开始行到当前行的第n行的expr值。

**返回值**

大数据计算服务返回值类型同expr类型。

##### 使用示例

`--` 建表

```
    user_id BIGINT,
    price DOUBLE
);
```

`--` 插入测试数据

```
INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 示例1：没有指定`ORDER BY`时，当前窗口为第一行到最后一行的范围，返回第2行的值

```
SELECT user_id, price, NTH_VALUE(price, 2) OVER (PARTITION BY user_id) AS nth_value F ROM test_src;
```

`--` 返回结果

```
+------------+------------+------------+ +------------+------------+------------+
| 1          | 4.5        | 6.5        |
```

| 1 | 6.5 | 6.5 | -- 当前窗口的第2行。

```
| 1          | 5.5        | 6.5        |
| 1          | 5.5        | 6.5        |
| 2          | NULL       | 3.0        |
```

| 2 | 3.0 | 3.0 | -- 当前窗口的第2行。

```
| 3          | NULL       | 4.0        |
```

| 3 | 4.0 | 4.0 | -- 当前窗口的第2行。

```
+------------+------------+------------+
```

`--` 示例2：没有指定`ORDER BY`时，当前窗口为第一行到最后一行的范围，返回第3行的值 `--` 注意第2个窗口和第3个窗口的长度只有2

```
SELECT user_id, price, NTH_VALUE(price, 3) OVER (PARTITION BY user_id) AS nth_value F ROM test_src;
```

`--` 返回结果

```
+------------+------------+------------+ +------------+------------+------------+
| 1          | 4.5        | 5.5        |
| 1          | 6.5        | 5.5        |
```

| 1 | 5.5 | 5.5 | -- 当前窗口的第3行。

```
| 1          | 5.5        | 5.5        |
| 2          | NULL       | NULL       |
| 2          | 3.0        | NULL       |
| 3          | NULL       | NULL       |
| 3          | 4.0        | NULL       |
```

大数据计算服务

```
+------------+------------+------------+
```

`--` 示例3：指定`ORDER BY`时，当前窗口为第一行到当前行的范围，返回第2行的值

```
SELECT user_id, price, NTH_VALUE(price, 2) OVER (PARTITION BY user_id ORDER BY price) AS nth_value FROM test_src;
```

`--` 返回结果

```
+---------+-------+-----------+ +---------+-------+-----------+
```

| 1 | 4.5 | NULL | -- 当前窗口只有1行，第2行超过了窗口长度。

```
| 1       | 5.5   | 5.5       |
| 1       | 5.5   | 5.5       |
| 1       | 6.5   | 5.5       |
| 2       | NULL  | NULL      |
| 2       | 3.0   | 3.0       |
| 3       | NULL  | NULL      |
| 3       | 4.0   | 4.0       |
+---------+-------+-----------+
```

`--` 示例4：没有指定`ORDER BY`时，当前窗口为第一行到最后一行的范围 `--` 返回第1行的值，`skipNull`设置为`True`

```
SELECT user_id, price, NTH_VALUE(price, 1, true) OVER (PARTITION BY user_id) AS nth_v alue FROM test_src;
```

`--` 返回结果

```
+------------+------------+------------+ +------------+------------+------------+
| 1          | 4.5        | 4.5        |
| 1          | 6.5        | 4.5        |
| 1          | 5.5        | 4.5        |
| 1          | 5.5        | 4.5        |
| 2          | NULL       | 3.0        | -- 第1行为NULL，被跳过。
| 2          | 3.0        | 3.0        |
| 3          | NULL       | 4.0        |
| 3          | 4.0        | 4.0        |
+------------+------------+------------+
```

##### CUME_DIST

本文介绍如何在MaxCompute中使用窗口函数CUME_DIST，用于计算累计分布。

**操作说明**

###### 使用说明

求累计分布，相当于求分组中值大于等于当前值的行数占分组总行数的比例。比较大小的值由ORDER BY 列指定。

**函数语法**

```
CUME_DIST() OVER (PARTITION BY [col1, col2, ...] ORDER BY [col1 [ASC|DESC], col2 [ASC
|DESC], ...]);
```

**参数说明**

大数据计算服务 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：必填，指定排序依据的值。

**返回值**

返回DOUBLE类型，值为分组中值大于等于当前值的行数占分组总行数的比例。

##### 使用示例

`--` 建表

```
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal BIGINT,
    comm BIGINT,
    deptno BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME'1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME'1981-02-20 00:00:00 ', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME'1981-02-22 00:00:00' , 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME'1981-04-02 00:00:00' , 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME'1981-09-28 00:00:0 0', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME'1981-05-01 00:00:00' , 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME'1981-06-09 00:00:00' , 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME'1987-04-19 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME'1981-11-17 00:00:00 ', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME'1981-09-08 00:00:0 0', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME'1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME'1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME'1981-12-03 00:00:00', 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME'1982-01-23 00:00:00', 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME'1981-04-12 00:00:00', 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME'1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME'1982-12-30 00:00:00', 1300, NULL, 10);
```

大数据计算服务

```
300,
```

U ,

```
0);
```

`--` 将所有职工根据部门分组，求`sal`在同一组内的前百分之几

```
SELECT deptno, ename, sal, CONCAT(ROUND(CUME_DIST() OVER (PARTITION BY deptno ORDER B Y sal DESC) * 100, 2), '%') AS cume_dist FROM emp;
```

`--` 返回结果

```
+--------+--------+--------+-----------+ +--------+--------+--------+-----------+
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

本文介绍如何在MaxCompute中使用窗口函数FIRST_VALUE，用于取分组内排序后截止到当前行的第一个值。

**操作说明**

###### 使用说明

取分组内排序后，截止到当前行，第一个值。

**函数语法**

```
FIRST_VALUE(expr) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col1 [ASC|DESC], co l2 [ASC|DESC], ...]] [windowing_clause]);
```

**参数说明**

expr：必填，任意基础数据类型。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填。不指定ORDER BY时，返回当前窗口内开始行的expr值。指定ORDER BY时，返回结果以指定的顺序排序，并且值为当前窗口开始行的 expr值。

**返回值**

返回值类型同expr类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    user_id BIGINT,
    price DOUBLE
);
```

`--` 插入测试数据

```
INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 示例1：没有指定`ORDER BY`时，当前窗口为第一行到最后一行的范围，返回当前窗口的开始行的值

```
SELECT user_id, price, FIRST_VALUE(price) OVER (PARTITION BY user_id) AS first_value FROM test_src;
```

`--` 返回结果

```
+---------+-------+-------------+ +---------+-------+-------------+
```

| 1 | 5.5 | 5.5 | --当前窗口的开始行。

```
| 1       | 4.5   | 5.5         |
| 1       | 6.5   | 5.5         |
| 1       | 5.5   | 5.5         |
```

| 2 | NULL | NULL | --当前窗口的开始行。

```
| 2       | 3.0   | NULL        |
```

| 3 | 4.0 | 4.0 | --当前窗口的开始行。

```
| 3       | NULL  | 4.0         |
+---------+-------+-------------+
```

`--` 示例2：指定`ORDER BY`时，当前窗口为第一行到当前行的范围，返回当前窗口的开始行的值

```
SELECT user_id, price, FIRST_VALUE(price) OVER (PARTITION BY user_id ORDER BY price) AS first_value FROM test_src;
```

`--` 返回结果

```
+---------+-------+-------------+ +---------+-------+-------------+
```

| 1 | 4.5 | 4.5 | --当前窗口的开始行。

```
| 1       | 5.5   | 4.5         |
| 1       | 5.5   | 4.5         |
| 1       | 6.5   | 4.5         |
```

| 2 | NULL | NULL | --当前窗口的开始行。

```
| 2       | 3.0   | NULL        |
```

| 3 | NULL | NULL | --当前窗口的开始行。

```
| 3       | 4.0   | NULL        |
+---------+-------+-------------+
```

大数据计算服务

##### LAST_VALUE

本文介绍如何在MaxCompute中使用窗口函数LAST_VALUE，用于取分组内排序后截止到当前行的最后一个值。

**操作说明**

###### 使用说明

取分组内排序后，截止到当前行，最后一个值。

**函数语法**

```
LAST_VALUE(expr) OVER (PARTITION BY [col1, col2, ...] [ORDER BY [col1 [ASC|DESC], col 2 [ASC|DESC], ...]] [windowing_clause]);
```

**参数说明**

expr：必填，任意基础数据类型。 PARTITION BY [col1, col2, ...]：选填，指定开窗口的列。 ORDER BY [col1 [ASC|DESC], col2 [ASC|DESC], ...]：选填。不指定ORDER BY时，返回当前窗口最后一行的expr值。指定ORDER BY时，返回结果以指定的顺序排序，并且值为当前窗口当前行的 expr值。

**返回值**

返回值类型同expr类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    user_id BIGINT,
    price DOUBLE
);
```

`--` 插入测试数据

```
INSERT INTO test_src VALUES (1, 4.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 5.5); INSERT INTO test_src VALUES (1, 6.5); INSERT INTO test_src VALUES (2, NULL); INSERT INTO test_src VALUES (2, 3.0); INSERT INTO test_src VALUES (3, NULL); INSERT INTO test_src VALUES (3, 4.0);
```

`--` 示例1：没有指定`ORDER BY`时，当前窗口为第一行到最后一行的范围，返回当前窗口的最后一行的值

```
SELECT user_id, price, LAST_VALUE(price) OVER (PARTITION BY user_id) AS last_value FR OM test_src;
```

`--` 返回结果

```
+---------+-------+------------+ +---------+-------+------------+
| 1       | 5.5   | 5.5        |
| 1       | 4.5   | 5.5        |
| 1       | 6.5   | 5.5        |
```

| 1 | 5.5 | 5.5 | -- 当前窗口的最后一行。

```
| 2       | NULL  | 3.0        |
```

| 2 | 3.0 | 3.0 | -- 当前窗口的最后一行。

```
| 3       | NULL  | 4.0        |
```

| 3 | 4.0 | 4.0 | -- 当前窗口的最后一行。

```
+---------+-------+------------+
```

`--` 示例2：指定`ORDER BY`时，当前窗口为第一行到当前行的范围，返回当前窗口的当前行的值

```
SELECT user_id, price, LAST_VALUE(price) OVER (PARTITION BY user_id ORDER BY price) A S last_value FROM test_src;
```

`--` 返回结果

```
+---------+-------+------------+ +---------+-------+------------+
```

| 1 | 4.5 | 4.5 | -- 当前窗口的当前行。
| 1 | 5.5 | 5.5 | -- 当前窗口的当前行。
| 1 | 5.5 | 5.5 | -- 当前窗口的当前行。
| 1 | 6.5 | 6.5 | -- 当前窗口的当前行。
| 2 | NULL | NULL | -- 当前窗口的当前行。
| 2 | 3.0 | 3.0 | -- 当前窗口的当前行。
| 3 | NULL | NULL | -- 当前窗口的当前行。
| 3 | 4.0 | 4.0 | -- 当前窗口的当前行。

```
+---------+-------+------------+
```

大数据计算服务

#### 聚合函数

##### 聚合函数过滤条件表达式

本文介绍如何在MaxCompute中使用聚合函数过滤条件表达式，用于在聚合函数中指定过滤条件。

**操作说明**

###### 使用说明

聚合函数都可以增加过滤条件表达式。如果指定了FILTER，则只有where_condition值为TRUE的行，才会传给对应的聚合函数处理。

**说明**

目前只有内置聚合函数支持FILTER (WHERE where_condition)，自定义聚合函数UDAF暂不支持。 COUNT(*)不能与FILTER (WHERE where_condition)联用，如有需要，请使用COUNT_IF 函数。

**函数语法**

```
aggregate_name(expression [, ...]) [FILTER (WHERE where_condition)];
```

**参数说明**

aggregate_name：聚合函数名称。 expression：聚合函数的表达式参数。 FILTER (WHERE where_condition)：选填，过滤条件表达式，只有where_condition值为TRUE的行才会参与聚合计算。

**返回值**

返回值类型取决于所使用的聚合函数。

##### 使用示例

```
    SUM(x),
    SUM(x) FILTER (WHERE y > 1),
    SUM(x) FILTER (WHERE y > 2)
FROM VALUES (NULL, 1), (1, 2), (2, 3), (3, NULL) AS t(x, y);
```

`--` 返回结果

```
+-----+-----+-----+
| _c0 | _c1 | _c2 |
+-----+-----+-----+
| 6   | 3   | 2   |
+-----+-----+-----+
```

##### COUNT

本文介绍如何在MaxCompute中使用COUNT函数计算记录数，并提供参考示例。

**操作说明**

大数据计算服务

**操作说明**

###### 使用说明

计算记录数。

**函数语法**

```
BIGINT COUNT([DISTINCT|ALL] value);
```

**参数说明**

distinct|all：指明在计数时是否去除重复记录，默认是**all**，即计算全部记录。如果指定**distinct**，则可以只计算去重后的值数量。 value：可以为任意数据类型，当**value**为NULL时，该行不参与计算。**value**可以为*，即

**返回值**

BIGINT类型。

##### 使用示例

示例1：简单计数

```
    col1 BIGINT
); (1), (2), (NULL); SELECT COUNT(*) FROM tbla;
```

`--` 返回结果

```
+--------+
|   _c0  |
+--------+
|    3   |
+--------+ SELECT COUNT(col1) FROM tbla;
```

`--` 返回结果

```
+--------+
|   _c0  |
+--------+
|    2   |
+--------+
```

大数据计算服务示例2：聚合计数聚合函数可以和GROUP BY一同使用。

```
    key   STRING COMMENT '键',
    value DOUBLE COMMENT '值'
); ('a', 2.0), ('a', 4.0), ('b', 1.0), ('b', 3.0); SELECT key, COUNT(value) AS count FROM test_src GROUP BY key;
```

`--` 返回结果

```
+-----+-------+ +-----+-------+
| a   | 2     |
+-----+-------+
| b   | 2     |
+-----+-------+
```

##### COUNT_IF

本文介绍如何在MaxCompute中使用聚合函数COUNT_IF，用于计算expr值为TRUE的记录数。

**操作说明**

###### 使用说明

用于计算expr值为TRUE的记录数。

**函数语法**

```
BIGINT COUNT_IF(BOOLEAN expr);
```

**参数说明**

expr：必填，BOOLEAN类型。当expr值为FALSE或NULL时，该行不参与计算。

**返回值**

返回BIGINT类型。

##### 使用示例

```
SELECT COUNT_IF(x > 1), COUNT_IF(x <= 1) FROM VALUES (NULL), (0), (1), (2) AS t(x);
```

`--` 返回结果

```
+-----+-----+
| _c0 | _c1 |
+-----+-----+
| 1   | 2   |
+-----+-----+
```

大数据计算服务

##### AVG

本文介绍如何在MaxCompute中使用聚合函数AVG，用于计算平均值。

**操作说明**

###### 使用说明

计算平均值。

**函数语法**

```
DOUBLE AVG(DOUBLE value); DECIMAL AVG(DECIMAL value);
```

**参数说明**

value：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为DOUBLE 类型后参与运算，输入其他类型时会发生报错。当value为NULL时，该行不参与计算。BOOLEAN类型不允许参与计算。

**返回值**

如果输入DECIMAL类型，则返回DECIMAL类型。 输入其他合法的类型时，返回DOUBLE类型。

##### 使用示例

`--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (NULL);
```

`--` 计算`value`列的平均值，即`(1+2)/2=1.5`

```
SELECT AVG(value) AS avg FROM tbla;
```

`--` 返回结果

```
+------+
| avg  |
+------+
| 1.5  |
+------+
```

##### MAX

本文介绍如何在MaxCompute中使用聚合函数MAX，用于计算最大值。

**操作说明**

###### 使用说明

计算最大值。

**函数语法**

大数据计算服务

```
MAX(value);
```

**参数说明**

value：必填，可以为任意数据类型。当列中的值为NULL时，该行不参与计算。BOOLEAN类型不允许参与运算。

**返回值**

返回值类型与value类型相同。

##### 使用示例

`--` 建表

```
    col1 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2);
```

`--` 计算`col1`列的最大值

```
SELECT MAX(col1) FROM tbla;
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

##### MIN

本文介绍如何在MaxCompute中使用聚合函数MIN，用于计算最小值。

**操作说明**

###### 使用说明

计算最小值。

**函数语法**

```
MIN(value);
```

**参数说明**

value：必填，可以为任意数据类型。当列中的值为NULL时，该行不参与计算。BOOLEAN类型不允许参与运算。

**返回值**

返回值类型与value类型相同。

##### 使用示例

大数据计算服务 `--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2);
```

`--` 计算`value`列的最小值

```
SELECT MIN(value) FROM tbla;
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+
```

##### MEDIAN

**操作说明**

###### 使用说明

计算中位数。

**函数语法**

```
DOUBLE MEDIAN(DOUBLE number); DECIMAL MEDIAN(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。输入其他类型时会发生报错。

**返回值**

如果输入DECIMAL类型，则返回DECIMAL类型。 输入其他合法的类型时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5);
```

`--` 计算`value`列的中位数

```
SELECT MEDIAN(value) FROM tbla;
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### STDDEV

本文介绍如何在MaxCompute中使用聚合函数STDDEV，用于计算总体标准差。

**操作说明**

###### 使用说明

计算总体标准差。

**函数语法**

```
DOUBLE STDDEV(DOUBLE number); DECIMAL STDDEV(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。输入其他类型时会发生报错。

**返回值**

如果输入DECIMAL类型，则返回DECIMAL类型。 输入其他合法的类型时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5);
```

`--` 计算`value`列的总体标准差

```
SELECT STDDEV(value) FROM tbla;
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 1.4142135623730951  |
+---------------------+
```

##### STDDEV_SAMP

本文介绍如何在MaxCompute中使用聚合函数STDDEV_SAMP，用于计算样本标准差。

**操作说明**

###### 使用说明

计算样本标准差。

**函数语法**

```
DOUBLE STDDEV_SAMP(DOUBLE number); DECIMAL STDDEV_SAMP(DECIMAL number);
```

**参数说明**

number：必填，DOUBLE或DECIMAL类型。如果输入为STRING或BIGINT类型，会隐式转换为 DOUBLE类型后参与运算。输入其他类型时会发生报错。

**返回值**

如果输入DECIMAL类型，则返回DECIMAL类型。 输入其他合法的类型时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (3); INSERT INTO tbla VALUES (4); INSERT INTO tbla VALUES (5);
```

`--` 计算`value`列的样本标准差

```
SELECT STDDEV_SAMP(value) FROM tbla;
```

`--` 返回结果

```
+----------------------+
| _c0                  |
+----------------------+
|  1.5811388300841898  |
+----------------------+
```

##### SUM

本文介绍如何在MaxCompute中使用聚合函数SUM，用于计算汇总值。

**操作说明**

###### 使用说明

计算汇总值。

**函数语法**

```
SUM(value);
```

**参数说明**

value：必填，DOUBLE、DECIMAL或BIGINT类型。如果输入为STRING类型会隐式转换为DOUBLE类型后参与运算，当列中的值为NULL时，该行不参与计算。BOOLEAN类型不允许参与计算。

**返回值**

输入BIGINT类型时，返回BIGINT类型。 输入DOUBLE或STRING类型时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    value BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1); INSERT INTO tbla VALUES (2); INSERT INTO tbla VALUES (NULL);
```

`--` 计算`value`列的汇总值

```
SELECT SUM(value) FROM tbla;
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3    |
+------+
```

##### WM_CONCAT

本文介绍如何在MaxCompute中使用聚合函数WM_CONCAT，用于用指定分隔符连接值。

**操作说明**

###### 使用说明

用指定的separator做分隔符，连接str中的值。

**函数语法**

```
STRING WM_CONCAT(STRING separator, STRING str);
```

**参数说明**

separator：必填，STRING类型常量，分隔符。其他类型或非常量会报错。 str：必填，STRING类型。如果输入为BIGINT、DOUBLE或DATETIME类型，会隐式转换为STRING 类型后参与运算。输入其他类型时会发生报错。

**返回值**

返回STRING类型。

**说明**

语句 SELECT WM_CONCAT(',', name) FROM test_src; 中，如果test_src为空集合，此条语句返回NULL值。

##### 使用示例

大数据计算服务 `--` 建表

```
    id INT,
    alphabet STRING
);
```

`--` 插入测试数据

```
INSERT INTO test VALUES (1, 'a'), (1, 'b'), (1, 'c'), (2, 'D'), (2, 'E'), (2, 'F');
```

`--` 按照`id`列进行分组排序，并将同组的内容以逗号分隔进行合并

```
SELECT id, WM_CONCAT(',', alphabet) FROM test GROUP BY id ORDER BY id LIMIT 100;
```

`--` 返回结果

```
+----+-------+
| id | _c1   |
+----+-------+
| 1  | a,b,c |
| 2  | D,E,F |
+----+-------+
```

##### PERCENTILE

本文介绍如何在MaxCompute中使用聚合函数PERCENTILE，用于返回指定列精确的第p位百分数。

**操作说明**

###### 使用说明

返回指定列精确的第p位百分数，p必须在0和1之间。只有整数值才能计算出真正的百分位数。

**函数语法**

```
DOUBLE PERCENTILE(BIGINT col, DOUBLE p); ARRAY<DOUBLE> PERCENTILE(BIGINT col, ARRAY(DOUBLE p1 [, DOUBLE p2, ...]));
```

**参数说明**

col：必填，BIGINT类型的列名称。 p：必填，需要精确的百分位数，DOUBLE类型，取值必须在0和1之间。

**返回值**

当p为单个DOUBLE值时，返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO var_test VALUES (8); INSERT INTO var_test VALUES (9); INSERT INTO var_test VALUES (10); INSERT INTO var_test VALUES (11);
```

`--` 示例1：求`c1`列的第p位百分数（单个p值）

```
SELECT PERCENTILE(c1, 0), PERCENTILE(c1, 0.3), PERCENTILE(c1, 0.5), PERCENTILE(c1, 1) FROM var_test;
```

`--` 返回结果

```
+------+------+------+------+
| _c0  | _c1  | _c2  | _c3  |
+------+------+------+------+
| 8.0  | 8.9  | 9.5  | 11.0 |
+------+------+------+------+ SELECT PERCENTILE(c1, ARRAY(0, 0.3, 0.5, 1)) FROM var_test;
```

`--` 返回结果

```
+-------------------+
| _c0               |
+-------------------+
| [8, 8.9, 9.5, 11] |
+-------------------+
```

##### 新扩展聚合函数

###### 使用说明

本文介绍使用新扩展的聚合函数要进行的设置。

**操作说明**

升级到MaxCompute 2.0以后，产品扩展了新的聚合函数，在使用新函数的SQL前，需要添加如下SET语句。

```
SET odps.sql.type.system.odps2=true;
```

**说明**

上述SET语句和新函数的SQL语句需要同时提交运行。

###### COLLECT_LIST

本文介绍如何在MaxCompute中使用聚合函数COLLECT_LIST，用于将指定列的值聚合为一个数组。 大数据计算服务

**操作说明**

###### 使用说明

在给定Group内，将col指定的表达式聚合为一个数组。

**函数语法**

```
ARRAY COLLECT_LIST(col);
```

**参数说明**

col：必填，某列的列名，可以为任意数据类型。

**返回值**

##### 使用示例

`--` 建表

```
    col1 BIGINT,
    col2 STRING
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (1, 'b'); INSERT INTO tbla VALUES (1, 'c'); INSERT INTO tbla VALUES (2, 'd'); INSERT INTO tbla VALUES (2, 'e');
```

`--` 按`col1`分组，将`col2`聚合为数组

```
SELECT col1, COLLECT_LIST(col2) FROM tbla GROUP BY col1;
```

`--` 返回结果

```
+------+-----------------+
| col1 | _c1             |
+------+-----------------+
| 1    | [a, b, c]       |
| 2    | [d, e]          |
+------+-----------------+
```

###### COLLECT_SET

本文介绍如何在MaxCompute中使用聚合函数COLLECT_SET，用于将指定列的值聚合为一个无重复元素的集合数组。

**操作说明**

###### 使用说明

在给定Group内，将col指定的表达式聚合为一个无重复元素的集合数组。

**函数语法**

```
ARRAY COLLECT_SET(col);
```

**参数说明**

大数据计算服务 col：必填，某列的列名，可为任意数据类型。

**返回值**

##### 使用示例

`--` 建表

```
    col1 BIGINT,
    col2 STRING
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (1, 'b'); INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (2, 'd'); INSERT INTO tbla VALUES (2, 'd');
```

`--` 按`col1`分组，将`col2`聚合为无重复元素的数组

```
SELECT col1, COLLECT_SET(col2) FROM tbla GROUP BY col1;
```

`--` 返回结果

```
+------+----------+
| col1 | _c1      |
+------+----------+
| 1    | [a, b]   |
| 2    | [d]      |
+------+----------+
```

###### VARIANCE/VAR_POP

本文介绍如何在MaxCompute中使用聚合函数VARIANCE/VAR_POP，用于计算指定数字列的方差。

**操作说明**

###### 使用说明

求指定数字列的方差。

**函数语法**

```
DOUBLE VARIANCE(col); DOUBLE VAR_POP(col);
```

**参数说明**

col：必填，数值类型列。为其他类型时返回NULL。

**返回值**

返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO test VALUES (8); INSERT INTO test VALUES (9); INSERT INTO test VALUES (10); INSERT INTO test VALUES (11);
```

`--` 求`c1`列的方差（`VARIANCE`和`VAR_POP`等价）

```
SELECT VARIANCE(c1) FROM test; SELECT VAR_POP(c1) FROM test;
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.25 |
+------+
```

###### VAR_SAMP

本文介绍如何在MaxCompute中使用聚合函数VAR_SAMP，用于计算指定数字列的样本方差。

**操作说明**

###### 使用说明

求指定数字列的样本方差。

**函数语法**

```
DOUBLE VAR_SAMP(col);
```

**参数说明**

col：必填，数值类型列。其他类型时返回NULL。

**返回值**

返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO test VALUES (8); INSERT INTO test VALUES (9); INSERT INTO test VALUES (10); INSERT INTO test VALUES (11);
```

`--` 求`c1`列的样本方差

```
SELECT VAR_SAMP(c1) FROM test;
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 1.6666666666666667  |
+---------------------+
```

###### COVAR_POP

本文介绍如何在MaxCompute中使用聚合函数COVAR_POP，用于计算指定两个数字列的总体协方差。

**操作说明**

###### 使用说明

求指定两个数字列的总体协方差。

**函数语法**

```
DOUBLE COVAR_POP(col1, col2);
```

**参数说明**

col1：必填，数值类型列。其他类型时返回NULL。 col2：必填，数值类型列。其他类型时返回NULL。

**返回值**

返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT,
    c2 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO test VALUES (3, 2); INSERT INTO test VALUES (14, 5); INSERT INTO test VALUES (50, 14); INSERT INTO test VALUES (26, 75);
```

`--` 求`c1`和`c2`的总体协方差

```
SELECT COVAR_POP(c1, c2) FROM test;
```

`--` 返回结果

```
+----------------------+
| _c0                  |
+----------------------+
| 123.49999999999997   |
+----------------------+
```

###### COVAR_SAMP

本文介绍如何在MaxCompute中使用聚合函数COVAR_SAMP，用于计算指定两个数字列的样本协方差。

**操作说明**

###### 使用说明

求指定两个数字列的样本协方差。

**函数语法**

```
DOUBLE COVAR_SAMP(col1, col2);
```

**参数说明**

col1：必填，数值类型列。其他类型时返回NULL。 col2：必填，数值类型列。其他类型时返回NULL。

**返回值**

返回DOUBLE类型。

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT,
    c2 BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO test VALUES (3, 2); INSERT INTO test VALUES (14, 5); INSERT INTO test VALUES (50, 14); INSERT INTO test VALUES (26, 75);
```

`--` 求`c1`和`c2`的样本协方差

```
SELECT COVAR_SAMP(c1, c2) FROM test;
```

`--` 返回结果

```
+----------------------+
| _c0                  |
+----------------------+
| 164.66666666666663   |
+----------------------+
```

###### ANY_VALUE

本文介绍如何在MaxCompute中使用聚合函数ANY_VALUE，用于在指定范围内任选一个非NULL值返回。

**操作说明**

###### 使用说明

在范围内任选一个值返回。

**函数语法**

```
ANY_VALUE(value);
```

**参数说明**

value：必填，可为任意类型。当value为NULL时，该行不参与计算。

**返回值**

返回类型和输入类型相同。

##### 使用示例

大数据计算服务

```
FROM VALUES (1, 'value1'), (1, 'value2'), (2, 'value3'), (2, NULL), (3, NULL) AS t(ke GROUP BY key;
```

`--` 返回结果

```
+------------+------------+
| key        | _c1        |
+------------+------------+
| 1          | value1     |
| 2          | value3     |
| 3          | NULL       |
+------------+------------+
```

###### NUMERIC_HISTOGRAM

本文介绍如何在MaxCompute中使用聚合函数NUMERIC_HISTOGRAM，用于统计指定列的近似直方图。

**操作说明**

###### 使用说明

统计指定列的近似直方图。

**函数语法**

```
MAP<DOUBLE, DOUBLE> NUMERIC_HISTOGRAM(BIGINT buckets, DOUBLE value);
```

**参数说明**

buckets：必填，BIGINT类型，返回的近似直方图的列的最大个数。 value：必填，DOUBLE类型，需要统计近似直方图的数据列。

**返回值**

MAP<DOUBLE, DOUBLE>类型。返回值中Key是近似直方图的X轴坐标点，Value是直方图一列的近似高度。

##### 使用示例

```
t(value);
```

`--` 返回结果

```
+-------------------------------------+
|               _c0                   |
+-------------------------------------+
| {1.5:2, 3.5:2, 5.5:2, 7.5:2, 9.5:2} |
+-------------------------------------+
```

###### PERCENTILE_APPROX

本文介绍如何在MaxCompute中使用聚合函数PERCENTILE_APPROX，用于返回指定数值列上指定百分比对应的近似值。

**操作说明**

大数据计算服务

###### 使用说明

返回指定数值列col上指定百分比p对应的值。

**函数语法**

```
DOUBLE PERCENTILE_APPROX(DOUBLE col, p [, B]); ARRAY<DOUBLE> PERCENTILE_APPROX(DOUBLE col, ARRAY(p1 [, p2]...) [, B]);
```

**参数说明**

col：必填，DOUBLE类型，需要计算近似百分位的数值列。 p：必填，百分比，取值为[0.0,1.0]。可以指定返回单个百分比值，也可以指定返回一个百分比数组。 B：选填，精度参数。精度越高产生的近似值误差越小。如果不设置该参数，默认值为10000。当col 中值的数目小于B时，将给出精确的百分位值。

**返回值**

PERCENTILE_APPROX(DOUBLE col, ARRAY(p1 [, p2]...) [, B]) 返回一个百分比数组。

##### 使用示例

```
SELECT PERCENTILE_APPROX(10.0, 0.5, 100);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 10.0 |
+------+ SELECT PERCENTILE_APPROX(10.0, ARRAY(0.5, 0.4, 0.1), 100);
```

`--` 返回结果

```
+------------------+
| _c0              |
+------------------+
| [10.0,10.0,10.0] |
+------------------+
```

###### APPROX_DISTINCT

本文介绍如何在MaxCompute中使用聚合函数APPROX_DISTINCT，用于返回输入的非重复值的近似数目。

**操作说明**

###### 使用说明

返回输入的非重复值的近似数目。

**函数语法**

```
BIGINT APPROX_DISTINCT(value);
```

**参数说明**

value：必填，需要统计去重的输入数据。 大数据计算服务

**返回值**

BIGINT类型。如果所有输入值都为空，则返回0。此函数会产生5%的标准误差。

##### 使用示例

```
SELECT APPROX_DISTINCT(value) FROM VALUES (1), (2), (2), (3), (3), (3), (4) AS t(valu e);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  4   |
+------+
```

#### 其他函数

##### ARRAY

本文为您介绍如何在MaxCompute中使用ARRAY函数，用于使用给定value构造ARRAY。

**操作说明**

###### 使用说明

**函数语法**

```
ARRAY ARRAY(value1, value2, ...);
```

**参数说明**

value：必填，可为任意数据类型，但是所有value必须类型一致。

**返回值**

##### 使用示例

```
SELECT ARRAY(123, 456, 789);
```

`--` 返回结果

```
+---------------+
| _c0           |
+---------------+
| [123,456,789] |
+---------------+
```

##### ARRAY_CONTAINS

本文为您介绍如何在MaxCompute中使用ARRAY_CONTAINS函数，用于检测给定ARRAY中是否包含指定值。

**操作说明**

###### 使用说明

大数据计算服务

**函数语法**

```
BOOLEAN ARRAY_CONTAINS(ARRAY<T> a, value v);
```

**参数说明**

**返回值**

BOOLEAN类型。

##### 使用示例

```
SELECT ARRAY_CONTAINS(ARRAY('a', 'b'), 'a');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ARRAY_CONTAINS(ARRAY(456, 789), 123);
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### CAST

本文介绍如何在MaxCompute中使用CAST函数将表达式结果转换为目标数据类型，并提供参考示例。

**操作说明**

###### 使用说明

将表达式的结果转换成目标类型，例如 `cast('1' as bigint)` 将字符串1转为整数类型的1。

**函数语法**

```
CAST(expr AS <type>);
```

**说明**

CAST(DOUBLE AS BIGINT)：将DOUBLE类型的值转换成BIGINT类型。 CAST(STRING AS BIGINT)：在将字符串转为BIGINT类型时，如果字符串中是以整型表达的数字，会直接转为BIGINT类型。如果字符串中是以浮点数或指数形式表达的数字，则会先转为DOUBLE类型，再转为BIGINT类型。 使用CAST(STRING AS DATETIME)或CAST(DATETIME AS STRING)时，会采用默认的日期格式**yyyy-mm-dd hh:mi:ss**。 大数据计算服务

**参数说明**

expr：必填，待转换的源表达式。 type：必填，目标数据类型（如BIGINT、STRING、DATETIME 等）。

**返回值**

返回值类型与指定的目标类型 `<type>` 一致。若转换失败或类型不兼容，将抛出异常。

##### 使用示例

```
SELECT CAST('12' AS BIGINT);
```

`--` 返回结果

```
+--------+
|   _c0  |
+--------+
|   12   |
+--------+
```

##### COALESCE

本文为您介绍如何在MaxCompute中使用COALESCE函数，用于返回列表中第一个非NULL的值。

**操作说明**

###### 使用说明

返回列表中第一个非NULL的值。

**函数语法**

```
COALESCE(expr1, expr2, ...);
```

**参数说明**

expr：必填，即为要测试的值。所有这些值的类型必须相同或为NULL，否则会报错。至少要有一个参数，否则会报错。

**返回值**

返回值类型和参数类型相同。

##### 使用示例

大数据计算服务

```
SELECT COALESCE(NULL, NULL, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  3   |
+------+ SELECT COALESCE(NULL, 'hello', 'world');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| hello |
+-------+
```

##### DECODE

本文为您介绍如何在MaxCompute中使用DECODE函数，用于实现if-then-else分支选择的功能。

**操作说明**

###### 使用说明

实现if-then-else分支选择的功能。

**函数语法**

```
DECODE(expression, search, result[, search, result]...[, default]);
```

**参数说明**

expression：必填，要比较的表达式。 search：必填，和expression进行比较的搜索项。 result：必填，search和expression的值匹配时的返回值。 default：选填，如果所有的搜索项都不匹配，则返回此default值，如果未指定，则返回NULL。

**返回值**

返回匹配的result。如果没有匹配，返回default。如果没有指定default，返回NULL。 至少要指定三个参数。所有的result类型必须一致，或为NULL，不一致的数据类型会报错。所有的 search和expression类型必须一致，否则报错。

##### 使用示例

大数据计算服务

```
SELECT DECODE(customer_id, 1, 'Taobao', 2, 'Alipay', 3, 'Aliyun', NULL, 'N/A', 'Other s') AS result FROM VALUES (1, 10),
            (1, 10),
            (2, NULL),
            (3, 13),
            (4, 0),
            (NULL, 6),
            (5, 18) AS t(customer_id, value);
```

`--` 返回结果

```
+--------+
| result |
+--------+
| Taobao |
| Taobao |
| Alipay |
| Others |
| N/A    |
| Others |
+--------+ IF customer_id = 1 THEN result := 'Taobao'; ELSIF customer_id = 2 THEN result := 'Alipay'; ELSIF customer_id = 3 THEN result := 'Aliyun'; ... ELSE
  result := 'Others';
END IF;
```

**说明**

通常MaxCompute SQL在计算NULL=NULL时返回NULL，但在**decode**函数中，NULL与 NULL的值是相等的。

##### EXPLODE

本文为您介绍如何在MaxCompute中使用EXPLODE函数，用于将一行数据转为多行的UDTF。

**操作说明**

###### 使用说明

将一行数据转为多行的UDTF。如果var是ARRAY类型，则将列中存储的ARRAY转为多行。如果var是 MAP<K, V>类型，则将列中存储的MAP的每个Key-Value转换为包含两列的行，其中一列存储Key，另一列存储Value。 大数据计算服务

**说明**

不可以与GROUP BY、CLUSTER BY、DISTRIBUTE BY以及SORT BY一起使用。

**函数语法**

```
EXPLODE(var);
```

**参数说明**

**返回值**

转换后的行。

##### 使用示例

```
SELECT EXPLODE(ARRAY(NULL, 'a', 'b', 'c'));
```

`--` 返回结果

```
+------+
| col  |
+------+
| NULL |
| a    |
| b    |
| c    |
+------+
```

##### GET_IDCARD_AGE

本文为您介绍如何在MaxCompute中使用GET_IDCARD_AGE函数，用于根据身份证号码返回当前的年龄。

**操作说明**

###### 使用说明

根据身份证号码返回当前的年龄，返回值为当前年份减去身份证中标识的出生年份的差值。

**函数语法**

```
BIGINT GET_IDCARD_AGE(STRING idcardno);
```

**参数说明**

idcardno：必填，STRING类型，15位或18位身份证号码。在计算时会根据省份代码以及最后一位校验码检查身份证的合法性，如果校验不通过会返回NULL。

**返回值**

BIGINT类型。如果输入为NULL，返回NULL。如果当前年份减去出生年份差值大于100，返回NULL。

##### 使用示例

大数据计算服务 `SELECT GET_IDCARD_AGE('`身份证号码'); `--` 返回结果（输入真实的身份证号码，返回年龄信息，例如`"18"`）

```
SELECT GET_IDCARD_AGE(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### GET_IDCARD_BIRTHDAY

本文为您介绍如何在MaxCompute中使用GET_IDCARD_BIRTHDAY函数，用于根据身份证号码返回出生日期。

**操作说明**

###### 使用说明

根据身份证号码返回出生日期。

**函数语法**

```
DATETIME GET_IDCARD_BIRTHDAY(STRING idcardno);
```

**参数说明**

idcardno：必填，STRING类型，15位或18位身份证号码。在计算时会根据省份代码以及最后一位校验码检查身份证的合法性，如果校验不通过会返回NULL。

**返回值**

DATETIME类型。如果输入为NULL，返回NULL。

##### 使用示例

```
SELECT GET_IDCARD_BIRTHDAY('身份证号码');
```

`--` 返回结果（根据真实的身份证号码，返回出生日期，例如`"2001-01-01 00:00:00"`）

```
SELECT GET_IDCARD_BIRTHDAY(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### GET_IDCARD_SEX

本文为您介绍如何在MaxCompute中使用GET_IDCARD_SEX函数，用于根据身份证号码返回性别。

**操作说明**

大数据计算服务

**操作说明**

###### 使用说明

根据身份证号码返回性别，返回值为M（男）或F（女）。

**函数语法**

```
STRING GET_IDCARD_SEX(STRING idcardno);
```

**参数说明**

idcardno：必填，STRING类型，15位或18位身份证号码。在计算时会根据省份代码以及最后一位校验码检查身份证的合法性，如果校验不通过会返回NULL。

**返回值**

STRING类型。如果输入为NULL，返回NULL。

##### 使用示例

`SELECT GET_IDCARD_SEX('`身份证号码'); `--` 返回结果（根据真实的身份证号码，返回性别，例如`"M"`）

```
SELECT GET_IDCARD_SEX(NULL);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| NULL |
+------+
```

##### GREATEST

本文为您介绍如何在MaxCompute中使用GREATEST函数，用于返回输入参数中的最大值。

**操作说明**

###### 使用说明

返回输入参数中的最大值。

**函数语法**

```
GREATEST(var1, var2, ...);
```

**参数说明**

var1：必填，可以为BIGINT、DOUBLE、DECIMAL、DATETIME或STRING类型。 var2：必填，可以为BIGINT、DOUBLE、DECIMAL、DATETIME或STRING类型。

**说明**

如果所有的参数值都为NULL，则返回NULL。

**返回值**

输入参数中的最大值，当不存在隐式转换时，返回值类型同输入参数类型。 大数据计算服务有类型转换时，DOUBLE、BIGINT、STRING类型之间的比较返回DOUBLE类型；STRING和 DATETIME类型之间的比较返回DATETIME类型；DECIMAL类型和DOUBLE、BIGINT、STRING类型之间的比较返回DECIMAL类型。不允许其他的隐式类型转换。 当 SET odps.sql.hive.compatible=true; 时，任意参数输入为NULL，都会返回NULL。

##### 使用示例

```
SELECT GREATEST(1, 2, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  3   |
+------+ SELECT GREATEST('a', 'b', 'c');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| c    |
+------+ SELECT GREATEST(NULL, 1, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  2   |
+------+
```

##### INDEX

本文为您介绍如何在MaxCompute中使用INDEX函数，用于返回数组或MAP中指定位置的元素值。

**操作说明**

###### 使用说明

如果var1是ARRAY类型，函数返回第var2个元素值；如果var1是MAP<K, V>类型，函数返回var1中 Key为var2的Value。

**说明**

当**var1**为NULL时，返回NULL。

**函数语法**

```
INDEX(var1[var2]);
```

**参数说明**

大数据计算服务 var2：必填，如果var1是ARRAY类型，则var2是BIGINT类型并且var2大于等于0；如果var1是 MAP<K, V>类型，var2是K类型。

**返回值**

如果var1是ARRAY类型，函数返回T类型，在var2超出ARRAY元素数目范围的情况下返回NULL。 如果var1是MAP<K, V>类型，函数返回V类型，在MAP<K, V>中不存在Key为var2的情况下返回 NULL。当var1为NULL时，返回NULL。

##### 使用示例

`--` 当`var1`为数组时

```
SELECT ARRAY('a', 'b', 'c')[2];
```

`--` 返回结果

```
+-----+
| _c0 |
+-----+
| c   |
+-----+
```

`--` 当`var1`为`MAP<K, V>`类型时

```
SELECT STR_TO_MAP("test1=1,test2=2")["test1"];
```

`--` 返回结果

```
+-----+
| _c0 |
+-----+
| 1   |
+-----+
```

##### MAX_PT

本文为您介绍如何在MaxCompute中使用MAX_PT函数，用于返回分区表的一级分区的最大值并读取该分区下的数据文件。

**操作说明**

###### 使用说明

对于分区表，此函数返回该分区表的一级分区的最大值，按字母排序，且读取该分区下对应的数据文件。

**函数语法**

```
MAX_PT(table_full_name);
```

**参数说明**

table_full_name：必填，STRING类型，指定表名（必须带上Project名，例如prj.src），您必须对此表有读权限。

**返回值**

一级分区的最大值。如果使用ALTER TABLE的方式新增一个分区，但此分区中并无任何数据文件，则此分区不会做为返回值。

##### 使用示例

大数据计算服务 `--` 建表

```
    id BIGINT,
    name STRING
) PARTITIONED BY (pt STRING);
```

`--` 插入测试数据

```
INSERT INTO tbl PARTITION (pt = '20120901') VALUES (1, 'Alice'); INSERT INTO tbl PARTITION (pt = '20120902') VALUES (2, 'Bob');
```

`--` 查询最大分区下的数据

```
SELECT * FROM tbl WHERE pt = MAX_PT('myproject.tbl');
```

`--` 返回结果

```
+----+-------+----------+
| id | name  | pt       |
+----+-------+----------+
| 2  | Bob   | 20120902 |
+----+-------+----------+
```

##### ORDINAL

函数声明如下。 用途：将输入变量按从小到大排序后，返回**nth**指定位置的值。 参数说明：
**nth**：BIGINT类型。指定要返回的位置，取值从 1 开始，为NULL时返回NULL。
**var**：BIGINT、DOUBLE、DATETIME或STRING类型。
返回值： 排在第**nth**位的值，当不存在隐式转换时，返回值类型同输入参数类型。 有类型转换时，DOUBLE、BIGINT、STRING类型之间的转换返回DOUBLE类型。STRING和 DATETIME类型之间的转换返回DATETIME类型。不允许其他的隐式类型转换。 NULL为最小值。 示例如下。 `--`返回2

```
select ordinal(3, 1, 3, 2, 5, 2, 4, 6);
```

##### LEAST

本文为您介绍如何在MaxCompute中使用LEAST函数，用于返回输入参数中的最小值。

**操作说明**

###### 使用说明

大数据计算服务返回输入参数中的最小值。

**函数语法**

```
LEAST(var1, var2, ...);
```

**参数说明**

var：必填，BIGINT、DOUBLE、DECIMAL、DATETIME或STRING类型。如果所有参数值都为NULL， 则返回NULL。

**返回值**

输入参数中的最小值，当不存在隐式转换时，返回值类型同输入参数类型。 有类型转换时，DOUBLE、BIGINT、STRING类型之间的比较返回DOUBLE类型；STRING和 DATETIME类型之间的比较返回DATETIME类型；DECIMAL类型和DOUBLE、BIGINT、STRING类型之间的比较返回DECIMAL类型。 不允许其它的隐式类型转换。NULL为最小值。

##### 使用示例

```
SELECT LEAST(1, 2, 3);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  1   |
+------+ SELECT LEAST('a', 'b', 'c');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| a    |
+------+ SELECT LEAST(NULL, 1, 2);
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  1   |
+------+
```

##### SIZE

本文为您介绍如何在MaxCompute中使用SIZE函数，用于返回给定MAP的K/V对数或ARRAY的元素数目。

**操作说明**

###### 使用说明

SIZE(MAP)返回给定MAP中K/V对数。SIZE(ARRAY)返回给定ARRAY中的元素数目。 大数据计算服务

**函数语法**

```
INT SIZE(MAP map); INT SIZE(ARRAY array);
```

**参数说明**

map：必填，MAP类型的数据。

**返回值**

INT类型。

##### 使用示例

```
SELECT SIZE(MAP('a', 123, 'b', 456));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  2   |
+------+ SELECT SIZE(MAP('a', 123, 'b', 456, 'c', 789));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  3   |
+------+ SELECT SIZE(ARRAY('a', 'b'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  2   |
+------+ SELECT SIZE(ARRAY(123, 456, 789));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
|  3   |
+------+
```

##### SPLIT

本文为您介绍如何在MaxCompute中使用SPLIT函数，用于使用指定分隔符将字符串分割后返回数组。 大数据计算服务

**操作说明**

###### 使用说明

使用pat将str分割后返回数组。

**函数语法**

```
ARRAY<STRING> SPLIT(STRING str, STRING pat);
```

**参数说明**

str：必填，STRING类型，指被分割的字符串。 pat：必填，STRING类型的分隔符，支持正则表达式。

**返回值**

##### 使用示例

```
SELECT SPLIT("a,b,c", ",");
```

`--` 返回结果

```
+-----------+
| _c0       |
+-----------+
| [a, b, c] |
+-----------+
```

##### STR_TO_MAP

本文为您介绍如何在MaxCompute中使用STR_TO_MAP函数，用于使用指定分隔符将字符串分割成Key- Value对并返回MAP。

**操作说明**

###### 使用说明

使用delimiter1将text分割成Key-Value对，然后使用delimiter2分割每个Key-Value对的Key和 Value。

**函数语法**

```
MAP<STRING, STRING> STR_TO_MAP(STRING text [, STRING delimiter1 [, STRING delimiter2]]);
```

**参数说明**

text：必填，STRING类型，指被分割的字符串。 delimiter1：选填，STRING类型，分隔符，不指定时默认为半角逗号（,）。 delimiter2：选填，STRING类型，分隔符，不指定时默认为等于号（=）。

**返回值**

MAP<STRING, STRING>类型，返回值是text被delimiter1和delimiter2分割后的结果。

##### 使用示例

大数据计算服务

```
SELECT STR_TO_MAP("test1=1,test2=2");
```

`--` 返回结果

```
+------------------------+
| _c0                    |
+------------------------+
| {test1:1, test2:2}     |
+------------------------+
```

##### UUID

本文为您介绍如何在MaxCompute中使用UUID函数，用于返回一个随机全局ID。

**操作说明**

###### 使用说明

返回一个随机ID，形式为29347a88-1e57-41ae-bb68-a9edbdd94212。UUID返回的是一个随机的全局ID，其重复的概率很小。

**函数语法**

```
STRING UUID();
```

**参数说明**

无。

**返回值**

STRING类型。

##### 使用示例

```
SELECT UUID();
```

`--` 返回结果

```
+--------------------------------------+
| _c0                                  |
+--------------------------------------+
| 623b7436-f12c-486f-892a-e66f93679db5 |
+--------------------------------------+
```

##### UNIQUE_ID

本文为您介绍如何在MaxCompute中使用UNIQUE_ID函数，用于返回一个随机的唯一ID。

**操作说明**

###### 使用说明

返回一个随机的唯一ID，形式为29347a88-1e57-41ae-bb68-a9edbdd94212_1。该函数比UUID函数的运行效率高。

**函数语法**

```
STRING UNIQUE_ID();
```

**参数说明**

大数据计算服务无。

**返回值**

STRING类型。

##### 使用示例

```
SELECT UNIQUE_ID();
```

`--` 返回结果

```
+----------------------------------------+
| _c0                                    |
+----------------------------------------+
| 94465fb0-cb34-4156-8bcf-2d94c0f42730_0 |
+----------------------------------------+
```

##### SAMPLE

本文为您介绍如何在MaxCompute中使用SAMPLE函数，用于根据指定条件对数据进行采样过滤。

**操作说明**

###### 使用说明

对所有column_name的值，SAMPLE根据x, y的设置做采样，并过滤掉不满足采样条件的行。

**函数语法**

```
BOOLEAN SAMPLE(BIGINT x, BIGINT y [, column_name1, column_name2, ...]);
```

**参数说明**

x：必填，BIGINT类型，取值范围大于0的整型常量。表示哈希为x份，取第y份。 y：必填，BIGINT类型，取值范围大于0的整型常量。y可省略，省略时默认取第一份。如果省略参数中的y，则必须同时省略column_name。 column_name：选填，采样的目标列。该参数可以省略，省略时根据x, y的值随机采样。任意类型， 列的值可以为NULL。不做隐式类型转换。如果column_name为常量，则会报错。

**说明**

x, y为其他类型或小于等于0时报错，如果y>x也报错。x, y任意一个输入为NULL时，返回NULL。

**返回值**

BOOLEAN类型。为避免NULL值带来的数据倾斜，对于column_name中为NULL的值，会在x份中进行均匀哈希。如果不指定column_name，则数据量少时输出不一定均匀，在这种情况下建议指定 column_name，以获得好的输出结果。

##### 使用示例

大数据计算服务 `--` 建表

```
    cola BIGINT,
    colb STRING
);
```

`--` 插入测试数据

```
INSERT INTO tbla VALUES (1, 'a'); INSERT INTO tbla VALUES (2, 'b'); INSERT INTO tbla VALUES (3, 'c'); INSERT INTO tbla VALUES (4, 'd'); INSERT INTO tbla VALUES (5, 'e'); INSERT INTO tbla VALUES (6, 'f'); INSERT INTO tbla VALUES (7, 'g'); INSERT INTO tbla VALUES (8, 'h');
```

`--` 根据`cola`哈希为4份，取第1份

```
SELECT * FROM tbla WHERE SAMPLE(4, 1, cola) = true;
```

`--` 返回结果（实际结果因哈希分布而异）

```
+------+------+
| cola | colb |
+------+------+
| 4    | d    |
+------+------+
```

`--` 对每行数据做随机哈希分配为4份，取第2份

```
SELECT * FROM tbla WHERE SAMPLE(4, 2) = true;
```

`--` 返回结果（实际结果因哈希分布而异）

```
+------+------+
| cola | colb |
+------+------+
| 3    | c    |
| 5    | e    |
+------+------+
```

##### CASE WHEN表达式

本文为您介绍如何在MaxCompute中使用CASE WHEN表达式函数，用于根据表达式的计算结果灵活返回不同的值。

**操作说明**

###### 使用说明

**函数语法**

大数据计算服务 `--` 方式一

```
CASE value
  WHEN value1 THEN result1
  WHEN value2 THEN result2
  ...
  ELSE resultn
END;
```

`--` 方式二

```
CASE
  WHEN (_condition1) THEN result1
  WHEN (_condition2) THEN result2
  WHEN (_condition3) THEN result3
  ...
  ELSE resultn
END;
```

**参数说明**

value：必填，要比较的表达式。 value1, value2, ...：必填，和value进行比较的值。 result1, result2, ...：必填，value与对应值匹配时返回的结果。 _condition1, _condition2, ...：必填，条件表达式。 resultn：选填，所有条件都不匹配时返回的默认值（ELSE子句）。

**返回值**

如果result的类型只有BIGINT和DOUBLE，统一转换为DOUBLE类型再返回。 如果result的类型中有STRING，统一转换为STRING类型再返回。 如果无法进行转换则会报错（例如BOOLEAN类型无法转换为STRING类型）。不允许其他类型之间的转换。

##### 使用示例

大数据计算服务 `--` 建表

```
    shop_name STRING,
    sale_amount BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO sale_detail VALUES ('hangzhou_shop', 100); INSERT INTO sale_detail VALUES ('shanghai_shop', 200); INSERT INTO sale_detail VALUES ('beijing_shop', 300); INSERT INTO sale_detail VALUES (NULL, 400);
```

`--` 根据`shop_name`的不同情况得出所属区域

```
  CASE
    WHEN shop_name IS NULL THEN 'default_region'
    WHEN shop_name LIKE 'hang%' THEN 'zj_region'
  END AS region
FROM sale_detail;
```

`--` 返回结果

```
+---------------+
| region        |
+---------------+
| zj_region     |
| NULL          |
| NULL          |
| default_region|
+---------------+
```

##### IF

本文介绍如何在MaxCompute中使用IF函数根据条件表达式返回不同的值，并提供参考示例。

**操作说明**

###### 使用说明

根据条件表达式的真假，返回对应的值。

**函数语法**

```
IF(testCondition, valueTrue, valueFalseOrNull);
```

**参数说明**

testCondition：BOOLEAN类型，要判断的表达式。 valueTrue：表达式**testCondition**为真时，返回的值。 valueFalseOrNull：表达式**testCondition**不为真时，返回的值，可以设为NULL。

**返回值**

返回值与valueTrue或valueFalseOrNull的类型一致。

##### 使用示例

大数据计算服务

```
SELECT IF(1=2,100,200);
```

`--` 返回结果

```
+--------+
|   _c0  |
+--------+
|   200  |
+--------+
```

##### 新扩展其他函数

###### 使用说明

本文介绍使用新扩展的其他函数要进行的设置。

**操作说明**

升级到MaxCompute 2.0以后，产品扩展了新的其他函数，在使用新函数的SQL前，需要添加如下SET语句。

```
SET odps.sql.type.system.odps2=true;
```

**说明**

上述SET语句和新函数的SQL语句需要同时提交运行。

###### MAP

本章节为您介绍其他函数中的MAP函数，并提供参考示例。

**操作说明**

###### 使用说明

**函数语法**

```
MAP MAP(K key1, V value1, K key2, V value2, ...);
```

**参数说明**

key：所有**key**类型一致（包括隐式转换后类型一致），必须是基本数据类型。 value：所有**value**类型一致（包括隐式转换后类型一致），可为任意数据类型。

**返回值**

MAP类型。

##### 使用示例

大数据计算服务

```
    c1 BIGINT,
    c2 STRING,
    c3 STRING,
    c4 BIGINT,
    c5 BIGINT
); (1000, 'k11', 'k21', 86, 15), (1001, 'k12', 'k22', 97, 2), (1002, 'k13', 'k23', 99, 1); SELECT map(c2,c4,c3,c5) FROM t_table;
```

`--` 返回结果

```
+------------------+
|        _c0       |
+------------------+
| {k11:86, k21:15} |
| {k12:97, k22:2}  |
| {k13:99, k23:1}  |
+------------------+
```

###### MAP_KEYS

本文为您介绍如何在MaxCompute中使用MAP_KEYS函数，用于将MAP中的所有Key作为数组返回。

**操作说明**

###### 使用说明

将MAP中的所有Key作为数组返回。

**函数语法**

```
ARRAY MAP_KEYS(MAP<K, V> map);
```

**参数说明**

map：必填，MAP类型数据。

**返回值**

##### 使用示例

大数据计算服务 `--` 建表

```
    c1 BIGINT,
    t_map MAP<STRING, BIGINT>
);
```

`--` 插入测试数据

```
INSERT INTO t_table_map VALUES (1000, MAP('k11', 86, 'k21', 15)); INSERT INTO t_table_map VALUES (1001, MAP('k12', 97, 'k22', 2)); INSERT INTO t_table_map VALUES (1002, MAP('k13', 99, 'k23', 1)); SELECT c1, MAP_KEYS(t_map) FROM t_table_map;
```

`--` 返回结果

```
+------+--------------+
| c1   | _c1          |
+------+--------------+
| 1000 | [k11, k21]   |
| 1001 | [k12, k22]   |
| 1002 | [k13, k23]   |
+------+--------------+
```

###### MAP_VALUES

本文为您介绍如何在MaxCompute中使用MAP_VALUES函数，用于将MAP中的所有Values作为数组返回。

**操作说明**

###### 使用说明

**函数语法**

```
ARRAY MAP_VALUES(MAP<K, V> map);
```

**参数说明**

map：必填，MAP类型数据。

**返回值**

##### 使用示例

```
SELECT MAP_VALUES(MAP('a', 123, 'b', 456));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| [123, 456] |
+------------+
```

###### SORT_ARRAY

大数据计算服务本文为您介绍如何在MaxCompute中使用SORT_ARRAY函数，用于对给定数组中的数据排序。

**操作说明**

###### 使用说明

对给定数组中的数据排序。

**函数语法**

```
ARRAY SORT_ARRAY(ARRAY<T>);
```

**参数说明**

**返回值**

##### 使用示例

`--` 建表

```
    c1 ARRAY<STRING>,
    c2 ARRAY<INT>,
);
```

`--` 插入测试数据

```
INSERT INTO t_array VALUES (ARRAY('a', 'c', 'f', 'b'), ARRAY(4, 5, 7, 2, 5, 8), ARRAY
```

`('`你`', '`我`', '`他'));

```
SELECT SORT_ARRAY(c1), SORT_ARRAY(c2), SORT_ARRAY(c3) FROM t_array;
```

`--` 返回结果

```
+-----------------+---------------------+-----------------+
| _c0             | _c1                 | _c2             |
+-----------------+---------------------+-----------------+
| [a, b, c, f]    | [2, 4, 5, 5, 7, 8] | [他, 你, 我]    |
+-----------------+---------------------+-----------------+
```

###### POSEXPLODE

本文为您介绍如何在MaxCompute中使用POSEXPLODE函数，用于将给定ARRAY展开为带有下标的多行数据。

**操作说明**

###### 使用说明

将给定ARRAY展开，每个Value一行，每行两列分别对应数组从0开始的下标和数组元素。

**函数语法**

```
POSEXPLODE(ARRAY<T>);
```

**参数说明**

**返回值**

大数据计算服务生成的表，包含两列：pos（下标，从0开始）和val（数组元素）。

##### 使用示例

```
SELECT POSEXPLODE(ARRAY('a', 'c', 'f', 'b'));
```

`--` 返回结果

```
+-----+-----+
| pos | val |
+-----+-----+
| 0   | a   |
| 1   | c   |
| 2   | f   |
| 3   | b   |
+-----+-----+
```

###### STRUCT

本文为您介绍如何在MaxCompute中使用STRUCT函数，用于使用给定value列表建立STRUCT。

**操作说明**

###### 使用说明

**函数语法**

```
STRUCT STRUCT(value1, value2, ...);
```

**参数说明**

value：必填，各value可为任意数据类型。

**返回值**

##### 使用示例

```
SELECT STRUCT('a', 123, 'true', 56.90);
```

`--` 返回结果

```
+------------------------------------------+
| _c0                                      |
+------------------------------------------+
| {col1:a, col2:123, col3:true, col4:56.9} |
+------------------------------------------+
```

###### NAMED_STRUCT

本文为您介绍如何在MaxCompute中使用NAMED_STRUCT函数，用于使用给定name/value列表建立

**操作说明**

###### 使用说明

大数据计算服务

**函数语法**

```
STRUCT NAMED_STRUCT(STRING name1, T1 value1, STRING name2, T2 value2, ...);
```

**参数说明**

name：必填，指定的STRING类型的Field名称。此参数为常量。 value：必填，各value可为任意数据类型。

**返回值**

##### 使用示例

```
SELECT NAMED_STRUCT('user_id', 10001, 'user_name', 'bob', 'married', 'F', 'weight', 6 3.50);
```

`--` 返回结果

```
+------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| {user_id:10001, user_name:bob, married:F, weight:63.5}    |
+------------------------------------------------------------+
```

###### INLINE

本文为您介绍如何在MaxCompute中使用INLINE函数，用于将给定STRUCT数组展开为多行多列数据。

**操作说明**

###### 使用说明

将给定STRUCT数组展开，每个数组元素对应一行，每行的每个STRUCT元素对应一列。

**函数语法**

```
INLINE(ARRAY<STRUCT<f1:T1, f2:T2, ...>>);
```

**参数说明**

**返回值**

表生成的函数。

##### 使用示例

大数据计算服务 `--` 建表

```
    t_struct STRUCT<user_id:BIGINT, user_name:STRING, married:STRING, weight:DOUBLE>
);
```

`--` 插入测试数据

```
INSERT INTO t_table VALUES (NAMED_STRUCT('user_id', 10001, 'user_name', 'LiLei', 'mar ried', 'N', 'weight', 63.5)); INSERT INTO t_table VALUES (NAMED_STRUCT('user_id', 10002, 'user_name', 'HanMeiMei', 'married', 'Y', 'weight', 43.5)); SELECT INLINE(ARRAY(t_struct)) FROM t_table;
```

`--` 返回结果

```
+---------+-----------+---------+--------+
| user_id | user_name | married | weight |
+---------+-----------+---------+--------+
| 10001   | LiLei     | N       | 63.5   |
| 10002   | HanMeiMei | Y       | 43.5   |
+---------+-----------+---------+--------+
```

###### BETWEEN AND表达式

本文为您介绍如何在MaxCompute中使用BETWEEN AND表达式函数，用于判断值是否在指定范围内。

**操作说明**

###### 使用说明

如果A、B或C为空，则为空；如果A大于或等于B且小于或等于C，则为True，否则为False。

**函数语法**

```
A [NOT] BETWEEN B AND C;
```

**参数说明**

A：必填，要判断的表达式。 B：必填，范围的下界。 C：必填，范围的上界。

**返回值**

BOOLEAN类型。如果A、B或C为空，返回NULL。如果A大于或等于B且小于或等于C，返回True，否则返回False。

##### 使用示例

`--` 建表

```
    empno BIGINT,
    ename STRING,
    job STRING,
    mgr BIGINT,
    hiredate DATETIME,
    sal DOUBLE,
    comm DOUBLE,
```

大数据计算服务

```
    deptno BIGINT
);
```

`--` 插入测试数据

```
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, DATETIME '1980-12-17 00:00:00', 800, NULL, 20); INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, DATETIME '1981-02-20 00:00:0 0', 1600, 300, 30); INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, DATETIME '1981-02-22 00:00:00 ', 1250, 500, 30); INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, DATETIME '1981-04-02 00:00:00 ', 2975, NULL, 20); INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, DATETIME '1981-09-28 00:00: 00', 1250, 1400, 30); INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, DATETIME '1981-05-01 00:00:00 ', 2850, NULL, 30); INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, DATETIME '1981-06-09 00:00:00 ', 2450, NULL, 10); INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, DATETIME '1987-04-19 00:00:00 ', 3000, NULL, 20); INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, DATETIME '1981-11-17 00:00:0 0', 5000, NULL, 10); INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, DATETIME '1981-09-08 00:00: 00', 1500, 0, 30); INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, DATETIME '1987-05-23 00:00:00', 1100, NULL, 20); INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, DATETIME '1981-12-03 00:00:00', 950, NULL, 30); INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, DATETIME '1981-12-03 00:00:00' , 3000, NULL, 20); INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, DATETIME '1982-01-23 00:00:00' , 1300, NULL, 10); INSERT INTO emp VALUES (7948, 'JACCKA', 'CLERK', 7782, DATETIME '1981-04-12 00:00:00' , 5000, NULL, 10); INSERT INTO emp VALUES (7956, 'WELAN', 'CLERK', 7649, DATETIME '1982-07-20 00:00:00', 2450, NULL, 10); INSERT INTO emp VALUES (7956, 'TEBAGE', 'CLERK', 7748, DATETIME '1982-12-30 00:00:00' , 1300, NULL, 10);
```

`--` 查询`sal`在大于等于`1000`小于等于`1500`之间的数据

```
SELECT * FROM emp WHERE sal BETWEEN 1000 AND 1500;
```

`--` 返回结果

```
+-------+--------+----------+------+---------------------+--------+--------+--------+
| empno | ename  | job      | mgr  | hiredate            | sal    | comm   | deptno |
+-------+--------+----------+------+---------------------+--------+--------+--------+
| 7521  | WARD   | SALESMAN | 7698 | 1981-02-22 00:00:00 | 1250.0 | 500.0  | 30     |
| 7654  | MARTIN | SALESMAN | 7698 | 1981-09-28 00:00:00 | 1250.0 | 1400.0 | 30     |
| 7844  | TURNER | SALESMAN | 7698 | 1981-09-08 00:00:00 | 1500.0 | 0.0    | 30     |
| 7876  | ADAMS  | CLERK    | 7788 | 1987-05-23 00:00:00 | 1100.0 | NULL   | 20     |
| 7934  | MILLER | CLERK    | 7782 | 1982-01-23 00:00:00 | 1300.0 | NULL   | 10     |
| 7956  | TEBAGE | CLERK    | 7748 | 1982-12-30 00:00:00 | 1300.0 | NULL   | 10     |
+-------+--------+----------+------+---------------------+--------+--------+--------+
```

大数据计算服务

###### NVL

当您在查询中希望用一个具体的值来代替NULL值时，MaxCompute支持使用NVL函数将NULL值替换为指定的值，确保在执行数据分析或生成报告时，结果中不会有意外的空值。本文为您介绍在MaxCompute中 NVL函数的使用。

**操作说明**

###### 使用说明

如果value值为NULL，返回default_value，否则返回value。函数的两个参数的数据类型必须一致。

**函数语法**

```
NVL(T value, T default_value);
```

**参数说明**

value：必填，输入参数。T指代输入数据类型，可以是MaxCompute支持的所有数据类型。 default_value：必填，替换后的值。必须与value的数据类型保持一致。

**返回值**

如果value值为NULL，返回default_value，否则返回value。

##### 使用示例

`--` 创建表

```
    c1 STRING,
    c2 BIGINT,
    c3 DATETIME
);
```

`--` 插入测试数据

```
INSERT INTO nvl_test VALUES ('aaa', 23, DATETIME '2024-01-11 00:00:00'); INSERT INTO nvl_test VALUES ('bbb', NULL, DATETIME '2024-01-12 08:00:00'); INSERT INTO nvl_test VALUES (NULL, 20, DATETIME '2024-01-13 05:00:00'); INSERT INTO nvl_test VALUES ('ddd', 25, NULL); SELECT NVL(c1, '00000'), NVL(c2, 0), NVL(c3,'-') FROM nvl_test;
```

`--` 返回结果

```
+-------+------------+--------------------+
| _c0   | _c1        | _c2                 |
+-------+------------+---------------------+
| ddd   | 25         | -                   |
| 00000 | 20         | 2024-01-13 05:00:00 |
| aaa   | 23         | 2024-01-11 00:00:00 |
| bbb   | 0          | 2024-01-12 08:00:00 |
+-------+--------+-------------------------+
```

###### TABLE_EXISTS

本文为您介绍如何在MaxCompute中使用TABLE_EXISTS函数，用于查询指定的表是否存在。

**操作说明**

大数据计算服务

###### 使用说明

查询指定的表是否存在。

**函数语法**

```
BOOLEAN TABLE_EXISTS(STRING table_name);
```

**参数说明**

table_name：必填，表名称，STRING类型。表名称中可以指定项目空间名称（例如

**返回值**

BOOLEAN类型。如果指定的表存在返回True，否则返回False。

##### 使用示例

`--` 建表

```
    col1 STRING,
    col2 STRING
);
```

`--` 插入测试数据

```
INSERT INTO abd VALUES ('value1', 'value2'); SELECT IF(TABLE_EXISTS('abd'), col1, col2) FROM abd;
```

`--` 返回结果

```
+--------+
| _c0    |
+--------+
| value1 |
+--------+
```

###### PARTITION_EXISTS

本文为您介绍如何在MaxCompute中使用PARTITION_EXISTS函数，用于查询指定的分区是否存在。

**操作说明**

###### 使用说明

查询指定的分区是否存在。

**函数语法**

```
BOOLEAN PARTITION_EXISTS(STRING table_name, STRING... partitions);
```

**参数说明**

table_name：必填，表名称，STRING类型。表名称中可以指定项目空间名称（例如 partitions：必填，分区名称，STRING类型。按照表分区列的顺序依次写出分区值，分区值数目必须与分区列数目一致。

**返回值**

大数据计算服务 BOOLEAN类型。如果指定的分区存在返回 `true` ，否则返回 `false` 。

##### 使用示例

`--` 创建分区表`foo`

```
    id BIGINT
) PARTITIONED BY (ds STRING, hr STRING);
```

`--` 为分区表`foo`新增分区

```
ALTER TABLE foo ADD PARTITION (ds = '20190101', hr = '1');
```

`--` 查询分区`ds='20190101'`和`hr='1'`是否存在

```
SELECT PARTITION_EXISTS('foo', '20190101', '1');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| true  |
+-------+
```

### UDF

#### Java UDF

##### 概述

本文介绍MaxCompute用户自定义函数（UDF）的分类、调用规则及跨项目使用方法。当内建函数无法满足需求时，您可通过自定义函数扩展SQL计算能力。

##### 功能介绍

UDF（User Defined Function）即用户自定义函数。MaxCompute提供多种内建函数来满足您的计算需求，同时您还可以通过创建自定义函数来满足更多的计算需求。

###### 使用说明

UDF的使用方法与普通的内建函数类似。Java和MaxCompute数据类型的对应关系，请参见参数与返回值类型。

**说明**

当UDF的命名与内建函数的命名相同时，使用 `select ::`函数名(表达式) ; 语句调用内建函数。例如，MaxCompute中包含命名为CONCAT的UDF，则系统默认调用此UDF，不会调用CONCAT内建函数。如果希望调用CONCAT内建函数，需要执行 select ::concat('ab', 'c') ; 语句。

**UDF函数分类**

MaxCompute支持的UDF有三种，如下表所示。

| UDF 分类 | 描述 |
|---|---|

大数据计算服务

| UDF（User Defined Scalar Function） | 自定义标量值函数。 其输入与输出是一对一的关系，即读入一行数据，写一条输出值 。 |
|---|---|
| UDTF（User Defined Table Valued Function） | 自定义表值函数。 用来解决一次函数调用输出多行数据的需求。它是唯一能够返回多个字段的自定义函数。UDTF不等于UDT（User Defined Type）。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数。 其输入与输出是多对一的关系， 即将多条输入记录聚合成一条输出值。它可以与SQL中的GROUP BY语句联用。 |

|  | 说明在SQL语句中使用自定义函数时，可能提示内存不足。这是由于计算的数据量过大并且存在倾斜，导致任务超出默认分配的内存。这种情况下，您可以通过 set odps.sql.udf.joiner.jvm.memory=xxxx; 语句手动设置内存来解决此问题。 |
|---|---|
|  | odps.sql.udf.joiner.jvm.memory=xxxx; |

##### 使用示例

MaxCompute的UDF支持跨项目分享，即在项目A中可以使用项目B的UDF。跨项目分享的SQL语句如下。

```
SELECT other_project:udf_in_other_project(arg0, arg1) AS res FROM table_t;
```

**说明**

`udf_in_other_project` ：在 `other_project` 项目中已注册的UDF函数名称。

**获取SDK依赖**

如果您使用Maven，您可以从Maven库中搜索 `odps-sdk-udf` ，获取SDK依赖版本信息。

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>odps-sdk-udf</artifactId>
   <version>0.29.10-public</version>
</dependency>
```

##### 参数与返回值类型

本文为您介绍MaxCompute中UDF函数的参数与返回值类型，以及Java数据类型与MaxCompute类型的映射规则。有助于您准确完成自定义函数的类型声明，避免因类型不匹配导致的运行时报错或数据精度丢失。

**特性说明**

大数据计算服务 MaxCompute 2.0版本升级后，Java UDF支持的数据类型从原来的BIGINT、STRING、DOUBLE及 BOOLEAN扩展了更多的新数据类型，同时还扩展支持了ARRAY、MAP、STRUCT以及Writable等复杂类型。

**新数据类型使用说明**

UDF使用新数据类型的方法，如下所示： UDAF和UDTF通过**@Resolve**注解来获取Signature，例如 `@Resolve("smallint-`

```
>varchar(10)") 。
```

UDF通过反射分析**evaluate**来获取Signature，此时MaxCompute内置类型与Java类型符合一一映射关系。

**重要**

用户可以使用 `type,*` 实现任意个数的传参，例如@resolve("string,*com.aliyun.odps.data.Struct从反射看不出field name和field type，所以需要用 @Resolve annotation来辅助。即如果需要在UDF中使用struct，要求在UDF class上也标注上@Resolve注解，这个注解只会影响参数或返回值中包含com.aliyun.odps.data.Struct的重载。 目前class上只能提供一个@Resolve annotation，因此一个UDF中带有struct参数或返回值的重载只能有一个。

**复杂类型使用说明**

UDF使用复杂类型的方法，如下所示： UDTF通过**@Resolve**注解指定Signature，例

```
如 @Resolve("array<string>,struct<a1:bigint,b1:string>,string-
```

UDF通过**evaluate**方法的Signature映射UDF的输入输出类型，此时参考MaxCompute类型与Java类型的映射关系。其中： MAP对应**java.util.Map**。 UDAF通过**@Resolve**注解来获取Signature，例如 `@Resolve("smallint->varchar(10)")` 。

**数据类型映射关系**

MaxCompute数据类型与Java数据类型的对应关系，如下所示。

| MaxCompute Type | Java Type |
|---|---|
| TINYINT | java.lang.Byte |
| SMALLINT | java.lang.Short |
| INT | java.lang.Integer |

大数据计算服务

| BIGINT | java.lang.Long |
|---|---|
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

**说明**

在UDF中输入或输出参数的类型请务必使用Java Type，否则会报错ODPS-0130071。 Java中对应的数据类型以及返回值数据类型是对象，数据类型首字母需大写。 SQL中的NULL值通过Java中的NULL引用表示，因此不允许使用Java Primitive Type，因为无法表示SQL中的NULL值。 MaxCompute 2.0版本支持定义Java UDF时，使用Writable类型作为参数和返回值。下面为

| MaxCompute Type | Java Writable Type |
|---|---|

大数据计算服务

| TINYINT | ByteWritable |
|---|---|
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
| INTERVAL YEAR MONTH _ _ | IntervalYearMonthWritable |
| INTERVAL DAY TIME _ _ | IntervalDayTimeWritable |
| ARRAY | N/A |
| MAP | N/A |
| STRUCT | N/A |

##### UDF

大数据计算服务本文为您介绍UDF函数中的自定义标量值函数（User Defined Scalar Function），并提供参考示例。

#### 使用须知

实现UDF需要继承**com.aliyun.odps.udf.UDF**类，并实现**evaluate**方法。
**evaluate**方法必须是非静态的 `public` 方法。
**evaluate**方法的参数和返回值类型将作为SQL中UDF的函数签名。
您可以在UDF中实现多个**evaluate**方法，在调用UDF时，框架会依据UDF调用的参数类型匹配正确的**evaluate**方法。

**说明**

不同的JAR包中最好不要有类名相同但实现功能逻辑不一样的类。例如**UDF(UDAF/UDTF)**：
**udf1**、**udf2**分别对应资源**udf1.jar**和**udf2.jar**。如果两个JAR包里都包含一
个**com.aliyun.UserFunction**类，当同一个SQL中同时使用到这两个UDF时，系统会随机加载其中一个类，导致UDF执行行为不一致，甚至编译失败。 如果1个SQL中同时使用2个UDF，执行时2个UDF会共享一个Classpath，不会隔离。如果2个 UDF引用的资源都包含同一个class，则Classloader会引用哪个class是不确定的。因此，请尽量避免在不同的资源中使用同一个Class。

##### 使用示例

可通过实现 `void setup(ExecutionContext ctx)` 和 `void close()` 来分别实现UDF的初始化和结束代码。

**Java Type类型**

使用Java类型实现将输入字符串转换为小写形式。

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.udf.UDF; public final class Lower extends UDF {
    public String evaluate(String s) {
        if (s == null) {
            return null;
        }
        return s.toLowerCase();
    }
}
```

大数据计算服务

```java
package com.aliyun.odps.udf.example; import com.aliyun.odps.io.Text; import com.aliyun.odps.udf.UDF;
    private Text ret = new Text();
    public Text evaluate(Text a, Text b) {
        if (a == null || b == null) {
            return null;
        }
        ret.clear();
        ret.append(a.getBytes(), 0, a.getLength());
        ret.append(b.getBytes(), 0, b.getLength());
        return ret;
    }
}
```

##### UDAF

本文为您介绍UDF函数中的自定义聚合函数（User Defined Aggregation Function），并提供参考示例。

###### 使用说明

实现UDAF类需要继承**com.aliyun.odps.udf.Aggregator**类，并实现以下几个方法。 大数据计算服务

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.ContextFunction; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; public abstract class Aggregator implements ContextFunction {
    @Override
    public void setup(ExecutionContext ctx) throws UDFException {
    }
    @Override
    public void close() throws UDFException {
    }
    /**
```

`*/`

```
    abstract public Writable newBuffer();
    /**
```

`* @param buffer` 聚合`buffer * @param args SQL`中调用`UDAF`时指定的参数，不能为`null`，但是`args` 里面的元素可以为`null`，代表对应的输入数据是`null * @throws UDFException`。 `*/`

```
    abstract public void iterate(Writable buffer, Writable[] args) throws UDFException;
    /**
```

* 生成最终结果 `* @param buffer * @return Object UDAF`的最终结果 `* @throws`

```
UDFException。
```

`*/`

```
    abstract public Writable terminate(Writable buffer) throws UDFException;
    abstract public void merge(Writable buffer, Writable partial) throws UDFException;
}
```

**实现过程**

其中最重要的是**iterate**、**merge**和**terminate**三个方法，UDAF的主要逻辑依赖于这三个方法的实现。 此外，还需要您实现自定义的Writable Buffer。以实现求平均值**avg**为例，下图简要说明了在 MaxCompute UDAF中这一函数的实现逻辑及计算流程。 iterate(a): 1; r.sum += a; terminate: merge(PartialResult pr): 4.2 r.count += pr.count; r.sum += pr.sum; iterate(a): 1; 大数据计算服务在上图中，输入数据被按照一定的大小进行分片，每片的大小适合一个Worker在适当的时间内完成。分片大小的设置需要您手动配置完成。 UDAF的计算过程分为两个阶段： 第一阶段：每个Worker统计分片内数据的个数及汇总值。您可以将每个分片内的数据个数及汇总值视为一个中间结果。 第二阶段：Worker汇总上一个阶段中每个分片内的信息。在最终输出时，**r.sum / r.count**即是所有输入数据的平均值。

##### 使用示例

计算平均值的UDAF示例。

```java
package org.alidata.odps.udf.examples; import java.io.DataInput; import java.io.DataOutput; import java.io.IOException; import com.aliyun.odps.io.DoubleWritable; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.Aggregator; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve("double->double") public class AggrAvg extends Aggregator {
    private static class AvgBuffer implements Writable {
        private double sum = 0;
        private long count = 0;
        @Override
        public void write(DataOutput out) throws IOException {
            out.writeDouble(sum);
            out.writeLong(count);
        }
        @Override
        public void readFields(DataInput in) throws IOException {
            sum = in.readDouble();
            count = in.readLong();
        }
    }
    private DoubleWritable ret = new DoubleWritable();
    @Override
        return new AvgBuffer();
    }
    @Override
    public void iterate(Writable buffer, Writable[] args) throws UDFException {
        DoubleWritable arg = (DoubleWritable) args[0];
        AvgBuffer buf = (AvgBuffer) buffer;
if(arg!=null){
```

大数据计算服务

```java
        if (arg != null) {
            buf.count += 1;
            buf.sum += arg.get();
        }
    }
    @Override
    public Writable terminate(Writable buffer) throws UDFException {
        AvgBuffer buf = (AvgBuffer) buffer;
            ret.set(0);
        } else {
            ret.set(buf.sum / buf.count);
        }
        return ret;
    }
    @Override
    public void merge(Writable buffer, Writable partial) throws UDFException {
        AvgBuffer buf = (AvgBuffer) buffer;
        AvgBuffer p = (AvgBuffer) partial;
        buf.sum += p.sum;
        buf.count += p.count;
    }
}
```

##### UDTF

###### 概述

本文为您介绍UDF函数中的自定义表值函数（User Defined Table Valued Function），并提供参考示例。

###### 使用说明

UDTF需要继承**com.aliyun.odps.udf.UDTF**类。这个类需要实现4个方法，如下表所示。

| 接口定义 | 描述 |
|---|---|
| public void setup(ExecutionContext ctx) throws UDFException | 初始化方法，在UDTF处理输入数据前，调用用户自定义的初始化行为。在每个Worker内setup会被先调用一次。 |
| public void process(Object[] args) throws UDFException | 这个方法由框架调用，SQL中每一条记录都会对应调用一次process，process的参数为SQL语句中指定的 UDTF输入参数。输入参数以Object[]的形式传入，输出结果通过forward函数输出。您需要在process函数内自行调用forward，以决定输出数据。 |
| public void close() throws UDFException | UDTF的结束方法，此方法由框架调用，并且只会被调用一次，即在处理完最后一条记录之后被调用。 |

大数据计算服务

| public void forward(Object …o) throws UDFException | 调用forward方法输出数据，每调用一次forward代表输出一条记录。SQL语句UDTF的AS子句指定的列须为该记录中的列。 |
|---|---|

##### 使用示例

1. 准备示例代码。

```java
package org.alidata.odps.udtf.examples; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.annotation.Resolve; import com.aliyun.odps.udf.UDFException; @Resolve("string,bigint->string,bigint") public class MyUDTF extends UDTF {
    @Override
    public void process(Object[] args) throws UDFException {
        String a = (String) args[0];
        Long b = (Long) args[1];
            forward(t, b);
        }
    }
}
```

2. 注册UDTF自定义函数。
假设在MaxCompute上创建UDTF时，注册函数名为 `user_udtf` 。
3. 使用UDTF自定义函数。
执行如下语句使用UDTF自定义函数。

```
    col0 STRING,
    col1 BIGINT
); ('A B', 1), ('C D', 2); SELECT user_udtf(col0, col1) AS (c0, c1) FROM my_table;
```

`--` 返回结果

```
+----+------------+
| c0 | c1         |
+----+------------+
| A  | 1          |
| B  | 1          |
| C  | 2          |
| D  | 2          |
+----+------------+
```

大数据计算服务

###### UDTF使用示例

**UDTF读取MaxCompute资源示例**

在UDTF中，您可以读取MaxCompute的资源，利用UDTF读取MaxCompute资源的示例如下所示。
1. 编写UDTF程序，编译成功后导出JAR包（假设为udtfexample1.jar）。

```java
package com.aliyun.odps.examples.udf; import java.io.BufferedReader; import java.io.IOException; import java.io.InputStream; import java.io.InputStreamReader; import java.util.Iterator; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.annotation.Resolve; /**
 * partitions: p2=1,p1=2
 * columns: colc,colb
```

`*/`

```java
@Resolve("string,string->string,bigint,string")
  ExecutionContext ctx;
  long fileResourceLineCount;
  long tableResource1RecordCount;
  long tableResource2RecordCount;
  @Override
  public void setup(ExecutionContext ctx) throws UDFException {
  this.ctx = ctx;
  try {
   InputStream in = ctx.readResourceFileAsStream("file_resource.txt");
   BufferedReader br = new BufferedReader(new InputStreamReader(in));
   String line;
   fileResourceLineCount = 0;
   while ((line = br.readLine()) != null) {
     fileResourceLineCount++;
   }
   br.close();
   Iterator<Object[]> iterator = ctx.readResourceTable("table_resource1").iterator();
   tableResource1RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource1RecordCount++;
     iterator.next();
   }
   iterator = ctx.readResourceTable("table_resource2").iterator();
   tableResource2RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource2RecordCount++;
     iterator.next();
```

大数据计算服务

```java
   }
 } catch (IOException e) {
   throw new UDFException(e);
 }
}
   @Override
   public void process(Object[] args) throws UDFException {
     String a = (String) args[0];
     long b = args[1] == null ? 0 : ((String) args[1]).length();
     forward(a, b, "fileResourceLineCount=" + fileResourceLineCount +
     + tableResource1RecordCount + "|tableResource2RecordCount=" +
tableResource2RecordCount);
    }
}
```

2. 添加资源到MaxCompute。

```
Add file file_resource.txt; Add jar udtfexample1.jar; Add table table_resource1 as table_resource1; Add table table_resource2 as table_resource2;
```

3. 在MaxCompute中创建UDTF函数（假设为mp_udtf ）。

```
create function mp_udtf as com.aliyun.odps.examples.udf.UDTFResource using 'udtfexample1.jar, file_resource.txt, table_resource1, table_resource2';
```

4. 运行该UDTF。

```
select mp_udtf("10","20") as (a, b, fileResourceLineCount) from table_resource1;
```

返回结果如下。

```
+-------+------------+-------+ +-------+------------+-------+
| 10    | 2          |
fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 |
| 10    | 2          |
fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 | +-------+------------+-------+
```

**复杂数据类型示例**

以下示例中，定义了一个有三个Overloads的UDF，其中第一个用了ARRAY作为参数，第二个用了MAP作为参数，第三个用了STRUCT作为参数。由于第三个Overloads将STRUCT作为参数或者返回值的类型，因此要求必须要对UDF Class打上**@Resolve**注解，指定STRUCT的具体类型。 大数据计算服务

```java
import com.aliyun.odps.udf.UDF; import com.aliyun.odps.udf.annotation.Resolve;
    public String evaluate(List vals, Long len) {
        return vals.get(len.intValue());
    }
    public String evaluate(Map map, String key) {
        return map.get(key);
    }
    public String evaluate(Struct struct, String key) {
        return struct.getFieldValue("a") + key;
    }
}
```

您可以直接将复杂类型传入UDF中。

```
create function my_index as 'UdfArray' using 'myjar.jar'; select id, my_index(array('red', 'yellow', 'green'), colorOrdinal) as color_name from c
```

o

**Hive UDF兼容示例**

MaxCompute 2.0支持Hive风格的UDF，部分Hive UDF、UDTF可以直接在MaxCompute上使用。 目前支持兼容的Hive版本为2.1.0，对应Hadoop版本为2.7.2。如果UDF是在其他版本的

**说明**

Hive/Hadoop开发的，则可能需要使用此Hive/Hadoop版本重新编译。 示例如下。 大数据计算服务

```java
package com.aliyun.odps.compiler.hive; import org.apache.hadoop.hive.ql.exec.UDFArgumentException; import org.apache.hadoop.hive.ql.metadata.HiveException; import org.apache.hadoop.hive.ql.udf.generic.GenericUDF; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspector; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspectorFactory; import java.util.ArrayList; import java.util.List; import java.util.Objects; public class Collect extends GenericUDF {
  @Override
  public ObjectInspector initialize(ObjectInspector[] objectInspectors) throws UDFArgum
entException {
      throw new UDFArgumentException("Collect: input args should >= 1");
    }
      if (objectInspectors[i] != objectInspectors[0]) {
        throw new UDFArgumentException("Collect: input oi should be the same for all ar
gs");
      }
    }
    return ObjectInspectorFactory.getStandardListObjectInspector(objectInspectors[0]);
  }
  @Override
  public Object evaluate(DeferredObject[] deferredObjects) throws HiveException {
    List<Object> objectList = new ArrayList<>(deferredObjects.length);
    for (DeferredObject deferredObject : deferredObjects) {
      objectList.add(deferredObject.get());
    }
    return objectList;
  }
  @Override
  public String getDisplayString(String[] strings) {
    return "Collect";
  }
}
```

上述UDF可以将任意类型、数量的参数打包成ARRAY输出。假设输出JAR包名为test.jar。 `--`添加资源。

```
Add jar test.jar; CREATE FUNCTION hive_collect as 'com.aliyun.odps.compiler.hive.Collect' using 'test.jar '; set odps.sql.hive.compatible=true; select hive_collect(4y,5y,6y) from dual;
```

返回结果如下。 大数据计算服务

```
+------+
| _c0  |
+------+
| [4, 5, 6] |
+------+
```

使用兼容Hive的UDF需要注意以下几点：

**说明**

创建UDF时需要指定JAR包，无法自动将所有JAR包加入Classpath。MaxCompute的 `add` 执行SQL语句时，需要在SQL前加 set odps.sql.hive.compatible=true; 语句，然后和 SQL语句一起提交执行。 需要注意MaxCompute的Java沙箱限制。

#### Python UDF

##### 使用前提

**操作说明**

使用Python UDF前，要求您在Project上必须打开isolation沙箱，设置路径为：adminconsole上的**project****设置** **> ISOLATION SETTING > odps.isolation.enable**，需要设置为True。

**说明**

Python UDF功能目前仅支持MaxCompute伏羲（sp44内核）版本使用。统一调度（sp52内核）版本暂不支持，如需使用请提交工单申请。

##### 使用限制

**限制说明**

MaxCompute Python UDF的Python版本为2.7，并以沙箱模式执行用户代码，即代码是在一个受限的运行环境中执行的。在该环境中，以下行为会被禁止： 读写本地文件。 启动子进程。 启动线程。 使用Socket通信。 其他系统调用。 基于上述原因，您上传的代码都必须通过标准Python实现，禁止C扩展模块。

**可用模块**

此外，Python的标准库中涉及到上述功能的模块都会被禁止。具体标准库的可用模块说明如下： 所有标准Python实现（不依赖扩展模块）的模块都可用。 大数据计算服务 C实现的扩展模块中下列模块可用。 audioop _bisect cmath _codecs_cn _codecs_hk _codecs_iso2022 _codecs_jp _codecs_kr _codecs_tw _collections cStringIO _functools future_builtins _hashlib _heapq itertools _json _locale _lsprof math _md5 _multibytecodec operator _random _sha256 _sha512 _sha strop time unicodedata _weakref cPickle 部分模块功能受限。例如沙箱限制了您的代码最多能往标准输出和标准错误输出写出数据的大小为20 KB，即 `sys.stdout/sys.stderr` 最多能写20 KB，多余的字符会被忽略。 大数据计算服务

##### 第三方库

###### 使用说明

运行环境中还安装了除标准库以外比较常用的三方库，作为标准库的补充，例如Numpy。

**警告**

使用第三方库存在限制，例如禁止本地访问、网络I/O受限，因此第三方库中涉及到相关功能的API也是禁止的。

##### 参数与返回值类型

**使用方式**

参数与返回值的指定方式如下。

```
@odps.udf.annotate(signature)
```

###### 使用说明

Python UDF支持的MaxCompute SQL数据类型包括BIGINT、STRING、DOUBLE、BOOLEAN、 DATETIME、DECIMAL、复杂数据类型（ARRAY、MAP和STRUCT）和复杂数据类型嵌套。在执行SQL语句前，必须确定所有函数的参数类型和返回值类型，因此对于Python这一动态类型语言，需要通过对UDF 类加Decorator的方式指定函数签名。 函数签名Signature通过字符串指定，命令格式如下。

```
arg_type_list '->' type_list arg_type_list: type_list | '*' | '' | 'char(n)' | 'varchar(n)' type_list: [type_list ','] type type: 'bigint' | 'string' | 'double' | 'boolean' | 'datetime' | 'float' | 'binary' | 'd ate' | 'decimal' | 'decimal(precision,scale)'
```

**说明**

箭头左边表示参数类型，右边表示返回值类型。 只有UDTF的返回值可以是多列，UDF和UDAF只能返回一列。 星号（*）代表变长参数。使用变长参数时，UDF、UDTF和UDAF可以匹配任意输入参数。 如果项目空间使用2.0数据类型版本，**decimal**可以设置precision和scale。 返回值暂不支持CHAR和VARCHAR类型。

##### 使用示例

合法的函数签名Signature示例如下。 大数据计算服务 `'bigint,double->string' #` 参数类型为`BIGINT`、`DOUBLE`，返回值类型为`STRING`。 `'bigint,boolean->string,datetime' # UDTF`参数类型为`BIGINT`、`BOOLEAN`，返回值类型为`STRING`，`DATE` `TIME`。 `'*->string' #` 变长参数，输入参数类型任意，返回值类型为`STRING`。 `'->double' #` 参数为空，返回值类型为`DOUBLE`。 `'array<bigint>->struct<x:string, y:int>' #` 参数类型为`ARRAY<BIGINT>`，返回值类型为`STRUCT<x:ST`

```
RING, y:BIGINT>。
```

`'->map<bigint, string>' #` 参数为空，返回值类型为`MAP<INT, STRING>`。

**数据类型**

查询语义解析阶段会检查不符合函数签名的用法，并返回错误，禁止执行此函数。执行时，UDF函数的参数会以函数签名指定的类型传入。返回值类型也要与函数签名指定的类型一致，否则检查到类型不匹配时也会

| MaxCompute SQL Type | Python Type |
|---|---|
| BIGINT | INT |
| STRING | STR |
| DOUBLE | FLOAT |
| BOOLEAN | BOOL |
| DATETIME | INT |
| FLOAT | FLOAT |
| CHAR | STR |
| VARCHAR | STR |
| BINARY | BYTEARRAY |
| DATE | INT |
| DECIMAL | DECIMAL.DECIMAL |
| ARRAY | LIST |
| MAP | DICT |

大数据计算服务

| STRUCT | COLLECTIONS.NAMEDTUPLE |
|---|---|

**说明**

DATETIME类型对应的Python类型是INT，值为Epoch UTC Time起至今的毫秒数。您可以通过Python标准库中的DATETIME模块处理日期时间类型。 `odps.udf.int(value,[silent=True])` 增加了参数**silent**。当**silent**为True时，如果**value**无法转为INT，则会返回None（不会返回异常）。 NULL值对应Python里的None。

##### UDF

本文为您介绍Python UDF中的自定义标量值函数（User Defined Scalar Function），并提供参考示例。

##### 使用示例

定义一个New-style Class，通过**evaluate**方法，即可实现Python UDF。

```python
from odps.udf import annotate @annotate("bigint,bigint->bigint") class MyPlus(object):
    def evaluate(self, arg0, arg1):
        if None in (arg0, arg1):
            return None
        return arg0 + arg1
```

**说明**

##### UDAF

本文为您介绍Python UDF中的自定义聚合函数（User Defined Aggregation Function），并提供参考示例。

###### 使用说明

| 类/方法 | 功能介绍 |
|---|---|
| class odps.udf.BaseUDAF | 继承此类实现Python UDAF。 |
| BaseUDAF.new buffer() _ | 返回聚合函数的中间值的buffer。buffer必须是Marshal对象（例如LIST、 DICT），并且buffer的大小不应该随数据量递增。在极限情况下，buffer在执行对象序列化后的大小不应该超过2 MB。 |

大数据计算服务

| BaseUDAF.iterate(buffer[, args, ...]) | 将args聚合到中间值buffer中。 |
|---|---|
| BaseUDAF.merge(buffer, pbuffer) | 将两个中间值buffer聚合到一起，即将pbuffer合并到buffer中。 |
| BaseUDAF.terminate(buffer ) | 将中间值buffer转换为MaxCompute SQL的基本类型。 |

##### 使用示例

使用UDAF计算平均值的示例如下。

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

本文为您介绍Python UDF中的自定义表值函数（User Defined Table Valued Function），并提供参考示例。

###### 使用说明

| 类/方法 | 功能介绍 |
|---|---|
| class odps.udf.BaseUDTF | Python UDTF的基类。您可以继承此类实现process或close等方法。 |

大数据计算服务

| BaseUDTF. init () __ __ | 初始化方法。继承类如果需要实现此方法，必须在一开始调用基类的初始化方法super(BaseUDTF, self). init ()。init方法在整个UDTF生命周期中 __ __ 只会被调用一次，即在处理第一条记录之前。当UDTF需要保存内部状态时， 可以通过此方法初始化所有状态。 |
|---|---|
| BaseUDTF.process([args, ...]) | 此方法由MaxCompute SQL框架调用，SQL中每一条记录都会调用一次process，process的参数为SQL语句中指定的UDTF输入参数。 |
| BaseUDTF.forward([args, ...]) | UDTF的输出方法。此方法由用户代码调用。每调用一次forward，便会输出一条记录。forward的参数为SQL语句中指定的UDTF的输出参数。 |
| BaseUDTF.close() | UDTF的结束方法。此方法由MaxCompute SQL框架调用，并且只会被调用一次，即在处理完最后一条记录之后被调用。 |

##### 使用示例

```bash
# coding:utf-8
from odps.udf import annotate from odps.udf import BaseUDTF @annotate('string -> string') class Explode(BaseUDTF):
```

# 将`string`按逗号分隔输出成多条记录。

```python
    def process(self, arg):
        for p in props:
            self.forward(p)
```

**说明**

Python UDTF可以不通过**annotate**指定参数类型和返回值类型。这样，在SQL中使用函数时可以匹配任意输入参数，但无法推导返回值类型，所有输出参数都将被视为STRING类型。因此在调用**forward**时，必须将所有输出值转换为STRING类型。

##### 引用资源

**操作说明**

Python UDF可以通过**odps.distcache**模块引用资源文件，支持引用文件资源和表资源。

**引用文件资源**

**语法信息**

大数据计算服务 `--` 返回指定名字的资源内容。

**参数说明**

**resource_name**，STRING类型，对应当前项目空间中已存在的资源名。如果资源名非法或者没有相
应的资源，则会返回异常。

**返回值**

返回值为File-like对象。在使用完此对象后，您需要调用 `close` 方法释放打开的资源文件。

##### 使用示例

```python
from odps.udf import annotate from odps.distcache import get_cache_file @annotate('bigint->string') class DistCacheExample(object):
    def __init__(self):
        cache_file = get_cache_file('test_distcache.txt')
        kv = {}
        for line in cache_file:
            line = line.strip()
            if not line:
                continue
            kv[int(k)] = v
        cache_file.close()
        self.kv = kv
    def evaluate(self, arg):
        return self.kv.get(arg)
```

**引用表资源**

**语法信息**

**参数说明**

**resource_name**，STRING类型，对应当前Project中已存在的资源表名。如果资源名非法或者没有相
应的资源，会返回异常。

**返回值**

返回值为GENERATOR类型，调用者通过遍历获取表的内容，每次遍历可得到以数组形式存在的表中的一条记录。

##### 使用示例

大数据计算服务

```python
from odps.udf import annotate @annotate('->string') class DistCacheTableExample(object):
    def __init__(self):
        self.ln = len(self.records)
    def evaluate(self):
        if self.counter > self.ln - 1:
            return None
        return str(ret)
```

#### Python 3 UDF

本文为您介绍使用Python 3编写UDF函数时的注意事项。

##### 背景信息

由于Python 2官方即将停止维护，因此MaxCompute支持Python 3。MaxCompute使用的Python 3版本为CPython-3.7.3。

##### 使用限制

Python 3与Python 2不兼容。由于在一个SQL作业中，只能选定Python 3或Python 2版本来执行，所以在您使用Python 3之前，需要考虑兼容性问题，在一个SQL里不允许同时使用Python 3和Python 2。

**开启Python 3**

只有作业级别支持Python 3。您在通过Python 3执行SQL语句时，增加如下命令，即可开启Python 3。

```
SET odps.sql.python.version=cp37;
```

##### 第三方库

MaxCompute Python UDF支持第三方库，Python 2运行环境中安装了第三方库Numpy，作为标准库的补充。 MaxCompute内置的Python 3运行环境中未安装第三方库Numpy。如果您需要使用Numpy的UDF，请手动上传Numpy的WHEEL包。从PyPI下载Numpy包时，包的文件名为**numpy-<****版本号****>-cp37-**
**cp37m-manylinux1_x86_64.whl**。

**Python 2 UDF迁移**

Python 2官方即将停止维护，建议您根据项目类型执行迁移操作： 全新项目：适用于新项目空间，或者第一次使用Python编写UDF的项目空间。建议所有的Python UDF 都直接使用Python 3编写。 存量项目：适用于使用了大量Python 2 UDF的项目空间，请您谨慎开启Python 3。因为在一个SQL中不允许同时使用Python 3和Python 2 。如果您计划逐步将所有Python 2 UDF迁移成Python 3 UDF，推荐如下方法： 大数据计算服务新作业和新UDF：使用Python 3编写，设置作业级别开启Python 3。 Python 2 UDF：改写Python 2 UDF，使其可以同时兼容Python 2和Python 3。改写方法请参见将 Python 2代码移植到Python 3。

**说明**

如果您需要编写公共UDF，并为多个项目空间授权，建议同时兼容Python 2和Python 3。

#### SQL Function

##### 背景信息

代码中通常会存在很多相似部分，维护不方便，且容易出错。如果引入UDF并编写代码后，您还需要进行代码编译（Java）、创建资源和创建函数操作，过程比较繁琐，且性能不如内建函数。示例如下。

```
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key1')), 'default') AS key1,
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key2')), 'default') AS key2,
    ...
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.keyN')), 'default') AS keyN
FROM t;
```

使用类似Java中Lambda表达式的功能，把函数作为参数传给另一个函数。

##### 功能介绍

SQL Function作为一种用户自定义函数，弥补了系统只能用Java或Python创建UDF的不足，还扩展了函数类型的参数和匿名函数特性，提升表达业务逻辑的灵活性。您可以通过该函数实现简单功能，提高代码复用率。具体功能如下： 支持在SQL脚本中使用SQL定义的UDF，并调用UDF。 支持函数类型的参数，调用时可以传入内置函数、UDF或SQL语言定义函数。 函数类型的参数可以为匿名函数，调用时可以传入匿名函数。

**命令格式**

创建永久SQL Function并存入Meta系统后，所有的查询操作都可以引用该函数。引用SQL Function需

```
CREATE SQL FUNCTION function_name(@parameter_in1 datatype[, @parameter_in2 datatype.. .]) [RETURNS @parameter_out datatype] AS [BEGIN] [END];
```

**参数说明**

**function_name**：新建SQL语言定义函数的名称。函数名称需要唯一，同名函数只能注册一次，不
能与系统内建函数同名。
**parameter_in**：函数的输入参数。
大数据计算服务
**RETURNS**：函数返回值变量。如果不指定，默认返回function_name的同名变量。
**parameter_out**：函数返回参数。

##### 使用示例

```
CREATE SQL FUNCTION my_add(@a BIGINT) AS @a + 1;
```

**@a + 1**为函数实现逻辑，可直接写为表达式，支持内置操作符、内建函数和UDF。
如果逻辑复杂，可以在定义中使用BEGIN和END，内部可以编写多条语句。RETURNS指定返回值变量，

```
CREATE SQL FUNCTION my_sum(@a BIGINT, @b BIGINT, @c BIGINT) RETURNS @my_sum BIGINT AS BEGIN
    @temp := @a + @b;
    @my_sum := @temp + @c;
END;
```

查询SQL Function的方式与Java UDF或Python UDF保持一致。示例如下。

```
DESC FUNCTION my_add;
```

删除SQL Function的方式与Java UDF或Python UDF保持一致。示例如下。

```
DROP FUNCTION my_add; SELECT my_sum(col1, col2 ,col3) FROM t;
```

如果您不需要把SQL Function存入MaxCompute的Meta系统，可以使用临时SQL Function。临时SQL

```
FUNCTION my_add(@a BIGINT) AS @a + 1; SELECT my_add(key), my_add(value) FROM src;
```

**支持函数类型参数**

支持函数类型的参数，SQL Function调用时可以传入内置函数、UDF或SQL语言定义函数。示例如下。 大数据计算服务

```
FUNCTION ADD(@a BIGINT) AS @a + 1; FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, ADD), OP(key, ABS) FROM VALUES (1),(2) AS t (key);
```

`--` 返回结果

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| 2          | 1          |
| 3          | 2          |
+------------+------------+
```

示例中，函数OP定义了2个输入参数。**@a**定义一个BIGINT类型数值；**@fun**定义一个函数，输入和输出均为BIGINT类型。函数OP将**@a**传入**@fun**函数，并传入ADD和ABS函数，对**@a**进行操作。

**支持匿名函数**

函数类型的参数可以为匿名函数，SQL Function调用时可以传入匿名函数。示例如下。

```
FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, FUNCTION (@a) AS @a + 1) FROM VALUES (1),(2) AS t (key);
```

示例中，**FUNCTION (@a) AS @a + 1**为匿名函数。匿名参数的输入参数**@a**不需要指定类型，编译器会根据OP函数的参数定义推导**@a**的类型。

#### Embedded UDF

##### 背景信息

**产生背景**

您可以通过MaxCompute的Embedded UDF解决以下代码实现过程繁琐，且不方便阅读和维护的问题： 创建UDF并完成代码开发后，您还需要完成代码编译（Java）、创建资源和创建函数操作，过程比较繁琐。 SQL脚本中如果包含UDF，您无法直接查看实现逻辑，或无法获取到JAR包的源码，维护不方便。 通过UDT使用Java库函数时，您需要编写长代码将Java代码写为表达式，阅读和维护不方便。另外还会存在Java代码无法写为表达式的问题，命令示例如下。

```
Foo f = new Foo(); f.execute(); f.getResult();
```

##### 功能介绍

###### 使用说明

Embedded UDF支持将Java或Python代码嵌入SQL脚本。Janino-compiler编译器会识别并提取嵌入的代码，完成代码编译（Java）、动态生成资源和创建临时函数操作。 大数据计算服务 Embedded UDF允许您将SQL脚本和第三方代码放入同一个源码文件，减少使用UDT或UDF的操作步骤，方便日常开发。

##### 使用限制

**限制说明**

嵌入式Java代码使用Janino-compiler编译器进行编译，且支持的Java语法只是标准Java JDK的一个子集。 嵌入式Java代码使用限制包含但不限于以下内容： 不支持Lambda表达式。 不支持Catch多种Exception类型，例如**catch(Exception1 | Exception2 e)**。 不支持泛型的自动推导，例如**Map map = new HashMap<>();**。 类型参数的推导会被忽略，必须显示Cast，例如**(String) myMap.get(key)**。 Assert会强制开启，不受JVM参数-ea控制。 不支持Java 8以上（不包含Java 8）版本的语言功能。

##### 使用示例

**UDT引用嵌入式代码**

`s,`

```java
FROM VALUES ('abc123def'),('apple') AS t(s);
#CODE ('lang'='JAVA')
package com.mypackage; import java.util.regex.Matcher; import java.util.regex.Pattern; public class Foo {
  final static Pattern compile = Pattern.compile(".*?([0-9]+).*");
  public static String extractNumber(String input) {
    final Matcher m = compile.matcher(input);
    if (m.find()) {
      return m.group(1);
    }
    return null;
  }
}
#END CODE;
```

大数据计算服务

**说明**

**#CODE**和**#END CODE**：表示嵌入式代码的开始和结束位置。位于脚本末尾的嵌入式代码块
作用域为整个脚本。
**'lang'='JAVA'**：表示嵌入式代码为Java代码。还支持**PYTHON**。

**Java代码嵌入式UDF**

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA')
package com.mypackage; import com.aliyun.odps.udf.UDF;
  public String evaluate(String input) {
    if (input == null) return null;
    StringBuilder ret = new StringBuilder();
      ret.append(input.toCharArray()[i]);
    }
    return ret.toString();
  }
}
#END CODE;
SELECT foo('abdc');
```

**说明**

嵌入式代码块可以置于**USING**后或脚本末尾，置于**USING**后的代码块作用域仅为 `CREATE` `CREATE TEMPORARY FUNCTION` 创建的函数为临时函数，仅在本次执行生效，不会存入 MaxCompute的Meta系统。

**Java代码嵌入式UDTF**

大数据计算服务

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA', 'filename'='embedded.jar')
package com.mypackage; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve({"string->string,string"})
  @Override
  public void process(Object[] objects) throws UDFException {
    String str = (String) objects[0];
    String[] split = str.split(",");
    forward(split[0], split[1]);
  }
}
#END CODE;
SELECT foo('ab,dc') AS (a,b);
```

**说明**

由于**@Resolve**返回值要求为**string[]**，但Janino-compiler编译器无法将**"string-**
**>string,string"**识别为**string[]**，**@Resolve**注解的参数需要加大括号（{}），为嵌入式代码特有
内容。用普通方式创建Java UDTF时可省略大括号（{}）。

**Python代码嵌入式UDF**

```python
CREATE TEMPORARY FUNCTION foo AS 'embedded.UDFTest' USING
#CODE ('lang'='PYTHON', 'filename'='embedded')
from odps.udf import annotate @annotate("bigint->bigint") class UDFTest(object):
  def evaluate(self, a):
    return a * a
#END CODE;
SELECT foo(4);
```

**说明**

Python代码的缩进需要符合Python语言规范。 由于注册Python UDF时**AS**后的类名需要包含Python源码的文件名，您可以通过 `'filename'='embedded'` 指定一个虚拟文件名。

### UDT

大数据计算服务

#### 使用场景及使用限制

##### 背景信息

MaxCompute基于新一代的SQL引擎推出新功能UDT（User Defined Type）。MaxCompute的UDT功能允许您在SQL中直接调用第三方语言的类（使用其方法）、或直接使用第三方对象获取其数据内容。

**适用场景**

MaxCompute没有提供，但可以使用其它语言简单实现的功能。 例如，只需调用一次Java内置类的方法即可实现，但MaxCompute却没有提供简单的方法实现的功能。 如果使用UDF实现，整个过程会过于繁杂。 SQL中需要调用第三方库实现相关功能。希望能够在SQL中直接调用，而不需要再Wrap一层UDF。 SQL中需要直接调用第三方语言源代码。SELECT TRANSFORM语法支持把脚本写到SQL语句中，提升可读性和代码易维护性。但是某些语言无法这样使用，例如Java源代码必须经过编译才能执行，通过UDT 功能将这些语言也可以直接写入SQL中。

##### 使用限制

**说明**

目前Runtime使用的JDK版本是JDK1.8，可能不支持更新版本的JDK。 UDT不能用作Shuffle Key：包括Join、Group By、Distribute By、Sort By、Order By和Cluster By 等结构的Key。 DDL不支持UDT，也不能将UDT对象Insert到表中，屏显的最终结果也不能是UDT类型。

#### 功能介绍

本文为您介绍UDT的功能并提供参考示例。

###### 使用说明

很多SQL引擎中UDT与MaxCompute的复杂类型STRUCT类似，相比之下，MaxCompute中的UDT与 Create Type的概念更类似，Type中包含数据域和方法。MaxCompute不需要用特殊的DDL语法来定义新类型，通过UDT可以在SQL中直接使用新类型。通过如下示例，为您直观地介绍UDT的功能。

##### 使用示例

您可以通过以下两种方式，在SQL中调用 `java.lang` 包。

**UDT方式**

通过UDT功能在SQL语句中直接调用java.lang。 `--`打开新类型，因为下面的操作会用到`INTEGER`，即`INT`类型。

```
SET odps.sql.type.system.odps2=true; SELECT java.lang.Integer.MAX_VALUE;
```

和Java语言一样，java.lang包可以省略，所以上述示例可以简写为如下语句。 大数据计算服务

```
SET odps.sql.type.system.odps2=true; SELECT Integer.MAX_VALUE;
```

`--` 返回结果

```
+------------+
| max_value  |
+------------+
| 2147483647 |
+------------+
```

**UDF方式**

使用UDF在SQL语句中调用java.lang。
1. 定义一个UDF的类。

```java
package org.alidata.odps.udf.examples; import com.aliyun.odps.udf.UDF; public class IntegerMaxValue extends UDF {
    public Integer evaluate() {
        return Integer.MAX_VALUE;
    }
}
```

2. 将上面的UDF编译，并打成JAR包，然后上传JAR包，并创建Function。

```
ADD jar odps-test.jar; CREATE FUNCTION integer_max_value AS 'com.aliyun.odps.test.IntegerMaxValue' USING 'od ps-test.jar';
```

3. 在SQL中使用。

```
SELECT integer_max_value();
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 2147483647 |
+------------+
```

由上例可以看出，UDT简化了上述一系列的过程，方便您使用其它语言扩展SQL的功能。

#### 实现原理及功能说明

本文为您介绍UDT的实现原理，并提供详细的功能说明。

**实现原理**

**执行过程**

通过以下示例为您介绍UDT的执行过程。 大数据计算服务 `--`示例数据。

```
@table1 := SELECT * FROM VALUES ('100000000000000000000') AS t(x); @table2 := SELECT * FROM VALUES (100L) AS t(y);
```

`--`代码逻辑。 `--new`创建对象。

```
@a := SELECT new java.math.BigInteger(x) x FROM @table1;
```

`--`静态方法调用。

```
@b := SELECT java.math.BigInteger.valueOf(y) y FROM @table2;
```

`--`实例方法调用。

```
SELECT /*+mapjoin(b)*/ x.add(y).toString() FROM @a a JOIN @b b;
```

`--`返回结果

```
+-----------------------+
| _c0                   |
+-----------------------+
| 100000000000000000100 |
+-----------------------+
```

**运行原理**

整个示例的运行过程如下图所示。 该UDT共有三个Stage：M1、R2和J3。如果您熟悉MapReduce原理即可知道，由于**Join**的存在需要做数据Reshuffle，所以会出现多个Stage。通常，不同的Stage是在不同的进程、不同的物理机器上运行的。 大数据计算服务 M1只执行 `new java.math.BigInteger(x)` 操作。 J3在不同阶段执行了 `java.math.BigInteger.valueOf(y)` 和 `x.add(y).toString()` 操作。这几个操作不仅分阶段执行，而且在不同的进程、不同的物理机器上执行。UDT把这个过程封装起来，将这个过程变得看起来和在同一个JVM中执行的效果几乎一样。 从上述示例中，您可以看到子查询的结果允许UDT类型的列。例如上面变量a的x列是**java.math.BigInteger**类型，而不是内置类型。UDT类型的数据可以被带到下一个Operator中，再调用其它方法，甚至可以参与数据Shuffle。

**功能说明**

UDT支持您上传自己的JAR包，并且直接引用。当前提供了一些Flag方便您的使用。
**set odps.sql.session.resources**：指定引用的资源，可以指定多个，用半角逗号（,）隔开。例

**说明**

这个Flag和**select transform**中指定资源的Flag相同，所以这个Flag会同时影响两个功能。

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.resources=odps-test.jar; SELECT new com.aliyun.odps.test.IntegerMaxValue().evaluate();
```

**odps.sql.session.java.imports**：指定默认的Java Package，可以指定多个，用半角逗号（,）
隔开。和Java的**import**语句类似，可以提供完整类路径，例如java.math.BigInteger，也可以使用星号（*）。暂不支持**static import**。

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.resources=odps-test.jar; SET odps.sql.session.java.imports=com.aliyun.odps.test.*;
```

`--` 指定默认的`Package`。

```
SELECT new IntegerMaxValue().evaluate();
```

过 `com.aliyun.odps.udf.impl.UDTExecutionContext.get()` 静态方法获取**ExecutionContext**对象，从而访问当前的**ExecutionContext**，进而访问资源（例如文件资源和表格资源）。 UDT支持的操作： 实例化对象的 `new` 操作。 实例化数组的 `new` 操作，包括使用初始化列表创建数组，例如 `new Integer[] { 1, 2, 3 }` 。 方法调用，包括静态方法调用。

**说明**

UDT中的标识符是大小写敏感的，包括Package、类名、方法名和域名。 暂不支持匿名类和Lambda表达式。 暂不支持无返回值的函数调用（因为UDT均出现在Expression中，没有返回值的函数调用无法嵌入到Expression中）。 UDT支持的数据类型： 大数据计算服务 UDT支持类型转换，支持SQL风格的类型转换，例如 `cast(1 as java.lang.Object)` 。但不支持 Java风格的类型转换，例如 `(Object)1` 。 UDT内置类型与特定Java类型有一一映射关系。 内置类型的数据能够直接调用其映射到的Java类型的方法，例如 `'123'.length() ,`

```
1L.hashCode() 。
```

UDT类型能够直接参与内置函数或者UDF的运算，例如 `chr(Long.valueOf('100'))` ，其中**Long.valueOf**返回的是**java.lang.Long**类型的数据，而内置函数Chr接受的数据类型是内置类型BIGINT。 Java的PRIMITIVE类型可以自动转化为其BOXING类型，并应用前两条规则。

**说明**

部分内置的新数据类型需要先设置 set odps.sql.type.system.odps2=true; 才可使用，否则会报错。 UDT扩展了类型转换规则： UDT对象可以被隐式类型转换为其基类对象。 UDT对象可以被强制类型转换为其基类或子类对象。 没有继承关系的两个对象之间遵守原来的类型转换规则，注意这时可能会导致内容的变化。例如**java.lang.Long**类型的数据是可以强制转换为**java.lang.Integer**的，应用的是内置类型的 BIGINT强制转换为INT的过程，而这个过程会导致数据内容的变化，甚至可能导致精度的损失。 UDT支持比较完整的泛型。例如 `java.util.Arrays.asList(new java.math.BigInteger('1'))` ， 编译器可以根据参数类型判断出该方法的返回值是**java.util.List<java.math.BigInteger>**类型。

**说明**

构造函数需要指定类型参数，否则需要使用**java.lang.Object**，这点和Java保持一致。 STRING的相加操作： `String.valueOf(1) + String.valueOf(2)` 的结果是3（STRING隐式转换为 DOUBLE，并且DOUBLE相加），而不是12（Java中STRING相加是Concatenate的语义）。 在Java语言中，判断相等应该用 `equals()` 方法，而非=操作，在SQL中=是判断相等。 UDT对同一对象的概念是模糊的，这是由数据的Reshuffle导致的。对象有可能会在不同进程、不同物理机器之间传输。在传输过程中，同一个对象可能分别引用了不同的对象（例如对象先被Shuffle到两台机器，然后下次又Shuffle回一起）。所以在使用UDT时，应该使用 `equals()` 方法判断相等，避免使用=判断相等时出现不准确的情况。 某行某列的对象，其内部包含的各个数据对象的相关性是可以保证的。不同行或者不同列的对象的数据相关性是不保证的。 UDT不能用作Shuffle Key，包括Join、Group By、Distribute By、Sort By、Order By和Cluster By 等结构的Key。 UDT可以在Expression中间的任意阶段使用，但不能作为最终输出。 UDT不仅可以实现Scalar函数的功能，配合内置函数COLLECT_SET和EXPLODE，UDT还可以实现

#### 功能优势

大数据计算服务本文为您介绍UDT的功能优势。

##### 功能介绍

功能方面，UDT的优势如下所示。 支持JDK的所有功能，扩展了SQL的能力。 代码可与SQL放于同一文件，便于管理。 可直接使用其它类库，代码重用率高。

#### 性能优势

本文为您介绍UDT的性能优势。

**性能介绍**

性能方面，因为UDT和UDF的执行过程非常接近，所以UDT与UDF的性能几乎一致。优化后的计算引擎使得UDT在特定场景下的性能更高。 UDT对象只有在跨进程时才需要做序列化和反序列化，因此在执行不需要数据Reshuffle的操作（如JOIN 或GGREGATE）时，UDT可节省序列化和反序列化的开销。 因为UDT的Runtime基于Codegen而非反射实现的，所以不存在反射带来的性能损失。在您使用过程中，连续多个UDT操作会合并在一个FunctionCall里一起执行。例如下面的示例中，看似存在调用多次 UDT，实际上只会调用一次UDF。所以，UDT操作的单元虽然较小，却并不会因多次函数调用而造成接口额外开销。

```
values[x].add(values[y]).divide(java.math.BigInteger.valueOf(2))
```

#### 安全优势

本文为您介绍UDT的安全优势。

**安全介绍**

在安全控制方面，UDT和UDF完全一样。即都会受到Java沙箱Policy的限制。因此如果要使用受限的操作， 需要打开沙箱隔离，或者申请沙箱白名单。

#### 更多示例

##### Java数组示例

##### 使用示例

大数据计算服务

```
SET odps.sql.type.system.odps2=true; SET odps.sql.udt.display.tostring=true;
```

`--`创建一个包含`10`个元素的数组。

```
    new Integer[10],
```

`--`通过初始化列表创建一个长度为3的数组。

```
    new Integer[] {c1, c2, c3},
```

`--`创建多维数组。

```
    new Integer[][] { new Integer[] {c1, c2}, new Integer[] {c3, c4} },
```

`--`通过下标操作访问数组元素

```
    new Integer[] {c1, c2, c3} [2],
```

`--`创建一个`List<Integer>`，也能当做`array<int>`来用，是另一种创建内置`ARRAY`数据的方法

```
FROM VALUES (1,2,3,4) AS t(c1, c2, c3, c4);
```

##### JSON示例

#### 使用须知

UDT运行时自带一个JSON的依赖（2.2.4版本），可以直接使用JSON。

**说明**

除JSON外，MaxCompute运行时自带的依赖还包括commons-logging（1.1.1版本）、commonslang（2.5版本）、commons-io（2.4版本）和protobuf-java（2.4.1版本）。

##### 使用示例

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.java.imports=java.util.*,java,com.google.gson.*; --同时导入多个Packa
```

`ge`时用逗号隔开。

```
@a := SELECT new Gson() gson; --构建Gson对象。 gson.toJson(new ArrayList<Integer>(Arrays.asList(1, 2, 3))), --将任意对象转成JSON字符串。 cast(gson.fromJson('["a","b","c"]', List.class) as List<String>) --反序列化JSON字符串，注
```

意`Gson`的接口，直接反序列化后是`List<Object>`类型，这里强制转换成`List<String>`，方便后续使用。

```
FROM @a;
```

返回结果如下。

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| [1,2,3]    | 1          |
+------------+------------+
```

相比于内建函数GET_JSON_OBJECT，该方法不仅使用方便，还会在提取JSON字符串内容时，将JSON字符串反序列化为格式化数据，提升工作效率。 大数据计算服务

##### 复杂类型操作示例

本文提供UDT的复杂类型示例，方便您参考使用。

#### 使用须知

内置类型ARRAY与**java.util.List**、MAP和**java.util.Map**存在映射关系： Java中实现**java.util.List**或**java.util.Map**接口类的对象，都可以参与MaxCompute SQL的复杂类型操作。 MaxCompute中ARRAY或MAP的数据，能够直接调用List或者MAP的接口。

##### 使用示例

```
SET odps.sql.type.system.odps2=true; SET odps.sql.session.java.imports=java.util.*;
```

`size(new ArrayList<Integer>()), --`对`ArrayList`数据调用内置函数`Size`。 `sort_array(new ArrayList<Integer>()), --`对`ArrayList`的数据进行排序。 `Objects.toString(a), --`之前不支持将`ARRAY`类型`Cast`成`STRING`，现在有绕过方法了。

```
FROM (select new ArrayList<Integer>(array(1,2,3)) as al, array(1,2,3) as a) t;
```

返回结果如下。

```
+------------+------------+------------+------------+------------+------------+
| _c0        | _c1        | _c2        | _c3        | _c4        | _c5        |
+------------+------------+------------+------------+------------+------------+
| 0          | 3          | []         | 2          | [1, 2, 3]  | [2]        |
+------------+------------+------------+------------+------------+------------+
```

##### 聚合操作示例

#### 使用须知

UDT实现聚合的原理是，先用内置函数COLLECT_SET或COLLECT_LIST函数将数据转变成List，之后对该 List应用UDT的标量方法计算数据的聚合值。

##### 使用示例

示例如下，计算BigInteger的中位数（由于数据是java.math.BigInteger类型的，所以不能直接用内建函大数据计算服务

```
SET odps.sql.session.java.imports=java.math.*; @test_data := SELECT * FROM VALUES (1),(2),(3),(5) AS t(value); @a := SELECT collect_list(new BigInteger(value)) VALUES FROM @test_data; --先把数据聚合
```

成`List`。

```
@b := SELECT sort_array(values) AS VALUES, values.size() cnt FROM @a; --计算中位数的逻辑
```

，先将数据排序。

```
@c := SELECT if(cnt % 2 == 1, new BigDecimal(values[cnt div 2]), new BigDecimal(values[cnt div 2 - 1].add(values[cnt div 2])).divide(new BigDecimal(2))) med from @b;
```

`--`最终结果。

```
SELECT med.toString() FROM @c;
```

返回结果如下。

```
+------------+
| _c0        |
+------------+
| 2.5        |
+------------+
```

**collect_list**会先将所有数据都收集到一起，无法实现Partial Aggregate，处理效率比内置聚合函数或者
UDAF低，请尽量使用内置聚合函数。同时，把一个Group的所有数据都收集到一起，会增加数据倾斜的风险。 如果UDAF的逻辑是要将所有数据收集到一起（例如类似内置聚合函数WM_CONCAT的功能），使用上述方法，处理效率比UDAF高。

##### 表值函数示例

#### 使用须知

表值函数允许输入多行多列数据，输出多行多列数据。可以按照如下操作实现： 输出多行多列数据，可以用UDT方法输出一个Collection类型的数据（List或者MAP），然后调用 UDT可以包含多个数据域，通过调用不同的Getter方法获取各个域的内容即可展开成多列。

##### 使用示例

示例如下，展开一个JSON字符串的内容。

```
@a := SELECT '[{"a":"1","b":"2"},{"a":"1","b":"2"}]' str; --示例数据。 @b := SELECT new com.google.gson.Gson().fromJson(str, java.util.List.class) l FROM @a;
```

`--`反序列化`JSON`。

```
@c := SELECT cast(e AS java.util.Map<Object,Object>) m FROM @b lateral view explode(l) @d := SELECT m.get('a') AS a, m.get('b') AS b FROM @c; --展开成多列。
```

SELECT a.toString() a, b.toString() b FROM @d; --最终结果输出（注意变量d的输出中a、b两列是 `Object`类型）。 返回结果如下。 大数据计算服务

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

#### UDJ背景介绍

本文为您介绍引入UDJ机制的背景信息。

**背景介绍**

MaxCompute内置了多种Join操作，包括Inner/Right Join、Outer/Left Jion、Outer/Full Join、 Outer/semi/Anti-semi Join等。这些内置的Join操作功能强大，但由于其标准的Join实现，无法满足很多跨表操作的需求场景。 通常，您可以通过UDF（User Defined Function）描述代码框架，但现有的UDF/UDTF/UDAF接口主要是针对在单个数据表上的操作而设计。一旦涉及多表的自定义操作，经常还需要依赖于内置Join +各种 UDF/UDTF，并配合比较复杂的SQL语句来完成。在多表操作的场景上，您不得不放弃SQL而使用自定义 MapReduce，才能完成所需的计算。 无论是Join +各种UDF/UDTF+复杂SQL还是自定义MapReduce门槛都比较高，同时还会带来一些问题： 使用Join +各种UDF/UDTF+复杂SQL：多个复杂的Join和散布在SQL语言各处的代码揉合在一起，将带来多处的逻辑黑盒，不利于生成最优的执行计划。 使用MapReduce：不仅更大程度上限制了系统进行执行优化的可能性，而且在深度优化本地运行代码时，由于MapReduce绝大部分代码由Java完成，在执行效率上会远低于MaxCompute基于LLVM的代码生成器。 针对上述问题，基于MaxCompute 2.0计算引擎，MaxCompute在UDF框架中新近引入的一种新扩展机制 UDJ（User Defined Join），来实现灵活的跨表、多表自定义操作，同时减少通过MapReduce等方式对分布式系统底层细节的操作。

#### UDJ使用示例

##### UDJ跨表Join功能

本文为您介绍UDJ的跨表Join功能，并提供参考示例。

###### 使用说明

**测试数据**

假设存在两个日志表，分别是payment和user_client_log。 payment：表中保存了用户的支付记录，一笔支付记录包含用户ID、支付时间和支付内容。样例数据如下。

| user id _ | time | pay info _ |
|---|---|---|

大数据计算服务

| 2656199 | 2018-02-13 22:30:00 | gZhvdySOQb |
|---|---|---|
| 8881237 | 2018-02-13 08:30:00 | pYvotuLDIT |
| 8881237 | 2018-02-13 10:32:00 | KBuMzRpsko |

user_client_log：保存了用户的客户端日志，每一条日志包含了用户ID、日志时间和日志内容。样例数据如下。

| user id _ | time | content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL |

**验证目标**

对于每一条客户端日志，找出该用户在payment表里时间最接近的一条支付记录，将其中的支付内容和日志内容合并输出。达到如下效果。

| user id _ | time | content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn, pay pYvotuLDIT |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL, pay pYvotuLDIT |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL, pay KBuMzRpsko |

##### 使用示例

面对此类需求通常使用UDJ方法实现。
1. 注册UDJ函数。
i. 配置新版本的SDK。

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-udf</artifactId>
  <version>0.30.8-public</version>
</dependency>
```

大数据计算服务 ii. 编写UDJ代码，并将代码打包为odps-udj-example.jar。

```java
package com.aliyun.odps.udf.example.udj; import com.aliyun.odps.Column; import com.aliyun.odps.OdpsType; import com.aliyun.odps.Yieldable; import com.aliyun.odps.data.ArrayRecord; import com.aliyun.odps.data.Record; import com.aliyun.odps.udf.DataAttributes; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDJ; import com.aliyun.odps.udf.annotation.Resolve; import java.util.ArrayList; import java.util.Iterator; /**
```

* 对于右表的每个记录，找到最近的左表记录
* 合并两条记录。
`*/`

```java
@Resolve("->string,bigint,string") public class PayUserLogMergeJoin extends UDJ {
    private Record outputRecord;
    /**
```

* 将在数据处理阶段之前调用。用户可以实施这个方法做初始化工作。
`*/`

```java
    @Override
    public void setup(ExecutionContext executionContext, DataAttributes
dataAttributes) {
```

`//`

```
                new Column("user_id", OdpsType.STRING),
                new Column("time", OdpsType.BIGINT),
                new Column("content", OdpsType.STRING)
        });
    }
```

`/**` 重写此方法以实现连接逻辑。 `* @param key` 当前连接键。 `* @param left` 左表对应当前键的记录组。 `* @param right` 对应当前键的右表记录组。 `* @param output` 用于输出`UDJ`的结果。 `*/`

```java
    @Override
    public void join(Record key, Iterator<Record> left, Iterator<Record> right, Yie
ldable<Record> output) {
        outputRecord.setString(0, key.getString(0));
        if (!right.hasNext()) {
```

`//` 空右组，什么都不做。

```
            return;
        } else if (!left.hasNext()) {
```

`//` 空左组。输出右侧组的所有记录而不合并。

```
            while (right.hasNext()) {
RecordlogRecord=rightnext();
```

大数据计算服务

```
                Record logRecord = right.next();
                outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
                outputRecord.setString(2, logRecord.getString(1));
                output.yield(outputRecord);
            }
            return;
        }
        ArrayList<Record> pays = new ArrayList<>();
```

`//` 左侧记录组将从开始到结束迭代。 `//` 对于右组的每个记录，迭代器无法重置。

```
        left.forEachRemaining(pay -> pays.add(pay.clone()));
        while (right.hasNext()) {
            Record log = right.next();
            long logTime = log.getDatetime(0).getTime();
            long minDelta = Long.MAX_VALUE;
            Record nearestPay = null;
```

`//` 迭代左边的所有记录，找到有的记录时间上的微小差异。

```
            for (Record pay : pays) {
                long delta = Math.abs(logTime - pay.getDatetime(0).getTime());
                if (delta < minDelta) {
                    minDelta = delta;
                    nearestPay = pay;
                }
            }
```

`//` 将日志记录与最近的支付记录合并，并输出到结果。

```java
            outputRecord.setBigint(1, log.getDatetime(0).getTime());
            outputRecord.setString(2, mergeLog(nearestPay.getString(1),
log.getString(1)));
            output.yield(outputRecord);
        }
    }
    String mergeLog(String payInfo, String logContent) {
        return logContent + ", pay " + payInfo;
    }
    @Override
    public void close() {
    }
}
```

iii. 在MaxCompute中添加JAR包资源。

```
ADD jar odps-udj-example.jar;
```

iv. 在MaxCompute中注册UDJ函数pay_user_log_merge_join。

```
'com.aliyun.odps.udf.example.udj.PayUserLogMergeJoin' USING 'odps-udj-example.jar';
```

2. 准备示例数据。
大数据计算服务 i. 创建示例表payment和user_client_log。

```
CREATE TABLE payment(user_id string,time datetime,pay_info string); CREATE TABLE user_client_log(user_id string,time datetime,content string);
```

ii. 为示例表中插入数据。 `--`向`payment`表中插入数据。

```
('1335656', datetime '2018-02-13 19:54:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 12:21:00', 'pYvotuLDIT'), ('2656199', datetime '2018-02-13 20:50:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 22:30:00', 'gZhvdySOQb'), ('8881237', datetime '2018-02-13 08:30:00', 'pYvotuLDIT'), ('8881237', datetime '2018-02-13 10:32:00', 'KBuMzRpsko'), ('9890100', datetime '2018-02-13 16:01:00', 'gZhvdySOQb'), ('9890100', datetime '2018-02-13 16:26:00', 'MxONdLckwa') ;
```

`--`向`user_client_log`表中插入数据。

```
('1000235', datetime '2018-02-13 00:25:36', 'click FNOXAibRjkIaQPB'), ('1000235', datetime '2018-02-13 22:30:00', 'click GczrYaxvkiPultZ'), ('1335656', datetime '2018-02-13 18:30:00', 'click MxONdLckpAFUHRS'), ('1335656', datetime '2018-02-13 19:54:00', 'click mKRPGOciFDyzTgM'), ('2656199', datetime '2018-02-13 08:30:00', 'click CZwafHsbJOPNitL'), ('2656199', datetime '2018-02-13 09:14:00', 'click nYHJqIpjevkKToy'), ('2656199', datetime '2018-02-13 21:05:00', 'click gbAfPCwrGXvEjpI'), ('2656199', datetime '2018-02-13 21:08:00', 'click dhpZyWMuGjBOTJP'), ('2656199', datetime '2018-02-13 22:29:00', 'click bAsxnUdDhvfqaBr'), ('2656199', datetime '2018-02-13 22:30:00', 'click XIhZdLaOocQRmrY'), ('4356142', datetime '2018-02-13 18:30:00', 'click DYqShmGbIoWKier'), ('4356142', datetime '2018-02-13 19:54:00', 'click DYqShmGbIoWKier'), ('8881237', datetime '2018-02-13 00:30:00', 'click MpkvilgWSmhUuPn'), ('8881237', datetime '2018-02-13 06:14:00', 'click OkTYNUHMqZzlDyL'), ('8881237', datetime '2018-02-13 10:30:00', 'click OkTYNUHMqZzlDyL'), ('9890100', datetime '2018-02-13 16:01:00', 'click vOTQfBFjcgXisYU'), ('9890100', datetime '2018-02-13 16:20:00', 'click WxaLgOCcVEvhiFJ') ;
```

3. 在SQL中使用UDJ函数。

```
    r.user_id,
    from_unixtime(CAST(time / 1000 AS BIGINT)) AS time,
    content
FROM (
    SELECT user_id, time, pay_info FROM payment
) p JOIN (
    SELECT user_id, time, content FROM user_client_log
) u ON p.user_id = u.user_id USING pay_user_log_merge_join(p.time, p.pay_info, u.time, u.content) r AS (user_id, time, content);
```

大数据计算服务

**说明**

USING子句中的参数说明：
**pay_user_log_merge_join**：是注册的UDJ在SQL中的函数名。
**(p.time, p.pay_info, u.time, u.content)**：是UDJ中用到的左右表的列。
r：是UDJ结果的别名，方便其他地方引用UDJ的结果。
**(user_id, time, content)**：是UDJ产生的结果的列名。
返回结果如下。

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

##### UDJ预排序

本文为您介绍UDJ的预排序功能，并提供参考示例。

###### 使用说明

为了找到payment值相差最小的一条记录，需要反复对payment表的数据进行iterator遍历。所以事先将相同user_id的payment记录全部加载到了ArrayList，当同一个用户一天之内的支付行为比较少时，这个方法可用。在其它场景中，有时同组内的数据量可能非常大，大到无法在内存中存放，此时就需要通过其他方式解决。此时，您可以通过SORT BY预排序解决。 当某个用户的支付数据量非常大，导致无法将payment放在内存中时，如果组内所有数据如果已经按照时间排序，则只需要比较两边iterator最顶部的数据，就可以实现这个功能。

##### 使用示例

该方式主要是使用SORT BY子句对UDJ的数据进行预排序。在这个过程中，最多只需要同时缓存3条记录， 就可以实现和之前算法的相同的功能。示例代码如下。 大数据计算服务

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
    }
    return;
  }
  long prevDelta = Long.MAX_VALUE;
  Record logRecord = right.next();
  Record payRecord = left.next();
  Record lastPayRecord = payRecord.clone();
  while (true) {
payRecord.getDatetime(0).getTime();
    if (left.hasNext() && delta > 0) {
```

`//`两个记录之间的时间差正在减少，我们仍然可以操作。 `//`探索左侧组以尝试获得更小的增量。

```
      lastPayRecord = payRecord.clone();
      prevDelta = delta;
      payRecord = left.next();
    } else {
```

`//`到达最小`delta`点。检查最后的记录， `//`输出合并结果并准备处理下一条记录。 `//`右组。

```
      Record nearestPay = Math.abs(delta) < prevDelta ? payRecord : lastPayRecord;
      outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
      String mergedString = mergeLog(nearestPay.getString(1), logRecord.getString(1));
      outputRecord.setString(2, mergedString);
      output.yield(outputRecord);
      if (right.hasNext()) {
        logRecord = right.next();
        prevDelta = Math.abs(
          logRecord.getDatetime(0).getTime() - lastPayRecord.getDatetime(0).getTime()
        );
      } else {
        break;
      }
    }
  }
}
```

#### 性能优势

本文为您介绍UDJ的性能优势。 大数据计算服务

**性能对比**

下面通过一个真实的线上MapReduce作业进行测试验证UDJ的性能，该MapReduce作业实现一套比较复杂的算法。将两个表合并在一起，用UDJ对该MapReduce进行改写，并且验证UDJ实现结果的正确性。在并发度相同的情况下，两者性能对比如下。 UDJ接口的引入，可以让您能更方便地描述对多表数据进行操作的复杂逻辑，同时大幅提升了性能（如上图可见）。代码只在UDJ内被调用，其上下游的逻辑（例如这个例子中的整个Mapper逻辑）则完全通过 MaxCompute高效的Native运行完成。在Java代码中，由于MaxCompute UDJ运行引擎和Java接口之间的数据交互逻辑有深度的优化，通过UDJ实现的Join逻辑也比其对等的Reducer更高效。

### 参数化视图

#### 使用须知

MaxCompute传统的视图（VIEW）中，底层封装一段逻辑复杂的SQL脚本，调用者可以像读普通表一样调用视图，无需关心底层的实现。传统的视图实现了一定程度的封装与重用，因此被广泛地使用。但是传统的视图并不接受调用者传递的任何参数（例如调用者无法对视图读取的底层表进行数据过滤或传递其他参数），导致代码重用能力低下。MaxCompute当前的SQL引擎支持带参数的视图，支持传入任意表或者其它变量，定制视图的行为。

**视图语法**

创建带参数的视图的语法如下。

```
-- view with parameters -- param @b -a string parameter -- returns a table with schema (key STRING,value STRING) CREATE VIEW IF NOT EXISTS pv1(@a table (k STRING,v BIGINT), @b STRING)
```

`AS`

```
SELECT srcp.key,srcp.value FROM srcp JOIN @a ON srcp.key=a.k AND srcp.p=@b;
```

**语法说明**

创建的视图pv1有两个参数，即表参数和STRING参数，参数可以是任意的表或者基本数据类型。 大数据计算服务支持使用子查询作为参数的值，例如 `SELECT * FROM view_name( (SELECT 1 FROM src WHERE a >`

```
0), 1); 。
```

定义视图时，您可以为参数指定ANY类型，表示任意数据类型。例如 `CREATE VIEW paramed_view`

```
(@a ANY) AS SELECT * FROM src WHERE CASE WHEN @a IS NULL THEN key1 ELSE key2 END =
```

key3; ，定义了视图的第一个参数可以接受任意类型。 但是ANY类型不能参与类似+、**AND**需要明确类型才能执行的运算。ANY类型通常用在TABLE参数中作为PassThrough列，示例如下。

```
CREATE VIEW paramed_view (@a TABLE(name STRING, id ANY, age BIGINT)) AS SELECT * FR OM @a WHERE name = 'foo' AND age < 25;
```

`--`调用示例。

```
SELECT * FROM paramed_view((SELECT name, id, age FROM students));
```

**说明**

使用 `CREATE VIEW` 创建视图后，可以执行 `DESC` 命令获取视图的描述。此描述中包含视图的返回类型信息。 视图的返回类型是在调用时重新推算的，它可能与创建视图时不一致，例如ANY类型。 定义视图时，Table值参数还支持使用星号（*）表示任意多个列。星号（*）可以指定数据类型，也可以使用ANY类型，示例如下。

```
CREATE VIEW param_view (@a TABLE(key STRING, * ANY), @b TABLE(key STRING, * STRING) ) AS SELECT a.* FROM @a JOIN @b ON a.key = b.key;
```

`--` 调用示例。

```
SELECT name, address FROM param_view((SELECT school, name, age, address FROM studen t), school) WHERE age < 20;
```

示例中的视图接受两个表值参数。第一个表值参数第一列是STRING类型，后面可以是任意多个任意类型的列；第二个表值参数的第一列是STRING类型，后面可以是任意多个STRING类型的列。注意事项如下： 变长部分必须写在表值参数定义语句的最后位置，即在星号（*）的后面不允许再出现其它列。因此，一个表值参数中最多只有一个变长列列表。 由于变长部分必须写在表值参数定义语句的最后位置，有时输入表的列不一定是按照这种顺序排列的，这时需要重排输入表的列，可以以子查询作为参数（参考上述示例），子查询外面必须加一层括号。 因为表值参数中变长部分没有名字，所以在视图定义过程中无法获得对这部分数据的引用，也无法对这些数据做运算。 虽然无法对变长部分做运算，但可以使用**SELECT ***这种通配符将变长部分的列传递出去。 表值参数的列与定义视图时指定的定长列部分不一定会完全一致。如果名字不一致，编译器会自动做重命名；如果类型不一致，编译器会做隐式转换（不能隐式转换时，会发生报错）。 调用已经定义的pv1视图的示例如下。 大数据计算服务

```
@a := SELECT * FROM src WHERE value >0; @b := SELECT * FROM pv1(@a,'20170101'); @another_day := '20170102'; @c := SELECT * FROM pv1(src2, @another_day); @d := SELECT * FROM @c UNION ALL SELECT * FROM @b; WITH t AS(SELECT * FROM src3) SELECT * FROM @c SELECT * FROM @d SELECT * FROM pv1(t,@another_day);
```

**说明**

您可以使用不同的参数调用pv1： 表参数可以是物理表、VIEW、表变量或者CTE中的表别名。 普通参数可以是变量或者常量。 参数化视图中，脚本中只能使用DML语句，不能使用INSERT或CREATE TABLE语句，也不能使用屏幕显示语句。

```
-- view with parameters -- param @b -a string parameter -- returns a table with schema (key string,value string) CREATE VIEW IF NOT EXISTS pv2(@a TABLE (k STRING,v BIGINT), @b STRING) AS BEGIN @srcp := SELECT * FROM srcp WHERE p=@b; @pv2 := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k; END;
```

**说明**

BEGIN到END之间的语句，就是这个视图的脚本。 `@pv2 :=...` 语句相当于其它语言中的RETURN 语句，用于向一个与视图同名的隐含表变量赋值。 在视图参数匹配时，实参和形参匹配的规则和普通的弱类型语言一样，如果传入的视图参数可以被隐式转换，则可与所定义的参数匹配。例如，BIGINT的值可以匹配DOUBLE类型的参数。对于表变量，如果表a 的Schema可以被用于插入到表b中，则意味着表a可以用来匹配和表b的Schema相同的表类型参数。 您可以明确地声明返回类型，以提升代码的可读性。 大数据计算服务

```
CREATE VIEW IF NOT EXISTS pv3(@a table (k STRING,v BIGINT), @b STRING)
```

`AS`

```
BEGIN
    @srcp := SELECT * FROM srcp WHERE p=@b;
    @ret := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k;
end;
```

**说明**

返回类型为**TABLE (x STRING,y STRING)** ，即返回给调用者的类型，可以在此处定制表的Schema。 返回参数为**@ret**，为它赋值的操作会在视图的脚本中进行，此处相当于定义了返回的参数名。 您可以将没有**BEGIN/END**和返回变量的视图，看作是此形式的简化形式。

### CLONE TABLE

CLONE TABLE可以复制表数据到另一个表中，极大地提高了数据迁移的效率。本文介绍如何使用CLONE

##### 使用限制

目标表与源表的Schema需要兼容。 支持分区表和非分区表，暂不支持对Hash CluteredTable使用CLONE TABLE命令进行复制。 目标表已存在时，一次性复制分区的数量上限为10000个。 目标表不存在时，无分区数量限制，满足原子性。 对同一个非分区表或者分区表的同一个分区，执行CLONE TABLE命令的次数不能超过7次。

**操作说明**

###### 使用说明

将源表src_table_name中的数据复制到目标表desc_table_name中。将数据复制到目标表之后，建议您执行数据验证（例如，执行SELECT COUNT命令查看表的行数、执行DESC命令查看表大小）以确保复制后数据的准确性。

**函数语法**

```
CLONE TABLE <[src_project_name.]src_table_name> [PARTITION(spec), ...] [IF EXISTS (OVERWRITE | IGNORE)];
```

**参数说明**

`src_project_name` ：选填，源表所在项目空间名称。不指定时，默认为当前项目空间。 大数据计算服务当目标表不存在时，CLONE TABLE会创建目标表（创建目标表使用的是CREATE TABLE LIKE语义）。 当目标表已存在并指定IF EXISTS OVERWRITE，则覆盖目标表对应分区的数据。 当目标表已存在并指定IF EXISTS IGNORE，则跳过已存在分区，不覆盖目标表已有分区的数据。 `dest_project_name` ：选填，目标表所在项目空间名称。不指定时，默认为当前项目空间。

**返回值**

无。

##### 使用示例

i. 准备示例数据为便于理解命令的使用方法，本文提供源数据。创建源表并添加数据，命令示例如下： `--` 创建非分区表

```
    key STRING,
); INSERT INTO src_copy VALUES ('1', 'ok');
```

`--` 创建分区表

```
    key STRING,
) PARTITIONED BY (ds STRING, hr STRING); INSERT INTO srcpart_copy PARTITION (ds = '2008-04-09', hr = '11') VALUES ('1', 'ok4 9'); INSERT INTO srcpart_copy PARTITION (ds = '2008-04-08', hr = '12') VALUES ('1', 'ok4 8');
```

ii. 操作示例 `--` 示例1：全量复制非分区表`src_copy`的数据至目标表`src_clone`

```
CLONE TABLE src_copy TO src_clone;
```

`--` 验证数据准确性

```
SELECT * FROM src_clone;
```

`--` 返回结果

```
+-----+-------+ +-----+-------+
| 1   | ok    |
+-----+-------+
```

`--` 示例2：复制分区表`srcpart_copy`指定分区的数据至目标表`srcpart_clone`

```
CLONE TABLE srcpart_copy PARTITION(ds = '2008-04-09', hr = '11') TO srcpart_clone I F EXISTS OVERWRITE;
```

`--` 验证数据准确性大数据计算服务验数据准确性

```
SELECT * FROM srcpart_clone;
```

`--` 返回结果

```
+-----+-------+------------+----+ +-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
+-----+-------+------------+----+
```

`--` 示例3：全量复制分区表并跳过目标表中已存在的分区

```
CLONE TABLE srcpart_copy TO srcpart_clone IF EXISTS IGNORE;
```

`--` 验证数据准确性

```
SELECT * FROM srcpart_clone;
```

`--` 返回结果

```
+-----+-------+------------+----+ +-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
| 1   | ok48  | 2008-04-08 | 12 |
+-----+-------+------------+----+
```

`--` 示例4：全量复制分区表至目标表`srcpart_clone2`

```
CLONE TABLE srcpart_copy TO srcpart_clone2;
```

`--` 验证数据准确性

```
SELECT * FROM srcpart_clone2;
```

`--` 返回结果

```
+-----+-------+------------+----+ +-----+-------+------------+----+
| 1   | ok49  | 2008-04-09 | 11 |
| 1   | ok48  | 2008-04-08 | 12 |
+-----+-------+------------+----+
```

### 地理函数

#### 使用须知

地理空间函数通过一套JAVA UDF函数集，支持用户直接在MaxCompute上进行空间几何计算。使用地理函数前，您需要了解如下使用前提。

**地理函数介绍**

地理函数的应用需要丰富的领域知识，同时，Esri开源了一套支持简单几何计算的Hive UDF（详情请参见spatial-framework-for-hadoop），MaxCompute支持使用Hive UDF，因此在此基础上进行了二次开发，扩充了球面函数、网格函数和索引的功能。函数名称基本与PostGIS保持一致，降低了用户的学习成本。主要支持如下： 提供符合OpenGIS标准的空间几何对象模型，支持以WKT和WKB等形式输入和输出ST_Point、 ST_MultiPoint、ST_LineString、ST_MultiLineString、ST_Polygon和ST_MultiPolygon等空间几何对象。 大数据计算服务提供一系列基于以上对象模型的处理函数，包括构造对象、测试几何关系、获取几何对象属性，计算平面/球面测量值（面积或距离等）。 提供一系列索引函数，如GeoHash、S2、RTree等，来优化Spatial Join场景。 地理函数所采用的算法均基于开源技术，其中spatial-sdk-odps.jar也是对开源资源的封装，因此用户可以免费使用。由于采用了开源算法封装，MaxCompute无法对外部能力进行控制或提供支持，因此不对UDF 的业务、性能和准确性等提供解释、维护或技术支持。如遇问题，用户可以基于开源实现进行比对测试、错误修复或替换。因此，该功能仅适合对开源地理函数有深入了解的用户使用。

**安装地理函数**

您可以根据以下步骤安装地理函数，并在项目中使用。
1. 下载已编译好的3个JAR包。
单击Spatial JAR下载Spatial JAR包，并将包名重命名为 `spatial-sdk-hive.jar` 。 单击esri-geometry-api下载Esri Geometry JAR包，并将包名重命名为 `esri-geometry-`

```
api.jar 。
```

获取spatial-sdk-odps.jar包。
2. 使用MaxCompute客户端（odpscmd）登录，在安装地理函数的项目中，执行以下脚本上传JAR包并安
装函数。函数可以在项目内使用，或者通过跨项目授权方式，授权用户在其他项目中使用。

```
ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar; CREATE FUNCTION ST_Aggr_ConvexHull AS 'com.esri.hadoop.hive.ST_Aggr_ConvexHull' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; 'com.esri.hadoop.hive.ST_Aggr_Intersection' USING 'spatial-sdk-hive.jar,esri-geomet ry-api.jar'; CREATE FUNCTION ST_Aggr_Union AS 'com.esri.hadoop.hive.ST_Aggr_Union' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Area AS 'com.esri.hadoop.hive.ST_Area' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsBinary AS 'com.esri.hadoop.hive.ST_AsBinary' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsGeoJson AS 'com.esri.hadoop.hive.ST_AsGeoJson' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsJson AS 'com.esri.hadoop.hive.ST_AsJson' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsShape AS 'com.esri.hadoop.hive.ST_AsShape' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_AsText AS 'com.esri.hadoop.hive.ST_AsText' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Bin AS 'com.esri.hadoop.hive.ST_Bin' USING 'spatial-sdk-hive.jar ,esri-geometry-api.jar'; CREATE FUNCTION ST_BinEnvelope AS 'com.esri.hadoop.hive.ST_BinEnvelope' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Boundary AS 'com.esri.hadoop.hive.ST_Boundary' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Buffer AS 'com.esri.hadoop.hive.ST_Buffer' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Centroid AS 'com.esri.hadoop.hive.ST_Centroid' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; USING'spatial
```

大数据计算服务

```
CREATE FUNCTION ST_Contains AS 'com.esri.hadoop.hive.ST_Contains' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_ConvexHull AS 'com.esri.hadoop.hive.ST_ConvexHull' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_CoordDim AS 'com.esri.hadoop.hive.ST_CoordDim' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Crosses AS 'com.esri.hadoop.hive.ST_Crosses' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Difference AS 'com.esri.hadoop.hive.ST_Difference' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Dimension AS 'com.esri.hadoop.hive.ST_Dimension' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Disjoint AS 'com.esri.hadoop.hive.ST_Disjoint' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Distance AS 'com.esri.hadoop.hive.ST_Distance' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_EndPoint AS 'com.esri.hadoop.hive.ST_EndPoint' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Envelope AS 'com.esri.hadoop.hive.ST_Envelope' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_EnvIntersects AS 'com.esri.hadoop.hive.ST_EnvIntersects' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Equals AS 'com.esri.hadoop.hive.ST_Equals' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_ExteriorRing AS 'com.esri.hadoop.hive.ST_ExteriorRing' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; 'com.esri.hadoop.hive.ST_GeodesicLengthWGS84' USING 'spatial-sdk-hive.jar,esri-geomet ry-api.jar'; CREATE FUNCTION ST_GeomCollection AS 'com.esri.hadoop.hive.ST_GeomCollection' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Geometry AS 'com.esri.hadoop.hive.ST_Geometry' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeometryN AS 'com.esri.hadoop.hive.ST_GeometryN' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeometryType AS 'com.esri.hadoop.hive.ST_GeometryType' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromGeoJson AS 'com.esri.hadoop.hive.ST_GeomFromGeoJson' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromJson AS 'com.esri.hadoop.hive.ST_GeomFromJson' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromShape AS 'com.esri.hadoop.hive.ST_GeomFromShape' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromText AS 'com.esri.hadoop.hive.ST_GeomFromText' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromWKB AS 'com.esri.hadoop.hive.ST_GeomFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_InteriorRingN AS 'com.esri.hadoop.hive.ST_InteriorRingN' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersection AS 'com.esri.hadoop.hive.ST_Intersection' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersects AS 'com.esri.hadoop.hive.ST_Intersects' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Is3D AS 'com.esri.hadoop.hive.ST_Is3D' USING 'spatial-sdk-hive jar,esri-geometry-apijar';
```

大数据计算服务

```
.jar,esrigeometryapi.jar; CREATE FUNCTION ST_IsClosed AS 'com.esri.hadoop.hive.ST_IsClosed' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsEmpty AS 'com.esri.hadoop.hive.ST_IsEmpty' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsMeasured AS 'com.esri.hadoop.hive.ST_IsMeasured' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsRing AS 'com.esri.hadoop.hive.ST_IsRing' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_IsSimple AS 'com.esri.hadoop.hive.ST_IsSimple' USING 'spatialsdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Length AS 'com.esri.hadoop.hive.ST_Length' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_LineFromWKB AS 'com.esri.hadoop.hive.ST_LineFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_LineString AS 'com.esri.hadoop.hive.ST_LineString' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_M AS 'com.esri.hadoop.hive.ST_M' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxM AS 'com.esri.hadoop.hive.ST_MaxM' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxX AS 'com.esri.hadoop.hive.ST_MaxX' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxY AS 'com.esri.hadoop.hive.ST_MaxY' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxZ AS 'com.esri.hadoop.hive.ST_MaxZ' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinM AS 'com.esri.hadoop.hive.ST_MinM' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinX AS 'com.esri.hadoop.hive.ST_MinX' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinY AS 'com.esri.hadoop.hive.ST_MinY' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MinZ AS 'com.esri.hadoop.hive.ST_MinZ' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MLineFromWKB AS 'com.esri.hadoop.hive.ST_MLineFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPointFromWKB AS 'com.esri.hadoop.hive.ST_MPointFromWKB' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPolyFromWKB AS 'com.esri.hadoop.hive.ST_MPolyFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiLineString AS 'com.esri.hadoop.hive.ST_MultiLineString' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiPoint AS 'com.esri.hadoop.hive.ST_MultiPoint' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiPolygon AS 'com.esri.hadoop.hive.ST_MultiPolygon' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumGeometries AS 'com.esri.hadoop.hive.ST_NumGeometries' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumInteriorRing AS 'com.esri.hadoop.hive.ST_NumInteriorRing' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumPoints AS 'com.esri.hadoop.hive.ST_NumPoints' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Overlaps AS 'com.esri.hadoop.hive.ST_Overlaps' USING 'spatialsdk-hive.jar,esri-geometry-api.jar';
```

大数据计算服务 j , g y p j

```
CREATE FUNCTION ST_Point AS 'com.esri.hadoop.hive.ST_Point' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointFromWKB AS 'com.esri.hadoop.hive.ST_PointFromWKB' USING ' spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointN AS 'com.esri.hadoop.hive.ST_PointN' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointZ AS 'com.esri.hadoop.hive.ST_PointZ' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PolyFromWKB AS 'com.esri.hadoop.hive.ST_PolyFromWKB' USING 'spat ial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Polygon AS 'com.esri.hadoop.hive.ST_Polygon' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Relate AS 'com.esri.hadoop.hive.ST_Relate' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SetSRID AS 'com.esri.hadoop.hive.ST_SetSRID' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SRID AS 'com.esri.hadoop.hive.ST_SRID' USING 'spatial-sdk-hive .jar,esri-geometry-api.jar'; CREATE FUNCTION ST_StartPoint AS 'com.esri.hadoop.hive.ST_StartPoint' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_SymmetricDiff AS 'com.esri.hadoop.hive.ST_SymmetricDiff' USI NG 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Touches AS 'com.esri.hadoop.hive.ST_Touches' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Union AS 'com.esri.hadoop.hive.ST_Union' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Within AS 'com.esri.hadoop.hive.ST_Within' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_X AS 'com.esri.hadoop.hive.ST_X' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Y AS 'com.esri.hadoop.hive.ST_Y' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Z AS 'com.esri.hadoop.hive.ST_Z' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHash' USI NG 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.geohash.ST_PointFromGeoHash' USING 'spatial-sdk-odps. jar'; 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHashNeighbours' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.geohash.ST_EnvelopeFromGeoHash' USING 'spatial-sdk-od ps.jar'; CREATE FUNCTION ST_AreaWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_AreaWGS84' USING 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_BufferWGS84' USING 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_DistanceWGS84' USING 'spatial-sdk-odps.jar ';
```

大数据计算服务

```
'com.aliyun.odps.geospatial.udf.compute.ST_GeodesicDistance' USING 'spatial-sdk-odps. jar'; CREATE FUNCTION ST_Transform AS 'com.aliyun.odps.geospatial.udf.compute.ST_Transform' USING 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_TransformWGS84' USING 'spatial-sdk-odps.ja r'; CREATE FUNCTION ST_IsValid AS 'com.aliyun.odps.geospatial.udf.compute.ST_IsValid' USI NG 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellCenterPoint' USING 'spatial-sdk-odps.ja r'; 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromGeom' USING 'spatial-sdk-odps.ja r'; 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromText' USING 'spatial-sdk-odps.ja r'; 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellNeighbours' USING 'spatial-sdk-odps.ja r'; 'com.aliyun.odps.geospatial.udf.compute.ST_Area_Sphere' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_Distance_Sphere' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_BuildRTreeIndex' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_ContainsFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_CrossesFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_EqualsFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_IntersectsFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_OverlapsFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_TouchesFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_WithinFromRTree' USING 'spatial-sdk-odps .jar'; 'com.aliyun.odps.geospatial.udf.index.ST_KNNFromRTree' USING 'spatial-sdk-odps
```

大数据计算服务

```
.jar'; CREATE FUNCTION ST_Simplify AS 'com.aliyun.odps.geospatial.udf.compute.ST_Simplify' USING 'spatial-sdk-odps.jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyVW' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_SimplifyPreserveTopology AS 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyPreserveTopology' USING 'spatial-s dk-odps.jar'; 'com.aliyun.odps.geospatial.udf.compute.ST_LineLocatePoint' USING 'spatial-sdk-odps.j ar';
```

如果是进行bugfix或者版本升级，请在编译后将JAR包名称更改为与上述一致，再通过odpscmd替换JAR 包即可，命令如下。

```
DROP resource esri-geometry-api.jar; DROP resource spatial-sdk-hive.jar; DROP resource spatial-sdk-odps.jar; ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar;
```

在使用这些函数的SQL前，请一并提交如下Flag，其中isolation是为UDF的运行提供安全隔离环境。

```
SET odps.sql.hive.compatible=true; SET odps.sql.udf.java.retain.legacy=false; SET odps.isolation.session.enable=true;
```

**测试验证**

通过MaxCompute客户端提交SQL语句，测试UDF是否可以正常使用。命令示例如下：

```
set odps.sql.hive.compatible=true; select ST_AsText(ST_Point(1, 2));
```

返回结果如下，说明安装成功。

```
+-----+
| _c0 |
+-----+
| POINT (1 2) |
+-----+
```

地理函数使用说明请参见对应的地理函数文档，或参考Esri的开源UDF说明文档UDF-Documentation。

#### Constructors

##### ST_AsBinary

本文为您介绍如何在MaxCompute中使用ST_AsBinary函数，用于返回几何图形的WKB二进制表达式。 大数据计算服务

**操作说明**

###### 使用说明

返回几何图形的WKB二进制表达式。

**函数语法**

```
ST_AsBinary(ST_Geometry);
```

**参数说明**

ST_Geometry：必填，几何图形对象。

**返回值**

返回几何图形的WKB（Well-Known Binary）二进制表达式。

##### 使用示例

```
SELECT ST_AsBinary(ST_Point(1, 2));
```

`--` 返回结果

```
+--------------------------------------------------------------+
| _c0                                                          |
+--------------------------------------------------------------+
| =01=01=00=00=00=00=00=00=00=00=00=F0?=00=00=00=00=00=00=00@  |
+--------------------------------------------------------------+
```

##### ST_AsGeoJson

本文为您介绍如何在MaxCompute中使用ST_AsGeoJson函数，用于返回几何图形的GeoJson表达式。

**操作说明**

###### 使用说明

返回几何图形的GeoJson表达式。

**函数语法**

```
ST_ASGEOJSON(ST_GEOMETRY geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

返回几何图形的GeoJson表达式。

##### 使用示例

```
SELECT ST_ASGEOJSON(ST_POINT(1.0, 2.0));
```

`--` 返回结果

```
+-------------------------------------------------+
| _c0                                             |
+-------------------------------------------------+
| {"type":"Point","coordinates":[1,2],"crs":null} |
+-------------------------------------------------+
```

大数据计算服务

##### ST_AsJson

本文为您介绍如何在MaxCompute中使用ST_ASJSON函数，用于返回几何图形的JSON表达式。

**操作说明**

###### 使用说明

返回几何图形的JSON表达式。

**函数语法**

```
ST_ASJSON(ST_GEOMETRY);
```

**参数说明**

ST_GEOMETRY：必填，几何图形对象。

**返回值**

返回几何图形的JSON表达式。

##### 使用示例

```
SELECT ST_ASJSON(ST_POINT(1.0, 2.0));
```

`--` 返回结果

```
+-----------------------+
| _c0                   |
+-----------------------+
| {"x":1.0,"y":2.0}     |
+-----------------------+ SELECT ST_ASJSON(ST_SETSRID(ST_POINT(1, 1), 4326));
```

`--` 返回结果

```
+-----------------------------------------------------------+
| _c0                                                       |
+-----------------------------------------------------------+
| {"x":1.0,"y":1.0,"spatialReference":{"wkid":4326}}        |
+-----------------------------------------------------------+
```

##### ST_AsShape

本文为您介绍如何在MaxCompute中使用ST_AsShape函数，用于返回几何图形的Esri shape表达式。

**操作说明**

###### 使用说明

返回几何图形的Esri shape表达式。

**函数语法**

```
ST_AsShape(ST_GEOMETRY);
```

**参数说明**

ST_GEOMETRY：必填，几何图形对象。

**返回值**

大数据计算服务返回几何图形的Esri shape表达式。

##### 使用示例

```
SELECT ST_AsShape(ST_POINT(1, 2));
```

##### ST_AsText

本文为您介绍如何在MaxCompute中使用ST_AsText函数，用于返回几何图形的WKT文本表达式。

**操作说明**

###### 使用说明

返回几何图形的WKT文本表达式。

**函数语法**

```
ST_ASTEXT(ST_GEOMETRY);
```

**参数说明**

ST_GEOMETRY：必填，几何图形对象。

**返回值**

返回几何图形的WKT（Well-Known Text）文本表达式。

##### 使用示例

```
SELECT ST_ASTEXT(ST_POINT(1, 2));
```

`--` 返回结果

```
+-------------+
| _c0         |
+-------------+
| POINT (1 2) |
+-------------+
```

##### ST_GeomCollection

本文为您介绍如何在MaxCompute中使用ST_GeomCollection函数，用于使用OGC的WKT文本表达式构建多部分的几何图形。

**操作说明**

###### 使用说明

使用OGC（开放地理空间信息联盟）的WKT文本表达式构建多部分的几何图形。MaxCompute上的

**函数语法**

```
ST_GeomCollection(STRING wkt);
```

**参数说明**

wkt：必填，STRING类型，OGC的WKT文本表达式。

**返回值**

返回多部分的几何图形对象。 大数据计算服务

##### 使用示例

```
SELECT ST_GeomCollection('MULTIPOINT ((1 0), (2 3))');
```

`--` 以下用法不支持（收集功能）

##### ST_GeomFromGeoJson

本文为您介绍如何在MaxCompute中使用ST_GeomFromGeoJson函数，用于使用GeoJSON表达式构建一个几何图形。

**操作说明**

###### 使用说明

使用GeoJSON表达式构建一个几何图形。

**函数语法**

```
ST_GeomFromGeoJson(STRING json);
```

**参数说明**

json：必填，STRING类型，GeoJSON表达式。

**返回值**

返回几何图形对象。

##### 使用示例

```
SELECT ST_GeomFromGeoJson('{"type":"Point", "coordinates":[1.2, 2.4]}'); SELECT ST_GeomFromGeoJson('{"type":"LineString", "coordinates":[[1,2], [3,4]]}');
```

##### ST_GeomFromJSON

本文为您介绍如何在MaxCompute中使用ST_GeomFromJSON函数，用于使用Esri JSON表达式构建一个几何图形。

**操作说明**

###### 使用说明

使用Esri JSON表达式构建一个几何图形。

**函数语法**

```
ST_GeomFromJSON(STRING json);
```

**参数说明**

json：必填，STRING类型，Esri JSON表达式。

**返回值**

返回几何图形对象。

##### 使用示例

大数据计算服务

```
SELECT ST_GeomFromJSON('{"x":0.0,"y":0.0}');
```

##### ST_GeomFromShape

本文为您介绍如何在MaxCompute中使用ST_GeomFromShape函数，用于使用Esri shape表达式构建一个几何图形。

**操作说明**

###### 使用说明

使用Esri shape表达式构建一个几何图形。

**函数语法**

```
ST_GeomFromShape(shape);
```

**参数说明**

shape：必填，Esri shape表达式。

**返回值**

返回几何图形对象。

##### 使用示例

```
SELECT ST_GeomFromShape(ST_AsShape(ST_Point(1, 2)));
```

##### ST_GeomFromText

本文为您介绍如何在MaxCompute中使用ST_GeomFromText函数，用于使用OGC WKT文本表达式构建一个几何图形。

**操作说明**

###### 使用说明

使用OGC WKT文本表达式构建一个几何图形。

**函数语法**

```
ST_GeomFromText(STRING wkt);
```

**参数说明**

wkt：必填，STRING类型，OGC WKT文本表达式。

**返回值**

返回几何图形对象。

##### 使用示例

```
SELECT ST_GeomFromText('linestring (1 0, 2 3)'); SELECT ST_GeomFromText('multipoint ((1 0), (2 3))');
```

##### ST_GeomFromWKB

大数据计算服务本文为您介绍如何在MaxCompute中使用ST_GeomFromWKB函数，用于使用OGC WKB表达式构建一个几何图形。

**操作说明**

###### 使用说明

使用OGC WKB表达式构建一个几何图形。

**函数语法**

```
ST_GeomFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

返回几何图形对象。

##### 使用示例

```
SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)'))); SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))')));
```

##### ST_GeometryType

本文为您介绍如何在MaxCompute中使用ST_GeometryType函数，用于返回几何图形的类型。

**操作说明**

###### 使用说明

返回几何图形的类型。

**函数语法**

```
ST_GeometryType(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

STRING类型，返回几何图形的类型名称（如ST_Point、ST_LineString、ST_Polygon等）。

##### 使用示例

大数据计算服务

```
SELECT ST_GeometryType(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+----------+
| _c0      |
+----------+ +----------+ SELECT ST_GeometryType(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+---------------+
| _c0           |
+---------------+ +---------------+ SELECT ST_GeometryType(ST_Polygon(2, 0, 2, 3, 3, 0));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+ +------------+
```

##### ST_LineString

本文为您介绍如何在MaxCompute中使用ST_LineString函数，用于构建二维直线。

**操作说明**

###### 使用说明

用来构建二维直线。

**函数语法**

```
ST_LineString(x, y, [x, y]*); ST_LineString('linestring( ... )'); ST_LineString(ARRAY(x+), ARRAY(y+)); ST_LineString(ARRAY(ST_Point(x,y)+));
```

**参数说明**

x, y：必填，DOUBLE类型，点的坐标值。 linestring( ... )：必填，STRING类型，WKT格式的linestring表达式。

**返回值**

##### 使用示例

大数据计算服务 `--` 通过坐标值构建

```
SELECT ST_LineString(1, 1, 2, 2, 3, 3);
```

`--` 通过`WKT`表达式构建

```
SELECT ST_LineString('linestring(1 1, 2 2, 3 3)');
```

`--` 通过坐标数组构建

```
SELECT ST_LineString(ARRAY(1, 2, 3), ARRAY(1, 2, 3)); SELECT ST_LineString(ARRAY(ST_Point(1, 1), ST_Point(2, 2), ST_Point(3, 3)));
```

##### ST_LineFromWKB

本文为您介绍如何在MaxCompute中使用ST_LineFromWKB函数，用于使用OGC well-known binary文本格式构建一个二维直线。

**操作说明**

###### 使用说明

使用OGC well-known binary文本格式构建一个二维直线。

**函数语法**

```
ST_LineFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

```
SELECT ST_LineFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)')));
```

##### ST_MultiLineString

本文为您介绍如何在MaxCompute中使用ST_MultiLineString函数，用于构建二维多线条。

**操作说明**

###### 使用说明

用来构建二维多线条。

**函数语法**

```
ST_MultiLineString(ARRAY(x1, y1, x2, y2, ...), ARRAY(x1, y1, x2, y2, ...), ...); ST_MultiLineString('multilinestring( ... )');
```

**参数说明**

multilinestring( ... )：必填，STRING类型，WKT格式的multilinestring表达式。

**返回值**

大数据计算服务

##### 使用示例

`--` 通过坐标数组构建二维多线条

```
SELECT ST_MultiLineString(ARRAY(1, 1, 2, 2), ARRAY(10, 10, 20, 20));
```

`--` 通过`WKT`表达式构建二维多线条

```
SELECT ST_MultiLineString('multilinestring ((1 1, 2 2), (10 10, 20 20))');
```

##### ST_MLineFromWKB

本文为您介绍如何在MaxCompute中使用ST_MLineFromWKB函数，用于使用OGC WKB二进制格式表达式构建二维多线条。

**操作说明**

###### 使用说明

使用OGC WKB二进制格式表达式构建二维多线条。

**函数语法**

```
ST_MLineFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

`--` 构建二维多线条

```
SELECT ST_MLineFromWKB(ST_AsBinary(ST_GeomFromText('multilinestring ((1 0, 2 3), (5 7 , 7 5))')));
```

##### ST_MultiPoint

本文为您介绍如何在MaxCompute中使用ST_MultiPoint函数，用于构建多点几何。

**操作说明**

###### 使用说明

用来构建多点几何。

**函数语法**

```
ST_MultiPoint(x1, y1, x2, y2, x3, y3); ST_MultiPoint('multipoint( ... )');
```

**参数说明**

x1, y1, x2, y2, ...：必填，DOUBLE类型，各点的坐标值。 multipoint( ... )：必填，STRING类型，WKT格式的multipoint表达式。

**返回值**

##### 使用示例

大数据计算服务 `--` 通过坐标值构建3个点

```
SELECT ST_MultiPoint(1, 1, 2, 2, 3, 3);
```

`--` 通过`WKT`表达式构建2个点

```
SELECT ST_MultiPoint('MULTIPOINT ((10 40), (40 30))');
```

##### ST_MPointFromWKB

本文为您介绍如何在MaxCompute中使用ST_MPointFromWKB函数，用于使用OGC WKB二进制格式表达式构建二维多点。

**操作说明**

###### 使用说明

使用OGC WKB二进制格式表达式构建二维多点。

**函数语法**

```
ST_MPointFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

```
SELECT ST_MPointFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))')));
```

##### ST_MultiPolygon

本文为您介绍如何在MaxCompute中使用ST_MultiPolygon函数，用于构建二维多边形。

**操作说明**

###### 使用说明

用来构建二维多边形。

**函数语法**

```
ST_MultiPolygon(ARRAY(x1, y1, x2, y2, ...), ARRAY(x1, y1, x2, y2, ...), ...); ST_MultiPolygon('multipolygon ( ... )');
```

**参数说明**

multipolygon ( ... )：必填，STRING类型，WKT格式的multipolygon表达式。

**返回值**

##### 使用示例

大数据计算服务

```
SELECT ST_MultiPolygon(ARRAY(1, 1, 1, 2, 2, 2, 2, 1), ARRAY(3, 3, 3, 4, 4, 4, 4, 3)); SELECT ST_MultiPolygon('multipolygon (((0 0, 0 1, 1 0, 0 0)), ((2 2, 2 3, 3 2, 2 2))) ');
```

##### ST_MPolyFromWKB

本文为您介绍如何在MaxCompute中使用ST_MPolyFromWKB函数，用于使用OGC WKB二进制格式表达式构建二维多边形。

**操作说明**

###### 使用说明

使用OGC WKB二进制格式表达式构建二维多边形。

**函数语法**

```
ST_MPolyFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

```
SELECT ST_MPolyFromWKB(ST_AsBinary(ST_GeomFromText('multipolygon (((0 0, 1 0, 0 1, 0 0)), ((2 2, 1 2, 2 1, 2 2)))')));
```

##### ST_Point

**操作说明**

###### 使用说明

用来构建二维点。

**函数语法**

```
ST_Point(DOUBLE x, DOUBLE y); ST_Point(STRING 'point (x y)');
```

**参数说明**

x, y：必填，DOUBLE类型，点的坐标值。 point (x y)：必填，STRING类型，WKT格式的point表达式。

**返回值**

##### 使用示例

大数据计算服务 `--` 通过坐标值构建二维点

```
SELECT ST_Point(1, 2);
```

`--` 通过`WKT`表达式构建二维点

```
SELECT ST_Point('point (0 0)');
```

##### ST_PointFromWKB

本文为您介绍如何在MaxCompute中使用ST_PointFromWKB函数，用于使用OGC well-known binary 二进制表达式构建二维点。

**操作说明**

###### 使用说明

使用OGC well-known binary二进制表达式构建二维点。

**函数语法**

```
ST_PointFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

```
SELECT ST_PointFromWKB(ST_AsBinary(ST_GeomFromText('point (1 0)')));
```

##### ST_PointZ

本文为您介绍如何在MaxCompute中使用ST_PointZ函数，用于构建三维点。

**操作说明**

###### 使用说明

用来构建三维点。

**函数语法**

```
ST_PointZ(DOUBLE x, DOUBLE y, DOUBLE z);
```

**参数说明**

x：必填，DOUBLE类型，点的X坐标值。 y：必填，DOUBLE类型，点的Y坐标值。 z：必填，DOUBLE类型，点的Z坐标值。

**返回值**

##### 使用示例

`--` 构建三维点

```
SELECT ST_PointZ(1, 2, 3);
```

大数据计算服务

##### ST_Polygon

本文为您介绍如何在MaxCompute中使用ST_Polygon函数，用于构建二维多边形。

**操作说明**

###### 使用说明

用来构建二维多边形。

**函数语法**

```
ST_Polygon(DOUBLE x, DOUBLE y, [DOUBLE x, DOUBLE y]*); ST_Polygon(STRING 'polygon( ... )');
```

**参数说明**

x, y：必填，DOUBLE类型，多边形各顶点的坐标值。 polygon( ... )：必填，STRING类型，WKT格式的polygon表达式。

**返回值**

##### 使用示例

`--` 通过坐标值构建一个正方形

```
SELECT ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1);
```

`--` 通过`WKT`表达式构建一个三角形

```
SELECT ST_Polygon('polygon ((1 1, 4 1, 1 4, 1 1))');
```

##### ST_PolyFromWKB

本文为您介绍如何在MaxCompute中使用ST_PolyFromWKB函数，用于使用OGC well-known binary二进制表达式构建二维多边形。

**操作说明**

###### 使用说明

使用OGC well-known binary二进制表达式构建二维多边形。

**函数语法**

```
ST_PolyFromWKB(BINARY wkb);
```

**参数说明**

wkb：必填，BINARY类型，OGC WKB表达式。

**返回值**

##### 使用示例

```
SELECT ST_PolyFromWKB(ST_AsBinary(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))') ));
```

大数据计算服务

##### ST_SetSRID

本文为您介绍如何在MaxCompute中使用ST_SetSRID函数，用于设置几何图形的SRID。

**操作说明**

###### 使用说明

设置几何图形的SRID。

**函数语法**

```
ST_SetSRID(ST_Geometry, SRID);
```

**参数说明**

ST_Geometry：必填，几何图形对象。 SRID：必填，BIGINT类型，空间参考标识符。

**返回值**

返回设置了SRID的几何图形对象。

##### 使用示例

```
SELECT ST_SetSRID(ST_Point(1.5, 2.5), 4326);
```

#### Accessors

##### ST_Area

本文为您介绍如何在MaxCompute中使用ST_Area函数，用于返回一个多边形或多个多边形的面积。

**操作说明**

###### 使用说明

返回一个多边形或多个多边形的面积。

**函数语法**

```
ST_Area(ST_Polygon);
```

**参数说明**

**返回值**

DOUBLE类型，返回多边形的面积。

##### 使用示例

```
SELECT ST_Area(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 9.0        |
+------------+
```

大数据计算服务

##### ST_Centroid

本文为您介绍如何在MaxCompute中使用ST_Centroid函数，用于返回多边形的最小外接矩形的中心点。

**操作说明**

###### 使用说明

返回多边形的最小外接矩形的中心点。

**函数语法**

```
ST_Centroid(ST_Polygon polygon);
```

**参数说明**

**返回值**

##### 使用示例

```
SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 3 6, 6 0, 0 0))')); SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 0 8, 8 0, 0 0))'));
```

##### ST_CoordDim

本文为您介绍如何在MaxCompute中使用ST_CoordDim函数，用于返回坐标点的坐标系维度数。

**操作说明**

###### 使用说明

返回坐标点的坐标系维度数。

**函数语法**

```
ST_CoordDim(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

BIGINT类型，返回坐标点的坐标系维度数（2、3或4）。

##### 使用示例

大数据计算服务 `--` 二维点

```
SELECT ST_CoordDim(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

`--` 三维点

```
SELECT ST_CoordDim(ST_PointZ(1.5, 2.5, 3));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3    |
+------+
```

`--` 四维点

```
SELECT ST_CoordDim(ST_Point(1.5, 2.5, 3., 4.));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 4    |
+------+
```

##### ST_Dimension

本文为您介绍如何在MaxCompute中使用ST_Dimension函数，用于返回几何图形的空间维数。

**操作说明**

###### 使用说明

返回几何图形的空间维数。

**函数语法**

```
ST_Dimension(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

BIGINT类型，返回几何图形的空间维数（0表示点，1表示线，2表示面）。

##### 使用示例

大数据计算服务

```
SELECT ST_Dimension(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+
```

`--` 线的空间维数

```
SELECT ST_Dimension(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+
```

`--` 面的空间维数

```
SELECT ST_Dimension(ST_Polygon(2, 0, 2, 3, 3, 0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

##### ST_Distance

本文为您介绍如何在MaxCompute中使用ST_Distance函数，用于返回2个几何图形之间的距离。

**操作说明**

###### 使用说明

返回2个几何图形之间的距离。

**函数语法**

```
ST_Distance(ST_Geometry, ST_Geometry);
```

**参数说明**

ST_Geometry1：必填，第一个几何图形对象。 ST_Geometry2：必填，第二个几何图形对象。

**返回值**

DOUBLE类型，返回2个几何图形之间的距离。

##### 使用示例

大数据计算服务

```
SELECT ST_Distance(ST_Point(0.0, 0.0), ST_Point(3.0, 4.0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 5.0  |
+------+
```

##### ST_GeodesicLengthWGS84

本文为您介绍如何在MaxCompute中使用ST_GeodesicLengthWGS84函数，用于返回WGS84球体上沿线的距离（以米为单位）。

**操作说明**

###### 使用说明

返回WGS84球体上沿线的距离，以米为单位。需要几何体在WGS84坐标系中，否则返回NULL。

**函数语法**

```
ST_GeodesicLengthWGS84(ST_Geometry line);
```

**参数说明**

line：必填，ST_Geometry类型的几何图形对象，需要几何体在WGS84坐标系中（SRID为4326），否则返回NULL。

**返回值**

DOUBLE类型，返回WGS84球体上沿线的距离，以米为单位。

##### 使用示例

```
SELECT ST_GeodesicLengthWGS84(ST_SetSRID(ST_LineString(0.0, 0.0, 0.3, 0.4), 4326));
```

`--` 返回结果

```
+---------------------+
| _c0                 |
+---------------------+
| 55421.408578278686  |
+---------------------+ SELECT ST_GeodesicLengthWGS84(ST_SetSRID(ST_GeomFromText('MultiLineString((0.0 80.0, 0.3 80.4))'), 4326));
```

`--` 返回结果

```
+--------------------+
| _c0                |
+--------------------+
| 45026.96274781222  |
+--------------------+
```

##### ST_GeometryN

大数据计算服务本文为您介绍如何在MaxCompute中使用ST_GeometryN函数，用于返回几何集合中指定位置的几何对象。

**操作说明**

###### 使用说明

返回集合中的第n个几何对象ST_Geometry，n从1开始。

**函数语法**

```
ST_GeometryN(ST_GeometryCollection, BIGINT n);
```

**参数说明**

ST_GeometryCollection：必填，几何集合对象。 n：必填，BIGINT类型，指定要返回的几何对象在集合中的位置，从1开始。

**返回值**

返回集合中第n个几何对象。

##### 使用示例

`--` 返回`multipoint`中第3个点

```
SELECT ST_GeometryN(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 10))' ), 3);
```

`--` 返回`multilinestring`中第2条线

```
SELECT ST_GeometryN(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8))'), 2);
```

##### ST_Is3D

本文为您介绍如何在MaxCompute中使用ST_Is3D函数，用于判断几何图形是否为3D图形。

**操作说明**

###### 使用说明

判断几何图形是否为3D图形，如果为3D图形，则返回true，否则返回false。

**函数语法**

```
ST_Is3D(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

BOOLEAN类型。如果几何图形为3D图形返回True，否则返回False。

##### 使用示例

大数据计算服务 `--` 二维多边形

```
SELECT ST_Is3D(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

`--` 二维线

```
SELECT ST_Is3D(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

`--` 二维点

```
SELECT ST_Is3D(ST_Point(3., 4.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

`--` 三维点

```
SELECT ST_Is3D(ST_PointZ(3., 4., 2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

##### ST_IsClosed

本文为您介绍如何在MaxCompute中使用ST_IsClosed函数，用于判断线串或多条线串是否闭合。

**操作说明**

###### 使用说明

如果一条线串或多条线串都为闭合的，则返回true，否则返回false。

**函数语法**

```
ST_IsClosed(ST_[Multi]LineString);
```

**参数说明**

大数据计算服务 ST_[Multi]LineString：必填，ST_LineString或ST_MultiLineString类型的几何图形对象。

**返回值**

BOOLEAN类型。如果线串为闭合的返回true，否则返回false。

##### 使用示例

`--` 闭合线串

```
SELECT ST_IsClosed(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

`--` 非闭合线串

```
SELECT ST_IsClosed(ST_LineString(0., 0., 3., 4.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_IsEmpty

本文为您介绍如何在MaxCompute中使用ST_IsEmpty函数，用于判断几何对象是否为空。

**操作说明**

###### 使用说明

如果几何对象是空，则返回true，否则返回false。

**函数语法**

```
ST_IsEmpty(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

BOOLEAN类型。如果几何对象为空返回true，否则返回false。

##### 使用示例

大数据计算服务 `--` 非空几何对象

```
SELECT ST_IsEmpty(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

`--` 空几何对象

```
SELECT ST_IsEmpty(ST_GeomFromText('point empty'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

##### ST_IsMeasured

本章节为您介绍Accessors函数中的ST_IsMeasured函数，并提供参考示例。 函数声明如下。 用途：返回几何图形是否有度量维度，是则返回True，否则返回False。 示例如下。

```
SELECT ST_IsMeasured(ST_Polygon(1,1, 1,4, 4,4, 4,1)) FROM src LIMIT 1;
```

`--` 返回`False`。

```
SELECT ST_IsMeasured(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1;
```

`--` 返回`False`。

```
SELECT ST_IsMeasured(ST_Point(3., 4.)) FROM src LIMIT 1;
```

`--` 返回`False`。

```
SELECT ST_IsMeasured(ST_PointM(3., 4., 2)) FROM src LIMIT 1;
```

`--` 返回`True`。

##### ST_IsSimple

本文为您介绍如何在MaxCompute中使用ST_IsSimple函数，用于判断几何对象是否为简单对象。

**操作说明**

###### 使用说明

判断几何对象是否为简单对象，是简单对象返回true，否则返回false。简单对象的范围包括以下几种情况： 简单点：一个点没有内部环，即只有一个坐标。 简单线：一条线段没有自交或交叉，即没有重叠部分，也没有内部环。 简单多点：一个多点几何对象由多个简单点组成，每个点没有内部环。 大数据计算服务简单多线：一个多线几何对象由多个简单线组成，每个线段没有自交或交叉，没有重叠部分，也没有内部环。 简单多边形：一个多边形几何对象由一个外环和可能的零个或多个内环组成。每个环都是一个简单线， 外环和内环之间没有自交或交叉，也没有重叠部分。

**函数语法**

```
ST_IsSimple(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

BOOLEAN类型。如果几何对象为简单对象返回true，否则返回false。

##### 使用示例

`--` 简单对象（点）

```
SELECT ST_IsSimple(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

`--` 非简单对象（自交线）

```
SELECT ST_IsSimple(ST_LineString(0., 0., 1., 1., 0., 1., 1., 0.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_IsRing

本文为您介绍如何在MaxCompute中使用ST_IsRing函数，用于判断线串是否为封闭环。

**操作说明**

###### 使用说明

判断几何对象是否为封闭环，即起点和终点是相同的。若属于封闭环则返回true，否则返回false。

**函数语法**

```
ST_IsRing(ST_LineString);
```

**参数说明**

**返回值**

BOOLEAN类型。如果线串为封闭环（起点和终点相同且无自交）返回true，否则返回false。 大数据计算服务

##### 使用示例

`--` 封闭环

```
SELECT ST_IsRing(ST_LineString(0., 0., 3., 4., 0., 4., 0., 0.));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

`--` 自交封闭线（非简单环）

```
SELECT ST_IsRing(ST_LineString(0., 0., 1., 1., 1., 2., 2., 1., 1., 1., 0., 0.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

`--` 非封闭线串

```
SELECT ST_IsRing(ST_LineString(0., 0., 3., 4.));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Length

本文为您介绍如何在MaxCompute中使用ST_Length函数，用于返回线段的长度。

**操作说明**

###### 使用说明

返回线段的长度。

**函数语法**

```
ST_Length(line);
```

**参数说明**

**返回值**

DOUBLE类型，返回线段的长度。

##### 使用示例

大数据计算服务

```
SELECT ST_Length(ST_LineString(0.0, 0.0, 3.0, 4.0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 5.0  |
+------+
```

##### ST_M

函数声明如下。

```
ST_M(geometry)
```

用途：返回几何图形三维坐标点的测量值M的值。 示例如下。

```
SELECT ST_M(ST_PointM(3., 4., 2)) FROM src LIMIT 1;
```

返回结果如下。

##### ST_MaxM

函数声明如下。 用途：返回几何对象最大的测量坐标。 示例如下。

```
SELECT ST_MaxM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

返回结果如下。

```
SELECT ST_MaxM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

返回结果如下。

##### ST_MinM

大数据计算服务函数声明如下。 用途：返回几何对象最小的测量坐标。 示例如下。

```
SELECT ST_MinM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

返回结果如下。

```
SELECT ST_MinM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

返回结果如下。

##### ST_X

本文为您介绍如何在MaxCompute中使用ST_X函数，用于返回点的X轴坐标。

**操作说明**

###### 使用说明

返回点的X轴坐标。

**函数语法**

```
ST_X(ST_Point point);
```

**参数说明**

**返回值**

DOUBLE类型，返回点的X轴坐标值。

##### 使用示例

```
SELECT ST_X(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.5  |
+------+
```

##### ST_Y

本文为您介绍如何在MaxCompute中使用ST_Y函数，用于返回点的Y轴坐标。

**操作说明**

大数据计算服务

###### 使用说明

返回点的Y轴坐标。

**函数语法**

```
ST_Y(ST_Point point);
```

**参数说明**

**返回值**

DOUBLE类型，返回点的Y轴坐标值。

##### 使用示例

```
SELECT ST_Y(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.5  |
+------+
```

##### ST_Z

本文为您介绍如何在MaxCompute中使用ST_Z函数，用于返回点的Z轴坐标。

**操作说明**

###### 使用说明

返回点的Z轴坐标。

**函数语法**

```
ST_Z(ST_Point point);
```

**参数说明**

**返回值**

DOUBLE类型，返回点的Z轴坐标值。

##### 使用示例

```
SELECT ST_Z(ST_Point(1.5, 2.5, 3.0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### ST_MaxX

大数据计算服务本文为您介绍如何在MaxCompute中使用ST_MaxX函数，用于返回几何对象最大的X轴坐标。

**操作说明**

###### 使用说明

返回几何对象最大的X轴坐标。

**函数语法**

```
ST_MaxX(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最大X轴坐标值。

##### 使用示例

```
SELECT ST_MaxX(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.5  |
+------+ SELECT ST_MaxX(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 3.0  |
+------+
```

##### ST_MaxY

本文为您介绍如何在MaxCompute中使用ST_MaxY函数，用于返回几何对象最大的Y轴坐标。

**操作说明**

###### 使用说明

返回几何对象最大的Y轴坐标。

**函数语法**

```
ST_MaxY(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最大Y轴坐标值。

##### 使用示例

大数据计算服务

```
SELECT ST_MaxY(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.5  |
+------+ SELECT ST_MaxY(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.5  |
+------+
```

##### ST_MaxZ

本文为您介绍如何在MaxCompute中使用ST_MaxZ函数，用于返回几何对象最大的Z轴坐标。

**操作说明**

###### 使用说明

返回几何对象最大的Z轴坐标。

**函数语法**

```
ST_MaxZ(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最大Z轴坐标值。

##### 使用示例

大数据计算服务

```
SELECT ST_MaxZ(ST_PointZ(1.5, 2.5, 2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT ST_MaxZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.0  |
+------+
```

##### ST_MinX

本文为您介绍如何在MaxCompute中使用ST_MinX函数，用于返回几何对象最小的X轴坐标。

**操作说明**

###### 使用说明

返回几何对象最小的X轴坐标。

**函数语法**

```
ST_MinX(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最小X轴坐标值。

##### 使用示例

大数据计算服务

```
SELECT ST_MinX(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.5  |
+------+ SELECT ST_MinX(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.5  |
+------+
```

##### ST_MinY

本文为您介绍如何在MaxCompute中使用ST_MinY函数，用于返回几何对象最小的Y轴坐标。

**操作说明**

###### 使用说明

返回几何对象最小的Y轴坐标。

**函数语法**

```
ST_MinY(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最小Y轴坐标值。

##### 使用示例

大数据计算服务

```
SELECT ST_MinY(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.5  |
+------+ SELECT ST_MinY(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.2  |
+------+
```

##### ST_MinZ

本文为您介绍如何在MaxCompute中使用ST_MinZ函数，用于返回几何对象最小的Z轴坐标。

**操作说明**

###### 使用说明

返回几何对象最小的Z轴坐标。

**函数语法**

```
ST_MinZ(ST_Geometry geometry);
```

**参数说明**

geometry：必填，几何图形对象。

**返回值**

DOUBLE类型，返回几何对象中所有坐标点的最小Z轴坐标值。

##### 使用示例

大数据计算服务

```
SELECT ST_MinZ(ST_PointZ(1.5, 2.5, 2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2.0  |
+------+ SELECT ST_MinZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1.0  |
+------+
```

##### ST_NumGeometries

本文为您介绍如何在MaxCompute中使用ST_NumGeometries函数，用于返回几何集合中几何对象的数量。

**操作说明**

###### 使用说明

返回几何集合中几何对象的数量。

**函数语法**

```
ST_NumGeometries(ST_GeometryCollection);
```

**参数说明**

ST_GeometryCollection：必填，几何集合对象。

**返回值**

BIGINT类型，返回几何集合中几何对象的数量。

##### 使用示例

大数据计算服务

```
SELECT ST_NumGeometries(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 1 0))'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 4    |
+------+ SELECT ST_NumGeometries(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8)) '));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+
```

##### ST_NumInteriorRing

本文为您介绍如何在MaxCompute中使用ST_NumInteriorRing函数，用于返回多边形内环的数量。

**操作说明**

###### 使用说明

返回多边形内环的数量。

**函数语法**

```
ST_NumInteriorRing(ST_Polygon);
```

**参数说明**

**返回值**

BIGINT类型，返回多边形内环的数量。

##### 使用示例

大数据计算服务 `--` 无内环的多边形

```
SELECT ST_NumInteriorRing(ST_Polygon(1, 1, 1, 4, 4, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+
```

`--` 有1个内环的多边形

```
SELECT ST_NumInteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+
```

##### ST_NumPoints

本文为您介绍如何在MaxCompute中使用ST_NumPoints函数，用于返回几何对象中点的数量。

**操作说明**

###### 使用说明

返回几何对象中点的数量。

**函数语法**

```
BIGINT ST_NumPoints(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的几何对象。

**返回值**

返回BIGINT类型，表示几何对象中包含的点的数量。

##### 使用示例

大数据计算服务

```
SELECT ST_NumPoints(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 1    |
+------+ SELECT ST_NumPoints(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 2    |
+------+ SELECT ST_NumPoints(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))'));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 4    |
+------+
```

##### ST_PointN

本文为您介绍如何在MaxCompute中使用ST_PointN函数，用于返回线串中第n个顶点。

**操作说明**

###### 使用说明

返回一个或多个线串中第n个顶点。

**函数语法**

```
GEOMETRY ST_PointN(GEOMETRY geometry, BIGINT n);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的线串几何对象。 n：必填，BIGINT类型，表示要返回的顶点的序号。

**返回值**

返回GEOMETRY类型，表示线串中第n个顶点。如果n超出顶点范围，返回NULL。

##### 使用示例

```
SELECT ST_PointN(ST_LineString(1.5, 2.5, 3.0, 2.2), 2);
```

##### ST_StartPoint

大数据计算服务本文为您介绍如何在MaxCompute中使用ST_StartPoint函数，用于返回线串的第一个点。

**操作说明**

###### 使用说明

返回线串的第一个点。

**函数语法**

```
GEOMETRY ST_StartPoint(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的线串几何对象。

**返回值**

返回GEOMETRY类型，表示线串的第一个点。

##### 使用示例

```
SELECT ST_StartPoint(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

##### ST_EndPoint

本文为您介绍如何在MaxCompute中使用ST_EndPoint函数，用于返回线串的最后一个点。

**操作说明**

###### 使用说明

返回线串的最后一个点。

**函数语法**

```
GEOMETRY ST_EndPoint(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的线串几何对象。

**返回值**

返回GEOMETRY类型，表示线串的最后一个点。

##### 使用示例

```
SELECT ST_EndPoint(ST_LineString(1.5, 2.5, 3.0, 2.2));
```

##### ST_SRID

本文为您介绍如何在MaxCompute中使用ST_SRID函数，用于返回几何对象的空间参考标识符（SRID）。

**操作说明**

###### 使用说明

返回几何对象的SRID（空间参考标识符）。

**函数语法**

```
BIGINT ST_SRID(GEOMETRY geometry);
```

**参数说明**

大数据计算服务 geometry：必填，GEOMETRY类型，表示输入的几何对象。

**返回值**

返回BIGINT类型，表示几何对象的SRID值。

##### 使用示例

```
SELECT ST_SRID(ST_Point(1.5, 2.5));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| 0    |
+------+
```

#### Operations

##### ST_Aggr_ConvexHull

本文为您介绍如何在MaxCompute中使用ST_Aggr_ConvexHull函数，用于返回所有几何图形聚合的凸包。

**操作说明**

###### 使用说明

返回所有几何图形聚合的凸包。

**函数语法**

```
GEOMETRY ST_Aggr_ConvexHull(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示参与聚合运算的几何对象列。

**返回值**

返回GEOMETRY类型，表示所有输入几何图形聚合后的凸包几何对象。

##### 使用示例

```
SELECT ST_Aggr_ConvexHull(ST_Point(1.5, 2.5));
```

##### ST_Aggr_Intersection

本文为您介绍如何在MaxCompute中使用ST_Aggr_Intersection函数，用于返回所有几何图形交集所占据的几何图形。

**操作说明**

###### 使用说明

聚合所有几何图形交集所占据的几何图形。

**函数语法**

```
GEOMETRY ST_Aggr_Intersection(GEOMETRY geometry);
```

**参数说明**

大数据计算服务 geometry：必填，GEOMETRY类型，表示参与聚合运算的几何对象列。

**返回值**

返回GEOMETRY类型，表示所有输入几何图形交集所占据的几何对象。

##### 使用示例

```
SELECT ST_Aggr_Intersection(ST_Point(1.5, 2.5));
```

##### ST_Aggr_Union

本文为您介绍如何在MaxCompute中使用ST_Aggr_Union函数，用于返回所有几何图形合集所占据的几何图形。

**操作说明**

###### 使用说明

聚合所有几何图形合集所占据的几何图形。

**函数语法**

```
GEOMETRY ST_Aggr_Union(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示参与聚合运算的几何对象列。

**返回值**

返回GEOMETRY类型，表示所有输入几何图形合集所占据的几何对象。

##### 使用示例

```
SELECT ST_Aggr_Union(ST_Point(1.5, 2.5));
```

##### ST_Bin

函数声明如下。 用途：返回指定点的Bin ID。

##### ST_BinEnvelope

函数声明如下。 用途：返回给定点的二进制包络。

```
SELECT ST_BinEnvelope(POINT(2, 3)) AS bin_envelope;
```

大数据计算服务

##### ST_Boundary

本文为您介绍如何在MaxCompute中使用ST_Boundary函数，用于返回几何对象的边界。

**操作说明**

###### 使用说明

输入几何对象，返回该几何对象的边界。

**函数语法**

```
GEOMETRY ST_Boundary(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的几何对象。

**返回值**

返回GEOMETRY类型，表示输入几何对象的边界。

##### 使用示例

```
SELECT ST_Boundary(ST_LineString(0, 1, 1, 0)); SELECT ST_Boundary(ST_Polygon(1, 1, 4, 1, 1, 4));
```

##### ST_Buffer

本文为您介绍如何在MaxCompute中使用ST_Buffer函数，用于返回与几何对象距离小于或等于指定半径的所有点。

**操作说明**

###### 使用说明

获取几何对象和距离，返回与源对象的距离小于或等于以输入距离为单位测量半径的所有点。

**函数语法**

```
GEOMETRY ST_Buffer(GEOMETRY geometry, DOUBLE distance);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的几何对象。 distance：必填，DOUBLE类型，表示缓冲距离。

**返回值**

返回GEOMETRY类型，表示与源对象距离小于或等于指定半径的所有点构成的几何对象。

##### 使用示例

```
SELECT ST_Buffer(ST_Point(1.5, 2.5), 1.0);
```

##### ST_ConvexHull

本文为您介绍如何在MaxCompute中使用ST_ConvexHull函数，用于返回指定几何对象的凸包。

**操作说明**

大数据计算服务

###### 使用说明

返回几何对象的凸包。

**函数语法**

```
GEOMETRY ST_ConvexHull(GEOMETRY geometry1, GEOMETRY geometry2, ...);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回GEOMETRY类型，表示所有输入几何对象的凸包几何对象。

##### 使用示例

```
SELECT ST_AsText(ST_ConvexHull(ST_Point(0, 0), ST_Point(0, 1), ST_Point(1, 1)));
```

`--` 返回结果

```
+---------------------------------------+
| _c0                                   |
+---------------------------------------+
| MULTIPOLYGON (((0 0, 1 1, 0 1, 0 0))) |
+---------------------------------------+
```

##### ST_Difference

本文为您介绍如何在MaxCompute中使用ST_Difference函数，用于返回两个几何对象的差集。

**操作说明**

###### 使用说明

返回两个几何对象差集的几何对象，即从第一个几何对象中移除与第二个几何对象重叠的部分。

**函数语法**

```
GEOMETRY ST_Difference(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回GEOMETRY类型，表示第一个几何对象减去与第二个几何对象交集部分后的几何对象。

##### 使用示例

大数据计算服务

```
SELECT ST_AsText(ST_Difference(ST_MultiPoint(1, 1, 1.5, 1.5, 2, 2), ST_Point(1.5, 1.5 )));
```

`--` 返回结果

```
+--------------------------+
| _c0                      |
+--------------------------+
| MULTIPOINT((1 1), (2 2)) |
+--------------------------+ SELECT ST_AsText(ST_Difference(ST_Polygon(0, 0, 0, 10, 10, 10, 10, 0), ST_Polygon(0, 0, 0, 5, 5, 5, 5, 0)));
```

`--` 返回结果

```
+---------------------------------------------------+
| _c0                                               |
+---------------------------------------------------+
| POLYGON ((5 0, 10 0, 10 10, 0 10, 0 5, 5 5, 5 0)) |
+---------------------------------------------------+
```

##### ST_Envelope

本文为您介绍如何在MaxCompute中使用ST_Envelope函数，用于返回几何对象的包络。

**操作说明**

###### 使用说明

返回几何对象的包络。如果几何对象是一个点或者是一条垂直或平行的线，ST_Envelope可能提供一个公差或者返回一个空的包络。

**函数语法**

```
GEOMETRY ST_Envelope(GEOMETRY geometry);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的几何对象。

**返回值**

返回GEOMETRY类型，表示输入几何对象的包络（最小边界矩形）。

##### 使用示例

```
SELECT ST_Envelope(ST_LineString(0, 0, 2, 2)); SELECT ST_Envelope(ST_Polygon(2, 0, 2, 3, 3, 0));
```

##### ST_ExteriorRing

本文为您介绍如何在MaxCompute中使用ST_ExteriorRing函数，用于以线串形式返回多边形的外部环。

**操作说明**

###### 使用说明

以线串形式返回多边形的外部环。 大数据计算服务

**函数语法**

```
GEOMETRY ST_ExteriorRing(GEOMETRY polygon);
```

**参数说明**

polygon：必填，GEOMETRY类型，表示输入的多边形几何对象。

**返回值**

返回GEOMETRY类型（LINESTRING），表示多边形的外部环。

##### 使用示例

```
SELECT ST_ExteriorRing(ST_Polygon(1, 1, 1, 4, 4, 1)); SELECT ST_ExteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1 ))'));
```

##### ST_InteriorRingN

本文为您介绍如何在MaxCompute中使用ST_InteriorRingN函数，用于以线串形式返回多边形的第n个内部环。

**操作说明**

###### 使用说明

以线串形式返回多边形的第n个内部环。

**函数语法**

```
GEOMETRY ST_InteriorRingN(GEOMETRY polygon, BIGINT n);
```

**参数说明**

polygon：必填，GEOMETRY类型，表示输入的多边形几何对象。 n：必填，BIGINT类型，表示要返回的内部环的序号。

**返回值**

返回GEOMETRY类型（LINESTRING），表示多边形的第n个内部环。

##### 使用示例

```
SELECT ST_InteriorRingN(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))'), 1);
```

##### ST_Intersection

本文为您介绍如何在MaxCompute中使用ST_Intersection函数，用于返回两个几何对象的交集。

**操作说明**

###### 使用说明

返回两个几何对象的交集。如果两个对象图形的交集维度低于对象图形的维度，则ST_Intersection可能丢失交集为低维度的图形，或者输出为一个闭合的线串。

**函数语法**

```
GEOMETRY ST_Intersection(GEOMETRY geometry1, GEOMETRY geometry2);
```

大数据计算服务

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回GEOMETRY类型，表示两个几何对象的交集。交集的维度可能低于输入对象的维度。

##### 使用示例

大数据计算服务

```
SELECT ST_AsText(ST_Intersection(ST_Point(1, 1), ST_Point(1, 1)));
```

`--` 返回结果

```
+--------------+
| _c0          |
+--------------+
| POINT(1 1)   |
+--------------+ SELECT ST_AsText(ST_Intersection(ST_GeomFromText('linestring(0 2, 0 0, 2 0)'), ST_Geo mFromText('linestring(0 3, 0 1, 1 0, 3 0)')));
```

`--` 返回结果

```
+--------------------------------------------------+
| _c0                                              |
+--------------------------------------------------+
| MULTILINESTRING((1 0, 2 0), (0 2, 0 1))          |
+--------------------------------------------------+ SELECT ST_AsText(ST_Intersection(ST_LineString(0, 2, 2, 3), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4)));
```

`--` 返回结果

```
+-------------------------------+
| _c0                           |
+-------------------------------+
| LINESTRING((1 2.5, 2 3))      |
+-------------------------------+ SELECT ST_AsText(ST_Intersection(ST_Polygon(2, 0, 2, 3, 3, 0), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4)));
```

`--` 返回结果

```
+--------------------------------------------------------+
| _c0                                                    |
+--------------------------------------------------------+
| POLYGON ((2 1, 2.6666666666666665 1, 2 3, 2 1))        |
+--------------------------------------------------------+ SELECT ST_AsText(ST_Intersection(ST_Polygon(2, 0, 3, 1, 2, 1), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4)));
```

`--` 返回结果

```
+-----------------------+
| _c0                   |
+-----------------------+
| LINESTRING (2 1, 3 1) |
+-----------------------+
```

##### ST_SymmetricDiff

本文为您介绍如何在MaxCompute中使用ST_SymmetricDiff函数，用于返回两个几何对象非公共部分组成的几何对象。 大数据计算服务

**操作说明**

###### 使用说明

返回由两个几何对象的非公共部分组成的几何对象。

**函数语法**

```
GEOMETRY ST_SymmetricDiff(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回GEOMETRY类型，表示两个几何对象非公共部分组成的几何对象。

##### 使用示例

```
SELECT ST_AsText(ST_SymmetricDiff(ST_LineString('linestring(0 2, 2 2)'), ST_LineString('linestring(1 2, 3 2)')));
```

`--` 返回结果

```
+------------------------------------------+
| _c0                                      |
+------------------------------------------+
| MULTILINESTRING ((0 2, 1 2), (2 2, 3 2)) |
+------------------------------------------+ SELECT ST_AsText(ST_SymmetricDiff(ST_Polygon('polygon((0 0, 2 0, 2 2, 0 2, 0 0))'), S T_Polygon('polygon((1 1, 3 1, 3 3, 1 3, 1 1))')));
```

`--` 返回结果

```
+-------------------------------------------------------------------------------------- ------+
| _c0
```

|

```
+-------------------------------------------------------------------------------------- ------+
| MULTIPOLYGON (((0 0, 2 0, 2 1, 1 1, 1 2, 0 2, 0 0)), ((2 1, 3 1, 3 3, 1 3, 1 2, 2 2
, 2 1))) | +-------------------------------------------------------------------------------------- ------+
```

##### ST_Union

本文为您介绍如何在MaxCompute中使用ST_Union函数，用于返回多个几何对象组合而成的几何对象。

**操作说明**

###### 使用说明

返回两个或多个几何对象组合而成的几何对象。

**函数语法**

```
GEOMETRY ST_Union(GEOMETRY geometry1, GEOMETRY geometry2, ...);
```

大数据计算服务

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回GEOMETRY类型，表示所有输入几何对象组合而成的几何对象。

##### 使用示例

```
SELECT ST_AsText(ST_Union(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Polygon(4, 1, 4, 4, 4, 8, 8, 1)));
```

`--` 返回结果

```
+------------------------------------------------------+
| _c0                                                  |
+------------------------------------------------------+
| MULTIPOLYGON (((1 1, 4 1, 8 1, 4 8, 4 4, 1 4, 1 1))) |
+------------------------------------------------------+
```

#### Relationship Tests

##### ST_Contains

本文为您介绍如何在MaxCompute中使用ST_Contains函数，用于判断一个几何对象是否包含另一个几何对象。

**操作说明**

###### 使用说明

如果几何对象geometry1包含几何对象geometry2，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Contains(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示被包含判断的几何对象。 geometry2：必填，GEOMETRY类型，表示需要判断是否被包含的几何对象。

**返回值**

返回BOOLEAN类型。如果geometry1包含geometry2，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Contains(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Point(2, 3));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Contains(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Point(8, 8));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Crosses

本文为您介绍如何在MaxCompute中使用ST_Crosses函数，用于判断两个几何对象是否相交（不包括相切或包含关系）。

**操作说明**

###### 使用说明

判断两个几何对象是否相交，但不包括相切或包含关系。如果两个几何对象有一个交叉点则返回true，否则返回false。该函数适用于线与线、线与多边形、多边形与多边形之间的关系判断。

**函数语法**

```
BOOLEAN ST_Crosses(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象有交叉点（不包括相切或包含），返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Crosses(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Crosses(ST_LineString(2, 0, 2, 3), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Crosses(ST_LineString(0, 2, 0, 1), ST_LineString(2, 0, 1, 0));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Disjoint

本文为您介绍如何在MaxCompute中使用ST_Disjoint函数，用于判断两个几何对象是否完全不相交。

**操作说明**

###### 使用说明

判断两个几何对象是否完全不相交。如果两个几何对象没有任何交集，即彼此之间没有相交的点、线或面，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Disjoint(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象完全不相交（没有任何交集），返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Disjoint(ST_LineString(0, 0, 0, 1), ST_LineString(1, 1, 1, 0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Disjoint(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_EnvIntersects

本文为您介绍如何在MaxCompute中使用ST_EnvIntersects函数，用于判断两个几何对象的外包矩形是否相交。

**操作说明**

###### 使用说明

判断两个几何对象的外包矩形是否相交。如果两个几何对象的外包矩形相交，则返回true，否则返回 false。

**函数语法**

```
BOOLEAN ST_EnvIntersects(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象的外包矩形相交，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_EnvIntersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 3, 2, 2));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+ SELECT ST_EnvIntersects(ST_LineString(0, 0, 2, 2), ST_LineString(1, 0, 3, 2));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+
```

##### ST_Equals

本文为您介绍如何在MaxCompute中使用ST_Equals函数，用于判断两个几何对象是否相同。

**操作说明**

###### 使用说明

判断两个几何对象是否相同。如果几何对象geometry1和几何对象geometry2在空间上完全一致，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Equals(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象在空间上完全相同，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Equals(ST_LineString(0, 0, 1, 1), ST_LineString(1, 1, 0, 0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Equals(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Intersects

本文为您介绍如何在MaxCompute中使用ST_Intersects函数，用于判断两个几何对象是否有共同交集。

**操作说明**

###### 使用说明

判断两个几何对象是否有共同交集。如果几何对象geometry1和几何对象geometry2具有共同的交集， 则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Intersects(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象具有共同的交集，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Intersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 1, 0, 0));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(0, 0, 1, 1), ST_LineString(1, 0, 0, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(2, 0, 2, 3), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Intersects(ST_LineString(8, 7, 7, 8), ST_Polygon(1, 1, 4, 1, 4, 4, 1, 4));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Overlaps

本文为您介绍如何在MaxCompute中使用ST_Overlaps函数，用于判断两个几何对象是否重叠（不包括相切）。

**操作说明**

###### 使用说明

判断两个几何对象是否重叠（不包括相切）。如果几何对象geometry1和几何对象geometry2重叠，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Overlaps(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 大数据计算服务 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象重叠（不包括相切），返回True；否则返回False。

##### 使用示例

```
SELECT ST_Overlaps(ST_Polygon(2, 0, 2, 3, 3, 0), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Overlaps(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Relate

本文为您介绍如何在MaxCompute中使用ST_Relate函数，用于判断两个几何对象是否存在DE-9IM拓扑关系。

**操作说明**

###### 使用说明

判断两个几何对象是否存在DE-9IM拓扑关系。如果几何对象geometry1和几何对象geometry2满足指定的DE-9IM拓扑模式，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Relate(GEOMETRY geometry1, GEOMETRY geometry2, STRING pattern);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。 pattern：必填，STRING类型，表示DE-9IM拓扑模式字符串，长度为9，由T、F、*组成的模式矩阵。

**返回值**

返回BOOLEAN类型。如果两个几何对象满足指定的DE-9IM拓扑模式，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Relate(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), '*
***T****');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Relate(ST_Polygon(2, 0, 2, 1, 3, 1), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), 'T
********');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+ SELECT ST_Relate(ST_LineString(0, 0, 3, 3), ST_LineString(1, 1, 4, 4), 'T********');
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Relate(ST_LineString(0, 0, 3, 3), ST_LineString(1, 1, 4, 4), '****T****');
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Touches

**操作说明**

###### 使用说明

判断两个几何对象是否仅在边界处接触。如果几何对象geometry1和几何对象geometry2至少有一个点相交，而且它们的内部不相交，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Touches(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示第一个输入的几何对象。 大数据计算服务 geometry2：必填，GEOMETRY类型，表示第二个输入的几何对象。

**返回值**

返回BOOLEAN类型。如果两个几何对象仅在边界处接触（至少有一个公共点且内部不相交），返回 true；否则返回false。

##### 使用示例

```
SELECT ST_Touches(ST_Point(1, 2), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Touches(ST_Point(8, 8), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

##### ST_Within

本文为您介绍如何在MaxCompute中使用ST_Within函数，用于判断一个几何对象是否被另一个几何对象包含。

**操作说明**

###### 使用说明

判断一个几何对象是否被另一个几何对象包含。如果几何对象geometry2包含几何对象geometry1，则返回true，否则返回false。

**函数语法**

```
BOOLEAN ST_Within(GEOMETRY geometry1, GEOMETRY geometry2);
```

**参数说明**

geometry1：必填，GEOMETRY类型，表示需要判断是否被包含的几何对象。 geometry2：必填，GEOMETRY类型，表示用于判断是否包含的几何对象。

**返回值**

返回BOOLEAN类型。如果geometry2包含geometry1，返回true；否则返回false。

##### 使用示例

大数据计算服务

```
SELECT ST_Within(ST_Point(2, 3), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+------+
| _c0  |
+------+
| true |
+------+ SELECT ST_Within(ST_Point(8, 8), ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1));
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+
```

#### GeoHash索引函数

##### ST_GeoHash

本文为您介绍如何在MaxCompute中使用ST_GeoHash函数，用于计算输入点的GeoHash值。

**操作说明**

###### 使用说明

计算输入点的GeoHash值，以字符串类型返回。支持输入经纬度或ST_函数得到的几何对象。精度不指定的情况下默认为最大精度，精度值大小取决于您的应用需求和空间数据的特性。

**函数语法**

```
STRING ST_GeoHash(GEOMETRY geometry, INT precision); STRING ST_GeoHash(DOUBLE longitude, DOUBLE latitude, INT precision);
```

**参数说明**

geometry：必填，GEOMETRY类型，表示输入的点几何对象。 longitude：必填，DOUBLE类型，表示经度值。 latitude：必填，DOUBLE类型，表示纬度值。 precision：选填，INT类型，表示GeoHash编码的精度。默认为最大精度。

**返回值**

返回STRING类型，表示输入点的GeoHash编码值。

##### 使用示例

大数据计算服务

```
SELECT ST_GeoHash(ST_Point(-102.849854, 36.451113), 8);
```

`--` 返回结果

```
+----------+
| _c0      |
+----------+
| 9wqz7eep |
+----------+ SELECT ST_GeoHash(ST_GeomFromText('POINT(-102.849854 36.451113)'));
```

`--` 返回结果

```
+--------------+
| _c0          |
+--------------+
| 9wqz7eep0eyq |
+--------------+ SELECT ST_GeoHash(-102.849854, 36.451113, 10);
```

`--` 返回结果

```
+------------+
| _c0        |
+------------+
| 9wqz7eep0e |
+------------+
```

##### ST_PointFromGeoHash

本文为您介绍如何在MaxCompute中使用ST_PointFromGeoHash函数，用于根据输入的GeoHash值返回对应的点对象。

**操作说明**

###### 使用说明

根据输入的GeoHash值，返回对应的点几何对象。精度不指定的情况下默认为最大精度，精度值大小取决于您的应用需求和空间数据的特性。

**函数语法**

```
GEOMETRY ST_PointFromGeoHash(STRING geohash, INT precision);
```

**参数说明**

geohash：必填，STRING类型，表示输入的GeoHash编码值。 precision：选填，INT类型，表示GeoHash编码的精度。默认为最大精度。

**返回值**

返回GEOMETRY类型（POINT），表示GeoHash编码对应的点几何对象。

##### 使用示例

大数据计算服务

```
SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq'));
```

`--` 返回结果

```
+------------------------------------------------+
| _c0                                            |
+------------------------------------------------+
| POINT (-102.84985402598977 36.451112972572446) |
+------------------------------------------------+ SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq', 4));
```

`--` 返回结果

```
+------------------------------------+
| _c0                                |
+------------------------------------+
| POINT (-102.83203125 36.474609375) |
+------------------------------------+
```

##### ST_EnvelopeFromGeoHash

本文为您介绍如何在MaxCompute中使用ST_EnvelopeFromGeoHash函数，用于根据输入的GeoHash 值返回对应精度的外接矩形。

**操作说明**

###### 使用说明

根据输入的GeoHash值，返回对应精度的外接矩形。精度不指定的情况下默认为最大精度，精度值大小取决于您的应用需求和空间数据的特性。

**函数语法**

```
GEOMETRY ST_EnvelopeFromGeoHash(STRING geohash, INT precision);
```

**参数说明**

geohash：必填，STRING类型，表示输入的GeoHash编码值。 precision：选填，INT类型，表示GeoHash编码的精度。默认为最大精度。

**返回值**

返回GEOMETRY类型（POLYGON），表示GeoHash编码对应精度的外接矩形。

##### 使用示例

大数据计算服务

```
SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq', 8));
```

`--` 返回结果

```
+------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| POLYGON ((-102.84988403320312 36.45109176635742, -102.84954071044922
36.45109176635742, -102.84954071044922 36.451263427734375, -102.84988403320312 36.451 263427734375, -102.84988403320312 36.45109176635742)) | +------------------------------------------------------------+ SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq'));
```

`--` 返回结果

```
+------------------------------------------------------------+
| _c0                                                        |
+------------------------------------------------------------+
| POLYGON ((-102.84985419362783 36.451112888753414, -102.84985385835171
36.451112888753414, -102.84985385835171 36.45111305639148, -102.84985419362783 36.451 11305639148, -102.84985419362783 36.451112888753414)) | +------------------------------------------------------------+
```

##### ST_GeoHashNeighbours

本文为您介绍如何在MaxCompute中使用ST_GeoHashNeighbours函数，用于返回指定点及其周围邻居的GeoHash编码值。

**操作说明**

###### 使用说明

该函数为UDTF，会产生9条数据。根据输入经纬度以及精度（不可省略），返回包含当前点在内的周围邻居共9个GeoHash字符串值。

**函数语法**

```
list_of_string ST_GeoHashNeighbours(DOUBLE longitude, DOUBLE latitude, INT precision) ;
```

**参数说明**

longitude：必填，DOUBLE类型，表示经度值。 latitude：必填，DOUBLE类型，表示纬度值。 precision：必填，INT类型，表示GeoHash编码的精度。此参数不可省略。

**返回值**

返回9个GeoHash字符串值，分别为当前点及其周围8个邻居的GeoHash编码。该函数为UDTF，会产生 9条数据。

##### 使用示例

大数据计算服务

```
SELECT ST_GeoHashNeighbours(-102.849854, 36.451113, 10) AS geohash;
```

`--` 返回结果

```
+------------+ +------------+
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

#### S2网格函数

##### ST_S2CellIdsFromGeom

本章节为您介绍S2网格函数中的ST_S2CellIdsFromGeom函数，并提供参考示例。 函数声明如下。

```
list_of_string ST_S2CellIdsFromGeom(st_geometry geometry, integer level)
```

用途：把输入的几何对象按指定的Level用S2 Cell覆盖，并返回所有的S2CellId。 示例如下。

```
SELECT ST_S2CellIdsFromGeom(ST_Point(-102.849854, 36.451113), 4); SELECT ST_S2CellIdsFromGeom(ST_LineString('LINESTRING(-71.160281 42.258729,-71.160837 4 2.259113,-71.161144 42.25932)'), 17) as cellid;
```

##### ST_S2CellIdsFromText

本章节为您介绍S2网格函数中的ST_S2CellIdsFromText函数，并提供参考示例。 函数声明如下。

```
list_of_string ST_S2CellIdsFromText(string wkt, integer level)
```

用途：把输入的几何对象的WKT格式按指定的Level用S2 Cell覆盖，并返回所有的S2CellId。 示例如下。

```
SELECT ST_S2CellIdsFromText(ST_GeomFromText('POINT(-102.849854 36.451113)'), 4); SELECT ST_S2CellIdsFromText('LINESTRING(-71.160281 42.258729,-71.160837 42.259113,-71.1 61144 42.25932)', 17) as cellid;
```

##### ST_S2CellCenterPoint

本章节为您介绍S2网格函数中的ST_S2CellCenterPoint函数，并提供参考示例。 大数据计算服务函数声明如下。 用途：计算输入的S2CellId所包含的Cell的中心点。 示例如下。

```
SELECT ST_S2CellCenterPoint('549015'); SELECT ST_AsText(ST_S2CellCenterPoint('89e37f091'));
```

##### ST_S2CellNeighbours

本文为您介绍如何在MaxCompute中使用ST_S2CellNeighbours函数，用于根据S2CellId和Level返回所有邻居的S2CellId。

**操作说明**

###### 使用说明

根据输入的S2CellId和Level，计算CellId在层级Level下的邻居，返回所有邻居的S2CellId。

**函数语法**

```
list_of_string ST_S2CellNeighbours(STRING cellId, INT level);
```

**参数说明**

cellId：必填，STRING类型，表示输入的S2CellId。 level：必填，INT类型，表示S2 Cell的层级。

**返回值**

返回包含指定CellId在对应层级下所有邻居的S2CellId。

##### 使用示例

大数据计算服务

```
SELECT ST_S2CellNeighbours('549015', 10) AS neighbour;
```

`--` 返回结果

```
+-----------+ +-----------+
| 549011    |
| 54903d    |
| 549017    |
| 54906b    |
| 549013    |
| 54903f    |
| 54906d    |
| 549041    |
+-----------+ SELECT ST_S2CellNeighbours('89e37f091', 16) AS neighbour;
```

`--` 返回结果

```
+-----------+ +-----------+
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

#### 球面计算函数

##### ST_AreaWGS84

函数声明如下。 用途：返回输入的几何对象在WGS84参考下的近似球面面积。具体做法是进行了EPSG:4326到 EPSG:3857的投影，再计算平面下的面积，单位是平方米。 示例如下。

```
SELECT ST_AreaWGS84(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 296 7450,743265.625 2967416,743238 2967416))'));
```

##### ST_DistanceWGS84

本章节为您介绍球面计算函数中的ST_DistanceWGS84函数，并提供参考示例。 大数据计算服务函数声明如下。

```
double ST_DistanceWGS84(st_geometry geometry1, st_geometry geometry2)
```

用途：返回输入的几何对象在WGS84参考下的近似球面距离。具体做法是进行了EPSG:4326到 EPSG:3857的投影，再计算平面下的距离，单位是米。 示例如下。

```
SELECT ST_DistanceWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), ST_GeomFromText('LINESTRING(-72.1260 42.45, -72.123 42.1546)'));
```

##### ST_BufferWGS84

函数声明如下。

```
st_geometry ST_BufferWGS84(st_geometry geometry, double radius)
```

用途：返回输入的几何对象在WGS84参考下的近似球面Buffer。具体做法是进行了EPSG:4326到 EPSG:3857的投影，再计算平面下的Buffer后，投影回EPSG:4326。 示例如下。

```
SELECT ST_AsText(ST_BufferWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), 10));
```

##### ST_GeodesicDistance

本章节为您介绍球面计算函数中的ST_GeodesicDistance函数，并提供参考示例。 函数声明如下。

```
double ST_GeodesicDistance(double lon1, double lat1, double lon2, double lat2, string m ethod = VINCENTY) double ST_GeodesicDistance(st_geometry geo1, st_geometry geo2, string method = VINCENTY
```

) 用途：使用指定的方法计算两点的球面距离，支持的方法为Vincenty、LawOfCosines和Haversine。通过Method参数指定，默认支持的方法为Vincenty，返回的单位为弧度。 示例如下。

```
SELECT ST_GeodesicDistance(ST_GeomFromText('POINT(152.352298 -24.875975)'), ST_GeomFromText('POINT(151.960336 -24.993289)'), 'LawOfCosines');
```

##### ST_Distance_Sphere

本章节为您介绍球面计算函数中的ST_Distance_Sphere函数，并提供参考示例。 函数声明如下。

```
double ST_Distance_Sphere(st_point geo1, st_point2 geo2) double ST_Distance_Sphere(double lng1, double lat1, double lng2, double lat2)
```

大数据计算服务用途：使用高德AMAP服务提供的算法计算输入的两点近似球面距离（单位：米），仅支持ST_Point或输入对应的经纬度值。 示例如下。

```
            ST_GeomFromText('POINT(116.292078 39.919622)'),
            ST_GeomFromText('POINT(116.286676 39.919593)'));
```

返回结果如下。

```
+------------+
| _c0        |
+------------+
| 460.6965312526471 |
+------------+
```

##### ST_Area_Sphere

函数声明如下。 用途：使用高德AMAP服务提供的算法计算输入的几何对象球面面积（单位：平方米），仅支持示例如下。

```
SELECT geospatial.ST_Area_Sphere(geospatial.ST_GeomFromText('POLYGON((116.259097 40.202 114,116.259024 40.20199,116.258768 40.201662,116.258376 40.201341,116.258031 40.201036,116.257675 40.200734,116.257429 40.200656,116.257357 40.200562,116.257392 40. 200051,116.257506 40.199433,116.257569 40.198586,116.257564 40.19756,116.257561 40.1973 72,116.257552 40.197036,116.257554 40.19675,116.257539 40.196647,116.257502 40.19653,116.257343 40.196389,116.257153 40.196276,116.256733 40.196071,116.25582 40.19 5646,116.255628 40.195611,116.255468 40.195653,116.255385 40.195742,116.255347 40.19584 9,116.255258 40.197143,116.255103 40.199576,116.255078 40.200585,116.251227 40.20059,116.251098 40.203978,116.259433 40.204111,116.259247 40.203079,116.259097 40.2 02114))'));
```

返回结果如下。

```
+------------+
| _c0        |
+------------+
| 353493.765625 |
+------------+
```

#### RTree索引函数

大数据计算服务

##### ST_BuildRTreeIndex

本章节为您介绍RTree索引函数中的ST_BuildRTreeIndex函数，并提供参考示例。 函数声明如下。

```
RTree ST_BuildRTreeIndex(string uniqueId, string geometryWkt)
```

用途：该函数是UDAF，输入是每一个几何对象的唯一ID和WKT字符串，用于创建RTree索引。该函数需要结合其他RTree函数一起使用。 示例如下。

```
SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index FROM poi_sample;
```

##### ST_ContainsFromRTree

函数声明如下。

```
ST_ContainsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中被该几何对象Contain的所有对象ID。用来加速ST_Contains的查询。

##### ST_CrossesFromRTree

函数声明如下。

```
ST_CrossesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中与该几何对象Cross的所有对象ID。用来加速ST_Crosses的查询。

##### ST_EqualsFromRTree

函数声明如下。

```
ST_EqualsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中与该几何对象Equal的所有对象ID。用来加速ST_Equals的查询。

##### ST_IntersectsFromRTree

本章节为您介绍RTree索引函数中的ST_IntersectsFromRTree函数。 函数声明如下。

```
ST_IntersectsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

大数据计算服务用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中与该几何对象Intersect的所有对象ID。用来加速ST_Intersects的查询。

##### ST_OverlapsFromRTree

函数声明如下。

```
ST_OverlapsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中与该几何对象Overlap的所有对象ID。用来加速ST_Overlaps的查询。

##### ST_TouchesFromRTree

函数声明如下。

```
ST_TouchesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中与该几何对象Touch的所有对象ID。用来加速ST_Touches的查询。

##### ST_WithinFromRTree

本章节为您介绍RTree索引函数中的ST_WithinFromRTree函数，并提供参考示例。 函数声明如下。

```
ST_WithinFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中包含该几何对象的所有对象ID。用来加速ST_Within的查询。 示例如下。 原始SQL语句，查询所有表A中线段与表B中的多边形相交的情况。

```
set odps.sql.allow.cartesian=true; SELECT a.id as link_id, b.id as shape_id
        geospatial.ST_LineString(a.line),
        geospatial.ST_Multipolygon(b.shape));
```

返回结果如下。 大数据计算服务

```
Summary: resource cost: cpu 3.28 Core * Min, memory 5.76 GB * Min inputs: outputs: Job run time: 111.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

使用新函数优化后。

```
SELECT /*+mapjoin(i)*/
      geospatial.ST_IntersectsFromRTree(id, line, i.index)
      AS (link_id, shape_id)
JOIN (
      SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index
) i;
```

返回结果如下。

```
Summary: resource cost: cpu 1.03 Core * Min, memory 1.99 GB * Min inputs: outputs: Job run time: 41.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

##### ST_KNNFromRTree

本章节为您介绍RTree索引函数中的ST_KNNFromRTree函数，并提供参考示例。 函数声明如下。

```
ST_KNNFromRTree(string uniqueId, string geometryWkt, int k, RTree rtree)
```

大数据计算服务用途：该函数是UDTF，输入是每一个几何对象的唯一ID和WKT字符串以及使用ST_BuildRTreeIndex创建的RTree索引，返回RTree中离输入几何对象最近的K个几何对象的ID。 示例如下。 把表的所有点创建RTree，并使用KNN函数在RTree寻找该表中每一点离自己最近的点（也就是自己）。

```
SELECT /*+mapjoin(i)*/
    geospatial.ST_KNNFromRTree(id, point, 1, i.index) AS (id1, id2)
JOIN (
    SELECT geospatial.ST_BuildRTreeIndex(id, point) AS index
) i;
```

返回结果如下。

```
Summary: resource cost: cpu 1.17 Core * Min, memory 2.24 GB * Min inputs: outputs: Job run time: 46.000 +-----+-----+
| id1 | id2 |
+-----+-----+
| B000A01B4E | B000A01B4E |
| B000A01C19 | B000A01C19 |
| B000A023A5 | B000A023A5 |
| B000A02F81 | B000A02F81 |
| B000A07BEE | B000A07BEE |
| B000A07E06 | B000A07E06 |
| B000A08863 | B000A08863 |
...
```

`--` 表一共有`1000`行数据，返回了`1000`行数据，符合预期。

#### 其他函数

##### ST_IsValid

函数声明如下。 用途：检查输入的几何对象或者WKT字符串是否符合标准。 示例如下。

```
SELECT ST_IsValid('POINT(-102.849854 36.451113)'); SELECT ST_IsValid(ST_Point('POINT(-102.849854 36.451113)'));
```

大数据计算服务

##### ST_Transform

函数声明如下。

```
st_geometry ST_TransformWGS84(st_geometry geometry) st_geometry ST_Transform(st_geometry geometry, integer toSRID) st_geometry ST_Transform(st_geometry geometry, integer fromSRID, integer toSRID)
```

用途：将输入的几何对象进行投影变换。其中ST_TransformWGS84把输入的几何图形按照EPSG:4326投影到EPSG:3857；ST_Transform则将输入的几何图形从fromSRID投影到toSRID；仅包含toSRID的重载示例如下。

```
SELECT ST_AsText(ST_Transform(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 2967450,743265.625 2967416,743238 2967416))', 2249, 4326))); SELECT ST_AsText(ST_TransformWGS84(ST_GeomFromText('POLYGON((-71.1776848522251 42.39028 96512902,-71.1776843766326 42.3903829478009, -71.1775844305465 42.3903826677917,-71.177 5825927231 42.3902893647987,-71.1776848522251 42.3902896512902))')));
```

### MaxCompute Hash Clustering

#### 功能背景

本文为您介绍MaxCompute Hash聚簇功能的产生背景。

##### 背景信息

##### 功能介绍

在MaxCompute查询中，Join是很常见的场景。目前，Join在MaxCompute内部主要有三种实现方法：
**Broadcast Hash Join**：当Join存在一个很小的表时，通常会采用这种方式，即把小表广播传递到所有
**Shuffle Hash Join**：如果Join表比较大，则不能直接广播。此时，通常会把两个表按照JoinKey进行
Hash Shuffle。由于相同的键值Hash结果也是一样的，因此保证了相同的Key的记录会收集到同一个 JoinTask Instance上面。然后，每个Instance对数据量小的一路建Hash表，数据量大的顺序读取Join。 大数据计算服务
**Sort Merge Join**：如果Join的表更大一些，由于内存已经不足以容纳建立一个Hash表，因此方法1和
方法2都不能使用。此时，通常的实现方法是先按照Join Key进行Hash Shuffle，然后再按照JoinKey进行排序，最后对Join双方进行归并操作，具体流程如下图所示。

**存储特性**

针对于MaxCompute的数据量和规模，目前在绝大多数情况下都是使用的Sort Merge Join方法。但是此方法会产生大量重复的Shuffle和Join，同时在对应的Join的Fuxi物理执行计划中，会需要多个Stage，成本很高。 大数据计算服务

**优化执行**

大数据计算服务因此，MaxCompute进行了如下尝试：如果在初始表数据生成时，按照Hash Shuffle和Sort的方式存储， 那么后续查询中将避免对数据的再次Shuffle和Sort。这样做的好处是，虽然在建表时付出了一次性的代价，却节省了将来可能产生的反复的Shuffle和Join。同时在对应的Join的Fuxi物理执行计划中，Stage也将被简化。以上一示例图为例，Stage将变为1个，节省了Shuffle和Sort的操作。 总体来说，MaxCompute Hash聚簇功能就是通过允许您在建表时设置表的Shuffle和Sort属性，进而让 MaxCompute根据数据已有的存储特性，优化执行计划，提高效率，节省资源消耗。

#### 功能描述

##### 功能开关

本文为您介绍如何开启MaxCompute Hash聚簇功能开关。

**开启聚簇功能开关**

Hash聚簇功能已经全面上线，缺省条件下即打开支持。但是，如果需要使用Clustered Index，需要设置上如下Flag。

```
SET odps.sql.cfile2.enable.read.write.index.flag=true;
```

###### 使用说明

设置上述Flag后，将对排序后的Hash Bucket自动建立Index，提高查询效率。如果希望使用Index功能， 则需要在建表和后续查询中都设置上述Flag。如果希望在Project中一直使用Index，请与MaxCompute团队联系。

**说明**

Clustered Index对于在排序键上的查询（等值或范围）有显著帮助，但是即使没有Enable上述 Flag，依然可以享受到Hash聚簇功能其他方面性能提升的好处。

##### 创建Hash聚簇表

大数据计算服务

**创建聚簇表语法**

您可以使用如下语句创建Hash聚簇表。其中，您需要指定Cluster Key（即Hash Key）以及Hash分片 （通常称之为Bucket）的数目。Sort是可选项，但在大多数情况下，建议和Cluster Key一致，以便取得最佳的优化效果。

```
[(col_name data_type [comment col_comment], ...)] [PARTITIONED BY (col_name data_type [comment col_comment], ...)] [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_nam e [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] [AS select_statement]
```

**参数说明**

CLUSTERED BY、SORTED BY以及INTO number_of_buckets BUCKETS子句的相关说明如下。

**CLUSTERED BY**

CLUSTERED BY子句用于指定Hash Key，MaxCompute将对指定列进行Hash运算，按照Hash值分散到各个Bucket里面。为避免数据倾斜和热点，取得较好的并行执行效果，CLUSTERED BY列适宜选择取值范围大、重复键值少的列。此外，为了达到Join优化的目的，也应该考虑选取常用的Join/AggregationKey， 即类似于传统数据库中的主键。

**SORTED BY**

SORTED BY子句用于指定在Bucket内字段的排序方式，建议SORTED BY和CLUSTERED BY一致，以取得较好的执行效果。此外，当SORTED BY子句指定之后，MaxCompute将自动生成索引，并且在查询的时候利用索引来加快执行。

**INTO number_of_buckets BUCKETS**

INTO number_of_buckets BUCKETS子句指定哈希桶的数目，这个数目必须提供，但需要您根据数据量大小来决定数值。Bucket越多并发度越大，Job整体运行时间越短；但同时，如果Bucket太多的话，可能导致小文件太多，另外并发度过高也会造成CPU时间的增加。因此，推荐设置每个Bucket数据大小在500 MB ~ 1 GB之间，如果是特别大的表，这个数值可以根据实际情况再调大一些。 目前，MaxCompute只能在Bucket Number完全一致的情况下去掉Shuffle步骤。需要注意，Bucket Number最大不能超过4096，否则可能会影响性能以及资源使用。 对于Join优化的场景，两个表的Join操作如果要去掉Shuffle和Sort步骤，通常要求哈希桶数目要一致。如果按照上述原则计算两个表的哈希桶数不一致时，通常建议统一使用数字大的Bucket Number，这样可以保证合理的并发度和执行效率。如果表的大小的确相差太远，那么在Bucket Number设置上，可以采用倍数关系，例如1024和256，可以利用数据特性进行优化。

##### 使用示例

普通表建表示例如下。

```
CREATE TABLE t1 (a string, b string, c bigint) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS;
```

分区表建表示例如下。

```
CREATE TABLE t2 (a string, b string, c bigint) PARTITIONED BY (dt string) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS;
```

大数据计算服务

##### 更改表属性

本文为您介绍如何更改Hash聚簇表的表属性。 对于分区表，MaxCompute支持通过ALTER TABLE语句来增加或去除Hash聚簇表的表属性。

```
 [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_na
me [ASC | DESC] ...])] INTO number_of_buckets BUCKETS] ALTER TABLE table_name NOT CLUSTERED;
```

**注意事项**

ALTER TABLE改变聚簇属性，只对于分区表有效，非分区表一旦聚簇属性建立就无法改变。 ALTER TABLE只会影响分区表的新建分区（包括Insert Overwrite生成的分区），新分区将按新的聚簇属性存储，老的数据分区保持不变。 总体来说，ALTER TABLE语句适用于存量表，在增加了新的聚簇属性之后，新的分区将进行Hash聚簇存储。

##### 表属性显示验证

**查看表属性**

```
DESC EXTENDED table_name;
```

Hash聚簇表的表属性将显示在Extended Info里面，如下图所示。

**查看分区属性**

对于分区表，除了可以使用上面的命令查看Table属性外，也可以通过如下命令查看分区的属性。

```
DESC EXTENDED table_name PARTITION(pt_spec);
```

大数据计算服务 Hash聚簇表的分区属性显示如下。

#### Hash Clustering的其他优点

##### Bucket Pruning和Index优化

**优化说明**

针对如下的查询示例。

```
CREATE TABLE t1 (id bigint, a string, b string) CLUSTERED BY (id) SORTED BY (id) into 1 000 BUCKETS; ... SELECT t1.id, t1.a, t1.b FROM t1 WHERE t1.id=12345;
```

对于普通表，上述示例中的查询通常意味着全表扫描操作，如果在表非常大的情况下，资源消耗量是非常可观的。但是，如果我们对**id**做Hash Shuffle处理，并且对**id**做排序，那么对应的查询可以大大简化，示例流程如下。
1. 通过查询值**12345**找到对应的Hash Bucket，此次的查询只需要在1个Bucket里面扫描，而不是全部
1000个。我们称之为**Bucket Pruning**。
2. 因为在Bucket内，数据按ID排序存放，MaxCompute会自动创建Index，利用Index Lookup直接定位
到相关记录。 从示例流程中可以看出，简化后不仅大大减少了Mapper的个数，并且由于利用了Index，Mapper可以直接定位到数据所在Page，加载读入的数据量也大大地减少了。

##### Aggregation优化

**优化说明**

针对如下的查询示例。

```
SELECT department, SUM(salary) FROM employee GROUP BY (department);
```

大数据计算服务在通常情况下，我们会对**department**进行Shuffle和Sort操作，然后做Stream Aggregate，统计每一个**department group**。但是如果表数据已经 `CLUSTERED BY (department) SORTED BY` `(department)` ，那么这个Shuffle和Sort的操作，可以相应节省掉。

##### 存储优化

本文为您介绍Hash聚簇功能带来的存储优化。

**优化说明**

即便不考虑以上所述的各种计算上的优化，只是把表Shuffle、并进行排序存储，也会对于存储空间节省上有很大帮助。因为MaxCompute底层使用列存储，通过排序，键值相同或相近的记录存放到一起，对于压缩和编码都会更加友好，从而使得压缩效率更高。在某些极端情况下，排序存储的表可以比无序表的存储空间节省50%。因此，对于生命周期很长的表，使用Hash聚簇存储，是一个很值得考虑的优化。 下图中是一个简单的实验示例，使用100G TPC-H lineitem表，包含了INT、DOUBLE以及STRING等多种数据类型，在数据和压缩方式等完全一样的情况下，使用Hash聚簇存储的表空间节省了约10%。 大数据计算服务

#### Shuffle Remove场景

**操作说明**

基于Range聚簇表的Join和Aggregate，当Join Key或Group Key是Range聚簇表的Key或其前缀的时候，消除数据的重分布，即Shuffle Remove，提升执行效率。
**使用方式**：通过Flag `odps.optimizer.enable.range.partial.repartitioning` 进行开关，默认关
闭。 两个Hash聚簇表相Join的时候，如果Bucket数目不同，但是两者的Bucket数目是倍数关系的时候，消除数据的重分布，进而提升执行效率。
**使用方式**：通过Flag `odps.optimizer.enable.hash.partial.repartitioning` 进行开关，默认打
开。 添加Correlated Shuffle Remove的功能，当数据满足分布，但不满足排序要求的时候，通过添加Sort 算子来避免数据的重分布。

#### 功能限制

本文为您介绍MaxCompute Hash聚簇功能的使用限制。

##### 使用限制

Hash聚簇功能存在如下的使用限制： 不支持INSERT INTO，只能通过INSERT OVERWRITE来添加数据。 大数据计算服务不支持小文件合并。由于区域聚集在切分的时候已经尽量保证数据在各个Bucket里面均匀分布，所以通常不存在小文件的问题。而直接的文件Merge将破坏区域聚集属性。但是，依然支持通过Merge和 ARCHIVE命令来改变表文件存储格式，以及RAID文件转换的功能。 由于Tunnel上传数据是无序的，因此不支持Tunnel直接Upload到Range聚簇表。

### MaxCompute常用SQL参数设置

#### Map设置

本文介绍MaxCompute中用于控制Map Task资源与输入分片的常用SET参数。合理调整这些参数可优化作业性能、避免数据倾斜或资源浪费。

**设置CPU数目**

###### 使用说明

设定处理Map Task每个Instance的CPU数目，默认值为100。[50，800]之间调整。

**SET命令**

```
SET odps.sql.mapper.cpu=100;
```

**设置Memory大小**

###### 使用说明

设定Map Task每个Instance的Memory大小，单位MB，默认值为1024 MB。[256，12288]之间调整。

**SET命令**

```
SET odps.sql.mapper.memory=1024;
```

**设置文件合并阈值**

###### 使用说明

设定控制文件被合并的最大阈值，单位MB，默认值为64 MB。您可以通过控制这个变量，从而达到对 Map端输入的控制。[0，Integer.MAX_VALUE]之间调整。

**SET命令**

```
SET odps.sql.mapper.merge.limit.size=64;
```

**设置MAP输入量**

###### 使用说明

设定一个Map的最大数据输入量，单位MB，默认256 MB。您可以通过控制这个变量，从而达到对Map 端输入的控制。[1，Integer.MAX_VALUE]之间调整。

**SET命令**

```
SET odps.sql.mapper.split.size=256;
```

#### Join设置

本文介绍MaxCompute中用于控制Join Task资源配置的常用SET参数。

###### 使用说明

大数据计算服务设定Join Task的Instance数量，默认值为-1。[0，2000]之间调整。

**SET命令**

```
SET odps.sql.joiner.instances=-1;
```

**设置CPU数目**

###### 使用说明

设定Join Task每个Instance的CPU数目，默认值为100。[50，800]之间调整。

**SET命令**

```
SET odps.sql.joiner.cpu=100;
```

**设置Memory大小**

###### 使用说明

设定Join Task每个Instance的Memory大小，单位为MB，默认值为1024 MB。[256，12288]之间调整。

**SET命令**

```
SET odps.sql.joiner.memory=1024;
```

#### Reduce设置

本文介绍MaxCompute中用于控制Reduce Task资源配置的常用SET参数。

###### 使用说明

设定Reduce Task的Instance数量，默认值为-1。[0，2000]之间调整。

**SET命令**

```
SET odps.sql.reducer.instances=-1;
```

**设置CPU数目**

###### 使用说明

设定处理Reduce Task每个Instance的CPU数目，默认值为100。[50，800]之间调整。

**SET命令**

```
SET odps.sql.reducer.cpu=100;
```

**设置Memory大小**

###### 使用说明

设定Reduce Task每个Instance的Memory大小，单位MB，默认值1024 MB。[256，12288]之间调整。

**SET命令**

```
SET odps.sql.reducer.memory=1024;
```

#### UDF设置

大数据计算服务本文介绍MaxCompute中用于控制UDF执行行为的常用SET参数。

**设置CPU数目**

###### 使用说明

设定UDF JVM Heap使用的最大内存，单位MB，默认值为1024 MB。[256，12288]之间调整。

**SET命令**

```
SET odps.sql.udf.jvm.memory=1024;
```

**设置超时时间**

###### 使用说明

设置UDF超时时间，单位秒，默认值为600秒。[0，3600]之间调整。

**SET命令**

```
SET odps.sql.udf.timeout=600;
```

**设置最大内存**

###### 使用说明

设定UDF Python使用的最大内存，单位MB，默认值为256 MB。[64，3072]之间调整。

**SET命令**

```
SET odps.sql.udf.python.memory=256;
```

**设置结果复用**

###### 使用说明

开启后，相同的UDF函数表达式，只计算一次，可以提高性能，默认值为True。

**SET命令**

```
SET odps.sql.udf.optimize.reuse=true/false;
```

**设置严格模式**

###### 使用说明

控制某些函数在遇到脏数据时是返回NULL还是报错，True是报错，False是返回NULL。

**SET命令**

```
SET odps.sql.udf.strict.mode=false/true;
```

#### MapJoin设置

**设置最大内存**

###### 使用说明

设置MapJoin时小表的最大内存，单位MB，默认值为512 MB。

**SET命令**

```
SET odps.sql.mapjoin.memory.max=512;
```

大数据计算服务

**设置启用Reshuffle**

###### 使用说明

动态分区某些场景很慢，关闭可以加快SQL速度。 如果动态分区值很少，关闭后可以避免出现数据倾斜。

**SET命令**

```
SET odps.sql.reshuffle.dynamicpt=true/false;
```

#### 数据倾斜设置

**开启Group By优化**

###### 使用说明

开启Group By优化。

**SET命令**

```
SET odps.sql.groupby.skewindata=true/false;
```

**开启Join优化**

###### 使用说明

开启Join优化，必须设置**odps.sql.skewinfo**才有效。

**SET命令**

```
SET odps.sql.skewjoin=true/false;
```

**设置Join优化**

###### 使用说明

设置Join优化具体信息。

**SET命令**

```
SET odps.sql.skewinfo;
```

具体命令格式如下。

```
SET odps.sql.skewinfo=skewed_src:(skewed_key)[("skewed_value")]
```

##### 使用示例

针对单个字段单个倾斜数值。

```
SET odps.sql.skewinfo=src_skewjoin1:(key)[("0")];
```

针对单个字段多个倾斜数值。

```
SET odps.sql.skewinfo=src_skewjoin1:(key)[("0")("1")];
```

### MapReduce转SQL执行

大数据计算服务

#### 概述

#### 使用须知

MaxCompute提供了MapReduce编程接口，支持通过Java API编写MapReduce程序以处理平台数据。 MaxCompute支持将MapReduce作业自动转换为SQL执行。转换后，MapReduce作业即可利用 MaxCompute 2.0的新一代编译器、基于代价的优化器及向量化执行引擎，并持续复用SQL引擎在功能、性能和稳定性等方面的迭代优化成果。

**说明**

该功能具有以下特性： 不需要您对原接口和作业逻辑做任何改动。 仅支持MapReduce接口编写的MapReduce作业，即OpenMR作业类型的MapReduce作业。 支持输入源为视图。 支持输入源为外表。 支持TempFile读写。 支持Hash Clustering表的读写。 支持准实时模式执行小作业。

#### 本地运行设置

1. 下载最新的客户端压缩包到本地并完成配置。

**说明**

进入下载页面后，您可以在**其他资源**区域获取对应版本的MaxCompute客户端下载包。
2. 设置执行模式。
执行模式可以通过开关控制，默认使用原本的执行模式，即关闭模式（或lot模式）。关闭模式下，作业仍然使用原MapReduce执行，作业执行过程中不涉及到新版本的SQL编译器、优化器和新的执行引擎。 您可以通过两种方式打开开关，开关名称为**odps.mr.run.mode**，取值分别为**lot**、**sql**和**hybrid**。 第一种方式是通过Project级别全局性统一开关打开，针对所有作业有效，需要Project管理员申请打开。开关为**odps.mr.run.mode**，参数值设置为**hybrid**或**sql**，其中**hybrid**模式下的SQL执行不通过时，会回退到MapReduce模式去执行。**sql**模式下的SQL执行不通过，则会报错。 第二种方式是通过Set命令设置Session级控制，只针对当前作业有效，Session级设置也有如下两种方式。 在JAR语句前面添加Set语句，例如 set odps.mr.run.mode=hybrid; 。 通过Job设置，如下所示。

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

大数据计算服务其中，对于Project级别全局性统一开关，MaxCompute项目运维会随着产品上线逐步分多批默认打开。

#### DataWorks中运行设置

本章节为您介绍使用MapReduce转SQL执行功能时要进行的DataWorks中运行设置。 DataWorks中运行的作业，由MaxCompute和DataWorks运维统一更新，您不需更新客户端。 单作业打开开关。 您可以在自己的作业前增加Set参数，也可通过MapReduce作业中的Job设置参数，该方法对Session级别有效，只影响当前作业执行。 您可通过以下两种方式进行Session级设置： 在JAR语句前面添加Set语句，例如 set odps.mr.run.mode=hybrid; 。 通过Job设置，如下所示。

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

#### 查看运行详情

本章节为您介绍如何查看MapReduce转化的SQL以及SQL作业的运行详情。 您可以通过Logview、MaxCompute Studio等查看MapReduce转化的SQL以及SQL作业的运行详情。 Logview Xml。 打开Logview，单击页面中心的LOT节点，在客户端提交的Xml信息中，节点内容显示了MapReduce作业转化为的SQL作业。示例如下。 大数据计算服务

```
create temporary function mr2sql_mapper_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotMapperUDTF' using ; create temporary function mr2sql_reducer_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotReducerUDTF' using ;
 @sub_query_mapper :=
k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku_ ock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_i ge_version,v_currency_code FROM( mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku ttr,sku_price,sku_stock,sku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discou ,sku_image_version,currency_code ) as (k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku tock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_ age_version,v_currency_code) FROM ae_antispam.product_sku_tt_inc WHERE ds = "20180615" AND hh = "21" mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku ttr,sku_price,sku_stock,sku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discou ,sku_image_version,currency_code ) as (k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku tock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_ age_version,v_currency_code) FROM ae_antispam.product_sku ) open_mr_alias1
 DISTRIBUTE BY k_id SORT BY k_id ASC;
@sub_query_reducer := mr2sql_reducer_152955927079392291755(k_id,v_gmt_create,v_gmt_modified,v_product_id,v_ad n_seq,v_sku_attr,v_sku_price,v_sku_stock,v_sku_code,v_sku_image,v_delivery_time,v_sku_b k_order,v_sku_bulk_discount,v_sku_image_version,v_currency_code) as (id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code, u_image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code) FROM @sub_query_mapper; FROM @sub_query_reducer id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code,s _image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code ;
```

Logview Detail/Summary。 您可以看到Job的执行采用了新版本的执行引擎Execution Engine。

```
Job run mode: fuxi job Job run engine: execution engine
```

Logview Detail/JSONSummary。 区别于MapReduce的JSONSummary信息仅包含了简单的Map和Reduce输入输出信息。SQL的 JSONSummary可以查看SQL执行各阶段的详细信息，包含所有执行参数、逻辑计划、物理计划和执行大数据计算服务详情等。示例如下。

```json
 "midlots" :
```

[

```
[[odps_flighting.flt_20180621104445_step1_ad_quality_tech_qp_algo_antifake_wordbag_filt _bag_change_result_lv2_20, auctionid,word,match_word(3) {0, 1, 2}]]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$2], word=[$3], match_word=[$4]) OdpsLogicalTableFunctionScan(invocation=[[MR2SQL_MAPPER_152955294118813063732($0, $1) ]()], rowType=[RecordType(VARCHAR(2147483647) item_id, VARCHAR(2147483647) text, VARC HAR(2147483647) __tf_0_0, VARCHAR(2147483647) __tf_0_1, VARCHAR(2147483647) __tf_0_2)
```

`])`

```
[[ad_quality_tech.qp_algo_antifake_wordbag_filter_bag_change_lv2_20, item_id,text(2) {0, 1}]])
```

]

#### 操作分布式文件系统

**操作步骤**

1. 指定Volume文件。
指定Volume文件有如下两种方式： 通过工具类指定输入文件和输出文件。

```
com.aliyun.odps.mapred.utils.InputUtils.addVolume( new VolumeInfo([project,]inVolume,inPartition, "inLabel"), new JobConf()); com.aliyun.odps.mapred.utils.OutputUtils.addVolume( new VolumeInfo([project,]outVolume, outPartition, "outLabel"), new JobConf());
```

其中，**project**和**label**是可选的，默认为当前Project和Default_Label。多个输入和输出时通过**label**进行区分，访问别的Project的Volume文件时需要先进行授权操作。 直接通过参数指定输入输出的Volume及Partition，多个输入输出通过英文逗号（,）连接在一起。

```
set odps.sql.volume.input[/output].desc = [<project>.]<table>.<partition>[:<label>] ;
```

2. 在Map和Reduce中通过**context**对象调用如下方法，将数据写入到分布式文件系统，或者编写数据流输
入输出文件。

```
context.getOutputVolumeFileSystem();
```

### SQL输入输出字段映射分析

#### 功能简介

**输入输出字段映射分析功能介绍**

大数据计算服务输入输出字段映射分析功能，是指对一个SQL输出表的字段和输入表的字段进行映射关系分析。例如下面的 SQL。

```
SELECT key, SUM(value) AS total FROM src GROUP BY key;
```

通过MaxCompute的字段映射分析功能可以得到如下的映射结果。 SQL脚本共输出2列，分别是**key**和**total**。其中**key**对应了输入表的**src.key**这一列，而**total**对应了输入表的**src.value**这一列。

#### 使用说明

本章节为您如何使用输入输出字段映射分析功能，并提供参考示例。

**输出结果格式**

字段映射分析支持阅读格式（Humanreadable）和JSON格式，通过设置SQL Flag `set`

```
odps.sql.select.output.format=HumanReadable/json; 来指定。
```

**通过SDK进行字段映射分析**

示例如下。

```
Odps odps = initOdps();
```

`//`需要分析请使用`LineageTask`。

```
LineageTask task = new LineageTask("task_name", "select * from dual;");
```

`//`通过`SQL Flag`设置结果格式（可选）。

```
Map<String, String> settings = new LinkedHashMap<>(); settings.putIfAbsent("odps.sql.select.output.format", "json"); task.setProperty("settings", JSON.toJSONString(settings));
```

`//`提交到服务器进行字段映射分析。

```java
Instance instance = odps.instances().create(task); System.out.println(instance.getId()); String logView = odps.logview().generateLogView(instance, 72); System.out.println(logView); instance.waitForSuccess();
```

`//`获取结果。

```java
System.out.println(instance.getTaskResults().get("task_name"));
```

**通过Odpscmd进行字段映射分析**

示例如下。 命令行模式：使用**-X**参数进行字段映射分析。 大数据计算服务

```
./bin/odpscmd.bat -X D:\lineage.q
```

交互模式：进入Odpscmd的交互模式后，可以通过设置SQL Flag来执行字段映射分析模式，使用方法和提交SQL作业类似。

```
lineage_test>set odps.sql.task.mode=LINEAGE;
```

`--` 返回`OK`，继续执行下一命令。

```
odps@ lineage_test>set odps.sql.select.output.format=Humanreadable;
```

`--` 返回`OK`，继续执行下一命令。

```
lineage_test>select * from dual;
```

返回结果如下。

```
== Column Lineage Column : id Source Columns :
  test2.dual.id
```

### MaxCompute SQL常见问题及使用

**建议**

#### 数据倾斜

##### 概述

本文为您介绍MaxCompute SQL常见问题中的数据倾斜问题，并针对不同类型的数据倾斜提供解决方案。

###### 使用说明

通常，运行Job的Instance的Time、Input Records和Output Records参数的Min、Max和Avg三个值不平衡时（例如Max远大于Avg时），都可以判定已经出现了数据倾斜问题。通过查看Logview，也可以定位数据倾斜问题，如下图所示。 每个Task的**Long Tails**展示了该Task中出现数据倾斜的Instance。产生数据倾斜的根本原因是有个别 Instance处理的数据量远远超过其他Instance，以致于个别Instance的运行时间也远远超过其他Instance 的平均时间，从而导致整个Job的运行速度变慢。 SQL中不同类型的数据倾斜可以采用不同的方式来处理。下面各章节将针对不同的数据倾斜情况进行原因说明，并提供解决方案。 大数据计算服务

##### Group By倾斜

**问题分析及解决**

**可能原因**：由于Group By的Key分布不均匀，从而导致Reduce端的数据倾斜。
**解决方案**：可以在SQL执行前设置防Group倾斜的参数。

```
SET odps.sql.groupby.skewindata=true;
```

**说明**

一旦该参数设置为True，系统会在进行Shuffle Hash算法时自动加入随机因素，并通过引入一个新增Task来防止数据倾斜问题。

##### Distribute By倾斜

本文为您介绍数据倾斜问题中造成Distribute By倾斜的原因，并提供解决方案。

**问题分析及解决**

**可能原因**：通常是想对全表做全排序，采用常量来进行Distribute By，从而导致Reduce端的数据倾
斜。
**解决方案**：
Distribute By控制Map（读数据）的输出在Reducer中是如何划分的，如果不希望Reducer的内容存在重叠，或需要对同一分组的数据一起处理，您可以使用Distribute By来保证同组数据分发到同一个 Reducer中。使用SELECT的输出列别名，当SELECT某列如果没有指定列的别名，则列名会被作为列的别名。命令示例如下： `--`查询表`sale_detail`中的列`region`值并按照`region`值进行哈希分片。

```
SELECT region FROM sale_detail DISTRIBUTE BY region;
```

因此在选择Distribute By列的时候，值必须要足够分散，防止出现热点倾斜。

##### Join倾斜

**问题分析及解决**

**可能原因**：由于Join ON所在的Key分布不均匀（例如有个别Key在Join的多个表中有大量重复），从而导
致个别Join Instance中的数据量以接近笛卡尔积式的数据量暴增，造成数据倾斜。 如果Join的两边有一个是小表，可以把Join改成Map Join来处理。 倾斜的Key用单独的逻辑来处理。例如经常出现的一种情况是两边表ON的Key里有大量NULL数据导致了倾斜，此时需要在Join前先过滤掉NULL的数据或通过Case When将NULL值替换为某种随机值，然后再进行Join。 如果不想更改SQL，可以通过设置如下参数让MaxCompute自动做优化。

```
SET odps.sql.skewinfo=tab1:(col1,col2)[(v1,v2),(v3,v4),...]; SET odps.sql.skewjoin=true;
```

大数据计算服务

##### Multi-Distinct倾斜

本文为您介绍数据倾斜问题中造成Multi-Distinct倾斜的原因，并提供解决方案。

**问题分析及解决**

**可能原因**：多个Distinct会放大Group By数据倾斜问题。
**解决方案**：通常避免使用Multi-Distinct，可以采用两层Group By来平缓数据倾斜问题。

##### 误用动态分区导致的数据倾斜

**问题分析及解决**

**可能原因**：在使用动态分区的场景下，如果有K个Map Instance和N个目标分区，可能产生K * N的小文
件数，过多的小文件会对文件系统造成巨大的管理压力。所以，在默认情况下如下设置是生效的。

```
SET odps.sql.reshuffle.dynamicpt=true;
```

即它会引入额外一级ReduceTask，相同的目标分区交由同一个（或少量几个）Reduce Instance来写入，从而避免小文件过多。但是Dynamic Partition Shuffle可能会导致数据倾斜。
**解决方案**：如果目标分区数比较少，根本不会造成小文件过多的困扰时，可以通过如下命令关闭上述功
能，避免Dynamic Partition Shuffle导致的数据倾斜。

```
SET odps.sql.reshuffle.dynamicpt=false;
```

如果分区数较多，无法避免小文件过多问题时，建议不使用动态分区。

##### Skew Join Hint避免热值倾斜

本文为您介绍数据倾斜问题中如何通过Skew Join Hint避免热值倾斜，并提供参考示例。

**使用方法**

方法一：Hint表名。需要注意，Hint的是表的Alias。示例如下。

```
SELECT /*+ skewjoin(a) */ * FROM T0 a JOIN T1 b ON a.c0 = b.c0 AND a.c1 = b.c1;
```

方法二：Hint表名和认为可能产生倾斜的列，下面的示例认为a的**c0**和**c1**列存在数据倾斜。

```
SELECT /*+ skewjoin(a(c0, c1)) */ * FROM T0 a JOIN T1 b ON a.c0 = b.c0 AND a.c1 = b.c 1 AND a.c2 = b.c2;
```

方法三：Hint表名和列，并提供发生倾斜的Key值。需要注意，如果是STRING类型，需要加上引号。下面的示例认为**(a.c0=1 and a.c1="2")**和**(a.c0=3 and a.c1="4")**的值都存在数据倾斜。

```
SELECT /*+ skewjoin(a(c0, c1)(("1", "2"), ("3", "4"))) */ * FROM T0 a JOIN T1 b ON a. c0 = b.c0 AND a.c1 = b.c1;
```

**使用方法的区别说明**

直接指定**skewvalue**（即方法三）的效率比不指定（即方法一和方法二）的高。 配合Analyze和Freeride收集Topk，可能不需要设置Hint也能自动生效SkewJoin。

##### 使用示例

大数据计算服务

**定位倾斜Join**

1. 以如下Logview为例，耗时最大Fuxi Task的为J5。
2. 选中J5_3_4后，观察J5的Instances，可以看到**J5_3_4#215_0**的耗时最长，且I/O record和I/O Bytes
大数据计算服务
3. 因此认为J5_3_4节点发生了数据倾斜，此时需要确定倾斜的是哪个Join。可以打开倾斜Instance的
StdOut（上图黄色框选的地方）和任一个不倾斜节点的StdOut，会显示下图，大多数情况下网页无法显示所有Stdout的内容，可以单击**Download**，下载后查看全部内容。
4. Download的内容如下图所示，可以看到倾斜Instance的StreamLineRead7的**read count**远远大于非
倾斜Instance，因此可以认为StreamLineWrite7到SreamLineRead7的这个Shuffle发生了倾斜。 大数据计算服务
5. 此时，再回到DAG图，可以在下图界面，鼠标右键选择**expland all**，即可以找到StreamLineWrite7
和StreamLineRead7。 大数据计算服务
6. 可以看到MergeJoin2发生了倾斜，倾斜的是MergeJoin2的StreamLineRead7这一路。此时，可以进一
步追溯StreamLineRead7的输入节点，可以看到是**dim_hm_item**和**dim_tb_itm_brand**进行Join之后的结果，再与StreamLine4（追溯Input后发现是**dim_tb_brand**表）进行Join，即MergeJoin2。 大数据计算服务

**修改问题SQL**

根据上一步骤中的相关表名，回到SQL中定位，确认是**left outer join**发生了倾斜，而倾斜的是t1这个表，因此，在SQL中添加如下命令即可。

```
/*+ skewjoin(t1) */
```

大数据计算服务

**注意事项**

支持的Join类型：Inner Join可以对Join两侧表中的任意一侧进行Hint；Left Join、Semi Join和Anti Join 只可以Hint左侧表；Right Join只可以Hint右侧表；Full Join不支持Skew Join Hint。 建议只对一定会出现数据倾斜的Join添加Hint，因为Hint会运行一个Aggregate，存在一定代价。 被Hint的Join的Left Side Join Key的类型需要与Right Side Join Key的类型一致，否则Skew Join Hint 不生效。 添加Hint后，Optimizer会运行一个Aggregate动态获取重复行数前20的热值。这个20是一个默认值， 可以通过添加如下Flag进行设置进行设置。

```
SET odps.optimizer.skew.join.topk.num = xx;
```

只支持对Join其中一侧进行Hint。 被Hint的Join一定要**left key** 等于**right key**，不支持笛卡尔积Join。 与其他Hint一起使用的方法时，需要注意，被Map Join Hint的Join不能再被Skew Join Hint。 可以在Logview的Json Summary中搜索是否出现**topk_agg**字段来判断Skew Join Hint是否生效。

#### 计算资源不足问题

本文为您介绍MaxCompute SQL常见问题中的计算资源不足问题，并提供解决方案。

**资源不足特征**

大数据计算服务在使用MaxCompute的时候，有时候会遇到计算资源不足的问题，涉及到对集群资源的规划和使用方式。 计算资源不足的作业通常有如下两个特征： 首先，作业输出一直停留在某个阶段，进度停滞不前。例如在下图中，作业中的M1_Stg1的完成百分比一直停留在0%（R2_1_Stg1由于依赖于M1_Stg1，所以在M1_Stg1完成前，其进度也会一直停留在 0%）。 其次，通过Logview（如下图所示），可以看到Task的Instance会一直处于**Ready**状态。该状态表明， 目前没有资源来运行这些随时待命的Task实例。一旦实例获得资源，就会转变为**Running**状态开始运行。注意区别于**Waiting**状态，**Waiting**状态表明在等待依赖任务的完成，而**Ready**状态是在等待资源的分配。

**原因分析**

大数据计算服务每个作业都会根据执行计划拆分成由多个Task组成的DAG图，而每个Task又会起多个Instance来并发执行计算任务。通常起一个Instance需要的资源是1核CPU和2 GB内存。为了合理分配资源，会为每个Project 分配一个Quota组，所属Quota组决定了该Pproject中所有作业同时可以使用的资源上限（CPU和内存）。 一旦同时运行的作业的资源使用量达到了Quota组的可用上限，就会出现因资源不足而导致的作业停滞的情况。

**解决方式**

解决该问题通常有如下两种方式： 让作业避开高峰，在空闲时间段运行。

#### MaxCompute储存优化技巧

**合理设置分区表**

MaxCompute支持分区表的概念，分区表指的是在创建表时指定的Partition的分区空间，即指定表内的某几个字段作为分区列。在多数情况下，您可以将分区类比为文件系统下的目录。MaxCompute将分区列的每个值作为一个分区（目录）。您可以指定多级分区，即将表的多个字段作为表的分区，分区之间类似多级目录的关系。在使用数据时如果指定了需要访问的分区名称，则只会读取相应的分区，避免全表扫描，提高处理效率，降低费用。

**分区示例**

```
CREATE TABLE src (key string, value bigint) PARTITIONED BY (pt string); SELECT * FROM src WHERE pt='20160901';
```

`--` 指定正确的分区格式，`MaxCompute`在生成查询计划时只会将`20160901`分区的数据纳入输入中。

**未分区示例**

```
SELECT * FROM src WHERE key = 'MaxCompute';
```

`--` 查询计划会扫描全表数据。

**分区设置示例**

常见的分区设置方式有根据日期或地区（国家）设置，也可以根据业务需要自行设置。示例如下。

```
shop_name string, customer_id string, total_price double) PARTITIONED BY (sale_date string,region string);
```

`--` 创建一个二级分区表，第一级分区`sale_date`是日期，第二级分区`region`是地区。

**合理设置表的生命周期**

MaxCompute平台中存储资源是非常宝贵的。您可以根据数据本身的使用情况，对表设置生命周期，MaxCompute会及时删除超过生命周期的数据，达到节省存储空间的目的。 示例如下。

```
CREATE TABLE test3 (key boolean) PARTITIONED BY (pt string, ds string) lifecycle 100;
```

`--` 创建一张生命周期为`100`的表。如果这张表或分区的最后修改时间超过了`100`天将会被删除。 大数据计算服务

**重要**

生命周期是以分区为最小单位的，所以针对一个分区表，如果部分分区达到了生命周期的阈值，那么这些分区会被直接删掉，未达到生命周期阈值的分区不受影响。 另外可以通过如下命令，修改已经创建好的表的生命周期。

```
ALTER TABLE table_name SET lifecycle days;
```

#### UDF OOM问题

本文为您介绍MaxCompute SQL常见问题中的UDF OOM问题，并提供解决方案。

**常见问题**

某些Job在运行时会报OOM的问题，报错信息如下。

```
FAILED: ODPS-0123144: Fuxi job failed - WorkerRestart errCode:9,errMsg:SigKill(OOM), us ually caused by OOM(out of memory)
```

**解决方案**

上述问题可以尝试通过设置UDF运行时的参数解决，如下所示。

```
SET odps.sql.mapper.memory=3072; SET odps.sql.udf.jvm.memory=2048; SET odps.sql.udf.python.memory=1536;
```

### MaxCompute SQL限制项汇总

**限制说明**

| 限制项 | 最大值/限制条件 | 分类 | 说明 |
|---|---|---|---|
| 表名长度 | 128字节 | 长度限制 | 表名、列名中不能有特殊字符，以字母开头，且只能用英文小写字母（a-z）、英文大写字母（A-Z）、数字和下划线（ ）。 _ |
| 注释长度 | 1024字节 | 长度限制 | 长度不超过1024字节的有效字符串。 |
| 表的列定义 | 1200个 | 数量限制 | 单表的列定义个数最多为1200个。 |
| 单表分区数 | 60000个 | 数量限制 | 单表的分区个数最多为60000个。 |

大数据计算服务

| 表的分区层级 | 6级 | 数量限制 | 在表中创建的分区层次不能超过6级。 |
|---|---|---|---|
| INSERT 目标个数 | 256个 | 数量限制 | MULTI-INSERT 场景，目标表的数量限制为256个。 |
| UNION ALL | 256个 | 数量限制 | UNION ALL 场景，最多允许合并256个表。 |
| MAPJOIN | 128个 | 数量限制 | MAPJOIN 场景，最多允许连接128个小表。 |
| MAPJOIN 内存限制 | 512 MB | 长度限制 | MAPJOIN 场景，所有小表的内存不能超过512 MB。 |
| 窗口函数 | 5个 | 数量限制 | 单个SELECT语句中最多允许存在5个窗口函数。 |
| ptinsubq | 1000行 | 数量限制 | 子查询中存在分区列时，子查询的返回结果不能超过 1000行。 |
| SQL语句长度 | 2 MB | 长度限制 | SQL语句的最大长度为2 MB。包括您使用SDK调用SQL 的场景。 |
| WHERE 子句条件个数 | 256个 | 数量限制 | WHERE 子句中的条件个数最大为256个。 |
| 列记录长度 | 8 MB | 长度限制 | 表中单个单元的最大长度为8 MB。 |
| IN的参数个数 | 1024 | 数量限制 | IN的最大参数限制，例如 in (1,2,3….,1024) 。如果 in(…) 的参数过多，会影响编译性能。1024为建议值，不是限制值。 |
| jobconf.json | 1 MB | 长度限制 | jobconf.json 的大小为1 MB。当表包含的分区数量较多时，大小可能超过 jobconf.json ，超过1 MB。 |
| 视图 | 不可写 | 操作限制 | 视图不支持写入，不支持 INSERT 操作。 |
| 列的数据类型 | 不可修改 | 操作限制 | 不允许修改列的数据类型及列位置。 |

大数据计算服务

| Java UDF函数 |  | 不允许为 ABSTRACT 或者 STATIC 。 | 操作限制 | Java UDF函数不能为 ABSTRACT 或 STATIC 。 |  |  |
|---|---|---|---|---|---|---|
| 最多查询分区个数 |  | 10000个 | 数量限制 | 最多查询分区个数不能超过10000个。 |  |  |
| SQL执行计划长度 |  |  | 长度限 | MaxCompute SQL生成的执行计划不能超过1 MB，否则会触发 FAILED: ODPS-0010000:System |  |  |
|  |  |  |  |  | FAILED: ODPS-0010000:System |  |
|  |  | 1 MB | 制 | internal error - The Size of Plan is too |  |  |
|  |  |  |  | large |  |  |

**重要**

### 附录

#### 转义字符

**转义字符列表**

在MaxCompute SQL中，反斜线（\）即为转义符，用来表达字符串中的特殊字符或将其后跟随的字符解释为其本身。当读入字符串常量时，如果反斜线（\）后跟随三位有效的8进制数字，范围在001 ~177之间， 系统会根据ASCII值转换为相应的字符。对于如下表所示的情况，则会将其解释为特殊字符。

| 转义 | 字符 |
|---|---|
| \b | 退格（backspace），将当前位置移到前一列。 |
| \t | 水平制表（tab）。 |
| \n | 换行（newline），将当前位置移到下一行开头。 |
| \r | 回车（carriage-return），将当前位置移到本行开头。 |
| \’ | 单引号。 |
| \” | 双引号。 |
| \ \ | 反斜线。 |

| 大数据计算服务 | 开发指南·MaxCompute SQ |
|---|---|

| \; | 分号。 |
|---|---|
| \Z | control-Z。 |
| \0或\00 | 结束符。 |

##### 使用示例

转义字符后字符解释为其本身。 MaxCompute SQL中的字符串常量可以用单引号（' '）或双引号（'' ''）表示。您可以在单引号（' '）括起的字符串中包含双引号（'' ''），或在双引号（'' ''）括起的字符串中包含单引号（' '），否则要用转义符来表达。表达方式如下。

```
"I'm a happy manong." 'I\'m a happy manong.'
```

特殊字符。

```
SELECT length('a\tb');
```

`--` 运行结果为3。表示字符串里有三个字符，\t被视为一个字符。

```
SELECT 'a\ab',length('a\ab');
```

`--` 运行结果为`aab`，3。\a被解释成了普通的a。

#### LIKE字符匹配

###### 使用说明

在LIKE匹配时，百分号（%）表示匹配任意多个字符，下划线（_）表示匹配单个字符。

##### 使用示例

如果要匹配百分号（%）或下划线（_）本身，则要对其进行转义，**\\%**匹配字符%，**\\_**匹配字符_。 大数据计算服务

```
SELECT 'abcd' LIKE 'ab%' ;
```

`--` 返回结果

```
+-------+
| _c0   |
+-------+
| true  |
+-------+ SELECT 'abcd' LIKE 'ab_' ;
```

`--`返回结果

```
+-------+
| _c0   |
+-------+
| false |
+-------+ SELECT 'ab_cde' LIKE 'ab\\_c%';
```

`--`返回结果

```
+-------+
| _c0   |
+-------+
| true  |
+-------+
```

**说明**

目前MaxCompute SQL支持UTF-8的字符集。如果数据是以其他格式编码，可能会导致计算结果不正确。

#### 正则表达式规范

#### 使用须知

MaxCompute SQL中的正则表达式采用的是PCRE的规范，匹配时按字符进行。

**RLIKE**

您可以使用RLIKE语句匹配正则表达式，支持的元字符如下表所示。

| 元字符 | 说明 |
|---|---|
| ^ | 行首。 |
| $ | 行尾。 |

大数据计算服务

| . | 任意字符。 |  |  |
|---|---|---|---|
| * | 匹配0次或多次。 |  |  |
| + | 匹配1次或多次。 |  |  |
| ? | 匹配0次或1次。 匹配修饰符，当该字符跟在任何一个其他限制符（ *、+、?、 {n}、 {n,}、 {n,m} ）后面时，匹配模式为非贪婪模式。非贪婪模式尽可能少地匹配所搜索的字符串，而默认的贪婪模式则尽可能多地匹配所搜索的字符串。 |  |  |
|  |  | *、+、?、 {n}、 {n,}、 |  |
| A\|B | A或B。 |  |  |
| (abc)* | 匹配abc序列0次或多次。 |  |  |
| {n}或{m,n} | 匹配的次数。 |  |  |
| [ab] | 匹配括号中的任一字符。模式匹配a或b。 |  |  |
| [a-d] | 匹配a、b、c、d任一字符。 |  |  |
| [^ab] | ^表示非，匹配任一非a非b的字符。 |  |  |
| [::] | 见下表POSIX字符组。 |  |  |
| \ | 转义符。 |  |  |
| \n | n为数字1~9，后向引用。 |  |  |
| \d | 匹配一位数字。 |  |  |
| \D | 匹配除数字以外的任意字符。 |  |  |

|  | {n,m} |
|---|---|

**POSIX字符组**

| POSIX字符组 | 说明 | 范围 |
|---|---|---|
| [[:alnum:]] | 字母字符和数字字符 | [a-zA-Z0-9] |

大数据计算服务

| [[:alpha:]] | 字母 | [a-zA-Z] |
|---|---|---|
| [[:ascii:]] | ASCII字符 | [\x00-\x7F] |
| [[:blank:]] | 空格字符和制表符 | [ \t] |
| [[:cntrl:]] | 控制字符 | [\x00-\x1F\x7F] |
| [[:digit:]] | 数字字符 | [0-9] |
| [[:graph:]] | 空白字符之外的字符 | [\x21-\x7E] |
| [[:lower:]] | 小写字母字符 | [a-z] |
| [[:print:]] | [:graph:]和空白字符 | [\x20-\x7E] |
| [[:punct:]] | 标点符号 | [][!”#$%&’()*+,./:;<=>? @\^ `{\|}~-] _ |
| [[:space:]] | 空白字符 | [ \t\r\n\v\f] |
| [[:upper:]] | 大写字母字符 | [A-Z] |
| [[:xdigit:]] | 十六进制字符 | [A-Fa-f0-9] |

**转义符**

| 字符串 | a+b |  |
|---|---|---|
| a\\+b |  |  |
|  |  | 。由 |

是 a\\\+b 。 示例如下，假设存在表test_dual。

```
SELECT 'a+b' rlike 'a\\\+b';
```

`--` 返回结果

```
+------+
| _c1  |
+------+
| true |
+------+
```

极端的情况，如果要匹配反斜线（\），由于在正则引擎中反斜线（\）是一个特殊字符，因此要表示为**\\**， 而系统还要对表达式进行一次转义，因此写成**\\\**。 大数据计算服务

```
SELECT 'a\\b', 'a\\b' rlike 'a\\\b';
```

`--` 返回结果

```
+------+------=+
| _c0  | _c1   |
+------+------=+
| a\b  | false |
+------+------=+
```

**说明**

在MaxCompute SQL中写 a\\b ，而在输出结果中显示 a\b ，同样是因为MaxCompute会对表达式进行转义。 如果字符串中有制表符TAB，系统在读入 \t 这两个字符时，已经将其存为一个字符，因此在正则的模式中它也是一个普通的字符。

```
SELECT 'a\tb', 'a\tb' rlike 'a\tb';
```

`--` 返回结果

```
+---------+------+
| _c0     | _c1  |
+---------+------+
| a     b | true |
+---------+------+
```

#### 保留字和关键字

**保留字与关键字介绍**

**重要**

命名表、列或分区时，不要使用保留字与关键字，否则可能会报错。 保留字、关键字都不区分大小写。

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
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
|BIGINT
|BLOB
|BOOLEAN
|BOTH
```

|
大数据计算服务

```
| BIGINT        | BINARY              | BLOB          | BOOLEAN      | BOTH            |
+---------------+---------------------+---------------+--------------+-----------------+
| BUCKET        | BUCKETS             | BY            | CASCADE      | CASE            |
+---------------+---------------------+---------------+--------------+-----------------+
| CAST          | CFILE               | CHANGE        | CLUSTER      | CLUSTERED       |
+---------------+---------------------+---------------+--------------+-----------------+
| CLUSTERSTATUS | COLLECTION          | COLUMN        | COLUMNS      | COMMENT         |
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
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
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
| GRANT         | GROUP               | HAVING        | HOLD_DDLTIME | IDXPROPERTIES   |
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
| INPATH        | INPUTDRIVER         | INPUTFORMAT   | INSERT       | INT             |
+---------------+---------------------+---------------+--------------+-----------------+
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
```

大数据计算服务

```
+---------------+---------------------+---------------+--------------+-----------------+
| RECORDREADER  | RECORDWRITER        | REDUCE        | REGEXP       | RENAME          |
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
| RLIKE         | ROW                 | ROWS          | SCHEMA       | SCHEMAS         |
+---------------+---------------------+---------------+--------------+-----------------+
| SELECT        | SEMI                | SEQUENCEFILE  | SERDE        | SERDEPROPERTIES |
+---------------+---------------------+---------------+--------------+-----------------+
| SET           | SHARED              | SHOW          | SHOW_DATABASE| SMALLINT        |
+---------------+---------------------+---------------+--------------+-----------------+
| SORT          | SORTED              | SSL           | STATISTICS   | STATUS          |
+---------------+---------------------+---------------+--------------+-----------------+ +---------------+---------------------+---------------+--------------+-----------------+
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

#### 新数据类型设置说明

**注意事项**

为了缓解因为新数据类型Flag设置过多难以使用的问题，SQL读新数据类型表时，不要求必须设置前面章节中提及的Flag setodps.sql.type.system.odps2=true; ，但需要注意以下几点。 在不设置新数据类型Flag的情况下，读出来的数据会被隐式转换为旧数据类型来进行所有计算。 整型常量在不设置新数据类型Flag的情况下，依然使用BIGINT类型，通过报错信息来提示。 写表时，如果新类型的数据仅仅是Passthrough，也可以不设置新数据类型Flag。但是如果存在计算， 则会因为隐式转换不合法而报错。

#### MaxCompute并发写行为的ACID语义

本文为您介绍MaxCompute在作业并发情况下ACID的语义。

**相关术语**

操作：指在MaxCompute上提交的单个作业。 数据对象：指持有实际数据的对象，例如非分区表、分区。 INTO类作业：指INSERT INTO、DYNAMIC INSERT INTO等包含关键字INTO的SQL作业。 大数据计算服务 OVERWRITE类作业：指INSERT OVERWRITE、DYNAMIC INSERT OVERWRITE等包含关键字 OVERWRITE的SQL作业。 Tunnel数据上传：可以归结为INTO类或OVERWRITE类作业。

**ACID语义描述**

原子性（Atomicity）：一个操作或是全部完成，或是全部不完成，不会结束在中间某个环节。 一致性（Consistency）：从操作开始至结束的期间，数据对象的完整性没有被破坏。 隔离性（Isolation）：操作独立于其它并发操作完成。 持久性（Durability）：操作处理结束后，对数据的修改将永久有效，即使出现系统故障，该修改也不会丢失。

**MaxCompute的ACID特性**

原子性（Atomicity） 任何时候MaxCompute会保证在冲突时只会一个作业成功，其它冲突作业失败。 对于单个表或分区的CREATE、OVERWRITE、DROP操作，可以保证其原子性。 跨表操作时不支持原子性（例如MULTI-INSERT）。 在极端情况下，以下操作可能不保证原子性： `DYNAMIC INSERT OVERWRITE` 多于一万个分区，不支持原子性。 INTO类操作：这类操作失败的原因是事务回滚时数据清理失败，但不会造成原始数据丢失。 一致性（Consistency） OVERWRITE类作业可保证一致性。 INTO类作业在冲突失败后可能存在失败作业的数据残留。 隔离性（Isolation） 非INTO类操作保证读已提交。 INTO类操作存在读未提交的场景。 持久性（Durability） MaxCompute保证数据的持久性。

**Transactional表的ACID特性**

在已有的ACID特性基础上，INTO类操作保证读已提交，冲突失败后无数据残留。 支持单个非分区表或单个分区Update/Delete原子性。例如对于一个分区被两个Update作业并发修改时，只会有一个成功，不会存在一个作业部分Update分区成功，也不会存在一个分区被两个作业分别 Update成功，留下部分Update成功的数据。 操作并发冲突说明：当作业并发运行且写入目标表相同时，可能出现冲突。有冲突时，先结束的作业会成功，后结束的作业会因冲突而报错失败。 下表为作业并发提交场景下，作业先后结束写同一个非分区表或分区的冲突说明。第一列是先结束的作业类型，第一行是后结束的作业类型。

| Before/After | INSERT OVERWRITE后结束 | INSERT INTO后结束 | UPDATE/DELET E后结束 | MERGE SMALLFILES后结束 |
|---|---|---|---|---|

大数据计算服务

| INSERT OVERWRITE先结束 | 先后结束的作业都会成功。后结束的作业会覆盖先结束作业的数据。 | 先后结束的作业都会成功。INSERT INTO会追加在先结束的INSERT OVERWRITE结果数据上。 | 后结束的UPDATE 对应的非分区表或分区被先结束的 INSERT OVERWRITE修改。后结束的 UPDATE作业会报错。 | 后结束的MERGE SMALLFILES对应的非分区表或分区被先结束的INSERT OVERWRITE修改。后结束的 MERGE SMALLFILES作业会报错。 |
|---|---|---|---|---|
| INSERT INTO先结束 | 先后结束的作业都会成功。后结束的 INSERT OVERWRITE会覆盖掉先结束的 INSERT INTO。 | 先后结束的作业都会成功。两个 INSERT INTO结果会依次追加在一起。 | 后结束的UPDATE 对应的非分区表或分区被先结束的 INSERT INTO修改。后结束的 UPDATE作业会报错。 | 后结束的MERGE SMALLFILES对应的非分区表或分区被先结束的INSERT INTO修改。后结束的MERGE SMALLFILES作业会报错。 |
| UPDATE/DELETE 先结束 | 先后结束的作业都会成功。后结束的 INSERT OVERWRITE会覆盖掉先结束的 UPDATE。 | 先后结束的作业都会成功。INSERT INTO会追加在先结束的UPDATE结果数据上。 | 后结束的UPDATE 对应的非分区表或分区被先结束的 UPDATE修改。后结束的UPDATE作业会报错。 | 后结束的MERGE SMALLFILES对应的非分区表或分区被先结束的 UPDATE修改。后结束的MERGE SMALLFILES作业会报错。 |
| MERGE SMALLFILES先结束 | 先后结束的作业都会成功。后结束的 INSERT OVERWRITE会覆盖掉先结束的 MERGE SMALLFILES。 | 先后结束的作业都会成功。后结束的 INSERT INTO会追加在掉先结束的 MERGE SMALLFILES结果数据上。 | 后结束的UPDATE 对应的非分区表或分区被先结束的 MERGE SMALLFILES修改。后结束的 UPDATE作业会报错。 | 后结束的MERGE SMALLFILES对应的非分区表或分区被先结束的MERGE SMALLFILES修改。后结束的 MERGE SMALLFILES作业会报错。 |

可以用更简化的数据变化冲突表描述这个规则。

| 操作类型 | 数据变化后，作业是否会因冲突报错 |
|---|---|
| INSERT OVERWRITE | N |
| INSERT INTO | N |
| UPDATE/DELETE | Y |
| MERGE SMALLFILES | Y |

大数据计算服务即INSERT操作不因数据变化而冲突，UPDATE/DELETE和MERGE SMALLFILES会因目标非分区表或分区数据变化而报错。

**说明**

MINOR/MAJOR COMPACT归类为MERGE SMALLFILES作业类型。 在极端场景下，如果多个作业同时处于元数据更新阶段，可能因元数据更新本身并发冲突而报错。 大数据计算服务

## MaxCompute开源支持

本章节为您介绍MaxCompute相关的开源功能。

**SDK**

MaxCompute提供Java SDK接口和Python SDK接口，实现创建、查看和删除MaxCompute表等操作。 通过SDK，您可以通过编辑代码灵活地操作MaxCompute。 服务支持方式：您可以通过访问官方文档和在线提交工单的方式获取支持。

**MaxCompute RODPS**

MaxCompute R语言插件。具体使用说明请参见ODPS Plugin for R。 服务支持方式：在GitHub中的ODPS Plugin for R里留言或新建Issue。

**MaxCompute JDBC**

MaxCompute JDBC是MaxCompute官方提供的JDBC驱动，它向Java程序提供了一套执行SQL任务的接口。项目托管在GitHub中的ODPS JDBC。 服务支持方式：在GitHub中的ODPS JDBC里留言或新建Issue。

**Data Collector**

Data Collector是MaxCompute主要开源数据采集工具的集合，包括：Flume插件、OGG插件、Sqoop、 Kettle插件和Hive Data Transfer UDTF。 从上述数据采集工具的实现技术上来看，Flume插件和OGG插件是基于DataHub的SDK实现的，而 Sqoop、Kettle插件以及Hive Data Transfer UDTF是基于Tunnel的SDK实现的。DataHub和Tunnel分别是MaxCompute系统的实时数据通道和批量数据通道。Flume插件和OGG插件面向于实时数据传输，而 Sqoop、Kettle插件和Hive Data Transfer UDTF则适合用于离线批量的数据传输。 参考源代码请参见Aliyun MaxCompute Data Collectors，插件说明请参见wiki。 服务支持方式：在Github中的Aliyun MaxCompute Data Collectors里留言或新建Issue。
