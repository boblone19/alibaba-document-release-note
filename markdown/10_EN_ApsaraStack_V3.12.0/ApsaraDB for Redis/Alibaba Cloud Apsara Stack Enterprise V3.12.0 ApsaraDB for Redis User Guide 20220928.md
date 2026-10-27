---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 52
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20ApsaraDB%20for%20Redis%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 ApsaraDB for Redis User Guide 20220928

## Table of Contents

- 1 What is KVStore for Redis?
- 2 Quick Start
  - 2.1 Get started with KVStore for Redis
  - 2.2 Log on to the KVStore for Redis console
  - 2.3 Create an instance
  - 2.4 Configure a whitelist
  - 2.5 Connect to an instance
    - 2.5.1 Use a Redis client
    - 2.5.2 Use redis-cli
- 3 Instance management
  - 3.1 Change the password
  - 3.2 Configure a whitelist
  - 3.3 Change configurations
  - 3.4 Set a maintenance window
  - 3.5 Upgrade the minor version
  - 3.6 Configure SSL encryption
  - 3.7 Clear data
  - 3.8 Release an instance
  - 3.9 Manage database accounts
  - 3.10 Use a Lua script
  - 3.11 Restart an instance
  - 3.12 Export the list of instances
- 4 Connection management
  - 4.1 View connection strings
  - 4.2 Apply for a public endpoint
  - 4.3 Change the connection string of an instance
- 5 Parameter configuration
- 6 Backup and recovery
  - 6.1 Back up data automatically
  - 6.2 Back up data manually
  - 6.3 Download backup files
  - 6.4 Restore data
  - 6.5 Clone an instance
- 7 Performance monitoring
  - 7.1 View monitoring data
  - 7.2 Customize metrics
  - 7.3 Modify monitoring frequency
  - 7.4 Monitoring metrics

s?

## 1 What is KVStore for Redis?

KVStore for Redis is a key-value storage database service that is compatible with open source Redis protocols. KVStore for Redis supports various data types, such as strings, lists, sets, sorted sets, and hash tables. The service also provides advanced features, such as transactions, message subscription, and message publishing. You can easily deploy and manage KVStore for Redis databases in the KVStore for Redis console. You can create an instance to initialize a database. Before you use a KVStore for Redis instance, add IP addresses or CIDR blocks that are used to access the database to the instance whitelist. You can manage instances in the KVStore for Redis console. To secure data, you can periodically or immediately back up or restore databases in the KVStore for Redis console. You can log on to a database by using a client and then execute SQL statements to perform database operations.

## 2 Quick Start

### 2.1 Get started with KVStore for Redis

This topic describes all operations on an instance, from creating an instance to logging on to a database. This allows you to understand how to create and manage an instance. The following figure shows the flowchart of managing a KVStore for Redis instance. This topic describes how to log on to the KVStore for Redis console. KVStore for Redis supports two types of networks: classic network and Virtual Private Cloud (VPC). You can create KVStore for Redis instances of one of these network types. Before you use a KVStore for Redis instance, add IP addresses or CIDR blocks that are used to access the database to the instance whitelist to enhance database security and stability. If you have not specified a password when you create the instance, set the password of the instance on the Inst ance Inf ormat ion page. Connect to the instance You can use a client that supports Redis protocols or use the Redis command-line interface (redis-cli) tool to connect to the KVStore for Redis instance.

### 2.2 Log on to the KVStore for Redis console

console This topic describes how to log on to the KVStore for Redis console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. In the top navigation bar, choose Product s > KVSt ore f or Redis.

### 2.3 Create an instance

This topic describes how to create an instance in the KVStore for Redis console. Prerequisites To use the Virtual Private Cloud (VPC) service, you must create a VPC network in the same region where you create the KVStore for Redis instance.

> Not e The network type cannot be changed after the instance is created.

Procedure
1. Log on to the KVStore for Redis console.
2. Click Creat e Inst ance in the upper-right corner.
3. Set the following parameters.
KVStore for Redis instance parameters

| Section | Parameter | Description |
|---|---|---|
| Basic | Organizati on | The organization to which the KVStore for Redis instance to be created belongs. |
|   | Resource Set | The resource set to which the KVStore for Redis instance belongs. Not ice After you select a resource set, the KVStore for Redis instance is accessible only to the members of the specified resource set. |
| Region | Region | Specifies the region where the KVStore for Redis instance is deployed. |
|   | Zone | Specifies the zone where the KVStore for Redis instance is deployed. |
| Specificatio ns | Engine Version | The following engine versions are supported: Redis2.8 Redis4.0 |
|   | Architectur e Type | The architecture type of the KVStore for Redis instance. KVStore for Redis provides cluster and standard architectures. The cluster architecture meets large-capacity or high-performance requirements. Native Redis databases run in a single-threading model. If your database does not require high performance, we recommend that you use a standard instance. For higher performance, select a cluster architecture. |
|   | Node Type | The node type for the KVStore for Redis instance. KVStore for Redis supports the primary-secondary dual-node structure. |
|   | Instance Type | The specification of the instance. The maximum connections and maximum internal network bandwidth vary among different instance specifications. |

| Section | Parameter | Description |
|---|---|---|
| Network | Network Type | The network type of the instance. On the Apsara Stack, a classic network and a VPC network have the following differences: Classic network: Cloud services in a classic network are not isolated. Unauthorized access to a cloud service is blocked by only security groups or the service whitelist policy. VPC: A VPC helps you build an isolated network environment on Apsara Stack. You can customize the routing table, Classless Inter-Domain Routing (CIDR) blocks, and gateway of a VPC network. You can also migrate applications to the cloud by using a leased line or virtual private network (VPN) without service interruption to integrate your on-premises data center and cloud resources in a VPC network into a virtual data center. Not e Before you select the VPC type, create a VPC network. For more information, see Create a VPC network and Cre ate a VSwitch in VPC User Guide . |
| Password | Instance Name | Enter the name of the KVStore for Redis instance. The name must be 2 to 128 characters in length and can contain uppercase and lowercase letters, digits, underscores ( ), and hyphens (-). It must start with a lowercase letter or Chinese _ character. |
|   | Password Setting | You can select Now or Lat er. |
|   | Password | Set a password used to connect to the instance. The password must follow these rules: The password must be 8 to 30 characters in length. The password must contain uppercase letters, lowercase letters, and digits. Special characters are not supported. |
|   | Confirm Password | Enter the specified password again. |

4. After you set the parameters, click Submit .

### 2.4 Configure a whitelist

Before using a KVStore for Redis instance, add IP addresses or CIDR blocks used to access the database to the instance whitelist to improve database security and stability. Context

> Not e A properly configured whitelist can guarantee the highest-level security protection for your KVStore for Redis instance. We recommend that you maintain the whitelist on a regular basis.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, find the target instance. Click the instance ID or click Manage in the
Act ions column.
3. On the Inst ance Inf ormat ion page, click Whit elist Set t ings in the left-side navigation pane.
4. On the Whit elist Set t ings page, proceed in either of the following ways:
To customize the whitelist group name, create a new whitelist group: a. Click Add a Whit elist Group in the upper-right corner. b. In the Add a Whitelist Group dialog box that appears, set Group Name.

> Not e A group name must be 2 to 32 characters in length and contain lowercase letters, digits, or underscores (_). The group name must start with a lowercase letter and end with a letter or digit. You cannot change this name after you create the whitelist group.

If you do not require a custom whitelist group, click Modif y next to the target whitelist group.
5. In the Add a Whit elist Group or Modif y Whit elist of Group**​** dialog box that appears, proceed in
either of the following ways: Manually modify the Whit elist of Group field: a. In the Whit elist of Group field, enter the IP addresses or CIDR blocks that you can use to connect to the KVStore for Redis instance. Manually modify the whitelist group

> Not e
> Set the whitelist to `0.0.0.0/0` to allow connections from all IP addresses.
> Set the whitelist to `127.0.0.1` to block connections from all IP addresses.
> Set the whitelist to a CIDR block to allow connections from the IP addresses within the CIDR block, such as `10.10.10.0/24` .
> When you enter multiple IP addresses or CIDR blocks, separate them with commas (,) and leave no space before or after each comma.
> You can add 1,000 or fewer IP addresses or CIDR blocks to each whitelist group.

b. Click OK. Load internal IP addresses of target ECS instances under the current Alibaba Cloud account: a. Click Load ECS Int ernal IP Addresses. Load internal IP addresses of target ECS instances b. Select internal IP addresses of target ECS instances. Select internal IP addresses of target ECS instances

> Not e You can perform a fuzzy search by ECS instance name, ID, or IP address on the search bar above the list of ECS internal IP addresses.

c. Click OK.

### 2.5 Connect to an instance

#### 2.5.1 Use a Redis client

You can connect to an KVStore for Redis instance by using clients for different programming languages. The database service of KVStore for Redis is compatible with that of native Redis. Therefore, you can connect to both database services in similar ways. All clients that are compatible with the Redis protocol support connections to KVStore for Redis. You can use any of these clients that are suitable for your applications. For more information about Redis clients, visit https://redis.io/clients. Prerequisites The internal IP address of the Elastic Compute Service (ECS) instance or the public IP address of the local host has been added to a whitelist of the KVStore for Redis instance. For more information, see Configure a whitelist. If you use a custom account to connect to the KVStore for Redis instance, the connection password must be in the format of `<user>:<password>` . For example, if the username of a custom account is `admin` and the password is `password` , the password used to connect to the KVStore for Redis instance must be in the format of `admin:password` . Jedis clien You can use a Jedis client to connect to KVStore for Redis in any of the following ways: Single Jedis connection. This method is not recommended because a client cannot automatically reconnect to KVStore for Redis after a connection times out. JedisPool-based connection. This method is recommended. To use a Jedis client to connect to an KVStore for Redis instance, perform the following steps:
1. Download and install the Jedis client. For more information, see Jedis.
2. Example of single Jedis connection
i. Open the Eclipse client, create a project, and then enter the following code:

```java
import redis.clients.jedis.Jedis; public class jedistest { public static void main(String[] args) { try {
     String host = "xx.kvstore.aliyuncs.com";//You can view the connection address
of the target instance in the console.
     int port = 6379;
     Jedis jedis = new Jedis(host, port);
     //Authentication information.
     jedis.auth("password");//password
     String key = "redis";
     String value = "aliyun-redis";
     //Select a database. Default value: 0.
     jedis.select(1);
     //Set a key.
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

`}` `}` `}` ii. Run the project. You have connected to KVStore for Redis if you see the following result in the Eclipse console.

```
Set Key redis Value aliyun-redis Get Key redis ReturnValue aliyun-redis
```

Then, you can use a Jedis client to manage your KVStore for Redis instance. You can also connect to your KVStore for Redis instance by using JedisPool.
3. Example of JedisPool-based connection
i. Open the Eclipse client, create a project, and then configure the following pom file:

```xml
<dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> <version>2.7.2</version> <type>jar</type> <scope>compile</scope> </dependency>
```

ii. Add the following application to the project:

```java
import org.apache.commons.pool2.PooledObject; import org.apache.commons.pool2.PooledObjectFactory; import org.apache.commons.pool2.impl.DefaultPooledObject; import org.apache.commons.pool2.impl.GenericObjectPoolConfig; import redis.clients.jedis.HostAndPort; import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig;
```

iii. If your Jedis client version is Jedis-2.7.2, enter the following code in the project:

```
JedisPoolConfig config = new JedisPoolConfig(); //Maximum number of idle connections. You can customize this parameter. Make sure t hat the specified maximum number of idle connections does not exceed the maximum nu mber of connections that the KVStore for Redis instance supports. config.setMaxIdle(200); //Maximum number of connections. You can customize this parameter. Make sure that t he specified maximum number of connections does not exceed the maximum number of co nnections that the KVStore for Redis instance supports. config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "Password"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); /// ... do stuff here ... for example jedis.set("foo", "bar"); String foobar = jedis.get("foo"); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); Set<String> sose = jedis.zrange("sose", 0, -1); } finally { if (jedis ! = null) { jedis.close();
```

`}` `}`

```
/// ... when closing your application: pool.destroy();
```

iv. If your Jedis client version is Jedis-2.6 or Jedis-2.5, enter the following code in the project:

```
JedisPoolConfig config = new JedisPoolConfig(); //Maximum number of idle connections. You can customize this parameter. Make sure t hat the specified maximum number of idle connections does not exceed the maximum nu mber of connections that the KVStore for Redis instance supports. config.setMaxIdle(200); //Maximum number of connections. You can customize this parameter. Make sure that t he specified maximum number of connections does not exceed the maximum number of co nnections that the KVStore for Redis instance supports. config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); String host = "*.aliyuncs.com"; String password = "Password"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; boolean broken = false; try {
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
} else if (jedis ! = null) {
     pool.returnResource(jedis);
```

`}` `}` v. Run the project. You have connected to KVStore for Redis if you see the following result in the Eclipse console.

```
Set Key redis Value aliyun-redis Get Key redis ReturnValue aliyun-redis
```

Then, you can use a Jedis client to manage your KVStore for Redis instance. PhpRedis client To use a PhpRedis client to connect to an KVStore for Redis instance, perform the following steps:
1. Download and install the PhpRedis client. For more information, see PhpRedis.
2. In an editor that supports PHP editing, enter the following code:

```
<? php
 /* Replace the following parameter values with the host name and port number of the ta
rget instance. */
 $host = "localhost";
 $port = 6379;
 /* Replace the following parameter values with the ID and password of the target insta
nce. */
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
  /* You can perform database operations after authentication. For more information, vi
sit https://github.com/phpRedis/phpredis. */.
 if ($redis->set("foo", "bar") == false) {
         die($redis->getLastError());
```

`}`

```
 $value = $redis->get("foo");
 echo $value;
 ? >
```

3. Run the code. Then, you can use a PhpRedis client to connect to your KVStore for Redis instance.
For more information, visit https://github.com/phpredis/phpredis. Redis-py client To use a redis-py client to connect to an KVStore for Redis instance, perform the following steps:
1. Download and install the redis-py client. For more information, see redis-py.
2. In an editor that supports Python editing, enter the following code. You can use a redis-py client to
connect to the KVStore for Redis instance and perform database operations.

```java
#! /usr/bin/env python
#-*- coding: utf-8 -*-
import redis
#Replace the following parameter values with the host name and port number of the target in
stance. host = 'localhost' port = 6379
#Replace the following parameter value with the password of the target instance.
pwd = 'test_password' r = redis.StrictRedis(host=host, port=port, password=pwd)
#You can perform database operations after you establish a connection. For more information
, visit https://github.com/andymccurdy/redis-py. r.set('foo', 'bar'); print r.get('foo')
```

C or C++ client To use a C or C++ client to connect to an KVStore for Redis instance, perform the following steps:
1. Download, compile, and install the C client by using the following code:

```python
     git clone https://github.com/redis/hiredis.git
     cd hiredis
     make
     sudo make install
```

2. Enter the following code in the C or C++ editor:

```
     #include <stdio.h>
     #include <stdlib.h>
     #include <string.h>
     #include <hiredis.h>
     int main(int argc, char **argv) {
     unsigned int j;
     redisContext *c;
     redisReply *reply;
     if (argc < 4) {
             printf("Usage: example xxx.kvstore.aliyuncs.com 6379 instance_id password\
n");
             exit(0);
```

`}`

```
     const char *hostname = argv[1];
     const int port = atoi(argv[2]);
     const char *instance_id = argv[3];
     const char *password = argv[4];
     struct timeval timeout = { 1, 500000 }; // 1.5 seconds
     c = redisConnectWithTimeout(hostname, port, timeout);
     if (c == NULL || c->err) {
     if (c) {
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
     /* AUTH */
     reply = redisCommand(c, "AUTH %s", password);
     printf("AUTH: %s\n", reply->str);
     freeReplyObject(reply);
     /* PING server */
     reply = redisCommand(c,"PING");
     printf("PING: %s\n", reply->str);
     freeReplyObject(reply);
     /* Set a key */
     reply = redisCommand(c,"SET %s %s", "foo", "hello world");
     printf("SET: %s\n", reply->str);
     freeReplyObject(reply);
     /* Set a key using binary safe API */
     reply = redisCommand(c,"SET %b %b", "bar", (size_t) 3, "hello", (size_t) 5);
     printf("SET (binary API): %s\n", reply->str);
     freeReplyObject(reply);
     /* Try a GET and two INCR */
     reply = redisCommand(c,"GET foo");
```

```
     printf("GET foo: %s\n", reply->str);
     freeReplyObject(reply);
     reply = redisCommand(c,"INCR counter");
     printf("INCR counter: %lld\n", reply->integer);
     freeReplyObject(reply);
     /* again ... */
     reply = redisCommand(c,"INCR counter");
     printf("INCR counter: %lld\n", reply->integer);
     freeReplyObject(reply);
     /* Create a list of numbers, from 0 to 9 */
     reply = redisCommand(c,"DEL mylist");
     freeReplyObject(reply);
     for (j = 0; j < 10; j++) {
             char buf[64];
             snprintf(buf,64,"%d",j);
             reply = redisCommand(c,"LPUSH mylist element-%s", buf);
             freeReplyObject(reply);
```

`}`

```
     /* Let's check what we have inside the list */
     reply = redisCommand(c,"LRANGE mylist 0 -1");
     if (reply->type == REDIS_REPLY_ARRAY) {
             for (j = 0; j < reply->elements; j++) {
             printf("%u) %s\n", j, reply->element[j]->str);
```

`}` `}`

```
     freeReplyObject(reply);
     /* Disconnects and frees the context */
     redisFree(c);
     return 0;
```

`}`
3. Compile the code.

```
gcc -o example -g example.c -I /usr/local/include/hiredis -lhiredis
```

4. Run a test.

```
 example xxx.kvstore.aliyuncs.com 6379 instance_id password
```

Now, the C or C++ client is connected to the KVStore for Redis instance. .NET client To use a .NET client to connect to an KVStore for Redis instance, perform the following steps:
1. Download and use the .NET client.

```
 git clone https://github.com/ServiceStack/ServiceStack.Redis
```

2. Create a .NET project on the .NET client.
3. Add the reference file stored in the library file directory ServiceStack.Redis/lib/tests to the client.
4. Enter the following code in the .NET project to connect to the KVStore for Redis instance. For more
information about API operations, visit https://github.com/ServiceStack/ServiceStack.Redis.

```
using System; usingSystemCollectionsGeneric;
```

```
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
         string host = "127.0.0.1";/*IP address of the host that you want to connect to
```

`*/`

```
         string password = "password";/*Password*/
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
         "redis://password@127.0.0.1:6379"/*redis://Password@IP address that you want t
o connect to:Port*/
```

};

```
 RedisConfig.VerifyMasterConnections = false;//You must set the parameter.
 PooledRedisClientManager redisPoolManager = new PooledRedisClientManager(10/*Number of
connections in the pool*/, 10/*Connection pool timeout value*/, testReadWriteHosts);
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

`}` `}` `}` node-redis client To use a node-redis client to connect to an KVStore for Redis instance, perform the following steps:
1. Download and install a node-redis client.

```
npm install hiredis redis
```

2. Enter and run the following code on the node-redis client to connect to the KVStore for Redis
instance.

```
 var redis = require("redis"),
 client = redis.createClient(<port>, <"host">, {detect_buffers: true});
 client.auth("password", redis.print)
```

> Not e In the code, the port field specifies the port of the KVStore for Redis instance. Default value: 6379. The host field specifies the endpoint of the KVStore for Redis instance. The following example shows the settings of the port and host fields:

```
client = redis.createClient(6379, "r-abcdefg.redis.rds.aliyuncs.com", {detect_buffe rs: true});
```

3. Use the KVStore for Redis instance.

```
   // Write data to the instance.
 client.set("key", "OK");
 // Query data on the instance. The instance returns data of the String type.
 client.get("key", function (err, reply) {
 console.log(reply.toString()); // print `OK`
 });
 // If a buffer is imported, a buffer is returned.
 client.get(new Buffer("key"), function (err, reply) {
 console.log(reply.toString()); // print `<Buffer 4f 4b>`
 });
 client.quit();
```

C# client StackExchange.Redis To use the C# client StackExchange.Redis to connect to an KVStore for Redis instance, perform the following steps:
1. Download and install StackExchange. Redis.
2. Add a reference.

```
using StackExchange.Redis;
```

3. Initialize ConnectionMultiplexer.
ConnectionMultiplexer is the core of StackExchange.Redis, and shared and reused in the entire application. You must use ConnectionMultiplexer as a singleton. ConnectionMultiplexer is initialized in the following way:

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
             if (redisConn == null || ! redisConn.IsConnected)
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

> Not e
> ConfigurationOptions contains multiple options, such as keepAlive, connectRetry, and name. For more information, see StackExchange.Redis.ConfigurationOptions.

4. GetDatabase() returns a lightweight object. You can obtain this object from the object of
ConnectionMultiplexer.

```
 redisConn = getRedisConn();
 var db = redisConn.GetDatabase();
```

5. The following examples show five types of data structures, which are strings, hashes, lists, sets,
and sorted sets. The API operations used in these examples are different from their usage in the native Redis service. string

```
//set get string strKey = "hello"; string strValue = "world"; bool setResult = db.StringSet(strKey, strValue); Console.WriteLine("set " + strKey + " " + strValue + ", result is " + setResult); //incr string counterKey = "counter"; long counterValue = db.StringIncrement(counterKey); Console.WriteLine("incr " + counterKey + ", result is " + counterValue); //expire db.KeyExpire(strKey, new TimeSpan(0, 0, 5)); Thread.Sleep(5 * 1000); Console.WriteLine("expire " + strKey + ", after 5 seconds, value is " + db.StringGet( strKey)); //mset mget KeyValuePair<RedisKey, RedisValue> kv1 = new KeyValuePair<RedisKey, RedisValue>("key1 ", "value1"); KeyValuePair<RedisKey, RedisValue> kv2 = new KeyValuePair<RedisKey, RedisValue>("key2 ", "value2"); db.StringSet(new KeyValuePair<RedisKey, RedisValue>[] {kv1,kv2}); RedisValue[] values = db.StringGet(new RedisKey[] {kv1.Key, kv2.Key}); Console.WriteLine("mget " + kv1.Key.ToString() + " " + kv2.Key.ToString() + ", result is " + values[0] + "&&" + values[1]);
```

hash

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

list

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

set

```
//set key string setKey = "mySet"; //sadd db.SetAdd(setKey, "a"); db.SetAdd(setKey, "b"); db.SetAdd(setKey, "c"); //sismember bool isContains = db.SetContains(setKey, "a"); Console.WriteLine("set " + setKey + " contains a is " + isContains );
```

sorted set

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

You can use the Redis command-line interface (redis-cli) tool to connect to a KVStore for Redis instance.

> Not ice KVStore for Redis only supports connections over an internal network. Therefore, you must install redis-cli on an Elastic Compute Service (ECS) instance in the same VPC network as an KVStore for Redis instance, and connect the ECS instance to the KVStore for Redis instance to manage data.

Install redis-cli Install a Linux-based version of Redis to use redis-cli. For more information, visit the Redis official website. Prerequisites Connections over an internal network If the KVStore for Redis instance and the ECS instance run in a classic network, both instances must be deployed in the same region. You have added the internal IP address of the ECS instance to an whitelist of the KVStore for Redis instance. The operating system of the local host must be Linux. You have installed the Linux-based version of Redis on the ECS instance. Connect to a KVStore for Redis instance On the command line, run the following command to connect to the KVStore for Redis instance.

```
redis-cli -h <host> -p <port> -a <password>
```

Parameters

| Parameter | Description |
|---|---|
| -h | Specifies the endpoint of the KVStore for Redis instance. |
| -p | Specifies the service port of the KVStore for Redis instance. The default port number is 6379 and cannot be changed. |
| -a | Specifies the password used to connect to the KVStore for Redis instance. To enhance data security, you can skip this parameter to avoid revealing the password in plaintext. After you run the preceding command, you can enter auth <password> to complete the authentication. The following figure shows an example. |

Example

## 3 Instance management

### 3.1 Change the password

If you forget your password, need to change your password, or have not set a password for an instance, you can set a new password for the instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the upper-right corner of the Basic Inf ormat ion page, click Modif y Password.
4. In the Change Password dialog box that appears, set Old Password, New Password, Conf irm
Password.

> Not e
> If you forget your password, you can click Forgot password? in the Change Password dialog box. In the Reset Password dialog box that appears, you can set a new password.
> The password must be 8 to 32 characters in length.
> The password must contain characters from at least three of the following categories: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) _ + - =

### 3.2 Configure a whitelist

Before using a KVStore for Redis instance, add IP addresses or CIDR blocks used to access the database to the instance whitelist to improve database security and stability. Context

> Not e A properly configured whitelist can guarantee the highest-level security protection for your KVStore for Redis instance. We recommend that you maintain the whitelist on a regular basis.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, find the target instance. Click the instance ID or click Manage in the
Act ions column.
3. On the Inst ance Inf ormat ion page, click Whit elist Set t ings in the left-side navigation pane.
4. On the Whit elist Set t ings page, proceed in either of the following ways:
To customize the whitelist group name, create a new whitelist group: a. Click Add a Whit elist Group in the upper-right corner. b. In the Add a Whitelist Group dialog box that appears, set Group Name.

> Not e A group name must be 2 to 32 characters in length and contain lowercase letters, digits, or underscores (_). The group name must start with a lowercase letter and end with a letter or digit. You cannot change this name after you create the whitelist group.

If you do not require a custom whitelist group, click Modif y next to the target whitelist group.
5. In the Add a Whit elist Group or Modif y Whit elist of Group**​** dialog box that appears, proceed in
either of the following ways: Manually modify the Whit elist of Group field: a. In the Whit elist of Group field, enter the IP addresses or CIDR blocks that you can use to connect to the KVStore for Redis instance. Manually modify the whitelist group

> Not e
> Set the whitelist to `0.0.0.0/0` to allow connections from all IP addresses.
> Set the whitelist to `127.0.0.1` to block connections from all IP addresses.
> Set the whitelist to a CIDR block to allow connections from the IP addresses within the CIDR block, such as `10.10.10.0/24` .
> When you enter multiple IP addresses or CIDR blocks, separate them with commas (,) and leave no space before or after each comma.
> You can add 1,000 or fewer IP addresses or CIDR blocks to each whitelist group.

b. Click OK. Load internal IP addresses of target ECS instances under the current Alibaba Cloud account: a. Click Load ECS Int ernal IP Addresses. Load internal IP addresses of target ECS instances b. Select internal IP addresses of target ECS instances. Select internal IP addresses of target ECS instances

> Not e You can perform a fuzzy search by ECS instance name, ID, or IP address on the search bar above the list of ECS internal IP addresses.

c. Click OK.

### 3.3 Change configurations

This topic describes how to change the configuration of a KVStore for Redis instance. Context

> Not e After configuration changes have been completed, the system will migrate data and experience transient disconnection for a few seconds during this process. We recommend that you upgrade or downgrade the instance configuration during off-peak hours.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, find the target instance. Then, click the instance ID or click Change
Conf igurat ions in the Act ions column.
3. On the Change Conf igurat ions page, change the configurations and click Submit .
The following example provides common configurations:

| Configuration | Description |
|---|---|
| Architecture Type | The architecture type of the KVStore for Redis instance. KVStore for Redis provides cluster and standard architectures. The cluster architecture meets large-capacity or high-performance requirements. Native Redis databases run in a single-threading model. If your database does not require high performance, we recommend that you use a standard instance. To achieve higher performance, select a cluster instance. |
| Instance Class | The specification of the instance. The maximum number of connections and maximum internal bandwidth vary, depending on the instance specification. |

### 3.4 Set a maintenance window

You can modify the default maintenance window to perform maintenance on KVStore for Redis during off-peak hours. Context To ensure the stability of KVStore for Redis instances on the Alibaba Cloud platform, the backend system performs maintenance on instances and servers occasionally. To guarantee the stability of the maintenance process, instances will enter the Maintaining Instance status before the preset maintenance window on the day of maintenance. While an instance is in this state, data in the database can still be accessed and query operations such as performance monitoring are still available. However, change operations such as configuration change are temporarily unavailable for this instance in the console.

> Not e During the maintenance process, instances may be disconnected in the process of maintenance. We recommend that you set the maintenance window to a period during off-peak hours.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Set t ings to the right of the Maint enance Window
field in the Basic Inf ormat ion section.
4. Select time periods and click Save.

> Not e The time periods are in UTC+8.

### 3.5 Upgrade the minor version

Alibaba Cloud has continuously optimized the kernel of KVStore for Redis to fix security vulnerabilities and provide more stable services. You can upgrade the kernel version (minor version) of a KVStore for Redis instance with one click in the console. Context

> Not e
> We recommend that you upgrade instance versions during off-peak hours and ensure that your application supports automatic reconnection.
> The system automatically checks the kernel version of an instance. If the current version is the latest, the Minor Version Upgrade button in the upper-right corner of the Basic Inf ormat ion section for this instance will appear dimmed.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Minor Version Upgrade in the upper-right corner of the
Basic Inf ormat ion section.
4. In the Minor Version Upgrade dialog box that appears, click Upgrade Now.
On the Inst ance Inf ormat ion page, the instance status will become Upgrading a minor version. When the instance status returns to Available, the upgrade has been completed.

### 3.6 Configure SSL encryption

The standard and cluster Instances of Redis 2.8 and the cluster instances of Redis 4.0 support secure sockets layer (SSL) encryption. You can enable SSL encryption to ensure more secure data transmission. Context

> Not e SSL encryption may increase the network response time of instances. We recommend that you enable this feature only when necessary.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click SSL Set t ings.
4. In the upper-right corner of the SSL Set t ings page, click Conf igure SSL.
5. In the Conf igure SSL dialog box that appears, turn on the Enable switch. The switch will turn
from green to gray when it is enabled. Click OK. If an error message is displayed to indicate that the instance is in an abnormal state, click OK in the message that appears. If an error message is displayed to indicate that the feature is not supported in this version, upgrade the minor version of the instance. For more information, see Upgrade the minor version. After the operation, you must wait for a short period of time before the system displays the operation result. You can also click Updat e Validit y and Download CA Cert if icat e in the upper-right corner of the SSL Settings page to perform relevant operations.

### 3.7 Clear data

You can clear the data of a KVStore for Redis instance in the console. Context

> **Warning:** This operation will delete all data contained on an instance. Deleted data cannot be restored. Proceed with caution.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the upper-right corner of the Inst ance Inf ormat ion page, click Clear Dat a.
4. In the Clear Dat a message that appears, click OK.

### 3.8 Release an instance

You can release a KVStore for Redis instance at any time based on your business needs. This topic describes how to release a KVStore for Redis instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance List page, find the target instance. Then, click Release in the Act ions column.

> **Warning:** After an instance is released, it cannot be restored. Proceed with caution. We recommend that you back up your data before releasing the instance.

4. In the Release Inst ance message that appears, click OK.

### 3.9 Manage database accounts

KVStore for Redis allows you to create up to 20 database accounts for an instance. You can grant permissions to these accounts and manage your instance based on the actual needs to minimize misoperations. Prerequisites The engine version of the instance is Redis 4.0 or later.

> Not e If the engine version of the instance is not Redis 4.0, only the default account is available. The default account is created when you create the instance. For more information about how to change the password of the default account, see Change the password.

Context You can create accounts, delete accounts, reset the password, and change the permissions. After an account is created, you can use this account to log on to the database and use the command-line tool to perform operations on the database with the account and granted permissions. Create an account
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Instances page, find the instance that you want to manage and click the instance ID. By
default, the Inst ance Inf ormat ion page is displayed. In the left-side navigation pane, click Account Management .

> Not e If Account Management is not available for an instance of Redis 4.0 or later, you can try to upgrade the minor version. For more information, see Upgrade the minor version.

4. In the upper-right corner of the Account Management page, click Creat e.
5. In the Creat e Account dialog box that appears, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Account | Your account must meet the following requirements: The account name can contain lowercase letters, digits, underscores ( ), and _ hyphens (-). The name must start with a lowercase letter. The name must be 1 to 16 characters in length. |
| Privilege | The permissions granted to the account. Valid values: Read-only, Read/Write, and Replicate. If you select Replicate, you are authorized to use the SYNC and PSYNC commands after you connect to an instance with this account. Not e You can create accounts that have the replicate permission only for standard instances of Redis 4.0 or later. |

| Parameter | Description |
|---|---|
| Password Settings | The password of your account must meet the following requirements: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. Special characters include: ! @#$%^&*()+-= _ |
| Confirm Password | Enter the password again. |
| Description | The description of an account must meet the following requirements: The description can contain letters, Chinese characters, digits, underscores ( ), and _ hyphens (-). The description must start with a letter or Chinese character, and cannot start with http:// or https://. The description must be 2 to 256 characters in length. You can skip this parameter when you create an account. |

> Not e After you create an account, the account is in the Unavailable status. After about one minute, its status changes to Available.

### 3.10 Use a Lua script

KVStore for Redis instances of all editions support Lua commands. Support for Lua commands Lua scripts improve the performance of KVStore for Redis. With support for the Lua environment, KVStore for Redis is able to perform check-and-set (CAS) operations, allowing you to combine and run multiple commands in an efficient manner.

> Not e If the Eval command cannot be executed, such as when the " `ERR command eval not`
> `support for normal user` " message is displayed, you can try to Upgrade the minor version. During
> the upgrade, the instance may be disconnected and become read-only for a few seconds. We recommend that you upgrade the version of an instance during off-peak hours.

Limits on Lua scripts To ensure that all operations in a Lua script are performed within the same hash slot, the cluster edition of KVStore for Redis sets the following limits on a Lua script:

> Not e If you want to break the Lua limits of Redis Cluster and can ensure that all operations are performed in the same hash slot in the code, you can set the script_check_enable parameter to 0 in the console to disable the backend script check.

### 3.11 Restart an instance

You can restart an instance from the Instance List page of the console. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, find the target instance. Then, click Rest art in the Act ions column.

> Not ice During the restart, the instance may be disconnected for a few seconds. We recommend that you restart instances during off-peak hours and ensure that your application supports automatic reconnection.

3. In the dialog box that appears, select a restart time and click OK.
Restart Immediately: restarts the instance immediately. Restart Within Maintenance Window: restarts the instance within the preset maintenance window.

### 3.12 Export the list of instances

You can export the list of KVStore for Redis instances from the KVStore for Redis console for offline management. Procedure
1. Log on to the KVStore for Redis console.
2. In the upper-right corner of the Inst ance List page, click the Export Inst ances icon.
3. In the upper-right corner of the Inst ance List page, click the Export Inst ances icon.
4. In the Export Inst ance List dialog box that appears, select the columns to export and click OK.

> Not e After you click OK, the browser begins to download the CSV file. You can use Excel or a text editor to view this file.

t

## 4 Connection management

### 4.1 View connection strings

You can view the internal and public endpoints of instances in the KVStore for Redis console. Context

> Not e
> The virtual IP address of a KVStore for Redis instance may change when you maintain or modify the service. To ensure connection availability, we recommend that you use a connection string to access the KVStore for Redis instance.

For more information about how to apply for a public connection string, see Applies for a public connection string. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, view Int ernal Connect ion Address (Host ) and Public
Endpoint (Host ) in the Connect ion Inf ormat ion section.

### 4.2 Apply for a public endpoint

This topic describes how to apply for a public endpoint. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Apply f or Ext ernal IP Address in the Connect ion
Inf ormat ion section.
4. In the Apply f or Ext ernal IP Address dialog box that appears, enter an endpoint and port
number, and click OK.

> Not e
> The custom endpoint prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter.
> The custom port ranges from 1024 to 65535. The default value is 6379.
> After you apply for a public endpoint, you must add the public IP address to an IP address whitelist of the instance to connect to the instance over the Internet. For more information, see Configure a whitelist.

5. On the Inst ance Inf ormat ion page, view the Public Endpoint in the Connect ion Inf ormat ion
section. t

> Not e If a public endpoint is no longer needed, you can click Release Public Endpoint next to the Public Endpoint to release the endpoint.

### 4.3 Change the connection string of an instance

an instance KVStore for Redis allows you to modify internal and public endpoints for instances. When changing the KVStore for Redis instance, you can change the endpoint of the new instance to the endpoint of the original instance without modifying the application. Prerequisites The instance is in the Running state. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. On the Inst ance Inf ormat ion page, click Modif y Public Endpoint in the Connect ion
Inf ormat ion section.
4. In the Modif y Public Endpoint dialog box that appears, set Connect ion T ype, Endpoint , and
Port . Click OK.

> Not e
> The custom endpoint prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter.
> The custom port range is 1024 to 65535. The default value is 6379.
> If Connect ion T ype is set to Int ernal Address, you cannot set Port .

## 5 Parameter configuration

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

| psaraDB for Redis | User Guide·Parameter configuratio |
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

## 6 Backup and recovery

### 6.1 Back up data automatically

An increasing number of applications use KVStore for Redis for persistent storage. Because of this, KVStore for Redis supports routine backup mechanisms to restore data after misoperations occur. Alibaba Cloud provides secondary nodes to back up .rdb files as snapshots. Backup operations do not affect the performance of your instance. You can customize the backup operation in the console. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Backup and Recovery.
4. On the Backup and Recovery page, click the Backup Settings tab.
5. Click Edit to customize the automatic backup cycle and backup time.

> Not e Backup data is retained for seven days. You cannot modify this configuration.

6. Click OK.

### 6.2 Back up data manually

You can initiate a manual backup task in the console at any time. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Backup and Recovery.
4. In the upper-right corner of the Dat a Backup tab, click Creat e Backup.
5. In the message that appears, click Conf irm.

> Not e On the Dat a Backup tab, you can select a time range to query historical backup data. Backup data is retained for seven days, so you can query historical backup data in the past seven days.

### 6.3 Download backup files

To archive these backup files for a longer period, you can copy their URLs in the console and download the database backup files to a local directory. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Backup and Recovery.
4. On the Dat a Backup tab, select the backup set to be archived and click Download.
5. In the Download Backup File dialog box that appears, click one of the following buttons to
continue with the procedure: Download: downloads the backup file to a local directory. Get URL f or Int ernet : copies the public URL for downloading the backup file, and downloads the backup file over the Internet. Get URL f or Int ranet : copies the internal URL for downloading the backup file, and downloads the backup file over the internal network. Cancel: cancels downloading the backup file.

### 6.4 Restore data

You can use backup files to restore data in the console. Context

> Not ice
> Data restoration is highly risky. Check the data to be restored before performing this operation. Proceed with caution.
> This feature is not applicable to non-cluster KVStore for Redis instances.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Backup and Recovery.
4. On the Dat a Backup tab, select the target backup file and click Rest ore Dat a.
5. In the Rest ore Dat a dialog box that appears, click Cont inue.
You can apply backup files to a new instance by cloning an instance.

### 6.5 Clone an instance

You can apply backup files to a new instance by cloning an instance. Context

> Not e This feature is applicable to non-cluster KVStore for Redis instances.

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Backup and Recovery.
4. On the Dat a Backup tab, select the target backup set and click Clone Inst ance.
5. In the Clone Inst ance message that appears, click OK.

## 7 Performance monitoring

### 7.1 View monitoring data

You can query the monitoring data of a KVStore for Redis instance for a specified period within the last month. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Perf ormance Monit or.
4. On the Hist orical Monit oring Dat a page, click the calendar icon next to Query T ime.
5. Set a time range in which you want to query monitoring data and click OK.

> Not e For more information about the monitoring metrics, see Understand metrics.

### 7.2 Customize metrics

You can select the metrics to be displayed on the Historical Monitoring Data page of the KVStore for Redis console as needed. Context KVStore for Redis supports more than 10 groups of monitoring metrics. By default, the Performance Monitor page displays the monitoring metrics of the basic monitoring group. You can click the Custom Metrics button to switch to the metrics of other monitoring groups. The following table describes the monitoring groups.

| Monitoring group | Description |
|---|---|
| Basic monitoring group | The basic instance monitoring information, such as the QPS, bandwidth, and memory usage. |
| Key monitoring group | The monitoring information on the use of key-value related commands, such as the number of times DEL and EXITS are called. |
| String monitoring group | The monitoring information on the use of string-related commands, such as the number of times APPEND and MGET are called. |
| Hash monitoring group | The monitoring information on the use of hash-related commands, such as the number of times HGET and HDEL are called. |
| List monitoring group | The monitoring information on the use of list-related commands, such as the number of times BLPOP and BRPOP are called. |
| Set monitoring group | The monitoring information on the use of set-related commands, such as the number of times SADD and SCARD are called. |

| psaraDB for Redis | User Guide·Performance monitorin |
|---|---|

| Monitoring group | Description |
|---|---|
| Zset monitoring group | The monitoring information on the use of zset-related commands, such as the number of times ZADD and ZCARD are called. |
| HyperLog monitoring group | The monitoring information on the use of HyperLogLog-related commands, such as the number of times PFADD and PFCOUNT are called. |
| Pub/Sub monitoring group | The monitoring information on the use of publication and subscription-related commands, such as the number of times PUBLISH and SUBSCRIBE are called. |
| Transaction monitoring group | The monitoring information on the use of transaction-related commands, such as the number of times WATCH, MULTI, and EXEC are called. |
| Lua script monitoring group | The monitoring information on the use of Lua script-related commands, such as the number of times EVAL and SCRIPT are called. |

Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Perf ormance Monit or.
4. On the Hist orical Monit oring Dat a page, click Cust omize Met rics in the Dat a Index section.
5. In the Cust omize Met rics dialog box that appears, select the new monitoring group and click OK.

### 7.3 Modify monitoring frequency

KVStore for Redis console allows you to set the frequency at which monitoring data is collected. Context You can set the monitoring frequency to either 5 or 60 seconds to specify how often monitoring data to be collected by KVStore for Redis. The default monitoring time of 60 seconds is sufficient to meet common monitoring requirements. If you need to observe certain metrics at a higher frequency and lower latency, you can change the monitoring frequency to 5 seconds as described in the following section. Monitoring data does not occupy instance storage space, and collection of monitoring data does not affect normal running of the instance. Procedure
1. Log on to the KVStore for Redis console.
2. On the Inst ance List page, click the ID of the instance.
3. In the left-side navigation pane of the Inst ance Inf ormat ion page, click Perf ormance Monit or.
4. In the upper-right corner of the Hist orical Monit oring Dat a page, click Monit oring Frequency.
5. In the Monit oring Frequency dialog box that appears, select the new monitoring frequency and
click OK.

### 7.4 Monitoring metrics

KVStore for Redis monitors more than 10 groups of metrics in real time. This allows you to monitor the running status of KVStore for Redis instances. This topic describes these metrics. Basic monitoring metrics

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| CpuUsage | % | The CPU usage. | Monitor the CPU usage when collecting monitoring data. |
| UsedMemory | Bytes | The amount of the used memory. | Monitor the amount of the used memory when collecting monitoring data. |
| TotalQps | Counts/s | The number of requests received by an instance per second. | Divide the number of requests in a monitoring cycle by the number of seconds in the monitoring cycle. |
| ConnCount | Counts | The number of connections. | Monitor the number of connections when collecting monitoring data. |
| InFlow | KBps | The amount of data received by an instance per second. | Divide the amount of data received in a monitoring cycle by the number of seconds in the monitoring cycle. |
| OutFlow | KBps | The amount of data sent by an instance per second. | Divide the amount of data sent in a monitoring cycle by the number of seconds in the monitoring cycle. |
| FailedCount | Counts/s | The average number of abnormal requests per second. | Divide the total number of abnormal requests in a monitoring cycle by the number of seconds in the monitoring cycle. |
| AvgRt | us | The average response time of all requests. Not e For more information, see Response time (RT) metrics. | Divide the processing time of all requests in a monitoring cycle by the number of requests in the monitoring cycle. |

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| MaxRt | us | The maximum response time of requests. Not e For more information, see Response time (RT) metrics. | Monitor the maximum amount of time consumed for processing a single request in a monitoring cycle. |
| Keys | Counts | The total number of keys. | Monitor the number of keys when collecting monitoring data. |
| Expires | Counts | The total number of keys for which an expiration time is set. | Monitor the total number of keys for which an expiration time is set when collecting monitoring data. |
| ExpiredKeys | Counts | The total number of expired keys. | Monitor the cumulative sum when collecting monitoring data. After the instance is restarted, the cumulative sum is calculated again. |
| EvictedKeys | Counts | The total number of keys that are evicted because the memory is fully occupied. | Monitor the cumulative sum when collecting monitoring data. After the instance is restarted, the cumulative sum is calculated again. |
| request | Bytes | The total amount of request data received by KVStore for Redis nodes in a monitoring cycle. | See the description of this metric. |
| response | Bytes | The total amount of response data sent by KVStore for Redis nodes in a monitoring cycle. | See the description of this metric. |
| request max _ | Bytes | The maximum amount of data that a single request has in a monitoring cycle. | See the description of this metric. |

| Metric | Unit | Description | Statistical method |
|---|---|---|---|
| response max _ | Bytes | The maximum amount of data that a single response has in a monitoring cycle. | See the description of this metric. |
| traffic control input _ _ | Counts | The number of times that downstream throttling is triggered. | Monitor the cumulative sum in a monitoring cycle. |
| traffic control output _ _ | Counts | The number of times that upstream throttling is triggered. | Monitor the cumulative sum in a monitoring cycle. |
| traffic control input st _ _ _ atus | Counts | Indicates whether downstream throttling has been triggered in a monitoring cycle. A value of 0 indicates that throttling has not been triggered. A value of 1 indicates that throttling has been triggered. | See the description of this metric. |
| traffic control output _ _ _ status | Counts | Indicates whether upstream throttling has been triggered in a monitoring cycle. A value of 0 indicates that throttling has not been triggered. A value of 1 indicates that throttling has been triggered. | See the description of this metric. |
| hit rate _ | % | The request hit ratio. This metric indicates the probability that data exists in a KVStore for Redis instance when the data is requested. | Calculate the percentage of the hit requests to the total number of requests in a monitoring cycle. |
| hit | Counts | The number of hit requests. | Monitor the number of hit requests in a monitoring cycle. |
| miss | Counts | The number of missed requests. | Monitor the number of missed requests in a monitoring cycle. |
| evicted keys per sec _ _ _ | Counts/s | The number of keys that are evicted per second. | Divide the total number of keys evicted in a monitoring cycle by the number of seconds in the monitoring cycle. |

Other monitoring metrics The system also uses other monitoring metrics to monitor specific types of data or specific features. These monitoring metrics are classified into: Metrics that reflect the number of times that commands are used. For example, the del, dump, and exists metrics for keys monitoring indicate the number of times the DEL, DUMP, and EXISTS commands are used. Response time (RT) metrics of commands. For example, the metrics that end with avg_rt such as del_avg_rt dump_avg_rt, and exists_avg_rt in the key monitoring group are used to monitor the average response time of the DEL, DUMP, and EXISTS commands in a monitoring cycle. Response time (RT) metrics All groups of monitoring metrics include response time metrics. Such metrics end with Rt or rt. For example, the AvgRt and MaxRt metrics in the basic monitoring metrics or the del_avg_rt and exists_avg_rt metrics in the keys monitoring. The AvgRt and MaxRt metrics in the basic monitoring group are the most frequently used response time metrics. These metrics have different meanings for proxy nodes and data nodes. For a cluster instance or a read/write splitting instance, the AvgRt metric of a proxy node reflects the average time consumed by the proxy node to process all commands. A proxy node processes a command by following these steps: i. The proxy node receives a command and forwards the command to a data node. ii. The data node processes the command and responds to the proxy node. iii. The proxy node returns the command processing result. The AvgRt metric of the proxy node includes the amount of time consumed by the data node to process a command and the waiting time. It also includes the amount of time consumed for network communication between the proxy node and the data node. For data nodes of a cluster instance or a read/write splitting instance or for a standard instance, the AvgRt metric reflects the average time consumed by a data node to process all commands. This metric records the period from the time when the data node receives the command to the time when the data node returns the result. This metric does not include the time consumed by the proxy node to process a command and the time consumed for network communication. The MaxRt metric specifies the maximum response time of requests. The statistical method of this metric is similar to that of the AvgRt metric for all KVStore for Redis instances.
