---
title: "Lindorm Developer Guide 20250825"
product_version: "V3.18.6"
pdf_pages: 426
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Lindorm Developer Guide 20250825.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/Lindorm/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Lindorm%20Developer%20Guide%2020250825.pdf"
converter: line-classifier (PyMuPDF)
---

# Lindorm Developer Guide 20250825

| Method | Reference |
|---|---|
| Application development based on Lindorm SQL | Use Java JDBC API operations to develop applications |
|  | Use Python DB-API to develop applications |
|  | Sample code used to connect to LindormTable by using different Java frameworks |
| Application development based open source APIs | Use the HBase API to connect to and use LindormTable |

| Network type | Description |
|---|---|
| VPC (recommended) | A virtual private cloud (VPC) is a private network dedicated to your Alibaba Cloud account. VPCs are logically isolated from each other Layer 2 for high security. When Lindorm-cli is deployed on your Elastic Compute Service (ECS) instance, you can use Lindorm-cli to connect to LindormTable over a VPC. This ensures high security and reduces network latency. |

## LindormTable

### Connect to LindormTable

#### Overview

LindormTable allows you to develop your applications in multiple methods to meet the requirements of different business scenarios. The following table describes the methods that you can use to develop your applications based on LindormTable.

#### Use Lindorm-cli to connect to and use

## LindormTable

This topic describes how to use Lindorm-cli to connect to and use LindormTable.

**Prerequisites**

The endpoint that is required when you use SQL to connect to and use LindormTable has been obtained. For more information, see the **View endpoints** topic of **Instance management** in **Lindorm User**
**Guide**.

**Types of networks used to connect to LindormTable**

| Classic network | If you want to use an on-premises device to test or manage LindormTable, you can deploy Lindorm-cli on the device and connect the device to LindormTable over the classic network. Note You are not charged for traffic generated when you connect to LindormTable over the classic network. However, the connection may be exposed to security risks. We recommend that you use a VPC to ensure security. Classic network endpoint must be enabled in the console. For more information about how to enable the endpoint, see the Enable a classic network endpoint topic of Instance management in Lindorm User Guide. |
|---|---|

| Client OS | Download link |
|---|---|
| Linux | lindorm-cli for linux |
| Mac | lindorm-cli for mac |
| Windows | lindorm-cli for windows-x64 |

| Parameter | Sample value | Method used to obtain the parameter value |
|---|---|---|
| jdbc url | jdbc:lindorm:table:url=http:// ld-bp17j28j2y7pm****-proxy- lindorm- pub.lindorm.rds.aliyuncs.com :30060 | For more information about how to obtain the endpoint of LindormTable SQL, see the "View endpoints" topic of "Instance management" in Lindorm User Guide. |

**Common commands**

For more information about Lindorm SQL syntax, see LindormTable SQL.
**!help**: You can run this command to view help information.
**!connect**: You can run this command to connect to a server.
**exit**, **quit**, and **ctrl+d**: You can run one of these commands to exit the current connection.

**Procedures**

1. Download an installation package of Lindorm-cli. You can download an installation package of Lindorm-
cli that is suitable for the operating system of your client. The following table provides the download links.
2. Decompress the installation package of Lindorm-cli.
3. Obtain required connection information and connect to LindormTable.
If your client is deployed in Linux or macOS, go to the path in which Lindorm-cli is located and then run the following command:

```
./lindorm-cli -url <jdbc url> -username <username> -password <password>
```

If your client is deployed in Windows, go to the path in which Lindorm-cli.exe is located and then run the following command:

```
lindorm-cli -url <jdbc url> -username <username> -password <password>
```

| Username | root | If you forget your password, you can change the password in the cluster management system of LindormTable. For more information about how to change the password, see the "User management" topic of "LindormTable" in Lindorm User Guide. Important After you change your password, you must restart LindormTable in the Lindorm console. |
|---|---|---|
| Password | root |  |

If the connection is successful, the following result is returned:

```
Connected to jdbc:lindorm:table:url=http://ld-bp17j28j2y7pm****-proxy-lindormpub.lindorm.rds.aliyuncs.com:30060 lindorm-cli version: 1.0.24
```

4. The following example shows the SQL syntax that you can use to access LindormTable.
i. Execute the following statement to create a database named test:

```
create database test;
```

ii. Execute the following statement to use the test database:

```
use test;
```

iii. Execute the following statement to create a table named tb in the test database and insert a row of data to tb:

```
create table tb (id varchar, name varchar, address varchar, primary key(id, name)) ; upsert into tb (id, name, address) values ('001', 'jack', 'hz');
```

iv. Execute the following statement to query data in the tb table:

```
select * from tb;
```

The following result is returned:

```
+-----+-------+---------+
| id  | name  | address |
+-----+-------+---------+
| 001 | jack  | hz      |
+-----+-------+---------+ 1 rows in set (24 ms)
```

**Note**

You can configure the format of the returned data. For more information, see the Format of returned data section of this topic.

**Format of returned data**

Returned data can be output in various formats, such as a table, a CSV file, or vertical columns. By default, data is returned as a table. You can use the `format` command to specify the format of the returned data. Data queried by SELECT statements is returned in the specified format.

**Important**

The `format` command is supported only in Lindorm-cli.

**Specify to output returned data as a table**

```
format table;
```

Data format:

```
+-----+-------+---------+
| id  | name  | address |
+-----+-------+---------+
| 001 | jack  | hz      |
+-----+-------+---------+ 1 rows in set (99 ms)
```

**Specify to output returned data as a CSV file**

```
format csv;
```

Data format:

```
id,name,address 001,jack,hz
```

**Specify to output returned data as vertical columns**

```
format vertical;
```

Data format:

```
********************* 1. row *************************
id: 001 name: jack address: hz 1 rows in set (99 ms)
```

#### Use Lindorm SQL to develop applications

##### Install LindormTable SQL drivers

This topic describes the development kits and tools that can be used to develop applications based on the SQL syntax provided by LindormTable.

**Database drivers**

Lindorm provides the following database drivers for applications developed by using common programming languages. These drivers can be used as SDKs to execute SQL statements.

**Java**

For applications developed by Java, Lindorm provides a driver that is compatible with the APIs provided by JDBC. For more information about how to install and use the driver, see Use Java JDBC APIs to develop applications.

**Go**

For applications developed by Go, Lindorm provides a driver that is compatible with the APIs provided by the database/sql library of Go. For more information about how to install and use the driver, see Use the APIs provided by the database/sql library of Go to develop applications. For applications developed by Python, Lindorm provides a driver that is compatible with the DB-API of Python. For more information about how to install and use the driver, see Use Python DB-API to develop applications.

**Develop and test SQL statements**

| Parameter | Example | Method used to obtain the parameter value |
|---|---|---|

We recommend that you fully verify an SQL statement in development before you officially use the statement in your application. Lindorm provides an interactive SQL command-line tool **lindorm-cli** for you to verify and test SQL statements in development.

##### Use Java JDBC APIs to develop applications

This topic describes how to use the JDBC APIs provided by Java to develop SQL-based LindormTable applications and provides examples.

**Prerequisites**

Java Development Kit (JDK) V1.8 or later is installed. The endpoint that is required when you use SQL to connect to and use LindormTable is obtained. For more information, see the **View endpoints** topic of **Instance management** in **Lindorm User Guide**. The procedure described in this topic is not applicable to LindormTable Serverless.

**Procedure**

**Note**

You can directly use the sample code provided in the following procedure, or download sample code from GitHub to your on-premises machine for compiling and running. The sample code provided in this topic is included in the `com.aliyun.lindorm.sql.demo.BasicDemo` class.
1. Download a Lindorm client. For example, you can add the following dependencies to the `pom.xml` file
in your Maven project. The following example shows how to add dependencies to the configuration file in a Maven project:

```xml
<dependency>
  <groupId>com.aliyun.lindorm</groupId>
  <artifactId>lindorm-all-client</artifactId>
  <version>2.1.2</version>
</dependency>
```

2. Initialize the Lindorm client. Enter the following code in your project. Then, modify the code based on
the description in the following table.

```
// The endpoint that is required when you use SQL to connect to and use LindormTable. String url = "jdbc:lindorm:table:url=http://ld-bp17j28j2y7pm****-proxy-lindormpub.lindorm.rds.aliyuncs.com:30060"; // The database username that is obtained from the Lindorm console. String username = "root"; // The database password that is obtained from the Lindorm console. String password = "root"; // You can specify the database to which you want to connect when you establish the connection. I f no database is specified, your client is connected to a database named default. String database = "default"; Properties properties = new Properties(); properties.put("user", username); properties.put("password", password); properties.put("database", database);
```

| url | jdbc:lindorm:table:url=http:// ld-bp17j28j2y7pm****-proxy- lindorm- pub.lindorm.rds.aliyuncs.co m:30060 | The endpoint that is required when you use SQL to connect to and use LindormTable. For more information about how to obtain the endpoint, see the View endpoints topic of Instance management in Lindorm User Guide. |
|---|---|---|
| username | root | The user name and password used to connect to LindormTable. If you forget your password, you can change the password in the cluster management system of LindormTable. For more information about how to change a password that is used to connect to LindormTable, see the User management topic of LindormTable in Lindorm User Guide. |
| password | root |  |
| database | default | The name of the database to which you want to connect. By default, your client is connected to a database named default. |

| com.aliyun.lindorm.client.shaded.org.apache.calcite.avatica.http.ConnectionDisconnectedException |  |
|---|---|

3. Run the following code to establish a connection between the Lindorm client and the database:

```
// Obtain the established connection. Connection connection = DriverManager.getConnection(url, properties);
```

**Important**

If a connection between the Lindorm client and server is idle for more than 10 minutes, the server
4. After the connection is established, call Java API operations for LindormTable SQL to access Lindorm
wide tables. The following example shows how to call Java API operations for LindormTable SQL to access Lindorm wide tables.

```java
/* -------------- Examples of CRUD operations based on JDBC ----------------- */ String tableName = "sql_table_" + new Random().nextInt(1000); // Create a table. try (Statement statement = connection.createStatement()) {
  String sql = "create table if not exists " + tableName + "(id VARCHAR, name VARCHAR, primary ke
y(id))";
  int ret = statement.executeUpdate(sql);
  System.out.println(ret);
} // Insert data to the table. String upsertSql = "upsert into " + tableName + "(id,name) values(?,?)"; try (PreparedStatement ps = connection.prepareStatement(upsertSql)) {
  int batchSize = 100;
  for (int i = 0; i < batchSize; i++) {
    ps.setString(1, "aa" + i);
    ps.setString(2, "bb" + i);
    // Add the write operation to a batch.
    ps.addBatch();
  }
  // Perform write operations in all batches.
  // To ensure the performance and stability of your application, do not perform write operations
in a large number of batches at the same time.
  // When you use the executeBatch() method to perform write operations in batches, we recommend
that you specify up to hundreds of batches.
  int[] ret = ps.executeBatch();
  System.out.println(Arrays.toString(ret));
} // Query data in the table. String querySql = "select * from " + tableName + " where id=?"; try (PreparedStatement ps = connection.prepareStatement(querySql)) {
  ps.setString(1, "aa");
  ResultSet rs = ps.executeQuery();
  while (rs.next()) {
    String id = rs.getString(1);
    String name = rs.getString(2);
    System.out.println("id=" + id);
    System.out.println("name=" + name);
  }
} // Delete data from the table. String deleteSql = "delete from " + tableName + " where id=?"; try (PreparedStatement ps = connection.prepareStatement(deleteSql)) {
  ps.setString(1, "aa");
  ps.executeUpdate();
} // Close the connection. Make sure the connection is closed after an operation is complete. Other wise, connection leaks occur. connection.close();
```

**Sample code for connecting to LindormTable by using different**

**frameworks**

To meet the requirements of a large number of users, this topic provides relevant links to the webpages that contain sample code that can be used to connect to LindormTable by using different Java frameworks. If you want to use Druid to connect to LindormTable, see Sample code for a Druid-based connection. If you want to use Spring to connect to LindormTable, see Sample code for a Spring-based connection. If you want to use Mybatis to connect to LindormTable, see Sample code for a Mybatis-based connection. If you want to use Hibernate to connect to LindormTable, see Sample code for a Hibernate-based connection.

**References**

For more information about Lindorm SQL syntax, see LindormTable SQL.

##### Use Druid to connect to LindormTable

Druid is a Java Database Connectivity (JDBC) connection pool used to connect to databases. This topic describes how to use Druid to connect to and use LindormTable.

**Prerequisites**

Java Development Kit (JDK) V1.8 or later is installed. The version of LindormTable is 2.3.1 or later. For more information about how to upgrade the version of LindormTable, see the **Version update** topic of **Instance management** in **Lindorm User Guide**.

**Preparations**

Before you use Druid to connect to LindormTable, you must install Druid and Lindorm JDBC Driver. For example, you can add the following dependencies to the pom.xml file in your Maven project:

```xml
<dependency>
  <groupId>com.alibaba</groupId>
  <artifactId>druid</artifactId>
  <version>1.2.11</version>
</dependency> <dependency>
  <groupId>com.aliyun.lindorm</groupId>
  <artifactId>lindorm-all-client</artifactId>
  <version>2.1.2</version>
</dependency>
```

If you want to use druid-spring-boot-starter to start Druid, you must first exclude the druid component on which druid-spring-boot-starter depends and then explicitly add the dependency on the druid component to the configuration file. The following example shows how to configure dependencies when you use druid-spring-boot-starter to start Druid:

```xml
<dependency>
   <groupId>com.alibaba</groupId>
   <artifactId>druid-spring-boot-starter</artifactId>
   <version>1.2.11</version>
   <exclusions>
      <exclusion>
         <groupId>com.alibaba</groupId>
         <artifactId>druid</artifactId>
      </exclusion>
   </exclusions>
</dependency> <dependency>
  <groupId>com.alibaba</groupId>
  <artifactId>druid</artifactId>
  <version>1.2.11</version>
</dependency> <dependency>
  <groupId>com.aliyun.lindorm</groupId>
  <artifactId>lindorm-all-client</artifactId>
  <version>2.1.2</version>
</dependency>
```

**Procedure**

**Note**

You can download the sample code and then directly compile and run the code on your local computer or develop your project based on the sample code.
1. Configure parameters for Druid. In the src/main/resources path of your Maven project, create a
druid.properties file and add the following configurations to the file:

```bash
# Specify the name of the driver class. You can keep this configuration unchanged.
driverClassName=com.aliyun.lindorm.table.client.Driver
# You can replace the url, username, and password parameters to the actual values in your busines
s. You can obtain the value of these parameters on the Lindorm console. url=jdbc:lindorm:table:url=http://ld-bp17j28j2y7pm****.lindorm.rds.aliyuncs.com:30060 username=**** password=****
# Replace **** with the database that you want to connect.
connectionProperties=database=****
# Initialize the connection pool to create a connection. We recommend that you keep this configur
ation unchanged. init=true
# Specify the number of connections that you want to create during initialization. You can config
ure this parameter based on your requirements. initialSize=10
# Specify the minimum number of idle connections in the connection pool. You can configure this p
arameter based on your requirements. minIdle=10
# Specify the maximum number of idle connections in the connection pool. You can configure this p
arameter based on your requirements. maxActive=20
# Specify the maximum time that the client can wait to obtain a connection. Unit: ms. We recommen
d that you keep this configuration unchanged. maxWait=30000
# Configure parameters related to connection keep-alive. We recommend that you keep these
configurations unchanged. Otherwise, the connection may be unexpectedly disconnected.
# In this case, the ConnectionDisconnectedException exception is reported.
druid.keepAlive=true druid.keepAliveBetweenTimeMillis=30000 minEvictableIdleTimeMillis=600000 maxEvictableIdleTimeMillis=900000 timeBetweenEvictionRunsMillis=5000
# Configure parameters that are required to verify connections. We recommend that you keep these
configurations unchanged. testWhileIdle=true testOnBorrow=false testOnReturn=false
# Configure parameters related to the PreparedStatement cache. In this example, the cache is disa
bled. We recommend that you keep these configurations unchanged.
# Otherwise, the NoSuchStatement exception may be reported.
poolPreparedStatements=false maxOpenPreparedStatements=-1 druid.maxPoolPreparedStatementPerConnectionSize=-1
```

**Note**

Adjust or replace the values of the following parameters in actual use: `url` : The endpoint that is required when you use Druid to connect to LindormTable. For more information about how to obtain the endpoint, see the **View endpoints** topic of **Instance management** in **Lindorm User Guide**. `username` : The username that is used to connect to LindormTable. You can view the username in the cluster management system of LindormTable. For more information, see the **User management** topic of **Instance management** in **Lindorm User**
**Guide**.
`password` : The password that is used to connect to LindormTable. If you forget your password, you can change the password in the cluster management system of LindormTable. For more information about how to change a password that is used to connect to LindormTable, see the **User management** topic of **Instance**
**management** in **Lindorm User Guide**.
For more information about the parameters that you can configure, see DruidDataSource parameter configurations.
2. Load the parameter configurations of Druid and initialize the connection pool.

```
// Load parameter configurations. Properties properties = new Properties(); InputStream inputStream = DruidPoolDemo.class.getClassLoader().getResourceAsStream("druid.properties"); properties.load(inputStream); // Initialize the connection pool. DataSource dataSource = DruidDataSourceFactory.createDataSource(properties);
```

3. Use Druid to obtain connection information from JDBC and connect to LindormTable.

```java
/* -------------- Example on how to connect to LindormTable by using JDBC ----------------- */ String tableName = "sql_table_" + new Random().nextInt(1000); // Create a table. try (Connection connection = dataSource.getConnection()) {
    try (Statement statement = connection.createStatement()) {
        String sql = "create table if not exists " + tableName + "(id VARCHAR, name VARCHAR, prim
ary key(id))";
        int ret = statement.executeUpdate(sql);
        System.out.println(ret);
    }
} // Insert data to the table. try (Connection connection = dataSource.getConnection()) {
    String sql = "upsert into " + tableName + "(id,name) values(?,?)";
    try (PreparedStatement ps = connection.prepareStatement(sql)) {
        ps.setString(1, "aa");
        ps.setString(2, "bb");
        int ret = ps.executeUpdate();
        System.out.println(ret);
    }
} // Query data in the table. try (Connection connection = dataSource.getConnection()) {
    String sql = "select * from " + tableName + " where id=?";
    try (PreparedStatement ps = connection.prepareStatement(sql)) {
        ps.setString(1, "aa");
        ResultSet rs = ps.executeQuery();
        while (rs.next()) {
            String id = rs.getString(1);
            String name = rs.getString(2);
            System.out.println("id=" + id);
            System.out.println("name=" + name);
        }
    }
} // Delete data from the table. try (Connection connection = dataSource.getConnection()) {
    String sql = "delete from " + tableName + " where id=?";
    try (PreparedStatement ps = connection.prepareStatement(sql)) {
        ps.setString(1, "aa");
        ps.executeUpdate();
    }
}
```

##### Use the APIs provided by the database/sql library

**of Go to develop applications**

This topic describes how to use the APIs provided by the database/sql library of Go to develop SQL-based LindormTable applications and provides examples.

**Prerequisites**

Go V1.17 or later is installed. For more information about how to download and install Go, see official documentation.

| Add the dependency on the database driver to the | .go | file. The following code provides an example: |
|---|---|---|
| import ( avatica "github.com/apache/calcite-avatica-go/v5" ) |  |  |

| Parameter |  | Required | Description |  |
|---|---|---|---|---|
| databaseUrl |  |  | The endpoint that is used to connect to LindormTable SQL. Example: http://ld-bp12pc23yfb38****- proxy-lindorm.lindorm.rds.aliyuncs.com:30060 . For more information about how to obtain the endpoint, see the View endpoints topic of Instance management in Lindorm User Guide. |  |
|  |  |  |  | http://ld-bp12pc23yfb38****- |
|  |  | Yes | proxy-lindorm.lindorm.rds.aliyuncs.com:30060 |  |
| user |  | Yes | The username that is used to connect to LindormTable. |  |
| password |  | Yes | The password that is used to connect to LindormTable. If you forget your password, you can change the password in the cluster management system of LindormTable. For more information about how to obtain the password, see the Cluster management system (Lindorm Insight) topic of LindormTable in Lindorm User Guide. |  |
| database |  | Yes | The name of the database that you want to access. |  |
| SetConnMaxIdleTime |  | No | The maximum idle time period for connections. Default value: 0. The default value indicates that connections to LindormTable never time out. |  |
| SetMaxOpenConns |  | No | The maximum number of connections in the connection pool. Default value: 0. The default value indicates that the number of connections in the connection pool is not limited. |  |

The procedure described in this topic is not applicable to LindormTable Serverless.

**Procedure**

1. Add the following dependencies to the go.mod file in your Go project:

```
require github.com/apache/calcite-avatica-go/v5 v5.0.0 replace github.com/apache/calcite-avatica-go/v5 => github.com/aliyun/alibabacloud-lindorm-go-sqldriver/v5 v5.0.1
```

3. Initialize the connection pool and configure related parameters in the main method of the `.go` file.
The following code provides an example:

```json
databaseUrl := "http://localhost:30060" conn := avatica.NewConnector(databaseUrl).(*avatica.Connector) conn.Info = map[string]string{
    "user":     "sql",
    "password": "test",
    "database": "default",
} db := sql.OpenDB(conn) // Configure parameters related to the connection pool. db.SetConnMaxIdleTime(8 * time.Minute) db.SetMaxOpenConns(20) db.SetMaxIdleConns(2)
```

The following table describes the parameters that you can configure for the connection pool.

| SetMaxIdleConns | No | The maximum number of idle connections in the connection pool. Default value: 2. |
|---|---|---|

4. Perform operations in LindormTable, such as creating tables, writing data to tables, querying data, and
deleting data. The following examples show how to perform operations in LindormTable: Create a table.

```
_, err := db.Exec("create table if not exists user_test(id int, name varchar,age int, primary k ey(id))") if err != nil {
    return
}
```

Write data to a table. Method 1: Directly write data to a table.

```
_, err = db.Exec("upsert into user_test(id,name,age) values(1,'zhangsan',17)") if err != nil {
    return
}
```

Method 2: Write data to a table by specifying parameters.

```
stmt, err := db.Prepare("upsert into user_test(id,name,age) values(?,?,?)") if err != nil {
    fmt.Println("prepare error", err)
    return
} _, err = stmt.Exec(1, "zhangsan", 17) if err != nil {
    return
}
```

Query data. Method 1: Directly query data.

```
if err != nil {
    return
} defer rows.Close() var id int var name string var age int for rows.Next() {
    err = rows.Scan(&id, &name, &age)
    if err != nil {
           fmt.Println("scan data error", err)
        return
    }
    fmt.Println("id:", id, "name:", name, "age:", age)
}
```

Method 2: Query data by specifying parameters.

```
stmt, err = db.Prepare("select * from user_test where id=?") if err != nil {
    fmt.Println("prepare error", err)
    return
} if err != nil {
    return
} defer rows.Close() var id int var name string var age int for rows.Next() {
    err = rows.Scan(&id, &name, &age)
    if err != nil {
           fmt.Println("scan data error", err)
        return
    }
    fmt.Println("id:", id, "name:", name, "age:", age)
}
```

Delete data.

```
if err != nil {
    return
}
```

**Note**

For the complete sample code, visit Sample code and Write and query data by specifying parameters.

##### Use Python DB-API to develop applications

This topic describes how to use Python DB-API to develop applications based on LindormTable and provides examples.

**Prerequisites**

The endpoint of LindormTable is obtained. For more information, see the **View endpoints** topic of
**Instance management** in **Lindorm User Guide**.
Python 3.7 or later is installed. The procedure that is described in this topic is not applicable to LindormTable Serverless.

**Procedure**

1. Run the `pip install phoenixdb` command to install phonenixdb. The following sample command
shows how to install phonenixdb V1.2.0:

```
pip install phoenixdb==1.2.0
```

2. Specify parameters that are required to establish a connection to the database, including the name of
the database that you want to access and the username and password that are used to access the database.

| Parameter | Example | Description |
|---|---|---|
| lindorm user _ | root | The username and password that are used to access the database. You can obtain the username and password in the cluster management system of LindormTable. If you forget your password, you can change the password in the cluster management system of LindormTable. For more information, see the User management topic of Instance management in Lindorm User Guide. |
| lindorm password _ | root |  |
| database | default | The name of the database that you want to access. You can connect to existing databases that you have permissions to access. If you do not specify a database, you are connected to the default database. |

| Parameter | Description |
|---|---|
| database url _ | The endpoint that is used to access LindormTable SQL. Example: http://ld- bp10m54739kg9****-proxy-lindorm.lindorm.rds.aliyuncs.com:30060. For information about how to obtain the endpoint, see the View endpoints topic of Instance management in Lindorm User Guide. |
| autocommit | Specify whether to automatically commit the command. This parameter must be set to True. |
| connect kw args _ _ | The parameter that is used to initialize the connection. You do not need to modify the value of this parameter. |

```json
connect_kw_args = {'lindorm_user': 'Username obtained from the Lindorm console', 'lindorm_password': 'Password obtained from the Lindorm console', 'database': 'Name of the databa se specified in your business'}
```

The following table describes the parameters.
3. Specify the **database_url** and **connect_kw_args** parameters to establish a connection to the
database.

```
connection = phoenixdb.connect(database_url, autocommit=True, **connect_kw_args)
```

The following table describes the parameters.
4. After you are connected to the database, perform data definition language (DDL) and data manipulation
language (DML) operations on the database. The following code provides an example on how to perform DDL and DML operations:

```python
with connection.cursor() as statement:
    # Create a table.
    sql_create_table = "create table if not exists test_python(c1 integer, c2 integer, primary ke
y(c1))"
    # Insert a row of data.
    sql_upsert = "upsert into test_python(c1, c2) values(1,1)"
    # Insert multiple rows of data.
    with connection.cursor() as stat:
        sql_upsert = "upsert into test_python(c1, c2) values(?,?)"
        # Delete data.
    sql_delete = "delete from test_python where c1=2"
    # Modify data.
    sql_update = "upsert into test_python(c1, c2) values(1,10)"
    print(sql_update)
    statement.execute(sql_update)
    # Query data.
    rows = statement.fetchall()
    print(rows)
    # Disable a table. You must disable a table before you delete the table.
    # Delete a table.
    sql_drop_table = "drop table if exists test_python"
# Close the connection to the database.
connection.close()
```

**Note**

For information about the complete sample code, see GitHub. For information about Lindorm SQL syntax, see LindormTable SQL.

##### Use DBUtils to connect to LindormTable

DBUtils is a Python connection pool used to connect to databases. This topic describes how to use DBUtils to connect to LindormTable.

**Prerequisites**

Python 3.8 or later is installed. The endpoint that is required when you use SQL to connect to and use LindormTable is obtained. For more information, see the **View endpoints** topic of **Instance management** in **Lindorm User Guide**. The version of LindormTable is 2.3.1 or later. For more information about how to upgrade the version of LindormTable, see the **Version update** topic of **Instance management** in **Lindorm User Guide**.

**Preparations**

Run the following code to install phoenixdb V1.2.0 and DBUtils V3.0.2:

```java
pip install phoenixdb==1.2.0 pip install DBUtils==3.0.2
#!/usr/bin/python3
from dbutils.pooled_db import PooledDB import importlib class DBUtilsDemo:
    def __init__(self, url, user, password, database):
        config = {
            'url': url,
            'lindorm_user': user,
            'lindorm_password': password,
            'database': database,
            'autocommit': True
        }
        db_creator = importlib.import_module("phoenixdb")
        # Create a connection pool based on DBUtils.
        self.pooled = PooledDB(db_creator,
                               maxcached=10,
                               # Specify the maximum number of idle connections in the connection po
ol based on your business requirements.
                               maxconnections=50,
                               # Specify the maximum number of connections in the connection pool ba
sed on your business requirements.
                               blocking=True,
                               # Specify whether the client waits if no idle connection is available
in the connection pool. True indicates that the client waits until a connection is available. False indicates that the client does not wait for an idle connection and returns an error.
                               ping=1,
                               # Check whether the server can be accessed.
                               **config)
    # Obtain a connection from the connection pool.
    def _connect(self):
        try:
            r = self.pooled.connection()
            return r
        except Exception as e:
            print("Failed to connect:" + str(e))
    # Return a connection to the connection pool.
    def _close(self, conn, stmt):
        if stmt:
            stmt.close()
        if conn:
connclose()
```

```python
            conn.close()
    # Query a single row.
    def select_row(self, sql):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            statement.execute(sql)
            row = statement.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)
    # Query multiple rows.
    def select_rows(self, sql):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            print(sql)
            statement.execute(sql)
            rows = statement.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)
    # Update and insert data to a table.
    def upsert_data(self, sql_upsert):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)
    # Update and insert data to a table by specifying parameters.
    def upsert_data_prams(self, sql_upsert, prams):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)
if __name__ == '__main__':
    # Specify the endpoint that is required when you use SQL to connect to and use LindormTable.
    url = 'http://xxxx-proxy-lindorm.lindorm.rds.aliyuncs.com:30060'
    # Specify the actual username used to connect to LindormTable. You can view the username and pa
sswordusedtoconnecttoLindormTableintheLindormTableclustermanagementsystem.
```

```python
ssword used to connect to LindormTable in the LindormTable cluster management system.
    user = 'root'
    # Specify the actual password used to connect to LindormTable.
    password = 'root'
    # Specify the name of the database to which you want to connect.
    database = 'test'
    poolUtils = DBUtilsDemo(url, user, password, database)
    print(rows)
```

**Important**

You can run the ping command to test the connectivity of connections established by using DBUtils. However, this method is not applicable to connections established by using phoenixdb. If a connection has not been used for more than 10 minutes, a NoSuchConnection exception is returned. In this case, you must obtain a new connection from the connection pool.

#### Use the HBase API to connect to and use

## LindormTable

##### Install ApsaraDB for HBase SDKs

For more information about how to install ApsaraDB for HBase SDK for Java, see Install and upgrade ApsaraDB for HBase SDK for Java. For information about how to use Java API operations to connect to LindormTable, see Use the HBase API to connect to and use LindormTable. For more information about how to install ApsaraDB for HBase SDK for a non-Java language such as C++, Python, and Go, and how to use ApsaraDB for HBase SDK for a non-Java language to connect to LindormTable, see Use ApsaraDB for HBase SDK for a non-Java language to connect to LindormTable.

##### Use the Apsara for HBase API for a non-Java

**language to connect to and use LindormTable**

You can use the HBase API for a non-Java language, such as C++, Python, or Go, to connect to a Lindorm cluster. For information about how to install and use HBase SDKs to connect to a Lindorm cluster, see Use the Apsara for HBase API for a non-Java language to connect to LindormTable.

##### Use HBaseue Shell to connect to and use

## LindormTable

This topic describes how to use HBaseue Shell to connect to and use LindormTable.

**Prerequisites**

A Lindorm instance is created.

**Usage notes**

We recommend that you deploy your client in a Linux or macOS environment when you use HBaseue Shell to connect to and use LindormTable. If you deploy your client in a Windows environment, an error may be returned because of library missing. In this case, you must add the corresponding library file in your OS.

**Preparations**

If HBaseue Shell is deployed on an Elastic Compute Service (ECS) instance, make sure that the Lindorm instance and the ECS instance meet the following requirements to ensure network connectivity: The Lindorm instance and the ECS instance are deployed in the same region. We recommend that you also deploy the two instances in the same zone to reduce network latency. The network types of your Lindorm instance and ECS instance are the same.

**Note**

We recommend that you deploy the two instances in a virtual private cloud (VPC) for better security. If you select **VPC** as the network type, make sure that you specify the same VPC ID for the two instances. The LindormTable endpoint that is displayed after **Access by Using HBase Java API** on the Wide Table Engine tab of the Lindorm console is obtained. For more information, see the "View endpoints" topic of "Instance management" in Lindorm User Guide.

**Procedure**

1. Download HBaseue Shell.

**Note**

You can download the TAR file of the Apache HBase client version that you need from the HBase official site and then import a JAR file to the HBase client to upgrade it to an ApsaraDB for HBase client. i. Log on to the Lindorm console. ii. In the upper-left corner of the page, select the region where your Lindorm instance is located. iii. On the **Instances** page, find the Lindorm instance that you want to manage and click its ID. iv. In the left-side navigation pane, click **Database Connections**. On the page that appears, click the
**Wide Table Engine** tab.
v. In the **HBase Compatibility Address** section, click **Download Lindorm Shell** to download the package of HBaseue Shell.
2. Run the following command to decompress the downloaded package of HBaseue Shell to the target
path. In this example, the package is decompressed to the alihbase-2.0.18 path.

```
tar zxvf hbaseue-shell.tar.gz
```

3. Configure the connection parameters.
i. Go to the alihbase-2.0.18/conf directory and open the hbase-site.xml file.

```
vi hbase-site.xml
```

ii. Specify the endpoint, username, and password that you can to use to connect to the Lindorm instance.

```xml
<configuration>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>ld-bp17j28j2y7pm****-proxy-lindorm-pub.lindorm.rds.aliyuncs.com:30020</value>
    </property>
    <property>
        <name>hbase.client.username</name>
        <value>testuser</value>
    </property>
    <property>
        <name>hbase.client.password</name>
        <value>password</value>
    </property>
    <property>
        <name>lindorm.rpc.only.use.seedserver</name>
        <value>true</value>
    </property>
</configuration>
```

**Note**

Replace **hbase.zookeeper.quorum** with the LindormTable endpoint that is displayed after **Access by Using HBase Java API** on the Wide Table Engine tab of the Lindorm console. Replace **hbase.client.username** and **hbase.client.password** with the username and password that you can use to connect to LindormTable. If you forget the password, you can change the password in the **cluster management system** of LindormTable. For more information about how to change a password that is used to connect to LindormTable, see the "User management" topic of "LindormTable" in Lindorm User Guide.
4. Use HBaseue Shell to connect to LindormTable. Go to the alihbase-2.0.18/bin path and then run the
following command:

```
./hbase shell
```

If the following result is returned, your client is connected to LindormTable.

```
Version 2.0.18, r08b8d58a9d6ce89765d5ebe2ddff425aed644c16, Mon Feb 1 12:46:39 CST 2021 Took 0.0034 seconds
```

**Note**

After you use HBaseue Shell to connect to LindormTable, you can only perform simple DDL operations, data reading operations, and data writing operations. For more information, see Limits.

##### Limits

You can use the HBase API for Java to connect to Lindorm. Take note of the following limits: Lindorm does not support HBase API operations for managing clusters, such as assign region and stopRegionServer. If you want to manage clusters, log on to the Lindorm console and use the Lindorm Insight system. Lindorm does not support HBase coprocessors. This feature will be available in the future. If you want to obtain more information, join a DingTalk group. Limited permissions are granted to access the underlying storage of Lindorm. You can access the underlying storage of Lindorm over the Hadoop Distributed File System (HDFS) protocol. You can directly import or export data as needed. You can use Spark to analyze data. You can also call the HBase API operations in Spark or call the TableInputFormat operation in MapReduce. **If you want to**

**perform bulk load operations, call the HDFS API operations.**

Lindorm does not support custom filters. If you want to define a custom filter, encapsulate the code of the filter class into a JAR file and upload the file to the lib directory of the server node or HDFS. Then, restart the server node or dynamically load the JAR file to validate the custom filter. However, Lindorm does not support this operation. If you have questions about the limits, submit a ticket or join a DingTalk group.

#### Use a third-party tool to connect to and use

## LindormTable

##### Use Apache Spark to access LindormTable

This topic describes how to use open source Apache Spark to access LindormTable.

**Prerequisites**

The version of LindormTable is 2.4.3 or later. Your application is deployed on an Elastic Compute Service (ECS) instance. The LindormTable endpoint of the HBase API for Java is obtained. For more information, see the "View endpoints" topic of "Instance management" in Lindorm User Guide.

**Usage notes**

You can connect to Lindorm instances **only by using virtual private clouds (VPCs)**.

**Important**

To connect to a Lindorm instance **over the classic network**, you must upgrade your SDK and change the configurations before you perform the operations described in this topic. For more information, see Use the ApsaraDB for HBase API for Java to connect to and use LindormTable. If your application is deployed on an ECS instance and you want to connect to a Lindorm instance over a VPC, make sure that your Lindorm instance and the ECS instance meet the following requirements in advance to ensure network connectivity: Your Lindorm instance and ECS instance are deployed in the same region. We recommend that you also deploy the two instances in the same zone to reduce network latency. Your Lindorm instance and ECS instance are deployed in the same VPC.

**Add configurations for accessing LindormTable**

Method 1: Add configurations to a configuration file Add the following configurations to the configuration file named `hbase-site.xml` :

```xml
<configuration>
      <!--
    -->
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>ld-xxxx-proxy-lindorm.lindorm.rds.aliyuncs.com:30020</value>
    </property>
    <property>
        <name>lindorm.rpc.only.use.seedserver</name>
        <value>true</value>
    </property>
</configuration>
```

Method 2: Add parameters to a Configuration object

```
// Create a Configuration object. Configuration conf = HBaseConfiguration.create(); // Specify the LindormTable endpoint of the HBase API for Java. conf.set("hbase.zookeeper.quorum", "ld-xxxx-proxy-lindorm.lindorm.rds.aliyuncs.com:30020"); conf.set("lindorm.rpc.only.use.seedserver", "true");
```

```json
test(" test the spark sql count result") {
  // 1. Add access configurations for the HBaseue Shell.
  var conf = HBaseConfiguration.create
  conf.set("hbase.zookeeper.quorum", "ld-xxxx-proxy-lindorm.lindorm.rds.aliyuncs.com:30020")
  conf.set("lindorm.rpc.only.use.seedserver", "true");
  // 2. Create an ApsaraDB for HBase table.
  val hbaseTableName = "testTable"
  val cf = "f"
  val column1 = cf + ":a"
  val column2 = cf + ":b"
  var rowsCount: Int = -1
  var namespace = "spark_test"
  val admin = ConnectionFactory.createConnection(conf).getAdmin()
  val tableName = TableName.valueOf(namespace, hbaseTableName)
  val htd = new HTableDescriptor(tableName)
  htd.addFamily(new HColumnDescriptor(cf))
  // 3. Insert test data into the created table.
  val rng = new Random()
  val k: Array[Byte] = new Array[Byte](3)
  val famAndQf = KeyValue.parseColumn(Bytes.toBytes(column))
  val puts = new util.ArrayList[Put]()
  var i = 0
  for (b1 <- ('a' to 'z')) {
      for (b2 <- ('a' to 'z')) {
        for (b3 <- ('a' to 'z')) {
          if(i < 10) {
            k(0) = b1.toByte
            k(1) = b2.toByte
            k(2) = b3.toByte
            val put = new Put(k)
            put.addColumn(famAndQf(0), famAndQf(1), ("value_" + b1 + b2 + b3).getBytes())
            puts.add(put)
            i = i + 1
          }
        }
      }
  }
  val conn = ConnectionFactory.createConnection(conf)
  val table = conn.getTable(tableName)
  table.put(puts)
  // 4. Create a Spark table.
  val sparkTableName = "spark_hbase"
  val createCmd = s"""CREATE TABLE ${sparkTableName} USING org.apache.hadoop.hbase.spark
                         |    OPTIONS ('catalog'=
                         |    '{"table":{"namespace":"$${hbaseTableName}",
"name":"${hbaseTableName}"},"rowkey":"rowkey",
                         |    "columns":{
                         |    "col0":{"cf":"rowkey", "col":"rowkey", "type":"string"},
                         |    "col1":{"cf":"cf1", "col":"a", "type":"string"},
                         |    "col2":{"cf":"cf1", "col":"b", "type":"String"}}}'
                         |    )""".stripMargin
  println(" createCmd: \n" + createCmd + " rows : " + rowsCount)
  sparkSession.sql(createCmd)
  // 5. Execute the statement that contains the COUNT() function.
  val result = sparkSession.sql("select count(*) from " + sparkTableName)
  val sparkCounts = result.collect().apply(0).getLong(0)
  println(" sparkCounts : " + sparkCounts)
```

| Resource group type | Feature | Usage notes |
|---|---|---|
| Exclusive resource group | DataWorks automatically purchases and manages exclusive resources. This saves you the need to worry about service performance and availability. | Exclusive resources cannot be shared across regions. For example, the exclusive resources in the China (Shanghai) region can be used only by the workspace in the China (Shanghai) region. The resources cannot be allocated to VPCs in other regions. Exclusive resources can access only Lindorm instances that are attached to the same vSwitch as the exclusive resources. |
| Custom resource group | Only DataWorks Enterprise Edition or a more advanced edition supports custom resource groups. You need to purchase ECS instances for custom resource groups. If the ECS instances are deployed in the VPC of the Lindorm instance, the ECS instances can access the Lindorm instance over the VPC. If the ECS instances and the Lindorm instance are not deployed in the same VPC, the ECS instances can access the Lindorm instance only over the Internet. | You have full permissions on the ECS instances that belong to your custom resource group. However, you must manually install, maintain, and update DataX. For more information about how to install DataX, see the references. |

### Data import and export

#### Data import methods

##### Use DataWorks or DataX to import data

Lindorm Tunnel Service (LTS) provided by Lindorm allows you to migrate and synchronize data between Lindorm instances of different versions in real time. You can also use LTS to synchronize data from ApsaraDB RDS or LogHub to Lindorm in real time. DataX is an offline data synchronization tool that is widely used within Alibaba Group. You can use DataX to efficiently synchronize data between heterogeneous data sources. These data sources include MySQL, Oracle, SQL Server, PostgreSQL, Hadoop Distributed File System (HDFS), Hive, AnalyticDB for MySQL, Lindorm, Tablestore, MaxCompute, and Distributed Relational Database Service (DRDS).

**Prerequisites**

If the Elastic Compute Service (ECS) instance and the ApsaraDB for HBase Performance-enhanced Edition instance are not in the same virtual private cloud (VPC), you must use the public endpoint. For more information about how to activate a classic network endpoint, see the "Activate a classic network endpoint" topic of "Instance management" in Lindorm User Guide.

**Use DataX to synchronize data**

You can use DataX to synchronize data by using one of the following methods: Use the Data Integration service provided by Alibaba Cloud DataWorks to configure synchronization tasks in DataX. We recommend that you use this method. Use open source DataX to configure synchronization tasks.

**Use DataWorks to configure synchronization tasks in DataX**

1. Creates a workspace.
2. Create a resource group. The following table describes different types of resource groups.

| Default resource group | The ECS instances in the default resource group cannot access a Lindorm instance over the VPC of the Lindorm instance. The ECS instances can access the Lindorm instance only over the Internet. | When the ECS instances access a Lindorm instance over the Internet, you are charged additional fees for DataWorks. |
|---|---|---|

| Note Click Download the installation package to download the latest version of the DataX installation package and then import the package. You need to download only the 1.x version (the latest version) of the aliLindorm-connector-1.x jar package and import the package to the DataX/plugin/writer/hbase11xwriter/libs directory. If you want to use DataX to read data from Lindorm, you must also import the package to the DataX/plugin/reader/hbase11xreader/libs directory . |  |  |
|---|---|---|
|  | DataX/plugin/reader/hbase11xreader/libs |  |

3. Create a synchronization task.
4. Modify the configuration of plug-ins.

```json
"configuration": {
  "lindorm.client.namespace" : "namespace",
  "lindorm.client.seedserver" : "host:30020",
  "lindorm.client.username" : "testuser",
  "lindorm.client.password" : "password",
  "lindorm.rpc.only.use.seedserver": "true"
}
```

**Note**

lindorm.client.namespace: the namespace of the tables that you want to access in the Lindorm instance. Lindorm.client.seedserver: the endpoint of the API for Java that is displayed in the Lindorm console. For more information, see Connect to a cluster. Lindorm.client.username/Lindorm.client.password: the username and password that you specified for logging on to your Lindorm instance. The default username and password are both root. Make sure that the account has the read and write permissions on the tables that are stored in the Lindorm instance. The default root account has the read and write permissions on all tables that are stored in the Lindorm instance.
5. Configure a resource group for the synchronization task.

**Use open source DataX to configure synchronization tasks (you can use**

1. Download the DataX installation package. Download URL: Download the installation package.
2. Decompress the DataX installation package.
3. Modify the configuration file. In DataX, the hbase11xreader plug-in is used to read data from Lindorm.
For more information about how to configure the plug-in, see hbase11xreader. The hbase11xwriter plug-in is used to write data to Lindorm. For more information about how to configure the plug-in, see hbase11xwriter. The following code snippet shows the Lindormconfig settings for reading data from and writing data to Lindorm. Keep the other settings the same as the default settings.

```json
"hbaseConfig": {
  "hbase.client.connection.impl" : "com.alibaba.hbase.client.AliHBaseUEConnection",
  "hbase.client.endpoint" : "host:30020",
  "hbase.client.username" : "testuser",
  "hbase.client.password" : "password",
  "lindorm.rpc.only.use.seedserver": "true"
}
```

**Note**

hbase.client.connection.impl: You do not need to modify this parameter. hbase.client.endpoint: the endpoint for the HBase mode. You can view the endpoint on the
**Database Connections** page of the Lindorm console.
Lindorm.client.username/Lindorm.client.password: the username and password that you specified for logging on to your Lindorm instance. The default username and password are root. Make sure that the account has the read and write permissions on the tables that are stored in the Lindorm instance. The default root account has the read and write permissions on all tables that are stored in the Lindorm instance.
4. Use DataX to migrate data.

#### Import data from ApsaraDB for MongoDB

DataWorks is an important platform as a service (PaaS) provided by Alibaba Cloud. DataWorks supports multiple computing engines and storage engines. This topic describes how to use DataWorks to migrate offline data from ApsaraDB for MongoDB to LindormTable.

**Background information**

DataWorks is an end-to-end big data development and governance platform that provides data warehousing, data lake, and data lakehouse solutions based on big data compute engines, such as MaxCompute (formerly ODPS), Hologres, E-MapReduce (EMR), AnalyticDB, and Cloudera Data Platform (CDP). Since 2009, DataWorks has been summarizing and improving the big data development methodology of Alibaba to support data mid-end building. DataWorks collaborates with public service sectors, state-owned enterprises, and customers in various industries, such as finance, retail, Internet, energy, and manufacturing, to improve data application efficiency and facilitate the digital transformation of industries.

**Usage notes**

To migrate offline data from ApsaraDB for MongoDB to LindormTable, unnest the nested JSON fields in the offline data. Take note that you do not need to convert the data.

**Note**

Perform the following steps if you want to process data during the migration process. For example, perform the following steps if you want to perform MD5 hashing on the primary key of MongoDB data during the migration process:
1. Use DataWorks to migrate the data from ApsaraDB for MongoDB to MaxCompute.
2. Execute SQL statements to process data in MaxCompute.
3. Use DataWorks to migrate data from MaxCompute to LindormTable.

**Preparations**

Before you migrate offline data from ApsaraDB for MongoDB to LindormTable, complete the following preparations: Prepare the data that you want to migrate in ApsaraDB for MongoDB:

```json
{
   "id" : ObjectId("624573dd7c0e2eea4cc8****"),
   "title" : "ApsaraDB for MongoDB tutorial",
   "description" : "ApsaraDB for MongoDB is a NoSQL database",
   "by" : "Trial Center",
   "url" : "http://www.runoob.com",
   "map" : {
        "a" : "mapa",
        "b" : "mapb"
    },
   "likes" : 100
}
```

Prepare schema data in LindormTable:

```
  title varchar not null primary key,
  desc varchar,
  by varchar,
  url varchar,
  a varchar,
  b varchar,
  likes int);
```

Use the Data Integration service of DataWorks to configure DataX tasks.

**Procedure**

1. Add an ApsaraDB for MongoDB data source to the DataWorks console.
2. Configure an offline data synchronization task in script mode.
i. Create a workflow. a. Log on to the DataWorks console. b. In the upper-left corner of the console, click the **More** icon. c. In the left-side navigation pane, choose All Products > Data Development and O&M > **DataStudio**. d. On the **DataStudio** page, move the pointer over the icon and click **Create Workflow**. e. In the **Create Workflow** dialog box, specify **Workflow Name** and **Description**.

**Note**

The name must be 1 to 128 characters in length and can contain letters, digits, underscores (_), and periods (.). f. Click **Create**. ii. Create a batch synchronization node. a. Click the newly created workflow and right-click **Data Integration**. b. Choose **Create Node > Batch Synchronization**. c. In the **Create Node** dialog box, specify **Name** and **Path**.

**Note**

The node name must be 1 to 128 characters in length, and can contain letters, digits, underscores (_), and periods (.). d. Click **Confirm**. iii. Configure the reader and writer of the batch synchronization node. a. After the batch synchronization node is created, click **Switch to Code Editor** in the toolbar. b. In the **Confirm** dialog box, click **OK** to open the code editor. c. The code editor has generated basic reader and writer settings. You can manually configure the data sources of the reader and writer for the batch synchronization node and specify the information about the tables to be synchronized. Example:

```json
{
    "type": "job",
    "version": "2.0",
    "steps": [
        {
            "stepType": "mongodb",
            "parameter": {
                "datasource": "test_mongo",   //The name of the ApsaraDB for MongoDB data sour
ce.
                "column": [
                    {
                        "name": "title",
                        "type": "string"
                    },
                    {
                        "name": "description",
```

```json
                        "type": "string"
                    },
                    {
                        "name": "by",
                        "type": "string"
                    },
                    {
                        "name": "url",
                        "type": "string"
                    },
                    {
                        "name": "map.a",
                        "type": "document.string"
                    },
                    {
                        "name": "map.b",
                        "type": "document.string"
                    },
                    {
                        "name": "likes",
                        "type": "int"
                    }
```

`],`

```json
                "collectionName": "testdatax"
            },
            "name": "Reader",
            "category": "reader"
        },
        {
            "stepType": "lindorm",
            "parameter": {
                "configuration":  {
                    "lindorm.client.seedserver": "ld-xxxx-proxy-
lindorm.lindorm.rds.aliyuncs.com:30020",
                    "lindorm.rpc.only.use.seedserver": "true",
                    "lindorm.client.username": "root",
                    "lindorm.client.namespace": "test",
                    "lindorm.client.password": "root"
                },
                "nullMode": "skip",
                "datasource": "",
                "writeMode": "api",
                "envType": 1,
                "columns": [
                    "title",
                    "desc",
                    "by",
                    "url",
                    "a",
                    "b",
                    "likes"
```

`],`

```json
                "dynamicColumn": "false",
                "table": "t1",
                "encoding": "utf8"
            },
            "name": "Writer",
            "category": "writer"
        }
```

`],`

```json
    "setting": {
"executeMode":null
```

```json
        "executeMode": null,
        "errorLimit": {
            "record": ""
        },
        "speed": {
            "concurrent": 2,
            "throttle": false
        }
    },
    "order": {
        "hops": [
            {
                "from": "Reader",
                "to": "Writer"
            }
```

]

```
    }
}
```

d. After you configure the batch synchronization node, save the node configurations and click the icon in the upper-left part of the code editor. On the **Runtime Log** tab, you can view the progress of the migration task.

### Developer guide

#### Dynamic columns

LindormTable supports dynamic columns. By using this feature, you can dynamically write data to or query data in columns that are not explicitly specified when you create a table.Lindorm This topic describes how to use Lindorm SQL to enable dynamic columns, and how to write data to or query data in dynamic columns.

**Background information**

The schema of a traditional relational database table must be predefined. If you want to add columns, you must modify the attributes of the table. The operation of modifying the attributes of a large table requires a long period of time. A predefined schema may be inconvenient for your business design. LindormTable provides the dynamic column feature. You do not need to predefine columns that you want to manage. You can use Lindorm SQL to read data from and write data to dynamic columns.

**Usage notes**

Before you use the dynamic column feature, take note of the following points: Make sure that the version of LindormTable is 2.2.19 or later. For more information, see the **Upgrade**
**the minor engine version of a Lindorm instance** topic of **Instance management** in **Lindorm**
**User Guide**.
Data in dynamic columns in LindormTable is of the VARBINARY type. You must convert the data type of dynamic columns to byte arrays when you query data in or write data to dynamic columns. If you use the HBase API for Java to create a table or write data to a table, you can use Lindorm SQL to query data from and write data to dynamic columns in the table.

**Important**

Dynamic columns cannot be disabled after they are enabled for a table. You can use one of the following methods to enable dynamic columns: Enable dynamic columns by using the WITH clause when you create a table.

```
CREATE TABLE tablename (p1 INT, c1 INT, c2 VARCHAR, PRIMARY KEY(p1)) WITH (DYNAMIC_COLUMNS='true');
```

| dynamic column c5 is the value f to 0f |  | f |
|---|---|---|
|  | 0f |  |
| UPSERT INTO t dynamic columns (p1, c5) VALUES (3, 'f'); _ _ |  |  |

| written to c6 is | gf | , which is not a hex string. |
|---|---|---|
| UPSERT INTO t dynamic columns (p1, c6) VALUES (4, 'gf'); _ _ |  |  |

Modify the attributes of an existing table to enable dynamic columns.

```
ALTER TABLE tablename SET 'DYNAMIC_COLUMNS' = 'true';
```

**Note**

After dynamic columns are enabled for a table, you can modify the attributes of the table to add new columns to the schema of the table. For example, you can execute the following statement to add the c3 column of the INT data type to the schema of the table.

```
ALTER TABLE t_dynamic_columns ADD COLUMN c3 int;
```

If you write data to a dynamic column named c3 before you add the c3 column to the schema of the table, an `IllegalDataException` exception is returned when you insert INT data to or query INT data in c3 because the type of data written to c3 is VARBINARY. This exception is not returned if the data type of the c3 column that you add to the schema of the table is VARBINARY. Therefore, take note of the data types when you change the schema of a table for which dynamic columns are enabled.

**Directly write data to dynamic columns by using SQL statements**

The syntax that is used to write data to a table for which dynamic columns are enabled is the same as the syntax that is used to write data to a table for which dynamic columns are not enabled. After dynamic columns are enabled for a table, you can write data to columns that are not defined in the table schema. However, the type of data in dynamic columns can only be VARBINARY, which indicates byte arrays. You can execute SQL statements in Lindorm-cli to write data to dynamic columns. The value that you want to write to dynamic columns by using an UPSERT statement must be converted into a hexadecimal string (**hex string**).

**Note**

A byte can be represented by a decimal number between 0 and 255, or two hexadecimal digits from 0x00 to 0xFF. The hex string for a byte array {0x00, 0xFF} is 00FF. For more information about how to convert a byte array to a hex string, see the Convert a byte array to a hex string section of this topic. The following examples show how to write data to dynamic columns: The following statement is executed to write data to the c3 column in the `t_dynamic_columns` table. The c3 column is a dynamic column. The write operation is successful.

```
UPSERT INTO t_dynamic_columns (p1, c2, c3) VALUES (1, '1', '41');
```

The following statement is executed to write data to the c4 column in the `t_dynamic_columns` table. The c4 column is a dynamic column. The write operation is successful.

```
UPSERT INTO t_dynamic_columns (p1, c4) VALUES (2, 'ef0011');
```

The following statement is executed to write data to the c5 column in the `t_dynamic_columns` table. The following statement is executed to write data to the c6 column in the `t_dynamic_columns` table. The

**Write data to dynamic columns by specifying parameters in SQL**

**statements (recommended)**

We recommend that you write byte arrays to dynamic columns by specifying the byte arrays as parameters in SQL statements in your application. If you want to write strings or numeric values to dynamic columns, you must encode the strings or numeric values to byte arrays and then specify the byte

| Important If you perform the query in the example in Lindorm-cli, the queried byte arrays in dynamic columns are converted to printable characters in the query results. If the byte arrays in dynamic columns cannot be converted to printable characters, they are displayed as question marks or spaces in the query results. In the preceding example, the value in the c3 column is displayed as a printable character A, which is converted from the hex string 0x41 that is stored in the c3 column. |  |  |
|---|---|---|
| The | SELECT * | statement is used to query data in a table for which dynamic columns are enabled. In |

arrays as parameters to write them into dynamic columns. The following Java code provides an example of how to write data into dynamic columns by specifying the data as parameters:

```
Connection conn = DriverManager.getConnection(lindorm-jdbc-url); String createTable = "CREATE TABLE testTable (p1 VARCHAR, c1 INT, PRIMARY KEY(p1)) 'DYNAMIC_COLUMNS' = 'true'"; Statement statement = conn.createStatement(); statement.execute(createTable); // Insert three columns p1, c1, and c2 into a table. The p1 and c1 columns are defined in the table schema. The c2 column is not defined and is inserted into the table as a dynamic column. String sqlUpsert = "upsert into " + tableName + "(p1, c1, c2) values(?, ?, ?)"; try (PreparedStatement stmt = conn.prepareStatement(sqlUpsert)) {
    stmt.setString(1, "pk");
    stmt.setInt(2, 4);
    stmt.setBytes(3, new byte[] {0,1});
    int updated = stmt.executeUpdate();
    Assert.assertEquals(1, updated);
}
```

The scenarios in which data can be queried in dynamic columns are classified into the following types: The field that you want to query is a dynamic column. The syntax that is used to query data in a table for which dynamic columns are enabled is the same as the syntax that is used to query data in a table for which dynamic columns are not enabled. After you enable dynamic columns for a table, you can query data in columns that are not defined in the table schema. In the following example, c3 and c4 are dynamic columns that are added after the table is created.

```
SELECT p1, c3, c4 FROM t_dynamic_columns WHERE p1 = 1;
```

The following result is returned:

```
+-----+-------+---------+
| p1  |   c3  |   c4    |
+-----+-------+---------+
|  1  | A     |  null   |
+-----+-------+---------+ 1 rows in set (43 ms)
```

integrity of the metadata of the result set.

```
SELECT * FROM t_dynamic_columns LIMIT 10;
```

The following result is returned:

```
+-----+-------+---------+-------+------------+
| p1  |   c1  |   c2    | c3    |     c4     |
+-----+-------+---------+-------+------------+
|  1  | null  |  1      | A     | null       |
|  2  | null  |  null   | null  | ?        |
+-----+-------+---------+-------+------------+ 2 rows in set (141 ms)
```

**Important**

If you use a `SELECT *` statement with the LIMIT clause specified to query data in a table for which dynamic columns are enabled, the default maximum value of LIMIT is 5,000. You can specify a maximum value. If the queried value exceeds the maximum value, an error is returned. Dynamic columns are used in `WHERE` conditions. To ensure query performance, you must include the primary key or index key columns in `WHERE` conditions. If you use Lindorm-cli or SQL statements to query data in dynamic columns, the values in dynamic columns in WHERE conditions must be hex strings. For example, if the c4 column in the table t_dynamic_columns is a dynamic column, the following statement can be executed to perform a successful query:

```
SELECT p1, c4 FROM t_dynamic_columns WHERE p1 >= 1 AND p1 < 3 AND c4 = 'ef0011';
```

In contrast, the following query fails because the value 1 of the c4 column in the WHERE conditions is not a hex string.

```
SELECT p1, c1, c4 FROM t_dynamic_columns WHERE p1 = 2 AND c4 = '1';
```

**Convert a byte array to a hex string**

The following Java code provides an example of how to convert a byte array to a hex string:

```java
private static final char[] DIGITS = {
  '0', '1', '2', '3', '4', '5', '6', '7',
  '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
  };
private static String toHexString(byte[] bytes) {
  char[] chars;
  int j = 0;
  chars = new char[bytes.length * 2];
  for (byte b : bytes) {
    chars[j++] = DIGITS[(b & 0xF0) >> 4];
    chars[j++] = DIGITS[b & 0x0F];
  }
  return new String(chars, 0, j);
} public void testToHexString() {
  String s = "Hello, world";
  // You can use the getBytes() method of a string to obtain the byte array that corresponds to the
string.
  byte[] bytes = s.getBytes(Charset.forName("UTF-8"));
  String hexString = toHexString(bytes);
  System.out.println(hexString); // The output is 48656c6c6f2c20776f726c64.
}
```

#### Secondary indexes

LindormTable supports the secondary index feature in the Tabular model. In query scenarios where primary key columns are not specified in conditions, native secondary indexes can help you reduce the complexity of application development, ensure data consistency, and improve write efficiency. This topic describes the secondary index feature in the Lindorm Tabular model and provides relevant examples.

**Background information**

In the Lindorm Tabular model, a wide table has a table schema, and the data types of the columns in the wide table are predefined. The native secondary index feature of Lindorm is used in Alibaba Cloud for years. The outstanding performance of this feature has been verified by the Double 11 Shopping Festival for years. This feature is suitable for the global indexing of large amounts of data. The Lindorm secondary index feature allows you to create multiple indexes for a single table. Each index is physically mapped to a data table that is independent of the base table. You can specify different storage policies for each index. For example, you can specify different compression algorithms and hot and cold data separation policies. When you write data to a base table, Lindorm automatically updates all associated index tables and ensures data consistency between the base table and the index tables. When you query data, you need only to initiate a query for the base table. Lindorm automatically selects an appropriate index or the base table based on the WHERE condition and the schemas of the base table and the index tables to perform the query. You can also use hints to intervene in the behavior of the optimizer. Lindorm secondary indexes provide the following basic features: Multiple indexes can be created for a single base table. Composite indexes are supported. You can use one or more columns in a base table to create an index. Covering indexes are supported. For an index that contains all the columns in a base table, a column is automatically added to the index each time the column is added to the base table. Query optimization is provided. Lindorm automatically selects an index based on the WHERE clause for a query and allows you to use hints to intervene in the behavior of the optimizer. Online schema changes are supported. Changes in indexes do not affect the read and write operations that are performed on the associated base tables. You can create, delete, and update indexes for a base table based on your business requirements. The time-to-live (TTL) feature is supported. The TTL value that is specified for a base table automatically takes effect on all associated index tables. When the data in a base table expires, the data in the index tables also expires. Dynamic columns are supported. You can create secondary indexes based on dynamic columns and specify dynamic columns as included columns in a secondary index. Custom data versions are supported. After you specify a custom timestamp for a data record in a base table, the custom timestamp automatically takes effect on the corresponding data records in the associated index tables. Secondary indexes in Lindorm are easy to use. Compared with secondary indexes in a relational database management system (RDBMS), the secondary indexes of Lindorm provide a better user experience. After you purchase a Lindorm instance, you can directly use the SQL syntax supported by LindormTable to use secondary indexes.

**Environment requirements**

Server: A Lindorm instance is used. Client: For more information, see Install LindormTable SQL drivers. Lindorm-cli: For more information, see Use Lindorm-cli to connect to and use LindormTable. Strong consistency: Lindorm ensures the data consistency between a base table and the associated index tables. To meet the requirements of data consistency, you can minimize the overheads of secondary indexes and improve the write throughput. The following limits related to strong consistency are imposed on the secondary indexes of Lindorm: Snapshot isolation is not supported. When data is being written to a base table, the data may not be available for queries. After the system returns a successful response to notify the client that the data is written, the data becomes available for queries in the base table and associated index tables. If a client timeout error or an I/O error occurs, the data may not be available for queries in the base table or associated index tables. However, eventual consistency is ensured between the data in the base table and the data in the index tables.

| Mutability type | Constraint | Cost | Description |
|---|---|---|---|
| No index is created for the base table. | N/A | 1 | If no index is created for the base table, the system directly writes data to a new index. Only one operation is required to complete a write operation. |
| IMMUTABLE | The system writes data by rows. Data cannot be updated or deleted. | 2 | The system writes data to the base table and writes data to the index table. This mutability type incurs the lowest cost and delivers the best performance in all scenarios. |
| IMMUTABLE ROWS _ | The system writes data by rows. Data cannot be updated or deleted. | 2 to 3 | In normal write scenarios, the system writes data to the base table and writes data to the index table. In special scenarios in which data needs to be deleted, an additional operation is required to read data from the base table. This mutability type delivers excellent performance that is second only to IMMUTABLE. |
| MUTABLE LATEST _ | Data can be updated and deleted. | 4 | The system reads data from the base table, deletes historical data from the index table, writes data to the index table, and writes data to the base table. |
| MUTABLE ALL _ | No limits are imposed. You can use custom timestamps to write data. | 4 | The system reads data from the base table, deletes historical data from the index table, writes data to the index table, and writes data to the base table. |

Mutability options: If a base table has one index, the following operations are performed to complete a write operation: reading data from the base table, deleting the historical data from the index, writing data to the index, and writing data to the base table. This process increases the index maintenance cost. Write amplification does not occur in all scenarios. For example, data is only inserted, and no update operation is performed for each write request in logging scenarios. In this case, no historical data exists in the index table. The system only writes data to the index and writes data to the base table. Therefore, Lindorm introduces the concept of mutability. Mutability is used to classify the write patterns for base tables and organize index data to minimize the index organization costs to meet different business requirements. The following table describes the mutability types. You can use the Table_Options parameter to configure the mutability attribute for a table when you create or modify the table. For more information, see CREATE TABLE.

**Note**

If you set the mutability attribute to IMMUTABLE or IMMUTABLE_ROWS, no update operation is performed. As a result, no write amplification occurs, and the costs are minimized. These two mutability types are suitable for high-throughput data write scenarios, such as logging and monitoring. If you set the mutability attribute to IMMUTABLE, no delete operation is performed. This way, you can fully use the multi-data center deployment capability provided by Lindorm to implement active-active data access. If you set the mutability attribute to IMMUTABLE or IMMUTABLE_ROWS, the write latency can be decreased and the overall throughput can be improved for tables that have indexes. In an actual business scenario for which the IMMUTABLE type is not suitable, you can configure data redundancy to reform your business scenario. Index updates based on custom timestamps: Lindorm allows you to write data based on custom timestamps and update data based on a specific timestamp. The system determines that the update operation takes effect only on the data that is associated with the largest timestamp. The custom timestamp feature is important for managing data TTL and processing out-of-order data and idempotent operations. This feature is widely used in HBase databases. Lindorm supports column-level timestamps. You can write data to base tables based on custom timestamps. In NoSQL systems that support secondary indexes and timestamps, you can hardly update indexes based on custom timestamps. If data is not written in sequence based on timestamps, the update and delete operations that are performed on index data are difficult to manage. Lindorm provides the global secondary index (GSI) feature to resolve this issue. You can use GSIs to update data based on column-level custom timestamps. The following business scenarios are examples of using custom timestamps: Import historical data and update real-time data in one task: If you want to update real-time data and import historical data at the same time, you can specify the current timestamp for real-time data and specify 23:59:59 on the previous day for historical data. This way, the import operation updates the data that has not been updated on the day and does not overwrite the data that has been updated. Clear message accumulation: A business system uses messages to trigger a series of processing logic. When message accumulation occurs, the system skips the accumulated messages and directly processes the most recent message if the custom timestamp feature is used. After the most recent message is processed, the system processes the accumulated historical messages to handle the previous tasks. Alternatively, if an issue related to the business logic occurs, the system can also skip some messages to bypass the issue and process these messages after the issue is fixed. In this case, your business system can use the timestamps of messages to write data to ensure that the historical messages are correctly overwritten by the real-time messages. Covering indexes that contain all columns in base tables: In most cases, a covering index is created based on specific columns in a base table to prevent the base table from being scanned after the index is scanned. A common redundancy solution is to create a covering index that contains all the columns in a base table. Lindorm supports three redundancy modes. If the schema of a base table changes or a base table contains dynamic columns, you can create covering indexes for the base table to implement full redundancy. Create a covering index that contains specified columns in the base table: You can explicitly specify the columns in the base table as included columns. Create a covering index that contains all columns in the schema of a base table: When you create a covering index that contains all columns in a base table, you do not need to explicitly specify each column in the CREATE INDEX statement. Instead, you can use a constant to specify to include all the columns in the index. After the covering index is created, a column is automatically added to the covering index when the column is added to the base table. You do not need to rebuild the index. This also eliminates the need to scan the base table if you want to query the data in the newly added column. Create a covering index that contains dynamic columns in the base table: Lindorm supports fixed schemas and loose schemas. A loose schema refers to dynamic columns. If the DYNAMIC redundancy mode is used, the index table can automatically include all dynamic columns in the base table and all columns in the schema of the base table. For more information about how to use the SQL syntax supported by LindormTable, see LindormTable SQL in the Overview topic.

**Create a secondary index**

After you create a base table in a Lindorm instance, you can create a secondary index based on specified columns in the base table. The following procedure provides an example of how to create a secondary index for a base table: After you create a base table in a Lindorm instance, you can create a secondary index based on specified columns in the base table. The following procedure provides an example on how to create a secondary index for a base table:

**Note**

You can create indexes in a synchronous or asynchronous manner. If a base table contains a small amount of data, you can use the synchronous method to create an index. In other cases, we recommend that you use the asynchronous method. For more information about the syntax, see CREATE INDEX. When you execute the **CREATE_INDEX** statement to create an index for a base table that contains data, the statement also synchronizes the existing data in the base table to the index table. If the base table contains large amounts of data, the execution of the **CREATE_INDEX** statement requires a long period of time to complete. The data synchronization task is executed on the server. Even if the Lindorm Shell process is deleted, the data synchronization task is not affected. You can use Lindorm SQL to view the status of all secondary indexes that are created for a base table. The following statement provides an example:

```
show index from shop_item_relation;
```

**Note**

In this example, the statement returns the name and type of each secondary index that is created for the shop_item_relation base table.

**Change the status of a secondary index**

After a secondary index is created for a base table, you must rebuild the index if the base table contains data. For more information about the syntax, see BUILD INDEX. If the base table does not contain data, you can execute the ALTER INDEX statement to change the status of the secondary index. The following statements provide examples of how to change the status of a secondary index:

```
alter index idxs1 on shop_item_relation ACTIVE; alter index idxs1 on shop_item_relation DISABLED;
```

**Note**

If you directly change the status of a secondary index from DISABLED to ACTIVE, data may be lost. Therefore, you must rebuild the index in advance. You can execute the DROP INDEX statement to delete a secondary index for a specified base table. The following statement provides an example:

```
drop index idxs1 on shop_item_relation;
```

**Note**

Before you delete an index, make sure that your account is granted the TRASH permission. When you perform a query, Lindorm selects a secondary index based on the rule-based optimization (RBO) policy. Lindorm matches the prefixes of the associated index tables based on the query conditions and uses the index table that has the highest match rate as the index for the query. The following sample code provides examples of optimized queries:

```
-- Create a base table, and then create indexes for the base table. create table dt (rowkey varchar, c1 varchar, c2 varchar, c3 varchar, c4 varchar, c5 varchar, constr aint pk primary key(rowkey)); create index idx1 on dt (c1); create index idx2 on dt (c2, c3, c4); create index idx3 on dt (c3) include (c1, c2, c4); create index idx4 on dt (c5) 'INDEX_COVERED_TYPE'='COVERED_ALL_COLUMNS_IN_SCHEMA'; -- Execute the following statements to execute optimized queries: select rowkey from dt where c1 = 'a'; select rowkey from dt where c2 = 'b' and c4 = 'd'; select * from dt where c2 = 'b' and c3 >= 'c' and c3 < 'f'; select * from dt where c5 = 'c';
```

**Note**

When Lindorm executes the select rowkey from dt where c1 = 'a' statement, Lindorm selects the idx1 index to run this query. When Lindorm executes the select rowkey from dt where c2 = 'b' and c4 = 'd' statement, Lindorm selects the idx2 index to run this query. This statement queries all rows that match the c2=b condition and then filters the rows based on the c4=d condition row by row. Although c4 is specified as an index key column, the query fails to match the prefix of idx2 because column c3 is not defined in the WHERE condition. When Lindorm executes the select * from dt where c2 = 'b' and c3 >= 'c' and c3 < 'f' statement, Lindorm selects the idx2 index to run this query. All the columns in the base table are selected in the query, and the index table does not contain all the columns. As a result, a table scan is required after the index is scanned. When the system scans the base table, the system may make several remote procedure calls (RPCs) because the row key columns may be dispersed in the base table. If large amounts of data need to be scanned, the response time is long. When Lindorm executes the select * from dt where c5 = 'c' statement, Lindorm selects the idx4 index to run this query. This query does not need to scan the base table because the idx4 index contains all the columns in the base table.

### Lindorm SQL statements

#### Usage limits

The SQL syntax supported by LindormTable includes Data Definition Language (DDL), Data Manipulation Language (DML), and Data Control Language (DCL) statements. This topic describes the limits on the SQL syntax supported by LindormTable and the usage notes for SQL keywords. LindormTable Serverless does not support the SQL syntax. Relational operators such as the plus (+) operator and minus (-) operator are not supported.

| Term | Definition in Lindorm | Description |
|---|---|---|
| Schema | NameSpace | A logical concept that is similar to a database. A schema contains multiple tables. |
| Table | Table | When you create a table, you must create a schema for the table. A table schema specifies the names and data types of columns in the table. |
| PRIMARY KEY | PRIMARY KEY | A primary key that is used to uniquely identify each row of data and find the position of the row. |
| HASH Table | HASH Table | A hash table. If you use the USE HASH attribute for a table, data is _ randomly distributed based on primary key values to prevent frequent access to specific regions in the table. You cannot perform a sequential scan on the table when this attribute is used. |
| NUMREGIONS | NUMREGIONS | The number of data regions in Lindorm. This attribute is one of the attributes that can be configured for region pre-splitting when you create a table. |

Transactions are not supported. Functions such as HAVING, user-defined functions (UDFs), and VIEW are not supported. Complex operations such as subqueries and nested queries are not supported. The SUM, AVG, MIN, and MAX functions are supported. ORDER BY is conditionally supported. GROUP BY, DISTINCT, and JOIN are conditionally supported. Lindorm uses only in-memory computing. If you use a Lindorm cluster to process a large amount of data, a full garbage collection (GC) error or an out of memory (OOM) error occurs in the cluster. We recommend that you check whether the Lindorm cluster is capable of processing the given amount of data in advance. Table names and column names are case-sensitive.

**Usage notes for keywords**

If you use the following keywords in the SQL statements supported by LindormTable, you must escape the keywords by enclosing them in grave accents (`). The following keywords are not case-sensitive. ADD ADMIN_USER ADMIN_TRASH ALL ALLOW ALTER ANALYZE AND ANY ARRAY AS ASC ASYNC AT BERNOULLI BETWEEN BUILD BY CALL CALLED CASCADE CASE CAST CATALOGS COLUMN COLUMNS COMMENT COMMIT COMMITTED CONSTRAINT CREATE SEARCH SEARCH_QUERY INDEX INCLUDE CROSS CUBE CURRENT CURRENT_DATE CURRENT_ROLE CURRENT_TIME CURRENT_TIMESTAMP CURRENT_USER DATA DATABASE DATABASES DATE DAY DEALLOCATE DEFINER DELETE DESC DESCRIBE DETERMINISTIC DISTINCT DISTRIBUTED DROP DUPLICATE ELSE END ESCAPE EXCEPT EXCLUDING EXECUTE EXISTS EXPLAIN EXTRACT EXTERNAL FALSE FILTER FILTERING FIRST FOLLOWING FOR FORCE FORMAT FROM FULL FUNCTION FUNCTIONS GLOBAL GRANT GRANTED GRANTS GRAPHVIZ GROUP GROUPING HAVING HOUR IF IDENTIFIED IGNORE IN INCLUDING INNER INPUT INSERT INTERSECT INTERVAL INTO INVOKER IO IS ISOLATION JSON JOIN KEY LANGUAGE LAST LATERAL LEFT LEVEL LIKE LIMIT LOCALTIME LOCALTIMESTAMP LOGICAL MAP MINUTE MONTH NAME NAMESPACE NAMESPACES NATURAL NFC NFD NFKC NFKD NO NONE NORMAL_USER NORMALIZE NOT NULL NULLIF NULLS OLDPASSWORD ON ONLY ONLINE OFFLINE OFFSET OPTION OR ORDER ORDINARILY OUTER OUTPUT OVER PARTITION PARTITIONS PASSWORD POSITION PRECEDING PREPARE PRIMARY PRIVILEGES PROPERTIES RANGE READ RECURSIVE RENAME REPEATABLE REPLACE RESET RESPECT RESTRICT RETURN RETURNS REVOKE RIGHT ROLE ROLES ROLLBACK ROLLUP ROW ROWS SCHEMA SCHEMAS SECOND SECURITY SELECT SERIALIZABLE SESSION SET SETS SHOW SOME SQL START STATS SUBSTRING SYSTEM TABLE TABLES TABLESAMPLE TEXT THEN TIME TIMESTAMP TO TRASH TRANSACTION TRUE TRY_CAST TRUNCATE TYPE UESCAPE UNBOUNDED UNCOMMITTED UNION UNNEST UPDATE UPSERT USE USER USERS USING VALIDATE VALUES VERBOSE VIEW WHEN WHERE WITH WORK WRITE YEAR ZONE

#### Terms

This topic introduces the common terms that are used in SQL statements for LindormTable.

| STARTKEY and ENDKEY | STARTKEY and ENDKEY | The range of a data region in Lindorm. STARTKEY and ENDKEY are the attributes that can be configured for region pre-splitting when you create a table. You can leave STARTKEY and ENDKEY unspecified. |
|---|---|---|
| Mutability attribute | Mutability attribute | The attribute that must be configured when you create an index in Lindorm. Valid values: immutable, immutable rows, mutable latest, _ _ and mutable all. _ |
| Dynamic column | Dynamic column | A column that can be inserted without the need to predefine the column in Lindorm. |

| SQL data type | Java data type | Description |
|---|---|---|
| BOOLEAN | java.lang.Boolean | A value of this data type is 1 byte in length. This data type stores boolean values. Valid values: true and false. |
| TINYINT | java.lang.Byte | A value of this data type is 1 byte in length. The data type stores fixed-length exact values. The value range depends on the value length and whether the values are signed. |
| SMALLINT | java.lang.Short | A value of this data type is 2 bytes in length. The data type stores fixed-length exact values. The value range depends on the value length and whether the values are signed. |
| INTEGER | java.lang.Integer | A value of this data type is 4 bytes in length. The data type stores fixed-length exact values. The value range depends on the value length and whether the values are signed. |
| BIGINT | java.lang.Long | A value of this data type is 8 bytes in length. The data type stores fixed-length exact values. The value range depends on the value length and whether the values are signed. |
| FLOAT | java.lang.Float | A value of this data type is 4 bytes in length. The data type stores fixed-length approximate values. The value range and precision depend on the value length, precision, and scale, and whether the values are signed. |
| DOUBLE | java.lang.Double | A value of this data type is 8 bytes in length. The data type stores fixed-length approximate values. The value range and precision depend on the value length, precision, and scale, and whether the values are signed. All the values of the DOUBLE data type in SQL statements must be expressed in scientific notation. |

#### Data types

##### Supported basic data types

LindormTable SQL is a typed language that supports a wide range of data types. This topic describes the basic data types supported by LindormTable SQL. The value length of a single primary key column cannot exceed 2 KB. The value length of all primary key columns in the same table cannot exceed 30 KB. The value length of a single non-primary key column cannot exceed 2 MB.

| DECIMAL(precision, scale) | java.lang.BigDecimal | This data type stores variable-length binary values. The values of this data type are expressed in decimal notation. The number of bytes consumed by values of this data type increases with the value precision. The DECIMAL data type stores data that requires a high precision, such as payment amounts. For other data such as monitoring data, you can use the FLOAT or DOUBLE data type. When you define the DECIMAL data type, you must specify the precision and scale parameters. precision: specifies the total number of digits in a value. Valid values: 1 to 38. scale: specifies the number of decimal places in a value. Valid values: 0 to the specified precision. |
|---|---|---|
| VARCHAR / CHAR(N) | java.lang.String | The values of these data types are strings. Chinese characters are supported. The VARCHAR data type stores variable-length strings. The CHAR data type stores fixed-length strings. You must specify the length N. |
| BINARY(N) | byte[] | This data type stores fixed-length binary values. N specifies the number of bytes. When you write a value of this type, the system adds bytes to the value or deletes bytes from the value to match the fixed length: If the specified value is less than N bytes, the system automatically adds trailing zeroes to the value to match the fixed length. If the specified value exceeds N bytes, the system automatically truncates the extra bytes to match the fixed length. |
| VARBINARY | byte[] | This data type stores variable-length binary values. If a column of this data type is used as a primary key column, the column must be the last primary key column. |
| DATE | java.sql.Types#DATE | This data type is the date and time type. However, the system stores only date values but not time values. These date values are prone to errors during time zone conversion. This data type is not recommended. |
| TIME | java.sql.Types#TIME | This data type stores time values. |
| TIMESTAMP | java.sql.Types#TIMESTAM P | This data type stores timestamp values. |

| Data type | Description | Example |
|---|---|---|

Complex data types such as arrays are not supported.

##### Spatial data types

Spatial data is used to represent spatial objects, geographic locations, and object shapes. This type of data is commonly used in aviation, navigation, and urban planning. This topic describes the spatial data The following table describes the spatial data types that are supported by Lindorm GanosBase SQL.

| Geometry | The general type of all spatial data. Geometry objects include three types of objects: point objects, LineString objects, and polygon objects. We recommend that you do not set the data type of a spatial column to Geometry. | Specify the data type of spatial columns when you create a spatio-temporal table. |
|---|---|---|
| Point | The data type of point objects. A point object is identified by its coordinates that consist of a longitude x and a latitude y. Note Three-dimensional point objects cannot be used for calculation. Lindorm GanosBase converts three- dimensional point objects into two- dimensional point objects in the calculation. | Specify the GPS coordinates that are received by vehicles and ships. |
| LineString | The data type of LineString objects. A LineString object consists of two or more point objects. In a LineString object, the end point of a line segment must be the start point of the next line segment. Note A line segment must consist of two or more point objects. Two line segments can have the same vertex. | Specify a street that may consist of multiple LineString objects. Specify the trajectory of a vehicle within a specific time range. The trajectory consists of multiple point objects. |
| Polygon | The data type of polygon objects. The outer boundary of a polygon object is a closed line. The coordinates of the start point and end point of the line are the same. Note A polygon object can be identified by at least three point objects. | Specify geofences. Specify polygon objects such as land blocks, forests, and administrative divisions in maps. Specify graphics such as rectangles and circles. |

#### Functions

##### AS function

The AS function renames results of requests with aliases.

```
select count(*) as countRow from test; select c1 as testC from test where c1 = '2';
```

##### Aggregate functions

###### COUNT function

The COUNT function is used to count the number of non-empty values in a specified column. This function can be used to count the number of returned rows.

```
select count(*) from test; select count(*) from test where c1 = 1; select count(c1) from test where c1 = 1;
```

| Category | Documentation | Description |
|---|---|---|
| Output functions | Output functions | Returns the information about a geometry object in Well-known Text (WKT) format. |
|  | ST Centroid _ | Returns the centroid of the specified geometry object. |
|  | ST EndPoint _ | Returns the last point of the specified LineString object. |
|  | ST NPoints _ | Returns the number of vertexes in the specified geometry object. |

###### Max and min functions

The max function returns the maximum value in a specified column. The min function returns the minimum value in a specified column.

```
SELECT max(c1) FROM test; SELECT min(c1) FROM test;
```

###### Sum function

The sum function returns the sum of all values in a specified column.

```
select sum(c1) from test;
```

###### Avg function

The avg function returns the average of all the values in a specified column.

```
// Calculate the average of all the values in the c1 column of the test table. SELECT avg(c1) FROM test;
```

##### Spatio-temporal functions

###### Overview

This topic describes the spatio-temporal functions supported by Lindorm GanosBase. The following table describes the spatio-temporal functions that are supported by Lindorm GanosBase.

**Note**

The names of the spatio-temporal functions are case-insensitive.

| Access functions |  |  |
|---|---|---|
|  | ST StartPoint _ | Returns the start point of the specified LineString object. |
|  | ST X _ | Returns the x coordinate of the specified point object. |
|  | ST XMax _ | Returns the maximum x coordinate on the bounding box of the specified geometry object. |
|  | ST XMin _ | Returns the minimum x coordinate on the bounding box of the specified geometry object. |
|  | ST Y _ | Returns the y coordinate of the specified point object. |
|  | ST YMax _ | Returns the maximum y coordinate on the bounding box of the specified geometry object. |
|  | ST YMin _ | Returns the minimum y coordinate on the bounding box of the specified geometry object. |
| Functions for spatial relationships | ST Contains _ | Checks whether the first geometry object that you specify contains the second geometry object that you specify. If the first geometry object contains the second geometry object, this function returns true. |
|  | ST DWithin _ | Checks whether the 2D distance between two geometry objects is within the specified range. If the 2D distance between the objects is within the specified range, this function returns true. |
|  | ST DWithinSphere _ | Checks whether the spherical distance between two geometry objects is within the specified range. If the spherical distance between the objects is within the specified range, this function returns true. |
|  | ST Intersects _ | Checks whether two geometry objects intersect. If the two geometry objects have any shared spatial space, this function determines that the two objects intersect and returns true. |
|  | ST Overlaps _ | Checks whether two geometry objects spatially overlap but one is not contained in the other. If the two geometry objects spatially overlap but one is not contained in the other, this function returns true. |
| > Document Version | : 20250825 57 |  |

|  | ST Within _ | Checks whether the second geometry object that you specify completely lies in the first geometry object that you specify. If the second geometry object completely lies in the first geometry object, this function returns true. |
|---|---|---|
| Aggregate functions | ST Length Rows _ _ | Returns the spherical length of the trajectory aggregated by all points in the specified point column. The unit of the returned value is meter. This function reads all points in the specified point column in the order of the primary keys, and then calculates the length of the trajectory aggregated by the points. |
|  | ST TrajectoryProfile _ | Calculates the trajectory aggregated by all points in the specified point column based on the order of time data in the specified time column, and returns the trajectory segments divided by a specific time threshold. This function is usually used together with spatial query conditions, such as ST TrajectoryProfile, to determine _ whether a trajectory is within or outside of a specified range. |

| Parameter | Description |
|---|---|
| g | The geometry object whose information you want to output. |

###### Output functions

This topic describes the `ST_AsText` function. This function returns the information about a geometry object in Well-Known Text (WKT) format. The Spatial Reference IDentifier (SRID) of the geometry object is not returned.

```
string ST_AsText(geometry g);
```

**Parameters**

**Note**

The specified geometry object can be a point, LineString, or polygon object. By default, the returned results support DOUBLE values with up to 16 decimal places.

```
SELECT ST_AsText(ST_GeomFromText('POINT(111.1111111 1.1111111)')) AS text;
```

The following result is returned:

```
+-------------------------------+
|             text              |
+-------------------------------+ +-------------------------------+
```

| Parameter | Description |
|---|---|
| g | The geometry object whose centroid you want to obtain. |

| Parameter | Description |
|---|---|
| g | The geometry object whose last point you want to obtain. |

###### Access functions

This topic describes the access functions that are supported by Lindorm GanosBase.

**ST_Centroid**

You can call the `ST_Centroid` function to obtain the centroid of the specified geometry object.

```
geometry ST_Centroid(geometry g);
```

**Parameters**

**Note**

If the object is an empty geometry, the corresponding empty geometry is returned. Example 1:

```
SELECT ST_AsText(ST_Centroid(ST_Collect(ST_MakePoint(1,1),ST_MakePoint(-1,-1)))) AS astext;
```

The following result is returned:

```
+-------------+
|   astext    |
+-------------+ +-------------+
```

Example 2:

```
SELECT ST_AsText(ST_Centroid(ST_GeomFromText('LINESTRING(0 0,0 1,1 2)'))) AS astext;
```

The following result is returned:

```
+--------------------------------+
|             astext             |
+--------------------------------+
| 1.085786437626905)             |
+--------------------------------+
```

You can call the `ST_EndPoint` function to obtain the last point of the specified LineString object.

```
geometry ST_EndPoint(geometry g);
```

**Parameters**

| Parameter | Description |
|---|---|
| g | The geometry object whose number of vertexes you want to obtain. |

| Parameter | Description |
|---|---|
| g | The geometry object whose start point you want to obtain. |

**Note**

If the specified geometry object is not a LineString object, this function returns NULL.

```
SELECT ST_AsText(ST_EndPoint(ST_GEOMFROMTEXT('LINESTRING(1 1, 2 2, 3 3)'))) AS endpoint;
```

The following result is returned:

```
+-------------+ +-------------+ +-------------+
```

You can call the `ST_NPoints` function to obtain the number of vertexes in the specified geometry object. This function applies to all types of supported geometry objects.

```
int ST_NPoints(geometry g);
```

**Parameters**

```
SELECT ST_NPoints(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)')) A S npoints;
```

The following result is returned:

```
+---------+ +---------+
| 4       |
+---------+
```

You can call the `ST_StartPoint` function to obtain the start point of the specified LineString object.

```
geometry ST_StartPoint(geometry g);
```

**Parameters**

| Parameter | Description |
|---|---|
| a point _ | The geometry object whose x coordinate you want to obtain. |

| Parameter | Description |
|---|---|
| g | The geometry object whose maximum x coordinate on the bounding box you want to obtain. |

**Note**

If the specified geometry object is not a LineString object, this function returns NULL.

```
SELECT ST_AsText(ST_StartPoint(ST_GEOMFROMTEXT('LINESTRING(0 1, 0 2)'))) AS startpoint;
```

The following result is returned:

```
+-------------+ +-------------+ +-------------+
```

**ST_X**

You can call the `ST_X` function to obtain the x coordinate of the specified point object.

```
double ST_X(geometry a_point);
```

**Parameters**

**Note**

The specified geometry object must be a point object. If you set this parameter to EMPTY or NULL, this function returns NULL.

```
SELECT ST_X(ST_MakePoint(1.0, 2.0)) AS x;
```

The following result is returned:

```
+---+
| x |
+---+
| 1 |
+---+
```

**ST_XMax**

You can call the `ST_XMax` function to obtain the maximum x coordinate on the bounding box of the specified geometry object.

```
double ST_XMax(geometry g);
```

**Parameters**

| Parameter | Description |
|---|---|
| g | The geometry object whose minimum x coordinate on the bounding box you want to obtain. |

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. If you set this parameter to EMPTY, this function returns -1.

```
SELECT ST_XMax(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS xmax;
```

The following result is returned:

```
+------+
| xmax |
+------+
| 5    |
+------+
```

**ST_XMin**

You can call the `ST_XMin` function to obtain the minimum x coordinate on the bounding box of the specified geometry object.

```
double ST_XMin(geometry g);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. If you set this parameter to EMPTY, this function returns 0.

```
SELECT ST_XMin(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS xmin;
```

The following result is returned:

```
+------+
| xmin |
+------+
| 1    |
+------+
```

**ST_Y**

You can call the `ST_Y` function to obtain the y coordinate of the specified point object.

```
double ST_Y(geometry a_point);
```

**Parameters**

| Parameter | Description |
|---|---|
| a point _ | The geometry object whose y coordinate you want to obtain. |

| Parameter | Description |
|---|---|
| g | The geometry object whose maximum y coordinate on the bounding box you want to obtain. |

**Note**

The specified geometry object must be a point object. If you set this parameter to EMPTY or NULL, this function returns NULL.

```
SELECT ST_Y(ST_MakePoint(1.0, 2.0)) AS y;
```

The following result is returned:

```
+---+
| y |
+---+
| 2 |
+---+
```

**ST_YMax**

You can call the `ST_YMax` function to obtain the maximum y coordinate on the bounding box of the specified geometry object.

```
double ST_YMax(geometry g);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. If you set this parameter to EMPTY, this function returns -1.

```
SELECT ST_YMax(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS ymax;
```

The following result is returned:

```
+------+
| ymax |
+------+
| 6    |
+------+
```

**ST_YMin**

You can call the `ST_YMin` function to obtain the minimum y coordinate on the bounding box of the specified geometry object.

| Parameter | Description |
|---|---|
| g | The geometry object whose minimum y coordinate on the bounding box you want to obtain. |

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

```
double ST_YMin(geometry g);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. If you set this parameter to EMPTY, this function returns 0.

```
SELECT ST_YMin(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS ymin;
```

The following result is returned:

```
+------+
| ymin |
+------+
| 3    |
+------+
```

###### Functions for spatial relationships

This topic describes the functions that are supported by Lindorm GanosBase to determine the spatial relationships between geometry objects.

**ST_Contains**

You can call the `ST_Contains` function to determine whether the first geometry object that you specify contains the second geometry object that you specify. If the first geometry object contains the second geometry object, this function returns true. Determine whether a geometry object contains another geometry object.

```
boolean ST_Contains(geometry geomA, geometry geomB);
```

Determine whether a geometry object contains the specified point object.

```
boolean ST_Contains(geometry g, double x, double y);
```

**Parameters**

**Note**

If all points of geomB are contained in the interior or on the boundary of geomA, geomA contains geomB. `ST_Contains` is the inverse function of `ST_Within` . The returned results of ST_Contains(A,B) and ST_Within(B,A) are the same. Example 1:

```
SELECT ST_Contains(ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))'), ST_GeomFromText('POINT(5 5)')) AS iscontain;
```

The following result is returned:

```
+-----------+
| iscontain |
+-----------+
| true      |
+-----------+
```

Example 2:

```
SELECT ST_Contains(ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))'),5,5) AS iscontain;
```

The following result is returned:

```
+-----------+
| iscontain |
+-----------+
| true      |
+-----------+
```

Example 3:

```
SELECT ST_Contains(ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))'), ST_GeomFromText('POINT(180 23)')) AS iscontain;
```

The following result is returned:

```
+-----------+
| iscontain |
+-----------+
| false     |
+-----------+
```

Example 4:

```
SELECT ST_Contains(ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))'),180,23) AS iscontain ;
```

The following result is returned:

```
+-----------+
| iscontain |
+-----------+
| false     |
+-----------+
```

**ST_DWithin**

You can call the `ST_DWithin` function to determine whether the 2D distance between two geometry objects is within the specified range. If the 2D distance between the objects is within the specified range, this function returns true. The distance specified in the function is measured in degrees.

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| distanceOfSrid | The distance in Spatial Reference System Identifier (SRID) 4326. Unit: degree. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

Determine whether the 2D distance between two geometry objects is within the specified range.

```
boolean ST_DWithin(geometry geomA, geometry geomB, double distanceOfSrid);
```

Determine whether the 2D distance between a geometry object and the specified point object is within the specified range.

```
boolean ST_DWithin(geometry g, double x, double y, double distanceOfSrid);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. Example 1:

```
SELECT ST_DWithin(ST_GeomFromText('POINT(5 5)'), ST_GeomFromText('POINT(6 6)'), 10) AS iswithin;
```

The following result is returned:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

Example 2:

```
SELECT ST_DWithin(ST_GeomFromText('POINT(5 5)'),6,6,10) AS iswithin;
```

The following result is returned:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

**ST_DWithinSphere**

You can call the `ST_DWithinSphere` function to determine whether the spherical distance between two geometry objects is within the specified range. If the spherical distance between the objects is within the specified range, this function returns true. The distance specified in the function is measured in meters. The function may have an error of centimeters when it determines the spherical distance.

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| distance | The spherical distance that you want to specify. Unit: meters. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

| Example 1: |  |  |
|---|---|---|
| SELECT ST DWithinSphere(ST GeomFromText('POINT(120 36)'), ST GeomFromText('POINT(116 40)'), 57000 _ _ _ 0) AS iswithin; |  |  |

Determine whether the spherical distance between two geometry objects is within the specified range.

```
boolean ST_DWithinSphere(geometry geomA, geometry geomB, double distance);
```

Determine whether the spherical distance between a geometry object and the specified point object is within the specified range.

```
boolean ST_DWithinSPhere(geometry g, double x, double y, double distance);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. The function may have an error of centimeters when it determines the spherical distance. In this example, the spherical distance between the point (120,36) and the point (116,40) is 566034.7930717631 meters, which falls within the specified range. Therefore, the ST_DWithinSphere function returns true, as shown in the following result:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

Example 2:

```
SELECT ST_DWithinSphere(ST_GeomFromText('POINT(120 36)'),116,40,570000) AS iswithin;
```

The following result is returned:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

**ST_Intersects**

You can call the ST_Intersects function to determine whether two geometry objects intersect. If the two geometry objects have any shared spatial space, `ST_Intersects` determines that the two objects intersect and returns true.

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

Determine whether two geometry objects intersect.

```
boolean ST_ Intersects(geometry geomA, geometry geomB);
```

Determine whether a geometry object and the specified point object intersect.

```
boolean ST_ Intersects(geometry g, double x, double y);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. Example 1:

```
SELECT ST_Intersects(ST_GeomFromText('POINT(0 0)'), ST_GeomFromText('LINESTRING ( 2 0, 0 2 )')) A S isinter;
```

The following result is returned:

```
+---------+
| isinter |
+---------+
| false   |
+---------+
```

Example 2:

```
SELECT ST_Intersects(ST_GeomFromText('LINESTRING ( 2 0, 0 2 )'), 0, 0) AS isinter;
```

The following result is returned:

```
+---------+
| isinter |
+---------+
| false   |
+---------+
```

Example 3:

```
SELECT ST_Intersects(ST_GeomFromText('POINT(0 0)'), ST_GeomFromText('LINESTRING ( 0 0, 0 2 )')) A S isinter;
```

The following result is returned:

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

```
+---------+
| isinter |
+---------+
| true    |
+---------+
```

Example 4:

```
SELECT ST_Intersects(ST_GeomFromText('LINESTRING ( 0 0, 0 2 )'), 0, 0) AS isinter;
```

The following result is returned:

```
+---------+
| isinter |
+---------+
| true    |
+---------+
```

**ST_Overlaps**

You can call the `ST_Overlaps` object to determine whether two geometry objects spatially overlap but one is not included in the other. If the two geometry objects spatially overlap but one is not included in the other, this function returns true. Determine whether two geometry objects spatially overlap.

```
boolean ST_Overlaps(geometry geomA, geometry geomB);
```

Determine whether a geometry object and the specified point object overlap.

```
boolean ST_Overlaps(geometry g, double x, double y);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. Example 1:

```
SELECT ST_Overlaps(ST_GeomFromText('LINESTRING(0 0,0 2)'),ST_GeomFromText('LINESTRING(0 1,0 3)')) as overlaps;
```

The following result is returned:

```
+----------+
| overlaps |
+----------+
| true     |
+----------+
```

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| g | The geometry object that you want to specify. |
| x | The longitude of the point object. |
| y | The latitude of the point object. |

Example 2:

```
SELECT ST_Overlaps(ST_GeomFromText('LINESTRING(0 0,0 2)'),ST_GeomFromText('POINT(0 1)')) as overl aps;
```

The following result is returned:

```
+----------+
| overlaps |
+----------+
| false    |
+----------+
```

Example 3:

```
SELECT ST_Overlaps(ST_GeomFromText('LINESTRING(0 0,0 2)'), 0, 1) as overlaps;
```

The following result is returned:

```
+----------+
| overlaps |
+----------+
| false    |
+----------+
```

**ST_Within**

You can call the `ST_Within` function to determine whether the second geometry object that you specify completely lies in the first geometry object that you specify. If the second geometry object completely lies in the first geometry object, this function returns true. Determine whether a geometry object completely lies in another geometry object.

```
boolean ST_Within(geometry geomA, geometry geomB);
```

Determine whether the specified point object lies in a geometry object.

```
bboolean ST_Within(double x, double y, geometry g);
```

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. If true is returned by both `ST_Within(A,B)` and `ST_Within(B,A)` , A and B are geometry objects that are spatially equal. Example 1:

| Parameter | Description |
|---|---|
| g | The source geometry object based on which the spherical distance of points is calculated. |
| radius | The 2D distance from the source geometry object to the points of the buffer geometry object. Unit: degree. |

```
SELECT ST_Within(ST_GeomFromText('POINT(5 5)'), ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))')) AS iswithin;
```

The following result is returned:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

Example 2:

```
SELECT ST_Within(5, 5, ST_GeomFromText('POLYGON((0 0, 0 10, 10 10, 10 0, 0 0))')) AS iswithin;
```

The following result is returned:

```
+----------+
| iswithin |
+----------+
| true     |
+----------+
```

###### Processing functions

This topic describes the processing functions that are supported by Lindorm GanosBase.

**ST_Buffer**

You can call the `ST_Buffer` function to obtain a buffer geometry object consisting of all points whose 2D distance to a specified source geometry object is equal to the specified radius.

```
ST_Buffer(geometry g, double radius);
```

**Parameters**

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If you specify a positive value for **radius**, the buffer geometry object rings away from the center of the source geometry object. If you specify a negative value for **radius**, the buffer geometry object rings towards the center of the source geometry object. The returned geometry may be empty. Only the default buffer style is supported. By default, the value of quadrantSegments is 8, and the value of endCapStyle is round. Example 1:

```
SELECT ST_AsText(ST_Buffer(ST_GeomFromText('POINT(120.18 30.25)'), 0.05)) AS buffer;
```

The following result is returned:

```
+--------------------------------+
|             buffer             |
+--------------------------------+
| POLYGON ((120.23 30.25,        |
| 120.22903926402017             |
| 30.240245483899194,            |
| 120.22619397662557             |
| 30.230865828381745,            |
| 120.22157348061513             |
| 30.22222148834902,             |
| 120.21535533905933             |
| 30.21464466094067,             |
| 120.20777851165099             |
| 30.208426519384872,            |
| 120.19913417161825             |
| 30.203806023374437,            |
| 120.18975451610082             |
| 30.200960735979837, 120.18     |
| 30.2, 120.1702454838992        |
| 30.200960735979837,            |
| 120.16086582838176             |
| 30.203806023374437,            |
| 120.15222148834903             |
| 30.208426519384872,            |
| 120.14464466094068             |
| 30.21464466094067,             |
| 120.13842651938488             |
| 30.22222148834902,             |
| 120.13380602337445             |
| 30.230865828381745,            |
| 120.13096073597984             |
| 30.240245483899194,            |
| 120.13000000000001             |
| 30.25, 120.13096073597984      |
| 30.259754516100806,            |
| 120.13380602337445             |
| 30.269134171618255,            |
| 120.13842651938488             |
| 30.27777851165098,             |
| 120.14464466094068             |
| 30.28535533905933,             |
| 120.15222148834903             |
| 30.291573480615128,            |
| 120.16086582838176             |
| 30.296193976625563,            |
| 120.1702454838992              |
| 30.299039264020163, 120.18     |
| 30.3, 120.18975451610082       |
| 30.299039264020163,            |
| 120.19913417161825             |
| 30.296193976625563,            |
| 120.20777851165099             |
| 30.291573480615128,            |
| 120.21535533905933             |
| 30.28535533905933,             |
| 120.22157348061513             |
| 30.27777851165098,             |
| 120.22619397662557             |
| 30.269134171618255,            |
|12022903926402017
```

|

```
| 120.22903926402017             |
| 30.259754516100806, 120.23     |
| 30.25))                        |
+--------------------------------+
```

Example 2:

```
SELECT ST_AsText(ST_Buffer(ST_GeomFromText('LINESTRING (120.18 30.25, 120.16 30.23)'), 0.01)) AS buffer;
```

The following result is returned:

```
+--------------------------------+
|             buffer             |
+--------------------------------+
| POLYGON ((120.16707106781186   |
| 30.222928932188132,            |
| 120.1655557023302              |
| 30.221685303876974,            |
| 120.16382683432364             |
| 30.220761204674886,            |
| 120.16195090322016             |
| 30.220192147195966, 120.16     |
| 30.22, 120.15804909677983      |
| 30.22019214719597,             |
| 120.15617316567635             |
| 30.22076120467489,             |
| 120.1544442976698              |
| 30.221685303876978,            |
| 120.15292893218813             |
| 30.222928932188136,            |
| 120.15168530387697             |
| 30.224444297669805,            |
| 120.15076120467488             |
| 30.226173165676354,            |
| 120.15019214719597             |
| 30.22804909677984,             |
| 120.14999999999999             |
| 30.230000000000004,            |
| 120.15019214719597             |
| 30.231950903220163,            |
| 120.15076120467488             |
| 30.233826834323654,            |
| 120.15168530387697             |
| 30.2355557023302,              |
| 120.15292893218813             |
| 30.23707106781187,             |
| 120.17292893218814             |
| 30.257071067811868,            |
| 120.17444429766981             |
| 30.258314696123026,            |
| 120.17617316567636             |
| 30.259238795325114,            |
| 120.17804909677984             |
| 30.259807852804034, 120.18     |
| 30.26, 120.18195090322017      |
| 30.25980785280403,             |
| 120.18382683432365             |
| 30.25923879532511,             |
| 120.1855557023302              |
| 30.258314696123023,            |
| 120.18707106781187             |
| 30.257071067811864,            |
```

| Parameter | Description |
|---|---|
| g | The source geometry object based on which the spherical distance of points is calculated. |
| radius | The spherical distance from the source geometry object to the points of the buffer geometry object. Unit: meter. |

```
| 120.18831469612303             |
| 30.255555702330195,            |
| 120.18923879532512             |
| 30.253826834323647,            |
| 120.18980785280404             |
| 30.25195090322016,             |
| 120.19000000000001             |
| 30.249999999999996,            |
| 120.18980785280404             |
| 30.248049096779837,            |
| 120.18923879532512             |
| 30.246173165676346,            |
| 120.18831469612303             |
| 30.2444442976698,              |
| 120.18707106781187             |
| 30.242928932188132,            |
| 120.16707106781186             |
| 30.222928932188132))           |
+--------------------------------+
```

**ST_BufferSphere**

You can call the `ST_BufferSphere` function to obtain a buffer geometry object that consisting of all points whose spherical distance to a specified source geometry object is equal to the specified radius.

```
ST_BufferSphere(geometry g, double radius);
```

**Parameters**

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If you specify a positive value for **radius**, the buffer geometry object rings away from the center of the source geometry object. If you specify a negative value for **radius**, the buffer geometry object rings towards the center of the source geometry object. The returned geometry may be empty. Only the default buffer style is supported. By default, the value of quadrantSegments is 8, and the value of endCapStyle is round. Example 1:

```
SELECT ST_AsText(ST_BufferSphere(ST_GeomFromText('POINT(120.18 30.25)'), 500)) AS buffer;
```

The following result is returned:

```
+--------------------------------+
|             buffer             |
+--------------------------------+
| POLYGON ((120.1851909310331    |
| 30.25011173053024,             |
```

|
,
|

```
| 120.18511627294788             |
| 30.249230378090658,            |
| 120.18484500297895             |
| 30.248378605521545,            |
| 120.18438755060062             |
| 30.247589145091563,            |
| 120.1837614989031              |
| 30.246892333708224,            |
| 120.18299090835872             |
| 30.24631494733322,             |
| 120.18210539193977             |
| 30.245879172318283,            |
| 120.18113897716789             |
| 30.24560175314354,             |
| 120.18012879881775             |
| 30.245493349257533,            |
| 120.17911367245745             |
| 30.245558125686234,            |
| 120.17813260355221             |
| 30.245793593106626,            |
| 120.17722328930826             |
| 30.246190703510113,            |
| 120.17642067070908             |
| 30.24673419777976,             |
| 120.17575559027851             |
| 30.247403191844143,            |
| 120.17525360707266             |
| 30.248171978919647,            |
| 120.1749340144007              |
| 30.249011017060198,            |
| 120.17480909803247             |
| 30.249888064116504,            |
| 120.17488366345407             |
| 30.250769416537622,            |
| 120.17515485043153             |
| 30.251621204446096,            |
| 120.17561224212514             |
| 30.252410693237966,            |
| 120.17623826468355             |
| 30.253107541687907,            |
| 120.17700886207045             |
| 30.253684968191145,            |
| 120.17789442027193             |
| 30.254120780286797,            |
| 120.1788609054053              |
| 30.25439822784955,             |
| 120.17987117198402             |
| 30.25450664710903,             |
| 120.18088639100795             |
| 30.254441870698788,            |
| 120.18186754290468             |
| 30.254206387939035,            |
| 120.1827769178333              |
| 30.25380924917365,             |
| 120.1835795655716              |
| 30.253265717837415,            |
| 120.1842446391596              |
| 30.252596683644782,            |
| 120.18474658058295             |
| 30.251827859488568,            |
| 120.18506610289342             |
```

```
| 30.250988792960012,            |
| 120.1851909310331              |
| 30.25011173053024))            |
+--------------------------------+
```

Example 2:

```
SELECT ST_AsText(ST_BufferSphere(ST_GeomFromText('LINESTRING (120.18 30.25, 120.16 30.23)'), 20)) AS buffer;
```

The following result is returned:

```
+--------------------------------+
|             buffer             |
+--------------------------------+
| POLYGON ((120.1601568095326    |
| 30.229881789491696,            |
| 120.16012723865646             |
| 30.22985749603038,             |
| 120.16009277809007             |
| 30.229838678911875,            |
| 120.16005475213065             |
| 30.229826061263992,            |
| 120.16001462208855             |
| 30.22982012797305,             |
| 120.15997393013107             |
| 30.229821107050387,            |
| 120.15993424001891             |
| 30.22982896087028,             |
| 120.15989707701289             |
| 30.229843387615915,            |
| 120.15986386926043             |
| 30.229863832877875,            |
| 120.15983589291346             |
| 30.229889510959428,            |
| 120.15981422308717             |
| 30.229919435069952,            |
| 120.15979969254388             |
| 30.22995245524614,             |
| 120.15979285969011             |
| 30.22998730254394,             |
| 120.15979398711634             |
| 30.23002263780298,             |
| 120.15980303150468             |
| 30.230057103109367,            |
| 120.15981964529222             |
| 30.230089373979652,            |
| 120.15984319002649             |
| 30.230118210260056,            |
| 120.17984317814214             |
| 30.250118233425205,            |
| 120.17987275990819             |
| 30.250142523059253,            |
| 120.17990723145967             |
| 30.250161335607235,            |
| 120.17994526807108             |
| 30.250173948109982,            |
| 120.17998540801094             |
| 30.250179875873307,            |
| 120.18002610871608             |
| 30.25017889109486,             |
| 120.18006580607275             |
|3025017103161881
```

|

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |
| geomN | The Nth geometry object that you want to specify. |

```
| 30.25017103161881,             |
| 120.18010297452594             |
| 30.250156599481485,            |
| 120.18013618570674             |
| 30.25013614930418,             |
| 120.18016416332479             |
| 30.25011046697896,             |
| 120.18018583221566             |
| 30.250080539466826,            |
| 120.18020035965924             |
| 30.250047516868772,            |
| 120.18020718737982             |
| 30.25001266822753,             |
| 120.18020605299972             |
| 30.249977332758547,            |
| 120.18019700012098             |
| 30.2499428683844,              |
| 120.18018037664854             |
| 30.249910599550603,            |
| 120.1801568214192              |
| 30.249881766327974,            |
| 120.1601568095326              |
| 30.229881789491696))           |
+--------------------------------+
```

**ST_Collect**

You can call the `ST_Collect` function to combine two or more geometry objects into a MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection object.

```
ST_Collect(geometry geomA, geometry geomB); ST_Collect(geometry geomA, geometry geomB, ...,geometry geomN);
```

**Parameters**

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |

**Note**

The `ST_Collect` function returns a MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection object. These types of objects can only be read, but cannot be written by Lindorm GanosBase SQL. The `ST_Collect` function and `ST_Union` can be interchanged in usage. However, the two functions have the following differences: The `ST_Collect` function returns a MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection object. The `ST_Union` may return a single geometry object. The `ST_Union` function splits a LineString object at the intersection of nodes, while the `ST_Collect` function returns a MultiLineString object. In general, the computing performance of `ST_Collect` is superior to `ST_Union` . This is because `ST_Collect` does not split the boundary of the specified geometry objects or check whether the specified MultiPolygon objects overlap. ST_Collect combines multiple geometry objects into a MultiPoint, MultiLineString, or MultiPolygon object or combines multiple MultiPoint, MultiLineString, or MultiPolygon objects into a GeometryCollection object. Example 1: Obtain a MultiPoint object.

```
SELECT ST_AsText(ST_Collect(ST_MakePoint(0,0),ST_MakePoint(0,1))) AS g;
```

The following result is returned:

```
+---------------------------+
|             g             |
+---------------------------+ +---------------------------+
```

Example 2: Obtain a GeometryCollection object.

```
SELECT ST_AsText(ST_Collect(ST_MakePoint(0,0),ST_GeomFromText('LINESTRING(0 2,0 3)'))) AS g;
```

The following result is returned:

```
+--------------------------------+
|               g                |
+--------------------------------+
| 0), LINESTRING (0 2, 0 3))     |
+--------------------------------+
```

**ST_Difference**

You can call the `ST_Difference` function to obtain a geometry object representing the part that the first geometry object that you specify does not intersect with the second geometry object that you specify.

```
ST_Difference(geometry geomA, geometry geomB);
```

**Parameters**

| Parameter | Description |
|---|---|
| g | The geometry object that is fully contained by the returned cycle. |

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If the first geometry object that you specify is empty or is fully contained by the second geometry object that you specify, an empty object is returned. If you specify a polygon that has intersecting edges, this function may not return a result. The order of the input geometry objects affects the output geometry object.

```
SELECT ST_AsText(ST_Difference(ST_GeomFromText('LINESTRING(50 100, 50 200)'),ST_GeomFromText('LINESTRING(50 50, 50 150)'))) AS diff;
```

The following result is returned:

```
+-----------------------------+
|            diff             |
+-----------------------------+
| LINESTRING (50 150, 50 200) |
+-----------------------------+
```

**ST_MinimumBoundingCircle**

You can call the `ST_MinimumBoundingCircle` function to obtain the smallest circle that can fully contain the specified geometry object.

```
ST_MinimumBoundingCircle(geometry g);
```

**Parameters**

**Note**

The `ST_MinimumBoundingCircle` function is commonly used for MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection objects. This function is not an aggregate function. However, you can use this function together with the `ST_Collect` function to obtain the smallest bounding circle of a set of geometry objects. Example:

```
 ST_MinimumBoundingCircle(ST_Collect(geometry geomA, geometry geomB, geometry geomC, ...)) .
SELECT ST_AsText(ST_MinimumBoundingCircle(ST_GeomFromText('POLYGON((0 0,1 0,1 1,0 1,0 0))'))) AS g;
```

The following result is returned:

```
+--------------------------------+
|               g                |
+--------------------------------+
| POLYGON ((1.2071067811865475   |
| 0.5, 1.1935199226610738        |
| 0.3620503103585285,            |
| 1.1532814824381883             |
| 0.2294019499269015,            |
| 1.0879378012096794             |
|01071525208064489
```

|

```
| 0.1071525208064489, 1          |
| 0, 0.8928474791935512          |
| -0.0879378012096794,           |
| 0.7705980500730986             |
| -0.1532814824381883,           |
| 0.6379496896414716             |
| -0.1935199226610738,           |
| 0.5 -0.2071067811865476,       |
| 0.3620503103585285             |
| -0.1935199226610738,           |
| 0.2294019499269015             |
| -0.1532814824381883,           |
| 0.107152520806449              |
| -0.0879378012096794,           |
| 0 -0.0000000000000001,         |
| -0.0879378012096794            |
| 0.1071525208064489,            |
| -0.1532814824381883            |
| 0.2294019499269014,            |
| -0.1935199226610738            |
| 0.3620503103585282,            |
| -0.2071067811865476            |
| 0.4999999999999999,            |
| -0.1935199226610738            |
| 0.6379496896414716,            |
| -0.1532814824381884            |
| 0.7705980500730985,            |
| -0.0879378012096795            |
| 0.892847479193551,             |
| -0.0000000000000001            |
| 1, 0.1071525208064489          |
| 1.0879378012096794,            |
| 0.2294019499269011             |
| 1.1532814824381883,            |
| 0.3620503103585282             |
| 1.1935199226610735,            |
| 0.4999999999999999             |
| 1.2071067811865475,            |
| 0.6379496896414716             |
| 1.1935199226610738,            |
| 0.7705980500730987             |
| 1.1532814824381883,            |
| 0.8928474791935508             |
| 1.0879378012096796,            |
| 0.9999999999999999             |
| 1, 1.0879378012096794          |
| 0.892847479193551,             |
| 1.1532814824381883             |
| 0.7705980500730989,            |
| 1.1935199226610735             |
| 0.6379496896414718,            |
| 1.2071067811865475 0.5))       |
+--------------------------------+
```

**ST_MinimumBoundingRadius**

You can call the `ST_MinimumBoundingRadius` function to obtain the radius of the smallest circle that can fully contain the specified geometry object.

| Parameter | Description |
|---|---|
| g | The geometry object that is fully contained by the returned cycle. |

| Parameter | Description |
|---|---|
| geomA | The first geometry object that you want to specify. |
| geomB | The second geometry object that you want to specify. |

```
ST_MinimumBoundingRadius(geometry g);
```

**Parameters**

**Note**

By default, the returned results support DOUBLE values with up to 16 decimal places. You can use this function together with the `ST_Collect` function to obtain the radius of the smallest bounding circle of a set of geometry objects.

```
SELECT ST_MinimumBoundingRadius(ST_GeomFromText('POLYGON((0 1,-1 0,0 -1,1 0,0 1))')) AS radius;
```

The following result is returned:

```
+----------+
|  radius  |
+----------+
|   1.0    |
+----------+
```

**ST_Intersection**

You can call the `ST_Intersection` function to obtain a geometry object representing the part that the first geometry object that you specify intersects with the second geometry object that you specify.

```
ST_Intersection(geometry geomA, geometry geomB);
```

**Parameters**

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If one of the specified geometry objects is empty, an empty object is returned. If you specify a polygon that has intersecting edges, this function may not return a result.

```
SELECT ST_AsText(ST_Intersection(ST_GeomFromText('POINT(0 0)'), ST_GeomFromText('LINESTRING ( 0 0, 0 2 )'))) AS inter;
```

The following result is returned:

| Parameter | Description |
|---|---|
| g1 | The first geometry object that you want to specify. |
| g2 | The second geometry object that you want to specify. |
| gn | The Nth geometry object that you want to specify. |

```
+-------------+ +-------------+ +-------------+
```

**ST_Union**

You can call the `ST_Union` function to obtain a geometry object representing the union of multiple specified geometry objects.

```
ST_Union(geometry g1, geometry g2, ..., geometry gn);
```

**Note**

This function can return a single geometry object, a MultiPoint, MultiLineString, or MultiPolygon object, or a GeometryCollection object.

**Parameters**

**Note**

Geometry objects supported by this function include point, LineString, and polygon objects. The type of geometry objects returned by this function varies based on the input parameters that you specify: If you specify two geometry objects, this function returns a single geometry object, a MultiPoint, MultiLineString, or MultiPolygon object, or a GeometryCollection object. If one of the two geometry objects that you specify is NULL, this function returns NULL. If one of the two geometry objects that you specify is an empty object, this function returns the other geometry object. If you specify two or more geometry objects, this function returns a single geometry object or a MultiPoint, MultiLineString, or MultiPolygon object. The `ST_Collect` function and the `ST_Union` function can be interchanged in usage. In general, the computing performance of `ST_Collect` is superior to `ST_Union` . This is because `ST_Collect` does not split the boundary of the specified geometry objects or check whether the specified MultiPolygon objects overlap. If you specify a polygon that has intersecting edges, this function may not return a result.

```
SELECT ST_AsText(ST_Union(ST_MakePoint(1.0, 1.0), ST_MakePoint(2.0, 2.0))) AS u;
```

The following result is returned:

```
+---------------------------+
|             u             |
+---------------------------+ +---------------------------+
```

| Parameter | Description |
|---|---|
| g | The geometry object that you want to specify. |

**ST_MakeValid**

You can call the `ST_MakeValid` function to convert an invalid geometry object to a valid geometry object.

```
geometry ST_MakeValid(geometry g);
```

**Parameters**

**Note**

You can call the `ST_MakeValid` function to convert a self-intersecting Polygon object into a MultiPolygon object that consists of multiple Polygon objects. For a MultiPolygon object that consists of multiple overlapping Polygon objects, you can call the `ST_MakeValid` function to calculate the union of the overlapping Polygon objects and merge the objects into one Polygon object. Example 1: Convert a self-intersecting Polygon object into a MultiPolygon object that consists of multiple Polygon objects without self-intersection.

```
SELECT ST_AsText(geom) as original, ST_AsText(ST_MakeValid(geom)) AS validated FROM mapdata WHERE id=10000001;
```

The following result is returned:

```
+--------------------------------+--------------------------------+
|            original            |           validated            |
+--------------------------------+--------------------------------+
| POLYGON ((0 0, 10 10, 0 10, 10 | MULTIPOLYGON (((0 0, 5 5, 10   |
| 0, 0 0))                       | 0, 0 0)), ((5 5, 0 10, 10 10,  |
|                                | 5 5)))                         |
+--------------------------------+--------------------------------+
```

Example 2: Convert a MultiPolygon object that consists of multiple overlapping Polygon objects into a Polygon object that is the union of the overlapping Polygon objects.

```
SELECT ST_AsText(geom) as original, ST_AsText(ST_MakeValid(geom)) AS validated FROM mapdata WHERE adcode=10000002;
```

The following result is returned:

```
+--------------------------------+--------------------------------+
|            original            |           validated            |
+--------------------------------+--------------------------------+
| MULTIPOLYGON (((0 0, 5 6, 10   | POLYGON ((4.166666666666667    |
| 0, 0 0)), ((5 4, 0 10, 10 10,  | 5, 0 10, 10 10,                |
| 5 4)))                         | 5.833333333333333 5, 10 0, 0   |
|                                | 0, 4.166666666666667 5))       |
+--------------------------------+--------------------------------+
```

###### Measurement functions

This topic describes the measurement functions that are supported by Lindorm GanosBase.

**ST_Area**

| Parameter | Description |
|---|---|
| g | The geometry object. |

You can call the `ST_Area` function to calculate the area of the specified polygon object.

```
double ST_Area(geometry g);
```

**Parameters**

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If you specify a geometry object, this function returns the 2D Cartesian area of the geometry object in the unit that is specified by the spatial reference system of the geometry object. Lindorm GanosBase SQL uses the spatial reference system with the SRID 4326. In this system, distances are measured in degrees. If the points of the specified polygon object enclose multiple closed figures, this function calculates the difference between the areas of the closed figures enclosed by the points clockwise and counterclockwise, and returns the absolute value of the difference. If you do not specify a polygon object, the value 0 is returned. Calculate the area of a polygon object.

```
SELECT ST_Area(ST_GeomFromText('POLYGON((2 2, 2 8, 8 8, 8 2, 2 2))')) AS area;
```

The following result is returned:

```
+------+
| area |
+------+
| 36   |
+------+
```

Calculate the area of a non-polygon object.

```
SELECT ST_Area(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS area;
```

The following result is returned:

```
+------+
| area |
+------+
| 0    |
+------+
```

**ST_Distance**

You can call the `ST_Distance` function to calculate the 2D Euclidean distance between two specified geometry objects. The returned distance is measured in degrees.

```
double ST_Distance(geometry geomA, geometry geomB);
```

**Parameters**

| Parameter | Description |
|---|---|
| geomA | The first geometry object. |
| geomB | The second geometry object. |

| Parameter | Description |
|---|---|
| geomA | The first geometry object. |
| geomB | The second geometry object. |

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If one of the geometry objects is empty, the value 0 is returned. Example 1:

```
SELECT ST_Distance(ST_GeomFromText('POINT(-72.1235 42.3521)'),ST_GeomFromText('LINESTRING(-72.126 0 42.45, -72.123 42.1546)')) AS d;
```

The following result is returned:

```
+-----------------------+
|           d           |
+-----------------------+
| 0.0015056772638228177 |
+-----------------------+
```

Example 2:

```
SELECT ST_Distance(ST_GeomFromText('POINT(-72.1235 42.3521)'),ST_GeomFromText('LINESTRING EMPTY') ) AS d;
```

The following result is returned:

```
+---+
| d |
+---+
| 0 |
+---+
```

**ST_DistanceSphere**

You can call the `ST_DistanceSphere` function to calculate the minimum spherical distance between two specified geometry objects. The returned distance is measured in meters.

```
double ST_DistanceSphere(geometry geomA, geometry geomB);
```

**Parameters**

| Parameter | Description |
|---|---|
| g | The geometry object. |

**Note**

You can specify a geometry object of the following types: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection. If one of the geometry objects is empty, the value 0 is returned. If one of the specified geometry objects is a polygon or LineString object, the result may have an error of centimeters. Example 1:

```
SELECT ST_DistanceSphere(ST_GeomFromText('POINT(-72.1235 42.3521)'),ST_GeomFromText('LINESTRING(- 72.1260 42.45, -72.123 42.1546)')) AS d;
```

The following result is returned:

```
+--------------------+
|         d          |
+--------------------+
| 124.53287523764577 |
+--------------------+
```

Example 2:

```
SELECT ST_DistanceSphere(ST_GeomFromText('POINT(-72.1235 42.3521)'),ST_GeomFromText('LINESTRING E MPTY')) AS d;
```

The following result is returned:

```
+---+
| d |
+---+
| 0 |
+---+
```

**ST_Length**

You can call the `ST_Length` function to calculate the 2D length of the specified geometry object. The returned length is measured in degrees.

```
double ST_Length(geometry g);
```

**Parameters**

**Note**

If the specified geometry object is a LineString object, the 2D length of the object in a Cartesian coordinate system is returned. If the specified geometry object is a polygon object, the value 0 is returned. Example 1:

```
SELECT ST_Length(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS length;
```

| Parameter | Description |
|---|---|
| g | The geometry object. |

The following result is returned:

```
+--------+
| length |
+--------+
| 5      |
+--------+
```

Example 2:

```
SELECT ST_Length(ST_GeomFromText('POLYGON((2 2, 2 8, 8 8, 8 2, 2 2))')) AS length;
```

The following result is returned:

```
+--------+
| length |
+--------+
| 0      |
+--------+
```

**ST_LengthSphere**

You can call the `ST_LengthSphere` functions to calculate the spherical length of the specified geometry object. The returned length is measured in meters.

```
double ST_LengthSphere(geometry g);
```

**Parameters**

**Note**

If the specified geometry object is a LineString object, the spherical length of the object is returned. If the specified geometry object is a polygon object, the value 0 is returned. Example 1:

```
SELECT ST_LengthSphere(ST_GeomFromText('LINESTRING(1 3,5 6)')) AS length;
```

The following result is returned:

```
+------------------+
|      length      |
+------------------+
| 554137.283806292 |
+------------------+
```

Example 2:

```
SELECT ST_LengthSphere(ST_GeomFromText('POLYGON((2 2, 2 8, 8 8, 8 2, 2 2))')) AS length;
```

The following result is returned:

| Parameter | Description |
|---|---|
| g | The geometry object. |

```
+--------+
| length |
+--------+
| 0      |
+--------+
```

**ST_IsValid**

The ST_IsValid function checks whether a geometry object is valid.

**Note**

Invalid geometry objects include self-intersecting polygons, MultiPolygon objects that include overlapped polygons, and other objects that do not comply with their definitions.

```
boolean ST_IsValid(geometry g);
```

**Parameters**

Check whether the geometry object whose ID is 110000 is valid.

```
SELECT ST_IsValid(geom) FROM mapdata WHERE id=110000;
```

The following result is returned:

```
+--------------------+
| "ST_IsValid"(geom) |
+--------------------+
| true               |
+--------------------+
```

The returned result is `true` , which indicates that the geometry object whose ID is 110000 is valid. If `false` is returned, the geometry object whose ID is 110000 is invalid.

###### Aggregate functions

This topic describes the aggregate functions that are supported by Lindorm GanosBase.

**ST_Length_Rows**

This function sorts out-of-order points by time, aggregates the points into a trajectory, and then returns the spherical length of the trajectory in meters. You can use the `ST_Length_Rows` function together with the `GROUP BY` clause to obtain the spherical length of the trajectory that is aggregated by the points in the specified column.

**Important**

You must use the primary keys to make sure that the points are aggregated in the correct order. Otherwise, the returned length may not be as expected. For example, you can use the vehicle ID column and the timestamp column as primary keys in Internet of Vehicles (IoV) scenarios to make sure that points are aggregated in the correct order.

| Parameter | Description |
|---|---|
| point column | The geometry object. Specify points for this parameter. |

| Parameter | Description |
|---|---|

```
double ST_Length_Rows(point column);
```

**Parameters**

Calculate the spherical length of the trajectory aggregated by points whose ID is 1 in the p column.

```
SELECT ST_LENGTH_ROWS(p) FROM tdrive WHERE id=1;
```

Returned result:

```
+-------------------------+
|    ST_LENGTH_ROWS(p)    |
+-------------------------+
| 441415.1379062134844505 |
+-------------------------+
```

Calculate the spherical length of the trajectories aggregated by the points grouped by their IDs.

```
SELECT id,ST_LENGTH_ROWS(p) FROM tdrive WHERE id<4 GROUP BY id;
```

Returned result:

```
+----+--------------------------+
| id |    ST_LENGTH_ROWS(p)     |
+----+--------------------------+
| 1  | 441415.1379062134844505  |
| 2  | 1672105.5085354075296573 |
| 3  | 1336898.1989478711426478 |
+----+--------------------------+
```

**ST_TrajectoryProfile**

This function sorts out-of-order points by time, aggregates the points into a trajectory, divides the trajectory into segments based on the specified temporal threshold, and then returns the coordinates and time of the start and end points of each segment. The `ST_TrajectoryProfile` function must be used together with the `GROUP BY` clause to calculate the coordinates and time of the start and end points of each trajectory segment that is aggregated by a group of points. The `ST_TrajectoryProfile` function is usually used together with functions for spatial relationship, such as ST_DWithinSphere. In this case, you can calculate the coordinates and time of the point that first enters a specified area and the point that last leaves a specified area in a trajectory segment.

```
String ST_TrajectoryProfile(String geomColumnName, String timeColumnName,long thresh); String ST_TrajectoryProfile(String xColumnName, String yColumnName, String timeColumnName,long thre sh);
```

**Parameters**

| geomColumnName | The geometry object. Specify points for this parameter. Note If the data of points is stored as point objects in the table, specify this parameter when you use the function. |
|---|---|
| xColumnName | The longitude column. Specify DOUBLE values for this parameter. This parameter must be specified together with the yColumnName parameter. Note If the data of points is stored as longitudes and latitudes in the table, specify this parameter when you use the function. |
| yColumnName | The latitude column. Specify DOUBLE values for this parameter. This parameter must be specified together with the xColumnName parameter. Note If the data of points is stored as longitudes and latitudes in the table, specify this parameter when you use the function. |
| timeColumnName | The time column. Points in the table are constructed in the increasing order of this column. |
| thresh | The time threshold based on which the trajectory is divided into segments. This parameter is optional. Unit: milliseconds. After points are sorted based on the time column, if the time interval between two adjacent points is equal to or smaller than the threshold, the two points are considered in the same trajectory segment. If the time interval between two adjacent points is larger than the threshold, the two points are considered in different trajectory segments. Default value: 10000. |

**Returned value**

This function returns a JSON string in the following format: {"Trajectory segment number":"{\"endY\":Latitude of the end point,\"endX\":Longitude of the endpoint,\"startY\":Latitude of the start point,\"startTime\":Time of the start point,\"startX\":Longitude of the start point,\"endTime\":Time of the end point}"}. In a table named test, aggregate the points collected by multiple devices within the specified time and spatial range into trajectory segments. In each trajectory segment, query the coordinates and time of the point that first enters the specified area and the point that last leaves the specified area.

```
SELECT device_code, st_trajectoryprofile(lon, lat, collect_time, 30000) FROM test WHERE st_dwithinsphere(st_geomfromtext('POINT (120.20495 30.187485810)'), lon, lat, 1000.0) and collect_t ime >= 1660673959000 and collect_time <= 1660750359000 group by device_code;
```

**Note**

If a secondary index is used in the query, all columns that are used in the query, including the aggregation key, filter condition columns, and function parameter columns, must be added to the index as redundant columns. This way, the query does not need to scan the data in the base table. For example, in the preceding statement, the device_code, lon, lat, and collect_time columns must be added to the secondary index as redundant columns.

| Statement | Description | Reference |
|---|---|---|
| SHOW | Queries schema or table information. | SHOW |
| USE | Uses a schema. | USE |
| DROP SCHEMA | Deletes a schema. | DROP DATABASE |
| CREATE TABLE | Creates a Lindorm wide table. | CREATE TABLE |
| ALTER TABLE | Adds one or more columns to a specified table or modifies table attributes. | ALTER TABLE |
| DROP TABLE | Deletes a Lindorm wide table. | DROP TABLE |
| CREATE INDEX | Creates a secondary index for a specified table. | CREATE INDEX |
| ALTER INDEX | Modifies the secondary index attributes for a specified table. | ALTER INDEX |
| SHOW INDEX | Queries a secondary index for a specified table. | SHOW INDEX |

Returned result:

```
+--------------+------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------+
| device_code  |
ST_TRAJECTORYPROFILE(lon, lat)
```

|

```
+--------------+------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------+
| 136229080991 | {"0":"
{\"endY\":30.187505,\"endX\":120.204922,\"startY\":30.187542,\"startTime\":1660722531000,\"startX\":1 205022,\"endTime\":1660723161000}","1":" {\"endY\":30.187467,\"endX\":120.204883,\"startY\":30.187508,\"startTime\":1660723192000,\"startX\":1 20493,\"endTime\":1660724452000}"}| +--------------+------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------+
```

#### DDL

##### Overview

This topic describes the data definition language (DDL) statements in LindormTable SQL. LindormTable is a wide table engine provided by Lindorm.

| DROP INDEX | Deletes a secondary index for a specified table. | DROP INDEX |
|---|---|---|
| CREATE SEARCH INDEX | Creates a search index for a specified table. | CREATE SEARCH INDEX |
| DROP SEARCH INDEX | Deletes a search index for a specified table. | DROP SEARCH INDEX |
| ALTER SEARCH INDEX | Modifies a search index for a specified table. You can add or delete index key columns. You can also modify search index attributes. | ALTER SEARCH INDEX |
| SHOW SEARCH INDEX | Queries a search index for a specified table. | SHOW SEARCH INDEX |

##### DESCRIBE/SHOW/USE

You can execute DESCRIBE or SHOW statements to query information about databases (also known as schemas), tables, or indexes. You can execute the USE statement to use a specified schema. The following statement can be executed to show all databases.

```
show schemas;
```

In LindormTable V2.2.16 or later, the following statement is used by default to show all databases:

```
show databases;
```

The following statement can be executed to show all tables in a specified schema. If no schema is specified, all tables in the default schema are returned.

```
show tables;
```

In LindormTable V2.2.16 or later, the following statement can be executed to show the details of a specified table. The details include the data types of columns in the table and other column information.

```
show columns in/from <Table name>;
```

The following statement can be executed to show the index idx1 that is created for the test table.

```
show index from test;
```

The following statement can be executed to show the details of the test table. The details includes the data types of columns in the table and other column information.

```
describe test;
```

The following statement can be executed to use a specific schema.

```
use schema;
```

##### DROP DATABASE

You can execute the DROP DATABASE statement to delete a Lindorm database.

| Option | Data type | Description |
|---|---|---|
| COMPRESSION | String | The algorithm used to compress the data in the table. Valid values: SNAPPY ZSTD LZ4 Note In LindormTable versions earlier than 2.3.4, no compression algorithm is specified by default when you create a table. In LindormTable 2.3.4 and later versions, the ZSTD algorithm is specified by default to compress a table when you create the table. |
| TTL | Int | The Time-to-Live (TTL) value of data in the table. Unit: seconds. By default, if you do not specify this option, data in the table does not expire. |
| MUTABILITY | String | An option related to indexes. This option specifies the mutability of the base table. Valid values: IMMUTABLE IMMUTABLE ROWS _ MUTABLE LATEST _ MUTABLE ALL _ Note For more information, see Secondary indexes. |
| CONSISTENCY | String | The consistency level of the table. Default value: eventual. Valid values: eventual: Data in the base table and index table become consistent after a point in time. strong: The values in the base table and index table are consistent at all points in time. |
| NUMREGIONS | Int | The number of data regions in the table that you want to create. |

```
drop_database_statement ::= DROP DATABASE [ IF EXISTS ] database_name
```

Note: By default, in Lindorm versions earlier than 2.2.16, you need to specify the schema name of a database when you use this statement to delete the database. This statement is equivalent to drop schema [if exists] schema_name.

```
drop schema if exists test; drop database if exists test;
```

##### CREATE TABLE

You can execute the CREATE TABLE statement to create a Lindorm wide table.

**The following table describes the table options.**

| STARTKEY and ENDKEY | Same data type as that of the first column in the primary key specified by PRIMARY KEY | The start key and end key of each region. Note The STARTKEY and ENDKEY options must be specified together with the NUMREGIONS option. If the NUMREGIONS option is not specified, the STARTKEY and ENDKEY options do not take effect. If you specify string values for the STARTKEY and ENDKEY options, the strings are implicitly converted to values with the same data types as the first column of the primary key. Only the following data types are supported for the STARTKEY and ENDKEY options: SMALLINT INTEGER BIGINT CHAR VARCHAR FLOAT DOUBLE |
|---|---|---|
| DYNAMIC COLUMNS _ | String | Specifies whether to enable dynamic columns. Valid values: True: Enable dynamic columns for the table. False: Disable dynamic columns for the table. This is the default value. Note Dynamic columns support only the VARBINARY data type. For more information about dynamic columns, see Dynamic columns. |

**Note**

In Lindorm 2.2.16 and later versions, you can use multiple keywords to configure table attributes. In Lindorm versions earlier than 2.2.16, you do not need to add the `WITH` keyword when you configure table attributes. In addition, you must enclose the keys of table attributes in single quotation marks (') when you configure table attributes. If the value of a table attribute is a string, you must also enclose the value in single quotation marks ('). Lindorm 2.2.16 and later versions support all syntax rules in earlier versions. In Lindorm 2.2.16 and later versions, you can add the `WITH` keyword before table attributes. You do not need to use single quotation marks (') to enclose the keys of table attributes. However, you must use single quotation marks (') to enclose the values of table attributes. The sample statements described in the following section can be directly executed. You can create a Lindorm wide table by using one of the following methods: Method 1

```
  p1 integer, p2 binary(3), c1 varchar, c2 decimal(22, 2),
  PRIMARY KEY(p1, p2 desc));
```

Method 2

```
  p1 integer, p2 binary(3), c1 varchar, c2 decimal(22, 2),
  constraint pk PRIMARY KEY(p1, p2 desc));
```

You can execute the following statement to create a wide table and specify the compression algorithm and data TTL of the table:

```
  p1 integer, p2 integer, c1 varchar, c2 bigint,
  constraint pk PRIMARY KEY(p1 desc)) WITH (COMPRESSION='ZSTD', TTL='2592000');
```

You can execute the following statement to create a wide table and enable dynamic columns for the table:

```
  p1 integer, p2 integer, c1 varchar, c2 bigint, PRIMARY KEY(p1))
  WITH (DYNAMIC_COLUMNS='TRUE');
```

You can execute the following statement to create a wide table with five regions whose start key is 1000 and end key is 9000:

```
  p1 int, c1 int, c2 varchar, c3 varchar primary key(p1))
  WITH (NUMREGIONS='5', STARTKEY='1000', ENDKEY='9000');
```

##### CREATE TABLE LIKE

You can sue the CREATE TABLE LIKE syntax to replica the schema of an existing table and create a table based on the schema. In the following examples, the original table is created by executing the following statement:Testable

```
  p1 INT NOT NULL,
  p2 INT NOT NULL,
  c1 VARCHAR,
  c2 BIGINT,
  PRIMARY KEY(p1, p2)
) WITH (SPLITKEYS = '100000,300000,500000,700000,900000');
```

**Replicate the table schema**

Create a new table named `table2` that has the same schema with the original table named `sensor` .

```
CREATE TABLE table2 LIKE sensor;
```

**Replicate the schema and partition start key of the original table.**

```
CREATE TABLE table2 LIKE sensor WITH (COPY_SPLITKEYS='true');
```

##### ALTER TABLE

This topic describes the statements that are used to add one or more columns to a table, and modify the attributes of a table.

```
alter_table_statement ::= ALTER TABLE table_name alter_table_instruction alter_table_instruction ::= ADD [COLUMN] column_name lql_type ( ',' column_name lql_type )*
                             | SET table_options
                             | COMPACT (idcName)?
```

**Note**

For more information about `table_options` , see the Usage notes section of the CREATE TABLE topic. The major_compact operation is applicable only to LindormTable V2.3.4 and later.

| Predicate | Description |
|---|---|
| ADD | Adds columns to a table. |
| SET | Configures the attributes of a table. For more information about the supported table options, see theT able options section of the CREATE TABLE topic. |
| COMPACT | Forcibly performs the major compact operation on the specified table. _ This predicate is only supported by Lindorm SQL statements. |

**Supported predicates**

You can execute the following statement to add a column named c4 to a table named test:

```
ALTER TABLE test ADD COLUMN c4 VARCHAR;
```

You can execute the following statement to add multiple columns to a table named test:

```
ALTER TABLE test ADD c3 INTEGER, c4 INTEGER, c5 VARCHAR;
```

You can execute the following statement to enable dynamic columns for a table named test. Dynamic columns support only the varbinary data type. For more information about dynamic columns, see Dynamic columns.

```
ALTER TABLE test SET 'DYNAMIC_COLUMNS' = 'true';
```

You can execute the following statement to configure data validity period for a table named test:

```
ALTER TABLE test SET 'TTL' = '2592000';
```

You can execute the following statement to configure the algorithm used to compress data in a table named test:

```
ALTER TABLE test SET 'COMPRESSION' = 'ZSTD';
```

You can execute the following statement to cancel the algorithm used to compress data in a table named test:

```
ALTER TABLE test SET 'COMPRESSION' = '';
```

You can execute the following statement to configure the storage period after which hot data is transferred to the cold data storage in a table named test: For more information about hot and cold data separation, see Overview.

```
ALTER TABLE test SET 'CHS' = '86400', 'CHS_L2' = 'storagetype=COLD';
```

You can execute the following statement to cancel the storage period after which hot data is transferred to the cold data storage in a table named test:

```
ALTER TABLE test SET 'CHS' = '', 'CHS_L2' = '';
```

You can execute the following statement to perform the major_compact operation on a table named test:

```
ALTER TABLE test COMPACT;
```

If your database is deployed in two zones, you can perform the major_compact operation on the data in specified data centers. You can execute the following statement to perform the major_compact operation on a table named test in idc2:

```
ALTER TABLE test COMPACT 'idc2';
```

**Note**

By default, if you do not specify a data center in the statement, the major_compact operation is performed on the data in idc1. You can execute the following statement to perform the major_compact operation on a table named test in both idc1 and idc2:

```
ALTER TABLE test COMPACT 'idc1,idc2';
```

##### TRUNCATE TABLE

You can use the TRUNCATE TABLE syntax to clear data from a specified table. In LindormTable 2.2.16 and later versions, execute the OFFLINE TABLE statement, and then execute the TRUNCATE TABLE statement to prevent table data from being cleared by accidental operations.

```
truncate_table_statement ::= TRUNCATE TABLE table_name
```

**Note**

**table_name** specifies the name of the destination table.

```
TRUNCATE TABLE dt; TRUNCATE TABLE my_schema.dt;
```

##### DROP TABLE

You can execute the DROP TABLE statement to delete a table. In LindormTable 2.2.16 and later versions, you must execute the OFFLINE TABLE statement before you can execute the DROP TABLE statement. This prevents users from accidentally dropping a table.

```
drop_table_statement ::= DROP TABLE [ IF EXISTS ] table_name use my_schema; DROP TABLE dt; DROP TABLE IF EXISTS dt; DROP TABLE my_schema.dt;
```

##### CREATE INDEX

You can execute the CREATE INDEX statement to create a secondary index. Lindorm provides the primary key indexing feature. You can create a primary key index for a table to sort rows based on the primary key values. Lindorm allows you to use the SELECT statement to perform efficient queries on the data of each row based on the primary key index. If you want to query a table based on columns other than the primary key, you can use secondary indexes provided by Lindorm.

| Parameter | Data type | Description |
|---|---|---|
| COMPRESSION | String | The compression algorithm that you want to use for the index table. Valid values: SNAPPY ZSTD LZ4 |
| INDEX COVERED TY _ _ PE | String | The columns of the base table that you want to include in the index table for redundant storage. Valid values: COVERED ALL COLUMNS IN SCHEMA: specifies to include all _ _ _ _ columns of the base table. COVERED DYNAMIC COLUMNS: specifies to include dynamic _ _ columns of the base table. If this option is not available, you can use INCLUDE to include columns. |
| STARTKEY | String | The start key of the index table. |
| ENDKEY | String | The end key of the index table. |
| NUMREGIONS | String | The estimated number of partitions of the index table. |

```
create_index_statement ::= CREATE INDEX [ index_name ]
                                ON table_name '(' index_identifier ')'
                              [INCLUDE include_identifier]
                              [ASYNC]
                                 [ index_options ]
index_identifier ::= '('column_name1 [desc],...,column_namen [desc]')' include_identifier ::= '('column_name1,...,column_namen ')'
```

**Index options**

**Note**

An index table can contain columns of the base table for redundant storage. This eliminates the need for scanning data in the corresponding columns from the base table and accelerates your queries. If you want to include only a few columns of the base table in the index table, you can use INCLUDE in your statement. For example, when you use INCLUDE (c1, c2), columns c1 and c2 are included in the index table. By default, indexes are created in a synchronous manner. If you want to use the ASYNC keyword to create an index in an asynchronous manner, you must execute the BUILD INDEX statement. A maximum of five index tables can be created. If you create an excessive number of index tables, the storage costs and response time for write requests are increased.

| Parameter | Description |
|---|---|
| index name _ | The name of the index table. |
| table name _ | The name of the wide table. |

```
// Create an index in an asynchronous manner. After the following statement is executed, the system returns the result without creating indexes on historical data. If you want to create an index on h istorical data, execute the BUILD INDEX statement. create index idx1 on test(c4 desc) include(c5,c6) async 'COMPRESSION'='ZSTD'; // Create an index in a synchronous manner. After the following statement is executed, the result c an be returned only after an index is created for historical data. create index idx1 on test(c4 desc) include(c5,c6) 'COMPRESSION'='ZSTD'; // Create an index that contains all columns of the base table. 'INDEX_COVERED_TYPE'='COVERED_ALL_COLUMNS_IN_SCHEMA'; // Create an index that contains dynamic columns of the base table. create index idx1 on test(c4 desc) 'INDEX_COVERED_TYPE'='COVERED_DYNAMIC_COLUMNS'; // If you want to pre-split a table into partitions, configure the STARTKEY option, ENDKEY option, and NUMREGIONS option. // Create an index without specifying the STARTKEY and ENDKEY options, and pre-split the entire tab le into 32 partitions. create index idx1 on test(c4 desc) include(c5,c6) 'NUMREGIONS' ='32'; // Create an index with the STARTKEY and ENDKEY options specified, and pre-split data ranging from 11111111 to 9999999 into 32 partitions. create index idx1 on test(c4 desc) include(c5,c6) 'NUMREGIONS' ='32','STARTKEY'='11111111', 'ENDKEY' = '9999999'";
```

##### ALTER INDEX

You can execute the ALTER INDEX statement to change the state of an index.

```
alter_index_statement ::= ALTER INDEX [ index_name ]
                                ON table_name index_state
```

If you want to create a secondary index on a database that contains data after an index is created for the database, you can use the `BUILD INDEX` statement. For more information, see BUILD INDEX.

**Parameters**

The following table describes the parameters that you can configure when you execute the ALTER INDEX statement.

| index state _ | The state of the index. If the version of LindormTable that you use is 2.2.16 or later, the following index states are supported: DISABLED: The index is disabled. Before you enable an index in the DISABLED state, you must first build the index for historical data and then execute the BUILD INDEX statement. BUILDING: The index is being built for historical data. After the index is built, the state of the index becomes ACTIVE. ACTIVE: The index is active. Note If the version of LindormTable that you use is earlier than 2.2.16, the following index states are supported: DISABLE: The index is disabled. Before you enable an index in the DISABLED state, you must rebuild the index for historical data. BUILDING: The index is being rebuilt for historical data. After the index is rebuilt, the state of the index becomes USABLE. UNUSABLE: The index cannot be used. Data is synchronized from the base table to the index table when the index is in the UNUSABLE state. Therefore, if you want to enable an index in the UNUSABLE state, you do not need to rebuild the index for historical data. USABLE: The index is enabled. |
|---|---|

If the version of LindormTable that you use is 2.2.16 or later, you can execute the following statements to change the state of an index:

```
ALTER INDEX idx1 ON test DISABLED; ALTER INDEX idx1 ON test ACTIVE; ALTER INDEX idx1 ON test BUILDING;
```

##### BUILD INDEX

In LindormTable 2.2.16 and later versions, you can execute the `BUILD INDEX` statement to individually build a secondary index. The following sample code provides an example on how to use the `BUILD INDEX` statement to create a secondary index on historical data after an index is built in LindormTable 2.2.16 and later versions. By default, the index is built in an asynchronous manner.

```
build_index_statement ::= BUILD INDEX [ index_name ]
                                ON table_name
BUILD INDEX idx ON test;
```

##### SHOW INDEX

You can execute the SHOW INDEX statement to show an index schema.

```
showindex_statement ::= show index from table_name;
```

```
show index from test;
```

##### DROP INDEX

You can execute the DROP INDEX statement to delete an index table. Before you delete an index table, make sure that the ALTER INDEX statement is executed to disable the index table.

```
dropindex_statement ::= drop index [if exists] index_name on table_name; drop index idx1 on test;
```

##### OFFLINE TABLE

In LindormTable 2.2.16 and later versions, you can execute the `OFFLINE TABLE` statement to disable LindormTable. Before you delete a wide table, make sure that the `OFFLINE TABLE` statement is executed to disable the wide table.

```
OFFLINE TABLE test;
```

##### ONLINE TABLE

In LindormTable 2.2.16 and later versions, you can execute the `ONLINE TABLE` statement to enable LindormTable.

```
ONLINE TABLE table_name; ONLINE TABLE test;
```

##### CREATE SEARCH INDEX

You can execute the `CREATE SEARCH INDEX` statement to create a search index in Lindorm.

**Usage notes**

Search indexes are suitable for multidimensional queries. You can use a search index to query data that is sorted based on one or more specified columns, or is displayed on the specified number of pages. Only one search index can be generated for each table. You can add index key columns to the existing search index. If the columns of historical data are updated, create an index for full data. You can use an asterisk (*) to create a search index on all columns.

| Paramete r | Data type | Description |
|---|---|---|
| indexed | String | Specifies whether to create a search index. Valid values: true: creates a search index. This is the default value. false: does not create a search index. |
| rowStore d | String | Specifies whether to store raw data. Valid values: true: stores raw data. false: does not store raw data. This is the default value. |
| columnSt ored | String | Specifies whether to use the columnar structure to accelerate data sorting and analysis. Valid values: true: uses the columnar structure. This is the default value. false: does not use the columnar structure. |
| type | String | The data type. When analyzers are used, set type to text for the related fields. In other scenarios, set the value of this option to the data type in your wide table by default. Note This option must be used together with analyzer. |

The following data types are supported for index key columns: TINYINT, SMALLINT, INTEGER, INT, BIGINT, LONG, FLOAT, DOUBLE, VARCHAR, BINARY, VARBINARY, and BOOLEAN.

```
        ON table_name '(' index_identifier ')'
        [ASYNC]
        [ WITH '(' index_options ')' ]
index_identifier: (column_name'(' column_options ')' ',' ... column_name'(' column_options ')')* | "*" column_options: option_name '=' option_value (',' option_name '='option_value) index_options: option_name '=' option_value (',' option_name '='option_value)
```

**Parameters**

The following table describes the **column options**.

| analyzer | String | The analyzer that you want to use. Valid values: standard english ik whitespace comma Note This option must be used together with type. If the data type of a column in your wide table is a numeric data type such as INT, set this option to standard. |
|---|---|---|

| Paramete r | Data type | Description |
|---|---|---|
| indexStat e | String | The state of the search index. Valid values: BUILDING: This is the default value. ACTIVE: specifies to enable the search index. If no historical data is available, set this option to ACTIVE. |
| numShar ds | String | The number of shards. The default value is equal to twice the number of search nodes. |
| RANGE TI _ ME PARTI _ TION STA _ RT | String | The number of days before you create the index. The first partition is created based on the point in time n days before the point in time when you create the index. The number of days is the value of n. This option can be specified in scenarios in which your table has historical data. If the timestamp of a row of historical data is earlier than the point in time based on which the first partition is created, an error message is returned. Note This option must be specified when you create a search index by using the time range partitioning policy. |
| RANGE TI _ ME PARTI _ TION INT _ ERVAL | String | The interval at which new partitions are created. For example, RANGE TIME PARTITION INTERVAL='7' specifies that new partitions are created at an _ _ _ interval of seven days. Note This option must be specified when you create a search index by using the time range partitioning policy. |

The following table describes the **index options**.

| RANGE TI _ ME PARTI _ TION TTL _ | String | The number of days for which partitions are retained. For example, RANGE TIME PARTITION TTL='180' specifies that data partitions are retained for 180 _ _ _ days. A data partition is automatically deleted after it expires. If you do not specify this option, partitions are not automatically deleted. Note This option is available only when you create a search index by using the time range partitioning policy. |
|---|---|---|
| RANGE TI _ ME PARTI _ TION MA _ X OVERL _ AP | String | If the timestamp of the data that you write indicates a time in the future, this option specifies the maximum time period between the point in time when data is written and the point in time when you create the index. Unit: days. If you do not specify this option, the timestamp of the data that you want to write is not limited. Note This option is available only when you create a search index by using the time range partitioning policy. |
| RANGE TI _ ME PARTI _ TION FIEL _ D TIMEUN _ IT | String | The unit of values in the partition key column. Default value: ms. The value ms means milliseconds. If you set the value of this parameter to s, each value in the partition key column is 10 digits in length. The value s means seconds. If you set the value of this parameter to ms, each value in the partition key column is 13 digits in length. Note This option is available only when you create a partition index. |

1. Create a schema and a table. If the schema and table already exist, skip this step.

```
CREATE SCHEMA test; USE test; CREATE TABLE IF NOT EXISTS tbn (p1 varchar, p2 varchar, col1 bigint, col2 varchar, col3 varchar, col4 bigint, constraint primary key (p1, p2 desc));
```

2. Create a search index based on your business scenarios.
Specify index key columns when you create a search index. By default, LindormTable creates the search index on historical data in a synchronous manner. This process requires a long period of time.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2, col3);
```

Create a search index in an asynchronous manner. If you do not need to create a search index in a synchronous manner, append `ASYNC` to the statement. For more information about how to create a search index in a synchronous manner for subsequent use, see Step 3.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2, col3) ASYNC;
```

Create search indexes for all columns in the table without configuring column options.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn("*");
```

Create search indexes on all columns and specify the options of each column.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn("*",col1(type=text,analyzer=ik,indexed=true));
```

Configure the shared column options for all columns. The options specified in the statement are applicable to all index columns. In this example, if the index includes the col1, col2, and col3 columns, the following options are applicable to all three columns: type=text, analyzer=ik, indexed=true.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn("*"(type=text,analyzer=ik,indexed=true));
```

Specify index key columns and do not configure column options when you create a search index.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2, col3);
```

Specify index key columns and the search index state, and configure specific column options when you create a search index.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2(type=text,analyzer=ik), col3) WITH (ind exState=ACTIVE, numShards=4);
```

**Note**

When you configure `column_options` , the type option and analyzer option must be specified together. Create a search index by using the time range partitioning policy and specify index columns. The following statement specifies that the first partition is created based on 30 days before the point in time when you create the index, sets the interval at which a new partition is created to 7 days, sets the retention period of your data in a partition to 90 days, and performs time range partitioning by the col4 column.

```
CREATE SEARCH INDEX idx ON tbn (col1, col2, col3, col4) partition by range time(col4) partitions 16 with (indexState=ACTIVE, RANGE_TIME_PARTITION_START='30', RANGE_TIME_PARTITION_INTERVAL='7', RA NGE_TIME_PARTITION_TTL='90', RANGE_TIME_PARTITION_MAX_OVERLAP='90');
```

3. If you already use `ASYNC` to create a search index in an asynchronous manner and you want to
retrieve historical data, execute the following statement. By default, the search index is created in a synchronous manner. You can perform the following operations to view the progress of the REBUILD operation: Log on to the Lindorm Tunnel Service (LTS) web UI. In the left-side navigation pane, choose
**Lindorm Search > Full Data replication to Search** .

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn REBUILD;
```

##### DROP SEARCH INDEX

You can execute the `DROP SEARCH INDEX` statement to delete a search index in Lindorm.

**Prerequisites**

Before deleting a search index, you need to change the attribute of the search index to `DISABLED` . For more information, see ALTER SEARCH INDEX.

```
DROP SEARCH INDEX [IF EXISTS] index_name ON table_name
```

1. Create a schema and a table. If the schema and table already exist, skip this step.

| Paramete r | Data type | Description |
|---|---|---|
| indexed | String | Specifies whether to create an index. Valid values: true: creates an index. This is the default value. false: does not create an index. |
| rowStore d | String | Specifies whether to store raw data. Valid values: true: stores raw data. false: does not store raw data. This is the default value. |

```
CREATE SCHEMA test; USE test; CREATE TABLE IF NOT EXISTS tbn (p1 varchar, p2 varchar, col1 bigint, col2 varchar, col3 varchar, constraint primary key (p1, p2 desc));
```

2. Create a search index.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2, col3);
```

3. Delete the search index of the table. Before you delete the search index, change the attribute of the
search index to DISABLED.

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn DISABLED; DROP SEARCH INDEX IF EXISTS idx ON tbn;
```

##### ALTER SEARCH INDEX

You can execute the `ALTER SEARCH INDEX` statement to add index key columns to a search index, delete index key columns from a search index, or modify the state of a search index in Lindorm. After you specify the attribute of an index key column, the attribute cannot be modified. The name of the index key column you want to add must be different from the names of index key columns that are deleted.

**Usage notes**

If you add or delete one or more index key columns, you must perform the `REBUILD` operation. The following data types are supported for index key columns: TINYINT, SMALLINT, INTEGER, INT, BIGINT, LONG, FLOAT, DOUBLE, VARCHAR, BINARY, VARBINARY, and BOOLEAN.

**Add one or more index key columns**

```
ALTER SEARCH INDEX [IF EXISTS] index_name ON table_name ADD COLUMNS '(' index_identifier ')' index_identifier: (column_name['(' column_options ')'] ',' ... column_name['(' column_options ')'])* column_options: option_name '=' option_value (',' option_name '=' option_value)
```

**Parameters**

The following table describes the **column options**.

| columnSt ored | String | Specifies whether to use the columnar structure to accelerate data sorting and analysis. Valid values: true: uses the columnar structure. This is the default value. false: does not use the columnar structure. |
|---|---|---|
| type | String | The data type. When analyzers are used, set type to text for the related fields. In other scenarios, set the value of this option to the data type in your wide table by default. Note This option must be used together with analyzer. |
| analyzer | String | The analyzer that you want to use. You must specify an analyzer in text segmentation scenarios. Valid values: standard english ik whitespace comma Note This option must be used together with type. If the data type of a column in your wide table is a numeric data type such as INT, set this option to standard. |

1. Create a schema and a table. If the schema and table already exist, skip this step.

```
CREATE SCHEMA test; USE test; CREATE TABLE IF NOT EXISTS tbn (p1 varchar, p2 varchar, col1 bigint, col2 varchar, col3 varchar, constraint primary key (p1, p2 desc));
```

2. Add one or more index key columns.
Do not configure column options when you add index key columns.

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn ADD COLUMNS(col1,col2,col3);
```

Configure column options when you add index key columns.

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn ADD COLUMNS(col1,col2,col3(type=text,analyzer=ik));
```

3. If an index on historical data is required, you must perform the `REBUILD` operation. By default, the
system creates the index in a synchronous manner. After you execute the statement, you can perform the following operations to view the progress of the REBUILD operation: Log on to the Lindorm Tunnel Service (LTS) web UI. In the left-side navigation pane, choose **Lindorm Search > Full Data**
**replication to Search**.

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn REBUILD; ALTER SEARCH INDEX [IF EXISTS] index_name ON table_name DROP COLUMNS '(' index_identifier ')' index_identifier: (column_name ',' ... column_name)*
```

Delete multiple index key columns without configuring column options.

| Paramete r | Data type | Description |
|---|---|---|
| DISABLED | String | Disables your search index. If you want to enable the index, perform the REBUILD operation. |
| REBUILD | String | Re-creates a search index on historical data. After the search index is created, the state of the search index automatically changes to USABLE. |
| UNUSABL E | String | Disables your search index. If you want to enable the index, you do not need to perform the REBUILD operation. This is because data is synchronized from the base table to the index table when the index is in the UNUSABLE state. |
| USABLE | String | Enables your search index. |

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn DROP COLUMNS(col2,col3);
```

After these columns are deleted, you must perform the `REBUILD` operation to re-create an index. By default, the system creates the index in a synchronous manner. After you execute the statement, you can perform the following operations to view the progress of the REBUILD operation: Log on to the LTS web UI. In the left-side navigation pane, choose **Lindorm Search > Full Data replication to Search** .

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn REBUILD;
```

**Modify the state of a search index**

```
ALTER SEARCH INDEX [IF EXISTS] index_name ON table_name index_state_definition
                                 [ASYNC]
index_state_definition: REBUILD | DISABLED | UNUSABLE | USABLE
```

**Parameters**

The following table describes the options for **index_state_definition**. Disable a specified search index.

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn DISABLED;
```

Re-create a search index on historical data. By default, the search index is created in a synchronous manner. If you want to create the search index in an asynchronous manner, use `ASYNC` in your statement. After you execute the statement, you can perform the following operations to view the progress of the REBUILD operation: Log on to the LTS web UI. In the left-side navigation pane, choose
**Lindorm Search > Full Data replication to Search** .

```
ALTER SEARCH INDEX IF EXISTS idx ON tbn REBUILD; ALTER SEARCH INDEX IF EXISTS idx ON tbn REBUILD ASYNC;
```

##### SHOW SEARCH INDEX

You can execute the `SHOW SEARCH INDEX` statement to query a search index of a specified table in Lindorm.

| force index(index name) _ |  |  |
|---|---|---|
| If | LIMIT | is followed by on |

1. Create a schema and a table. If the schema and table already exist, skip this step.

```
CREATE SCHEMA test; USE test; CREATE TABLE IF NOT EXISTS tbn (p1 varchar, p2 varchar, col1 bigint, col2 varchar, col3 varchar, constraint primary key (p1, p2 desc));
```

2. Create a search index.

```
CREATE SEARCH INDEX IF NOT EXISTS idx on tbn(col1, col2, col3);
```

3. Query a search index for a specified table.

```
SHOW SEARCH INDEX FROM tbn;
```

#### DML

##### SELECT

You can execute the SELECT statement to query the data of rows from one or more tables.

**Note**

This topic describes how to execute the SELECT statement to query the data of rows from one or more tables.

```
    FROM table_name
    [force index(index_name)]
    [ WHERE where_clause ]
    [ ORDER BY ordering_clause ]
    [ LIMIT integer ] | [LIMIT integer, integer]
    [`ALLOW FILTERING`]
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] )
                      | term
                      | COUNT '(' '*' ')'
where_clause ::= relation ( AND|OR relation )* relation ::= column_name operator term
                      '(' column_name ( ',' column_name )* ')' operator tuple_literal
operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | IS NOT? NULL ordering_clause ::= column_name [ ASC | DESC ] ( ',' column_name [ ASC | DESC ] )* hint_clause::=/*+hint_items*/ hint_items::=hint_item(','hint_item)* hint_item::=identifier('('hint_option(','hint_option)*')') hint_option::=expression
```

**Parameters**

Take note of the following items when you configure parameters in SELECT statements: that specifies the number of rows to be skipped in the query, and the second number specifies the number of rows to be returned for the query. You can add `ALLOW FILTERING` to the end of the SQL statement to skip the query check and execute

| WHERE |  | clause. |
|---|---|---|
| the | WHERE |  |

the inefficient query by force. If LindormTable determines that a SELECT query is an inefficient query, LindormTable does not process the query by default and throws an exception to ensure stable performance. For example, a table named dt is stored in your Lindorm database. When you execute the SELECT * FROM dt WHERE nonPK=100; statement, the following error message is returned. For more information about the solution to an inefficient query, see the FAQ section of this topic.

```
DoNotRetryIOException: Detect inefficient query: SELECT * FROM dt WHERE nonPK=100 supportEmptyResult true. This query may be a full table scan and thus may have unpredictable perf ormance.
```

For more information about how to use hints in SELECT statements, see Overview.

```
// Perform simple queries. SELECT * FROM dt; // Select all columns. SELECT c1,c2 FROM dt; // Select specific columns. SELECT * FROM dt LIMIT 10; SELECT * FROM dt WHERE pk = 10; SELECT * FROM dt WHERE pk > 10 LIMIT 5, 20; // Skip 5 rows and obtain up to 20 rows. SELECT * FROM dt WHERE pk > 10 LIMIT 20 OFFSET 5; // LIMIT 20 OFFSET 5 is equivalent to LIMIT 5, 20. SELECT c1 FROM dt WHERE pk > 10; SELECT c1 AS xx FROM dt WHERE pk > 10; // Perform aggregate queries. SELECT count(*) FROM dt; SELECT count(c1) FROM dt; SELECT sum(c2) FROM dt; SELECT sum(c2), AVG(c2),MIN(c2),MAX(c2) FROM dt; // Use conditions such as IS NULL in the WHERE clause. SELECT c1, c2 FROM dt WHERE (c1>1 OR (c2>0 AND c7 is null)) AND c3 <>1.0 AND c6 is not null; // Use aliases. SELECT count(*) AS countRow FROM dt; SELECT c1 AS testC FROM t1 WHERE c1 = '2'; // Use the IN keyword. SELECT * FROM dt WHERE dt in ('a', 'b'); // Force LindormTable to perform an inefficient query. SELECT * FROM dt WHERE nonPK=100 ALLOW FILTERING;
```

**FAQ**

Q: What is an inefficient query? A: If the query conditions specified in a SELECT statement meet all the following conditions, the SELECT query is considered inefficient:

```
clause .
```

One or more conditions that are specified in the `WHERE` clause are not related to the first primary key column or the first index key column. Q: What can I do if my query is identified as an inefficient query? A: You can use one of the following methods to solve this issue: Add `ALLOW FILTERING` to the end of inefficient query statements to skip the query check and execute the statements by force. The following statement provides an example:

```
SELECT * FROM dt WHERE nonPK=100 ALLOW FILTERING;
```

Add one or more conditions related to the primary key of your table to the `WHERE` clause. Redesign the primary key of the table to avoid queries that need to scan large amounts of data. Use secondary indexes that provide high performance. For more information, see the "Secondary indexes" topic in Lindorm User Guide.

##### UPSERT

Updates or inserts data. The UPSERT statement is a combination of the INSERT statement and UPDATE statement. The UPSERT statement updates a row if the specified value already exists and inserts a row if the specified value does not exist. When you execute the UPSERT statement, you must specify the column that is used as the primary key. The UPSERT statement can insert individual rows or multiple rows with timestamps.

```
                      '('columns| _l_ts_')'
                      VALUES '(' values ')'
                      [ ON DUPLICATE KEY update_column = update_value |IGNORE ]?
columns ::= column_name, columns values ::= term, values,'(' values ')' update_column ::= column_name update_value ::= term
```

**Note**

The UPSERT statement can insert multiple rows in a batch. You must specify the columns to which the values are inserted. You can use the Values keyword to determine the number of rows that you want to insert. The UPSERT ON DUPLICATE KEY operation is supported. This operation is similar to the CHECK AND PUT operation. Make sure that the specified values can identify a row. If you specify the column that you want to update and the new value after ON DUPLICATE KEY, and the column exists in the table, an exception is thrown. This is because ON DUPLICATE KEY cannot update values by checking whether the specified column exists. ON DUPLICATE KEY IGNORE is used to skip the duplicate column check and directly insert rows. You can use standard Java Database Connectivity (JDBC) to submit regular SQL statements or prepared statements to Lindorm. You can submit prepared statements by using standard JDBC to perform standard batch insert operations only in Lindorm 2.2.16 and later versions.

```
upsert into dt (p1,p2,c1,c2) values(10, 20, 30, 40); upsert into dt (p1,p2,c2) values(10, 20, 40); -- Insert values to specific columns in a row. upsert into dt (p1,p2,c1) values(10, 20, 30); -- Insert values to other columns in the same row. -- Equivalent to upsert into dt (p1,p2,c2) values(10, 20, 5). ON DUPLICATE KEY IGNORE is specified to skip the duplicate column check. upsert into dt (p1,p2,c2) values(10, 20, 5) on duplicate key ignore; -- Conditional update. Insert values into the c1 = 30 column in the p1=10, p2=20, and c2=5 rows. upsert into dt (p1,p2,c2) values(10, 20, 5) on duplicate key update c1 = 30; -- Insert a row with a timestamp of 111232.
 UPSERT INTO dt (p1,p2,p3,_l_ts_) values('1','2','3',111232);
-- Insert multiple rows in a batch. upsert into dt (p1,p2,c1,c2) values(1,2,3,4), (2,3,4,5), (3,4,5,6); --- UPSERT ON DUPLICATE KEY IGNORE. If the row identified by the values 1, 2, 3, 4, and 5 does not exist, a row is inserted. upsert into dt (p1,p2,p3,c1,c2) values (1,2,3,4,5) on duplicate key ignore; --- UPSERT ON DUPLICATE KEY. If the row identified by the values 1, 2, 3, 4, and 5 does not exist, no row is inserted and an exception is thrown. If the row exists, the value of c2 is updated to 6. upsert into dt (p1,p2,p3,c1,c2) values (1,2,3,4,5) on duplicate key update c2 = 6;
```

##### DELETE

You can execute the DELETE statement to delete only one row of data from a specified table. You can specify filter conditions in the statement. DELETE operations are high-risk operations. To ensure data security, Lindorm imposes limits on the DELETE statement. In a DELETE statement, you must specify a primary key condition to scan only one row of data for the operation.

```
                      WHERE where_clause
```

**Note**

When you use the WHERE clause, you must specify a condition that can be used to identify a unique row of data. In the WHERE clause of the DELETE statement, you must specify a primary key condition to scan only one row of data for the operation. Each DELETE statement can delete only one row of data. After you execute a DELETE statement, Lindorm adds a delete marker to the data that you want to delete, instead of querying the data before the delete operation. Therefore, the delete operation is successful regardless of whether the row that you want to delete exists. You can specify a timestamp in the DELETE statement. In this case, the statement deletes the columns whose timestamps are earlier than or equal to the specified timestamp from the row that you want to delete.

```
delete from dt where p1 = 10 and p2 = 20; -- The following statements are invalid. delete from dt where p1 = 10; -- The dt table contains two primary key columns. More than one row o f data matches the specified condition in the WHERE clause. delete from dt where c1 = 30; -- You must specify a primary key condition to scan only one row of d ata for the operation.
```

| Permission | Description |
|---|---|
| READ | Read permissions on a single table or on all tables in a schema. |
| WRITE | Write permissions on a single table or on all tables in a schema. |
| ADMIN | Administrator permissions on a single table or on all tables in a schema. |
| TRASH | Delete permissions on a single table or on all tables in a schema. |
| SYSTEM | System management permissions on a single table or on all tables in a schema. In most cases, the system management permissions are not granted to users. |
| NORMAL USER _ | Read and write permissions on a single table or on all tables in a schema. |
| ADMIN USER _ | Read, write, and administrator permissions on a single table or on all tables in a schema. |
| ADMIN TRASH _ | Read, write, administrator, and delete permissions on a single table or on all tables in a schema. |
| ALL | Read, write, administrator, delete, and system management permissions on a single table or on all tables in a schema. |

#### DCL

##### Overview

Data Control Language (DCL) consists of syntax for user role management and syntax for user permission management.

**Syntax for user role management**

In the SQL syntax supported by LindormTable, database users are used to define user roles. The following sample code provides an example.

```
user_name ::= identifier | string
```

**Syntax for user permission management**

The SQL syntax supported by LindormTable allows you to grant a user permissions on a schema or a table. If you do not specify a schema or table when you grant permissions to a user, the user is granted global permissions. The following table describes the permissions that you can grant.

##### SHOW USERS

You can execute the SHOW USERS statement to show all users.

```
show users;
```

##### CREATE USER

You can execute the CREATE USER statement to create a user and specify the password for the user.

```
create_user_statement ::= CREATE USER user_name identified by '''password'''; password ::= string
```

| Parameter | Description |
|---|---|
| user name _ | The name of the user. |
| password | The logon password for the user. |

**Parameters**

The following sample code provides an example of how to create a user and specify the password for the user.

```
create user test_user identified by 'testuserpassword';
```

##### ALTER USER

You can execute the ALTER USER statement to change the password of a specified user.

```
alter_user_statement ::= ALTER USER user_name SET password='newpassord'
            | WHERE oldpassword='oldpassword';
```

The following sample code provides an example on how to change the password of a specified user.

```
 alter user test_user set password='fda.@' where oldpassword='t12a@Hi';
```

##### DROP USER

You can execute the DROP USER statement to remove a user.

**Parameters**

The **user_name** parameter specifies the name of the user that you want to remove.

```
DROP USER test_user;
```

##### GRANT PRIVILEGE

This topic describes the syntax that is used to execute the GRANT PERMISSION statement, which grants specified permissions to a user.

```
grant_permission_statement ::= GRANT privilege_definition ON [GLOBAL|SCHEMA schema| TABLE table] r esource TO user_name privilege_definition ::= ALL | READ | WRITE | ADMIN | TRASH resource ::= schema_name
                               | table_name
```

| Parameter | Description |
|---|---|
| user name _ | The name of the user. |
| privilege definition _ | ALL Grant the user all permissions on the resources, including READ, WRITE, ADMIN, and TRASH. READ Grant the user the read permission on the resources. WRITE Grant the user the write permission on the resources. ADMIN Grant the user the administrator permissions on the resources. TRASH Grant the user the delete permission on the resources. |
| resource | The resources on which you want to grant permissions. Valid values: ALL , SCHEMA , and TABLE . |
| schema name _ | The name of the schema. |
| table name _ | The name of the table. |

| Parameter | Description |
|---|---|
| user name _ | The name of the user. |

**Note**

You can revoke permissions on different levels of resources. The following permission levels from high to low are supported: GLOBAL, DATABASE (SCHEMA), and TABLE.

**Parameters**

```
GRANT READ TO User1; GRANT WRITE ON TABLE Table1 TO User2; GRANT ADMIN ON TABLE my_schema.my_table TO User2; GRANT TRASH ON SCHEMA my_schema TO User3;
```

##### REVOKE PRIVILEGE

You can execute the REVOKE PERMISSION statement to revoke the specified permissions from a user.

```
revoke_permission_statement ::= REVOKE privilege_definition ON [GLOBAL | SCHEMA | TABLE] resource FROM user_name resource ::= schema_name | table_name
```

**Parameters**

| privilege definition _ | ALL Revoke all permissions on the resources, including READ, WRITE, ADMIN, and TRASH, from the user. READ Revoke the read permission on the resources from the user. WRITE Revoke the write permission on the resources from the user. ADMIN Revoke the administrator permission on the resources from the user. TRASH Revoke the delete permission on the resources from the user. |
|---|---|
| resource | The resources on which you want to grant permissions. Valid values: ALL , SCHEMA , and TABLE . |

**Note**

You can revoke permissions on different levels of resources. The following permission levels from high to low are supported: GLOBAL, DATABASE (SCHEMA), and TABLE.

```
REVOKE READ FROM User1; REVOKE WRITE ON TABLE Table1 FROM User2; REVOKE ADMIN ON TABLE my_schema.my_table FROM User2; REVOKE TRASH ON SCHEMA my_schema FROM User3;
```

#### EXPLAIN

This topic describes the syntax that is used to execute the EXPLAIN statement, which queries the execution plan of a specified SELECT statement. The EXPLAIN statement helps you find the position where an index is added in your table. This way, the index can be used to retrieve rows of data to accelerate your queries.

```
explain select select_options; explain select c1,c2, c3 from test where c1>1 and c2<3;
```

#### HINT

##### Overview

Hints are supplementary to the SQL syntax and play an important role in queries performed on databases. You can use hints in a SQL statement to change the method in which the SQL statement is executed. LindormTable supports hints in SQL statements. For example, you can use hints in LindormTable SQL statements to manage multiple versions of data. This topic describes the syntax and scenarios of hints in LindormTable.

| Attribute | Description | Applicable statement |
|---|---|---|
| l ts (N) __ _ | Specifies a timestamp for the version. | UPSERT and SELECT |
| l versions (N) __ _ | Specifies that the latest N versions of the data you query are returned. | SELECT |
| l ts min (N) __ _ _ | Specifies that versions whose timestamps are larger than N are returned. | SELECT |

**Usage notes**

Hints are supported by LindormTable 2.3.1 and later. For more information about how to upgrade the version of LindormTable, see the "Version update" topic in Lindorm User Guide. Hints can be used only after the INSERT, UPSERT, and SELECT keywords in SQL statements. Hints cannot be used in SQL statements that are executed to perform complex queries, such as subqueries and group queries. Hints do not support the PreparedStatement method.

```
hintExpression ::= /*+ hintItems */ hintItems ::= hintItem (',' hintItem )* hintItem ::= identifier ('(' hintOption ( ',' hintOption)* ')')? hintOption ::= expression
```

**Note**

Hints are used in the `/*+ hintItems */` format, in which `hintItems` indicates operationspecific hints. Multiple `hintItems` are separated by commas (,). Hints are enclosed by `/*+` and `*/` . Hints can be used only after the INSERT, UPSERT, and SELECT keywords in LindormTable SQL statements. Example:

```
UPSERT /*+ _l_ts_(3000) */ INTO t_test_ts(c1, c3) VALUES (1, 'c3'); SELECT /*+ _l_versions_(1) */ c1, c3, c3_l_ts FROM t_test_ts;
```

**Note**

Hints cannot be used after other keywords. For example, hints in the following statements are invalid: UPSERT INTO /*+ _l_ts_(3000) */ t_test_ts(c1, c3) VALUES (1, 'c3'); .

##### Use hints to implement data versioning

This topic describes how to use hints in LindormTable SQL to configure timestamps for data versioning.

**Features**

A timestamp is recorded for data that is written to each column of LindormTable. This timestamp indicates the server time when the data is written to the column. By default, the timestamp is used as the version ID of the data written to the column. You can also specify a timestamp for the data that you write to a column. A larger timestamp indicates a later version. To store multiple versions of data written to each column of LindormTable, you must configure the `'VERSIONS' = 'n'` attribute when you create the table. In the attribute, n is a positive integer that indicates the maximum number of versions that can be stored for each column. To query versioned data based on timestamps in LindormTable, you must specify specific attributes in SQL statements. The following table describes the attributes that you can specify.

| l ts max (N) __ _ _ | Specifies that versions whose timestamps are smaller than N are returned. | SELECT |
|---|---|---|

| Example 2: Query data whose timestamp is in the | [1000, 2001) | range. |
|---|---|---|
| SELECT /*+ l ts min (1000), l ts max (2001) */ c1, c3, c3 l ts FROM t test versions 2 WHERE c _ _ _ _ _ _ _ _ _ _ _ _ _ 1 = 1; |  |  |

**Use method**

In LindormTable, you can configure timestamps for non-primary key columns and use the timestamps to query the specified version of data.
1. To create a test table, execute the following statement:

```
CREATE TABLE t_test_versions_2 (c1 INT , c2 INT, c3 VARCHAR(50), PRIMARY KEY(c1)) 'VERSIONS'='5';
```

2. Write data to the table. Specify the version attribute and execute the following statement to configure
timestamps:

```
UPSERT /*+ _l_ts_(1000) */ INTO t_test_versions_2(c1, c3) values (1, '11') UPSERT /*+ _l_ts_(2001) */ INTO t_test_versions_2(c1, c3) values (1, '22') UPSERT /*+ _l_ts_(1000) */ INTO t_test_versions_2(c1, c2) values (1, 1) UPSERT /*+ _l_ts_(2001) */ INTO t_test_versions_2(c1, c2) values (2, 1) UPSERT /*+ _l_ts_(2002) */ INTO t_test_versions_2(c1, c2) values (2, 2) UPSERT /*+ _l_ts_(2003) */ INTO t_test_versions_2(c1, c2) values (2, 3) UPSERT /*+ _l_ts_(2004) */ INTO t_test_versions_2(c1, c2) values (2, 4) UPSERT /*+ _l_ts_(2005) */INTO t_test_versions_2(c1, c2) values (2, 5) UPSERT /*+ _l_ts_(2006) */ INTO t_test_versions_2(c1, c2) values (2, 6)
```

3. Query the specified versions of data by using timestamps. To view the timestamps of the queried
columns in the result, add the `_l_ts` suffix to the column names in the statement. Example 1: Query data whose timestamp is 1000.

```
SELECT /*+ _l_ts_(1000) */ c1, c3, c3_l_ts FROM t_test_versions_2 WHERE c1 = 1;
```

The following result is returned:

```
+----+----+---------+
| c1 | c3 | c3_l_ts |
+----+----+---------+
| 1  | 11 | 1000    |
+----+----+---------+
```

The following result is returned:

```
+----+----+---------+
| c1 | c3 | c3_l_ts |
+----+----+---------+
| 1  | 11 | 1000    |
+----+----+---------+
```

Example 3: Query the latest N versions of the specified data by specifying the `_l_versions_(N)` attribute. In this example, the value of N is set to 1.

```
SELECT /*+ _l_versions_(1) */ c1, c3, c3_l_ts FROM t_test_versions_2 WHERE c1 = 1;
```

The following result is returned:

| column are returned even if the | l versions (6) _ _ _ | attribute is specified in the statement. |
|---|---|---|
| SELECT /*+ l versions (6) */ c1, c2, c2 l ts FROM t test versions 2 WHERE c1=2; _ _ _ _ _ _ _ _ |  |  |

```
+----+----+---------+
| c1 | c3 | c3_l_ts |
+----+----+---------+
| 1  | 22 | 2001    |
+----+----+---------+
```

Example 4: Query the latest two versions of all columns and display different columns with the same timestamp in the same row. If you specify the `_l_versions_(N)` attribute in the statement, the timestamps of all non-primary key columns are returned.

```
SELECT /*+ _l_versions_(2) */ * FROM t_test_versions_2;
```

The following result is returned:

```
+----+------+---------+---------+---------+
| c1 |  c2  |  c3  | c2_l_ts | c3_l_ts |
+----+------+------+---------+---------+
| 1  | null | 22   | null    | 2001    |
| 1  | 1    | 11   | 1000    | 1000    |
| 2  | 6    | null | 2006    | null    |
| 2  | 5    | null | 2005    | null    |
+----+------+------+---------+---------+
```

Example 5: Query the latest six versions of the specified column. However, the VERSIONS attribute of The following result is returned:

```
+----+----+---------+
| c1 | c2 | c2_l_ts |
+----+----+---------+
| 2  | 6  | 2006    |
| 2  | 5  | 2005    |
| 2  | 4  | 2004    |
| 2  | 3  | 2003    |
| 2  | 2  | 2002    |
+----+----+---------+
```

### Best practices

#### Use ORDER BY in large result sets

This topic describes how to use the ORDER BY clause in SQL statements for Lindorm and provides the best practices in scenarios in which a large number of result entries are returned.

**Scenarios**

The ORDER BY clause in Lindorm SQL statements is commonly used in the following scenarios: If the number of result entries is less than 100,000, ORDER BY can be used to query data in the memory without limits. In these scenarios, you must enable in-memory computing. To enable this feature, submit a ticket. If the number of result entries is greater than or equal to 100,000, Lindorm imposes limits on the use of ORDER BY. The limits are affected by the data storage rules in Lindorm. When you execute the ORDER BY clause, result entries are not sorted by the SQL engine. If you want to sort result entries based on a specific column, you can specify the column as the single-equivalent prefix column.

**Warning**

If a large number of result entries are returned after in-memory computing is enabled, your client may stop responding.

| he | SELECT * FROM test WHERE p1=? ORDER BY p3 |  |
|---|---|---|
| CREATE INDEX idx ON test(p1, p3) |  | to create a s |

**Solutions**

In most cases, after a table is created, you can sort data only with the limits. If you want to sort result entries based on a specific column, you can specify the column as the single-equivalent prefix column. Sample code:

```
CREATE TABLE test(p1, p2, p3, c1, c2, c3, primary key(p1, p2, p3)) // p1, p2, and p3 compose the primary key. SELECT * FROM test WHERE p1=? ORDER BY p2 // ORDER BY can be used in this SQL s tatement. SELECT * FROM test WHERE p1=? and p2=? ORDER BY p3 // ORDER BY can be used in this SQL statement. SELECT * FROM test WHERE p1=? and c1=? ORDER BY p2 // ORDER BY can be used in this SQL statement. An equality condition is specified for the primary key column p2. SELECT * FROM test ORDER BY p1 // ORDER BY can be used in this SQL statement. However, we recommend that you do not use ORDER BY in this manner. SELECT * FROM test WHERE p1=? ORDER BY p3 // ORDER BY cannot be used in this SQ L statement. All primary key columns must be included in this statement. SELECT * FROM test WHERE p1<? ORDER BY p2 // ORDER BY cannot be used in this SQ L statement. You must specify a single equality condition for the primary key column p1 in the WHER E clause. SELECT * FROM test WHERE p1=? and p2>? ORDER BY p3 // ORDER BY cannot be used in this S QL statement. You must specify an equality condition for the primary key column p2 in the WHERE cla use. SELECT * FROM test WHERE p1=? and p2=? and p3=? ORDER BY c1 // ORDER BY cannot be used in this SQL statement. c1 is not a primary key column. SELECT * FROM test WHERE p1=a and p1=b ORDER BY p2 // This SQL statement does not support ORDER BY and requires an equality condition. However, p1 provides several values
```

. If you must use ORDER BY to sort a large number of result entries, you can use the following solutions: Change the primary key of your table. The following sample code provides examples on how to use ORDER BY to sort a large number of result entries: The secondary index and the data of the base table are stored in different tables. If you create a secondary index and use ORDER BY to sort result entries based on the index key columns of the secondary index, specify all index key columns in the order that is defined for the secondary index in the ORDER BY clause. Sample code:

```
// Sort result entries based on the c1 column. // Solution: Create a secondary index to sort result entries based on the c1 column.
```

You can achieve optimal performance by using a commonly used sorting method to sort data based on the index key columns of your secondary index. Sample code:

```
// Sort result entries based on the c1 column. // Solution: Create a secondary index to sort result entries based on the c1 column.
```

In the ORDER BY clause that includes multiple columns, specify the columns in the order that they appear in your base table and do not skip one or more of the columns. This way, you can achieve optimal performance. Sample code:

```
// Create a base table based on the specified schema. // Sort result entries based on the c1 and c2 index key columns. SELECT * FROM table WHERE p1 = ? ORDER BY c1 desc, c2 asc // When you create a secondary index for sorting, specify the c1 and c2 index key columns in the same order that they appear in the ORDER BY clause.
```

#### Design primary keys for Lindorm wide tables

The design of primary keys plays an important role in data partitioning and data queries in Lindorm. This topic describes the considerations for primary key design and provides examples.

**Considerations**

Q: Are primary key values unique? A: Different versions of a row use the same primary key value. By default, the latest version is returned when a query is performed. In most cases, primary keys must be unique unless multi-versioning is used. Best practice: A primary key can be a column or a set of multiple columns. Each primary key value corresponds to a record. `[userid]` : Only one column is specified as the primary key. Only one record is generated for each user. `[userid][orderid]` : Two columns are specified as the primary key. Multiple records are generated for each user. Q: How do I design the primary key in different scenarios? The primary key design limits the query methods that can be used. Lindorm supports `SELECT` statements that use the following methods: GET method: The primary key is used to query data. Example: `SELECT * FROM table WHERE`

```
userid='abc' AND orderid=123 .
```

**Note**

To use the GET method, you must specify all primary key columns. The values in all primary key columns must be explicit. SCAN method: Data is queried based on the primary key range. Example: `SELECT * FROM table WHERE`

```
userid='abc' AND 123<orderid<456 .
```

**Note**

To use the SCAN method, you must specify the range that you want to scan in the first primary key column. By default, if you do not specify the range, Lindorm rejects queries that must scan all data in the table because full table scans are inefficient. For more information, see SELECT. Best practice: How do I submit complex queries by using the preceding query methods? Solution: Create an index table. Specify the columns that you want to scan other than the primary key columns in the query conditions. Lindorm automatically filters out the irrelevant data. Use secondary indexes. Use `ORDER BY` to sort the data in descending order. This way, new records are sorted to the top rows of the table. Example: `SELECT * FROM table WHERE userid='abc' AND 123<orderid<456 ORDER BY orderid` `DESC` .

**Note**

In scenarios in which most queries are submitted to retrieve the up-to-date data, you can design the primary key as `[userid][orderid DESC]` to sort the data in descending order. Q: Do stacked hot spots exist if the data is distributed? A: No, hot spots do not exist if the data is distributed. The hash method is used to distribute data to different partitions. This prevents a server from being overloaded due to hot spots when other servers are idle. This can help you gain the benefits of distributed computing and parallel computing.

| [buyer id][timestmap][order number] _ _ |  |  |  | . The pri |
|---|---|---|---|---|
| ned as [seller id][timestmap][order number] designed as [order number] . _ | [seller id][timestmap][order number] |  |  |  |
|  |  | [order number] _ | . |  |

Best practices: Design a MD5 hash algorithm. The primary key is `[md5(userid).subStr(0,4)][userId][orderid]` . Design a reverse index. The primary key is `[reverse(userid)][orderid]` . Design the modulo operation. The primary key is [bucket][timestamp][hostname][log-event]; long

```
bucket = timestamp % numBuckets .
```

Add random numbers. The primary key is `[userId][orderid][random(100)]` . Q: Can the primary key design be simplified? A: You can reduce the number of primary key columns to decrease the amount of data that is scanned and improve the efficiency of queries and insert operations. Best practices: Replace the STRING data type with the LONG or INT data type. Example: `'2015122410' =>`

```
Long(2015122410) .
```

Replace names with codes. Example: `'taobao'=> 'tb'` . Q: Does the server return data that I do not need if I use the SCAN method to query data? A: No, the server does not return data that you do not need if you use the SCAN method to query data. The SQL syntax supported by LindormTable supports multiple data types. Each data type is separately encoded. For more information about the supported data types, see Basic data types.

**Commonly used designs**

Primary key designs for log data and time series data. Common scenarios: Query the data of a metric that is generated over a period of time. The primary key is designed as

```
 [hostname][log-event][timestamp] .
```

Query the most recent records of a metric. The primary key is designed as `[hostname][log-event]`

```
[timestamp DESC] .
```

Query data that contains only the time dimension or query data whose volume is large in a specific dimension. Design the primary key as long bucket = timestamp % numBuckets; [bucket][timestamp]

```
[hostname][log-event] .
```

Primary key designs for transaction data. Common scenarios: Query the transaction records of a seller within a specific period of time. Design the primary key as

```
 [seller_id][timestmap][order_number] .
```

Query the transaction records of a buyer within a specific period of time. Design the primary key as

```
 [buyer_id][timestmap][order_number] .
```

Query data based on order IDs. Design the primary key as `[order_number]` .

| Operating system | Download URL |
|---|---|
| Linux | lindorm-cli for linux |
| macOS | lindorm-cli for macOS |
| Windows | lindorm-cli for windows-x64 |
| Linux-arm64 | lindorm-cli for linux-arm64 |

## LindormTSDB

**Important**

Beginning September 1, 2024, LindormTSDB is **no longer available for purchase**. Users who purchased LindormTSDB or migrated from TSDB databases before this date can continue using LindormTSDB.

### Connection guide

#### Use Lindorm-cli to connect to and use

## LindormTSDB

This topic describes how to use Lindorm-cli to connect to and use LindormTSDB.

**Important**

Beginning September 1, 2024, LindormTSDB is **no longer available for purchase**. Users who purchased LindormTSDB or migrated from TSDB databases before this date can continue using LindormTSDB.

**Prerequisites**

The endpoint of LindormTSDB is obtained. For more information about how to obtain the endpoint of LindormTSDB, see the **View endpoints** topic of **Instance management** in **Lindorm User Guide**.

**Before you begin**

Download a Lindorm-cli client. You can download a compressed Lindorm-cli package based on the operating system of your client.

**Procedure**

1. Run the following command to decompress the downloaded Lindorm-cli client package. In this example,
the client is decompressed in Linux.

```
tar zxvf lindorm-cli-linux-latest.tar.gz
```

2. Connect to LindormTSDB.
If your client is deployed in Linux or macOS, go to the path in which **lindorm-cli.exe** is located, run the following command:

| Parameter |  | Required | Description |  |  |
|---|---|---|---|---|---|
| jdbc url |  | Yes | The endpoint and port that are required to connect to LindormTSDB. For more information about how to enable the endpoint, see the Enable a classic network endpoint topic of Instance management in Lindorm User Guide.. Example: jdbc:lindorm:tsdb:url=http://ld- |  |  |
|  |  |  |  | jdbc:lindorm:tsdb:url=http://ld- |  |
|  |  |  | bp12pc23yfb3*****-proxy-tsdb- |  |  |
|  |  |  | pub.lindorm.rds.aliyuncs.com:8242 |  |  |
| Username |  | No | The username used to connect to LindormTSDB. If the user authentication and permission verification feature is not enabled for LindormTSDB, you do not need to configure the username and password. |  |  |
| Password |  | No | The password used to connect to LindormTSDB. If you forget your password, you can change the password in the cluster management system console of LindormTable. |  |  |
| Database name |  | No | The name of the database to which you want to connect by using Lindorm-cli. If you do not specify a database, the client tries to connect to the default database named default. During this process, you can run the use <Database name> command to connect to a specified database. |  |  |

```
./lindorm-cli -url <jdbc url> -username <Username> -password <Password> -database <Database nam
```

`e>` If your client is deployed in Windows, you can use one of the following methods to connect to LindormTSDB: Open **lindorm-cli.exe** and run the following command:

```
connect <jdbc url> <Username> <Password> -database <Database name>
```

Go to the path in which **lindorm-cli.exe** is located and then run the following command in Command Prompt:

```
lindorm-cli -url <jdbc url> -username <Username> -password <Password> -database <Database name>
```

The following table describes the parameters. After the client is connected to LindormTSDB, the following result is returned:

```
Connected to jdbc:lindorm:tsdb:url=http://****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242 lindorm-cli version: 1.0.24
```

3. Use the syntax supported by LindormTSDB to perform operations. The following examples show how to
perform operations in LindormTSDB: i. Create a time series table. Create a time series table named sensor. We recommend that you specify a primary key when you create a time series table. In most cases, you can specify columns that correspond to the unique identifiers (UIDs) of a data source as a primary key, such as device ID columns in IoT scenarios, vehicle ID columns in Internet of vehicles (IoV) scenarios, and application ID or `ip:port` columns in monitoring scenarios. You must set the name of the timestamp column to time. This column provides the timestamps of your data. The unit of the timestamps is milliseconds.

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time TIMESTAMP,
    temperature DOUBLE,
    humidity BIGINT,
    PRIMARY KEY(device_id));// Delete this line if you use single-node Lindorm instances.
```

ii. Query time series tables in a database.

```
SHOW tables;
```

The following result is returned:

```
+-------------------+
| Tables_In_default |
+-------------------+
| sensor            |
+-------------------+
```

iii. Query the information about a specific column in a time series table.

```
DESCRIBE table sensor;
```

The following result is returned:

```
+-------------+-----------+------------+------------+
| columnName  | typeName  | columnKind | primaryKey |
+-------------+-----------+------------+------------+
| device_id   | VARCHAR   | TAG        | true       |
| region      | VARCHAR   | TAG        | false      |
| time        | TIMESTAMP | TIMESTAMP  | false      |
| temperature | DOUBLE    | FIELD      | false      |
| humidity    | BIGINT    | FIELD      | false      |
+-------------+-----------+------------+------------+
```

iv. Write data to the time series table.

**Note**

If two rows of data have the same primary key value and the same value in the time column, the two rows of data are considered the same data record. In this case, the row of data that is written later overwrites the other row of data. Write single rows of data into a time series table in sequence.

```
INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES('F07A1260','northcn','2021-04-22 15:33:00',12.1,45); INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES('F07A1260','northcn','2021-04-22 15:33:10',13.2,47); INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES('F07A1260','northcn','2021-04-22 15:33:20',10.6,46); INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES('F07A1261','southcn','2021-04-22 15:33:00',18.1,44); INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES('F07A1261','southcn','2021-04-22 15:33:10',19.7,44);
```

Write multiple rows of data at the same time to a time series table.

```
INSERT INTO sensor (device_id, region, time, temperature, humidity) VALUES ('F07A1260','north-cn','2021-04-22 15:33:00',12.1,45),
       ('F07A1260','north-cn','2021-04-22 15:33:10',13.2,47),
       ('F07A1260','north-cn','2021-04-22 15:33:20',10.6,46),
       ('F07A1261','south-cn','2021-04-22 15:33:00',18.1,44),
       ('F07A1261','south-cn','2021-04-22 15:33:10',19.7,44);
```

v. Query data in a time series table by condition.

**Important**

If no result is returned when you query data that has been written to a table, execute the
**DESCRIBE DATABASE <Database name>** statement to query whether a Time to Live (TTL) is
configured for the database. Data that is retained for a period longer than the TTL is automatically cleared and cannot be queried. Query data by condition. Query data that was generated by the `F07A1260` device from `2021-04-22 15:33:00` to `2021-04-`

```
22 15:33:20 . SELECT device_id,region,time,temperature,humidity FROM sensor WHERE device_id = 'F07A1260' AN D time >= '2021-04-22 15:33:00' AND time <= '2021-04-22 15:33:20';
```

The following result is returned:

| ted by the | F07A1260 |
|---|---|
| 2021-04-22 15:33:20 |  |

```
+-----------+----------+---------------------------+-------------+----------+
| device_id |  region  |           time            | temperature | humidity |
+-----------+----------+---------------------------+-------------+----------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.1        | 45       |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 13.2        | 47       |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.6        | 46       |
+-----------+----------+---------------------------+-------------+----------+
```

Perform a downsampling query in which sampling ratio is decreased to reduce the number of time records in the result set.

```
SELECT device_id,region,time,max(temperature) AS max_temperature FROM sensor WHERE device_id = 'F07A1260' AND time >= '2021-04-22 15:33:00' AND time <= '2021-04-22 15:33:20' SAMPLE BY 20 s;
```

The following result is returned:

```
+-----------+----------+---------------------------+-----------------+
| device_id |  region  |           time            | max_temperature |
+-----------+----------+---------------------------+-----------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 13.2            |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.6            |
+-----------+----------+---------------------------+-----------------+
```

Query aggregated data. Query the highest temperature of each region within the specified time range.

```
SELECT region,max(temperature) AS max_temperature FROM sensor WHERE time >= '2021-04-22 15:33 :00' AND time <= '2021-04-22 15:33:20' GROUP BY region;
```

The following result is returned:

```
+----------+-----------------+
|  region  | max_temperature |
+----------+-----------------+
| north-cn | 13.2            |
| south-cn | 19.7            |
+----------+-----------------+
```

4. Optional. Import CSV files into a time series table or export CSV files from a time series table.
Run the following command to import a CSV file into a time series table named `sensor` :

```
./lindorm-cli -url http://ld-bp1y919033x1k****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/ -f ormat=csv -input /path/of/data.csv -table sensor
```

**Important**

You can import only one CSV file into a time series table at a time. Make sure that the columns in the CSV file correspond to those in the time series table. Otherwise, errors may occur. You can specify the following parameters to import multiple rows of data in a batch or import data by using multiple concurrent threads:
**-batch**: the number of rows of data that are imported to the table in each import
operation. Default value: 2000.
**-concurrent**: the number of concurrent threads are used to import data to the table.
Default value: 10. Execute the following statement to export a CSV file from a time series table named `sensor` :

```
./lindorm-cli -url http://ld-bp1y919033x1k****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/ -e xecute 'select * from sensor' -format=csv -output /path/of/data.csv
```

**Common commands used in Lindorm-cli**

`help` : You can run this command to view help information. `connect` : You can run this command to connect to a server. `precision` : You can run this command to specify the time format. Valid values: rfc3339, h, m, s, ms, u, and ns. `exit` or `quit` : You can run one of the two commands to exit the current connection to LindormTSDB.

#### LindormTSDB Native SDK for Java

##### Initialize a LindormTSDB client

LindormTSDBClient is a Java client that you can use to read data from and write data to LindormTSDB. Before you use LindormTSDB SDK for Java to initiate a read request or write request, you must initialize a LindormTSDBClient instance and modify the ClientOptions parameters. When you create a LindormTSDBClient instance, you must specify the endpoint of the database that you want to access. For more information about how to obtain the endpoint of LindormTSDB, see the **View**
**endpoints** topic of **Instance management** in **Lindorm User Guide**. You can also configure optional
parameters to specify the connection timeout period, size of each batch for asynchronous batch write operations, and maximum number of times to resend a request. The following code provides an example on how to create a LindormTSDBClient instance:

| Parameter | Required | Description | Method |
|---|---|---|---|
| url | Required | The endpoint of LindormTSDB. | ClientOptions.Builder() |

```
// Obtain the connection string used to access LindormTSDB. String url = "http://ld-xxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242"; // Specify the username. String username = "username"; // Specify the password. String password = "password"; // For more information about the description and default values of the ClientOptions parameters, s ee the "Configure the LindormTSDBClient instance" section of this topic. ClientOptions options = ClientOptions
                // This parameter is required.
                .newBuilder(url)
                // This parameter is optional if authentication is disabled for LindormTSDB. This pa
rameter is required if authentication is enabled for LindormTSDB.
                .setUsername(username)
                // This parameter is optional if authentication is disabled for LindormTSDB. This pa
rameter is required if authentication is enabled for LindormTSDB.
                .setPassword(password)
                // This parameter is optional.
                .setNumBatchThreads(1)
                // This parameter is optional.
                .setMaxRetries(3)
                // This parameter is optional.
                .setRetryBackoffMs(1000)
                 // This parameter is optional.
                .setRequestTimeoutMs(30000)
                 // This parameter is optional.
                .setConnectTimeoutMs(30000)
                 // This parameter is optional.
                .setMaxWaitTimeMs(300)
                 // This parameter is optional.
                .setBatchSize(500)
                 // This parameter is optional.
                .build();
// Create a LindormTSDBClient instance. You can reuse the LindormTSDBClient thread without posing s ecurity risks. This way, you do not need to frequently delete and recreate the thread. LindormTSDBClient client = LindormTSDBFactory.connect(options); // Shut down the LindormTSDBClient instance. client.shutdown();
```

ClientOptions is a configuration class of LindormTSDBClient. You can configure ClientOptions parameters to specify the connection timeout period, size of each batch for asynchronous batch write operations, and maximum number of times to resend a request. The following table describes the parameters that you can configure for ClientOptions.

|  | username |  | Required if the user authentication and permission verification feature is enabled for LindormTSDB. For more information, see the User and permission management topic of Instance management in Lindorm User Guide. | The username. | ClientOptions.Builder#setUsername |
|---|---|---|---|---|---|
|  | password |  | Required if the user authentication and permission verification feature is enabled for LindormTSDB. For more information, see the User and permission management topic of Instance management in Lindorm User Guide. | The password. | ClientOptions.Builder#setPassword |
|  | numBatchThread s |  | No | The number of threads for asynchronous batch write operations. Default value: 1. | ClientOptions.Builder#setNumBatch Threads |
|  |  | numBatchThread |  |  |  |
|  | s |  |  |  |  |
|  | maxRetries |  | No | The maximum number of times to resend a write request that fails due to an internal server error or network error. Default value: 3. | ClientOptions.Builder#setMaxRetries |
|  | retryBackoffMs |  | No | The waiting period after a write request fails. Unit: milliseconds. Default value: 1000. By default, the instance waits 1,000 milliseconds before the instance resends a failed request. | ClientOptions.Builder#setRetryBacko ffMs |
|  |  | retryBackoffMs |  |  |  |
|  | requestTimeout Ms |  | No | The timeout period of requests. Unit: milliseconds. Default value: 90000. | ClientOptions.Builder#setRequestTi meoutMs |
|  |  | requestTimeout |  |  |  |
|  | Ms |  |  |  |  |

|  | connectTimeout Ms |  | No | The timeout period of connections. Unit: milliseconds. Default value: 90000. | ClientOptions.Builder#setConnectTi meoutMs |
|---|---|---|---|---|---|
|  |  | connectTimeout |  |  |  |
|  | Ms |  |  |  |  |
|  | maxWaitTimeMs |  | No | The maximum amount of time that a batch write request waits in a queue. Unit: milliseconds. Default value: 300. | ClientOptions.Builder#setMaxWaitTi meMs |
|  | batchSize |  | No | The size of each batch that is sent to the server. Default value: 500. | ClientOptions.Builder#setBatchSize |
|  | maxPointBatche s |  | No | The maximum number of batches that can be contained in a queue. Default value: 256. Note The maximum number of data points that can be contained in a queue can be calculated by using the following formula: maxPointBatches × batchSize. If the number of data points in a queue exceeds this value, write operations are blocked. | ClientOptions.Builder#setMaxPointB atches |
|  |  | maxPointBatche |  |  |  |
|  | s |  |  |  |  |
|  | defaultDatabas e |  | No | The default database that you want to access. Default value: default. By default, LindormTSDB automatically creates a database named default. | ClientOptions.Builder#setDefaultDat abase |
|  |  | defaultDatabas |  |  |  |
|  | e |  |  |  |  |
|  | queryChunkSize |  | No | The default number of rows to be returned in each batch for a query. Default value: 1000. | ClientOptions.Builder#setQueryChun kSize |
|  |  | queryChunkSize |  |  |  |
|  | schemaPolicy |  | No | The schema constraint of tables. Valid values: Strong and Weak. Default value: Strong. | ClientOptions.Builder#setSchemaPoli cy |

|  |  | maxWaitTimeMs |
|---|---|---|

##### Interfaces

This topic describes how to use the common interfaces provided by LindormTSDB SDKs. LindormTSDB SDKs provide management interfaces, write interfaces, and a query interface. LindormTSDB allows you to execute SQL statements to perform Data Definition Language (DDL) and Data Control Language (DCL) operations. This section provides examples on how to submit SQL statements to perform DDL and DCL operations. LindormTSDB SDKs allow you to use one of the following overload methods to submit SQL statements to LindormTSDB to perform DDL and DCL operations.

```
// Directly submit a SQL statement. Result execute(String sql); // Perform a DDL operation for a specified database. For example, you can perform a DDL operation to create a table in the database. Result execute(String database, String sql);
```

The Result object contains the execution result of the SQL statement. For example, after you submit a SHOW DATABASES statement, you can obtain the list of existing databases from the Result object. The Result object consists of the columns, metadata, and rows fields. The columns field contains the names of all columns in the returned results. The metadata field contains the data types of the columns. The rows field contains the results that are returned by row.

```java
public class Result {
    private List<String> columns;
    private List<String> metadata;
    private List<List<Object>> rows;
    ....
 }
```

**Examples of database management and table management**

You can perform DDL operations to create, delete, and query databases or tables. Sample code:

```java
// 1. Query existing databases. String showDatabase = "show databases"; Result result = lindormTSDBClient.execute(showDatabase); System.out.println("before create, db list: " + result.getRows().stream().map(e -> (String) e.get( 0)).collect(Collectors.toList())); // 2. Create a database. String createDatabase = "create database demo"; result = lindormTSDBClient.execute(createDatabase); System.out.println("create database:" + result.isSuccessful()); // 3. Query existing databases. result = lindormTSDBClient.execute(showDatabase); System.out.println("after create, db list: " + result.getRows().stream().map(e -> (String) e.get(0 )).collect(Collectors.toList())); String database = "demo"; // 4. Query existing tables. String showTables = "show tables"; result = lindormTSDBClient.execute(database, showTables); System.out.println("before create, table list: " + result.getRows().stream().map(e -> (String) e.g et(0)).collect(Collectors.toList())); // 5. Create a table. String createTable = "CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR TAG,time BIGINT,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))"; result = lindormTSDBClient.execute(database, createTable); System.out.println("create table: " + result.isSuccessful()); // 6. Query existing tables. result = lindormTSDBClient.execute(database, showTables); System.out.println("after create, table list: " + result.getRows().stream().map(e -> (String) e.ge t(0)).collect(Collectors.toList())); // 7. Query the detailed information about a table.
```

```java
String describeTable = "describe table sensor"; result = lindormTSDBClient.execute(database, describeTable); System.out.println("------------ describe table -------------------"); List<String> columns = result.getColumns(); System.out.println("columns: " + columns); List<String> metadata = result.getMetadata(); System.out.println("metadata: " + metadata); List<List<Object>> rows = result.getRows(); for (int i = 0, size = rows.size(); i < size; i++) {
    List<Object> row = rows.get(i);
    System.out.println("column #" + i + " : " + row);
} System.out.println("------------ describe table -------------------"); // 8. Delete a table. String dropTable = "drop table sensor"; result = lindormTSDBClient.execute(database, dropTable); System.out.println("drop table: " + result.isSuccessful()); // 9. Query existing tables. result = lindormTSDBClient.execute(database, showTables); System.out.println("after drop, table list: " + result.getRows().stream().map(e -> (String) e.get( 0)).collect(Collectors.toList())); // 10. Drop a database. String dropDatabase = "drop database demo"; result = lindormTSDBClient.execute(dropDatabase); System.out.println("drop database:" + result.isSuccessful()); // 11. Query existing databases. result = lindormTSDBClient.execute(showDatabase); System.out.println("after drop, db list : " + result.getRows().stream().map(e -> (String) e.get(0) ).collect(Collectors.toList()));
```

Sample results:

```
before create, db list: [default] after create, db list: [default, demo] columns: [columnName, typeName, columnKind] metadata: [VARCHAR, VARCHAR, VARCHAR] column #0 : [device_id, VARCHAR, TAG] column #1 : [region, VARCHAR, TAG] column #2 : [time, TIMESTAMP, TIMESTAMP] column #3 : [temperature, DOUBLE, FIELD] column #4 : [humidity, DOUBLE, FIELD] after drop, db list : [default]
```

**Note**

Other management-related operations, such as DDL operations performed to create and delete continuous queries, are not described in this section. You can refer to the SQL syntax supported by LindormTSDB to perform these operations. For more information about the SQL statements supported by LindormTSDB, see SQL syntax reference. LindormTSDB SDKs provide multiple write interfaces. These write interfaces are write methods whose names are the same but use different parameters. The write interfaces can be classified into the following types based on how the interfaces process write results: write interfaces that use the CompletableFuture<WriteResult> class to process write results, and write interfaces that use callback functions to process asynchronous write results. By default, LindormTSDBClient uses the asynchronous batch write method to improve the efficiency of write operations. If you want to perform synchronous write operations, call the join method of the CompletableFuture<WriteResult> class returned by the write method.

**Write operation records**

LindormTSDB SDKs use a Record object to store the information about a row that is to be written into a table. You must specify the table name, timestamp, tags, field names, and field values in a Record object. The timestamp and tags are used to create indexes. By default, LindormTSDB SDKs verify the validity of characters when you create a Record object. You can specify the parameter 'false' in the build() method.

```
Record record = Record
    // The name of the table.
    .table("sensor")
    // The timestamp that is accurate to the millisecond.
    .time(currentTime)
    // The tags.
    .tag("device_id", "F07A1260")
    .tag("region", "north-cn")
    // The field names and field values.
    .addField("temperature", 12.1)
    .addField("humidity", 45.0)
    .build();
```

**Interfaces that use the CompletableFuture object to process write**

Submit only one write operation record each time.

```
// Write data to the default database. CompletableFuture<WriteResult> future = lindormTSDBClient.write(record); // Write data to a specified database. String database = "demo"; CompletableFuture<WriteResult> future = lindormTSDBClient.write(database, record);
```

Submit multiple write operation records in a batch. We recommend that you use this method. You can use this method to reduce lock contention issues that occur in the pending tasks in the asynchronous queue when you use LindormTSDB SDKs to submit tasks.

```
List<Record> records; // Write data to the default database. CompletableFuture<WriteResult> future = lindormTSDBClient.write(records); // Write data to a specified database. String database = "demo"; CompletableFuture<WriteResult> future = lindormTSDBClient.write(database, records);
```

Process the result returned by the CompletableFuture<WriteResult> object. The following code block shows an example. You can call other methods of the CompletableFuture object based on your business requirements.

```java
CompletableFuture<WriteResult> future = lindormTSDBClient.write(records); // Process asynchronous write results. future.whenComplete((r, ex) -> {
    if (ex != null) { // A submission exception occurs. In most cases, the exception is returned be
cause a write operation fails.
        System.out.println("Failed to write.");
        Throwable throwable = ExceptionUtils.getRootCause(ex);
        if (throwable instanceof LindormTSDBException) {
            LindormTSDBException e = (LindormTSDBException) throwable;
            System.out.println("Caught an LindormTSDBException, which means your request made it to
                               + "but was rejected with an error response for some reason.");
            System.out.println("Error Code: " + e.getCode());
            System.out.println("SQL State:  " + e.getSqlstate());
            System.out.println("Error Message: " + e.getMessage());
        }  else {
            throwable.printStackTrace();
        }
    } else  { // The write operation is successful.
        if (r.isSuccessful()) {
            System.out.println("Write successfully.");
        } else {
            System.out.println("Write failure.");
        }
    }
});
```

**Important**

Do not use the whenComplete method of the CompletableFuture object to perform complex and timeconsuming calculation. Otherwise, the calculation may become stuck. If you want to perform complex and time-consuming calculation, submit the calculation task to other independent thread pools. For more information about the error codes, see Common error codes.

**Interfaces that use callback functions to process asynchronous write**

The following code block shows a write callback. The result parameter in the onCompletion method indicates the write result, the records parameter indicates the write operation record that corresponds to the callback, and the e parameter indicates the exception that is thrown when a write operation fails.

```
public interface Callback {
    void onCompletion(WriteResult result, List<Record> records, Throwable e);
}
```

The following example shows how to use a callback to process write results:

```java
Callback callback = new Callback() {
    @Override
    public void onCompletion(WriteResult result, List<Record> list,
                             Throwable throwable) {
        if (throwable != null) { // Write operation failure.
            if (throwable instanceof LindormTSDBException) {
                LindormTSDBException ex = (LindormTSDBException) throwable;
                System.out.println("errorCode: " + ex.getCode());
                System.out.println("sqlstate: " + ex.getSqlstate());
                System.out.println("message: " + ex.getMessage());
            } else {
                // Other errors.
                throwable.printStackTrace();
            }
        } else {
            if (result.isSuccessful()) {
                System.out.println("Write successfully.");
            } else {
                System.out.println("Write failure.");
            }
        }
    }
};
```

**Important**

Do not use the onCompletion method of the callback to perform complex and time-consuming calculation. Otherwise, the calculation may become stuck. If you want to perform complex and timeconsuming calculation, submit the calculation task to other independent thread pools. For more information about the error codes, see Common error codes. Submit only one write operation record each time.

```
// Write data to the default database. lindormTSDBClient.write(record, callback); // Write data to a specified database. String database = "demo"; lindormTSDBClient.write(database, record, callback);
```

Submit multiple write operation records in a batch. We recommend that you use this method. You can use this method to reduce lock contention issues that occur in the pending tasks in the asynchronous queue when you use LindormTSDB SDKs to submit tasks.

```
List<Record> records; // Write data to the default database. lindormTSDBClient.write(records, callback); // Write data to a specified database. String database = "demo"; lindormTSDBClient.write(database, records, callback);
```

The query interface provided by LindormTSDB SDKs allows you to use SQL statements to query data. For more information, see SQL syntax reference. The following code block provides an example of the query interface provided by LindormTSDB SDK. You must configure the input parameters to specify the database that you want to query, the SQL statement that is used to query data, and the chunk size that specifies the number of rows to be returned in each batch.

```
ResultSet query(String database, String sql, int chunkSize);
```

The following code block shows the ResultSet interface that is used by LindormTSDB SDKs to display the results of SQL statements:

```
public interface ResultSet extends Closeable {
    QueryResult next();
    void close();
}
```

You can use the next() method of the ResultSet interface to obtain the query results in a loop. If the QueryResult object returned by the next() method is null, all query results are obtained. After all query results are obtained, you can call the close() method of the ResultSet interface to release the occupied input and output resources. The QueryResult object consists of the columns, metadata, and rows fields. The columns field contains the names of all columns in the query results. The metadata field contains the data types of the columns. The rows field contains the query results that are returned by row. For more information about the data types supported by LindormTSDB, see Data types. The following example shows how to use ResultSet to process query results.

```java
String sql = "select * from sensor"; int chunkSize = 100; ResultSet resultSet = lindormTSDBClient.query("demo", sql, chunkSize); // Process query results. try {
    QueryResult result = null;
    // If the next() method of ResultSet returns null, all query results are obtained.
    while ((result = resultSet.next()) != null) {
        List<String> columns = result.getColumns();
        System.out.println("columns: " + columns);
        List<String> metadata = result.getMetadata();
        System.out.println("metadata: " + metadata);
        List<List<Object>> rows = result.getRows();
        for (int i = 0, size = rows.size(); i < size; i++) {
            List<Object> row = rows.get(i);
            System.out.println("row #" + i + " : " + row);
        }
    }
} finally {
    // After all query results are obtained, make sure that you call the close() method of ResultSe
t to release the occupied input and output resources.
    resultSet.close();
}
```

**Important**

Regardless of whether a query is successful, you must explicitly call the close() method of ResultSet to release input and output resources after the query is complete. Otherwise, a connection leak occurs. LindormTSDB SDKs also provide multiple implementations for overloading the query interface. You can choose one of the following implementations based on your business requirements.

| Parameter | Description |
|---|---|
| code | The error code that is returned by LindormTSDB. |
| sqlstate | The sqlstate value that is returned by LindormTSDB. |
| message | The error message that is returned by LindormTSDB. |

```
// The SQL statement. String sql = "xxxx"; // 1. Execute a SQL statement to query the default database. By default, 1,000 rows are returned in each batch. ResultSet resultSet = lindormTSDBClient.query(sql); String database = "demo"; // 2. Execute a SQL statement to query a specified database. By default, 1,000 rows are returned in each batch. ResultSet resultSet = lindormTSDBClient.query(database, sql);
```

##### Handle exceptions

This topic describes how to configure your application to handle exceptions that are returned by LindormTSDB SDKs. Exceptions thrown by LindormTSDB SDKs can be classified into two types: ClientException that indicates client-related exceptions and LindormTSDBException that indicates server-related exceptions. Both exception types are inherited from RuntimeExceptions.

**ClientException**

A ClientException can be thrown when a client sends a request or transmits data to LindormTSDB. For example, a ClientException is thrown if a request is sent in poor network conditions. A LindormTSDBException can be triggered by server errors. It is thrown based on the error information returned from the server. A LindormTSDBException contains the error code and error message that are returned by LindormTSDB. You can use the information to identify the cause and then handle the exception. The following table describes the information that is included in a LindormTSDBException in common scenarios.

**Note**

For more information about the error messages that are returned by LindormTSDB, see Common error codes. The following sample code provides an example on how to handle exceptions:

```java
try {
    // The operation that is performed by LindormTSDB, such as a query.
    lindormTSDBClient.query(....);
    System.out.println("Caught an LindormTSDBException, which means your request made it to Lindorm
TSDB, "
            + "but was rejected with an error response for some reason.");
    System.out.println("Error Code: " + e.getCode());
    System.out.println("SQL State:  " + e.getSqlstate());
    System.out.println("Error Message: " + e.getMessage());
} catch(ClientException ce) {
    System.out.println("Caught an ClientException, which means the client encountered "
            + "a serious internal problem while trying to communicate with Lindorm TSDB, "
            + "such as not being able to access the network.");
    System.out.println("Error Message: " + ce.getMessage());
}
```

**Note**

For more information about the error messages that are returned by LindormTSDB, see Common error codes.

##### Release notes

This topic describes the release notes for LindormTSDB Native SDK for Java.

**Note**

You can obtain all versions of LindormTSDB Native SDK for Java from the Maven repository. For more information, visit Maven repository.

**V1.0.4**

The issue that the execute() interface cannot parse the returned result is fixed.

**V1.0.3**

The value of **schema_policy** can be set to `None` . This way, LindormTSDB does not create tables when you write data. A connection pool can be used to configure the **keepAliveMs** and **maxIdleConn** parameters. Message sequences in error logs can be converted to readable characters. The query() interface can parse the type of data based on the schema. The issue that an error is reported when data is checked based on its timestamp is fixed.

**V1.0.2**

Loose rules are used to verify strings.

**V1.0.1**

HTTPS is supported. The okhttp3 library is renamed to prevent dependency conflicts. The writeSync method is added. You can configure specific parameters when you use this method to synchronously write data. The forced flush method is added. You can use this method to force the system to flush the data in an asynchronous queue. A health check interface **isHealth** is added. You can use this interface to check the health status of LindormTSDB.

| following dependencies to the | dependencies | section in the pom.xml file. |
|---|---|---|
| <dependency> <groupId>com.aliyun.lindorm</groupId> <artifactId>lindorm-tsdb-client</artifactId> <version>1.0.4</version> </dependency> |  |  |

URL verification is supported. The system checks the availability of the requested URL when the system creates a client. Server version verification is supported. The version of the server must be 3.4.8 or later.

**V1.0.0**

The first version of the LindormTSDB Native SDK for Java is released. The first version supports features such as basic authentication, asynchronous batch writes, and streaming queries.

##### Tutorial: Use LindormTSDB SDK for Java to

**connect to and use LindormTSDB**

This topic describes how to use LindormTSDB SDK for Java to connect to LindormTSDB and how to use LindormTSDB.

**Prerequisites**

Java Development Kit (JDK) V1.8 or later is installed. The version of LindormTSDB is 3.4.7 or later. For more information about how to view the version of LindormTSDB and how to update LindormTSDB, see the **Update Lindorm instances and**
**LindormTSDB** topic of **Instance management** in **Lindorm User Guide**.
The endpoint of LindormTSDB is obtained. For more information, see the **View endpoints** topic of
**Instance management** in **Lindorm User Guide**.

**Preparations**

Before you use LindormTSDB SDK for Java to connect to LindormTSDB, you must install LindormTSDB SDK for Java. For example, you can use one of the following methods to install LindormTSDB SDK for Java V1.0.0:

**Note**

LindormTSDB SDK for Java provides a Maven-based sample project. You can download the demo of the sample project, and compile and run the sample project on your on-premises machine. You can also develop a new project based on the sample project. Method 2: Import the JAR files of LindormTSDB SDK to an Eclipse project. i. Download the JAR files of LindormTSDB SDK. ii. Extract files from the package. iii. Import the files that are extracted to the Eclipse project. a. In Eclipse, open the project in which you want to run LindormTSDB SDK for Java, right-click the project name, and then click **Properties** from the shortcut menu. b. In the dialog box that appears, choose **Java Build Path > Libraries > Add JARs** and select the lindorm-tsdb-client-1.0.0.jar file and JAR files in the lib folder. c. Click **Apply and Close**. Method 3: Import the JAR files of LindormTSDB SDK to an IntelliJ IDEA project i. Download the JAR files of LindormTSDB SDK. ii. Extract files from the package. iii. Import the files to the IntelliJ IDEA project. a. In IntelliJ IDEA, open the project in which you want to run LindormTSDB SDK for Java. In the menu bar, choose **File > Project Structure**. b. On the left-side navigation pane of the **Project Structure** dialog box, choose **Project Structure >**
**Modules**.
c. Click the icon and click **JARs or directories**. d. In the dialog box that appears, select the lindorm-tsdb-client-1.0.0.jar file and the JAR files in the lib folder, and click **OK**. e. Click **Apply**. f. Click **OK**.

**Note**

You can obtain each version of LindormTSDB SDK for Java from the Maven repository. For more information, see Maven Repository. For more information about the versions of LindormTSDB SDK for Java, see Release notes.

**Procedure**

1. Create a database instance. When you create a LindormTSDB client, you must specify the endpoint of
LindormTSDB. For more information about how to obtain the endpoint, see the **View the endpoint** topic of the **Instance management** in **Lindorm User Guide**.

```
String url = "http://ld-bp17j28j2y7pm****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242"; // LindormTSDB clients are thread-safe and can be reused. You do not need to create a client for each thread and then destroy the client after operations are complete. ClientOptions options = ClientOptions.newBuilder(url).build(); LindormTSDBClient lindormTSDBClient = LindormTSDBFactory.connect(options);
```

2. Create a database named demo and a time series table named sensor. For information about the SQL
statements that are used to create databases and time series tables, see CREATE DATABASE and CREATE TABLE.

```
lindormTSDBClient.execute("CREATE DATABASE demo"); lindormTSDBClient.execute("demo","CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR TAG,t ime BIGINT,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))");
```

3. Write data to a table.

**Note**

By default, the LindormTSDB client asynchronously writes data in batches to a table to improve the write performance. If you want to write data synchronously, you can call the `write()` method to write data, use `CompletableFuture<WriteResult>` to process the data, and then call the `join()` method to join the results.

```java
int numRecords = 10; List<Record> records = new ArrayList<>(numRecords); long currentTime = System.currentTimeMillis(); for (int i = 0; i < numRecords; i++) {
    Record record = Record
        .table("sensor")
        .time(currentTime + i * 1000)
        .tag("device_id", "F07A1260")
        .tag("region", "north-cn")
        .addField("temperature", 12.1 + i)
        .addField("humidity", 45.0 + i)
        .build();
    records.add(record);
} CompletableFuture<WriteResult> future = lindormTSDBClient.write("demo", records); // Process the data that is asynchronously written. future.whenComplete((r, ex) -> {
    // Process write failures.
    if (ex != null) {
        System.out.println("Failed to write.");
            LindormTSDBException e = (LindormTSDBException) ex;
            System.out.println("Caught an LindormTSDBException, which means your request made it
                               + "but was rejected with an error response for some reason.");
            System.out.println("Error Code: " + e.getCode());
            System.out.println("SQL State:  " + e.getSqlstate());
            System.out.println("Error Message: " + e.getMessage());
        }  else {
            ex.printStackTrace();
        }
    } else  {
        System.out.println("Write successfully.");
    }
}); // In this example, a simple synchronization operation is performed to process the data that is w ritten to the table. System.out.println(future.join());
```

4. Query data in the time series table. For information about the SQL statements that can be used to
query data, see Basic syntax of the SELECT statement.

```java
String sql = "select * from sensor limit 10"; ResultSet resultSet = lindormTSDBClient.query("demo", sql); try {
    // Process the query results.
    QueryResult result = null;
    // Query results are returned in batches. By default, a batch can contain up to 1,000 rows.
    // When the next() method that is used to obtain result sets returns null, this means that al
l results are retrieved.
    while ((result = resultSet.next()) != null) {
        List<String> columns = result.getColumns();
        System.out.println("columns: " + columns);
        List<String> metadata = result.getMetadata();
        System.out.println("metadata: " + metadata);
        List<List<Object>> rows = result.getRows();
        for (int i = 0, size = rows.size(); i < size; i++) {
            List<Object> row = rows.get(i);
            System.out.println("row #" + i + " : " + row);
        }
    }
} finally {
    // After all query results are obtained, make sure that you call the close method of ResultSe
t to release the occupied input and output resources.
    resultSet.close();
} import com.aliyun.lindorm.tsdb.client.ClientOptions; import com.aliyun.lindorm.tsdb.client.LindormTSDBClient; import com.aliyun.lindorm.tsdb.client.LindormTSDBFactory; import com.aliyun.lindorm.tsdb.client.exception.LindormTSDBException; import com.aliyun.lindorm.tsdb.client.model.QueryResult; import com.aliyun.lindorm.tsdb.client.model.Record; import com.aliyun.lindorm.tsdb.client.model.ResultSet; import com.aliyun.lindorm.tsdb.client.model.WriteResult; import com.aliyun.lindorm.tsdb.client.utils.ExceptionUtils; import java.util.ArrayList; import java.util.List; import java.util.concurrent.CompletableFuture; public class QuickStart {
    public static void main(String[] args) {
        // 1. Create a client.
        String url = "http://ld-xxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242";
        // LindormTSDB clients are thread-safe and can be reused. You do not need to create a clien
t for each thread and then destroy the client after operations are complete.
        ClientOptions options = ClientOptions.newBuilder(url).build();
        LindormTSDBClient lindormTSDBClient = LindormTSDBFactory.connect(options);
        // 2. Create a database named demo and a table named sensor.
        lindormTSDBClient.execute("CREATE DATABASE demo");
        lindormTSDBClient.execute("demo","CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR
TAG,time BIGINT,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))");
        // 3. Write data to the table.
        int numRecords = 10;
        List<Record> records = new ArrayList<>(numRecords);
```

y

```java
( );
        long currentTime = System.currentTimeMillis();
        for (int i = 0; i < numRecords; i++) {
            Record record = Record
                    .table("sensor")
                    .time(currentTime + i * 1000)
                    .tag("device_id", "F07A1260")
                    .tag("region", "north-cn")
                    .addField("temperature", 12.1 + i)
                    .addField("humidity", 45.0 + i)
                    .build();
            records.add(record);
        }
        CompletableFuture<WriteResult> future = lindormTSDBClient.write("demo", records);
        // Process the data that is asynchronously written.
        future.whenComplete((r, ex) -> {
            // Process write failures.
            if (ex != null) {
                System.out.println("Failed to write.");
                Throwable throwable = ExceptionUtils.getRootCause(ex);
                if (throwable instanceof LindormTSDBException) {
                    LindormTSDBException e = (LindormTSDBException) throwable;
                    System.out.println("Caught an LindormTSDBException, which means your request mad
                            + "but was rejected with an error response for some reason.");
                    System.out.println("Error Code: " + e.getCode());
                    System.out.println("SQL State:  " + e.getSqlstate());
                    System.out.println("Error Message: " + e.getMessage());
                }  else {
                    throwable.printStackTrace();
                }
            } else  {
                System.out.println("Write successfully.");
            }
        });
        // In this example, a simple synchronization operation is performed to process the data tha
t is written to the table.
        System.out.println(future.join());
        // 4. Query data.
        String sql = "select * from sensor limit 10";
        ResultSet resultSet = lindormTSDBClient.query("demo", sql);
        try {
            // Process the query results.
            QueryResult result = null;
            // Query results are returned in batches. By default, a batch can contain up to 1,000
rows.
            // When the next() method that is used to obtain result sets returns null, this means
that all results are retrieved.
            while ((result = resultSet.next()) != null) {
                List<String> columns = result.getColumns();
                System.out.println("columns: " + columns);
                List<String> metadata = result.getMetadata();
                System.out.println("metadata: " + metadata);
                List<List<Object>> rows = result.getRows();
                for (int i = 0, size = rows.size(); i < size; i++) {
                    List<Object> row = rows.get(i);
                    System.out.println("row #" + i + " : " + row);
                }
            }
```

```
        } finally {
            // After all query results are obtained, make sure that you call the close method of
ResultSet to release the occupied input and output resources.
            resultSet.close();
        }
        lindormTSDBClient.shutdown();
    }
}
```

#### Java JDBC driver

This topic describes how to use the Java Database Connectivity (JDBC) driver for Lindorm to connect to and use LindormTSDB and the supported API operations and methods.

**Background information**

The JDBC driver of LindormTSDB complies with API operations that are defined in the JDBC 4.1 specifications. LindormTSDB is a time series database. Therefore, the features provided by the JDBC driver are a subset of the basic feature set that is defined in the JDBC 1.0 specifications.

**Prerequisites**

Java Development Kit (JDK) V1.8 or later is installed. The IP address of your client is added to the whitelist of the Lindorm cluster. For more information, see Configure whitelists. The endpoint of Lindorm is obtained. For more information, see View endpoints.

**Procedure**

1. You can use one of the following methods to install the JDBC driver for Lindorm:
Manually install the JDBC driver Download the Lindorm-all-client JAR package to your client and install the JDBC driver. Select the JDBC driver version that you want to install. For example, if you want to install JDBC driver 2.1.2, download the lindorm-all-client-2.1.2.jar package. Use Maven to download the JDBC driver To integrate the JDBC driver into a Maven project, create a Maven project and add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun.lindorm</groupId>
    <artifactId>lindorm-all-client</artifactId>
    <version>2.1.2</version>
</dependency>
```

**Note**

Specify the version of lindorm-all-client based on your business requirements.
2. Access LindormTSDB. For more information about the sample code, see Tutorial: Use the JDBC driver for
Lindorm to connect to and use LindormTSDB. i. Establish a connection between LindormTSDB and your client.

```
String url = "jdbc:lindorm:tsdb:url=http://<host:port>"; Connection conn = DriverManager.getConnection(url);
```

**Note**

`host:port` : specifies the endpoint and port that are used to connect to LindormTSDB,

```
such as ld-bp17j28j2y7pm****-proxy-tsdb.lindorm.rds.aliyuncs.com:8242 .
```

`jdbc:lindorm:tsdb:url=http://<host:port>` : specifies the URL of the JDBC driver. For information about the syntax and connection parameters, see URL of the JDBC driver. ii. Create a time series database and a table.

```
Statement stmt = conn.createStatement(); stmt.execute("CREATE DATABASE test"); stmt.execute("USE test"); stmt.execute("CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR TAG,time TIMESTAMP,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))");
```

iii. Write data to the table.

```
// Use PreparedStatement to write multiple rows of data in batches. We recommend that you use t his method. PreparedStatement pstmt = conn.prepareStatement("INSERT INTO sensor (device_id, region, time, t emperature, humidity) VALUES (?, ?, ?, ?, ?)"); int batchSize = 100; long ts = System.currentTimeMillis(); for (int i = 0; i < batchSize; i++) {
     // Specify parameters for columns in the order in which the columns are specified in the I
NSERT statement.
     pstmt.setString(1, "F07A1260");
     pstmt.setString(2, "north-cn");
     pstmt.setLong(3, ts + i * 10000);
     pstmt.setDouble(4, 12.1);
     pstmt.setLong(5, 45);
     pstmt.addBatch();
} pstmt.executeBatch(); pstmt.clearBatch(); // Write multiple rows of data to the table in batches. Statement stmt = conn.createStatement(); stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1260','north-cn',1619076780000,12.1,45)"); stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1260','north-cn',1619076790000,13.2,47)"); stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1260','north-cn',1619076800000,10.6,46)"); stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1261','south-cn',1619076780000,18.1,44)"); stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1261','south-cn',1619076790000,19.7,44)"); stmt.executeBatch(); stmt.clearBatch(); // Write a single row of data. We recommend that you do not use this method. Statement stmt = conn.createStatement(); stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity) values('F07A1260','north-cn',1619076780000,12.1,45)");
```

iv. Query data in the sensor table.

```java
ResultSet rs = stmt.executeQuery("select device_id, region,time,temperature,humidity from senso r where time >= 1619076780000 and time <= 1619076800000"); while (rs.next()) {
    String device_id = rs.getString("device_id");
    String region = rs.getString("region");
    Long time = rs.getLong("time");
    Double temperature = rs.getDouble("temperature");
    Long humidity = rs.getLong("humidity");
    System.out.printf("%s %s %d %f %d\n", device_id, region, time, temperature, humidity);
}
```

| API operation | Supported method |
|---|---|
| Connection | close() createStatement(int, int) createStatement(int, int, int) getSchema() prepareStatement(String, int, int) prepareStatement(String, int, int, int) setSchema(String) Note The Connection API operation provided by the JDBC driver for Lindorm is not thread-safe. We recommend that you do not use the same Connection object in multiple threads. |
| Statement | addBatch(String) close() execute(String) executeQuery(String) getMoreResult isClosed() setFetchSize(int) |
| ResultSet | addBatch() clearBatch() close() execute() executeBatch() executeQuery() getParameterNumber() setNull(int) setXXX(int, T) Note For information about the data types supported by LindormTSDB, see Data types. |

The following table describes the API operations and methods that are supported when you use the JDBC driver to access LindormTSDB.

**Note**

API operations that are not described in the following table are partially compatible with the upperlayer framework and return the default values. If you have any questions, submit a ticket.

| PreparedStatement | close() getStatement() next() wasNull() getXXX(int) Note For information about the data types supported by LindormTSDB, see Data types. |
|---|---|

| Parameter | Description |
|---|---|
| user | The username of the Lindorm cluster. The username that is used for authentication when you connect to LindormTSDB. Note If the user authentication feature is not enabled for LindormTSDB, you do not need to specify the username. |
| password | The password that corresponds to the username. The password that is used for authentication when you connect to LindormTSDB. If you forget the password, you can change the password in the cluster management system of LindormTable. For more information, see the Change the password of a user section of the Manage users topic. Note If the user authentication feature is not enabled for LindormTSDB, you do not need to specify the password. |
| database | The database that you want to access. If you do not specify this parameter, you are connected to the default database by default. |
| lindorm.tsdb.driver.connect.timeout | The timeout period of connections created to the server of LindormTSDB. Unit: milliseconds. The default value is 60,000, which is equal to 60 seconds. |

The URL of the JDBC driver is important when applications call the Connection operation to establish database connections. The URL of the JDBC driver is usually used to specify the protocol for database connections. LindormTSDB is connected by using the JDBC driver. The following sample code shows the URL of the JDBC driver:

```
jdbc:lindorm:tsdb:url=http://${host:port}[;${connection_parameter}=${connection_value}]...
```

**Note**

`host:port` : This field specifies the endpoint and port that are used to connect to LindormTSDB, such

```
as ld-bp17j28j2y7pm****-proxy-tsdb.lindorm.rds.aliyuncs.com:8242 .
```

The following table describes the connection parameters that are included in the URL of the JDBC driver.

| lindorm.tsdb.driver.socket.timeout | The maximum interval between socket read and write operations. Unit: milliseconds. The default value is -1, which indicates that no interval is specified. |
|---|---|

**Important**

If a connection between the Lindorm client and server is idle for 60 minutes, the server closes the connection to improve resource utilization. If you use a connection closed by the server, the

```
 com.aliyun.lindorm.client.shaded.org.apache.calcite.avatica.http.ConnectionDisconnectedException
```

error is reported. To resolve the issue, establish a new connection.

**Use the connection pool Alibaba Druid to access LindormTSDB**

When you use Java to develop an application that stores data in LindormTSDB, we recommend that you configure the application to use the JDBC driver to connect to LindormTSDB. In this case, you also need to create Connection objects. If a new Connection object is created each time LindormTSDB is connected, excessive resource overheads are incurred. To reduce the resource overheads, use a connection pool to create and manage connections. Various connection pools are available. The following section describes how to use the open source connection pool Alibaba Druid.
1. Add the dependency of the connection pool Alibaba Druid to a Maven project. Start the client, create a
project, and configure a Maven dependency in the pom.xml file. The following sample code shows the detailed information about the dependency.

```xml
<dependency>
      <groupId>com.alibaba</groupId>
      <artifactId>druid</artifactId>
      <version>1.2.6</version>
    </dependency>
```

2. Add the dependency of the JDBC driver for Lindorm to the Maven project. For more information, see
Step 1 in the Procedure section of this topic.
3. Run the following code to create a DataSource object and specify the URL of the JDBC driver for the
DataSource object:

```
dataSource = new DruidDataSource();
        try {
dataSource.setDriver(DriverManager.getDriver("jdbc:lindorm:tsdb:url=http://<host:port>"));
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
```

**Note**

`host:port` : the endpoint and port used to access LindormTSDB. Example: `ld-bp17j28j2y7pm****-`

```
proxy-tsdb.lindorm.rds.aliyuncs.com:8242 .
```

4. Establish a JDBC connection based on the DataSource object and access LindormTSDB. The following
code block provides an example:

```java
import com.alibaba.druid.pool.DruidDataSource; import java.sql.*; public class App {
    private DruidDataSource dataSource;
    public void setUp() {
        dataSource = new DruidDataSource();
        try {
            dataSource.setDriver(DriverManager.getDriver("jdbc:lindorm:tsdb:url=http://ld-
bp17j28j2y7pm****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242"));
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        dataSource.setUrl("jdbc:lindorm:tsdb:url=http://ld-bp17j28j2y7pm****-proxy-tsdb-
pub.lindorm.rds.aliyuncs.com:8242");
        dataSource.setValidationQuery("select 1");
        dataSource.setMaxActive(1);
        dataSource.setUsername("username");
        dataSource.setPassword("****");
        dataSource.setKeepAlive(true);
        dataSource.setMinEvictableIdleTimeMillis(80);
        dataSource.setMaxWait(10000);
        dataSource.init();
    }
    public void close() {
        dataSource.close();
    }
        try (Connection conn = this.dataSource.getConnection()) {
            try (Statement stmt = conn.createStatement()) {
                ResultSet rs = stmt.executeQuery("select * from sensor");
                long count = 0;
                while (rs.next()) {
                    count++;
                }
                System.out.println("count=" + count + " ");
            } catch (RuntimeException e) {
                e.printStackTrace();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } catch (RuntimeException e) {
            System.out.println("connection failed.");
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public static void main( String[] args ) {
        App app = new App();
        app.setUp();
        app.testQuery();
        app.close();
    }
}
```

| Supported API operation | Supported method |
|---|---|
| Connection | close() createStatement(int, int) createStatement(int, int, int) getSchema() prepareStatement(String, int, int) prepareStatement(String, int, int, int) setSchema(String) Note The Connection API operation provided by the JDBC driver for Lindorm is not thread-safe. We recommend that you do not use the same Connection object in multiple threads. |
| Statement | addBatch(String) close() execute(String) executeQuery(String) getMoreResult isClosed() setFetchSize(int) |

##### Supported API operations and methods

This topic describes the API operations and methods that are supported when you use the Java Database Connectivity (JDBC) driver to access LindormTSDB.

**Note**

API operations that are not described in the following table are partially compatible with the upperlayer framework and return the default values. If you have questions, contact the technical support of LindormTSDB (DingTalk ID: s0s3eg3).

| ResultSet | addBatch() clearBatch() close() execute() executeBatch() executeQuery() getParameterNumber() setNull(int) setXXX(int, T) Note For more information about the data types supported by LindormTSDB, see Data types. |
|---|---|
| PreparedStatement | close() getStatement() next() wasNull() getXXX(int) Note For more information about the data types supported by LindormTSDB, see Data types. |

| Category | Parameter | Example | Description |
|---|---|---|---|

##### URL of the JDBC driver

This topic describes the URL of the JDBC driver. The URL of the JDBC driver is important to applications that need to establish database connections by calling the Connection operation. The URL of the JDBC driver is usually used to specify the protocol for database connections. LindormTSDB is connected to the client by using the JDBC driver. The following example shows the syntax of the URL of the JDBC driver:

```
jdbc:lindorm:tsdb:url=http://${host:port}[;${connection_parameter}=${connection_value}]...
```

**Parameters**

| host:port | None | jdbc:lindorm :tsdb:url=htt p://ld- bp12pc23yf b3*****- proxy-tsdb- pub.lindorm. rds.aliyuncs. com:8242 | The endpoint and port used to connect to LindormTSDB. For more information, see the View endpoints topic in Lindorm User Guide. |
|---|---|---|---|
| connection _ parameter | username | root | The username of the Lindorm cluster. The username that is used for authentication when you connect to LindormTSDB. Note If the user authentication feature is not enabled for LindormTSDB, you do not need to specify the username. |
|  | password | root | The password that corresponds to the username. The password that is used for authentication when you connect to LindormTSDB. Note If the user authentication feature is not enabled for LindormTSDB, you do not need to specify the password. |
|  | database | default | The database to which you want to connect. If you do not specify this parameter, you are connected to the default database by default. |
|  | lindorm.tsdb .driver.conn ect.timeout | 60 | The timeout period of connections created to the server of LindormTSDB. Unit: milliseconds. The default value is 60,000, which is equal to 60 seconds. |
|  | lindorm.tsdb .driver.socke t.timeout | 60 | The maximum interval between socket read and write operations. Unit: milliseconds. The default value is -1, which indicates that no interval is specified. |

**Important**

If a connection is idle for more than 90 seconds, the LindormTSDB server closes the connection to save resources. If you use a connection that is closed by the server, the

```
 com.aliyun.lindorm.client.shaded.org.apache.calcite.avatica.http.ConnectionDisconnectedException
```

error is reported. To resolve the issue, you can establish a new connection.

##### Tutorial: Use the Druid connection pool to

**connect to LindormTSDB**

This topic describes how to use the Druid connection pool to connect to LindormTSDB.

**Background information**

When you use Java to develop an application that stores data in LindormTSDB, we recommend that you configure the application to use the JDBC driver to connect to LindormTSDB. In this case, Connection objects are created to connect to LindormTSDB. If a new Connection object is created each time the application connects to LindormTSDB, excessive amounts of resources are occupied. To reduce the resources required for creating connections, you can use a connection pool to create and manage connections.

**Prerequisites**

Java Development Kit (JDK) 1.8 or later is installed. The endpoint used to connect to LindormTSDB is obtained. For more information, see the **View**
**endpoints** topic in **Lindorm User Guide**.

**Procedure**

The open source connection pool Alibaba Druid is used in this topic as an example. To download Alibaba Druid, visit GitHub.
1. Add the dependency of Alibaba Druid to a Maven project. Start the client, create a Maven project, and
add the following dependency to the pom.xml file: Sample code:

```xml
<dependency>
      <groupId>com.alibaba</groupId>
      <artifactId>druid</artifactId>
      <version>1.2.6</version>
    </dependency>
```

2. You can use one of the following methods to install the JDBC driver for Lindorm:
Manually install the JDBC driver Download the Lindorm-all-client JAR package to your client and install the JDBC driver. You can select the JDBC driver version that you want to install. For example, if you want to install the JDBC driver 2.1.5, download the lindorm-all-client-2.1.5.jar package. Use Maven to download the JDBC driver To integrate the JDBC driver into a Maven project, create a Maven project and add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun.lindorm</groupId>
    <artifactId>lindorm-all-client</artifactId>
    <version>2.2.1.3</version>
</dependency>
```

**Note**

Specify the version of lindorm-all-client based on your business requirements.
3. Create a DataSource object, establish a JDBC connection based on the DataSource object, and then
connect to LindormTSDB. Sample code:

```java
import com.alibaba.druid.pool.DruidDataSource; import java.sql.*; public class App {
    private DruidDataSource dataSource;
    public void setUp() {
        dataSource = new DruidDataSource();
        try {
            dataSource.setDriver(DriverManager.getDriver("jdbc:lindorm:tsdb:url=http://ld-
bp17j28j2y7pm****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242"));// Specify the endpoint of Lind ormTSDB that you obtained in the Lindorm console. dtS tUl("jdb lid tdb lhtt //ldb17j28j27
****
tdb bli
```

```java
            dataSource.setUrl("jdbc:lindorm:tsdb:url=http://ld-bp17j28j2y7pm****-proxy-tsdb-pub.li
ndorm.rds.aliyuncs.com:8242");// Specify the endpoint of LindormTSDB that you obtained from the L indorm console.
          dataSource.setValidationQuery("select 1");
          dataSource.setMaxActive(1);
          dataSource.setUsername("username");// Specify a username or use the default username.
          dataSource.setPassword("****");// Specify the password or use the default password.
          dataSource.setKeepAlive(true);
          dataSource.setMinEvictableIdleTimeMillis(80);
          dataSource.setMaxWait(10000);
          dataSource.init();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }
    public void close() {
        dataSource.close();
    }
        try (Connection conn = this.dataSource.getConnection()) {
            try (Statement stmt = conn.createStatement()) {
                ResultSet rs = stmt.executeQuery("select * from sensor");
                long count = 0;
                while (rs.next()) {
                    count++;
                }
                System.out.println("count=" + count + " ");
            } catch (RuntimeException e) {
                e.printStackTrace();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } catch (RuntimeException e) {
            System.out.println("connection failed.");
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public static void main( String[] args ) {
        App app = new App();
        app.setUp();
        app.testQuery();
        app.close();
    }
}
```

**Note**

For more information about the parameters that you can configure for the JDBC URL, see URL of the JDBC driver. The default username and password are both root.

##### Tutorial: Use the JDBC driver for Lindorm to

**connect to and use LindormTSDB**

This topic describes how to use the Java Database Connectivity (JDBC) driver for Lindorm to connect to and use LindormTSDB.

**Prerequisites**

Java Development Kit (JDK) V1.8 or later is installed. The endpoint of LindormTSDB is obtained. For more information, see the **View endpoints** topic in
**Lindorm User Guide**.

**Procedure**

1. You can use one of the following methods to install the JDBC driver for Lindorm:
Manually install the JDBC driver. Download the Lindorm-all-client JAR package to your client and install the JDBC driver. You can select the JDBC driver version that you want to install. For example, if you want to install the JDBC driver 2.1.5, download the lindorm-all-client-2.1.5.jar package. Use Maven to download the JDBC driver. To integrate the JDBC driver into a Maven project, create a Maven project and add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>com.aliyun.lindorm</groupId>
    <artifactId>lindorm-all-client</artifactId>
    <version>2.1.5</version>
</dependency>
```

**Note**

Specify the version of lindorm-all-client based on your business requirements.
2. Access LindormTSDB. The following code block shows an example:

```java
import java.sql.Connection; import java.sql.DriverManager; import java.sql.ResultSet; import java.sql.Statement; import java.sql.SQLException; class Test {
    public static void main(String[] args) {
        String url = "jdbc:lindorm:tsdb:url=http://<host:port>";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url);
            Statement stmt = conn.createStatement();
            //Create a time series table. By default, the time series table is created in the dat
abase named default.
            stmt.execute("CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR TAG,time TIMES
TAMP,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))");
            // Insert a single row.
            //stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:00',12.1,45)");
            //stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:10',13.2,47)");
            //stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:20',10.6,46)");
            //stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity)
```

l

```
('F07A1261''
```

`th`

```
''20210422153300'18144)")
```

```java
values('F07A1261','south-cn','2021-04-22 15:33:00',18.1,44)");
            //stmt.execute("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1261','south-cn','2021-04-22 15:33:10',19.7,44)");
            //Insert multiple rows in a batch.
            stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:00',12.1,45)");
            stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:10',13.2,47)");
            stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1260','north-cn','2021-04-22 15:33:20',10.6,46)");
            stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1261','south-cn','2021-04-22 15:33:00',18.1,44)");
            stmt.addBatch("INSERT INTO sensor(device_id, region, time, temperature, humidity)
values('F07A1261','south-cn','2021-04-22 15:33:10',19.7,44)");
            stmt.executeBatch();
            stmt.clearBatch();
            // Query data. We recommend that you specify a time range to reduce the scope of data
that is scanned.
            ResultSet rs = stmt.executeQuery("select device_id, region,time,temperature,humidity
from sensor where time >= '2021-04-22 15:33:00' and time <= '2021-04-22 15:33:20'");
            while (rs.next()) {
                String device_id = rs.getString("device_id");
                String region = rs.getString("region");
                Long time = rs.getLong("time");
                Double temperature = rs.getDouble("temperature");
                Long humidity = rs.getLong("humidity");
                System.out.printf("%s %s %d %f %d\n", device_id, region, time, temperature, humidi
ty);
            }
        } catch (SQLException e) {
            // Handle exceptions based on the business logic of your application.
            e.printStackTrace();
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

**Note**

For more information about the parameters that you can configure for the JDBC URL, see URL of the JDBC driver. For more information about the API operations and methods that are supported when you use the JDBC driver to access LindormTSDB, see Supported API operations and methods. For more information about the SQL syntax supported by LindormTSDB, see SQL syntax reference.

#### HTTP-based SQL API

This topic describes the definition of the HTTP-based SQL API provided by LindormTSDB and how to use the API.

| Request path | Method | Description |
|---|---|---|
| /api/v2/sql | POST | Send and execute an SQL statement. |

**Usage notes**

For applications that are not developed by using Java, you can directly use the API described in this topic to send SQL statements to LindormTSDB. For Java applications, we recommend that you use the Java Database Connectivity (JDBC) driver to connect your applications to LindormTSDB. For more information, see Java JDBC driver.

**Note**

Single-node Lindorm instances do not support the HTTP-based SQL API.

**Request path and method**

**Request content**

When you call the preceding API, include an SQL statement in the request body of the HTTP request. We recommend that you set `Content-Type` to `text/plain` in the request header. The following Python code provides an example on how to call the `/api/v2/sql` API to send an SQL statement:

```java
import requests url = "http://ld-xxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/v2/sql" payload = """insert into sensor (device_id, region, time, temperature, humidity) values ('F07A1260','north-cn','2021-04-22 15:33:00',12.1,45), ('F07A1260','north-cn','2021-04-22 15:33:10',13.2,47), ('F07A1260','north-cn','2021-04-22 15:33:20',10.6,46), ('F07A1261','south-cn','2021-04-22 15:33:00',18.1,44), ('F07A1261','south-cn','2021-04-22 15:33:10',19.7,44)""" r = requests.post(url, payload) if r.status_code == 200:
    print(r.content)
else:
    print(r.content)
r = requests.post(url, payload) if r.status_code == 200:
    print(r.content)
else:
    print(r.content)
```

**Note**

LindormTSDB allows you to use semicolons (;) as the terminator of SQL statements based on the SQL- 92 standard. However, when you call the `/api/v2/sql` API to pass an SQL statement, semicolons (;) cannot be used as the terminator of the SQL statement. Otherwise, the request throws an error. The following table describes the URL query parameters that are supported by the /api/v2/sql API.

| Parameter | Description |
|---|---|
| database | The default database on which the SQL statement is executed. You can pass an SQL statement into an SQL API request to write data to a time series table or query data in a time series table. If the database to which the time series table belongs is not specified in the SQL statement, LindormTSDB searches for the specified table in the database that is specified by the database parameter. If you do not specify the database parameter, LindormTSDB searches for the specified table in the database named default . |
| chunked | Specify whether to return the results in chunks. Default value: false. If this parameter is set to true, the query result is divided into multiple JSON blocks and then returned. Each JSON block contains a maximum of N rows of data. N is specified by the chunk size parameter. When your application _ receives the query results, it needs to only parse the JSON blocks one by one. For more information about the structure of each JSON block, see the "Response parameters" section of this topic. |
| chunk size _ | The maximum number of rows to return at a time. This parameter takes effect when the chunked parameter is set to true. Default value: 1000. |

| API uses the | BASIC AUTH |  |
|---|---|---|
| Authorization |  | field of t |

| Parameter | Type | Description |
|---|---|---|

**Specify user credentials for authentication**

If user authentication is enabled for LindormTSDB, you must include the authentication information of the user in the HTTP request headers when you use the `/api/v2/sql` API to send SQL statements. The You can specify user credentials in the following format for basic authentication:

```
BASIC {Base64-encoded authentication information}
```

The **Base64-encoded authentication information** is in the following format: ${username}:${password} . The username and password are separated by a colon (:).

**Note**

For more information about how to encode and specify user credentials for basic authentication by using different programming languages, see the documentation for relevant class libraries of the programming languages. For example, if you use the default username and password (which are both root) as the credential for basic authentication, the Base64-encoded value of the **Authorization** field in the HTTP header is Basic cm9vdDpyb290, as shown in the following example:

```
Authorization: Basic cm9vdDpyb290
```

If a request is successful, the HTTP status code in the response is 200 and the response content is returned in JSON format. The following table describes the response parameters.

| columns | Array | An array of strings. It indicates the name of each column in the returned result set. |
|---|---|---|
| metadata | Array | An array of strings. It indicates the data type of each column in the returned result set. For more information about the types of returned data, see Data types. |
| rows | Array | An array of arrays. It indicates a collection of rows in the returned result set. Each array indicates a row of data, and the specific values in each row correspond to the columns that are indicated by the columns parameter. |

| Parameter | Type | Description |
|---|---|---|
| code | int | The returned error code. |
| sqlstate | String | The returned SQL status code. |
| message | String | The returned error message. |

If an SQL execution error occurs, the HTTP status code in the response is 400, and the response content is returned in JSON format. The following table describes the parameters.

**Note**

For more information about the error codes, see Common error codes. The following examples show how to call the /api/v2/sql API to execute SQL statements in LindormTSDB. In these examples, curl is used. Create a database named DB1.

```bash
curl -X POST http://ld-xxxxxxxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/v2/sql -d 'CREA TE DATABASE DB1'
```

Create a time series table named SENSOR in DB1. You can execute one of the following two statements to create the table:

```bash
curl -X POST http://ld-xxxxxxxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/v2/sql?database =DB1 -d 'CREATE TABLE SENSOR (device_id VARCHAR TAG,region VARCHAR TAG,time TIMESTAMP,temperature DOUBLE,humidity DOUBLE)'
```

You can also execute the following statement to create the table:

```bash
curl -X POST http://ld-xxxxxxxxx-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/v2/sql -d 'CREA TE TABLE DB1.SENSOR (device_id VARCHAR TAG,region VARCHAR TAG,time TIMESTAMP,temperature DOUBLE,h umidity DOUBLE)'
```

If user authentication is enabled, use an account whose username is `tsdbuser` to query data in the
**SENSOR** time series table.

| Data type | Description |
|---|---|
| Float | Floating-point numbers. Float is the default data type. Example: 1, 1.0, 1.e+10, and 1.E+10. |
| Integer | 64-bit integers. You must append a letter i to the end of a number to specify that the number is an integer. Example: 12i and 101i. |
| String | Strings. Strings must be enclosed in double quotation marks ("). Example: "hello world". |
| Boolean | Boolean values. Valid values: True and False. The value of True supports the following formats: t, T, true, True, and TRUE. The value of False supports the following formats: f, F, false, False, and FALSE. |
| Timestamp | Timestamps. The InfluxDB line protocol supports timestamps in nanoseconds. However, timestamps are converted to milliseconds when they are stored in LindormTSDB. If you want to change the precision of timestamps, specify the precision parameter. |

| Parameter | Required | Description |
|---|---|---|

```bash
curl -X POST -u tsdbuser:password http://ld-xxxxxxxxx-proxy-tsdbpub.lindorm.rds.aliyuncs.com:8242/api/v2/sql?database=DB1 -d 'SELECT device_id, region, time, MAX (temperature) as max_t FROM SENSOR WHERE time >= 1619076780000 AND time <= 1619076800000 SAMPLE B Y 20s'
```

**Note**

Make sure that tsdbuser is granted the required permissions on the SENSOR time series table.

#### Use the InfluxDB® line protocol to write data

This topic describes how to write data to LindormTSDB by using the InfluxDB line protocol and provides examples.

**Background information**

LindormTSDB is compatible with the format defined by the InfluxDB line protocol. For more information, see Line Protocol. You can use applications or devices that support the InfluxDB line protocol to write data to LindormTSDB. The syntax of the InfluxDB line protocol supports the following data types: Float, Integer, String, Boolean, and Timestamp. The following table describes the data types supported by the InfluxDB line protocol.

**Request path**

Request path: /api/v2/write When you create a request to write data points to LindormTSDB by using the InfluxDB line protocol, you must change the format of the data points to the format defined by the InfluxDB line protocol and then use the data points as the body of the POST request. The following table describes the parameters that you can configure in a request.

| precision | No | The precision of timestamps. Default value: ns. Valid values: ns, us, ms, s, m, and h. |
|---|---|---|
| db | No | The name of the database to which you want to write data points. |
| schema policy _ | No | The constraint policy for the scheme. The default value of this parameter is WEAK. If you specify a weak constraint policy, time series tables can be automatically created. Valid values: WEAK: Specify a weak constraint policy for the scheme. STRONG: Specify a strong constraint policy for the schema. For more information, see Constraint policies for schemas. |

| Parameter | Required | Description |
|---|---|---|
| table name _ | Yes | The name of the table to which you want to write data points. |
| tag set _ | No | The tags of the data point that you want to write. The tags can be used to search data points. |
| field set _ | Yes | The field of the data point that you want to write. |
| timestamp | No | The timestamp of the data point that you want to write. By default, the current time is specified. Default unit: nanoseconds. Note If you want to change the precision of timestamps, specify the precision parameter. |

**Data format of the InfluxDB line protocol**

You can use the InfluxDB line protocol to write data to LindormTSDB in the following format:

```xml
<table_name>[,<tag_key>=<tag_value>[,<tag_key>=<tag_value>]] <field_key>=<field_value>[,<field_key> =<field_value>] [<timestamp>]
```

**Note**

Separate multiple data points with line feeds (\n). When you use the InfluxDB line protocol to write data points to LindormTSDB, the schema constraints used by the engine are weak constraints. The following sample code shows how to write data by using InfluxDB line protocol:

```
POST /api/v2/write?precision=ms&db=default sensor,device_id=F07A1260,region=north-cn temperature=12.1,humidity=45 1619076780000 sensor,device_id=F07A1260,region=north-cn temperature=13.2,humidity=47 1619076790000 sensor,device_id=F07A1260,region=north-cn temperature=10.6,humidity=46 1619076800000 sensor,device_id=F07A1260,region=north-cn temperature=18.1,humidity=44 1619076780000 sensor,device_id=F07A1260,region=north-cn temperature=19.7,humidity=44 1619076790000
```

If the request is successful, the status code 204 is returned.

### Data importing

#### Use DataWorks to import data

This topic describes how to use the data integration feature provided by DataWorks to migrate data from other services to LindormTSDB.

**Prerequisites**

The endpoint of LindormTSDB for HTTP is obtained. For more information, see View endpoints. A workspace is created on the DataWorks console. For more information, see Create a workspace.

**Procedure**

**Configure a whitelist**

To use a shared resource group, you must add the IP addresses of the resource group to the whitelist of the Lindorm instance. i. Obtain the CIDR blocks of the severs in the region where the DataWorks workspace resides. For more information, see Configure an IP address whitelist. ii. Add the obtained CIDR blocks to the whitelist of the Lindorm instance. For more information, see Configure whitelists. If you use a custom resource group that you create, add the IP addresses corresponding to the resource group to the whitelist of the Lindorm instance. For more information, see Configure whitelists.

**Create a batch synchronization node**

1. Go to the DataStudio page in the DataWorks console. For more information, see Go to the DataStudio
page.
2. Create a batch synchronization node. For more information, see Step 1: Create a batch synchronization
task.
3. Configure the data source of the synchronization node. For example, you can select **Stream** for **Source**
and **TSDB** for **Destination**. Then, select a resource group schema for **Recommended Resource**
**Groups** based on your requirements.
4. Click **Next**.

**Configure the batch synchronization node**

1. Compile code in the code editor to configure the batch synchronization node.

```json
{
    "type": "job",
    "version": "2.0",
    "steps": [
        {
            "stepType": "stream",
            "parameter":{
                "column":[
                    {
                        "type":"string",
                        "value":"tag1"
                    },
                    {
                        "type":"string",
                        "value":"tag2"
                    },
                    {
                        "type":"string",
                        "value":"field1"
                    },
                    {
```

```json
{
                        "type":"double",
                        "value":10.0
                    },
                    {
                        "type":"long",
                        "value":100
                    },
                    {
                        "type":"bool",
                        "value":true
                    }
```

`],`

```json
                "sliceRecordCount":"100000"
            },
            "name": "Reader",
            "category": "reader"
        },
        {
            "stepType": "tsdb",
            "parameter": {
                "endpoint": "http://ld-bp12pc23yfb3*****-proxy-tsdb-
pub.lindorm.rds.aliyuncs.com:8242",
                "sourceDbType": "RDB",
                "batchSize": 256,
                "columnType": [
                    "tag",
                    "tag",
                    "field_string",
                    "field_double",
                    "timestamp",
                    "field_bool"
```

`],`

```json
                "column": [
                    "tag1",
                    "tag2",
                    "field1",
                    "field2",
                    "timestamp",
                    "field3"
```

`],`

```json
                "multiField":"true",
                "table":"testmetric",
                "username":"testuser",
                "password":"password",
                "ignoreWriteError":"false",
                "database":"default"
            },
            "name": "Writer",
            "category": "writer"
        },
        {
            "name": "Processor",
            "stepType": null,
            "category": "processor",
            "parameter": {}
        }
```

`],`

```json
    "setting": {
        "executeMode": null,
        "errorLimit": {
            "record": ""
```

| Paramete r | Required | Type | Default value | Description |
|---|---|---|---|---|
| column | Yes | STRING | No default value. | The names of the columns that you want to synchronize. |

| Paramete r | Required | Type | Default value | Description |
|---|---|---|---|---|
| endpoint | Yes | STRIN G | No default value. | The endpoint of LindormTSDB for HTTP. For more information about how to obtain the endpoint, see View endpoints. |
| sourceDbT ype | No | STRIN G | TSDB | The type of the data source. Valid values: TSDB and RDB. |
| batchSize | No | INT | 100 | The number of data records that you want to add in the batch synchronization node. The value of this parameter must be larger than 0. |
| multiField | Yes | BOOL | false | Specifies whether to use the HTTP API to write multi- value data. Valid values: true: Use the HTTP API to write multi-value data. false: Use the HTTP API to write single-value data. |
| columnTyp e | Required when RDB is selected for sourceDbTyp e | STRIN G | No default value. | The data types of the columns in the database in LindormTSDB after the columns are synchronized. The following data types are supported: timestamp: a timestamp column. tag: a tag column. metric num: a metric column whose value is of a _ numeric data type. metric string: a metric column whose value is of a _ string data type. |

```json
        },
        "speed": {
            "concurrent": 2,
            "throttle": false
        }
    },
    "order": {
        "hops": [
            {
                "from": "Reader",
                "to": "Writer"
            }
```

]

```
    }
}
```

**Reader parameters**

**Writer parameters**

| column | Required when RDB is selected for sourceDbTyp e | STRIN G | No default value. | The names of the columns that you want to synchronize. |
|---|---|---|---|---|
| username | No | STRIN G | No default value. | The name of the database account that is used to connect to the database. |
| password | No | STRIN G | No default value. | The password of the database account that is used to connect to the database. |
| ignoreWrit eError | No | BOOL | false | Specifies whether to ignore data writing errors. Valid values: true: Ignore data writing errors and continue to write data. false: Stop writing data when errors occur during data writing. |
| database | No | STRIN G | default | The name of the TSDB database to which you want to synchronize data. |

2. Configure scheduling properties for the batch synchronization node. For more information, see Step 5:
Configure scheduling properties for the batch synchronization task.

**Synchronize data**

Click the icon to run the batch synchronization node, check the configurations, and submit the node. For more information, see Deploy nodes.

#### Use DataX to migrate data from relational

**databases to LindormTSDB**

This topic describes how to use DataX to migrate data from a relational database to LindormTSDB. DataX is an open source tool provided by Alibaba Group.

**Background information**

DataX is an offline data synchronization tool that is widely used within Alibaba Group. You can use DataX to efficiently synchronize data between various disparate data sources, including MySQL, Oracle, SQL Server, PostgreSQL, Hadoop Distributed File System (HDFS), Hive, AnalyticDB for MySQL, HBase, Tablestore (OTS), MaxCompute, and PolarDB-X. MaxCompute is previously known as Open Data Processing Service (ODPS). For more information about how to use DataX, see README. The following sections describe DataX and provide an example on how to migrate data from a relational database to a database in LindormTSDB. A MySQL database is used in the example. MySQL Reader and TSDB Writer are used to perform data migration.

**MySQL Reader**

MySQL Reader is a plug-in that is powered by DataX. You can use MySQL Reader to query data from a MySQL database.

**TSDB Writer**

DataX provides the TSDB Writer plug-in that is used to write data to a database in LindormTSDB.

**Precautions**

**Make sure that DataX can access LindormTSDB.**

TSDB Writer calls the HTTP endpoint `/api/mput` and the HTTP endpoint `/api/put` to write data. If you want to migrate data, make sure that each process of the migration task can access the HTTP endpoint provided by LindormTSDB. Otherwise, a connection exception is thrown.

**Make sure that your MySQL database can be accessed by each process of the migration task.**

MySQL Reader uses Java Database Connectivity (JDBC) to read data. If you need to migrate data, make sure that each process of the migration task can access the JDBC API that is provided by your MySQL database. Otherwise, a connection exception is thrown.

**Preparations**

1. Configure an environment.
Linux Java Development Kit (JDK): Use JDK 1.8 or later. Python: We recommend that you use Python 2.6.x. MySQL: DataX is compatible only with MySQL 5.x. LindormTSDB: Activate LindormTSDB.
2. Download DataX and the plug-ins.
Click here to download the corresponding TAR file.
3. Use the built-in script provided by DataX to test whether data can be migrated as expected.
The plug-ins used in the test are Stream Reader and Stream Writer. Stream Reader and Stream Writer do not require external dependencies. Therefore, Stream Reader and Stream Writer are suitable for tests. Stream Reader and Stream Writer are used to simulate a simple data migration process. Stream Reader generates random character strings. Stream Writer receives the strings and displays them in your CLI.

**Install DataX**

Decompress the installation package to DATAX_HOME. Then, run the following command to start a migration testing task:

```bash
$ cd ${DATAX_HOME} $ python bin/datax.py job/job.json
```

**Check the migration result**

The following example shows the summary information that is returned if the data is migrated as expected:

```
Task start time : 2019-04-26 11:18:07 Task end time : 2019-04-26 11:18:17 Execution time : 10s Average traffic : 253.91KB/s Write rate : 10000rec/s Records obtained : 100000 Number of write and read failures : 0
```

**Configure and run a task that migrates data from a MySQL database to**

In the preceding step, data can be migrated as expected when Stream Reader and Stream Writer are used. The migration result indicates that you can use DataX to migrate data. In this case, you can use MySQL Reader and TSDB Writer to migrate data from your MySQL database to a database in LindormTSDB.

**Parameters**

The following tables describe the parameters that you can configure.

**MySQL Reader parameters**

| Parameter | Type | Required | Description |  | Default value |  | Example |  |  |
|---|---|---|---|---|---|---|---|---|---|
| jdbcUrl | String | Yes | Specifies the database URL that is used by JDBC to connect to the MySQL database. |  | None |  | jdbc:mysql:/ |  |  |
|  |  |  |  |  |  |  |  | jdbc:mysql:/ |  |
|  |  |  |  |  |  | e | /127.0.0.1:330 |  |  |
|  |  |  |  | connect ySQL |  |  |  |  |  |
|  |  |  |  |  |  |  | 6/datax |  |  |
| username | String | Yes | Specifies the username that is used to connect to the MySQL database. |  | None |  | root |  |  |
| password | String | Yes | Specifies the password that is used to connect to the MySQL database. |  | None |  | root |  |  |
| table | String | Yes | Specifies the table that contains the data that you want to migrate. |  | None |  | book |  |  |
| column | Array | Yes | Specifies the names of the columns that you want to migrate. |  | [] |  | ["m"] |  |  |
| splitPk | String | No | Specifies the shard key that is used for table sharding. If you specify a value for splitPk, the table is sharded based on the specified value. |  | None |  | id |  |  |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|

**TSDB Writer parameters**

| sourceDbType | String | No | Valid values: TSDB and RDB. The value of TSDB specifies a time series engine, such as OpenTSDB, InfluxDB, Prometheus, or TimeScale. The value of RDB specifies a relational database engine, such as MySQL, Oracle, PostgreSQL, or PolarDB-X. |  | TSDB |  |  |  | RDB |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| column | Array | Yes | Specifies the names of the columns that you want to migrate. |  | [] |  |  |  | ["name","typ |  |  |
|  |  |  |  |  |  |  |  |  |  | ["name","typ |  |
|  |  |  |  |  |  | [] |  |  | e","create tim _ |  |  |
|  |  |  |  | t to . |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | e","price"] |  |  |

| columnType | Array | Yes | Specifies the data types of the columns in the database in LindormTSDB after the columns are migrated. Valid values: timestamp, tag, metric num, _ and metric string. _ The value timestamp specifies that the column contains timestamps. The value tag specifies that the column contains tags. The value metric num _ specifies that the column contains data of a numeric data type. The value metric string _ specifies that the column contains data of a string data type. |  | [] |  |  |  | ["tag","tag" |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | ["tag","tag" |  |
|  |  |  |  |  |  | [] |  |  | ,"timestamp"," |  |  |
|  |  |  |  | mn |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | metric num"] _ |  |  |
| endpoint | String | Yes | Specifies the endpoint of LindormTSDB. Specify the value in the IP:PORT format. |  | None |  |  |  | ld- xxxx:8242 |  |  |

|  |  | ld- |
|---|---|---|
|  | xxxx:8242 |  |

| multiField | Bool | Yes | Specifies whether to perform your data write operation by calling the /api/mput HTTP endpoint. We recommend that you set the value to true. | false | true |
|---|---|---|---|---|---|
| table | String | Yes | Specifies the table that you want to migrate to the database in LindormTSDB. | None | table |
| username | String | No | Specifies the username that is used to connect to the database in LindormTSDB. | None | tsdbuser |
| password | String | No | Specifies the password that is used to connect to the database in LindormTSDB. | None | tsdbpsw |
| ignoreWriteErro r | Bool | Yes | Specifies whether to ignore write failures. | false | true |
| database | String | No | Specifies the name of the database to which you want to write the data. | default | default |

**Configure a data migration task**

Configure a task to migrate data from the MySQL database to the database in LindormTSDB. In this example, the task name is `mysql2tsdb.json` . The following code provides an example on how to configure a data migration task. For more information about the parameters, see Parameters.

```json
{
  "job": {
    "content": [
      {
        "reader": {
          "name": "mysqlreader",
          "parameter": {
            "column": [
              "name",
              "type",
```

`yp` ,

```
              "create_time",
              "price",
              "description",
              "available"
```

`],`

```json
            "connection": [
              {
                "jdbcUrl": [
                  "jdbc:mysql://127.0.0.1:3306/datax"
```

`],`

```json
                "table": [
                  "book"
```

]

```
              }
```

`],`

```json
            "password": "xxx",
            "splitPk": "id",
            "username": "root"
          }
        },
        "writer": {
          "name": "tsdbwriter",
          "parameter": {
            "column": [
              "name",
              "type",
              "create_time",
              "price",
              "description",
              "available"
```

`],`

```json
            "columnType": [
              "tag",
              "tag",
              "timestamp",
              "field_double",
              "field_string",
              "field_bool"
```

`],`

```json
            "sourceDbType": "RDB",
            "endpoint": "http://localhost:8242",
            "table": "my_book",
            "multiField": "true",
            "username":"xxx",
            "password":"xxx",
            "ignoreWriteError":"false",
            "database":"default"
          }
        }
      }
```

`],`

```json
    "setting": {
      "speed": {
        "channel": 1
      }
    }
  }
}
```

**Consistent column name sequences**

Make sure that the sequence of the column names configured in TSDB Writer is the same as that of the column names configured in MySQL Reader. Otherwise, data cannot be processed as expected.

**Start the task**

```bash
$ cd ${DATAX_HOME}/.. $ ls
  datax/  datax.tar.gz  mysql2tsdb.json
$ python datax/bin/datax.py mysql2tsdb.json
```

**Check the migration result**

The following example shows the summary information that is returned if the data is migrated as expected:

```
Task start time : 2019-05-21 18:25:16 Task end time : 2019-05-21 18:25:27 Execution time : 11s Average traffic : 3B/s Write rate : 0rec/s Records obtained : 3 Number of write and read failures : 0
```

**FAQ**

**Can I change the Java Virtual Machine (JVM) memory size for a migration process?**

Yes, you can change the JVM memory size for a migration process. If you want to adjust the JVM memory size for a task that migrates data from a MySQL database to a database in LindormTSDB, you can run the following command:

```
python datax/bin/datax.py mysql2tsdb.json -j "-Xms4096m -Xmx4096m"
```

**How do I configure an IP address whitelist for LindormTSDB?**

For more information, see Configure whitelists.

**If my migration task runs on an Elastic Compute Service (ECS) instance, how do I configure a**

**virtual private cloud (VPC) and what are the common issues?**

For more information, see Use cases of ECS security groups and FAQ about VPCs.

#### Use DataX to import data from Prometheus

This topic describes how to use DataX to migrate data from Prometheus Service (Prometheus) to LindormTSDB. DataX is an open source tool that is provided by Alibaba Cloud.

**Background information**

For information about how to use DataX, see README. Two plug-ins are required to migrate data from Prometheus to LindormTSDB: Prometheus Reader and TSDB Writer. DataX is an offline data synchronization tool that is widely used within Alibaba Group. You can use DataX to efficiently synchronize data between various disparate data sources, including MySQL, Oracle, SQL Server, PostgreSQL, Hadoop Distributed File System (HDFS), Hive, AnalyticDB, HBase, Tablestore, MaxCompute, and PolarDB-X. MaxCompute is previously known as Open Data Processing Service (ODPS), and PolarDB-X is previously known as Distributed Relational Database Service (DRDS).

**Prometheus Reader**

The Prometheus Reader plug-in is provided by DataX. You can use this plug-in to read data from Prometheus.

**TSDB Writer**

The TSDB Writer plug-in is provided by DataX. You can use this plug-in to write data to LindormTSDB.

**Quick start**

**Step 1: Configure an environment**

Linux Java Development Kit (JDK): You can use JDK 1.8 or later. We recommend that you use JDK 1.8. Python: We recommend that you use Python 2.6.x. Prometheus: Only Prometheus versions 2.9.x are supported. If you use other versions, compatibility issues may occur. LindormTSDB: Only V2.4.x and later are supported. If you use other versions, compatibility issues may occur.

**Step 2: Download DataX and the related plug-ins**

Download DataX and the Prometheus Reader and TSDB Writer plug-ins.

**Step 3: Use the built-in script that is provided by DataX to test whether data can be migrated**

**as expected**

The plug-ins Stream Reader and Stream Writer are used in the test. These plug-ins do not require external dependencies. Stream Reader and Stream Writer are used to simulate a simple data migration process. Stream Reader generates random character strings. Stream Writer receives the strings and prints them on your CLI.

**Install DataX**

Decompress the installation package to a specified directory and then run the datax.py script to start the migration task.

```bash
$ cd ${DATAX_HOME} $ python bin/datax.py job/job.json
```

**Check the migration result**

If the following information is returned, the data is migrated as expected:

```
Task start time : 2019-04-26 11:18:07 Task end time : 2019-04-26 11:18:17 Execution time : 10s Average traffic : 253.91KB/s Write rate : 10000rec/s Number of records obtained : 100000 Number of write and read failures : 0
```

For more information about the sample code, watch the following video: Quick start to migrate data.

**Step 4: Configure a task to migrate data from Prometheus to LindormTSDB**

After the test performed in Step 3 confirms that DataX can be used to migrate data, you can use the Prometheus Reader and TSDB Writer plug-ins to migrate data from Prometheus to LindormTSDB.

**Configure a migration task**

Configure a task to migrate data from Prometheus to LindormTSDB. In this example, the task name is `prometheus2tsdb.json` . The following sample code provides an example of the task configuration. For more information about the parameters, see the "Parameters" section.

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|

```json
{
  "job": {
    "content": [
      {
        "reader": {
          "name": "prometheusreader",
          "parameter": {
            "endpoint": "http://localhost:9090",
            "column": [
              "up"
```

`],`

```json
            "beginDateTime": "2019-05-20T16:00:00Z",
            "endDateTime": "2019-05-20T16:00:10Z"
          }
        },
        "writer": {
          "name": "tsdbhttpwriter",
          "parameter": {
          }
        }
      }
```

`],`

```json
    "setting": {
      "speed": {
        "channel": 1
      }
    }
  }
}
```

**Start the migration task**

```bash
$ cd ${DATAX_HOME}/.. $ ls
  datax/  datax.tar.gz  prometheus2tsdb.json
$ python datax/bin/datax.py prometheus2tsdb.json
```

**Check the migration result**

If the following information is returned, the data is migrated as expected:

```
Task start time : 2019-05-20 20:22:39 Task end time : 2019-05-20 20:22:50 Execution time : 10s Average traffic : 122.07KB/s Write rate : 1000rec/s Number of records obtained : 10000 Number of write and read failures : 0
```

For more information about how to migrate data from Prometheus to a TSDB database, watch the following video: Migrate data from Prometheus to a TSDB database.

**Parameters**

The following tables describe the parameters that you can configure.

**Prometheus Reader parameters**

| endpoint | String | Yes | The HTTP endpoint of Prometheus. | None |  | http://127.0 .0.1:9090 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | http://127.0 |  |
|  |  |  |  |  | e | .0.1:9090 |  |  |
| column | Array | Yes | The columns of data that you want to migrate. | [] |  | ["m"] |  |  |
| beginDateTime | String | Yes | This parameter is used together with the endDateTime parameter to specify a time range. The data that is generated within this time range is migrated. | None |  | 2019-05-13 15:00:00 |  |  |
| endDateTime | String | Yes | This parameter is used together with the beginDateTime parameter to specify a time range. The data that is generated within this time range is migrated. | None |  | 2019-05-13 17:00:00 |  |  |

|  |  | 2019-05-13 |  |
|---|---|---|---|
|  | 15:00:00 |  |  |

|  |  | 2019-05-13 |  |
|---|---|---|---|
|  | 17:00:00 |  |  |

| Parameter | Type | Required | Description | Default value |  | Example |  |  |
|---|---|---|---|---|---|---|---|---|
| endpoint | String | Yes | The HTTP endpoint of LindormTSDB. | None |  | http://127.0 .0.1:8242 |  |  |
|  |  |  |  |  |  |  | http://127.0 |  |
|  |  |  |  |  | e | .0.1:8242 |  |  |
| batchSize | Integer | No | The number of data records that you want to migrate at a time. The value must be an integer greater than 0. | 100 |  | 100 |  |  |
| maxRetryTime | Integer | No | The maximum number of retries that are allowed after a migration failure occurs. The value must be an integer greater than 1. | 3 |  | 3 |  |  |

**TSDB Writer parameters**

| ignoreWriteErro r | Boolean | No | Specifies whether to ignore write errors after the maximum number of retries is reached. If the ignoreWriteErro r parameter is set to true, the system ignores write errors and continues to write data. If the ignoreWriteErro r parameter is set to false, the data writing task is terminated after the maximum number of retries is reached. | false | false |
|---|---|---|---|---|---|

**Usage notes**

**Make sure that DataX can connect to LindormTSDB.**

TSDB Writer writes data by calling the `/api/put` operation. To ensure successful data migration, make sure that each process of the migration task can access the HTTP API that is provided by LindormTSDB. Otherwise, a connection exception is reported.

**Make sure that DataX can connect to Prometheus.**

Prometheus Reader reads data by calling the `/api/v1/query_range` operation. To ensure successful data migration, make sure that each process of the migration task can access the HTTP API that is provided by Prometheus. Otherwise, a connection exception is reported.

**FAQ**

**Can I change the Java Virtual Machine (JVM) memory size for a migration process?**

Yes, you can adjust the JVM memory size for a migration process. If you want to adjust the JVM memory size for a task that migrates data from Prometheus to LindormTSDB, run the following command:

```
python datax/bin/datax.py prometheus2tsdb.json -j "-Xms4096m -Xmx4096m"
```

**How do I configure an IP address whitelist for a Lindorm instance that runs LindormTSDB?**

For more information about how to configure an IP address whitelist for a Lindorm instance that runs LindormTSDB, see Configure a whitelist for a TSDB instance.

**If my migration task runs on an Elastic Compute Service (ECS) instance, how do I configure a**

**virtual private cloud (VPC) and what are the common issues that can occur?**

For more information, see Configure security groups in different scenarios and FAQ.

### Developer Guide

#### Overview of application development

This topic describes how to develop applications that use Lindorm Time Series Database (LindormTSDB) to store data.

**Procedure**

In general, you can perform the following steps to develop an application that uses LindormTSDB. Lindorm allows you to use a variety of SQL-based methods to develop applications that need to access LindormTSDB. If you use Java to develop applications, you can use LindormTSDB SDK for Java or the JDBC driver for Lindorm. For more information, see Java Native SDK and Java JDBC Driver. We recommend that you use **LindormTSDB SDK for Java** to develop your applications. LindormTSDB SDK for Java allows your applications to access LindormTSDB in an efficient and easy-to-use method and provides various features such as underlying connection management, batch data writing, and error retry mechanism. In addition, the encoding in data transmission is optimized in LindormTSDB SDK for Java for higher data writing efficiency. If you use other programming languages to develop applications, you can use the HTTP-based SQL API of LindormTSDB and the InfluxDB line protocol. For more information, see Use the HTTP-based SQL API of LindormTSDB and Write data by using the InfluxDB line protocol. We recommend that you use the **InfluxDB line protocol** to write data to LindormTSDB and use the
**HTTP-based SQL API of LindormTSDB** to query data.
Before you create a time series data and table, you must create data models based on your business to determine the tag, time, and value columns in the table. Then, you must determine the primary key of the time series table based on data characteristics and distribute data into different shards. For more information, see Data models. LindormTSDB provides three types of schema constraint policies: strong constraint, weak constraint, and no constraint. You can select a policy based on your requirements. For more information, see Constraints on the schemas of time series models. You can use multiple methods to write data to Lindorm, such as LindormTSDB SDK for Java, the InfluxDB line protocol, or standard SQL statements. LindormTSDB provides three types of schema constraint policies: strong constraint, weak constraint, and no constraint. If you use LindormTSDB SDK for Java, the InfluxDB line protocol, or API operations that are compatible to Time Series Database (TSDB) to write data to LindormTSDB, you can set the schema constraint policy to weak constraint. In this case, LindormTSDB automatically creates tables in schemaless scenarios. Select a method to write data based on your requirements. LindormTSDB allows you to access time series data by using standard SQL statements. In addition, LindormTSDB optimizes the SQL syntax for time series data and supports features that are specific to time series data, such as data downsampling, data aggregation, and latest value queries. Continuous queries are applicable to big data scenarios. You can create a continuous query to preaggregate data that is newly written. This way, the amount of data that is queried in real time is reduced and the query latency is decreased. Pre-downsampling is applicable to query data within a long time range. Data is downsampled based on the specified rules when it is written to LindormTSDB. When the downsampled data is queried, the amount of data that is queried is reduced to decrease query latency.

**Procedure for the development of applications that use OpenTSDB or**

**TSDB to store data**

LindormTSDB is compatible with the API operations of OpenTSDB and TSDB. You can perform the following steps to migrate the database engine used by your application from OpenTSDB or TSDB to LindormTSDB: i. Change the endpoint of OpenTSDB or TSDB to the endpoint of LindormTSDB in the application code. For more information about how to obtain the endpoint of LindormTSDB, see Obtain the endpoint. ii. Modify the application based on the capabilities of LindormTSDB. Applications developed based on HTTP-based API operations: The HTTP-based API operations provided by LindormTSDB are basically compatible with the API operations provided by TSDB. For more information, see HTTP API overview. Java applications developed by using SDKs for TSDB: LindormTSDB is compatible with 90% of the capabilities provided by TSDB. You can directly use your application to access LindormTSDB without modification. Applications that use multi-value models to write data: By default, data is written to the database named default in LindormTSDB. The default schema constraint policy in LindormTSDB is no constraint, which indicates that time series tables are not automatically created in LindormTSDB. To use SQL statements to query data in LindormTSDB, you can manually create time series tables or set the schema constraint policy to weak constraint. LindormTSDB provides SQL-based features that are specific to time series data and optimizes the performance of SQL queries for time series data. We recommend that you use SQL statements to query data in LindormTSDB. Applications that use OpenTSDB or single-value models to write data: The default schema constraint policy in LindormTSDB is no constraint, which indicates that time series tables cannot be automatically created in LindormTSDB. Therefore, these applications cannot use SQL statements to query data in LindormTSDB. iii. Connect the application to LindormTSDB to perform debugging and testing and then release the application after the application passes all tests.
2. Migrate application data
Data in TSDB can be fully migrated to LindormTSDB. For more information, see Migrate all data from TSDB to LindormTSDB.

**Procedure for the development of applications that use Prometheus**

LindormTSDB supports the remote write and remote read interfaces for remote storage and supports the native PromQL syntaxes for queries. For more information, see Use Prometheus to connect to and use LindormTSDB.

**Procedure for the development of applications that use InfluxDB**

You can use the InfluxDB line protocol to write data to LindormTSDB. For more information, see Line protocol reference.

#### Create data models

This topic describes how to use LindormTSDB to create data models.

**Create a time series database**

After you create a Lindorm cluster, a database named default is automatically created. By default, data written to the cluster is stored in the database. The default database cannot be deleted. LindormTSDB allows you to create multiple databases. Data stored in different databases is physically isolated. You can also configure different data time-to-lives (TTLs) and partition intervals for different databases. For more information about how to create a database, see CREATE DATABASE. Create a database named DB1 and specify that data in DB1 does not expire.

```
CREATE DATABASE DB1;
```

Create a database named DB2 and set the data TTL to 60 days.

```
CREATE DATABASE DB2 WITH (ttl=60);
```

**Create partitions based on time**

You can partition a LindormTSDB database by time. Data within different time ranges is stored in different partitions. Each partition contains time series data and the indexes for the time series. If you periodically create periodic time series, we recommend that you partition your database by time in case large numbers of inactive time series are generated. These time series can lead to oversized indexes. The default partition interval is 30 days. We recommend that you set the partition interval to 7 or 30 days. For more information about how to partition a database by time, see CREATE DATABASE. When you query data in a database, only the partition that stores the data within the specified time range is queried. Create a database named DB4 and set the partition interval to 30 days.

```
CREATE DATABASE DB4 WITH (partition_interval=30);
```

For an existing database, you can change its partition interval by modifying the **partition_interval** parameter.

```
ALTER DATABASE DB4 WITH (partition_interval=60);
```

**Important**

After you change the partition interval of a database, the new partition interval does not immediately take effect. After the partition interval is changed, LindormTSDB specifies the last day when data is written to the current partition as the end time of the partition and creates a new partition to store data that is written to the database after the day. The new partition interval takes effect only on the partition created after the interval is changed. The partition interval of existing partitions remains unchanged. For example, the partition interval of the database DB4 is changed from 30 days to 60 days. When the interval is changed, data within 50 days has been separately stored in two partitions named Partition1 and Partition2 in DB4. Partition1 stores data written to DB4 from day 1 to day 30. Partition2 stores data written to DB4 from day 31 to day 50. After the partition interval is changed, data written to DB4 from day 51 is written to the new partition whose partition interval is 60 days. The partition interval of Partition1 and Partition2 remains unchanged.

**Create a time series table**

Before you create a time series table, you must create data models for the table and determine the tags, timestamps, and fields in the table. Typically, LindormTSDB uses tags to match time series in queries and creates an inverted index for each tag. In addition, you can use the primary key of the table as the partition key. LindormTSDB partitions data by using the partition key and routes data to different storage nodes based on the hashes of data. If the condition specified in a query matches a partition key, LindormTSDB queries data only on the corresponding node instead of scanning data on all nodes. We recommend that you use a column that contains unique values as the primary key, such as Internet of Things (IoT) device IDs. For more information, see Data model and Design a time series table. Create a table named sensor.

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time   TIMESTAMP,
    temperature DOUBLE,
    humidity DOUBLE);
```

Create a table that stores sensor information and specify the device_id column as the primary key.

| Element | Description |
|---|---|

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time   TIMESTAMP,
    temperature DOUBLE,
    humidity DOUBLE,
    PRIMARY KEY(device_id));
```

**Automatically create a table**

LindormTSDB provides three types of schema constraint policies: strong constraint, weak constraint, and no constraint. You can specify the schema constraint policy when you write data by using LindormTSDB SDK for Java, the InfluxDB line protocol, or the multi-value data model compatible with TSDB APIs. In scenarios where the weak constraint policy is specified, LindormTSDB automatically creates a table or column when the table or column to which you want to write data does not exist. LindormTSDB automatically verifies the data type of the column to which you want to write data when the column exists. Single values written to a table by using the OpenTSDB protocol or TSDB APIs are stored by using the single-value model. LindormTSDB does not create tables for single-value data. LindormTSDB optimizes the underlying storage of multi-value data to improve the efficiency of data reads. In addition, LindormTSDB automatically creates a table for multi-value data even if the weak constraint policy is specified. Therefore, we recommend that you use the multi-value data model to store data.

#### Data model

This topic describes the data model of LindormTSDB and the terms that are related to the data model. In scenarios where time series data is used, such as IoT, application monitoring, and Industrial Internet scenarios, data sources constantly generate time series data based on a specific cycle. A row of time series data is described by using elements such as tag, timestamp, and field. Data that has the same characteristics is stored in the same table. The following figure describes the elements.

| table | A time series table stores data of the same type. For example, you can create a time series table to store monitored data that is generated by air quality sensors. |
|---|---|
| tag | A tag is used to describe a data source. In most cases, a tag value remains unchanged over time. For example, you can create tags for a sensor based on information such as the ID of the sensor and the region where the sensor is deployed. A database in LindormTSDB automatically indexes tags and allows you to query data based on tags. A tag consists of a tag key and a tag value. Tag keys and tag values must be of the STRING type. When you define a time series table, you can explicitly specify a rule based on which data sharding on multiple nodes is performed by specifying a tag column as the primary key of the table. This way, the performance of your business can be improved. |
| timestamp | A timestamp indicates the point in time when a row of data is generated. You can specify the timestamp of data when you write data to LindormTSDB. The system can also automatically generate the timestamp of the data that is written to a table. |
| field | A field describes a metric of a data source. In most cases, field values change over time. For example, you can create fields for a sensor based on information such as temperature and humidity. You are not required to create a fixed schema for field columns before the corresponding time series table is created. You can add or delete a field column when your business is running. A field consists of a field key and a field value. A field key must be of the STRING data type. For more information about the data types supported by field values, see Data types. |
| data point | A data point is a field value that is generated by a data source at a point in time. When you query data in a database or write data to a database, the number of data points is used as a metric. |
| time series | A time series is generated based on a metric that you specify for a data source. The values of the metric change over time. A time series is determined by tags. Time series data can be calculated based on operations such as downsampling, aggregation, and interpolation. You can aggregate time series data by using multiple functions, such as the sum, count, max, and min aggregate functions. The operations are performed on data in a time series. When a database stores data, the database stores data that is in the same time series in the same table. This helps increase the efficiency of access to time series data and allows time series data compression in LindormTSDB. In a time series table, a time series consists of data rows that have the same tag values. |

| Operation | Description |
|---|---|
| aggregation | Aggregation refers to operations such as grouping, counting the number of data points, and calculating the sum of data points in one or more time series. |
| downsampling | If the time range to be queried is large and the sampling rate of your raw data is high, you can perform downsampling to reduce the display precision of your query. For example, if your raw data is sampled at a granularity of seconds, you can perform downsampling in your query to sample the data at a granularity of hours. This way, you can reduce the number of data points in your result set. |
| interpolation | If no data points are collected within a specific time window in a time series, you can perform interpolation to insert values. |

A LindormTSDB database provides a time-to-live (TTL)-based management mechanism and supports various data operations, such as aggregation, downsampling, and interpolation.

| TTL | TTL is a validity period during which your data is retained. If the validity period of your data ends, the data is cleared. By default, data is permanently retained. |
|---|---|

**Scenarios**

A wind turbine power station has multiple intelligent wind turbines. A table named `Wind-generators` is created to store information about the wind turbines. Tags are used to describe the wind turbines. The tags include `ID` , `model` , and `manufacturer` . Each of the wind turbines reports field values, such as the values of `power` and `wind speed` , to a cloud database in LindormTSDB in real time. The following figure shows data that corresponds to the wind turbines used in the preceding scenario.

| d | wind speed |  |
|---|---|---|
| 7AD45EC |  | and |

| of | power |  |
|---|---|---|
| 7AD45EC |  | . |

A LindormTSDB database supports high-concurrency writes, provides a high compression rate, and can process the following types of queries: You can query data points that are generated within the specified time range in the specified time series. For example, you can query the values of `wind speed` for a wind turbine whose ID is `7AD45EC` within a 30-minute time range from `2020-10-24T00:00:00Z to 2020-10-24T00:30:00Z` . You can query data points that are generated within the specified time range in multiple time series and perform downsampling on the data points at a granularity of five minutes in the query. values at a granularity of `five minutes` . You can perform aggregation on data points that are generated within the specified time range in the specified time series. You can query the latest data points in multiple time series. For example, you can query the latest values of `power` and `wind speed` for a wind turbine whose ID is `7AD45EC` . You can perform an aggregate query on data points in multiple time series based on a tag. For example, you can perform an aggregate query to query the average value of `wind speed` at `2020-10-24T00:00:00Z` based on `KingWind` .

#### Write data to LindormTSDB

You can use the following methods to write data to LindormTSDB: LindormTSDB SDK for Java, the InfluxDB line protocol, standard SQL statements, API operations provided by Time Series Database (TSDB), the remote write interface of Prometheus, and Realtime Compute for Apache Flink. This topic describes how to use these methods to write data to LindormTSDB. LindormTSDB SDK for Java is suitable for developers who use Java to develop their applications. For more information about how to use LindormTSDB SDK for Java to write data to LindormTSDB, see Tutorial: Use LindormTSDB SDK for Java to connect to and use LindormTSDB. LindormTSDB SDK for Java has the following benefits: You can asynchronously write data to LindormTSDB without the need to wait for data synchronization. Data is automatically written in batches, which simplifies the development process and improves data write efficiency. Connections in the pool can be reused. This prevents the risk of creating large numbers of connections. Failed requests are automatically retried. You do not need to develop the retry mechanism for your application. LindormTSDB SDK for Java uses a custom encoding protocol to efficiently encode and decode data. LindormTSDB SDK for Java is thread-safe. You do not need to worry about the security of threads when you develop your applications. LindormTSDB SDK for Java supports three schema constraint policies: strong constraint, weak constraint, and no constraint.

```java
// Specify the endpoint of LindormTSDB. String url = "http://ld-bp17j28j2y7pm****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242"; // Create a LindormTSDB client. LindormTSDB clients are thread-safe and can be reused. You do not n eed to create a client for each thread and then shut down the client after operations are complete. ClientOptions options = ClientOptions.newBuilder(url).build(); LindormTSDBClient lindormTSDBClient = LindormTSDBFactory.connect(options); // Create a database and a table. lindormTSDBClient.execute("CREATE DATABASE demo"); lindormTSDBClient.execute("demo","CREATE TABLE sensor (device_id VARCHAR TAG,region VARCHAR TAG,tim e BIGINT,temperature DOUBLE,humidity DOUBLE,PRIMARY KEY(device_id))"); // Write data to LindormTSDB. int numRecords = 10; List<Record> records = new ArrayList<>(numRecords); long currentTime = System.currentTimeMillis(); for (int i = 0; i < numRecords; i++) {
    Record record = Record
        .table("sensor")
        .time(currentTime + i * 1000)
        .tag("device_id", "F07A1260")
        .tag("region", "north-cn")
        .addField("temperature", 12.1 + i)
        .addField("humidity", 45.0 + i)
        .build();
    records.add(record);
} CompletableFuture<WriteResult> future = lindormTSDBClient.write("demo", records); // Process the data that is asynchronously written. future.whenComplete((r, ex) -> {
    // Process write failures.
    if (ex != null) {
        System.out.println("Failed to write.");
            LindormTSDBException e = (LindormTSDBException) ex;
            System.out.println("Caught an LindormTSDBException, which means your request made it to
                               + "but was rejected with an error response for some reason.");
            System.out.println("Error Code: " + e.getCode());
            System.out.println("SQL State:  " + e.getSqlstate());
            System.out.println("Error Message: " + e.getMessage());
        }  else {
            ex.printStackTrace();
        }
    } else  {
        System.out.println("Write successfully.");
    }
}); // In this example, a simple synchronization operation is performed to process the data that is wri tten to the table. System.out.println(future.join());
```

LindormTSDB allows you to use the InfluxDB line protocol to write data. If your application is not developed by using Java, we recommend that you use the InfluxDB line protocol to write data to LindormTSDB. You can configure the schema constraint policy when you use the InfluxDB line protocol to write data. By default, the schema constraint policy is weak constraint. For more information, see Write data by using InfluxDB line protocol.

| Method | Scenario | Description | References |
|---|---|---|---|
| Use Java Database Connectivity (JDBC) to write data. | Applications developed by using Java | When you use JDBC to write data to LindormTSDB, you must write code in your application or use Druid to manage the connection pool. | Java JDBC driver |
| Use API operations to write data. | Applications developed by using non-Java programming languages | LindormTSDB allows you to use SQL statements to write data by calling HTTP- based API operations. | Use the HTTP-based SQL API of LindormTSDB |

| Method | Description | References |
|---|---|---|

**Important**

When you use the InfluxDB line protocol to write data to LindormTSDB, the written data is accurate to milliseconds. Therefore, precision loss occurs when data with a time precision higher than milliseconds is written to LindormTSDB by using the InfluxDB line protocol.

```
POST /api/v2/write?precision=ms&db=default sensor,device_id=F07A1260,region=north-cn temperature=12.1,humidity=45 1619076780000 sensor,device_id=F07A1260,region=north-cn temperature=13.2,humidity=47 1619076790000 sensor,device_id=F07A1260,region=north-cn temperature=10.6,humidity=46 1619076800000 sensor,device_id=F07A1260,region=north-cn temperature=18.1,humidity=44 1619076780000 sensor,device_id=F07A1260,region=north-cn temperature=19.7,humidity=44 1619076790000
```

**Use standard SQL statements**

The following table describes the two methods that can be used when you use SQL statements to write data to LindormTSDB.

**Use the API operations provided by TSDB**

LindormTSDB is compatible with the API operations of TSDB. If your application uses TSDB to store data, you can use the API operations provided by TSDB to write data to LindormTSDB. The following table describes the two methods that can be used when you use API operations provided by TSDB to write data.

| Write multi- value data. | The /api/mput operation is used to write multi-value data. In this case, the default schema constraint policy is no constraint, which indicates that time series tables are not created and SQL statements cannot be used to query data. For applications that are newly developed or use TSDB, we recommend that you use other methods supported by the multi-value model to write data. If you want to use SQL statements to query data, you can manually create time series tables before or after you write data. You can also set the schema constraint policy to weak constraint to allow automatic creation of time series tables. Sample code: curl -X POST http://ld-xxxxxxxxx- proxy-tsdb- pub.lindorm.rds.aliyunc s.com:8242/api/config - d'{"schema.policy.opent sdb":"WEAK"}' | Write multi-value data by calling the API: For more information, see the "Write multi-value data points" topic in Lindorm Developer Guide. Write multi-value data by using an SDK: For more information, see the "Use the LindormTSDB SDK to write multi-value data" topic in Lindorm Developer Guide. Note Metrics in TSDB correspond to tables in LindormTSDB. |
|---|---|---|
| Write single- value data. | The /api/put operation is used to write single-value data. This method can be used to write data to OpenTSDB. In this case, the default schema constraint policy is no constraint, which indicates that time series tables are not created and SQL statements cannot be used to query data. We recommend that you do not use this method to write data to LindormTSDB. | Write single-value data by calling the API: For more information, see the "Write data" topic of Write single-value data points in Lindorm Developer Guide. Write single-value data by using an SDK: For more information, see the "Write data" section in Write data points to a single- value model time series. |

You can use the Sink connector that integrates LindormTSDB SDK for Java to write data to LindormTSDB. For more information, see Use Realtime Compute for Apache Flink to write data to LindormTSDB.

#### Query data

This topic describes how to query data in LindormTSDB and perform related operations. LindormTSDB optimizes the SQL syntax for time series data and supports features that are specific to time series data, such as data downsampling, aggregation, and latest value queries. In addition, the optimized SQL syntax provides various function operators and computing and analysis capabilities for time series data. We recommend that you use SQL statements to query data. For more information about the SQL syntax, see SQL syntax reference. A downsampling query is an aggregate query that is performed based on the specified time interval. For more information, see Downsampling queries.

| Query method | Scenario | Description | Procedure |
|---|---|---|---|
| Use LindormTSDB SDK for Java to perform SQL queries | Java application development | LindormTSDB SDK for Java supports streaming data transmission and provides secure threads for API calling. Therefore, you do not need to manage underlying connections. | Tutorial: Use LindormTSDB SDK for Java to connect to and use LindormTSDB |
| Use JDBC to perform SQL queries | Java application development | You must write code in your applications or use Druid to manage the connection pool. JDBC must be used together with the Object- Relational Mapping (ORM) framework. | Use the JDBC driver to connect to and use LindormTSDB |

You can use the GROUP BY clause to aggregate multiple time series. A latest value query is performed to query the latest value of each time series. For more information, see Query the latest values. The SQL syntax of LindormTSDB provides function operators for time series data, such as sum, count, max, and min. For more information, see Common time series functions. LindormTSDB provides various computing and analysis capabilities based on calcite. For more information, see calcite documentation. Perform downsampling to reduce the time precision of data to eight hours.

```
SELECT device_id,region,time,count(humidity) AS count_humidity FROM sensor WHERE device_id='F07A1260' sample by 8h;
```

Perform downsampling to reduce the time precision of data, and then aggregate the data by device ID.

```
SELECT device_id, max(avg_humidity) AS max_humidity FROM (SELECT device_id,region,time,avg(humidity) AS avg_humidity FROM sensor sample by 8h) group by device_id;
```

**Note**

The SAMPLE BY clause is used to downsample a single time series. The GROUP BY clause is used to aggregate the data of multiple time series. If you want to use the SAMPLE BY and GROUP BY clauses in the same SQL statement, you must use a subquery in the statement.

**Access methods supported by SQL queries**

You can use Java Database Connectivity (JDBC), LindormTSDB SDK for Java, and API operations to perform SQL queries. The following table describes the three methods.

| Use API operations to perform SQL queries | Non-Java application development | LindormTSDB provides HTTP- based API operations to perform SQL queries. The results can be returned in streaming mode. | Use the HTTP-based SQL API of LindormTSDB |
|---|---|---|---|

| Query method | Description | References |
|---|---|---|
| Query multi-value data | You can query multi-value data that is inserted by SQL statements, LindormTSDB SDK for Java, the InfluxDB line protocol, and API operations that are compatible with TSDB. Note Metrics in TSDB correspond to tables in LindormTSDB. | API query: For more information, see the "Query multi-value data" topic in Lindorm Developer Guide. SDK query: For more information, see the "Use the LindormTSDB SDK to perform a multi-value query" topic in Lindorm Developer Guide. |
| Query single-value data | You can query single-value data inserted by API operations that are compatible with TSDB. We recommend that you do not use this method to query data. Note If you want to query data that is inserted by using SQL statements, LindormTSDB SDK for Java, and the InfluxDB, or multi-value data inserted by using API operations that are compatible with TSDB, you must set metrics in the metric@field format to adapt the query to multi-value data. In this format, set metric to the name of the table and field to the name of the column that stores the data you want to query. | API query: For more information, see the "Query single-value data" topic in Lindorm Developer Guide. SDK query: For more information, see the "Query data" topic in Lindorm Developer Guide. |

**Query data by using methods that are compatible with Time Series**

**Database (TSDB)**

LindormTSDB is compatible with 90% of the capabilities provided by TSDB. Therefore, if your application uses TSDB to store data, you can directly use the SQL syntax supported by LindormTSDB to query data without the need to modify your application. We recommend that you use SQL statements to query data in LindormTSDB.

| Method | Scenario | Description | Difference |
|---|---|---|---|
| Use pre- aggregation | Aggregate and query a large number of time series in real time. | Pre-aggregation uses the continuous query feature provided by LindormTSDB to calculate the data to be queried in advance and save the results to a result table. This way, the query is accelerated because only data in the result table needs to be queried. | In pre-aggregation, data is aggregated before it is queried. The result table that stores the aggregation results is different from the original table. Therefore, you must specify the original table and result table in your queries if you use pre-aggregation. |

Grafana is an open source tool that can be used to visualize large amounts of measurement data. You can use the Alibaba Cloud Lindorm data source plug-in provided by Grafana to access time series data in LindormTSDB. By using the Alibaba Cloud Lindorm data source plug-in provided by Grafana, you can use the SQL statements that are automatically generated in the editor or create custom SQL statements to query data.

**Use the Grafana plug-in for OpenTSDB to query data**

LindormTSDB provides API operations that are compatible with OpenTSDB to query data. You can use the OpenTSDB data source plug-in provided by Grafana to query data.

**Note**

If you want to query data that is inserted by using SQL statements, LindormTSDB SDK for Java, and the InfluxDB, or multi-value data inserted by using API operations that are compatible with TSDB, you must set metrics in the metric@field format to adapt the query to multi-value data. In this format, set metric to the name of the table and field to the name of the column that stores the data you want to query.

| Use pre- downsampling | Query time series within a wide time range. | Pre-downsampling uses LindormDFS to downsample and separately store the inserted data. When you query the data, data that is downsampled at the precision ratio closest to the precision ratio specified in the query conditions is queried. Then, the queried data is aggregated. This way, the amount of data that needs to be queried in real time is reduced, and therefore the query latency is decreased. | In pre-downsampling, the time precision of the original data is decreased. The downsampled data and original data are stored in the same table. Therefore, you do not need to specify different tables in your queries if you use pre-downsampling. |
|---|---|---|---|

#### Continuous queries

This topic introduces the concept of continuous queries (CQs) in LindormTSDB and the features that are related to CQs. CQs are automatically executed on time series data in LindormTSDB at a specified interval. In time series applications, real-time data is written into databases based on timestamps. In some cases, you want to calculate the time series data that matches specified conditions at scheduled intervals and store the calculation results based on your business requirements. For example, you want to perform aggregate operations on the time series data that is written within a specified time window at scheduled intervals. The following figure shows a scenario in which CQs are performed. CQs are suitable for such scenarios. In a time series engine, CQs provide a simplified stream computing capability. This capability allows the time series engine to calculate the data written within a time window after the time window ends.

**Use CQs**

**Manage CQs**

LindormTSDB allows you to use SQL to manage CQs in your databases. Create a CQ You can create a CQ in the specified database. For more information about the SQL syntax, see CREATE CONTINUOUS QUERY. You can delete an existing CQ from the specified database. For more information about the SQL syntax, see DROP CONTINUOUS QUERY. View the information about a CQ You can query the metadata of a CQ. For more information about the SQL syntax, see SHOW CONTINUOUS QUERIES.

**Schedule time windows for CQs**

CQs use the timestamps of local LindormTSDB nodes to determine the time when to perform calculations and use these timestamps as a reference to calculate time windows. A CQ automatically runs to calculate data that is written within the previous window each time a new time window starts. For example, if the specified time window for a CQ is 1 hour, the CQ calculates data at the beginning of each hour. If a calculation is triggered at 20:00, the time range of the data to be calculated is **[19:00:00,20:00:00)**.

**Important**

Although a CQ starts to calculate data immediately after the end of the defined time window, it may take a period of time to save the calculation results to the destination table. The latency varies based on the amount of data that you want to query and the real-time loads on the instance in which the data is stored. The accuracy of the results of a CQ depends on whether the data is written in chronological order. In some cases, LindormTSDB still writes data that belongs to the previous time window when a new time window starts. In these cases, these data records are out of order and cannot be queried or calculated during the previous time window. When a database is deleted, all CQs that are created for the database are deleted.

**Common scenarios and examples**

**Common scenarios of CQs**

Cost-efficient data persistence For scenarios in which a large amount of data is stored, the storage costs of the data become a critical issue. You can use CQs together with the time-to-live (TTL) or cold data archiving capability to reduce the cost of data persistence. For more information about the TTL and cold data archiving capabilities, see Manage databases. If you directly run a downsampling query that spans a large time range or an aggregate query across time series on raw data, the query may take a long period of time to process. In this case, you can use a CQ to precalculate the results, and then query the data from the result table when necessary. This way, both the query performance and query throughput can be improved. The following example shows how to use CQs and the TTL feature to achieve cost-efficient data persistence. In some cases, your business application generates large amounts of raw data, and only the data of the last month can be retained. After downsampling is performed, the data of the last several years can be retained. In the following example, the sampling period of raw data is 1 second and is downsampled to 1 minute to persist the data.
1. Execute the following statement to create a database named db_sensor_month to store raw data and
set the maximum data retention period to 30 days:

```
CREATE DATABASE db_sensor_month WITH (ttl=30);
```

2. Execute the following statement to create another database to store data that is returned after a CQ is
run:

```
CREATE DATABASE db_sensor_year WITH (ttl=365);
```

3. Execute the following statement to create a table to store the calculation results:

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time TIMESTAMP,
    temperature DOUBLE,
    humidity BIGINT);
```

4. Execute the following statement to create a CQ to perform downsampling:

```
CREATE CONTINUOUS QUERY db_sensor_year.my_cq WITH (INTERVAL='1m')
```

`AS`

```
  INSERT into db_sensor_year.sensor(time, temperature, humidity, device_id,region)
  SELECT time, mean(temperature) AS temperature, mean(humidity) humidity, device_id, region
  FROM db_sensor_month.sensor
  SAMPLE BY 60s;
```

#### Pre-downsampling

This topic describes how to configure, query, and delete pre-downsampling rules and provides best practices for pre-downsampling.

**Introduction**

Pre-downsampling is performed to calculate data before it is written to databases. Pre-downsampling downsamples data and separately stores the data to be written based on the specified pre-downsampling rule. When you query the written data, data that is downsampled at a pre-downsampling ratio that is closest to the downsampling ratio specified in the query conditions is queried. Then, the queried data is sent to and processed by the compute engine. This way, the amount of data that needs to be queried and calculated in real time is reduced, and the query latency is decreased. To use pre-downsampling, the version of LindormTSDB must be 3.4.19 or later. Compared with continuous queries, pre-downsampling has the following benefits: The downsampled data can be queried immediately after it is written. You do not need to wait for the execution of continuous queries. Pre-downsampling does not affect the write performance. Downsampled data is stored in real time when it is written. The pre-downsampled data and original data are stored in the same table. When you perform predownsampling queries, pre-downsampled data that best matches the specified rule is queried. If the pre-downsampled data does not match the specified rule, the original data is queried. A pre-downsampling rule applies only to data that is written after the rule is configured. If you configure a pre-downsampling rule for a database, the rule applies to all data in the database. You can configure different time-to-lives (TTLs) for the pre-downsampled data and original data. By default, the TTL of the pre-downsampled data is the same as that configured for the database in which the pre-downsampled data is stored.

**Use SQL statements to configure a pre-downsampling rule**

You can use the SQL statements in the following examples to configure a pre-downsampling rule. To configure a pre-downsampling rule that applies only to a table, you must use SQL statements to configure the rule. Configure a pre-downsampling rule in which the pre-downsampling ratio is set to one hour and the sum and max operations are performed on the pre-downsampled data.

```
CREATE PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `max`) ON sensor;
```

Configure a pre-downsampling rule in which the pre-downsampling ratio is set to one hour, the sum and max operations are performed on the pre-downsampled data, and the TTL of the pre-downsampled data is set to 90 days.

| Request path | Request method | Description |
|---|---|---|
| /api/database | POST PUT | Configure a pre-downsampling rule for the specified database. If you initiate a POST request, the database is created. If the specified database already exists, you must use the PUT method to initiate a request to update the pre-downsampling rule of the database. Note A database named default is automatically created after you create a Lindorm instance. In this case, you must use the PUT method to initiate a request to update the pre-downsampling rule. |

| Parameter | Required | Description |
|---|---|---|
| name | Yes | The database name. Example: default. |
| downsampleRules | Yes | The list of pre-downsampling rules that you want to configure. The list of rules is specified in JSON format. Each time you update the pre-downsampling rules of the database, all rules in the list are updated. |

| Parameter | Required | Description | Example |
|---|---|---|---|
| aggregator | Yes | The aggregate function used in pre-downsampling. Note The avg function is not supported in pre- downsampling. You can calculate the average value of pre-downsampled data by using the results of the count and sum functions. However, if data is repeatedly added and overwritten, the average value may be inaccurate. | sum, count, max, min, first, last, and median. |
| intervals | Yes | The list of time intervals based on which pre-downsampling is performed. The following units are supported: s (second), m (minute), h (hour), and d (day). | For example, if the parameter is set to ["10m", "1h"] , the original data is separately pre- downsampled based on an interval of 10 minutes and an interval of one hour. |

```
CREATE PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `max`) TTL `90d` ON sensor;
```

**Use API operations to configure a pre-downsampling rule**

Request path and method Request parameters

| Developer Guide·Lind | ormTSDB |  | Lindorm |
|---|---|---|---|

| Request path | Request method | Description |
|---|---|---|

Sample request PUT /api/database

```json
{
    "name": "default",
    "downsampleRules": {
        "rules": [
            {
                "aggregator": "sum",
                "intervals": [
                    "1m",
                    "1h"
```

]

```json
            },
            {
                "aggregator": "max",
                "intervals": [
                    "1m",
                    "1h"
```

]

```
            }
```

]

```
    }
}
```

If the request is successful, the HTTP status code 200 is returned. You can use API operations or SQL statements to query pre-downsampling rules. If pre-downsampling rules are configured for a database and a table in the database at the same time, the rules of the table prevail when you query data. We recommend that you use SQL statements to query pre-downsampling rules.

**Use SQL statements to query pre-downsampling rules**

You can use the SQL statements in the following examples to query all pre-downsampling rules configured for a database or a table. Query all pre-downsampling rules configured for all tables in a database. Query all pre-downsampling rules configured for a table named sensor. For more information about the syntax, see SHOW PREDOWNSAMPLES.

**Use API operations to query pre-downsampling rules**

Request path and method

| /api/database | GET | Query the pre-downsampling rules configured for a database or a table. |
|---|---|---|

Sample request

```json
[{
    "name": "default",
    "downsampleRules": {
        "rules": [
            {
                "aggregator": "sum",
                "intervals": [
                    "1m",
                    "1h"
```

]

```json
            },
            {
                "aggregator": "max",
                "intervals": [
                    "1m",
                    "1h"
```

]

```
            }
```

]

```
    }
}]
```

If the request is successful, the HTTP status code 200 is returned. You can use the SQL statements in the following examples to delete pre-downsampling rules.

```
DROP PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `max`) ON sensor;
```

**Important**

After you delete a pre-downsampling rule, data that has been pre-downsampled based on the rule is not immediately deleted. However, the deleted pre-downsampling rule is not returned when you query pre-downsampling rules. For more information about the syntax, see DROP PREDOWNSAMPLE.

**Matching rules for pre-downsampled data**

If pre-downsampling rules are configured for a database and a table in the database at the same time, the rules configured for the table prevail in pre-downsampling queries. If the downsampling ratio specified in a query does not exactly match that of the pre-downsampled data, the pre-downsampled data whose pre-downsampling ratio best matches the specified downsampling ratio is queried. We recommend that you set the time intervals based on which predownsampling is performed to 1m, 10m, 1h, and 1d to meet the requirements of most downsampling queries.

| Request path | Request method | Description |
|---|---|---|
| /api/mquery | GET | Query pre-downsampled data. |

| Parameter | Required | Description | Example |
|---|---|---|---|
| downsampleSource | No | The data source that is queried. Valid values: raw: The original data is queried. This is the default value. downsample: The pre- downsampled data is queried. | downsample |

**Note**

If the pre-downsampling ratio of the pre-downsampled data is the maximum value that can divide the downsampling ratio specified in the query, the pre-downsampling ratio best matches the downsampling ratio specified in the query. For example, if the original data is pre-downsampled based on 1m, 5m, 8m, and 15m and the downsampling ratio specified in a query is 10m, the predownsampling ratio that best matches the specified downsampling ratio is 5m. In no pre-downsampling ratio matches the downsampling ratio specified in a query, the original data is queried.

**Use SQL statements to query pre-downsampled data**

By default, when you query pre-downsampled data, the raw data before pre-downsampling is queried. To query only pre-downsampled data, you must add the /*+ PREDOWNSAMPLE */ hint to the query statements.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619085600000 SAMPLE BY 1h
```

**Query pre-downsampled data by using methods that are compatible**

**with TSDB**

You can use query pre-downsampled data in Time Series Database (TSDB) by using the following three method: API-based multi-value queries, API-based single-value queries, and SDKs.

**Query pre-downsampled data by using API-based multi-value queries**

When you use API operations to query pre-downsampled data, you must configure the
**downsampleSource** parameter to specify the data source.
Request path and method Request parameters Sample request

```json
{
    "end": 1619085600000,
    "queries": [
        {
            "downsampleDataSource" : "downsample",
            "metric": "aggMetric",
            "fields" : [
                {
                    "field" : "score",
                    "aggregator" : "none",
                    "downsample" : "1h-sum"
                }
```

`],`

```json
                      "tags":{
                    "sensor":"IOTE_8859_0005"
                  }
        }
```

`],`

```json
    "start": 1619074800000
}
```

**Query pre-downsampled data by using API-based single-value queries**

The API operation used to query single-value data is compatible with OpenTSDB. You can also use the Grafana plug-in for OpenTSDB to configure the data source. In this case, you must set metrics in the
**metric@field##downsample** format. In this format, set metric to the name of the table and field to the
value that you want to query. The downsample suffix indicates that pre-downsampled data is queried. When you use an SDK to query pre-downsampled data, you must configure the **downsampleDataSource** parameter in MultiFieldSubQuery Builder.

```
long startTime = 1619074800000; long endTime = 1619085600000; final String metric = "wind"; final String field = "speed"; MultiFieldSubQueryDetails fieldSubQueryDetails = MultiFieldSubQueryDetails
        .field(field)
        .aggregator(Aggregator.SUM)
        .downsample("1h-sum")
        .build();
MultiFieldSubQuery subQuery = MultiFieldSubQuery
        .metric(metric)
        // Query pre-downsampled data.
        .downsampleDataSource(DownsampleDataSource.DOWNSAMPLE)
        .build();
MultiFieldQuery query = MultiFieldQuery.
        start(startTime).
        end(endTime).
        sub(subQuery).
        build();
List<MultiFieldQueryResult> result = tsdb.multiFieldQuery(query);
```

Parameters You can set the **DownsampleDataSource** parameter to one of the following values: DOWNSAMPLE: Query the pre-downsampled data. RAW: Query the raw data. The default value of this parameter is RAW.

**// Query pre-downsampled data.**

For data that is sampled at an interval of seconds, we recommend that you configure pre-downsampling rules based on intervals of one minute, one hour, and one day to perform a downsampling query at a downsampling ratio of any minute, hour, or day. Configure pre-downsampling rules in which the sum, count, min, and max aggregate functions are specified based on intervals of one minute, one hour, and one day.

```
CREATE PREDOWNSAMPLE `1m` AGGREGATORS (`sum`, `count`, `min`, `max`) ON sensor; CREATE PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `count`, `min`, `max`) ON sensor; CREATE PREDOWNSAMPLE `1d` AGGREGATORS (`sum`, `count`, `min`, `max`) ON sensor;
```

Perform a downsampling query at a downsampling ratio of any minute by using the pre-downsampling rule configured based on an interval of one minute.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature), max(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619085600000 SAMPLE BY <N>m;
```

Perform a downsampling query at a downsampling ratio of any hour by using the pre-downsampling rule configured based on an interval of one hour.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature), max(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619085600000 SAMPLE BY <N>h;
```

Perform a downsampling query at a downsampling ratio of any day by using the pre-downsampling rule configured based on an interval of one day.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature), max(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619600400000 SAMPLE BY <N>d;
```

**Pre-downsampling for data sampled at an interval of minutes**

For data that is sampled at an interval of minutes, we recommend that you configure pre-downsampling rules based on intervals of one hour and one day to perform a downsampling query at a downsampling ratio of any hour or day. Configure pre-downsampling rules in which the sum, count, min, and max aggregate functions are specified based on intervals of one hour and one day.

```
CREATE PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `count`, `min`, `max`) ON sensor; CREATE PREDOWNSAMPLE `1d` AGGREGATORS (`sum`, `count`, `min`, `max`) ON sensor;
```

Perform a downsampling query at a downsampling ratio of any hour by using the pre-downsampling rule configured based on an interval of one hour.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature), max(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619085600000 SAMPLE BY <N>h;
```

Perform a downsampling query at a downsampling ratio of any day by using the pre-downsampling rule configured based on an interval of one day.

```
SELECT /*+ PREDOWNSAMPLE */ sum(temperature), max(temperature) from sensor WHERE time >= 1619074800000 AND time <= 1619600400000 SAMPLE BY <N>d;
```

#### Constraint policies for schemas

You can configure constraint policies for schemas to specify whether to check the existence of tables, the consistency between the table schemas, and the consistency of the field data types when you write data to table. The supported constraint policies for schemas vary with the method that you use to write data. This topic describes the constraint policies for schemas in LindormTSDB and how to use these policies.

**Schema of the Lindorm time series model**

LindormTSDB abstracts the concept of time series tables based on the information about business data models in time series scenarios. When you develop applications based on LindormTSDB, you can access time series tables in a similar manner in which relational tables are accessed in traditional relational databases. However, the time series model is different from the relational data model. The time series model is more like a semi-structured data model that supports data queries based on the specified structure and allows columns to be dynamically added or reduced in application performance management (APM), IoT, or traditional industrial scenarios. The structure of the semi-structured data model is different from the tabular structure of data models that are associated with relational databases. In actual business scenarios, data models that are generated by devices may frequently change because the devices continue to be improved, upgraded, or iterated. For example, the number of fields that are generated by devices is increased, and the field types are changed. LindormTSDB provides the ALTER TABLE statement to allow you to change time series tables. However, in some time series scenarios, if the constraints on the table schemas are as strict as the constraints on the schemas of tables in relational databases, application development may become more difficult. In this case, LindormTSDB provides more flexible policies for users to apply constraints on table schemas.

**Schema constraints**

In most cases, schema constraints take effect when data is written to tables. The schema constraints can define whether the written fields are consistent with the fields that are contained in the predefined table schema, whether the data types of the written fields are consistent with or compatible with the predefined data types, or whether the table to which data is written exists. In traditional relational databases, strict constraints are applied. Based on the schema constraints in LindormTSDB, the system performs the following verification operations: Verify whether the destination table to which data is written exists. Verify whether the TAG or FIELD column to which data is written is predefined. Verify whether the types of the data that is written are consistent with the data types that are predefined. Verify whether the data types of fields that are returned are consistent with the data types that are specified when the table is created.

**Supported schema constraint policies**

LindormTSDB provides three types of schema constraint policies: **strong constraint**, **weak constraint**, and **no constraint**. You can select a policy based on your business requirements.

**Strong constraint**

LindormTSDB strictly verifies the name of the table to which data is written, the field name of data that is written, and the types of data that is written based on the predefined table schema. This process is similar to the verification process in traditional relational databases. An error is thrown if the table name, field name, or data type is inconsistent with that predefined in the table schema.

**Weak constraint**

When the table to which data is written does not exist, LindormTSDB does not throw an error. Instead, LindormTSDB automatically creates a table. When a tag or field is added to the data that is written, LindormTSDB does not report an error. Instead, LindormTSDB automatically adds a TAG or FIELD column to the time series table. If the data type of a field to which data is written changes, the data fails to be written because LindormTSDB detects that the data type of the field is inconsistent with the predefined data type. In this case, you must execute the ALTER TABLE statement to manually modify the data type of the field.

| Data writing method | Schema constraint policy | Sample code used to change schema constraint policies |
|---|---|---|
| Java JDBC driver | Only strong constraint is supported. | N/A |
| Java Native SDK | Supported constraint policies: Strong constraint (default) Weak constraint No constraint | // Specify the endpoint. String url = "http://ld-bp1489gr5t*****-proxy- tsdb.lindorm.rds.aliyuncs.com:8242"; // Create a LindormTSDB client. A LindormTSDB client is thread-safe and can be reused. You do not need to create a client for each thread and then shut down the client after operations are complete. ClientOptions options = ClientOptions .newBuilder(url) .setSchemaPolicy(SchemaPolicy.WEAK) .build(); LindormTSDBClient lindormTSDBClient = LindormTSDBFactory.connect(options); |
| HTTP-based SQL API of LindormTSDB | Only strong constraint is supported. | N/A |
| InfluxDB line protocol | Supported constraint policies: Strong constraint Weak constraint (default) No constraint | curl -X POST 'http://ld-bp1489gr5t*****-proxy- tsdb.lindorm.rds.aliyuncs.com:8242/api/v2/write? db=default&schema policy=WEAK' -d _ 'sensor,device id=F07A1260,region=north-cn _ temperature=12.1,humidity=45 1619076780000' |

**Note**

When a weak constraint policy is used, some verification operations are still performed. For example, if you try to write a non-string value to the TAG column or write data of a non-timestamp type to the timestamp column, the verification fails.

**No constraint**

No constraints are applied. If you use this policy, no error is thrown when the table to which you want to write data does not exist. You can call interfaces that are compatible with Time Series Database (TSDB) to query the written data. If you manually create a table when the table to which you want to write data does not exist, you can execute SQL statements to query the written data. However, no error is thrown for inconsistent field data types.

**Note**

The no constraint policy is reserved by the system to ensure the compatibility with TSDB. We recommend that you do not use the no constraint policy.

**Select a schema constraint policy based on the data writing method**

In LindormTSDB, the schema constraint policies that are used when data is written are closely related to the methods used to write data. The following table describes schema constraint policies that correspond to different data writing methods.

| Multi-value data | Supported constraint policies: Weak constraint Strong constraint No constraint (default) | curl -X POST http://ld-bp1489gr5t*****-proxy- tsdb.lindorm.rds.aliyuncs.com:8242/api/config - d'{"schema.policy.opentsdb":"WEAK"}' |
|---|---|---|
| Single-value data | Only no constraint is supported. | N/A |

| Item | Description |
|---|---|
| Database name | A database name must be 2 to 64 characters in length and can contain uppercase letters, lowercase letters, digits, and underscores ( ). _ |
| Number of databases | Up to 16 databases, including the default database, can be created in a Lindorm instance. |
| Table name | A table name can be up to 128 characters in length and can contain uppercase letters, lowercase letters, digits, and underscores ( ). _ |
| Number of tables | Up to 10,000 tables can be created in a Lindorm database. |
| Name of the tag column | The name of the tag column can contain only visible characters and can be up to 200 characters in length. |
| Value of the tag column | The value of the tag column can contain only visible characters and can be up to 20,480 characters in length. |
| Name of the field column | The name of the field column can contain only visible characters and can be up to 200 characters in length. |
| Value of the field column | The value of the field column can contain only visible characters and can be up to 20,480 characters in length. |
| Name of the timestamp column | The name of the timestamp column can contain only visible characters and can be up to 200 characters in length. A table can have only one timestamp column, which is used as the time index by default. |
| Value of the timestamp column | The unit of the value of the timestamp column is milliseconds. |
| Number of columns | Up to 1,024 columns, including the tag, field, and timestamp columns, can be created in a table. |

#### Limits

This topic describes the limits on LindormTSDB.

| Data type | Description |  |  |
|---|---|---|---|
| BIGINT | Integers. |  |  |
| DOUBLE | Floating points. |  |  |
| VARCHAR | String data. |  |  |
| BOOLEAN | Boolean data. Valid values: true and false. |  |  |
| TIMESTAMP | Timestamp data. You can use one of the following methods to insert a value of the timestamp data type: Insert a string. The string must be in the yyyy-MM-DD HH:mm:ss(.sss) format. Example: 2022-01-01 12:00:00 . Insert an integer, which is a 64-bit UNIX timestamp. The timestamp is accurate to the millisecond. The UNIX timestamp represents the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 Coordinated Universal Time (UTC). |  |  |
|  |  | 2022-01-01 |  |

|  | 12:00:00 |
|---|---|

### SQL syntax reference

#### Data types

This topic describes the data types that are supported by LindormTSDB. The following table describes the data types that LindormTSDB allows you to use in SQL statements.

**Important**

1. When you create a time series table, you can specify only one column of the timestamp data type.
2. LindormTSDB encodes and parses timestamps based on Beijing Time (GMT+8).
3. The UNIX timestamps in outdated systems are still parsed to 32-bit values. We recommend that you
multiply these timestamps by 1000 before you insert the timestamps to LindormTSDB. If you insert the timestamps to LindormTSDB without converting the timestamps, LindormTSDB cannot parse the timestamps as normal. For example, the **1641009600** timestamp is parsed as `2022-01-01 12:00:00` in an outdated system. LindormTSDB parses the timestamp as `1970-01-20 07:50:09(GMT+8)` .

#### Common time series functions

This topic describes the common functions supported by LindormTSDB SQL and provides some examples.

**Prerequisites**

The LindormTSDB version is 3.4.7 or later.

**Prepare data**

A time series table named `sensor` contains the following two time series. Time Series 1 that has the `device_id=F07A1260, region=north-cn` tag and contains the temperature and humidity fields. Time Series 2 that has the `device_id=F07A1261, region=south-cn` tag and contains the temperature and humidity fields.

```
DESCRIBE sensor; +-------------+-----------+------------+
| columnName  | typeName  | columnKind |
+-------------+-----------+------------+
| device_id   | VARCHAR   | TAG        |
| region      | VARCHAR   | TAG        |
| time        | TIMESTAMP | TIMESTAMP  |
| temperature | DOUBLE    | FIELD      |
| humidity    | DOUBLE    | FIELD      |
+-------------+-----------+------------+ SELECT * FROM sensor; +-----------+----------+---------------------------+-------------+-----------+
| device_id |  region  |           time            | temperature | humidity  |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.100000   | 45.000000 |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 13.200000   | 47.000000 |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   | 46.000000 |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 12.100000   | 51.000000 |
| F07A1261  | south-cn | 2021-04-22T15:51:21+08:00 | 13.200000   | 52.000000 |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | 10.600000   | 53.000000 |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 20.600000   | 55.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

**CURRENT_TIMESTAMP**

**Description**

You can call this function to obtain the current system time.

```
CURRENT_TIMESTAMP
```

**Important**

You do not need to specify parameters when you call the `CURRENT_TIMESTAMP` function. The timestamp returned by the CURRENT_TIMESTAMP function is accurate to the millisecond. Example: `2023-04-23T21:13:15.819+08:00` . The CURRENT_TIMESTAMP function returns the system time of the server on which the Lindorm instance is running. Therefore, make sure that the time data generated by this function can meet your business requirements. Do not use the timestamps generated by this function when you write data **in your business**. We recommend that you use this function to generate large amounts of test data for testing and development. Add a row of data to the sensor table. The tag of the data is `device_id=F07A1262, region=north-cn` , and the timestamp of the data is the current system time when the data is written to the table.

```
INSERT INTO sensor(device_id,region,time,temperature,humidity) VALUES ('F07A1262','north-cn',CURREN T_TIMESTAMP,19.9,42);
```

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |

**SUM**

**Description**

You can call this function to calculate the sum of values in a field column.

```
SUM(field_name)
```

**Note**

The SUM function returns DOUBLE or BIGINT values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, calculate the sum of values in the temperature column.

```
SELECT device_id, region, time, sum(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 25.300000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 35.900000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually calculate the sum of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, sum(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 1970-01-01T08:00:00+08:00 | 35.900000   |
| F07A1261  | south-cn | 1970-01-01T08:00:00+08:00 | 56.500000   |
+-----------+----------+---------------------------+-------------+
```

Example 3: Calculate the sum of temperature values generated by all devices.

```
SELECT sum(temperature) AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and ti me >= '2021-04-22T15:33:00+08:00';
```

Sample response:

```
+-------------+
| temperature |
+-------------+
| 92.400000   |
+-------------+
```

**AVG**

**Description**

You can call this function to calculate the average value of values in a field column.

```
AVG(field_name)
```

**Note**

The AVG function returns DOUBLE values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, calculate the average value of values in the temperature column.

```
SELECT device_id, region, time, avg(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. |

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.650000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 11.966667   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually calculate the average value of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, avg(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 1970-01-01T08:00:00+08:00 | 11.966667   |
| F07A1261  | south-cn | 1970-01-01T08:00:00+08:00 | 14.125000   |
+-----------+----------+---------------------------+-------------+
```

Example 3: Calculate the average value of temperature values generated by all devices.

```
SELECT avg(temperature) AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and ti me >= '2021-04-22T15:33:00+08:00';
```

Sample response:

```
+-------------+
| temperature |
+-------------+
| 13.200000   |
+-------------+
```

**Description**

You can call this function to count the number of values in a field column.

```
COUNT(field_name)
```

**Note**

The COUNT function returns BIGINT values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, count the number of values in the temperature column within each interval.

```
SELECT device_id, region, time, count(temperature) AS temperature FROM sensor WHERE time <= '2021-0 4-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 2           |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 3           |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 1           |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 1           |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually count the number of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, count(temperature) AS temperature FROM sensor WHERE time <= '2021-0 4-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 1970-01-01T08:00:00+08:00 | 3           |
| F07A1261  | south-cn | 1970-01-01T08:00:00+08:00 | 4           |
+-----------+----------+---------------------------+-------------+
```

Example 3: Count the number of temperature values generated by all devices.

```
SELECT count(temperature) AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00';
```

Sample response:

```
+-------------+
| temperature |
+-------------+
| 7           |
+-------------+
```

**MIN**

**Description**

You can call this function to query the minimum value of values in a field column.

```
MIN(field_name)
```

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |

**Note**

The MIN function returns DOUBLE or BIGINT values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, query the minimum value of values in the temperature column within each interval.

```
SELECT device_id, region, time, min(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.100000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 10.600000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the minimum value of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, min(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | 10.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 3: Query the minimum value of temperature values generated by all devices.

```
SELECT min(temperature) AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and ti me >= '2021-04-22T15:33:00+08:00';
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |

```
+-------------+
| temperature |
+-------------+
| 10.600000   |
+-------------+
```

**MAX**

**Description**

You can call this function to query the maximum value of values in a field column.

```
MAX(field_name)
```

**Note**

The MAX function returns DOUBLE or BIGINT values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, query the maximum value of values in the temperature column within each interval.

```
SELECT device_id, region, time, max(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 13.200000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 13.200000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the maximum value of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, max(temperature) AS temperature FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. |

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 13.200000   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 3: Query the maximum value of temperature values generated by all devices.

```
SELECT max(temperature) AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and ti me >= '2021-04-22T15:33:00+08:00';
```

Sample response:

```
+-------------+
| temperature |
+-------------+
| 20.600000   |
+-------------+
```

**FIRST**

**Description**

You can call this function to query the first value of values in a field column.

```
FIRST(field_name)
```

**Note**

The FIRST function returns data whose type is the same as that of data in the specified field column.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, query the first value of values in the temperature column within each interval.

```
SELECT device_id, region, time, first(temperature) AS temperature FROM sensor WHERE time <= '2021-0 4-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. |

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.100000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 12.100000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the first value of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, first(temperature) AS temperature FROM sensor WHERE time <= '2021-0 4-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.100000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 12.100000   |
+-----------+----------+---------------------------+-------------+
```

**LAST**

**Description**

You can call this function to query the last value of values in a field column.

```
LAST(field_name)
```

**Note**

The LAST function returns data whose type is the same as that of data in the specified field column.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, query the last value of values in the temperature column within each interval.

```
SELECT device_id, region, time, last(temperature) AS temperature FROM sensor WHERE time <= '2021-04 -22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |
| P | An integer or a floating-point number. Valid values: 0 to 100. Default value: 50. |

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 13.200000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 10.600000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the last value of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, last(temperature) AS temperature FROM sensor WHERE time <= '2021-04 -22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

**PERCENTILE**

**Description**

You can call this function to query the specified percentile of values in a field column.

```
PERCENTILE(field_name,P)
```

**Note**

The PERCENTILE function returns DOUBLE values.

**Parameters**

Example 1: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, query the 90th percentile of values in the temperature column within each interval.

| (t | 1 | ,v | 1 | ), |
|---|---|---|---|---|

| (t | 2 | ,v | 2 | ) ... (t | N | ,v | N | ) |
|---|---|---|---|---|---|---|---|---|

```
SELECT device_id, region, time, percentile(temperature, 90) AS temperature FROM sensor WHERE time < = '2021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 13.200000   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00 | 13.200000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the 90th percentile of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, percentile(temperature, 90) AS temperature FROM sensor WHERE time < = '2021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 1970-01-01T08:00:00+08:00 | 13.200000   |
| F07A1261  | south-cn | 1970-01-01T08:00:00+08:00 | 20.600000   |
+-----------+----------+---------------------------+-------------+
```

**RATE**

**Description**

You can call this function to calculate the slope of values in a field column. following formula:

**Note**

The `interval` parameter in the preceding formula indicates the specified interval used to calculate the slope. The value of this parameter is measured in seconds.

```
RATE(field_name, 'interval units')
```

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |
| interval units | The interval based on which the slope is calculated. Default value: 1s. Valid units: s (seconds), m (minutes), h (hours), and d (days). |

**Note**

The RATE function returns DOUBLE values. The RATE operator must be separately used in an SQL statement.

**Parameters**

Example 1: Individually calculate the slope of temperature values generated by two devices whose IDs are F07A1260 and F07A1261 within the 1-second interval.

```
SELECT device_id, region, time, rate(temperature) AS temperature FROM sensor WHERE time <= '2021-04 -22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 0.110000    |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | -0.260000   |
| F07A1261  | south-cn | 2021-04-22T15:51:21+08:00 | 1.100000    |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | -0.433333   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 0.500000    |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually calculate the slope of temperature values generated by two devices whose IDs are F07A1260 and F07A1261 within the one-minute interval.

```
SELECT device_id, region, time, rate(temperature, '1m') AS temperature FROM sensor WHERE time <= '2 021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 6.600000    |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | -15.600000  |
| F07A1261  | south-cn | 2021-04-22T15:51:21+08:00 | 66.000000   |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | -26.000000  |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 30.000000   |
+-----------+----------+---------------------------+-------------+
```

| (t | 1 | ,v | 1 | ), |
|---|---|---|---|---|

| (t 2 ,v 2 ) ... (t points are returned: (t 2 (t N ,v N - ,v N-1 | (t | 2 | ,v | 2 | ) ... (t |  |  |  |  | N | ,v |  | N | ) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | (t |  | 2 | ,v |  | 2 |  |  |
| (t |  | N | ,v | N |  | ,v |  | N-1 |  | ) |  |  |  |  |

| v | 1 | ), (t | 3 | ,v | 3 |
|---|---|---|---|---|---|

| v | 2 | ) ... |
|---|---|---|

| Parameter | Description |
|---|---|

Example 3: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, calculate the average values of values in the temperature column within each 20-second interval. At last, calculate the slope of the average values within the one-minute interval.

```
SELECT device_id, region, time, rate(avg(temperature), '1m') AS temperature FROM sensor WHERE time <= '2021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | -6.150000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 25.900000   |
+-----------+----------+---------------------------+-------------+
```

Example 4: The RATE operator must be separately used in an SQL statement. Do not use the RATE operator in the methods shown in the following examples:

```
// Sample error SQL statement 1: SELECT region, time, rate(temperature), rate(humidity) FROM sensor WHERE time <= '2021-04- 22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0; // Sample response: ERROR 9001 (0A000): UNSUPPORTED: latest/rate/delta must be the only aggregator in a single SQL stat // Sample error SQL statement 2: SELECT region, time, rate(temperature), latest(humidity) FROM sensor WHERE time <= '2021-04-22T15:5 1:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0; // Sample response: ERROR 9001 (0A000): UNSUPPORTED: latest/rate/delta must be the only aggregator in a single SQL stat
```

**DELTA**

**Description**

You can call this function to calculate the difference between each value and the value in the previous row within the same field column.

```
DELTA(field_name)
```

**Note**

The DELTA function returns DOUBLE values. The DELTA operator must be separately used in an SQL statement.

**Parameters**

| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |
|---|---|

Example 1: Individually calculate the difference between each value and the value in the previous row within the same column of temperature values generated by two devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, delta(temperature) AS temperature FROM sensor WHERE time <= '2021-0 4-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 1.100000    |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | -2.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:21+08:00 | 1.100000    |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | -2.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 10.000000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Perform downsampling at a 20-second interval on the two time series that individually contain data generated by two devices whose IDs are F07A1260 and F07A1261. Then, calculate the average values of values in the temperature column within each 20-second interval. At last, calculate the difference between each value and the value in the previous row within the column of average values.

```
SELECT device_id, region, time, delta(avg(temperature)) AS temperature FROM sensor WHERE time <= '2 021-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 20s;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | -2.050000   |
| F07A1261  | south-cn | 2021-04-22T15:51:40+08:00 | 8.633333    |
+-----------+----------+---------------------------+-------------+
```

Example 3: The DELTA operator must be separately used in an SQL statement. Do not use the DELTA operator in the method shown in the following example:

```
// Sample error SQL statement: SELECT region, time, delta(temperature), rate(humidity) FROM sensor WHERE time <= '2021-04-22T15:51 :47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0; // Sample response: ERROR 9001 (0A000): UNSUPPORTED: latest/rate/delta must be the only aggregator in a single SQL stat
```

**Description**

You can call this function to query the latest N values in a field column.

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. |
| N | An integer that specifies the number of the latest values that you want to query in the field column. The default value of this parameter is 1, which indicates that only latest value in the field column is queried |

```
LATEST(field_name, N)
```

**Note**

The LATEST function returns data whose type is the same as that of data in the specified field column. The LATEST operator must be separately used in an SQL statement.

**Parameters**

Example 1: Individually query the latest temperature values generated by the devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, latest(temperature) AS temperature FROM sensor WHERE time <= '2021- 04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 20.600000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 2: Individually query the latest two temperature values generated by the devices whose IDs are F07A1260 and F07A1261.

```
SELECT device_id, region, time, latest(temperature, 2) AS temperature FROM sensor WHERE time <= '20 21-04-22T15:51:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+
| device_id |  region  |           time            | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00 | 10.600000   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00 | 20.600000   |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 13.200000   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00 | 10.600000   |
+-----------+----------+---------------------------+-------------+
```

Example 3: The LATEST operator must be separately used in an SQL statement. Do not use the LATEST operator in the method shown in the following example:

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |
| algo name _ | The name of the algorithm used to detect anomalies. The online anomaly detection algorithms developed by DAMO Academy are supported. esd: an algorithm that is applicable to spiked anomalies, such as spikes in monitoring curves and scenarios in which a small number of data points are significantly different from other data points. nsigma: an algorithm that is simple and easy to analyze the causes of anomalies. ttest: an algorithm that is used to identify whether the metrics related to time series data are abnormal because of a change in the average value. istl-esd: an algorithm that is applicable to detect anomalies in periodic data. Note The algo identifier parameter is applicable to scenarios in which in- _ database machine learning is not enabled and anomalies related to time series data must be detected. |
| model name _ | The name of the model used to forecast the values. Note The value of the model name parameter is of the VARCHAR type. _ |

```
// Sample error SQL statement: SELECT region, time, latest(temperature), rate(humidity) FROM sensor WHERE time <= '2021-04-22T15:5 1:47+08:00' and time >= '2021-04-22T15:33:00+08:00' sample by 0; // Sample response: ERROR 9001 (0A000): UNSUPPORTED: latest/rate/delta must be the only aggregator in a single SQL stat
```

**Description**

You can call this function to detect anomalies in a specified field column.

```
ANOMALY_DETECT(field_name, [algo_name | model_name], options)
```

**Note**

The ANOMALY_DETECT function returns BOOLEAN values.

**Parameters**

| options | The options used to adjust the detection effect. The optional parameters. Specify the value of this parameter in the key1=value1[, key2=value2] format. |
|---|---|

Example 1: Use the ESD algorithm to detect anomalies in the temperature data within a specific time range in a time series table named sensor.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd') AS detect_result FROM sensor WHE RE time >= '2022-01-01T00:00:00+08:00' and time < '2022-01-01T00:01:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | true          |
| F07A1260  | north-cn | 2022-01-01T00:00:20+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:40+08:00 | true          |
| F07A1261  | south-cn | 2022-01-01T00:00:00+08:00 | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:20+08:00 | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:40+08:00 | false         |
+-----------+----------+---------------------------+---------------+
```

Example 2: Use the ESD algorithm to detect anomalies in the temperature data of the F07A1260 device within a specific time range in the sensor table.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd') AS detect_result FROM sensor WHE RE device_id in ('F07A1260') and time >= '2022-01-01T00:00:00+08:00' and time < '2022-01-01T00:01:0 0+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | true          |
| F07A1260  | north-cn | 2022-01-01T00:00:20+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:40+08:00 | true          |
+-----------+----------+---------------------------+---------------+
```

Example 3: Use the ESD algorithm to detect anomalies in the temperature data of the F07A1260 device within a specific time range in the sensor table. In addition, set the lenHistoryWindow option to 30 and the maxAnomalyRatio option to 0.1.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd', 'lenHistoryWindow=30,maxAnomalyRatio=0.1') AS detect_result FROM sensor where device_id in ('F07A1260') and time >= '2022-01-01T00:00:00+08:00' and time < '2022-01-01T00:01:00+08:00' sample by 0;
```

Sample response:

| Parameter | Required | Description |
|---|---|---|
| field name _ | Yes | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |
| options | No | The feature binning policy and output mode. Specify the value of this parameter in the key1=value1, key2=value2 format. |

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:20+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:40+08:00 | true          |
+-----------+----------+---------------------------+---------------+
```

Example 4: Use the anomaly detection model created in the in-database machine learning feature to detect anomalies in the temperature data within a specific time range in the sensor table.

```
SELECT device_id, region, `time`, raw(temperature) as temperature, anomaly_detect(temperature, ad_m odel) AS detect_result FROM sensor WHERE time >= '2022-01-01T00:00:00+08:00' and time < '2022-01-01 T00:01:00+08:00' sample by 0;
```

Sample response:

```
+-----------+----------+---------------------------+-------------+---------------+
| device_id |  region  |           time            | temperature | detect_result |
+-----------+----------+---------------------------+-------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | 59.100000   | true          |
| F07A1260  | north-cn | 2022-01-01T00:00:20+08:00 | 13.200000   | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:40+08:00 | 64.600000   | true          |
| F07A1261  | south-cn | 2022-01-01T00:00:00+08:00 | 12.100000   | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:20+08:00 | 13.200000   | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:40+08:00 | 10.600000   | false         |
+-----------+----------+---------------------------+-------------+---------------+
```

**Description**

You can call this function to perform feature binning on the data in the specified field column of a time series table. Feature binning is also known as discrete binning or discrete bucketing and is a technique used to preprocess data.

```
BINS(field_name, options)
```

**Note**

The BINS function returns VARCHAR values.

**Parameters**

Example 1: Perform feature binning on the temperature data within the specified time range in a time series table named sensor.

```
SELECT device_id, region, time, bins(temperature) AS temperature_bin FROM sensor WHERE time >= '2 021-04-22 00:00:00' AND time < '2022-04-23 00:01:00' sample by 0;
```

Sample response:

```
+-----------+----------+--------------------------------+--------------------+
| device_id |  region  |           time                 |  temperature_bin   |
+-----------+----------+--------------------------------+--------------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00      |    [10.60,12.10)   |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00      |    [12.10,13.20]   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00      |    [10.60,10.60)   |
| F07A1261  | south-cn | 2021-04-22T15:51:20+08:00      |    [10.60,12.10)   |
| F07A1261  | south-cn | 2021-04-22T15:51:21+08:00      |    [12.10,13.20)   |
| F07A1261  | south-cn | 2021-04-22T15:51:27+08:00      |    [10.60,10.60)   |
| F07A1261  | south-cn | 2021-04-22T15:51:47+08:00      |    [13.20,20.60]   |
+-----------+-----------+-------------------------------+--------------------+
```

Example 2: Perform feature binning on the temperature data of a device whose ID is F07A1260 within the specified time range in a time series table named sensor.

```
SELECT device_id, region, time, bins(temperature) AS temperature_bin FROM sensor WHERE device_id in ('F07A1260') AND time >= '2021-04-22 00:00:00' AND time < '2022-04-23 00:01:00' sample by 0;
```

Sample response:

```
+-----------+----------+--------------------------------+--------------------+
| device_id |  region  |           time                 |  temperature_bin   |
+-----------+----------+--------------------------------+--------------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00      |    [10.60,12.10)   |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00      |    [12.10,13.20]   |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00      |    [10.60,10.60)   |
+-----------+----------+--------------------------------+--------------------+
```

Example 3: Perform feature binning on the temperature data of a device whose ID is F07A1260 within the specified time range in a time series table named sensor. In addition, specify the n_bins option to 2, the output_type option to ordinal, and the strategy option to uniform.

```
SELECT device_id, region, time, bins(temperature, 'n_bins=2, output_type=ordinal, strategy=uniform') AS temperature_bin FROM sensor WHERE device_id in ('F07A1260') AND time >= '20 21-04-22 00:00:00' AND time < '2022-04-23 00:01:00' sample by 0;
```

Sample response:

```
+-----------+----------+--------------------------------+--------------------+
| device_id |  region  |           time                 |  temperature_bin   |
+-----------+----------+--------------------------------+--------------------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00      |  1                 |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00      |  1                 |
| F07A1260  | north-cn | 2021-04-22T15:33:20+08:00      |  0                 |
+-----------+----------+--------------------------------+--------------------+
```

#### DDL

##### CREATE DATABASE

This topic describes the syntax that is used to create a Lindorm TSDB database.

| Parameter | Description |
|---|---|
| attribute statement _ | The attributes of the database. |
| attr name _ | The name of the attribute. The name must be an SQL constant or identifier. |
| attr val _ | The value of the attribute. The value must be an SQL constant. |

| Attribute | Type | Default value | Description | Example |
|---|---|---|---|---|
| ttl | BIGINT | No default value. By default, data is permanently retained. | The retention period of data. Data that exceeds the retention period is automatically deleted. Unit: days. If you set this parameter to 0, data is permanently retained. | 60 |
| partition inte _ rval | BIGINT | 0 Note The default value of this parameter is 30 if the version of Lindorm TSDB is 3.4.19 or later. | The interval based on which data is partitioned. Data and indexes within the same interval are stored in the same partition. Unit: days. | 30 |

```
create_database_statement ::= CREATE DATABASE database_name [ WITH attribute_statement ] attribute_statement ::= '(' attribute_definition (',' attribute_definition)* ')' attribute_definition ::= attr_name '=' attr_val
```

**Parameters**

The following table describes the supported database attributes. The following code provides an example on how to create a database named DB1. The data will be deleted after 60 days.

```
CREATE DATABASE DB1 WITH (ttl=60);
```

##### CREATE TABLE

This topic describes the syntax that is used to create a time series table.

| Parameter | Description |
|---|---|
| tag name _ | The name of the tag column. The data type of the column is set to VARCHAR. You must use TAG to explicitly identify the name of the tag column. Otherwise, LindormTSDB treats the specified column as a field column. You are not required to declare the data type of the tag column. |
| time column name _ _ | The name of the timestamp column. You must set the data type of the column to TIMESTAMP. Timestamps supported by LindormTSDB are accurate to milliseconds. |
| field name _ | The names of the field columns. The following data types are supported: BIGINT, DOUBLE, VARCHAR, and BOOLEAN. |

```json
create_table_statement ::= CREATE TABLE table_name '('
                              tag_definition
                              ( ',' tag_definition )*
                              ( ',' time_definition)?
                              ( ',' field_definition )*
                              [',' primary_key_definition]
                              ')'
tag_definition ::= tag_name [ VARCHAR ] TAG time_definition ::= time_column_name TIMESTAMP field_definition ::= field_name TYPE primary_key_definition ::= PRIMARY KEY '(' tag_name [',' tagname]* ')'
```

**Usage notes**

Before you write data to LindormTSDB, create a table and specify the data types of the columns. For more information, see Design a time series table. A primary key in a database of LindormTSDB is used for a different purpose than a primary key in a relational database. A primary key in LindormTSDB is used to specify a data sharding rule for a time series table. The column names that you specify for PRIMARY KEY must be included in the tag column names that you specify for `tag_definition` . PRIMARY KEY is introduced in the syntax of LindormTSDB V3.4.9 or later.

**Note**

Single-node Lindorm instances do not support primary keys. To use primary keys, use Lindorm clusters. A column that stores unique identifiers (UIDs) of a data source is commonly used as a primary key. For example, a column that stores device IDs is commonly used as a primary key in IoT scenarios, a column that stores vehicle IDs is commonly used as a primary key in Internet of vehicles (IoV) scenarios, and a column that stores application IDs or ip:port is commonly used in monitoring scenarios. For more information, see the Best practice for designing primary keys section of the Design a time series table topic. You want to create a time series table named sensor and specify the device_id column and the region column as tag columns, and specify the temperature column and humidity column as field columns. You want to explicitly specify the device_id column as the primary key of the table because the instantaneous data of a single device is queried in most scenarios. You can execute the following CREATE TABLE statement to create the table:

| Parameter | Description |
|---|---|
| user name _ | The username. The value can be an SQL constant or identifier. |
| password definition _ | The password. The value must be an SQL constant of the VARCHAR type. |

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time   TIMESTAMP,
    temperature DOUBLE,
    humidity DOUBLE,
    PRIMARY KEY(device_id));
```

##### CREATE USER

This topic describes the syntax that is used to create a user.

```
create_user_statement ::= CREATE USER [IF NOT EXISTS] user_name IDENTIFIED BY password_definition
```

**Parameters**

**Important**

If the username already exists and IF NOT EXISTS is not specified in the statement, the system throws an error. When IF NOT EXISTS is specified in the statement, the system does not throw an error but aborts the creation process. In the following example, a user named `tsdbuser` is created. The password that corresponds to the username is `asdf1234` .

```
CREATE USER IF NOT EXISTS `tsdbuser` IDENTIFIED BY 'asdf1234';
```

##### CREATE CONTINUOUS QUERY

This topic describes the SQL syntax that is used to create a continuous query.

```
create_cq_statement ::= CREATE CONTINUOUS QUERY [database_name.] cq_name WITH ( cq_attribute_statement ) AS insert_select_statement cq_attribute_statement ::= attribute_definition (',' attribute_definition)* attribute_definition ::= attr_name '=' attr_val
```

**Parameters**

**database_name**

| Attribute | Description |
|---|---|
| interval | Specifies the interval at which queries are continuously performed. The interval is accurate to seconds. The interval must be in the following format: %d%h%m%s. For example, a value of 1h30s specifies an interval of 1 hour and 30 seconds, and a value of 1d specifies an interval of 1 hour. Where: d: days h: hours m: minutes s: seconds |
| window | The time window of the data that is queried each time. This attribute is optional. If you do not specify this attribute, the value is the same as the value of the interval attribute. The format of this attribute is the same as that of the interval attribute. For example, if you set the interval attribute to 10m and the window attribute to 20m, continuous queries are performed every 10 minutes and data within the previous 20 minutes is queried each time. The time window is a left-closed and right-open interval. |

The name of the database on which you want to perform a continuous query. If you do not specify this parameter, the continuous query is performed on the current database. The specified database name must be an SQL constant or an SQL identifier.

**cq_name**

The name of the continuous query that you want to perform. The attributes of the continuous query that you want to perform. The following table describes the attributes that you can configure.

**Important**

When you specify insert_select_statement, you do not need to specify a time range for your query. In this case, LindormTSDB queries data within the specified time window. The following example shows how to create a continuous query. In this example, a continuous query is created to query the average temperature and humidity per hour within the previous two hours by scanning the sensor table in the db_sensor database. The results are inserted to a table named `sensor` in the `db_sensor_year` database.

```
CREATE CONTINUOUS QUERY `db_sensor`.`my_cq` WITH (INTERVAL='1h', WINDOW='2h') AS SELECT MEAN(`temperature`) AS `temperature`,
       MEAN(`humidity`) AS `humidity`, `device_id`, `region`
FROM `db_sensor`.`sensor` SAMPLE BY 1h;
```

##### ALTER DATABASE

This topic describes the syntax that is used to modify the attributes of a database.

| Parameter | Description |
|---|---|
| attribute statement _ | The additional attributes of the database. |
| attr name _ | The name of the attribute. The name must be an SQL constant or an SQL identifier. |
| attr val _ | The value of the attribute. The value must be a SQL constant. |

| Parameter | Description |
|---|---|
| table name _ | The table name. |
| column name _ | The column name. |

```
alter_database_statement ::= ALTER DATABASE database_name [ WITH attribute_statement ] attribute_statement ::= '(' attribute_definition (',' attribute_definition)* ')' attribute_definition ::= attr_name '=' attr_val
```

**Parameters**

**Note**

For more information about the database attributes that are supported by this statement, see CREATE DATABASE.

**Important**

You can use the ALTER DATABASE statement to modify only database attributes. You cannot use this statement to modify database names. The following example shows how to change the time to live (TTL) value of the DB1 database to 40 days.

```
ALTER DATABASE DB1 WITH (ttl=40);
```

##### ALTER TABLE

This topic describes the syntax that is used to modify the structure of a time series table.

```
alter_table_statement ::= ALTER TABLE table_name alter_option ( ',' alter_option )* alter_option ::= ADD | ALTER [COLUMN] column_definition column_definition ::= column_name TYPE [TAG]
```

**Parameters**

| Parameter | Description |
|---|---|
| configuration name _ | The name of the dynamic configuration parameter. The name must be a SQL identifier. |
| configuration value _ | The value of the dynamic parameter. The value must be a SQL constant. The data type of the SQL constant can be BIGINT, DOUBLE, BOOLEAN, or VARCHAR based on the dynamic parameter that you want to modify. |

| Parameter | Data type | Description |
|---|---|---|

**Important**

1. You can use the ALTER TABLE statement to perform the following operations:
i. Add columns. You can add only tag or field columns. ii. Change the data type of field columns. The data type of tag and timestamp columns cannot be changed.
2. A tag column that is added to a table cannot be specified as the primary key.
3. After you change the data type of a field column, the type of the existing data in the column
remains unchanged. However, the system considers that all data in the column is converted to the specified data type. As a result, the system may fail to retrieve the existing data in the column when the system processes queries. The following example shows how to add a field column named `co` to the `aqm` table:

```
ALTER TABLE aqm ADD co DOUBLE;
```

The following example shows how to add a tag column named `region` to the `aqm` table:

```
ALTER TABLE aqm ADD region VARCHAR TAG;
```

The following example shows how to change the data type of the `co` column in the `aqm` table to BIGINT:

```
ALTER TABLE aqm ALTER COLUMN co BIGINT;
```

##### ALTER SYSTEM

This topic describes the syntax that is used to modify information about a system-level dynamic configuration parameter.

```
alter_system_statement ::= ALTER SYSTEM SET configuration_name = configuration_value;
```

**Parameters**

**The following table describes the dynamic parameters that can be**

**modified by using the ALTER SYSTEM statement.**

| USER AUTH _ | boolean | Specifies whether to enable the user authentication feature for LindormTSDB. Valid values: TRUE Enables user authentication. If this feature is enabled, you must provide your username and password when you connect to LindormTSDB. LindormTSDB verifies your identity and the data objects in the SQL query that is sent over the connection. FALSE Disables user authentication. If this feature is disabled, you can connect to LindormTSDB without the need to provide your username and password. Default value: FALSE. |
|---|---|---|

| Parameter | Description |
|---|---|
| user name _ | The username used to connect to LindormTSDB. The value can be an SQL constant or identifier. |
| password definition _ | The password of the user. The value must be an SQL constant of the VARCHAR type. |

Enable user authentication and permission verification

```
ALTER SYSTEM SET USER_AUTH=TRUE;
```

After the user authentication and permission verification feature is enabled for LindormTSDB, user credentials are required for all subsequent requests. If you do not specify user credentials in a request, the request may fail the authentication. You must also specify user credentials when you execute the `ALTER SYSTEM` statement to enable the user authentication and permission verification feature. After the user authentication and permission verification feature is enabled, some existing services may become inaccessible. Therefore, we recommend that you carefully plan and fully evaluate the impacts before you enable this feature. After the user authentication and permission verification feature is enabled, you can execute the following ALTER SYSTEM statement to disable the feature: ALTER SYSTEM SET USER_AUTH=FALSE; To check whether the user authentication and permission verification feature is enabled for your instance, run the following SHOW PARAMETER statement: SHOW PARAMETER USER_AUTH; Disable user authentication and permission verification

```
ALTER SYSTEM SET USER_AUTH=FALSE;
```

##### ALTER USER

This topic describes the syntax that is used to change the password of a user.

```
alter_user_statement ::= ALTER USER [IF EXISTS] user_name SET PASSWORD '=' password_definition [ WH ERE OLDPASSWORD '=' password_definition];
```

**Parameters**

| Parameter | Description |
|---|---|

**Important**

1. For example, you want to change the password of a user whose username does not exist. If you do
not specify IF EXISTS, an error message notifies you that the username does not exist. If you specify IF EXISTS, no error is reported, and the task for changing the password is stopped.
2. If you want to change the password of the username that is used to connect to LindormTSDB, you
must specify `WHERE OLDPASSWORD = password_definition` to perform password verification.
3. You can execute the ALTER USER statement to change only the password of a user. If you want to
change the username of a user, you must execute the DROP USER statement to delete a user and execute the CREATE USER statement to create a user. The following sample code provides an example on how to change the password of `tsdbuser` to `newpassword` after another user who has global administrator permissions is connected to LindormTSDB:

```
ALTER USER IF EXISTS `tsdbuser` SET PASSWORD = 'newpassword';
```

The following sample code provides an example on how to change the password of `tsdbuser` to `newpassword` after tsdbuser connects to LindormTSDB:

```
ALTER USER `tsdbuser` SET PASSWORD = 'newpassword' WHERE OLDPASSWORD = 'asdf1234';
```

##### DROP DATABASE

This topic describes the syntax that is used to drop a database.

```
drop_database_statement ::= DROP DATABASE database_name;
```

**Important**

You cannot drop the `default` database. The following code provides an example on how to drop a database named DB1:

```
DROP DATABASE DB1;
```

##### DROP TABLE

This topic describes the syntax that is used to delete tables and the parameters that you can configure.

```
drop_table_statement ::= DROP TABLE [IF EXISTS] table_name;
```

**Parameters**

| table name _ | The name of the time series table that you want to delete. The value can be an SQL constant or identifier. |
|---|---|

| Parameter | Description |
|---|---|
| user name _ | The username. The username can be an SQL constant or identifier. |

**Important**

After a table is deleted by using the DROP TABLE syntax, the storage space occupied by the table is not immediately released. You can configure a TTL for the database to permanently delete a table. For more information about how to configure a TTL for a database, see ALTER DATABASE. Before you permanently delete data by setting the TTL attribute, take note of the following items: In LindormTSDB, TTLs can be specified only for databases but not for tables. Therefore, when you configure a TTL for a database to permanently delete a table, make sure that other data in the database are not deleted due to the TTL setting. You can execute the following statement to delete a table named sensor:

```
DROP TABLE IF EXISTS `sensor`;
```

##### DROP USER

This topic describes the syntax that is used to delete a user.

```
drop_user_statement ::= DROP USER [IF EXISTS] user_name;
```

**Parameters**

**Important**

If the name of the user that you want to delete does not exist and IF EXISTS is not specified in the statement, the system throws an error. When IF EXISTS is specified in the statement, the system does not throw an error but aborts the deletion process. The following example shows how to delete a user named `tsdbuser` .

```
DROP USER IF EXISTS `tsdbuser`;
```

##### DROP CONTINUOUS QUERY

This topic describes the SQL syntax that is used to delete a continuous query.

| Parameter | Description |
|---|---|
| databasename _ | The name of the database in which you want to perform a continuous query. If you do not specify this parameter, the continuous query is performed in the current database. |
| cqname _ | The name of the continuous query that you want to perform. |

| Column | Type |
|---|---|
| attribute | VARCHAR |
| value | VARCHAR |

```
drop_cq_statement ::= DROP CONTINUOUS QUERY [database_name.]cq_name
```

**Parameters**

The following sample code shows how to delete the continuous query that is created in the CREATE CONTINUOUS QUERY topic:

```
DROP CONTINUOUS QUERY `db_sensor`.`my_cq`;
```

##### DESCRIBE DATABASE

This topic describes the syntax that is used to query the attributes of a database.

```
describe_database_statement ::= DESCRIBE DATABASE database_name;
```

The DESCRIBE DATABASE statement returns a result set as a table. The following table describes the schema of a table that is returned. The following sample code provides an example on how to query the attributes of a database named DB1:

```
DESCRIBE DATABASE DB1; +-----------+-------+
| attribute | value |
+-----------+-------+
| ttl       |    60 |
+-----------+-------+
```

##### DESCRIBE TABLE

This topic describes the syntax that is used to query information about the schema of a time series table.

| Column name | Type | Result description |
|---|---|---|
| columnName | VARCHAR | The name of column in the table. |
| typeName | VARCHAR | The data type of the column in the table. |
| columnKind | VARCHAR | The type of the column in the table. The type of a column is determined by the statement that is used to create the corresponding table. Valid values: TAG: indicates that the column is a tag column. TIMESTAMP: indicates that the column is a timestamp column. A time series table contains only one timestamp column. FIELD: indicates that the column is a field column. All columns other than timestamp and tag columns are field columns. A field column is used to record the event data that is reported. |

```
describe_table_statement ::= DESCRIBE TABLE table_name
```

After the DESCRIBE TABLE statement is executed, the result set is returned in a table. The following table describes the schema of the returned table.

```
> DESCRIBE TABLE sensor;
+-------------+-----------+------------+
| columnName  | typeName  | columnKind |
+-------------+-----------+------------+
| device_id   | VARCHAR   | TAG        |
| region      | VARCHAR   | TAG        |
| time        | TIMESTAMP | TIMESTAMP  |
| temperature | DOUBLE    | FIELD      |
| humidity    | BIGINT    | FIELD      |
+-------------+-----------+------------+
```

##### SHOW

This topic describes the syntax that is used to query the metadata of a specified object in LindormTSDB.

```
show_statement ::= SHOW target_statement target_statement ::= { DATABASES | TABLES | USERS | PRIVILEGES }
```

| Column name | Type | Result description |
|---|---|---|
| database | VARCHAR | This column stores the names of all databases in the current Lindorm cluster. |

| Column name | Type | Result description |
|---|---|---|
| Tables In ${Database name} _ _ | VARCHAR | This column stores the names of all tables in the current database. If you want to query the tables in other databases, execute the USE statement to switch to the database that you want to query. |

| Column name | Type | Result description |
|---|---|---|
| name | VARCHAR | This column stores the names of all users of the current Lindorm cluster. |

| Column name | Type | Result description |
|---|---|---|
| user | VARCHAR | This column stores the names of the users that have full permissions. |
| global privileges | VARCHAR | This column stores the names of the users that have global permissions. |

**Note**

1. The following objects are supported by the SHOW statement:
DATABASES: query all databases in the current Lindorm cluster. TABLES: query all time series tables in the current Lindorm cluster. USERS: query all users of the current Lindorm cluster. PRIVILEGES: query the permissions of the users of the current Lindorm cluster.
2. The permissions that are required to execute the SHOW statement vary based on the object that is
specified in the statement. The result sets of SHOW statements are organized in tables and returned. The following table describes the result sets of SHOW statements that are executed to query different objects.

**SHOW DATABASES**

**SHOW PRIVILEGES**

| database privileges | VARCHAR | This column stores the names of the users that have database-level permissions. |
|---|---|---|
| table privileges | VARCHAR | This column stores the names of the users that have table-level permissions. |

**Note**

1. The data in the permission columns is displayed in JSON format. This way, applications can directly
process the data. JSON data is stored as key-value pairs. key: the name of the object that is queried, such as a database name or table name. The key for global permissions is fixed to `GLOBAL` . value: the list of permissions. The Example section shows the details. If the queried users do not have the permissions of the specified level, an empty JSON string is returned.
2. LindormTSDB does not support table-level permission control.
The following example shows how to query all databases in the current Lindorm cluster:

```
> SHOW DATABASES;
+----------+ +----------+
| default  |
| metadata |
+----------+ 2 rows in set (13 ms)
```

The following example shows how to query all time series tables in the current Lindorm cluster:

```
> SHOW TABLES;
+-------------+------------+
| tableSchema | tableName  |
+-------------+------------+
| default     | sensor     |
| metadata    | COLUMNS    |
| metadata    | TABLES     |
+-------------+------------+
```

The following example shows how to query all users of the current Lindorm cluster:

```
> SHOW USERS;
+-----------+
|   name    |
+-----------+
| testuser  |
| dbwriter  |
| root      |
+-----------+ 3 rows in set (11 ms)
```

| Parameter | Description |
|---|---|
| configuration name _ | The name of the dynamic configuration parameter. The specified name must be an SQL identifier. |

The following example shows how to query the permissions of the users of the current Lindorm cluster:

```
> SHOW PRIVILEGES;
+------------+-------------------------------------+--------------------------------------+---------- ------+
|    user    |          global privileges          |         database privileges          | table pri
vileges | +------------+-------------------------------------+--------------------------------------+---------- ------+
| testuser   | {"GLOBAL":["READ"]}                 | {}                                   | {}
```

|

```
| dbaccessor | {"GLOBAL":["ADMIN","READ","WRITE"]} | {"DB2":["READ"],"default":["WRITE"]} | {}
```

|

```
+------------+-------------------------------------+--------------------------------------+---------- ------+
```

##### SHOW PARAMETER

This topic describes the syntax that is used to query information about a system-level dynamic configuration parameter.

```
show_parameter_statement ::= SHOW PARAMETER configuration_name
```

**Parameters**

**Note**

1. The SHOW PARAMETER statement is frequently used in combination with the ALTER SYSTEM
statement.
2. For information about dynamic configuration parameters that are supported by the SHOW
PARAMETER statement, see ALTER SYSTEM. The following sample code provides an example on how to query the value of USER_AUTH:

```
> SHOW PARAMETER USER_AUTH;
+-----------+
| USER_AUTH |
+-----------+
| FALSE     |
+-----------+ 1 rows in set (48 ms)
```

##### SHOW CONTINUOUS QUERIES

This topic describes the syntax that is used to query the existing continuous queries that run on the current database.

| Column name | Type | Result description |
|---|---|---|
| name | VARCHAR | The name of the continuous query. |
| interval | VARCHAR | The interval at which the continuous query is performed. This value is specified by the interval string _ parameter in the CREATE CONTINUOUS QUERY statement. |
| query | VARCHAR | The statement that is executed in the continuous query. |

```
show_cq_statement
```

**Note**

This statement displays all existing continuous queries that run on the current database. If you want to query the continuous queries that run on a different database, execute the USE statement to switch to the database. Display all continuous queries that run on the current database.

```
SHOW CONTINUOUS QUERIES; +-------+----------+--------------------------------+ +-------+----------+--------------------------------+
|       |          | `db_sensor_year`.`sensor`      |
|       |          | AS `temperature`,              |
|       |          | MEAN(`humidity`) AS          |
|       |          | `humidity`, `device_id`,       |
|       |          | `region` FROM                  |
|       |          | `db_sensor_month`.`sensor`)    |
+-------+----------+--------------------------------+ 1 rows in set (66 ms)
```

##### USE

This topic describes the SQL syntax that is used to switch to the destination database.

```
use_statement
   ::= USE database_name;
```

**Parameters**

| Parameter | Description |
|---|---|
| database name _ | The name of the destination database to which you want to switch. The following requirements must be met: The destination database exists. The name of the destination database must be an SQL constant or identifier. |

| Column name | Type | Description |  |  |
|---|---|---|---|---|
| ID | VARCHAR | The ID of the SQL statement that is being executed. To terminate the SQL statement, execute KILL QUERY '<ID>' . |  |  |
|  |  |  | KILL QUERY |  |
| USER | VARCHAR | The user who submits the SQL statement. |  |  |
| HOST | VARCHAR | The server on which the SQL statement is executed. |  |  |
| DB | VARCHAR | The database that stores the data queried by the SQL statement. |  |  |
| TYPE | VARCHAR | The type of the SQL statement. Example: SELECT and CREATE. |  |  |
| CREATED | VARCHAR | The time when the SQL statement is created. |  |  |
| SQL | VARCHAR | The SQL statement that is being executed. |  |  |

|  | '<ID>' |
|---|---|

**Note**

After you explicitly specify the destination database in the USE statement, if you do not explicitly specify the name of the database to which a database object, such as a time series table, belongs when you specify the database object in an SQL query, the database object is searched from the database in the current context by default. When you use Lindorm-cli or Java Database Connectivity (JDBC) to establish a connection to access LindormTSDB, you need to specify a database name in the connection string. This way, the database can be accessed by default. In this case, if you execute the USE statement, the database is switched based on the context of the current connection.

##### SHOW PROCESSLIST

This topic describes the syntax that is used to query the SQL statements that are being executed.

**Returned result**

The following table describes the columns that are included in the execution results of `SHOW`

```
PROCESSLIST .
```

You can execute the following statement to query the SQL statements that are being executed: The following results are returned:

| Parameter | Description |
|---|---|
| id | The ID of the SQL statement that you want to terminate. You can execute the SHOW PROCESSLIST statement to query the ID of an SQL statement. For more information, see SHOW PROCESSLIST. |

| Parameter | Description |
|---|---|
| interval | The interval at which time series data is aggregated. The value of this parameter is a positive integer. |
| units | The unit of the interval. Valid values: s (seconds), m (minutes), h (hours), and d (days). |

```
+-------------------------------------------------+------+----------+------+---------+--------------- --------------+--------------------------------+
|                       ID                        | USER |   HOST   |  DB  |  TYPE   |            CRE
TED | SQL | +-------------------------------------------------+------+----------+------+---------+--------------- --------------+--------------------------------+
| dHNkYi0x@2a2adf60-89d8-4d16-8417-455189644070@1 | root | dHNkYi0x | null | UNKNOWN | 2022-07-08T1
|                                                 |      |          |      |         |
| `value` FROM `cpu_user`        |
+-------------------------------------------------+------+----------+------+---------+--------------- --------------+--------------------------------+ 1 rows in set (112 ms)
```

##### KILL QUERY

This topic describes the syntax that is used to terminate an SQL statement that is being executed.

**Parameters**

```
KILL QUERY 'dHNkYi0x@2a2adf60-89d8-4d16-8417-455189644070@1'
```

##### CREATE PREDOWNSAMPLE

This topic describes the syntax used to create pre-downsampling rules. Lindorm generates predownsampled data based on the pre-downsampling rules that you create.

```
create_predownsample_statement ::= CREATE PREDOWNSAMPLE time_interval
                                    AGGREGATORS '('function_name ( ',' function_name) ')'
                                    [ TTL time_interval ]
                                    ON table_name
time_interval ::= interval units
```

**Parameters**

| function name _ | The name of the aggregate function. For more information about the aggregate functions supported in pre-downsampling, see Supported aggregate functions. Note You can specify one or more aggregate functions with the same interval in a single statement. You can also specify multiple aggregate functions in multiple statements. |
|---|---|
| TTL | The time to live (TTL) of the pre-downsampled data. Note If you specify different TTLs in multiple pre-downsampling rules, the largest TTL apply to all pre-downsampling rules. |
| table name _ | The name of the table for which you want to configure pre-downsampling rules. |

| Function | Description |
|---|---|
| count | Returns the total number of pre-downsampled data points. |
| first | Returns the value of the first pre-downsampled data point. |
| last | Returns the value of the last pre-downsampled data point. |
| min | Returns the minimum value of the pre-downsampled data points. |
| max | Returns the maximum value of the pre-downsampled data points. |
| sum | Returns the sum of the values of pre-downsampled data points. |

By default, when you query pre-downsampled data, the original data before pre-downsampling is queried. To query only pre-downsampled data, you must add the `/*+ PREDOWNSAMPLE */` hint in the query statements.

**Note**

The avg function is not supported in pre-downsampling. You can calculate the average of pre-downsampled data based on the results of the count and sum functions. However, if data is overwritten, the average may be inaccurate.
1. Create a pre-downsampling rule and set the TTL of pre-downsampled data to 90 days.

```
CREATE PREDOWNSAMPLE `1h` AGGREGATORS (`sum`, `max`) TTL `90d` ON sensor;
```

2. Query data that is pre-downsampled on an hourly basis.

```
SELECT /*+ PREDOWNSAMPLE */ SUM(temperature) FROM sensor WHERE time >= 1619076780000 AND time <= 1619076800000 SAMPLE BY 1h;
```

##### SHOW PREDOWNSAMPLES

This topic describes the syntax used to query the pre-downsampling rules configured for all tables or a specified table.

| Parameter | Required | Description |
|---|---|---|
| table name _ | No | The name of the time series table whose pre-downsampling rules you want to query. |

| Parameter | Description |
|---|---|
| interval | The interval at which time series data is aggregated. The value of this parameter must be a positive integer. |
| units | The unit of the interval. Valid values: s (seconds), m (minutes), h (hours), and d (days). |

**Parameters**

Example 1: Query the pre-downsampling rules configured for all tables. The following results are returned:

```
+--------+ -------------- +------------+-----+ ------------------ +
| table  | interval | aggregator | ttl | update_time          |
+--------+----------+------------+-----+----------------------+
| sensor | 1h       | sum, max   | 90d | 2021-10-10T08:00:00Z |
| sensor | 5m       | sum, max   | 30d | 2021-10-10T08:00:00Z |
| test   | 1m       | sum, max   | 30d | 2021-10-10T08:00:00Z |
| test   | 2h       | sum, max   | 30d | 2021-10-10T08:00:00Z |
+--------+----------+------------+-----+----------------------+
```

Example 2: Query the pre-downsampling rules configured for the table named sensor. The following results are returned:

```
+--------+ -------------- +------------+-----+ ------------------ +
| table  | interval | aggregator | ttl | update_time          |
+--------+----------+------------+-----+----------------------+
| sensor | 1h       | sum, max   | 90d | 2021-10-10T08:00:00Z |
| sensor | 5m       | sum, max   | 30d | 2021-10-10T08:00:00Z |
+--------+----------+------------+-----+----------------------+
```

##### DROP PREDOWNSAMPLE

This topic describes the syntax used to delete the pre-downsampling rules that are configured for a specified table.

```
drop_predownsample_statement ::= DROP PREDOWNSAMPLE time_interval
                                    AGGREGATORS '('function_name ( ',' function_name) ')' ON
table_name time_interval ::= interval units
```

**Parameters**

| function name _ | The name of the aggregate function. For more information about the aggregate functions supported in pre-downsampling, see the Supported aggregate functions section of this topic. Note You can specify one or more aggregation functions with the same interval in a single statement. You can also specify multiple aggregation functions in multiple statements. |
|---|---|
| table name _ | The name of the time series table. |

| Parameter | Description |
|---|---|
| tag name _ | The tag names of the data that you want to write. The tag names must be consistent with the names of the tags that are specified in the CREATE TABLE statement. All tags specified in the CREATE TABLE statement must be specified in this parameter. This parameter is required. |
| time | The time when the data is written. The value of this parameter must be a positive integer. Unit: milliseconds. This parameter is required. |
| field name _ | The name of the column to which data is written. We recommend that you specify a column whose data type is the same as that specified in the CREATE TABLE statement. Otherwise, the type of the data that is most recently written to the column prevails. If a column is not specified, the value in this column is set to null by default. |

```
DROP PREDOWNSAMPLE `1d` AGGREGATORS (`sum`, `max`) ON sensor;
```

#### DML

##### Write data to LindormTSDB

This topic describes the SQL syntax that is used to write data to LindormTSDB.

```
                              tag_name
                              (',' tag_name)*
                              ',' time ','
                              field_name
                              (',' field_name)*
                           ')' VALUES
                           ('('
                              (',' tag_value)*
                              ',' time_value ','
                              field_value
                              (',' tag_value)*
                           ')')+
```

**Parameters**

**Important**

In LindormTSDB, existing data is overwritten when new data with the same timestamp is written to the table. When you execute the INSERT statement to write a row of data, if the time series of the row exists in the table and the timestamp of the data is the same as the timestamp of the existing data in the time series, the existing row is overwritten by the inserted row. You can execute the following statements to write each single row of data to a time series table in sequence:

```
insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076780000,12.1,45); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076790000,13.2,47); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076800000,10.6,46); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1261','south-cn', 1619076780000,18.1,44); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1261','south-cn', 1619076790000,19.7,44);
```

You can also execute the following statement to write multiple rows of data to a time series table in a batch:

```
insert into sensor (device_id, region, time, temperature, humidity) values
    ('F07A1260','north-cn',1619076780000,12.1,45),
    ('F07A1260','north-cn',1619076790000,13.2,47),
    ('F07A1260','north-cn',1619076800000,10.6,46),
    ('F07A1261','south-cn',1619076780000,18.1,44),
    ('F07A1261','south-cn',1619076790000,19.7,44);
```

##### Basic syntax of the SELECT statement

This topic describes the basic syntax of the SELECT statement.

```
                      FROM table_name
                      WHERE where_clause
                      [ SAMPLE BY time_interval [ OFFSET offset_interval ] [ FILL fill_option ] ]
                      [ GROUP BY group_by_clause ]
                      [ ORDER BY ordering_clause ]
                      [ LIMIT integer [ OFFSET integer ] ]
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] )
                      | field_name
                      | COUNT '(' '*' ')'
where_clause ::= relation ( ( AND | OR ) relation )* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | CONTAINS | CONTAINS KEY group_by_clause ::= field_name ( ',' field_name )* ordering_clause ::= field_name [ ASC | DESC ] ( ',' field_name [ ASC | DESC ] )*
```

**Usage notes**

You must specify a time range in the SELECT statement. For example, you can specify a time range in the `time > xxx and time < xxx` format. The LIMIT clause is used to filter the results that are returned by the SELECT statement. We recommend that you add more conditions in the WHERE clause to reduce the number of data points that are scanned because the LIMIT clause is not efficient in data filtering. Query the number of data records that are reported by the device whose ID is `F07A1260` at the specified point in time.

```
SELECT count(*) FROM sensor WHERE device_id = 'F07A1260' AND time = '2021-04-22 15:33:00'; +--------+
| EXPR$0 |
+--------+
| 1      |
+--------+ 1 rows in set (97 ms)
```

Query all metrics of the device whose ID is `F07A1260` with the specified time range.

```
SELECT * FROM sensor WHERE device_id = 'F07A1260' AND time >= '2021-04-22 15:33:00' AND time < '2 021-04-22 15:33:20'; +-----------+----------+---------------------------+-------------+-----------+
| device_id |  region  |           time            | temperature | humidity  |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260  | north-cn | 2021-04-22T15:33:00+08:00 | 12.100000   | 45.000000 |
| F07A1260  | north-cn | 2021-04-22T15:33:10+08:00 | 13.200000   | 47.000000 |
+-----------+----------+---------------------------+-------------+-----------+ 2 rows in set (57 ms)
```

Query all values of the `device_id` field in the `sensor` table.

```
SELECT DISTINCT device_id FROM sensor; +----------+
|          |
+----------+
| F07A1260 |
+----------+ 1 rows in set (114 ms)
```

Query the maximum temperature of the device whose ID is `F07A1260` within the specified time range.

```
SELECT max(temperature) AS max_temp FROM sensor WHERE device_id = 'F07A1260' AND time >= '2021-04 -22 15:33:00' AND time < '2021-04-22 15:33:20'; +-----------+
| max_temp  |
+-----------+
| 13.200000 |
+-----------+ 1 rows in set (103 ms)
```

##### Downsampling queries

A downsampling query is an aggregate query that is performed based on a specified time interval. Downsampling queries are performed to decrease the sample rate in time series scenarios. This topic describes the syntax supported by LindormTSDB to perform downsampling queries.

**Prerequisites**

The version of LindormTSDB is 3.4.15 or later.

| Function | Description |
|---|---|
| SUM | Returns the sum of values that are collected within each time window. For more information, see SUM. |
| AVG | Returns the average value that is calculated based on values that are collected within each time window. For more information, see AVG. |
| COUNT | Returns the number of values that are collected within each time window. For more information, see COUNT. |
| MIN | Returns the minimum value that is collected within each time window. For more information, see MIN. |
| MAX | Returns the maximum value that is collected within each time window. For more information, see MAX. |

```
select_sample_by_statement ::= SELECT ( select_clause | '*' )
                                FROM table_name
                                WHERE where_clause
                                SAMPLE BY time_interval [ OFFSET offset_interval ] [ FILL
fill_option ] select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] ) selector ::= tag_name | time | function_name '(' field_name [ ',' function_args ] ')' where_clause ::= relation ( AND relation )* (OR relation)* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | CONTAINS | CONTAINS KEY time_interval ::= interval units | 0 offset_interval ::= interval units
```

The following fields can be specified for the `time_interval` parameter: `interval:` an exponential value that is an integer, such as 5 and 60. The value of the interval parameter specifies the time window in which a time series is aggregated. `units:` the unit of the interval. The following units are supported: s (second), m (minute), h (hour), d (day), n (month), and y (year).

**Note**

By default, modulo operations are performed to align timestamps. Timestamps are aligned based on the following formula: Aligned timestamp = Timestamp when data is generated - (Timestamp when data is generated % Value of interval). You can downsample data based on a calendar time interval. To specify a calendar time interval, append c to the value of **units**. For example, `1dc` specifies the 24-hour period from 00:00:00 on the current day to 00:00:00 on the next day, and 1nc specifies the calendar month from 00:00:00 on the first day of the current month to 00:00:00 on the first day of the next month.

**Aggregate functions supported for downsampling queries**

The `SAMPLE BY` is a downsampling operation for each independent timeline. The following table lists the functions supported by `SAMPLE BY` .

| FIRST | Returns the first value that is collected within each time window. For more information, see FIRST. |
|---|---|
| LAST | Returns the last value that is collected within each time window. For more information, see LAST. |
| PERCENTILE | Returns the specified percentile of values that are collected within each time window. For more information, see PERCENTILE. |
| LATEST | Returns the latest values that are collected within a time window. For more information, see LATEST. |
| RATE | Returns the change rate of the value in the current data point compared with the value of the previous data point. For more information, see RATE. |
| DELTA | Returns the difference between the value of the current data point and the value in the previous data point. For more information, see DELTA. |

You do not need to specify a function for downsampling in the SELECT statement to query data from the tag column of a table. If you want to query data from non-tag columns, you must specify a function for downsampling. The following code provides a sample statement that is executed to query data from a table named sensor and the sample results that are returned:

```
SELECT * FROM sensor; +-----------+----------+---------------------------+-------------+-----------+
| device_id |  region  |           time            | temperature | humidity  |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260  | north-cn | 2021-01-01T09:00:00+08:00 | 0.000000    | 9.000000  |
| F07A1260  | north-cn | 2021-01-01T12:01:00+08:00 | 1.000000    | 45.000000 |
| F07A1260  | north-cn | 2021-01-01T14:03:00+08:00 | 2.000000    | 46.000000 |
| F07A1260  | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000   | 47.000000 |
| F07A1261  | north-cn | 2021-02-10T12:00:30+08:00 | 3.000000    | 40.000000 |
| F07A1261  | north-cn | 2021-03-01T12:01:00+08:00 | 4.000000    | 41.000000 |
| F07A1261  | north-cn | 2021-03-08T12:08:00+08:00 | 5.000000    | 42.000000 |
| F07A1261  | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000    | 43.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

**Sample downsampling queries and downsampling queries that include**

**subqueries**

**Note**

Subqueries are not supported in downsampling queries. However, downsampling queries can be used as subqueries in other types of queries. Downsampling is performed at an interval that is specified based on the Coordinated Universal Time (UTC) time. The following statement is executed to aggregate time series based on an 8-hour interval and return the number of values that are collected in the humidity column within each time window.

```
SELECT device_id,region,time,count(humidity) AS count_humidity FROM sensor WHERE device_id='F07A1260' sample by 8h; +-----------+----------+---------------------------+----------------+
| device_id |  region  |           time            | count_humidity |
+-----------+----------+---------------------------+----------------+
| F07A1260  | north-cn | 2021-01-01T08:00:00+08:00 | 3              |
| F07A1260  | north-cn | 2021-01-01T16:00:00+08:00 | 1              |
+-----------+----------+---------------------------+----------------+
```

Downsampling is performed at an interval that is specified based on the UTC time and a specified time offset. The following statement specifies that time series are aggregated based on an 8-hour interval, the offset of the start time of each time window is 3 hours, and the number of values that are collected in the humidity column within each time window is calculated.

```
SELECT device_id,region,time,count(humidity) AS count_humidity FROM sensor WHERE device_id='F07A1260' sample by 8h offset 3h; +-----------+----------+---------------------------+----------------+
| device_id |  region  |           time            | count_humidity |
+-----------+----------+---------------------------+----------------+
| F07A1260  | north-cn | 2021-01-01T03:00:00+08:00 | 1              |
| F07A1260  | north-cn | 2021-01-01T11:00:00+08:00 | 2              |
| F07A1260  | north-cn | 2021-01-01T19:00:00+08:00 | 1              |
+-----------+----------+---------------------------+----------------+
```

Downsampling is performed at a monthly interval based on the local calendar.

```
SELECT device_id, time, count(temperature) FROM sensor WHERE device_id='F07A1261' sample by 1nc; +-----------+---------------------------+--------+
| device_id |           time            | EXPR$2 |
+-----------+---------------------------+--------+
| F07A1261  | 2021-02-01T00:00:00+08:00 | 1      |
| F07A1261  | 2021-03-01T00:00:00+08:00 | 2      |
| F07A1261  | 2021-05-01T00:00:00+08:00 | 1      |
+-----------+---------------------------+--------+
```

The SAMPLE BY clause cannot be used together with the GROUP BY clause, LIMIT OFFSET clause, or ORDER BY clause. You can include the GROUP BY clause, LIMIT OFFSET clause, and ORDER BY clause in SQL statements to specify subqueries.

```
SELECT device_id, max(avg_humidity) AS max_humidity FROM (SELECT device_id,region,time,avg(humidity) AS avg_humidity FROM sensor sample by 8h) group by device_id; +-----------+--------------+
| device_id | max_humidity |
+-----------+--------------+
| F07A1261  | 43.000000    |
| F07A1260  | 47.000000    |
+-----------+--------------+
```

You can use the LIMIT OFFSET clause to specify the number of results that you want to obtain.

```
SELECT device_id,region, avg_humidity FROM (select device_id,region,time,avg(humidity) AS avg_humidity FROM sensor sample by 8h) limit 1 offset 1; +-----------+----------+--------------+
| device_id |  region  | avg_humidity |
+-----------+----------+--------------+
| F07A1261  | north-cn | 40.000000    |
+-----------+----------+--------------+
```

**Sample interpolation queries**

You can interpolate a specified value based on a specified time interval. Example:

```
SELECT * from (select device_id,region,time, avg(humidity) AS humidity FROM sensor WHERE device_id='F07A1260' sample by 2h fill 1) order by device_id; +-----------+----------+---------------------------+-----------+
| device_id |  region  |           time            | humidity  |
+-----------+----------+---------------------------+-----------+
| F07A1260  | north-cn | 2021-01-01T08:00:00+08:00 | 9.000000  |
| F07A1260  | north-cn | 2021-01-01T10:00:00+08:00 | 1.000000  |
| F07A1260  | north-cn | 2021-01-01T12:00:00+08:00 | 45.000000 |
| F07A1260  | north-cn | 2021-01-01T14:00:00+08:00 | 46.000000 |
| F07A1260  | north-cn | 2021-01-01T16:00:00+08:00 | 1.000000  |
| F07A1260  | north-cn | 2021-01-01T18:00:00+08:00 | 1.000000  |
| F07A1260  | north-cn | 2021-01-01T20:00:00+08:00 | 47.000000 |
+-----------+----------+---------------------------+-----------+
```

You can interpolate the value that is collected within the previous time window. Example:

```
SELECT * from (select device_id,region,time,avg(humidity) AS humidity FROM sensor WHERE device_id='F07A1260' sample by 2h fill after) order by device_id; +-----------+----------+---------------------------+-----------+
| device_id |  region  |           time            | humidity  |
+-----------+----------+---------------------------+-----------+
| F07A1260  | north-cn | 2021-01-01T08:00:00+08:00 | 9.000000  |
| F07A1260  | north-cn | 2021-01-01T10:00:00+08:00 | 45.000000 |
| F07A1260  | north-cn | 2021-01-01T12:00:00+08:00 | 45.000000 |
| F07A1260  | north-cn | 2021-01-01T14:00:00+08:00 | 46.000000 |
| F07A1260  | north-cn | 2021-01-01T16:00:00+08:00 | 47.000000 |
| F07A1260  | north-cn | 2021-01-01T18:00:00+08:00 | 47.000000 |
| F07A1260  | north-cn | 2021-01-01T20:00:00+08:00 | 47.000000 |
+-----------+----------+---------------------------+-----------+
```

You can use the AVG function to perform downsampling at an interval of 2 hours and then use the `RATE` function to calculate the change rate of values between two data points. Example:

```
SELECT device_id,region,time,rate(avg(humidity)) AS rate_humidity FROM sensor WHERE device_id='F07A1260' sample by 2h; +-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | rate_humidity |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2021-01-01T12:00:00+08:00 | 0.002500      |
| F07A1260  | north-cn | 2021-01-01T14:00:00+08:00 | 0.000139      |
| F07A1260  | north-cn | 2021-01-01T20:00:00+08:00 | 0.000046      |
+-----------+----------+---------------------------+---------------+
```

| Fill Policy | Interpolated value |
|---|---|
| none | No values are interpolated. This is the default value. |
| zero | Interpolates the value 0. |
| linear | Performs linear interpolation. |
| previous | Interpolates the previous value. |
| near | Interpolates the adjacent value. |
| after | Interpolates the next value. |
| fixed | Interpolates a specified value. |

You can perform downsampling at an interval of 2 hours and then use the DELTA function to calculate the difference between the values of two data points. Example:

```
SELECT device_id,region,time,delta(avg(humidity)) AS humidity FROM sensor WHERE device_id='F07A1260' sample by 2h; +-----------+----------+---------------------------+-----------+
| device_id |  region  |           time            | humidity  |
+-----------+----------+---------------------------+-----------+
| F07A1260  | north-cn | 2021-01-01T12:00:00+08:00 | 36.000000 |
| F07A1260  | north-cn | 2021-01-01T14:00:00+08:00 | 1.000000  |
| F07A1260  | north-cn | 2021-01-01T20:00:00+08:00 | 1.000000  |
+-----------+----------+---------------------------+-----------+
```

**Interpolation**

During downsampling, all time series are split based on a specified time interval, and values of data points in each time window are aggregated. If no value is collected within a time window, a specified fill policy can be used to interpolate a value for the data point. For example, the timestamps of values that are collected in a time series after downsampling is complete are: t + 0, t + 20, and t + 30. If you do not specify conditions for interpolation in the query statement, only three values are returned. If you specify 1 for interpolation, four values are returned. The value 1 is interpolated as the value of the data point at t + 10. The following table describes the interpolation functions.

##### Query the latest values

This topic describes the syntax that is used to query the latest values of each time series in LindormTSDB.

```
select_latest_by_statement ::= SELECT ( select_clause )
                                FROM table_name
                                WHERE where_clause
                                SAMPLE BY 0
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] ) selector ::= tag_name | time | latest '(' field_name [ ',' integer ] ')' where_clause ::= relation ( AND relation )* (OR relation)* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN
```

**Note**

Latest-value queries are used to query the values of the latest time points in time series. You can use `latest(field_name, N)` to query the latest N records of data. A latest-value query must be used together with `SAMPLE BY 0` to query the latest values of each time series. Latest-value queries cannot be used together with other aggregate functions such as RATE, DELTA, MAX, or MIN. For example, if you execute the `select time, latest(f1), max(f2) from` `sensor sample by 0` statement, a syntax error occurs. For information about the `LATEST` function, see the LATEST section of the Common time series functions topic. Query the latest temperature of the device `F07A1260` and `F07A1261` :

```
lindorm> select device_id,region,time,latest(temperature) as temperature from sensor where device_i d in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+
| device_id | region |      time      | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  |
+-----------+----------+---------------------------+-------------+
```

Query the latest temperature and humidity records of the `F07A1260` device and the `F07A1261` device.

```
lindorm> select device_id,region,time,latest(temperature) as temperature, latest(humidity) as humid ity from sensor where device_id in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+-----------+
| device_id | region |      time      | temperature | humidity |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  | 47.000000 |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  | 43.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

When you use the LATEST function to query the latest values of multiple columns, null is displayed if the latest values of multiple columns cannot be aligned in time. The following statement provides an example:

```
lindorm> select device_id,region,time,latest(temperature) as temperature, latest(humidity) as humid ity from sensor where device_id in ('F07A1260') sample by 0; +-----------+----------+---------------------------+-------------+-----------+
| device_id | region |      time      | temperature | humidity |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260 | north-cn | 2021-01-01T12:00:00+08:00 | 15.200000  | null   |
| F07A1260 | north-cn | 2021-01-01T13:00:00+08:00 | null    | 47.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

Query the latest two temperature records of the `F07A1260` device and the `F07A1261` device.

```
lindorm> select device_id,region,time,latest(temperature, 2) as temperature from sensor where devic e_id in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+
| device_id | region |      time      | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260 | north-cn | 2021-01-01T14:03:00+08:00 | 2.000000  |
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  |
| F07A1261 | north-cn | 2021-03-08T12:08:00+08:00 | 5.000000  |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  |
+-----------+----------+---------------------------+-------------+
```

**Note**

Latest-value queries cannot be directly used with clauses such as OFFSET, LIMIT, or GROUP BY. You can use a latest-value query as a subquery in an SQL statement that contains these clauses. Use the LATEST function together with the GROUP BY clause to group returned data records.

```
lindorm> select device_id, max(temperature) as max_temperature from (select device_id, region,time, latest(temperature,2) as temperature from sensor sample by 0) group by device_id; +-----------+-----------------+
| device_id | max_temperature |
+-----------+-----------------+
| F07A1261 | 6.000000    |
| F07A1260 | 10.000000    |
+-----------+-----------------+
```

Use the LATEST function together with the LIMIT and OFFSET clauses to limit the number of data records that can be returned.

```
lindorm> select device_id, region, temperature from (select device_id, region, time, latest(temperature,2) as temperature from sensor sample by 0) limit 1 offset 1; +-----------+----------+-------------+
| device_id | region | temperature |
+-----------+----------+-------------+
| F07A1260 | north-cn | 10.000000  |
+-----------+----------+-------------+
```

##### Time series anomaly detection

This topic describes the algorithms and syntax that are used to detect time series anomalies.

| Parameter | Description |
|---|---|
| field name _ | The name of the field column. Note Data in the specified field column cannot be of the VARCHAR or BOOLEAN type. |

The time series anomaly detection syntax must be used together with the `SAMPLE BY` clause. Time series anomaly detection supports the online anomaly detection algorithms developed by DAMO Academy to detect abnormal points in the specified time series. During detection, these algorithms continuously learn the characteristics of time series data, such as data trends or periods, to detect anomalies in time series points that are newly inserted. For example, if the value of a newly added time series point is significantly different from other points, the algorithm assumes that this point may be abnormal. You can use time series anomaly detection with the `SAMPLE BY` clause by using the following methods: Use the `SAMPLE BY 0` clause to detect each data point in all time series. For more information about how to use the clause, see Example 1, Example 2, and Example 3. Use the `SAMPLE BY INTERVAL` clause to specify the downsampling interval and use nested downsampling operators, such as MIN, MAX, AVG, COUNT, and SUM.

**Important**

The value of **INTERVAL** cannot be 0. For more information about how to use the clause, see Example 4. Use the `SAMPLE BY 0` clause and nested downsampling operators, such as LATEST, DELTA, and RATE, to query different data. For more information about how to use the clause, see Example 5.

```
select_sample_by_statement ::= SELECT ( select_clause )
                                FROM table_name
                                WHERE where_clause
                                SAMPLE BY 0
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] ) selector ::= tag_name | time | anomaly_detect '(' field_name ',' algo_name | mode l_name [ ',' options] ')' where_clause ::= relation ( AND relation )* (OR relation)* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | CONTAINS | CONTAINS KEY
```

In the syntax, `anomaly_detect` indicates the anomaly detection function. The following table describes the parameters that you can configure.

| algo name _ | The name of the algorithm used to detect anomalies. The online anomaly detection algorithms developed by DAMO Academy are supported. esd: an algorithm that is applicable to spiked anomalies, such as spikes in monitoring curves and scenarios in which a small number of data points are significantly different from other data points. nsigma: an algorithm that is simple and easy to analyze the causes of anomalies. ttest: an algorithm that is used to identify whether the metrics related to time series data are abnormal because of a change in the average value. ostl-esd: an algorithm that is applicable to detect anomalies in periodic data. istl-esd: an algorithm that is applicable to detect anomalies in periodic data. Note The algo name parameter is applicable to scenarios in which in-database machine learning is not _ enabled and anomalies related to time series data must be detected. |
|---|---|
| model nam _ e | The name of the model used to forecast the values. Note The value of the model name parameter is of the VARCHAR type. _ The model name parameter is applicable to scenarios in which in-database machine _ learning is enabled and anomalies related to time series data must be detected. For more information, see Activate Lindorm AI. |
| options | The options used to adjust the detection effect. This parameter is optional. Configure the options in the key1=value1 key2=value2 format. |

| Algorithm | Use scenario |
|---|---|
| esd | This algorithm can detect single abnormal points. This algorithm is applicable to detection of abnormal data spikes. This algorithm can accurately detect a small number of abnormal points whose values are significantly different from other points. To detect anomalies in periodic data, this algorithm must be used together with the Online STL algorithm. |
| nsigma | This algorithm can detect single abnormal points. This algorithm is simple and easy to use. You can use the results returned by this algorithm to easily identify the root causes of the detected anomalies. Note We recommend that you do not use this algorithm to detect a small number of abnormal points whose values are significantly different from other points. In this case, the detection results returned by this algorithm may be inaccurate. |

**Algorithm categories**

The following table describes the anomaly detection algorithms supported by LindormTSDB and scenarios to which the algorithms are applicable.

| ttest | This algorithm can detect time series data within a specific time window. This algorithm detects anomalies that are caused by the variation of the average value of the specified metrics within a specific time window. For example, the algorithm can detect whether the average value of a time series array within the specified time window is significantly different from the average value of a time series array within the reference time window. You can obtain the time window within which you want to detect anomalies for time series data by checking the array length specified by lenDetectWindow. You can obtain the reference time window by checking the array length specified by lenHistoryWindow. To detect anomalies in periodic data, this algorithm must be used together with the Online STL algorithm. |
|---|---|
| Online STL with ESD (ostl-esd) | This algorithm is applicable to detection of anomalies in periodic data. The ostl-esd algorithm is an Online STL algorithm developed by DAMO Academy. The Online STL algorithm can decompose periodic data into periodic terms, trend terms, and residual terms. This algorithm needs to initialize data within four periods. The periodic data is decomposed to prevent normal periodic spikes in your business from being detected as anomalies. The ostl-esd algorithm integrates the Online STL algorithm with the esd algorithm. The Online STL algorithm is used to decompose periodic data, and the esd algorithm is used to detect anomalies in the residual terms decomposed from the periodic data. |
| Incremental STL with ESD (istl- esd) | This algorithm is applicable to detection of anomalies in periodic data. The istl-esd algorithm is an Incremental STL algorithm developed by DAMO Academy. The Incremental STL algorithm can decompose periodic incremental data into periodic terms, trend terms, and residual terms. The istl- esd algorithm integrates the Incremental STL algorithm with the esd algorithm. The Incremental STL algorithm is used to decompose periodic incremental data, and the esd algorithm is used to detect anomalies in the residual terms decomposed from the periodic data. The esd algorithm can detect non-periodic spikes based on the decomposed residual terms. |
| Incremental STL with Nsigma (istl- nsigma) | This algorithm is applicable to detection of anomalies in periodic data. The Incremental STL algorithm can decompose periodic incremental data into periodic terms, trend terms, and residual terms. The istl-nsigma algorithm integrates the Incremental STL algorithm with the nsigma algorithm. The Incremental STL algorithm is used to decompose periodic incremental data, and the nsigma algorithm is used to detect anomalies in the residual terms decomposed from the periodic data. The nsigma algorithm can detect non-periodic spikes based on the decomposed residual terms. |

**Parameters**

You can configure parameters for the anomaly detection algorithms that you use. These parameters can be categorized into common parameters, training parameters, and inference parameters. You can specify the optional parameter named options to adjust the detection performance of the anomaly detection algorithm.

**Note**

Common parameters, training parameters, and inference parameters are configured in the same parameter list. For example, you can configure parameters for the ttest algorithm in the following format: `lenDetectWindow=100,adhoc_stat=true` . For more information about how to configure parameters for ideal detection results, see Parameter tuning for statistical algorithms and Parameter tuning for decomposition algorithms.

**Common parameters**

You can configure common parameters to control the debugging, diagnosis, and other behaviors performed by algorithms during anomaly detection. Common parameters are applicable to all supported anomaly detection algorithms. The following table describes the common parameters that you can configure.

| Paramet er | Type | Default value | Description |
|---|---|---|---|
| verbose | BOOLEAN | FALSE | Specifies whether to return detailed information and identify the detection result of the specified columns. The returned information varies with the algorithm that you use. You can set this parameter to one of the following values: TRUE FALSE If you set this parameter to TRUE , additional columns are displayed in the returned results to show the detailed information. For more information, see the "Detailed information returned for the verbose parameter" section of this topic. |
| adhoc sta _ te | BOOLEAN | FALSE | Specifies whether the anomaly detection status of the algorithm is available only in the current query. For more information about the anomaly detection status, see Exception detection status. |
| direction | VARCHAR | UP | The types of anomalies that you want to detect. You can set this parameter to one of the following values: Up: Only the abnormal increases in time series data are detected as anomalies. Down: Only the abnormal decreases in time series data are detected as anomalies. Both: The abnormal increases and decreases in time series data are both detected as anomalies. |

| Algorit hm | Additional column | Type | Value | Description |
|---|---|---|---|---|
|  | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | detectedDir ection | STRING | UP DOWN NONE | UP: The value of the current data point is larger than the statistical value within the window. DOWN: The value of the current data point is less than the statistical value within the window. NONE: The current data point is normal, and the value in the anomaly column is FALSE. |
|  | anomalySco re | DOUBLE | [0, Double.MAX VALU _ E] | The score of the detected anomaly. A larger value indicates that the anomaly of the current data point is more obvious. |

**Detailed information returned for the verbose parameter**

|  | threshold | DOUBLE | [0, Double.MAX VALU _ E] | The threshold based on which the algorithm determines whether the current data point is abnormal. If the value in the anomalyScore column is larger than the value in the threshold column, the current data point is abnormal. If the value in the anomalyScore column is less than the value in the threshold column, the current data point is normal. The threshold is calculated based on the alpha and lenHistoryWindow parameters. The threshold increases when the value of alpha decreases or the value of lenHistoryWindow increases. |
|---|---|---|---|---|
| esd |  |  |  |  |
|  | upperBound | DOUBLE | All values of the DOUBLE type | The upper boundary for anomaly detection. For example, if you set the maxAnomalyRatio parameter to 0.3, the value in the upperBound column is the 70% (calculated by the following formula: 1 - maxAnomalyRatio) distribution value of the ordered data within the window. In this case, data points whose values are smaller than the upperBound value are not detected for anomalies. Note The length of the window is specified by the lenHistoryWindow parameter. If the value of a data point is within the [lowerBound, upperBound] range, the algorithm determines that the data point is normal. If the value of a data point is not within the range, the algorithm calculates the value of anomalyScore for the data point. If the anomalyScore of the data point is larger than the value in the threshold column, the data point is determined abnormal. |
|  | lowerBound | DOUBLE | All values of the DOUBLE type | The lower boundary for anomaly detection. For example, if you set the maxAnomalyRatio parameter to 0.3, the value in the lowerBound column is the 30% distribution value of the ordered data within the window. In this case, data points whose values are larger than the lowerBound value are not detected for anomalies. Note The length of the window is specified by the lenHistoryWindow parameter. If the value of a data point is within the [lowerBound, upperBound] range, the algorithm determines that the data point is normal. If the value of a data point is not within the range, the algorithm calculates the value of anomalyScore for the data point. If the anomalyScore of the data point is larger than the value in the threshold column, the data point is determined abnormal. |
|  | mean | DOUBLE | All values of the DOUBLE type | The average value of the data points within the window. |

|  | median | DOUBLE | All values of the DOUBLE type | The median of the data points within the window. |
|---|---|---|---|---|
|  | std | DOUBLE | All values of the DOUBLE type | The standard deviation of the data points within the window. |
|  | latestTimest amp | LONG | Positive integer | The timestamp of the latest data point within the window. |
|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. FALSE: The algorithm is initialized. |
| ttest | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | detectedDir ection | STRING | UP DOWN NONE | UP: The value of the current data point is larger than the statistical value within the window. DOWN: The value of the current data point is less than the statistical value within the window. NONE: The current data point is normal, and the value of anomaly is FALSE . |
|  | pValue | DOUBLE | (0, 1) | The ratio that indicates how the value of the current data point deviates from the statistical value within the window. A larger value indicates that value of the current data point deviates from the statistical value more significantly. |
|  | threshold | DOUBLE | (0, 1) | The threshold based on which the algorithm determines whether the current data point is abnormal. If the value in the pValue column is less than the value in the threshold column, the current data point is abnormal. If the value of pValue is larger than the value in the threshold column, the current data point is normal. |
|  | trendScore | DOUBLE | All values of the DOUBLE type | The degree of change in the trend of the data points. The larger the absolute value, the more obvious the trend changes. If the value in the trendScore column is larger than zero, the trend of the data points is upward. If the value in the trendScore column is less than zero, the trend of the data points is downward. |

|  | mean | DOUBLE | All values of the DOUBLE type | The average value of the data points within the window. The length of the window is specified by the lenHistoryWindow parameter. |
|---|---|---|---|---|
|  | std | DOUBLE | All values of the DOUBLE type | The standard deviation of the data points within the window. |
|  | latestTimest amp | LONG | Positive integer | The timestamp of the latest data point within the window. |
|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. FALSE: The algorithm is initialized. |
|  | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | detectedDir ection | STRING | UP DOWN NONE | UP: The value of the current data point is larger than the statistical value within the window. DOWN: The value of the current data point is less than the statistical value within the window. NONE: The current data point is normal, and the value of anomaly is FALSE . |
| nsigma |  |  |  |  |
|  | anomalySco re | DOUBLE | [0, Double.MAX VALU _ E] | The larger the value, the more obvious the anomaly of the current data point. |
|  | threshold | DOUBLE | [0, Double.MAX VALU _ E] | The judgment threshold, which is used to determine whether the current data point is abnormal. If the value of anomalyScore is greater than the value of threshold, the current data point is abnormal. If the value of anomalyScore is less than the value of threshold, the current data point is normal. |
|  | mean | DOUBLE | All values of the DOUBLE type | The average value of the data points within the window. |
|  | std | DOUBLE | All values of the DOUBLE type | The standard deviation of the data points within the window. |
|  | latestTimest amp | LONG | Positive integer | The timestamp of the latest data point within the window. |
| > Docume | nt Version: 20250825 259 |  |  |  |

|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. FALSE: The algorithm is initialized. |
|---|---|---|---|---|
|  | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | residual | DOUBLE | All values of the DOUBLE type | The residual value of the original data after the periodic component and the trend component are removed. In the ISTL algorithm, data points are decomposed into three components in the following format: residual+trend+season . If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | trend | DOUBLE | All values of the DOUBLE type | The trending component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
| istl-esd |  |  |  |  |
|  | season | DOUBLE | All values of the DOUBLE type | The periodic component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. Note Four cycles of data points are required to initialize the algorithm. During initialization, values returned in the residual, trend, and season columns are invalid. The default value 0 is returned in these columns. FALSE: The algorithm is initialized. |

|  | Other additional columns (same as the additional columns returned for the esd algorithm) | Same as the data types of the columns returned for the esd algorith m. | Same as the valid values of the columns returned for the esd algorithm. | If you specify esd.verbose=true when you call a anomaly detection function, the esd verbose mode is enabled. In this case, all columns for the esd and ttest algorithms (excluding the anomaly, warmup, and anomalyLevel columns) in the verbose mode are returned. |
|---|---|---|---|---|
| istl- nsigma | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | trend | DOUBLE | All values of the DOUBLE type | The trending component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | season | DOUBLE | All values of the DOUBLE type | The periodic component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | residual | DOUBLE | All values of the DOUBLE type | The residual value of the original data after the periodic component and the trend component are removed. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. Note Four cycles of data points are required to initialize the algorithm. During initialization, values returned in the residual, trend, and season columns are invalid. The default value 0 is returned in these columns. FALSE: The algorithm is initialized. |

|  | Other additional columns (same as the additional columns returned for the nsigma algorithm) | Same as the data types of the columns returned for the nsigma algorith m | Same as the valid values of the columns returned for the nsigma algorithm | If you specify nsigma.verbose=true when you call an anomaly detection function, the nsigma verbose mode is enabled. |
|---|---|---|---|---|
| ostl-esd | anomaly | BOOLEA N | TRUE FALSE | TRUE: The current data point is abnormal. FALSE: The current data point is normal. |
|  | anomalyLev el | STRING | NORMAL UNKNOW | NORMAL: No anomalies are detected for the current data point. UNKNOW: Anomalies are detected for the current data point and are not classified. |
|  | trend | DOUBLE | All values of the DOUBLE type | The trending component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | season | DOUBLE | All values of the DOUBLE type | The periodic component in the original data. If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | residual | DOUBLE | All values of the DOUBLE type | The residual value of the original data after the periodic component and the trend component are removed. In the OSTL algorithm, data points are decomposed into three components in the following format: residual+trend+season . If the algorithm is being initialized (value in the warmup column is TRUE ), only the default value 0 is returned in this column. |
|  | warmup | BOOLEA N | TRUE FALSE | TRUE: The algorithm is being initialized and does not detect anomalies. Note Four cycles of data points are required to initialize the algorithm. During initialization, values returned in the residual, trend, and season columns are invalid. The default value 0 is returned in these columns. FALSE: The algorithm is initialized. |

|  | Other additional columns (same as the additional columns returned for the esd algorithm) | Same as the data types of the columns returned for the esd algorith m | Same as the valid values of the columns returned for the esd algorithm | If you specify esd.verbose=true when you call an anomaly detection function, the esd verbose mode is enabled. In this case, all columns for the esd and ttest algorithms (excluding the anomaly, warmup, and anomalyLevel columns) in the verbose mode are returned. |
|---|---|---|---|---|

| Algori thm | Paramete r | Type | Value | Description |
|---|---|---|---|---|
| esd | compressio n | INTEG ER | A positive integer. Valid values: (10,1000) . Default value: 100. | The spatial complexity of the data structure in the algorithm. A larger value of this parameter indicates that the algorithm uses more memory during detection and returns more accurate results. |
|  | lenHistory Window | INTEG ER | Valid values: positive integers that are equal to or larger than 20. Default value: null. | The length of the reference time window. If you specify a short reference time window, only the recent data points within the time window are used as references during the detection. If you set this parameter to null, all data points that are inserted after the first detection are used as references. |
| nsigm a | lenHistory Window | INTEG ER | Valid values: positive integers that are equal to or larger than 20. Default value: null. | The length of the reference time window. If you specify a short reference time window, only the recent data points within the time window are used as references during the detection. If you set this parameter to null, all data points that are inserted after the first detection are used as references. |
| ttest | lenDetect Window | INTEG ER | A positive integer. Default value: 10. | The length of the most recent time window within which you want to detect anomalies. |

**Training parameters**

You can specify an algorithm and configure the training parameters to determine the model used to detect anomalies. The values of training parameters are cleared after you restart LindormTSDB. In this case, you must configure the training parameters again to train the model. The model is trained in real time during detection to adapt to learn and adapt the characteristics of the time series data.

**Note**

Take note of the following items when you configure training parameters: The names of the parameters are not case-sensitive. The values of training parameters can be digits and strings and cannot be NULL. The values of the parameters must be within the specific ranges.

|  | lenHistory Window | INTEG ER | Valid values: positive integers that are equal to or larger than 20. Default value: 100. | The length of the reference time window. If you specify a short reference time window, only the recent data points within the time window are used as references during the detection. If you set this parameter to null, all data points that are inserted after the first detection are used as references. Note The value of this parameter must be larger than the value of lenDetectWindow. |
|---|---|---|---|---|
| ostl- esd | alphaStl | DOUB LE | Valid values: (0,1) . Default value: 0.35. | The smoothing parameter used for periodic data filtering. |
|  | periods | INT[] | A positive integer. Default value: [1440]. | The total period length of the periodic data, which is the number of data points. Multiple cycle lengths may be conveyed through the indexer. Example: periods[0]=1440;periods[1]=1880. |
|  | esd.* | N/A | The training parameters that are required to define the esd algorithm. These parameters are the same as the training parameters described in the esd section of this table. You can add the esd. prefix to the training parameters of the esd algorithm to configure these parameters. Example: esd.lenHistoryWindow=10 . |  |
| istl- esd | frequency | VARC HAR | A string that consists of a digit and a time unit. Examples: 5M, 24H, and 1D. Valid time units: n/ns: nanosecond. u/us: microsecond. m/ms: millisecond. s/S: second. M/min: minute. H/h: hour. D/d: day. | The frequency at which the time series data is collected. For example, if one time series data point is collected per hour, set this parameter to 1H . Important If this parameter is not specified, the algorithm automatically calculates the frequency at which the time series data is collected. However, if a lot of values are missing in the time series data, the calculated frequency may be inaccurate. If you specify the frequency parameter, the value of this parameter must be the same as that of the INTERVAL parameter specified in the SAMPLE BY INTERVAL statement. |
|  | periods | VARC HAR | A string that consists of a digit and a time unit. Examples: 5M, 24H, and 1D. Valid time units: n/ns: nanosecond. u/us: microsecond. m/ms: millisecond. s/S: second. M/min: minute. H/h: hour. D/d: day. | The total period length of the periodic data. Note If this parameter is not specified, the algorithm automatically calculates the period. |

|  | esd.* | N/A | The training parameters that are required to define the esd algorithm. These parameters are the same as the training parameters described in the esd section of this table. You can add the esd. prefix to the training parameters of the esd algorithm to configure these parameters. Example: esd.lenHistoryWindow=10 . |  |
|---|---|---|---|---|
| istl- nsigm a | frequency | VARC HAR | A string that consists of a digit and a time unit. Examples: 5M, 24H, and 1D. Valid time units: n/ns: nanosecond. u/us: microsecond. m/ms: millisecond. s/S: second. M/min: minute. H/h: hour. D/d: day. | The frequency at which the time series data is collected. For example, if one time series data point is collected per hour, set this parameter to 1H . Important If this parameter is not specified, the algorithm automatically calculates the frequency at which the time series data is collected. However, if a lot of values are missing in the time series data, the calculated frequency may be inaccurate. If you specify the frequency parameter, the value of this parameter must be the same as that of the INTERVAL parameter specified in the SAMPLE BY INTERVAL statement. |
|  | periods | VARC HAR | A string that consists of a digit and a time unit. Examples: 5M, 24H, and 1D. Valid time units: n/ns: nanosecond. u/us: microsecond. m/ms: millisecond. s/S: second. M/min: minute. H/h: hour. D/d: day. | The total period length of the periodic data. Note If this parameter is not specified, the algorithm automatically calculates the period. |

|  | nsigma.* | N/A | The training parameters that are required to define the nsigma algorithm. These parameters are the same as the training parameters described in the nsigma section of this table. You can add the nsigma. prefix to the training parameters of the nsigma algorithm to configure these parameters. Example: nsigma.lenHistoryWindow=10 . |
|---|---|---|---|

| Algori thm | Parameter | Type | Value | Description |
|---|---|---|---|---|
|  | alpha | DOUBLE | Valid values: (0,1) . Default value: 0.1. | The sensitivity of anomaly detection. A larger value of this parameter indicates that the algorithm is more sensitive to anomalies and reports more anomalies. |
|  | direction | VARCHAR | Default value: Up. | The types of anomalies that you want to detect. Up: Only the abnormal increases in time series data are detected as anomalies. Down: Only the abnormal decreases in time series data are detected as anomalies. Both: The abnormal increases and decreases in time series data are both detected as anomalies. |
| esd |  |  |  |  |
|  | maxAnomalyR atio | DOUBLE | Valid values: (0,1] . Default value: 0.3. If you set this parameter to 1, no anomalies are returned. | The maximum ratio based on which anomalies are detected. For example, if you set maxAnomalyRatio to 0.3 and direction to Up, data points whose values are less than the 70th percentile are not detected as anomalies. If you set direction to Up, you can configure this parameter to prevent data points with smaller values from being detected as anomalies. If you set direction to Down, you can configure this parameter to prevent data points with larger values from being detected as anomalies. |
|  | warmupCount | INTEGER | A positive integer. Default value: 20. | The minimum number of data points that is required for the algorithm to start to report anomalies. For example, if you set this parameter to 20, the algorithm does not report anomalies when the number of data points that need to be detected is less than 20. |
| nsigm a | n | DOUBLE | A non-zero floating- point number. Default value: 3.0. | If you set n to a positive number, the algorithm reports an anomaly when the difference between the current value and the average value is larger than the product of n and the standard deviation. If you set n to a negative number, the algorithm reports an anomaly when the difference between the average value and the current value is larger than the product of n and the standard deviation. |
| 266 | > Document Version: 20250825 |  |  |  |

**Inference parameters**

Inference parameters take effect only during anomaly detection and are not case-sensitive.

|  | warmupCount | INTEGER | A positive integer. Default value: 20. | The minimum number of data points that is required for the algorithm to start to report anomalies. For example, if you set this parameter to 20, the algorithm does not report anomalies when the number of data points that need to be detected is less than 20. |
|---|---|---|---|---|
| ttest | alpha | DOUBLE | Valid values: (0,1) . Default value: 0.05. | The sensitivity of anomaly detection. A larger value of this parameter indicates that the algorithm is more sensitive to anomalies and reports more anomalies. |
|  | direction | VARCHAR | Default value: Up. | The types of anomalies that you want to detect. Up: Only the abnormal increases in time series data are detected as anomalies. Down: Only the abnormal decreases in time series data are detected as anomalies. Both: The abnormal increases and decreases in time series data are both detected as anomalies. |
| ostl- esd | esd.* | N/A | The inference parameters that are required to define the esd algorithm. These parameters are the same as the inference parameters described in the esd section of this table. You can add the esd. prefix to the inference parameters of the esd algorithm to configure these parameters. Example: esd.direction=Both . |  |
| istl- esd | esd.* | N/A | The inference parameters that are required to define the esd algorithm. These parameters are the same as the inference parameters described in the esd section of this table. You can add the esd. prefix to the inference parameters of the esd algorithm to configure these parameters. Example: esd.direction=Both . |  |
| istl- nsigm a | nsigma.* | N/A | Define the inference parameters required by the nsigma algorithm. For more information, see Inference parameters of the nsigma algorithm. You can add the nsigma. prefix to the inference parameters of the nsigma algorithm to configure these parameters. Example: nsigma.n=5 . |  |

Example 1: Use the esd algorithm to detect anomalies in the temperature data within a specific time range in a time series table named sensor.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd') AS detect_result FROM sensor W HERE time >= '2022-01-01 00:00:00' and time < '2022-01-01 00:01:00' SAMPLE BY 0;
```

Sample response:

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | true          |
| F07A1260  | north-cn | 2022-01-01T00:00:01+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:02+08:00 | true          |
| F07A1261  | south-cn | 2022-01-01T00:00:00+08:00 | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:01+08:00 | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:02+08:00 | false         |
| F07A1261  | south-cn | 2022-01-01T00:00:03+08:00 | false         |
+-----------+----------+---------------------------+---------------+
```

Example 2: Use the esd algorithm to detect anomalies in the temperature data of the F07A1260 device within a specific time range in the sensor table.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd') AS detect_result FROM sensor W HERE device_id in ('F07A1260') and time >= '2022-01-01 00:00:00' and time < '2022-01-01 00:01:00' SAMPLE BY 0;
```

Sample response:

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | true          |
| F07A1260  | north-cn | 2022-01-01T00:00:01+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:02+08:00 | true          |
+-----------+----------+---------------------------+---------------+
```

Example 3: Use the esd algorithm and configure parameters to detect anomalies in the temperature data of the F07A1260 device within a specific time range in the sensor table.

```
SELECT device_id, region, time, anomaly_detect(temperature, 'esd', 'lenHistoryWindow=30,maxAnomalyRatio=0.1') AS detect_result FROM sensor WHERE device_id in ('F07A 1260') and time >= '2022-01-01 00:00:00' and time < '2022-01-01 00:01:00' SAMPLE BY 0;
```

Sample response:

```
+-----------+----------+---------------------------+---------------+
| device_id |  region  |           time            | detect_result |
+-----------+----------+---------------------------+---------------+
| F07A1260  | north-cn | 2022-01-01T00:00:00+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:01+08:00 | false         |
| F07A1260  | north-cn | 2022-01-01T00:00:02+08:00 | true          |
+-----------+----------+---------------------------+---------------+
```

Example 4: Use the nested downsampling operator MAX in the statement and specify the downsampling interval as 1 minute.

```
SELECT time, anomaly_detect(max(f1), 'esd') AS ad_result, max(f1) AS rawVal FROM sensor SAMPLE BY 1m;
```

Sample response:

| Parameter | Description |
|---|---|
| user name _ | The name of the user to whom you want to grant the permissions. The value must be an SQL identifier. |

```
+---------------------------+-----------+-------------+
|           time            | ad_result |   rawVal    |
+---------------------------+-----------+-------------+
| 2022-04-12T06:00:00+08:00 | null      | 923091.3175 |
| 2022-04-11T08:00:00+08:00 | null      | 8035700     |
| 2022-04-11T09:00:00+08:00 | null      | 8035690.25  |
| 2022-04-11T10:00:00+08:00 | null      | 3306277.545 |
| 2022-04-11T11:00:00+08:00 | null      | 5921167.787 |
| 2022-04-11T12:00:00+08:00 | null      | 833541.304  |
+---------------------------+-----------+-------------+
```

Example 5: Use the nested non-downsampling operator LATEST in the statement and specify the downsampling interval as 0.

```
SELECT time, anomaly_detect(latest(f1), 'esd') AS ad_result, latest(f1) AS latestVal FROM sensor SAMPLE BY 0;
```

Sample response:

```
+---------------------------+-----------+-------------+
|           time            | ad_result |  latestVal  |
+---------------------------+-----------+-------------+
| 2022-04-12T06:00:00+08:00 | false     | 923091.3175 |
| 2022-04-13T07:00:00+08:00 | false     | 8037506.75  |
| 2022-04-13T07:00:00+08:00 | false     | 50490.2     |
+---------------------------+-----------+-------------+
```

#### DCL

##### GRANT

This topic describes the syntax that is used to grant permissions to a user. You can use the following syntax to grant the specified permission on an object to a specified user: Syntax:

```
grant_statement ::= GRANT privilege_definition ON resource_definition TO user_name privilege_definition ::= ALL [PRIVILEGES] | READ | WRITE | ADMIN | SYSTEM resource_definition ::= GLOBAL | DATABASE database_name
```

**Parameters**

| privilege definition _ | The permissions that you want to grant to the user. Valid values: READ The permission to query data. WRITE The permission to write data. ADMIN The management permission. SYSTEM The permission to manage clusters. The SYSTEM permission includes the ADMIN permission on the GLOBAL scope. ALL or ALL PRIVILEGES All permissions. All permissions consist of the READ, WRITE, and ADMIN permissions. |
|---|---|
| resource definition _ | The scope of resources whose permissions you want to grant. Valid values: GLOBAL The specified permission on all resources is globally granted. DATABASE The specified permission on the specified database is granted. |
| database name _ | The name of the database whose permissions you want to grant. This parameter is required if resource definition is set to DATABASE. The value _ must be an SQL identifier. |

**Important**

1. The permissions on the GLOBAL scope take precedence over the permissions on the DATABASE
scope. If you are granted the READ permission on the GLOBAL scope, you can query time series tables in all databases. If you are granted the READ permission on the DATABASE scope, you can query time series tables in only the database. **We recommend that you do not grant permissions on the**

**GLOBAL scope, particularly the ALL PRIVILEGES permission on the GLOBAL scope.**

2. The ADMIN permission is independent of the READ and WRITE permissions. Even if you are granted
the ADMIN permission on a specific database, you may be unable to read data from and write data to time series tables in the database.
3. You cannot grant the SYSTEM permission on a specific database.
4. You cannot grant permissions on a resource object that does not exist. You also cannot grant
permissions to a user that does not exist.
5. Whether a GRANT statement can be executed successfully depends on the permissions that are
granted to the user who executes the statement. For more information, see the **User and**
**permission management** topic of **Instance management** in **Lindorm User Guide**.
In the following example, the read permission on a database named `DB1` is granted to a user named

```
 tsdbuser .
GRANT READ ON DATABASE `DB1` TO `tsdbuser`;
```

In the following example, the write permission on a database named `DB2` is granted to a user named

```
 tsdbuser .
```

| Parameter | Description |
|---|---|
| user name _ | The name of the user from whom you want to revoke the permissions. The value must be an SQL identifier. |
| privilege definition _ | The permissions that you want to revoke. Valid values: READ The permission to query data. WRITE The permission to write data. ADMIN The management permission. SYSTEM The permission to manage clusters. The SYSTEM permission includes the ADMIN permission on the GLOBAL scale. ALL or ALL PRIVILEGES All permissions. All permissions consist of the READ, WRITE, and ADMIN permissions. |
| resource definition _ | The scope of resources on which the permissions are revoked. Valid values: GLOBAL The specified permission on all resources is revoked. DATABASE The specified permission on the specified database is revoked. |
| database name _ | The name of the database on which the permission is revoked. This parameter is required if resource definition is set to DATABASE. The value _ must be an SQL identifier. |

```
GRANT WRITE ON DATABASE `DB2` TO `tsdbuser`;
```

In the following example, all permissions on a database named `DB3` are granted to a user named

```
 tsdbuser .
GRANT ALL PRIVILEGES ON DATABASE `DB3` TO `tsdbuser`;
```

##### REVOKE

This topic describes the syntax that is used to revoke permissions. You can use the following syntax to revoke the specified permission on an object from the specified user:

```
revoke_statement ::= REVOKE privilege_definition ON resource_definition FROM user_name privilege_definition ::= ALL [PRIVILEGES] | READ | WRITE | ADMIN | SYSTEM resource_definition ::= GLOBAL | DATABASE database_name
```

**Parameters**

| ErrorCode | SQLSTATE | Error message format | Suggestion |
|---|---|---|---|
| 1227 | 42501 | %s | Make sure that the user account has sufficient permissions on the object that you want to access. |

| ErrorCode | SQLSTATE | Error message format | Suggestion |
|---|---|---|---|
| 1006 | HY000 | Can't create database '%s' (errno: %d - %s) | LindormTSDB failed to create the database. Check whether the input parameters are valid based on the returned error message. |

**Important**

Whether the REVOKE statement can be executed successfully depends on the permissions that are granted to the user who executes the statement. For more information, see the **User and**
**permission management** topic of **Instance management** in **Lindorm User Guide**.
In the following example, the READ permission on a database named `DB1` is revoked from a user named `tsdbuser` .

```
REVOKE READ ON DATABASE `DB1` FROM `tsdbuser`;
```

In the following example, the WRITE permission on a database named `DB2` is revoked from a user named `tsdbuser` .

```
REVOKE WRITE ON DATABASE `DB2` FROM `tsdbuser`;
```

In the following example, all permissions on a database named `DB3` are revoked from a user named

```
 tsdbuser .
REVOKE ALL PRIVILEGES ON DATABASE `DB3` FROM `tsdbuser`;
```

#### Common error codes

##### Common error codes

This topic describes the common error codes that are returned when you send SQL queries to LindormTSDB.

**Permission errors**

**DDL errors**

| 1007 | HY000 | Can't create database '%s'; database exists | LindormTSDB failed to create the database because the database name is already used. Use a different database name. |
|---|---|---|---|
| 1008 | HY000 | Can't drop database '%s'; database doesn't exist | LindormTSDB failed to delete the database because the database name does not exist. Specify an existing database name. |
| 1009 | HY000 | Error dropping database (can't delete '%s', errno: %d - %s) | LindormTSDB failed to delete the database. Check the cause of failure based on the returned error message. If the error persists, contact the product engineer. |
| 1045 | 28000 | %s | Check whether the user information that is used for authentication is valid. |
| 1049 | 42000 | Unknown database '%s' | No database is specified. Specify the database that you want to access. |
| 1050 | 42S01 | Table '%s' already exists | The table name is already used. Use a different table name. |
| 1064 | 42000 | You have an error in your SQL syntax; %s | The SQL statement contains grammatical errors. Refer to the SQL developer guide and resolve the errors. |
| 1146 | 42S02 | Table '%s.%s' doesn't exist | The table does not exist. Check whether the table name is valid. |
| 8000 | HY000 | Can't alter database '%s' (errno: %d - %s) | The database cannot be modified. Check whether the input parameters are valid based on the returned error message. |

| 8001 | HY000 | Can't create continuous query '%s' (errno: %d - %s) | The continuous query failed to be created. Check whether the input parameters are valid based on the returned error message. |
|---|---|---|---|
| 8002 | HY000 | Can't create continuous query '%s'; continuous query exists | The name of the continuous query is already used. Use a different name. |
| 8004 | HY000 | Continuous query '%s.%s' doesn't exist | The specified continuous query does not exist. Check whether the query name is valid. |

| ErrorCode | SQLSTATE | Error message format | Suggestion |
|---|---|---|---|
| 3024 | HY000 | Query execution was interrupted, maximum statement execution time exceeded | The query timed out. Try again. If the query timed out again, contact the product engineer. |
| 8005 | HY000 | Table '%s' not found | The table does not exist. Check whether the table name is valid. |
| 8006 | HY000 | Query failed; %s | The query failed. Check the cause of failure based on the returned error message. If the error persists, contact the product engineer. |
| 8007 | HY000 | Insert failed; %s | The write operation failed. Check the cause of failure based on the returned error message. If the error persists, contact the product engineer. |

**DML errors**

| 8008 | HY000 | Quota exceeded; %s | The upper limit is exceeded. Check the cause of failure based on the returned error message. For queries, you can shorten the time range that is queried or add a WHERE condition to reduce the results that hit the query. For write operations, you can limit the number of transactions that are written per second (TPS). |
|---|---|---|---|

| ErrorCode | SQLSTATE | Error message format | Suggestion |
|---|---|---|---|
| 9000 | HY000 | Server internal error; %s | Contact the product engineer. |
| 9001 | 0A000 | UNSUPPORTED: %s | Refer to the SQL syntax supported by LindormTSDB. Do not use SQL statements that are not supported by LindormTSDB. |

**System errors**

### Best practices

#### Design a time series table

You can use time series tables to improve query performance and storage performance. This topic describes how to design a time series table based on the source of time series data and the business scenario in which the time series data is used.

**Sample time series data**

Modeling is critical for time series data. You need to analyze the query scenarios and the characteristics of data sources to create appropriate data tables. This way, you can obtain optimal storage and query performance. The following figure provides an example. In the example, air quality monitoring (AQM) data is used. The data record that is generated at each point in time can be divided into the following parts: Table: indicates a collection of time series data that is of the same type. Tags: indicate the attributes of an object for which metrics are monitored. A tag consists of a tag key and a tag value. By default, LindormTSDB creates an index that maps tags to time series for the keyvalue pair of each tag. In specific scenarios, tags may be referred to as labels or dimensions. Timestamp: indicates the time when the data record is generated. Field: indicates an aspect of metrics. A data record can contain values of multiple fields. LindormTSDB does not create indexes for fields.

**Best practice for designing time series tables**

You can use measurements for the time series data of the same type as table names based on the preceding data model, and then execute the CREATE TABLE SQL statement to design tables. For example, the measurement AQM that is shown in the preceding figure can be used as a table name. The following sample code provides an example on how to define a table. In the example, the preceding AQM time series model is used.

```
    city        VARCHAR TAG,
    district    VARCHAR TAG,
    id          VARCHAR TAG,
    time        TIMESTAMP,
    pm2_5       DOUBLE,
    pm10        DOUBLE,
    so2         DOUBLE,
    no2         DOUBLE,
    PRIMARY KEY(id)  //// Single-node Lindorm instances do not support primary keys. If your
Lindorm instance is a single-node Lindorm instance, delete this row. );
```

After the table is defined, execute INSERT statements to write data to the table.

```
INSERT INTO aqm (city, district, id, time, pm2_5, pm10, so2, no2) VALUES ('hangzhou', 'yuhang', 'HY00001', '2019-04-18 10:00:00', 31.0, 66.0, 10.0, 43.0); INSERT INTO aqm (city, district, id, time, pm2_5, pm10, so2, no2) VALUES ('hangzhou', 'yuhang', 'HY00001', '2019-04-18 10:01:00', 31.2, 66.0, 10.5, 43.1);
```

You can also execute the following INSERT statement to write multiple records into the table at a time:

```
INSERT INTO aqm (city, district, id, time, pm2_5, pm10, so2, no2) VALUES ('hangzhou', 'yuhang', 'HY00001', '2019-04-18 10:02:00', 31.3, 66.0, 10.0, 42.9), ('hangzhou', 'yuhang', 'HY00001', '2019-04-18 10:03:00', 31.2, 66.4, 10.3, 43.0);
```

**Note**

The **TAG** keyword is a syntax extension of SQL. This keyword is used to specify a column in a table as a tag. When you create a time series table, we recommend that you define columns as tags based on the following rules: Make sure that the column that is defined as a tag can uniquely identify an attribute of the data source. We recommend that you do not use attributes whose values frequently change as tags. For example, we recommend that you do not use process IDs and time-related attributes as tags. We recommend that you define these attributes as fields even if the data type of these attributes is STRING. If these attributes are used as tags, the number of time series increases. As a result, the size of the time series index increases. This affects data queries in a negative manner.

**Best practice for designing primary keys**

Databases perform storage sharding and query optimization based on primary keys. If primary keys are specified in queries, the query efficiency is increased. We recommend that you specify a primary key when you create a table.

**Note**

Single-node Lindorm instances do not support primary keys. In most cases, we recommend that you use the unique identifier of the data source as the primary key based on actual scenarios. In Internet of Things (IoT) and Industrial Internet of Things (IIoT) scenarios, you can use the device ID as the primary key. In Internet of Vehicles (IoV) scenarios, you can use the unique identifier of vehicles as the primary key. In monitoring scenarios, you can use an identifier such as the app ID or host:port as the primary key. In the time series table aqm that is used in the preceding example, you can use the ID as the primary key to obtain optimal query performance if a large number of queries are performed based on IDs.

```
    city        VARCHAR TAG,
    district    VARCHAR TAG,
    id          VARCHAR TAG,
    time        TIMESTAMP,
    pm2_5       DOUBLE,
    pm10        DOUBLE,
    so2         DOUBLE,
    no2         DOUBLE,
    PRIMARY KEY (id)   // Single-node Lindorm instances do not support primary keys. If your
Lindorm instance is a single-node Lindorm instance, delete this row. );
```

**Important**

Time series tables are different from tables in traditional relational databases. Time series tables do not require the values in primary key columns to be unique. If you want to specify a column as the primary key column, make sure that the column is labeled as a tag. For more information about the data types supported by LindormTSDB, see Data types. When you create a time series table, we recommend that you select data types based on the following rules: Tag columns Values in columns that are declared as tags must be of the VARCHAR data type. The data type of these columns cannot be changed. Timestamp columns LindormTSDB stores timestamps as BIGINT values in the UNIX time format in LindormDFS. This improves the performance of timestamp compression. When you create a table, you can specify the BIGINT or TIMESTAMP type based on your calculation requirements for timestamps. Field columns Field columns support all data types. To ensure excellent data compression and optimal query performance, we recommend that you do not use VARCHAR as the data type for the values in field columns.

#### Write data in an efficient manner

This topic describes how to write data to LindormTSDB based on Java Database Connectivity (JDBC).

**Develop applications to perform efficient data write operations based**

**on JDBC**

If you use JDBC to develop applications, we recommend that you use a `PreparedStatement` object in JDBC. This way, you can insert multiple records into a database at the same time. Perform the following steps:
1. Use JDBC to create a `Connection` object.
For information about how to use JDBC to connect to a database, see Java JDBC Driver.
2. Create a `PreparedStatement` object and specify an INSERT statement that contains the required
parameters. The following sample code provides an example on how to create a `PreparedStatement` object based on the air test data provided in the Design a time series table topic:

```
    StringBuilder builder = new StringBuilder();
    builder.append("INSERT INTO aqm (city, district, id, time, pm2_5, pm10, so2, no2) ");
    builder.append("VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
    PreparedStatement preparedStmt = connection.prepareStatement(builder.toString());
```

3. Associate input parameters with the `PreparedStatement` object and execute the INSERT statement to
write data specified by the input parameters to the database. The following sample code provides an example on how to associate the input parameters in the INSERT statement created in Step 2 with the PreparedStatement object:

```
    for (int i = 0; i < batchSize; i++) {
        // Associate the parameters with the object in the order in which the column parameters a
re specified in the INSERT statement.
        // The parameters such as city, district, id, ts, and pm25 in the following code are loca
l variables that are used to associate with parameters:
        preparedStmt.setString(1, city);
        preparedStmt.setString(2, district);
        preparedStmt.setString(3, id);
        preparedStmt.setTimestamp(4, ts);
        preparedStmt.setDouble(5, pm25);
        preparedStmt.setDouble(6, pm10);
        preparedStmt.setDouble(7, so2);
        preparedStmt.setDouble(8, no2);
        // Add the parameters to a batch.
        preparedStmt.addBatch();
    }
    // Write data specified in the batch to the database.
    int[] results = preparedStmt.executeBatch();
    // Query the number of written data records from results. The remaining code is skipped.
}
```

**Note**

When you use JDBC in LindormTSDB, you can use a `PreparedStatement` object to configure parameters only by using the question mark (?) placeholder. When you call the API operations that are provided by `PreparedStatement` to associate with parameters, make sure that the value that corresponds to a parameter index specified for `setXXX()` is consistent with the column parameter that corresponds to the placeholder. If the input parameters are associated in batches before the `executeBatch()` method is called for the `PreparedStatement` object, a larger number of batches does not indicate better database performance. The database performance varies based on the definition of the table into which data is inserted. If the table contains only one field column and at most five tag columns, and the `batchSize` variable in the `PreparedStatement` object is set to **5000**, the database provides optimal write performance.

#### Query time series data in an efficient manner

This topic describes the index mechanism of time series tables and provides best practices for querying data in time series tables.

**Background information**

For more information about the model of time series data, see Design a time series table. Data in time series tables is organized by time series. In these tables, all columns marked with **TAG** are defined as index columns. Each value of these columns specifies the time series to which a record belongs to identify the data source. The following figure provides an example in which a time series table is used. The data records shown in the following figure belong to the same time series. For more information about time series tables, see Design a time series table. If a value in a tag column changes, the data record that corresponds to the value falls in another time series. In most cases, a time series can identify a data source from which time series data is generated. LindormTSDB creates indexes by using each **tag column**. Each of the indexes is an inverted index. The name and each value of a tag column are used as an index key to index all time series that contain the same key-value pair of the index key. The index key is used to identify the data range that corresponds to a tag from the time series dimension in a short period of time. When data is continuously written into the time series table, inverted indexes in the table change. The following figure shows the changed inverted indexes in the table. By default, LindormTSDB creates a Block Range Index (BRIN) for a timestamp column. This ensures that the data range that you want to query can be located in a large amount of time series data in a short period of time. LindormTSDB does not create indexes for field columns.

**Suggestions**

The following suggestions are provided based on the index mechanism of LindormTSDB for querying data from a time series table stored in LindormTSDB: We recommend that you add equivalent filter clauses for tag columns and filter clauses for your timestamp column in your query statement. This ensures that your query statement does not contain only filter clauses for field columns. If a query statement contains filter clauses for multiple tag columns and an inclusion relationship between time series ranges that are mapped by the tag columns exists, we recommend that you retain the filter for the tag column that can identify a record in an efficient manner. For example, in the preceding figure, the **id** column can identify a unique record, but the **city** column cannot identify a unique record. If the time range specified in your query condition is large, the system scans a large amount of data. As a result, the query speed is low. In this case, we recommend that you reduce the time range in which you want to query data to improve query performance.

**Common scenarios and operations for time series queries**

**Important**

If you want to reproduce the results of the following query scenarios, download the SQL script and use sample data recorded in the SQL script. For more information about the SQL script, see SQL script.

**Query values of a field reported within a specified time range**

Execute the following statement to query all sulfur dioxide (SO2) values that the devices in the Yuhang district reported from 2019-04-18 10:00:00 to 2019-04-18 10:30:00:

```
SELECT id, so2 FROM aqm WHERE district='yuhang' AND time >= '2019-04-18 10:00:00' AND time < '2019- 04-18 10:30:00';
```

The following figure shows the query result.

**Query all values in a specific tag column in a time series table**

When data that is generated by the devices of the same type is written to one time series table, you may want to query all values in a specific tag column in the time series table. For example, you can execute the following SQL statement to query all values in the `id` column of the `aqm` table for all devices that are used to monitor air quality:

```
SELECT DISTINCT(id) FROM aqm;
```

The following figure shows the query result.

**Note**

If values in a tag column of a table are queried, you do not need to worry about performance issues due to a full table scan. This is because LindormStore queries the values based on the indexes that are created for all tag columns in the table by default. Take note that an index-based query can be time-consuming when the data of excessive devices is stored in your time series table. Execute the following statement to query average PM2.5 and SO2 values based on PM2.5 and SO2 values reported by the devices in the Yuhang district from 2019-04-18 10:00:00 to 2019-04-18 10:30:00. The PM2.5 and SO2 values are split based on a 5-minute interval, and the average PM2.5 and SO2 values at each interval are calculated.

```
SELECT id, time, avg(pm2_5) AS avg_pm2_5, avg(so2) AS avg_so2 FROM aqm WHERE district='yuhang' AND time >= '2019-04-18 10:00:00' AND time < '2019-04-18 10:30:00' SAMPLE BY 5m;
```

The following figure shows the query result.

**Note**

Downsampling is used to aggregate data in a time series based on the time dimension.

**Use aggregation functions to query data across devices**

Execute the following statement to query the maximum average PM2.5 and SO2 values based on PM2.5 and SO2 values reported by the devices in the Yuhang district from 2019-04-18 10:00:00 to 2019-04-18 10:30:00. The maximum average PM2.5 and SO2 values are calculated based on PM2.5 values and SO2 values that are reported in each 5-minute time window.

```
SELECT max(avg_pm2_5) AS max_avg_pm25, max(avg_so2) AS max_avg_so2 FROM (SELECT district, id, time, avg(pm2_5) AS avg_pm2_5, avg(so2) AS avg_so2 FROM aqm WHERE district='yuhang' AND time >= '2019-04- 18 10:00:00' AND time < '2019-04-18 10:30:00' SAMPLE BY 5m) GROUP BY district;
```

The following figure shows the query result.

### Third-party tools

#### Use Telegraf to write data to LindormTSDB

Telegraf is an open source agent that is used to collect data. You can use the plug-ins provided by Telegraf to collect metrics from different services and third-party components. You can also use the builtin plug-ins provided by Telegraf to import the collected data to OpenTSDB. LindormTSDB is fully compatible with OpenTSDB. You can connect Telegraf to LindormTSDB. This topic describes how to deploy Telegraf to your existing application environment and connect Telegraf to a Lindorm cluster on Alibaba Cloud. After you perform these operations, the Lindorm cluster can receive monitoring data from Telegraf.

**Prerequisites**

1. Make sure that your existing application environment is connected to the Internet and has a public IP
address.
2. Create a Lindorm cluster on Alibaba Cloud based on your business requirements and apply for a public
IP address for the cluster. Then, add the public IP address of the application environment to the whitelist of the Lindorm cluster. Apply for a public endpoint on the Time Series Engine page of the Lindorm cluster. The following figure shows how to apply for a public endpoint. Configure a whitelist for the Lindorm cluster. The following figure shows how to configure a whitelist.
3. After you apply for a public endpoint for the Lindorm cluster, make sure that the application
environment can be connected to the public endpoint. After you apply for a public endpoint for the Lindorm cluster, you can view the endpoint and port of the cluster on the Time Series Engine page. The following figure shows how to view the endpoint in the console.

**Install Telegraf**

The method that is used to install Telegraf varies based on the platform where your application environment is deployed. For more information about how to select the suitable method, see Install Telegraf.
1. In the `telegraf.conf` configuration file of Telegraf, find the **OUTPUT PLUGINS** section.
2. Disable the output.influxdb plug-in and enable the output.opentsdb plug-in.

```
  ......
  #[[outputs.influxdb]]
  (Details are not displayed.)
  [[outputs.opentsdb]]
  ......
```

3. Configure parameters for the outputs.opentsdb plug-in.
Specify the domain name and port of the Lindorm cluster. The following code block provides an example:

```
 host = "http://{The ID of the Lindorm cluster}.hitsdb.rds.aliyuncs.com"
 port = 3242
```

**Note**

The endpoint must be prefixed with http://. Port 3242 is the default public port of a Lindorm cluster on Alibaba Cloud. Configure an HTTP API to report data. To collect data to Telegraph, specify http_path = "/api/put". You can also set the http_batch_size parameter to specify the number of data points to be written in each batch. Specify a delimiter that is used to separate the metrics. You can set the separator parameter to specify a delimiter. You can use only the delimiters that are supported by LindormTSDB. For more information, see Write single-value data points. For more information about other configuration items, see Configuration options.
4. Start Telegraf to collect data. After Telegraf starts to collect data, you can view the collected data on the
Instance Monitoring page of the Lindorm cluster. To go to the Instance Monitoring page, **log on to the**

**Lindorm console, click the ID of the Lindorm cluster, and then click Instance Monitoring in**

**the left-side navigation pane**.

#### Use Realtime Compute for Apache Flink to

#### write data to LindormTSDB

This topic describes how to create a time series table in Realtime Compute for Apache Flink and write data in the table to Lindorm.

**Prerequisites**

Realtime Compute for Apache Flink is activated, or a self-managed Flink service is created.

**Note**

The version of Ververica Runtime (VVR) used by Realtime Compute for Apache Flink must be 4.0.13 or later. VVR 4.0.13 is developed based on Apache Flink V1.13. LindormTSDB is activated for your Lindorm instance. The version of LindormTSDB is 3.4.7 or later.

| Parameter | Data type | Required | Description |
|---|---|---|---|
| timestamp | BIGINT | Yes | The timestamp of the time series data. Unit: milliseconds. Note The value is a 13-digit timestamp. If you specify a 10-digit timestamp for this parameter, it is converted to a 13-digit timestamp when the data is written to LindormTSDB. |
| tag tagname _ | VARCHAR | Yes | The tags of the time series data. You can set the name of a tag by specifying tagname. The specified tag must contain the tag _ prefix. Note The value of tag tagname can contain one or more column _ names. |

The Lindorm instance and the Realtime Compute for Apache Flink workspace reside in the same virtual private cloud (VPC). This ensures network connectivity.

**Background information**

The SINK plug-in for LindormTSDB is used to write the time series result table to the LindormTSDB sink connector. You can use this plug-in to efficiently write data from multiple sources to LindormTSDB for business analysis. To use the LindormTSDB sink connector, you need to obtain the JAR package of the LindormTSDB sink connector and then upload the JAR package to the Realtime Compute for Apache Flink console. For more information, see Develop a JAR draft. You can use the following syntax to create a time series result table in Realtime Compute for Apache Flink:

```
CREATE TEMPORARY TABLE tsdb_sink(
  `timestamp` BIGINT,
  tag_tagname VARCHAR,
  field_fieldname1 DOUBLE,
  field_fieldname2 VARCHAR,
  field_fieldname3 BIGINT,
  field_fieldname4 BOOLEAN
  -- table VARCHAR (optional)
```

)

```
with (
    'connector' = 'lindormtsdb',
    'url'='http://ld-bp159jt4eivt3****-proxy-tsdb.lindorm.rds.aliyuncs.com:8242',
    'table'='mytable',
    'schemaPolicy'='weak',
    'sync'='false',
    'debug'='false'
);
```

**Parameters**

**Default parameters**

| field fieldna _ me | DOUBLE, VARCHAR, BIGINT, and BOOLEAN | Yes | The fields of the time series data. You can set the name of a field by specifying fieldname. The specified field must contain the field prefix. _ Note The value of field fieldname can contain one or more column _ names. |
|---|---|---|---|
| table | VARCHAR | No | The time series table in which the data you want to write to LindormTSDB is stored. If you want to write data from one time series table to LindormTSDB, we recommend that you configure the parameters in the WITH clause. If you want to write data from multiple time series tables to LindormTSDB, you can specify the table names in this parameter. |

| Parameter | Required | Description |
|---|---|---|
| connector | Yes | Set this parameter to lindormtsdb, which indicates the LindormTSDB sink connector. |
| url | Yes | The endpoint of LindormTSDB. |
| table | No | The time series table in which the data you want to write to LindormTSDB is stored. We recommend that you configure this parameter if you want to write data from one time series table to LindormTSDB. If you want to write data from multiple time series tables to LindormTSDB, we recommend that you configure the table parameter described in the preceding table. |
| username | No | By default, user authentication and permission verification are not enabled for LindormTSDB. In this case, you do not need to provide a username or password when you connect to LindormTSDB. To ensure data security, we recommend that you enable user authentication and permission verification for LindormTSDB. After these features are enabled, you must provide a username and a password when you connect to LindormTSDB. |
| password | No |  |
| defaultDatabase | No | The Lindorm database to which you want to write data. Default value: default. |

**Parameters in the WITH clause**

| schemaPolicy | No | The schema constraint policy of the table. Default value: Strong. Valid values: Strong: LindormTSDB strictly verifies the table names, parameter names, and types of the data to be written based on the predefined table schema. Weak: When the table to which you want to write data does not exist, LindormTSDB does not report an error. Instead, LindormTSDB automatically creates the table. None: If you use this policy, you cannot query the written data by executing SQL statements. Note If you set this parameter to Strong or None, you must manually create a table when you write data to LindormTSDB. For more information, see Constraint policies for schemas. |
|---|---|---|
| ignoreErrorData | No | Specifies whether to ignore write errors. Default value: false. Valid values: false: Write errors are not ignored. A write operation is canceled when an error occurs. true: Write errors are ignored. A write operation continues even if an error occurs. |
| maxRetries | No | The maximum number of attempts to resend a write request that fails due to an internal server error or network error. Default value: 3. |
| batchSize | No | The number of data points that can be written to the server by a single write operation. Default value: 500. |
| connectTimeout Ms | No | The timeout period of HTTP connections. Default value: 90000. |
| debug | No | Specifies whether to enable the debug mode to display the logs of the data points that are written to LindormTSDB. Default value: false. false: disables the debug mode. true: enables the debug mode. |
| sync | No | Specifies whether to write data synchronously. Default value: false. We recommend that you keep the default value. false: writes data asynchronously. Data can be written more efficiently if you use this method. true: writes data synchronously. |

The following sample code shows how to write random time series data generated by datagen_source to a LindormTSDB table named tsdb_sink: Sample code:

```
CREATE TEMPORARY TABLE datagen_source (
  id INTEGER,
  score DOUBLE,
  name STRING
```

)

```
WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE tsdb_sink(
  tag_tagk VARCHAR,
  field_score DOUBLE,
  field_name STRING,
  `timestamp` BIGINT
```

)

```
WITH (
    'connector' = 'lindormtsdb',
    'url'='http://ld-bp159jt4eivt3****-proxy-tsdb.lindorm.rds.aliyuncs.com:8242',
    'table'= 'mytable'
);
  CAST(id as STRING) as tag_tagk,
  score as field_score,
  name as field_name,
  UNIX_TIMESTAMP(now()) * 1000  as `timestamp`
FROM datagen_source;
```

#### Use Grafana to access LindormTSDB

Grafana is an open source visualization tool that can visualize large amounts of metric data. Grafana is commonly used to analyze Internet applications and is also widely used in industrial monitoring, meteorological monitoring, home automation, procedure management, and other sectors. LindormTSDB provides the Alibaba Cloud Lindorm data source plug-in for you to add Lindorm to Grafana as a data source. This topic describes how to use Grafana to access LindormTSDB and analyze data in a visualized manner.

**Use Managed Service for Grafana to access LindormTSDB**

**Prerequisites**

A Grafana workspace is created. If you want to access LindormTSDB over a virtual private cloud (VPC), perform the following operations: Enable the VPC endpoint of Grafana. If you want to access LindormTSDB over the Internet, perform the following operations: Enable the Internet endpoint of LindormTSDB.

**Procedure**

In this topic, Grafana 10.0.x is used as an example to demonstrate how to access LindormTSDB.
1. Log on to the Managed Service for Grafana console. In the left-side navigation pane, click **Workspace**
**Management**. Then, click the workspace that you want to use to connect to LindormTSDB.
2. In the Basic Information section, click the Internet endpoint or VPC endpoint. Enter the username and
password. The username is admin. Enter the password that is specified when the workspace is created.
3. Add Lindorm to Grafana as a data source.
i. Click the icon in the upper-left corner and select **Manage**. Then, click the data source.

| Section | Parameter | Requi red | Description |
|---|---|---|---|
| Name |  | Yes | The name of the data source. You can retain the default value or enter a custom name. |
| HTTP | URL | Yes | The LindormTSDB endpoint for HTTP. Important If the VPC endpoint of Grafana is enabled and the Grafana service resides in the same VPC as the Lindorm cluster, use the VPC endpoint of LindormTSDB. Otherwise, use the Internet endpoint of LindormTSDB. If you specify the VPC endpoint of LindormTSDB, make sure that the VPC endpoint of the Grafana service is added to the whitelist of the Lindorm cluster. If you specify the Internet endpoint of LindormTSDB, make sure that the Internet endpoint of the Grafana service is added to the whitelist of the Lindorm cluster. |
| Auth | Basic auth | No | If the user authentication and permission verification feature is enabled for LindormTSDB, turn on Basic auth and enter the username and password used to log on to LindormTSDB in the Basic Auth Details section. |
| Basic Auth Details | User | No | The username that is used to log on to the Lindorm cluster. You must specify this parameter if you turn on Basic auth. |
|  | Password | No | The password that is used to log on to the Lindorm cluster. You must specify this parameter if you turn on Basic auth. |
| Lindorm TSDB Details | Database | No | The LindormTSDB database that you want to access. |

ii. On the Manage page, click the data source. iii. On the data source configuration page, click Add data source. iv. Enter Alibaba Cloud Lindorm in the search box of the Add data source page. Find and then click the data source. v. Configure the parameters described in the following table on the **Settings** tab. You can keep the default values for other parameters. vi. Click **Save & test**. If the "test success" message is returned, the connection test is successful.
4. Click **Build a dashboard**.
5. On the New Dashboard page, click **Add a new panel**.
6. Select the Lindorm data source that is added in Step 3.
7. Query data on the **Query** tab.
i. Select the data source that you want to use from the **Data source** drop-down list. ii. To query data in Grafana, you can use the SQL statement editor or template-based query editor.

**SQL statement editor**

| Keyword | Description |
|---|---|
| SELECT | Specify the name of the field that you want to query. |
| FROM | Specify the name of the table that you want to query. |
| WHERE | Add query conditions. |
| GROUP BY | Add aggregate conditions. |

Click the icon in upper-right corner of the A section and switch the editor to Raw Query Mode. Then, you can enter Lindorm SQL statements to perform complex queries. Sample code:

```
SELECT region,time,avg(temperature) FROM sensor WHERE time >= $from AND time <= $to SAMPLE BY $ interval
```

**Note**

For more information about how to use Lindorm SQL, see Basic syntax of the SELECT statement. time >= $from AND time <= $to specifies a time condition. This condition is required in the statement. If you do not specify it, the query result is not returned. The variables in the condition are automatically replaced with the time range selected on the dashboard page. You can click **Query options** and specify the **Min interval** and **Max data points** parameters to adjust the value of **Interval**. You can use **ALIAS BY** to rename the tags of time series. The alias of a time series is in the $tag_<tag_name> format. For example, you can set the tag of a time series to $tag_host . In this case, the tag of the time series is the hostname. You can use **OFFSET** to configure a time offset. This allows you to compare data that is generated within different time periods. You can specify query conditions and the tables and fields that you want to query in a template to perform simple queries. The following table describes the keywords that you can specify in the editor.

| SAMPLE BY | Select the downsampling interval. You can click Query options and specify the Min interval and Max data points parameters to adjust the value of Interval. |
|---|---|
| ORDER BY TIME | Specify the sorting order. |
| LIMIT | Specify the maximum number of rows that can be returned in a result set. |
| ALIAS BY | Rename the tag of the time series. The alias of a time series is in the $tag <tag name> format. For example, you can set the tag of a time series _ _ to $tag host . In this case, the tag of the time series is the hostname. _ |
| OFFSET | Specify the time offset. This allows you to compare data that is generated within different time periods. |

**Use a self-managed Grafana service deployed on an ECS instance to**

**Deployment requirements**

The operating system of the ECS instance is CentOS 7.3 64-bit or later. The ECS instance must have more than 1 vCPU and 2 GB of memory, and at least 10 GB of available storage space.

**Prerequisites**

Before you start, make sure that the following prerequisites: A rule that allows inbound traffic on port 3000 is added to the security group of the ECS instance. The IP address of the ECS instance is added to the whitelist of the Lindorm instance. If the ECS instance and the Lindorm cluster reside in different VPCs, assign a public IP address to the ECS instance. If you access Grafana over the Internet endpoint, make sure that a public IP address is assigned to the ECS instance. If you access Grafana over the VPC endpoint, you do not need to assign a public IP address to the ECS instance.

**Procedure**

1. Install Grafana. If Grafana is installed, skip this step.
i. Connect to an ECS instance. ii. Run the following command to download Grafana:

```
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-8.2.2-1.x86_64.rpm
```

**Note**

In this example, Grafana 8.2.2-1 is used. You can choose the version of Grafana that you want to install based on your requirements. For more information about how to download other versions of Grafana, visit the Grafana official website. iii. Run the following command to install Grafana:

```bash
sudo yum install grafana-enterprise-8.2.2-1.x86_64.rpm
```

| In the [plugins] section, change | ;allow loading unsigned plugins= _ _ _ |
|---|---|
| allow loading unsigned plugins = alibabacloud-lindorm-datasource _ _ _ |  |

iv. Run the following command to start Grafana:

```bash
sudo service grafana-server start
```

2. Install the Alibaba Cloud Lindorm data source plug-in.
i. Run the following command to download the Alibaba Cloud Lindorm data source plug-in:

```
wget https://tsdbtools.oss-cn-hangzhou.aliyuncs.com/grafana-alibabacloud-lindorm-datasource-lat est.zip
```

ii. Run the following command to extract the package to the default directory. The default directory in Linux is /var/lib/grafana/plugins/.

```
unzip grafana-alibabacloud-lindorm-datasource-latest.zip -d /var/lib/grafana/plugins/
```

iii. Run the following command to modify the grafana.ini file. By default, the path of the file in Linux is /etc/grafana/grafana.ini.

```bash
sudo nano -w /etc/grafana/grafana.ini
```

**Important**

When you modify the grafana.ini file, you must delete the semicolon (;) in

```
 ;allow_loading_unsigned_plugins .
```

v. Run the following command to restart Grafana:

```bash
sudo service grafana-server restart
```

3. Add Lindorm to Grafana as a data source.
i. Enter the following URL in the address bar of your browser: http://IP:3000/. Replace "IP" in the URL with the public IP address or primary private IP address of the ECS instance. Enter the username and password. If you log on to the self-managed Grafana service for the first time, both the username and password are admin. Change the password after you log on to the Grafana service. For more information, see Sign in to Grafana. ii. Click the icon on the left and select **Data Sources** from the drop-down list. iii. On the **Configuration** page, click **Add data source**. iv. On the **Add data source page**, enter `Alibaba Cloud Lindorm` in the search box, find the data source that you want to add, and then click **Select**.

| Section | Parameter | Requi red | Description |
|---|---|---|---|
| Name |  | Yes | The name of the data source. You can retain the default value or enter a custom name. |
| HTTP | URL | Yes | The LindormTSDB endpoint for HTTP. Important If the ECS instance belongs to the same VPC as the Lindorm cluster, use the VPC endpoint of LindormTSDB. Otherwise, use the Internet endpoint of LindormTSDB. If you specify the VPC endpoint of LindormTSDB, make sure that the primary private IP address of the ECS instance is added to the whitelist of the Lindorm cluster. If you specify the Internet endpoint of LindormTSDB, make sure that the public IP address of the ECS instance is added to the whitelist of the Lindorm cluster. |
| Auth | Basic auth | No | If the user authentication and permission verification feature is enabled for LindormTSDB, turn on Basic auth and enter the username and password used to log on to LindormTSDB in the Basic Auth Details section. |
| Basic Auth Details | User | No | The username that is used to log on to the Lindorm cluster. You must specify this parameter if you turn on Basic auth. |
|  | Password | No | The password that is used to log on to the Lindorm cluster. You must specify this parameter if you turn on Basic auth. |
| Lindorm TSDB Details | Database | No | The LindormTSDB database that you want to access. |

v. Configure the parameters described in the following table on the **Settings** tab. You can keep the default values for other parameters. vi. Click **Save & test**. If the "test success" message is returned, the connection test is successful.
4. After you connect the self-managed Grafana service to the Lindorm cluster, you can create and use
dashboards in the Grafana service. For more information, see Create a dashboard.
5. Query data on the **Query** tab.
i. Select the data source that you want to use from the **Data source** drop-down list. ii. To query data in Grafana, you can use the SQL statement editor or template-based query editor.

**SQL statement editor**

Click the icon in upper-right corner of the A section and switch the editor to Raw Query Mode. Then, you can enter Lindorm SQL statements to perform complex queries. Sample code:

```
SELECT region,time,avg(temperature) FROM sensor WHERE time >= $from AND time <= $to SAMPLE BY $ interval
```

| Keyword | Description |
|---|---|
| SELECT | Specify the name of the field that you want to query. |
| FROM | Specify the name of the table that you want to query. |
| WHERE | Add query conditions. |
| GROUP BY | Add aggregate conditions. |
| SAMPLE BY | Select the downsampling interval. You can click Query options and specify the Min interval and Max data points parameters to adjust the value of Interval. |
| ORDER BY TIME | Specify the sorting order. |

**Note**

For more information about how to use Lindorm SQL, see Basic syntax of the SELECT statement. time >= $from AND time <= $to specifies a time condition. This condition is required in the statement. If you do not specify it, the query result is not returned. The variables in the condition are automatically replaced with the time range selected on the dashboard page. You can click **Query options** and specify the **Min interval** and **Max data points** parameters to adjust the value of **Interval**. You can use **ALIAS BY** to rename the tags of time series. The alias of a time series is in the $tag_<tag_name> format. For example, you can set the tag of a time series to $tag_host . In this case, the tag of the time series is the host name. You can use **OFFSET** to configure a time offset. This allows you to compare data that is generated within different time periods. You can specify query conditions and the tables and fields that you want to query in a template to perform simple queries. The following table describes the keywords that you can specify in the editor.

| LIMIT | Specify the maximum number of rows that can be returned in a result set. |
|---|---|
| ALIAS BY | Rename the tag of the time series. The alias of a time series is in the $tag <tag name> format. For example, you can set the tag of a time series _ _ to $tag host . In this case, the tag of the time series is the hostname. _ |
| OFFSET | Specify the time offset. This allows you to compare data that is generated within different time periods. |

#### Use Prometheus to connect to and use

## LindormTSDB

LindormTSDB provides APIs for the remote write and remote read features of Prometheus. You can use these APIs to connect LindormTSDB to Prometheus and specify LindormTSDB as the remote storage of Prometheus. You can also use PromQL to call the APIs to efficiently access data in LindormTSDB.

**View the database endpoints for remote read and remote write**

1. Log on to the Lindorm console.
2. On the **Instances** page, click the ID of the Lindorm instance that you want to manage. The **Instance**
**Details** page appears.
3. In the left-side navigation pane of the instance details page, click **Database Connections**.
4. Click the **Time Series Engine** tab.
5. On the **Time Series Engine** tab, you can view the **endpoints** of LindormTSDB.
Based on the LindormTSDB endpoints obtained in the console, you can create the endpoints that can be used for remote read and remote write operations in the following formats: http://ld-****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/prom_write http://ld-****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/prom_read

**Configure Prometheus to remotely read data from and write data to**

Open the Prometheus.yaml configuration file and append the following content to the file. Replace the URLs in the **remote_write** and **remote_read** fields with the endpoints that are created in the preceding step.

```
remote_write:
  - url: "http://ld-****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/prom_write"
remote_read:
  - url: "http://ld-****-proxy-tsdb-pub.lindorm.rds.aliyuncs.com:8242/api/prom_read"
    read_recent: true
```

LindormTSDB provides native support for PromQL. For example, you can use the PromQL plug-in of Grafana to connect to and use LindormTSDB. You can perform the following steps to obtain the LindormTSDB endpoint for PromQL:
1. Log on to the Lindorm console.
2. On the **Instances** page, click the ID of the Lindorm instance that you want to manage. The **Instance**
**Details** page appears.
3. In the left-side navigation pane of the instance details page, click **Database Connections**.
4. Click the **Time Series Engine** tab.
5. Click **PromQL Compatibility Address** to view the endpoints that you can use in PromQL to access
LindormTSDB over the **virtual private cloud (VPC)** or **Internet**.

### Performance white paper

#### Test environment and test tool

This topic describes the test environment used to test the performance of LindormTSDB and how to use the corresponding test tool.

**Requirements on the test environment**

The OS used in the test is Alibaba Cloud Linux 3.2104 64-bit. The stress testing client and LindormTSDB clusters are deployed in the same virtual private cloud (VPC). The instance type of the machine on which the stress testing client runs is ecs.c6e.26xlarge. We recommend that you use a machine that has a specification of 32 cores and 128 GB of memory or higher. Four LindormTSDB clusters of the following specifications are used for testing. All the four clusters use the Standard storage type. Cluster 1: 3-node LindormTSDB cluster in which the specification of each node is 4 cores and 16 GB of memory Cluster 2: 3-node LindormTSDB cluster in which the specification of each node is 8 cores and 32 GB of memory Cluster 3: 3-node LindormTSDB cluster in which the specification of each node is 16 cores and 64 GB of memory Cluster 4: 3-node LindormTSDB cluster in which the specification of each node is 32 cores and 128 GB of memory

**Note**

The preceding specifications are available to the public. The storage type of the clusters is Standard. You can use the Performance storage type for better performance. The version of LindormTSDB that is used for the clusters is 3.4.9.

**Introduction to the test tool**

The test tool is developed to adapt Lindorm based on influxdb-comparisons that is widely used in the sphere of time series databases. The Devops data model of the test tool is used as the data model in the stress testing. This data model is used in scenarios in which a set of servers report system metric values and application metric values at a specified interval. For example, a server samples 101 measurement values in the 9 subsystems at an interval of 10 seconds and reports the values to databases in LindormTSDB. The subsystems are the CPU, memory, disk, disk I/O, kernel, network, Redis, PostgreSQL, and Nginx subsystems.

**Download the test tool**

You can click the download link to download the compressed file of the stress testing tool. Before you perform stress testing, upload the file to your machine on which your stress testing client runs and decompress the file.

**Note**

For more information about how to use the tool, see influxdb-comparisons. You can use the tool in the way similar to influxdb-comparisons.

**Data write test**

Generate the data that you want to write.

```bash
# ${scale}: the number of devices that generate data.
# ${data_file}: the name of the file that you want to generate to store the data.
# ${batch_size}: the size of a batch.
GOGC=500 ./bulk_data_gen -format lindormtsdbbatch -use-case devops -seed 100 -sampling-interval 10s -scale-var ${scale} -batchSize ${batchsize} > ${data_file}
```

Write the generated data.

```bash
# ${data_file}: the name of the generated file.
# ${add}: the endpoint of your LindormTSDB cluster. The endpoint is in the ip:port format. For exam
ple, you can specify ld-8vb458k154q7xxxx-proxy-tsdb.lindorm.rds.aliyuncs.com:8242 as the endpoint.
# ${wokers}: the number of concurrent threads for writing the data.
GOGC=500 ./bulk_load_lindormtsdb_batch -file ${data_file} -url ${add} -workers ${workers} -time-lim it 10m
```

Generate a file that contains your query statements.

```bash
# ${query_type}: the query type.
# ${scale}: the number of devices that are used to query.
# ${queryfile}: the name of the file that you generate to contain your query statements.
GOGC=500 ./bulk_query_gen -seed 123 -queries 100000 -format lindormtsdb -use-case devops -query-typ e ${query_type} -scale-var ${scale} > ${queryfile}
```

**Note**

For more information about ${query_type} , see Results of query tests. Perform the query.

```bash
# ${workers}: the number of concurrent threads for querying the data.
# ${add}: the endpoint of your LindormTSDB cluster. The endpoint is in the ip:port format. For exam
ple, you can specify ld-8vb458k154q7xxxx-proxy-tsdb.lindorm.rds.aliyuncs.com:8242 as the endpoint.
# ${queryfile}: the name of the generated file that contains the query statements.
GOGC=500 ./query_benchmarker_lindormtsdb -workers ${workers} -url ${add} -file ${queryfile}
```

#### Write performance test results

This topic compares the write performance of different ApsaraDB for Lindorm (Lindorm) clusters. This test is performed in an environment in which optimal performance is ensured. During the test, no queries are performed in the environment. The write performance may decrease if the volume of time series data is large or a large number of queries are performed at the same time. We recommend that you analyze your business scenarios before you run the test. The test results are provided only for reference.

**Examples on writing data to ApsaraDB for Lindorm**

Collect 101 measurement values from 9 subsystems of a server, including CPU, memory, disk, disk I/O, kernel, network, Redis, PostgreSQL, and NGINX, at an interval of 10 seconds, and report these values to LindormTSDB. A table is created in LindormTSDB for each subsystem. For information about the definitions of the tables, tags, and fields, see Data model. The following statements are used to create the tables. In each statement, the hostname parameter specifies the unique ID of each device.

```
CREATE table cpu(hostname VARCHAR primary TAG,region VARCHAR TAG,datacenter VARCHAR TAG,rack VARCHA
```

```
R TAG,os VARCHAR TAG,arch VARCHAR TAG,team VARCHAR TAG,service VARCHAR TAG,service_version VARCHAR TAG,service_environment VARCHAR TAG,time BIGINT,usage_user double,usage_system double,usage_idle do uble,usage_nice double,usage_iowait double,usage_irq double,usage_softirq double,usage_steal double ,usage_guest double,usage_guest_nice double); CREATE table mem(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack VAR CHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, time BIGINT,total BIGINT, available BIGINT, used BIGI NT, `free` BIGINT, cached BIGINT, buffered BIGINT, used_percent double, available_percent double, b uffered_percent double); CREATE table disk(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack VA RCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, path VARCHAR TAG, fstype VARCHAR TAG,time BIGINT,tota l BIGINT, `free` BIGINT, used BIGINT, used_percent BIGINT, inodes_total BIGINT, inodes_free BIGINT, inodes_used BIGINT); CREATE table diskio(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack VARCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, serial VARCHAR TAG,time BIGINT,`reads` BIGINT, writes BIGINT, read_bytes BIGINT, write_bytes BIGINT, read_time BIGINT, writ e_time BIGINT, io_time BIGINT); CREATE table kernel(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack VARCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG,time BIGINT,boot_time BIGINT, interrup ts BIGINT, context_switches BIGINT, processes_forked BIGINT, disk_pages_in BIGINT, disk_pages_out B IGINT); CREATE table net(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack VAR CHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, interface VARCHAR TAG,time BIGINT, bytes_sent BIGINT, bytes_recv BIGINT, packets_sent BIGINT, packets_recv BIGINT, err_in BIGINT, err_out BIGINT, drop_in BIGINT, drop_out BIGINT ); CREATE table redis(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack V ARCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, port VARCHAR TAG, server VARCHAR TAG, time BIGINT, uptime_in_seconds BIGINT, total_connections_received BIGINT, expired_keys BIGINT, evic ted_keys BIGINT, keyspace_hits BIGINT, keyspace_misses BIGINT, instantaneous_ops_per_sec BIGINT, in stantaneous_input_kbps BIGINT, instantaneous_output_kbps BIGINT, connected_clients BIGINT, used_mem ory BIGINT, used_memory_rss BIGINT, used_memory_peak BIGINT, used_memory_lua BIGINT, rdb_changes_since_last_save BIGINT, sync_full BIGINT, sync_partial_ok BIGINT, sync_partial_err BIGI NT, pubsub_channels BIGINT, pubsub_patterns BIGINT, latest_fork_usec BIGINT, connected_slaves BIGIN T, master_repl_offset BIGINT, repl_backlog_active BIGINT, repl_backlog_size BIGINT, repl_backlog_histlen BIGINT, mem_fragmentation_ratio BIGINT, used_cpu_sys BIGINT, used_cpu_user BIG INT, used_cpu_sys_children BIGINT, used_cpu_user_children BIGINT); CREATE table postgresl(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, ra ck VARCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, time BIGINT,numbackends BIGINT, xact_ commit BIGINT, xact_rollback BIGINT, blks_read BIGINT, blks_hit BIGINT, tup_returned BIGINT, tup_fe tched BIGINT, tup_inserted BIGINT, tup_updated BIGINT, tup_deleted BIGINT, conflicts BIGINT, temp_f iles BIGINT, temp_bytes BIGINT, deadlocks BIGINT, blk_read_time BIGINT, blk_write_time BIGINT ); CREATE table nginx(hostname VARCHAR primary TAG, region VARCHAR TAG, datacenter VARCHAR TAG, rack V ARCHAR TAG, os VARCHAR TAG, arch VARCHAR TAG, team VARCHAR TAG, service VARCHAR TAG, service_version VARCHAR TAG, service_environment VARCHAR TAG, port VARCHAR TAG, server VARCHAR TAG, time BIGINT,accepts BIGINT, active BIGINT, handled BIGINT, reading BIGINT, requests BIGINT, waiting BIGINT, writing BIGINT );
```

The following sample statements show how to insert data into each table:

```
cpu(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment, time ,usage_user,usage_system,usage_idle,usage_nice,usage_iowait,usage_irq,usage_softirq,usage_steal,usage est,usage_guest_nice) VALUES ('host_0','ap-northeast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test',1514764800000,60.4660287979619540,94.0509088045012 ,66.4560053218490481,43.7714187186980155,42.4637497071265670,68.6823072867109374,6.5637019217476222,1 519254732791246,9.6969518914484567,30.0911860585287059); diskio(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment,seria time ,`reads`,writes,read_bytes,write_bytes,read_time,write_time,io_time) VALUES ('host_0','ap-nort heast-1','ap-northeast-1a','72','Ubuntu16.10','x86','CHI','10','0','test','694-511- 162',1514764800000,0,0,3,0,0,7,0); disk(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment,path,fs e, time ,total,`free`,used,used_percent,inodes_total,inodes_free,inodes_used) VALUES ('host_0','apnortheast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test','/dev/sda9','ext4',1514764800000,1099511627776,549 813888,549755813888,50,268435456,134217728,134217728); kernel(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment, ti me ,boot_time,interrupts,context_switches,processes_forked,disk_pages_in,disk_pages_out) VALUES ('h ost_0','ap-northeast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test',1514764800000,233,0,1,0,0,0); mem(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment, time ,total,available,used,`free`,cached,buffered,used_percent,available_percent,buffered_percent) VALUE S ('host_0','ap-northeast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test',1514764800000,8589934592,6072208808,2517725783,583 2948,1877356426,2517725783,29.3101857336815748,70.6898142663184217,78.1446947407235797); net(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment,interfac time ,bytes_sent,bytes_recv,packets_sent,packets_recv,err_in,err_out,drop_in,drop_out) VALUES ('hos t_0','ap-northeast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test','eth3',1514764800000,0,0,0,2,0,0,0,0); nginx(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment,port,s er, time ,accepts,active,handled,reading,requests,waiting,writing) VALUES ('host_0','ap-northeast-1 ','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test','12552','nginx_65466',1514764800000,0,0,11,0,0,0,0 postgresl(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment, time ,numbackends,xact_commit,xact_rollback,blks_read,blks_hit,tup_returned,tup_fetched,tup_inserted,tup_u ted,tup_deleted,conflicts,temp_files,temp_bytes,deadlocks,blk_read_time,blk_write_time) VALUES ('ho st_0','ap-northeast-1','ap-northeast- 1a','72','Ubuntu16.10','x86','CHI','10','0','test',1514764800000,0,0,0,0,3,0,0,0,0,0,0,0,12,0,0,0); redis(hostname,region,datacenter,rack,os,arch,team,service,service_version,service_environment,port,s er, time ,uptime_in_seconds,total_connections_received,expired_keys,evicted_keys,keyspace_hits,keyspace_misses stantaneous_ops_per_sec,instantaneous_input_kbps,instantaneous_output_kbps,connected_clients,used_mem ,used_memory_rss,used_memory_peak,used_memory_lua,rdb_changes_since_last_save,sync_full,sync_partial_ sync_partial_err,pubsub_channels,pubsub_patterns,latest_fork_usec,connected_slaves,master_repl_offset pl_backlog_active,repl_backlog_size,repl_backlog_histlen,mem_fragmentation_ratio,used_cpu_sys,used_cp ser,used_cpu_sys_children,used_cpu_user_children) VALUES ('host_0','ap-northeast-1','ap-northeast-1 a','72','Ubuntu16.10','x86','CHI','10','0','test','19071','redis_86258',1514764800000,0,0,0,5,0,0,0,0 0,8589934592,8589934592,8589934592,8589934592,0,0,0,0,36,0,0,0,0,0,0,0,0,0,16,0,0);
```

| batch | worker | tps | max cpu _ |
|---|---|---|---|
| 1 | 1 | 4,846.48 | 36.68 |
| 1 | 16 | 36,862.15 | 78.50 |
| 1 | 50 | 31,653.44 | 73.46 |
| 1 | 100 | 31,521.71 | 74.32 |
| 1 | 200 | 31,651.03 | 73.03 |
| 50 | 1 | 126,462.85 | 65.43 |
| 50 | 16 | 460,032.75 | 79.89 |
| 50 | 50 | 457,791.78 | 81.50 |

In this test, SQL statements are executed to write data. To improve the write performance, execute batch insert statements on each table. You can include a PreparedStatement object in each SQL statement and bind parameters to the object to insert data entries in batches. For more information, see Write data in an efficient manner. The number of devices is 10,000. Each device reports 101 measurement values at an interval of 10 seconds. The values that are collected within 15 days are reported.

**Performance metrics**

This section describes the metrics that are collected to monitor the write performance. tps: the average number of measurement values that are written into a database per second. In LindormTSDB, the tps metric indicates the number of field values that are written into the database per second. For more information, see Terms. worker: the number of concurrent write operations. batch: the number of rows that are written in each batch. max_cpu: the peak CPU utilization in percentage.

**Important**

In this test, data points are inserted in batches. Each write request is sent to write a batch of data points. During the test, no queries are performed on LindormTSDB. Figure 1 Write TPS of Lindorm clusters that use different specifications when the batch size is 500 in different concurrency scenarios

**Table 1 Cluster 1 (3 nodes with a specification of 4 cores and 16 GB of memory)**

| 50 | 100 | 457,956.53 | 82.69 |
|---|---|---|---|
| 50 | 200 | 434,573.47 | 81.18 |
| 100 | 1 | 168,643.80 | 74.14 |
| 100 | 16 | 468,008.25 | 84.09 |
| 100 | 50 | 470,608.31 | 84.34 |
| 100 | 100 | 451,384.44 | 83.32 |
| 100 | 200 | 457,740.22 | 84.61 |
| 200 | 1 | 205,046.31 | 74.77 |
| 200 | 16 | 480,309.56 | 84.74 |
| 200 | 50 | 489,903.34 | 86.73 |
| 200 | 100 | 484,745.44 | 86.77 |
| 200 | 200 | 475,824.97 | 86.55 |
| 500 | 1 | 239,847.34 | 74.76 |
| 500 | 16 | 511,989.50 | 87.86 |
| 500 | 50 | 544,544.75 | 88.23 |
| 500 | 100 | 543,131.56 | 88.12 |
| 500 | 200 | 528,027.12 | 88.57 |

| batch | worker | tps | max cpu _ |
|---|---|---|---|
| 1 | 1 | 3,601.72 | 19.88 |
| 1 | 16 | 46,701.05 | 46.97 |
| 1 | 50 | 69,892.66 | 59.77 |

**Table 2 Cluster 2 (3 nodes with a specification of 8 cores and 32 GB of memory)**

| 1 | 100 | 70,219.33 | 60.32 |
|---|---|---|---|
| 1 | 200 | 70,187.81 | 60.54 |
| 50 | 1 | 114,062.01 | 22.88 |
| 50 | 16 | 1,123,739.88 | 64.66 |
| 50 | 50 | 1,416,314.00 | 70.99 |
| 50 | 100 | 1,421,701.75 | 70.94 |
| 50 | 200 | 1,422,040.12 | 71.56 |
| 100 | 1 | 183,456.98 | 22.38 |
| 100 | 16 | 1,651,046.25 | 65.09 |
| 100 | 50 | 2,029,514.75 | 74.16 |
| 100 | 100 | 2,040,670.38 | 73.39 |
| 100 | 200 | 2,025,066.12 | 73.98 |
| 200 | 1 | 254,914.23 | 24.27 |
| 200 | 16 | 2,172,662.25 | 71.47 |
| 200 | 50 | 2,670,999.25 | 76.47 |
| 200 | 100 | 2,674,582.25 | 76.95 |
| 200 | 200 | 2,693,531.50 | 76.41 |
| 500 | 1 | 332,250.78 | 23.86 |
| 500 | 16 | 2,820,651.50 | 72.56 |
| 500 | 50 | 3,429,375.00 | 80.98 |
| 500 | 100 | 3,442,593.75 | 80.62 |

| 500 | 200 | 3,440,201.50 | 81.12 |
|---|---|---|---|

| batch | worker | tps | max cpu _ |
|---|---|---|---|
| 1 | 1 | 3,897.79 | 8.97 |
| 1 | 16 | 58,217.44 | 27.30 |
| 1 | 50 | 127,110.89 | 50.49 |
| 1 | 100 | 165,754.09 | 62.31 |
| 1 | 200 | 202,844.20 | 70.72 |
| 50 | 1 | 136,378.39 | 11.77 |
| 50 | 16 | 1,634,203.88 | 41.92 |
| 50 | 50 | 2,773,785.75 | 58.96 |
| 50 | 100 | 3,363,458.25 | 67.87 |
| 50 | 200 | 3,703,033.00 | 74.14 |
| 100 | 1 | 198,375.67 | 10.35 |
| 100 | 16 | 2,494,268.00 | 45.86 |
| 100 | 50 | 4,007,320.25 | 60.87 |
| 100 | 100 | 4,753,680.50 | 69.29 |
| 100 | 200 | 5,095,771.00 | 75.17 |
| 200 | 1 | 278,253.53 | 10.57 |
| 200 | 16 | 3,368,596.50 | 45.48 |
| 200 | 50 | 5,214,060.50 | 64.57 |
| 200 | 100 | 6,040,166.50 | 72.35 |

**Table 3 Cluster 3 (3 nodes with a specification of 16 cores and 64 GB of memory)**

| 200 | 200 | 6,283,312.00 | 77.07 |
|---|---|---|---|
| 500 | 1 | 352,744.78 | 10.80 |
| 500 | 16 | 4,281,761.50 | 47.17 |
| 500 | 50 | 6,544,214.00 | 71.73 |
| 500 | 100 | 7,267,295.50 | 77.15 |
| 500 | 200 | 7,290,116.00 | 83.91 |

| batch | worker | tps | max cpu _ |
|---|---|---|---|
| 1 | 1 | 3,405.32 | 4.52 |
| 1 | 16 | 51,460.87 | 11.04 |
| 1 | 50 | 134,289.62 | 27.32 |
| 1 | 100 | 201,014.75 | 40.45 |
| 1 | 200 | 255,692.84 | 51.99 |
| 50 | 1 | 113,644.64 | 5.33 |
| 50 | 16 | 1,596,669.88 | 19.13 |
| 50 | 50 | 3,676,491.50 | 38.75 |
| 50 | 100 | 5,217,282.50 | 50.84 |
| 50 | 200 | 6,345,112.00 | 62.49 |
| 100 | 1 | 188,352.08 | 5.05 |
| 100 | 16 | 2,624,622.50 | 21.15 |
| 100 | 50 | 5,740,561.50 | 40.49 |
| 100 | 100 | 7,521,672.00 | 55.85 |

**Table 4 Cluster 4 (3 nodes with a specification of 32 cores and 128 GB of memory)**

| 100 | 200 | 8,507,855.00 | 61.68 |
|---|---|---|---|
| 200 | 1 | 249,571.77 | 5.05 |
| 200 | 16 | 3,637,803.50 | 21.23 |
| 200 | 50 | 8,141,380.50 | 45.39 |
| 200 | 100 | 10,289,145.00 | 57.85 |
| 200 | 200 | 10,462,525.00 | 60.48 |
| 500 | 1 | 334,678.31 | 5.47 |
| 500 | 16 | 4,657,772.50 | 24.23 |
| 500 | 50 | 10,098,200.00 | 46.90 |
| 500 | 100 | 12,405,648.00 | 64.57 |
| 500 | 200 | 12,136,903.00 | 66.01 |

#### Results of query tests

This topic describes how to test query performance and provides sample test results for queries that are performed on different Lindorm clusters. This test is performed in an environment in which optimal performance is ensured. During the test, no data write operations are performed in the environment. The query performance may decrease in the following scenarios: the volume of time series data is large, a large number of write operations are performed at the same time, and a large number of time series and time points are scanned. We recommend that you analyze your business scenarios before you run the test. The test results are provided only for reference.

**Amount of basic data to be queried**

The number of devices is 100. Each device reports 101 measurement values at an interval of 10 seconds. The data that is collected within one day is reported. Test multiple types of queries. The following items describe the types of queries that can be performed: 1-host-1-hr-raw: queries all the values of the cpu.usage_user metric that are reported from a specified device within a specified 1-hour period.

```
select time, usage_user from cpu where (hostname = 'host_17') and time >=1514837782646 and time < 1 514841382646 ;
```

1-host-1-hr: queries the maximum value of the cpu.usage_user metric that is reported from a specified device in each minute within a specified 1-hour period.

```
select time, max(usage_user) as max_usage_user from cpu where (hostname = 'host_17') and time >=151 4837782646 and time < 1514841382646 sample by 1m
```

| queryType | worker | qps | max cpu _ | max mem _ |
|---|---|---|---|---|
| 1-host-1-hr | 16 | 1,420.96 | 86.95 | 48.08 |
| 1-host-1-hr | 50 | 1,865.50 | 83.45 | 49.32 |
| 1-host-1-hr | 100 | 1,887.00 | 81.71 | 48.95 |

1-host-12-hr-raw: queries all the values of the cpu.usage_user metric that are reported from a specified device within a specified 12-hour period.

```
select time, usage_user from cpu where (hostname = 'host_0') and time >=1514787382646 and time < 15 14830582646;
```

1-host-12-hr: queries the maximum value of the cpu.usage_user metric that is reported from a specified device in each minute within a specified 12-hour period.

```
select time, max(usage_user) as max_usage_user from cpu where (hostname = 'host_0') and time >=1514 787382646 and time < 1514830582646 sample by 1m ;
```

1-host-latest: queries the latest value of the cpu.usage_user metric that is reported from a specified device.

```
select time, latest(usage_user) as latest_usage_user from cpu where (hostname = 'host_50') sample by 0
```

8-host-latest: queries the latest values of the cpu.usage_user metric that are reported from eight devices.

```
select time, latest(usage_user) as latest_usage_user from cpu where (hostname = 'host_64' or hostn ame = 'host_80' or hostname = 'host_21' or hostname = 'host_5' or hostname = 'host_79' or hostname = 'host_47' or hostname = 'host_25' or hostname = 'host_18') sample by 0
```

**Performance metrics**

This section describes the performance metrics that are monitored for the queries that are performed in this test. queryType: the query type. For more information, see the description that is provided in the "Query samples" section. worker: the number of concurrent queries that are performed. qps: the number of SQL queries that are performed per second. max_cpu: the peak CPU utilization in percentage. max_mem: the peak memory usage in percentage.

**Important**

The following query results are separately measured when only the test is run on LindormTSDB. No other workload is run on LindormTSDB. Figure 1. Queries per second (QPS) of Lindorm clusters that use different specifications when different types of queries are performed at a concurrency of 200

**Table 1. Cluster 1 (3 nodes with a specification of 4 cores and 16 GB memory)**

| 1-host-1-hr | 200 | 1,846.00 | 82.99 | 48.87 |
|---|---|---|---|---|
| 1-host-1-hr-raw | 16 | 1,324.80 | 79.54 | 50.34 |
| 1-host-1-hr-raw | 50 | 1,722.00 | 86.42 | 50.96 |
| 1-host-1-hr-raw | 100 | 1,737.00 | 86.36 | 50.92 |
| 1-host-1-hr-raw | 200 | 1,752.00 | 87.09 | 50.88 |
| 1-host-12-hr | 16 | 497.44 | 86.77 | 48.81 |
| 1-host-12-hr | 50 | 555.00 | 95.05 | 48.81 |
| 1-host-12-hr | 100 | 571.00 | 94.97 | 48.90 |
| 1-host-12-hr | 200 | 584.00 | 94.77 | 49.11 |
| 1-host-12-hr-raw | 16 | 286.56 | 82.20 | 51.04 |
| 1-host-12-hr-raw | 50 | 328.00 | 95.34 | 51.14 |
| 1-host-12-hr-raw | 100 | 330.00 | 96.51 | 51.21 |
| 1-host-12-hr-raw | 200 | 334.00 | 96.70 | 51.56 |
| 1-host-latest | 16 | 1,025.12 | 81.79 | 49.34 |
| 1-host-latest | 50 | 1,146.00 | 93.36 | 49.42 |
| 1-host-latest | 100 | 1,144.00 | 92.41 | 49.36 |
| 1-host-latest | 200 | 1,164.00 | 92.89 | 49.44 |
| 8-host-latest | 16 | 175.20 | 96.65 | 49.64 |
| 8-host-latest | 50 | 180.00 | 97.01 | 49.95 |
| 8-host-latest | 100 | 181.00 | 96.59 | 50.05 |
| 8-host-latest | 200 | 182.00 | 96.73 | 50.15 |

**Table 2. Cluster 2 (3 nodes with a specification of 8 cores and 32 GB memory)**

| queryType | worker | qps | max cpu _ | max mem _ |
|---|---|---|---|---|
| 1-host-1-hr | 16 | 2,426.56 | 79.45 | 31.83 |
| 1-host-1-hr | 50 | 3,363.50 | 71.58 | 33.50 |
| 1-host-1-hr | 100 | 3,530.00 | 73.80 | 35.44 |
| 1-host-1-hr | 200 | 3,584.00 | 70.12 | 35.43 |
| 1-host-1-hr-raw | 16 | 2,181.92 | 52.67 | 36.10 |
| 1-host-1-hr-raw | 50 | 3,231.50 | 69.77 | 36.20 |
| 1-host-1-hr-raw | 100 | 3,371.00 | 72.88 | 36.19 |
| 1-host-1-hr-raw | 200 | 3,348.00 | 69.80 | 35.08 |
| 1-host-12-hr | 16 | 877.44 | 59.57 | 35.66 |
| 1-host-12-hr | 50 | 1,132.50 | 82.37 | 35.51 |
| 1-host-12-hr | 100 | 1,145.00 | 84.10 | 35.55 |
| 1-host-12-hr | 200 | 1,152.00 | 84.69 | 35.62 |
| 1-host-12-hr-raw | 16 | 445.44 | 58.55 | 35.29 |
| 1-host-12-hr-raw | 50 | 641.00 | 84.98 | 35.31 |
| 1-host-12-hr-raw | 100 | 668.00 | 90.79 | 35.35 |
| 1-host-12-hr-raw | 200 | 670.00 | 91.98 | 35.42 |
| 1-host-latest | 16 | 1,785.44 | 51.20 | 35.80 |
| 1-host-latest | 50 | 2,273.50 | 64.86 | 35.92 |
| 1-host-latest | 100 | 2,280.00 | 64.97 | 35.82 |
| 1-host-latest | 200 | 2,284.00 | 65.01 | 35.85 |
| 8-host-latest | 16 | 439.04 | 85.04 | 35.98 |

| 8-host-latest | 50 | 471.50 | 91.71 | 36.00 |
|---|---|---|---|---|
| 8-host-latest | 100 | 472.00 | 92.42 | 36.08 |
| 8-host-latest | 200 | 470.00 | 93.10 | 36.09 |

| queryType | worker | qps | max cpu _ | max mem _ |
|---|---|---|---|---|
| 1-host-1-hr | 16 | 3,287.84 | 49.77 | 25.83 |
| 1-host-1-hr | 50 | 6,543.50 | 56.06 | 26.45 |
| 1-host-1-hr | 100 | 7,713.00 | 59.81 | 26.48 |
| 1-host-1-hr | 200 | 8,902.00 | 75.23 | 26.47 |
| 1-host-1-hr-raw | 16 | 2,857.60 | 32.42 | 26.89 |
| 1-host-1-hr-raw | 50 | 5,173.00 | 50.44 | 26.96 |
| 1-host-1-hr-raw | 100 | 6,177.00 | 56.88 | 26.95 |
| 1-host-1-hr-raw | 200 | 6,530.00 | 59.20 | 26.98 |
| 1-host-12-hr | 16 | 1,148.48 | 38.69 | 26.52 |
| 1-host-12-hr | 50 | 1,920.50 | 71.18 | 26.57 |
| 1-host-12-hr | 100 | 2,181.00 | 82.79 | 26.62 |
| 1-host-12-hr | 200 | 2,398.00 | 91.44 | 26.64 |
| 1-host-12-hr-raw | 16 | 539.20 | 33.78 | 27.04 |
| 1-host-12-hr-raw | 50 | 704.50 | 46.87 | 27.12 |
| 1-host-12-hr-raw | 100 | 612.00 | 41.76 | 27.17 |
| 1-host-12-hr-raw | 200 | 694.00 | 46.89 | 27.24 |
| 1-host-latest | 16 | 2,141.60 | 40.24 | 26.69 |

**Table 3. Cluster 3 (3 nodes with a specification of 16 cores and 64 GB memory)**

| 1-host-latest | 50 | 3,602.00 | 77.84 | 26.69 |
|---|---|---|---|---|
| 1-host-latest | 100 | 4,098.00 | 91.87 | 26.72 |
| 1-host-latest | 200 | 4,356.00 | 94.94 | 26.71 |
| 8-host-latest | 16 | 541.28 | 81.87 | 26.77 |
| 8-host-latest | 50 | 599.50 | 97.52 | 26.77 |
| 8-host-latest | 100 | 648.00 | 97.85 | 26.88 |
| 8-host-latest | 200 | 832.00 | 97.40 | 26.94 |

| queryType | worker | qps | max cpu _ | max mem _ |
|---|---|---|---|---|
| 1-host-1-hr | 16 | 3,543.04 | 24.25 | 28.33 |
| 1-host-1-hr | 50 | 9,351.00 | 34.14 | 28.89 |
| 1-host-1-hr | 100 | 12,567.00 | 46.42 | 28.92 |
| 1-host-1-hr | 200 | 15,072.00 | 57.27 | 28.94 |
| 1-host-1-hr-raw | 16 | 2,811.20 | 15.41 | 29.11 |
| 1-host-1-hr-raw | 50 | 6,086.50 | 27.85 | 29.13 |
| 1-host-1-hr-raw | 100 | 7,881.00 | 36.44 | 29.14 |
| 1-host-1-hr-raw | 200 | 8,762.00 | 40.97 | 29.17 |
| 1-host-12-hr | 16 | 1,394.24 | 18.85 | 28.91 |
| 1-host-12-hr | 50 | 3,317.50 | 49.89 | 28.96 |
| 1-host-12-hr | 100 | 4,160.00 | 67.13 | 28.96 |
| 1-host-12-hr | 200 | 4,808.00 | 79.02 | 28.96 |
| 1-host-12-hr-raw | 16 | 542.56 | 17.31 | 29.22 |

**Table 4. Cluster 4 (3 nodes with a specification of 32 cores and 128 GB memory)**

| 1-host-12-hr-raw | 50 | 826.50 | 24.96 | 29.24 |
|---|---|---|---|---|
| 1-host-12-hr-raw | 100 | 669.00 | 23.55 | 29.28 |
| 1-host-12-hr-raw | 200 | 772.00 | 24.86 | 29.32 |
| 1-host-latest | 16 | 2,600.00 | 16.04 | 28.97 |
| 1-host-latest | 50 | 6,590.00 | 46.11 | 28.98 |
| 1-host-latest | 100 | 8,516.00 | 65.60 | 28.99 |
| 1-host-latest | 200 | 9,634.00 | 75.93 | 28.98 |
| 8-host-latest | 16 | 949.12 | 55.91 | 29.03 |
| 8-host-latest | 50 | 1,525.50 | 83.49 | 29.04 |
| 8-host-latest | 100 | 1,710.00 | 93.16 | 29.06 |
| 8-host-latest | 200 | 1,758.00 | 95.54 | 29.09 |

| Term | Description |
|---|---|
| Table | A time series table stores data of the same type. For example, you can create a time series table to store monitoring data that is generated by air quality sensors. |
| Time | The time when the data is collected from the data source. The data is accurate to milliseconds. |
| Tag | A tag is used to describe a data source. In most cases, a tag value remains unchanged over time. For example, you can create tags for a sensor based on information such as the ID of the sensor and the region where the sensor is deployed. A database in LindormTSDB automatically indexes tags and allows you to query data based on tags form multiple dimensions. Tags must be of the String type and can only be specified when you create a table. |
| Field | A metric that describes a data source. The value of a field consistently changes over time. For example, fields such as temperature and humidity are defined for sensors. |

| Data type | Description |
|---|---|
| double | Numeric data. |

### TSQL syntax

#### Terms

#### Data types

| indorm | Developer Guide·LindormTSDB |
|---|---|

| Data type | Description |
|---|---|
| varchar | String data. |
| boolean | Boolean data. Valid values: true and false. |
| time | Time data. Only positive integers whose unit is ms (millisecond) are supported. |

| Parameter | Description |
|---|---|
| tag definition _ | Specify a tag column in the table. You must specify a tag column. Otherwise, the data is identified as field data, and the data type is VARCHAR. |
| time | Specify a time column that is accurate to the millisecond and uses the BIGINT data type. |
| field name _ | Specify the field column. Supported data types include DOUBLE, VARCHAR, and BOOLEAN. |

#### DDL

##### CREATE TABLE

Create a table.

```
create_table_statement ::= CREATE TABLE table_name '('
                              tag_definition
                              ( ',' tag_definition )*
                              ( ',' time_definition)?
                              ( ',' field_definition )*
                              ')'
tag_definition ::= tag_name VARCHAR TAG time_definition ::= time BIGINT field_definition ::= field_name TYPE
```

**Usage notes**

You must create a table before you can write data. You must specify a tag list in advance. The tag list cannot be modified after it is created. You can specify the time and field_name parameters before or after you write data. When data is being written, the system automatically creates and adjusts the data types based on the recently written data. Create a time series table named sensor and specify the device_id column and the region column as tag columns. Use the temperature column and humidity column as field columns.

```
    device_id VARCHAR TAG,
    region VARCHAR TAG,
    time BIGINT,
    temperature DOUBLE,
    humidity DOUBLE);
```

##### SHOW TABLES

This topic describes the syntax that is used to query the information about tables.

```
> show tables;
+-------------+------------+
| tableSchem  | tableName  |
+-------------+------------+
| default     | sensor     |
| metadata    | COLUMNS    |
| metadata    | TABLES     |
+-------------+------------+
```

##### DESCRIBE TABLE

This topic describes the syntax that is used to query the schema of a table.

```
describe_table_statement ::= DESCRIBE TABLE table_name
> describe table sensor;
+--------------+-----------+
|  columnName  | typeName  |
+--------------+-----------+
| device_id    | VARCHAR   |
| region       | VARCHAR   |
| time         | BIGINT    |
| temperature  | DOUBLE    |
| humidity     | DOUBLE    |
+--------------+-----------+
```

#### DML

##### SELECT

This topic describes the syntax of the SELECT statement.

```
                      FROM table_name
                      WHERE where_clause
                      [ SAMPLE BY time_interval [ FILL fill_option ] ]
                      [ GROUP BY group_by_clause ]
                      [ ORDER BY ordering_clause ]
                      [ LIMIT integer [ OFFSET integer ] ]
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] )
                      | field_name
                      | COUNT '(' '*' ')'
where_clause ::= relation ( ( AND | OR ) relation )* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | CONTAINS | CONTAINS KEY group_by_clause ::= field_name ( ',' field_name )* ordering_clause ::= field_name [ ASC | DESC ] ( ',' field_name [ ASC | DESC ] )*
```

**Usage notes**

You must specify a time range in the SELECT statement. For example, you can specify a time range in the `time > xxx and time < xxx` format. The LIMIT clause is used to filter the results that are returned by the SELECT statement. We recommend that you add more conditions in the WHERE clause to reduce the number of data points that are scanned because the LIMIT clause is not efficient in data filtering. To count the number of data records generated for the device whose ID is `1234ABC` within a time period, execute the following statement:

```
> select count(*) from sensor where device_id = '1234ABC' and time >= 1619076780000 and time <= 1
619076800000; +---------+
| EXPR$0  |
+---------+
| 5       |
+---------+
```

To query all metrics of the device whose ID is `1234ABC` within a time period, execute the following statement:

```
> select * from sensor where device_id = '1234ABC' and time >= 1619076780000 and time <= 16190768
00000; +------------+-----------+----------------+--------------+-----------+
| device_id  |  region   |      time      | temperature  | humidity  |
+------------+-----------+----------------+--------------+-----------+
| 1234ABC   | north-cn  | 1619076780000  | 12.1         | 45        |
| 1234ABC   | north-cn  | 1619076790000  | 13.2         | 47        |
| 1234ABC   | north-cn  | 1619076800000  | 10.6         | 46        |
+------------+-----------+----------------+--------------+-----------+
```

To query the temperature and humidity of the device whose ID is `1234ABC` within a time period, execute the following statement:

| Parameter | Description |
|---|---|
| interval | Specify a numeric value, such as 5 or 60. A value of 0all specifies that the data points within the time range are aggregated into a single data point. |
| units | s represents seconds. m represents minutes. h represents hours. d represents days. n represents months. y represents years. Note You can downsample data based on a calendar time interval. To use the calendar time interval, add c to the end of the value of the units parameter. For example, 1dc indicates the 24-hour period from 00:00 of the current day to 00:00 of the next day. |

|  | c |
|---|---|
| 1dc |  |

```
> select region,time,temperature,humidity from sensor where device_id = '1234ABC' and time >= 161
9076780000 and time <= 1619076800000; +-----------+----------------+--------------+-----------+
|  region   |      time      | temperature  | humidity  |
+-----------+----------------+--------------+-----------+
| north-cn  | 1619076780000  | 12.1         | 45        |
| north-cn  | 1619076790000  | 13.2         | 47        |
| north-cn  | 1619076800000  | 10.6         | 46        |
+-----------+----------------+--------------+-----------+
```

To query the maximum temperature of the device whose ID is `1234ABC` within a time period, execute the following statement:

```
> select max(temperature) from sensor where device_id = '1234ABC' and time >= 1619076780000 and t
ime <= 1619076800000; +---------+
| EXPR$0  |
+---------+
| 13.2    |
+---------+
```

##### Downsampling

```
select_sample_by_statement ::= SELECT ( select_clause | '*' )
                                FROM table_name
                                WHERE where_clause
                                SAMPLE BY time_interval [ FILL fill_option ]
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] ) selector ::= tag_name | time | function_name '(' field_name [ ',' function_args ] ')' where_clause ::= relation ( AND relation )* (OR relation)* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN | CONTAINS | CONTAINS KEY time_interval ::= interval units
```

**Parameters**

The downsampling query reduces the precision of each timeline based on the time specified by sample by. For more information about timelines, see Terms. Interpolation: interpolates points in time when no data is found after downsampling. For more information about the supported fill policies, see Table 2: Interpolation functions. To query data from the tag column of a table, you do not need to specify a function for downsampling in the SELECT statement. If you want to query data from non-tag columns, you must specify a function for downsampling. For more information about the supported downsampling functions, see Table 1: Downsampling aggregate operators. Sample statement:

```
select device_id,region,time,avg(temperature) from sensor where device_id = 'F07A1260' and time >= 1619076780000 and time <= 1619076800000 sample by 20s;
```

The SAMPLE BY clause cannot be used together with the GROUP BY or LIMIT OFFSET clause. However, you can include the GROUP BY and LIMIT OFFSET clauses in SQL statements to specify subqueries. Example:

```
> select region, max(avg_temperature) from (select device_id,region,time,avg(temperature) as avg_te
mperature from sensor where time >= 1619076780000 and time <= 1619076800000 sample by 20s) group by region; +-----------+---------------------+
|  region   |       EXPR$1        |
+-----------+---------------------+
| north-cn  | 12.649999999999999  |
| south-cn  | 18.9                |
+-----------+---------------------+
```

When you include the LIMIT OFFSET clause in SQL statements, we recommend that you limit the amount of data because the LIMIT OFFSET clause does not support pushdown optimization.

```
> select device_id,region, avg_temperature from (select device_id,region,time,avg(temperature) as a
vg_temperature from sensor where time >= 1619076780000 and time <= 1619076800000 sample by 20s) lim it 1 offset 1; +------------+-----------+------------------+
| device_id  |  region   | avg_temperature  |
+------------+-----------+------------------+
| F07A1260   | north-cn  | 10.6             |
+------------+-----------+------------------+
```

Interpolate a specified value based on a specified time interval:

```
> select device_id,region,time,avg(temperature) from sensor where time >= 1619076780000 and time <=
1619076800000 sample by 20s fill 1; +------------+-----------+----------------+---------------------+
| device_id  |  region   |      time      |       EXPR$3        |
+------------+-----------+----------------+---------------------+
| F07A1260   | north-cn  | 1619076780000  | 12.649999999999999  |
| F07A1260   | north-cn  | 1619076800000  | 10.6                |
| F07A1260   | north-cn  | 1619076820000  | 1.0                 |*
| F07A1261   | south-cn  | 1619076780000  | 18.9                |
| F07A1261   | south-cn  | 1619076800000  | 1.0                 |*
| F07A1261   | south-cn  | 1619076820000  | 1.0                 |*
+------------+-----------+----------------+---------------------+
```

Interpolate the value that is collected within the previous time window:

| Operator | Description |
|---|---|
| avg | Returns the average value. |
| count | Returns the number of data points. |
| first | Returns the first value. |
| last | Returns the last value. |
| min | Returns the minimum value. |
| max | Returns the maximum value. |
| median | Returns the median data point value. |
| sum | Returns the sum of values. |
| zimsum | Returns the sum of values. |
| rfirst | The same as the first operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rlast | The same as the last operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rmin | The same as the min operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rmax | The same as the max operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |

```
> select device_id,region,time,avg(temperature) from sensor where time >= 1619076780000 and time <=
1619076800000 sample by 20s fill previous; +------------+-----------+----------------+---------------------+
| device_id  |  region   |      time      |       EXPR$3        |
+------------+-----------+----------------+---------------------+
| F07A1260   | north-cn  | 1619076780000  | 12.649999999999999  |
| F07A1260   | north-cn  | 1619076800000  | 10.6                |
| F07A1260   | north-cn  | 1619076820000  | 10.6                |*
| F07A1261   | south-cn  | 1619076780000  | 18.9                |
| F07A1261   | south-cn  | 1619076800000  | 18.9                |*
| F07A1261   | south-cn  | 1619076820000  | 18.9                |*
+------------+-----------+----------------+---------------------+
```

Interpolation is not supported by the rfirst, rlast, rmin, and rmax operators.

| Fill Policy | Interpolated value |
|---|---|
| none | No values are interpolated. This is the default value. |
| nan | NaN |
| null | null |
| zero | 0 |
| linear | Performs linear interpolation. |
| previous | Interpolates the previous value. |
| near | Interpolates the adjacent value. |
| after | Interpolates the next value. |
| fixed | Interpolates a specified value. |

##### Query the latest values

This topic describes the syntax that is used to query the latest values of each time series in LindormTSDB. LindormTSDB is a time series engine provided by Lindorm.

```
select_latest_by_statement ::= SELECT ( select_clause )
                                FROM table_name
                                WHERE where_clause
                                SAMPLE BY 0
select_clause ::= selector [ AS identifier ] ( ',' selector [ AS identifier ] ) selector ::= tag_name | time | latest '(' field_name [ ',' integer ] ')' where_clause ::= relation ( AND relation )* (OR relation)* relation ::= ( field_name | tag_name ) operator term operator ::= '=' | '<' | '>' | '<=' | '>=' | '!=' | IN
```

**Note**

Latest-value queries are used to query the values of the latest time points in time series. You can use `latest(field_name, N)` to query the latest N records of data. A latest-value query must be used together with `SAMPLE BY 0` to query the latest values of each time series. Latest-value queries cannot be used together with other aggregate functions such as RATE, DELTA, MAX, or MIN. For example, if you execute the `select time, latest(f1), max(f2) from` `sensor sample by 0` statement, a syntax error occurs. Query the latest temperature records of the `F07A1260` device and the `F07A1261` device.

```
lindorm> select device_id,region,time,latest(temperature) as temperature from sensor where device_i d in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+
| device_id | region |      time      | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  |
+-----------+----------+---------------------------+-------------+
```

Query the latest temperature and humidity records of the `F07A1260` device and the `F07A1261` device.

```
lindorm> select device_id,region,time,latest(temperature) as temperature, latest(humidity) as humid ity from sensor where device_id in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+-----------+
| device_id | region |      time      | temperature | humidity |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  | 47.000000 |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  | 43.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

When you use the LATEST function to query the latest values of multiple columns, null is displayed if the latest values of multiple columns cannot be aligned in time. The following statement provides an example:

```
lindorm> select device_id,region,time,latest(temperature) as temperature, latest(humidity) as humid ity from sensor where device_id in ('F07A1260') sample by 0; +-----------+----------+---------------------------+-------------+-----------+
| device_id | region |      time      | temperature | humidity |
+-----------+----------+---------------------------+-------------+-----------+
| F07A1260 | north-cn | 2021-01-01T12:00:00+08:00 | 15.200000  | null   |
| F07A1260 | north-cn | 2021-01-01T13:00:00+08:00 | null    | 47.000000 |
+-----------+----------+---------------------------+-------------+-----------+
```

Query the latest two temperature records of the `F07A1260` device and the `F07A1261` device.

```
lindorm> select device_id,region,time,latest(temperature, 2) as temperature from sensor where devic e_id in ('F07A1260', 'F07A1261') sample by 0; +-----------+----------+---------------------------+-------------+
| device_id | region |      time      | temperature |
+-----------+----------+---------------------------+-------------+
| F07A1260 | north-cn | 2021-01-01T14:03:00+08:00 | 2.000000  |
| F07A1260 | north-cn | 2021-01-01T20:00:00+08:00 | 10.000000  |
| F07A1261 | north-cn | 2021-03-08T12:08:00+08:00 | 5.000000  |
| F07A1261 | north-cn | 2021-05-01T13:00:00+08:00 | 6.000000  |
+-----------+----------+---------------------------+-------------+
```

**Note**

Latest-value queries cannot be directly used with clauses such as OFFSET, LIMIT, or GROUP BY. You can use a latest-value query as a subquery in an SQL statement that contains these clauses. Use the LATEST function together with the GROUP BY clause to group returned data records.

```
lindorm> select device_id, max(temperature) as max_temperature from (select device_id, region,time, latest(temperature,2) as temperature from sensor sample by 0) group by device_id; +-----------+-----------------+
| device_id | max_temperature |
+-----------+-----------------+
| F07A1261 | 6.000000    |
| F07A1260 | 10.000000    |
+-----------+-----------------+
```

Use the LATEST function together with the LIMIT and OFFSET clauses to limit the number of data records that can be returned.

| Parameter | Description |
|---|---|
| tag name _ | The tag names of the data that you want to write. The tag names must be consistent with the names of the tags that are specified in the CREATE TABLE statement. All tags specified in the CREATE TABLE statement must be specified in this parameter. This parameter is required. |
| time | The time when the data is written. The value of this parameter must be a positive integer. This parameter is required. Unit: milliseconds. |
| field name _ | The name of the column to which data is written. We recommend that you specify a column whose data type is the same as that specified in the CREATE TABLE statement. Otherwise, the type of the data that is most recently written to the column prevails. If a column is not specified, the value in this column is set to null by default. |

```
lindorm> select device_id, region, temperature from (select device_id, region, time, latest(temperature,2) as temperature from sensor sample by 0) limit 1 offset 1; +-----------+----------+-------------+
| device_id | region | temperature |
+-----------+----------+-------------+
| F07A1260 | north-cn | 10.000000  |
+-----------+----------+-------------+
```

##### INSERT

Write data.

```
create_table_statement ::= insert into table_name'('
                              tag_name
                              (',' tag_name)*
                              ',' time ','
                              field_name
                              (',' field_name)*
                           ')' values
                           ('('
                              (',' tag_value)*
                              ',' time_value ','
                              field_value
                              (',' tag_value)*
                           ')')+
```

**Usage notes**

Write one data entry each time:

```
insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076780000,12.1,45); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076790000,13.2,47); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1260','north-cn', 1619076800000,10.6,46); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1261','south-cn', 1619076780000,18.1,44); insert into sensor (device_id, region, time, temperature, humidity) values('F07A1261','south-cn', 1619076790000,19.7,44);
```

| API | Description |
|---|---|
| /api/put | Write data points to a single-value model time series |
| /api/mput | Write data points to a multi-value model time series |
| /api/mquery | Query data points from a multi-value model time series |
| /api/query/mlast | Query the latest data points from a multi-value model time series |
| /api/suggest | Query metrics, fields, tag keys, and tag values |
| /api/dump meta _ | Query tag values by tag key |
| /api/ttl | Configure a data TTL |
| /api/delete data _ | Delete data from a time series |

Write data entries in a batch:

```
insert into sensor (device_id, region, time, temperature, humidity) values
    ('F07A1260','north-cn',1619076780000,12.1,45),
    ('F07A1260','north-cn',1619076790000,13.2,47),
    ('F07A1260','north-cn',1619076800000,10.6,46),
    ('F07A1261','south-cn',1619076780000,18.1,44),
    ('F07A1261','south-cn',1619076790000,19.7,44);
```

### HTTP API reference

#### HTTP API overview

LindormTSDB allows you to write and query data over HTTP. LindormTSDB provides an HTTP API which establishes communication with external systems. You can call API operations to use almost all features of LindormTSDB. For example, you can query time series data, manage metadata, and store data points by calling the corresponding API operations. The HTTP API of LindormTSDB is a RESTful API. The HTTP API also supports alternative access methods because not all clients comply with the RESTful conventions. By default, data is transmitted in the JSON format. All responses contain standard HTTP status codes. Error messages are returned in a specific format. You can call the following API operations to read, write, and manage data. For more information about how to call each API operation, click the links in the Reference column.

#### Request method

##### Request syntax

This topic describes the request syntax of the LindormTSDB API. You can view the endpoints of a LindormTSDB instance on the Instance Details page. For example, the endpoint may be ts-xxx.hitsdb.rds.aliyuncs.com:8242.

| HTTP METHOD | Description | Alternative parameter |
|---|---|---|
| GET | Queries data. | N/A |
| POST | Submits data. | method override=post _ |
| PUT | Overwrites data. | method override=put _ |
| DELETE | Deletes data. | method override=delete _ |

| Field | Type | Required | Description | Example |
|---|---|---|---|---|
| code | Integer | Yes | The HTTP status code. | 400 |

You can send requests over HTTP. You can send requests by using the HTTP POST method.

**Request path**

You must specify the path for the API operation in each request, such as `/api/delete_data` .

**Request parameters**

You can specify request parameters for each write request on LindormTSDB. The request parameters specify the expected content in the response and the timeout period of the write request.

**Request content**

You must specify the requested content for each API request on LindormTSDB. Specify the data that you want to query and the operation that you want to perform.

**Request standards**

The HTTP API of LindormTSDB is a RESTful API. This means that you must use an HTTP method to specify an operation and comply with the RESTful conventions. If you use the GET method, the system only returns data. If you use the PUT or POST method, you can only modify data. If you use the DELETE method, you can only delete data. However, in some cases, methods such as DELETE and PUT are blocked by firewalls or proxies, or not implemented on a client. In addition, most developers use GET and POST to send requests. The LindormTSDB API allows you to add the method_override parameter to a query string instead of using HTTP methods. This parameter allows clients to use query strings instead of the HTTP request body to call most API operations. For example, you do not need to use the GET method to delete data. Instead, you can use the following query string: /api/delete_meta?m=cpu.usage&method_override=delete. The following table describes the HTTP methods and corresponding values of the method_override parameter.

##### Response

The LindormTSDB API returns a standard HTTP response status code for each request. Most responses contain response content. For example, failure responses contain specific error information.

**Success request**

If a request is successful, a success status code is returned. If this request queries data, the queried data is returned. Different API operations return different data in different formats. For more information, see Write data points to a single-value model time series and Query data points from a single-value model time series.

**Error request**

If an error occurs, the called API operation returns a formatted JSON object that describes the error. The JSON object contains the following parameters.

| message | String | Yes | The description of the error. | Missing required parameter |
|---|---|---|---|---|
| details | String | Optional | The details of the error. | Missing value: type |

| Request path | Request method | Description |
|---|---|---|
| /api/put | POST | Writes multiple data points at the same time. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| summary | Untyped | No | Specifies whether to return the summary. | false | /api/put? summary |
| details | Untyped | No | Specifies whether to return the details. | false | /api/put?details |

Each error response contains an HTTP status code and response content that describes the error details. Sample response to an error request:

```
1. {
2.    "error": {
3.        "code": 400,
4.        "message": "Missing parameter <code>type</code>"
5.    }
6.  }
```

##### Signature method

This topic describes the signature method of LindormTSDB. LindormTSDB does not provide an identity authentication system or an access control system. Therefore, LindormTSDB does not verify the identity of the user who calls the API operations to write and read data. However, LindormTSDB supports virtual private clouds (VPCs) on Alibaba Cloud. You can deploy your Lindorm instance in a VPC to isolate and secure your data. LindormTSDB also allows you to configure an IP address whitelist for your Lindorm instance to ensure fine-grained data protection.

#### Write data points to a single-value model

**time series**

##### Write data points to a single-value model time

**series**

**Request path and method**

**Request parameters**

| sync timeout _ | Integer | No | The timeout period. Unit: milliseconds. A value of 0 specifies that the request never times out. | 0 | /api/put/? sync&sync time _ out=60000 |
|---|---|---|---|---|---|

| Parameter | Type | Required | Limit | Description | Example |
|---|---|---|---|---|---|
| metric | String | Yes | It can contain uppercase letters, lowercase letters, digits, and the following special characters: - . _ / ( ) : , [ ] = ' # | The name of the metric to be stored. | sys.cpu |
| timestamp | Long | Yes | None | The timestamp. Unit: seconds or milliseconds. For more information about how LindormTSDB determines the unit of a timestamp, see the "Timestamp units" section of this topic. | 1499158925 |
| value | Long,Double,Str ing,Boolean | Yes | None | The value in the data point. | 42.5, true |
| tags | Map | No | It can contain letters, digits, and the following special characters: - . _ / ( ) : , [ ] = ' # | The tag key- value pairs. Tag keys and tag values are character strings. Specify at least one tag key-value pair. | {"host":"web01" }. Tag keys and tag values that are not of the STRING data type are explicitly converted to the STRING type. |

**Important**

The system determines that the value of an untyped parameter is true if the parameter is specified. For example, the system determines that the value of the summary parameter is true regardless of whether you set the parameter to true or false. If you specify both the details parameter and the summary parameter, the API operation returns the details.

**Request content**

Specify a data point in the JSON format. The following table describes the parameters for a data point. Timestamp units: This section describes the rules for determining the unit of a timestamp. These rules apply to the following API operations: /api/put and api/query. /api/put and is used to write data, and /api/query is used to query data. Timestamps can be measured in seconds or milliseconds. LindormTSDB determines the unit of a timestamp based on the numeric value of the timestamp. The following content describes the rules: If a timestamp is in the range of [4294768,9999999999], LindormTSDB determines that the timestamp is in seconds. In this case, the corresponding date and time range is [1970-02-20 00:59:28,2286-11-21

| Instance type | Maximum number of tag keys supported by a single time series |
|---|---|
| mLarge | 16 |
| Large | 16 |
| 3xLarge | 20 |
| 4xLarge | 20 |
| 6xLarge | 20 |
| 12xLarge | 20 |
| 24xLarge | 24 |
| 48xLarge | 24 |
| 96xLarge | 24 |

01:46:39]. If the value falls within the range of [10000000000,9999999999999], LindormTSDB determines that the timestamp is in milliseconds. In this case, the corresponding date and time range is [1970-04-27 01:46:40.000, 2286-11-21 01:46:39.999]. If the timestamp is in the range of (-∞,4294768) or (9999999999999,+∞), LindormTSDB determines that the timestamp is invalid. Values in data points: The values in two data points can be of different data types only if the metric parameter has different values in the data points. For example, the following two data writing requests are allowed because the metric parameter has different values in the data points.

```
1.  [{"metric":"fakemetric1", "tags":{"tagk":"tagv1"},"timestamp":1514736000, "value":"val"}, {"met
ric":"fakemetric1", "tags":{"tagk":"tagv1"},"timestamp":1514736030, "value":"val2"}]
2.  [{"metric":"fakemetric2", "tags":{"tagk":"tagv2"},"timestamp":1514736000, "value":12.34}, {"met
ric":"fakemetric2", "tags":{"tagk":"tagv2"},"timestamp":1514736030, "value":34.56}]
```

Values of the STRING data type can contain all characters and can be stored in the JSON format. The size of a string value cannot exceed 20 KB. Tags: When you write data to a time series, you can specify only a limited number of tag keys. The maximum number of tag keys varies based on the instance type of the LindormTSDB instance, as listed in the following table.

**Example: Write data**

Request: `POST /api/put` Request body:

| Attribute | Data type | Description |
|---|---|---|
| success | Integer | The number of data points that have been written. |
| failed | Integer | The number of data points that failed to be written. |
| N/A | Array | An array that lists the data points that failed to be written and the causes of failures. This parameter is valid only if the details parameter is specified. |

```
1. [
2.    {
3.        "metric": "sys.cpu.nice",
4.        "timestamp": 1346846400,
5.        "value": 18,
6.        "tags": {
7.           "host": "web01",
8.           "dc": "lga"
9.        }
10.    },
11.    {
12.        "metric": "sys.cpu.nice",
13.        "timestamp": 1346846400,
14.        "value": 9,
15.        "tags": {
16.           "host": "web02",
17.           "dc": "lga"
18.        }
19.    },
20.    {
21.        "metric": "sys.cpu.alter",
22.        "timestamp": 1346846400,
23.        "value": "High CPU Load",
24.        "tags": {
25.           "host": "web03",
26.           "dc": "lga"
27.        }
28.    },
29.    {
30.        "metric": "sys.cpu.nice",
31.        "timestamp": 1346846400,
32.        "value": true,
33.        "tags": {
34.           "host": "web04",
35.           "dc": "lga"
36.        }
37.    }
38. ]
```

If all data points are written, the status code 204 is returned. If some data points fail to be written, the status code 400 is returned, and the response contains the error details. If you specify the summary or details parameter in the request, the response includes the following attributes. Sample response if the summary parameter is specified: Request: POST /api/put?summary Request body:

```
1. [
2.    {
3.        "metric": "sys.cpu.nice",
4.        "timestamp": 1346846400,
5.        "value": 9,
6.        "tags": {
7.           "host": "web02",
8.           "dc": "lga"
9.        }
10.  }
11. ]
```

Response:

```
1.   {
2.        "failed": 1,
3.        "success": 0
4.    }
```

The response indicates that no data points were written and one data point failed to be written.

**Sample response if the details parameter is specified:**

Request: POST /api/put?details Request body:

```
1.    [
2.        {
3.                      "metric": "sys.cpu.nice",
4.                      "timestamp": 1365465600,
5.                      "value": "NaN",
6.                      "tags": {
7.                          "host": "web01"
8.                      }
9.        }
10.    ]
```

Response:

```
1.    {
2.        "errors": [
3.            {
5.                    "metric": "sys.cpu.nice",
6.                    "timestamp": 1365465600,
7.                    "value": "NaN",
8.                    "tags": {
9.                        "host": "web01"
10.                    }
11.                },
12.                "error": "Unable to parse value to a number"
13.            }
14.        ],
15.        "failed": 1,
16.        "success": 0
17.    }
```

The response indicates that no data points were written and one data point failed to be written. The datapoint parameter indicates the data points that failed to be written. The error parameter indicates the cause of failure.

##### Sample code

Download the following two dependencies: HTTP Client and FastJSON.

```
1.  <!-- https://mvnrepository.com/artifact/org.apache.httpcomponents/httpclient -->
2.  <dependency>
3.    <groupId>org.apache.httpcomponents</groupId>
4.    <artifactId>httpclient</artifactId>
5.    <version>4.5.2</version>
6.  </dependency>
7.  <!-- https://mvnrepository.com/artifact/com.alibaba/fastjson -->
8.  <dependency>
9.    <groupId>com.alibaba</groupId>
10.   <artifactId>fastjson</artifactId>
11.   <version>1.2.34</version>
12. </dependency>
1.  package org.hitsdb.client;
```

2. `

```
3.  import java.io.IOException;
4.  import java.util.ArrayList;
5.  import java.util.HashMap;
6.  import java.util.List;
7.  import java.util.Map;
```

`8.`

```
9.  import org.apache.http.HttpResponse;
10. import org.apache.http.client.ClientProtocolException;
11. import org.apache.http.client.methods.HttpPost;
12. import org.apache.http.entity.StringEntity;
13. import org.apache.http.impl.client.CloseableHttpClient;
14. import org.apache.http.impl.client.HttpClients;
15. import org.junit.Test;
16.
17. import com.alibaba.fastjson.JSON;
18.
19. public class HttpWrite {
20.  private final static String HITSDB_IP = "192.168.11.17"; // The IP address of the instance.
21.  private final static int HITSDB_PORT = 8242; // The port of the instance.
22.  private final static int SYNC_TIMEOUT_MS = 60 * 1000;
23.  private Long startTime = System.currentTimeMillis();
24.
25.  static String putUrl = "http://" + HITSDB_IP + ":" + HITSDB_PORT +
26.             "/api/put?sync_timeout=" + SYNC_TIMEOUT_MS;
27.  static String queryUrl = "http://" + HITSDB_IP + ":" + HITSDB_PORT +
28.            "/api/query";
29. 30.
32.    public String metric;
33.    public Long timestamp;
34.    public Double value;
35.    public Map<String, String> tags;
36.  }
```

```
37.
38.  String buildData() {
39.    // Build an entity of the data to write.
40.    List<DataPoint> dataPoints = new ArrayList<DataPoint>();
41.    for (int i = 0; i < 3600; ++i) {
42.      DataPoint dataPoint = new DataPoint();
43.      dataPoint.metric = "sys.cpu";
44.      dataPoint.timestamp = startTime + i * 1000;
45.      dataPoint.value = 32.4;
46.      dataPoint.tags = new HashMap<String, String>();
47.      dataPoint.tags.put("host", "host1");
48.      dataPoint.tags.put("appName", "test1");
49.      dataPoints.add(dataPoint);
50.    }
51.    return JSON.toJSONString(dataPoints);
52.  }
53.
54.  @Test
55.  public void putDemo() throws ClientProtocolException, IOException {
56.    CloseableHttpClient httpClient = HttpClients.createDefault();
57.    HttpPost httpPost = new HttpPost(putUrl);
58.    StringEntity eStringEntity = new StringEntity(buildData(), "utf-8");
59.    eStringEntity.setContentType("application/json");
60.    httpPost.setEntity(eStringEntity);
61.    HttpResponse response = httpClient.execute(httpPost);
62.    int statusCode = response.getStatusLine().getStatusCode();
63.    if (statusCode == 200 || statusCode == 204) {
64.      System.out.println("write OK");
65.    }
66.    httpClient.close();
67.  }
68. }
```

#### Write data points to a multi-value model time

**series**

The multi-value data model is created based on data sources. Each data entry is created for a specific data source at a specific point in time and contains the values of multiple metric fields. For example, a data entry can contain the values of the following fields of a server: CPU, memory, and load. This allows you to manage multiple fields at the same time.

| Request method | Description |
|---|---|
| POST | Writes multiple data points at the same time. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| summary | Untyped | No | Specifies whether to return the summary. | false | /api/put? summary |
| details | Untyped | No | Specifies whether to return the details. | false | /api/put? details |
| sync timeout _ | Integer | No | The timeout period. Unit: milliseconds. A value of 0 specifies that the request never times out. | 0 | /api/put/? sync&sync ti _ meout=6000 0 |

#### Write data points to a multi-value model time series

**Request path and method**

**Important**

The request path that you use to insert a single-value data point is different from that you use to insert a multi-value data point. To write a single-value data point, call the /api/put operation. To query multi-value data points, call the /api/mquery operation. To write single-value data points, call the /api/query operation.

**Request parameters**

**Important**

The system determines that the value of an untyped parameter is true if the parameter is specified. For example, the system determines that the value of the summary parameter is true regardless of whether you set the parameter to true or false. If you specify both the details parameter and the summary parameter, the API operation returns the details.

**Request content**

| Parameter | Type | Required | Limit | Description | Example |
|---|---|---|---|---|---|
| metric | String | Yes | It can contain uppercase letters, lowercase letters, digits, and the following special characters: - . / ( ) : , _ [ ] = ' # | The name of the metric to be stored. | sys.cpu Importa nt The metric name must be 1 to 255 bytes in length. |
| timestamp | Long | Yes | None | The timestamp. Unit: seconds or milliseconds. For more information about how LindormTSDB determines the unit of a timestamp, see the "Timestamp units" section of this topic. | 1499158925 |
| fields | Map | Yes | The limits on field names are the same as those on metric names. The data type of a field value must be STRING, NUMBER, or BOOLEAN. | The values of the fields. | "fields" : {"speed" : 20.8, "level" : 4, "direction" : "East", "description" : "Fresh breeze"} |
| tags | Map | Yes | It can contain uppercase letters, lowercase letters, digits, and the following special characters: - . / ( ) : , _ [ ] = ' # | The tag key- value pairs. Tag keys and tag values are character strings. Specify at least one tag key-value pair. | {"host":"web 01"}. Tag keys and tag values that are not of the STRING data type are explicitly converted to the STRING type. |

Specify a data point in the JSON format. The following table describes the parameters for a data point.

**Timestamp units**

This section describes the rules for determining the unit of a timestamp. These rules apply to the following API operations: `/api/put` , `/api/mput` , `/api/query` , and `/api/mquery` . /api/put and /api/mput are used to write data. /api/query and /api/mquery are used to query data. Timestamps can be measured in seconds or milliseconds. LindormTSDB determines the unit of a timestamp based on the numeric value of the timestamp. The following rules apply: If a timestamp is in the range of [4284768,9999999999], LindormTSDB determines that the timestamp is in seconds. In this case, the corresponding date and time range is [1970-02-20 00:59:28,2286-11-21 01:46:39]. If the timestamp is in the range of [10000000000,9999999999999], LindormTSDB determines that the timestamp is in milliseconds. In this case, the corresponding date and time range is [1970-04-27 01:46:40.000, 2286-11-21 01:46:39.999]. If the timestamp is in the range of (-∞,4284768) or (9999999999999,+∞), LindormTSDB determines that the timestamp is invalid.

**Field values**

You can write two data points that contain values of different data types only if the data points contain different metrics or different fields. For example, the following two data writing requests are allowed: The metric parameter has the same value in the two data points in each request. Both data points in each request contain the same tag. However, the data points in each request contain different fields. Therefore, you can write field values of different data types in these data points.

```json
[{"metric":"fakemetric", "tags":{"tagk":"tagv1"},"timestamp":1514736000, "values":{"field1":"val", "field2": 111.11}, {"metric":"fakemetric", "tags":{"tagk":"tagv1"},"timestamp":1514736030, "values" :{"field1":"val2", "field2": 222.22}}] [{"metric":"fakemetric", "tags":{"tagk":"tagv1"},"timestamp":1514736000, "values":{"field1":"aaa", "field2": 333.33}}, {"metric":"fakemetric", "tags":{"estamp", "1514736030":"tagv1"} "values":{"fiel d1":"bbb", "field2": 444.44}}}]
```

**Example: Write data**

**Request:** POST/api/mput

**Request body:**

[

```json
        {
            "metric" : "wind",
            "fields" : {
                "speed" : 20.8,
                "level" : 4,
                "direction" : "East",
                "description" : "Fresh breeze"
            },
            "tags" : {
                "sensor":"IOTE_8859_0001",
                "city":"hangzhou",
                "province":"zhejiang",
                "country":"china"
            },
            "timestamp" : 1346846400
        },
        {
            "metric" : "wind",
            "fields" : {
                "speed" : 40.2,
                "level" : 6,
                "direction" : "South",
                "description" : "Fresh breeze"
            },
            "tags" : {
                "sensor":"IOTE_8859_0002",
                "city":"hangzhou",
                "province":"zhejiang",
                "country":"china"
            },
            "timestamp" : 1346846401
        }
```

]

#### Query data points from a multi-value model

**time series**

| Request path | Request method | Description |
|---|---|---|
| /api/query/mlast | POST | Queries the latest data point from a multi-value model time series. The returned data point contains the latest values of the specified fields of the specified metric. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| queries | Array | Yes | The subquery array. | None | For more information, see the "Parameters for subqueries in the JSON format" section of this topic. |

##### Query the latest data points from a multi-value

**time series**

**Request path and method**

**Request content**

| timestamp | Long | No | The UNIX timestamp. Unit: seconds or milliseconds. If you specify a timestamp, the subquery queries the latest data point that is imported to the database before the specified timestamp. If you do not specify a timestamp, the subquery queries the latest data point that is imported before the current time. This parameter is at the same level as the queries parameter in the request. For more information, see the following sample request. | None | 1539763573 |
|---|---|---|---|---|---|
| tupleFormat | Boolean | No | Specifies whether to return the tuple structure of the latest data point of the queried fields. For more information, see the following sample request and response. | false | false |
| tupleOffset | Long | No | The offset of the tuples. This parameter only takes effect when the tupleFormat parameter is set to true. | 0 | 5 |

| tupleLimit | Long | No | The maximum number of tuples. This parameter only takes effect when the tupleFormat parameter is set to true. | 0 | 100 |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| metric | String | Yes | The metric associated with the latest data points that you want to query. | None | wind |
| fields | List | Yes | The metric fields that you want to query. If you set this parameter to an asterisk (*), the values of all the fields in the specified metric are returned. | None | {speed, level, description} |
| tags | String | No | The tags associated with the latest data points that you want to query. | None | sensor = IOTE 1988 000 _ _ 1 |

**Important**

You can use /api/query/mlast to query only the latest data point from a multi-value model time series. If you want to query the latest data point from a single-value model time series, use /api/query/last.

**Subqueries in the JSON format**

**Sample request in the JSON format**

**Objective:** Query the latest data point from a multi-value model time series. The returned data point
contains the values of the usage_system and usage_idle fields in the cpu metric. The time series is defined by the cpu metric and the "host_name":"host1" tag.

**Request body:**

| Parameter | Description |
|---|---|
| metric | The metric. |
| columns | The names of the columns in the returned result set. The value of this parameter contains the timestamp field name and the names of the metric fields that you want to query. |
| tags | The set of tag key-value pairs associated with the data points. |
| values | The values of the metric fields. The order of the values is the same as the order of the columns. |

```json
    {
        "tupleFormat": true,
        "tupleOffset":5,
        "tupleLimit":100,
        "timestamp" : 1551851846,
        "queries": [
            {
                "metric": "cpu",
                "fields": ["usage_system", "usage_idle"],
                "tags": {
                    "host_name": "host1"
                }
            }
```

]

```
    }
```

If the HTTP status code 200 is returned, the query is successful. In this case, the latest data points in the time series that meet the specified query conditions are returned in the JSON format. If no time series meets the query conditions, an empty set is returned. The following table describes the response parameters.

**Important**

If you set the tupleFormat parameter to false in the request, the format of the response is the same as that of the response format for single-value metrics.

| Request path | Request method | Description |
|---|---|---|
| /api/mquery | POST | Queries data points from a multi- value time series. |

| Paramet er | Type | Required | Descripti on | Default value | Example |
|---|---|---|---|---|---|

[

```json
  {
    "metric": "wind",
    "columns": [
      "timestamp",
      "level",
      "speed"
```

`],`

```json
    "tags": {
      "city": "hangzhou",
      "country": "china",
      "province": "zhejiang",
      "sensor": "IOTE_8859_0001"
    },
    "values": [
      [1346846405000, 5.1, 45.1]
```

]

```
  }
```

]

##### Query data points from a multi-value time series

This topic describes how to call HTTP API operations to query data points from a multi-value time series.

**Request path and method**

**Important**

The request path that you use to insert a multi-value data point is different from that you use to insert a multi-value data point. To write single-value data points, call the /api/put operation. To query multivalue data points, call the /api/mquery operation. To write single-value data points, call the /api/query operation.

**Request content**

| start | Long | Yes | The beginning of the time range to query. Unit: seconds or millisecon ds. For more informatio n about how to determine the unit of a timestam p, see the "Timesta mp units" section of this topic. | None | 1499158925 |
|---|---|---|---|---|---|
| end | Long | No | The end of the time range to query. Unit: seconds or millisecon ds. For more informatio n about how to determine the unit of a timestam p, see the "Timesta mp units" section of this topic. By default, the current system time of the LindormT SDB server is used. | The current time. | 1499162916 |
| queries | Array | Yes | The array of subquerie s. | None | For more information, see the "Subqueries in the JSON format" section of this topic. |

| msResolut ion | boolean | No | The array of subquerie s. | false | This parameter takes effect only if the timestamps of the data points that you query are measured in seconds. If you set the value to true, TSDB returns the timestamps in milliseconds. If the original timestamps are measured in milliseconds, TSDB returns the original timestamps. |
|---|---|---|---|---|---|

| Paramete r | Type | Required | Description | Default value |
|---|---|---|---|---|
| metric | String | Yes | The metric name, such as wind . | None |
| fields | List | Yes | The fields to return. | None |
| limit | Integer | No | The maximum number of data points to return on each page for a subquery. The query results are paginated. Example: 1000. | 0 |
| offset | Integer | No | The number of the returned data points that you want to skip for a subquery. The query results are paginated. Example: 500. | 0 |
| tags | Map | No | The tags of the data points to return. This parameter conflicts with the filters parameter. | None |

**Timestamp units**

Timestamps can be measured in seconds or milliseconds. LindormTSDB determines the unit of a timestamp based on the numeric value of the timestamp. The following rules apply: If a timestamp is in the range of [4284768,9999999999], LindormTSDB determines that the timestamp is in seconds. In this case, the corresponding date and time range is [1970-02-20 00:59:28,2286-11-21 01:46:39]. If the timestamp is in the range of [10000000000,9999999999999], LindormTSDB determines that the timestamp is in milliseconds. In this case, the corresponding date and time range is [1970-04-27 01:46:40.000, 2286-11-21 01:46:39.999]. If the timestamp is in the range of (-∞,4284768) or (9999999999999,+∞), LindormTSDB determines that the timestamp is invalid.

**Note**

This section describes the rules for determining the unit of a timestamp. These rules apply to the following API operations: `/api/put` , `/api/mput` , `/api/query` , and `/api/mquery` . /api/put and /api/mput are used to write data. /api/query and /api/mquery are used to query data. LindormTSDB allows you to query data points at a single point in time. To query data points at a single point in time, set the start time and the end time to the same value. For example, you can set the `start` and `end` parameters to 1356998400.

**Subqueries in the JSON format**

| filters | List | No | The filtering condition. This parameter conflicts with the tags parameter. | None |
|---|---|---|---|---|

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| aggregator | String | Yes | The aggregate function. For more information, see the "Parameter: aggregator" section of this topic. | None | sum |
| field | String | Yes | The name of the field. You can use an asterisk (*) to query all fields of the metric. | None | None |
| alias | String | No | The alias of the field to return. | None | None |
| downsample | String | No | Downsamples data points to cover a wider time span. | None | 60m-avg |
| rate | Boolean | No | Specifies whether to calculate the growth rate between the values of a specified metric. The growth rate is calculated based on the following formula: Growth rate = (Vt - Vt- 1)/(t1 - t-1). | false | true |

**Note**

You can specify a maximum of 200 fields in each query. Example: In this example, three subqueries are specified in a query. Three fields are specified in the first query. Two fields are specified in the second subquery. Six fields are specified in the third subquery. Therefore, the total number of fields in the query equals 11. Before you run the query, make sure that the total number of fields in the query does not exceed 200. If you specify the tags and filters parameters in a query, the parameter that you specify in the latter position takes effect.

**Parameters for field queries in the JSON format**

| dpValue | String | No | The filtering conditions based on which the data points are filtered to return. The following operators are supported: >, <, =, <=, >=, and !=. | None | >=1000 |
|---|---|---|---|---|---|

**Request body:**

```json
{
    "start" : 1346846400,
    "end" :   1346846411,
    "msResolution" : true,
    "queries" : [
        {
            "metric" : "wind",
            "fields" : [
                {
                    "field" : "speed",
                    "aggregator" : "sum",
                    "downsample" : "2s-last",
                      "alias" : "speed_sum"
                },
                {
                    "field" : "*",
                    "aggregator" : "sum",
                    "downsample" : "2s-count"
                }
```

]

```
        }
```

]

```
}
```

**Use the Limit and Offset parameters for paged queries**

**limit**: specifies the maximum number of data points that are returned on each page for a subquery. The
default value is 0, which specifies that the number of data points to return is unlimited.
**offset**: the offset from which LindormTSDB starts to return the data points for a subquery. The default
value is 0, which specifies that the returned data points are not skipped.

**Important**

You cannot set the Limit or Offset parameter to a negative value. The Limit and Offset parameters take effect on the multi-value data points to return for a paged query. You cannot use the two parameters for a single-field query. If you want to obtain the data points whose rankings are 1001 to 1500, set the limit parameter to 500 and the offset parameter to 1000.

```json
{
    "start" : 1346846400,
    "end" :   1346846411,
    "msResolution" : true,
    "queries" : [
        {
            "metric" : "wind",
            "fields" : [
                {
                    "field" : "*",
                    "aggregator" : "sum",
                    "downsample" : "2s-count"
                }
```

`],`

```json
            "filters" : [
                {
                    "filter" : "IOTE_8859_0005|IOTE_8859_0004",
                    "tagk" : "sensor",
                    "type" : "literal_or"
                }
```

`],`

```json
            "limit" : 500,
            "offset" : 1000
        }
```

]

```
}
```

**Parameter: dpValue**

The dpValue parameter specifies the limit on field values. You can use this parameter to filter the data points to return. Valid operators: >, <, =, <=, >=, and ! =.

**Important**

The dpValue relationship between different fields is OR. The AND relationship is not supported.

| Operator | Description |
|---|---|
| avg | Returns the average value. |
| count | Returns the number of data points. |
| first | Returns the first value. |

```json
{
    "start" : 1346846400,
    "end" :   1346846411,
    "msResolution" : true,
    "queries" : [
        {
            "metric" : "wind",
            "fields" : [
                {
                    "field" : "level",
                    "aggregator" : "avg",
                    "downsample" : "2s-avg",
                    "dpValue" : ">=8.0"
                }
```

`],`

```json
            "filters" : [
                {
                    "filter" : "IOTE_8859_0005|IOTE_8859_0004",
                    "tagk" : "sensor",
                    "type" : "literal_or"
                }
```

]

```
        }
```

]

```
}
```

**Parameter: downsample**

If you query data over a long period of time, you can downsample the data to retrieve the query results in reduced precision. The following sample code provides an example on the format of a query:

```xml
<interval><units>-<aggregator>[-fill policy]
```

Take note of the following items:
**interval**: the interval time across which LindormTSDB aggregates the data points. For example, you can
set interval to 5 or 60. The 0all value specifies that LindormTSDB aggregates all the data points in a time series into a data point.
**units**: the unit of the interval time. Valid values: s, m, h, d, n, and y. s specifies seconds, m specifies
minutes, h specifies hours, d specifies days, n specifies months, and y specifies years.

**Note**

You can downsample data based on a calendar time interval. To use the calendar time interval, append c to the **units** value. For example, `1dc` specifies the 24-hour period from 00:00 of the current day to 00:00 of the next day.
**aggregator**: the operator for downsampling. The following table describes the operators.

| last | Returns the last value. |
|---|---|
| min | Returns the minimum value. |
| max | Returns the maximum value. |
| sum | Returns the sum of values. |
| zimsum | Returns the sum of values. |
| rfirst | The same as the first operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rlast | The same as the last operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rmin | The same as the min operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |
| rmax | The same as the max operator. However, this operator returns the data point at the original timestamp instead of the aligned timestamp. The timestamps of data points are aligned after data is downsampled. |

| Fill Policy | Fill value |
|---|---|
| none | The default behavior that does not interpolate values. |
| nan | NaN |
| null | null |
| zero | 0 |

**Note**

If you use rfirst, rlast, rmin, or rmax for downsampling, you cannot specify a fill policy.

**Fill policy**

A fill policy emits a pre-defined value when a data point at a specified timestamp is missing. When you downsample data, all time series are segmented at a specified interval and the data points at each interval are aggregated. If a data point is missing at a specified timestamp, you can specify a fill policy to emit a pre-defined value. For example, after you downsample data in a time series, the aligned timestamps are t+0, t+20, and t+30. In this scenario, if you do not specify a fill policy, a data point is missing at the t+10 timestamp. If you specify a fill policy that emits null, Lindorm TSDB emits null at the t+10 timestamp. The following table describes the fill policies and the values to be filled.

| linear | Performs linear interpolation. |
|---|---|
| previous | Interpolates the previous value. |
| near | Interpolates the adjacent value. |
| after | Interpolates the next value. |
| fixed | Interpolates a user-specified fixed value. For more information, see the "Fill policy (fixed value)" section of this topic. |

**Fixed Fill Policy**

To emit a pre-defined value, append the pre-defined value to the number sign (#). You can specify the fixed value as a positive or negative number. and must be in the following format:

```xml
<interval><units>-<aggregator>-fixed#<number>
```

**Examples**: 1h-sum-fixed#6 and 1h-avg-fixed#-8
Examples: 1m-avg, 1h-sum-zero, and 1h-sum-near

**Important**

The downsample parameter is optional for field queries. You can set this parameter to null or leave this parameter empty: {"downsample": null} or {"downsample": ""}. In this case, data points are not downsampled. If you specify the downsample parameter in a field query, specify this parameter in the other field queries that belong to the same subquery. You must specify the same interval time to downsample field data in all the field queries that belong to the same subquery.

**Parameter: aggregator**

After data is downsampled, values along multiple time series are obtained and the timestamps of these time series are aligned. You can merge these time series into one time series by aggregating the values at each aligned timestamp. Aggregation is not performed if only one time series exists. During aggregation, each time series must have a value at each aligned timestamp. If no value can be found at an aligned timestamp, interpolation is performed. For more information, see the following "Interpolation" section.

**Important**

In field queries, the aggregator parameter is required. You can set this parameter to none. This specifies that data is not aggregated. If you specify the aggregator parameter in a field query, you must also specify this parameter in other field queries that belong to the same subquery. Lindorm TSDB does not allow you to aggregate only part of field data in a subquery.

**Interpolation**

If a time series has no value at a timestamp, a value is interpolated to this time series at the timestamp. This occurs only if you do not specify a fill policy for the time series, and one of the other time series to be aggregated has a value at this timestamp. For example, you want to merge two time series by using the sum operator. The downsampling and aggregation settings are {"downsample": "10s-avg", "aggregator": "sum"}. After you perform downsampling, the timestamps in which values can be found are provided in the following part: In Time Series 1, values can be found at the timestamps t+0, t+10, t+20, and t+30. In timeline 2, values can be found at the timestamps t+0, t+20, and t+30.

| Operator | Description | Interpolation method |
|---|---|---|
| avg | Returns the average value. | Performs linear interpolation based on linear slopes. |
| count | Returns the number of data points. | Interpolates the value 0. |
| mimmin | Returns the minimum value. | The maximum value is interpolated. |
| mimmax | Returns the maximum value. | The minimum value is interpolated. |
| min | Returns the minimum value. | Performs linear interpolation. |
| max | Returns the maximum value. | Performs linear interpolation. |
| none | Skips data aggregation. | Interpolates the value 0. |
| sum | Returns the sum of values. | Performs linear interpolation. |
| zimsum | Returns the sum of values. | Interpolates the value 0. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| type | String | Yes | The filter type. For more information, see the "Filter types" section of this topic. | None | literal or _ |
| tagk | String | Yes | The name of the tag key. | None | host |
| filter | String | Yes | The filter expression. | None | web01\|web02 |

In Time Series 2, the value at the t+10 timestamp is missing. Then, before the aggregation is performed, a value is interpolated for time series 2 at the t+10 timestamp. The interpolation method varies based on aggregation operators. The following table describes the operators and interpolation methods.

**Parameter: filters**

You can use the following methods to configure the filters parameter: Use tagk to specify filters.
**tagk = ***: performs a GROUP BY operation on all the tag values that are paired with a specified tag
key and then aggregates the same tag values.
**tagk = tagv1|tagv2**: aggregates data points that have the specified tag values that are paired with
a tag key. Use the JSON format.

| groupBy | Boolean | No | Specifies whether to perform a GROUP BY operation on the tag values. | false | false |
|---|---|---|---|---|---|

| Parameter | Example | Description |
|---|---|---|
| literal or _ | web01\|web02 | Aggregation is separately performed on multiple case- sensitive tag values. |
| wildcard | *mysite.com | Aggregation is separately performed on the tag values that contain the specified wildcard. These tag values are case-sensitive. |

**Filter types**

Use filters to query data. **Request body**:

```json
{
    "start" : 1346846400,
    "end" :   1346846411,
    "msResolution" : true,
    "queries" : [
        {
            "metric" : "wind",
            "fields" : [
                {
                    "field" : "speed",
                    "aggregator" : "none",
                    "alias" : "column_speed"
                },
                {
                    "field" : "*",
                    "aggregator" : "none",
                    "alias" : "column_"
                }
```

`],`

```json
            "filters" : [
                {
                    "filter" : "IOTE_8859_0005|IOTE_8859_0004",
                    "tagk" : "sensor",
                    "type" : "literal_or"
                }
```

]

```
        }
```

]

```
}
```

If a query is successful, the HTTP 200 status code is returned and the response is returned in the JSON format. The following table describes the response parameters.

| Parameter | Description |
|---|---|
| metric | The metric. |
| columns | The names of the columns returned. |
| tags | The tags of which the tag values are not aggregated. |
| aggregateTags | The tags of which the tag values are aggregated. |
| values | The tuples returned. |

The following sample code shows the query result when the aggregator parameter is set to none. [

```json
   {
      "metric":"wind",
      "columns":[
         "timestamp",
         "column_speed",
         "column_description",
         "column_direction",
         "column_level",
         "column_speed"
```

`],`

```json
      "tags":{
         "city":"hangzhou",
         "country":"china",
         "province":"zhejiang",
         "sensor":"IOTE_8859_0005"
      },
      "aggregatedTags":[],
      "values":[
         [ 1346846406000, null, "Fresh breeze", "East", 0.5, null ],
         [ 1346846407000, null, "Fresh breeze", "South", 1.5, null ]
   },
   {
      "metric":"wind",
      "columns":[
         "timestamp",
         "column_speed",
         "column_description",
         "column_direction",
         "column_level",
         "column_speed"
```

`],`

```json
      "tags":{
         "city":"hangzhou",
         "country":"china",
         "province":"zhejiang",
         "sensor":"IOTE_8859_0004"
      },
      "aggregatedTags":[],
      "values":[
         [ 1346846400000, 40.4, "Fresh breeze", "East", 0.4, 40.4 ],
         [ 1346846401000, 41.4, "Fresh breeze", "South", 1.4, 41.4 ],
         [ 1346846402000, 42.4, "Fresh breeze", "West", 2.4, 42.4 ],
         [ 1346846403000, 43.4, "Fresh breeze", "North", 3.4,43.4 ]
   }
```

] The following sample code shows the query result when the aggregator parameter is set to avg. The result indicates the average wind speed and the average wind level based on the data from all sensors in the Hangzhou city.

| Request path | Request method | Description |
|---|---|---|
| /api/dump meta _ | POST | Queries tag values by tag key. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| tagkey | String | Yes | The tag key. | None | host |
| tagvalueprefix | String | Yes | The prefix of the tag values to query. | None | 127.0.0 |
| max | Integer | No | The maximum number of tag values to return. | 1000 | 2 |

[

```json
  {
    "metric": "wind",
    "columns": [
      "timestamp",
      "avg_level",
      "avg_speed"
```

`],`

```json
    "tags": {
      "city": "hangzhou"
    },
    "aggregatedTags": [
      "country",
      "province",
      "sensor"
```

`],`

```json
    "values": [
      [1346846400000, 0.25, 40.25],
      [1346846401000, 1.25, 41.25],
      [1346846402000, 2.5, 42.5],
      [1346846411000, 5.5, null]
```

]

```
  }
```

]

#### Query tag values by tag key

**Request path and method**

**Request content**

**Sample request in the JSON format**

**Objective**: Query tag key-value pairs that meet the specified conditions. In this example, two tag pairs of
which the tag values are prefixed with 127.0.0 are queried.
**Request**: `POST/api/dump_meta`

**Request body:**

| Request path | Request method | Description |
|---|---|---|
| /api/suggest | POST | Queries metrics, fields, tag keys, and tag values. |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| type | String | Yes | The type of the objects that you need to query, such as metrics, field, tag key, and tag value. | None | metrics |
| metric | String | No | The metric that you want to query. The field values, tag keys, and tag values that correspond to the specified metric are returned. If you set type to metrics, this parameter is ignored. | None | - |
| q | String | No | The prefix of the tag values to query. | None | my _ |
| max | Integer | No | The maximum number of the returned entries. | 25 | 4 |

```json
{
  "tagkey": "host",
  "tagvalueprefix": "127.0.0",
  "max": 2
}
```

The tag key-value pairs that meet the specified conditions are returned. Sample response:

```
[ {"host": "127.0.0.1"}, {"host": "127.0.0.2"} ]
```

#### Query metrics, fields, tag keys, and tag

**values**

**Request path and method**

**Request content**

**Sample request in the JSON format**

| Request path | Request method | Description |
|---|---|---|
| /api/ttl | POST | Configure a time-to-live (TTL) for data. |

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| val | Integer | Yes | The value of the TTL. Unit: seconds. The value range is [1,2147483647]. You can use Integer.MAX VALUE to _ specify the maximum value 2147483647. If you use a Lindorm instance of High-availability Edition, the value range is [3600,2147483647]. If you set the TTL to a value smaller than 3600, an error is thrown. If you set the TTL to 2147483647 or a greater value, the system determines that no TTL is configured. If you set the TTL to a value greater than 2147483647, the system determines that the TTL is 2147483647. | 7776000 |

```json
    {
      "type": "metrics",
      "q": "my_",
      "max": 4
    }
```

**Objective**: Query four field names prefixed by the letter d based on the wind metric.
**Request**: `POST /api/suggest`

**Request body:**

```json
    {
      "type": "field",
      "metric": "wind",
      "q": "d",
      "max": 4
    }
```

A string array is returned.

```json
    The following result is returned for the first sample request:
    [ "my_metric1", "my_metric2", "my_metric3", "my_metric4" ]
    The following result is returned for the second sample request. Only the two entries that meet
the requirements are returned.
    [ "description", "direction" ]
```

#### Configure a data TTL

**Request path and method**

**Request content**

| Request path | Request method | Description |
|---|---|---|
| /api/ttl | GET | Queries the TTL. |

| Request path | Request method | Description |
|---|---|---|
| /api/delete data _ | POST | Deletes data from a time series |

| Parameter | Type | Required | Description | Default value | Example |
|---|---|---|---|---|---|
| metric | String | Yes | The metric for the time series that you want to delete. | None | cpu |

**Sample request in the JSON format**

**Request:** `POST/api/ttl`

**Request body:**

```json
{ "val": 7776000 }
```

The HTTP 200 status code indicates that the request is successful. Other status codes indicate request failures. For more information, see Response status codes.

**TTL rules**

1. The TTL is not calculated based on the timestamp of a data point. The TTL is calculated based on **the**
**time when the data point is written to the database**.
2. A data point does not become invalid immediately when the TTL of the data point ends. Instead, the
data point remains in the database for some time before the database backend cleans up the data point.
3. If a data point becomes invalid, the time series to which the data point belongs remains valid. If the time
series has not been used for a long time, we recommend that you call specific operations to clean up data.

**Request path and method**

**Request content**

No request required. The HTTP 200 status code indicates that the request is successful. Other status codes indicate request failures. For more information, see Response status codes. Sample response in the JSON format:

```json
{ "val": 7776000 }
```

The value of val is the TTL. The unit is seconds.

#### Delete data from a time series

**Request path and method**

**Request content**

| tags | Map | No | The tags of the time series that you want to delete. This parameter is optional. If no tag is specified, all the time series related to the specified metric are deleted. | None | See the sample requests. |
|---|---|---|---|---|---|
| fields | List | No | The field data for the metric that you want to delete. | None | usage system, _ usage guest _ |
| start | Integer | Yes | The beginning of the timestamp range to delete data. Unit: seconds. | None | 1499308591 |
| end | Integer | No | The end of the timestamp range to delete data. Unit: seconds. | The current time. | 1499508591 |

**Important**

If you leave the fields parameter empty, LindormTSDB deletes all the time series data for the metric. For example, LindormTSDB deletes all the single-value data or all the field data for the metric. If a time series contains the metric and tags that are specified in the request body, the time series is deleted, regardless of whether the time series contains other tags.

**Sample requests in the JSON format**

**Objective**: Delete all data of the cpu metric during the 1499308591 and 1499508591 time range.
**Request**: `POST/api/delete_data` . **Request body:**

```json
    {
        "metric": "cpu",
        "start": 1499308591,
        "end": 1499508591
    }
```

**Objective**: Delete all data of the cpu metric and that has the "host: 192.168.0.2", "appName: hitsdb" tags
during the 1499308591 and 1499508591 time range. **Request**: `POST/api/delete_data` . **Request body:**

```json
    {
        "metric": "cpu",
        "tags": {
            "host": "192.168.0.2",
            "appName": "hitsdb"
        },
        "start": 1499308591,
        "end": 1499508591
    }
```

| Request path | Request method | Description |
|---|---|---|
| /api/delete meta _ | POST | Deletes time series. |

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| metric | String | Yes | The metric of the time series that you want to delete. | cpu |
| fields | List | No | The metric fields of the time series that you want to delete. This parameter is optional. If no field is specified, all the single-value model time series and the multi-value model time series related to the specified metric are deleted. | usage system, _ usage guest _ |
| tags | Map | No | The tags of the time series that you want to delete. This parameter is optional. If no tag is specified, all the time series related to the specified metric are deleted. | See the sample requests. |
| deleteData | Boolean | No | Specifies whether to delete the data associated with the time series. If you set this parameter to true, the associated data is deleted. If you set this parameter to false, the associated data is not deleted. Take note that the system consumes resources and time to delete the data associated with the time series. It takes less time to delete only the time series. Default value: true. | false |

**Objective**: Delete all data of the usage_system and usage_guest fields of the cpu metric during the
1499308591 and 1499508591 time range. **Request**: `POST/api/delete_data` . **Request body:**

```json
    {
        "metric": "cpu",
        "fields": ["usage_system", "usage_guest"],
        "start": 1499308591,
        "end": 1499508591
    }
```

The HTTP 200 status code indicates that the request is successful. Other status codes indicate request failures. For more information, see Response status codes.

#### Delete time series

**Request path and method**

**Request content**

| recursive | Boolean | No | Specifies whether to exactly match the specified tag keys and tag values. true: If the tag of the target timeline contains the specified tagKV, the tag is deleted. false: If the tag of the target timeline contains the specified tagKV, the tag is deleted. Default value: true. For example, a database has two time series: Time Series 1 and Time Series 2. Time Series 1 has two tags that are "TagK1":"TagV1" and "TagK2":"TagV2". Time Series 2 has one tag that is "Tagk1":"TagV1". Assume that you set the tags parameter to "TagK1":"TagV1" in the request. If you set the recursive parameter to true, both Time Series 1 and Time Series 2 are deleted. If you set the recursive parameter to false, only Time Series 2 is deleted. | false |
|---|---|---|---|---|

**Sample requests in the JSON format**

**Objective**: Delete all single-value and multi-value time series that are associated with all fields of the cpu
metric based on the "host: 192.168.0.2" and "appName: hitsdb" tags. **Request**: `POST/api/delete_meta` .

**Request body:**

```json
    {
        "metric": "cpu",
        "tags": {
            "host": "192.168.0.2",
            "appName": "hitsdb"
        }
    }
```

**Objective**: Delete all time series that are associated with the usage_system and usage_idle fields of the
cup metric and have the "host: 192.168.0.2" and "appName: hitsdb" tags. **Request**: `POST/api/delete_meta` . **Request body:**

```json
    {
        "metric": "cpu.usage",
        "fields": ["usage_system", "usage_idle"],
        "tags": {
            "host": "192.168.0.2",
            "appName": "hitsdb"
        }
    }
```

The HTTP 200 status code indicates that the request is successful. Other status codes indicate request failures. For more information, see Response status codes.

#### Clear data

This topic describes how to clear data from LindormTSDB. You can use this operation to efficiently clear test data.

| Request path | Request method | Description |
|---|---|---|
| /api/truncate | POST | Clears up data. |

| Response code | Description |
|---|---|
| 200 | Indicates that the request is successful and the response parameters are returned. This code may be returned when you query data. |
| 204 | Indicates that the request is successful and no response parameters are returned. This code may be returned when you write data. |

| Response code | Description |
|---|---|
| 400 | Indicates that the request has failed because a request parameter or the requested content is invalid or incomplete. The response includes the details of the error. |
| 404 | Indicates that the request path is not found. |
| 405 | Indicates that the request method is not supported. |
| 406 | Indicates that the requested resources are not available. |
| 408 | Indicates that the request timed out. |
| 413 | Indicates that the size of the response is larger than the size of the server cache. |

**Important**

After you call this operation to clear data, all data in your LindormTSDB database is cleared can cannot be restored. Proceed with caution. Alibaba Cloud does not proactively clear your data. When you call /api/truncate to clear data from LindormTSDB, all nodes in the LindormTSDB cluster reject data writes. Proceed with caution.

**Request path and method**

Request content None Sample request Request: POST/api/truncate The HTTP 200 status code indicates that the request is successful. Other status codes indicate request failures. For more information, see the Common error codes topic. If this operation returns the HTTP 500 status code, check whether the error message includes the following content: "The attempt to broadcast locking truncate remotely against [ address 1,… ] failed,while the attempt against [ address 2,… ] succeeded". If yes, the truncate operation failure caused inconsistent states between the nodes in the LindormTSDB cluster. If you do not resolve the status inconsistency issue, you may fail to write data to LindormTSDB. If this error occurs, submit the error message to the Alibaba Cloud O&M team for technical support.

#### HTTP status codes

| 429 | Indicates that the resources required by the request are not sufficient because a large number of requests are sent to the server at a high frequency. |
|---|---|
| 500 | Indicates an internal server error. |
| 501 | Indicates that the requested feature is unavailable. |
| 503 | Indicates that the server does not have sufficient resources to process the request. |

| Feature | Scenario | References |
|---|---|---|
| Data migration between HBase and LindormTable | Seamless data migration between existing clusters and new clusters, cluster upgrades, online and offline workload decoupling, primary/secondary disaster recovery, and active geo- redundancy. | Synchronize full and incremental data |
| MaxCompute/Hive -> Lindorm | Offline query acceleration, and the transmission of details and metrics from data warehouses to Lindorm for online queries. | For more information, contact the technical support. |

## LTS

### Overview

Lindorm Tunnel Service (LTS) is a data ecosystem service that is customized based on the characteristics of business scenarios in which Lindorm is used. LTS provides easy-to-use capabilities, including data exchange, processing, and change tracking. You can use these capabilities to migrate data, track realtime data changes, dump data to data lakes, and synchronize data from data warehouses to Lindorm databases. You can also use these capabilities to back up and restore data, and implement multi-active redundancy based on units. This way, LTS provides an all-in-one data ecosystem service for Lindorm.

**Core capabilities**

**Cloud native distributed system**: LTS is a distributed system that is deployed based on Elastic
Compute Service (ECS). LTS features excellent horizontal scalability and allows you to configure resources based on your business requirements.
**Ease of use**: LTS allows you to configure data migration, import, change tracking, and archiving tasks
with a few clicks. For example, to create a data migration task, you need only to specify the source, destination, and columns that you want to synchronize. LTS automatically replicates schemas, full data, or incremental data based on your settings.
**High security and reliability**: LTS minimizes the impact on the source and destination systems and
minimizes the risks of potential failures due to incompatibility. Before a task is started, LTS prechecks the network connectivity and security. While the task is running, LTS monitors the synchronization latency and the storage usage of the destination cluster in real time. LTS also implements throttling and reports alerts based on the monitoring data. After the task is complete, LTS verifies data.
**Cost-effectiveness**: LTS is an optimized service based on open source systems, such as Apache
HBase. LTS allows you to process data at the physical file level. This is 10 times more efficient than traditional data replication. LTS also provides optimized CPU, cache, memory, and network I/O capabilities. This enables LTS to provide cost-effective tunnels and helps reduce your costs of data transfer and processing.

**Features**

| Subscription to real-time data in LogHub Important This feature is no longer available for LTS instances that are purchased on and after June 16, 2023. If your LTS instance is purchased before June 16, 2023, you can still use this feature as expected. | Subscription to real-time data from LogHub for consumption in Lindorm | Import incremental data from Simple Log Service |
|---|---|---|

**Log lifecycle management**

If log data is not consumed after you enable the log subscription feature, the log data is retained for 48 hours by default. After the period expires, the subscription is automatically canceled, and the retained data is automatically deleted. Log data may fail to be consumed if your LTS cluster is released while your task is still running or if your synchronization task is suspended. You can enable the log subscription feature for the following types of tasks in Lindorm: incremental synchronization, data archiving, data backup, and data subscription.

**Common scenarios**

Cluster migration Usage scope Data migration from HBase to Lindorm. Data center migration across regions. Workload decoupling. Characteristics Data can be migrated without service interruption. LTS can migrate historical data and synchronize real-time incremental data in one task. During the migration, LTS does not interact with the source HBase or Lindorm cluster. LTS reads data only from the Hadoop Distributed File System (HDFS) of the source cluster. This minimizes the impact on the online business that runs on the source cluster. In most cases, compared with data migration at the API layer, data replication at the file layer can help you reduce more than 50% of the data usage. LTS is efficient. Each node can migrate data at a rate of up to 100 MB/s. You can add nodes for horizontal scaling to migrate terabytes or even petabytes of data. LTS provides stable services by retrying failed tasks, monitoring the synchronization rates and progress of tasks in real time, and reporting alerts when tasks fail. LTS ensures data accuracy by verifying the synchronized data. Automatic schema synchronization is supported to ensure consistent partitions. Primary/secondary disaster recovery LTS supports two-way data synchronization between an active cluster and a standby cluster. When the active cluster fails, you can switch to the standby cluster to reduce the impact on your workloads. After the active cluster recovers, you can use LTS to synchronize the incremental data from the standby cluster to the active cluster.

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Organization | Select the organization to which the LTS instance belongs. |
|  | Resource Set | Select the resource set that is used to manage the LTS instance. |
|  | Instance name | Specify the name of the LTS instance. The name is used to identify and manage the instance. |
| Area | Geography | Select the region where the LTS instance resides. Note After you create the LTS instance, you cannot change the region where the instance resides. Proceed with caution. If your application is deployed on an Elastic Compute Service (ECS) instance, we recommend that you deploy the LTS instance in the region where the ECS instance resides. If the LTS instance and the ECS instance are deployed in different regions, your application cannot communicate with the LTS instance over an internal network. |
|  | Availability Zone | Select the zone to which the LTS instance belongs. Note If your application is deployed on an ECS instance, we recommend that you deploy the LTS instance in the zone where the ECS instance resides to reduce network latency. |
| Specification Configuration | Data Channel Service Specifications | Select the specification of nodes on the LTS instance. |
|  | Number of specification nodes | Specify the number of nodes on the LTS instance. Valid values: 1 to 20. |

### Purchase an LTS instance and log

**on to the LTS web UI**

Lindorm Tunnel Service (LTS) is a tunnel service developed by Alibaba Cloud for Lindorm. You can use LTS to import and export data, track data changes, and back up and restore data. This topic describes how to purchase an LTS instance and log on to the LTS web UI.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Database Services > Lindorm**.
3. On the **Instances** page, click **CreateLTS**.
4. On the Create LTS page, configure the parameters. The following table describes the parameters.
5. Click **Submit**.

| Type of HBase data source | Method to add an HBase data source |
|---|---|
| Self-managed HBase cluster | For more information, see the Use LTS to add an HBase data source section of this topic. |
| E-MapReduce (EMR) HBase cluster |  |

| Parameter | Description |
|---|---|
| Name | The name of the HBase data source. |
| Data Source Type | The type of the data source. Specify this parameter based on the version of the HBase data source. Valid values: HBase1x: specifies that the HBase data source is an HBase V1.0 cluster. HBase2x: specifies that the HBase data source is an ApsaraDB for HBase V2.0 cluster. HBase098: specifies that the HBase data source is a self-managed HBase V0.98 cluster. HBase094: specifies that the HBase data source is a self-managed HBase V0.94 cluster. |

**Important**

After you purchase an LTS instance, the status of the instance is **Creating** in the console. You can log on to the LTS web UI only after the instance status becomes **Running**.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-left corner of the page that appears, select the organization to which the instance belongs.
3. On the **Instances** page, find the instance that you want to manage and click the ID of the instance or
**View Instance Details** in the **Actions** column.
4. In the **LTS WebUI Access** section, click **ClusterManager** to go to the LTS web UI.

### Data source management

#### Add an HBase data source

After you add an HBase data source to a Lindorm Tunnel Service (LTS) instance, you can migrate or synchronize data from the source. This topic describes how to add an HBase data source to an LTS instance.

**Types of HBase data sources and methods to add a data source**

1. Activate LTS and log on to the LTS web UI. For more information, see the "Create an LTS instance" topic
of User Guide.
2. In the left-side navigation pane of the LTS web UI, choose **Data Source Manage > Add Data Source**.
3. On the **Add data source** page, configure the parameters. The following table describes the
parameters.

|  | The parameters that are used to connect to the HBase data source. { "clusterKey":"xxxzkhost1,xxxzkhost2,xxxzkhost3:2181:/xxxhbase", "hbaseDir":"/xxxhbase", "hdfsUri":"hdfs://xxxnn1:8020,xxxnn2:8020" } clusterKey: the connection information about the HBase data source. Specify this parameter in the following format: ZooKeeper node: ZooKeeper port: The path of the parent node that is used by the HBase data source in ZooKeeper . The path of the parent node that is used by the HBase data source is specified by the zookeeper.znode.parent option of the ApsaraDB for HBase cluster. hbaseDir: the Hadoop Distributed File System (HDFS) path that corresponds to the data of the HBase data source. This path is specified by the hbase.rootdir option of the ApsaraDB for HBase cluster. Note The value of this parameter is the lowest-level directory in which the HBase data source is located and does not include the hdfs://xx prefix. For example, if the HDFS path that corresponds to the data of the HBase data source is hdfs://hbase/hbase , you can set this parameter to /hbase . hdfsUri: the HDFS connection URL of the self-managed HBase cluster. If you use a high-availability HBase data source, specify this parameter in the hdfs://namenode1:port,namenode2:port format. If you use a single-node HBase data source, specify this parameter in the hdfs://namenode:port format. |  |  |
|---|---|---|---|
|  |  | ZooKeeper node: ZooKeeper port: The path of the parent node |  |
|  | that is used by the HBase data source in ZooKeeper |  |  |
| Parameters |  |  |  |
| Cluster/etc/ hosts (only EMR or OpenSourc e Cluster needed) | The /etc/hosts configuration file of the HBase cluster. The hostnames and IP addresses of the nodes in the HBase cluster are specified in this file. Note This parameter is required only if you add a self-managed HBase cluster or an EMR HBase cluster as the data source. |  |  |

| Parameter | Description |
|---|---|
| Name | The name of the data source. The name can contain letters and digits. |
| Data Source Type | The type of the data source. Select LQL. |

4. Click **Add**.

#### Add a LindormTable data source

This topic describes how to add a LindormTable data source to a Lindorm Tunnel Service (LTS) instance.

**Prerequisites**

You are logged on to the web UI of the LTS instance.

**Add a Lindorm SQL data source**

1. Log on to the LTS web UI. In the left-side navigation pane, choose **Data Source Manage** > **Add Data**
**Source**.
2. On the **Add data source** page, configure the parameters. The following table describes the
parameters.

|  |  | { "clusterKey":"x.hbaseue.rds.aliyuncs.com:30020:$username:$password" } x.hbaseue.rds.aliyuncs.com:30020 : the private endpoint that is used to connect to LindormTable by using the HBase API for Java. For more information about how to obtain the endpoint, see the View endpoints topic of User Guide. username : the username that is used to connect to LindormTable. password : the password that is used to connect to LindormTable. |  |  |
|---|---|---|---|---|
|  |  |  | { |  |
|  |  | "clusterKey":"x.hbaseue.rds.aliyuncs.com:30020:$username:$password" |  |  |
|  |  | } |  |  |
| Parameters |  |  |  | x.hbaseue.rds.aliyuncs.com:30020 |

| Parameter |  | Description |  |  |  |
|---|---|---|---|---|---|
| Name |  | The name of the data source. The name can contain letters and digits. |  |  |  |
| Data Source Type |  | The type of the data source. Select Lindorm for HBase(Enhanced Edition). |  |  |  |
|  |  | { |  |  |  |
|  |  |  | { |  |  |
|  |  | "clusterKey":"{x.hbaseue.rds.aliyuncs.com:30020}:{username}:{password}" |  |  |  |
|  |  | } |  |  |  |
| Parameters |  |  |  | x.hbaseue.rds.aliyuncs.com:30020 |  |
| Cluster/etc/hosts (Only EMR or OpenSource Cluster needed) |  | This parameter is required only if you want to add a self-managed HBase cluster or an E-MapReduce (EMR) HBase cluster as a data source. The host names and the IP addresses stored in the /etc/hosts files that correspond to your HBase cluster. |  |  |  |

3. Click **Add**.

**Add an HBase-compatible LindormTable data source**

1. Log on to the LTS web UI. In the left-side navigation pane, choose **Data Source Manage** > **Add Data**
**Source**.
2. On the **Add data source** page, configure the parameters. The following table describes the
parameters.
3. Click **Add**.

#### Add an ApsaraMQ for Kafka data source

This topic describes how to add an ApsaraMQ for Kafka data source to a Lindorm Tunnel Service (LTS) instance.

**Prerequisites**

You are logged on to the LTS web UI. For information, see Purchase an LTS instance and log on to the LTS web UI.

**Procedure**

1. Log on to the LTS web UI. In the left-side navigation pane, choose **Data Source Manage** > **Add Data**
**Source**.

| Parameter | Description |
|---|---|
| Name | The name of the data source. The name can contain letters and digits. |
| Data Source Type | The type of the data source. Select KAFKA. |
| Parameters | {bootstrap.servers:"server1:port1,server2:port2"} bootstrap.servers : the endpoint of the source ApsaraMQ for Kafka instance. You must use the default endpoint that is displayed on the details page of the ApsaraMQ for Kafka instance. The source ApsaraMQ for Kafka instance must be deployed in the same virtual private cloud (VPC) as the destination Lindorm instance. server1:port1 : the server port. The value is in the Endpoint:Port number format. |

|  |  | server1:port1 |
|---|---|---|
|  | number |  |

| Endpoint:Port |  |
|---|---|

2. On the **Add data source** page, configure the parameters. The following table describes the
parameters.
3. Click **Add**.

#### Add an HDFS data source

After you add a Hadoop Distributed File System (HDFS) data source to Lindorm, you can use LindormTable to access data in HDFS. If you want to migrate data in HDFS to a wide table in Lindorm, add an HDFS data source. This topic describes how to add an HDFS data source to a Lindorm Tunnel Service (TLS) instance.

**Prerequisites**

An LTS instance is purchased. For more information, see Purchase an LTS instance and log on to the LTS web UI. The IP address of the client is added to the IP address whitelist.

**Procedure**

1. Log on to the LTS web UI.
2. In the left-side navigation pane, choose **Data Source Management > Add Data Source**.
3. On the **Add data source** page, configure the following parameters:
**Name**: the name of the data source.
**Type**: the type of the data source. Select **HDFS2.7**.
**Parameters**: the domain name and port of the Namenode in HDFS. The value is in the
`hdfs://xnn1:port,xnn2:port` format.
4. Click **Add**.

#### Add an OSS data source

You can add an Object Storage Service (OSS) data source for LindormTable to read data stored in OSS. To import data stored in OSS to a Lindorm wide table, you must first add an OSS data source. This topic describes how to add an OSS data source to a Lindorm Tunnel Service (LTS) instance.

**Prerequisites**

An LTS instance is purchased. For more information, see Purchase an LTS instance and log on to the LTS web UI.

**Procedure**

1. Log on to the LTS web UI.
2. In the left-side navigation pane, choose **Data Source Manage > Add Data Source**.
3. On the **Add data source** page, configure the following parameters:

| Parameter | Description |
|---|---|
| accessId | The AccessKey ID of your Apsara Stack tenant account or Resource Access Management (RAM) user that is used to access data stored in OSS. |
| accessKey | The AccessKey secret of your Apsara Stack tenant account or RAM user that is used to access data stored in OSS. |
| bucketName | The name of the OSS bucket that is used as the data source. |
| endpoint | The internal endpoint of the region in which the bucket is located. |

**Name**: the name of the data source.
**Data Source Type**: the type of the data source. Select **OSS**.
**Parameters**: Specify the parameters in the following format:

```json
{
  "accessId": "xaccessId",
  "accessKey": "xaccessKey",
  "bucketName": "xbds-pro-test",
  "endpoint": "oss-cn-qingdao-internal.aliyuncs.com"
}
```

The following table describes the parameters in the preceding code.
4. Click **Add**.

### Migrate data between Lindorm or

**HBase clusters**

#### Migrate data between Lindorm and HBase

**clusters**

This topic describes how to create a task to migrate data between a self-built HBase cluster and a Lindorm instance.

**Scenarios**

Major version upgrades. For example, you can upgrade the major version of your HBase cluster from V1.x to V2.x. Data migration across regions. For example, you can migrate data from a data center in the China (Qingdao) region to a data center in the China (Beijing) region. Cluster specification upgrades. For example, you can upgrade the specification of your HBase clusters from 4 CPU cores and 8 GB memory to 8 CPU cores and 16 GB memory. Workload distribution. For example, you can migrate some of your business to a new cluster.

**Features**

Migration without business interruption between two of the following instances is supported: HBase V0.94 clusters, HBase V0.98 clusters, HBase V1.x clusters, HBase V2.x clusters, and Lindorm instances. Table schema migration, real-time data synchronization, and full data migration are supported. Migration based on databases, namespaces, and tables is supported. Table renaming is supported. Time ranges, row key ranges, and columns can be specified during migration. An API operation is provided to create migration tasks.

**Benefits**

Your business is not interrupted during migration. Both the historical data and real-time incremental data can be migrated during one migration task. During the migration, the destination self-built HBase cluster does not interact with the source HBase cluster. The destination HBase cluster reads data only from the Hadoop Distributed File System (HDFS) of the source cluster. This minimizes the impact on the online business that runs on the source cluster. In most cases, compared with data migration at the API layer, data replication at the file layer helps you reduce more than 50% of the data usage and improves efficiency. Each node can migrate data at a rate of up to 150 MB/s to meet stability requirements for data migration. You can add nodes for horizontal scaling to migrate terabytes or petabytes of data. LTS implements a robust retry mechanism to respond to errors. LTS monitors the task speed and the task progress in real time, and generates alerts when tasks fail. LTS automatically synchronizes schemas to ensure consistency among partitions. HBase clusters that have Kerberos enabled are not supported. Single-node ApsaraDB for HBase instances are not supported. ApsaraDB for HBase instances that are deployed in the classic network are not supported due to network compatibility issues. LTS implements an asynchronous mode to synchronize incremental data based on write-ahead logging (WAL). Data that is imported by using bulk loading and data that is not written to WAL are not synchronized.

**Usage notes**

Before you migrate data, make sure that the HDFS capacity of the destination cluster is sufficient. This helps you prevent the data from exhausting the capacity during migration. Before you submit an incremental synchronization task, we recommend that you modify the log retention period for the source cluster. You must reserve time for LTS to handle incremental synchronization errors. For example, you can change the hbase.master.logcleaner.ttl setting in the hbase-site.xml file to a value greater than 12 hours and restart the HBase Master. You do not need to manually create tables in the destination cluster. LTS automatically creates tables in the same way as those in the source cluster. The automatically created tables in the destination cluster are partitioned in the same way as the tables in the source cluster. The partitioning scheme of a manually created table may be different from that of the source table. As a result, the manually created table may be frequently split or compacted after the migration process is complete. If the table stores a large amount of data, the entire process may take a long time. If the source table has a coprocessor, make sure that the destination cluster contains the corresponding JAR file of the coprocessor when you create a destination table. If log data is not consumed after you enable the incremental synchronization feature, the log data is retained for 48 hours by default. After the period expires, the subscription is automatically canceled, and the retained data is automatically deleted.

**Prerequisites**

The networks among the source cluster, the destination cluster, and LTS are connected. The HBase and Lindorm data sources are added. For more information, see Add an HBase data source and Add a LindormTable data source. Log on to the LTS web UI.

**Create a task**

1. In the left-side navigation pane, choose **Migration > Quick Migration**.
2. Click **create new job**.
3. In the **job name(optional)** field, enter the name of the task. The task name can contain only letters
and digits. You can leave the task name unspecified. In this case, the task ID is used as the task name.
4. Configure the **Source Cluster** and **Target Cluster** parameters as prompted.
5. Select the operations that you want to perform.
**migration table schema**: creates tables in the destination cluster. These tables have the same
schema and partition information as the source tables. If a table already exists in the destination cluster, the data in this table is not migrated.
**real time data replication**: synchronizes real-time incremental data from the source cluster.
**history data migration**: physically migrates all the files at a file level.
6. Enter required information in the **table mapping** and **advance configuration** fields. The advance
configuration field can be left unspecified.
7. Click **create**.

**View the details of a task**

1. In the left-side navigation pane, choose **Migration** > **Quick Migration** to view the task that you
created.
2. On the page that appears, click the name of the task that you want to view. On the page that appears,
view the execution status of the task.

**Perform a switchover**

1. Wait until the full migration task is complete. The latency of incremental synchronization is as low as
several seconds or hundreds of milliseconds.
2. Enable LTS data sampling and verification. When you sample and verify large tables, make sure that the
sampling ratio is appropriate to prevent the online business from being affected.
3. Verify your business.
4. Perform a switchover on your business.

**FAQ**

Q: Why does the data in the task fail to be consumed? A: The LTS cluster is released while the task is still running, the synchronization task is suspended, or the task is abnormally blocked.

## SDK reference

### LindormTable

#### HBase API

##### Install and upgrade ApsaraDB for HBase SDK for

**Java**

To access LindormTable through ApsaraDB for HBase API for Java, see the following sections to upgrade your HBase client version.

**Maven dependency**

Clients of version 1.x are used to manage ApsaraDB for HBase clusters of version 1.x. Clients of version 2.x are used to manage ApsaraDB for HBase clusters of version 2.x. We recommend HBase clients of V2.x for new users.

**HBase V1.x**

```xml
<dependency>
  <groupId>com.aliyun.hbase</groupId>
  <artifactId>alihbase-client</artifactId>
  <version>1.8.2</version>
</dependency>
```

**HBase V2.x**

```xml
<dependency>
  <groupId>com.aliyun.hbase</groupId>
  <artifactId>alihbase-client</artifactId>
  <version>2.8.2</version>
</dependency>
```

**Other scenarios**

**Note**

If your client is reliant on the client of the community edition and you cannot upgrade the client to the preceding recommended versions, follow these methods to upgrade: Modify Maven dependencies to upgrade your ApsaraDB for HBase clients so that the clients correspond to the HBase community edition. For more information, see Modify Maven dependencies to upgrade your clients of earlier versions. Replace JAR files to upgrade your ApsaraDB for HBase clients so that the clients correspond to the HBase community edition. For more information, see Replace JAR files to upgrade your clients of earlier versions.

##### Install and upgrade HBase SDK for a non-Java

**programming language**

You can use non-Java languages such as C++, Python, and Go to access LindormTable if Thrift supports these languages. The ApsaraDB for Lindorm server supports Thrift version 0.12.0. Although Thrift is backward compatible, we recommend that you download Thrift of the version 0.12.0. Some languages provide specific methods to manage dependencies. You can install Thrift based on relevant syntax. For example, you can run the `pip install thrift` command if you use Python, and run the `import` `{"github.com/apache/thrift/lib/go/thrift"}` command if you use Go. LindormTable uses Thrift 2 as the interface definition language (IDL) file. You must download the Thrift 2 definition file to generate the API for the specified language. Compared with Thrift 1, Thrift 2 provides clearer definitions for API operations. You can perform the operations in a similar way as you call Java API operations. The earlier versions of Thrift 2 are not widely used because they do not support some data definition language (DDL) operations such as creating and deleting tables. The Thrift 2 API definitions have been provided by Alibaba Cloud and released to the community. For more information, see HBASE-21649. Thrift 2 provides more comprehensive and easy-to-use features than Thrift 1.

**Preparation**

1. Download the Thrift installation package.
2. Download the Thrift 2 definition file of ApsaraDB for HBase.

**Access method**

The following sections describe how to get started with Thrift. For more information, see Apache Thrift Tutorial.
1. Generate the interface definition file for the specified programming language.
Download the interface definition file and use the following syntax to generate the corresponding interface definition files.

```
thrift --gen <language> Hbase.thrift
```

For example:

```
1. thrift --gen php Hbase.thrift
2. thrift --gen cpp Hbase.thrift
3. thrift --gen py Hbase.thrift
```

2. Initialize a client to access Lindorm.
The Thrift server in Lindorm uses HTTP in the transport layer. The ThttpClient of Thrift is required when you create a client. The method of creating the client varies based on the languages. If the Access Control List (ACL) is enabled, specify the username and password in two headers in the ThttpClient for authentication. The username and password are not required if ACL is disabled. Thrift allows you to call a function for a language to customize a header in ThttpClient. The following example shows how to initialize the client and specify the connection string, username, and password based on Python. For more information, see the Demos for multiple languages section in this topic.

```
1.  # -*- coding: utf-8  -*-
2.  # You can run the pip install thrift command to retrieve the following modules.
3.  from thrift.protocol import TBinaryProtocol
4.  from thrift.transport import THttpClient
```

`5.`

```
6.  # The following module is generated by the thrift --gen py hbase.thrift command.
7.  from hbase import THBaseService
8.  from hbase.ttypes import TColumnValue, TColumn, TTableName, TTableDescriptor,
TColumnFamilyDescriptor, TNamespaceDescriptor, TGet, TPut, TScan
```

`9.`

```
10. # Connection address
11. url = "http://host:9190"
12. transport = THttpClient.THttpClient(url)
13. headers = {}
14. # Username
15. headers["ACCESSKEYID"]="root";
16. # Password
17. headers["ACCESSSIGNATURE"]="root"
18. transport.setCustomHeaders(headers)
19. protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
20. client = THBaseService.Client(protocol)
21. transport.open()
22. # The operations. The connection is finally closed.
23. transport.close()
```

**Demos for multiple languages**

All the demo code has been uploaded to GitHub. The code includes the Thrift definition files and dependencies that are supported by some languages. You can download the code for a language from GitHub. Go C++ node.js PHP

**More languages**

For more information, see Apache Thrift Tutorial.

##### Modify Maven dependencies to upgrade your

**clients of earlier versions**

**Description**

This topic applies if your applications are reliant on the client of the HBase community edition and cannot be upgraded to the ApsaraDB for HBase client of the latest stable version by using the methods described in Install and upgrade ApsaraDB for HBase SDK for Java. You can modify the Maven dependency to upgrade your ApsaraDB for HBase client to a version that is compatible with the community edition.

**Direct reliance of applications on the clients of the HBase community**

**edition**

```xml
    <dependency>
          <groupId>org.apache.hbase</groupId>
          <artifactId>hbase-client</artifactId>
          <version>x.x.x</version>
    </dependency>
```

Replace the preceding code block with the following code block:

```xml
    <dependency>
        <groupId>com.alibaba.hbase</groupId>
        <artifactId>alihbase-client</artifactId>
        <version>x.x.x</version>
    </dependency>
    <!--Replace ${connector-version} with the version of alihbase-connector that corresponds to the
version of hbase-client. For more information, see the version mappings in the following table.-->
    <dependency>
        <groupId>com.alibaba.hbase</groupId>
        <artifactId>alihbase-connector</artifactId>
        <version>${connector-version}</version>
        <exclusions>
            <exclusion>
                <groupId>org.apache.hbase</groupId>
                <artifactId>hbase-client</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
```

**Indirect reliance of applications on the clients of the HBase community**

**edition**

This method is applicable to applications whose third-party dependencies are reliant on HBase.

```xml
    <!--The third-party package dependency-->
    <dependency>
          <groupId>xxx.xxx.xxx</groupId>
          <artifactId>yyy</artifactId>
          <version>z.z.z</version>
    </dependency>
```

Replace the preceding code block with the following code block:

| hbase-client version | alihbase-connector version |
|---|---|
| 1.0.0 | 1.0.24.1 |
| 1.0.1 | 1.0.24.1 |
| 1.0.1.1 | 1.0.24.1 |
| 1.0.2 | 1.0.24.1 |
| 1.0.3 | 1.0.24.1 |
| 1.1.0 | 1.0.24.1 |
| 1.1.0.1 | 1.0.24.1 |
| 1.1.1 | 1.0.24.1 |
| 1.1.2 | 1.0.24.1 |
| 1.1.3 | 1.0.24.1 |
| 1.1.4 | 1.0.24.1 |
| 1.1.5 | 1.0.24 |

```xml
    <!--Remove the hbase-client dependency from the third-party dependency.-->
    <dependency>
        <groupId>xxx.xxx.xxx</groupId>
        <artifactId>yyy</artifactId>
        <version>z.z.z</version>
        <exclusions>
            <exclusion>
                <groupId>org.apache.hbase</groupId>
                <artifactId>hbase-client</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
    <!--Add the alihbase-client dependency.-->
    <dependency>
        <groupId>com.alibaba.hbase</groupId>
        <artifactId>alihbase-client</artifactId>
        <version>x.x.x</version>
    </dependency>
    <!--Replace ${connector-version} with the version of alihbase-connector that corresponds to the
version of hbase-client. For more information, see the version mappings in the following table.-->
    <dependency>
        <groupId>com.alibaba.hbase</groupId>
        <artifactId>alihbase-connector</artifactId>
        <version>${connector-version}</version>
        <exclusions>
            <exclusion>
                <groupId>org.apache.hbase</groupId>
                <artifactId>hbase-client</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
```

**Version mappings between hbase-client and alihbase-connector**

| 1.1.6 | 1.0.24 |
|---|---|
| 1.1.7 | 1.0.24 |
| 1.1.8 | 1.0.24 |
| 1.1.9 | 1.0.24 |
| 1.1.10 | 1.0.24 |
| 1.1.11 | 1.0.24 |
| 1.1.12 | 1.0.24 |
| 1.1.13 | 1.0.24 |
| 1.2.0 | 1.0.24.1 |
| 1.2.1 | 1.0.24 |
| 1.2.2 | 1.0.24 |
| 1.2.3 | 1.0.24 |
| 1.2.4 | 1.0.24 |
| 1.2.5 | 1.0.24 |
| 1.2.6 | 1.0.24 |
| 1.2.6.1 | 1.0.24 |
| 1.2.7 | 1.0.24 |
| 1.2.8 | 1.0.24 |
| 1.2.9 | 1.0.24 |
| 1.2.10 | 1.0.24 |
| 1.2.11 | 1.0.24 |
| 1.2.12 | 1.0.24 |
| 1.3.0 | 1.0.24 |
| 1.3.1 | 1.0.24 |
| 1.3.2 | 1.0.24 |
| 1.3.2.1 | 1.0.24 |
| 1.3.3 | 1.0.24 |
| 1.3.4 | 1.0.24 |
| 1.3.5 | 1.0.24 |
| 1.3.6 | 1.0.24 |
| 1.4.0 | 1.0.24 |
| 1.4.1 | 1.0.24 |
| 1.4.2 | 1.0.24 |

| 1.4.3 | 1.0.24 |
|---|---|
| 1.4.4 | 1.0.24 |
| 1.4.5 | 1.0.24 |
| 1.4.6 | 1.0.24 |
| 1.4.7 | 1.0.24 |
| 1.4.8 | 1.0.24 |
| 1.4.9 | 1.0.24 |
| 1.4.10 | 1.0.24 |
| 1.4.11 | 1.0.24 |
| 1.4.12 | 1.0.24 |
| 1.4.13 | 1.0.24 |
| 1.5.0 | 1.0.24 |
| 1.6.0 | 1.0.24 |
| 2.0.0 | 2.0.24 |
| 2.0.1 | 2.0.24 |
| 2.0.2 | 2.0.24.1 |
| 2.0.3 | 2.0.24.1 |
| 2.0.4 | 2.0.24.1 |
| 2.0.5 | 2.0.24.1 |
| 2.0.6 | 2.0.24.1 |
| 2.1.0 | 2.0.24 |
| 2.1.1 | 2.0.24.1 |
| 2.1.2 | 2.0.24.1 |
| 2.1.3 | 2.0.24.1 |
| 2.1.4 | 2.0.24.1 |
| 2.1.5 | 2.0.24.1 |
| 2.1.6 | 2.0.24.1 |
| 2.1.7 | 2.0.24.1 |
| 2.1.8 | 2.0.24.1 |
| 2.1.9 | 2.0.24.1 |
| 2.2.0 | 2.0.24.1 |
| 2.2.1 | 2.0.24.1 |
| 2.2.2 | 2.0.24.1 |

| 2.2.3 | 2.0.24.1 |
|---|---|

##### Replace JAR files to upgrade your clients of

**earlier versions**

**Description**

This topic applies if your applications are reliant on the client of the HBase community edition and cannot be upgraded to the ApsaraDB for HBase client of the latest stable version by using the methods described in Install and upgrade ApsaraDB for HBase SDK for Java. You can replace the original JAR file with the ApsaraDB for HBase JAR file when you deploy the backend service. This way, you can upgrade your client to the ApsaraDB for HBase version that corresponds to the HBase community edition.

**Replace the JAR file**

Find the hbase-client-x.x.x.jar JAR file in the lib directory of the open source service. x.x.x is the version of hbase-client. Then, replace the JAR file with the corresponding version of the alihbase-client JAR file. For example, if the original JAR file is hbase-client-1.0.0.jar, replace it with alihbase-client-1.0.0.jar. Download link:

```
https://hbaseuepublic.oss-cn-beijing.aliyuncs.com/alihbase-client-x.x.x.jar
```

**Download the plug-in**

Download only the plug-ins of Lindorm. The hbase-client plug-in is excluded.

```bash
# Plug-in of version 1.x
https://hbaseuepublic.oss-cn-beijing.aliyuncs.com/alihbase-connector-1.0.24.jar
# Plug-in of version 2.x
https://hbaseuepublic.oss-cn-beijing.aliyuncs.com/alihbase-connector-2.0.24.jar
```

#### Cassandra CQL Driver

##### Install and upgrade a Cassandra client driver for

**Java**

To access LindormTable through Cassandra client driver for Java, see the following section to upgrade your client version.

**Maven dependency**

You can use Datastax Java Driver to access Lindorm CQL. We recommend that you use Datastax Java Driver V3.7 or later. The following example shows how to add the dependency to your Maven project.

```xml
<dependency>
    <groupId>com.datastax.cassandra</groupId>
    <artifactId>cassandra-driver-core</artifactId>
    <version>3.7.2</version>
</dependency>
```

Some public libraries are introduced after you add the dependency. To prevent issues caused by dependency conflicts, test the dependency in a new project first.

#### Phoenix SQL API

##### Install PhoenixSQL Java SDK

To use the PhoenixSQL Java SDK, add the Maven dependency to your project.

**Maven dependency**

Allow access only from PhoenixSQL think client:

```xml
<dependency>
  <groupId>com.aliyun.phoenix</groupId>
  <artifactId>ali-phoenix-queryserver-client</artifactId>
  <version>5.2.5-HBase-2.x</version>
</dependency>
```

**JDBC connection**

The format of Java Database Connectivity (JDBC) connection string is as follows.

```
  jdbc:phoenix:thin:[key=value[;key=value...]]
```

Simple example

```
  jdbc:phoenix:thin:url=http://localhost:8765;serialization=PROTOBUF
```

### LindormTSDB

**Important**

Starting September 1, 2024, you can **no longer purchase LindormTSDB**. Users who purchased LindormTSDB and migrated data from TSDB to LindormTSDB before September 1, 2024 can still use LindormTSDB as expected.

#### Usage details

##### Use the TSDBConfig class to configure a

**LindormTSDB client**

You can use the TSDBConfig class to configure all settings of a LindormTSDB client. You can call the config() method to build a TSDBConfig object. For more information about how to use TSDBConfig to configure a LindormTSDB client, see the following sample code.

```
    // Configure the endpoint of the LindormTSDB client. example.tsdb.com specifies the domain or t
he IP address of the LindormTSDB client. The value 8242 specifies the port that is used by the Lind ormTSDB client.
    .address("example.tsdb.com", 8242)
    // tsdbuser and password specify the username and password that are used for user authenticatio
n. You can create a user for a LindormTSDB instance on the instance details page in the LindormTSDB console. If user authentication is disabled for the LindormTSDB instance, you do not ne ed to call the basicAuth() method when you create a TSDBConfig object.
    .basicAuth("tsdbuser", "password")
    // Specify whether the TSDBConfig object is read-only. By default, the value is false. If you s
et the value to true, asynchronous write operations cannot be performed.
    .readonly(false)
```

```java
     // Configure the size of the connection pool. By default, the value is 64.
    .httpConnectionPool(64)
    // Configure the timeout period for an HTTP connection. Unit: seconds. By default, the value is
90.
    .httpConnectTimeout(90)
    // Configure the number of I/O threads. By default, the value is 1.
    .ioThreadCount(1)
    // Specify whether to allow asynchronous write operations. By default, the value is true. We re
commend that you retain the default value.
    .asyncPut(true)
    // Specifies the length of the buffer queue for a client. By default, the length is 10,000 requ
ests. This method only takes effect when asynchronous writes are enabled.
    .batchPutBufferSize(20000)
    // Configure the number of consumer threads in the buffer. By default, the value is 1. This par
ameter takes effect only when asynchronous write operations are allowed.
    .batchPutConsumerThreadCount(2)
    // Configure the number of data points to be submitted to the LindormTSDB client. By default, t
he value is 500. This parameter takes effect only when asynchronous writes are allowed.
    .batchPutSize(500)
    // Configure the maximum waiting time. Unit: milliseconds. By default, the value is 300. This p
arameter takes effect only when asynchronous write operations are allowed.
    .batchPutTimeLimit(300)
    // Configure the number of write request queues. By default, the value equals the number of con
nection pools. This parameter takes effect only when asynchronous write operations are allowed. You can configure this parameter based on the read/write ratio.
    .putRequestLimit(100)
    // Specify whether to remove the limit on the number of write request queues. We recommend that
you impose the limit because out-of-memory (OOM) errors can occur if you remove the limit. This par ameter takes effect only when asynchronous write operations are allowed.
    .closePutRequestLimit()
    // Use the callback interface for asynchronous PUT requests. This parameter takes effect only w
hen asynchronous writes are allowed.
    .listenBatchPut(new BatchPutCallback() {
         // The following callback function is invoked if a write operation is successful.
        @Override
        public void response(List<Point> input, Result output) {;;}
        // The following callback function is invoked if a write operation fails.
        @Override
        public void failed(String address, List<Point> input, Exception ex) {;;}
    })
    // Configure the maximum number of data points that you want to submit per second. This paramet
er is used to configure traffic throttling.
    .maxTPS(50000)
    .config();// Build a TSDBConfig object.
```

##### Query data

Before you query data, build a Query object. A Query object contains query conditions. You can specify tags, metrics, and aggregated query conditions in a Query object. This way, you can query the data that meets the specified conditions. Build a Query object that contains query conditions.

```
    .timeRange(startTime, endTime)    // Specify the time range during which you want to query data
```

.

```
    .sub(SubQuery.metric("hello").aggregator(Aggregator.AVG).tag("tagk1", "tagv1").build())    // C
reate a subquery.
    .sub(SubQuery.metric("world").aggregator(Aggregator.SUM).tag("tagk2", "tagv2").build())    // C
reate a subquery.
    .build();
```

**Subqueries**

You can create multiple SubQuery objects in a Query object. This way, you can create subqueries that contain multiple query conditions. Create a sample subquery.

```
           .metric("test-metric")
           .aggregator(Aggregator.AVG)
           .downsample("60m-avg")
           .tag("tagk1", "tagv1")
           .tag("tagk2", "tagv2")
           .build();
```

SubQuery is an object in which you can define a subquery. Aggregator is an enumeration class. LindormTSDB SDK allows you to query data in thread synchronization mode. Use the query() method to query data in a synchronous manner.

```java
List<QueryResult> result = tsdb.query(query); System.out.println("Returned result" + result);
```

LindormTSDB SDK allows you to query data in an asynchronous thread manner. Use the query() method to query data in an asynchronous manner and configure a callback to define how the query result is returned.

```java
    @Override
    public void response(Query input, List<QueryResult> result) {
        System.out.println("Query parameters:" + input);
        System.out.println("Returned result:" + result);
    }
 };
 tsdb.query(query, cb);
```

**Query data and sort the query result in descending order**

LindormTSDB SDK allows you to query data and sort the query result in descending or ascending order. The getOrderDps(boolean ordeset) method can be used to sort query results based on timestamps in descending order. If you use getOrderDps(true) in a query, the returned query result is sorted based on timestamps in descending order. If you use getOrderDps() in a query, the returned query result is sorted based on timestamps in ascending order.

```java
        .timeRange(current - 1000,start + 1000)
        .sub(SubQuery.metric(metric).aggregator(Aggregator.NONE).tag(tags).build())
        .build();
try {
     // Run a query and obtain the query result.
     List<QueryResult> result = tsdb.query(query);
         // Obtain unordered data points.
         System.out.println(queryResult.getDps());
         System.out.println("-------------");
         // Obtain a collection of data points sorted based on timestamps in ascending order.
         System.out.println(queryResult.getOrderDps());
         System.out.println("-------------");
         // Obtain a collection of data points sorted based on timestamps in descending order.
         System.out.println(queryResult.getOrderDps(true));
      }
} catch (HttpUnknowStatusException e) {
      e.printStackTrace();
}
```

If you use the query() method to query data, the query result is returned in List<QueryResult>. QueryResult indicates the query result of a subquery. You can use the getDps() method in QueryResult to obtain query results. LindormTSDB SDK allows you to query the latest data point before a specified timestamp. Sample code:

**Example 1**

Create a query that contains subqueries. The metrics and tags are specified in subqueries.

```java
// Create tags. Map<String,String> tags = new HashMap<String, String>(); tags.put("uid","1"); tags.put("id","6"); String metric = "test.1"; // Create a query to return the latest data point. LastPointQuery query = LastPointQuery.builder()
        // Specify a timestamp.
        .timestamp(1537520409729l)
        // Move forward by the specified number of hours from the given timestamp. The default
value is 0, which means the hour of the given timestamp itself.
        // -1 means keep moving forward until data is found.
        .backScan(0)
        // Specify whether to use a timestamp in milliseconds to query data.
        .msResolution(true)
        // Create a subquery to return the latest data point of a specified time series.
        // You can create multiple subqueries at the same time.
        .sub(LastPointSubQuery.builder(metric,tags).build()).build();
// Obtain the latest point of each time series. Each time series has a LastDataValue. List<LastDataValue> lastDataValues = tsdb.queryLast(query); System.out.println(lastDataValues);
```

The tsuids value can be obtained from the query result in Example 1. The first time you query data based on Example 1, you can save the tsuids value returned in the query result for subsequent use.

##### Call other APIs

**TTL**

Time To Live (TTL) indicates the validity period of data. Specify TTL. Unit: seconds:

```
tsdb.ttl(time);
```

Obtain TTL. Unit: seconds:

```
int ttl = tsdb.ttl();
```

**Suggest**

Query metric, tag key, and tag value. Query 10 metric names that start with hel:

```java
List<String> metrics = tsdb.suggest(Suggest.Metrics, "hel", 10); System.out.println("Query result:" + metrics);
```

**DumpMeta**

Query tag value by tag key. Query 10 tag key-value pairs where the tag name is "tagk1" and the value starts with "tagv1":

| Class | Description |
|---|---|
| TSDBConfig | The configuration class of LindormTSDB. All client options are configured in this class. |
| TSDBConfig.Builder | The TSDBConfig builder. TSDBConfig objects are created by using this class. |
| TSDBClientFactory | The engineering class of LindormTSDB clients. TSDB objects are created by using TSDBConfig objects. |

```java
List<TagResult> dumpMeta = tsdb.dumpMeta("tagk1", "tagv1", 10); System.out.println("Query result:" + dumpMeta);
```

Delete data within a time range. Delete all data whose metric name is "hello" between startTime and nowTime:

```
tsdb.deleteData("hello", startTime, nowTime);
```

Clear all table data.

```
tsdb.truncate()
```

##### Shut down the client

This topic describes how to shut down the LindormTSDB client.

**Use graceful shutdown**

The LindormTSDB client provides the graceful shutdown feature. The client is suspended during the shutdown process until the server finishes processing all requests. We recommend that you use the graceful shutdown feature in case data loss occurs.
**Sample code**:

```
tsdb.close(); // This is equivalent to tsdb.close(false);
```

If you do not want to use the graceful shutdown feature, you can forcefully shut down the client.
**Sample code**:

```
tsdb.close(true);
```

#### Common classes and methods

##### Overview of common SDK classes

This topic describes common classes in LindormTSDB SDKs by SDK package name. For information about the details and use methods of some important common classes, click their names to view the corresponding documentation.

| TSDBClient | The operation class of LindormTSDB. This class is used to implement the com.aliyun.hitsdb.client.TSDB API operation. The class is thread-safe and used to complete all operations on LindormTSDB. In most cases, only one LindormTSDB class object is required globally. |
|---|---|
| TSDB | The API operation class of TSDBClient. |

| Class | Description |
|---|---|
| Point | The class for time points. This class indicates the data to be written to LindormTSDB. |
| Point.MetricBuilder | The point builder. Point objects are created from this class. |
| Timeline | The class for timelines. This class indicates the timeline of LindormTSDB. |
| Query | The class for queries. |
| Query.Builder | The query builder. |
| SubQuery | The class for subqueries. |
| SubQuery.Builder | The subquery builder. |
| Filter | The class for filtering. |
| Filter.Builder | The filter builder. |
| MetricTimeRange | The MetricTimeRange value. |
| TTLValue | The time-to-live (TTL) value. |
| SuggestValue | The SuggestValue value. |

| Class | Description |
|---|---|
| QueryResult | The class for query results. |
| SQLResult | The class for SQL query results. |
| TagResult | The class for tag query results. |
| LastDPValue | The value of the last query result. |

| Class | Description |
|---|---|
| Aggregator | The class for aggregate computing. |
| FilterType | The class for filtering types. |
| Suggest | The class for query results. |

| Class | Description |
|---|---|

**Package name: com.aliyun.hitsdb.client.value.request**

**Package name: com.aliyun.hitsdb.client.value.response**

**Package name: com.aliyun.hitsdb.client.value.type**

| QueryCallback | The class for query callbacks. |
|---|---|
| BatchPutCallback | The class for write callbacks. |
| BatchPutDetailsCallback | The class for write callbacks. |
| BatchPutSummaryCallback | The class for write callbacks. |

| Class | Description |
|---|---|
| BufferQueueFullException | The queue is full. |

| Class | Description |
|---|---|
| HttpClientConnectionRefusedException | The LindormTSDB server rejects the connection. |
| HttpClientException | A client exception occurs. |
| HttpClientInitException | An exception occurs during client initialization. |
| HttpClientSocketTimeoutException | A network timeout occurs. |
| HttpServerErrorException | The server returns the 500 error code or an error code that is larger than 500. |
| HttpServerNotSupportException | The server returns the 400 error code or an error code that is larger than 400. |
| HttpUnknowStatusException | The server returns an undefined error code. |

| Qualifier and type | Method and description |
|---|---|
| void | close() Shuts down a LindormTSDB client. |
| void | close(boolean force) Shuts down a LindormTSDB client. |
| void | delete(Query query) Deletes data. This method does not take effect. |

**Package name: com.aliyun.hitsdb.client.exception**

**Package name: com.aliyun.hitsdb.client.exception.http**

##### TSDBClient

java.lang.Object Implemented API operations: TSDB, Closeable, and AutoCloseable

```java
public class TSDBClient extends Object implements TSDB
```

| void | deleteData(String metric, Date startDate, Date endDate) Deletes data. You must specify a metric and a time range. |
|---|---|
| void | deleteData(String metric, long startTime, long endTime) Deletes data. You must specify a metric and a time range. |
| void | deleteMeta(String metric, Map<String,String> tags) Deletes a timeline and all data that is related to the timeline. |
| void | deleteMeta(Timeline timeline) Deletes a timeline and all data that is related to the timeline. |
| List<TagResult> | dumpMeta(String tagkey, String tagValuePrefix, int max) Queries tags. |
| List<QueryResult> | last(Query query,int num) Queries data. |
| List<LastDPValue> | lastdp(Collection<Timeline> timelines) Queries the last data point in a timeline. |
| List<LastDPValue> | lastdp(Timeline… timelines) Queries the last data point in a timeline. |
| void | put(Point… points) Asynchronously writes time points to LindormTSDB. |
| void | put(Point point) Asynchronously writes time points to LindormTSDB. put(Point point) |
| <T extends Result>T | putSync(Class<T> resultType, Collection<Point> points) Synchronously writes time points to LindormTSDB. |
| <T extends Result>T | putSync(Class<T> resultType, Point… points) Synchronously writes time points to LindormTSDB. |
| Result | putSync(Collection<Point> points) Synchronously writes time points to LindormTSDB. |
| <T extends Result>T | putSync(Collection<Point> points, Class<T> resultType) Synchronously writes time points to LindormTSDB. |
| Result | putSync(Point… points) Synchronously writes time points to LindormTSDB. |
| List<QueryResult> | query(Query query) Queries data. |

| void | query(Query query, QueryCallback callback) Queries data. |
|---|---|
| List<String> | suggest(Suggest type, String prefix, int max) Queries metrics that meet specific conditions. |
| int | ttl() Queries a time-to-live (TTL) value. Unit: seconds. |
| void | ttl(int lifetime) Specifies a TTL value. Unit: seconds. |
| void | ttl(int lifetime,TimeUnit unit) |

Methods inherited from the java.lang.Object class clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait Constructor details

```
public TSDBClient(TSDBConfig config) throws HttpClientInitException
```

Exception thrown: HttpClientInitException Method details close

```
public void close() throws IOException
```

The designator: close specifier: Closeable The designator: close specifier: AutoCloseable Exception thrown: IOException close

```
public void close(boolean force) throws IOException
```

Shuts down a LindormTSDB instance. You can call this method before you exit the program. The designator: close specifier: TSDB Parameters: force - true or false Exception thrown: IOException - exception

```
public void deleteData(String metric, long startTime, long endTime)
```

The designator: Parameters: metric - the metric name startTime - the start timestamp endTime - the end timestamp

```
public void deleteData(String metric, Date startDate, Date endDate)
```

Deletes the data of the specified metric in the specified time range. The designator: Parameters: metric - the metric name startDate - the start date endDate - the end date

```
public void deleteMeta(String metric,Map<String,String> tags)
```

Deletes timeline data. The designator: Parameters: metric - the metric name Tags - the tag key-value pairs in the map format The designator: Parameters: timeline - the instance of the Timeline class dumpMeta

```
public List<TagResult> dumpMeta(String tagkey, String tagValuePrefix, int max)
```

Queries tags that meet specific conditions. The designator: dumpMeta specifier: TSDB Parameters: tagkey - the tag key tagValuePrefix - the prefix of the tag value max - the maximum value Response: The list of TagResult put Asynchronously writes data. The designator: put specifier: TSDB Parameters: Queries data. The designator: Parameters: Response: Asynchronously queries data. The query result is returned in a callback. The designator: Parameters: callback - the instance of the QueryCallback class. The query result is asynchronously returned in a callback. suggest

```
public List<String> suggest(Suggest type, String prefix, int max)
```

suggest method The designator: suggest specifier: TSDB Parameters: type - the data type prefix - the prefix max - the maximum value Response: ttl

```
public int ttl()
```

Queries a TTL value. Unit: seconds. The designator: suggest specifier: TSDB Response: The TTL value. Unit: seconds. ttl

```
public void ttl(int lifetime)
```

Specifies a TTL value. The designator: ttl specifier: TSDB Parameters: lifetime - the TTL value. Unit: seconds. ttl

```
public void ttl(int lifetime, TimeUnit unit)
```

The designator: ttl specifier: TSDB Parameters: lifetime - the TTL value unit - the unit of the TTL value last

```
public List<QueryResult> last(Query query, int num) throws HttpUnknowStatusException
```

The designator: last specifier: TSDB Parameters: num - the number of last data points in the timeline Response: A list of results Exception thrown: HttpUnknowStatusException - Exception putSync

```
public Result putSync(Collection<Point> points)
```

Synchronously writes time points. The designator: putSync specifier: TSDB Parameters: Response: A Result instance. This object is used only to indicate that the method returns a result. putSync

```
public <T extends Result> T putSync(Collection<Point> points, Class<T> resultType)
```

Synchronously writes data. The designator: putSync specifier: TSDB Type parameter: T - Result.class, SummaryResult.class, DetailsResult.class Parameters: resultType - the result type Response: A Result instance

```
public void delete(Query query) throws HttpUnknowStatusException
```

Deletes data. This method does not take effect. The designator: Parameters: Exception thrown: HttpUnknowStatusException - Exception lastdp

```
public List<LastDPValue> lastdp(Collection<Timeline> timelines) throws HttpUnknowStatusException
```

Queries the last data point in a timeline. The designator: lastdp specifier: TSDB Parameters: timelines - the instance of the Timelines class Response: The result Exception thrown: HttpUnknowStatusException - Exception lastdp

```
public List<LastDPValue> lastdp(Timeline… timelines) throws HttpUnknowStatusException
```

Queries the last data point in a timeline. The designator: lastdp specifier: TSDB Parameters: timelines - the instance of the Timelines class Response: List Exception thrown: HttpUnknowStatusException - Exception put Asynchronously writes time points. The designator: put specifier: TSDB Parameters: putSync Synchronously writes time points. The designator: putSync specifier: TSDB Parameters: Response: putSync

```
public <T extends Result> T putSync(Class<T> resultType, Collection<Point> points)
```

Synchronously writes data. The designator: putSync specifier: TSDB Type parameter: T - Result.class, SummaryResult.class, DetailsResult.class Parameters: resultType - the result type Response: putSync

```
public <T extends Result> T putSync(Class<T> resultType, Point… points)
```

Synchronously writes data. The designator: putSync specifier: TSDB Type parameter: T - Result.class, SummaryResult.class, DetailsResult.class Parameters: resultType - the result type

| Qualifier and type | Class and description |
|---|---|
| static class | TSDBConfig.Builder |

| Qualifier and type | Method and description |
|---|---|
| static TSDBConfig.Builder | address(String host, int port) Configures the endpoint of a TSDB client to obtain TSDB.Builder. |
| int | getBatchPutBufferSize() Queries the size of the buffer for asynchronous writes. |
| AbstractBatchPutCallback | getBatchPutCallback() Queries the instances of the AbstractBatchPutCallback class. |
| int | AbstractBatchPutCallback<?> getBatchPutCallback() Queries the number of consumer threads in the buffer. |
| int | getBatchPutConsumerThreadCount() Queries the number of retries. |
| int | getBatchPutSize() Queries the number of data points that are automatically submitted at a time. |
| int | getBatchPutTimeLimit() Queries the time limit for data writing. Unit: milliseconds. |
| int | getHttpConnectionLiveTime() Queries the duration during which each HTTP connection is alive. Unit: seconds. |
| int | getHttpConnectionPool() Queries the maximum number of connections in a connection pool. |
| int | getHttpConnectTimeout() Queries the timeout period for each HTTP connection. Unit: seconds. |

Response:

##### TSDBConfig

java.lang.Object Nested classes

| int | getHttpKeepaliveTime() Queries the duration during which each persistent connection is alive. Unit: seconds. |
|---|---|
| int | getIoThreadCount() Queries the number of I/O threads for asynchronous writes. |
| int | getMaxTPS() Queries the maximum number of transactions per second (TPS). |
| boolean | isAsyncPut() Queries whether asynchronous writes are allowed. |
| boolean | isHttpCompress() Queries whether data is transmitted after compression. |

Methods inherited from the java.lang.Object class clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Constructor details**

**Method details**

**address**

```
public static TSDBConfig.Builder address(String host, int port)
```

**address**

```
public static TSDBConfig.Builder address(TSDBNetAddress… netAddresses)
```

**getPutRequestLimit**

```
public int getPutRequestLimit()
```

**getBatchPutBufferSize**

```
public int getBatchPutBufferSize()
```

**getBatchPutCallback**

```
public AbstractBatchPutCallback<?> getBatchPutCallback()
```

**getBatchPutConsumerThreadCount**

```
public int getBatchPutConsumerThreadCount()
```

**getBatchPutRetryCount**

```
public int getBatchPutRetryCount()
```

**getBatchPutSize**

```
public int getBatchPutSize()
```

**getBatchPutTimeLimit**

```
public int getBatchPutTimeLimit()
```

**getHttpConnectionPool**

```
public int getHttpConnectionPool()
```

**getHttpConnectTimeout**

```
public int getHttpConnectTimeout()
```

**getIoThreadCount**

```
public int getIoThreadCount()
```

**isHttpCompress**

```
public boolean isHttpCompress()
```

**isBackpressure**

```
public boolean isBackpressure()
```

**getHttpConnectionLiveTime**

```
public int getHttpConnectionLiveTime()
```

**getHttpKeepaliveTime**

```
public int getHttpKeepaliveTime()
```

**isAsyncPut**

```
public boolean isAsyncPut()
```

**getMaxTPS**

```
public int getMaxTPS()
```

##### TSDBConfig.Builder

**Class name: com.aliyun.hitsdb.client.TSDBConfig.Builder**

java.lang.Object

```
public static class TSDBConfig.Builder extends Object
```

**Constructor summary**

**Constructor and description**

```
Builder(Stringhost, intport) Uses the IP address and port of LindormTSDB to create a TSDBConfig.Builder instance.
```

| Qualifier and type | Method and description |
|---|---|
| TSDBConfig.Builder | asyncPut(boolean asyncPut) Specifies whether to enable asynchronous writes. Default value: true. We recommend that you retain the default value. |
| TSDBConfig.Builder | batchPutBufferSize(int batchPutBufferSize) Specifies the length of the buffer queue for a client. Default value: 10000. This method takes effect only when asynchronous writes are enabled. |
| TSDBConfig.Builder | batchPutConsumerThreadCount(int batchPutConsumerThreadCount) Specifies the number of consumer threads in the buffer queue. Default value: 1. This parameter takes effect only when asynchronous writes are enabled. |
| TSDBConfig.Builder | batchPutSize(int batchPutSize) Specifies the number of data points that are submitted to clients at a time. Default value: 500. This method takes effect only when asynchronous writes are enabled. |
| TSDBConfig.Builder | batchPutTimeLimit(int batchPutTimeLimit) Specifies the timeout period for each asynchronous write. Unit: milliseconds. Default value: 300. Unit: milliseconds. This method takes effect only when asynchronous writes are enabled. |
| TSDBConfig.Builder | closePutRequestLimit() Specifies whether to disable the limit on the number of queues for write requests. We recommend that you enable the limit because out-of-memory (OOM) errors may occur if you disable the limit. This method takes effect only when asynchronous writes are enabled. |
| TSDBConfig | config() Constructs a TSDBConfig object. |
| TSDBConfig.Builder | httpCompress(boolean httpCompress) Specifies whether to enable HTTP compression. |
| TSDBConfig.Builder | httpConnectionLiveTime(int httpConnectionLiveTime) Specifies the duration during which a connection is alive. Unit: seconds. The default value is 0, which specifies that this method does not take effect. |
| TSDBConfig.Builder | httpConnectionPool(int connectionPool) Specifies the size of the HTTP connection pool. |
| TSDBConfig.Builder | httpConnectTimeout(int httpConnectTimeout) Specifies the timeout period for each HTTP request. Unit: seconds. Default value: 90. |
| TSDBConfig.Builder | httpKeepaliveTime(int httpKeepaliveTime) Specifies the period during which each HTTP persistent connection is alive. |
| TSDBConfig.Builder | ioThreadCount(int ioThreadCount) Specifies the number of I/O threads. Default value: 1. |

| TSDBConfig.Builder | listenBatchPut(AbstractBatchPutCallback<?> cb) Specifies the callback API operation for asynchronous batch writes. |
|---|---|
| TSDBConfig.Builder | maxTPS(int maxTPS) Specifies the limit on the transactions per second (TPS) for clients. By default, no limit is imposed on the TPS for clients. |
| TSDBConfig.Builder | openHttpCompress() Enables HTTP compression. |
| TSDBConfig.Builder | putRequestLimit(int limit) Specifies the number of queues for write requests. By default, the number is equal to the number of connection pools. This method takes effect only when asynchronous writes are enabled. You can configure this parameter based on the read/write ratio. |
| TSDBConfig.Builder | readonly() Turns on the read-only switch. If you set the value to true, asynchronous write operations cannot be performed. |
| TSDBConfig.Builder | readonly(boolean readonly) Specifies whether to turn on the read-only switch. By default, the read-only switch is turned off. If you set the value to true, asynchronous write operations cannot be performed. |

**Methods inherited from** the java.lang.Object class
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Constructor details**

```
public Builder(String host, int port) public Builder(TSDBNetAddress… netAddresses)
```

**Method details**

**putRequestLimit**

```
public TSDBConfig.Builder putRequestLimit(int limit)
```

**batchPutBufferSize**

```
public TSDBConfig.Builder batchPutBufferSize(int batchPutBufferSize)
```

**batchPutConsumerThreadCount**

```
public TSDBConfig.Builder batchPutBufferSize(int batchPutBufferSize)
```

**batchPutRetryCount**

```
public TSDBConfig.Builder batchPutRetryCount(int batchPutRetryCount)
```

**batchPutSize**

```
public TSDBConfig.Builder batchPutSize(int batchPutSize)
```

**batchPutTimeLimit**

```
public TSDBConfig.Builder batchPutTimeLimit(int batchPutTimeLimit)
```

**closePutRequestLimit**

```
public TSDBConfig.Builder closePutRequestLimit()
```

**closeBackpressure**

**backpressure**

```
public TSDBConfig.Builder backpressure(boolean backpressure)
```

**httpConnectionLiveTime**

```
public TSDBConfig.Builder httpConnectionLiveTime(int httpConnectionLiveTime)
```

**httpKeepaliveTime**

```
public TSDBConfig.Builder httpKeepaliveTime(int httpKeepaliveTime)
```

**readonly**

**readonly**

```
public TSDBConfig.Builder readonly(boolean readonly)
```

**asyncPut**

```
public TSDBConfig.Builder asyncPut(boolean asyncPut)
```

**maxTPS**

**httpCompress**

```
public TSDBConfig.Builder httpCompress(boolean httpCompress)
```

**httpConnectionPool**

```
public TSDBConfig.Builder httpConnectionPool(int connectionPool)
```

**httpConnectTimeout**

```
public TSDBConfig.Builder httpConnectTimeout(int httpConnectTimeout)
```

**ioThreadCount**

```
public TSDBConfig.Builder ioThreadCount(int ioThreadCount)
```

**listenBatchPut**

```
public TSDBConfig.Builder listenBatchPut(AbstractBatchPutCallback<?> cb)
```

| Qualifier and type | Method and description |
|---|---|
| static TSDB | connect(TSDBConfig config) Configures the endpoint and the port to create a TSDB instance. This method is a static method. |
| static TSDB | connect(String host, int port) Uses the TSDBConfig class to create a TSDBClient instance. This method is a static method. |

**openHttpCompress**

##### TSDBClientFactory

**Class name: com.aliyun.hitsdb.client.TSDBClientFactory**

java.lang.Object

```java
public class TSDBClientFactory extends Object
```

Constructor: TSDBClientFactory() Engineering method for TSDB instances Methods inherited from the java.lang.Object class clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Constructor details**

**Method details**

```
public static TSDB connect(String host, int port) throws HttpClientInitException
```

Exception thrown: HttpClientInitException

```
public static TSDB connect(TSDBConfig config) throws HttpClientInitException
```

Exception thrown: HttpClientInitException

##### Point

**Class name: com.aliyun.hitsdb.client.value.request.Point**

java.lang.Object Nested classes

| Qualifier and type | Class and description |
|---|---|
| static class | Point.MetricBuilder |

| Qualifier and type | Method and description |
|---|---|
| static void | checkPoint(Point point) Verifies the format of a time point. |
| String | getAggregator() Queries Aggregator parameters. |
| String | getMetric() Queries the name of a metric. |
| Map<String,String> | getTags() Queries tags. |
| Long | getTimestamp() Queries a timestamp. |
| Number | getValue() Queries a time value. |
| Long | getVersion() Queries the version number of a value. |
| static Point.MetricBuilder | metric(String metric) Specifies a metric and creates and obtains a Point.MetricBuilder instance. |
| void | setAggregator(String aggregator) Specifies Aggregator. We recommend that you do not use this method. |
| void | setMetric(String metric) Specifies a metric. We recommend that you do not use this method. |
| void | setTags(Map<String,String> tags) Specifies tags. We recommend that you do not use this method. |
| void | setTimestamp(Long timestamp) Specifies a timestamp. We recommend that you do not use this method. |
| void | setValue(Number value) Specifies a value. We recommend that you do not use this method. |
| void | setVersion(Long version) Specifies the version of a time point. We recommend that you do not use this method. |

| String | toJSON() Converts the configuration to a JSON object. |
|---|---|

Methods inherited from the com.aliyun.hitsdb.client.value.JSONValue class appendJSON, parseObject, and toString Methods inherited from the java.lang.Object class clone, equals, finalize, getClass, hashCode, notify, notifyAll, and wait

**Constructor details**

**Method details**

```
public static Point.MetricBuilder metric(String metric)
```

set the metric Parameters: metric - metric Response: MetricBuilder get a builder

**getMetric**

```
public String getMetric()
```

**getTags**

```
public Map<String,String> getTags()
```

**getTimestamp**

```
public Long getTimestamp()
```

**getValue**

```
public Number getValue()
```

**getAggregator**

```
public String getAggregator()
```

**getGranularityType**

```
public Granularity getGranularityType()
```

**getGranularity**

```
public String getGranularity()
```

**setMetric**

```
public void setMetric(String metric)
```

**setTags**

| Qualifier and type | Method and description |
|---|---|

```
public void setTags(Map<String,String> tags)
```

**setTimestamp**

```
public void setTimestamp(Long timestamp)
```

**setValue**

```
public void setValue(Number value)
```

**setGranularity**

```
public void setGranularity(String granularity)
```

**setAggregator**

```
public void setAggregator(String aggregator)
```

**getVersion**

```
public Long getVersion()
```

**setVersion**

```
public void setVersion(Long version)
```

**toJSON**

```
public String toJSON()
```

Overwrite: toJSON specifier: JSONValue Parameters:

##### Point.MetricBuilder

**Class name: com.aliyun.hitsdb.client.value.request.Point.MetricBuilder**

java.lang.Object

```
public static class Point.MetricBuilder extends Object
```

Constructors MetricBuilder(String metric). The parameter is Metric.

| Point.MetricBuilder | aggregator(String aggregator) Specifies Aggregator parameters. |
|---|---|
| Point | build() Constructs a time point. |
| Point | build(boolean checkPoint) Constructs a time point. |
| Point.MetricBuilder | tag(Map<String,String> tags) Adds a group of tag key-value pairs. |
| Point.MetricBuilder | tag(String tagName,String value) Adds a group of tag key-value pairs. |
| Point.MetricBuilder | timestamp (DateDate) Specifies a timestamp. Unit: seconds or milliseconds. |
| Point.MetricBuilder | timestamp(long timestamp) Specifies a timestamp. Unit: seconds or milliseconds. |
| Point.MetricBuilder | value(Date date,Number value) Specifies the time and value of a time point. |
| Point.MetricBuilder | value(long timestamp,Number value) Specifies the value of a time point. |
| Point.MetricBuilder | value(Number value) Specifies the value of a time point. |
| Point.MetricBuilder | version(Long version) Specifies the value version of a time point. |

Methods inherited from the java.lang.Object class clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Constructor details**

```
public MetricBuilder() public MetricBuilder(String metric)
```

**Method details**

**tag**

```
public Point.MetricBuilder tag(String tagName, String value)
```

Adds a tag key-value pair. Parameters: tagName - the tag name alue - the tag value Response:

**tag**

```
public Point.MetricBuilder tag(Map<String,String> tags)
```

Adds a tag key-value pair. Parameters: tags - the tag key-value pairs in the map format Response:

**aggregator**

```
public Point.MetricBuilder aggregator(String aggregator)
```

Specifies the value of Aggregator. Parameters: aggregator - the Aggregator enum instance Response:

**timestamp**

```
public Point.MetricBuilder timestamp(long timestamp)
```

Specifies a timestamp. Unit: seconds or milliseconds. Parameters: timestamp - the timestamp Response:

**timestamp**

```
public Point.MetricBuilder timestamp(Date date)
```

Specifies a timestamp. Unit: seconds or milliseconds. Parameters: date - the time specified by the java.util.Date class Response: Specifies the value of a time point. Parameters: value - the value Response:

```
public Point.MetricBuilder value(long timestamp, Number value)
```

| Qualifier and type | Class and description |
|---|---|
| static class | Query.Builder |

Specifies the time and value of a time point. Parameters: timestamp - the timestamp. Unit: seconds or milliseconds. value - the value. The value can be of the following types: double, long, and int. Response:

```
public Point.MetricBuilder value(Date date, Number value)
```

Specifies the time and value of a time point. Parameters: timestamp - the time specified by the java.util.Date class value - the value. The value can be of the following types: double, long, and int. Response:

**granularity**

```
public Point.MetricBuilder granularity(Granularity granularity) public Point.MetricBuilder version(Long version)
```

Constructs a time point. Response: Constructs a time point.

##### Query

**Class name: com.aliyun.hitsdb.client.value.response.QueryResult**

java.lang.Object Nested classes

| Qualifier and type | Method and description |
|---|---|
| Boolean | getDelete() Specify whether to delete the queried data. |
| long | getEnd() Obtain the end time of the time range that is queried. |
| List<SubQuery> | getQueries() Obtain all subqueries. |
| long | getStart() Obtain the start time of the time range that is queried. |
| static Query.Builder | start(Date startDate) We recommend that you do not use this method. Specify the start time of the time range to be queried. |
| static Query.Builder | start(long startTime) We recommend that you do not use this method. Specify the start time of the time range to be queried. |
| static Query.Builder | timeRange(Date startDate, Date endDate) Specify the start time and end time of the time range to be queried and obtain the Query.Builder instance. |
| static Query.Builder | timeRange(long startTime, long endTime) Specify the start time and end time of the time range to be queried and obtain the Query.Builder instance. |

Methods inherited from the com.aliyun.hitsdb.client.value.JSONValue class: appendJSON, parseObject, toJSON, and toString Methods inherited from the java.lang.Object class: clone, equals, finalize, getClass, hashCode, notify, notifyAll, and wait

**Builder details**

**Method details**

**start**

```
public static Query.Builder start(long startTime)
```

Specify the start time of the time range to be queried. Parameters: startTime - The start timestamp. Response: Obtain the Query.Builder instance.

**start**

```
public static Query.Builder start(Date startDate)
```

Specify the start time of the time range to be queried. Parameters: startDate - start date Response:

**timeRange**

```
public static Query.Builder timeRange(Date startDate, Date endDate)
```

Specify the start time and end time. Parameters: startDate - The start time. endDate - The end time. Response:

**timeRange**

```
public static Query.Builder timeRange(long startTime, long endTime)
```

Specify the start time and end time. Parameters: startTime - The start timestamp. endTime - The end timestamp. Response:

**getStart**

```
public long getStart()
```

Obtain the start time of the time range that is queried.

**getEnd**

```
public long getEnd()
```

Obtain the end time of the time range that is queried. Obtain the setting that specifies whether to delete the queried data. This feature is unavailable.

**getQueries**

Obtain all subqueries.

##### Query.Builder

**Class name: com.aliyun.hitsdb.client.value.request.Query.Builder**

java.lang.Object com.aliyun.hitsdb.client.value.request.Query.Builder

| Qualifier and type | Method and description |
|---|---|
| Query | build() Build a query condition. |
| Query.Builder | delete() Delete the queried data. This feature is unavailable. Ignore this method. |
| Query.Builder | delete(boolean delete) Delete the queried data. This feature is unavailable. Ignore this method. |
| Query.Builder | end(long endTime) Specify the end time of the time range to be queried. |
| Query.Builder | sub(Collection<SubQuery> subQuerys) Add multiple subquery objects. |
| Query.Builder | sub(SubQuery… subQuerys) Add multiple subquery objects. |

```
public static class Query.Builder extends Object
```

Builders: Builder(long startTime) - Build an instance based on the start time. Builder(long startTime,long endTime) - Build an instance based on the start time and end time. Methods inherited from the java.lang.Object class: clone, equals, finalize, getClass, hashCode notify, notifyAll, toString, and wait

**Builder details**

```
public Builder(long startTime)
```

Build an instance based on the start time.

```
public Builder(long startTime, long endTime)
```

Build an instance based on the start time and end time.

**Method details**

**end**

Specify the end time of the time range to be queried.

**sub**

Add multiple subquery objects.

**sub**

| Qualifier and type | Class and description |
|---|---|
| static class | SubQuery.AggregatorBuilder: an intermediate class for the builder SubQuery.Builder. |
| static class | SubQuery.BuilderSubQuery: a builder class for instances. |
| static class | SubQuery.MetricBuilder: an intermediate class for the builder SubQuery.Builder. |

| Qualifier and type | Class and description |
|---|---|
| static SubQuery.AggregatorBuilder | aggregator(Aggregator aggregator) Specify an aggregator to obtain a SubQuery.AggregatorBuilder instance. |
| String | getAggregator() Obtain an aggregator. |
| Aggregator | getAggregatorType() Obtain the aggregator type. |
| String | getDownsample() Obtain the downsampling string. |

```
public Query.Builder sub(Collection<SubQuery> subQuerys)
```

Add multiple subquery objects. Delete the queried data. This feature is unavailable. Ignore this method. Delete the queried data. This feature is unavailable. Ignore this method. Build a query condition instance.

##### SubQuery

**Class name: com.aliyun.hitsdb.client.value.request.SubQuery**

java.lang.Object com.aliyun.hitsdb.client.value.request.SubQuery Nested classes

| List<Filter> | getFilters() Obtain all filter conditions. |
|---|---|
| String | getMetric() Obtain the name of a metric. |
| Boolean | getRate() Obtain the rate. |
| Map<String,String> | getTags() Obtain the key-value pairs of tags in the map format. |
| Boolean | isExplicitTags() Obtain the explicit value. |
| static SubQuery.MetricBuilder | metric(String metric) Create a SubQuery.MetricBuilder instance based on a Metric name. |
| static SubQuery.Builder | metric(String metric, Aggregator aggregator) |
| String | toJSON() Convert to a JSON string. |

Methods inherited from the java.lang.Object class: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Builder details**

**Method details**

```
public static SubQuery.Builder metric(String metric, Aggregator aggregator)
```

Obtain a SubQuery.Builder instance based on an aggregator.

```
public static SubQuery.MetricBuilder metric(String metric)
```

Obtain a SubQuery.Builder instance based on a metric name.

**aggregator**

```
public static SubQuery.AggregatorBuilder aggregator(Aggregator aggregator)
```

**getAggregatorType**

```
public Aggregator getAggregatorType()
```

**getAggregator**

```
public String getAggregator()
```

Obtain an aggregator.

| Qualifier and type | Method and description |
|---|---|
| SubQuery | build() Create a subquery. |
| SubQuery.Builder | downsample(String downsample) Set the downsampling string. |
| SubQuery.Builder | explicitTags() Enable explicitTags. |

**getMetric**

```
public String getMetric()
```

Obtain the name of a metric.

**getDownsample**

```
public String getDownsample()
```

Obtain the downsampling string.

**getRate**

```
public Boolean getRate()
```

Obtain the rate.

**getTags**

```
public Map<String,String> getTags()
```

Obtain the key-value pairs of tags in the map format.

**toJSON**

```
public String toJSON()
```

Convert to a JSON string.

**getFilters**

```
public List<Filter> getFilters()
```

Obtain all filter conditions.

##### SubQuery.Builder

**Class name: com.aliyun.hitsdb.client.value.request.SubQuery.Builder**

java.lang.Object com.aliyun.hitsdb.client.value.request.SubQuery.Builder

```
public static class SubQuery.Builder extends Object
```

Builder: Builder(String metric, Aggregator aggregator) creates a SubQuery.Builder instance based on a metric name and an aggregator type.

| SubQuery.Builder | explicitTags(boolean explicitTags) Set the status of explicitTags. |
|---|---|
| SubQuery.Builder | filter(Filter filter) Add a filter. |
| SubQuery.Builder | filter(FilterType type, String tagk, String filter) Add a filter. |
| SubQuery.Builder | filter(FilterType type, String tagk, String filter,Boolean groupBy) Add a filter. |
| SubQuery.Builder | rate() Specify whether to enable value differential on time. |
| SubQuery.Builder | rate(boolean rate) Specify whether to enable value differential on time. |
| SubQuery.Builder | tag(Map<String,String> tags) Adds a tag in the key-value format. |
| SubQuery.Builder | tag(String tagk, String tagv) Adds a tag in the key-value format. |

Methods inherited from the java.lang.Object class: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, and wait

**Builder details**

```
public Builder(String metric, Aggregator aggregator)
```

Create a SubQuery.Builder instance based on a metric name and an aggregate type.

**Method details**

**rate**

Specify whether to enable value differential on time. By default, value differential on time is disabled.

**filter**

```
public SubQuery.Builder filter(FilterType type,String tagk, String filter,Boolean groupBy)
```

Add a filter condition. The Filter and Tags fields are mutually exclusive. Parameters: type - FilterType enumeration. This parameter indicates the type of filter. tagk - the tag key. filter - the tag values to be filtered. groupBy - Set to false to aggregate. Set to false to not aggregate. Returned result:

**filter**

Add a filter condition. The Filter and Tags fields are mutually exclusive. Parameters: filter - a Filter instance. Returned result:

**filter**

```
public SubQuery.Builder filter(FilterType type,String tagk,String filter)
```

Add a filter condition. The Filter and Tags fields are mutually exclusive. Parameters: type - FilterType enumeration. This parameter indicates the type of filter. tagk - the tag key. filter - the tag values to be filtered. Returned result:

**rate**

Set the status of the query rate. Parameters: rate - a boolean value. Set to true to calculate the value differential on time. Set to false to not calculate the value differential on time. Default value: false. Returned result:

```
public SubQuery.Builder downsample(String downsample)
```

Set the downsampling string. Parameters: downsample - the downsampling string. Returned result:

**tag**

```
public SubQuery.Builder tag(String tagk,String tagv)
```

Adds a tag in the key-value format. Parameters: tagk - the tag key. tagv - the tag value. Returned result:

**tag**

```
public SubQuery.Builder tag(Map<String,String> tags)
```

| Qualifier and type | Method and description |
|---|---|
| List<String> | getAggregateTags() Obtain the aggregated tags. |
| LinkedHashMap<Long,Number> | getDps() Obtain the query result. |
| String | getMetric() Obtain the name of a metric. |
| Map<String,String> | getTags() Obtain the queried tags. |
| void | setAggregateTags(List<String> aggregateTags) |
| void | setDps(LinkedHashMap<Long,Number> dps) |
| void | setMetric(String metric) |

Add multiple tags in the key-value format. Parameters: tags - the key-value pairs of the tags in the map format. Returned result:

**explicitTags**

Enable explicitTags. That is, set the value of explicitTags to true.

**explicitTags**

```
public SubQuery.Builder explicitTags(boolean explicitTags)
```

Set the status of explicitTags. Create a SubQuery instance.

##### QueryResult

**Class name: com.aliyun.hitsdb.client.value.response.QueryResult**

java.lang.Object com.aliyun.hitsdb.client.value.response.QueryResult Builders Builders and description QueryResult(): a query result class.

| void | setTags(Map<String,String> tags) |
|---|---|

Methods inherited from the com.aliyun.hitsdb.client.value.JSONValue class: appendJSON, parseObject, toJSON, and toString Methods inherited from the java.lang.Object class: clone, equals, finalize, getClass, hashCode, notify, notifyAll, and wait

**Builder details**

**Method details**

**getAggregateTags**

```
public List<String> getAggregateTags()
```

**setAggregateTags**

```
public void setAggregateTags(List<String> aggregateTags)
```

**getDps**

```
public LinkedHashMap<Long,Number> getDps()
```

**getMetric**

```
public String getMetric()
```

**getTags**

```
public Map<String,String> getTags()
```

**setDps**

```
public void setDps(LinkedHashMap<Long,Number> dps)
```

**setMetric**

```
public void setMetric(String metric)
```

**setTags**

```
public void setTags(Map<String,String> tags)
```

#### SDK examples

##### Use the LindormTSDB SDK to write multi-value

**data**

This topic describes how to use the multi-value model to write data and provides sample code.

**Note**

Only LindormTSDB SDK V0.2.0 and later support the multi-value model. For more information about the latest SDK version and download link, see Release notes.

**Use the multi-value model to write data**

**Sample code:**

`/*`

```
 * Use the multiFieldPutSync() API.
 * This API supports single-data-point or multi-data-point (LIST) writes.
```

*

```
 * The following information is required when you write data:
 * Metric: the category of a metric. Metrics are similar to InfluxDB measurements.
 * Fields: the measurement information of a metric. Each field specifies a sub-category of a metric
. A metric can contain multiple fields. For example, a metric is named wind. This metric contains t he following fields: direction, speed, direction, description, and temperature.
 * Timestamp: the timestamp of a data point.
 * Tags: the additional information of a timeline, for example, a model of ABC123 and a manufacture
r part number of 1234567890.
```

`*/`

```
MultiFieldPoint multiValuedPoint = MultiFieldPoint.metric("wind").timestamp(1346846400L)
        .fields("speed", 20.0)
        .fields("level", 5)
        .fields("direction", "NE")
        .fields("description", "Breeze")
        .fields("temperature", "18.9")
        .tag("sensor", "IOTE_1988_0001")
        .tag("district", "Yuhang")
        .tag("city", "Hangzhou")
        .tag("province", "Zhejiang")
        .build();
// Synchronously write data. tsdb.multiFieldPutSync(multiValuedPoint); // Synchronously write data and return the result (successful or failed). tsdb.multiFieldPutSync(multiValuedPoint, SummaryResult.class); // Synchronously write data and obtain the detailed information about result. tsdb.multiFieldPutSync(multiValuedPoint, DetailsResult.class);
```

**Use the multi-value model to asynchronously write data**

**Note**

Only LindormTSDB SDK V0.2.1 and later support the multi-value model. For more information about the latest SDK version and download link, see Release notes.

**Do not use a callback method**

By default, no callback method is specified in the TSDBConfig class to perform asynchronous multi-value writes. **Sample code**:

```
TSDBConfig config = TSDBConfig.address("127.0.0.1", 8242)
        // The volume of data that is written in each batch.
        .batchPutSize(500)
        // The number of threads that are used to process asynchronous single-value writes.
        .batchPutConsumerThreadCount(1)
        // The length of the queue for asynchronous multi-value writes.
        .multiFieldBatchPutBufferSize(10000)
        // The number of threads that are used to process asynchronous multi-value writes.
        .multiFieldBatchPutConsumerThreadCount(1)
        .config();
// Take note that you need to initialize a TSDB instance only once. TSDB tsdb = TSDBClientFactory.connect(config);
        .metric("test-test-test")
        .tag("a", "1")
        .tag("b", "2")
        .timestamp(System.currentTimeMillis())
        .field("f1", Math.random())
        .field("f2", Math.random())
        .build();
tsdb.multiFieldPut(point); // Take note that you do not need to shut down the specified TSDB instance within the lifecycle of an application unless the application is terminated. tsdb.close();
```

**Use a common callback method**

A common callback method returns the data points of a successful write operation, or the data points of a failed write operation, and the relevant write exceptions.

**Sample code:**

```java
// Creates a common callback method to process successful or failed writes. AbstractMultiFieldBatchPutCallback callback = new MultiFieldBatchPutCallback() {
    @Override
    public void response(String address, List<MultiFieldPoint> points, Result result) {
        int count = num.addAndGet(points.size());
        System.out.println(result);
        System.out.println("Processed" + count + "data points");
    }
    final AtomicInteger num = new AtomicInteger();
    @Override
    public void failed(String address, List<MultiFieldPoint> points, Exception ex) {
        System.err.println("The callback failed." + points.size() + " error!");
        ex.printStackTrace();
    }
}; TSDBConfig config = TSDBConfig.address("127.0.0.1", 8242)
        .httpConnectTimeout(90)
        // The volume of data that is written in each batch.
        .batchPutSize(500)
        // The number of threads that are used to process asynchronous single-value writes.
        .batchPutConsumerThreadCount(1)
        // The length of the queue for asynchronous multi-value writes.
        .multiFieldBatchPutBufferSize(10000)
        // The number of threads that are used to process asynchronous multi-value writes.
        .multiFieldBatchPutConsumerThreadCount(1)
        // The callback method that is used to obtain the results of asynchronous multi-value write
```

`s.`

```
        .listenMultiFieldBatchPut(callback)
        .config();
// Take note that you need to initialize a TSDB instance only once. TSDB tsdb = TSDBClientFactory.connect(config);
        .metric("test-test-test")
        .tag("a", "1")
        .tag("b", "2")
        .timestamp(System.currentTimeMillis())
        .field("f1", Math.random())
        .field("f2", Math.random())
        .build();
tsdb.multiFieldPut(point); // Take note that you do not need to shut down the specified TSDB instance within the lifecycle of an application unless the application is terminated. tsdb.close();
```

**Use a summary callback method**

If a write operation succeeds, the summary callback method returns the data points of the write operation and the relevant summarized information. The information includes the number of successful data points and the number of failed data points. If a write operation fails, the summary callback method returns the data points of the write operation and the relevant write exceptions.
**Sample code**:

```java
// Creates a summary callback method to process successful writes or failed writes. AbstractMultiFieldBatchPutCallback callback = new MultiFieldBatchPutSummaryCallback() {
    final AtomicInteger num = new AtomicInteger();
    @Override
    public void response(String address, List<MultiFieldPoint> points, SummaryResult result) {
        int count = num.addAndGet(points.size());
        System.out.println(result);
        System.out.println("Processed" + count + "data points");
    }
    @Override
    public void failed(String address, List<MultiFieldPoint> points, Exception ex) {
        System.err.println("The callback failed." + points.size() + " error!");
        ex.printStackTrace();
    }
}; TSDBConfig config = TSDBConfig.address("127.0.0.1", 8242)
        .httpConnectTimeout(90)
        // The volume of data that is written in each batch.
        .batchPutSize(500)
        // The number of threads that are used to process asynchronous single-value writes.
        .batchPutConsumerThreadCount(1)
        // The length of the queue for asynchronous multi-value writes.
        .multiFieldBatchPutBufferSize(10000)
        // The number of threads that are used to process asynchronous multi-value writes.
        .multiFieldBatchPutConsumerThreadCount(1)
        // The callback method that is used to obtain the results of asynchronous multi-value write
```

`s.`

```
        .listenMultiFieldBatchPut(callback)
        .config();
// Take note that you need to initialize a TSDB instance only once. TSDB tsdb = TSDBClientFactory.connect(config);
        .metric("test-test-test")
        .tag("a", "1")
        .tag("b", "2")
        .timestamp(System.currentTimeMillis())
        .field("f1", Math.random())
        .field("f2", Math.random())
        .build();
tsdb.multiFieldPut(point); // Take note that you do not need to shut down the specified TSDB instance within the lifecycle of an application unless the application is terminated. tsdb.close();
```

**Use a details callback method**

If a write operation succeeds, the details callback method returns the data points and details of the write operation. The details include the failed data points and the relevant errors. If a write operation fails, the details callback method returns the data points of the write operation and the relevant write exceptions.
**Sample code**:

```java
// Creates a details callback method to process successful writes or failed writes. MultiFieldBatchPutDetailsCallback callback = new MultiFieldBatchPutDetailsCallback() {
    final AtomicInteger num = new AtomicInteger();
    @Override
    public void response(String address, List<MultiFieldPoint> points, DetailsResult result) {
        int count = num.addAndGet(points.size());
        System.out.println(result);
        System.out.println("Processed" + count + "data points");
    }
    @Override
    public void failed(String address, List<MultiFieldPoint> points, Exception ex) {
        System.err.println("The callback failed." + points.size() + " error!");
        ex.printStackTrace();
    }
}; TSDBConfig config = TSDBConfig.address("127.0.0.1", 8242)
        .httpConnectTimeout(90)
        // The volume of data that is written in each batch.
        .batchPutSize(500)
        // The number of threads that are used to process asynchronous single-value writes.
        .batchPutConsumerThreadCount(1)
        // The length of the queue for asynchronous multi-value writes.
        .multiFieldBatchPutBufferSize(10000)
        // The number of threads that are used to process asynchronous multi-value writes.
        .multiFieldBatchPutConsumerThreadCount(1)
        // The callback method that is used to obtain the results of asynchronous multi-value write
```

`s.`

```
        .listenMultiFieldBatchPut(callback)
        .config();
// Take note that you need to initialize a TSDB instance only once. TSDB tsdb = TSDBClientFactory.connect(config);
        .metric("test-test-test")
        .tag("a", "1")
        .tag("b", "2")
        .timestamp(System.currentTimeMillis())
        .field("f1", Math.random())
        .field("f2", Math.random())
        .build();
tsdb.multiFieldPut(point); // Take note that you do not need to shut down the specified TSDB instance within the lifecycle of an application unless the application is terminated. tsdb.close();
```

##### Use the LindormTSDB SDK to perform a multi-

**value query**

This topic describes how to create a multi-value data model to perform multi-value queries. Sample code: `/*`

```
 *  Call the multiFieldQuery() API operation.
 *  Procedure for creating a request: MultiFieldSubQueryDetails List -> MultiFieldSubQuery -> Multi
 *  A multi-value query can contain multiple subqueries.
```

*

```
 *  You must specify the following information when you perform a multi-value query:
 *  MultiFieldSubQueryDetails List: queries the measurement values of a metric. For example, query
only the "speed" or "direction".
 *                                  You can specify aggregate operators such as Aggregator, dpValue,
rate, or downsample.
 *  Metric: the data metric that is queried, such as "wind".
 *  Time Range: Start Time and End Time
```

*

```
 *  Optional information:
 *  Tags: used to filter information by time.
 *  Limit/Offset: enable pagination.
```

`*/`

```
 // Specify the fields to be queried.
 MultiFieldSubQueryDetails speedFieldDetails = MultiFieldSubQueryDetails
     .field("speed").aggregator(Aggregator.SUM).downsample("2s-sum").build();
 MultiFieldSubQueryDetails levelFieldDetails = MultiFieldSubQueryDetails
     .field("level").aggregator(Aggregator.AVG).downsample("2s-avg").build();
 MultiFieldSubQueryDetails tempFieldDetails = MultiFieldSubQueryDetails
     .field("temperature").aggregator(Aggregator.COUNT).downsample("2s-count").build();
 MultiFieldSubQueryDetails allFieldsDetails1 = MultiFieldSubQueryDetails
     .field("*").aggregator(Aggregator.MAX).downsample("2s-max").alias("max_").build();
 MultiFieldSubQueryDetails allFieldsDetails2 = MultiFieldSubQueryDetails
     .field("*").aggregator(Aggregator.MIN).downsample("2s-min").alias("min_").build();
 List<MultiFieldSubQueryDetails> subQueryDetails = new LinkedList<>();
 subQueryDetails.add(speedFieldDetails);
 subQueryDetails.add(levelFieldDetails);
 subQueryDetails.add(tempFieldDetails);
 subQueryDetails.add(allFieldsDetails1);
 subQueryDetails.add(allFieldsDetails2);
 // Create a multi-value subquery.
 MultiFieldSubQuery subQuery = MultiFieldSubQuery.metric(metric).fieldsInfo(subQueryDetails)
     .filter(Filter.filter(FilterType.LiteralOr, "district", "Yuhang|Xiacheng|Xihu", true).build())
     .build();
 // Create a multi-value query.
 MultiFieldQuery query = MultiFieldQuery.start(1542772000L).end(1542772020L).msResolution(false)
     .sub(subQuery).build();
 List<MultiFieldQueryResult> results = tsdb.multiFieldQuery(query);
```

##### Use the LindormTSDB SDK to query the latest

**multi-value data**

Sample code:

| Exception | Description |
|---|---|
| HttpClientException | The client encounters an exception. |
| HttpClientConnectionRefusedException | The LindormTSDB server rejects the connection. |
| HttpClientInitException | The client encounters an initialization exception. |
| HttpClientConnectionRefusedException | The LindormTSDB server rejects the connection. |
| HttpClientSocketTimeoutException | The request timed out. |
| HttpServerErrorException | A 5xx error code is returned by the LindormTSDB server. |
| HttpServerNotSupportException | A 4xx error code is returned by the LindormTSDB server. |
| HttpUnknowStatusException | The response code returned by the LindormTSDB server is unknown. |
| BufferQueueFullException | The queue for asynchronous operations is full. |

`/*`

```
* The multiFieldQueryLast() API.
* The query method is similar to that of the single-value model. You must provide fields when you c
reate a LastPointSubQuery.
* Information that must be provided when you query the latest multi-value data:
* Metric: the metric that is queried, for example, "metric":"wind".
* Fields: the fields (sub-categories) that are queried, such as "speed", "level", and "temperature"
```

. `*/`

```
List<String> fields = new ArrayList<>(); fields.add("speed"); fields.add("level"); fields.add("temperature"); LastPointSubQuery lastPointSubQuery = LastPointSubQuery.builder("wind", fields, Collections.emptyMap()).build(); // No tag filter is added. LastPointQuery.builder().sub(lastPointSubQuery).tupleFormat(true).msResolution(false).build(); List<MultiFieldQueryLastResult> results = tsdb.multiFieldQueryLast(lastPointQuery);
```

#### Handle exceptions

The LindormTSDB SDK does not forcefully handle exceptions. All exceptions are thrown as RuntimeExceptions. You can capture and handle these exceptions based on your business requirements.

**Common exceptions**

Handle exceptions that occur when synchronous operations are performed:

| Release | Description | SDK download link |
|---|---|---|
| 0.2.7 | User authentication information can be configured by using the user authentication feature of LindormTSDB. | hitsdb-client-0.2.7.jar |

```
try {
    tsdb.ttl(10000);
} catch(HttpServerNotSupportException e) {
    int status = e.getStatus();
    String message = e.getMessage();
    System.err.println(status + "," + message);
} catch(HttpServerErrorException e) {
    int status = e.getStatus();
    String message = e.getMessage();
    System.err.println(status + "," + message);
}
```

Handle exceptions that occur when asynchronous operations are performed: Override the failed() method to handle an exception.

```java
    @Override
    public void response(Query input, List<QueryResult> result) {
        System.out.println("Query parameters:" + input);
        System.out.println("Returned result:" + result);
    // Override the failed() method to handle an exception.
    @Override
        super.failed(request, ex);
    }
}; BatchPutCallback cb = new BatchPutCallback() {
    @Override
    public void response(List<Point> input, Result output) {
        long afterNum = num.addAndGet(input.size());
        System.out.println("Successful" + input.size() + ", Processed" + afterNum);
    }
    @Override
    public void failed(List<Point> input, Exception ex) {
        ex.printStackTrace();
        long afterNum = num.addAndGet(input.size());
        System.out.println("Failed" + input.size() + ", Processed" + afterNum);
    }
};
```

#### Release notes

| 0.2.6 | The dependency on Guava is removed. The delta operator is supported for subqueries. The delta operator is used to calculate the difference between the values of two single-value data points. | hitsdb-client-0.2.6.jar |
|---|---|---|
| 0.2.5 | Whether to recursively delete time series can be specified. Multi-value time series can be deleted. | hitsdb-client-0.2.5.jar |
| 0.2.4 | The circular reference issue during JSON serialization when you configure the LastPointQuery object is fixed. | hitsdb-client-0.2.4.jar |
| 0.2.3 | The issue that filters cannot be configured when you configure the MultiFieldSubQuery object is fixed. The preDpValue operator is supported. The preDpValue operator is used to filter data points before queries are performed. | hitsdb-client-0.2.3.jar |
| 0.2.2 | SQL queries can be submitted. | hitsdb-client-0.2.2.jar |
| 0.2.1 | Asynchronous writes are supported by the multi-value model. | hitsdb-client-0.2.1.jar |
| 0.2.0 | The API operations related to the multi-value model are provided. | hitsdb-client-0.2.0.jar |
