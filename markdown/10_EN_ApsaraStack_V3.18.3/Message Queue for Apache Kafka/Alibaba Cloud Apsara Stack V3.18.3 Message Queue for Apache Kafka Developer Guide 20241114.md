---
title: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Developer Guide 20241114"
product_version: "V3.18.3"
doc_version: "20241114"
pdf_pages: 95
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Developer Guide 20241114.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97kafka/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Message%20Queue%20for%20Apache%20Kafka%20Developer%20Guide%2020241114.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Developer Guide 20241114

## Table of Contents

- 1 Demo projects
  - 1.1 Overview
  - 1.2 Prepare the environment
  - 1.3 Configure a demo project
  - 1.4 Run a demo
- 2 SDK reference
  - 2.1 SDK for Java
  - 2.2 SDK for Python
  - 2.3 SDK for C++
  - 2.4 SDK for Go
  - 2.5 SDK for PHP
  - 2.6 SDK for Ruby
  - 2.7 SDK for Node.js
- 3 API reference
  - 3.1 Common request parameters
  - 3.2 Common response parameters
  - 3.3 Use the domain name to access API operations
  - 3.4 Use the gateway signature to access API operations
  - 3.5 Instance management
    - 3.5.1 CreateInstance
    - 3.5.2 CreateDisasterRecoveryInstance
    - 3.5.3 DeleteDisasterRecoveryInstance
    - 3.5.4 CreateInstanceRelation
    - 3.5.5 GetInstanceConfig
    - 3.5.6 GetInstanceIdList
    - 3.5.7 DeleteInstance
    - 3.5.8 GetDisasterRecoveryInstanceList
    - 3.5.9 GetInstanceList
    - 3.5.10 GetInstanceRelationList
    - 3.5.11 GetInstanceStatus
    - 3.5.12 GetKafkaInstanceList
    - 3.5.13 ScaleInstance
    - 3.5.14 HotSwitchDisasterRecoveryInstance
    - 3.5.15 UpdateInstanceConfig
    - 3.5.16 UpdateInstanceName
    - 3.5.17 GetZoneList
  - 3.6 Topic management
    - 3.6.1 CreateTopic
    - 3.6.2 GetTopicList
    - 3.6.3 GetTopicListAll
    - 3.6.4 DeleteTopic
    - 3.6.5 GetTopicConfigList
    - 3.6.6 GetTopicListByConsumerId
    - 3.6.7 GetTopicQuotaTip
    - 3.6.8 GetTopicStatus
    - 3.6.9 GetTopicSubscribeStatus
    - 3.6.10 UpdateTopicConfig
    - 3.6.11 RebalanceTopic
    - 3.6.12 ModifyPartitionNum
  - 3.7 Group management
    - 3.7.1 GetConsumerList
    - 3.7.2 GetConsumerProgress
    - 3.7.3 GetConsumerProgressByTopic
    - 3.7.4 GetConsumerTimespan
  - 3.8 Message management
    - 3.8.1 QueryMessage
    - 3.8.2 DownloadMessage
    - 3.8.3 SendMessage
    - 3.8.4 ResetOffset
  - 3.9 Resource management
    - 3.9.1 DescribeCpuTypes
    - 3.9.2 GetPaasResource
    - 3.9.3 GetReplicatorList
    - 3.9.4 GetMetaData
    - 3.9.5 GetRegionList
    - 3.9.6 GetUnscheduledTaskList
  - 3.10 ACLs
    - 3.10.1 CreateACL
    - 3.10.2 DeleteAcl
    - 3.10.3 CreateSaslUser
    - 3.10.4 DeleteSaslUser
    - 3.10.5 DescribeAcls
    - 3.10.6 DescribeSaslUsers
    - 3.10.7 QueryExistedAclResource
  - 3.11 VIPs
    - 3.11.1 ApplyVipInfo
  - 3.12 Tags
    - 3.12.1 GetKafkaTagList

## 1 Demo projects

A demo is a sample program for messaging by using an SDK. This topic describes how to build a test project in ApsaraMQ for RocketMQ to send and receive messages by using the SDK for Java.

**Process**

The following items describe the process:
1. Prepare the environment: the preparations before you configure the demo project. The
preparations include installing an integrated development environment (IDE), downloading the demo project, installing the Java Development Kit (JDK), and creating topics.
2. Configure the demo project: the configurations of the demo project.
3. Run the demo: After you configure the demo project, you can run the demo to send and
receive messages.

### 1.1 Overview

A demo is a sample program for messaging by using an SDK. This topic describes how to build a test project in ApsaraMQ for Kafka to send and receive messages by using the SDK for Java.

**Process**

The following items describe the process:
1. Prepare the environment: the preparations before you configure the demo project. The
preparations include installing an integrated development environment (IDE), downloading the demo project, installing the Java Development Kit (JDK), and creating topics.
2. Configure the demo project: the configurations of the demo project.
3. Run the demo: After you configure the demo project, you can run the demo to send and
receive messages.

### 1.2 Prepare the environment

This topic describes the preparations before you configure a demo project. The preparations include installing an integrated development environment (IDE), downloading the demo project, installing the Java Development Kit (JDK), and creating topics.

**Install an IDE**

You can use IntelliJ IDEA or Eclipse as the IDE. In this topic, IntelliJ IDEA is used. Download IntelliJ IDEA Ultimate from https://www.jetbrains.com/idea/ and follow the instructions to install it.

**Download a demo project**

Go to the ApsaraMQ for Kafka demo library and click to download the demo project to your on-premises machine. After you decompress the package of the demo project, a folder named aliware-kafka-demos appears on your on-premises machine.

**Install the JDK**

If the JDK is not installed on your on-premises machine, visit Java Downloads to download JDK 1.8 or later and install it on your on-premises machine.

**Install Maven**

If Maven is not installed on your on-premises machine, visit Downloading Apache Maven to download Maven 2.5 or later and install it on your on-premises machine.

**Create topics**

You can create the required topics in the ApsaraMQ for Kafka console. For more information, see **Create topics** in ApsaraMQ for Kafka **User Guide**.

### 1.3 Configure a demo project

This topic describes how to configure a demo project.

**Procedure**

1. Import the demo project to IntelliJ IDEA.
i. On the IntelliJ IDEA interface, choose **New > Project From Existing Sources…** and then select the kafka-java-demo folder. ii. Select Maven. iii. Click **Finish** and wait until the project is imported. The project requires 2 to 3 minutes to be imported because the JAR dependency needs to be loaded to the demo project.
2. Configure the kafka.properties class based on the following sample code:

```
## Configure the endpoint. You can view the VIP information parameter in the Basic in
formation section of the Instance details tab in the ApsaraMQ for Kafka console to ob tain the endpoint. bootstrap.servers=xxxxxxxxxxxxxxxxxxxxx
## Configure a topic. Specify the name of the topic that you created in the ApsaraMQ
for Kafka console. topic=alikafka-topic-demo
## Configure a consumer group. ApsaraMQ for Kafka automatically creates a consumer gr
oup for you. group.id=CID-consumer-group-demo
```

### 1.4 Run a demo

After you configure a demo project, you can run the demo to send and receive messages. This topic describes how to run a demo to send and receive messages.

**Send messages**

1. Run the KafkaProducerDemo.java class to send messages.
2. Verify whether a message is sent.
i. Log on to the ApsaraMQ for Kafka console. For more information, see **Console**
**operations > Log on to the ApsaraMQ for Kafka console** in **ApsaraMQ for Kafka**
**User Guide**.
ii. On the **Instance List** page, find the instance that you want to manage and click **Details** in the **Operation** column. iii. On the **Instance details** page, click the **Topic management** tab and find the topic to which the message is sent to query whether the message is sent to the topic. If the message is sent to the topic, you can view the message in the query result.

**Subscribe to messages**

1. You can subscribe to messages by using one of the following methods:
Run the KafkaConsumerDemo.java class to subscribe to messages by using a single consumer. Run the KafkaMultiConsumerDemo.java class to subscribe to messages by using multiple consumers. After the class is successfully run, you can view logs that indicate the messages are consumed. Class initialization requires a few seconds to complete. In production environments, class initialization is seldom performed.
2. Query the consumption status.
i. Log on to the ApsaraMQ for Kafka console. For more information, see **Console**
**operations > Log on to the ApsaraMQ for Kafka console** in **ApsaraMQ for Kafka**
**User Guide**.
ii. On the **Instance List** page, find the instance that you want to manage and click **Details** in the **Operation** column. iii. On the Instance details page, click the **Group management** tab. On the **Group**
**management** tab, find the consumer group whose consumption status you want to
query and click **Consumption status** in the **Operation** column. If messages are successfully consumed, you can see that the started consumers are online and the subscriptions of the consumers are consistent.

## 2 SDK reference

This topic describes SDKs for multiple programming languages that are supported by ApsaraMQ for Kafka. ApsaraMQ for Kafka supports the following SDKs for multiple programming languages: For more information, see ApsaraMQ for Kafka demo library.

### 2.1 SDK for Java

This topic describes how to use the SDK for Java to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

Java Development Kit (JDK) 1.8 or later is installed. To install the latest version of JDK, see Java Downloads. Maven 2.5 or later is installed. To install the latest version of Maven, see Downloading Apache Maven.

**Install Java dependencies**

Add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>2.2.0</version>
</dependency> <dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.6</version>
</dependency>
```

> **Note:** We recommend that your client version be consistent with the major version of your ApsaraMQ for Kafka instance. You can view the major version of your ApsaraMQ for Kafka instance on the **Instance Details** page in the ApsaraMQ for Kafka console.

**Create configuration files**

1. Create a Log4j configuration file named log4j.properties.

```bash
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
```

`#`

```bash
#    http://www.apache.org/licenses/LICENSE-2.0
```

`#`

```bash
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
log4j.rootLogger=INFO, STDOUT log4j.appender.STDOUT=org.apache.log4j.ConsoleAppender log4j.appender.STDOUT.layout=org.apache.log4j.PatternLayout log4j.appender.STDOUT.layout.ConversionPattern=[%d] %p %m (%c)%n
```

2. Create a configuration file named kafka.properties for ApsaraMQ for Kafka.

```
## Configure the endpoint. You can view the endpoint of your ApsaraMQ for Kafka insta
nce in the ApsaraMQ for Kafka console. bootstrap.servers=xxxxxxxxxxxxxxxxxxxxx
## Configure a topic. You can create a topic in the ApsaraMQ for Kafka console.
topic=alikafka-topic-demo
## Configure a consumer group. ApsaraMQ for Kafka automatically creates a consumer gr
oup for you. group.id=CID-consumer-group-demo
```

3. Create a program named JavaKafkaConfigurer.java to load the configuration files.

```java
public class JavaKafkaConfigurer {
    private static Properties properties;
    public synchronized static Properties getKafkaProperties() {
       if (null != properties) {
           return properties;
       // Obtain the content of the kafka.properties file.
       Properties kafkaProperties = new Properties();
       try {
kafkaProperties.load(KafkaProducerDemo.class.getClassLoader().getResourceAsStream("kafk properties"));
       } catch (Exception e) {
           // If the file cannot be loaded, exit the program.
           e.printStackTrace();
       properties = kafkaProperties;
       return kafkaProperties;
```

**Send messages**

1. Create a producer program named KafkaProducerDemo.java.

```java
import java.util.ArrayList; import java.util.List; import java.util.Properties; import java.util.concurrent.Future; import java.util.concurrent.TimeUnit; import org.apache.kafka.clients.CommonClientConfigs; import org.apache.kafka.clients.producer.KafkaProducer; import org.apache.kafka.clients.producer.ProducerConfig; import org.apache.kafka.clients.producer.ProducerRecord; import org.apache.kafka.clients.producer.RecordMetadata; public class KafkaProducerDemo {
    public static void main(String args[]) {
        // Load the kafka.properties file.
        Properties kafkaProperties =  JavaKafkaConfigurer.getKafkaProperties();
        Properties props = new Properties();
        // Specify the endpoint. You can obtain the endpoint used to access the topic
on the Instance Details page in the ApsaraMQ for Kafka console.
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
kafkaProperties.getProperty("bootstrap.servers"));
        // The method for serializing messages in ApsaraMQ for Kafka.
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringSerializer");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringSerializer");
        // The maximum waiting time for a request.
        props.put(ProducerConfig.MAX_BLOCK_MS_CONFIG, 30 * 1000);
        // The maximum number of retries for messages on the client.
        props.put(ProducerConfig.RETRIES_CONFIG, 5);
        // The interval between two consecutive retries for messages on the client.
        props.put(ProducerConfig.RECONNECT_BACKOFF_MS_CONFIG, 3000);
        // Construct a thread-safe producer object. Construct one producer object for
a process.
        // To improve performance, you can construct multiple producer objects. We re
commend that you construct up to five producer objects.
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(pr
ops);
        // Create a message.
        String topic = kafkaProperties.getProperty("topic"); // The topic to which th
e message belongs. Enter the topic that you created in the ApsaraMQ for Kafka console
```

`.`

```
        String value = "this is the message's value"; // The message content.
        try {
            // Obtain multiple future objects at the same time. This helps improve
efficiency. However, do not obtain a large number of future objects at the same time.
```

```java
            List<Future<RecordMetadata>> futures = new
ArrayList<Future<RecordMetadata>>(128);
            for (int i =0; i < 100; i++) {
                // Send the message and obtain a future object.
                ProducerRecord<String, String> kafkaMessage =  new
ProducerRecord<String, String>(topic, value + ": " + i);
                Future<RecordMetadata> metadataFuture = producer.send(kafkaMessage);
                futures.add(metadataFuture);
            producer.flush();
            for (Future<RecordMetadata> future: futures) {
                // Obtain the results of the future object in a synchronous manner.
                try {
                    RecordMetadata recordMetadata = future.get();
                    System.out.println("Produce ok:" + recordMetadata.toString());
                } catch (Throwable t) {
                    t.printStackTrace();
        } catch (Exception e) {
            // If the message still fails to be sent after the maximum number of retri
es is reached, troubleshoot the error.
            System.out.println("error occurred");
            e.printStackTrace();
```

2. Compile and run KafkaProducerDemo.java to send messages.

**Subscribe to messages**

You can subscribe to messages by using one of the following methods: Use a single consumer to subscribe to messages i. Create a single-consumer program named KafkaConsumerDemo.java.

```java
import java.util.ArrayList; import java.util.List; import java.util.Properties; import org.apache.kafka.clients.consumer.ConsumerConfig; import org.apache.kafka.clients.consumer.ConsumerRecord; import org.apache.kafka.clients.consumer.ConsumerRecords; import org.apache.kafka.clients.consumer.KafkaConsumer; import org.apache.kafka.clients.producer.ProducerConfig; public class KafkaConsumerDemo {
    public static void main(String args[]) {
        // Load the kafka.properties file.
        Properties kafkaProperties =  JavaKafkaConfigurer.getKafkaProperties();
        Properties props = new Properties();
```

```java
        // Specify the endpoint. You can obtain the endpoint used to access the top
ic on the Instance Details page in the ApsaraMQ for Kafka console.
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
kafkaProperties.getProperty("bootstrap.servers"));
        // The maximum interval between two consecutive polling cycles.
        // The default value is 30 seconds. If the consumer does not return a heart
beat message within the interval, the broker determines that the consumer is not al ive. Then, the broker removes the consumer from the consumer group and triggers a rebalance.
        props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
        // The maximum number of messages that can be polled at the same time.
        // Do not set this parameter to an excessively large value. If all polled m
essages are not consumed before the next polling cycle starts, load balancing is tr iggered and performance may deteriorate.
        props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 30);
        // The method that is used to deserialize messages.
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringDeserializer");
        // The consumer instances that belong to the same consumer group. The insta
nces consume messages in load balancing mode.
        props.put(ConsumerConfig.GROUP_ID_CONFIG,
kafkaProperties.getProperty("group.id"));
        // Construct a message object, which is a consumer instance.
        KafkaConsumer<String, String> consumer = new
org.apache.kafka.clients.consumer.KafkaConsumer<String, String>(props);
        // Specify one or more topics to which the consumer group subscribes.
        // We recommend that you configure the consumers with the same
GROUP_ID_CONFIG value to subscribe to the same topics.
        List<String> subscribedTopics =  new ArrayList<String>();
        // If you want to subscribe to multiple topics, add the topics here.
        // You must create the topics in the ApsaraMQ for Kafka console in advance.
        String topicStr = kafkaProperties.getProperty("topic");
        String[] topics = topicStr.split(",");
        for (String topic: topics) {
            subscribedTopics.add(topic.trim());
        consumer.subscribe(subscribedTopics);
        // Consume messages in a loop.
        while (true){
            try {
                ConsumerRecords<String, String> records = consumer.poll(1000);
                // All messages must be consumed before the next polling cycle
starts. The total duration cannot exceed the interval specified by SESSION_TIMEOUT_ MS_CONFIG.
                // We recommend that you create a separate thread pool to consume
messages and return the results in an asynchronous manner.
                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(String.format("Consume partition:%d offset:%d
", record.partition(), record.offset()));
```

```
            } catch (Exception e) {
                try {
                    Thread.sleep(1000);
                } catch (Throwable ignore) {
                e.printStackTrace();
```

ii. Compile and run KafkaConsumerDemo.java to consume messages. Use multiple consumers to consume messages i. Create a multi-consumer program named KafkaMultiConsumerDemo.java.

```java
import java.util.ArrayList; import java.util.List; import java.util.Properties; import java.util.concurrent.atomic.AtomicBoolean; import org.apache.kafka.clients.consumer.ConsumerConfig; import org.apache.kafka.clients.consumer.ConsumerRecord; import org.apache.kafka.clients.consumer.ConsumerRecords; import org.apache.kafka.clients.consumer.KafkaConsumer; import org.apache.kafka.clients.producer.ProducerConfig; import org.apache.kafka.common.errors.WakeupException; /**
 * This tutorial shows you how to use multiple consumers to simultaneously consume
messages in one process.
 * Make sure that the total number of consumers in the environment does not exceed
the number of partitions of the topics to which the consumers subscribe.
```

`*/`

```java
public class KafkaMultiConsumerDemo {
    public static void main(String args[]) throws InterruptedException {
        // Load the kafka.properties file.
        Properties kafkaProperties = JavaKafkaConfigurer.getKafkaProperties();
        Properties props = new Properties();
        // Specify the endpoint. You can obtain the endpoint used to access the top
ic on the Instance Details page in the ApsaraMQ for Kafka console.
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
kafkaProperties.getProperty("bootstrap.servers"));
        // The maximum interval between two consecutive polling cycles.
        // The default value is 30 seconds. If the consumer does not return a heart
beat message within the interval, the broker determines that the consumer is not al ive. Then, the broker removes the consumer from the consumer group and triggers a rebalance.
        props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
        // The maximum number of messages that can be polled at the same time.
        // Do not set this parameter to an excessively large value. If all polled m
essages are not consumed before the next polling cycle starts, load balancing is tr iggered and performance may deteriorate.
```

```java
        props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 30);
        // The method that is used to deserialize messages.
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
"org.apache.kafka.common.serialization.StringDeserializer");
        // The consumer instances that belong to the same consumer group. The insta
nces consume messages in load balancing mode.
        props.put(ConsumerConfig.GROUP_ID_CONFIG,
kafkaProperties.getProperty("group.id"));
        int consumerNum = 2;
        Thread[] consumerThreads = new Thread[consumerNum];
        for (int i = 0; i < consumerNum; i++) {
            KafkaConsumer<String, String> consumer = new KafkaConsumer<String, Stri
ng>(props);
            List<String> subscribedTopics = new ArrayList<String>();
            subscribedTopics.add(kafkaProperties.getProperty("topic"));
            consumer.subscribe(subscribedTopics);
            KafkaConsumerRunner kafkaConsumerRunner = new
KafkaConsumerRunner(consumer);
            consumerThreads[i] = new Thread(kafkaConsumerRunner);
        for (int i = 0; i < consumerNum; i++) {
            consumerThreads[i].start();
        for (int i = 0; i < consumerNum; i++) {
            consumerThreads[i].join();
    static class KafkaConsumerRunner implements Runnable {
        private final AtomicBoolean closed = new AtomicBoolean(false);
        private final KafkaConsumer consumer;
        KafkaConsumerRunner(KafkaConsumer consumer) {
            this.consumer = consumer;
        @Override
        public void run() {
            try {
                while (!closed.get()) {
                    try {
                        ConsumerRecords<String, String> records =
consumer.poll(1000);
                        // All messages must be consumed before the next polling cyc
le starts. The total duration cannot exceed the interval specified by SESSION_TIMEO UT_MS_CONFIG.
                        for (ConsumerRecord<String, String> record : records) {
Systemoutprintln(Stringformat("Thread:%sConsumepart
```

```java
                            System.out.println(String.format("Thread:%s Consume part
ition:%d offset:%d", Thread.currentThread().getName(), record.partition(), record.o ffset()));
                    } catch (Exception e) {
                        try {
                            Thread.sleep(1000);
                        } catch (Throwable ignore) {
                        e.printStackTrace();
            } catch (WakeupException e) {
                // If the consumer is shut down, ignore the exception.
                if (!closed.get()) {
                    throw e;
            } finally {
                consumer.close();
        // Implement a shutdown hook that can be called by another thread.
        public void shutdown() {
            closed.set(true);
            consumer.wakeup();
```

ii. Compile and run KafkaMultiConsumerDemo.java to consume messages.

**References**

For information about the sample code of SDKs for other programming languages, see ApsaraMQ for Kafka demo library.

### 2.2 SDK for Python

This topic describes how to use the SDK for Python to connect to ApsaraMQ for Kafka to send and receive messages.

**Background information**

Python is installed. For more information, see Python.

> **Note:** Python 2.7, 3.4, 3.5, 3.6, and 3.7 are supported.

pip is installed. For more information, see Installation.

**Install the Python library**

Run the following command to install the Python library:

```
pip install kafka-python
```

**Create a configuration file**

Create a configuration file named setting.py for ApsaraMQ for Kafka.

```json
kafka_setting = {
    'bootstrap_servers': ["XXX", "XXX", "XXX"],
    'topic_name': 'XXX',
    'consumer_id': 'XXX'
```

| Parameter | Description |
|---|---|
| bootstrap servers _ | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
| topic name _ | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
| consumer id _ | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |

**Send messages**

1. Create a producer program named aliyun_kafka_producer.py.

```java
#!/usr/bin/env python
# encoding: utf-8
import socket from kafka import KafkaProducer from kafka.errors import KafkaError import setting conf = setting.kafka_setting print conf producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'],
                        api_version = (0,10),
                        retries=5)
partitions = producer.partitions_for(conf['topic_name']) print 'Partitions in the topic: %s' % partitions try:
    future = producer.send(conf['topic_name'], 'hello aliyun-kafka!')
    future.get()
    print 'send message succeed.'
except KafkaError, e:
    print 'send message failed.'
    print e
```

2. Run the following command to send messages:

```
python aliyun_kafka_producer.py
```

**Subscribe to messages**

1. Create a consumer program named aliyun_kafka_consumer.py.

```java
#!/usr/bin/env python
# encoding: utf-8
import socket from kafka import KafkaConsumer from kafka.errors import KafkaError import setting conf = setting.kafka_setting consumer = KafkaConsumer(bootstrap_servers=conf['bootstrap_servers'],
                        group_id=conf['consumer_id'],
                        api_version = (0,10,2),
                        session_timeout_ms=25000,
                        max_poll_records=100,
                        fetch_max_bytes=1 * 1024 * 1024)
print 'consumer start to consuming...' consumer.subscribe((conf['topic_name'], )) for message in consumer:
    print message.topic, message.offset, message.key, message.value, message.value, m
essage.partition
```

2. Run the following command to subscribe to messages:

```
python aliyun_kafka_consumer.py
```

### 2.3 SDK for C++

This topic describes how to use the SDK for C++ to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

GNU Compiler Collection (GCC) is installed. For more information, see Installing GCC.

**Install the C++ library**

1. Run the following command to switch to the /etc/yum.repos.d/ yum repository directory:

```
cd /etc/yum.repos.d/
```

2. Create a yum repository configuration file named confluent.repo.

```
[Confluent.dist] name=Confluent repository (dist) baseurl=https://packages.confluent.io/rpm/5.1/7 gpgcheck=1 gpgkey=https://packages.confluent.io/rpm/5.1/archive.key enabled=1 [Confluent] name=Confluent repository baseurl=https://packages.confluent.io/rpm/5.1 gpgcheck=1 gpgkey=https://packages.confluent.io/rpm/5.1/archive.key enabled=1
```

3. Run the following command to install the C++ library:

```bash
yum install librdkafka-devel
```

**Send messages**

1. Create a producer program named kafka_producer.c.
`/*`

```
 * librdkafka - Apache Kafka C library
```

`*`

```
 * Copyright (c) 2017, Magnus Edenhill
 * All rights reserved.
```

`*`

```
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
```

`*`

```
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
```

`*`

```
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
```

`*/`

```
/**
 * Simple Apache Kafka producer
 * using the Kafka driver from librdkafka
 * (https://github.com/edenhill/librdkafka)
```

`*/`

```
#include <stdio.h>
#include <signal.h>
#include <string.h>
/* Typical include path would be <librdkafka/rdkafka.h>, but this program
 * is builtin from within the librdkafka source tree and thus differs. */
#include "librdkafka/rdkafka.h"
static int run = 1; /**
 * @brief Signal termination of program
```

`*/`

```
static void stop (int sig) {
        run = 0;
        fclose(stdin); /* abort fgets() */
/**
 * @brief Message delivery report callback.
```

`*`

```
 * This callback is called exactly once per message, indicating if
 * the message was succesfully delivered
 * (rkmessage->err == RD_KAFKA_RESP_ERR_NO_ERROR) or permanently
 * failed delivery (rkmessage->err != RD_KAFKA_RESP_ERR_NO_ERROR).
```

`*`

```
 * The callback is triggered from rd_kafka_poll() and executes on
 * the application's thread.
```

`*/`

```
static void dr_msg_cb (rd_kafka_t *rk,
                       const rd_kafka_message_t *rkmessage, void *opaque) {
        if (rkmessage->err)
                fprintf(stderr, "%% Message delivery failed: %s\n",
                        rd_kafka_err2str(rkmessage->err));
        else
                fprintf(stderr,
                        "%% Message delivered (%zd bytes, "
                        "partition %"PRId32")\n",
                        rkmessage->len, rkmessage->partition);
        /* The rkmessage is destroyed automatically by librdkafka */
int main (int argc, char **argv) {
        rd_kafka_t *rk;         /* Producer instance handle */
        rd_kafka_topic_t *rkt;  /* Topic object */
        rd_kafka_conf_t *conf;  /* Temporary configuration object */
        char errstr[512];       /* librdkafka API error reporting buffer */
```

```
        char buf[512];          /* Message value temporary buffer */
        const char *brokers;    /* Argument: broker list */
        const char *topic;      /* Argument: topic to produce to */
```

`/*`

```
         * Argument validation
```

`*/`

```
        if (argc != 3) {
                fprintf(stderr, "%% Usage: %s <broker> <topic>\n", argv[0]);
                return 1;
        brokers = argv[1];
        topic   = argv[2];
```

`/*`

```
         * Create Kafka client configuration place-holder
```

`*/`

```
        conf = rd_kafka_conf_new();
        /* Set bootstrap broker(s) as a comma-separated list of
         * host or host:port (default port 9092).
         * librdkafka will use the bootstrap brokers to acquire the full
         * set of brokers from the cluster. */
        if (rd_kafka_conf_set(conf, "bootstrap.servers", brokers,
                              errstr, sizeof(errstr)) != RD_KAFKA_CONF_OK) {
                fprintf(stderr, "%s\n", errstr);
                return 1;
        /* Set the delivery report callback.
         * This callback will be called once per message to inform
         * the application if delivery succeeded or failed.
         * See dr_msg_cb() above. */
        rd_kafka_conf_set_dr_msg_cb(conf, dr_msg_cb);
```

`/*`

```
         * Create producer instance.
```

`*`

```
         * NOTE: rd_kafka_new() takes ownership of the conf object
         *       and the application must not reference it again after
         *       this call.
```

`*/`

```
        rk = rd_kafka_new(RD_KAFKA_PRODUCER, conf, errstr, sizeof(errstr));
        if (!rk) {
                fprintf(stderr,
                        "%% Failed to create new producer: %s\n", errstr);
                return 1;
        /* Create topic object that will be reused for each message
```

```
         * produced.
```

`*`

```
         * Both the producer instance (rd_kafka_t) and topic objects (topic_t)
         * are long-lived objects that should be reused as much as possible.
```

`*/`

```
        rkt = rd_kafka_topic_new(rk, topic, NULL);
        if (!rkt) {
                fprintf(stderr, "%% Failed to create topic object: %s\n",
                        rd_kafka_err2str(rd_kafka_last_error()));
                rd_kafka_destroy(rk);
                return 1;
        /* Signal handler for clean shutdown */
        signal(SIGINT, stop);
        fprintf(stderr,
                "%% Type some text and hit enter to produce message\n"
                "%% Or just hit enter to only serve delivery reports\n"
                "%% Press Ctrl-C or Ctrl-D to exit\n");
        while (run && fgets(buf, sizeof(buf), stdin)) {
                size_t len = strlen(buf);
                if (buf[len-1] == '\n') /* Remove newline */
                        buf[--len] = '\0';
                if (len == 0) {
                        /* Empty line: only serve delivery reports */
                        rd_kafka_poll(rk, 0/*non-blocking */);
                        continue;
```

`/*`

```
                 * Send/Produce message.
                 * This is an asynchronous call, on success it will only
                 * enqueue the message on the internal producer queue.
                 * The actual delivery attempts to the broker are handled
                 * by background threads.
                 * The previously registered delivery report callback
                 * (dr_msg_cb) is used to signal back to the application
                 * when the message has been delivered (or failed).
```

`*/`

```
        retry:
                if (rd_kafka_produce(
                            /* Topic object */
                            rkt,
                            /* Use builtin partitioner to select partition*/
                            RD_KAFKA_PARTITION_UA,
                            /* Make a copy of the payload. */
                            RD_KAFKA_MSG_F_COPY,
                            /* Message payload (value) and length */
                            buf, len,
                            /* Optional key and its length */
NULL
```

```
                            NULL, 0,
                            /* Message opaque, provided in
                             * delivery report callback as
                             * msg_opaque. */
                            NULL) == -1) {
                        /**
                         * Failed to *enqueue* message for producing.
```

`*/`

```
                        fprintf(stderr,
                                "%% Failed to produce to topic %s: %s\n",
                                rd_kafka_topic_name(rkt),
                                rd_kafka_err2str(rd_kafka_last_error()));
                        /* Poll to handle delivery reports */
                        if (rd_kafka_last_error() ==
                            RD_KAFKA_RESP_ERR__QUEUE_FULL) {
                                /* If the internal queue is full, wait for
                                 * messages to be delivered and then retry.
                                 * The internal queue represents both
                                 * messages to be sent and messages that have
                                 * been sent or failed, awaiting their
                                 * delivery report callback to be called.
```

`*`

```
                                 * The internal queue is limited by the
                                 * configuration property
                                 * queue.buffering.max.messages */
                                rd_kafka_poll(rk, 1000/*block for max 1000ms*/);
                                goto retry;
                } else {
                        fprintf(stderr, "%% Enqueued message (%zd bytes) "
                                "for topic %s\n",
                                len, rd_kafka_topic_name(rkt));
                /* A producer application should continually serve
                 * the delivery report queue by calling rd_kafka_poll()
                 * at frequent intervals.
                 * Either put the poll call in your main loop, or in a
                 * dedicated thread, or call it after every
                 * rd_kafka_produce() call.
                 * Just make sure that rd_kafka_poll() is still called
                 * during periods where you are not producing any messages
                 * to make sure previously produced messages have their
                 * delivery report callback served (and any other callbacks
                 * you register). */
                rd_kafka_poll(rk, 0/*non-blocking*/);
        /* Wait for final messages to be delivered or fail.
         * rd_kafka_flush() is an abstraction over rd_kafka_poll() which
         * waits for all messages to be delivered. */
fprintf(stderr "%%Flushingfinalmessages \n");
```

```
        fprintf(stderr, %% Flushing final messages..\n);
        rd_kafka_flush(rk, 10*1000 /* wait for max 10 seconds */);
        /* Destroy topic object */
        rd_kafka_topic_destroy(rkt);
        /* Destroy the producer instance */
        rd_kafka_destroy(rk);
        return 0;
```

2. Run the following command to compile kafka_producer.c:

```
gcc -lrdkafka ./kafka_producer.c -o kafka_producer
```

3. Run the following command to send messages:

```
./kafka_producer <bootstrap_servers> <topic>
```

| Parameter | Description |
|---|---|
| bootstrap servers _ | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
| topic | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |

**Subscribe to messages**

1. Create a consumer program named kafka_consumer.c.
`/*`

```
 * librdkafka - Apache Kafka C library
```

`*`

```
 * Copyright (c) 2015, Magnus Edenhill
 * All rights reserved.
```

`*`

```
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
```

`*`

```
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
```

`*`

```
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
```

```
SSO
```

`S` `O` `B` `CO` `G` `O` `S` `CO`

```
BUOS
```

`S` `S`

```
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
```

`*/`

```
/**
 * Apache Kafka high level consumer example program
 * using the Kafka driver from librdkafka
 * (https://github.com/edenhill/librdkafka)
```

`*/`

```
#include <ctype.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <syslog.h>
#include <sys/time.h>
#include <errno.h>
#include <getopt.h>
/* Typical include path would be <librdkafka/rdkafka.h>, but this program
 * is builtin from within the librdkafka source tree and thus differs. */
#include "librdkafka/rdkafka.h"  /* for Kafka driver */
static int run = 1; static rd_kafka_t *rk; static int exit_eof = 0; static int wait_eof = 0; /* number of partitions awaiting EOF */ static int quiet = 0; static enum {
    OUTPUT_HEXDUMP,
    OUTPUT_RAW,
} output = OUTPUT_HEXDUMP; static void stop (int sig) {
        if (!run)
                exit(1);
    run = 0;
    fclose(stdin); /* abort fgets() */
static void hexdump (FILE *fp, const char *name, const void *ptr, size_t len) {
    const char *p = (const char *)ptr;
    unsigned int of = 0;
```

```
    if (name)
        fprintf(fp, "%s hexdump (%zd bytes):\n", name, len);
    for (of = 0 ; of < len ; of += 16) {
        char hexen[16*3+1];
        char charen[16+1];
        int hof = 0;
        int cof = 0;
        int i;
        for (i = of ; i < (int)of + 16 && i < (int)len ; i++) {
            hof += sprintf(hexen+hof, "%02x ", p[i] & 0xff);
            cof += sprintf(charen+cof, "%c",
                       isprint((int)p[i]) ?  p[i] : '.');
        fprintf(fp, "%08x: %-48s %-16s\n",
            of, hexen, charen);
/**
 * Kafka logger callback (optional)
```

`*/`

```
static void logger (const rd_kafka_t *rk, int level,
            const char *fac, const char *buf) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    fprintf(stdout, "%u.%03u RDKAFKA-%i-%s: %s: %s\n",
        (int)tv.tv_sec, (int)(tv.tv_usec / 1000),
        level, fac, rd_kafka_name(rk), buf);
/**
 * Handle and print a consumed message.
 * Internally crafted messages are also used to propagate state from
 * librdkafka to the application. The application needs to check
 * the `rkmessage->err` field for this purpose.
```

`*/`

```
static void msg_consume (rd_kafka_message_t *rkmessage) {
    if (rkmessage->err) {
        if (rkmessage->err == RD_KAFKA_RESP_ERR__PARTITION_EOF) {
            fprintf(stderr,
                "%% Consumer reached end of %s [%"PRId32"] "
                   "message queue at offset %"PRId64"\n",
                   rd_kafka_topic_name(rkmessage->rkt),
                   rkmessage->partition, rkmessage->offset);
            if (exit_eof && --wait_eof == 0) {
                                fprintf(stderr,
```

```
                                        "%% All partition(s) reached EOF: "
                                        "exiting\n");
                run = 0;
            return;
                if (rkmessage->rkt)
                        fprintf(stderr, "%% Consume error for "
                                "topic \"%s\" [%"PRId32"] "
                                "offset %"PRId64": %s\n",
                                rd_kafka_topic_name(rkmessage->rkt),
                                rkmessage->partition,
                                rkmessage->offset,
                                rd_kafka_message_errstr(rkmessage));
                else
                        fprintf(stderr, "%% Consumer error: %s: %s\n",
                                rd_kafka_err2str(rkmessage->err),
                                rd_kafka_message_errstr(rkmessage));
                if (rkmessage->err == RD_KAFKA_RESP_ERR__UNKNOWN_PARTITION ||
                    rkmessage->err == RD_KAFKA_RESP_ERR__UNKNOWN_TOPIC)
                        run = 0;
        return;
    if (!quiet)
        fprintf(stdout, "%% Message (topic %s [%"PRId32"], "
                        "offset %"PRId64", %zd bytes):\n",
                        rd_kafka_topic_name(rkmessage->rkt),
                        rkmessage->partition,
            rkmessage->offset, rkmessage->len);
    if (rkmessage->key_len) {
        if (output == OUTPUT_HEXDUMP)
            hexdump(stdout, "Message Key",
                rkmessage->key, rkmessage->key_len);
        else
            printf("Key: %.*s\n",
                   (int)rkmessage->key_len, (char *)rkmessage->key);
    if (output == OUTPUT_HEXDUMP)
        hexdump(stdout, "Message Payload",
            rkmessage->payload, rkmessage->len);
    else
        printf("%.*s\n",
               (int)rkmessage->len, (char *)rkmessage->payload);
static void print_partition_list (FILE *fp,
                                  const rd_kafka_topic_partition_list_t
```

```
                                  *partitions) {
        int i;
        for (i = 0 ; i < partitions->cnt ; i++) {
                fprintf(stderr, "%s %s [%"PRId32"] offset %"PRId64,
                        i > 0 ?  ",":"",
                        partitions->elems[i].topic,
                        partitions->elems[i].partition,
            partitions->elems[i].offset);
        fprintf(stderr, "\n");
static void rebalance_cb (rd_kafka_t *rk,
                          rd_kafka_resp_err_t err,
              rd_kafka_topic_partition_list_t *partitions,
                          void *opaque) {
    fprintf(stderr, "%% Consumer group rebalanced: ");
    switch (err)
```

`{`

```
    case RD_KAFKA_RESP_ERR__ASSIGN_PARTITIONS:
        fprintf(stderr, "assigned:\n");
        print_partition_list(stderr, partitions);
        rd_kafka_assign(rk, partitions);
        wait_eof += partitions->cnt;
        break;
    case RD_KAFKA_RESP_ERR__REVOKE_PARTITIONS:
        fprintf(stderr, "revoked:\n");
        print_partition_list(stderr, partitions);
        rd_kafka_assign(rk, NULL);
        wait_eof = 0;
        break;
    default:
        fprintf(stderr, "failed: %s\n",
                        rd_kafka_err2str(err));
                rd_kafka_assign(rk, NULL);
        break;
static int describe_groups (rd_kafka_t *rk, const char *group) {
        rd_kafka_resp_err_t err;
        const struct rd_kafka_group_list *grplist;
        int i;
        err = rd_kafka_list_groups(rk, group, &grplist, 10000);
        if (err) {
                fprintf(stderr, "%% Failed to acquire group list: %s\n",
                        rd_kafka_err2str(err));
return
```

1;

```
                return -1;
        for (i = 0 ; i < grplist->group_cnt ; i++) {
                const struct rd_kafka_group_info *gi = &grplist->groups[i];
                int j;
                printf("Group \"%s\" in state %s on broker %d (%s:%d)\n",
                       gi->group, gi->state,
                       gi->broker.id, gi->broker.host, gi->broker.port);
                if (gi->err)
                        printf(" Error: %s\n", rd_kafka_err2str(gi->err));
                printf(" Protocol type \"%s\", protocol \"%s\", "
                       "with %d member(s):\n",
                       gi->protocol_type, gi->protocol, gi->member_cnt);
                for (j = 0 ; j < gi->member_cnt ; j++) {
                        const struct rd_kafka_group_member_info *mi;
                        mi = &gi->members[j];
                        printf("  \"%s\", client id \"%s\" on host %s\n",
                               mi->member_id, mi->client_id, mi->client_host);
                        printf("    metadata: %d bytes\n",
                               mi->member_metadata_size);
                        printf("    assignment: %d bytes\n",
                               mi->member_assignment_size);
                printf("\n");
        if (group && !grplist->group_cnt)
                fprintf(stderr, "%% No matching group (%s)\n", group);
        rd_kafka_group_list_destroy(grplist);
        return 0;
static void sig_usr1 (int sig) {
    rd_kafka_dump(stdout, rk);
int main (int argc, char **argv) {
        char mode = 'C';
    char *brokers = "localhost:9092";
    int opt;
    rd_kafka_conf_t *conf;
    rd_kafka_topic_conf_t *topic_conf;
    char errstr[512];
    const char *debug = NULL;
    int do_conf_dump = 0;
    char tmp[16];
rdkafkaresperrterr;
```

```
        rd_kafka_resp_err_t err;
        char *group = NULL;
        rd_kafka_topic_partition_list_t *topics;
        int is_subscription;
        int i;
    quiet = !isatty(STDIN_FILENO);
    /* Kafka configuration */
    conf = rd_kafka_conf_new();
        /* Set logger */
        rd_kafka_conf_set_log_cb(conf, logger);
    /* Quick termination */
    snprintf(tmp, sizeof(tmp), "%i", SIGIO);
    rd_kafka_conf_set(conf, "internal.termination.signal", tmp, NULL, 0);
    /* Topic configuration */
    topic_conf = rd_kafka_topic_conf_new();
    while ((opt = getopt(argc, argv, "g:b:qd:eX:ADO")) != -1) {
        switch (opt) {
        case 'b':
            brokers = optarg;
            break;
                case 'g':
                        group = optarg;
                        break;
        case 'e':
            exit_eof = 1;
            break;
        case 'd':
            debug = optarg;
            break;
        case 'q':
            quiet = 1;
            break;
        case 'A':
            output = OUTPUT_RAW;
            break;
        case 'X':
```

`{`

```
            char *name, *val;
            rd_kafka_conf_res_t res;
            if (!strcmp(optarg, "list") ||
                !strcmp(optarg, "help")) {
                rd_kafka_conf_properties_show(stdout);
                exit(0);
            if (!strcmp(optarg, "dump")) {
                do_conf_dump = 1;
                continue;
```

```
            name = optarg;
            if (!(val = strchr(name, '='))) {
                fprintf(stderr, "%% Expected "
                    "-X property=value, not %s\n", name);
                exit(1);
            *val = '\0';
            val++;
            res = RD_KAFKA_CONF_UNKNOWN;
            /* Try "topic." prefixed properties on topic
             * conf first, and then fall through to global if
             * it didnt match a topic configuration property. */
            if (!strncmp(name, "topic.", strlen("topic.")))
                res = rd_kafka_topic_conf_set(topic_conf,
                                  name+
                                  strlen("topic."),
                                  val,
                                  errstr,
                                  sizeof(errstr));
            if (res == RD_KAFKA_CONF_UNKNOWN)
                res = rd_kafka_conf_set(conf, name, val,
                            errstr, sizeof(errstr));
            if (res != RD_KAFKA_CONF_OK) {
                fprintf(stderr, "%% %s\n", errstr);
                exit(1);
        break;
                case 'D':
                case 'O':
                        mode = opt;
                        break;
        default:
            goto usage;
    if (do_conf_dump) {
        const char **arr;
        size_t cnt;
        int pass;
        for (pass = 0 ; pass < 2 ; pass++) {
            if (pass == 0) {
                arr = rd_kafka_conf_dump(conf, &cnt);
```

```
                printf("# Global config\n");
            } else {
                printf("# Topic config\n");
                arr = rd_kafka_topic_conf_dump(topic_conf,
                                   &cnt);
            for (i = 0 ; i < (int)cnt ; i += 2)
                printf("%s = %s\n",
                       arr[i], arr[i+1]);
            printf("\n");
            rd_kafka_conf_dump_free(arr, cnt);
        exit(0);
    if (strchr("OC", mode) && optind == argc) {
    usage:
        fprintf(stderr,
            "Usage: %s [options] <topic[:part]> <topic[:part]>..\n"
            "\n"
            "librdkafka version %s (0x%08x)\n"
            "\n"
            " Options:\n"
                        "  -g <group>      Consumer group (%s)\n"
            "  -b <brokers>    Broker address (%s)\n"
            "  -e              Exit consumer when last message\n"
            "                  in partition has been received.\n"
                        "  -D              Describe group.\n"
                        "  -O              Get commmitted offset(s)\n"
            "  -d [facs..]     Enable debugging contexts:\n"
            "                  %s\n"
            "  -q              Be quiet\n"
            "  -A              Raw payload output (consumer)\n"
            "  -X <prop=name> Set arbitrary librdkafka "
            "configuration property\n"
            "               Properties prefixed with \"topic.\" "
            "will be set on topic object.\n"
            "               Use '-X list' to see the full list\n"
            "               of supported properties.\n"
            "\n"
                        "For balanced consumer groups use the 'topic1 topic2..'"
                        " format\n"
                        "and for static assignment use "
                        "'topic1:part1 topic1:part2 topic2:part1..'\n"
            "\n",
            argv[0],
            rd_kafka_version_str(), rd_kafka_version(),
                        group, brokers,
            RD_KAFKA_DEBUG_CONTEXTS);
```

```
        exit(1);
    signal(SIGINT, stop);
    signal(SIGUSR1, sig_usr1);
    if (debug &&
        rd_kafka_conf_set(conf, "debug", debug, errstr, sizeof(errstr)) !=
        RD_KAFKA_CONF_OK) {
        fprintf(stderr, "%% Debug configuration failed: %s: %s\n",
            errstr, debug);
        exit(1);
```

`/*`

```
         * Client/Consumer group
```

`*/`

```
        if (strchr("CO", mode)) {
                /* Consumer groups require a group id */
                if (!group)
                        group = "rdkafka_consumer_example";
                if (rd_kafka_conf_set(conf, "group.id", group,
                                      errstr, sizeof(errstr)) !=
                    RD_KAFKA_CONF_OK) {
                        fprintf(stderr, "%% %s\n", errstr);
                        exit(1);
                /* Consumer groups always use broker based offset storage */
                if (rd_kafka_topic_conf_set(topic_conf, "offset.store.method",
                                            "broker",
                                            errstr, sizeof(errstr)) !=
                    RD_KAFKA_CONF_OK) {
                        fprintf(stderr, "%% %s\n", errstr);
                        exit(1);
                /* Set default topic config for pattern-matched topics. */
                rd_kafka_conf_set_default_topic_conf(conf, topic_conf);
                /* Callback called on partition assignment changes */
                rd_kafka_conf_set_rebalance_cb(conf, rebalance_cb);
                rd_kafka_conf_set(conf, "enable.partition.eof", "true",
                                  NULL, 0);
        /* Create Kafka handle */
        if (!(rk = rd_kafka_new(RD_KAFKA_CONSUMER, conf,
                                errstr, sizeof(errstr)))) {
                fprintf(stderr,
                        "%% Failed to create new consumer: %s\n",
errstr)
```

```
                        errstr);
                exit(1);
        /* Add brokers */
        if (rd_kafka_brokers_add(rk, brokers) == 0) {
                fprintf(stderr, "%% No valid brokers specified\n");
                exit(1);
        if (mode == 'D') {
                int r;
                /* Describe groups */
                r = describe_groups(rk, group);
                rd_kafka_destroy(rk);
                exit(r == -1 ?  1 : 0);
        /* Redirect rd_kafka_poll() to consumer_poll() */
        rd_kafka_poll_set_consumer(rk);
        topics = rd_kafka_topic_partition_list_new(argc - optind);
        is_subscription = 1;
        for (i = optind ; i < argc ; i++) {
                /* Parse "topic[:part] */
                char *topic = argv[i];
                char *t;
                int32_t partition = -1;
                if ((t = strstr(topic, ":"))) {
                        *t = '\0';
                        partition = atoi(t+1);
                        is_subscription = 0; /* is assignment */
                        wait_eof++;
                rd_kafka_topic_partition_list_add(topics, topic, partition);
        if (mode == 'O') {
                /* Offset query */
                err = rd_kafka_committed(rk, topics, 5000);
                if (err) {
                        fprintf(stderr, "%% Failed to fetch offsets: %s\n",
                                rd_kafka_err2str(err));
                        exit(1);
                for (i = 0 ; i < topics->cnt ; i++) {
                        rd_kafka_topic_partition_t *p = &topics->elems[i];
                        printf("Topic \"%s\" partition %"PRId32,
p->topic,p->partition);
```

```
                               p>topic, p>partition);
                        if (p->err)
                                printf(" error %s",
                                       rd_kafka_err2str(p->err));
                        else {
                                printf(" offset %"PRId64"",
                                       p->offset);
                                if (p->metadata_size)
                                        printf(" (%d bytes of metadata)",
                                               (int)p->metadata_size);
                        printf("\n");
                goto done;
        if (is_subscription) {
                fprintf(stderr, "%% Subscribing to %d topics\n", topics->cnt);
                if ((err = rd_kafka_subscribe(rk, topics))) {
                        fprintf(stderr,
                                "%% Failed to start consuming topics: %s\n",
                                rd_kafka_err2str(err));
                        exit(1);
        } else {
                fprintf(stderr, "%% Assigning %d partitions\n", topics->cnt);
                if ((err = rd_kafka_assign(rk, topics))) {
                        fprintf(stderr,
                                "%% Failed to assign partitions: %s\n",
                                rd_kafka_err2str(err));
        while (run) {
                rd_kafka_message_t *rkmessage;
                rkmessage = rd_kafka_consumer_poll(rk, 1000);
                if (rkmessage) {
                        msg_consume(rkmessage);
                        rd_kafka_message_destroy(rkmessage);
done:
        err = rd_kafka_consumer_close(rk);
        if (err)
                fprintf(stderr, "%% Failed to close consumer: %s\n",
                        rd_kafka_err2str(err));
        else
                fprintf(stderr, "%% Consumer closed\n");
```

`p` `,`

```
        rd_kafka_topic_partition_list_destroy(topics);
        /* Destroy handle */
        rd_kafka_destroy(rk);
    /* Let background threads clean up and terminate cleanly. */
    run = 5;
    while (run-- > 0 && rd_kafka_wait_destroyed(1000) == -1)
        printf("Waiting for librdkafka to decommission\n");
    if (run <= 0)
        rd_kafka_dump(stdout, rk);
    return 0;
```

2. Run the following command to compile kafka_consumer.c:

```
gcc -lrdkafka ./kafka_consumer.c -o kafka_consumer
```

3. Run the following command to subscribe to messages:

```
./kafka_consumer -g <group> -b <bootstrap_servers> <topic>
```

| Parameter | Description |
|---|---|
| group | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |
| bootstrap servers _ | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
| topic | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |

### 2.4 SDK for Go

This topic describes how to use the SDK for Go to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

Go is installed. For more information, see All releases.

**Install the Go library**

1. Run the following commands to install the Go libraries:

```
i. go get github.com/Shopify/sarama/ ii. go get github.com/bsm/sarama-cluster
```

2. Run the following commands to compile the Go library:

```
i. go install services ii. go install services/producer iii. go install services/consumer
```

**Create configuration files**

1. Create a configuration file named kafka.json for ApsaraMQ for Kafka.
`{`

```json
  "topics": ["XXX"],
  "servers": ["XXX","XXX","XXX"],
  "consumerGroup": "XXX"
```

| Parameter | Description |
|---|---|
| topics | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
| servers | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
| consumerGroup | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |

2. Create a configurator named configs.go.

```java
package configs import (
    "encoding/json"
    "fmt"
```

```
    "io/ioutil"
    "os"
    "path/filepath"
```

`)`

```
var (
    configPath string
```

`)`

```
func init() {
    var err error
    workPath, err := os.Getwd()
    if err != nil {
        panic(err)
    configPath = filepath.Join(workPath, "conf")
// LoadJsonConfig is used to load a configuration file to config in JSON format. // config indicates a pointer to a struct. Otherwise, a panic exception is thrown. func LoadJsonConfig(config interface{}, filename string) {
    var err error
    var decoder *json.Decoder
    file := OpenFile(filename)
    defer file.Close()
    decoder = json.NewDecoder(file)
    if err = decoder.Decode(config); err != nil {
        msg := fmt.Sprintf("Decode json fail for config file at %s. Error: %v", filen
ame, err)
        panic(msg)
    json.Marshal(config)
func LoadJsonFile(filename string) (cfg string) {
    file := OpenFile(filename)
    defer file.Close()
    content, err := ioutil.ReadAll(file)
    if err != nil {
        msg := fmt.Sprintf("Read config to string error. file at %s. Error: %v", file
name, err)
        panic(msg)
    cfg = string(content)
    return cfg
```

```
func GetFullPath(filename string) string {
    return filepath.Join(configPath, filename)
func OpenFile(filename string) *os.File {
    fullPath := filepath.Join(configPath, filename)
    var file *os.File
    var err error
    if file, err = os.Open(fullPath); err != nil {
        msg := fmt.Sprintf("Can not load config at %s. Error: %v", fullPath, err)
        panic(msg)
    return file
```

3. Create a configurator named types.go.

```java
package configs type MqConfig struct {
    Topics     []string `json:"topics"`
    Servers    []string `json:"servers"`
    ConsumerId string   `json:"consumerGroup"`
```

**Send messages**

1. Create a producer program named producer.go.

```java
import (
    "fmt"
    "services"
    "time"
    "strconv"
    "github.com/Shopify/sarama"
```

`)`

```
var cfg *configs.MqConfig var producer sarama.SyncProducer func init() {
    fmt.Print("init kafka producer, it may take a few seconds to init the
connection\n")
    var err error
    cfg = &configs.MqConfig{}
    configs.LoadJsonConfig(cfg, "kafka.json")
```

```
    mqConfig := sarama.NewConfig()
    mqConfig.Producer.Return.Successes = true
    mqConfig.Version=sarama.V0_10_2_1
    if err = mqConfig.Validate(); err != nil {
        msg := fmt.Sprintf("Kafka producer config invalidate. config: %v. err: %v", *
cfg, err)
        fmt.Println(msg)
        panic(msg)
    producer, err = sarama.NewSyncProducer(cfg.Servers, mqConfig)
    if err != nil {
        msg := fmt.Sprintf("Kafak producer create fail. err: %v", err)
        fmt.Println(msg)
        panic(msg)
func produce(topic string, key string, content string) error {
    msg := &sarama.ProducerMessage{
        Topic: topic,
        Key:   sarama.StringEncoder(key),
        Value: sarama.StringEncoder(content),
        Timestamp: time.Now(),
    _, _, err := producer.SendMessage(msg)
    if err != nil {
        msg := fmt.Sprintf("Send Error topic: %v. key: %v. content: %v", topic, key,
content)
        fmt.Println(msg)
        return err
    fmt.Printf("Send OK topic:%s key:%s value:%s\n", topic, key, content)
    return nil
func main() {
    key := strconv.FormatInt(time.Now().UTC().UnixNano(), 10)
    value := "this is a kafka message!"
    produce(cfg.Topics[0], key, value)
```

2. Run the following command to send messages:

```
go run producer.go
```

**Subscribe to messages**

1. Create a consumer program named consumer.go.

```java
import (
    "fmt"
    "os"
    "services"
    "os/signal"
    "github.com/Shopify/sarama"
    "github.com/bsm/sarama-cluster"
```

`)`

```
var cfg *configs.MqConfig var consumer *cluster.Consumer var sig chan os.Signal func init() {
    fmt.Println("init kafka consumer, it may take a few seconds...")
    var err error
    cfg := &configs.MqConfig{}
    configs.LoadJsonConfig(cfg, "kafka.json")
    clusterCfg := cluster.NewConfig()
    clusterCfg.Consumer.Return.Errors = true
    clusterCfg.Consumer.Offsets.Initial = sarama.OffsetOldest
    clusterCfg.Group.Return.Notifications = true
    clusterCfg.Version = sarama.V0_10_2_1
    if err = clusterCfg.Validate(); err != nil {
        msg := fmt.Sprintf("Kafka consumer config invalidate. config: %v. err: %v", *
clusterCfg, err)
        fmt.Println(msg)
        panic(msg)
    consumer, err = cluster.NewConsumer(cfg.Servers, cfg.ConsumerId, cfg.Topics, clus
terCfg)
    if err != nil {
        msg := fmt.Sprintf("Create kafka consumer error: %v. config: %v", err, cluste
rCfg)
        fmt.Println(msg)
        panic(msg)
    sig = make(chan os.Signal, 1)
func Start() {
    go consume()
func consume() {
    for {
```

```
        select {
        case msg, more := <-consumer.Messages():
            if more {
                fmt.Printf("Partition:%d, Offset:%d, Key:%s, Value:%s Timestamp:%s\n",
msg.Partition, msg.Offset, string(msg.Key), string(msg.Value), msg.Timestamp)
                consumer.MarkOffset(msg, "")
        case err, more := <-consumer.Errors():
            if more {
                fmt.Println("Kafka consumer error: %v", err.Error())
        case ntf, more := <-consumer.Notifications():
            if more {
                fmt.Println("Kafka consumer rebalance: %v", ntf)
        case <-sig:
            fmt.Errorf("Stop consumer server...")
            consumer.Close()
            return
func Stop(s os.Signal) {
    fmt.Println("Recived kafka consumer stop signal...")
    sig <- s
    fmt.Println("kafka consumer stopped!!!")
func main() {
    signals := make(chan os.Signal, 1)
    signal.Notify(signals, os.Interrupt)
    Start()
    select {
    case s := <-signals:
        Stop(s)
```

2. Run the following command to subscribe to messages:

```
go run consumer.go
```

### 2.5 SDK for PHP

This topic describes how to use the SDK for PHP to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

GNU Compiler Collection (GCC) is installed. For more information, see Installing GCC. PHP is installed. For more information, see Downloads. PHP Extension Community Library (PECL) is installed. For more information, see Downloading PECL extensions.

**Install the C++ library**

1. Run the following command to switch to the /etc/yum.repos.d/ yum repository directory:

```
cd /etc/yum.repos.d/
```

2. Create a yum repository configuration file named confluent.repo.

```
[Confluent.dist] name=Confluent repository (dist) baseurl=https://packages.confluent.io/rpm/5.1/7 gpgcheck=1 gpgkey=https://packages.confluent.io/rpm/5.1/archive.key enabled=1 [Confluent] name=Confluent repository baseurl=https://packages.confluent.io/rpm/5.1 gpgcheck=1 gpgkey=https://packages.confluent.io/rpm/5.1/archive.key enabled=1
```

3. Run the following command to install the C++ library:

```bash
yum install librdkafka-devel
```

**Install the PHP library**

1. Run the following command to install the PHP library:

```
pecl install rdkafka
```

2. In the PHP initialization file php.ini, add the following line to enable Kafka extensions:

```
extension=rdkafka.so
```

**Create a configuration file**

Create a configuration file named setting.php.

```
<?php return [
    'bootstrap_servers' => "xxx:xx,xxx:xx",
    'topic_name' => 'xxx',
    'consumer_id' => 'xxx'
```

];

| Parameter | Description |
|---|---|

| bootstrap servers _ | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
|---|---|
| topic name _ | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
| consumer id _ | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |

**Send messages**

1. Create a producer program named kafka-producer.php.

```
<?php $setting = require __DIR__ . '/setting.php'; $conf = new RdKafka\Conf(); $conf->set('api.version.request', 'true'); $conf->set('message.send.max.retries', 5); $rk = new RdKafka\Producer($conf);
## If want to debug, set log level to LOG_DEBUG
$rk->setLogLevel(LOG_INFO); $rk->addBrokers($setting['bootstrap_servers']); $topic = $rk->newTopic($setting['topic_name']); $a = $topic->produce(RD_KAFKA_PARTITION_UA, 0, "Message hello kafka"); $rk->poll(0); while ($rk->getOutQLen() > 0) {
    $rk->poll(50);
echo "send succ" . PHP_EOL;
```

2. Run the following command to send messages:

```
php kafka-producer.php
```

**Subscribe to messages**

1. Create a consumer program named kafka-consumer.php.

```
<?php $setting = require __DIR__ . '/setting.php'; $conf = new RdKafka\Conf(); $conf->set('api.version.request', 'true'); $conf->set('group.id', $setting['consumer_id']); $conf->set('metadata.broker.list', $setting['bootstrap_servers']); $topicConf = new RdKafka\TopicConf(); $conf->setDefaultTopicConf($topicConf); $consumer = new RdKafka\KafkaConsumer($conf); $consumer->subscribe([$setting['topic_name']]); echo "Waiting for partition assignment... (make take some time when\n"; echo "quickly re-joining the group after leaving it.)\n"; while (true) {
    $message = $consumer->consume(30 * 1000);
    switch ($message->err) {
        case RD_KAFKA_RESP_ERR_NO_ERROR:
            var_dump($message);
            break;
        case RD_KAFKA_RESP_ERR__PARTITION_EOF:
            echo "No more messages; will wait for more\n";
            break;
        case RD_KAFKA_RESP_ERR__TIMED_OUT:
            echo "Timed out\n";
            break;
        default:
            throw new \Exception($message->errstr(), $message->err);
            break;
```

?>
2. Run the following command to subscribe to messages:

```
php kafka-consumer.php
```

### 2.6 SDK for Ruby

This topic describes how to use the SDK for Ruby to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

Ruby is installed. For more information, see Ruby.

**Install the Ruby library**

Run the following command to install the Ruby library:

```
gem install ruby-kafka -v 0.6.8
```

**Send messages**

1. Create a producer program named producer.rb.

```bash
# frozen_string_literal: true
$LOAD_PATH.unshift(File.expand_path("../../lib", __FILE__)) require "kafka" logger = Logger.new($stdout)
#logger.level = Logger::DEBUG
logger.level = Logger::INFO brokers = "xxx:xx,xxx:xx" topic = "xxx" kafka = Kafka.new(
        seed_brokers: brokers,
        client_id: "simple-producer",
        logger: logger,
```

`)`

```
producer = kafka.producer begin
    $stdin.each_with_index do |line, index|
    producer.produce(line, topic: topic)
    producer.deliver_messages
end ensure
    producer.deliver_messages
    producer.shutdown
end
```

| Parameter | Description |
|---|---|
| brokers | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |

| topic | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
|---|---|

2. Run the following command to send messages:

```
ruby producer.rb
```

**Subscribe to messages**

1. Create a consumer program named consumer.rb.

```bash
# frozen_string_literal: true
$LOAD_PATH.unshift(File.expand_path("../../lib", __FILE__)) require "kafka" logger = Logger.new(STDOUT)
#logger.level = Logger::DEBUG
logger.level = Logger::INFO brokers = "XXX:XX,XXX:XX" topic = "XXX" consumerGroup = "XXX" kafka = Kafka.new(
        seed_brokers: brokers,
        client_id: "test",
        socket_timeout: 20,
        logger: logger,
```

`)`

```
consumer = kafka.consumer(group_id: consumerGroup) consumer.subscribe(topic, start_from_beginning: false) trap("TERM") { consumer.stop } trap("INT") { consumer.stop } begin
    consumer.each_message(max_bytes: 64 * 1024) do |message|
    logger.info("Get message: #{message.value}")
    end
rescue Kafka::ProcessingError => e
    warn "Got error: #{e.cause}"
    consumer.pause(e.topic, e.partition, timeout: 20)
    retry
end
```

| Parameter | Description |
|---|---|

| brokers | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
|---|---|
| topic | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
| consumerGroup | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |

2. Run the following command to subscribe to messages:

```
ruby consumer.rb
```

### 2.7 SDK for Node.js

This topic describes how to use the SDK for Node.js to connect to ApsaraMQ for Kafka to send and receive messages.

**Prerequisites**

GNU Compiler Collection (GCC) is installed. For more information, see Installing GCC. Node.js is installed. For more information, see Downloads.

> **Important:** The version of Node.js must be 4.0.0 or later.

OpenSSL is installed. For more information, see Downloads.

**Install the Node.js library**

1. Run the following command to specify the path of the OpenSSL header file for the
preprocessor:

```bash
# Set this parameter to the path of the OpenSSL header file that is installed on your
on-premises machine. export CPPFLAGS=-I</usr/local/opt/openssl/include>
```

2. Run the following command to specify the path of the OpenSSL library for the connector:

```bash
# Set this parameter to the path of the OpenSSL library file that is installed on you
r on-premises machine. export LDFLAGS=-L</usr/local/opt/openssl/lib>
```

3. Run the following command to install the Node.js library:

```
npm install i --unsafe-perm node-rdkafka
```

> **Note:** Run the **whereis openssl** command to obtain the path of the OpenSSL header file and the path of the OpenSSL library.

**Create a configuration file**

Create a configuration file named setting.js for ApsaraMQ for Kafka.

```json
module.exports = {
    'bootstrap_servers': ["kafka-ons-internet.aliyun.com:8080"],
    'topic_name': 'xxx',
    'consumer_id': 'xxx'
```

| Parameter | Description |
|---|---|
| bootstrap servers _ | The endpoint that is used to access the instance. You can obtain the endpoint on the Instance Details page of the corresponding ApsaraMQ for Kafka instance in the ApsaraMQ for Kafka console. |
| topic name _ | The topic name. You must create a topic before you send and receive messages. You can create topics on the Topics page in the ApsaraMQ for Kafka console. |
| consumer id _ | The name of the consumer group. You do not need to create a consumer group before you send and receive messages. ApsaraMQ for Kafka automatically creates a consumer group based on your configurations. You can view the automatically created consumer group on the Consumer Groups page in the ApsaraMQ for Kafka console. |

**Send messages**

1. Create a producer program named producer.js that contains the following code:

```
const Kafka = require('node-rdkafka');
```

`t` `fi` `i`

```
('/ tti
```

`')`

```json
const config = require('./setting'); console.log("features:" + Kafka.features); console.log(Kafka.librdkafkaVersion); var producer = new Kafka.Producer({
    /*'debug': 'all', */
    'api.version.request': 'true',
    'bootstrap.servers': config['bootstrap_servers'],
    'dr_cb': true,
    'dr_msg_cb': true
}); var connected = false producer.setPollInterval(100); producer.connect(); producer.on('ready', function() {
  connected = true
  console.log("connect ok")
}); producer.on("disconnected", function() {
  connected = false;
  producer.connect();
```

`})`

```
producer.on('event.log', function(event) {
      console.log("event.log", event);
}); producer.on("error", function(error) {
    console.log("error:" + error);
}); function produce() {
  try {
    producer.produce(
      config['topic_name'],
      null,
      new Buffer('Hello Ali Kafka'),
      null,
      Date.now()
```

);

```
  } catch (err) {
    console.error('A problem occurred when sending our message');
    console.error(err);
producer.on('delivery-report', function(err, report) { consolelog("delivery-report:producerok");
```

```
    console.log(deliveryreport: producer ok);
}); producer.on('event.error', function(err) {
    console.error('event.error:' + err);
```

`})`

```
setInterval(produce,1000,"Interval");
```

2. Run the following command to send messages:

```
node producer.js
```

**Subscribe to messages**

1. Create a consumption program named consumer.js.

```
const Kafka = require('node-rdkafka'); const config = require('./setting'); console.log(Kafka.features); console.log(Kafka.librdkafkaVersion); console.log(config) var consumer = new Kafka.KafkaConsumer({
    /*'debug': 'all',*/
    'api.version.request': 'true',
    'bootstrap.servers': config['bootstrap_servers'],
    'group.id' : config['consumer_id']
}); consumer.connect(); consumer.on('ready', function() {
  console.log("connect ok");
  consumer.subscribe([config['topic_name']]);
  consumer.consume();
```

`})`

```
consumer.on('data', function(data) {
  console.log(data);
}); consumer.on('event.log', function(event) {
      console.log("event.log", event);
}); consumer.on('error', function(error) {
    console.log("error:" + error);
}); consumer.on('event', function(event) {
        console.log("event:" + event);
});
```

2. Run the following command to subscribe to messages:

```
node consumer.js
```

## 3 API reference

### 3.1 Common request parameters

A client calls ApsaraMQ for Kafka API operations based on HTTPS. Common request parameters must be included in all API requests and sent to the backend service of ApsaraMQ for Kafka for permission verification. The following table describes common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| requestId | String | No | The request ID. We recommend that you save the request ID for log tracking. |
| userId _ | Long | No | The username. |
| callerType _ | String | No | The user type. Valid values: partner: an account in an account group customer: an Alibaba Cloud account sub: a Resource Access Management (RAM) user AssumedRoleUser: a user that uses a temporary Security Token Service (STS) token. |
| parentId _ | Long | No | If you set callerType to sub, specify the ID of the Alibaba Cloud account for this parameter. If you set callerType to other values, leave this parameter empty. When you access resources by using an STS token, this parameter is not passed. |
| AccessKeyId | String | No | The AccessKey ID of the user. |

| SecurityToken | String | No | The security token. The value of this parameter is the caller ID and all the preceding IDs. |
|---|---|---|---|
| stsTokenCallerUid | Long | No | The ID of the Alibaba Cloud account that owns the token when you access resources by using an STS token. |
| stsTokenCallerBid | Long | No | The ID of the account group to which the caller belongs when you access resources by using an STS token. |
| stsTokenUserId | Long | No | The user ID when you access resources by using an STS token of the ImpersonatedUser type. |
| regionId _ | String | Yes | The region ID. |
| IspSignature | String | No | The signature string of the current request. For more information, see Use gateway signature to access API operations. |
| IspSignatureSecretKey | String | No | The AccessKey secret used for the signature. For more information, see Use gateway signature to access API operations. |

### 3.2 Common response parameters

A client sends an HTTP request to the backend service of ApsaraMQ for Kafka. The backend service processes the request and then returns results in an HTTP response to the client in the same way. In normal cases, the HTTP status code is 200 in the response. The returned content is contained in the body as a JSON string. The client needs to parse the JSON string to determine whether the call is successful. JSON format: `{`

```json
    "code": 200,
    "message": "operation success",
    "requestId": "",
    "success": true,
```

Valid values: code: the HTTP status code. A value of 200 indicates that the request was successful. Other values indicate that the request failed. message: the processing result. success: indicates whether the request was successful. RequestId: the request ID. The value is a string.

### 3.3 Use the domain name to access API operations

**access API operations**

You can access API operations by using the domain name of ApsaraMQ for Kafka.

**Obtain the domain name**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the following command to obtain the domain name of ApsaraMQ for Kafka on OPS:

```bash
$ kubectl get ingress | grep kafka
```

Sample output: The complete API URL is in the `http://<Domain name of ApsaraMQ for Kafka>/pop/<API` `operation>` format. The value of API operation varies based on operations. For example, the complete API URL for the ApplyVipInfo operation is `http://<Domain name of ApsaraMQ for` `Kafka>/pop/kafkaInstance/applyVipInfo` . For more information, see the documentation of the corresponding API operation.

### 3.4 Use the gateway signature to access API operations

**access API operations**

To allow clients to use the gateway signature to access API operations, the service provider must add the IspSignatureSecretKey and IspSignature parameters in API operations. The system verifies whether data is correctly transmitted based on the received values of the IspSignatureSecretKey and IspSignature parameters.

**RPC**

The IspSignatureSecretKey parameter specifies the AccessKey secret of the signature. If you enter multiple key pairs in POP, hot replacement and signed keys are supported. This way, the backend can determine which key is used. The IspSignature parameter specifies the signing result. The value of the name parameter is the name of the parameter that is mapped to the backend. You can specify a custom value for the name parameter. The following items describe how to add parameters to an API operation. XML

```
<Parameter type="String" tagPosition="System" name="secretKey" required="false" tagNa me="IspSignatureSecretKey"/> <Parameter type="String" tagPosition="System" name="signature" required="false" tagNa me="IspSignature"/>
```

**ROA**

| nd | x-acs-sign | parameters in the |
|---|---|---|
| request.getHeader("x-acs-sign") |   |   |

Read the `x-acs-isp-signature-secret-key` and `x-acs-sign` parameters in the request header. For example, in Java, you can run the `request.getHeader("x-acs-sign")` command to read the x-acs-sign parameter. To verify the signature, you need only to compare whether the signature of the gateway is the same as the signature calculated by HTTP.

### 3.5 Instance management

#### 3.5.1 CreateInstance

Creates an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/create
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceType | String | No | The instance type. Valid values: Single-zone instance Dual-zone instance Three-zone instance |
| zoneId | String | Yes | The zone ID. |
| zoneB | String | No | Zone B. This parameter is required only if you specify Dual-zone instance or Three-zone instance as the instance type. |

| zoneC | String | No | Zone C. This parameter is required only if you specify Three-zone instance as the instance type. |
|---|---|---|---|
| instanceName | String | Yes | The instance name. |
| namespace | String | No | The namespace to which the instance belongs. Default value: default. |
| replicas | String | No | The number of broker nodes on the instance. |
| spec | String | No | The instance specification. Valid values: broker4c16g broker8c32g broker16c64g broker32c128g |
| cpuType | String | No | The CPU type of the node on which the broker is deployed. |
| vpcId | String | No | The ID of the virtual private cloud (VPC) to which the instance belongs. This parameter is required only if you set vipType to SingleTunnel. |
| vSwitchId | String | No | The ID of the vSwitch with which the instance is associated. This parameter is required only if you set vipType to SingleTunnel. |

| vipType | String | Yes | The type of the virtual IP address (VIP). Valid values: SingleTunnel AnyTunnel |
|---|---|---|---|
| uid | String | No | The user ID. |
| vipAction | String | No | The operation to be performed. Valid values: create delete |
| endpointTypes | String | Yes | The endpoint type. Valid values: PLAINTEXT SASL |
| department | String | Yes | The organization to which the instance belongs in the Apsara Uni-manager Management Console. |
| resourceGroup | String | Yes | The resource set to which the instance belongs in the Apsara Uni-manager Management Console. |
| tags | String | Yes | The tags that are added to the instance in STS mode. |
| scope | String | No | The scope to which the tags added to the instance belongs in STS mode. |
| tagOwnerUid | Long | Yes | The tag owner. |

For information about common response parameters, see Common response parameters.

| 2 |   | > Document Version: 2024111 |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| instanceId | String | The ID of the instance that is created. |

#### 3.5.2 CreateDisasterRecoveryInstance

Creates a zone-disaster recovery instance.

| http://<Domain name of ApsaraMQ for |   |
|---|---|

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| name | String | No | The name of the zone- disaster recovery instance. |
| targetInstanceId | String | No | The ID of the destination ApsaraMQ for Kafka instance. |
| instanceId1 | String | No | The ID of ApsaraMQ for Kafka Instance 1. |
| replicatorId1 | String | No | The ID of ApsaraMQ for Kafka Replicator 1. |
| instanceId2 | String | No | The ID of ApsaraMQ for Kafka Instance 2. |
| replicatorId2 | String | No | The ID of ApsaraMQ for Kafka Replicator 2. |
| autoOffsetReset | String | No | The offset to start data synchronization. Valid values: Earliest offset Latest offset |

| dateTimeOfOffset | String | No | The point in time if you specify a time point as the offset to start data synchronization. |
|---|---|---|---|
| quota | String | No | The throttling limit. Unit: MB/s. |

For information about the response parameters, see Common response parameters.

#### 3.5.3 DeleteDisasterRecoveryInstance

Deletes a zone-disaster recovery instance.

| http://<Domain name of ApsaraMQ for |   |
|---|---|

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| sourceInstanceId | String | Yes | The ID of the source ApsaraMQ for Kafka instance. |

For information about the response parameters, see Common response parameters.

#### 3.5.4 CreateInstanceRelation

Creates instance relationships.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/relation/create
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |

| ownerId | String | Yes | The owner ID of the instance. |
|---|---|---|---|
| department | String | Yes | The organization ID of the instance. |
| resourceGroup | String | Yes | The resource group ID of the instance. |
| departmentName | String | No | The owner name of the instance. |
| resourceGroupName | String | No | The organization name of the instance. |
| tags | String | Yes | The tags that are added to the instance in STS mode. |
| scope | String | No | The scope to which the tags added to the instance belongs in STS mode. |
| tagOwnerUid | Long | Yes | The owner ID of the tags added to the instance. |

For information about the response parameters, see Common response parameters.

#### 3.5.5 GetInstanceConfig

Queries the configurations of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/getInstanceConfig
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.5.6 GetInstanceIdList

Queries the list of instance IDs.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/listAllInstanceIds
```

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.5.7 DeleteInstance

Deletes an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/delete
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| namespace | String | Yes | The namespace to which the instance belongs. Default value: default. |

For information about the response parameters, see Common response parameters.

#### 3.5.8 GetDisasterRecoveryInstanceList

Queries the list of disaster recovery instances.

```
 http://<Domain name of ApsaraMQ for
Kafka>/pop/kafkaDisasterRecoveryInstance/listKafkaDisasterRecoveryInstances
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| kafkaInstance | String | Yes | The ApsaraMQ for Kafka instance. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.5.9 GetInstanceList

Queries the list of instances.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/list
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| orderId | String | No | The order ID. |
| instanceId | String | No | The instance ID. If you configure this parameter, only the information about the specified instance is returned. |

| instanceIds | String | No | The instance IDs. If you configure this parameter, only the information about the specified instances is returned. |
|---|---|---|---|
| tags | String | No | The tags. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| InstanceList | String | The instances. |

#### 3.5.10 GetInstanceRelationList

Queries the relationships of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/relation/list
```

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.5.11 GetInstanceStatus

Queries the status of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/status
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The instance ID. |
|---|---|---|---|
| namespace | String | No | The namespace to which the instance belongs. Default value: default. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| InstanceStatus | String | The instance status. |

#### 3.5.12 GetKafkaInstanceList

Queries the list of ApsaraMQ for Kafka instances.

| http://<Domain name of ApsaraMQ for |   |
|---|---|

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.5.13 ScaleInstance

Scales out an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/scale
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The instance ID. |
|---|---|---|---|
| namespace | String | No | Default value: default. You cannot specify a custom value. |
| replicas | String | No | The number of nodes after you scale out the instance. |

For information about the response parameters, see Common response parameters.

#### 3.5.14 HotSwitchDisasterRecoveryInstance

Performs hot switchover for a disaster recovery instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaDisasterRecoveryInstance/hotSwitch
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| expectedSourceInstan ceId | String | Yes | The ID of the source instance of the disaster recovery cluster for which you want to perform hot switchover. |

For information about the response parameters, see Common response parameters.

#### 3.5.15 UpdateInstanceConfig

Updates the configurations of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/updateConfig
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The instance ID. |
|---|---|---|---|
| config | String | Yes | The name of the configuration item. |
| value | String | No | The value of the configuration item. |

For information about the response parameters, see Common response parameters.

#### 3.5.16 UpdateInstanceName

Updates the name of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/updateInstanceName
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| instanceName | String | Yes | The instance name. |

For information about the response parameters, see Common response parameters.

#### 3.5.17 GetZoneList

Queries the most recent list of zones.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/region/listZones
```

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

### 3.6 Topic management

#### 3.6.1 CreateTopic

Creates a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/create
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The name of the topic that you want to create. |
| compactTopic | Boolean | No | Specifies whether the topic is a compact topic. |
| partitionNum | String | No | The number of partitions in the topic. |
| replicationFactor | String | No | The number of replicas of the topic. |
| minInsyncReplicas | String | No | The minimum number of synchronized replicas. |
| retentionHours | String | No | The retention period of data in the topic. |

For information about the response parameters, see Common response parameters.

#### 3.6.2 GetTopicList

Queries the list of topics on an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/listInPage
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| currentPage | String | No | The page number. |
| pageSize | String | No | The number of entries per page. |
| search | String | No | The keyword that you specify for fuzzy search when you query the topics. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| total | Int | The number of consumers. |
| pageSize | Int | The number of entries per page. |
| currentPage | Int | The page number. |
| data | String | The response data. |

#### 3.6.3 GetTopicListAll

Queries the list of topics on an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/listAllTopic
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| currentPage | String | No | The page number. |
| pageSize | String | No | The number of entries per page. |
| topic | String | No | The topic name. |
| search | String | No | The keyword that you specify for fuzzy search when you query the topics. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| total | Int | The number of consumers. |
| pageSize | Int | The number of entries per page. |
| currentPage | Int | The page number. |
| data | String | The response data. |

#### 3.6.4 DeleteTopic

Deletes a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/delete
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The instance name. |
|---|---|---|---|
| topic | String | Yes | The topic name. |

For information about the response parameters, see Common response parameters.

#### 3.6.5 GetTopicConfigList

Queries the configurations of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/listTopicConfig
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | No | The topic name. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.6.6 GetTopicListByConsumerId

Queries the list of topics subscribed by a consumer.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/subscription/listTopicsByConsumerId
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | Yes | The instance ID. |
|---|---|---|---|
| consumerId | String | Yes | The consumer ID. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.6.7 GetTopicQuotaTip

Queries the partition quota of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/quataTipOfTopic
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.6.8 GetTopicStatus

Queries the status of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/status
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | No | The topic on the instance. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.6.9 GetTopicSubscribeStatus

Queries the subscription status of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/topicSubscribeStatus
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | No | The topic name. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.6.10 UpdateTopicConfig

Updates the configurations of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/updateTopicConfig
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The topic name. |
| config | String | Yes | The name of the configuration item. |
| value | String | Yes | The value of the configuration item. |

For information about the response parameters, see Common response parameters.

#### 3.6.11 RebalanceTopic

Rebalances topics.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/rebalance
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topics | String | No | The topics that you want to rebalance. If you do not configure this parameter, all topics in the cluster are selected. |

| destBrokerIds | String | No | The IDs of the brokers to which you want to rebalance the topics. If you do not configure this parameter, all online brokers are selected. |
|---|---|---|---|
| interBrokerThrottle | Long | No | The throttling threshold when topics are replicated between brokers. If you do not configure this parameter, no throttling limit is imposed. |
| logDirThrottle | Long | No | The rate at which logs are written to shards in a specific directory. If you do not configure this parameter, no limit is imposed. |
| additional | Boolean | No | Specifies whether to overwrite the previous rebalance. |

For information about the response parameters, see Common response parameters.

#### 3.6.12 ModifyPartitionNum

Changes the number of partitions in a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/addPartition
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The topic name. |

| partitionNum | Int | Yes | The final number of partitions in the topic. |
|---|---|---|---|

For information about the response parameters, see Common response parameters.

### 3.7 Group management

#### 3.7.1 GetConsumerList

Queries the list of consumers of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/subscription/listInPage
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| currentPage | String | No | The page number. |
| pageSize | String | No | The number of entries per page. |
| search | String | No | The keyword that you specify for fuzzy search when you query the consumers. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| total | Int | The number of consumers. |
| pageSize | Int | The number of entries per page. |

| currentPage | Int | The page number. |
|---|---|---|
| data | String | The response data. |

#### 3.7.2 GetConsumerProgress

Queries the consumer progress in a consumer group.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/subscription/progress2
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| consumerId | String | Yes | The name of the consumer group. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.7.3 GetConsumerProgressByTopic

Queries the consumer progress of a topic.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/topic/consumerProgressOneTopic
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |

| consumerId | String | Yes | The consumer ID. |
|---|---|---|---|
| topic | String | Yes | The topic name. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.7.4 GetConsumerTimespan

Queries the time range in which consumption can be reset in a consumer group.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/subscription/timespan
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| consumerId | String | Yes | The name of the consumer group. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

### 3.8 Message management

#### 3.8.1 QueryMessage

Queries a message.

**U**

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaMessage/queryMessage
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The topic name. |
| queryType | String | No | The query type. Valid values: byOffset: queries the message by offset. byTimeStamp: queries the message by timestamp. |
| partition | String | No | The partition in the topic from which the message was sent. This parameter is required only if you set queryType to byOffset. |
| timestampStr | String | No | The timestamp that indicates when the message was sent. This parameter is required only if you set queryType to byTimestamp. |
| offset | String | No | The message offset. This parameter is required only if you set queryType to byOffset. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|

| data | String | The response data. |
|---|---|---|

#### 3.8.2 DownloadMessage

Downloads a message.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaMessage/downloadMessage
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The topic name. |
| queryType | String | No | The query type of the message. key: queries the message by key. byOffset: queries the message by offset. |
| partition | String | No | The partition from which the message was sent. |
| offset | String | No | The message offset. |

For information about the response parameters, see Common response parameters.

#### 3.8.3 SendMessage

Sends a test message.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaMessage/sendMessage
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| topic | String | Yes | The topic name. |
| partition | String | No | The partition in the topic. If you do not configure this parameter, the system randomly selects a partition. |
| key | String | Yes | The message key. |
| value | String | Yes | The message value. |

For information about the response parameters, see Common response parameters.

#### 3.8.4 ResetOffset

Resets a consumer offset.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/subscription/resetOffset
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| consumerId | String | Yes | The consumer ID. |
| topic | String | Yes | The topic name. |
| timeStampStr | String | Yes | The timestamp that specifies the point in time to which you want to reset the consumer offset. Unit: milliseconds. |

For information about the response parameters, see Common response parameters.

### 3.9 Resource management

#### 3.9.1 DescribeCpuTypes

Queries the CPU types of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/getCpuTypesByZone
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| zoneId | String | No | The zone ID. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.9.2 GetPaasResource

Queries the physical resources that are exclusively used by an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/paasResource
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| labels | String | No | The labels of the node on which you want to query the physical resources. By default, this parameter is left empty. |

| taints | String | No | The taints of the node on which you want to query the physical resources. By default, this parameter is left empty. |
|---|---|---|---|

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.9.3 GetReplicatorList

Queries the list of replicators on a disaster recovery instance.

| http://<Domain name of ApsaraMQ for |   |
|---|---|

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.9.4 GetMetaData

Queries the frontend configurations of an instance.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/meta/data
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|

| instanceId | String | No | The instance ID. |
|---|---|---|---|

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.9.5 GetRegionList

Queries the most recent list of regions.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/region/list
```

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.9.6 GetUnscheduledTaskList

Queries the list of unscheduled tasks.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaScheduledTask/listUnscheduledTasks
```

For information about the request parameters, see Common request parameters. For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

### 3.10 ACLs

#### 3.10.1 CreateACL

Creates an access control list (ACL).

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/createAcl
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | No | The username. |
| aclResourceType | String | No | The type of the resource with which the ACL is associated. |
| aclResourceName | String | No | The name of the resource with which the ACL is associated. |
| aclResourcePatternTyp e | String | No | The mode in which the resource with which the ACL is associated is matched. |
| aclOperationType | String | No | The type of operation that is allowed by the ACL. |

For information about the response parameters, see Common response parameters.

#### 3.10.2 DeleteAcl

Deletes an access control list (ACL).

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/deleteAcl
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | Yes | The username. |
| aclResourceType | String | No | The type of the resource with which the ACL is associated. |
| aclResourceName | Boolean | No | The name of the resource with which the ACL is associated. |
| aclResourcePatternTyp e | String | No | The mode in which the resource with which the ACL is associated is matched. |
| aclOperationType | String | No | The type of operation that is allowed by the ACL. |

For information about the response parameters, see Common response parameters.

#### 3.10.3 CreateSaslUser

Creates a Simple Authentication and Security Layer (SASL) user.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/addSaslUser
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | Yes | The username of the SASL user. |

| password | String | Yes | The password of the SASL user. |
|---|---|---|---|
| type | String | No | The type of the SASL user. Only SASL users of the SCRAM type are supported. |

For information about the response parameters, see Common response parameters.

#### 3.10.4 DeleteSaslUser

Deletes a Simple Authentication and Security Layer (SASL) user.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/deleteSaslUser
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | Yes | The username. |
| type | String | No | The type of the SASL user. Only SASL users of the SCRAM type are supported. |

For information about the response parameters, see Common response parameters.

#### 3.10.5 DescribeAcls

Queries access control lists (ACLs).

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/describeAcls
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | No | The username. |
| aclResourceType | String | No | The type of the resource with which the ACL is associated. |
| aclResourceName | Boolean | No | The name of the resource with which the ACL is associated. |
| aclResourcePatternTyp e | String | No | The mode in which the resource with which the ACL is associated is matched. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

#### 3.10.6 DescribeSaslUsers

Queries Simple Authentication and Security Layer (SASL) users.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/describeSaslUsers
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |

For information about the response parameters, see Common response parameters.

#### 3.10.7 QueryExistedAclResource

Query existing resources associated with an access control list (ACL).

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaAcl/queryExistedAclResource
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| username | String | No | The username. |
| aclResourceType | String | No | The type of the resource with which the ACL is associated. |
| aclResourceName | String | No | The name of the resource with which the ACL is associated. |
| aclResourcePatternTyp e | String | No | The mode in which the resource with which the ACL is associated is matched. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |

### 3.11 VIPs

#### 3.11.1 ApplyVipInfo

Creates or deletes a virtual IP address (VIP).

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaInstance/applyVipInfo
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| instanceId | String | Yes | The instance ID. |
| vpcId | String | No | The ID of the virtual private cloud (VPC) to which the instance belongs. This parameter is required only if you set vipType to SingleTunnel. |
| vSwitchId | String | No | The ID of the vSwitch with which the instance is associated. This parameter is required only if you set vipType to SingleTunnel. |
| vipType | String | Yes | The VIP type. Valid values: SingleTunnel AnyTunnel |
| uid | String | No | The user ID. |
| vipAction | String | No | The operation to be performed. Valid values: create delete |
| endpointTypes | String | Yes | The endpoint type. Valid values: PLAINTEXT SASL |

For information about the response parameters, see Common response parameters.

### 3.12 Tags

#### 3.12.1 GetKafkaTagList

Queries the list of tags.

```
 http://<Domain name of ApsaraMQ for Kafka>/pop/kafkaTags/listTags
```

For information about common request parameters, see Common request parameters.

| Parameter | Type | Required | Description |
|---|---|---|---|
| pageStart | String | No | The page number. |
| pageSize | String | No | The number of entries per page. |

For information about common response parameters, see Common response parameters.

| Parameter | Type | Description |
|---|---|---|
| data | String | The response data. |
