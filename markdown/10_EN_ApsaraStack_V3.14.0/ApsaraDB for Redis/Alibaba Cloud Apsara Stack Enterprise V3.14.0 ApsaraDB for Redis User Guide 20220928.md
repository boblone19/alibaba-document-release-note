---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 58
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20for%20Redis%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis User Guide 20220928

## Table of Contents

- 1 What is KVStore for Redis?
- 2 Quick Start
  - 2.1 Get started with KVStore for Redis
  - 2.2 Log on to the KVStore for Redis console
  - 2.3 Create a KVStore for Redis instance
  - 2.4 Configure a whitelist
  - 2.5 Connect to an instance
    - 2.5.1 Use a Redis client
    - 2.5.2 Use redis-cli
- 3 Instance management
  - 3.1 Change a password
  - 3.2 Configure a whitelist
  - 3.3 Change specifications
  - 3.4 Specify a maintenance window
  - 3.5 Upgrade the minor version
  - 3.6 Configure SSL encryption
  - 3.7 Clear data
  - 3.8 Release an instance
  - 3.9 Manage database accounts
  - 3.10 Restart an instance
  - 3.11 Export the list of instances
  - 3.12 Use a Lua script
- 4 Connection management
  - 4.1 View endpoints
  - 4.2 Apply for a public endpoint
  - 4.3 Modify the endpoint of an KVStore for Redis instance
- 5 Performance monitoring
  - 5.1 Query monitoring data
  - 5.2 Select metrics
  - 5.3 Modify the data collection interval
  - 5.4 Understand metrics
- 6 Parameter configuration
- 7 Backup and recovery
  - 7.1 Automatically back up data
  - 7.2 Back up an instance
  - 7.3 Download backup files
  - 7.4 Restore data
  - 7.5 Clone an instance
- 8 CloudDBA
  - 8.1 Performance trends
  - 8.2 Add a performance trend chart
  - 8.3 View performance metrics in real time
  - 8.4 Instance sessions
  - 8.5 Slow queries

s?

## 1 What is KVStore for Redis?

KVStore for Redis is a database service that is compatible with Redis-native protocols. KVStore for Redis provides a highly available hot standby architecture and can scale to meet the requirements of high-performance and low-latency read/write operations. Features KVStore for Redis supports various data types, such as strings, lists, sets, sorted sets, hash tables, and streams. This service also supports advanced features, such as transactions, message subscription, and message publishing. KVStore for Redis Enhanced Edition (Tair), which is a key-value pair cloud caching service, is an advanced version of KVStore for Redis Community Edition. Instance type

| Instance type | Overview |
|---|---|
| Community Edition | KVStore for Redis Community Edition is compatible with the data caching service of Redis-native engines. This service supports master-replica instances and cluster instances. |
| Performance- enhanced instances of KVStore for Redis Enhanced Edition (Tair) | KVStore for Redis Enhanced Edition (Tair) provides a multi-threading model and integrates some features of Alibaba Tair. KVStore for Redis Enhanced Edition (Tair) supports multiple data structures of Tair and is suitable for diverse scenarios. |

## 2 Quick Start

### 2.1 Get started with KVStore for Redis

This topic describes all operations that you can perform on an instance from instance creation to database logon. This topic helps you understand how to create and manage an instance. The following figure shows how to manage a KVStore for Redis instance. This topic describes how to log on to the KVStore for Redis console. Create an instance KVStore for Redis supports classic networks and virtual private clouds (VPCs). You can create KVStore for Redis instances in these networks. Before you use a KVStore for Redis instance, add IP addresses or CIDR blocks that are used to access the database to the whitelist of the instance to improve the security and stability of the database. If you do not specify a password when you create the instance, specify a password on the Inst ance Inf ormat ion page. Connect to a KVStore for Redis instance To connect to the KVStore for Redis instance, you can use a client that supports Redis protocols or use the Redis command-line interface (redis-cli) tool.

### 2.2 Log on to the KVStore for Redis console

console This topic describes how to log on to the KVStore for Redis console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click Login.
4. In the top navigation bar, choose Product s > KVSt ore f or Redis.

### 2.3 Create a KVStore for Redis instance

instance This topic describes how to create a KVStore for Redis instance in the KVStore for Redis console. Procedure
1. Log on to the KVStore for Redis console.
2. Click Creat e Inst ance in the upper-right corner of the page.
3. Set the following parameters.
KVStore for Redis instance parameters

| Section | Parameter | Description |
|---|---|---|
| Basic Set t ings | Organizat ion | Select the organization to which the KVStore for Redis instance that you want to create belongs. |
|   | Resource Set | Select the resource set to which the instance belongs. Not ice After you select a resource set, the instance is accessible only to the members of the specified resource set. |
| Region | Region | Select the region to which the instance belongs. |
|   | Zone | Select the zone to which the instance belongs. |
| Specif icat ions | Engine Version | Select the engine version of the KVStore for Redis instance that you want to create. |
|   | Archit ect ure T ype | Select the architecture type of the instance. KVStore for Redis provides cluster and standard architectures. The cluster architecture is applicable to scenarios that require a large capacity or high performance. Redis-native databases run in a single- threading model. If your database does not require high performance, we recommend that you use a standard instance. If your database requires high performance, select a cluster architecture. |
|   | Node T ype | Mast er-replica is automatically selected. The node type has one master node and one replica node. |
|   | Inst ance T ype | Select the specification of the instance. The maximum number of connections and maximum internal bandwidth vary based on the instance specification. For more information, see Insta nce specifications in Product Introduction. |
| Net work | Net work T ype | Classic network: Cloud services in a classic network are not isolated. Unauthorized access to a cloud service is blocked by security groups or the service whitelist. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize the route table, CIDR block, and gateway of a VPC. You can also migrate applications to the cloud without service interruption. You can use an Express Connect circuit or VPN to connect data centers to cloud resources in a VPC. Not e Before you can select VPC, you must create a VPC. For more information, see Create a VPC and Create a vSwitch in VPC Us er Guide. |

| Section | Parameter | Description |
|---|---|---|
| Password | Inst ance Name | Enter a name that can help you identify the instance. The name must be 2 to 128 characters in length. The name can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter. |
|   | Password Set t ing | You can select Set Now or Set af t er Purchase. |
|   | Logon Password | Enter a password to access the instance. The password must meet the following requirements: The password must be 8 to 30 characters in length. The password must contain uppercase letters, lowercase letters, and digits. The password must not contain special characters. |
|   | Conf irm Password | Enter the specified password again. |

4. After you configure the parameters, click Submit .

### 2.4 Configure a whitelist

Before you use a KVStore for Redis instance, add IP addresses or CIDR blocks that are used to access the database to the whitelist of the instance to improve the security and stability of the database. Context

> Not e A properly configured whitelist can ensure a higher level of security protection for your KVStore for Redis instance. We recommend that you maintain the whitelist on a regular basis.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Whit elist Set t ings.
4. Find the IP address whitelist that you want to manage and click Modif y.

> Not e You can also click Add Whit elist to create an IP address whitelist. The name of the IP address whitelist must be 2 to 32 characters in length and can contain lowercase letters, digits, and underscores (_). The name of the whitelist must start with a lowercase letter and end with a lowercase letter or digit.

5. In the dialog box that appears, perform one of the following operations:

| Action | Procedure |
|---|---|
| Manually modify the IP address whitelist | Enter IP addresses or CIDR blocks. Manually modify the IP address whitelist Not e Separate multiple IP addresses with commas (,). You can add up to 1,000 unique IP addresses. Supported formats are specific IP addresses such as 10.23.12.24 and CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. An IP address prefix can be 1 to 32 bits in length. If you set the prefix length to 0, for example, 0.0.0.0/0 or 127.0.0.1/0, all IP addresses are allowed to access the instance. In this case, the security risk of your instance is high. Proceed with caution. |
| Add private IP addresses of ECS instances to an IP address whitelist | i. Click Load ECS Int ernal Net work IP. ii. Select IP addresses based on your business requirements. Add private IP addresses of ECS instances Not e To find the ECS instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |

| Action | Procedure |
|---|---|
| Remove IP addresses from the IP address whitelist | To remove all IP addresses from the IP address whitelist and retain the IP address whitelist, click Delet e. |

6. Then, click OK.

### 2.5 Connect to an instance

#### 2.5.1 Use a Redis client

KVStore for Redis is compatible with open source Redis. You can connect to KVStore for Redis and open source Redis in a similar manner. Therefore, you can use a client that is compatible with the Redis protocols to connect to KVStore for Redis. You can connect to a KVStore for Redis instance by using clients of different programming languages. Prerequisites The private IP address of an Elastic Compute Service (ECS) instance or the public IP address of an onpremises machine is added to a whitelist of the instance. For more information, see Configure a whitelist. Obtain connection information When you use a client to connect to a KVStore for Redis instance, you must obtain the following information and specify the information in the code:

| Information | Description |
|---|---|
| Endpoint | You can find the endpoint in the Connect ion Inf ormat ion section on the Inst ance Inf ormat ion page. Not e KVStore for Redis instances support multiple types of endpoints. We recommend that you use endpoints in a VPC for higher security and lower network latency. |
| Port number | The default port number is 6379. |
| The account of the instance. This parameter is not required by some clients. | By default, a KVStore for Redis instance provides a database account that is named after the instance ID, such as, r-bp10noxlhcoim2****. |
| The password of the account. | If you forget your password, you can reset the password. For more information, see Change the password. |

Commonly used clients For the list of clients supported by Redis, see Redis clients. Jedis client PhpRedis client Redis-py client C or C++ client .NET client Node-redis client C# client StackExchange.Redis Jedis client
1. Download and install the Jedis client. For more information, see Jedis.
2. Select a connection method to meet your business requirements.
JedisPool-based connection: This connection method is recommended. a. Launch the Eclipse client, create a project, and then configure the following pom file:

```xml
<dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> <version>2.7.2</version> <type>jar</type> <scope>compile</scope> </dependency>
```

b. Enter the following code in the project to add the relevant applications:

```java
import org.apache.commons.pool2.PooledObject; import org.apache.commons.pool2.PooledObjectFactory; import org.apache.commons.pool2.impl.DefaultPooledObject; import org.apache.commons.pool2.impl.GenericObjectPoolConfig; import redis.clients.jedis.HostAndPort; import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig;
```

c. Enter the following code in the project based on the Jedis client version and modify the code based on the comments.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

Jedis 2.7.2

```
JedisPoolConfig config = new JedisPoolConfig(); //Maximum number of idle connections. You can configure this parameter. Make su re that the specified value does not exceed the maximum number of connections t hat the KVStore for Redis instance supports. config.setMaxIdle(200); //Maximum number of connections. You can configure this parameter. Make sure th at the specified value does not exceed the maximum number of connections that t he KVStore for Redis instance supports. config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "Password"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); /// ... do stuff here ... for example jedis.set("foo", "bar"); String foobar = jedis.get("foo"); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); Set<String> sose = jedis.zrange("sose", 0, -1); } finally { if (jedis != null) { jedis.close();
```

`}` `}`

```
/// ... when closing your application: pool.destroy();
```

Jedis 2.6 or Jedis 2.5

```
JedisPoolConfig config = new JedisPoolConfig(); //Maximum number of idle connections. You can configure this parameter. Make su re that the specified value does not exceed the maximum number of connections t hat the KVStore for Redis instance supports. config.setMaxIdle(200); //Maximum number of connections. You can configure this parameter. Make sure th at the specified value does not exceed the maximum number of connections that t he KVStore for Redis instance supports. config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "Password"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; boolean broken = false; try {
     jedis = pool.getResource();
     /// ... do stuff here ... for example
     jedis.set("foo", "bar");
     String foobar = jedis.get("foo");
     jedis.zadd("sose", 0, "car");
     jedis.zadd("sose", 0, "bike");
     Set<String> sose = jedis.zrange("sose", 0, -1);
```

`}`

```
catch(Exception e)
```

`{`

```
     broken = true;
} finally { if (broken) {
     pool.returnBrokenResource(jedis);
} else if (jedis != null) {
     pool.returnResource(jedis);
```

`}` `}` Single Jedis connection: This connection method does not allow a client to automatically reconnect to the KVStore for Redis instance after a connection times out. Therefore, this connection is not recommended. Launch the Eclipse client, create a project, enter the following code, and then modify the code based on the comments.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

```java
import redis.clients.jedis.Jedis; public class jedistest { public static void main(String[] args) { try {
     String host = "xx.kvstore.aliyuncs.com";//You can find the connection address in
the console.
     int port = 6379;
     Jedis jedis = new Jedis(host, port);
     //Authentication information.
     jedis.auth("password");//password
     String key = "redis";
     String value = "aliyun-redis";
     //Select a database. Default value: 0.
     jedis.select(1);
     //Specify a key.
     jedis.set(key, value);
     System.out.println("Set Key " + key + " Value: " + value);
     //Obtain the configured key and value.
     String getvalue = jedis.get(key);
     System.out.println("Get Key " + key + " ReturnValue: " + getvalue);
     jedis.quit();
     jedis.close();
```

`}`

```
catch (Exception e) {
 e.printStackTrace();
```

`}` `}` `}`
3. Run the project. If Eclipse returns the following result, it indicates that the client is connected to
the KVStore for Redis instance.

```
Set Key redis Value aliyun-redis Get Key redis ReturnValue aliyun-redis
```

PhpRedis client
1. Download and install the PhpRedis client. For more information, see PhpRedis.
2. Enter the following code in a PHP editor and modify the code based on the comments.

> Not e For more information about how to obtain the connection address, account, and password of the KVStore for Redis instance, see Obtain connection information.

```
<?php
 /* Replace the parameter values with the endpoint and port number of the instance. */
 $host = "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com";
 $port = 6379;
 /* Replace the following parameter values with the ID and password of the instance. */
 $user = "test_username";
 $pwd = "test_password";
 $redis = new Redis();
 if ($redis->connect($host, $port) == false) {
         die($redis->getLastError());
```

`}`

```
 if ($redis->auth($pwd) == false) {
         die($redis->getLastError());
```

`}`

```
  /* You can manage the database after you pass the authentication. For more informatio
n, visit https://github.com/phpRedis/phpredis. */
 if ($redis->set("foo", "bar") == false) {
         die($redis->getLastError());
```

`}`

```
 $value = $redis->get("foo");
 echo $value;
```

?>
3. Run the preceding code to connect to the instance.
For more information, see PhpRedis. Redis-py client
1. Download and install the redis-py client. For more information, see redis-py.
2. Enter the following code in a Python editor and modify the code based on the comments.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

```java
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import redis
#Replace the value of the host parameter with the endpoint of the instance and replace
the value of the port parameter with the port number. host = 'localhost' port = 6379
#Replace the following parameter value with the password of the instance.
pwd = 'test_password' r = redis.StrictRedis(host=host, port=port, password=pwd)
#You can perform database operations after you establish a connection. For more informa
tion, visit https://github.com/andymccurdy/redis-py. r.set('foo', 'bar'); print r.get('foo')
```

3. Run the preceding code to connect to the instance.
C or C++ client
1. Run the following commands to download, compile, and install the C client:

```python
git clone https://github.com/redis/hiredis.git cd hiredis make sudo make install
```

2. Enter the following code in a C or C ++ editor and modify the code based on the comments.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <hiredis.h>
int main(int argc, char **argv) { unsigned int j; redisContext *c; redisReply *reply; if (argc < 4) {
        printf("Usage: example xxx.kvstore.aliyuncs.com 6379 instance_id password\n");
        exit(0);
```

`}`

```
const char *hostname = argv[1]; const int port = atoi(argv[2]); const char *instance_id = argv[3]; const char *password = argv[4]; struct timeval timeout = { 1, 500000 }; // 1.5 seconds c = redisConnectWithTimeout(hostname, port, timeout); if (c == NULL || c->err) { if (c) {
        printf("Connection error: %s\n", c->errstr);
        redisFree(c);
} else {
        printf("Connection error: can't allocate redis context\n");
```

`}`

```
exit(1);
```

`}`

```
/* AUTH */ reply = redisCommand(c, "AUTH %s", password); printf("AUTH: %s\n", reply->str); freeReplyObject(reply); /* PING server */ reply = redisCommand(c,"PING"); printf("PING: %s\n", reply->str); freeReplyObject(reply); /* Set a key */ reply = redisCommand(c,"SET %s %s", "foo", "hello world"); printf("SET: %s\n", reply->str); freeReplyObject(reply); /* Set a key using binary safe API */ reply = redisCommand(c,"SET %b %b", "bar", (size_t) 3, "hello", (size_t) 5); printf("SET (binary API): %s\n", reply->str);
```

`p`

```
t(S
```

`(b` `a``y`

```
):%s\
```

`,`

```
epy st); freeReplyObject(reply); /* Try a GET and two INCR */ reply = redisCommand(c,"GET foo"); printf("GET foo: %s\n", reply->str); freeReplyObject(reply); reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* again ... */ reply = redisCommand(c,"INCR counter"); printf("INCR counter: %lld\n", reply->integer); freeReplyObject(reply); /* Create a list of numbers, from 0 to 9 */ reply = redisCommand(c,"DEL mylist"); freeReplyObject(reply); for (j = 0; j < 10; j++) {
        char buf[64];
        snprintf(buf,64,"%d",j);
        reply = redisCommand(c,"LPUSH mylist element-%s", buf);
        freeReplyObject(reply);
```

`}`

```
/* Let's check what we have inside the list */ reply = redisCommand(c,"LRANGE mylist 0 -1"); if (reply->type == REDIS_REPLY_ARRAY) {
        for (j = 0; j < reply->elements; j++) {
        printf("%u) %s\n", j, reply->element[j]->str);
```

`}` `}`

```
freeReplyObject(reply); /* Disconnects and frees the context */ redisFree(c); return 0;
```

`}`
3. Compile the code.

```
gcc -o example -g example.c -I /usr/local/include/hiredis -lhiredis
```

4. Perform a test run and connect to the instance.

```
 example xxx.kvstore.aliyuncs.com 6379 instance_id password
```

.NET client

> **Warning:** If you need to switch or select a database from multiple databases in a cluster instance, you must set the cluster_compat_enable parameter to 0 and restart the client application. This disables the support for the cluster syntax of open source Redis. Otherwise, the system sends the following error message: `Multiple databases are not supported on this`
> server; cannot switch to database . For more information, see Parameter configuration.

1. Run the following command to download the .NET client.

```
 git clone https://github.com/ServiceStack/ServiceStack.Redis
```

2. Create a .NET project on the .NET client.
3. Add a reference. The reference file is stored in the library file directory ServiceStack.Redis/lib/tests.
4. Enter the following code in the .NET project and modify the code based on the comments. For
more information, see ServiceStack.Redis.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

```
using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using ServiceStack.Redis;
 namespace ServiceStack.Redis.Tests
```

`{`

```
         class Program
```

`{`

```
 public static void RedisClientTest()
```

`{`

```
         string host = "127.0.0.1";/*The endpoint of the host.*/
         string password = "password";/*The password*/
         RedisClient redisClient = new RedisClient(host, 6379, password);
         string key = "test-aliyun";
         string value = "test-aliyun-value";
         redisClient.Set(key, value);
         string listKey = "test-aliyun-list";
         System.Console.WriteLine("set key " + key + " value " + value);
         string getValue = System.Text.Encoding.Default.GetString(redisClient.Get(key))
```

;

```
         System.Console.WriteLine("get key " + getValue);
         System.Console.Read();
```

`}`

```
 public static void RedisPoolClientTest()
```

`{`

```
         string[] testReadWriteHosts = new[] {
         "redis://password@127.0.0.1:6379"/* redis://password@endpoint:port */
```

};

```
 RedisConfig.VerifyMasterConnections = false;//Required.
 PooledRedisClientManager redisPoolManager = new PooledRedisClientManager(10/*Number of
connection pools*/, 10/*Connection pool timeout value*/, testReadWriteHosts);
 for (int i = 0; i < 100; i++){
         IRedisClient redisClient = redisPoolManager.GetClient();//Obtain the connectio
```

`n.`

```
         RedisNativeClient redisNativeClient = (RedisNativeClient)redisClient;
         redisNativeClient.Client = null;//KVStore for Redis does not support the CLIEN
T SETNAME command. Set Client to null.
 try
```

`{`

```
         string key = "test-aliyun1111";
         string value = "test-aliyun-value1111";
         redisClient.Set(key, value);
```

`t``i`

```
litK
```

`"t` `t` `li`

```
lit"
```

```
         string listKey = "test-aliyun-list";
         redisClient.AddItemToList(listKey, value);
         System.Console.WriteLine("set key " + key + " value " + value);
         string getValue = redisClient.GetValue(key);
         System.Console.WriteLine("get key " + getValue);
         redisClient.Dispose();//
 }catch (Exception e)
```

`{`

```
         System.Console.WriteLine(e.Message);
```

`}` `}`

```
         System.Console.Read();
```

`}`

```
 static void Main(string[] args)
```

`{`

```
         //Single-connection mode.
         RedisClientTest();
         //Connection-pool mode.
         RedisPoolClientTest();
```

`}` `}` `}` Node-redis client
1. Download and install the node-redis client.

```
npm install hiredis redis
```

2. Enter the following code in the node-redis client and modify the code based on the comments.

> Not e For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see Obtain connection information.

```
 var redis = require("redis"),
 client = redis.createClient(<port>, <"host">, {detect_buffers: true});
 client.auth("password", redis.print)
```

Parameters: <port>: the service port number of the KVStore for Redis database. The default port number is 6379. <"host">: the endpoint of the KVStore for Redis instance. Configuration examples:

```
var redis = require("redis"), client = redis.createClient(6379, "r-abcdefg.redis.rds.aliyuncs.com", {detect_buffers: true}); client.auth("password", redis.print)
```

3. Run the preceding code to connect to the KVStore for Redis instance.
4. Use KVStore for Redis.

```
//Write data to the instance.
 client.set("key", "OK");
 //Query data on the instance. The returned data is of the STRING type.
 client.get("key", function (err, reply) {
 console.log(reply.toString()); // print `OK`
 });
 //If the input parameter is a buffer, the returned value is also a buffer.
 client.get(new Buffer("key"), function (err, reply) {
 console.log(reply.toString()); // print `<Buffer 4f 4b>`
 });
 client.quit();
```

C# client StackExchange.Redis

| Warning If you need to switch or select a database from multiple databases in a cluster instance, you must set the cluster compat enable parameter to 0 and restart the client _ _ application. This disables the support for the cluster syntax of open source Redis. Otherwise, the system sends the following error message: RedisCommandException: Multiple databases are not |   |
|---|---|
|   | RedisCommandException: Multiple databases are not |
| supported on this server; cannot switch to database: 1 |   |

configuration.
1. Download and install the StackExchange.Redis client.
2. Add a reference.

```
using StackExchange.Redis;
```

3. Initialize ConnectionMultiplexer.
ConnectionMultiplexer is the core of StackExchange.Redis and is shared and reused in the entire application. You must use ConnectionMultiplexer as a singleton. ConnectionMultiplexer is initialized in the following method:

> Not e
> For more information about how to obtain the connection endpoint and password of the KVStore for Redis instance, see .
> ConfigurationOptions contains multiple options, such as keepAlive, connectRetry, and name. For more information, see ConfigurationOptions.

```java
 // redis config
 private static ConfigurationOptions configurationOptions = ConfigurationOptions.Parse(
"127.0.0.1:6379,password=xxx,connectTimeout=2000");
  //the lock for singleton
 private static readonly object Locker = new object();
  //singleton
 private static ConnectionMultiplexer redisConn;
 //singleton
 public static ConnectionMultiplexer getRedisConn()
```

`{`

```
     if (redisConn == null)
```

`{`

```
         lock (Locker)
```

`{`

```
             if (redisConn == null || !redisConn.IsConnected)
```

`{`

```
                 redisConn = ConnectionMultiplexer.Connect(configurationOptions);
```

`}` `}` `}`

```
     return redisConn;
```

`}`
4. GetDatabase() returns a lightweight object. You can obtain this object from the object of
ConnectionMultiplexer.

```
 redisConn = getRedisConn();
 var db = redisConn.GetDatabase();
```

5. You can use the client to perform database operations.

> Not e The following examples describe the commands for common data types. These commands are slightly different from the Redis-native commands.

String

```
//set get string strKey = "hello"; string strValue = "world"; bool setResult = db.StringSet(strKey, strValue); Console.WriteLine("set " + strKey + " " + strValue + ", result is " + setResult); //incr string counterKey = "counter"; long counterValue = db.StringIncrement(counterKey); Console.WriteLine("incr " + counterKey + ", result is " + counterValue); //expire db.KeyExpire(strKey, new TimeSpan(0, 0, 5)); Thread.Sleep(5 * 1000); Console.WriteLine("expire " + strKey + ", after 5 seconds, value is " + db.StringGet( strKey)); //mset mget KeyValuePair<RedisKey, RedisValue> kv1 = new KeyValuePair<RedisKey, RedisValue>("key1 ", "value1"); KeyValuePair<RedisKey, RedisValue> kv2 = new KeyValuePair<RedisKey, RedisValue>("key2 ", "value2"); db.StringSet(new KeyValuePair<RedisKey, RedisValue>[] {kv1,kv2}); RedisValue[] values = db.StringGet(new RedisKey[] {kv1.Key, kv2.Key}); Console.WriteLine("mget " + kv1.Key.ToString() + " " + kv2.Key.ToString() + ", result is " + values[0] + "&&" + values[1]);
```

Hash

```
string hashKey = "myhash"; //hset db.HashSet(hashKey,"f1","v1"); db.HashSet(hashKey,"f2", "v2"); HashEntry[] values = db.HashGetAll(hashKey); //hgetall Console.Write("hgetall " + hashKey + ", result is"); for (int i = 0; i < values.Length;i++)
```

`{`

```
  HashEntry hashEntry = values[i];
  Console.Write(" " + hashEntry.Name.ToString() + " " + hashEntry.Value.ToString());
```

`}`

```
Console.WriteLine();
```

List

```
//list key string listKey = "myList"; //rpush db.ListRightPush(listKey, "a"); db.ListRightPush(listKey, "b"); db.ListRightPush(listKey, "c"); //lrange RedisValue[] values = db.ListRange(listKey, 0, -1); Console.Write("lrange " + listKey + " 0 -1, result is "); for (int i = 0; i < values.Length; i++)
```

`{`

```
 Console.Write(values[i] + " ");
```

`}`

```
Console.WriteLine();
```

Set

```
//set key string setKey = "mySet"; //sadd db.SetAdd(setKey, "a"); db.SetAdd(setKey, "b"); db.SetAdd(setKey, "c"); //sismember bool isContains = db.SetContains(setKey, "a"); Console.WriteLine("set " + setKey + " contains a is " + isContains );
```

Sorted Set

```
string sortedSetKey = "myZset"; //sadd db.SortedSetAdd(sortedSetKey, "xiaoming", 85); db.SortedSetAdd(sortedSetKey, "xiaohong", 100); db.SortedSetAdd(sortedSetKey, "xiaofei", 62); db.SortedSetAdd(sortedSetKey, "xiaotang", 73); //zrevrangebyscore RedisValue[] names = db.SortedSetRangeByRank(sortedSetKey, 0, 2, Order.Ascending); Console.Write("zrevrangebyscore " + sortedSetKey + " 0 2, result is "); for (int i = 0; i < names.Length; i++)
```

`{`

```
  Console.Write(names[i] + " ");
```

`}`

```
Console.WriteLine();
```

#### 2.5.2 Use redis-cli

The redis-cli tool is a command-line interface (CLI) of Redis. You can use redis-cli to connect to a KVStore for Redis instance from an Elastic Compute Service (ECS) instance or on-premises machine and manage data. Prerequisites The ECS instance and KVStore for Redis instance are deployed in the same classic network or virtual private cloud (VPC). The private IP address of the ECS instance is added to the whitelist of the KVStore for Redis instance. For more information, see Configure a whitelist. The ECS instance runs a Linux operating system and open source Redis is installed. For more information, see Redis official website. Procedure
1. Log on to the CLI of the ECS instance and run the following command to connect to the Redis
instance:

```
src/redis-cli -h <hostname> -p <port>
```

Parameters

| Parameter | Description |
|---|---|
| <hostname> | The internal endpoint of the KVStore for Redis instance. You can find the endpoint in the Connect ion Inf ormat ion section on the Inst ance Inf ormat ion page. |
| <port> | The service port number of the KVStore for Redis instance. Default value: 6379. |

Example

```
src/redis-cli -h r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com -p 6379
```

2. Run the following command to verify the password:

```
AUTH <password>
```

<password>: the password that you specify when you create the instance. If you forget your password, you can reset the password. For more information, see Change the password. Example:

```
AUTH testaccount:Rp829dlwa
```

If the password verification is successful, the following result is returned: `OK`

## 3 Instance management

### 3.1 Change a password

If you forget your password, need to change your password, or have not set a password for an instance, you can set a new password for the instance. Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. In the upper-right corner of the Basic Inf ormat ion page, click Modif y Password.
4. In the dialog box that appears, enter the current password and a new password.

> Not e
> If you forget your password, you can click Forgot password in the Change Password dialog box and enter a new password.
> The password must be 8 to 32 characters in length.
> The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @

```bash
# $ % ^ & * ( ) _ + - = .
```

5. Click OK.

### 3.2 Configure a whitelist

Before you use a KVStore for Redis instance, add IP addresses or CIDR blocks that are used to access the database to the whitelist of the instance to improve the security and stability of the database. Context

> Not e A properly configured whitelist can ensure a higher level of security protection for your KVStore for Redis instance. We recommend that you maintain the whitelist on a regular basis.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Whit elist Set t ings.
4. Find the IP address whitelist that you want to manage and click Modif y.

> Not e You can also click Add Whit elist to create an IP address whitelist. The name of the IP address whitelist must be 2 to 32 characters in length and can contain lowercase letters, digits, and underscores (_). The name of the whitelist must start with a lowercase letter and end with a lowercase letter or digit.

5. In the dialog box that appears, perform one of the following operations:

| Action | Procedure |
|---|---|
| Manually modify the IP address whitelist | Enter IP addresses or CIDR blocks. Manually modify the IP address whitelist Not e Separate multiple IP addresses with commas (,). You can add up to 1,000 unique IP addresses. Supported formats are specific IP addresses such as 10.23.12.24 and CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix. An IP address prefix can be 1 to 32 bits in length. If you set the prefix length to 0, for example, 0.0.0.0/0 or 127.0.0.1/0, all IP addresses are allowed to access the instance. In this case, the security risk of your instance is high. Proceed with caution. |

| Action | Procedure |
|---|---|
| Add private IP addresses of ECS instances to an IP address whitelist | i. Click Load ECS Int ernal Net work IP. ii. Select IP addresses based on your business requirements. Add private IP addresses of ECS instances Not e To find the ECS instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |
| Remove IP addresses from the IP address whitelist | To remove all IP addresses from the IP address whitelist and retain the IP address whitelist, click Delet e. |

6. Then, click OK.

### 3.3 Change specifications

This topic describes how to change the configuration of a KVStore for Redis instance. Precautions After configuration changes, the system migrates data and switches the instance. The instance is disconnected for a few seconds during this process. We recommend that you upgrade or downgrade the instance during off-peak hours. Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. On the page that appears, configure the required parameters.

| Parameter | Description |
|---|---|
| Archit ect ure T ype | Select the architecture type of the KVStore for Redis instance. KVStore for Redis supports cluster and standard architectures. The cluster architecture is suitable for scenarios that require large capacity or high performance. Redis-native databases run in a single-threading model. If your database does not require high performance, we recommend that you use a standard instance. If your database requires high performance, select a cluster architecture. |
| Inst ance T ype | Select the specification of the instance. The maximum connections and maximum internal network bandwidth vary based on the instance type. |

4. Click Submit .

### 3.4 Specify a maintenance window

You can modify the default maintenance window to perform maintenance on KVStore for Redis during off-peak hours. Context To ensure the stability of KVStore for Redis instances on the Alibaba Cloud platform, the backend system performs maintenance on instances and servers occasionally. To guarantee the stability of the maintenance process, instances will enter the Maintaining Instance status before the preset maintenance window on the day of maintenance. While an instance is in this state, data in the database can still be accessed and query operations such as performance monitoring are still available. However, change operations such as configuration change are temporarily unavailable for this instance in the console.

> Not e During the maintenance process, instances may be disconnected in the process of maintenance. We recommend that you set the maintenance window to a period during off-peak hours.

Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. In the Basic Inf ormat ion section, click Set t ings on the right of Maint enance Window.
4. Select a time period for maintenance and click Save.

> Not e The time periods are in UTC+8.

### 3.5 Upgrade the minor version

Alibaba Cloud has continuously optimized the kernel of KVStore for Redis to fix security vulnerabilities and provide more stable services. You can upgrade the kernel version (minor version) of a KVStore for Redis instance with one click in the console. Context

> Not e
> We recommend that you upgrade instance versions during off-peak hours and ensure that your application supports automatic reconnection.
> The system automatically checks the kernel version of an instance. If the current version is the latest, the Minor Version Upgrade button in the upper-right corner of the Basic Inf ormat ion section for this instance will appear dimmed.

Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Minor Version Upgrade in the upper-right corner of the
Basic Inf ormat ion section.
4. In the Minor Version Upgrade dialog box that appears, click Upgrade Now.
On the Inst ance Inf ormat ion page, the instance status will become Upgrading a minor version. When the instance status returns to Available, the upgrade has been completed.

### 3.6 Configure SSL encryption

The standard and cluster Instances of Redis 2.8 and the cluster instances of Redis 4.0 support secure sockets layer (SSL) encryption. You can enable SSL encryption to ensure more secure data transmission. Context

> Not e SSL encryption may increase the network response time of instances. We recommend that you enable this feature only when necessary.

Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click SSL Set t ings.
4. In the upper-right corner of the SSL Set t ings page, click Conf igure SSL.
5. In the dialog box that appears, turn on Enable SSL Cert if icat e.

> Not e If the version of the instance is not supported, upgrade the minor version. For more information, see Upgrade the minor version.

6. Click OK.

> Not e
> The result of the operation is displayed after a short period of time.
> In the upper-right corner of the SSL Settings page, you can also click Updat e Validit y and Download CA Cert if icat e to perform relevant operations.

### 3.7 Clear data

You can clear the data of a KVStore for Redis instance in the console. Context

> **Warning:** This operation will delete all data contained on an instance. Deleted data cannot be restored. Proceed with caution.

Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ance List page, click the ID of the instance.
3. In the upper-right corner of the Inst ance Inf ormat ion page, click Clear Dat a.
4. In the Clear Dat a message that appears, click OK.

### 3.8 Release an instance

You can release a KVStore for Redis instance at any time based on your business needs. This topic describes how to release a KVStore for Redis instance. Procedure
1. Log on to the KVStore for Redis console. For more information, see Log on to the KVStore for Redis
console.
2. On the Inst ances page, click the instance ID or choose
> Release in the Act ions column.

> **Warning:** After an instance is released, the instance cannot be restored. Proceed with caution. We recommend that you back up your data before you release an instance.

3. In the Release Inst ance message that appears, click OK.

### 3.9 Manage database accounts

KVStore for Redis allows you to create up to 20 database accounts for an instance. You can grant permissions to these accounts and manage your instance to prevent user errors. Prerequisites The engine version of the instance is Redis 4.0 or later.

> Not e If the engine version of the instance is not Redis 4.0, only the default account that is created when you create the instance is available. For more information about how to change the password of the default account, see Change the password.

Context You can create accounts, delete accounts, reset the password, and change the permissions. After an account is created, you can use this account to log on to the database and use the command-line tool to perform operations on the database with the account and granted permissions. Create an account
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ances page, find the instance that you want to manage and click the instance ID. In the
left-side navigation pane, click Account Management .

> Not e If Account Management is unavailable for an instance of Redis 4.0 or later, you must upgrade the minor version of the instance. For more information, see Upgrade the minor version.

4. In the upper-right corner of the Account Management page, click Creat e.
5. In the dialog box that appears, configure the required parameters and click OK. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Account | The account name must be 1 to 16 characters in length. The name can contain lowercase letters, digits, and underscores ( ) and must start with a letter. _ |
| Privilege | Specify the permissions that are granted to the account. Valid values: Read-only, Read/Write, and Replicate. If you select Replicate, you can run the SYNC and PSYNC commands after you connect to an instance by using your account. Not e You can create accounts that have the replicate permissions only for standard instances of Redis 4.0 or later. |
| Password Set t ings | Specify a password for the account. The password must be 8 to 32 characters in length. The password must contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: !@ # $ % ^ & * ( ) + - = . _ |
| Conf irm Password | Enter the password again. |
| Descript ion | The description of the account. |

### 3.10 Restart an instance

You can restart an instance from the Instance List page of the console. Procedure
1. Log on to the KVStore for Redis console.
2. In the Act ions column, choose
> Rest art .

> **Warning:** During the restart, the instance may be disconnected for a few seconds. We recommend that you restart instances during off-peak hours. You must also make sure that your application supports automatic reconnection.

3. In the dialog box that appears, specify the upgrade time and click OK.
Restart Immediately: restarts the instance immediately. Restart Within Maintenance Window: restarts the instance within the preset maintenance window.

### 3.11 Export the list of instances

You can export the list of KVStore for Redis instances from the KVStore for Redis console for offline management. Procedure
1. Log on to the KVStore for Redis console.
2. In the upper-right corner of the Inst ance List page, click the Export Inst ances icon.
3. In the upper-right corner of the Inst ance List page, click the Export Inst ances icon.
4. In the Export Inst ance List dialog box that appears, select the columns to export and click OK.

> Not e After you click OK, the browser begins to download the CSV file. You can use Excel or a text editor to view this file.

### 3.12 Use a Lua script

KVStore for Redis instances of all editions support Lua commands. Support for Lua commands Lua scripts improve the performance of KVStore for Redis. With support for the Lua environment, KVStore for Redis is able to perform check-and-set (CAS) operations, allowing you to combine and run multiple commands in an efficient manner.

> Not e If the EVAL command cannot be executed, for example, the " `ERR command eval not`
> `support for normal user` " message appears, you can Upgrade the minor version. During the
> upgrade, the instance may be disconnected and become read-only for a few seconds. We recommend that you upgrade instance versions during off-peak hours.

Limits on Lua scripts A Lua script, which is supported by the cluster instance of KVStore for Redis, has the following limits to ensure that all operations in the script are performed within the same hash slot: The Lua script uses the redis.call/redis.pcall function to run Redis commands. . For Redis commands, the keys must be passed by using the KEYS array, which cannot be replaced by Lua variables. If the KEYS array is not used, the following error message is returned:

```
-ERR bad lua script for redis cluster, all the keys that the script uses should be passed using the KEYS array\r\n
```

All keys that are used by the script must be allocated to the same hash slot. If the keys are allocated to different hash slots, the following error message is returned:

```
-ERR eval/evalsha command keys must be in same slot\r\n
```

Keys must be included in all commands that you want to run. If the keys are not included in all commands, the following error message is returned:

```
-ERR for redis cluster, eval/evalsha number of keys can't be negative or zero\r\n
```

The following Pub/Sub commands are not supported: PSUBSCRIBE, PUBSUB, PUBLISH, PUNSUBSCRIBE, SUBSCRIBE, and UNSUBSCRIBE. The UNPACK function is not supported.

> Not e If you do not want to impose the preceding limits but can make sure that all operations are performed in the same hash slot in the code, you can set the script_check_enable parameter to 0 in the console to disable the backend script check.

t

## 4 Connection management

### 4.1 View endpoints

You can view the internal and public endpoints of instances in the KVStore for Redis console. Context

> Not e
> The virtual IP address of a KVStore for Redis instance may change when you maintain or modify the instance. To ensure that the connection is available, we recommend that you use an endpoint to access the KVStore for Redis instance.

For more information about how to apply for a public endpoint, see Applies for a public connection string. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the Connect ion Inf ormat ion section, you can view the private and public endpoints of the
instance.

> Not e By default, only a private endpoint is provided by a KVStore for Redis instance. If you want to connect to a KVStore for Redis instance over the Internet, you must apply for a public endpoint. For more information, see Apply for a public endpoint.

### 4.2 Apply for a public endpoint

This topic describes how to apply for a public endpoint for a KVStore for Redis instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the Connect ion Inf ormat ion section, click Apply f or Public Endpoint .
4. In the dialog box that appears, enter an endpoint and a port number and click OK.

> Not e
> The custom endpoint must be 8 to 64 characters in length and can contain lowercase letters and digits. The endpoint must start with a lowercase letter.
> The custom port number ranges from 1024 to 65535. The default value is 6379.
> After you apply for a public endpoint, you must add the public endpoint to the IP address whitelist of the instance. This way, you can connect to the instance over the Internet. For more information, see Configure a whitelist.

t
5. On the Inst ance Inf ormat ion page, view the Public Endpoint in the Connect ion Inf ormat ion
section.

> Not e If you no longer use the public endpoint, click Release Public Endpoint next to Public Endpoint to release the endpoint.

### 4.3 Modify the endpoint of an KVStore for Redis instance

KVStore for Redis instance KVStore for Redis allows you to modify internal and public endpoints for instances. When changing the KVStore for Redis instance, you can change the endpoint of the new instance to the endpoint of the original instance without modifying the application. Prerequisites The instance is in the Running state. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Modif y Public Endpoint in the Connect ion
Inf ormat ion section.
4. In the Modif y Public Endpoint dialog box, set the following parameters:

| Parameter | Description |
|---|---|
| Connection type | Select Int ernal Endpoint or Public Endpoint . |
| Endpoint | Set the prefix of the endpoint. The endpoint can contain lowercase letters and digits. It must start with a lowercase letter. The endpoint must be 8 to 64 characters in length. |
| Port | Specify a port number. Valid value: 1024 to 65535. Not e It takes about 10 minutes for the modified port number of the public endpoint to take effect. You can refresh the page to view the latest port number information. |

5. In the Modif y Public Endpoint dialog box, modify Connect ion T ype, Endpoint , and Port , and
then click OK. t

> Not e
> The custom endpoint prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter.
> The custom port number ranges from 1024 to 65535. The default value is 6379.

## 5 Performance monitoring

### 5.1 Query monitoring data

You can query the monitoring data of a KVStore for Redis instance for a specified period within the last month. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Perf ormance Monit or.
4. Select the start and end time and click OK.

> Not e For more information about the metrics, see Understand metrics.

### 5.2 Select metrics

You can select the metrics to be displayed on the Historical Monitoring Data page of the KVStore for Redis console as needed. Context KVStore for Redis supports more than 10 monitoring groups. By default, the Performance Monitor page displays the metrics of the basic monitoring group. You can click Cust omize Met rics to switch to the metrics of other monitoring groups. The following table describes the monitoring groups.

| Monitoring group | Description |
|---|---|
| Basic monitoring group | The basic monitoring information about an instance, such as the queries per second (QPS), bandwidth, and memory usage of the instance. |
| Key monitoring group | The monitoring information about the use of key-value related commands, such as the number of times that the DEL and EXITS commands are executed. |
| String monitoring group | The monitoring information about the use of string commands, such as the number of times that the APPEND and MGET commands are executed. |
| Hash monitoring group | The monitoring information about the use of hash commands, such as the number of times that the HGET and HDEL commands are executed. |
| List monitoring group | The monitoring information about the use of list commands, such as the number of times that the BLPOP and BRPOP commands are executed. |
| Set monitoring group | The monitoring information about the use of set commands, such as the number of times that the SADD and SCARD commands are executed. |
| Zset monitoring group | The monitoring information about the use of zset commands, such as the number of times that the ZADD and ZCARD commands are executed. |

| psaraDB for Redis | User Guide·Performance monitorin |
|---|---|

| Monitoring group | Description |
|---|---|
| HyperLog monitoring group | The monitoring information about the use of HyperLogLog commands, such as the number of times that the PFADD and PFCOUNT commands are executed. |
| Pub/Sub monitoring group | The monitoring information about the use of publication and subscription commands, such as the number of times that the PUBLISH and SUBSCRIBE commands are executed. |
| Transaction monitoring group | The monitoring information about the use of transaction commands, such as the number of times that the WATCH, MULTI, and EXEC commands are executed. |
| Lua script monitoring group | The monitoring information about the use of Lua script commands, such as the number of times that the EVAL and SCRIPT commands are executed. |

For more information about the definitions of the metrics in each monitoring group, see Understand metrics. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Perf ormance Monit or.
4. On the Hist orical Monit oring Dat a page, click Cust omize Met rics in the Dat a Index section.
5. In the dialog box that appears, specify a monitoring group and click OK.
On the Historical Monitoring Data page, the metrics in the selected monitoring group appear.

### 5.3 Modify the data collection interval

interval KVStore for Redis console allows you to set the frequency at which monitoring data is collected. Context You can set the monitoring frequency to either 5 or 60 seconds to specify how often monitoring data to be collected by KVStore for Redis. The default monitoring time of 60 seconds is sufficient to meet common monitoring requirements. If you need to observe certain metrics at a higher frequency and lower latency, you can change the monitoring frequency to 5 seconds as described in the following section. Monitoring data does not occupy instance storage space, and collection of monitoring data does not affect normal running of the instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Perf ormance Monit or.
4. In the upper-right corner of the Hist orical Monit oring Dat a page, click Monit oring Frequency.
5. In the Monit oring Frequency dialog box that appears, select the new monitoring frequency and
click OK.

### 5.4 Understand metrics

KVStore for Redis updates more than 10 monitoring groups of metrics in real time. This allows you to monitor the status of KVStore for Redis instances. This topic describes the metrics of the monitoring groups. Metrics of basic monitoring groups

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| CpuUsage | % | The CPU utilization | Check the CPU utilization when the monitoring data is collected. |
| UsedMemory | Bytes | The amount of the used memory. | Check the memory usage when the monitoring data is collected. |
| TotalQps | Counts/s | The number of requests that are received by the instance per second. | Divide the number of requests in a monitoring cycle by the number of seconds in the monitoring cycle. |
| ConnCount | Counts | The number of connections. | Check the number of connections when collecting monitoring data. |
| InFlow | KBps | The amount of data received by the instance per second. | Divide the amount of data that is received in a monitoring cycle by the number of seconds in the monitoring cycle. |
| OutFlow | KBps | The amount of data sent by the instance per second. | Divide the amount of data that is sent in a monitoring cycle by the number of seconds in the monitoring cycle. |

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| FailedCount | Counts/s | The average number of abnormal requests per second. | Divide the total number of abnormal requests in a monitoring cycle by the number of seconds in the monitoring cycle. |
| AvgRt | us | The average response time of all requests. Not e For more information, see Response time (RT) metrics. | Divide the processing time of all requests in a monitoring cycle by the number of requests in the monitoring cycle. |
| MaxRt | us | The maximum response time of requests. Not e For more information, see Response time (RT) metrics. | The maximum time that is required to process a request in a monitoring cycle. |
| Keys | Counts | The total number of keys. | The number of keys when the monitoring data is collected. |
| Expires | Counts | The total number of keys for which an expiration time is configured. | The total number of keys for which an expiration time is set when the monitoring data is collected. |
| ExpiredKeys | Counts | The total number of expired keys. | The cumulative sum when the monitoring data is collected. After the instance is restarted, the cumulative sum is calculated again. |
| EvictedKeys | Counts | The total number of keys that are evicted because the memory is exhausted. | The cumulative sum when the monitoring data is collected. After the instance is restarted, the cumulative sum is calculated again. |
| request | Bytes | The total amount of request data received by KVStore for Redis nodes in a monitoring cycle. | See the description of this metric. |
| response | Bytes | The total amount of response data sent by KVStore for Redis nodes in a monitoring cycle. | See the description of this metric. |
| request max _ | Bytes | The maximum amount of data in a request in a monitoring cycle. | See the description of this metric. |

| User Guide·Perform | ance monitori | ng | ApsaraDB for Redi |
|---|---|---|---|

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| response max _ | Bytes | The maximum amount of data in a response in a monitoring cycle. | See the description of this metric. |
| traffic control i _ _ nput | Counts | The number of times that downstream throttling is triggered. | Monitor the cumulative sum in a monitoring cycle. |
| traffic control _ _ output | Counts | The number of times that uplink throttling is triggered. | Monitor the cumulative sum in a monitoring cycle. |
| traffic control i _ _ nput status _ | Counts | Indicates whether downstream throttling was triggered in a monitoring cycle. A value of 0 indicates that throttling was not triggered. A value of 1 indicates that throttling was triggered. | See the description of this metric. |
| traffic control _ _ output status _ | Counts | Indicates whether upstream throttling was triggered in a monitoring cycle. A value of 0 indicates that throttling was not triggered. A value of 1 indicates that throttling was triggered. | See the description of this metric. |
| hit rate _ | % | The request hit rate, which is the probability that data exists in a KVStore for Redis instance for a data access request. | Calculate the percentage of the hit requests to the total number of requests in a monitoring cycle. |
| hit | Counts | The number of hit requests. | Check the number of hit requests in a monitoring cycle. |
| miss | Counts | The number of missed requests. | Check the number of missed requests in a monitoring cycle. |
| evicted keys p _ _ er sec _ | Counts/s | The number of keys that are evicted per second. | Divide the total number of keys that are evicted in a monitoring cycle by the number of seconds in the monitoring cycle. |

Metrics in other monitoring groups The system also uses other metrics to monitor specific types of data or specific features. The metrics are classified into: Metrics that indicate the number of times that commands are used. For example, the del, dump, and exists metrics that are used to monitor keys indicate the number of times that the DEL, DUMP, and EXISTS commands are executed. Response time (RT) metrics of commands. For example, the metrics that end with avg_rt, such as del_avg_rt dump_avg_rt, and exists_avg_rt, in the key monitoring group are used to monitor the average response time of the DEL, DUMP, and EXISTS commands in a monitoring cycle. Response time (RT) metrics All monitoring groups have RT metrics. RT metrics end with Rt or rt. For example, the AvgRt and MaxRt metrics are used in the basic monitoring group and the del_avg_rt and exists_avg_rt metrics are used to monitor keys. The AvgRt and MaxRt metrics in the basic monitoring group are the most frequently used RT metrics. These metrics have different meanings for proxy nodes and data nodes. For a cluster instance or a read/write splitting instance, the AvgRt metric of a proxy node indicates the average time consumed by the proxy node to process all commands. The following process shows how a proxy node processes a command: i. The proxy node receives a command and forwards the command to a data node. ii. The data node processes the command and responds to the proxy node. iii. The proxy node returns the command processing result. The AvgRt metric of the proxy node includes the amount of time consumed by the data node to process a command and the time that is required to wait for the command to be processed. This metric also includes the amount of time consumed for network communication between the proxy node and the data node. For data nodes of a cluster instance or a read/write splitting instance or for a standard instance, the AvgRt metric indicates the average time consumed by a data node to process all commands. This metric records the period of time from the time when the data node receives the command to the time when the data node returns the result. This metric does not include the time consumed by the proxy node to process a command and the time that is required for network communication. The MaxRt metric indicates the maximum response time of requests. The statistical method of this metric is similar to the statistical method of the AvgRt metric for all KVStore for Redis instances.

## 6 Parameter configuration

KVStore for Redis allows you to customize certain instance parameters. This topic describes parameters and the common methods to modify them in the KVStore for Redis console. Context KVStore for Redis is completely compatible with the native database services of Redis. The method to set parameters for KVStore for Redis is similar to that of an on-premises Redis database. You can set the parameters described in this topic in the KVStore for Redis console. Parameters Parameters

| Parameter | Description |
|---|---|
| #no loose check-whitelist- _ _ always | Specifies whether to check whether the client IP address is in the whitelist of the KVStore for Redis instance after password-free access is enabled in Virtual Private Cloud (VPC). Default value: no. If you set this parameter to yes, the whitelist will still take effect in password- free access mode for VPC. Valid values: yes no |
| #no loose disabled-commands _ _ | Specifies the disabled commands. Separate multiple commands with commas (,). You can disable the following commands: FLUSHALL, FLUSHDB, KEYS, HGET ALL, EVAL, EVALSHA, and SCRIPT . |
| #no loose ssl-enabled _ _ | Specifies whether to enable SSL encryption. Default value: no. Valid values: yes no |
| #no loose sentinel-enabled _ _ | Specifies whether to enable Sentinel-compatible mode. Default value: no. Valid values: yes no |

| Parameter | Description |
|---|---|
| client-output-buffer-limit pubsub | Limits the size of output buffers for Pub/Sub clients. This parameter can contain options in the following format: <hard limit> <soft limit> <soft seconds> . Hard limit: If the output buffer of a Pub/Sub client reaches or exceeds the number of bytes specified by hard limit, the client is immediately disconnected. soft limit and soft seconds: If the output buffer of a Pub/Sub client reaches or exceeds the size in bytes specified by soft limit for a period of time in seconds specified by soft seconds, the client will be disconnected. |
| dynamic-hz | Specifies whether to enable dynamic frequency control for background tasks. Default value: yes. Valid values: yes no |
| hash-max-ziplist-entries | Specifies the maximum size of each key-value pair stored within a hash in bytes. A hash is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the hash in bytes must be less than the value of the hash-max-ziplist-value parameter. 2. The number of key-value pairs stored within the hash must be less than the value of the hash-max-ziplist-entries parameter. |
| hash-max-ziplist-value | Specifies the maximum size of each key-value pair stored within a hash in bytes. A hash is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the hash in bytes must be less than the value of the hash-max-ziplist-value parameter. 2. The number of key-value pairs stored within the hash must be less than the value of the hash-max-ziplist-entries parameter. |
| hz | Specifies the execution frequency for background tasks, such as tasks to evict expired keys. Valid values: 1 to 500. Default value: 10. The larger the value of the hz parameter, the more frequently background tasks are performed and the more precisely timeout events are handled, but the more CPU KVStore for Redis consumes. We recommend that you do not set the hz parameter to a value greater than 100. |
| lazyfree-lazy-eviction | Specifies whether to enable lazyfree for the eviction feature. Default value: no. Valid values: yes no |

|   | limit> <soft seconds> |
|---|---|

| User Guide·Parameter configuration | ApsaraDB for Redi |
|---|---|
| Parameter | Description |
| lazyfree-lazy-expire | Specifies whether to enable lazyfree to delete expired keys. Default value: yes. Valid values: yes no |
| lazyfree-lazy-server-del | Specifies whether to enable lazyfree to asynchronously delete data with the DEL command. Default value: yes. Valid values: yes no |
| list-compress-depth | Specifies the number of nodes that are not compressed at each side in a list. Default value: 0. Valid values: 0: does not compress any nodes in the list. 1: does not compress the first node from each side of the list, but compresses all nodes in between. 2: does not compress the first two nodes from each side of the list, but compresses all nodes in between. 3: does not compress the first three nodes from each side of the list, but compresses all nodes in between. And so on up to 65535. |
| list-max-ziplist-size | Specifies the maximum size of each ziplist in a quicklist. A positive number indicates the maximum number of elements in each ziplist of a quicklist. For example, if you set this parameter to 5, each ziplist of a quicklist can contain a maximum of five elements. A negative number indicates the maximum number of bytes in each ziplist of a quicklist. Default value: -2. Valid values: -5: indicates that each ziplist of a quicklist cannot exceed 64 KB (1 KB = 1,024 bytes). -4: indicates that each ziplist of a quicklist cannot exceed 32 KB. -3: indicates that each ziplist of a quicklist cannot exceed 16 KB. -2: indicates that each ziplist of a quicklist cannot exceed 8 KB. -1: indicates that each ziplist of a quicklist cannot exceed 4 KB. |

| Parameter | Description |
|---|---|
| maxmemory-policy | Specifies the policy used to evict keys if the memory is fully occupied. Valid values: LRU means least recently used. LFU means least frequently used. LRU, LFU, and TTL are implemented by using approximated randomized algorithms. volatile-lru: evicts the approximated least recently used (LRU) keys among keys with a preset expiration time. allkeys-lru: evicts the approximated LRU keys. volatile-lfu: evicts the approximated least frequently used (LFU) keys among keys with a preset expiration time. allkeys-lfu: evicts the approximated LFU keys. volatile-random: evicts random keys among keys with a preset expiration time. allkeys-random: evicts random keys. volatile-ttl: evicts keys with the nearest time to live (TTL) among keys with a preset expiration time. noeviction: does not evict any keys, but returns an error on write operations. |
| notify-keyspace-events | Specifies the events that the Redis server can notify clients of. The value of this parameter is any combination of the following characters, each of which specifies a type of event to be notified: K: keyspace events, published with the keyspace@<db> prefix. __ __ E: keyevent events, published with the keyevent@<db> prefix. __ __ g: generic commands that are non-type specific, such as DEL, EXPIRE, and RENAME. l: list commands. s: set commands. h: hash commands. z: sorted set commands. x: expired key events. An expired key event is generated when a key expires. e: evicted key events. An evicted key event is generated when a key is evicted due to the policy specified by the maxmemory-policy parameter. A: the alias for g$lshzxe. |
| set-max-intset-entries | Specifies the maximum number of data entries in a set. A set is encoded by using intset when it meets the following conditions: 1. The set is composed of just strings. The number of strings is less than the value of this parameter. 2. All strings are integers in radix 10 in the range of 64-bit signed integers. |

| Parameter | Description |
|---|---|
| slowlog-log-slower-than | Specifies whether to log slow queries. Negative number: does not log slow queries. 0: logs all queries. Positive number: logs queries that exceed an execution time specified by this positive number, in microseconds. Valid values: 0 to 10,000,000. Default value: 10,000. |
| slowlog-max-len | Specifies the maximum number of slow query log entries that can be stored. Valid values: 100 to 10,000. Default value: 1,024. |
| stream-node-max-bytes | Specifies the maximum memory that can be used by each macro node in streams. Valid values: 0 to 999,999,999,999,999. If you set the parameter to 0, each macro node can use an unlimited amount of memory. |
| stream-node-max-entries | Specifies the maximum number of stream entries that can be stored within each macro node. Valid values: 0 to 999,999,999,999,999. If you set the parameter to 0, each macro node can store unlimited stream entries. |
| timeout | Specifies a timeout period for client connections. Unit: seconds. Valid values: 0 to 100,000. 0 indicates that client connections never time out. |
| zset-max-ziplist-entries | Specifies the maximum size of each key-value pair stored within a sorted set in bytes. A sorted set is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the sorted set in bytes must be less than the value of the zset-max-ziplist- value parameter. 2. The number of key-value pairs stored within the sorted set must be less than the value of the zset-max-ziplist-entries parameter. |
| zset-max-ziplist-value | Specifies the maximum size of each key-value pair stored within a sorted set in bytes. A sorted set is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the sorted set in bytes must be less than the value of the zset-max-ziplist- value parameter. 2. The number of key-value pairs stored within the sorted set must be less than the value of the zset-max-ziplist-entries parameter. |

| Parameter | Description |
|---|---|
| list-max-ziplist-entries | Specifies the maximum size of each key-value pair stored within a list in bytes. A list is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the list in bytes must be less than the value of the list-max-ziplist-value parameter. 2. The number of elements stored within the list is less than the value of the list-max-ziplist-entries parameter. |
| list-max-ziplist-value | Specifies the maximum size of each key-value pair stored within a list in bytes. A list is encoded using ziplist when it meets the following conditions: 1. The maximum size of each key-value pair stored within the list in bytes must be less than the value of the list-max-ziplist-value parameter. 2. The number of elements stored within the list is less than the value of the list-max-ziplist-entries parameter. |
| cluster compat enable _ _ | Specifies whether to enable compatibility with the syntax of Redis Cluster. Default value: 1. Valid values: 0: no 1: yes |
| script check enable _ _ | Specifies whether to confirm that all the keys used in a Lua script are in the same hash slot. Default value: 1. Valid values: 0: no 1: yes |

> Not e The maxclients parameter, which is used to specify the maximum number of connections to Redis data nodes, is fixed to 10,000. You cannot modify the value of this parameter.

Configure parameters in the KVStore for Redis console
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Syst em Paramet ers.
4. Find the target parameter and click Modif y in the Act ion column.
5. In the dialog box that appears, modify the parameter value and click OK.

## 7 Backup and recovery

### 7.1 Automatically back up data

An increasing number of applications use Redis for persistent storage. In this case, an automatic backup mechanism is required to back up data on a regular basis so that you can restore data if user errors occur. KVStore for Redis uses Redis database backup (RDB) snapshots to back up data on replica nodes. The backup process does not have negative impacts on the performance of your instance. You can configure a custom backup policy in the console. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Backup and Recovery.
4. Click the Backup Set t ings tab.
5. Click Edit and specify Backup Cycle and Backup Time.
Ret ent ion Days: The number of days for which backups are retained. This parameter is set to seven days and cannot be changed. Backup Cycle: You can select one or more days in a week. By default, one backup is created per day. Backup T ime: You can specify a period of time in hours within a day. We recommend that you back up data during off-peak hours.
6. Click OK.

### 7.2 Back up an instance

You can initiate a manual backup task in the console at any time. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Backup and Recovery.
4. In the upper-right corner of the page, click Creat e Backup.
5. Click OK.

> Not e On the Dat a Backup tab, you can select a time range to query existing backups. Backups are retained for seven days.

### 7.3 Download backup files

To archive backup files for a long period, you can copy the URLs in the console and download the database backup files to an on-premises machine.
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Backup and Recovery.
4. Find the backup that you want to download and click in the Act ions column.
5. In the dialog box that appears, perform one of the actions that are described in the following
table.

| Action | Procedure |
|---|---|
| Download the backup file over the Internet | i. Click Get URL f or Int ernet . ii. Paste the URL into the address bar of a browser and press Enter. The browser automatically downloads the backup file. |
| Download the backup file over an internal network. For example, you can download the backup file on an Elastic Compute Service (ECS) instance. | i. Click Get URL f or Int ranet . ii. Select a downloading method based on the operating system of the client. Windows: Paste the URL into the address bar of a browser and press Enter. The browser automatically downloads the backup file. Linux: Run the following command in the specified format: wget -c '<URL that is used to download the backup file over the internal network>' -O <Name of the downloaded backup file>.<The extension that is added to the name of the downloaded backup file> Example: wget -c 'http://rds****.oss-cn-hangzhou- internal.aliyuncs.com/custins416****/hins1****.rdb?... ' -O backupfile.rdb Not e If you download the backup file on an ECS instance, the ECS instance and the KVStore for Redis instance can be deployed in different types of networks. |

### 7.4 Restore data

KVStore for Redis allows you to restore data from a specified backup set to the current KVStore for Redis instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Backup and Recovery.
4. Perform one of the following operations based on the architecture of your KVStore for Redis
instance: Master-replica instance: Find the backup set that you want to restore and click Rest ore Dat a in the Act ions column. Cluster instance: Select the backup sets of all data shards that were generated at the same point in time and click Rest ore Dat a in the upper-right corner.

> **Warning:** Risks may occur when you restore data. Proceed with caution. Verify the data that you want to restore before you restore the data.

5. In the message that appears, read the content and click Cont inue.
You can also restore backup data by cloning an instance. For more information, see Clone an instance.

### 7.5 Clone an instance

KVStore for Redis allows you to create an instance from a specified backup set. The data in the new instance is the same as the data in the backup set. This feature can be applied in scenarios such as data recovery, quick workload deployment, and data verification. Prerequisites The KVStore for Redis instance is of the master-replica type. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, click Backup and Recovery.
4. Find the backup set that you want to restore and click Clone Inst ance in the Act ions column.
5. In the message that appears, click OK.
6. On the Restore Instance page, configure the parameters and click Submit .
Not e For more information about the configurations of the new instance, see Create an instance.

## 8 CloudDBA

### 8.1 Performance trends

CloudDBA provides the performance trends feature that allows you to monitor the basic performance of a KVStore for Redis instance and the operational trends within a specified period of time. The performance trends include the CPU utilization, memory usage, queries per second (QPS), total connections, response time, data transfer, and key hit ratio. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, choose CloudDBA > Perf ormance T rends.
4. You can use the following methods to view performance trends:

> Not e If the KVStore for Redis instance uses a cluster architecture, the Performance Trends page displays the information about the nodes. The performance data during the last 1 hour is displayed. If you click the node ID, you can view the details of a specified node.

Perf ormance t rends On the Perf ormance T rends tab, specify a time range and click Search.

> Not e
> By default, Correlat ion is enabled. If you move the pointer over the CPU chart to view the CPU metric of the KVStore for Redis instance at 09:00, other charts also display other metrics of the instance at 09:00.
> To view the definition of the performance metric and the performance trend, click Def init ion? and Det ails in the upper-right corner of the chart.

Perf ormance t rend comparison To compare the performance trends within two periods of time, click the Perf ormance T rend Comparison tab, specify two periods of time, select more metrics, and then click Search. Cust om chart The preceding two methods display the basic metrics of a KVStore for Redis instance. If you want to display only basic metrics, you can configure custom performance trend charts. For more information, see Add a performance trend chart.

### 8.2 Add a performance trend chart

The default performance trends tab displays the basic performance metrics of a KVStore for Redis instance. You can add a chart that contains only specified performance metrics to analyze the performance trends of your instances. This topic describes how to add a performance trend chart to a dashboard for KVStore for Redis instances. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, choose CloudDBA > Perf ormance T rends.
4. Click the Cust om Chart tab.
5. Click Add Monit oring Dashboard. In the Create Monitoring Dashboard dialog box, enter a
dashboard name and click OK.
6. Click + Add Chart or Add Monit oring Chart . Select the metrics that you want to add and click
OK.
7. (Optional)You can view, modify, and delete monitoring dashboards.
View a monitoring dashboard Select the monitoring dashboard, specify a time range, and then click Search. Modify a monitoring dashboard Click the following icons to modify or delete a chart in the monitoring dashboard. Delete a monitoring dashboard Choose Operat e Dashboard > Delet e Monit oring Dashboard.

### 8.3 View performance metrics in real time

time CloudDBA allows you to view the performance metrics of KVStore for Redis instances in real time. The performance metrics include information about CPU utilization, memory usage, queries per second (QPS), network traffic, servers, keys, clients, and connections. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, choose CloudDBA > Real-t ime Perf ormance.
4. Select a view based on your business requirements.
In the upper part of the page, performance metrics are displayed in real time. The metrics include information about the server, keys, memory, clients, and connections. The details about the performance metrics are displayed in Real-t ime Chart s and Real-t ime T ables.

> Not e The metrics are automatically updated every 5 minutes. Therefore, you can view real-time changes in performance. The remaining updating times are displayed in the upper- right corner. To stop updating the performance metrics, you can click Pause.

| View | Description |
|---|---|

| View | Description |
|---|---|
| Real-t ime Chart s | Displays the real-time performance metrics of an instance in curve charts, such as key information, key hit information, key hit ratio, CPU utilization, memory information, QPS, and network traffic. |
| Real-t ime T ables | Displays the information about keys, QPS, memory usage, CPU utilization, network traffic, clients, and connections. The table displays up to 999 records. A new record is added to the table every 5 seconds. |

### 8.4 Instance sessions

Instance sessions allow you to view the information about sessions between a KVStore for Redis instance and a client in real time, which includes the client information, commands that are run, and connection duration. You can also terminate abnormal sessions based on your business requirements. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, choose CloudDBA > Inst ance Sessions.
4. Perform the operations that are described in the following table based on your business
requirements. View sessions: By default, the details of all sessions are displayed. You can move the pointer over a specific parameter name to view information.

> Not e
> You can enter keywords in the search box to filter session information.
> To refresh instance session information, click Ref resh in the upper-left corner or enable Aut o Ref resh to automatically refresh the page every 30 seconds.

Terminate sessions: Press the Shift key and select the specified session. To terminate the selected session, click Kill Select ed in the upper-right corner. To terminate all sessions, click Kill All.

> **Warning:** To avoid unexpected results, we recommend that you do not terminate system-level sessions.

View session statistics: Session statistics record the total number of clients, active clients, and source IP addresses of instance sessions.

> Not e In the St at ist ics by Source table, click the icon on the right of the source IP address to modify the source alias. In the Total Sessions column, click a value to view the details about a source IP address.

### 8.5 Slow queries

Slow queries reduce the stability of KVStore for Redis instances. To monitor and analyze slow queries, you can view the details about slow query logs in CloudDBA. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane, choose CloudDBA > Slow Queries.
4. Query the details about the slow query logs.

> Not e You can select the number of log entries to be displayed or enter keywords in the search box to filter log entries.
